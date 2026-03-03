# Chapter: Performance and Load Testing

## Introduction to Performance Testing

Performance testing is the discipline of evaluating how a system behaves under various conditions of load, stress, and resource contention. It answers fundamental questions that functional testing cannot: How fast does the application respond? How many concurrent users can it handle? What happens when traffic spikes unexpectedly? Where are the bottlenecks? Will the system degrade gracefully or crash catastrophically?

Performance issues are among the most expensive defects to fix in production. A slow page load increases bounce rates, reduces conversion, and damages brand reputation. Amazon famously reported that every 100ms of latency cost them 1% in sales. Google found that a half-second delay in search page generation caused a 20% drop in traffic. These numbers underscore why performance testing is not optional — it is a business imperative.

Performance testing encompasses several distinct disciplines, each targeting different system characteristics:

- **Load testing** evaluates system behavior under expected normal and peak load conditions
- **Stress testing** pushes the system beyond its capacity to identify breaking points
- **Soak testing** (endurance testing) runs the system under sustained load for extended periods to identify memory leaks, resource exhaustion, and degradation
- **Spike testing** subjects the system to sudden, dramatic increases in load
- **Scalability testing** determines how well the system scales when resources are added
- **Volume testing** evaluates system performance with large amounts of data
- **Configuration testing** compares performance across different configurations

This chapter covers the full spectrum of performance testing, from methodology and tool selection to execution, analysis, and integration with development workflows. We examine industry-leading tools including k6, Locust, JMeter, and Gatling, and provide practical guidance on performance budgets, bottleneck identification, and real user monitoring.

---

## Performance Testing Methodology

### Defining Performance Requirements

Before writing a single test, you must define what "good performance" means for your application. Vague goals like "the app should be fast" are useless. Performance requirements must be specific, measurable, and tied to business objectives.

**Response time requirements** specify acceptable latency for different operations:

```
# Performance SLAs (Service Level Agreements)
Page Load:
  - Homepage: p50 < 1s, p95 < 2s, p99 < 3s
  - Product listing: p50 < 1.5s, p95 < 3s, p99 < 5s
  - Product detail: p50 < 800ms, p95 < 1.5s, p99 < 2.5s
  - Checkout: p50 < 2s, p95 < 4s, p99 < 6s

API Endpoints:
  - GET /api/users/:id: p50 < 50ms, p95 < 150ms, p99 < 300ms
  - GET /api/products (list): p50 < 100ms, p95 < 300ms, p99 < 500ms
  - POST /api/orders: p50 < 200ms, p95 < 500ms, p99 < 1000ms
  - Search: p50 < 200ms, p95 < 500ms, p99 < 1500ms

Database Queries:
  - Simple reads: < 10ms
  - Complex joins: < 100ms
  - Aggregation queries: < 500ms
  - Report generation: < 5s
```

**Throughput requirements** define how many operations the system must handle:

```
# Throughput Targets
Normal Load:
  - 500 concurrent users
  - 100 requests/second
  - 50,000 page views/hour

Peak Load (Black Friday / sales events):
  - 5,000 concurrent users
  - 1,000 requests/second
  - 500,000 page views/hour

Background Processing:
  - Email queue: 10,000 emails/hour
  - Order processing: 500 orders/minute
  - Report generation: 100 reports/hour
```

**Resource utilization thresholds** define acceptable infrastructure consumption:

```
# Resource Limits
CPU: < 70% average, < 90% peak
Memory: < 80% utilization
Disk I/O: < 70% capacity
Network: < 60% bandwidth
Database connections: < 80% pool size
Error rate: < 0.1% under normal load, < 1% under peak load
```

### Creating a Performance Test Plan

A comprehensive performance test plan documents the testing approach, scope, and success criteria:

```markdown
# Performance Test Plan — E-Commerce Platform v3.2

## 1. Objectives
- Validate the system handles 500 concurrent users with response times under SLA
- Identify the maximum throughput before degradation exceeds acceptable thresholds
- Verify system stability under sustained load for 8 hours
- Identify bottlenecks in the checkout flow
- Validate auto-scaling triggers at appropriate thresholds

## 2. Scope
### In Scope
- Web application (homepage, product catalog, search, cart, checkout)
- REST API (all CRUD endpoints)
- Payment processing integration
- Database performance
- CDN performance

### Out of Scope
- Admin panel (low traffic, tested separately)
- Batch processing jobs
- Third-party API performance (mocked)

## 3. Test Environment
- Production-equivalent infrastructure (same instance types, same database tier)
- Database seeded with production-like data volume (10M users, 1M products, 50M orders)
- Third-party services mocked or stubbed
- Network conditions: LAN (from load generators to target)

## 4. Workload Model
### User Journey Mix
| Journey          | Percentage | Steps                                        |
|-----------------|------------|----------------------------------------------|
| Browse Only     | 40%        | Home → Category → Product → Product          |
| Search & Browse | 25%        | Home → Search → Product → Product            |
| Add to Cart     | 20%        | Home → Product → Add to Cart → Continue      |
| Purchase        | 10%        | Home → Product → Cart → Checkout → Confirm   |
| Account Mgmt   | 5%         | Login → Profile → Orders → Order Detail      |

### Think Times
- Between page views: 3-10 seconds (random)
- Form filling: 15-30 seconds (random)
- Reading content: 5-20 seconds (random)

## 5. Test Scenarios
1. Baseline test: 50 users, 30 minutes
2. Load test: Ramp to 500 users over 10 min, hold 60 min
3. Peak test: Ramp to 2000 users over 15 min, hold 30 min
4. Stress test: Ramp to failure (increment 500 users every 10 min)
5. Soak test: 500 users sustained for 8 hours
6. Spike test: 100 → 3000 → 100 users in 5 minutes

## 6. Success Criteria
- All response time SLAs met under load test scenario
- Error rate < 0.1% under normal load
- Error rate < 1% under peak load
- No memory leaks detected during soak test
- System recovers within 5 minutes after stress test
- Auto-scaling triggers within 2 minutes of threshold breach

## 7. Monitoring
- Application metrics: Datadog APM
- Infrastructure: CloudWatch / Grafana
- Database: pg_stat_statements, slow query log
- Custom dashboards for test execution
```

### Workload Modeling

Realistic workload models are essential for meaningful performance tests. They should reflect actual user behavior patterns:

