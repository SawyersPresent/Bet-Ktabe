
```
kali@kali ~> nmap -sV -sC 10.10.11.48
Starting Nmap 7.94SVN ( https://nmap.org ) at 2025-01-26 10:35 EST
Nmap scan report for 10.10.11.48
Host is up (0.096s latency).
Not shown: 998 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.9p1 Ubuntu 3ubuntu0.10 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   256 48:b0:d2:c7:29:26:ae:3d:fb:b7:6b:0f:f5:4d:2a:ea (ECDSA)
|_  256 cb:61:64:b8:1b:1b:b5:ba:b8:45:86:c5:16:bb:e2:a2 (ED25519)
80/tcp open  http    Apache httpd 2.4.52 ((Ubuntu))
|_http-title: Apache2 Ubuntu Default Page: It works
|_http-server-header: Apache/2.4.52 (Ubuntu)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 60.08 seconds

```



```python
kali@kali ~ [SIGINT]> nmap -sC -sV -sU -p 161 10.10.11.48
Starting Nmap 7.94SVN ( https://nmap.org ) at 2025-01-26 10:50 EST
Nmap scan report for 10.10.11.48
Host is up (0.069s latency).

PORT    STATE SERVICE VERSION
161/udp open  snmp    SNMPv1 server; net-snmp SNMPv3 server (public)
| snmp-sysdescr: Linux underpass 5.15.0-126-generic #136-Ubuntu SMP Wed Nov 6 10:38:22 UTC 2024 x86_64
|_  System uptime: 20m42.94s (124294 timeticks)
| snmp-info: 
|   enterprise: net-snmp
|   engineIDFormat: unknown
|   engineIDData: c7ad5c4856d1cf6600000000
|   snmpEngineBoots: 31
|_  snmpEngineTime: 20m43s
Service Info: Host: UnDerPass.htb is the only daloradius server in the basin!

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 5.60 seconds

```


```python
kali@kali ~> snmpwalk -v2c -c public 10.10.11.48
iso.3.6.1.2.1.1.1.0 = STRING: "Linux underpass 5.15.0-126-generic #136-Ubuntu SMP Wed Nov 6 10:38:22 UTC 2024 x86_64"
iso.3.6.1.2.1.1.2.0 = OID: iso.3.6.1.4.1.8072.3.2.10
iso.3.6.1.2.1.1.3.0 = Timeticks: (164396) 0:27:23.96
iso.3.6.1.2.1.1.4.0 = STRING: "steve@underpass.htb"
iso.3.6.1.2.1.1.5.0 = STRING: "UnDerPass.htb is the only daloradius server in the basin!"
iso.3.6.1.2.1.1.6.0 = STRING: "Nevada, U.S.A. but not Vegas"
iso.3.6.1.2.1.1.7.0 = INTEGER: 72
iso.3.6.1.2.1.1.8.0 = Timeticks: (2) 0:00:00.02
iso.3.6.1.2.1.1.9.1.2.1 = OID: iso.3.6.1.6.3.10.3.1.1
iso.3.6.1.2.1.1.9.1.2.2 = OID: iso.3.6.1.6.3.11.3.1.1
iso.3.6.1.2.1.1.9.1.2.3 = OID: iso.3.6.1.6.3.15.2.1.1
iso.3.6.1.2.1.1.9.1.2.4 = OID: iso.3.6.1.6.3.1
iso.3.6.1.2.1.1.9.1.2.5 = OID: iso.3.6.1.6.3.16.2.2.1
iso.3.6.1.2.1.1.9.1.2.6 = OID: iso.3.6.1.2.1.49
iso.3.6.1.2.1.1.9.1.2.7 = OID: iso.3.6.1.2.1.50
iso.3.6.1.2.1.1.9.1.2.8 = OID: iso.3.6.1.2.1.4
iso.3.6.1.2.1.1.9.1.2.9 = OID: iso.3.6.1.6.3.13.3.1.3
iso.3.6.1.2.1.1.9.1.2.10 = OID: iso.3.6.1.2.1.92
iso.3.6.1.2.1.1.9.1.3.1 = STRING: "The SNMP Management Architecture MIB."
iso.3.6.1.2.1.1.9.1.3.2 = STRING: "The MIB for Message Processing and Dispatching."
iso.3.6.1.2.1.1.9.1.3.3 = STRING: "The management information definitions for the SNMP User-based Security Model."
iso.3.6.1.2.1.1.9.1.3.4 = STRING: "The MIB module for SNMPv2 entities"
iso.3.6.1.2.1.1.9.1.3.5 = STRING: "View-based Access Control Model for SNMP."
iso.3.6.1.2.1.1.9.1.3.6 = STRING: "The MIB module for managing TCP implementations"
```



