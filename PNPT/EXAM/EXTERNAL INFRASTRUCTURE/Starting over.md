


# OSINT



# EXTERNAL


```
kali@kali ~> ./sweep.sh 10.10.155
10.10.155.5
```


```
kali@kali ~> autorecon 10.10.155.5
[*] Scanning target 10.10.155.5
[!] [10.10.155.5/top-100-udp-ports] UDP scan requires AutoRecon be run with root privileges.
[*] [10.10.155.5/all-tcp-ports] Discovered open port tcp/80 on 10.10.155.5
[*] [10.10.155.5/all-tcp-ports] Discovered open port tcp/587 on 10.10.155.5
[*] [10.10.155.5/all-tcp-ports] Discovered open port tcp/993 on 10.10.155.5
[*] [10.10.155.5/all-tcp-ports] Discovered open port tcp/25 on 10.10.155.5
[*] [10.10.155.5/all-tcp-ports] Discovered open port tcp/443 on 10.10.155.5
[*] [10.10.155.5/all-tcp-ports] Discovered open port tcp/22 on 10.10.155.5
[*] [10.10.155.5/all-tcp-ports] Discovered open port tcp/143 on 10.10.155.5
```

```
kali@kali ~> nmap -sC -sV -Pn -T4 10.10.155.5
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-08-14 12:13 EDT
Stats: 0:00:39 elapsed; 0 hosts completed (1 up), 1 undergoing Service Scan
Service scan Timing: About 77.78% done; ETC: 12:14 (0:00:04 remaining)
Nmap scan report for 10.10.155.5
Host is up (0.27s latency).
Not shown: 991 closed tcp ports (conn-refused)
PORT    STATE SERVICE  VERSION
22/tcp  open  ssh      OpenSSH 7.6p1 Ubuntu 4ubuntu0.7 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 ca:8d:f9:d8:62:2f:b9:df:dd:c2:af:91:9a:7a:c8:18 (RSA)
|   256 74:27:39:90:00:13:ab:60:ce:ae:68:68:77:ff:d2:41 (ECDSA)
|_  256 fe:a4:f4:52:1f:01:62:08:4b:96:2d:49:f4:06:85:cb (ED25519)
25/tcp  open  smtp     Postfix smtpd
|_smtp-commands: SMTP: EHLO 521 5.5.1 Protocol error\x0D
80/tcp  open  http     nginx
|_http-title: Did not follow redirect to https://10.10.155.5/
110/tcp open  pop3     Dovecot pop3d
|_ssl-date: TLS randomness does not represent time
| ssl-cert: Subject: commonName=mail.thepastamentors.com/organizationName=mail.thepastamentors.com/stateOrProvinceName=GuangDong/countryName=CN
| Not valid before: 2021-04-05T20:22:31
|_Not valid after:  2031-04-03T20:22:31
|_pop3-capabilities: SASL UIDL STLS AUTH-RESP-CODE RESP-CODES PIPELINING CAPA TOP
143/tcp open  imap     Dovecot imapd (Ubuntu)
| ssl-cert: Subject: commonName=mail.thepastamentors.com/organizationName=mail.thepastamentors.com/stateOrProvinceName=GuangDong/countryName=CN
| Not valid before: 2021-04-05T20:22:31
|_Not valid after:  2031-04-03T20:22:31
|_imap-capabilities: post-login ENABLE ID have STARTTLS more IMAP4rev1 SASL-IR OK LOGIN-REFERRALS capabilities Pre-login IDLE LITERAL+ listed LOGINDISABLEDA0001
|_ssl-date: TLS randomness does not represent time
443/tcp open  ssl/http nginx
|_ssl-date: TLS randomness does not represent time
|_http-title: Site doesn't have a title (text/html).
| tls-nextprotoneg:
|   h2
|_  http/1.1
| ssl-cert: Subject: commonName=mail.thepastamentors.com/organizationName=mail.thepastamentors.com/stateOrProvinceName=GuangDong/countryName=CN
| Not valid before: 2021-04-05T20:22:31
|_Not valid after:  2031-04-03T20:22:31
| tls-alpn:
|   h2
|_  http/1.1
| http-robots.txt: 1 disallowed entry
|_/
587/tcp open  smtp     Postfix smtpd
|_smtp-commands: mail.thepastamentors.com, PIPELINING, SIZE 15728640, ETRN, STARTTLS, ENHANCEDSTATUSCODES, 8BITMIME, DSN, SMTPUTF8
| ssl-cert: Subject: commonName=mail.thepastamentors.com/organizationName=mail.thepastamentors.com/stateOrProvinceName=GuangDong/countryName=CN
| Not valid before: 2021-04-05T20:22:31
|_Not valid after:  2031-04-03T20:22:31
|_ssl-date: TLS randomness does not represent time
993/tcp open  ssl/imap Dovecot imapd (Ubuntu)
|_ssl-date: TLS randomness does not represent time
|_imap-capabilities: post-login ENABLE ID have AUTH=PLAIN more IMAP4rev1 SASL-IR OK LOGIN-REFERRALS capabilities Pre-login AUTH=LOGINA0001 LITERAL+ listed IDLE
| ssl-cert: Subject: commonName=mail.thepastamentors.com/organizationName=mail.thepastamentors.com/stateOrProvinceName=GuangDong/countryName=CN
| Not valid before: 2021-04-05T20:22:31
|_Not valid after:  2031-04-03T20:22:31
995/tcp open  ssl/pop3 Dovecot pop3d
|_pop3-capabilities: SASL(PLAIN LOGIN) UIDL USER AUTH-RESP-CODE RESP-CODES PIPELINING CAPA TOP
|_ssl-date: TLS randomness does not represent time
| ssl-cert: Subject: commonName=mail.thepastamentors.com/organizationName=mail.thepastamentors.com/stateOrProvinceName=GuangDong/countryName=CN
| Not valid before: 2021-04-05T20:22:31
|_Not valid after:  2031-04-03T20:22:31
Service Info: Hosts: -mail.thepastamentors.com,  mail.thepastamentors.com; OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
```