```javascript
// k6 workload model
import http from 'k6/http';
import { sleep, group, check } from 'k6';
import { randomIntBetween } from 'https://jslib.k6.io/k6-utils/1.2.0/index.js';

const BASE_URL = __ENV.BASE_URL || 'https://staging.example.com';

// Weighted scenario selection
const scenarios = [
  { name: 'browse', weight: 40, fn: browseScenario },
  { name: 'search', weight: 25, fn: searchScenario },
  { name: 'addToCart', weight: 20, fn: addToCartScenario },
  { name: 'purchase', weight: 10, fn: purchaseScenario },
  { name: 'account', weight: 5, fn: accountScenario },
];

export const options = {
  scenarios: {
    browse_users: {
      executor: 'ramping-vus',
      startVUs: 0,
      stages: [
        { duration: '5m', target: 200 },
        { duration: '30m', target: 200 },
        { duration: '5m', target: 0 },
      ],
      exec: 'browseScenario',
    },
    search_users: {
      executor: 'ramping-vus',
      startVUs: 0,
      stages: [
        { duration: '5m', target: 125 },
        { duration: '30m', target: 125 },
        { duration: '5m', target: 0 },
      ],
      exec: 'searchScenario',
    },
    shopping_users: {
      executor: 'ramping-vus',
      startVUs: 0,
      stages: [
        { duration: '5m', target: 100 },
        { duration: '30m', target: 100 },
        { duration: '5m', target: 0 },
      ],
      exec: 'addToCartScenario',
    },
    purchasing_users: {
      executor: 'ramping-vus',
      startVUs: 0,
      stages: [
        { duration: '5m', target: 50 },
        { duration: '30m', target: 50 },
        { duration: '5m', target: 0 },
      ],
      exec: 'purchaseScenario',
    },
    account_users: {
      executor: 'ramping-vus',
      startVUs: 0,
      stages: [
        { duration: '5m', target: 25 },
        { duration: '30m', target: 25 },
        { duration: '5m', target: 0 },
      ],
      exec: 'accountScenario',
    },
  },
  thresholds: {
    http_req_duration: ['p(95)<3000'],
    http_req_failed: ['rate<0.01'],
    'http_req_duration{scenario:browse_users}': ['p(95)<2000'],
    'http_req_duration{scenario:purchasing_users}': ['p(95)<4000'],
  },
};

export function browseScenario() {
  group('Homepage', () => {
    const res = http.get(`${BASE_URL}/`);
    check(res, { 'homepage 200': (r) => r.status === 200 });
    sleep(randomIntBetween(3, 10));
  });

  group('Category Page', () => {
    const categories = ['electronics', 'clothing', 'home', 'sports'];
    const cat = categories[Math.floor(Math.random() * categories.length)];
    const res = http.get(`${BASE_URL}/api/products?category=${cat}&limit=20`);
    check(res, { 'category 200': (r) => r.status === 200 });
    sleep(randomIntBetween(5, 15));
  });

  group('Product Detail', () => {
    const productId = randomIntBetween(1, 10000);
    const res = http.get(`${BASE_URL}/api/products/${productId}`);
    check(res, { 'product 200': (r) => r.status === 200 });
    sleep(randomIntBetween(5, 20));
  });
}

export function searchScenario() {
  group('Homepage', () => {
    http.get(`${BASE_URL}/`);
    sleep(randomIntBetween(2, 5));
  });

  group('Search', () => {
    const terms = ['laptop', 'headphones', 'camera', 'phone case', 'charger', 'monitor', 'keyboard'];
    const term = terms[Math.floor(Math.random() * terms.length)];
    const res = http.get(`${BASE_URL}/api/search?q=${encodeURIComponent(term)}&limit=20`);
    check(res, {
      'search 200': (r) => r.status === 200,
      'search has results': (r) => r.json('data').length > 0,
    });
    sleep(randomIntBetween(3, 10));
  });

  group('Product from Search', () => {
    const productId = randomIntBetween(1, 10000);
    const res = http.get(`${BASE_URL}/api/products/${productId}`);
    check(res, { 'product 200': (r) => r.status === 200 });
    sleep(randomIntBetween(5, 15));
  });
}

export function addToCartScenario() {
  // Login first
  const loginRes = http.post(`${BASE_URL}/api/auth/login`, JSON.stringify({
    email: `loadtest-${__VU}@example.com`,
    password: 'LoadTest123!'
  }), { headers: { 'Content-Type': 'application/json' } });

  const token = loginRes.json('access_token');
  const headers = {
    'Content-Type': 'application/json',
    'Authorization': `Bearer ${token}`
  };

  group('Browse Product', () => {
    const productId = randomIntBetween(1, 10000);
    http.get(`${BASE_URL}/api/products/${productId}`, { headers });
    sleep(randomIntBetween(5, 15));
  });

  group('Add to Cart', () => {
    const productId = randomIntBetween(1, 10000);
    const res = http.post(`${BASE_URL}/api/cart/items`, JSON.stringify({
      product_id: productId,
      quantity: randomIntBetween(1, 3)
    }), { headers });
    check(res, { 'add to cart 201': (r) => r.status === 201 });
    sleep(randomIntBetween(3, 10));
  });

  group('View Cart', () => {
    const res = http.get(`${BASE_URL}/api/cart`, { headers });
    check(res, { 'cart 200': (r) => r.status === 200 });
    sleep(randomIntBetween(5, 15));
  });
}

export function purchaseScenario() {
  const loginRes = http.post(`${BASE_URL}/api/auth/login`, JSON.stringify({
    email: `loadtest-${__VU}@example.com`,
    password: 'LoadTest123!'
  }), { headers: { 'Content-Type': 'application/json' } });

  const token = loginRes.json('access_token');
  const headers = {
    'Content-Type': 'application/json',
    'Authorization': `Bearer ${token}`
  };

  group('Add to Cart', () => {
    const productId = randomIntBetween(1, 10000);
    http.post(`${BASE_URL}/api/cart/items`, JSON.stringify({
      product_id: productId,
      quantity: 1
    }), { headers });
    sleep(randomIntBetween(2, 5));
  });

  group('Checkout', () => {
    const res = http.post(`${BASE_URL}/api/orders`, JSON.stringify({
      shipping_address: {
        street: '123 Load Test St',
        city: 'Test City',
        state: 'TS',
        zip: '12345',
        country: 'US'
      },
      payment_token: 'tok_test_visa'
    }), { headers });
    check(res, { 'order created': (r) => r.status === 201 });
    sleep(randomIntBetween(3, 8));
  });
}

export function accountScenario() {
  const loginRes = http.post(`${BASE_URL}/api/auth/login`, JSON.stringify({
    email: `loadtest-${__VU}@example.com`,
    password: 'LoadTest123!'
  }), { headers: { 'Content-Type': 'application/json' } });

  const token = loginRes.json('access_token');
  const headers = { 'Authorization': `Bearer ${token}` };

  group('Profile', () => {
    http.get(`${BASE_URL}/api/users/me`, { headers });
    sleep(randomIntBetween(3, 8));
  });

  group('Order History', () => {
    http.get(`${BASE_URL}/api/orders?limit=10`, { headers });
    sleep(randomIntBetween(5, 15));
  });
}
```

---

## Performance Testing Tools Deep Dive

### k6: Modern Load Testing

k6 is Grafana's open-source load testing tool. It uses JavaScript ES6+ for scripting, executes tests in Go for high performance, and integrates natively with Grafana Cloud and Prometheus.

**Key advantages**:
- Developer-friendly JavaScript scripting
- High performance (single machine can simulate thousands of VUs)
- Built-in metrics and thresholds
- Native cloud integration
- Extensions via xk6 for custom protocols

**Advanced k6 features**:

```javascript
// Browser-level testing with k6 browser module
import { browser } from 'k6/experimental/browser';
import { check } from 'k6';

export const options = {
  scenarios: {
    browser: {
      executor: 'constant-vus',
      vus: 10,
      duration: '5m',
      options: {
        browser: {
          type: 'chromium',
        },
      },
    },
  },
  thresholds: {
    browser_web_vital_lcp: ['p(95)<2500'],
    browser_web_vital_fid: ['p(95)<100'],
    browser_web_vital_cls: ['p(95)<0.1'],
  },
};

export default async function () {
  const page = browser.newPage();

  try {
    await page.goto('https://example.com');

    // Wait for page to be fully loaded
    await page.waitForLoadState('networkidle');

    // Interact with the page
    await page.locator('input[name="search"]').fill('test product');
    await page.locator('button[type="submit"]').click();

    // Verify results loaded
    const results = page.locator('.search-results .product-card');
    check(results, {
      'search results visible': (r) => r.count() > 0,
    });
  } finally {
    page.close();
  }
}
```

**k6 with custom metrics and tags**:

