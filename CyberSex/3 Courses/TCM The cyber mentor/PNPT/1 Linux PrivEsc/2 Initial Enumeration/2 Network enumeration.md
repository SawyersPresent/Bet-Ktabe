
# SUPER IMPORTANT!
## Some might work some might not







# Basic enumeration

`ifconfig`

```
TCM@debian:~$ ifconfig
eth0      Link encap:Ethernet  HWaddr 02:10:4a:46:13:6d  
          inet addr:10.10.239.200  Bcast:10.10.255.255  Mask:255.255.0.0
          inet6 addr: fe80::10:4aff:fe46:136d/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:9001  Metric:1
          RX packets:3081 errors:0 dropped:0 overruns:0 frame:0
          TX packets:2648 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:221745 (216.5 KiB)  TX bytes:272580 (266.1 KiB)
          Interrupt:20 

lo        Link encap:Local Loopback  
          inet addr:127.0.0.1  Mask:255.0.0.0
          inet6 addr: ::1/128 Scope:Host
          UP LOOPBACK RUNNING  MTU:16436  Metric:1
          RX packets:104 errors:0 dropped:0 overruns:0 frame:0
          TX packets:104 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0 
          RX bytes:8756 (8.5 KiB)  TX bytes:8756 (8.5 KiB)
```



`ip a` 

```
TCM@debian:~$ ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 16436 qdisc noqueue state UNKNOWN 
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 9001 qdisc pfifo_fast state UP qlen 1000
    link/ether 02:10:4a:46:13:6d brd ff:ff:ff:ff:ff:ff
    inet 10.10.239.200/16 brd 10.10.255.255 scope global eth0
    inet6 fe80::10:4aff:fe46:136d/64 scope link 
       valid_lft forever preferred_lft forever
```


## Checking for route

`route` or `ip route`

```
TCM@debian:~$ route 
Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
10.10.0.0       *               255.255.0.0     U     0      0        0 eth0
default         ip-10-10-0-1.eu 0.0.0.0         UG    0      0        0 eth0
```

```
TCM@debian:~$  ip route
10.10.0.0/16 dev eth0  proto kernel  scope link  src 10.10.239.200 
default via 10.10.0.1 dev eth0
```

to check for other routes using different ways maybe using `arp -a` or its newer alternative `ip neigh` 

```
TCM@debian:~$ ip neigh
10.10.0.1 dev eth0 lladdr 02:c8:85:b5:5a:aa DELAY
```


# Identifying open ports
`netstat -ano`, identify what ports are open and what communications exist


