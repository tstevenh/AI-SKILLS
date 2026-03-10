# Chapter: API Testing Deep Dive

## Introduction to API Testing

Application Programming Interfaces (APIs) serve as the backbone of modern software architecture. They enable communication between services, power mobile applications, feed data to front-end interfaces, and facilitate integrations with third-party systems. API testing is the practice of verifying that these interfaces work correctly, securely, and performantly — without relying on a graphical user interface.

Unlike UI testing, which validates what users see and interact with, API testing operates at the service layer. This makes it faster to execute, more stable (less prone to flakiness), and capable of catching defects earlier in the development lifecycle. A well-constructed API test suite can validate business logic, data transformations, authentication flows, error handling, and performance characteristics — all before a single pixel is rendered on screen.

API testing sits in the middle of the testing pyramid. Unit tests form the base, API/integration tests occupy the middle, and UI tests sit at the top. The middle layer is often the most valuable because it combines broad coverage with reasonable execution speed. A single API test can validate an entire workflow — user registration, data persistence, email triggering — in milliseconds rather than the seconds required by a browser-based test.

The importance of API testing has grown dramatically with the rise of microservices architectures. When a monolithic application is decomposed into dozens or hundreds of services, the number of inter-service APIs explodes. Each API represents a contract between teams, and breaking changes can cascade through the system. Rigorous API testing, including contract testing, becomes essential to maintaining system stability.

This chapter provides a comprehensive deep dive into API testing methodologies, tools, and best practices. We cover REST and GraphQL testing, automation with Postman and Newman, contract testing with Pact, schema validation, security testing, performance testing, and service virtualization. By the end, you will have the knowledge to build a robust API testing strategy for any application.

---

## REST API Testing Fundamentals

### Understanding REST Architecture

Representational State Transfer (REST) is an architectural style for designing networked applications. RESTful APIs use HTTP methods to perform operations on resources identified by URLs. The core principles include:

- **Statelessness**: Each request contains all information needed to process it
- **Resource-based URLs**: Endpoints represent resources (e.g., `/users/123`)
- **HTTP methods**: GET (read), POST (create), PUT (update), PATCH (partial update), DELETE (remove)
- **Standard status codes**: 200 (OK), 201 (Created), 400 (Bad Request), 401 (Unauthorized), 404 (Not Found), 500 (Internal Server Error)
- **Content negotiation**: Clients specify desired format via Accept headers

### HTTP Methods and Their Testing Implications

Each HTTP method has specific semantics that dictate testing requirements:

**GET requests** should be idempotent and safe (no side effects). Testing GET endpoints involves:

```bash
# Basic GET request with curl
curl -X GET https://api.example.com/users/123 \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIs..." \
  -H "Accept: application/json"

# Expected response
{
  "id": 123,
  "name": "Jane Doe",
  "email": "jane@example.com",
  "created_at": "2024-01-15T10:30:00Z",
  "role": "admin"
}
```

Test cases for GET endpoints include:
- Valid resource retrieval returns 200 with correct data
- Non-existent resource returns 404
- Unauthorized access returns 401
- Forbidden access returns 403
- Query parameters filter results correctly
- Pagination works (limit, offset, cursor)
- Response headers include correct Content-Type
- Caching headers (ETag, Last-Modified) are present

**POST requests** create new resources. Testing involves:

```bash
# Create a new user
curl -X POST https://api.example.com/users \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIs..." \
  -H "Content-Type: application/json" \
  -d '{
    "name": "John Smith",
    "email": "john@example.com",
    "password": "SecureP@ss123",
    "role": "user"
  }'

# Expected response (201 Created)
{
  "id": 456,
  "name": "John Smith",
  "email": "john@example.com",
  "role": "user",
  "created_at": "2024-03-20T14:22:00Z"
}
```

Test cases for POST endpoints include:
- Valid creation returns 201 with Location header
- Duplicate resource returns 409 Conflict
- Missing required fields return 400 with descriptive errors
- Invalid field formats return 422 Unprocessable Entity
- Exceeding field length limits returns appropriate error
- SQL injection attempts are rejected
- XSS payloads are sanitized
- Resource is actually persisted (verify with GET)

**PUT and PATCH requests** modify existing resources:

```bash
# Full update with PUT
curl -X PUT https://api.example.com/users/123 \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIs..." \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Jane Smith",
    "email": "jane.smith@example.com",
    "role": "admin"
  }'

# Partial update with PATCH
curl -X PATCH https://api.example.com/users/123 \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIs..." \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Jane Smith"
  }'
```

**DELETE requests** remove resources:

```bash
# Delete a user
curl -X DELETE https://api.example.com/users/123 \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIs..."

# Expected: 204 No Content or 200 with confirmation
```

### Response Validation Strategies

Thorough API testing goes beyond checking status codes. A comprehensive validation strategy includes:

**Status code validation**: Verify the correct HTTP status code for each scenario.

**Response body validation**: Check that response data matches expected values, data types, and structure.

**Header validation**: Verify Content-Type, Cache-Control, CORS headers, rate limit headers, and custom headers.

**Response time validation**: Ensure responses arrive within acceptable thresholds (e.g., under 200ms for simple queries).

**Schema validation**: Verify the response structure matches the documented API schema.

Here is an example using JavaScript with the `supertest` library:

```javascript
const request = require('supertest');
const app = require('../app');

describe('Users API', () => {
  describe('GET /api/users/:id', () => {
    it('should return a user with valid structure', async () => {
      const response = await request(app)
        .get('/api/users/123')
        .set('Authorization', `Bearer ${authToken}`)
        .expect(200)
        .expect('Content-Type', /json/);

      expect(response.body).toHaveProperty('id', 123);
      expect(response.body).toHaveProperty('name');
      expect(response.body).toHaveProperty('email');
      expect(response.body).toHaveProperty('created_at');
      expect(typeof response.body.name).toBe('string');
      expect(response.body.email).toMatch(/^[^\s@]+@[^\s@]+\.[^\s@]+$/);
      expect(new Date(response.body.created_at)).toBeInstanceOf(Date);
    });

    it('should return 404 for non-existent user', async () => {
      const response = await request(app)
        .get('/api/users/999999')
        .set('Authorization', `Bearer ${authToken}`)
        .expect(404);

      expect(response.body).toHaveProperty('error');
      expect(response.body.error).toContain('not found');
    });

    it('should return 401 without authentication', async () => {
      await request(app)
        .get('/api/users/123')
        .expect(401);
    });
  });

  describe('POST /api/users', () => {
    it('should create a user and return 201', async () => {
      const newUser = {
        name: 'Test User',
        email: `test-${Date.now()}@example.com`,
        password: 'SecureP@ss123',
        role: 'user'
      };

      const response = await request(app)
        .post('/api/users')
        .set('Authorization', `Bearer ${adminToken}`)
        .send(newUser)
        .expect(201)
        .expect('Content-Type', /json/);

      expect(response.body).toHaveProperty('id');
      expect(response.body.name).toBe(newUser.name);
      expect(response.body.email).toBe(newUser.email);
      expect(response.body).not.toHaveProperty('password');
      expect(response.headers).toHaveProperty('location');
    });

    it('should reject duplicate email with 409', async () => {
      const duplicateUser = {
        name: 'Another User',
        email: 'existing@example.com',
        password: 'SecureP@ss123',
        role: 'user'
      };

      await request(app)
        .post('/api/users')
        .set('Authorization', `Bearer ${adminToken}`)
        .send(duplicateUser)
        .expect(409);
    });

    it('should validate required fields', async () => {
      const response = await request(app)
        .post('/api/users')
        .set('Authorization', `Bearer ${adminToken}`)
        .send({ name: 'Incomplete User' })
        .expect(400);

      expect(response.body.errors).toContainEqual(
        expect.objectContaining({ field: 'email' })
      );
    });
  });
});
```

### Testing Query Parameters and Filtering

APIs often support complex query parameters for filtering, sorting, and pagination:

```javascript
describe('GET /api/products', () => {
  it('should filter by category', async () => {
    const response = await request(app)
      .get('/api/products?category=electronics')
      .set('Authorization', `Bearer ${authToken}`)
      .expect(200);

    response.body.data.forEach(product => {
      expect(product.category).toBe('electronics');
    });
  });

  it('should paginate results', async () => {
    const page1 = await request(app)
      .get('/api/products?page=1&limit=10')
      .set('Authorization', `Bearer ${authToken}`)
      .expect(200);

    expect(page1.body.data).toHaveLength(10);
    expect(page1.body.meta.total).toBeGreaterThan(10);
    expect(page1.body.meta.page).toBe(1);
    expect(page1.body.meta.totalPages).toBeGreaterThan(1);

    const page2 = await request(app)
      .get('/api/products?page=2&limit=10')
      .set('Authorization', `Bearer ${authToken}`)
      .expect(200);

    expect(page2.body.data[0].id).not.toBe(page1.body.data[0].id);
  });

  it('should sort by price descending', async () => {
    const response = await request(app)
      .get('/api/products?sort=-price')
      .set('Authorization', `Bearer ${authToken}`)
      .expect(200);

    const prices = response.body.data.map(p => p.price);
    expect(prices).toEqual([...prices].sort((a, b) => b - a));
  });

  it('should handle date range filtering', async () => {
    const response = await request(app)
      .get('/api/orders?created_after=2024-01-01&created_before=2024-03-31')
      .set('Authorization', `Bearer ${authToken}`)
      .expect(200);

    response.body.data.forEach(order => {
      const date = new Date(order.created_at);
      expect(date >= new Date('2024-01-01')).toBe(true);
      expect(date <= new Date('2024-03-31')).toBe(true);
    });
  });
});
```