```javascript
import http from 'k6/http';
import { Trend, Counter, Rate, Gauge } from 'k6/metrics';

// Custom metrics
const orderLatency = new Trend('order_processing_time', true);
const ordersCreated = new Counter('orders_created');
const orderFailRate = new Rate('order_failures');
const activeOrders = new Gauge('active_orders_in_system');

export default function() {
  // Tag requests for filtering in dashboards
  const params = {
    tags: {
      endpoint: 'create_order',
      team: 'checkout',
      priority: 'critical'
    }
  };

  const start = Date.now();
  const res = http.post(`${BASE_URL}/api/orders`, orderPayload, params);
  const duration = Date.now() - start;

  orderLatency.add(duration);

  if (res.status === 201) {
    ordersCreated.add(1);
    orderFailRate.add(false);
  } else {
    orderFailRate.add(true);
  }

  activeOrders.add(res.status === 201 ? 1 : 0);
}
```

**k6 output to Prometheus and Grafana**:

```bash
# Run k6 with Prometheus remote write output
k6 run \
  --out experimental-prometheus-rw \
  -e K6_PROMETHEUS_RW_SERVER_URL=http://prometheus:9090/api/v1/write \
  -e K6_PROMETHEUS_RW_TREND_AS_NATIVE_HISTOGRAM=true \
  load-test.js
```

### Locust: Python-Based Load Testing

Locust uses Python for test scripting, making it accessible to teams already proficient in Python. It features a web-based UI for real-time monitoring and distributed execution.

**Installation**:

```bash
pip install locust
```

**Basic Locust test**:

```python
# locustfile.py
from locust import HttpUser, task, between, tag, events
import json
import random
import logging

logger = logging.getLogger(__name__)


class ECommerceUser(HttpUser):
    wait_time = between(1, 10)  # Think time between requests
    host = "https://api.staging.example.com"

    def on_start(self):
        """Called when a simulated user starts. Used for login."""
        response = self.client.post("/api/auth/login", json={
            "email": f"loadtest-{self.environment.runner.user_count}@example.com",
            "password": "LoadTest123!"
        })
        if response.status_code == 200:
            self.token = response.json()["access_token"]
            self.headers = {
                "Authorization": f"Bearer {self.token}",
                "Content-Type": "application/json"
            }
        else:
            logger.error(f"Login failed: {response.status_code}")
            self.token = None
            self.headers = {}

    @task(40)
    @tag("browse")
    def browse_products(self):
        """Browse product catalog - most common user action"""
        # View category page
        categories = ["electronics", "clothing", "home", "sports", "books"]
        category = random.choice(categories)
        with self.client.get(
            f"/api/products?category={category}&limit=20&page=1",
            headers=self.headers,
            name="/api/products?category=[cat]",  # Group in stats
            catch_response=True
        ) as response:
            if response.status_code == 200:
                data = response.json()
                if len(data.get("data", [])) == 0:
                    response.failure("Empty product list")
                else:
                    response.success()
                    # View a random product from results
                    product = random.choice(data["data"])
                    self.client.get(
                        f"/api/products/{product['id']}",
                        headers=self.headers,
                        name="/api/products/[id]"
                    )
            else:
                response.failure(f"Status {response.status_code}")

    @task(25)
    @tag("search")
    def search_products(self):
        """Search for products"""
        search_terms = [
            "wireless headphones", "laptop stand", "USB-C cable",
            "mechanical keyboard", "monitor arm", "webcam HD",
            "mouse pad", "desk lamp", "phone case"
        ]
        term = random.choice(search_terms)
        with self.client.get(
            f"/api/search?q={term}&limit=20",
            headers=self.headers,
            name="/api/search?q=[term]",
            catch_response=True
        ) as response:
            if response.status_code == 200:
                results = response.json()
                if "data" in results:
                    response.success()
                else:
                    response.failure("Invalid search response structure")
            else:
                response.failure(f"Search failed: {response.status_code}")

    @task(20)
    @tag("cart")
    def add_to_cart(self):
        """Add a product to cart"""
        product_id = random.randint(1, 10000)
        with self.client.post(
            "/api/cart/items",
            json={
                "product_id": product_id,
                "quantity": random.randint(1, 3)
            },
            headers=self.headers,
            name="/api/cart/items",
            catch_response=True
        ) as response:
            if response.status_code in [200, 201]:
                response.success()
            elif response.status_code == 404:
                response.success()  # Product not found is acceptable in load test
            else:
                response.failure(f"Cart add failed: {response.status_code}")

    @task(10)
    @tag("checkout")
    def checkout(self):
        """Complete a purchase"""
        # Add item to cart
        self.client.post("/api/cart/items", json={
            "product_id": random.randint(1, 10000),
            "quantity": 1
        }, headers=self.headers)

        # Submit order
        with self.client.post(
            "/api/orders",
            json={
                "shipping_address": {
                    "street": "123 Load Test Blvd",
                    "city": "Test City",
                    "state": "CA",
                    "zip": "90210",
                    "country": "US"
                },
                "payment_token": "tok_test_visa"
            },
            headers=self.headers,
            name="/api/orders",
            catch_response=True
        ) as response:
            if response.status_code == 201:
                response.success()
            else:
                response.failure(f"Order failed: {response.status_code} - {response.text[:200]}")

    @task(5)
    @tag("account")
    def view_account(self):
        """View account and order history"""
        self.client.get("/api/users/me", headers=self.headers, name="/api/users/me")
        self.client.get(
            "/api/orders?limit=10&sort=-created_at",
            headers=self.headers,
            name="/api/orders"
        )


class AdminUser(HttpUser):
    """Simulates admin users performing management tasks"""
    wait_time = between(5, 30)
    weight = 1  # Much fewer admin users

    def on_start(self):
        response = self.client.post("/api/auth/login", json={
            "email": "admin@example.com",
            "password": "AdminP@ss123!"
        })
        self.token = response.json().get("access_token")
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }

    @task(50)
    def view_dashboard(self):
        self.client.get("/api/admin/dashboard/stats", headers=self.headers)

    @task(30)
    def view_orders(self):
        self.client.get("/api/admin/orders?limit=50&status=pending", headers=self.headers)

    @task(20)
    def view_users(self):
        self.client.get("/api/admin/users?limit=50", headers=self.headers)


# Custom event hooks for reporting
@events.request.add_listener
def on_request(request_type, name, response_time, response_length, response, exception, **kwargs):
    if response_time > 5000:
        logger.warning(f"SLOW REQUEST: {request_type} {name} took {response_time}ms")


@events.test_stop.add_listener
def on_test_stop(environment, **kwargs):
    stats = environment.runner.stats
    logger.info(f"\nFinal Stats:")
    logger.info(f"Total requests: {stats.total.num_requests}")
    logger.info(f"Failure rate: {stats.total.fail_ratio:.2%}")
    logger.info(f"Avg response time: {stats.total.avg_response_time:.0f}ms")
    logger.info(f"P95 response time: {stats.total.get_response_time_percentile(0.95):.0f}ms")
```

**Running Locust**:

```bash
# Web UI mode (default)
locust -f locustfile.py --host https://api.staging.example.com

# Headless mode for CI/CD
locust -f locustfile.py \
  --host https://api.staging.example.com \
  --headless \
  --users 500 \
  --spawn-rate 10 \
  --run-time 30m \
  --html report.html \
  --csv results

# Distributed mode (1 master + N workers)
# Master:
locust -f locustfile.py --master --expect-workers 4

# Workers (run on separate machines):
locust -f locustfile.py --worker --master-host 192.168.1.100

# Filter by tags
locust -f locustfile.py --tags browse search --exclude-tags checkout
```

### Apache JMeter: Enterprise Load Testing

JMeter is a Java-based load testing tool with extensive protocol support and a large ecosystem of plugins.

**JMeter CLI execution**:

```bash
# Run test plan in non-GUI mode
jmeter -n \
  -t test-plan.jmx \
  -l results.jtl \
  -j jmeter.log \
  -e -o reports/ \
  -Jusers=500 \
  -Jramp_up=60 \
  -Jduration=1800 \
  -Jtarget_host=api.staging.example.com

# Distributed execution
jmeter -n \
  -t test-plan.jmx \
  -l results.jtl \
  -R worker1:1099,worker2:1099,worker3:1099 \
  -Gusers=500
```

