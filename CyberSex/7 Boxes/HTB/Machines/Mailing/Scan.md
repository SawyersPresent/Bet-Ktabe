

```
kali@kali ~> nmap -sC -sV -Pn 10.10.11.14
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-05-28 02:28 EDT
Stats: 0:01:33 elapsed; 0 hosts completed (1 up), 1 undergoing Script Scan
NSE Timing: About 78.75% done; ETC: 02:30 (0:00:00 remaining)
Nmap scan report for 10.10.11.14
Host is up (0.15s latency).
Not shown: 990 filtered tcp ports (no-response)
PORT    STATE SERVICE       VERSION
25/tcp  open  smtp          hMailServer smtpd
| smtp-commands: mailing.htb, SIZE 20480000, AUTH LOGIN PLAIN, HELP
|_ 211 DATA HELO EHLO MAIL NOOP QUIT RCPT RSET SAML TURN VRFY
80/tcp  open  http          Microsoft IIS httpd 10.0
|_http-title: Did not follow redirect to http://mailing.htb
|_http-server-header: Microsoft-IIS/10.0
110/tcp open  pop3          hMailServer pop3d
|_pop3-capabilities: USER TOP UIDL
135/tcp open  msrpc         Microsoft Windows RPC
139/tcp open  netbios-ssn   Microsoft Windows netbios-ssn
143/tcp open  imap          hMailServer imapd
|_imap-capabilities: CAPABILITY SORT IMAP4 IMAP4rev1 CHILDREN OK IDLE completed NAMESPACE QUOTA RIGHTS=texkA0001 ACL
445/tcp open  microsoft-ds?
465/tcp open  ssl/smtp      hMailServer smtpd
|_ssl-date: TLS randomness does not represent time
| ssl-cert: Subject: commonName=mailing.htb/organizationName=Mailing Ltd/stateOrProvinceName=EU\Spain/countryName=EU
| Not valid before: 2024-02-27T18:24:10
|_Not valid after:  2029-10-06T18:24:10
| smtp-commands: mailing.htb, SIZE 20480000, AUTH LOGIN PLAIN, HELP
|_ 211 DATA HELO EHLO MAIL NOOP QUIT RCPT RSET SAML TURN VRFY
587/tcp open  smtp          hMailServer smtpd
|_ssl-date: TLS randomness does not represent time
| smtp-commands: mailing.htb, SIZE 20480000, STARTTLS, AUTH LOGIN PLAIN, HELP
|_ 211 DATA HELO EHLO MAIL NOOP QUIT RCPT RSET SAML TURN VRFY
| ssl-cert: Subject: commonName=mailing.htb/organizationName=Mailing Ltd/stateOrProvinceName=EU\Spain/countryName=EU
| Not valid before: 2024-02-27T18:24:10
|_Not valid after:  2029-10-06T18:24:10
993/tcp open  ssl/imap      hMailServer imapd
|_imap-capabilities: CAPABILITY SORT IMAP4 IMAP4rev1 CHILDREN OK IDLE completed NAMESPACE QUOTA RIGHTS=texkA0001 ACL
|_ssl-date: TLS randomness does not represent time
| ssl-cert: Subject: commonName=mailing.htb/organizationName=Mailing Ltd/stateOrProvinceName=EU\Spain/countryName=EU
| Not valid before: 2024-02-27T18:24:10
|_Not valid after:  2029-10-06T18:24:10
Service Info: Host: mailing.htb; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-security-mode:
|   3:1:1:
|_    Message signing enabled but not required
| smb2-time:
|   date: 2024-05-28T06:29:20
|_  start_date: N/A

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 100.14 seconds

```




```
kali@kali ~> autorecon 10.10.11.14
[*] Scanning target 10.10.11.14
[!] [10.10.11.14/top-100-udp-ports] UDP scan requires AutoRecon be run with root privileges.
[*] [10.10.11.14/all-tcp-ports] Discovered open port tcp/143 on 10.10.11.14
[*] [10.10.11.14/all-tcp-ports] Discovered open port tcp/587 on 10.10.11.14
[*] [10.10.11.14/all-tcp-ports] Discovered open port tcp/80 on 10.10.11.14
[*] [10.10.11.14/all-tcp-ports] Discovered open port tcp/110 on 10.10.11.14
[*] [10.10.11.14/all-tcp-ports] Discovered open port tcp/993 on 10.10.11.14
[*] [10.10.11.14/all-tcp-ports] Discovered open port tcp/25 on 10.10.11.14
[*] [10.10.11.14/all-tcp-ports] Discovered open port tcp/135 on 10.10.11.14
[*] [10.10.11.14/all-tcp-ports] Discovered open port tcp/139 on 10.10.11.14
[*] [10.10.11.14/all-tcp-ports] Discovered open port tcp/445 on 10.10.11.14
[*] [10.10.11.14/all-tcp-ports] Discovered open port tcp/47001 on 10.10.11.14
[*] 02:30:10 - There are 2 scans still running against 10.10.11.14
[*] [10.10.11.14/all-tcp-ports] Discovered open port tcp/49668 on 10.10.11.14
[*] [10.10.11.14/all-tcp-ports] Discovered open port tcp/5985 on 10.10.11.14
[*] 02:31:10 - There are 2 scans still running against 10.10.11.14
[*] [10.10.11.14/all-tcp-ports] Discovered open port tcp/49667 on 10.10.11.14
[*] [10.10.11.14/tcp/80/http/vhost-enum] The target was not a hostname, nor was a hostname provided as an option. Skipping virtual host enumeration.
[*] 02:32:10 - There are 15 scans still running against 10.10.11.14
[*] 02:33:10 - There are 6 scans still running against 10.10.11.14
[*] [10.10.11.14/all-tcp-ports] Discovered open port tcp/49669 on 10.10.11.14
[*] 02:34:10 - There are 5 scans still running against 10.10.11.14
[!] [10.10.11.14/tcp/139/netbios-ssn/smbmap] A line was longer than 64 KiB and cannot be processed. Ignoring.
[*] [10.10.11.14/all-tcp-ports] Discovered open port tcp/465 on 10.10.11.14
[*] [10.10.11.14/all-tcp-ports] Discovered open port tcp/7680 on 10.10.11.14
[*] [10.10.11.14/all-tcp-ports] Discovered open port tcp/49664 on 10.10.11.14
[*] [10.10.11.14/all-tcp-ports] Discovered open port tcp/49666 on 10.10.11.14
[*] 02:35:10 - There are 5 scans still running against 10.10.11.14
[*] [10.10.11.14/all-tcp-ports] Discovered open port tcp/5040 on 10.10.11.14
[*] 02:36:11 - There are 5 scans still running against 10.10.11.14
[*] [10.10.11.14/all-tcp-ports] Discovered open port tcp/49665 on 10.10.11.14

```