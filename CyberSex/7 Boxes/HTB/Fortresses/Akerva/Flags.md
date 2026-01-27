
first flag

```
<!-- Hello folks! -->
<!-- This machine is powered by @lydericlefebvre from Akerva company. -->
<!-- You have to find 8 flags on this machine. Have a nice root! -->
<!-- By the way, the first flag is: AKERVA{Ikn0w_F0rgoTTEN#CoMmeNts} -->
```



second flag

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
iso.3.6.1.2.1.25.4.2.1.5.1229 = STRING: "-c /opt/check_backup.sh"
iso.3.6.1.2.1.25.4.2.1.5.1230 = STRING: "-c /opt/check_devSite.sh"
iso.3.6.1.2.1.25.4.2.1.5.1231 = STRING: "/opt/check_backup.sh"
iso.3.6.1.2.1.25.4.2.1.5.1232 = STRING: "/opt/check_devSite.sh"
iso.3.6.1.2.1.25.4.2.1.5.1235 = STRING: "/var/www/html/dev/space_dev.py"
iso.3.6.1.2.1.25.4.2.1.5.1236 = STRING: "/var/www/html/scripts/backup_every_17minutes.sh AKERVA{IkN0w_SnMP@@@MIsconfigur@T!onS}" <---------------------- important
```