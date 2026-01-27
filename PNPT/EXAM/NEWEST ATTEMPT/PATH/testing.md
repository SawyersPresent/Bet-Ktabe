
![[Pasted image 20240815143102.png]]


![[Pasted image 20240815143130.png]]


![[Pasted image 20240815143440.png]]

![[Pasted image 20240815143857.png]]

![[Pasted image 20240815143909.png]]

![[Pasted image 20240815143949.png]]

![[Pasted image 20240815144019.png]]


![[Pasted image 20240815144115.png]]


```
kali@kali ~/pnpt> sublist3r -d thepastamentors.com

                 ____        _     _ _     _   _____
                / ___| _   _| |__ | (_)___| |_|___ / _ __
                \___ \| | | | '_ \| | / __| __| |_ \| '__|
                 ___) | |_| | |_) | | \__ \ |_ ___) | |
                |____/ \__,_|_.__/|_|_|___/\__|____/|_|

                # Coded By Ahmed Aboul-Ela - @aboul3la

[-] Enumerating subdomains now for thepastamentors.com
[-] Searching now in Baidu..
[-] Searching now in Yahoo..
[-] Searching now in Google..
[-] Searching now in Bing..
[-] Searching now in Ask..
[-] Searching now in Netcraft..
[-] Searching now in DNSdumpster..
[-] Searching now in Virustotal..
[-] Searching now in ThreatCrowd..
[-] Searching now in SSL Certificates..
[-] Searching now in PassiveDNS..
[!] Error: Virustotal probably now is blocking our requests
[-] Total Unique Subdomains Found: 1
www.thepastamentors.com
```


summer22! happens sometimes


port scanning the host 

```
kali@kali ~> nmap -sC -sV -Pn -T4 10.10.155.5
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-08-16 07:24 EDT
Nmap scan report for mail.thepastamentors.com (10.10.155.5)
Host is up (0.26s latency).
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
|_http-title: Did not follow redirect to https://mail.thepastamentors.com/
110/tcp open  pop3     Dovecot pop3d
| ssl-cert: Subject: commonName=mail.thepastamentors.com/organizationName=mail.thepastamentors.com/stateOrProvinceName=GuangDong/countryName=CN
| Not valid before: 2021-04-05T20:22:31
|_Not valid after:  2031-04-03T20:22:31
|_ssl-date: TLS randomness does not represent time
|_pop3-capabilities: RESP-CODES SASL STLS AUTH-RESP-CODE PIPELINING CAPA TOP UIDL
143/tcp open  imap     Dovecot imapd (Ubuntu)
| ssl-cert: Subject: commonName=mail.thepastamentors.com/organizationName=mail.thepastamentors.com/stateOrProvinceName=GuangDong/countryName=CN
| Not valid before: 2021-04-05T20:22:31
|_Not valid after:  2031-04-03T20:22:31
|_imap-capabilities: LOGIN-REFERRALS IMAP4rev1 have post-login LOGINDISABLEDA0001 listed IDLE capabilities more ID STARTTLS OK SASL-IR Pre-login ENABLE LITERAL+
|_ssl-date: TLS randomness does not represent time
443/tcp open  ssl/http nginx
| tls-alpn:
|   h2
|_  http/1.1
| tls-nextprotoneg:
|   h2
|_  http/1.1
|_http-title: Site doesn't have a title (text/html).
| ssl-cert: Subject: commonName=mail.thepastamentors.com/organizationName=mail.thepastamentors.com/stateOrProvinceName=GuangDong/countryName=CN
| Not valid before: 2021-04-05T20:22:31
|_Not valid after:  2031-04-03T20:22:31
| http-robots.txt: 1 disallowed entry
|_/
|_ssl-date: TLS randomness does not represent time
587/tcp open  smtp     Postfix smtpd
| ssl-cert: Subject: commonName=mail.thepastamentors.com/organizationName=mail.thepastamentors.com/stateOrProvinceName=GuangDong/countryName=CN
| Not valid before: 2021-04-05T20:22:31
|_Not valid after:  2031-04-03T20:22:31
|_ssl-date: TLS randomness does not represent time
|_smtp-commands: mail.thepastamentors.com, PIPELINING, SIZE 15728640, ETRN, STARTTLS, ENHANCEDSTATUSCODES, 8BITMIME, DSN, SMTPUTF8
993/tcp open  ssl/imap Dovecot imapd (Ubuntu)
|_imap-capabilities: LOGIN-REFERRALS IMAP4rev1 have AUTH=PLAIN post-login listed IDLE capabilities more ID SASL-IR OK AUTH=LOGINA0001 Pre-login ENABLE LITERAL+
| ssl-cert: Subject: commonName=mail.thepastamentors.com/organizationName=mail.thepastamentors.com/stateOrProvinceName=GuangDong/countryName=CN
| Not valid before: 2021-04-05T20:22:31
|_Not valid after:  2031-04-03T20:22:31
|_ssl-date: TLS randomness does not represent time
995/tcp open  ssl/pop3 Dovecot pop3d
|_ssl-date: TLS randomness does not represent time
| ssl-cert: Subject: commonName=mail.thepastamentors.com/organizationName=mail.thepastamentors.com/stateOrProvinceName=GuangDong/countryName=CN
| Not valid before: 2021-04-05T20:22:31
|_Not valid after:  2031-04-03T20:22:31
|_pop3-capabilities: RESP-CODES SASL(PLAIN LOGIN) AUTH-RESP-CODE USER PIPELINING CAPA TOP UIDL
Service Info: Hosts: -mail.thepastamentors.com,  mail.thepastamentors.com; OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 53.30 seconds

```