---

## GraphQL API Testing

### Understanding GraphQL

GraphQL is a query language for APIs developed by Facebook. Unlike REST, where the server defines the response structure, GraphQL clients specify exactly what data they need. This eliminates over-fetching and under-fetching problems common in REST APIs.

Key concepts:
- **Queries**: Read operations (equivalent to GET)
- **Mutations**: Write operations (equivalent to POST/PUT/DELETE)
- **Subscriptions**: Real-time data via WebSocket
- **Schema**: Strongly typed definition of available operations and data types
- **Resolvers**: Server-side functions that populate response data

### Testing GraphQL Queries

```javascript
const request = require('supertest');
const app = require('../app');

describe('GraphQL API', () => {
  describe('User Queries', () => {
    it('should fetch a user with selected fields', async () => {
      const query = `
        query GetUser($id: ID!) {
          user(id: $id) {
            id
            name
            email
            posts {
              id
              title
              publishedAt
            }
          }
        }
      `;

      const response = await request(app)
        .post('/graphql')
        .set('Authorization', `Bearer ${authToken}`)
        .send({
          query,
          variables: { id: '123' }
        })
        .expect(200);

      expect(response.body.data.user).toBeDefined();
      expect(response.body.data.user.id).toBe('123');
      expect(response.body.data.user.name).toBeDefined();
      expect(response.body.data.user.posts).toBeInstanceOf(Array);
      expect(response.body.errors).toBeUndefined();
    });

    it('should return null for non-existent user', async () => {
      const query = `
        query GetUser($id: ID!) {
          user(id: $id) {
            id
            name
          }
        }
      `;

      const response = await request(app)
        .post('/graphql')
        .set('Authorization', `Bearer ${authToken}`)
        .send({
          query,
          variables: { id: '999999' }
        })
        .expect(200);

      expect(response.body.data.user).toBeNull();
    });

    it('should handle nested query with pagination', async () => {
      const query = `
        query GetUserPosts($userId: ID!, $first: Int!, $after: String) {
          user(id: $userId) {
            posts(first: $first, after: $after) {
              edges {
                node {
                  id
                  title
                  content
                  comments {
                    totalCount
                  }
                }
                cursor
              }
              pageInfo {
                hasNextPage
                endCursor
              }
            }
          }
        }
      `;

      const response = await request(app)
        .post('/graphql')
        .set('Authorization', `Bearer ${authToken}`)
        .send({
          query,
          variables: { userId: '123', first: 5 }
        })
        .expect(200);

      const posts = response.body.data.user.posts;
      expect(posts.edges).toHaveLength(5);
      expect(posts.pageInfo.hasNextPage).toBeDefined();
      posts.edges.forEach(edge => {
        expect(edge.node).toHaveProperty('id');
        expect(edge.node).toHaveProperty('title');
        expect(edge.cursor).toBeDefined();
      });
    });
  });
});
```

### Testing GraphQL Mutations

```javascript
describe('GraphQL Mutations', () => {
  it('should create a post', async () => {
    const mutation = `
      mutation CreatePost($input: CreatePostInput!) {
        createPost(input: $input) {
          id
          title
          content
          author {
            id
            name
          }
          publishedAt
        }
      }
    `;

    const response = await request(app)
      .post('/graphql')
      .set('Authorization', `Bearer ${authToken}`)
      .send({
        query: mutation,
        variables: {
          input: {
            title: 'Test Post',
            content: 'This is a test post content.',
            categoryId: '5'
          }
        }
      })
      .expect(200);

    expect(response.body.data.createPost).toBeDefined();
    expect(response.body.data.createPost.title).toBe('Test Post');
    expect(response.body.data.createPost.author.id).toBeDefined();
    expect(response.body.errors).toBeUndefined();
  });

  it('should handle validation errors in mutations', async () => {
    const mutation = `
      mutation CreatePost($input: CreatePostInput!) {
        createPost(input: $input) {
          id
          title
        }
      }
    `;

    const response = await request(app)
      .post('/graphql')
      .set('Authorization', `Bearer ${authToken}`)
      .send({
        query: mutation,
        variables: {
          input: {
            title: '',
            content: ''
          }
        }
      })
      .expect(200);

    expect(response.body.errors).toBeDefined();
    expect(response.body.errors[0].extensions.code).toBe('VALIDATION_ERROR');
  });
});
```

### GraphQL-Specific Testing Concerns

GraphQL introduces unique testing challenges:

**Query depth limiting**: Deeply nested queries can cause performance issues. Test that depth limits are enforced:

```javascript
it('should reject deeply nested queries', async () => {
  const deepQuery = `
    query {
      user(id: "1") {
        posts {
          edges {
            node {
              comments {
                edges {
                  node {
                    author {
                      posts {
                        edges {
                          node {
                            comments {
                              edges {
                                node {
                                  content
                                }
                              }
                            }
                          }
                        }
                      }
                    }
                  }
                }
              }
            }
          }
        }
      }
    }
  `;

  const response = await request(app)
    .post('/graphql')
    .send({ query: deepQuery })
    .expect(200);

  expect(response.body.errors).toBeDefined();
  expect(response.body.errors[0].message).toContain('depth');
});
```

**Query complexity analysis**: Test that the server rejects overly complex queries:

```javascript
it('should reject queries exceeding complexity limit', async () => {
  const complexQuery = `
    query {
      allUsers(first: 1000) {
        edges {
          node {
            posts(first: 100) {
              edges {
                node {
                  comments(first: 100) {
                    edges {
                      node { content }
                    }
                  }
                }
              }
            }
          }
        }
      }
    }
  `;

  const response = await request(app)
    .post('/graphql')
    .send({ query: complexQuery })
    .expect(200);

  expect(response.body.errors[0].message).toContain('complexity');
});
```

**Introspection control**: In production, introspection should typically be disabled:

```javascript
it('should disable introspection in production', async () => {
  const introspectionQuery = `
    query {
      __schema {
        types {
          name
        }
      }
    }
  `;

  const response = await request(app)
    .post('/graphql')
    .send({ query: introspectionQuery })
    .expect(200);

  expect(response.body.errors).toBeDefined();
});
```

---

## Postman and Newman Automation

### Building API Test Collections in Postman

Postman is the industry-standard tool for API development and testing. Collections organize requests into logical groups, and tests are written in JavaScript using the Postman sandbox.

**Setting up environment variables**:

```javascript
// Pre-request script for authentication
const loginUrl = pm.environment.get('base_url') + '/auth/login';

pm.sendRequest({
  url: loginUrl,
  method: 'POST',
  header: {
    'Content-Type': 'application/json'
  },
  body: {
    mode: 'raw',
    raw: JSON.stringify({
      email: pm.environment.get('test_email'),
      password: pm.environment.get('test_password')
    })
  }
}, (err, response) => {
  if (err) {
    console.error('Authentication failed:', err);
    return;
  }
  const token = response.json().access_token;
  pm.environment.set('auth_token', token);
});
```

**Writing test assertions in Postman**:

```javascript
// Tests tab for GET /api/users/:id
pm.test('Status code is 200', () => {
  pm.response.to.have.status(200);
});

pm.test('Response time is under 500ms', () => {
  pm.expect(pm.response.responseTime).to.be.below(500);
});

pm.test('Response has correct structure', () => {
  const jsonData = pm.response.json();
  pm.expect(jsonData).to.have.property('id');
  pm.expect(jsonData).to.have.property('name');
  pm.expect(jsonData).to.have.property('email');
  pm.expect(jsonData.id).to.be.a('number');
  pm.expect(jsonData.name).to.be.a('string');
  pm.expect(jsonData.email).to.match(/^[^\s@]+@[^\s@]+\.[^\s@]+$/);
});

pm.test('Response headers are correct', () => {
  pm.response.to.have.header('Content-Type', 'application/json; charset=utf-8');
  pm.response.to.have.header('X-Request-Id');
});

pm.test('No sensitive data exposed', () => {
  const jsonData = pm.response.json();
  pm.expect(jsonData).to.not.have.property('password');
  pm.expect(jsonData).to.not.have.property('password_hash');
  pm.expect(jsonData).to.not.have.property('ssn');
});

// Schema validation using tv4
const schema = {
  type: 'object',
  required: ['id', 'name', 'email', 'created_at'],
  properties: {
    id: { type: 'number' },
    name: { type: 'string', minLength: 1 },
    email: { type: 'string', format: 'email' },
    created_at: { type: 'string', format: 'date-time' },
    role: { type: 'string', enum: ['user', 'admin', 'moderator'] }
  },
  additionalProperties: false
};

pm.test('Response matches schema', () => {
  pm.response.to.have.jsonSchema(schema);
});
```

