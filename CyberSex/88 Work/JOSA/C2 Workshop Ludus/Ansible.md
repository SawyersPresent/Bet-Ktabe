


## Vuln script


```
#Requires -RunAsAdministrator

<#
.SYNOPSIS
    Creates vulnerable Windows services for security testing and training purposes.

.DESCRIPTION
    This script creates two intentionally vulnerable services:
    1. ServiceTester - Has an unquoted service path vulnerability
    2. ServicePermissions - Has overly permissive file permissions allowing binary modification

.NOTES
    WARNING: This script creates INTENTIONALLY VULNERABLE services for educational/testing purposes only.
    Only use in isolated lab environments. Never run on production systems.
    Author: Security Training Lab
    Requires: Administrator privileges
#>

# Color output functions
function Write-Success { param($Message) Write-Host "[+] $Message" -ForegroundColor Green }
function Write-Info { param($Message) Write-Host "[*] $Message" -ForegroundColor Cyan }
function Write-Warn { param($Message) Write-Host "[!] $Message" -ForegroundColor Yellow }
function Write-Fail { param($Message) Write-Host "[-] $Message" -ForegroundColor Red }

Write-Host "`n========================================" -ForegroundColor Yellow
Write-Host "  Vulnerable Services Creator" -ForegroundColor Yellow
Write-Host "  For Security Testing Only!" -ForegroundColor Yellow
Write-Host "========================================`n" -ForegroundColor Yellow

# Check if running as admin
$isAdmin = ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
if (-not $isAdmin) {
    Write-Fail "This script must be run as Administrator!"
    exit 1
}

# Create base directory with spaces (for unquoted path vulnerability)
$vulnPath = "C:\Program Files\Vulnerable Services"
$serviceTesterPath = "$vulnPath\Service Tester"
$servicePermissionsPath = "$vulnPath\ServicePermissions"

Write-Info "Creating directory structure..."
try {
    New-Item -Path $vulnPath -ItemType Directory -Force | Out-Null
    New-Item -Path $serviceTesterPath -ItemType Directory -Force | Out-Null
    New-Item -Path $servicePermissionsPath -ItemType Directory -Force | Out-Null
    Write-Success "Directories created successfully"
} catch {
    Write-Fail "Failed to create directories: $_"
    exit 1
}

# Create a simple dummy executable (just copies cmd.exe for testing)
Write-Info "Creating service executables..."

$serviceTesterExe = "$serviceTesterPath\ServiceTester.exe"
$servicePermissionsExe = "$servicePermissionsPath\ServicePermissions.exe"

try {
    # Copy cmd.exe as a placeholder service executable
    Copy-Item -Path "C:\Windows\System32\cmd.exe" -Destination $serviceTesterExe -Force
    Copy-Item -Path "C:\Windows\System32\cmd.exe" -Destination $servicePermissionsExe -Force
    Write-Success "Service executables created"
} catch {
    Write-Fail "Failed to create executables: $_"
    exit 1
}

# ========================================
# 1. Create ServiceTester with Unquoted Service Path
# ========================================
Write-Info "`nCreating ServiceTester (Unquoted Path Vulnerability)..."

$serviceName1 = "ServiceTester"
$displayName1 = "Service Tester Application"
$description1 = "Vulnerable service with unquoted service path for testing"

# Remove service if it already exists
if (Get-Service -Name $serviceName1 -ErrorAction SilentlyContinue) {
    Write-Warn "Service $serviceName1 already exists. Removing..."
    Stop-Service -Name $serviceName1 -Force -ErrorAction SilentlyContinue
    sc.exe delete $serviceName1 | Out-Null
    Start-Sleep -Seconds 2
}

# Create service with UNQUOTED path (the vulnerability)
$unquotedPath = "$serviceTesterPath\ServiceTester.exe"
Write-Info "Creating service with unquoted path: $unquotedPath"

$createResult = sc.exe create $serviceName1 binPath= "$unquotedPath" start= demand DisplayName= "$displayName1"
if ($LASTEXITCODE -eq 0) {
    Write-Success "ServiceTester created successfully"
    
    # Set description
    sc.exe description $serviceName1 "$description1" | Out-Null
    
    Write-Info "Unquoted path vulnerability details:"
    Write-Host "  Original Path: $unquotedPath" -ForegroundColor White
    Write-Host "  Windows will try these paths in order:" -ForegroundColor White
    Write-Host "    1. C:\Program.exe" -ForegroundColor Magenta
    Write-Host "    2. C:\Program Files\Vulnerable.exe" -ForegroundColor Magenta
    Write-Host "    3. C:\Program Files\Vulnerable Services\Service.exe" -ForegroundColor Magenta
    Write-Host "    4. $unquotedPath" -ForegroundColor Magenta
} else {
    Write-Fail "Failed to create ServiceTester"
}

