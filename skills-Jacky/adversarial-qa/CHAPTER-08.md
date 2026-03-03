# Chapter 8: Advanced Adversarial Testing Strategies

## 8.1 Chaos Engineering Principles

### What is Chaos Engineering?

Chaos Engineering is the discipline of experimenting on a system to build confidence in its capability to withstand turbulent conditions in production.

**Core Principles:**
1. Build a hypothesis around steady-state behavior
2. Vary real-world events
3. Run experiments in production
4. Automate experiments for continuous validation
5. Minimize blast radius

### Steady-State Hypothesis

**Definition:**
A measurable system output that indicates normal behavior.

**Examples:**
- Response time p99 < 200ms
- Error rate < 0.1%
- Throughput > 1000 req/s
- CPU utilization < 70%

**Measurement:**
```python
def steady_state_metrics():
    return {
        'response_time_p99': measure_p99_latency(),
        'error_rate': calculate_error_rate(),
        'throughput': measure_requests_per_second(),
        'cpu_utilization': get_cpu_usage()
    }
```

## 8.2 Failure Injection Techniques

### Network Failures

**Latency Injection:**
```python
# Using Toxiproxy
import toxiproxy

proxy = toxiproxy.create_proxy("mysql", "127.0.0.1:3306")
proxy.add_toxic(
    name="latency_downstream",
    type="latency",
    attributes={"latency": 1000, "jitter": 50}
)
```

**Packet Loss:**
```bash
# Using tc (traffic control)
tc qdisc add dev eth0 root netem loss 10%
```

**DNS Failures:**
```python
# Block DNS resolution
import socket
original_getaddrinfo = socket.getaddrinfo

def failing_getaddrinfo(*args, **kwargs):
    if args[0] == "api.example.com":
        raise socket.gaierror("Name resolution failed")
    return original_getaddrinfo(*args, **kwargs)

socket.getaddrinfo = failing_getaddrinfo
```

### Resource Exhaustion

**CPU Exhaustion:**
```python
import multiprocessing
import time

def consume_cpu():
    while True:
        pass

# Start CPU-intensive processes
for _ in range(multiprocessing.cpu_count()):
    multiprocessing.Process(target=consume_cpu).start()
```

**Memory Exhaustion:**
```python
# Gradually consume memory
memory_hog = []
while True:
    memory_hog.append(" " * 1024 * 1024)  # 1MB chunks
    time.sleep(0.1)
```

**Disk Exhaustion:**
```bash
# Fill disk space
dd if=/dev/zero of=/tmp/fill_disk bs=1M count=10240
```

## 8.3 Game Day Exercises

### Planning a Game Day

**Preparation Phase:**
1. Define objectives
2. Identify critical systems
3. Create failure scenarios
4. Establish safety mechanisms
5. Prepare rollback procedures

**Execution Phase:**
1. Brief participants
2. Inject failures
3. Monitor system response
4. Document observations
5. Track recovery time

**Post-Game Analysis:**
1. Review metrics
2. Identify gaps
3. Document learnings
4. Update runbooks
5. Schedule improvements

### Sample Game Day Scenarios

**Scenario 1: Database Failover**
- Primary database becomes unavailable
- Verify automatic failover
- Check data consistency
- Measure recovery time

**Scenario 2: Third-Party Outage**
- Payment processor goes down
- Test fallback mechanisms
- Verify order queuing
- Check customer communication

**Scenario 3: Traffic Spike**
- Simulate 10x normal traffic
- Test auto-scaling
- Monitor performance degradation
- Verify circuit breakers

## 8.4 Resilience Patterns

### Circuit Breaker Pattern

**States:**
- Closed: Normal operation
- Open: Failing, rejecting requests
- Half-Open: Testing if recovered

**Implementation:**
```python
class CircuitBreaker:
    def __init__(self, failure_threshold=5, recovery_timeout=30):
        self.failure_threshold = failure_threshold
        self.recovery_timeout = recovery_timeout
        self.failure_count = 0
        self.last_failure_time = None
        self.state = 'CLOSED'
    
    def call(self, func, *args, **kwargs):
        if self.state == 'OPEN':
            if self.should_attempt_reset():
                self.state = 'HALF_OPEN'
            else:
                raise CircuitBreakerOpen()
        
        try:
            result = func(*args, **kwargs)
            self.on_success()
            return result
        except Exception as e:
            self.on_failure()
            raise e
    
    def on_failure(self):
        self.failure_count += 1
        self.last_failure_time = time.time()
        if self.failure_count >= self.failure_threshold:
            self.state = 'OPEN'
    
    def on_success(self):
        self.failure_count = 0
        self.state = 'CLOSED'
```

### Bulkhead Pattern

**Concept:**
Isolate failures to prevent cascading effects.

**Implementation:**
```python
from concurrent.futures import ThreadPoolExecutor

class Bulkhead:
    def __init__(self, name, max_concurrent, queue_size=0):
        self.name = name
        self.executor = ThreadPoolExecutor(
            max_workers=max_concurrent,
            maxsize=queue_size
        )
    
    def submit(self, func, *args, **kwargs):
        try:
            return self.executor.submit(func, *args, **kwargs)
        except Exception:
            raise BulkheadFull(f"Bulkhead {self.name} is full")
```

## 8.5 Observability for Resilience

### Key Metrics

**RED Method:**
- Rate: Requests per second
- Errors: Error rate
- Duration: Response time

**USE Method:**
- Utilization: Resource usage
- Saturation: Queue lengths
- Errors: Error counts

### Alerting Strategy

**Severity Levels:**
- P1: Service down, immediate response
- P2: Degraded performance, respond within 15 min
- P3: Anomaly detected, respond within 1 hour
- P4: Informational, next business day

This advanced adversarial testing knowledge ensures systems can withstand real-world failures.