**Data-driven testing with CSV/JSON files**:

Create a CSV file `test-users.csv`:
```csv
name,email,role,expected_status
Valid User,valid@example.com,user,201
Admin User,admin@example.com,admin,201
,missing-name@example.com,user,400
No Email,,user,400
Invalid Role,role@example.com,superadmin,400
SQL Injection,'; DROP TABLE users;--,user,400
XSS Attack,<script>alert(1)</script>@test.com,user,400
```

```javascript
// Tests for data-driven request
pm.test(`Create user: ${pm.iterationData.get('name')} returns ${pm.iterationData.get('expected_status')}`, () => {
  pm.response.to.have.status(parseInt(pm.iterationData.get('expected_status')));
});
```

### Newman: CLI Collection Runner

Newman is the command-line companion to Postman that enables CI/CD integration.

**Installation and basic usage**:

```bash
# Install Newman globally
npm install -g newman

# Run a collection
newman run collection.json \
  --environment staging.json \
  --reporters cli,htmlextra \
  --reporter-htmlextra-export ./reports/api-test-report.html

# Run with data file for data-driven testing
newman run collection.json \
  --environment staging.json \
  --iteration-data test-users.csv \
  --iteration-count 50

# Run with specific folder
newman run collection.json \
  --folder "User Management" \
  --environment staging.json

# Run with delay between requests (rate limiting)
newman run collection.json \
  --delay-request 100 \
  --environment staging.json

# Run with bail (stop on first failure)
newman run collection.json \
  --bail \
  --environment staging.json
```

**Newman in CI/CD pipelines** (GitHub Actions):

```yaml
name: API Tests
on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  api-tests:
    runs-on: ubuntu-latest
    services:
      postgres:
        image: postgres:15
        env:
          POSTGRES_DB: testdb
          POSTGRES_USER: testuser
          POSTGRES_PASSWORD: testpass
        ports:
          - 5432:5432
        options: >-
          --health-cmd pg_isready
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5

    steps:
      - uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'

      - name: Install dependencies
        run: npm ci

      - name: Start application
        run: |
          npm start &
          sleep 10
        env:
          DATABASE_URL: postgresql://testuser:testpass@localhost:5432/testdb
          NODE_ENV: test

      - name: Install Newman
        run: npm install -g newman newman-reporter-htmlextra

      - name: Run API tests
        run: |
          newman run tests/api-collection.json \
            --environment tests/environments/ci.json \
            --reporters cli,htmlextra,junit \
            --reporter-htmlextra-export reports/api-report.html \
            --reporter-junit-export reports/api-results.xml

      - name: Upload test results
        if: always()
        uses: actions/upload-artifact@v4
        with:
          name: api-test-reports
          path: reports/

      - name: Publish test results
        if: always()
        uses: dorny/test-reporter@v1
        with:
          name: API Test Results
          path: reports/api-results.xml
          reporter: java-junit
```

**Programmatic Newman usage**:

```javascript
const newman = require('newman');

newman.run({
  collection: require('./collection.json'),
  environment: require('./environments/staging.json'),
  reporters: ['cli', 'htmlextra'],
  reporter: {
    htmlextra: {
      export: './reports/api-test-report.html',
      title: 'API Test Results',
      browserTitle: 'API Tests',
      showEnvironmentData: true,
      showGlobalData: false
    }
  },
  iterationCount: 1,
  bail: false,
  timeoutRequest: 10000
}, (err, summary) => {
  if (err) {
    console.error('Collection run encountered an error:', err);
    process.exit(1);
  }

  const { stats } = summary.run;
  console.log(`Tests: ${stats.tests.total}, Failed: ${stats.tests.failed}`);
  console.log(`Assertions: ${stats.assertions.total}, Failed: ${stats.assertions.failed}`);

  if (stats.assertions.failed > 0) {
    process.exit(1);
  }
});
```

---

## Contract Testing with Pact

### Why Contract Testing Matters

In microservices architectures, services are developed and deployed independently by different teams. This independence creates a challenge: how do you ensure that changes to a provider API don't break its consumers?

Traditional integration testing requires spinning up all dependent services simultaneously, which is slow, fragile, and expensive. Contract testing offers an alternative: each consumer defines a "contract" specifying what it expects from the provider, and the provider independently verifies it can fulfill those contracts.

Pact is the most popular contract testing framework. It supports the "consumer-driven contract" pattern where consumers define their expectations and providers verify them.

### Consumer-Side Testing

The consumer writes tests that define its expectations:

```javascript
// consumer/tests/userService.pact.test.js
const { PactV3, MatchersV3 } = require('@pact-foundation/pact');
const { like, eachLike, regex, integer, string, timestamp } = MatchersV3;
const { fetchUser, fetchUserOrders } = require('../src/userServiceClient');

const provider = new PactV3({
  consumer: 'OrderService',
  provider: 'UserService',
  logLevel: 'warn'
});

describe('User Service Contract', () => {
  describe('GET /api/users/:id', () => {
    it('returns a user when one exists', async () => {
      await provider
        .given('a user with ID 123 exists')
        .uponReceiving('a request for user 123')
        .withRequest({
          method: 'GET',
          path: '/api/users/123',
          headers: {
            Authorization: regex(/^Bearer .+$/, 'Bearer token123'),
            Accept: 'application/json'
          }
        })
        .willRespondWith({
          status: 200,
          headers: {
            'Content-Type': 'application/json'
          },
          body: {
            id: integer(123),
            name: string('Jane Doe'),
            email: regex(/^[^\s@]+@[^\s@]+\.[^\s@]+$/, 'jane@example.com'),
            role: regex(/^(user|admin|moderator)$/, 'admin'),
            created_at: timestamp("yyyy-MM-dd'T'HH:mm:ss'Z'", '2024-01-15T10:30:00Z')
          }
        })
        .executeTest(async (mockServer) => {
          const user = await fetchUser(mockServer.url, 123);
          expect(user.id).toBe(123);
          expect(user.name).toBeDefined();
          expect(user.email).toBeDefined();
        });
    });

    it('returns 404 when user does not exist', async () => {
      await provider
        .given('no user with ID 999 exists')
        .uponReceiving('a request for non-existent user')
        .withRequest({
          method: 'GET',
          path: '/api/users/999',
          headers: {
            Authorization: regex(/^Bearer .+$/, 'Bearer token123')
          }
        })
        .willRespondWith({
          status: 404,
          body: {
            error: string('User not found')
          }
        })
        .executeTest(async (mockServer) => {
          await expect(fetchUser(mockServer.url, 999))
            .rejects.toThrow('User not found');
        });
    });
  });

  describe('GET /api/users/:id/orders', () => {
    it('returns orders for a user', async () => {
      await provider
        .given('user 123 has orders')
        .uponReceiving('a request for user orders')
        .withRequest({
          method: 'GET',
          path: '/api/users/123/orders',
          query: { status: 'completed', limit: '10' },
          headers: {
            Authorization: regex(/^Bearer .+$/, 'Bearer token123')
          }
        })
        .willRespondWith({
          status: 200,
          body: {
            data: eachLike({
              id: integer(1),
              total: like(99.99),
              status: string('completed'),
              items: eachLike({
                product_id: integer(1),
                quantity: integer(2),
                price: like(49.99)
              })
            }),
            meta: {
              total: integer(25),
              page: integer(1)
            }
          }
        })
        .executeTest(async (mockServer) => {
          const result = await fetchUserOrders(mockServer.url, 123, {
            status: 'completed',
            limit: 10
          });
          expect(result.data).toBeInstanceOf(Array);
          expect(result.data.length).toBeGreaterThan(0);
        });
    });
  });
});
```

### Provider-Side Verification

The provider verifies it can fulfill all consumer contracts:

```javascript
// provider/tests/pact.verify.test.js
const { Verifier } = require('@pact-foundation/pact');
const app = require('../src/app');

describe('Pact Provider Verification', () => {
  let server;

  beforeAll(async () => {
    server = app.listen(3001);
    // Seed test data
    await seedDatabase();
  });

  afterAll(async () => {
    server.close();
    await cleanDatabase();
  });

  it('validates all consumer contracts', async () => {
    const verifier = new Verifier({
      providerBaseUrl: 'http://localhost:3001',
      pactUrls: [
        './pacts/orderservice-userservice.json'
      ],
      // Or from a Pact Broker:
      // pactBrokerUrl: 'https://pact-broker.example.com',
      // provider: 'UserService',
      // providerVersion: process.env.GIT_SHA,
      // publishVerificationResult: process.env.CI === 'true',

      stateHandlers: {
        'a user with ID 123 exists': async () => {
          await db.query(`
            INSERT INTO users (id, name, email, role, created_at)
            VALUES (123, 'Jane Doe', 'jane@example.com', 'admin', '2024-01-15T10:30:00Z')
            ON CONFLICT (id) DO NOTHING
          `);
        },
        'no user with ID 999 exists': async () => {
          await db.query('DELETE FROM users WHERE id = 999');
        },
        'user 123 has orders': async () => {
          await db.query(`
            INSERT INTO orders (id, user_id, total, status)
            VALUES (1, 123, 99.99, 'completed')
            ON CONFLICT (id) DO NOTHING
          `);
          await db.query(`
            INSERT INTO order_items (id, order_id, product_id, quantity, price)
            VALUES (1, 1, 1, 2, 49.99)
            ON CONFLICT (id) DO NOTHING
          `);
        }
      }
    });

    await verifier.verifyProvider();
  });
});
```

