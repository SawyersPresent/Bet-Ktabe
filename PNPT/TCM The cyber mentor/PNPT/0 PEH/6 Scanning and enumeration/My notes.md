


- Computer
	- Hostname
		- Kioptrix.level1
	- Operating System
		- Redhat linux
	- Ports
		- 22 
			- SSH 
				- SSH-1.99-OpenSSH_2.9p2
		- 80 
			- Apache 1.3.20
				- Apache 1.3.20
		- 111 
			- rpcbind
		- 139 
			- smbd Samba 
				- Version 
					- Samba 2.2.1a
				- Anonymous login successful
					- IPC$
				- Comments 
					- Description
						- Samba Server
					- Group
						- Workgroup
							- MYGROUP
						- Master
							- KIOPTRIX
		- 443 
			- SSL 2.8.4 / OpenSSL 0.9.6b
		- 1024 
			- tcp RPC
	- Website
		- directories
			- manual
			- mrtg
			- test.php
			- usage
		- 




```
kali@kali ~> nmap -sC -sV -p- 192.168.244.133
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-02-15 13:20 EST
Nmap scan report for 192.168.244.133
Host is up (0.0022s latency).
Not shown: 65529 closed tcp ports (conn-refused)
PORT     STATE SERVICE     VERSION
22/tcp   open  ssh         OpenSSH 2.9p2 (protocol 1.99)
| ssh-hostkey: 
|   1024 b8:74:6c:db:fd:8b:e6:66:e9:2a:2b:df:5e:6f:64:86 (RSA1)
|   1024 8f:8e:5b:81:ed:21:ab:c1:80:e1:57:a3:3c:85:c4:71 (DSA)
|_  1024 ed:4e:a9:4a:06:14:ff:15:14:ce:da:3a:80:db:e2:81 (RSA)
|_sshv1: Server supports SSHv1
80/tcp   open  http        Apache httpd 1.3.20 ((Unix)  (Red-Hat/Linux) mod_ssl/2.8.4 OpenSSL/0.9.6b)
|_http-title: Test Page for the Apache Web Server on Red Hat Linux
| http-methods: 
|_  Potentially risky methods: TRACE
|_http-server-header: Apache/1.3.20 (Unix)  (Red-Hat/Linux) mod_ssl/2.8.4 OpenSSL/0.9.6b
111/tcp  open  rpcbind     2 (RPC #100000)
| rpcinfo: 
|   program version    port/proto  service
|   100000  2            111/tcp   rpcbind
|   100000  2            111/udp   rpcbind
|   100024  1           1024/tcp   status
|_  100024  1           1024/udp   status
139/tcp  open  netbios-ssn Samba smbd (workgroup: MYGROUP)
443/tcp  open  ssl/https   Apache/1.3.20 (Unix)  (Red-Hat/Linux) mod_ssl/2.8.4 OpenSSL/0.9.6b
|_http-server-header: Apache/1.3.20 (Unix)  (Red-Hat/Linux) mod_ssl/2.8.4 OpenSSL/0.9.6b
| sslv2: 
|   SSLv2 supported
|   ciphers: 
|     SSL2_RC4_64_WITH_MD5
|     SSL2_DES_192_EDE3_CBC_WITH_MD5
|     SSL2_RC2_128_CBC_WITH_MD5
|     SSL2_RC4_128_WITH_MD5
|     SSL2_RC4_128_EXPORT40_WITH_MD5
|     SSL2_RC2_128_CBC_EXPORT40_WITH_MD5
|_    SSL2_DES_64_CBC_WITH_MD5
|_http-title: 400 Bad Request
|_ssl-date: 2024-02-15T19:22:51+00:00; +1h01m51s from scanner time.
| ssl-cert: Subject: commonName=localhost.localdomain/organizationName=SomeOrganization/stateOrProvinceName=SomeState/countryName=--
| Not valid before: 2009-09-26T09:32:06
|_Not valid after:  2010-09-26T09:32:06
1024/tcp open  status      1 (RPC #100024)

Host script results:
|_clock-skew: 1h01m50s
|_smb2-time: Protocol negotiation failed (SMB2)
|_nbstat: NetBIOS name: KIOPTRIX, NetBIOS user: <unknown>, NetBIOS MAC: <unknown> (unknown)

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 26.95 seconds

```




```
kali@kali ~> dirsearch -u http://192.168.244.133
/usr/lib/python3/dist-packages/dirsearch/dirsearch.py:23: DeprecationWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html
  from pkg_resources import DistributionNotFound, VersionConflict

  _|. _ _  _  _  _ _|_    v0.4.3
 (_||| _) (/_(_|| (_| )

Extensions: php, aspx, jsp, html, js | HTTP method: GET | Threads: 25 | Wordlist size: 11460

Output File: /home/kali/reports/http_192.168.244.133/_24-02-15_13-27-18.txt

Target: http://192.168.244.133/

[13:27:18] Starting: 
[13:27:21] 403 -  281B  - /.ht_wsr.txt
[13:27:21] 403 -  284B  - /.htaccess.orig
[13:27:21] 403 -  284B  - /.htaccess.bak1
[13:27:21] 403 -  286B  - /.htaccess.sample
[13:27:21] 403 -  284B  - /.htaccess.save
[13:27:21] 403 -  282B  - /.htaccess_sc
[13:27:21] 403 -  284B  - /.htaccess_orig
[13:27:21] 403 -  282B  - /.htaccessBAK
[13:27:21] 403 -  282B  - /.htaccessOLD
[13:27:21] 403 -  283B  - /.htaccessOLD2
[13:27:21] 403 -  285B  - /.htaccess_extra
[13:27:21] 403 -  275B  - /.html
[13:27:21] 403 -  284B  - /.htpasswd_test
[13:27:21] 403 -  280B  - /.htpasswds
[13:27:21] 403 -  274B  - /.htm
[13:27:21] 403 -  281B  - /.httr-oauth
[13:27:39] 403 -  278B  - /cgi-bin/
[13:27:44] 403 -  278B  - /doc/api/
[13:27:44] 403 -  289B  - /doc/html/index.html
[13:27:44] 403 -  288B  - /doc/stable.version
[13:27:44] 403 -  289B  - /doc/en/changes.html
[13:27:44] 403 -  274B  - /doc/
[13:27:54] 301 -  306B  - /manual  ->  http://kioptrix.level1/manual/
[13:27:56] 200 -   17KB - /mrtg/
[13:28:11] 200 -   27B  - /test.php
[13:28:13] 301 -  305B  - /usage  ->  http://kioptrix.level1/usage/
[13:28:18] 403 -  279B  - /~operator
[13:28:18] 403 -  275B  - /~root

Task Completed

```