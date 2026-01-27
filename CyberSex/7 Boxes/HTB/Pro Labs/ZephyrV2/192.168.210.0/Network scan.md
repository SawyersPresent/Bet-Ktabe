
```
kali@kali ~> nmap -sC -sV -Pn 192.168.210.0/24
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-07-14 09:38 EDT
Stats: 0:03:05 elapsed; 0 hosts completed (64 up), 64 undergoing Connect Scan
Connect Scan Timing: About 13.17% done; ETC: 09:59 (0:18:54 remaining)
Stats: 0:05:39 elapsed; 0 hosts completed (64 up), 64 undergoing Connect Scan
Connect Scan Timing: About 60.17% done; ETC: 09:47 (0:03:36 remaining)
Stats: 0:07:14 elapsed; 0 hosts completed (64 up), 64 undergoing Connect Scan
Connect Scan Timing: About 85.11% done; ETC: 09:46 (0:01:14 remaining)
Stats: 0:10:23 elapsed; 0 hosts completed (64 up), 64 undergoing Service Scan
Service scan Timing: About 97.06% done; ETC: 09:48 (0:00:04 remaining)
Stats: 0:11:09 elapsed; 0 hosts completed (64 up), 64 undergoing Service Scan
Service scan Timing: About 97.06% done; ETC: 09:49 (0:00:05 remaining)
Stats: 0:12:40 elapsed; 0 hosts completed (64 up), 64 undergoing Script Scan
NSE Timing: About 98.75% done; ETC: 09:50 (0:00:01 remaining)
Nmap scan report for 192.168.210.0
Host is up.
All 1000 scanned ports on 192.168.210.0 are in ignored states.
Not shown: 1000 filtered tcp ports (no-response)

Nmap scan report for 192.168.210.1
Host is up (0.090s latency).
Not shown: 997 filtered tcp ports (no-response)
PORT    STATE SERVICE   VERSION
53/tcp  open  domain    Unbound 1.16.0
| dns-nsid:
|   id.server: OPNsense.localdomain
|_  bind.version: unbound 1.16.0
80/tcp  open  http      OPNsense
| fingerprint-strings:
|   FourOhFourRequest:
|     HTTP/1.0 301 Moved Permanently
|     Location: https:///nice%20ports%2C/Trinity.txt.bak
|     Content-Length: 0
|     Connection: close
|     Date: Sun, 14 Jul 2024 13:46:37 GMT
|     Server: OPNsense
|   GenericLines:
|     HTTP/1.0 400 Bad Request
|     Content-Type: text/html
|     Content-Length: 345
|     Connection: close
|     Date: Sun, 14 Jul 2024 13:46:37 GMT
|     Server: OPNsense
|     <?xml version="1.0" encoding="iso-8859-1"?>
|     <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
|     "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
|     <html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
|     <head>
|     <title>400 Bad Request</title>
|     </head>
|     <body>
|     <h1>400 Bad Request</h1>
|     </body>
|     </html>
|   GetRequest, HTTPOptions:
|     HTTP/1.0 301 Moved Permanently
|     Location: https:///
|     Content-Length: 0
|     Connection: close
|     Date: Sun, 14 Jul 2024 13:46:31 GMT
|     Server: OPNsense
|   RTSPRequest:
|     HTTP/1.0 400 Bad Request
|     Content-Type: text/html
|     Content-Length: 345
|     Connection: close
|     Date: Sun, 14 Jul 2024 13:46:31 GMT
|     Server: OPNsense
|     <?xml version="1.0" encoding="iso-8859-1"?>
|     <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
|     "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
|     <html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
|     <head>
|     <title>400 Bad Request</title>
|     </head>
|     <body>
|     <h1>400 Bad Request</h1>
|     </body>
|_    </html>
|_http-title: Did not follow redirect to https://192.168.210.1/
|_http-server-header: OPNsense
443/tcp open  ssl/https OPNsense
|_ssl-date: TLS randomness does not represent time
|_http-server-header: OPNsense
|_http-trane-info: Problem with XML parsing of /evox/about
|_http-title: Login | OPNsense
| ssl-cert: Subject: commonName=OPNsense.localdomain/organizationName=OPNsense self-signed web certificate/stateOrProvinceName=Zuid-Holland/countryName=NL
| Subject Alternative Name: DNS:OPNsense.localdomain
| Not valid before: 2022-03-11T09:13:36
|_Not valid after:  2023-04-12T09:13:36
| fingerprint-strings:
|   GetRequest:
|     HTTP/1.0 200 OK
|     Set-Cookie: PHPSESSID=4c29c3697fe1f214ee4ba5ab26220879; path=/; secure; HttpOnly
|     Set-Cookie: PHPSESSID=4c29c3697fe1f214ee4ba5ab26220879; path=/; secure; HttpOnly
|     Expires: Thu, 19 Nov 1981 08:52:00 GMT
|     Cache-Control: no-store, no-cache, must-revalidate
|     Pragma: no-cache
|     Content-Security-Policy: default-src 'self'; script-src 'self' 'unsafe-inline' 'unsafe-eval'; style-src 'self' 'unsafe-inline' 'unsafe-eval';
|     X-Frame-Options: SAMEORIGIN
|     X-Content-Type-Options: nosniff
|     X-XSS-Protection: 1; mode=block
|     Referrer-Policy: same-origin
|     Content-type: text/html; charset=UTF-8
|     Content-Length: 1823
|     Connection: close
|     Date: Sun, 14 Jul 2024 13:46:37 GMT
|     Server: OPNsense
|     <!doctype html>
|     <!--[if IE 8 ]><html lang="en" class="ie ie8 lte9 lte8 no-js"><![endif]-->
|     <!--[if IE 9 ]><html lang="en" class="ie ie9 lte9 no-js"><![endif]-->
|     <!--[if (gt IE 9)|!(IE)]><!--><html lang="
|   HTTPOptions:
|     HTTP/1.0 403 Forbidden
|     Set-Cookie: PHPSESSID=88f3df3113e0b936bcd94593c18f2d28; path=/; secure; HttpOnly
|     Set-Cookie: PHPSESSID=88f3df3113e0b936bcd94593c18f2d28; path=/; secure; HttpOnly
|     Expires: Thu, 19 Nov 1981 08:52:00 GMT
|     Cache-Control: no-store, no-cache, must-revalidate
|     Pragma: no-cache
|     Content-type: text/html; charset=UTF-8
|     Content-Length: 563
|     Connection: close
|     Date: Sun, 14 Jul 2024 13:46:43 GMT
|     Server: OPNsense
|     <html><head><title>CSRF check failed</title>
|     <script>
|     document ).ready(function() {
|     $.ajaxSetup({
|     'beforeSend': function(xhr) {
|     xhr.setRequestHeader("X-CSRFToken", "QUc2MVlnOGgrU05teWpSNVRxZTk0dz09" );
|     </script>
|     </head>
|     <body>
|_    <p>CSRF check failed. Your form s
2 services unrecognized despite returning data. If you know the service/version, please submit the following fingerprints at https://nmap.org/cgi-bin/submit.cgi?new-service :
==============NEXT SERVICE FINGERPRINT (SUBMIT INDIVIDUALLY)==============
SF-Port80-TCP:V=7.94SVN%I=7%D=7/14%Time=6693D6B6%P=x86_64-pc-linux-gnu%r(G
SF:etRequest,94,"HTTP/1\.0\x20301\x20Moved\x20Permanently\r\nLocation:\x20
SF:https:///\r\nContent-Length:\x200\r\nConnection:\x20close\r\nDate:\x20S
SF:un,\x2014\x20Jul\x202024\x2013:46:31\x20GMT\r\nServer:\x20OPNsense\r\n\
SF:r\n")%r(HTTPOptions,94,"HTTP/1\.0\x20301\x20Moved\x20Permanently\r\nLoc
SF:ation:\x20https:///\r\nContent-Length:\x200\r\nConnection:\x20close\r\n
SF:Date:\x20Sun,\x2014\x20Jul\x202024\x2013:46:31\x20GMT\r\nServer:\x20OPN
SF:sense\r\n\r\n")%r(RTSPRequest,1ED,"HTTP/1\.0\x20400\x20Bad\x20Request\r
SF:\nContent-Type:\x20text/html\r\nContent-Length:\x20345\r\nConnection:\x
SF:20close\r\nDate:\x20Sun,\x2014\x20Jul\x202024\x2013:46:31\x20GMT\r\nSer
SF:ver:\x20OPNsense\r\n\r\n<\?xml\x20version=\"1\.0\"\x20encoding=\"iso-88
SF:59-1\"\?>\n<!DOCTYPE\x20html\x20PUBLIC\x20\"-//W3C//DTD\x20XHTML\x201\.
SF:0\x20Transitional//EN\"\n\x20\x20\x20\x20\x20\x20\x20\x20\x20\"http://w
SF:ww\.w3\.org/TR/xhtml1/DTD/xhtml1-transitional\.dtd\">\n<html\x20xmlns=\
SF:"http://www\.w3\.org/1999/xhtml\"\x20xml:lang=\"en\"\x20lang=\"en\">\n\
SF:x20<head>\n\x20\x20<title>400\x20Bad\x20Request</title>\n\x20</head>\n\
SF:x20<body>\n\x20\x20<h1>400\x20Bad\x20Request</h1>\n\x20</body>\n</html>
SF:\n")%r(FourOhFourRequest,B3,"HTTP/1\.0\x20301\x20Moved\x20Permanently\r
SF:\nLocation:\x20https:///nice%20ports%2C/Trinity\.txt\.bak\r\nContent-Le
SF:ngth:\x200\r\nConnection:\x20close\r\nDate:\x20Sun,\x2014\x20Jul\x20202
SF:4\x2013:46:37\x20GMT\r\nServer:\x20OPNsense\r\n\r\n")%r(GenericLines,1E
SF:D,"HTTP/1\.0\x20400\x20Bad\x20Request\r\nContent-Type:\x20text/html\r\n
SF:Content-Length:\x20345\r\nConnection:\x20close\r\nDate:\x20Sun,\x2014\x
SF:20Jul\x202024\x2013:46:37\x20GMT\r\nServer:\x20OPNsense\r\n\r\n<\?xml\x
SF:20version=\"1\.0\"\x20encoding=\"iso-8859-1\"\?>\n<!DOCTYPE\x20html\x20
SF:PUBLIC\x20\"-//W3C//DTD\x20XHTML\x201\.0\x20Transitional//EN\"\n\x20\x2
SF:0\x20\x20\x20\x20\x20\x20\x20\"http://www\.w3\.org/TR/xhtml1/DTD/xhtml1
SF:-transitional\.dtd\">\n<html\x20xmlns=\"http://www\.w3\.org/1999/xhtml\
SF:"\x20xml:lang=\"en\"\x20lang=\"en\">\n\x20<head>\n\x20\x20<title>400\x2
SF:0Bad\x20Request</title>\n\x20</head>\n\x20<body>\n\x20\x20<h1>400\x20Ba
SF:d\x20Request</h1>\n\x20</body>\n</html>\n");
==============NEXT SERVICE FINGERPRINT (SUBMIT INDIVIDUALLY)==============
SF-Port443-TCP:V=7.94SVN%T=SSL%I=7%D=7/14%Time=6693D6C1%P=x86_64-pc-linux-
SF:gnu%r(GetRequest,9D8,"HTTP/1\.0\x20200\x20OK\r\nSet-Cookie:\x20PHPSESSI
SF:D=4c29c3697fe1f214ee4ba5ab26220879;\x20path=/;\x20secure;\x20HttpOnly\r
SF:\nSet-Cookie:\x20PHPSESSID=4c29c3697fe1f214ee4ba5ab26220879;\x20path=/;
SF:\x20secure;\x20HttpOnly\r\nExpires:\x20Thu,\x2019\x20Nov\x201981\x2008:
SF:52:00\x20GMT\r\nCache-Control:\x20no-store,\x20no-cache,\x20must-revali
SF:date\r\nPragma:\x20no-cache\r\nContent-Security-Policy:\x20default-src\
SF:x20'self';\x20script-src\x20'self'\x20'unsafe-inline'\x20'unsafe-eval';
SF:\x20style-src\x20'self'\x20'unsafe-inline'\x20'unsafe-eval';\r\nX-Frame
SF:-Options:\x20SAMEORIGIN\r\nX-Content-Type-Options:\x20nosniff\r\nX-XSS-
SF:Protection:\x201;\x20mode=block\r\nReferrer-Policy:\x20same-origin\r\nC
SF:ontent-type:\x20text/html;\x20charset=UTF-8\r\nContent-Length:\x201823\
SF:r\nConnection:\x20close\r\nDate:\x20Sun,\x2014\x20Jul\x202024\x2013:46:
SF:37\x20GMT\r\nServer:\x20OPNsense\r\n\r\n<!doctype\x20html>\n<!--\[if\x2
SF:0IE\x208\x20\]><html\x20lang=\"en\"\x20class=\"ie\x20ie8\x20lte9\x20lte
SF:8\x20no-js\"><!\[endif\]-->\n<!--\[if\x20IE\x209\x20\]><html\x20lang=\"
SF:en\"\x20class=\"ie\x20ie9\x20lte9\x20no-js\"><!\[endif\]-->\n<!--\[if\x
SF:20\(gt\x20IE\x209\)\|!\(IE\)\]><!--><html\x20lang=\"")%r(HTTPOptions,3E
SF:6,"HTTP/1\.0\x20403\x20Forbidden\r\nSet-Cookie:\x20PHPSESSID=88f3df3113
SF:e0b936bcd94593c18f2d28;\x20path=/;\x20secure;\x20HttpOnly\r\nSet-Cookie
SF::\x20PHPSESSID=88f3df3113e0b936bcd94593c18f2d28;\x20path=/;\x20secure;\
SF:x20HttpOnly\r\nExpires:\x20Thu,\x2019\x20Nov\x201981\x2008:52:00\x20GMT
SF:\r\nCache-Control:\x20no-store,\x20no-cache,\x20must-revalidate\r\nPrag
SF:ma:\x20no-cache\r\nContent-type:\x20text/html;\x20charset=UTF-8\r\nCont
SF:ent-Length:\x20563\r\nConnection:\x20close\r\nDate:\x20Sun,\x2014\x20Ju
SF:l\x202024\x2013:46:43\x20GMT\r\nServer:\x20OPNsense\r\n\r\n<html><head>
SF:<title>CSRF\x20check\x20failed</title>\n\x20\x20\x20\x20\x20\x20\x20\x2
SF:0\x20\x20\x20\x20<script>\n\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20
SF:\x20\x20\x20\$\(\x20document\x20\)\.ready\(function\(\)\x20{\n\x20\x20\
SF:x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\$\.ajax
SF:Setup\({\n\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\
SF:x20\x20\x20'beforeSend':\x20function\(xhr\)\x20{\n\x20\x20\x20\x20\x20\
SF:x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20xhr\
SF:.setRequestHeader\(\"X-CSRFToken\",\x20\"QUc2MVlnOGgrU05teWpSNVRxZTk0dz
SF:09\"\x20\);\n\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x
SF:20\x20\x20\x20}\n\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x
SF:20\x20\x20}\);\n\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x2
SF:0}\);\n\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20</script>\n\x20\
SF:x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20</head>\n\x20\x20\x20\x20\x2
SF:0\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20<body>\n\x20\x20\x
SF:20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20<p>CSRF\x
SF:20check\x20failed\.\x20Your\x20form\x20s");


Nmap scan report for ZPH-SVRDC01.zsm.local (192.168.210.10)
Host is up (0.088s latency).
Not shown: 990 filtered tcp ports (no-response)
PORT     STATE SERVICE       VERSION
53/tcp   open  domain        Simple DNS Plus
88/tcp   open  kerberos-sec  Microsoft Windows Kerberos (server time: 2024-07-14 13:46:32Z)
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: zsm.local0., Site: Default-First-Site-Name)
|_ssl-date: TLS randomness does not represent time
| ssl-cert: Subject:
| Subject Alternative Name: DNS:ZPH-SVRDC01.zsm.local, DNS:zsm.local, DNS:ZSM
| Not valid before: 2024-07-14T03:11:08
|_Not valid after:  2025-07-14T03:11:08
445/tcp  open  microsoft-ds?
464/tcp  open  kpasswd5?
636/tcp  open  ssl/ldap      Microsoft Windows Active Directory LDAP (Domain: zsm.local0., Site: Default-First-Site-Name)
| ssl-cert: Subject:
| Subject Alternative Name: DNS:ZPH-SVRDC01.zsm.local, DNS:zsm.local, DNS:ZSM
| Not valid before: 2024-07-14T03:11:08
|_Not valid after:  2025-07-14T03:11:08
|_ssl-date: TLS randomness does not represent time
3268/tcp open  ldap          Microsoft Windows Active Directory LDAP (Domain: zsm.local0., Site: Default-First-Site-Name)
| ssl-cert: Subject:
| Subject Alternative Name: DNS:ZPH-SVRDC01.zsm.local, DNS:zsm.local, DNS:ZSM
| Not valid before: 2024-07-14T03:11:08
|_Not valid after:  2025-07-14T03:11:08
|_ssl-date: TLS randomness does not represent time
3269/tcp open  ssl/ldap      Microsoft Windows Active Directory LDAP (Domain: zsm.local0., Site: Default-First-Site-Name)
| ssl-cert: Subject:
| Subject Alternative Name: DNS:ZPH-SVRDC01.zsm.local, DNS:zsm.local, DNS:ZSM
| Not valid before: 2024-07-14T03:11:08
|_Not valid after:  2025-07-14T03:11:08
|_ssl-date: TLS randomness does not represent time
Service Info: Host: ZPH-SVRDC01; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-security-mode:
|   3:1:1:
|_    Message signing enabled and required
| smb2-time:
|   date: 2024-07-14T13:49:47
|_  start_date: N/A
|_clock-skew: 3s

Nmap scan report for ZPH-SVRMGMT1.zsm.local (192.168.210.11)
Host is up (0.086s latency).
Not shown: 998 filtered tcp ports (no-response)
PORT    STATE SERVICE       VERSION
135/tcp open  msrpc         Microsoft Windows RPC
445/tcp open  microsoft-ds?
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-time:
|   date: 2024-07-14T13:50:06
|_  start_date: N/A
| smb2-security-mode:
|   3:1:1:
|_    Message signing enabled but not required
|_clock-skew: 1s

Nmap scan report for ZPH-SVRCA01.zsm.local (192.168.210.12)
Host is up (0.084s latency).
Not shown: 997 filtered tcp ports (no-response)
PORT    STATE SERVICE       VERSION
80/tcp  open  http          Microsoft IIS httpd 10.0
| http-methods:
|_  Potentially risky methods: TRACE
|_http-title: IIS Windows Server
|_http-server-header: Microsoft-IIS/10.0
135/tcp open  msrpc         Microsoft Windows RPC
445/tcp open  microsoft-ds?
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-time:
|   date: 2024-07-14T13:50:16
|_  start_date: N/A
|_clock-skew: 3s
| smb2-security-mode:
|   3:1:1:
|_    Message signing enabled but not required

Nmap scan report for monitor.zsm.local (192.168.210.13)
Host is up (0.093s latency).
Not shown: 932 filtered tcp ports (no-response), 67 closed tcp ports (conn-refused)
PORT    STATE SERVICE  VERSION
443/tcp open  ssl/http nginx 1.18.0 (Ubuntu)
| tls-alpn:
|_  http/1.1
| http-robots.txt: 2 disallowed entries
|_/ /zabbix/".
| tls-nextprotoneg:
|_  http/1.1
|_http-server-header: nginx/1.18.0 (Ubuntu)
| ssl-cert: Subject: commonName=monitor.zsm.local/organizationName=Zephyr Managed Services/stateOrProvinceName=London/countryName=GB
| Not valid before: 2022-03-21T19:39:06
|_Not valid after:  2032-03-18T19:39:06
|_ssl-date: TLS randomness does not represent time
|_http-title: Zabbix
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Nmap scan report for ZPH-SVRADFS1.zsm.local (192.168.210.14)
Host is up (0.085s latency).
Not shown: 996 filtered tcp ports (no-response)
PORT    STATE SERVICE       VERSION
80/tcp  open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
135/tcp open  msrpc         Microsoft Windows RPC
443/tcp open  https?
445/tcp open  microsoft-ds?
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-time:
|   date: 2024-07-14T13:50:09
|_  start_date: N/A
| smb2-security-mode:
|   3:1:1:
|_    Message signing enabled but not required
|_clock-skew: 1s

Nmap scan report for ZPH-SVRSQL01.zsm.local (192.168.210.15)
Host is up (0.089s latency).
Not shown: 999 filtered tcp ports (no-response)
PORT    STATE SERVICE       VERSION
445/tcp open  microsoft-ds?

Host script results:
|_clock-skew: 3s
| smb2-security-mode:
|   3:1:1:
|_    Message signing enabled but not required
| smb2-time:
|   date: 2024-07-14T13:50:25
|_  start_date: N/A

Nmap scan report for ZPH-SVRCDC01.INTERNAL.ZSM.LOCAL (192.168.210.16)
Host is up (0.085s latency).
Not shown: 990 filtered tcp ports (no-response)
PORT     STATE SERVICE       VERSION
53/tcp   open  domain        Simple DNS Plus
88/tcp   open  kerberos-sec  Microsoft Windows Kerberos (server time: 2024-07-14 13:46:40Z)
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: zsm.local0., Site: Default-First-Site-Name)
|_ssl-date: TLS randomness does not represent time
| ssl-cert: Subject: commonName=ZPH-SVRCDC01.internal.zsm.local
| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1::<unsupported>, DNS:ZPH-SVRCDC01.internal.zsm.local
| Not valid before: 2023-11-23T18:42:36
|_Not valid after:  2024-11-22T18:42:36
445/tcp  open  microsoft-ds?
464/tcp  open  kpasswd5?
636/tcp  open  ssl/ldap      Microsoft Windows Active Directory LDAP (Domain: zsm.local0., Site: Default-First-Site-Name)
| ssl-cert: Subject: commonName=ZPH-SVRCDC01.internal.zsm.local
| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1::<unsupported>, DNS:ZPH-SVRCDC01.internal.zsm.local
| Not valid before: 2023-11-23T18:42:36
|_Not valid after:  2024-11-22T18:42:36
|_ssl-date: TLS randomness does not represent time
3268/tcp open  ldap          Microsoft Windows Active Directory LDAP (Domain: zsm.local0., Site: Default-First-Site-Name)
| ssl-cert: Subject: commonName=ZPH-SVRCDC01.internal.zsm.local
| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1::<unsupported>, DNS:ZPH-SVRCDC01.internal.zsm.local
| Not valid before: 2023-11-23T18:42:36
|_Not valid after:  2024-11-22T18:42:36
|_ssl-date: TLS randomness does not represent time
3269/tcp open  ssl/ldap      Microsoft Windows Active Directory LDAP (Domain: zsm.local0., Site: Default-First-Site-Name)
|_ssl-date: TLS randomness does not represent time
| ssl-cert: Subject: commonName=ZPH-SVRCDC01.internal.zsm.local
| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1::<unsupported>, DNS:ZPH-SVRCDC01.internal.zsm.local
| Not valid before: 2023-11-23T18:42:36
|_Not valid after:  2024-11-22T18:42:36
Service Info: Host: ZPH-SVRCDC01; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-security-mode:
|   3:1:1:
|_    Message signing enabled and required
|_clock-skew: 3s
| smb2-time:
|   date: 2024-07-14T13:50:27
|_  start_date: N/A

Nmap scan report for 192.168.210.17
Host is up.

```