## Directory searching


```ls
kali@kali ~> dirsearch -u https://10.10.155.5/

  _|. _ _  _  _  _ _|_    v0.4.3.post1
 (_||| _) (/_(_|| (_| )

Extensions: php, aspx, jsp, html, js | HTTP method: GET | Threads: 25 | Wordlist size: 11460

Output File: /home/kali/reports/https_10.10.155.5/__24-08-14_12-18-25.txt

Target: https://10.10.155.5/

[12:18:25] Starting:
[12:18:30] 403 -  564B  - /%2e%2e;/test
[12:18:45] 301 -  178B  - /.well-known/caldav  ->  https://10.10.155.5/SOGo/dav
[12:18:45] 301 -  178B  - /.well-known/carddav  ->  https://10.10.155.5/SOGo/dav
[12:19:02] 403 -  564B  - /admin/.config
[12:19:17] 403 -  564B  - /admpar/.ftppass
[12:19:17] 403 -  564B  - /admrev/.ftppass
[12:19:24] 403 -  564B  - /bitrix/.settings
[12:19:24] 403 -  564B  - /bitrix/.settings.bak
[12:19:24] 403 -  564B  - /bitrix/.settings.php
[12:19:24] 403 -  564B  - /bitrix/.settings.php.bak
[12:19:52] 403 -  564B  - /ext/.deps
[12:20:03] 200 -    5KB - /iredadmin
[12:20:09] 403 -  564B  - /lib/flex/uploader/.actionScriptProperties
[12:20:09] 403 -  564B  - /lib/flex/uploader/.project
[12:20:09] 403 -  564B  - /lib/flex/uploader/.flexProperties
[12:20:09] 403 -  564B  - /lib/flex/uploader/.settings
[12:20:09] 403 -  564B  - /lib/flex/varien/.actionScriptProperties
[12:20:09] 403 -  564B  - /lib/flex/varien/.flexLibProperties
[12:20:09] 403 -  564B  - /lib/flex/varien/.project
[12:20:09] 403 -  564B  - /lib/flex/varien/.settings
[12:20:12] 301 -  178B  - /mail  ->  https://10.10.155.5/mail/
[12:20:12] 200 -    5KB - /mail
[12:20:12] 403 -  564B  - /mailer/.env
[12:20:16] 502 -  568B  - /Microsoft-Server-ActiveSync/
[12:20:19] 401 -  590B  - /netdata
[12:20:19] 303 -    0B  - /newsletter/  ->  https://10.10.155.5/iredadmin/newsletter
[12:20:34] 403 -  564B  - /resources/.arch-internal-preview.css
[12:20:34] 403 -  564B  - /resources/sass/.sass-cache/
[12:20:34] 200 -   26B  - /robots.txt
[12:20:46] 403 -  564B  - /status
[12:20:46] 403 -  564B  - /status?full=true
[12:20:55] 403 -  564B  - /twitter/.env

Task Completed
```