**JMeter with Docker**:

```yaml
# docker-compose.yml for distributed JMeter
version: '3.8'
services:
  jmeter-master:
    image: justb4/jmeter:5.6
    volumes:
      - ./tests:/tests
      - ./reports:/reports
    command: >
      -n -t /tests/api-test-plan.jmx
      -l /reports/results.jtl
      -e -o /reports/html
      -R jmeter-worker-1,jmeter-worker-2
      -Gusers=1000
      -Gramp_up=120
    depends_on:
      - jmeter-worker-1
      - jmeter-worker-2

  jmeter-worker-1:
    image: justb4/jmeter:5.6
    command: -s -Jserver.rmi.ssl.disable=true

  jmeter-worker-2:
    image: justb4/jmeter:5.6
    command: -s -Jserver.rmi.ssl.disable=true
```

**JMeter BeanShell/Groovy scripting for dynamic behavior**:

```groovy
// JSR223 PreProcessor (Groovy) - Dynamic data generation
import groovy.json.JsonOutput
import java.util.concurrent.ThreadLocalRandom

def random = ThreadLocalRandom.current()

// Generate unique user data
def timestamp = System.currentTimeMillis()
def threadNum = ctx.getThreadNum()
def email = "loadtest-${threadNum}-${timestamp}@example.com"
def name = ["John", "Jane", "Bob", "Alice", "Charlie"][random.nextInt(5)] + " " +
           ["Smith", "Johnson", "Williams", "Brown", "Jones"][random.nextInt(5)]

vars.put("user_email", email)
vars.put("user_name", name)
vars.put("product_id", String.valueOf(random.nextInt(1, 10001)))
vars.put("quantity", String.valueOf(random.nextInt(1, 6)))

// Dynamic JSON body
def body = JsonOutput.toJson([
    name: name,
    email: email,
    password: "LoadTest123!",
    role: "user"
])
vars.put("request_body", body)
```

### Gatling: Scala-Based High-Performance Testing

Gatling is a load testing tool built on Scala and Akka, designed for high performance and developer-friendly DSL.

**Installation**:

```bash
# Download and extract
wget https://repo1.maven.org/maven2/io/gatling/highcharts/gatling-charts-highcharts-bundle/3.9.5/gatling-charts-highcharts-bundle-3.9.5-bundle.zip
unzip gatling-charts-highcharts-bundle-3.9.5-bundle.zip

# Or with Maven
mvn archetype:generate \
  -DarchetypeGroupId=io.gatling.highcharts \
  -DarchetypeArtifactId=gatling-highcharts-maven-archetype
```

**Gatling simulation**:

```scala
// src/test/scala/simulations/ECommerceSimulation.scala
package simulations

import io.gatling.core.Predef._
import io.gatling.http.Predef._
import scala.concurrent.duration._

class ECommerceSimulation extends Simulation {

  val httpProtocol = http
    .baseUrl("https://api.staging.example.com")
    .acceptHeader("application/json")
    .contentTypeHeader("application/json")
    .userAgentHeader("Gatling/LoadTest")
    .shareConnections

  // Feeders for dynamic data
  val searchTermFeeder = csv("search-terms.csv").random
  val productIdFeeder = csv("product-ids.csv").random
  val userCredentialsFeeder = csv("test-users.csv").circular

  // Scenario: Authentication
  val authenticate = exec(
    http("Login")
      .post("/api/auth/login")
      .body(StringBody("""{"email":"${email}","password":"${password}"}"""))
      .check(
        status.is(200),
        jsonPath("$.access_token").saveAs("authToken")
      )
  )

  // Scenario: Browse Products
  val browseProducts = group("Browse") {
    exec(
      http("Homepage API")
        .get("/api/featured")
        .header("Authorization", "Bearer ${authToken}")
        .check(status.is(200))
    )
    .pause(3, 10)
    .exec(
      http("Category Products")
        .get("/api/products?category=electronics&limit=20")
        .header("Authorization", "Bearer ${authToken}")
        .check(
          status.is(200),
          jsonPath("$.data[*].id").findAll.saveAs("productIds")
        )
    )
    .pause(5, 15)
    .feed(productIdFeeder)
    .exec(
      http("Product Detail")
        .get("/api/products/${productId}")
        .header("Authorization", "Bearer ${authToken}")
        .check(status.is(200))
    )
    .pause(5, 20)
  }

  // Scenario: Search
  val searchProducts = group("Search") {
    feed(searchTermFeeder)
    .exec(
      http("Search")
        .get("/api/search?q=${searchTerm}&limit=20")
        .header("Authorization", "Bearer ${authToken}")
        .check(
          status.is(200),
          jsonPath("$.data").exists
        )
    )
    .pause(3, 10)
  }

  // Scenario: Checkout
  val checkout = group("Checkout") {
    feed(productIdFeeder)
    .exec(
      http("Add to Cart")
        .post("/api/cart/items")
        .header("Authorization", "Bearer ${authToken}")
        .body(StringBody("""{"product_id":${productId},"quantity":1}"""))
        .check(status.in(200, 201))
    )
    .pause(2, 5)
    .exec(
      http("Create Order")
        .post("/api/orders")
        .header("Authorization", "Bearer ${authToken}")
        .body(StringBody("""{
          "shipping_address":{"street":"123 Test","city":"LA","state":"CA","zip":"90210","country":"US"},
          "payment_token":"tok_test_visa"
        }"""))
        .check(
          status.is(201),
          jsonPath("$.id").saveAs("orderId")
        )
    )
    .pause(3, 8)
  }

  // User journey definitions
  val browsingUser = scenario("Browsing User")
    .feed(userCredentialsFeeder)
    .exec(authenticate)
    .repeat(5)(exec(browseProducts))

  val searchingUser = scenario("Searching User")
    .feed(userCredentialsFeeder)
    .exec(authenticate)
    .repeat(3)(exec(searchProducts).exec(browseProducts))

  val purchasingUser = scenario("Purchasing User")
    .feed(userCredentialsFeeder)
    .exec(authenticate)
    .exec(browseProducts)
    .exec(checkout)

  // Load profile
  setUp(
    browsingUser.inject(
      rampUsers(200).during(5.minutes),
      constantUsersPerSec(10).during(30.minutes)
    ),
    searchingUser.inject(
      rampUsers(125).during(5.minutes),
      constantUsersPerSec(6).during(30.minutes)
    ),
    purchasingUser.inject(
      rampUsers(50).during(5.minutes),
      constantUsersPerSec(2).during(30.minutes)
    )
  )
  .protocols(httpProtocol)
  .assertions(
    global.responseTime.percentile3.lt(3000),    // p95 < 3s
    global.successfulRequests.percent.gt(99.0),    // > 99% success
    forAll.responseTime.percentile3.lt(5000),      // All endpoints p95 < 5s
    details("Checkout / Create Order").responseTime.percentile3.lt(4000)
  )
}
```

**Running Gatling**:

```bash
# Run simulation
./bin/gatling.sh -s simulations.ECommerceSimulation

# With Maven
mvn gatling:test -Dgatling.simulationClass=simulations.ECommerceSimulation

# With specific options
mvn gatling:test \
  -Dgatling.simulationClass=simulations.ECommerceSimulation \
  -DbaseUrl=https://api.staging.example.com \
  -Dusers=500 \
  -Dduration=1800
```

---

## Performance Budgets

### Defining Performance Budgets

Performance budgets set concrete limits on metrics that impact user experience. They serve as guardrails to prevent performance regression.

