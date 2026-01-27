

first thing we usually do is `history` or `cat .bash_history`


## History

`history`
 
```
TCM@debian:~$ history
    1  ls -al
    2  cat .bash_history 
    3  ls -al
    4  mysql -h somehost.local -uroot -ppassword123
<...SNIP...>
```


`.bash_history`

```
TCM@debian:~$ cat .bash_history
ls -al
cat .bash_history 
ls -al
mysql -h somehost.local -uroot -ppassword123
exit
cd /tmp
<...SNIP...>
```




### Files containing passwords

```
grep --color=auto -rnw '/' -ie "PASSWORD" --color=always 2> /dev/null
find . -type f -exec grep -i -I "PASSWORD" {} /dev/null \;
```

```
cat /home/user/.irssi/config | grep -ie passw
```




sometimes passwords are right infront of you 

```
TCM@debian:~$ ls
myvpn.ovpn  tools
TCM@debian:~$ cat myvpn.ovpn 
client
dev tun
proto udp
remote 10.10.10.10 1194
resolv-retry infinite
nobind
persist-key
persist-tun
ca ca.crt
tls-client
remote-cert-tls server
auth-user-pass /etc/openvpn/auth.txt
comp-lzo
verb 1
reneg-sec 0

TCM@debian:~$ cat /etc/openvpn/auth.txt
user
password321
```



credentials could be hidden in the processes, like to be used to run a process like in `ps aux` or rather having a password stored in the config files of a webserver

