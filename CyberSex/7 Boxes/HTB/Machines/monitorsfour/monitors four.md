
```
kali@kali 2025-12-09 18:15:24 ~> nmap -sC -sV 10.129.9.166
Starting Nmap 7.95 ( https://nmap.org ) at 2025-12-09 18:15 UTC
Nmap scan report for 10.129.9.166
Host is up (0.16s latency).
Not shown: 998 filtered tcp ports (no-response)
PORT     STATE SERVICE VERSION
80/tcp   open  http    nginx
|_http-title: Did not follow redirect to http://monitorsfour.htb/
5985/tcp open  http    Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-title: Not Found
|_http-server-header: Microsoft-HTTPAPI/2.0
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .

```

```
kali@kali 2025-12-09 18:15:35 ~> ./fscan1 -h 10.129.9.166 -nobr

   ___                              _    
  / _ \     ___  ___ _ __ __ _  ___| | __ 
 / /_\/____/ __|/ __| '__/ _` |/ __| |/ /
/ /_\\_____\__ \ (__| | | (_| | (__|   <    
\____/     |___/\___|_|  \__,_|\___|_|\_\   
                     fscan version: 1.8.4
start infoscan
10.129.9.166:80 open
[*] alive ports len is: 1
start vulscan
[*] WebTitle http://10.129.9.166       code:302 len:138    title:302 Found 跳转url: http://monitorsfour.htb/
已完成 1/1
[*] 扫描结束,耗时: 3.5056878s

```













