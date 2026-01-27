
```
Target: http://analytical.htb/

[11:38:43] Starting:
[11:38:47] 301 -  178B  - /js  ->  http://analytical.htb/js/
[11:39:38] 301 -  178B  - /css  ->  http://analytical.htb/css/
[11:39:51] 301 -  178B  - /images  ->  http://analytical.htb/images/
[11:39:51] 403 -  564B  - /images/
[11:39:54] 403 -  564B  - /js/
```

now lets grep the version by looking through the source code of the login page at `dev.analytical.htb`

```

```


priv esc CVE 2023 2640 CVE 

![[Pasted image 20231023232838.png]]

![[Pasted image 20231023232753.png]]




```
╔══════════╣ Environment
╚ Any private information inside environment variables?
HISTFILESIZE=0
MB_LDAP_BIND_DN=
LANGUAGE=en_US:en
USER=metabase
HOSTNAME=2d6236cc9038
FC_LANG=en-US
SHLVL=5
LD_LIBRARY_PATH=/opt/java/openjdk/lib/server:/opt/java/openjdk/lib:/opt/java/openjdk/../lib
HOME=/home/metabase
OLDPWD=/
MB_EMAIL_SMTP_PASSWORD=
LC_CTYPE=en_US.UTF-8
JAVA_VERSION=jdk-11.0.19+7
LOGNAME=metabase
_=linpeas.sh
MB_DB_CONNECTION_URI=
PATH=/opt/java/openjdk/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
MB_DB_PASS=
MB_JETTY_HOST=0.0.0.0
META_PASS=An4lytics_ds20223#
LANG=en_US.UTF-8
MB_LDAP_PASSWORD=
HISTSIZE=0
SHELL=/bin/sh
MB_EMAIL_SMTP_USERNAME=
MB_DB_USER=
META_USER=metalytics
LC_ALL=en_US.UTF-8
JAVA_HOME=/opt/java/openjdk
PWD=/tmp
HISTFILE=/dev/null
MB_DB_FILE=//metabase.db/metabase.db

```