# ========================================
# 2. Create ServicePermissions with Weak File Permissions
# ========================================
Write-Info "`nCreating ServicePermissions (Weak File Permissions)..."

$serviceName2 = "ServicePermissions"
$displayName2 = "Service Permissions Test"
$description2 = "Vulnerable service with weak file permissions for testing"

# Remove service if it already exists
if (Get-Service -Name $serviceName2 -ErrorAction SilentlyContinue) {
    Write-Warn "Service $serviceName2 already exists. Removing..."
    Stop-Service -Name $serviceName2 -Force -ErrorAction SilentlyContinue
    sc.exe delete $serviceName2 | Out-Null
    Start-Sleep -Seconds 2
}

# Create service with QUOTED path (secure)
$quotedPath = "`"$servicePermissionsExe`""
Write-Info "Creating service with quoted path: $quotedPath"

$createResult = sc.exe create $serviceName2 binPath= "$quotedPath" start= demand DisplayName= "$displayName2"
if ($LASTEXITCODE -eq 0) {
    Write-Success "ServicePermissions created successfully"
    
    # Set description
    sc.exe description $serviceName2 "$description2" | Out-Null
    
    # Now make the binary world-writable (THE VULNERABILITY)
    Write-Info "Setting overly permissive file permissions..."
    
    try {
        # Get current ACL
        $acl = Get-Acl $servicePermissionsExe
        
        # Add full control for Everyone
        $everyone = New-Object System.Security.Principal.SecurityIdentifier("S-1-1-0")
        $everyoneIdentity = $everyone.Translate([System.Security.Principal.NTAccount])
        $rule = New-Object System.Security.AccessControl.FileSystemAccessRule(
            $everyoneIdentity,
            "FullControl",
            "Allow"
        )
        $acl.AddAccessRule($rule)
        
        # Add full control for Authenticated Users
        $authUsers = New-Object System.Security.Principal.SecurityIdentifier("S-1-5-11")
        $authUsersIdentity = $authUsers.Translate([System.Security.Principal.NTAccount])
        $rule2 = New-Object System.Security.AccessControl.FileSystemAccessRule(
            $authUsersIdentity,
            "FullControl",
            "Allow"
        )
        $acl.AddAccessRule($rule2)
        
        # Apply the modified ACL
        Set-Acl -Path $servicePermissionsExe -AclObject $acl
        
        Write-Success "Weak permissions applied successfully"
        Write-Info "File permissions vulnerability:"
        Write-Host "  Path: $servicePermissionsExe" -ForegroundColor White
        Write-Host "  Permissions: Everyone and Authenticated Users have Full Control" -ForegroundColor Magenta
        Write-Host "  Impact: Any user can replace the service binary" -ForegroundColor Magenta
    } catch {
        Write-Fail "Failed to set weak permissions: $_"
    }
} else {
    Write-Fail "Failed to create ServicePermissions"
}

# ========================================
# Summary and Testing Instructions
# ========================================
Write-Host "`n========================================" -ForegroundColor Green
Write-Host "  Services Created Successfully!" -ForegroundColor Green
Write-Host "========================================`n" -ForegroundColor Green

Write-Host "Service Details:" -ForegroundColor Yellow
Write-Host "`n1. ServiceTester (Unquoted Path Vulnerability)" -ForegroundColor Cyan
Write-Host "   Name: $serviceName1"
Write-Host "   Path: $unquotedPath"
Write-Host "   Vulnerability: Unquoted service path with spaces"
Write-Host "   To exploit: Place malicious executable at one of the intermediate paths"

Write-Host "`n2. ServicePermissions (Weak File Permissions)" -ForegroundColor Cyan
Write-Host "   Name: $serviceName2"
Write-Host "   Path: $servicePermissionsExe"
Write-Host "   Vulnerability: Service binary is writable by all users"
Write-Host "   To exploit: Replace the service binary with a malicious one"