### Pact Broker Integration

The Pact Broker manages contracts between consumers and providers:

```bash
# Publish consumer pacts to broker
pact-broker publish ./pacts \
  --consumer-app-version $(git rev-parse HEAD) \
  --broker-base-url https://pact-broker.example.com \
  --broker-token $PACT_BROKER_TOKEN \
  --tag $(git branch --show-current)

# Can I deploy? Check if all contracts are verified
pact-broker can-i-deploy \
  --pacticipant OrderService \
  --version $(git rev-parse HEAD) \
  --to production \
  --broker-base-url https://pact-broker.example.com \
  --broker-token $PACT_BROKER_TOKEN
```

---

## Schema Validation

### JSON Schema Validation

JSON Schema provides a declarative way to validate API response structures. It is invaluable for ensuring API responses conform to documented specifications.

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "$id": "https://api.example.com/schemas/user.json",
  "title": "User",
  "description": "A user in the system",
  "type": "object",
  "required": ["id", "name", "email", "created_at", "role"],
  "properties": {
    "id": {
      "type": "integer",
      "minimum": 1,
      "description": "Unique user identifier"
    },
    "name": {
      "type": "string",
      "minLength": 1,
      "maxLength": 255,
      "description": "Full name of the user"
    },
    "email": {
      "type": "string",
      "format": "email",
      "description": "Email address"
    },
    "role": {
      "type": "string",
      "enum": ["user", "admin", "moderator"],
      "description": "User role in the system"
    },
    "created_at": {
      "type": "string",
      "format": "date-time",
      "description": "Account creation timestamp"
    },
    "avatar_url": {
      "type": ["string", "null"],
      "format": "uri",
      "description": "URL to user avatar image"
    },
    "preferences": {
      "type": "object",
      "properties": {
        "theme": {
          "type": "string",
          "enum": ["light", "dark", "auto"]
        },
        "language": {
          "type": "string",
          "pattern": "^[a-z]{2}(-[A-Z]{2})?$"
        },
        "notifications": {
          "type": "object",
          "properties": {
            "email": { "type": "boolean" },
            "push": { "type": "boolean" },
            "sms": { "type": "boolean" }
          },
          "required": ["email", "push"]
        }
      }
    }
  },
  "additionalProperties": false
}
```

**Implementing schema validation in tests**:

```javascript
const Ajv = require('ajv');
const addFormats = require('ajv-formats');
const userSchema = require('./schemas/user.json');
const orderSchema = require('./schemas/order.json');

const ajv = new Ajv({ allErrors: true, strict: false });
addFormats(ajv);

const validateUser = ajv.compile(userSchema);
const validateOrder = ajv.compile(orderSchema);

describe('Schema Validation', () => {
  it('GET /api/users/:id response matches user schema', async () => {
    const response = await request(app)
      .get('/api/users/123')
      .set('Authorization', `Bearer ${authToken}`)
      .expect(200);

    const valid = validateUser(response.body);
    if (!valid) {
      console.error('Schema validation errors:', validateUser.errors);
    }
    expect(valid).toBe(true);
  });

  it('GET /api/users returns array of valid users', async () => {
    const response = await request(app)
      .get('/api/users?limit=10')
      .set('Authorization', `Bearer ${authToken}`)
      .expect(200);

    response.body.data.forEach((user, index) => {
      const valid = validateUser(user);
      if (!valid) {
        console.error(`User ${index} failed validation:`, validateUser.errors);
      }
      expect(valid).toBe(true);
    });
  });
});
```

### OpenAPI (Swagger) Specification Validation

OpenAPI specifications serve as the single source of truth for API behavior. Testing against the spec ensures implementation matches documentation:

```javascript
const OpenApiValidator = require('express-openapi-validator');
const SwaggerParser = require('@apidevtools/swagger-parser');

// Validate the spec itself
describe('OpenAPI Specification', () => {
  it('should be a valid OpenAPI 3.0 document', async () => {
    const api = await SwaggerParser.validate('./openapi.yaml');
    expect(api.openapi).toMatch(/^3\./);
    expect(api.info.title).toBeDefined();
    expect(api.paths).toBeDefined();
  });
});

// Use as middleware for runtime validation
const validator = OpenApiValidator.middleware({
  apiSpec: './openapi.yaml',
  validateRequests: true,
  validateResponses: true,
  validateSecurity: true
});

// In tests, validate responses against spec
const { OpenApiResponseValidator } = require('openapi-response-validator');
const spec = require('./openapi.json');

function validateResponseAgainstSpec(path, method, statusCode, body) {
  const pathSpec = spec.paths[path][method.toLowerCase()];
  const responseSpec = pathSpec.responses[statusCode.toString()];

  if (!responseSpec) {
    throw new Error(`No spec found for ${method} ${path} ${statusCode}`);
  }

  const validator = new OpenApiResponseValidator({
    responses: pathSpec.responses,
    components: spec.components
  });

  const errors = validator.validateResponse(statusCode, body);
  return errors;
}

describe('Response Spec Compliance', () => {
  it('GET /api/users/123 matches OpenAPI spec', async () => {
    const response = await request(app)
      .get('/api/users/123')
      .set('Authorization', `Bearer ${authToken}`);

    const errors = validateResponseAgainstSpec(
      '/api/users/{id}', 'GET', response.status, response.body
    );

    expect(errors).toBeUndefined();
  });
});
```

---

## API Security Testing

### Authentication and Authorization Testing

API security testing verifies that authentication and authorization mechanisms work correctly and cannot be bypassed.

**Authentication testing scenarios**:

```javascript
describe('Authentication Security', () => {
  it('should reject requests without authentication', async () => {
    await request(app)
      .get('/api/users/123')
      .expect(401);
  });

  it('should reject expired tokens', async () => {
    const expiredToken = generateToken({ userId: 123, exp: Math.floor(Date.now() / 1000) - 3600 });
    await request(app)
      .get('/api/users/123')
      .set('Authorization', `Bearer ${expiredToken}`)
      .expect(401);
  });

  it('should reject tampered tokens', async () => {
    const validToken = generateToken({ userId: 123 });
    const tamperedToken = validToken.slice(0, -5) + 'XXXXX';
    await request(app)
      .get('/api/users/123')
      .set('Authorization', `Bearer ${tamperedToken}`)
      .expect(401);
  });

  it('should reject tokens signed with wrong key', async () => {
    const wrongKeyToken = jwt.sign({ userId: 123 }, 'wrong-secret-key');
    await request(app)
      .get('/api/users/123')
      .set('Authorization', `Bearer ${wrongKeyToken}`)
      .expect(401);
  });

  it('should handle token with modified claims (privilege escalation)', async () => {
    // User token trying to access admin endpoint
    const userToken = generateToken({ userId: 456, role: 'user' });
    await request(app)
      .get('/api/admin/users')
      .set('Authorization', `Bearer ${userToken}`)
      .expect(403);
  });

  it('should prevent IDOR (Insecure Direct Object Reference)', async () => {
    // User A trying to access User B's data
    const userAToken = generateToken({ userId: 100 });
    await request(app)
      .get('/api/users/200/private-data')
      .set('Authorization', `Bearer ${userAToken}`)
      .expect(403);
  });

  it('should enforce rate limiting', async () => {
    const requests = Array(110).fill(null).map(() =>
      request(app)
        .get('/api/users/123')
        .set('Authorization', `Bearer ${authToken}`)
    );

    const responses = await Promise.all(requests);
    const rateLimited = responses.filter(r => r.status === 429);
    expect(rateLimited.length).toBeGreaterThan(0);
  });
});
```

### Input Validation and Injection Testing

```javascript
describe('Input Validation Security', () => {
  const injectionPayloads = [
    { name: 'SQL Injection (basic)', value: "'; DROP TABLE users; --" },
    { name: 'SQL Injection (union)', value: "' UNION SELECT * FROM passwords --" },
    { name: 'SQL Injection (blind)', value: "' OR '1'='1" },
    { name: 'XSS (script tag)', value: '<script>alert("xss")</script>' },
    { name: 'XSS (event handler)', value: '<img src=x onerror=alert(1)>' },
    { name: 'XSS (javascript URI)', value: 'javascript:alert(1)' },
    { name: 'Command Injection', value: '; cat /etc/passwd' },
    { name: 'Path Traversal', value: '../../../etc/passwd' },
    { name: 'LDAP Injection', value: '*)(uid=*))(|(uid=*' },
    { name: 'NoSQL Injection', value: '{"$gt": ""}' },
    { name: 'Template Injection', value: '{{7*7}}' },
    { name: 'Header Injection', value: 'value\r\nX-Injected: true' }
  ];

  injectionPayloads.forEach(({ name, value }) => {
    it(`should handle ${name} in request body`, async () => {
      const response = await request(app)
        .post('/api/users')
        .set('Authorization', `Bearer ${adminToken}`)
        .send({
          name: value,
          email: 'test@example.com',
          password: 'SecureP@ss123'
        });

      // Should either reject (400) or sanitize — never execute
      expect(response.status).not.toBe(500);
      if (response.status === 201) {
        // If accepted, verify the value was sanitized
        expect(response.body.name).not.toContain('<script>');
        expect(response.body.name).not.toContain('DROP TABLE');
      }
    });

    it(`should handle ${name} in query parameters`, async () => {
      const response = await request(app)
        .get(`/api/users?search=${encodeURIComponent(value)}`)
        .set('Authorization', `Bearer ${authToken}`);

      expect(response.status).not.toBe(500);
    });

    it(`should handle ${name} in URL path`, async () => {
      const response = await request(app)
        .get(`/api/users/${encodeURIComponent(value)}`)
        .set('Authorization', `Bearer ${authToken}`);

      expect([400, 404]).toContain(response.status);
    });
  });
});
```

### CORS and Security Header Testing

```javascript
describe('Security Headers', () => {
  it('should include security headers', async () => {
    const response = await request(app)
      .get('/api/health')
      .expect(200);

    expect(response.headers['x-content-type-options']).toBe('nosniff');
    expect(response.headers['x-frame-options']).toBe('DENY');
    expect(response.headers['strict-transport-security']).toMatch(/max-age=\d+/);
    expect(response.headers['x-xss-protection']).toBe('0');
    expect(response.headers['content-security-policy']).toBeDefined();
  });

  it('should handle CORS correctly', async () => {
    // Allowed origin
    const allowedResponse = await request(app)
      .options('/api/users')
      .set('Origin', 'https://app.example.com')
      .set('Access-Control-Request-Method', 'GET')
      .expect(204);

    expect(allowedResponse.headers['access-control-allow-origin']).toBe('https://app.example.com');
    expect(allowedResponse.headers['access-control-allow-methods']).toContain('GET');

    // Disallowed origin
    const disallowedResponse = await request(app)
      .options('/api/users')
      .set('Origin', 'https://evil.com')
      .set('Access-Control-Request-Method', 'GET');

    expect(disallowedResponse.headers['access-control-allow-origin']).toBeUndefined();
  });

  it('should not expose server information', async () => {
    const response = await request(app).get('/api/health');
    expect(response.headers['server']).toBeUndefined();
    expect(response.headers['x-powered-by']).toBeUndefined();
  });
});
```

---

## Performance Testing APIs with k6 and JMeter

### k6 for API Load Testing

k6 is a modern, developer-friendly load testing tool that uses JavaScript for test scripts.

**Installation**:

```bash
# macOS
brew install k6

