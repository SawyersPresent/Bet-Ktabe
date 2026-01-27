
```
TCM@debian:~$ hostname
debian
TCM@debian:~$ uname -a
Linux debian 2.6.32-5-amd64 #1 SMP Tue May 13 16:34:35 UTC 2014 x86_64 GNU/Linux
TCM@debian:~$ cat /proc/version
Linux version 2.6.32-5-amd64 (Debian 2.6.32-48squeeze6) (jmm@debian.org) (gcc version 4.3.5 (D
ebian 4.3.5-4) ) #1 SMP Tue May 13 16:34:35 UTC 2014
TCM@debian:~$ lscpu
Architecture:          x86_64
CPU op-mode(s):        64-bit
CPU(s):                1
Thread(s) per core:    1
Core(s) per socket:    1
CPU socket(s):         1
NUMA node(s):          1
Vendor ID:             GenuineIntel
CPU family:            6
Model:                 79
Stepping:              1
CPU MHz:               2299.996
Hypervisor vendor:     Xen
Virtualization type:   full
L1d cache:             32K
L1i cache:             32K
L2 cache:              256K
L3 cache:              46080K
```


`hostname`

`uname -a`

`cat /proc/version`

`lscpu`


Enumerate and check this

`ps aux`

`ps aux | grep root`

`ps aux | grep <user>`