### Mail directory

```ls
kali@kali ~> dirsearch -u https://10.10.155.5/mail/

  _|. _ _  _  _  _ _|_    v0.4.3.post1
 (_||| _) (/_(_|| (_| )

Extensions: php, aspx, jsp, html, js | HTTP method: GET | Threads: 25 | Wordlist size: 11460

Output File: /home/kali/reports/https_10.10.155.5/_mail__24-08-14_12-13-00.txt

Target: https://10.10.155.5/

[12:13:00] Starting: mail/
[12:13:06] 403 -  564B  - /mail/%2e%2e;/test
[12:13:36] 403 -  564B  - /mail/admin/.config
[12:13:53] 403 -  564B  - /mail/admpar/.ftppass
[12:13:53] 403 -  564B  - /mail/admrev/.ftppass
[12:14:00] 403 -  564B  - /mail/bin
[12:14:00] 403 -  564B  - /mail/bin/
[12:14:00] 403 -  564B  - /mail/bin/config.sh
[12:14:00] 403 -  564B  - /mail/bin/hostname
[12:14:00] 403 -  564B  - /mail/bin/libs
[12:14:00] 403 -  564B  - /mail/bin/reset-db.sh
[12:14:00] 403 -  564B  - /mail/bin/reset-db-prod.sh
[12:14:00] 403 -  564B  - /mail/bin/target
[12:14:00] 403 -  564B  - /mail/bin/RhoBundle
[12:14:00] 403 -  564B  - /mail/bin/tmp
[12:14:00] 403 -  564B  - /mail/bitrix/.settings
[12:14:00] 403 -  564B  - /mail/bitrix/.settings.bak
[12:14:00] 403 -  564B  - /mail/bitrix/.settings.php
[12:14:00] 403 -  564B  - /mail/bitrix/.settings.php.bak
[12:14:04] 403 -  564B  - /mail/CHANGELOG
[12:14:04] 403 -  564B  - /mail/CHANGELOG.HTML
[12:14:04] 403 -  564B  - /mail/CHANGELOG.MD
[12:14:04] 403 -  564B  - /mail/CHANGELOG.md
[12:14:04] 403 -  564B  - /mail/CHANGELOG.html
[12:14:04] 403 -  564B  - /mail/CHANGELOG.log
[12:14:04] 403 -  564B  - /mail/CHANGELOG.TXT
[12:14:04] 403 -  564B  - /mail/CHANGELOG.txt
[12:14:10] 403 -  564B  - /mail/composer.json
[12:14:10] 403 -  564B  - /mail/config
[12:14:11] 403 -  564B  - /mail/config/apc.php
[12:14:11] 403 -  564B  - /mail/config/
[12:14:11] 403 -  564B  - /mail/config/app.php
[12:14:11] 403 -  564B  - /mail/config/app.yml
[12:14:11] 403 -  564B  - /mail/config/AppData.config
[12:14:11] 403 -  564B  - /mail/config/autoload/
[12:14:11] 403 -  564B  - /mail/config/aws.yml
[12:14:11] 403 -  564B  - /mail/config/banned_words.txt
[12:14:11] 403 -  564B  - /mail/config/config.inc
[12:14:11] 403 -  564B  - /mail/config/config.ini
[12:14:11] 403 -  564B  - /mail/config/database.yml.pgsql
[12:14:11] 403 -  564B  - /mail/config/initializers/secret_token.rb
[12:14:11] 403 -  564B  - /mail/config/database.yml.sqlite3
[12:14:11] 403 -  564B  - /mail/config/database.yml~
[12:14:11] 403 -  564B  - /mail/config/master.key
[12:14:11] 403 -  564B  - /mail/config/development/
[12:14:11] 403 -  564B  - /mail/config/monkcheckout.ini
[12:14:11] 403 -  564B  - /mail/config/databases.yml
[12:14:11] 403 -  564B  - /mail/config/db.inc
[12:14:11] 403 -  564B  - /mail/config/monkdonate.ini
[12:14:11] 403 -  564B  - /mail/config/monkid.ini
[12:14:11] 403 -  564B  - /mail/config/producao.ini
[12:14:11] 403 -  564B  - /mail/config/routes.yml
[12:14:11] 403 -  564B  - /mail/config/settings.inc
[12:14:11] 403 -  564B  - /mail/config/settings.ini
[12:14:11] 403 -  564B  - /mail/config/settings.ini.cfm
[12:14:11] 403 -  564B  - /mail/config/settings.local.yml
[12:14:11] 403 -  564B  - /mail/config/settings/production.yml
[12:14:11] 403 -  564B  - /mail/config/site.php
[12:14:11] 403 -  564B  - /mail/config/xml/
[12:14:12] 200 -   79KB - /mail/composer.lock
[12:14:12] 403 -  564B  - /mail/config/database.yml
[12:14:23] 403 -  564B  - /mail/ext/.deps
[12:14:33] 403 -  564B  - /mail/INSTALL
[12:14:33] 403 -  564B  - /mail/INSTALL.HTML
[12:14:33] 403 -  564B  - /mail/INSTALL.html
[12:14:33] 403 -  564B  - /mail/INSTALL.MD
[12:14:33] 403 -  564B  - /mail/INSTALL.md
[12:14:33] 403 -  564B  - /mail/INSTALL.mysql.txt
[12:14:33] 403 -  564B  - /mail/INSTALL.pgsql
[12:14:33] 403 -  564B  - /mail/INSTALL.mysql
[12:14:33] 403 -  564B  - /mail/INSTALL.pgsql.txt
[12:14:33] 403 -  564B  - /mail/INSTALL.TXT
[12:14:33] 403 -  564B  - /mail/INSTALL.txt
[12:14:33] 403 -  564B  - /mail/INSTALL_admin
[12:14:33] 403 -  564B  - /mail/installer
[12:14:37] 403 -  564B  - /mail/lib/flex/uploader/.actionScriptProperties
[12:14:37] 403 -  564B  - /mail/lib/flex/uploader/.flexProperties
[12:14:37] 403 -  564B  - /mail/lib/flex/uploader/.project
[12:14:37] 403 -  564B  - /mail/lib/flex/uploader/.settings
[12:14:37] 403 -  564B  - /mail/lib/flex/varien/.actionScriptProperties
[12:14:37] 403 -  564B  - /mail/lib/flex/varien/.flexLibProperties
[12:14:37] 403 -  564B  - /mail/lib/flex/varien/.project
[12:14:37] 403 -  564B  - /mail/LICENSE
[12:14:37] 403 -  564B  - /mail/LICENSE.md
[12:14:37] 403 -  564B  - /mail/LICENSE.txt
[12:14:37] 403 -  564B  - /mail/lib/flex/varien/.settings
[12:14:40] 403 -  564B  - /mail/logs
[12:14:40] 403 -  564B  - /mail/logs/
[12:14:40] 403 -  564B  - /mail/logs/access.log
[12:14:40] 403 -  564B  - /mail/logs/access_log
[12:14:40] 403 -  564B  - /mail/logs/error_log
[12:14:40] 403 -  564B  - /mail/logs/error.log
[12:14:40] 403 -  564B  - /mail/logs/errors.log
[12:14:40] 403 -  564B  - /mail/logs/liferay.log
[12:14:40] 403 -  564B  - /mail/logs/mail.log
[12:14:40] 403 -  564B  - /mail/logs/proxy_access_ssl_log
[12:14:40] 403 -  564B  - /mail/logs/proxy_error_log
[12:14:40] 403 -  564B  - /mail/logs/wsadmin.traceout
[12:14:40] 403 -  564B  - /mail/logs/www-error.log
[12:14:40] 403 -  564B  - /mail/mailer/.env
[12:15:01] 301 -  178B  - /mail/plugins  ->  https://10.10.155.5/mail/plugins/
[12:15:01] 403 -  564B  - /mail/plugins/
[12:15:03] 403 -  564B  - /mail/program/
[12:15:04] 301 -  178B  - /mail/public_html  ->  https://10.10.155.5/mail/public_html/
[12:15:05] 403 -  564B  - /mail/README
[12:15:05] 403 -  564B  - /mail/README.htm
[12:15:05] 403 -  564B  - /mail/README.html
[12:15:05] 403 -  564B  - /mail/README.mkd
[12:15:05] 403 -  564B  - /mail/README.md
[12:15:05] 403 -  564B  - /mail/README.MD
[12:15:05] 403 -  564B  - /mail/README.TXT
[12:15:05] 403 -  564B  - /mail/README.txt
[12:15:05] 403 -  564B  - /mail/README_VELOCE
[12:15:06] 403 -  564B  - /mail/resources/sass/.sass-cache/
[12:15:06] 403 -  564B  - /mail/resources/.arch-internal-preview.css
[12:15:13] 301 -  178B  - /mail/skins  ->  https://10.10.155.5/mail/skins/
[12:15:23] 403 -  564B  - /mail/temp
[12:15:23] 403 -  564B  - /mail/temp/
[12:15:26] 403 -  564B  - /mail/twitter/.env
[12:15:29] 403 -  564B  - /mail/vendor/
[12:15:29] 403 -  564B  - /mail/vendor/assets/bower_components
[12:15:29] 403 -  564B  - /mail/vendor/autoload.php
[12:15:29] 403 -  564B  - /mail/vendor/composer/autoload_classmap.php
[12:15:29] 403 -  564B  - /mail/vendor/composer/autoload_files.php
[12:15:29] 403 -  564B  - /mail/vendor/composer/autoload_psr4.php
[12:15:29] 403 -  564B  - /mail/vendor/bundle
[12:15:29] 403 -  564B  - /mail/vendor/composer/autoload_namespaces.php
[12:15:29] 403 -  564B  - /mail/vendor/composer/autoload_real.php
[12:15:29] 403 -  564B  - /mail/vendor/composer/autoload_static.php
[12:15:29] 403 -  564B  - /mail/vendor/composer/ClassLoader.php
[12:15:29] 403 -  564B  - /mail/vendor/phpunit/phpunit/phpunit
[12:15:29] 403 -  564B  - /mail/vendor/composer/installed.json
[12:15:29] 403 -  564B  - /mail/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
[12:15:29] 403 -  564B  - /mail/vendor/composer/LICENSE
[12:15:29] 403 -  564B  - /mail/vendor/phpunit/phpunit/Util/PHP/eval-stdin.php
[12:15:29] 403 -  564B  - /mail/vendor/phpunit/src/Util/PHP/eval-stdin.php
[12:15:30] 403 -  564B  - /mail/vendor/phpunit/Util/PHP/eval-stdin.php

Task Completed
```