# Docker
docker run --rm -i grafana/k6 run - <script.js

# Linux
sudo gpg -k
sudo gpg --no-default-keyring --keyring /usr/share/keyrings/k6-archive-keyring.gpg \
  --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys C5AD17C747E3415A3642D57D77C6C491D6AC1D68
echo "deb [signed-by=/usr/share/keyrings/k6-archive-keyring.gpg] https://dl.k6.io/deb stable main" | \
  sudo tee /etc/apt/sources.list.d/k6.list
sudo apt-get update && sudo apt-get install k6
```

**Basic API load test**:

```javascript
// k6-api-test.js
import http from 'k6/http';
import { check, sleep, group } from 'k6';
import { Rate, Trend, Counter } from 'k6/metrics';

// Custom metrics
const errorRate = new Rate('errors');
const userCreationDuration = new Trend('user_creation_duration');
const successfulLogins = new Counter('successful_logins');

// Test configuration
export const options = {
  stages: [
    { duration: '1m', target: 10 },   // Ramp up to 10 users
    { duration: '3m', target: 50 },   // Ramp up to 50 users
    { duration: '5m', target: 50 },   // Stay at 50 users
    { duration: '2m', target: 100 },  // Ramp up to 100 users
    { duration: '3m', target: 100 },  // Stay at 100 users
    { duration: '2m', target: 0 },    // Ramp down
  ],
  thresholds: {
    http_req_duration: ['p(95)<500', 'p(99)<1000'],
    http_req_failed: ['rate<0.01'],
    errors: ['rate<0.05'],
    user_creation_duration: ['p(95)<1000'],
  },
};

const BASE_URL = __ENV.BASE_URL || 'https://api.staging.example.com';

// Setup: runs once before the test
export function setup() {
  const loginRes = http.post(`${BASE_URL}/auth/login`, JSON.stringify({
    email: 'loadtest@example.com',
    password: 'LoadTest123!'
  }), {
    headers: { 'Content-Type': 'application/json' }
  });

  const token = loginRes.json('access_token');
  return { token };
}

// Main test function: runs for each virtual user
export default function(data) {
  const headers = {
    'Content-Type': 'application/json',
    'Authorization': `Bearer ${data.token}`
  };

  group('User API', () => {
    // GET user list
    const listRes = http.get(`${BASE_URL}/api/users?limit=20`, { headers });
    check(listRes, {
      'list status is 200': (r) => r.status === 200,
      'list has data': (r) => r.json('data').length > 0,
      'list response time < 300ms': (r) => r.timings.duration < 300,
    });
    errorRate.add(listRes.status !== 200);

    sleep(1);

    // GET single user
    const userId = listRes.json('data.0.id');
    if (userId) {
      const userRes = http.get(`${BASE_URL}/api/users/${userId}`, { headers });
      check(userRes, {
        'user status is 200': (r) => r.status === 200,
        'user has id': (r) => r.json('id') === userId,
        'user response time < 200ms': (r) => r.timings.duration < 200,
      });
      errorRate.add(userRes.status !== 200);
    }

    sleep(0.5);

    // POST create user
    const timestamp = Date.now();
    const createStart = Date.now();
    const createRes = http.post(`${BASE_URL}/api/users`, JSON.stringify({
      name: `Load Test User ${timestamp}`,
      email: `loadtest-${timestamp}-${__VU}@example.com`,
      password: 'TestP@ss123',
      role: 'user'
    }), { headers });

    userCreationDuration.add(Date.now() - createStart);

    check(createRes, {
      'create status is 201': (r) => r.status === 201,
      'create returns id': (r) => r.json('id') !== undefined,
    });
    errorRate.add(createRes.status !== 201);

    sleep(1);
  });

  group('Search API', () => {
    const searchRes = http.get(`${BASE_URL}/api/users?search=test&sort=name&order=asc`, { headers });
    check(searchRes, {
      'search status is 200': (r) => r.status === 200,
      'search response time < 500ms': (r) => r.timings.duration < 500,
    });
    errorRate.add(searchRes.status !== 200);

    sleep(0.5);
  });
}

// Teardown: runs once after the test
export function teardown(data) {
  // Clean up test data
  http.del(`${BASE_URL}/api/test/cleanup`, null, {
    headers: { 'Authorization': `Bearer ${data.token}` }
  });
}
```

**Running k6 tests**:

```bash
# Basic run
k6 run k6-api-test.js

# With environment variables
k6 run -e BASE_URL=https://api.staging.example.com k6-api-test.js

# Output to JSON for analysis
k6 run --out json=results.json k6-api-test.js

# Output to InfluxDB for Grafana dashboards
k6 run --out influxdb=http://localhost:8086/k6 k6-api-test.js

# Cloud execution
k6 cloud k6-api-test.js
```

### JMeter for Complex API Testing

Apache JMeter supports complex test scenarios with its GUI and XML-based test plans. While typically configured via GUI, test plans can be managed as code:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<jmeterTestPlan version="1.2">
  <hashTree>
    <TestPlan guiclass="TestPlanGui" testclass="TestPlan" testname="API Load Test">
      <elementProp name="TestPlan.user_defined_variables" elementType="Arguments">
        <collectionProp name="Arguments.arguments">
          <elementProp name="BASE_URL" elementType="Argument">
            <stringProp name="Argument.name">BASE_URL</stringProp>
            <stringProp name="Argument.value">${__P(base_url,https://api.staging.example.com)}</stringProp>
          </elementProp>
        </collectionProp>
      </elementProp>
    </TestPlan>
    <hashTree>
      <ThreadGroup guiclass="ThreadGroupGui" testclass="ThreadGroup" testname="API Users">
        <intProp name="ThreadGroup.num_threads">50</intProp>
        <intProp name="ThreadGroup.ramp_time">60</intProp>
        <longProp name="ThreadGroup.duration">300</longProp>
        <boolProp name="ThreadGroup.scheduler">true</boolProp>
      </ThreadGroup>
      <hashTree>
        <HTTPSamplerProxy guiclass="HttpTestSampleGui" testclass="HTTPSamplerProxy" testname="Get Users">
          <stringProp name="HTTPSampler.domain">${BASE_URL}</stringProp>
          <stringProp name="HTTPSampler.path">/api/users</stringProp>
          <stringProp name="HTTPSampler.method">GET</stringProp>
        </HTTPSamplerProxy>
      </hashTree>
    </hashTree>
  </hashTree>
</jmeterTestPlan>
```