Write-Host "`nTesting Commands:" -ForegroundColor Yellow
Write-Host "  # View service details"
Write-Host "  sc.exe qc $serviceName1" -ForegroundColor White
Write-Host "  sc.exe qc $serviceName2" -ForegroundColor White
Write-Host ""
Write-Host "  # Check file permissions"
Write-Host "  icacls `"$servicePermissionsExe`"" -ForegroundColor White
Write-Host ""
Write-Host "  # Find unquoted service paths (PowerShell)"
Write-Host "  Get-WmiObject win32_service | Where-Object {`$_.PathName -notlike '*`"*' -and `$_.PathName -like '* *'} | Select Name,PathName" -ForegroundColor White
Write-Host ""
Write-Host "  # Find writable service binaries (PowerShell)"
Write-Host "  Get-Service | ForEach-Object { `$_.Name }" -ForegroundColor White

Write-Host "`nCleanup Commands:" -ForegroundColor Yellow
Write-Host "  # Remove services"
Write-Host "  sc.exe delete $serviceName1" -ForegroundColor White
Write-Host "  sc.exe delete $serviceName2" -ForegroundColor White
Write-Host "  # Remove directory"
Write-Host "  Remove-Item -Path `"$vulnPath`" -Recurse -Force" -ForegroundColor White

Write-Host "`n" -ForegroundColor Yellow
Write-Warn "REMEMBER: These are VULNERABLE services for testing purposes only!"
Write-Warn "Only use in isolated lab environments. Remove when testing is complete."
Write-Host ""
```








```
---
- name: Run Windows vulnerability script
  hosts:
    - CEO_PC
    - INTERN_PC
  gather_facts: no

  tasks:
    - name: Copy windows_vuln.ps1 to target
      ansible.windows.win_copy:
        src: windows_vuln.ps1
        dest: C:\Temp\windows_vuln.ps1

    - name: Execute windows_vuln.ps1
      ansible.windows.win_powershell:
        script: |
          Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process -Force
          C:\Temp\windows_vuln.ps1

```



# Connection variables


```
[windows]
CEO_PC ansible_host=10.10.10.10
INTERN_PC ansible_host=10.10.10.11

[windows:vars]
ansible_connection=winrm
ansible_winrm_transport=ntlm
ansible_winrm_server_cert_validation=ignore
ansible_user=Administrator
ansible_password=Password123!
```




```
ludus:
  - vm_name: "CEO_PC"
    hostname: "CEO-PC"
    template: win2019-server-x64-template
    vlan: 10
    ip_last_octet: 10
    ram_gb: 4
    cpus: 2
    windows:
      sysprep: false
      gpos:
        - disable_defender
    domain:
      fqdn: company.local
      role: primary-dc
    testing:
      snapshot: true
      block_internet: true

  - vm_name: "INTERN_PC"
    hostname: "INTERN"
    template: win11-22h2-x64-enterprise-template
    vlan: 10
    ip_last_octet: 20
    ram_gb: 4
    cpus: 2
    windows:
      sysprep: false
    domain:
      fqdn: company.local
      role: member
    testing:
      snapshot: true
      block_internet: true

defaults:
  ad_domain_functional_level: Win2012R2
  ad_forest_functional_level: Win2012R2
  ad_domain_admin: Administrator
  ad_domain_admin_password: P@ssw0rd123!
  ad_domain_user: domainuser
  ad_domain_user_password: User123!
  ad_domain_safe_mode_password: SafeMode123!
  timezone: America/New_York
  enable_dynamic_wallpaper: true
```




```
[domain_controllers]

CEO-PC ansible_host=10.2.10.10

  

[workstations]

INTERN-PC ansible_host=10.2.10.20

  

[windows:children]

domain_controllers

workstations

  

[windows:vars]

ansible_user=josa\JosaAdmin

ansible_password=JosaAdmin

ansible_connection=winrm

ansible_winrm_transport=ntlm

ansible_winrm_server_cert_validation=ignore

ansible_port=5986

  

[all:vars]

domain_name=josa.local

domain_admin=JosaAdmin

domain_user=JosaUser
```



```
root@ludus:~/JOSA-Workshop# ansible windows -i inventory.ini -m win_ping
INTERN-PC | SUCCESS => {
    "changed": false,
    "ping": "pong"
}
CEO-PC | SUCCESS => {
    "changed": false,
    "ping": "pong"
}
```






















