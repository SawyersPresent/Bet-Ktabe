

```
kali@kali ~> nmap -sC -sV -Pn 10.13.37.11
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-06-18 17:07 EDT
Stats: 0:00:22 elapsed; 0 hosts completed (1 up), 1 undergoing Connect Scan
Connect Scan Timing: About 46.02% done; ETC: 17:07 (0:00:19 remaining)
Stats: 0:00:50 elapsed; 0 hosts completed (1 up), 1 undergoing Connect Scan
Connect Scan Timing: About 80.27% done; ETC: 17:08 (0:00:11 remaining)
Nmap scan report for 10.13.37.11
Host is up (0.27s latency).
Not shown: 997 closed tcp ports (conn-refused)
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 0d:e4:41:fd:9f:a9:07:4d:25:b4:bd:5d:26:cc:4f:da (RSA)
|   256 f7:65:51:e0:39:37:2c:81:7f:b5:55:bd:63:9c:82:b5 (ECDSA)
|_  256 28:61:d3:5a:b9:39:f2:5b:d7:10:5a:67:ee:81:a8:5e (ED25519)
80/tcp   open  http    Apache httpd 2.4.29 ((Ubuntu))
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: Root of the Universe &#8211; by @lydericlefebvre &amp; @akerva_fr
|_http-generator: WordPress 5.4-alpha-47225
5000/tcp open  http    Werkzeug httpd 0.16.0 (Python 2.7.15+)
| http-auth:
| HTTP/1.0 401 UNAUTHORIZED\x0D
|_  Basic realm=Authentication Required
|_http-server-header: Werkzeug/0.16.0 Python/2.7.15+
|_http-title: Site doesn't have a title (text/html; charset=utf-8).
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 100.74 seconds

```



```
kali@kali ~> ffuf -w /usr/share/wordlists/seclists/Discovery/Web-Content/common.txt -u http://10.13.37.11/FUZZ

        /'___\  /'___\           /'___\
       /\ \__/ /\ \__/  __  __  /\ \__/
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/
         \ \_\   \ \_\  \ \____/  \ \_\
          \/_/    \/_/   \/___/    \/_/

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://10.13.37.11/FUZZ
 :: Wordlist         : FUZZ: /usr/share/wordlists/seclists/Discovery/Web-Content/common.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
________________________________________________

.htaccess               [Status: 403, Size: 276, Words: 20, Lines: 10, Duration: 2652ms]
.htpasswd               [Status: 403, Size: 276, Words: 20, Lines: 10, Duration: 2654ms]
.hta                    [Status: 403, Size: 276, Words: 20, Lines: 10, Duration: 4678ms]
backups                 [Status: 301, Size: 312, Words: 20, Lines: 10, Duration: 279ms]
dev                     [Status: 301, Size: 308, Words: 20, Lines: 10, Duration: 281ms]
index.php               [Status: 301, Size: 0, Words: 1, Lines: 1, Duration: 365ms]
javascript              [Status: 301, Size: 315, Words: 20, Lines: 10, Duration: 323ms]
scripts                 [Status: 401, Size: 458, Words: 42, Lines: 15, Duration: 286ms]
server-status           [Status: 403, Size: 276, Words: 20, Lines: 10, Duration: 278ms]
wp-admin                [Status: 301, Size: 313, Words: 20, Lines: 10, Duration: 277ms]
wp-content              [Status: 301, Size: 315, Words: 20, Lines: 10, Duration: 281ms]
wp-includes             [Status: 301, Size: 316, Words: 20, Lines: 10, Duration: 301ms]
xmlrpc.php              [Status: 405, Size: 42, Words: 6, Lines: 1, Duration: 419ms]
:: Progress: [4727/4727] :: Job [1/1] :: 126 req/sec :: Duration: [0:00:39] :: Errors: 0 ::

```


DIRSEARCH