**Running JMeter from command line**:

```bash
# Non-GUI mode (recommended for actual tests)
jmeter -n -t api-test-plan.jmx \
  -l results.jtl \
  -e -o reports/ \
  -Jbase_url=https://api.staging.example.com \
  -Jthreads=100 \
  -Jramp_up=60 \
  -Jduration=300

# Generate HTML report from results
jmeter -g results.jtl -o reports/
```

---

## API Mocking and Service Virtualization

### Why Mock APIs?

API mocking and service virtualization are essential for testing in isolation. Common scenarios include:

- Third-party APIs with rate limits or costs (payment gateways, SMS providers)
- APIs that aren't yet built (parallel development)
- Simulating error conditions that are hard to reproduce (500 errors, timeouts)
- Testing without network dependencies (offline development)
- Creating deterministic test environments

### WireMock for Service Virtualization

WireMock is a powerful HTTP mock server that can simulate API behaviors:

```bash
# Run WireMock standalone
java -jar wiremock-standalone-3.3.1.jar --port 8080 --verbose
```

**Defining stubs via JSON mappings**:

```json
// mappings/get-user-123.json
{
  "request": {
    "method": "GET",
    "urlPathPattern": "/api/users/[0-9]+",
    "headers": {
      "Authorization": {
        "matches": "Bearer .+"
      }
    }
  },
  "response": {
    "status": 200,
    "headers": {
      "Content-Type": "application/json"
    },
    "jsonBody": {
      "id": 123,
      "name": "Jane Doe",
      "email": "jane@example.com",
      "role": "admin"
    }
  }
}
```

```json
// mappings/create-user.json
{
  "request": {
    "method": "POST",
    "url": "/api/users",
    "headers": {
      "Content-Type": {
        "equalTo": "application/json"
      }
    },
    "bodyPatterns": [
      {
        "matchesJsonPath": "$.name"
      },
      {
        "matchesJsonPath": "$.email"
      }
    ]
  },
  "response": {
    "status": 201,
    "headers": {
      "Content-Type": "application/json",
      "Location": "/api/users/{{randomValue type='UUID'}}"
    },
    "jsonBody": {
      "id": "{{randomValue type='UUID'}}",
      "name": "{{jsonPath request.body '$.name'}}",
      "email": "{{jsonPath request.body '$.email'}}",
      "created_at": "{{now}}"
    },
    "transformers": ["response-template"]
  }
}
```

**Simulating failures and delays**:

```json
// mappings/slow-response.json
{
  "request": {
    "method": "GET",
    "url": "/api/slow-endpoint"
  },
  "response": {
    "status": 200,
    "fixedDelayMilliseconds": 5000,
    "jsonBody": {
      "message": "This took a while"
    }
  }
}
```

```json
// mappings/intermittent-failure.json
{
  "request": {
    "method": "GET",
    "url": "/api/flaky-endpoint"
  },
  "response": {
    "fault": "RANDOM_DATA_THEN_CLOSE"
  },
  "serveEventListeners": [],
  "scenarioName": "flaky",
  "requiredScenarioState": "Started",
  "newScenarioState": "Recovered"
}
```

### MSW (Mock Service Worker) for Frontend Testing

MSW intercepts network requests at the service worker level, making it ideal for frontend API testing:

```javascript
// mocks/handlers.js
import { rest } from 'msw';

export const handlers = [
  rest.get('/api/users/:id', (req, res, ctx) => {
    const { id } = req.params;

    if (id === '999') {
      return res(
        ctx.status(404),
        ctx.json({ error: 'User not found' })
      );
    }

    return res(
      ctx.status(200),
      ctx.json({
        id: parseInt(id),
        name: 'Jane Doe',
        email: 'jane@example.com',
        role: 'admin'
      })
    );
  }),

  rest.post('/api/users', async (req, res, ctx) => {
    const body = await req.json();

    if (!body.email) {
      return res(
        ctx.status(400),
        ctx.json({
          errors: [{ field: 'email', message: 'Email is required' }]
        })
      );
    }

    return res(
      ctx.status(201),
      ctx.json({
        id: Math.floor(Math.random() * 1000),
        ...body,
        created_at: new Date().toISOString()
      })
    );
  }),

  // Simulate network error
  rest.get('/api/unreachable', (req, res) => {
    return res.networkError('Connection refused');
  }),

  // Simulate slow response
  rest.get('/api/slow', async (req, res, ctx) => {
    await new Promise(resolve => setTimeout(resolve, 5000));
    return res(ctx.json({ data: 'finally' }));
  })
];
```

```javascript
// mocks/server.js (for Node.js/test environment)
import { setupServer } from 'msw/node';
import { handlers } from './handlers';

export const server = setupServer(...handlers);
```

```javascript
// test setup
import { server } from './mocks/server';

beforeAll(() => server.listen({ onUnhandledRequest: 'error' }));
afterEach(() => server.resetHandlers());
afterAll(() => server.close());

describe('UserProfile component', () => {
  it('displays user data', async () => {
    render(<UserProfile userId={123} />);
    expect(await screen.findByText('Jane Doe')).toBeInTheDocument();
    expect(screen.getByText('jane@example.com')).toBeInTheDocument();
  });

  it('handles server error', async () => {
    server.use(
      rest.get('/api/users/:id', (req, res, ctx) => {
        return res(ctx.status(500), ctx.json({ error: 'Internal server error' }));
      })
    );

    render(<UserProfile userId={123} />);
    expect(await screen.findByText('Something went wrong')).toBeInTheDocument();
  });
});
```

### Nock for Node.js HTTP Mocking

Nock intercepts HTTP requests at the Node.js level:

```javascript
const nock = require('nock');

describe('External API Integration', () => {
  afterEach(() => {
    nock.cleanAll();
  });

  it('should handle payment processing', async () => {
    // Mock Stripe API
    const stripeScope = nock('https://api.stripe.com')
      .post('/v1/charges')
      .reply(200, {
        id: 'ch_test_123',
        amount: 2000,
        currency: 'usd',
        status: 'succeeded'
      });

    const result = await processPayment({
      amount: 2000,
      currency: 'usd',
      source: 'tok_test'
    });

    expect(result.status).toBe('succeeded');
    expect(stripeScope.isDone()).toBe(true);
  });

  it('should retry on transient failures', async () => {
    nock('https://api.stripe.com')
      .post('/v1/charges')
      .reply(503, { error: 'Service unavailable' })
      .post('/v1/charges')
      .reply(503, { error: 'Service unavailable' })
      .post('/v1/charges')
      .reply(200, {
        id: 'ch_test_456',
        status: 'succeeded'
      });

    const result = await processPayment({
      amount: 2000,
      currency: 'usd',
      source: 'tok_test'
    });

    expect(result.status).toBe('succeeded');
  });

  it('should handle timeout', async () => {
    nock('https://api.stripe.com')
      .post('/v1/charges')
      .delayConnection(10000)
      .reply(200, {});

    await expect(processPayment({
      amount: 2000,
      currency: 'usd',
      source: 'tok_test'
    })).rejects.toThrow('timeout');
  });
});
```

---

## Advanced API Testing Patterns

### Chained Request Testing

Many API workflows require chaining multiple requests together, where the output of one request feeds into the next:

```javascript
describe('E-commerce Order Workflow', () => {
  let authToken, userId, productId, cartId, orderId;

  it('Step 1: Register a new user', async () => {
    const response = await request(app)
      .post('/api/auth/register')
      .send({
        name: 'E2E Test User',
        email: `e2e-${Date.now()}@example.com`,
        password: 'SecureP@ss123'
      })
      .expect(201);

    userId = response.body.id;
    authToken = response.body.token;
    expect(userId).toBeDefined();
  });

  it('Step 2: Browse products', async () => {
    const response = await request(app)
      .get('/api/products?category=electronics&limit=5')
      .set('Authorization', `Bearer ${authToken}`)
      .expect(200);

    expect(response.body.data.length).toBeGreaterThan(0);
    productId = response.body.data[0].id;
  });

  it('Step 3: Add product to cart', async () => {
    const response = await request(app)
      .post('/api/cart/items')
      .set('Authorization', `Bearer ${authToken}`)
      .send({
        product_id: productId,
        quantity: 2
      })
      .expect(201);

    cartId = response.body.cart_id;
    expect(response.body.items).toHaveLength(1);
    expect(response.body.total).toBeGreaterThan(0);
  });

  it('Step 4: Apply discount code', async () => {
    const response = await request(app)
      .post(`/api/cart/${cartId}/discount`)
      .set('Authorization', `Bearer ${authToken}`)
      .send({ code: 'SAVE10' })
      .expect(200);

    expect(response.body.discount_applied).toBe(true);
    expect(response.body.discount_amount).toBeGreaterThan(0);
  });

  it('Step 5: Create order', async () => {
    const response = await request(app)
      .post('/api/orders')
      .set('Authorization', `Bearer ${authToken}`)
      .send({
        cart_id: cartId,
        shipping_address: {
          street: '123 Test St',
          city: 'Test City',
          state: 'TS',
          zip: '12345',
          country: 'US'
        },
        payment_method: 'credit_card',
        payment_token: 'tok_test_visa'
      })
      .expect(201);

    orderId = response.body.id;
    expect(response.body.status).toBe('pending');
    expect(response.body.total).toBeGreaterThan(0);
  });

  it('Step 6: Verify order status', async () => {
    const response = await request(app)
      .get(`/api/orders/${orderId}`)
      .set('Authorization', `Bearer ${authToken}`)
      .expect(200);

    expect(response.body.id).toBe(orderId);
    expect(response.body.status).toBe('confirmed');
    expect(response.body.items).toHaveLength(1);
    expect(response.body.shipping_address.city).toBe('Test City');
  });

  it('Step 7: Verify cart is cleared', async () => {
    const response = await request(app)
      .get(`/api/cart`)
      .set('Authorization', `Bearer ${authToken}`)
      .expect(200);

    expect(response.body.items).toHaveLength(0);
  });
});
```

### Idempotency Testing

APIs should handle duplicate requests gracefully:

```javascript
describe('Idempotency', () => {
  it('should handle duplicate POST requests with idempotency key', async () => {
    const idempotencyKey = `idem-${Date.now()}`;
    const payload = {
      amount: 5000,
      currency: 'usd',
      recipient: 'user_123'
    };

    // First request
    const response1 = await request(app)
      .post('/api/payments')
      .set('Authorization', `Bearer ${authToken}`)
      .set('Idempotency-Key', idempotencyKey)
      .send(payload)
      .expect(201);

    // Duplicate request with same idempotency key
    const response2 = await request(app)
      .post('/api/payments')
      .set('Authorization', `Bearer ${authToken}`)
      .set('Idempotency-Key', idempotencyKey)
      .send(payload)
      .expect(200); // Returns existing, not 201

    expect(response1.body.id).toBe(response2.body.id);
    expect(response2.headers['x-idempotent-replayed']).toBe('true');
  });

  it('GET requests should be naturally idempotent', async () => {
    const response1 = await request(app)
      .get('/api/users/123')
      .set('Authorization', `Bearer ${authToken}`)
      .expect(200);

    const response2 = await request(app)
      .get('/api/users/123')
      .set('Authorization', `Bearer ${authToken}`)
      .expect(200);

    expect(response1.body).toEqual(response2.body);
  });

  it('DELETE should be idempotent', async () => {
    // First delete
    await request(app)
      .delete('/api/temp-resources/456')
      .set('Authorization', `Bearer ${authToken}`)
      .expect(204);

    // Second delete of same resource
    await request(app)
      .delete('/api/temp-resources/456')
      .set('Authorization', `Bearer ${authToken}`)
      .expect(204); // Should not return 404
  });
});
```

### Concurrency Testing

Testing how APIs handle concurrent requests:

```javascript
describe('Concurrency', () => {
  it('should handle concurrent updates without data corruption', async () => {
    // Set initial balance
    await request(app)
      .put('/api/accounts/123')
      .set('Authorization', `Bearer ${authToken}`)
      .send({ balance: 1000 })
      .expect(200);

    // 10 concurrent withdrawals of 100 each
    const withdrawals = Array(10).fill(null).map(() =>
      request(app)
        .post('/api/accounts/123/withdraw')
        .set('Authorization', `Bearer ${authToken}`)
        .send({ amount: 100 })
    );

    const results = await Promise.all(withdrawals);

    // Check final balance
    const finalBalance = await request(app)
      .get('/api/accounts/123')
      .set('Authorization', `Bearer ${authToken}`)
      .expect(200);

    // Balance should be exactly 0 (not negative due to race conditions)
    expect(finalBalance.body.balance).toBe(0);

    // All successful withdrawals should total 1000
    const successfulWithdrawals = results.filter(r => r.status === 200);
    const totalWithdrawn = successfulWithdrawals.reduce(
      (sum, r) => sum + r.body.amount, 0
    );
    expect(totalWithdrawn).toBe(1000);
  });

  it('should maintain inventory consistency under concurrent orders', async () => {
    // Set product stock to 5
    await request(app)
      .put('/api/products/789/stock')
      .set('Authorization', `Bearer ${adminToken}`)
      .send({ quantity: 5 })
      .expect(200);

    // 10 concurrent purchase attempts
    const purchases = Array(10).fill(null).map((_, i) =>
      request(app)
        .post('/api/orders')
        .set('Authorization', `Bearer ${authToken}`)
        .send({
          items: [{ product_id: 789, quantity: 1 }],
          payment_token: `tok_test_${i}`
        })
    );

    const results = await Promise.all(purchases);
    const successful = results.filter(r => r.status === 201);
    const outOfStock = results.filter(r => r.status === 409);

    expect(successful).toHaveLength(5);
    expect(outOfStock).toHaveLength(5);
  });
});
```

### Webhook Testing

Testing webhook delivery and processing:

```javascript
const express = require('express');

describe('Webhook Integration', () => {
  let webhookServer;
  let receivedPayloads = [];

  beforeAll(async () => {
    // Start a local webhook receiver
    const webhookApp = express();
    webhookApp.use(express.json());
    webhookApp.post('/webhook', (req, res) => {
      receivedPayloads.push({
        headers: req.headers,
        body: req.body
      });
      res.status(200).json({ received: true });
    });
    webhookServer = webhookApp.listen(9999);
  });

  afterAll(() => {
    webhookServer.close();
  });

  beforeEach(() => {
    receivedPayloads = [];
  });

  it('should deliver webhook on order completion', async () => {
    // Register webhook
    await request(app)
      .post('/api/webhooks')
      .set('Authorization', `Bearer ${authToken}`)
      .send({
        url: 'http://localhost:9999/webhook',
        events: ['order.completed'],
        secret: 'webhook_secret_123'
      })
      .expect(201);

    // Create and complete an order
    const orderRes = await request(app)
      .post('/api/orders')
      .set('Authorization', `Bearer ${authToken}`)
      .send({
        items: [{ product_id: 1, quantity: 1 }],
        payment_token: 'tok_test'
      })
      .expect(201);

    // Wait for webhook delivery
    await new Promise(resolve => setTimeout(resolve, 2000));

    expect(receivedPayloads).toHaveLength(1);
    expect(receivedPayloads[0].body.event).toBe('order.completed');
    expect(receivedPayloads[0].body.data.order_id).toBe(orderRes.body.id);

    // Verify webhook signature
    const signature = receivedPayloads[0].headers['x-webhook-signature'];
    expect(signature).toBeDefined();

    const crypto = require('crypto');
    const expectedSignature = crypto
      .createHmac('sha256', 'webhook_secret_123')
      .update(JSON.stringify(receivedPayloads[0].body))
      .digest('hex');
    expect(signature).toBe(expectedSignature);
  });

  it('should retry webhook on failure', async () => {
    // This test would verify retry logic by having the webhook
    // receiver return errors initially, then succeed
    let callCount = 0;

    // Override the webhook handler temporarily
    webhookServer.close();
    const retryApp = express();
    retryApp.use(express.json());
    retryApp.post('/webhook', (req, res) => {
      callCount++;
      if (callCount < 3) {
        res.status(500).json({ error: 'Temporary failure' });
      } else {
        res.status(200).json({ received: true });
      }
    });
    webhookServer = retryApp.listen(9999);

    // Trigger webhook event
    await request(app)
      .post('/api/test/trigger-webhook')
      .set('Authorization', `Bearer ${adminToken}`)
      .send({ event: 'test.event' })
      .expect(200);

    // Wait for retries
    await new Promise(resolve => setTimeout(resolve, 10000));

    expect(callCount).toBeGreaterThanOrEqual(3);
  });
});
```

---

## API Testing Best Practices

### Test Organization and Structure

Organize API tests following a consistent pattern:

```
tests/
├── api/
│   ├── auth/
│   │   ├── login.test.js
│   │   ├── register.test.js
│   │   ├── password-reset.test.js
│   │   └── oauth.test.js
│   ├── users/
│   │   ├── create-user.test.js
│   │   ├── get-user.test.js
│   │   ├── update-user.test.js
│   │   ├── delete-user.test.js
│   │   └── user-permissions.test.js
│   ├── orders/
│   │   ├── create-order.test.js
│   │   ├── order-workflow.test.js
│   │   └── order-search.test.js
│   ├── webhooks/
│   │   └── webhook-delivery.test.js
│   └── security/
│       ├── injection.test.js
│       ├── authentication.test.js
│       └── rate-limiting.test.js
├── contracts/
│   ├── consumer/
│   │   └── order-service-user-service.test.js
│   └── provider/
│       └── user-service-verification.test.js
├── performance/
│   ├── k6/
│   │   ├── api-load-test.js
│   │   └── stress-test.js
│   └── jmeter/
│       └── api-test-plan.jmx
├── schemas/
│   ├── user.json
│   ├── order.json
│   └── product.json
├── fixtures/
│   ├── users.json
│   ├── products.json
│   └── test-data.csv
├── helpers/
│   ├── auth.js
│   ├── database.js
│   └── assertions.js
└── mocks/
    ├── handlers.js
    └── server.js
```

### Environment Management

Maintain separate configurations for each environment:

```javascript
// config/environments.js
module.exports = {
  local: {
    baseUrl: 'http://localhost:3000',
    dbUrl: 'postgresql://localhost:5432/testdb',
    timeout: 5000,
    retries: 0
  },
  staging: {
    baseUrl: 'https://api.staging.example.com',
    dbUrl: null, // No direct DB access in staging
    timeout: 10000,
    retries: 2
  },
  production: {
    baseUrl: 'https://api.example.com',
    dbUrl: null,
    timeout: 15000,
    retries: 3,
    readOnly: true // Only GET requests allowed
  }
};

// Helper to get current environment config
function getConfig() {
  const env = process.env.TEST_ENV || 'local';
  const config = module.exports[env];
  if (!config) {
    throw new Error(`Unknown test environment: ${env}`);
  }
  return config;
}
```

### Data Management Strategies

**Test data factories**:

```javascript
// helpers/factories.js
const { faker } = require('@faker-js/faker');

const factories = {
  user: (overrides = {}) => ({
    name: faker.person.fullName(),
    email: faker.internet.email(),
    password: 'TestP@ss123',
    role: 'user',
    ...overrides
  }),

  product: (overrides = {}) => ({
    name: faker.commerce.productName(),
    description: faker.commerce.productDescription(),
    price: parseFloat(faker.commerce.price({ min: 10, max: 1000 })),
    category: faker.commerce.department(),
    sku: faker.string.alphanumeric(10).toUpperCase(),
    stock: faker.number.int({ min: 0, max: 100 }),
    ...overrides
  }),

  order: (overrides = {}) => ({
    items: [
      {
        product_id: faker.number.int({ min: 1, max: 100 }),
        quantity: faker.number.int({ min: 1, max: 5 })
      }
    ],
    shipping_address: {
      street: faker.location.streetAddress(),
      city: faker.location.city(),
      state: faker.location.state({ abbreviated: true }),
      zip: faker.location.zipCode(),
      country: 'US'
    },
    payment_token: 'tok_test_visa',
    ...overrides
  })
};

module.exports = factories;
```

**Database seeding and cleanup**:

```javascript
// helpers/database.js
const db = require('../src/db');

async function seedTestData() {
  await db.query(`
    INSERT INTO users (id, name, email, password_hash, role, created_at) VALUES
    (1, 'Admin User', 'admin@test.com', '$2b$10$hash1', 'admin', NOW()),
    (2, 'Regular User', 'user@test.com', '$2b$10$hash2', 'user', NOW()),
    (3, 'Moderator', 'mod@test.com', '$2b$10$hash3', 'moderator', NOW())
    ON CONFLICT (id) DO NOTHING
  `);

  await db.query(`
    INSERT INTO products (id, name, price, stock, category) VALUES
    (1, 'Test Product A', 29.99, 100, 'electronics'),
    (2, 'Test Product B', 49.99, 50, 'electronics'),
    (3, 'Test Product C', 9.99, 200, 'accessories')
    ON CONFLICT (id) DO NOTHING
  `);
}

async function cleanTestData() {
  await db.query("DELETE FROM order_items WHERE order_id IN (SELECT id FROM orders WHERE user_id IN (SELECT id FROM users WHERE email LIKE '%@test.com'))");
  await db.query("DELETE FROM orders WHERE user_id IN (SELECT id FROM users WHERE email LIKE '%@test.com')");
  await db.query("DELETE FROM users WHERE email LIKE '%@test.com'");
}

async function resetSequences() {
  await db.query("SELECT setval('users_id_seq', (SELECT MAX(id) FROM users))");
  await db.query("SELECT setval('orders_id_seq', (SELECT MAX(id) FROM orders))");
}

module.exports = { seedTestData, cleanTestData, resetSequences };
```

### Reporting and Monitoring

**Custom test reporter for API metrics**:

```javascript
// reporters/api-metrics-reporter.js
class ApiMetricsReporter {
  constructor(globalConfig, options) {
    this.results = [];
  }

  onTestResult(test, testResult) {
    testResult.testResults.forEach(result => {
      this.results.push({
        name: result.fullName,
        status: result.status,
        duration: result.duration,
        suite: test.path
      });
    });
  }

  onRunComplete(contexts, results) {
    const summary = {
      timestamp: new Date().toISOString(),
      total: results.numTotalTests,
      passed: results.numPassedTests,
      failed: results.numFailedTests,
      skipped: results.numPendingTests,
      duration: results.testResults.reduce((sum, r) => sum + (r.perfStats?.end - r.perfStats?.start || 0), 0),
      slowTests: this.results
        .filter(r => r.duration > 1000)
        .sort((a, b) => b.duration - a.duration)
        .slice(0, 10)
    };

    console.log('\n📊 API Test Summary:');
    console.log(`   Total: ${summary.total}`);
    console.log(`   ✅ Passed: ${summary.passed}`);
    console.log(`   ❌ Failed: ${summary.failed}`);
    console.log(`   ⏭️ Skipped: ${summary.skipped}`);
    console.log(`   ⏱️ Duration: ${(summary.duration / 1000).toFixed(1)}s`);

    if (summary.slowTests.length > 0) {
      console.log('\n🐌 Slowest Tests:');
      summary.slowTests.forEach(t => {
        console.log(`   ${t.name}: ${t.duration}ms`);
      });
    }
  }
}

module.exports = ApiMetricsReporter;
```

---

## Comprehensive API Test Checklist

When testing any API endpoint, consider these categories:

### Functional Testing
- Happy path returns correct status code and data
- All required fields are present in response
- Data types match specification
- Pagination works correctly (first page, last page, out of range)
- Filtering returns only matching results
- Sorting orders results correctly
- Search returns relevant results
- Nested resources load correctly
- Relationships between resources are consistent

### Error Handling
- Missing required fields return 400 with specific error messages
- Invalid data types return 400/422 with clear descriptions
- Non-existent resources return 404
- Duplicate resources return 409
- Unauthorized requests return 401
- Forbidden requests return 403
- Rate-limited requests return 429 with Retry-After header
- Server errors return 500 with safe error messages (no stack traces)

### Security
- Authentication is required on protected endpoints
- Authorization prevents cross-tenant/cross-user access
- Token expiration is enforced
- SQL injection is prevented
- XSS payloads are sanitized
- CORS is properly configured
- Rate limiting is effective
- Sensitive data is not exposed in responses
- Security headers are present

### Performance
- Response times meet SLA requirements
- Endpoints handle expected concurrent load
- Large result sets don't cause memory issues
- Database queries are optimized (no N+1)
- Caching headers are set appropriately
- Compression is enabled for large responses

### Compatibility
- API versioning works correctly
- Backward compatibility is maintained
- Deprecated endpoints return appropriate warnings
- Content negotiation handles different Accept types
- Character encoding (UTF-8) works for international data

This comprehensive checklist ensures thorough API coverage and helps teams build reliable, secure, and performant APIs. Each item should be automated where possible and included in the continuous integration pipeline to catch regressions early.

---

## Summary

API testing is a critical discipline that encompasses functional validation, security testing, performance testing, and contract verification. The key takeaways from this chapter are:

1. **REST testing** requires systematic validation of each HTTP method, status code, response body, and header across happy path and error scenarios.

2. **GraphQL testing** adds unique concerns around query depth, complexity, and introspection control that REST tests don't address.

3. **Postman and Newman** provide an accessible entry point for API testing, with Newman enabling CI/CD integration and data-driven testing at scale.

4. **Contract testing with Pact** decouples consumer and provider testing, enabling independent deployment while maintaining API compatibility.

5. **Schema validation** using JSON Schema and OpenAPI specifications ensures responses conform to documented contracts.

6. **Security testing** must cover authentication, authorization, injection attacks, CORS, and security headers — automated and integrated into every build.

7. **Performance testing** with k6 and JMeter reveals how APIs behave under load, identifying bottlenecks before they impact production users.

8. **Mocking and virtualization** with WireMock, MSW, and Nock enable isolated testing, deterministic environments, and simulation of failure conditions.

A mature API testing strategy combines all these elements into a layered approach: fast schema validation catches structural issues, functional tests verify business logic, contract tests ensure compatibility, security tests prevent vulnerabilities, and performance tests validate scalability. Together, they provide comprehensive confidence in API quality.