```
TCM@debian:~$ ps aux
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root         1  0.0  0.0   8396   812 ?        Ss   10:37   0:00 init [2]  
root         2  0.0  0.0      0     0 ?        S    10:37   0:00 [kthreadd]
root         3  0.0  0.0      0     0 ?        S    10:37   0:00 [migration/0]
root         4  0.0  0.0      0     0 ?        S    10:37   0:00 [ksoftirqd/0]
root         5  0.0  0.0      0     0 ?        S    10:37   0:00 [watchdog/0]
root         6  0.0  0.0      0     0 ?        S    10:37   0:00 [events/0]
root         7  0.0  0.0      0     0 ?        S    10:37   0:00 [cpuset]
root         8  0.0  0.0      0     0 ?        S    10:37   0:00 [khelper]
root         9  0.0  0.0      0     0 ?        S    10:37   0:00 [netns]
root        10  0.0  0.0      0     0 ?        S    10:37   0:00 [async/mgr]
root        11  0.0  0.0      0     0 ?        S    10:37   0:00 [pm]
root        12  0.0  0.0      0     0 ?        S    10:37   0:00 [xenwatch]
root        13  0.0  0.0      0     0 ?        S    10:37   0:00 [xenbus]
root        14  0.0  0.0      0     0 ?        S    10:37   0:00 [sync_supers]
root        15  0.0  0.0      0     0 ?        S    10:37   0:00 [bdi-default]
root        16  0.0  0.0      0     0 ?        S    10:37   0:00 [kintegrityd/0]
root        17  0.0  0.0      0     0 ?        S    10:37   0:00 [kblockd/0]
root        18  0.0  0.0      0     0 ?        S    10:37   0:00 [kacpid]
root        19  0.0  0.0      0     0 ?        S    10:37   0:00 [kacpi_notify]
root        20  0.0  0.0      0     0 ?        S    10:37   0:00 [kacpi_hotplug]
root        21  0.0  0.0      0     0 ?        S    10:37   0:00 [kseriod]
root        23  0.0  0.0      0     0 ?        S    10:37   0:00 [kondemand/0]
root        24  0.0  0.0      0     0 ?        S    10:37   0:00 [khungtaskd]
root        25  0.0  0.0      0     0 ?        S    10:37   0:00 [kswapd0]
root        26  0.0  0.0      0     0 ?        SN   10:37   0:00 [ksmd]
root        27  0.0  0.0      0     0 ?        S    10:37   0:00 [aio/0]
root        28  0.0  0.0      0     0 ?        S    10:37   0:00 [crypto/0]
root       151  0.0  0.0      0     0 ?        S    10:37   0:00 [ata/0]
root       152  0.0  0.0      0     0 ?        S    10:37   0:00 [ata_aux]
root       153  0.0  0.0      0     0 ?        S    10:37   0:00 [scsi_eh_0]
root       154  0.0  0.0      0     0 ?        S    10:37   0:00 [scsi_eh_1]
root       184  0.0  0.0      0     0 ?        S    10:37   0:00 [kjournald]
root       247  0.0  0.0      0     0 ?        S    10:37   0:00 [flush-202:0]
root       249  0.0  0.0  16916   936 ?        S<s  10:37   0:00 udevd --daemon
root       448  0.0  0.0      0     0 ?        S    10:37   0:00 [kpsmoused]
root       983  0.0  0.0  16912   856 ?        S<   10:39   0:00 udevd --daemon
root       984  0.0  0.0  16912   784 ?        S<   10:39   0:00 udevd --daemon
root      1280  0.0  0.0   6796  1020 ?        Ss   10:39   0:00 dhclient -v -pf /var/run/dhcl
daemon    1310  0.0  0.0   8136   616 ?        Ss   10:39   0:00 /sbin/portmap
statd     1342  0.0  0.0  14424   896 ?        Ss   10:39   0:00 /sbin/rpc.statd
root      1345  0.0  0.0      0     0 ?        S    10:39   0:00 [rpciod/0]
root      1347  0.0  0.0      0     0 ?        S<   10:39   0:00 [kslowd000]
root      1348  0.0  0.0      0     0 ?        S<   10:39   0:00 [kslowd001]
root      1349  0.0  0.0      0     0 ?        S    10:39   0:00 [nfsiod]
root      1356  0.0  0.0  27064   588 ?        Ss   10:39   0:00 /usr/sbin/rpc.idmapd
root      1595  0.0  0.0  54336  1664 ?        Sl   10:39   0:00 /usr/sbin/rsyslogd -c4
root      1689  0.0  0.0   3960   648 ?        Ss   10:39   0:00 /usr/sbin/acpid
root      1730  0.0  0.0      0     0 ?        S    10:39   0:00 [lockd]
root      1731  0.0  0.0      0     0 ?        S    10:39   0:00 [nfsd4]
root      1732  0.0  0.0      0     0 ?        S    10:39   0:00 [nfsd]
root      1733  0.0  0.0      0     0 ?        S    10:39   0:00 [nfsd]
root      1734  0.0  0.0      0     0 ?        S    10:39   0:00 [nfsd]
root      1735  0.0  0.0      0     0 ?        S    10:39   0:00 [nfsd]
root      1736  0.0  0.0      0     0 ?        S    10:39   0:00 [nfsd]
root      1737  0.0  0.0      0     0 ?        S    10:39   0:00 [nfsd]
root      1738  0.0  0.0      0     0 ?        S    10:39   0:00 [nfsd]
root      1739  0.0  0.0      0     0 ?        S    10:39   0:00 [nfsd]
root      1744  0.0  0.0  14668   432 ?        Ss   10:39   0:00 /usr/sbin/rpc.mountd --manage
root      1778  0.0  0.1  71424  2892 ?        Ss   10:39   0:00 /usr/sbin/apache2 -k start
www-data  1780  0.0  0.0  71156  1992 ?        S    10:39   0:00 /usr/sbin/apache2 -k start
www-data  1781  0.0  0.1 295100  3384 ?        Sl   10:39   0:00 /usr/sbin/apache2 -k start
www-data  1782  0.0  0.1 295268  3540 ?        Sl   10:39   0:00 /usr/sbin/apache2 -k start
root      1880  0.0  0.0  22440   884 ?        Ss   10:39   0:00 /usr/sbin/cron
root      2187  0.0  0.0  61864  1316 ?        Ss   10:39   0:00 nginx: master process /usr/sb
www-data  2189  0.0  0.0  62232  1848 ?        S    10:39   0:00 nginx: worker process
www-data  2190  0.0  0.0  62232  1848 ?        S    10:39   0:00 nginx: worker process
www-data  2191  0.0  0.1  62232  2288 ?        S    10:39   0:00 nginx: worker process
www-data  2192  0.0  0.0  62232  1828 ?        S    10:39   0:00 nginx: worker process
root      2195  0.0  0.0  49220  1168 ?        Ss   10:39   0:00 /usr/sbin/sshd
101       2218  0.0  0.0  32724  1032 ?        Ss   10:39   0:00 /usr/sbin/exim4 -bd -q30m
root      2258  0.0  0.0   5972   632 tty1     Ss+  10:39   0:00 /sbin/getty 38400 tty1
root      2259  0.0  0.0   5972   632 tty2     Ss+  10:39   0:00 /sbin/getty 38400 tty2
root      2260  0.0  0.0   5972   636 tty3     Ss+  10:39   0:00 /sbin/getty 38400 tty3
root      2261  0.0  0.0   5972   636 tty4     Ss+  10:39   0:00 /sbin/getty 38400 tty4
root      2262  0.0  0.0   5972   632 tty5     Ss+  10:39   0:00 /sbin/getty 38400 tty5
root      2263  0.0  0.0   5972   636 tty6     Ss+  10:39   0:00 /sbin/getty 38400 tty6
root      2430  0.0  0.1  76728  3356 ?        Ss   10:54   0:00 sshd: TCM [priv] 
TCM       2432  0.0  0.0  76728  1764 ?        S    10:54   0:00 sshd: TCM@pts/0  
TCM       2433  0.0  0.1  19324  2120 pts/0    Ss   10:54   0:00 -bash
TCM       2646  0.0  0.0  16380  1184 pts/0    R+   11:15   0:00 ps aux
```