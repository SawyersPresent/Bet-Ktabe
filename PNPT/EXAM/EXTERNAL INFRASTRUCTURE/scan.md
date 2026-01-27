
```
kali@kali ~> sudo nmap -sS -T4 -vv 10.10.155.0/24
Scanning 10.10.155.5 [1000 ports]
Discovered open port 80/tcp on 10.10.155.5
Discovered open port 22/tcp on 10.10.155.5
Discovered open port 995/tcp on 10.10.155.5
Discovered open port 993/tcp on 10.10.155.5
- [ ] Discovered open port 110/tcp on 10.10.155.5
Discovered open port 25/tcp on 10.10.155.5
Discovered open port 143/tcp on 10.10.155.5
Discovered open port 443/tcp on 10.10.155.5
Discovered open port 587/tcp on 10.10.155.5
Completed SYN Stealth Scan at 16:41, 4.17s elapsed (1000 total ports)
Nmap scan report for 10.10.155.5
Host is up, received echo-reply ttl 63 (0.29s latency).
Scanned at 2024-08-12 16:41:45 EDT for 5s
Not shown: 991 closed tcp ports (reset)
PORT    STATE SERVICE    REASON
22/tcp  open  ssh        syn-ack ttl 63
25/tcp  open  smtp       syn-ack ttl 63
80/tcp  open  http       syn-ack ttl 63
110/tcp open  pop3       syn-ack ttl 63
143/tcp open  imap       syn-ack ttl 63
443/tcp open  https      syn-ack ttl 63
587/tcp open  submission syn-ack ttl 63
993/tcp open  imaps      syn-ack ttl 63
995/tcp open  pop3s      syn-ack ttl 63

Read data files from: /usr/bin/../share/nmap
Nmap done: 256 IP addresses (1 host up) scanned in 21.26 seconds

```


