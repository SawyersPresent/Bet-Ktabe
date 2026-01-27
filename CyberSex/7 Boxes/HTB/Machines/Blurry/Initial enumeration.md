
```
kali@kali ~> nmap -sC -sV 10.10.11.19
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-06-10 08:15 EDT
Nmap scan report for 10.10.11.19
Host is up (0.11s latency).
Not shown: 998 closed tcp ports (conn-refused)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.4p1 Debian 5+deb11u3 (protocol 2.0)
| ssh-hostkey:
|   3072 3e:21:d5:dc:2e:61:eb:8f:a6:3b:24:2a:b7:1c:05:d3 (RSA)
|   256 39:11:42:3f:0c:25:00:08:d7:2f:1b:51:e0:43:9d:85 (ECDSA)
|_  256 b0:6f:a0:0a:9e:df:b1:7a:49:78:86:b2:35:40:ec:95 (ED25519)
80/tcp open  http    nginx 1.18.0
|_http-title: Did not follow redirect to http://app.blurry.htb/
|_http-server-header: nginx/1.18.0
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 39.69 seconds
⏎                                                                     
```


- Look at
	- `blurry.htb`
	- `app.blurry.htb`



https://davidhamann.de/2020/04/05/exploiting-python-pickle/

https://exploit-notes.hdks.org/exploit/web/framework/python/python-pickle-rce/




```
kali@kali ~> ffuf -w /usr/share/wordlists/amass/subdomains-top1mil-20000.txt -u http://app.blurry.htb/ -H "Host: FUZZ.blurry.htb" -fs 169

        /'___\  /'___\           /'___\
       /\ \__/ /\ \__/  __  __  /\ \__/
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/
         \ \_\   \ \_\  \ \____/  \ \_\
          \/_/    \/_/   \/___/    \/_/

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://app.blurry.htb/
 :: Wordlist         : FUZZ: /usr/share/wordlists/amass/subdomains-top1mil-20000.txt
 :: Header           : Host: FUZZ.blurry.htb
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
 :: Filter           : Response size: 169
________________________________________________

files                   [Status: 200, Size: 2, Words: 1, Lines: 1, Duration: 124ms]
app                     [Status: 200, Size: 13327, Words: 382, Lines: 29, Duration: 243ms]
chat                    [Status: 200, Size: 218733, Words: 12692, Lines: 449, Duration: 466ms]
:: Progress: [20000/20000] :: Job [1/1] :: 180 req/sec :: Duration: [0:00:57] :: Errors: 0 ::

```