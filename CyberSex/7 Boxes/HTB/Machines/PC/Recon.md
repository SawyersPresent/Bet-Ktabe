
```
kali@kali ~> nmap -sC -sV 10.10.11.191 nfs-ls
Starting Nmap 7.94 ( https://nmap.org ) at 2023-10-20 11:36 EDT
Nmap scan report for 10.10.11.191
Host is up (0.15s latency).
Not shown: 996 closed tcp ports (conn-refused)
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 48:ad:d5:b8:3a:9f:bc:be:f7:e8:20:1e:f6:bf:de:ae (RSA)
|   256 b7:89:6c:0b:20:ed:49:b2:c1:86:7c:29:92:74:1c:1f (ECDSA)
|_  256 18:cd:9d:08:a6:21:a8:b8:b6:f7:9f:8d:40:51:54:fb (ED25519)
80/tcp   open  http    Apache httpd 2.4.41 ((Ubuntu))
|_http-title: Built Better
|_http-server-header: Apache/2.4.41 (Ubuntu)
111/tcp  open  rpcbind 2-4 (RPC #100000)
| rpcinfo: 
|   program version    port/proto  service
|   100000  2,3,4        111/tcp   rpcbind
|   100000  2,3,4        111/udp   rpcbind
|   100000  3,4          111/tcp6  rpcbind
|   100000  3,4          111/udp6  rpcbind
|   100003  3           2049/udp   nfs
|   100003  3           2049/udp6  nfs
|   100003  3,4         2049/tcp   nfs
|   100003  3,4         2049/tcp6  nfs
|   100005  1,2,3      33870/udp6  mountd
|   100005  1,2,3      41186/udp   mountd
|   100005  1,2,3      46629/tcp6  mountd
|   100005  1,2,3      54427/tcp   mountd
|   100021  1,3,4      37131/udp6  nlockmgr
|   100021  1,3,4      39639/tcp   nlockmgr
|   100021  1,3,4      40415/tcp6  nlockmgr
|   100021  1,3,4      60739/udp   nlockmgr
|   100227  3           2049/tcp   nfs_acl
|   100227  3           2049/tcp6  nfs_acl
|   100227  3           2049/udp   nfs_acl
|_  100227  3           2049/udp6  nfs_acl
2049/tcp open  nfs     3-4 (RPC #100003)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

```
msf6 auxiliary(scanner/nfs/nfsmount) > exploit

[+] 10.10.11.191:111      - 10.10.11.191 Mountable NFS Export: /home/ross [*]
[+] 10.10.11.191:111      - 10.10.11.191 Mountable NFS Export: /var/www/html [*]
[*] 10.10.11.191:111      - Scanned 1 of 1 hosts (100% complete)
[*] Auxiliary module execution completed

```

```
kali@kali ~> showmount -e 10.10.11.191
Export list for 10.10.11.191:
/home/ross    *
/var/www/html *

```