```
TCM@debian:~$ netstat -ano
Active Internet connections (servers and established)       <------------------------------- PART 1
Proto Recv-Q Send-Q Local Address           Foreign Address         State       Timer
tcp        0      0 0.0.0.0:111             0.0.0.0:*               LISTEN      off (0.00/0/0)
tcp        0      0 0.0.0.0:8080            0.0.0.0:*               LISTEN      off (0.00/0/0)
tcp        0      0 0.0.0.0:49972           0.0.0.0:*               LISTEN      off (0.00/0/0)
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      off (0.00/0/0)
tcp        0      0 0.0.0.0:25              0.0.0.0:*               LISTEN      off (0.00/0/0)
tcp        0      0 0.0.0.0:37534           0.0.0.0:*               LISTEN      off (0.00/0/0)
tcp        0      0 0.0.0.0:59839           0.0.0.0:*               LISTEN      off (0.00/0/0)
tcp        0      0 0.0.0.0:2049            0.0.0.0:*               LISTEN      off (0.00/0/0)
tcp        0      0 10.10.239.200:22        10.100.2.58:44554       ESTABLISHED keepalive (4302.42/0/0)
tcp        0      0 10.10.239.200:22        10.100.2.58:47760       ESTABLISHED keepalive (6774.20/0/0)
tcp        0      0 10.10.239.200:22        10.100.2.58:48098       ESTABLISHED keepalive (7190.92/0/0)
tcp6       0      0 :::80                   :::*                    LISTEN      off (0.00/0/0)
tcp6       0      0 :::22                   :::*                    LISTEN      off (0.00/0/0)
udp        0      0 0.0.0.0:44721           0.0.0.0:*                           off (0.00/0/0)
udp        0      0 0.0.0.0:68              0.0.0.0:*                           off (0.00/0/0)
udp        0      0 0.0.0.0:111             0.0.0.0:*                           off (0.00/0/0)
udp        0      0 0.0.0.0:2049            0.0.0.0:*                           off (0.00/0/0)
udp        0      0 0.0.0.0:54412           0.0.0.0:*                           off (0.00/0/0)
udp        0      0 0.0.0.0:42903           0.0.0.0:*                           off (0.00/0/0)
udp        0      0 127.0.0.1:670           0.0.0.0:*                           off (0.00/0/0)
Active UNIX domain sockets (servers and established)     <---------------------------------------- PART 2
Proto RefCnt Flags       Type       State         I-Node   Path
unix  2      [ ACC ]     STREAM     LISTENING     4093     /var/run/acpid.socket
unix  2      [ ]         DGRAM                    1949     @/org/kernel/udev/udevd
unix  2      [ ACC ]     STREAM     LISTENING     4298     /var/run/apache2/cgisock.1778
unix  7      [ ]         DGRAM                    3998     /dev/log
unix  3      [ ]         STREAM     CONNECTED     6641     
unix  3      [ ]         STREAM     CONNECTED     6640     
unix  2      [ ]         DGRAM                    6639     
unix  3      [ ]         STREAM     CONNECTED     6471     
unix  3      [ ]         STREAM     CONNECTED     6470     
unix  2      [ ]         DGRAM                    6469     
unix  2      [ ]         DGRAM                    5682     
unix  3      [ ]         STREAM     CONNECTED     5497     
unix  3      [ ]         STREAM     CONNECTED     5496     
unix  2      [ ]         DGRAM                    5495     
unix  3      [ ]         STREAM     CONNECTED     4564     
unix  3      [ ]         STREAM     CONNECTED     4563     
unix  3      [ ]         STREAM     CONNECTED     4562     
unix  3      [ ]         STREAM     CONNECTED     4561     
unix  3      [ ]         STREAM     CONNECTED     4560     
unix  3      [ ]         STREAM     CONNECTED     4559     
unix  3      [ ]         STREAM     CONNECTED     4558     
unix  3      [ ]         STREAM     CONNECTED     4557     
unix  2      [ ]         DGRAM                    4090     
unix  3      [ ]         STREAM     CONNECTED     3727     
unix  3      [ ]         STREAM     CONNECTED     3726     
unix  3      [ ]         DGRAM                    1954     
unix  3      [ ]         DGRAM                    1953 
```


lets focus on part 1 for now

```
TCM@debian:~$ netstat -ano
Active Internet connections (servers and established)       <------------------------------- PART 1
Proto Recv-Q Send-Q Local Address           Foreign Address         State       Timer
tcp        0      0 0.0.0.0:111             0.0.0.0:*               LISTEN      off (0.00/0/0)
tcp        0      0 0.0.0.0:8080            0.0.0.0:*               LISTEN      off (0.00/0/0)
tcp        0      0 0.0.0.0:49972           0.0.0.0:*               LISTEN      off (0.00/0/0)
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      off (0.00/0/0)
tcp        0      0 0.0.0.0:25              0.0.0.0:*               LISTEN      off (0.00/0/0)
tcp        0      0 0.0.0.0:37534           0.0.0.0:*               LISTEN      off (0.00/0/0)
tcp        0      0 0.0.0.0:59839           0.0.0.0:*               LISTEN      off (0.00/0/0)
tcp        0      0 0.0.0.0:2049            0.0.0.0:*               LISTEN      off (0.00/0/0)
tcp        0      0 10.10.239.200:22        10.100.2.58:44554       ESTABLISHED keepalive (4302.42/0/0) <------ who is this?
tcp        0      0 10.10.239.200:22        10.100.2.58:47760       ESTABLISHED keepalive (6774.20/0/0)
tcp        0      0 10.10.239.200:22        10.100.2.58:48098       ESTABLISHED keepalive (7190.92/0/0)
tcp6       0      0 :::80                   :::*                    LISTEN      off (0.00/0/0)
tcp6       0      0 :::22                   :::*                    LISTEN      off (0.00/0/0)
udp        0      0 0.0.0.0:44721           0.0.0.0:*                           off (0.00/0/0)
udp        0      0 0.0.0.0:68              0.0.0.0:*                           off (0.00/0/0)
udp        0      0 0.0.0.0:111             0.0.0.0:*                           off (0.00/0/0)
udp        0      0 0.0.0.0:2049            0.0.0.0:*                           off (0.00/0/0)
udp        0      0 0.0.0.0:54412           0.0.0.0:*                           off (0.00/0/0)
udp        0      0 0.0.0.0:42903           0.0.0.0:*                           off (0.00/0/0)
udp        0      0 127.0.0.1:670           0.0.0.0:*                           off (0.00/0/0)   <------ 127.0.0.1 means its open internally, but why? investigate it
```