### netdata 
```
⏎                                                                                                                                                                                                                 kali@kali ~>    dirsearch -u https://10.10.155.5/netdata

  _|. _ _  _  _  _ _|_    v0.4.3.post1
 (_||| _) (/_(_|| (_| )

Extensions: php, aspx, jsp, html, js | HTTP method: GET | Threads: 25 | Wordlist size: 11460

Output File: /home/kali/reports/https_10.10.155.5/_netdata_24-08-14_12-32-53.txt

Target: https://10.10.155.5/

[12:32:53] Starting: netdata/
[12:32:58] 403 -  564B  - /netdata/%2e%2e;/test
[12:32:58] 404 -  564B  - /netdata/%2e%2e//google.com
[12:33:27] 403 -  564B  - /netdata/admin/.config
[12:33:42] 403 -  564B  - /netdata/admpar/.ftppass
[12:33:42] 403 -  564B  - /netdata/admrev/.ftppass
[12:33:49] 403 -  564B  - /netdata/bitrix/.settings
[12:33:49] 403 -  564B  - /netdata/bitrix/.settings.bak
[12:33:49] 403 -  564B  - /netdata/bitrix/.settings.php
[12:33:49] 403 -  564B  - /netdata/bitrix/.settings.php.bak
[12:34:12] 403 -  564B  - /netdata/ext/.deps
[12:34:25] 403 -  564B  - /netdata/lib/flex/uploader/.actionScriptProperties
[12:34:25] 403 -  564B  - /netdata/lib/flex/uploader/.flexProperties
[12:34:25] 403 -  564B  - /netdata/lib/flex/uploader/.project
[12:34:25] 403 -  564B  - /netdata/lib/flex/uploader/.settings
[12:34:25] 403 -  564B  - /netdata/lib/flex/varien/.actionScriptProperties
[12:34:25] 403 -  564B  - /netdata/lib/flex/varien/.flexLibProperties
[12:34:25] 403 -  564B  - /netdata/lib/flex/varien/.project
[12:34:25] 403 -  564B  - /netdata/lib/flex/varien/.settings
[12:34:32] 403 -  564B  - /netdata/mailer/.env
[12:34:54] 403 -  564B  - /netdata/resources/.arch-internal-preview.css
[12:34:54] 403 -  564B  - /netdata/resources/sass/.sass-cache/
[12:35:13] 403 -  564B  - /netdata/twitter/.env

Task Completed

```


