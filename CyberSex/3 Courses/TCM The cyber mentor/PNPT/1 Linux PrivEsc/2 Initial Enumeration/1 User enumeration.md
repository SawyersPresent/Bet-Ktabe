

what permissions we have, who we are, what are we capable of doing


`whoami`

`id`

`sudo -l ` will be touched upon later (?)

`cat /etc/passwd` or `cat /etc/passwd | cut -d : -f 1`


`-d <Thing here>` is the delimiter as to separate fields, so for example `root:x:0:0:root:/root:/bin/bash`, the first delimiter will be the first `:`
`-f <FETCH>` The thing we want to fetch basically in the same example `root:x:0:0:root:/root:/bin/bash`, because of the dimiliter seperating shit, the first field will be `root` the second field will be `x` the third field will be `0`


```
TCM@debian:~$ cat /etc/passwd
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/bin/sh
bin:x:2:2:bin:/bin:/bin/sh
sys:x:3:3:sys:/dev:/bin/sh
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/bin/sh
man:x:6:12:man:/var/cache/man:/bin/sh
lp:x:7:7:lp:/var/spool/lpd:/bin/sh
mail:x:8:8:mail:/var/mail:/bin/sh
news:x:9:9:news:/var/spool/news:/bin/sh
uucp:x:10:10:uucp:/var/spool/uucp:/bin/sh
proxy:x:13:13:proxy:/bin:/bin/sh
www-data:x:33:33:www-data:/var/www:/bin/sh
backup:x:34:34:backup:/var/backups:/bin/sh
list:x:38:38:Mailing List Manager:/var/list:/bin/sh
irc:x:39:39:ircd:/var/run/ircd:/bin/sh
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/bin/sh
nobody:x:65534:65534:nobody:/nonexistent:/bin/sh
libuuid:x:100:101::/var/lib/libuuid:/bin/sh
Debian-exim:x:101:103::/var/spool/exim4:/bin/false
sshd:x:102:65534::/var/run/sshd:/usr/sbin/nologin
statd:x:103:65534::/var/lib/nfs:/bin/false
TCM:x:1000:1000:user,,,:/home/user:/bin/bash
```


# Access to sensitive files


`TCM@debian:~$ cat /etc/shadow`


```
TCM@debian:~$ cat /etc/shadow
root:$6$Tb/euwmK$OXA.dwMeOAcopwBl68boTG5zi65wIHsc84OWAIye5VITLLtVlaXvRDJXET..it8r.jbrlpfZeMdwD
3B0fGxJI0:17298:0:99999:7:::
daemon:*:17298:0:99999:7:::
bin:*:17298:0:99999:7:::
sys:*:17298:0:99999:7:::
sync:*:17298:0:99999:7:::
games:*:17298:0:99999:7:::
man:*:17298:0:99999:7:::
lp:*:17298:0:99999:7:::
mail:*:17298:0:99999:7:::
news:*:17298:0:99999:7:::
uucp:*:17298:0:99999:7:::
proxy:*:17298:0:99999:7:::
www-data:*:17298:0:99999:7:::
backup:*:17298:0:99999:7:::
list:*:17298:0:99999:7:::
irc:*:17298:0:99999:7:::
gnats:*:17298:0:99999:7:::
nobody:*:17298:0:99999:7:::
libuuid:!:17298:0:99999:7:::
Debian-exim:!:17298:0:99999:7:::
sshd:*:17298:0:99999:7:::
statd:*:17299:0:99999:7:::
TCM:$6$hDHLpYuo$El6r99ivR20zrEPUnujk/DgKieYIuqvf9V7M.6t6IZzxpwxGIvhqTwciEw16y/B.7ZrxVk1LOHmVb/
xyEyoUg.:18431:0:99999:7:::
```


## Access group file

`cat /etc/group`


# Accessing history

`TCM@debian:~$ history`



```
TCM@debian:~$ history
    1  ls -al
    2  cat .bash_history 
    3  ls -al
    4  mysql -h somehost.local -uroot -ppassword123
    5  exit
    6  cd /tmp
    7  clear
    8  ifconfig
    9  netstat -antp
   10  nano myvpn.ovpn 
   11  ls
   12  cd tools/
   13  mkdir linux-exploit-suggester
   14  cd linux-exploit-suggester/
   15  nano linux-exploit-suggester.sh
   16  chmod +x linux-exploit-suggester.sh 
   17  cat /etc/issue
   18  uname -a
   19  cat /etc/lsb-release
   20  cat /etc/passwd | cut -d: -f1
   21  awk -F: '($3 == "0") {print}' /etc/passwd
   22  cat /proc/version
   23  uname -a
   24  hostname
   25  lscpu
   26  cat /etc/profile
```

lets look at line 4 `4  mysql -h somehost.local -uroot -ppassword123`, yummy lateral movement