```python
  from pkg_resources import DistributionNotFound, VersionConflict

  _|. _ _  _  _  _ _|_    v0.4.3                                                                                                                                                                                                             
 (_||| _) (/_(_|| (_| )                                                                                                                                                                                                                      
                                                                                                                                                                                                                                             
Extensions: php, aspx, jsp, html, js | HTTP method: GET | Threads: 25 | Wordlist size: 11460

Output File: /home/kali/reports/http_underpass.htb/_daloradius_25-01-26_11-29-43.txt

Target: http://underpass.htb/

[11:29:43] Starting: daloradius/                                                                                                                                                                                                             
[11:30:02] 200 -  221B  - /daloradius/.gitignore                            
[11:30:51] 301 -  323B  - /daloradius/app  ->  http://underpass.htb/daloradius/app/
[11:31:06] 200 -   24KB - /daloradius/ChangeLog                             
[11:31:21] 200 -    2KB - /daloradius/docker-compose.yml                    
[11:31:21] 200 -    2KB - /daloradius/Dockerfile                            
[11:31:22] 301 -  323B  - /daloradius/doc  ->  http://underpass.htb/daloradius/doc/
[11:31:46] 301 -  327B  - /daloradius/library  ->  http://underpass.htb/daloradius/library/
[11:31:47] 200 -   18KB - /daloradius/LICENSE                               
[11:32:20] 200 -   10KB - /daloradius/README.md                             
[11:32:27] 301 -  325B  - /daloradius/setup  ->  http://underpass.htb/daloradius/setup/

```


docker - compose

```python
version: "3"

services:

  radius-mysql:
    image: mariadb:10
    container_name: radius-mysql
    restart: unless-stopped
    environment:
      - MYSQL_DATABASE=radius
      - MYSQL_USER=radius
      - MYSQL_PASSWORD=radiusdbpw
      - MYSQL_ROOT_PASSWORD=radiusrootdbpw
    volumes:
      - "./data/mysql:/var/lib/mysql"

  radius:
    container_name: radius
    build:
      context: .
      dockerfile: Dockerfile-freeradius
    restart: unless-stopped
    depends_on: 
      - radius-mysql
    ports:
      - '1812:1812/udp'
      - '1813:1813/udp'
    environment:
      - MYSQL_HOST=radius-mysql
      - MYSQL_PORT=3306
      - MYSQL_DATABASE=radius
      - MYSQL_USER=radius
      - MYSQL_PASSWORD=radiusdbpw
      # Optional settings
      - DEFAULT_CLIENT_SECRET=testing123
    volumes:
      - ./data/freeradius:/data
    # If you want to disable debug output, remove the command parameter
    command: -X

  radius-web:
    build: .
    container_name: radius-web
    restart: unless-stopped
    depends_on:
      - radius
      - radius-mysql
    ports:
      - '80:80'
      - '8000:8000'
    environment:
      - MYSQL_HOST=radius-mysql
      - MYSQL_PORT=3306
      - MYSQL_DATABASE=radius
      - MYSQL_USER=radius
      - MYSQL_PASSWORD=radiusdbpw
      # Optional Settings:
      - DEFAULT_CLIENT_SECRET=testing123
      - DEFAULT_FREERADIUS_SERVER=radius
      - MAIL_SMTPADDR=127.0.0.1
      - MAIL_PORT=25
      - MAIL_FROM=root@daloradius.xdsl.by
      - MAIL_AUTH=

    volumes:
      - ./data/daloradius:/data

```


docker file


```python
# Official daloRADIUS Dockerfile
# GitHub: https://github.com/lirantal/daloradius
#
# Build image:
# 1. git pull git@github.com:lirantal/daloradius.git
# 2. docker build . -t lirantal/daloradius
#
# Run the container:
# 1. docker run -p 80:80 -p 8000:8000 -d lirantal/daloradius

FROM debian:11-slim
MAINTAINER Liran Tal <liran.tal@gmail.com>

LABEL Description="daloRADIUS Official Docker based on Debian 11 and PHP7." \
	License="GPLv2" \
	Usage="docker build . -t lirantal/daloradius && docker run -d -p 80:80 -p 8000:8000 lirantal/daloradius" \
	Version="2.0beta"

ENV DEBIAN_FRONTEND noninteractive

# default timezone
ENV TZ Europe/Vienna

# PHP install
RUN apt-get update \
  && apt-get install --yes --no-install-recommends \
  ca-certificates \
  apt-utils \
  freeradius-utils \
  tzdata \
  apache2 \
  libapache2-mod-php \
  cron \
  net-tools \
  php \
  php-common \
  php-gd \
  php-cli \
  php-curl \
  php-mail \
  php-dev \
  php-mail-mime \
  php-mbstring \
  php-db \
  php-mysql \
  php-zip \
  mariadb-client \
  default-libmysqlclient-dev \
  unzip \
  wget \
  && rm -rf /var/lib/apt/lists/*

ADD contrib/docker/operators.conf /etc/apache2/sites-available/operators.conf
ADD contrib/docker/users.conf /etc/apache2/sites-available/users.conf
RUN a2dissite 000-default.conf && \
    a2ensite users.conf operators.conf && \
    sed -i 's/Listen 80/Listen 80\nListen 8000/' /etc/apache2/ports.conf

# Create directories
# /data should be mounted as volume to avoid recreation of database entries
RUN mkdir /data
ADD . /var/www/daloradius

#RUN touch /var/www/html/library/daloradius.conf.php
RUN chown -R www-data:www-data /var/www/daloradius

# Remove the original sample web folder
RUN rm -rf /var/www/html
#
# Create daloRADIUS Log file
RUN touch /tmp/daloradius.log && chown -R www-data:www-data /tmp/daloradius.log
RUN mkdir -p /var/log/apache2/daloradius && chown -R www-data:www-data /var/log/apache2/daloradius
RUN echo "Mutex posixsem" >> /etc/apache2/apache2.conf

## Expose Web port for daloRADIUS
EXPOSE 80
EXPOSE 8000
#
## Run the script which executes Apache2 in the foreground as a running process
CMD ["/bin/bash", "/var/www/daloradius/init.sh"]

```


