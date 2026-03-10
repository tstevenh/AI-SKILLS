# Chapter 14: Monitoring, Logging, and Observability

## Table of Contents
1. [Introduction to Observability](#introduction)
2. [Structured Logging](#structured-logging)
3. [Metrics Collection](#metrics)
4. [Distributed Tracing](#tracing)
5. [Health Checks and Alerting](#health-checks)
6. [Dashboards and Visualization](#dashboards)
7. [Error Tracking](#error-tracking)
8. [Performance Monitoring](#performance)

---

## Introduction to Observability

Production scraping systems operate unattended for extended periods. Without proper observability, failures go unnoticed, performance degrades silently, and debugging becomes nearly impossible. This chapter covers comprehensive monitoring strategies that keep your scraping infrastructure healthy and transparent.

### The Three Pillars of Observability

1. **Logs** - Discrete events with context
2. **Metrics** - Numeric measurements over time
3. **Traces** - Request flows through the system

Together, these provide complete visibility into system behavior.

---

## Structured Logging

### JSON-Structured Logger

```python
import logging
import json
import sys
from datetime import datetime
from typing import Any, Dict
import traceback


class StructuredLogFormatter(logging.Formatter):
    """Format log records as JSON for structured logging"""
    
    def format(self, record):
        log_data = {
            'timestamp': datetime.utcnow().isoformat() + 'Z',
            'level': record.levelname,
            'logger': record.name,
            'message': record.getMessage(),
            'module': record.module,
            'function': record.funcName,
            'line': record.lineno,
        }
        
        # Add extra fields
        if hasattr(record, 'spider_name'):
            log_data['spider_name'] = record.spider_name
        if hasattr(record, 'url'):
            log_data['url'] = record.url
        if hasattr(record, 'duration_ms'):
            log_data['duration_ms'] = record.duration_ms
        if hasattr(record, 'items_count'):
            log_data['items_count'] = record.items_count
        
        # Add exception info if present
        if record.exc_info:
            log_data['exception'] = {
                'type': record.exc_info[0].__name__ if record.exc_info[0] else None,
                'message': str(record.exc_info[1]) if record.exc_info[1] else None,
                'traceback': traceback.format_exception(*record.exc_info),
            }
        
        # Add any extra attributes
        for key, value in record.__dict__.items():
            if key not in log_data and not key.startswith('_'):
                log_data[key] = value
        
        return json.dumps(log_data, default=str)


def setup_structured_logging(level=logging.INFO):
    """Configure structured logging for the application"""
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(StructuredLogFormatter())
    
    root_logger = logging.getLogger()
    root_logger.setLevel(level)
    root_logger.handlers = []
    root_logger.addHandler(handler)
    
    return root_logger


# Usage with context
class SpiderLogger:
    """Logger with spider context"""
    
    def __init__(self, spider_name):
        self.logger = logging.getLogger(f'spider.{spider_name}')
        self.spider_name = spider_name
        self.extra = {'spider_name': spider_name}
    
    def info(self, message, **kwargs):
        self.logger.info(message, extra={**self.extra, **kwargs})
    
    def warning(self, message, **kwargs):
        self.logger.warning(message, extra={**self.extra, **kwargs})
    
    def error(self, message, **kwargs):
        self.logger.error(message, extra={**self.extra, **kwargs})
    
    def log_request(self, url, status_code, duration_ms, items_extracted=0):
        """Log a completed request with full context"""
        self.logger.info(
            f"Request completed: {url}",
            extra={
                'spider_name': self.spider_name,
                'url': url,
                'status_code': status_code,
                'duration_ms': duration_ms,
                'items_count': items_extracted,
            }
        )


# File-based structured logging
class FileStructuredLogger:
    """Write structured logs to rotating files"""
    
    def __init__(self, name, log_dir='logs', max_bytes=10*1024*1024, backup_count=5):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        
        # Ensure log directory exists
        import os
        os.makedirs(log_dir, exist_ok=True)
        
        # Rotating file handler
        from logging.handlers import RotatingFileHandler
        handler = RotatingFileHandler(
            filename=f'{log_dir}/{name}.log',
            maxBytes=max_bytes,
            backupCount=backup_count,
        )
        handler.setFormatter(StructuredLogFormatter())
        
        self.logger.addHandler(handler)
    
    def log(self, level, message, **kwargs):
        """Log with arbitrary extra fields"""
        extra = kwargs
        
        if level == 'debug':
            self.logger.debug(message, extra=extra)
        elif level == 'info':
            self.logger.info(message, extra=extra)
        elif level == 'warning':
            self.logger.warning(message, extra=extra)
        elif level == 'error':
            self.logger.error(message, extra=extra)
        elif level == 'critical':
            self.logger.critical(message, extra=extra)
```

---

## Metrics Collection

### In-Memory Metrics Collector

```python
from dataclasses import dataclass, field
from collections import defaultdict
from typing import Dict, List
from datetime import datetime, timedelta
import threading
import time


@dataclass
class MetricPoint:
    """Single metric data point"""
    timestamp: datetime
    value: float
    labels: Dict[str, str] = field(default_factory=dict)


class MetricsCollector:
    """Collect and aggregate metrics"""
    
    def __init__(self, retention_minutes=60):
        self.retention = timedelta(minutes=retention_minutes)
        self.counters: Dict[str, List[MetricPoint]] = defaultdict(list)
        self.gauges: Dict[str, MetricPoint] = {}
        self.histograms: Dict[str, List[MetricPoint]] = defaultdict(list)
        self._lock = threading.Lock()
    
    def increment(self, name: str, value: float = 1, labels: dict = None):
        """Increment a counter metric"""
        with self._lock:
            point = MetricPoint(
                timestamp=datetime.now(),
                value=value,
                labels=labels or {}
            )
            self.counters[name].append(point)
            self._cleanup_old()
    
    def gauge(self, name: str, value: float, labels: dict = None):
        """Set a gauge metric"""
        with self._lock:
            self.gauges[name] = MetricPoint(
                timestamp=datetime.now(),
                value=value,
                labels=labels or {}
            )
    
    def histogram(self, name: str, value: float, labels: dict = None):
        """Record a value in a histogram"""
        with self._lock:
            point = MetricPoint(
                timestamp=datetime.now(),
                value=value,
                labels=labels or {}
            )
            self.histograms[name].append(point)
            self._cleanup_old()
    
    def _cleanup_old(self):
        """Remove data points older than retention period"""
        cutoff = datetime.now() - self.retention
        
        for name in list(self.counters.keys()):
            self.counters[name] = [
                p for p in self.counters[name] if p.timestamp > cutoff
            ]
        
        for name in list(self.histograms.keys()):
            self.histograms[name] = [
                p for p in self.histograms[name] if p.timestamp > cutoff
            ]
    
    def get_counter(self, name: str, since: datetime = None) -> float:
        """Get counter total since timestamp"""
        points = self.counters.get(name, [])
        if since:
            points = [p for p in points if p.timestamp >= since]
        return sum(p.value for p in points)
    
    def get_gauge(self, name: str) -> float:
        """Get current gauge value"""
        point = self.gauges.get(name)
        return point.value if point else 0
    
    def get_histogram_stats(self, name: str, since: datetime = None) -> dict:
        """Get histogram statistics"""
        points = self.histograms.get(name, [])
        if since:
            points = [p for p in points if p.timestamp >= since]
        
        if not points:
            return {'count': 0, 'min': 0, 'max': 0, 'avg': 0, 'p95': 0}
        
        values = [p.value for p in points]
        values.sort()
        
        n = len(values)
        p95_idx = int(n * 0.95)
        
        return {
            'count': n,
            'min': values[0],
            'max': values[-1],
            'avg': sum(values) / n,
            'p95': values[min(p95_idx, n - 1)],
        }
    
    def get_all_metrics(self) -> dict:
        """Get snapshot of all metrics"""
        return {
            'counters': {
                name: self.get_counter(name)
                for name in self.counters.keys()
            },
            'gauges': {
                name: self.get_gauge(name)
                for name in self.gauges.keys()
            },
            'histograms': {
                name: self.get_histogram_stats(name)
                for name in self.histograms.keys()
            },
        }


# Predefined scraping metrics
class ScrapingMetrics:
    """Common metrics for web scraping"""
    
    def __init__(self):
        self.collector = MetricsCollector()
    
    def record_request(self, spider_name: str, status_code: int, duration_ms: float):
        """Record a completed HTTP request"""
        self.collector.increment('requests_total', 1, {'spider': spider_name})
        self.collector.increment(f'requests_status_{status_code}', 1, {'spider': spider_name})
        self.collector.histogram('request_duration_ms', duration_ms, {'spider': spider_name})
    
    def record_item(self, spider_name: str, item_type: str = 'default'):
        """Record an extracted item"""
        self.collector.increment('items_extracted', 1, {
            'spider': spider_name,
            'type': item_type,
        })
    
    def record_error(self, spider_name: str, error_type: str):
        """Record an error"""
        self.collector.increment('errors_total', 1, {
            'spider': spider_name,
            'type': error_type,
        })
    
    def set_active_spiders(self, count: int):
        """Set gauge for active spiders"""
        self.collector.gauge('spiders_active', count)
    
    def set_queue_size(self, spider_name: str, size: int):
        """Set gauge for URL queue size"""
        self.collector.gauge('queue_size', size, {'spider': spider_name})


# Prometheus-compatible metrics endpoint
class PrometheusExporter:
    """Export metrics in Prometheus format"""
    
    def __init__(self, collector: MetricsCollector):
        self.collector = collector
    
    def export(self) -> str:
        """Generate Prometheus text format output"""
        lines = []
        
        # Counters
        for name, points in self.collector.counters.items():
            total = sum(p.value for p in points)
            label_str = self._format_labels(points[0].labels) if points else ''
            lines.append(f'# TYPE {name} counter')
            lines.append(f'{name}{label_str} {total}')
        
        # Gauges
        for name, point in self.collector.gauges.items():
            label_str = self._format_labels(point.labels)
            lines.append(f'# TYPE {name} gauge')
            lines.append(f'{name}{label_str} {point.value}')
        
        # Histograms
        for name, points in self.collector.histograms.items():
            values = [p.value for p in points]
            if values:
                label_str = self._format_labels(points[0].labels)
                lines.append(f'# TYPE {name} histogram')
                lines.append(f'{name}_count{label_str} {len(values)}')
                lines.append(f'{name}_sum{label_str} {sum(values)}')
        
        return '\\n'.join(lines)
    
    def _format_labels(self, labels: dict) -> str:
        """Format labels for Prometheus"""
        if not labels:
            return ''
        label_pairs = [f'{k}="{v}"' for k, v in labels.items()]
        return '{' + ','.join(label_pairs) + '}'
```

---

## Health Checks and Alerting

### Health Check System

```python
from dataclasses import dataclass
from typing import Callable, Dict, List
from datetime import datetime
import threading
import time


@dataclass
class HealthStatus:
    """Health check result"""
    name: str
    status: str  # 'healthy', 'degraded', 'unhealthy'
    message: str
    timestamp: datetime
    duration_ms: float


class HealthChecker:
    """System health monitoring"""
    
    def __init__(self):
        self.checks: Dict[str, Callable] = {}
        self.results: Dict[str, HealthStatus] = {}
        self._lock = threading.Lock()
    
    def register(self, name: str, check_func: Callable):
        """Register a health check"""
        self.checks[name] = check_func
    
    def run_check(self, name: str) -> HealthStatus:
        """Run a single health check"""
        start = time.time()
        
        try:
            check_func = self.checks[name]
            result = check_func()
            
            if result is True:
                status = 'healthy'
                message = 'OK'
            elif result is False:
                status = 'unhealthy'
                message = 'Check failed'
            else:
                status = result.get('status', 'healthy')
                message = result.get('message', 'OK')
        
        except Exception as e:
            status = 'unhealthy'
            message = str(e)
        
        duration = (time.time() - start) * 1000
        
        health_status = HealthStatus(
            name=name,
            status=status,
            message=message,
            timestamp=datetime.now(),
            duration_ms=duration,
        )
        
        with self._lock:
            self.results[name] = health_status
        
        return health_status
    
    def run_all(self) -> List[HealthStatus]:
        """Run all registered health checks"""
        return [self.run_check(name) for name in self.checks.keys()]
    
    def get_overall_status(self) -> str:
        """Get aggregate health status"""
        with self._lock:
            statuses = [r.status for r in self.results.values()]
        
        if 'unhealthy' in statuses:
            return 'unhealthy'
        elif 'degraded' in statuses:
            return 'degraded'
        return 'healthy'


# Common health checks for scraping
class ScrapingHealthChecks:
    """Predefined health checks for scraping infrastructure"""
    
    def __init__(self, spider_manager, proxy_pool=None, storage=None):
        self.spider_manager = spider_manager
        self.proxy_pool = proxy_pool
        self.storage = storage
    
    def register_all(self, checker: HealthChecker):
        """Register all scraping health checks"""
        checker.register('spiders_active', self.check_spiders_active)
        checker.register('proxy_pool', self.check_proxy_pool)
        checker.register('storage', self.check_storage)
        checker.register('disk_space', self.check_disk_space)
        checker.register('memory', self.check_memory)
    
    def check_spiders_active(self):
        """Check that spiders are running"""
        active = self.spider_manager.get_active_count()
        if active == 0:
            return {'status': 'unhealthy', 'message': 'No active spiders'}
        return True
    
    def check_proxy_pool(self):
        """Check proxy pool health"""
        if not self.proxy_pool:
            return True
        
        healthy = self.proxy_pool.get_healthy_count()
        total = self.proxy_pool.get_total_count()
        
        if healthy == 0:
            return {'status': 'unhealthy', 'message': 'No healthy proxies'}
        elif healthy / total < 0.5:
            return {'status': 'degraded', 'message': f'Only {healthy}/{total} proxies healthy'}
        return True
    
    def check_storage(self):
        """Check storage connectivity"""
        if not self.storage:
            return True
        
        try:
            self.storage.ping()
            return True
        except Exception as e:
            return {'status': 'unhealthy', 'message': str(e)}
    
    def check_disk_space(self):
        """Check available disk space"""
        import shutil
        stat = shutil.disk_usage('/')
        free_gb = stat.free / (1024**3)
        
        if free_gb < 1:
            return {'status': 'unhealthy', 'message': f'Only {free_gb:.1f}GB free'}
        elif free_gb < 5:
            return {'status': 'degraded', 'message': f'Only {free_gb:.1f}GB free'}
        return True
    
    def check_memory(self):
        """Check available memory"""
        import psutil
        mem = psutil.virtual_memory()
        
        if mem.percent > 95:
            return {'status': 'unhealthy', 'message': f'Memory at {mem.percent}%'}
        elif mem.percent > 85:
            return {'status': 'degraded', 'message': f'Memory at {mem.percent}%'}
        return True


# Alert manager
class AlertManager:
    """Manage and send alerts"""
    
    def __init__(self):
        self.handlers: List[Callable] = []
        self.alert_history: List[dict] = []
        self.cooldowns: Dict[str, float] = {}
        self.default_cooldown = 300  # 5 minutes
    
    def add_handler(self, handler: Callable):
        """Add an alert handler"""
        self.handlers.append(handler)
    
    def send_alert(self, level: str, message: str, source: str = None, cooldown_key: str = None):
        """Send an alert through all handlers"""
        # Check cooldown
        if cooldown_key:
            last_sent = self.cooldowns.get(cooldown_key, 0)
            if time.time() - last_sent < self.default_cooldown:
                return  # Still in cooldown
            self.cooldowns[cooldown_key] = time.time()
        
        alert = {
            'timestamp': datetime.now().isoformat(),
            'level': level,
            'message': message,
            'source': source,
        }
        
        self.alert_history.append(alert)
        
        for handler in self.handlers:
            try:
                handler(alert)
            except Exception as e:
                logging.error(f"Alert handler failed: {e}")
    
    def send_slack_alert(self, webhook_url: str):
        """Create Slack alert handler"""
        import requests
        
        def handler(alert):
            color = {
                'info': '#36a64f',
                'warning': '#ff9900',
                'error': '#ff0000',
                'critical': '#990000',
            }.get(alert['level'], '#cccccc')
            
            payload = {
                'attachments': [{
                    'color': color,
                    'title': f"[{alert['level'].upper()}] Scraping Alert",
                    'text': alert['message'],
                    'footer': alert.get('source', 'scraper'),
                    'ts': int(time.time()),
                }]
            }
            
            requests.post(webhook_url, json=payload)
        
        self.add_handler(handler)
```

---

## Dashboards and Visualization

### Simple Dashboard Server

```python
from http.server import HTTPServer, BaseHTTPRequestHandler
import json


class MetricsHandler(BaseHTTPRequestHandler):
    """HTTP handler for metrics dashboard"""
    
    metrics_collector = None
    
    def do_GET(self):
        if self.path == '/metrics':
            self._serve_metrics()
        elif self.path == '/health':
            self._serve_health()
        elif self.path == '/':
            self._serve_dashboard()
        else:
            self.send_error(404)
    
    def _serve_metrics(self):
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        
        metrics = self.metrics_collector.get_all_metrics()
        self.wfile.write(json.dumps(metrics, indent=2).encode())
    
    def _serve_health(self):
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        
        health = {
            'status': 'healthy',
            'timestamp': datetime.now().isoformat(),
        }
        self.wfile.write(json.dumps(health).encode())
    
    def _serve_dashboard(self):
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()
        
        html = '''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Scraping Dashboard</title>
            <meta http-equiv="refresh" content="5">
            <style>
                body { font-family: sans-serif; margin: 20px; }
                .metric { background: #f5f5f5; padding: 15px; margin: 10px 0; border-radius: 5px; }
                .metric h3 { margin-top: 0; }
                .value { font-size: 24px; font-weight: bold; color: #333; }
                .healthy { color: green; }
                .warning { color: orange; }
                .error { color: red; }
            </style>
        </head>
        <body>
            <h1>Scraping Dashboard</h1>
            <div id="metrics"></div>
            <script>
                fetch('/metrics')
                    .then(r => r.json())
                    .then(data => {
                        const container = document.getElementById('metrics');
                        container.innerHTML = '<pre>' + JSON.stringify(data, null, 2) + '</pre>';
                    });
            </script>
        </body>
        </html>
        '''
        self.wfile.write(html.encode())
    
    def log_message(self, format, *args):
        # Suppress request logging
        pass


def start_dashboard_server(collector, port=8080):
    """Start metrics dashboard server"""
    MetricsHandler.metrics_collector = collector
    server = HTTPServer(('0.0.0.0', port), MetricsHandler)
    print(f"Dashboard running on http://localhost:{port}")
    server.serve_forever()
```

---

## Error Tracking

### Centralized Error Tracking

```python
import hashlib
import traceback
from collections import defaultdict
from datetime import datetime


class ErrorTracker:
    """Track and aggregate errors"""
    
    def __init__(self, max_errors=1000):
        self.max_errors = max_errors
        self.errors: List[dict] = []
        self.error_counts: Dict[str, int] = defaultdict(int)
        self._fingerprint_cache = {}
    
    def track(self, exception, context: dict = None):
        """Track an exception"""
        error_data = {
            'timestamp': datetime.now().isoformat(),
            'type': type(exception).__name__,
            'message': str(exception),
            'traceback': traceback.format_exc(),
            'fingerprint': self._fingerprint(exception),
            'context': context or {},
        }
        
        # Add to list
        self.errors.append(error_data)
        if len(self.errors) > self.max_errors:
            self.errors.pop(0)
        
        # Increment count
        self.error_counts[error_data['fingerprint']] += 1
        
        return error_data
    
    def _fingerprint(self, exception) -> str:
        """Generate error fingerprint for grouping"""
        # Hash of exception type + first line of traceback
        tb_lines = traceback.format_exc().strip().split('\\n')
        key = f"{type(exception).__name__}:{tb_lines[-1] if tb_lines else ''}"
        return hashlib.md5(key.encode()).hexdigest()[:16]
    
    def get_summary(self) -> dict:
        """Get error summary"""
        # Group by fingerprint
        grouped = defaultdict(list)
        for error in self.errors:
            grouped[error['fingerprint']].append(error)
        
        summary = []
        for fingerprint, errors in sorted(
            grouped.items(),
            key=lambda x: len(x[1]),
            reverse=True
        )[:10]:
            summary.append({
                'fingerprint': fingerprint,
                'count': len(errors),
                'type': errors[0]['type'],
                'message': errors[0]['message'][:100],
                'last_occurrence': errors[-1]['timestamp'],
            })
        
        return {
            'total_errors': len(self.errors),
            'unique_errors': len(grouped),
            'top_errors': summary,
        }
```

This chapter provides comprehensive monitoring infrastructure for production scraping systems. With structured logging, metrics collection, health checks, alerting, and error tracking, you'll have complete visibility into your scraping operations and can quickly detect and respond to issues.