```javascript
// performance-budget.json
{
  "budgets": [
    {
      "path": "/",
      "name": "Homepage",
      "resourceSizes": [
        { "resourceType": "total", "budget": 500 },
        { "resourceType": "script", "budget": 200 },
        { "resourceType": "image", "budget": 150 },
        { "resourceType": "stylesheet", "budget": 50 },
        { "resourceType": "font", "budget": 80 },
        { "resourceType": "document", "budget": 20 }
      ],
      "resourceCounts": [
        { "resourceType": "script", "budget": 15 },
        { "resourceType": "image", "budget": 20 },
        { "resourceType": "stylesheet", "budget": 5 },
        { "resourceType": "third-party", "budget": 10 }
      ],
      "timings": [
        { "metric": "first-contentful-paint", "budget": 1500 },
        { "metric": "largest-contentful-paint", "budget": 2500 },
        { "metric": "cumulative-layout-shift", "budget": 0.1 },
        { "metric": "total-blocking-time", "budget": 200 },
        { "metric": "time-to-interactive", "budget": 3000 },
        { "metric": "speed-index", "budget": 3000 }
      ]
    },
    {
      "path": "/products/*",
      "name": "Product Pages",
      "resourceSizes": [
        { "resourceType": "total", "budget": 600 },
        { "resourceType": "script", "budget": 250 },
        { "resourceType": "image", "budget": 200 }
      ],
      "timings": [
        { "metric": "first-contentful-paint", "budget": 1800 },
        { "metric": "largest-contentful-paint", "budget": 3000 },
        { "metric": "time-to-interactive", "budget": 3500 }
      ]
    }
  ]
}
```

### Enforcing Performance Budgets in CI/CD

**Using Lighthouse CI**:

```yaml
# .lighthouserc.json
{
  "ci": {
    "collect": {
      "url": [
        "https://staging.example.com/",
        "https://staging.example.com/products",
        "https://staging.example.com/products/1",
        "https://staging.example.com/checkout"
      ],
      "numberOfRuns": 3,
      "settings": {
        "preset": "desktop",
        "throttlingMethod": "simulate"
      }
    },
    "assert": {
      "assertions": {
        "categories:performance": ["error", { "minScore": 0.9 }],
        "first-contentful-paint": ["error", { "maxNumericValue": 1500 }],
        "largest-contentful-paint": ["error", { "maxNumericValue": 2500 }],
        "cumulative-layout-shift": ["error", { "maxNumericValue": 0.1 }],
        "total-blocking-time": ["error", { "maxNumericValue": 200 }],
        "interactive": ["warn", { "maxNumericValue": 3500 }],
        "resource-summary:script:size": ["error", { "maxNumericValue": 200000 }],
        "resource-summary:total:size": ["error", { "maxNumericValue": 500000 }]
      }
    },
    "upload": {
      "target": "lhci",
      "serverBaseUrl": "https://lhci.example.com"
    }
  }
}
```

```yaml
# GitHub Actions workflow for performance budget enforcement
name: Performance Budget Check
on:
  pull_request:
    branches: [main]

jobs:
  lighthouse:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Deploy to preview
        id: deploy
        run: |
          # Deploy PR to preview environment
          echo "url=https://pr-${{ github.event.number }}.preview.example.com" >> $GITHUB_OUTPUT

      - name: Run Lighthouse CI
        uses: treosh/lighthouse-ci-action@v11
        with:
          urls: |
            ${{ steps.deploy.outputs.url }}
            ${{ steps.deploy.outputs.url }}/products
          configPath: .lighthouserc.json
          uploadArtifacts: true
          temporaryPublicStorage: true

      - name: Bundle size check
        run: |
          npm run build
          npx bundlesize

      - name: k6 performance test
        run: |
          k6 run tests/performance/api-budget-test.js \
            -e BASE_URL=${{ steps.deploy.outputs.url }}
```

**Using bundlesize for JavaScript bundle budgets**:

```json
// package.json
{
  "bundlesize": [
    {
      "path": "dist/main.*.js",
      "maxSize": "150 kB",
      "compression": "gzip"
    },
    {
      "path": "dist/vendor.*.js",
      "maxSize": "100 kB",
      "compression": "gzip"
    },
    {
      "path": "dist/*.css",
      "maxSize": "30 kB",
      "compression": "gzip"
    },
    {
      "path": "dist/images/*",
      "maxSize": "200 kB"
    }
  ]
}
```

---

## Bottleneck Identification

### Common Performance Bottlenecks

Performance bottlenecks typically fall into several categories:

**Application-level bottlenecks**:
- Inefficient algorithms (O(n²) instead of O(n log n))
- Excessive memory allocation and garbage collection
- Synchronous operations blocking the event loop
- Missing or misconfigured caching
- Unoptimized database queries (N+1 problem)
- Missing connection pooling
- Excessive logging in hot paths

**Database bottlenecks**:
- Missing indexes on frequently queried columns
- Full table scans on large tables
- Lock contention from concurrent writes
- Connection pool exhaustion
- Unoptimized queries with unnecessary joins
- Missing query plan optimization

**Infrastructure bottlenecks**:
- Insufficient CPU or memory
- Network bandwidth limitations
- Disk I/O saturation
- Load balancer misconfiguration
- DNS resolution delays
- TLS handshake overhead

**External dependency bottlenecks**:
- Slow third-party API responses
- Missing circuit breakers
- Synchronous calls to external services
- Missing retry/timeout configurations

### Identifying Bottlenecks During Load Tests

**Using k6 with Grafana dashboards**:

```javascript
// k6 test with detailed timing breakdowns
import http from 'k6/http';
import { Trend } from 'k6/metrics';

const dbQueryTime = new Trend('custom_db_query_time');
const cacheHitRate = new Trend('custom_cache_hit_rate');

export default function() {
  const res = http.get(`${BASE_URL}/api/products?category=electronics`);

  // Server-side timing headers
  if (res.headers['Server-Timing']) {
    const timings = parseServerTiming(res.headers['Server-Timing']);
    if (timings.db) dbQueryTime.add(timings.db);
    if (timings.cache) cacheHitRate.add(timings.cache === 'hit' ? 1 : 0);
  }

  // HTTP timing breakdown (built into k6)
  // res.timings.blocked    - Time spent blocked (DNS lookup, TCP connect)
  // res.timings.connecting - Time spent establishing TCP connection
  // res.timings.tls_handshaking - Time spent on TLS handshake
  // res.timings.sending    - Time spent sending request
  // res.timings.waiting    - Time waiting for response (TTFB)
  // res.timings.receiving  - Time spent receiving response
  // res.timings.duration   - Total request duration
}

function parseServerTiming(header) {
  const timings = {};
  header.split(',').forEach(entry => {
    const parts = entry.trim().split(';');
    const name = parts[0];
    parts.forEach(part => {
      if (part.includes('dur=')) {
        timings[name] = parseFloat(part.split('=')[1]);
      }
    });
  });
  return timings;
}
```

**Database query analysis during load tests**:

```sql
-- PostgreSQL: Find slow queries during load test
SELECT
  calls,
  round(total_exec_time::numeric, 2) AS total_time_ms,
  round(mean_exec_time::numeric, 2) AS mean_time_ms,
  round(max_exec_time::numeric, 2) AS max_time_ms,
  round((100 * total_exec_time / sum(total_exec_time) OVER ())::numeric, 2) AS percent_total,
  query
FROM pg_stat_statements
ORDER BY total_exec_time DESC
LIMIT 20;

-- Find missing indexes
SELECT
  schemaname,
  tablename,
  seq_scan,
  seq_tup_read,
  idx_scan,
  idx_tup_fetch,
  n_tup_ins,
  n_tup_upd,
  n_tup_del
FROM pg_stat_user_tables
WHERE seq_scan > idx_scan
  AND seq_scan > 100
ORDER BY seq_tup_read DESC
LIMIT 20;

-- Lock contention
SELECT
  locktype,
  relation::regclass,
  mode,
  granted,
  pid,
  query
FROM pg_locks l
JOIN pg_stat_activity a ON l.pid = a.pid
WHERE NOT granted
ORDER BY a.query_start;

-- Connection pool utilization
SELECT
  count(*) AS total_connections,
  count(*) FILTER (WHERE state = 'active') AS active,
  count(*) FILTER (WHERE state = 'idle') AS idle,
  count(*) FILTER (WHERE state = 'idle in transaction') AS idle_in_transaction,
  max_conn AS max_connections
FROM pg_stat_activity
CROSS JOIN (SELECT setting::int AS max_conn FROM pg_settings WHERE name = 'max_connections') mc
GROUP BY max_conn;
```