init.sh

```python
#!/bin/bash
# Executable process script for daloRADIUS docker image:
# GitHub: git@github.com:lirantal/daloradius.git
DALORADIUS_PATH=/var/www/daloradius
DALORADIUS_CONF_PATH=/var/www/daloradius/app/common/includes/daloradius.conf.php


function init_daloradius {

    if ! test -f "$DALORADIUS_CONF_PATH" || ! test -s "$DALORADIUS_CONF_PATH"; then
        cp "$DALORADIUS_CONF_PATH.sample" "$DALORADIUS_CONF_PATH"
    fi
    [ -n "$MYSQL_HOST" ] && sed -i "s/\$configValues\['CONFIG_DB_HOST'\] = .*;/\$configValues\['CONFIG_DB_HOST'\] = '$MYSQL_HOST';/" $DALORADIUS_CONF_PATH || MYSQL_HOST=localhost
    [ -n "$MYSQL_PORT" ] && sed -i "s/\$configValues\['CONFIG_DB_PORT'\] = .*;/\$configValues\['CONFIG_DB_PORT'\] = '$MYSQL_PORT';/" $DALORADIUS_CONF_PATH
    [ -n "$MYSQL_PASSWORD" ] && sed -i "s/\$configValues\['CONFIG_DB_PASS'\] = .*;/\$configValues\['CONFIG_DB_PASS'\] = '$MYSQL_PASSWORD';/" $DALORADIUS_CONF_PATH || MYSQL_PASSWORD=radpass
    [ -n "$MYSQL_USER" ] && sed -i "s/\$configValues\['CONFIG_DB_USER'\] = .*;/\$configValues\['CONFIG_DB_USER'\] = '$MYSQL_USER';/" $DALORADIUS_CONF_PATH || MYSQL_USER=raduser
    [ -n "$MYSQL_DATABASE" ] && sed -i "s/\$configValues\['CONFIG_DB_NAME'\] = .*;/\$configValues\['CONFIG_DB_NAME'\] = '$MYSQL_DATABASE';/" $DALORADIUS_CONF_PATH || MYSQL_DATABASE=raddb
    sed -i "s/\$configValues\['FREERADIUS_VERSION'\] = .*;/\$configValues\['FREERADIUS_VERSION'\] = '3';/" $DALORADIUS_CONF_PATH
    [ -n "$PASSWORD_MIN_LENGTH" ] && sed -i "s/\$configValues\['CONFIG_DB_PASSWORD_MIN_LENGTH'\] = .*;/\$configValues\['CONFIG_DB_PASSWORD_MIN_LENGTH'\] = '$PASSWORD_MIN_LENGTH';/" $DALORADIUS_CONF_PATH
    [ -n "$PASSWORD_MAX_LENGTH" ] && sed -i "s/\$configValues\['CONFIG_DB_PASSWORD_MAX_LENGTH'\] = .*;/\$configValues\['CONFIG_DB_PASSWORD_MAX_LENGTH'\] = '$PASSWORD_MAX_LENGTH';/" $DALORADIUS_CONF_PATH

    [ -n "$DEFAULT_FREERADIUS_SERVER" ] \
        && sed -i "s/\$configValues\['CONFIG_MAINT_TEST_USER_RADIUSSERVER'\] = .*;/\$configValues\['CONFIG_MAINT_TEST_USER_RADIUSSERVER'\] = '$DEFAULT_FREERADIUS_SERVER';/" $DALORADIUS_CONF_PATH \
        || sed -i "s/\$configValues\['CONFIG_MAINT_TEST_USER_RADIUSSERVER'\] = .*;/\$configValues\['CONFIG_MAINT_TEST_USER_RADIUSSERVER'\] = 'radius';/" $DALORADIUS_CONF_PATH
    [ -n "$DEFAULT_FREERADIUS_PORT" ] && sed -i "s/\$configValues\['CONFIG_MAINT_TEST_USER_RADIUSPORT'\] = .*;/\$configValues\['CONFIG_MAINT_TEST_USER_RADIUSPORT'\] = '$DEFAULT_FREERADIUS_PORT';/" $DALORADIUS_CONF_PATH
    [ -n "$DEFAULT_CLIENT_SECRET" ] && sed -i "s/\$configValues\['CONFIG_MAINT_TEST_USER_RADIUSSECRET'\] = .*;/\$configValues\['CONFIG_MAINT_TEST_USER_RADIUSSECRET'\] = '$DEFAULT_CLIENT_SECRET';/" $DALORADIUS_CONF_PATH

    [ -n "$MAIL_SMTPADDR" ] && sed -i "s/\$configValues\['CONFIG_MAIL_SMTPADDR'\] = .*;/\$configValues\['CONFIG_MAIL_SMTPADDR'\] = '$MAIL_SMTPADDR';/" $DALORADIUS_CONF_PATH
    [ -n "$MAIL_PORT" ] && sed -i "s/\$configValues\['CONFIG_MAIL_SMTPPORT'\] = .*;/\$configValues\['CONFIG_MAIL_SMTPPORT'\] = '$MAIL_PORT';/" $DALORADIUS_CONF_PATH
    [ -n "$MAIL_FROM" ] && sed -i "s/\$configValues\['CONFIG_MAIL_SMTPFROM'\] = .*;/\$configValues\['CONFIG_MAIL_SMTPFROM'\] = '$MAIL_FROM';/" $DALORADIUS_CONF_PATH
    [ -n "$MAIL_AUTH" ] && sed -i "s/\$configValues\['CONFIG_MAIL_SMTPAUTH'\] = .*;/\$configValues\['CONFIG_MAIL_SMTPAUTH'\] = '$MAIL_AUTH';/" $DALORADIUS_CONF_PATH
    sed -i "s/\$configValues\['CONFIG_LOG_FILE'\] = .*;/\$configValues\['CONFIG_LOG_FILE'\] = '\/tmp\/daloradius.log';/" $DALORADIUS_CONF_PATH

    echo "daloRADIUS initialization completed."
}

function init_database {
    mysql -u root -p"$MYSQL_ROOT_PASSWORD" -e "CREATE DATABASE $MYSQL_DATABASE;"
    mysql -u root -p"$MYSQL_ROOT_PASSWORD" -e "CREATE USER '$MYSQL_USER'@'localhost' IDENTIFIED BY '$MYSQL_PASSWORD';"
    mysql -u root -p"$MYSQL_ROOT_PASSWORD" -e "GRANT ALL PRIVILEGES ON $MYSQL_DATABASE.* TO '$MYSQL_USER'@'localhost'";
    mysql -h "$MYSQL_HOST" -u "$MYSQL_USER" -p"$MYSQL_PASSWORD" "$MYSQL_DATABASE" < $DALORADIUS_PATH/contrib/db/mariadb-daloradius.sql
    echo "Database initialization for daloRADIUS completed."
}

echo "Starting daloRADIUS..."

INIT_LOCK=/data/.init_done
if test -f "$INIT_LOCK"; then
    #
    if ! test -f "$DALORADIUS_CONF_PATH" || ! test -s "$DALORADIUS_CONF_PATH"; then
        echo "Init lock file exists but config file does not exist or is 0 bytes, performing initial setup of daloRADIUS."
        init_daloradius
    fi
    echo "Init lock file exists and config file exists, skipping initial setup of daloRADIUS."
else
    init_daloradius
    date > $INIT_LOCK
fi

# wait for MySQL-Server to be ready
echo -n "Waiting for mysql ($MYSQL_HOST)..."
while ! mysqladmin ping -h"$MYSQL_HOST" -p"$MYSQL_PASSWORD" --silent; do
    sleep 20
done
echo "ok"

DB_LOCK=/data/.db_init_done
if test -f "$DB_LOCK"; then
    echo "Database lock file exists, skipping initial setup of mysql database."
else
    init_database
    date > $DB_LOCK
fi

# Start Apache2 in the foreground
/usr/sbin/apachectl -DFOREGROUND -k start

```