```
kali@kali ~> nmap -sC -sV -Pn 10.10.155.5
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-08-12 21:15 EDT
Stats: 0:00:09 elapsed; 0 hosts completed (1 up), 1 undergoing Connect Scan
Connect Scan Timing: About 51.45% done; ETC: 21:15 (0:00:09 remaining)
Nmap scan report for 10.10.155.5
Host is up (0.16s latency).
Not shown: 991 closed tcp ports (conn-refused)
PORT    STATE SERVICE  VERSION
22/tcp  open  ssh      OpenSSH 7.6p1 Ubuntu 4ubuntu0.7 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 ca:8d:f9:d8:62:2f:b9:df:dd:c2:af:91:9a:7a:c8:18 (RSA)
|   256 74:27:39:90:00:13:ab:60:ce:ae:68:68:77:ff:d2:41 (ECDSA)
|_  256 fe:a4:f4:52:1f:01:62:08:4b:96:2d:49:f4:06:85:cb (ED25519)
25/tcp  open  smtp     Postfix smtpd
|_smtp-commands: SMTP: EHLO 521 5.5.1 Protocol error\x0D
80/tcp  open  http     nginx
|_http-title: Did not follow redirect to https://10.10.155.5/
110/tcp open  pop3     Dovecot pop3d
| ssl-cert: Subject: commonName=mail.thepastamentors.com/organizationName=mail.thepastamentors.com/stateOrProvinceName=GuangDong/countryName=CN
| Not valid before: 2021-04-05T20:22:31
|_Not valid after:  2031-04-03T20:22:31
|_pop3-capabilities: STLS SASL AUTH-RESP-CODE UIDL RESP-CODES CAPA PIPELINING TOP
|_ssl-date: TLS randomness does not represent time
143/tcp open  imap     Dovecot imapd (Ubuntu)
| ssl-cert: Subject: commonName=mail.thepastamentors.com/organizationName=mail.thepastamentors.com/stateOrProvinceName=GuangDong/countryName=CN
| Not valid before: 2021-04-05T20:22:31
|_Not valid after:  2031-04-03T20:22:31
|_imap-capabilities: LITERAL+ capabilities LOGINDISABLEDA0001 more ID IDLE have listed ENABLE SASL-IR Pre-login OK LOGIN-REFERRALS post-login IMAP4rev1 STARTTLS
|_ssl-date: TLS randomness does not represent time
443/tcp open  ssl/http nginx
| ssl-cert: Subject: commonName=mail.thepastamentors.com/organizationName=mail.thepastamentors.com/stateOrProvinceName=GuangDong/countryName=CN
| Not valid before: 2021-04-05T20:22:31
|_Not valid after:  2031-04-03T20:22:31
| tls-nextprotoneg:
|   h2
|_  http/1.1
|_http-title: Site doesn't have a title (text/html).
|_ssl-date: TLS randomness does not represent time
| http-robots.txt: 1 disallowed entry
|_/
| tls-alpn:
|   h2
|_  http/1.1
587/tcp open  smtp     Postfix smtpd
|_ssl-date: TLS randomness does not represent time
|_smtp-commands: mail.thepastamentors.com, PIPELINING, SIZE 15728640, ETRN, STARTTLS, ENHANCEDSTATUSCODES, 8BITMIME, DSN, SMTPUTF8
| ssl-cert: Subject: commonName=mail.thepastamentors.com/organizationName=mail.thepastamentors.com/stateOrProvinceName=GuangDong/countryName=CN
| Not valid before: 2021-04-05T20:22:31
|_Not valid after:  2031-04-03T20:22:31
993/tcp open  ssl/imap Dovecot imapd (Ubuntu)
| ssl-cert: Subject: commonName=mail.thepastamentors.com/organizationName=mail.thepastamentors.com/stateOrProvinceName=GuangDong/countryName=CN
| Not valid before: 2021-04-05T20:22:31
|_Not valid after:  2031-04-03T20:22:31
|_imap-capabilities: LITERAL+ AUTH=PLAIN have more ID IDLE AUTH=LOGINA0001 capabilities ENABLE SASL-IR Pre-login listed LOGIN-REFERRALS post-login IMAP4rev1 OK
|_ssl-date: TLS randomness does not represent time
995/tcp open  ssl/pop3 Dovecot pop3d
| ssl-cert: Subject: commonName=mail.thepastamentors.com/organizationName=mail.thepastamentors.com/stateOrProvinceName=GuangDong/countryName=CN
| Not valid before: 2021-04-05T20:22:31
|_Not valid after:  2031-04-03T20:22:31
|_ssl-date: TLS randomness does not represent time
|_pop3-capabilities: USER SASL(PLAIN LOGIN) AUTH-RESP-CODE UIDL RESP-CODES CAPA PIPELINING TOP
Service Info: Hosts: -mail.thepastamentors.com,  mail.thepastamentors.com; OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 52.56 seconds

```

```
kali@kali ~/pnpt [1]> sudo nmap -sU -Pn -T4 10.10.155.5
[sudo] password for kali:
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-08-14 02:59 EDT
Warning: 10.10.155.5 giving up on port because retransmission cap hit (6).
Nmap scan report for 10.10.155.5
Host is up (0.16s latency).
Not shown: 988 closed udp ports (port-unreach)
PORT      STATE         SERVICE
3/udp     open|filtered compressnet
23/udp    open|filtered telnet
68/udp    open|filtered dhcpc
512/udp   open|filtered biff
1046/udp  open|filtered wfremotertm
1900/udp  open|filtered upnp
7000/udp  open|filtered afs3-fileserver
32528/udp open|filtered unknown
32770/udp open|filtered sometimes-rpc4
49174/udp open|filtered unknown
49201/udp open|filtered unknown
58178/udp open|filtered unknown

Nmap done: 1 IP address (1 host up) scanned in 1051.31 seconds

```