## nikto

```
kali@kali ~> nikto -host 10.10.155.5
- Nikto v2.5.0
---------------------------------------------------------------------------
+ Target IP:          10.10.155.5
+ Target Hostname:    10.10.155.5
+ Target Port:        80
+ Start Time:         2024-08-14 12:12:32 (GMT-4)
---------------------------------------------------------------------------
+ Server: nginx
+ Root page / redirects to: https://10.10.155.5/
 - STATUS: Completed 10 requests (~0% complete, 34.7 minutes left): currently in plugin 'Test Authentication'
- STATUS: Running average: Not enough data.
 - STATUS: Completed 30 requests (~0% complete, 30.8 minutes left): currently in plugin 'Test Authentication'
- STATUS: Running average: 10 requests: 0.2737 sec.
 - STATUS: Completed 40 requests (~1% complete, 37.5 minutes left): currently in plugin 'Test Authentication'
- STATUS: Running average: 10 requests: 0.2721 sec.
+ No CGI Directories found (use '-C all' to force check all possible dirs)
 - STATUS: Completed 310 requests (~4% complete, 35.4 minutes left): currently in plugin 'HTTP Headers'
- STATUS: Running average: 100 requests: 0.31598 sec, 10 requests: 0.2813 sec.
+ .: The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type. See: https://www.netsparker.com/web-vulnerability-scanner/vulnerabilities/missing-content-type-header/
 - STATUS: Completed 2440 requests (~35% complete, 23.7 minutes left): currently in plugin 'Nikto Tests'
- STATUS: Running average: 100 requests: 0.29873 sec, 10 requests: 0.3023 sec.
  - STATUS: Completed 4570 requests (~66% complete, 12.5 minutes left): currently in plugin 'Nikto Tests'
- STATUS: Running average: 100 requests: 0.29862 sec, 10 requests: 0.3023 sec.
- STATUS: Completed 4580 requests (~66% complete, 12.4 minutes left): currently in plugin 'Nikto Tests'
- STATUS: Running average: 100 requests: 0.29852 sec, 10 requests: 0.3021 sec.
 - STATUS: Completed 5760 requests (~83% complete, 6.2 minutes left): currently in plugin 'Nikto Tests'
- STATUS: Running average: 100 requests: 0.30212 sec, 10 requests: 0.3062 sec.
 - STATUS: Completed 5770 requests (~83% complete, 6.1 minutes left): currently in plugin 'Nikto Tests'
- STATUS: Running average: 100 requests: 0.30207 sec, 10 requests: 0.3061 sec.
 - STATUS: Completed 6240 requests (~90% complete, 3.7 minutes left): currently in plugin 'Nikto Tests'
- STATUS: Running average: 100 requests: 0.29961 sec, 10 requests: 0.3033 sec.
 - STATUS: Completed 7970 requests: currently in plugin 'Nikto Tests'
- STATUS: Running average: 100 requests: 0.14575 sec, 10 requests: 0.1458 sec.
+ 8074 requests: 0 error(s) and 1 item(s) reported on remote host
+ End Time:           2024-08-14 12:51:20 (GMT-4) (2328 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested

```











![[Pasted image 20240814200957.png]]






- checklists
- playbook
- methodology