```python
kali@kali ~> dirsearch -u http://underpass.htb/daloradius -r
/usr/lib/python3/dist-packages/dirsearch/dirsearch.py:23: DeprecationWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html
  from pkg_resources import DistributionNotFound, VersionConflict

  _|. _ _  _  _  _ _|_    v0.4.3
 (_||| _) (/_(_|| (_| )

Extensions: php, aspx, jsp, html, js | HTTP method: GET | Threads: 25 | Wordlist size: 11460

Output File: /home/kali/reports/http_underpass.htb/_daloradius_25-01-26_12-08-46.txt

Target: http://underpass.htb/

[12:08:46] Starting: daloradius/
[12:08:49] 200 -  221B  - /daloradius/.gitignore                            
[12:09:04] 301 -  323B  - /daloradius/app  ->  http://underpass.htb/daloradius/app/
Added to the queue: daloradius/app/
[12:09:11] 200 -   24KB - /daloradius/ChangeLog                             
[12:09:16] 301 -  323B  - /daloradius/doc  ->  http://underpass.htb/daloradius/doc/
Added to the queue: daloradius/doc/
[12:09:16] 200 -    2KB - /daloradius/Dockerfile                            
[12:09:16] 200 -    2KB - /daloradius/docker-compose.yml                    
[12:09:23] 301 -  327B  - /daloradius/library  ->  http://underpass.htb/daloradius/library/
Added to the queue: daloradius/library/
[12:09:23] 200 -   18KB - /daloradius/LICENSE                               
[12:09:32] 200 -   10KB - /daloradius/README.md                             
[12:09:34] 301 -  325B  - /daloradius/setup  ->  http://underpass.htb/daloradius/setup/
Added to the queue: daloradius/setup/                                       
   
[12:09:44] Starting: daloradius/app/
[12:10:03] 301 -  330B  - /daloradius/app/common  ->  http://underpass.htb/daloradius/app/common/
Added to the queue: daloradius/app/common/
[12:10:32] 301 -  329B  - /daloradius/app/users  ->  http://underpass.htb/daloradius/app/users/
Added to the queue: daloradius/app/users/                                   
[12:10:32] 302 -    0B  - /daloradius/app/users/  ->  home-main.php         
[12:10:32] 200 -    2KB - /daloradius/app/users/login.php                   
 
[12:10:36] Starting: daloradius/doc/
[12:11:03] 301 -  331B  - /daloradius/doc/install  ->  http://underpass.htb/daloradius/doc/install/
Added to the queue: daloradius/doc/install/
 
[12:11:28] Starting: daloradius/library/
 
[12:12:16] Starting: daloradius/setup/
 
[12:13:21] Starting: daloradius/app/common/
[12:13:54] 301 -  339B  - /daloradius/app/common/includes  ->  http://underpass.htb/daloradius/app/common/includes/
Added to the queue: daloradius/app/common/includes/                         
[12:13:56] 301 -  338B  - /daloradius/app/common/library  ->  http://underpass.htb/daloradius/app/common/library/
Added to the queue: daloradius/app/common/library/                          
[12:14:14] 301 -  337B  - /daloradius/app/common/static  ->  http://underpass.htb/daloradius/app/common/static/
Added to the queue: daloradius/app/common/static/                           
[12:14:16] 301 -  340B  - /daloradius/app/common/templates  ->  http://underpass.htb/daloradius/app/common/templates/
Added to the queue: daloradius/app/common/templates/                        
 
[12:14:25] Starting: daloradius/app/users/
[12:14:28] 403 -  278B  - /daloradius/app/users/.ht_wsr.txt                 
[12:14:28] 403 -  278B  - /daloradius/app/users/.htaccess.bak1              
[12:14:28] 403 -  278B  - /daloradius/app/users/.htaccess.sample
[12:14:28] 403 -  278B  - /daloradius/app/users/.htaccess.save
[12:14:28] 403 -  278B  - /daloradius/app/users/.htaccess.orig              
[12:14:28] 403 -  278B  - /daloradius/app/users/.htaccess_orig              
[12:14:28] 403 -  278B  - /daloradius/app/users/.htaccessOLD
[12:14:28] 403 -  278B  - /daloradius/app/users/.htaccess_extra
[12:14:28] 403 -  278B  - /daloradius/app/users/.htaccess_sc
[12:14:28] 403 -  278B  - /daloradius/app/users/.htaccessBAK                
[12:14:28] 403 -  278B  - /daloradius/app/users/.htm                        
[12:14:28] 403 -  278B  - /daloradius/app/users/.htaccessOLD2               
[12:14:28] 403 -  278B  - /daloradius/app/users/.html                       
[12:14:28] 403 -  278B  - /daloradius/app/users/.htpasswds                  
[12:14:28] 403 -  278B  - /daloradius/app/users/.httr-oauth
[12:14:28] 403 -  278B  - /daloradius/app/users/.htpasswd_test              
[12:14:29] 403 -  278B  - /daloradius/app/users/.php                        
[12:14:58] 403 -  278B  - /daloradius/app/users/include/                    
[12:14:58] 301 -  337B  - /daloradius/app/users/include  ->  http://underpass.htb/daloradius/app/users/include/
Added to the queue: daloradius/app/users/include/                           
[12:15:00] 301 -  334B  - /daloradius/app/users/lang  ->  http://underpass.htb/daloradius/app/users/lang/
Added to the queue: daloradius/app/users/lang/                              
[12:15:01] 301 -  337B  - /daloradius/app/users/library  ->  http://underpass.htb/daloradius/app/users/library/
Added to the queue: daloradius/app/users/library/
[12:15:02] 302 -    0B  - /daloradius/app/users/logout.php  ->  login.php   
[12:15:19] 301 -  336B  - /daloradius/app/users/static  ->  http://underpass.htb/daloradius/app/users/static/
Added to the queue: daloradius/app/users/static/
 
[12:15:31] Starting: daloradius/doc/install/                                                                                                                                                                                                 
[12:15:58] 200 -    8KB - /daloradius/doc/install/INSTALL                   
 
[12:16:27] Starting: daloradius/app/common/includes/                                                                                                                                                                                         
[12:17:07] 404 -    0B  - /daloradius/app/common/includes/mail.php          
 
[12:17:38] Starting: daloradius/app/common/library/                                                                                                                                                                                          
[12:18:23] 301 -  348B  - /daloradius/app/common/library/phpmailer  ->  http://underpass.htb/daloradius/app/common/library/phpmailer/
Added to the queue: daloradius/app/common/library/phpmailer/
 
[12:18:44] Starting: daloradius/app/common/static/                                                                                                                                                                                           
[12:18:45] 301 -  340B  - /daloradius/app/common/static/js  ->  http://underpass.htb/daloradius/app/common/static/js/
Added to the queue: daloradius/app/common/static/js/                         
[12:18:47] 403 -  278B  - /daloradius/app/common/static/.ht_wsr.txt          
[12:18:47] 403 -  278B  - /daloradius/app/common/static/.htaccess.bak1       
[12:18:47] 403 -  278B  - /daloradius/app/common/static/.htaccess.orig       
[12:18:47] 403 -  278B  - /daloradius/app/common/static/.htaccess.save       
[12:18:47] 403 -  278B  - /daloradius/app/common/static/.htaccess.sample
[12:18:47] 403 -  278B  - /daloradius/app/common/static/.htaccess_extra      
[12:18:47] 403 -  278B  - /daloradius/app/common/static/.htaccess_sc
[12:18:47] 403 -  278B  - /daloradius/app/common/static/.htaccess_orig
[12:18:47] 403 -  278B  - /daloradius/app/common/static/.htaccessBAK
[12:18:47] 403 -  278B  - /daloradius/app/common/static/.htaccessOLD2        
[12:18:47] 403 -  278B  - /daloradius/app/common/static/.htaccessOLD
[12:18:47] 403 -  278B  - /daloradius/app/common/static/.html                
[12:18:47] 403 -  278B  - /daloradius/app/common/static/.htm
[12:18:47] 403 -  278B  - /daloradius/app/common/static/.httr-oauth          
[12:18:47] 403 -  278B  - /daloradius/app/common/static/.htpasswds
[12:18:47] 403 -  278B  - /daloradius/app/common/static/.htpasswd_test       
[12:18:49] 403 -  278B  - /daloradius/app/common/static/.php                 
[12:19:10] 301 -  341B  - /daloradius/app/common/static/css  ->  http://underpass.htb/daloradius/app/common/static/css/
Added to the queue: daloradius/app/common/static/css/
[12:19:18] 301 -  344B  - /daloradius/app/common/static/images  ->  http://underpass.htb/daloradius/app/common/static/images/
Added to the queue: daloradius/app/common/static/images/
[12:19:18] 302 -    0B  - /daloradius/app/common/static/images/  ->  ../../index.php
[12:19:20] 302 -    0B  - /daloradius/app/common/static/js/  ->  ../../index.php
 
[12:19:52] Starting: daloradius/app/common/templates/                                                                                                                                                                                        
 
[12:20:58] Starting: daloradius/app/users/include/                                                                                                                                                                                           
[12:21:21] 301 -  344B  - /daloradius/app/users/include/common  ->  http://underpass.htb/daloradius/app/users/include/common/
Added to the queue: daloradius/app/users/include/common/
[12:21:21] 301 -  344B  - /daloradius/app/users/include/config  ->  http://underpass.htb/daloradius/app/users/include/config/
Added to the queue: daloradius/app/users/include/config/                     
[12:21:35] 301 -  348B  - /daloradius/app/users/include/management  ->  http://underpass.htb/daloradius/app/users/include/management/
Added to the queue: daloradius/app/users/include/management/
[12:21:36] 301 -  342B  - /daloradius/app/users/include/menu  ->  http://underpass.htb/daloradius/app/users/include/menu/
Added to the queue: daloradius/app/users/include/menu/                       
 
[12:22:02] Starting: daloradius/app/users/lang/                                                                                                                                                                                              
[12:22:40] 200 -    0B  - /daloradius/app/users/lang/main.php                
 
[12:23:08] Starting: daloradius/app/users/library/                                                                                                                                                                                           
[12:23:30] 302 -    0B  - /daloradius/app/users/library/checklogin.php  ->  ../index.php
[12:23:44] 301 -  348B  - /daloradius/app/users/library/javascript  ->  http://underpass.htb/daloradius/app/users/library/javascript/
Added to the queue: daloradius/app/users/library/javascript/
 
[12:24:10] Starting: daloradius/app/users/static/                                                                                                                                                                                            
[12:24:11] 301 -  339B  - /daloradius/app/users/static/js  ->  http://underpass.htb/daloradius/app/users/static/js/
Added to the queue: daloradius/app/users/static/js/                          
[12:24:13] 403 -  278B  - /daloradius/app/users/static/.ht_wsr.txt           
[12:24:13] 403 -  278B  - /daloradius/app/users/static/.htaccess.bak1        
[12:24:13] 403 -  278B  - /daloradius/app/users/static/.htaccess.sample      
[12:24:13] 403 -  278B  - /daloradius/app/users/static/.htaccess.orig
[12:24:13] 403 -  278B  - /daloradius/app/users/static/.htaccess.save
[12:24:13] 403 -  278B  - /daloradius/app/users/static/.htaccess_sc          
[12:24:13] 403 -  278B  - /daloradius/app/users/static/.htaccess_extra
[12:24:13] 403 -  278B  - /daloradius/app/users/static/.htaccess_orig        
[12:24:13] 403 -  278B  - /daloradius/app/users/static/.htaccessBAK
[12:24:13] 403 -  278B  - /daloradius/app/users/static/.htaccessOLD
[12:24:13] 403 -  278B  - /daloradius/app/users/static/.htaccessOLD2
[12:24:13] 403 -  278B  - /daloradius/app/users/static/.htm                  
[12:24:13] 403 -  278B  - /daloradius/app/users/static/.html
[12:24:13] 403 -  278B  - /daloradius/app/users/static/.htpasswd_test        
[12:24:13] 403 -  278B  - /daloradius/app/users/static/.htpasswds
[12:24:13] 403 -  278B  - /daloradius/app/users/static/.httr-oauth
[12:24:14] 403 -  278B  - /daloradius/app/users/static/.php                  
[12:24:30] 301 -  340B  - /daloradius/app/users/static/css  ->  http://underpass.htb/daloradius/app/users/static/css/
Added to the queue: daloradius/app/users/static/css/                         
[12:24:35] 301 -  343B  - /daloradius/app/users/static/images  ->  http://underpass.htb/daloradius/app/users/static/images/
[12:24:35] 302 -    0B  - /daloradius/app/users/static/images/  ->  ../../index.php
Added to the queue: daloradius/app/users/static/images/                      
[12:24:36] 302 -    0B  - /daloradius/app/users/static/js/  ->  ../../index.php
 
[12:24:59] Starting: daloradius/app/common/library/phpmailer/                                                                                                                                                                                
 
[12:25:48] Starting: daloradius/app/common/static/js/                                                                                                                                                                                        
[12:25:51] 403 -  278B  - /daloradius/app/common/static/js/.ht_wsr.txt       
[12:25:51] 403 -  278B  - /daloradius/app/common/static/js/.htaccess_extra   
[12:25:51] 403 -  278B  - /daloradius/app/common/static/js/.htaccess.save
[12:25:51] 403 -  278B  - /daloradius/app/common/static/js/.htaccess_orig    
[12:25:51] 403 -  278B  - /daloradius/app/common/static/js/.htaccess_sc      
[12:25:51] 403 -  278B  - /daloradius/app/common/static/js/.htaccessBAK      
[12:25:51] 403 -  278B  - /daloradius/app/common/static/js/.htaccess.sample  
[12:25:51] 403 -  278B  - /daloradius/app/common/static/js/.htm
[12:25:51] 403 -  278B  - /daloradius/app/common/static/js/.htaccessOLD2
[12:25:51] 403 -  278B  - /daloradius/app/common/static/js/.htaccess.bak1    
[12:25:51] 403 -  278B  - /daloradius/app/common/static/js/.html             
[12:25:51] 403 -  278B  - /daloradius/app/common/static/js/.htaccess.orig
[12:25:51] 403 -  278B  - /daloradius/app/common/static/js/.htaccessOLD      
[12:25:51] 403 -  278B  - /daloradius/app/common/static/js/.htpasswd_test    
[12:25:51] 403 -  278B  - /daloradius/app/common/static/js/.httr-oauth
[12:25:51] 403 -  278B  - /daloradius/app/common/static/js/.htpasswds
[12:25:52] 403 -  278B  - /daloradius/app/common/static/js/.php              
 
[12:26:37] Starting: daloradius/app/common/static/css/                                                                                                                                                                                       
[12:26:40] 403 -  278B  - /daloradius/app/common/static/css/.ht_wsr.txt      
[12:26:40] 403 -  278B  - /daloradius/app/common/static/css/.htaccess.bak1   
[12:26:40] 403 -  278B  - /daloradius/app/common/static/css/.htaccess.sample 
[12:26:40] 403 -  278B  - /daloradius/app/common/static/css/.htaccess.orig   
[12:26:40] 403 -  278B  - /daloradius/app/common/static/css/.htaccess.save
[12:26:40] 403 -  278B  - /daloradius/app/common/static/css/.htaccess_extra
[12:26:40] 403 -  278B  - /daloradius/app/common/static/css/.htaccess_orig
[12:26:40] 403 -  278B  - /daloradius/app/common/static/css/.htaccessOLD     
[12:26:40] 403 -  278B  - /daloradius/app/common/static/css/.htaccess_sc
[12:26:40] 403 -  278B  - /daloradius/app/common/static/css/.htaccessBAK
[12:26:40] 403 -  278B  - /daloradius/app/common/static/css/.htaccessOLD2
[12:26:40] 403 -  278B  - /daloradius/app/common/static/css/.htm             
[12:26:40] 403 -  278B  - /daloradius/app/common/static/css/.html
[12:26:40] 403 -  278B  - /daloradius/app/common/static/css/.htpasswds       
[12:26:40] 403 -  278B  - /daloradius/app/common/static/css/.httr-oauth      
[12:26:40] 403 -  278B  - /daloradius/app/common/static/css/.htpasswd_test
[12:26:41] 403 -  278B  - /daloradius/app/common/static/css/.php             
[12:27:01] 301 -  347B  - /daloradius/app/common/static/css/icons  ->  http://underpass.htb/daloradius/app/common/static/css/icons/
Added to the queue: daloradius/app/common/static/css/icons/
 
[12:27:23] Starting: daloradius/app/common/static/images/                                                                                                                                                                                    
[12:27:26] 403 -  278B  - /daloradius/app/common/static/images/.ht_wsr.txt   
[12:27:26] 403 -  278B  - /daloradius/app/common/static/images/.htaccess.bak1
[12:27:26] 403 -  278B  - /daloradius/app/common/static/images/.htaccess.orig
[12:27:26] 403 -  278B  - /daloradius/app/common/static/images/.htaccess.save
[12:27:26] 403 -  278B  - /daloradius/app/common/static/images/.htaccess.sample
[12:27:26] 403 -  278B  - /daloradius/app/common/static/images/.htaccess_orig
[12:27:26] 403 -  278B  - /daloradius/app/common/static/images/.htaccess_sc  
[12:27:26] 403 -  278B  - /daloradius/app/common/static/images/.htaccess_extra
[12:27:26] 403 -  278B  - /daloradius/app/common/static/images/.htaccessOLD
[12:27:26] 403 -  278B  - /daloradius/app/common/static/images/.htaccessOLD2
[12:27:26] 403 -  278B  - /daloradius/app/common/static/images/.htaccessBAK
[12:27:26] 403 -  278B  - /daloradius/app/common/static/images/.htm          
[12:27:26] 403 -  278B  - /daloradius/app/common/static/images/.html         
[12:27:26] 403 -  278B  - /daloradius/app/common/static/images/.htpasswd_test
[12:27:26] 403 -  278B  - /daloradius/app/common/static/images/.htpasswds    
[12:27:26] 403 -  278B  - /daloradius/app/common/static/images/.httr-oauth
[12:27:27] 403 -  278B  - /daloradius/app/common/static/images/.php          
 
[12:28:12] Starting: daloradius/app/users/include/common/                                                                                                                                                                                    
 
[12:29:00] Starting: daloradius/app/users/include/config/                                                                                                                                                                                    
```



  

| Hash                             | Type | Result            |
| -------------------------------- | ---- | ----------------- |
| 412DD4759978ACFCC81DEAB01B382403 | md5  | underwaterfriends |






http://underpass.htb/daloradius/app/users/login.php




# Mistakes

- user
	- use dirsearch with wordlists **always** stop being a fat fucking pussy dude
	- there is a tool yknow its a webapp so obviously the next thought should be to see if it exists as a subdirectory
	- linux isnt so different from windows sometimes, when you get creds dont be afraid to spray them
- root
	- look up what your trying to exploit first
	- remember fundamentals
	- dont bruteforce think piece by piece