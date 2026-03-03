# Advanced Automation Patterns

> Complex workflow patterns, multi-system orchestration, and enterprise automation architectures.

---

## Table of Contents

1. [Event-Driven Architecture](#event-driven-architecture)
2. [Multi-System Orchestration](#multi-system-orchestration)
3. [State Management](#state-management)
4. [Error Recovery Patterns](#error-recovery-patterns)
5. [Scalability Patterns](#scalability-patterns)
6. [Testing & Validation](#testing--validation)
7. [Monitoring & Observability](#monitoring--observability)
8. [Enterprise Patterns](#enterprise-patterns)

---

## Event-Driven Architecture

### The Event-Driven Model

```
Traditional: Request → Process → Response (synchronous)

Event-Driven: Event → Queue → Process → Event → Queue → Process...
```

### Event Sources

**Internal events:**
- User actions (form submit, click)
- System events (file upload, threshold crossed)
- Scheduled events (cron, time-based)
- Database changes (insert, update, delete)

**External events:**
- Webhooks from third-party services
- Email/message arrival
- API callbacks
- Social media mentions

### Event Processing Patterns

#### Webhook Handler
```yaml
workflow: Webhook Event Handler

nodes:
  - Webhook:
      name: Receive Event
      path: /events/{{ source }}
      method: POST
      authentication: hmac
      
  - Code:
      name: Validate Payload
      code: |
        const signature = $input.headers['x-signature'];
        const isValid = verifyHMAC(signature, $input.body, secret);
        if (!isValid) throw new Error('Invalid signature');
        return $input.body;
        
  - Switch:
      name: Route by Event Type
      property: event_type
      conditions:
        - user.created: → Process User Created
        - order.completed: → Process Order
        - payment.failed: → Process Payment Failed
        
  - Multiple Paths:
      - Process specific event type
      - Update local database
      - Trigger dependent workflows
      
  - Webhook Response:
      status: 200
      body: { "received": true }
```

#### Event Bus Pattern
```yaml
workflow: Event Publisher

# When something happens, publish to event bus
nodes:
  - Trigger: Internal action
  - Code:
      name: Create Event
      code: |
        return {
          event_id: uuid(),
          event_type: 'order.created',
          timestamp: new Date().toISOString(),
          data: $input,
          metadata: {
            source: 'order_service',
            version: '1.0'
          }
        };
        
  - HTTP Request:
      name: Publish to Event Bus
      url: {{ event_bus_url }}/events
      method: POST
      body: {{ $json }}
      
---

workflow: Event Subscriber

# Subscribe to specific events
nodes:
  - Webhook:
      name: Receive Event
      path: /subscribe/order.created
      
  - Code:
      name: Process Event
      
  - Parallel:
      - Update Inventory
      - Notify Customer
      - Update Analytics
      - Sync to Data Warehouse
```

### Dead Letter Queues

Handle events that fail processing:

```yaml
workflow: Dead Letter Handler

trigger: schedule - every 15 minutes

steps:
  - Get failed events from DLQ
  
  - For each event:
      - Analyze failure reason
      - If transient error: Retry
      - If permanent error: Alert + Archive
      - If fixable: Auto-fix and retry
      
  - Report:
      - Count of retries
      - Count of permanent failures
      - Alert if threshold exceeded
```

---

## Multi-System Orchestration

### Saga Pattern

For distributed transactions across systems:

```yaml
workflow: Order Processing Saga

nodes:
  - Start: Order received
  
  # Step 1: Reserve inventory
  - Inventory Service:
      action: reserve_items
      items: {{ order.items }}
      on_error: → Compensation
      
  # Step 2: Process payment
  - Payment Service:
      action: charge_card
      amount: {{ order.total }}
      on_error: → Compensation (release inventory)
      
  # Step 3: Create shipment
  - Shipping Service:
      action: create_shipment
      on_error: → Compensation (refund + release)
      
  # Step 4: Update order status
  - Order Service:
      action: mark_confirmed
      
  - Success: Notify customer

  # Compensation handlers
  - Compensation:
      - If step 3 failed:
          - Refund payment
          - Release inventory
      - If step 2 failed:
          - Release inventory
      - Log compensation
      - Alert operations
```

### Choreography vs Orchestration

**Choreography** (decentralized):
```
Service A → Event → Service B
Service B → Event → Service C
Service C → Event → Service D

Each service knows what to do when it receives an event.
```

**Orchestration** (centralized):
```
Orchestrator → Service A
           → Service B (when A done)
           → Service C (when B done)
           → Service D (when C done)

Central workflow controls the sequence.
```

**When to use which:**

| Factor | Choreography | Orchestration |
|--------|-------------|---------------|
| Complexity | Simple flows | Complex flows |
| Coupling | Loose | Tighter |
| Visibility | Harder to trace | Easy to trace |
| Changes | Each service | Central place |
| Best for | Microservices | Business processes |

### Cross-System Data Sync

```yaml
workflow: CRM-ERP Sync

trigger: schedule - every 5 minutes

steps:
  # Get changes from both systems
  - parallel:
      - CRM: Get records modified since last sync
      - ERP: Get records modified since last sync
      
  # Resolve conflicts
  - Code:
      name: Conflict Resolution
      code: |
        const conflicts = findConflicts(crm_changes, erp_changes);
        
        return conflicts.map(c => {
          // Last write wins (or custom logic)
          return c.crm_updated > c.erp_updated ? 
            { source: 'crm', record: c.crm } :
            { source: 'erp', record: c.erp };
        });
        
  # Apply changes
  - For each change:
      - If source == 'crm': Update ERP
      - If source == 'erp': Update CRM
      
  # Log sync
  - Database:
      table: sync_log
      record: { timestamp, changes_count, conflicts_count }
```

---

## State Management

### Workflow State

For long-running workflows:

```python
class WorkflowState:
    def __init__(self, workflow_id: str):
        self.id = workflow_id
        self.status = "pending"
        self.current_step = 0
        self.data = {}
        self.history = []
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    
    def advance(self, step_name: str, result: dict):
        self.history.append({
            "step": step_name,
            "result": result,
            "timestamp": datetime.now()
        })
        self.current_step += 1
        self.data.update(result)
        self.updated_at = datetime.now()
        self.save()
    
    def fail(self, step_name: str, error: str):
        self.status = "failed"
        self.history.append({
            "step": step_name,
            "error": error,
            "timestamp": datetime.now()
        })
        self.save()
    
    def resume_from(self, step: int):
        """Resume workflow from a specific step"""
        self.current_step = step
        self.status = "running"
        self.save()
```

### State Machines

```yaml
workflow: Order State Machine

states:
  - pending
  - confirmed
  - processing
  - shipped
  - delivered
  - cancelled
  - refunded

transitions:
  pending:
    - confirm → confirmed
    - cancel → cancelled
    
  confirmed:
    - start_processing → processing
    - cancel → cancelled
    
  processing:
    - ship → shipped
    - cancel → cancelled (with refund)
    
  shipped:
    - deliver → delivered
    - return → processing (return)
    
  delivered:
    - request_refund → refunded
    
  cancelled:
    - [] # terminal state
    
  refunded:
    - [] # terminal state

on_transition:
  - Update database
  - Send notification
  - Log event
  - Trigger dependent workflows
```

### Idempotency

Ensure operations can be retried safely:

```python
class IdempotentOperation:
    def __init__(self, db):
        self.db = db
    
    async def execute(
        self, 
        operation_id: str, 
        operation: Callable
    ) -> dict:
        # Check if already executed
        existing = await self.db.get_operation(operation_id)
        if existing and existing.status == "completed":
            return existing.result
        
        # Create or update operation record
        await self.db.upsert_operation(
            operation_id,
            status="in_progress"
        )
        
        try:
            result = await operation()
            await self.db.update_operation(
                operation_id,
                status="completed",
                result=result
            )
            return result
            
        except Exception as e:
            await self.db.update_operation(
                operation_id,
                status="failed",
                error=str(e)
            )
            raise
```

---

## Error Recovery Patterns

### Circuit Breaker

Prevent cascading failures:

```python
class CircuitBreaker:
    def __init__(
        self,
        failure_threshold: int = 5,
        recovery_timeout: int = 60
    ):
        self.failure_threshold = failure_threshold
        self.recovery_timeout = recovery_timeout
        self.failures = 0
        self.last_failure_time = None
        self.state = "closed"  # closed, open, half-open
    
    async def execute(self, operation: Callable):
        if self.state == "open":
            if self.should_try_recovery():
                self.state = "half-open"
            else:
                raise CircuitOpenError()
        
        try:
            result = await operation()
            self.on_success()
            return result
            
        except Exception as e:
            self.on_failure()
            raise
    
    def on_success(self):
        self.failures = 0
        self.state = "closed"
    
    def on_failure(self):
        self.failures += 1
        self.last_failure_time = time.time()
        
        if self.failures >= self.failure_threshold:
            self.state = "open"
    
    def should_try_recovery(self) -> bool:
        return (time.time() - self.last_failure_time) > self.recovery_timeout
```

### Retry with Backoff

```yaml
workflow: Resilient API Call

nodes:
  - HTTP Request:
      name: Call External API
      url: {{ api_url }}
      retry:
        enabled: true
        max_attempts: 5
        wait_between: exponential
        initial_wait: 1000  # ms
        max_wait: 60000     # ms
        retry_on:
          - status: 429  # Rate limit
          - status: 500  # Server error
          - status: 502  # Bad gateway
          - status: 503  # Service unavailable
          - status: 504  # Gateway timeout
          - error: ETIMEDOUT
          - error: ECONNRESET
```

### Compensation Handlers

```yaml
workflow: Booking with Compensation

nodes:
  - Book Flight:
      action: create_flight_booking
      save_to: flight_booking_id
      on_error: → End with Error
      
  - Book Hotel:
      action: create_hotel_booking
      save_to: hotel_booking_id
      on_error: → Compensate Flight
      
  - Book Car:
      action: create_car_booking
      save_to: car_booking_id
      on_error: → Compensate Hotel and Flight
      
  - Charge Card:
      action: process_payment
      on_error: → Compensate All
      
  - Success: → Confirm All Bookings

compensation:
  - Compensate Flight:
      - Cancel flight: {{ flight_booking_id }}
      - Log cancellation
      → End with Error
      
  - Compensate Hotel and Flight:
      - Cancel hotel: {{ hotel_booking_id }}
      - Cancel flight: {{ flight_booking_id }}
      - Log cancellations
      → End with Error
      
  - Compensate All:
      - Cancel car: {{ car_booking_id }}
      - Cancel hotel: {{ hotel_booking_id }}
      - Cancel flight: {{ flight_booking_id }}
      - Log cancellations
      → End with Error
```

---

## Scalability Patterns

### Work Distribution

```yaml
workflow: Batch Processor

trigger: schedule - daily

steps:
  # Get all items to process
  - Database:
      action: Get items where status = 'pending'
      
  # Split into batches
  - Code:
      name: Create Batches
      code: |
        const batchSize = 100;
        return chunk($input.items, batchSize).map((batch, i) => ({
          batch_id: i,
          items: batch
        }));
        
  # Process batches in parallel (limited concurrency)
  - Split In Batches:
      batch_size: 10  # Process 10 batches at a time
      
      - For Each Item in Batch:
          - Process item
          - Update status
          
  # Aggregate results
  - Merge:
      - Count successes
      - Count failures
      - Report
```

### Queue-Based Processing

```yaml
workflow: Queue Worker

# This runs continuously or is triggered by queue

steps:
  - Get Message from Queue:
      queue: work_queue
      wait: true
      timeout: 30s
      
  - Process Message:
      - Parse payload
      - Execute work
      - Handle errors
      
  - Acknowledge Message:
      if: success
      
  - Dead Letter:
      if: failed and retries > 3
      
  - Re-queue:
      if: failed and retries <= 3
      delay: exponential_backoff
```

### Fan-Out / Fan-In

```yaml
workflow: Parallel Processing

nodes:
  # Fan-out: Distribute work
  - Split:
      name: Distribute to Workers
      items: {{ $json.data }}
      
  # Parallel processing
  - Parallel For Each:
      concurrency: 20
      
      - HTTP Request:
          name: Process Item
          
  # Fan-in: Collect results
  - Aggregate:
      name: Combine Results
      mode: combine
      
  - Code:
      name: Final Processing
      code: |
        return {
          total: $input.results.length,
          success: $input.results.filter(r => r.success).length,
          errors: $input.results.filter(r => !r.success)
        };
```

---

## Testing & Validation

### Workflow Testing

```python
class WorkflowTester:
    def __init__(self, workflow):
        self.workflow = workflow
        self.mocks = {}
    
    def mock_node(self, node_name: str, response: dict):
        """Mock a node's response"""
        self.mocks[node_name] = response
    
    async def run_test(self, input_data: dict) -> dict:
        """Run workflow with mocks"""
        original_nodes = self.workflow.nodes.copy()
        
        # Inject mocks
        for node_name, response in self.mocks.items():
            self.workflow.nodes[node_name] = MockNode(response)
        
        try:
            result = await self.workflow.execute(input_data)
            return result
        finally:
            # Restore original nodes
            self.workflow.nodes = original_nodes
    
    async def test_error_handling(self, node_name: str, error: Exception):
        """Test workflow handles errors correctly"""
        self.mock_node(node_name, MockErrorNode(error))
        
        with pytest.raises(WorkflowError):
            await self.run_test(sample_input)

# Usage
def test_order_workflow():
    tester = WorkflowTester(order_workflow)
    
    tester.mock_node("payment_service", {"status": "success", "id": "pay_123"})
    tester.mock_node("inventory_service", {"status": "reserved"})
    
    result = await tester.run_test({"order_id": "123", "total": 100})
    
    assert result["status"] == "completed"
```

### Data Validation

```yaml
workflow: Validated Data Processing

nodes:
  - Webhook:
      name: Receive Data
      
  - JSON Schema Validator:
      name: Validate Input
      schema:
        type: object
        required: [email, name, order_id]
        properties:
          email:
            type: string
            format: email
          name:
            type: string
            minLength: 1
          order_id:
            type: string
            pattern: "^ORD-[0-9]+"
      on_error: → Validation Error Response
      
  - Process Data:
      # Now safe to process
      
  - Validation Error Response:
      status: 400
      body:
        error: "Validation failed"
        details: "{{ $json.validation_errors }}"
```

---

## Monitoring & Observability

### Logging Strategy

```yaml
workflow: Workflow with Comprehensive Logging

nodes:
  - Start:
      log:
        level: info
        message: "Workflow started"
        data:
          workflow_id: "{{ $workflow.id }}"
          input: "{{ $json }}"
          
  - For Each Step:
      - Before:
          log:
            level: debug
            message: "Starting step: {{ $node.name }}"
            
      - Execute Step
      
      - After:
          log:
            level: debug
            message: "Completed step: {{ $node.name }}"
            data:
              duration_ms: "{{ $node.duration }}"
              result_size: "{{ JSON.stringify($json).length }}"
              
  - On Error:
      log:
        level: error
        message: "Workflow failed"
        data:
          error: "{{ $error.message }}"
          stack: "{{ $error.stack }}"
          step: "{{ $node.name }}"
```

### Metrics Collection

```python
class WorkflowMetrics:
    def __init__(self, prometheus_client):
        self.execution_count = prometheus_client.Counter(
            'workflow_executions_total',
            'Total workflow executions',
            ['workflow_name', 'status']
        )
        self.execution_duration = prometheus_client.Histogram(
            'workflow_execution_duration_seconds',
            'Workflow execution duration',
            ['workflow_name']
        )
        self.step_errors = prometheus_client.Counter(
            'workflow_step_errors_total',
            'Step errors',
            ['workflow_name', 'step_name', 'error_type']
        )
    
    def record_execution(self, workflow_name: str, status: str, duration: float):
        self.execution_count.labels(
            workflow_name=workflow_name,
            status=status
        ).inc()
        
        self.execution_duration.labels(
            workflow_name=workflow_name
        ).observe(duration)
    
    def record_step_error(self, workflow_name: str, step_name: str, error_type: str):
        self.step_errors.labels(
            workflow_name=workflow_name,
            step_name=step_name,
            error_type=error_type
        ).inc()
```

### Alerting Rules

```yaml
alerts:
  - name: workflow_high_failure_rate
    condition: |
      rate(workflow_executions_total{status="failed"}[5m]) / 
      rate(workflow_executions_total[5m]) > 0.1
    severity: critical
    message: "Workflow {{ $labels.workflow_name }} has >10% failure rate"
    
  - name: workflow_slow_execution
    condition: |
      histogram_quantile(0.95, workflow_execution_duration_seconds) > 300
    severity: warning
    message: "Workflow {{ $labels.workflow_name }} p95 latency > 5 minutes"
    
  - name: workflow_queue_backup
    condition: |
      workflow_queue_length > 1000
    severity: warning
    message: "Workflow queue has over 1000 pending items"
```

---

## Enterprise Patterns

### Multi-Tenant Architecture

```yaml
workflow: Multi-Tenant Workflow

nodes:
  - Webhook:
      name: Receive Request
      
  - Code:
      name: Extract Tenant
      code: |
        const tenantId = $input.headers['x-tenant-id'] ||
                         $input.body.tenant_id;
        if (!tenantId) throw new Error('Tenant ID required');
        return { tenant_id: tenantId, ...$input.body };
        
  - Database:
      name: Get Tenant Config
      query: SELECT * FROM tenants WHERE id = {{ $json.tenant_id }}
      
  - Switch:
      name: Route by Tenant Type
      property: tenant_type
      conditions:
        - enterprise: → Enterprise Flow
        - standard: → Standard Flow
        - trial: → Trial Flow
        
  - Each Flow:
      - Apply tenant-specific config
      - Process with tenant isolation
      - Log with tenant context
```

### Audit Trail

```python
class AuditLogger:
    def __init__(self, db):
        self.db = db
    
    async def log(
        self,
        action: str,
        actor: str,
        resource: str,
        resource_id: str,
        changes: dict = None,
        metadata: dict = None
    ):
        await self.db.insert('audit_log', {
            'id': uuid4(),
            'timestamp': datetime.utcnow(),
            'action': action,
            'actor': actor,
            'resource': resource,
            'resource_id': resource_id,
            'changes': json.dumps(changes) if changes else None,
            'metadata': json.dumps(metadata) if metadata else None,
            'ip_address': get_client_ip(),
            'user_agent': get_user_agent()
        })

# Usage in workflow
@audit_logged
async def update_customer(customer_id: str, data: dict):
    old_data = await get_customer(customer_id)
    await db.update('customers', customer_id, data)
    
    await audit.log(
        action='customer.updated',
        actor=current_user.id,
        resource='customer',
        resource_id=customer_id,
        changes={
            'before': old_data,
            'after': data
        }
    )
```

### Approval Workflows

```yaml
workflow: Expense Approval

nodes:
  - Trigger: New expense submitted
  
  - Determine Approvers:
      rules:
        - amount < 100: auto_approve
        - amount < 1000: manager
        - amount < 10000: manager + finance
        - amount >= 10000: manager + finance + cfo
        
  - If Auto Approve:
      - Mark approved
      - Process payment
      - End
      
  - Create Approval Request:
      - Store in pending_approvals
      - Set deadline
      - Notify approvers
      
  - Wait for Approvals:
      type: wait_for_condition
      condition: all_approved OR rejected OR deadline_passed
      timeout: 7 days
      
  - Check Result:
      - All approved: → Process Payment
      - Rejected: → Notify Submitter of Rejection
      - Timeout: → Escalate
      
  - Process Payment:
      - Create payment
      - Update status
      - Notify submitter
```

---

## Summary

### Pattern Selection Guide

| Scenario | Pattern |
|----------|---------|
| Distributed transactions | Saga |
| High throughput | Queue-based + Fan-out |
| Long-running processes | State machine |
| External service calls | Circuit breaker + Retry |
| Multi-step with rollback | Compensation |
| Real-time reactions | Event-driven |
| Data synchronization | CDC + Conflict resolution |

### Best Practices

1. **Design for failure** - Every external call can fail
2. **Make operations idempotent** - Safe to retry
3. **Keep state explicit** - Persist workflow state
4. **Log everything** - Debug issues easily
5. **Monitor proactively** - Alert before users notice
6. **Test compensation** - Verify rollback works
7. **Document flows** - Future you will thank you

See [../implementation/roadmap.md](../implementation/roadmap.md) for implementation guidance →