**Application profiling during load tests**:

```javascript
// Node.js CPU profiling during load test
const v8Profiler = require('v8-profiler-next');
const fs = require('fs');

// Start profiling when load test begins
app.post('/debug/start-profiling', (req, res) => {
  v8Profiler.startProfiling('LoadTest');
  res.json({ status: 'profiling started' });
});

// Stop profiling and save results
app.post('/debug/stop-profiling', (req, res) => {
  const profile = v8Profiler.stopProfiling('LoadTest');
  profile.export((error, result) => {
    fs.writeFileSync(`./profiles/cpu-${Date.now()}.cpuprofile`, result);
    profile.delete();
    res.json({ status: 'profile saved' });
  });
});

// Memory snapshot
app.post('/debug/heap-snapshot', (req, res) => {
  const snapshot = v8Profiler.takeSnapshot('heap');
  snapshot.export((error, result) => {
    fs.writeFileSync(`./profiles/heap-${Date.now()}.heapsnapshot`, result);
    snapshot.delete();
    res.json({ status: 'snapshot saved' });
  });
});
```

---

## Stress, Soak, and Spike Testing

### Stress Testing

Stress testing pushes the system beyond its normal capacity to identify the breaking point and observe failure behavior:

```javascript
// k6 stress test
export const options = {
  stages: [
    { duration: '2m', target: 100 },    // Below normal
    { duration: '5m', target: 100 },    // Stay at normal
    { duration: '2m', target: 200 },    // Normal load
    { duration: '5m', target: 200 },    // Stay at normal peak
    { duration: '2m', target: 500 },    // Above normal
    { duration: '5m', target: 500 },    // Stay at high load
    { duration: '2m', target: 1000 },   // Well above capacity
    { duration: '5m', target: 1000 },   // Stay at extreme load
    { duration: '2m', target: 2000 },   // Breaking point territory
    { duration: '5m', target: 2000 },   // Observe behavior at breaking point
    { duration: '10m', target: 0 },     // Recovery phase
  ],
  thresholds: {
    // Relaxed thresholds for stress test
    http_req_failed: ['rate<0.5'],  // Allow up to 50% failure at breaking point
  },
};
```

Key observations during stress testing:
- At what load does the error rate begin increasing?
- How does response time degrade as load increases?
- Does the system recover gracefully after overload?
- Are there cascading failures?
- Do circuit breakers activate?
- Does auto-scaling trigger?

### Soak Testing (Endurance Testing)

Soak testing runs the system under sustained load for extended periods (4-24 hours) to identify:
- Memory leaks
- Connection pool exhaustion
- Log file growth
- Database connection leaks
- Thread leaks
- Gradual performance degradation

```javascript
// k6 soak test
export const options = {
  stages: [
    { duration: '5m', target: 200 },    // Ramp up
    { duration: '8h', target: 200 },    // Sustained load for 8 hours
    { duration: '5m', target: 0 },      // Ramp down
  ],
  thresholds: {
    http_req_duration: ['p(95)<3000'],
    http_req_failed: ['rate<0.01'],
  },
};

// Monitor memory usage over time
export function handleSummary(data) {
  return {
    'soak-test-summary.json': JSON.stringify(data, null, 2),
  };
}
```

**Monitoring checklist for soak tests**:

```bash
# Monitor memory usage over time
watch -n 60 'curl -s http://app:3000/metrics | grep process_resident_memory_bytes'

# Monitor database connections
watch -n 30 'psql -c "SELECT count(*) FROM pg_stat_activity"'

# Monitor disk space
watch -n 300 'df -h /var/log'

# Monitor open file descriptors
watch -n 60 'ls /proc/$(pgrep node)/fd | wc -l'

# Monitor garbage collection (Node.js)
watch -n 10 'curl -s http://app:3000/metrics | grep nodejs_gc'
```

### Spike Testing

Spike testing simulates sudden, dramatic traffic increases:

```javascript
// k6 spike test
export const options = {
  stages: [
    { duration: '2m', target: 100 },     // Normal load
    { duration: '10s', target: 3000 },    // SPIKE! 30x traffic in 10 seconds
    { duration: '3m', target: 3000 },     // Maintain spike
    { duration: '10s', target: 100 },     // Back to normal
    { duration: '5m', target: 100 },      // Recovery observation
    { duration: '10s', target: 5000 },    // Even bigger spike
    { duration: '3m', target: 5000 },     // Maintain
    { duration: '30s', target: 0 },       // Full stop
    { duration: '5m', target: 0 },        // Recovery observation
  ],
};
```

---

## Real User Monitoring (RUM)

### Implementing RUM

Real User Monitoring captures performance data from actual users in production:

```javascript
// Custom RUM implementation
class PerformanceMonitor {
  constructor(config = {}) {
    this.endpoint = config.endpoint || '/api/rum';
    this.sampleRate = config.sampleRate || 0.1; // 10% of users
    this.buffer = [];
    this.flushInterval = config.flushInterval || 5000;

    if (Math.random() < this.sampleRate) {
      this.init();
    }
  }

  init() {
    // Navigation Timing
    window.addEventListener('load', () => {
      setTimeout(() => this.collectNavigationTiming(), 0);
    });

    // Core Web Vitals
    this.observeWebVitals();

    // Long Tasks
    this.observeLongTasks();

    // Resource Timing
    this.observeResources();

    // Periodic flush
    setInterval(() => this.flush(), this.flushInterval);

    // Flush on page unload
    window.addEventListener('visibilitychange', () => {
      if (document.visibilityState === 'hidden') {
        this.flush();
      }
    });
  }

  collectNavigationTiming() {
    const nav = performance.getEntriesByType('navigation')[0];
    if (!nav) return;

    this.buffer.push({
      type: 'navigation',
      url: window.location.href,
      timestamp: Date.now(),
      metrics: {
        dns: nav.domainLookupEnd - nav.domainLookupStart,
        tcp: nav.connectEnd - nav.connectStart,
        tls: nav.secureConnectionStart > 0 ? nav.connectEnd - nav.secureConnectionStart : 0,
        ttfb: nav.responseStart - nav.requestStart,
        download: nav.responseEnd - nav.responseStart,
        domParsing: nav.domInteractive - nav.responseEnd,
        domContentLoaded: nav.domContentLoadedEventEnd - nav.fetchStart,
        loadComplete: nav.loadEventEnd - nav.fetchStart,
        transferSize: nav.transferSize,
        encodedBodySize: nav.encodedBodySize,
        decodedBodySize: nav.decodedBodySize
      }
    });
  }

  observeWebVitals() {
    // Largest Contentful Paint (LCP)
    new PerformanceObserver((list) => {
      const entries = list.getEntries();
      const lastEntry = entries[entries.length - 1];
      this.buffer.push({
        type: 'web-vital',
        metric: 'LCP',
        value: lastEntry.startTime,
        element: lastEntry.element?.tagName,
        url: window.location.href,
        timestamp: Date.now()
      });
    }).observe({ type: 'largest-contentful-paint', buffered: true });

    // First Input Delay (FID) / Interaction to Next Paint (INP)
    new PerformanceObserver((list) => {
      list.getEntries().forEach(entry => {
        this.buffer.push({
          type: 'web-vital',
          metric: 'FID',
          value: entry.processingStart - entry.startTime,
          eventType: entry.name,
          url: window.location.href,
          timestamp: Date.now()
        });
      });
    }).observe({ type: 'first-input', buffered: true });

    // Cumulative Layout Shift (CLS)
    let clsValue = 0;
    new PerformanceObserver((list) => {
      list.getEntries().forEach(entry => {
        if (!entry.hadRecentInput) {
          clsValue += entry.value;
        }
      });
      this.buffer.push({
        type: 'web-vital',
        metric: 'CLS',
        value: clsValue,
        url: window.location.href,
        timestamp: Date.now()
      });
    }).observe({ type: 'layout-shift', buffered: true });
  }

  observeLongTasks() {
    new PerformanceObserver((list) => {
      list.getEntries().forEach(entry => {
        this.buffer.push({
          type: 'long-task',
          duration: entry.duration,
          startTime: entry.startTime,
          url: window.location.href,
          timestamp: Date.now()
        });
      });
    }).observe({ type: 'longtask', buffered: true });
  }

  observeResources() {
    new PerformanceObserver((list) => {
      list.getEntries().forEach(entry => {
        if (entry.duration > 1000) { // Only slow resources
          this.buffer.push({
            type: 'slow-resource',
            name: entry.name,
            duration: entry.duration,
            transferSize: entry.transferSize,
            initiatorType: entry.initiatorType,
            url: window.location.href,
            timestamp: Date.now()
          });
        }
      });
    }).observe({ type: 'resource', buffered: true });
  }

  flush() {
    if (this.buffer.length === 0) return;

    const payload = [...this.buffer];
    this.buffer = [];

    // Use sendBeacon for reliability during page unload
    if (navigator.sendBeacon) {
      navigator.sendBeacon(this.endpoint, JSON.stringify(payload));
    } else {
      fetch(this.endpoint, {
        method: 'POST',
        body: JSON.stringify(payload),
        headers: { 'Content-Type': 'application/json' },
        keepalive: true
      }).catch(() => {}); // Silently fail
    }
  }
}

// Initialize
const monitor = new PerformanceMonitor({
  endpoint: 'https://analytics.example.com/rum',
  sampleRate: 0.1
});
```

### RUM Data Analysis

```sql
-- Analyze RUM data in a data warehouse
-- P50, P75, P95 LCP by page
SELECT
  url_path,
  COUNT(*) as sample_count,
  PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY lcp_ms) AS p50_lcp,
  PERCENTILE_CONT(0.75) WITHIN GROUP (ORDER BY lcp_ms) AS p75_lcp,
  PERCENTILE_CONT(0.95) WITHIN GROUP (ORDER BY lcp_ms) AS p95_lcp,
  AVG(lcp_ms) AS avg_lcp
FROM rum_web_vitals
WHERE metric = 'LCP'
  AND timestamp >= NOW() - INTERVAL '7 days'
GROUP BY url_path
ORDER BY p95_lcp DESC;

-- Performance trend over time
SELECT
  DATE_TRUNC('hour', timestamp) AS hour,
  PERCENTILE_CONT(0.95) WITHIN GROUP (ORDER BY value) AS p95_value,
  COUNT(*) AS samples
FROM rum_web_vitals
WHERE metric = 'LCP'
  AND timestamp >= NOW() - INTERVAL '30 days'
GROUP BY DATE_TRUNC('hour', timestamp)
ORDER BY hour;

-- Performance by device type and connection
SELECT
  device_type,
  connection_type,
  COUNT(*) AS samples,
  PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY lcp_ms) AS p50_lcp,
  PERCENTILE_CONT(0.95) WITHIN GROUP (ORDER BY lcp_ms) AS p95_lcp
FROM rum_web_vitals rv
JOIN rum_sessions rs ON rv.session_id = rs.id
WHERE metric = 'LCP'
  AND timestamp >= NOW() - INTERVAL '7 days'
GROUP BY device_type, connection_type
ORDER BY p95_lcp DESC;
```

---

## Core Web Vitals Testing

### Understanding Core Web Vitals

Google's Core Web Vitals are three metrics that measure real-world user experience:

1. **Largest Contentful Paint (LCP)**: Measures loading performance. Good: < 2.5s
2. **Interaction to Next Paint (INP)**: Measures interactivity. Good: < 200ms (replaced FID in March 2024)
3. **Cumulative Layout Shift (CLS)**: Measures visual stability. Good: < 0.1

### Automated Core Web Vitals Testing

```javascript
// Lighthouse programmatic testing
const lighthouse = require('lighthouse');
const chromeLauncher = require('chrome-launcher');

async function runLighthouse(url, options = {}) {
  const chrome = await chromeLauncher.launch({ chromeFlags: ['--headless'] });

  const result = await lighthouse(url, {
    port: chrome.port,
    output: 'json',
    logLevel: 'error',
    ...options
  });

  await chrome.kill();
  return result.lhr;
}

async function testCoreWebVitals() {
  const pages = [
    { url: 'https://example.com/', name: 'Homepage' },
    { url: 'https://example.com/products', name: 'Product Listing' },
    { url: 'https://example.com/products/1', name: 'Product Detail' },
    { url: 'https://example.com/checkout', name: 'Checkout' }
  ];

  const results = [];

  for (const page of pages) {
    // Run 3 times and take median
    const runs = [];
    for (let i = 0; i < 3; i++) {
      const result = await runLighthouse(page.url, {
        onlyCategories: ['performance'],
        formFactor: 'mobile',
        throttling: {
          rttMs: 150,
          throughputKbps: 1638.4,
          cpuSlowdownMultiplier: 4
        }
      });
      runs.push(result);
    }

    // Extract median values
    const lcpValues = runs.map(r => r.audits['largest-contentful-paint'].numericValue).sort();
    const clsValues = runs.map(r => r.audits['cumulative-layout-shift'].numericValue).sort();
    const tbtValues = runs.map(r => r.audits['total-blocking-time'].numericValue).sort();
    const siValues = runs.map(r => r.audits['speed-index'].numericValue).sort();

    const median = arr => arr[Math.floor(arr.length / 2)];

    results.push({
      page: page.name,
      url: page.url,
      lcp: median(lcpValues),
      cls: median(clsValues),
      tbt: median(tbtValues),
      speedIndex: median(siValues),
      performanceScore: median(runs.map(r => r.categories.performance.score).sort()),
      lcpPassing: median(lcpValues) < 2500,
      clsPassing: median(clsValues) < 0.1,
      tbtPassing: median(tbtValues) < 200
    });
  }

  // Report results
  console.table(results.map(r => ({
    Page: r.page,
    'LCP (ms)': Math.round(r.lcp),
    'CLS': r.cls.toFixed(3),
    'TBT (ms)': Math.round(r.tbt),
    'Score': Math.round(r.performanceScore * 100),
    'Pass': r.lcpPassing && r.clsPassing && r.tbtPassing ? '✅' : '❌'
  })));

  // Assert all pages pass
  const failing = results.filter(r => !r.lcpPassing || !r.clsPassing || !r.tbtPassing);
  if (failing.length > 0) {
    console.error('\nFailing pages:');
    failing.forEach(r => {
      if (!r.lcpPassing) console.error(`  ${r.page}: LCP ${Math.round(r.lcp)}ms > 2500ms`);
      if (!r.clsPassing) console.error(`  ${r.page}: CLS ${r.cls.toFixed(3)} > 0.1`);
      if (!r.tbtPassing) console.error(`  ${r.page}: TBT ${Math.round(r.tbt)}ms > 200ms`);
    });
    process.exit(1);
  }
}

testCoreWebVitals();
```