```python
kali@kali ~> dirsearch -u http://10.13.37.11/

  _|. _ _  _  _  _ _|_    v0.4.3.post1
 (_||| _) (/_(_|| (_| )

Extensions: php, aspx, jsp, html, js | HTTP method: GET | Threads: 25 | Wordlist size: 11460

Output File: /home/kali/reports/http_10.13.37.11/__24-06-18_19-17-55.txt

Target: http://10.13.37.11/

[19:17:56] Starting:
[19:18:10] 403 -  276B  - /.htaccess_extra
[19:18:10] 403 -  276B  - /.ht_wsr.txt
[19:18:10] 403 -  276B  - /.htaccess.sample
[19:18:10] 403 -  276B  - /.htaccess.orig
[19:18:10] 403 -  276B  - /.htaccess.bak1
[19:18:10] 403 -  276B  - /.htaccess.save
[19:18:10] 403 -  276B  - /.htaccess_orig
[19:18:10] 403 -  276B  - /.htaccess_sc
[19:18:10] 403 -  276B  - /.htaccessBAK
[19:18:10] 403 -  276B  - /.htaccessOLD
[19:18:10] 403 -  276B  - /.htm
[19:18:10] 403 -  276B  - /.html
[19:18:10] 403 -  276B  - /.htpasswds
[19:18:10] 403 -  276B  - /.httr-oauth
[19:18:10] 403 -  276B  - /.htaccessOLD2
[19:18:10] 403 -  276B  - /.htpasswd_test
[19:18:14] 403 -  276B  - /.php
[19:19:05] 301 -  312B  - /backups  ->  http://10.13.37.11/backups/
[19:19:05] 403 -  276B  - /backups/
[19:19:22] 301 -  308B  - /dev  ->  http://10.13.37.11/dev/
[19:19:22] 403 -  276B  - /dev/
[19:19:38] 301 -    0B  - /index.php  ->  http://10.13.37.11/
[19:19:38] 404 -    9KB - /index.php/login/
[19:19:41] 301 -  315B  - /javascript  ->  http://10.13.37.11/javascript/
[19:19:45] 200 -    7KB - /license.txt
[19:20:16] 200 -    3KB - /readme.html
[19:20:19] 401 -  458B  - /scripts
[19:20:19] 401 -  458B  - /scripts/
[19:20:19] 401 -  458B  - /scripts/cgimail.exe
[19:20:19] 401 -  458B  - /scripts/ckeditor/ckfinder/core/connector/asp/connector.asp
[19:20:19] 401 -  458B  - /scripts/ckeditor/ckfinder/core/connector/aspx/connector.aspx
[19:20:19] 401 -  458B  - /scripts/ckeditor/ckfinder/core/connector/php/connector.php
[19:20:19] 401 -  458B  - /scripts/convert.bas
[19:20:19] 401 -  458B  - /scripts/counter.exe
[19:20:19] 401 -  458B  - /scripts/fpcount.exe
[19:20:19] 401 -  458B  - /scripts/root.exe?/c+dir
[19:20:19] 401 -  458B  - /scripts/samples/search/webhits.exe
[19:20:19] 401 -  458B  - /scripts/no-such-file.pl
[19:20:19] 401 -  458B  - /scripts/tiny_mce
[19:20:19] 401 -  458B  - /scripts/iisadmin/ism.dll?http/dir
[19:20:19] 401 -  458B  - /scripts/samples/
[19:20:19] 401 -  458B  - /scripts/setup.php
[19:20:19] 401 -  458B  - /scripts/tinymce
[19:20:19] 401 -  458B  - /scripts/tools/newdsn.exe
[19:20:19] 401 -  458B  - /scripts/tools/getdrvs.exe
[19:20:20] 403 -  276B  - /server-status/
[19:20:20] 403 -  276B  - /server-status
[19:20:48] 301 -  313B  - /wp-admin  ->  http://10.13.37.11/wp-admin/
[19:20:48] 400 -    1B  - /wp-admin/admin-ajax.php
[19:20:48] 500 -    3KB - /wp-admin/setup-config.php
[19:20:48] 302 -    0B  - /wp-admin/  ->  http://10.13.37.11/wp-login.php?redirect_to=http%3A%2F%2F10.13.37.11%2Fwp-admin%2F&reauth=1
[19:20:48] 200 -  560B  - /wp-admin/install.php
[19:20:48] 200 -    0B  - /wp-config.php
[19:20:49] 301 -  315B  - /wp-content  ->  http://10.13.37.11/wp-content/
[19:20:49] 200 -    0B  - /wp-content/
[19:20:49] 403 -  276B  - /wp-content/plugins/akismet/admin.php
[19:20:49] 403 -  276B  - /wp-content/plugins/akismet/akismet.php
[19:20:50] 403 -  276B  - /wp-content/upgrade/
[19:20:50] 403 -  276B  - /wp-content/uploads/
[19:20:50] 200 -    2KB - /wp-login.php
[19:20:50] 500 -    0B  - /wp-includes/rss-functions.php
[19:20:50] 403 -  276B  - /wp-includes/
[19:20:50] 301 -  316B  - /wp-includes  ->  http://10.13.37.11/wp-includes/
[19:20:50] 200 -    0B  - /wp-cron.php
[19:20:50] 302 -    0B  - /wp-signup.php  ->  http://10.13.37.11/wp-login.php?action=register
[19:20:52] 405 -   42B  - /xmlrpc.php

```


```
kali@kali ~> curl -d '<?xml version="1.0"?> <methodCall> <methodName>system.listMethods</methodName> <params></params> </methodCall>' http://10.13.37.11:80/xmlrpc.php
<?xml version="1.0" encoding="UTF-8"?>
<methodResponse>
  <fault>
    <value>
      <struct>
        <member>
          <name>faultCode</name>
          <value><int>-32700</int></value>
        </member>
        <member>
          <name>faultString</name>
          <value><string>parse error. not well formed</string></value>
        </member>
      </struct>
    </value>
  </fault>
</methodResponse>

```







https://otakunozoku.com/using-curl-to-debug-wordpress-xmlrpc-calls/