# Methodology


# Basic commands

Show list of shares
```
kali@kali ~> showmount -e 10.129.85.164
Export list for 10.129.85.164:
/var/nfs      10.0.0.0/8
/mnt/nfsshare 10.0.0.0/8
```


Mounting a share
```
kali@kali ~> mkdir target-NFS
kali@kali ~> sudo mount -t nfs 10.129.85.164:/ ./target-NFS/ -o nolock
[sudo] password for kali: 
kali@kali ~> cd target-NFS/
kali@kali ~/target-NFS> tree .
.
├── mnt
│   └── nfsshare
│       └── flag.txt
└── var
    └── nfs
	        └── flag.txt

5 directories, 2 files
```

## Enumeration

```
nfs-ls #List NFS exports and check permissions
nfs-showmount #Like showmount -e
nfs-statfs #Disk statistics and info from NFS share
```

make shift

```
kali@kali ~> showmount -e 192.168.100.168
Export list for 192.168.100.168:
/srv/nfs 172.16.0.0/12,10.0.0.0/8,192.168.0.0/16
```

## Mounting

### Mounting 1
```
kali@kali ~> sudo mount -t nfs 192.168.100.168:/ target-NFS -o nolock
kali@kali ~> ls -ld target-NFS/
drwxr-xr-x 18 root root 4096 Jun  1  2021 target-NFS//
```



### Mounting 2

```

```


## ExportFS or uploding a mount

```shell-session
root@nfs:~# echo '/mnt/nfs  10.129.14.0/24(sync,no_subtree_check)' >> /etc/exports
root@nfs:~# systemctl restart nfs-kernel-server 
root@nfs:~# exportfs

/mnt/nfs      	10.129.14.0/24
```

We have shared the folder `/mnt/nfs` to the subnet `10.129.14.0/24` with the setting shown above. This means that all hosts on the network will be able to mount this NFS share and inspect the contents of this folder.