### Web Vitals Testing with Playwright

```javascript
// playwright-web-vitals.test.js
const { test, expect } = require('@playwright/test');

test.describe('Core Web Vitals', () => {
  test('Homepage meets LCP budget', async ({ page }) => {
    // Inject web-vitals library
    await page.addInitScript(() => {
      window.__webVitals = {};
    });

    await page.goto('https://example.com');

    // Measure LCP
    const lcp = await page.evaluate(() => {
      return new Promise((resolve) => {
        new PerformanceObserver((list) => {
          const entries = list.getEntries();
          resolve(entries[entries.length - 1].startTime);
        }).observe({ type: 'largest-contentful-paint', buffered: true });

        // Timeout after 10s
        setTimeout(() => resolve(null), 10000);
      });
    });

    expect(lcp).toBeLessThan(2500);
  });

  test('Homepage meets CLS budget', async ({ page }) => {
    await page.goto('https://example.com');

    // Wait for page to settle
    await page.waitForTimeout(5000);

    const cls = await page.evaluate(() => {
      return new Promise((resolve) => {
        let clsValue = 0;
        new PerformanceObserver((list) => {
          list.getEntries().forEach(entry => {
            if (!entry.hadRecentInput) {
              clsValue += entry.value;
            }
          });
        }).observe({ type: 'layout-shift', buffered: true });

        setTimeout(() => resolve(clsValue), 3000);
      });
    });

    expect(cls).toBeLessThan(0.1);
  });

  test('No long tasks blocking interactivity', async ({ page }) => {
    const longTasks = [];

    await page.addInitScript(() => {
      window.__longTasks = [];
      new PerformanceObserver((list) => {
        list.getEntries().forEach(entry => {
          window.__longTasks.push({
            duration: entry.duration,
            startTime: entry.startTime
          });
        });
      }).observe({ type: 'longtask', buffered: true });
    });

    await page.goto('https://example.com');
    await page.waitForTimeout(5000);

    const tasks = await page.evaluate(() => window.__longTasks);

    // No long task should exceed 200ms
    tasks.forEach(task => {
      expect(task.duration).toBeLessThan(200);
    });

    // Total blocking time should be under 300ms
    const totalBlockingTime = tasks.reduce(
      (sum, task) => sum + Math.max(0, task.duration - 50), 0
    );
    expect(totalBlockingTime).toBeLessThan(300);
  });
});
```

---

## CI/CD Integration and Performance Regression Detection

### Automated Performance Gates

```yaml
# GitHub Actions with performance gates
name: Performance Tests
on:
  pull_request:
    branches: [main]

jobs:
  performance:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Build and deploy preview
        run: |
          docker compose -f docker-compose.test.yml up -d
          sleep 30  # Wait for services

      - name: Seed test data
        run: |
          docker compose exec -T app npm run db:seed:perf

      - name: Run k6 baseline test
        run: |
          k6 run tests/performance/baseline.js \
            --out json=k6-results.json \
            -e BASE_URL=http://localhost:3000
        continue-on-error: true

      - name: Analyze results
        id: analyze
        run: |
          node scripts/analyze-performance.js k6-results.json
        env:
          P95_THRESHOLD_MS: 500
          ERROR_RATE_THRESHOLD: 0.01

      - name: Comment PR with results
        if: github.event_name == 'pull_request'
        uses: actions/github-script@v7
        with:
          script: |
            const fs = require('fs');
            const summary = fs.readFileSync('performance-summary.md', 'utf8');
            github.rest.issues.createComment({
              owner: context.repo.owner,
              repo: context.repo.repo,
              issue_number: context.issue.number,
              body: summary
            });

      - name: Fail if regression detected
        if: steps.analyze.outputs.regression == 'true'
        run: exit 1
```

**Performance analysis script**:

```javascript
// scripts/analyze-performance.js
const fs = require('fs');

const resultsFile = process.argv[2];
const results = fs.readFileSync(resultsFile, 'utf8')
  .split('\n')
  .filter(line => line.trim())
  .map(line => JSON.parse(line));

const httpMetrics = results.filter(r => r.type === 'Point' && r.metric === 'http_req_duration');
const durations = httpMetrics.map(r => r.data.value).sort((a, b) => a - b);

const p50 = durations[Math.floor(durations.length * 0.5)];
const p95 = durations[Math.floor(durations.length * 0.95)];
const p99 = durations[Math.floor(durations.length * 0.99)];

const errorPoints = results.filter(r => r.type === 'Point' && r.metric === 'http_req_failed');
const errorRate = errorPoints.filter(r => r.data.value === 1).length / errorPoints.length;

const P95_THRESHOLD = parseInt(process.env.P95_THRESHOLD_MS || '500');
const ERROR_THRESHOLD = parseFloat(process.env.ERROR_RATE_THRESHOLD || '0.01');

const regression = p95 > P95_THRESHOLD || errorRate > ERROR_THRESHOLD;

const summary = `## 📊 Performance Test Results

| Metric | Value | Threshold | Status |
|--------|-------|-----------|--------|
| P50 Response Time | ${Math.round(p50)}ms | - | ℹ️ |
| P95 Response Time | ${Math.round(p95)}ms | ${P95_THRESHOLD}ms | ${p95 <= P95_THRESHOLD ? '✅' : '❌'} |
| P99 Response Time | ${Math.round(p99)}ms | - | ℹ️ |
| Error Rate | ${(errorRate * 100).toFixed(2)}% | ${(ERROR_THRESHOLD * 100).toFixed(2)}% | ${errorRate <= ERROR_THRESHOLD ? '✅' : '❌'} |
| Total Requests | ${durations.length} | - | ℹ️ |

${regression ? '⚠️ **Performance regression detected!** Please investigate before merging.' : '✅ **All performance checks passed.**'}
`;

fs.writeFileSync('performance-summary.md', summary);

// Set output for GitHub Actions
if (process.env.GITHUB_OUTPUT) {
  fs.appendFileSync(process.env.GITHUB_OUTPUT, `regression=${regression}\n`);
}

console.log(summary);
process.exit(regression ? 1 : 0);
```

---

## Performance Testing Best Practices Summary

### Before Testing
1. Define clear, measurable performance requirements tied to business goals
2. Create a realistic workload model based on production traffic patterns
3. Use a production-equivalent test environment
4. Seed the database with production-scale data volumes
5. Mock external dependencies to isolate your system
6. Set up comprehensive monitoring before starting tests

### During Testing
1. Start with baseline tests to establish reference metrics
2. Run load tests incrementally — don't jump to maximum load
3. Monitor server resources (CPU, memory, disk, network) in real-time
4. Watch for errors, not just slow responses
5. Capture database query performance and connection pool metrics
6. Record all environment details for reproducibility

### After Testing
1. Compare results against defined SLAs and budgets
2. Identify the top bottlenecks and prioritize fixes
3. Document findings with specific metrics, not vague observations
4. Create tickets for performance improvements with clear acceptance criteria
5. Re-run tests after fixes to verify improvement
6. Archive results for historical comparison

### Continuous Performance
1. Integrate performance tests into CI/CD pipelines
2. Set automated performance gates that block regressions
3. Monitor real user metrics (RUM) alongside synthetic tests
4. Track Core Web Vitals trends over time
5. Review performance budgets quarterly and tighten them
6. Share performance dashboards with the entire team

Performance testing is not a one-time activity but an ongoing practice. By embedding it into the development workflow, teams can catch regressions early, maintain user experience, and ensure the application scales to meet business demands. The tools and techniques covered in this chapter provide a comprehensive foundation for building a world-class performance testing practice.