```
kali@kali ~> dirsearch -u https://10.10.155.5/

  _|. _ _  _  _  _ _|_    v0.4.3.post1
 (_||| _) (/_(_|| (_| )

Extensions: php, aspx, jsp, html, js | HTTP method: GET | Threads: 25 | Wordlist size: 11460

Output File: /home/kali/reports/https_10.10.155.5/__24-08-12_16-43-24.txt

Target: https://10.10.155.5/

[16:43:24] Starting:
[16:43:27] 403 -  564B  - /%2e%2e;/test
[16:43:37] 301 -  178B  - /.well-known/carddav  ->  https://10.10.155.5/SOGo/dav
[16:43:37] 301 -  178B  - /.well-known/caldav  ->  https://10.10.155.5/SOGo/dav
[16:43:44] 403 -  564B  - /admin/.config
[16:43:58] 403 -  564B  - /admpar/.ftppass
[16:43:58] 403 -  564B  - /admrev/.ftppass
[16:44:03] 403 -  564B  - /bitrix/.settings
[16:44:03] 403 -  564B  - /bitrix/.settings.php.bak
[16:44:03] 403 -  564B  - /bitrix/.settings.bak
[16:44:03] 403 -  564B  - /bitrix/.settings.php
[16:44:15] 403 -  564B  - /ext/.deps
[16:44:26] 200 -    5KB - /iredadmin
[16:44:28] 403 -  564B  - /lib/flex/uploader/.actionScriptProperties
[16:44:28] 403 -  564B  - /lib/flex/uploader/.flexProperties
[16:44:28] 403 -  564B  - /lib/flex/uploader/.project
[16:44:28] 403 -  564B  - /lib/flex/varien/.actionScriptProperties
[16:44:28] 403 -  564B  - /lib/flex/varien/.flexLibProperties
[16:44:28] 403 -  564B  - /lib/flex/varien/.settings
[16:44:28] 403 -  564B  - /lib/flex/uploader/.settings
[16:44:28] 403 -  564B  - /lib/flex/varien/.project
[16:44:30] 301 -  178B  - /mail  ->  https://10.10.155.5/mail/
[16:44:30] 200 -    5KB - /mail/
[16:44:31] 403 -  564B  - /mailer/.env
[16:44:33] 502 -  568B  - /Microsoft-Server-ActiveSync/
[16:44:35] 401 -  590B  - /netdata/
[16:44:35] 303 -    0B  - /newsletter/  ->  https://10.10.155.5/iredadmin/newsletter
[16:44:45] 403 -  564B  - /resources/.arch-internal-preview.css
[16:44:45] 403 -  564B  - /resources/sass/.sass-cache/
[16:44:45] 200 -   26B  - /robots.txt
[16:44:51] 403 -  564B  - /status
[16:44:51] 403 -  564B  - /status?full=true
[16:44:56] 403 -  564B  - /twitter/.env

Task Completed
```


tried to go to dav

![[Pasted image 20240812234416.png]]



now we know its nginx


![[Pasted image 20240812235232.png]]



![[Pasted image 20240812235239.png]]





```
kali@kali ~/username-anarchy (master)> ./username-anarchy --input-file listofnames.txt > brutelist.txt
```

  

© 2023 by The Pasta Mentors  
Web Admin: [Leo Fusilli](mailto:leo@thepastamentors.com)

  

© 2023 by The Pasta Mentors  
Web Admin: [Leo Fusilli](mailto:leo@thepastamentors.com)

- brute forcing
	- new script
		- Days 
			- running
		- 10k 
			- running
		- Seasons
			- Running
		- fasttrack
			- Doesnt work not inside of it
	- iredadmin
		- firstemail pattern
			- Leo
				- common passwords
					- No hits
				- days.txt
					- Not yet
				- months.txt
					- Not yet
				- fasttrack.txt
					- Tried ig?
	- gatari's nuke
		- 10k wordlist (running)
		- fasttrack (didnt work)
		- seasons (didnt work)



what did i try

- network
	- Nmap
		- TCP and UDP
- Website
	- directory searching 
		- Mail is interesting
		- Iredadmin
			- composer?
			- SGO something?
	- subdomain
		- Nothing
	- OSINT
		- Found email pattern
		- Found list of users
		- 




# NOTHING

- i searched for subdomains
	- `site:pastamentors.com -www`
		- Returned nothing
	- `site:pastamentors.com`
		- nothing\
	- Fingerprint certificate was nothing
	- Email research + verification = nothing



  

© 2023 by The Pasta Mentors  
Web Admin: [Leo Fusilli](mailto:leo@thepastamentors.com)