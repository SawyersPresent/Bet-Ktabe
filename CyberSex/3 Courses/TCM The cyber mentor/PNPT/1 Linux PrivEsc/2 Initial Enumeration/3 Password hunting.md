### More will be done on later on LESSONS of the course, again this is only an INTRODUCTION





# Grep command with color coordination


im not posting this output because its insane but this is the first way to find a password 
`grep --color=auto -rnw '/' -ie "PASSWORD" --color=always 2>/dev/null`

this is the second way
`grep --color=auto -rnw '/' -ie "PASSWORD=" --color=always 2>/dev/null`

`TCM@debian:~$ grep --color=auto -rnw '/' -ie "PASSWORD=" --color=always 2>/dev/null`

theres also `locate password | more`

```
TCM@debian:~$ locate password | more
locate: warning: database `/var/cache/locate/locatedb' is more than 8 days old (actual age is 
1348.3 days)
/boot/grub/password.mod
/boot/grub/password_pbkdf2.mod
/etc/pam.d/common-password
/usr/lib/grub/i386-pc/password.mod
/usr/lib/grub/i386-pc/password_pbkdf2.mod
/usr/share/pam/common-password
/usr/share/pam/common-password.md5sums
/var/cache/debconf/passwords.dat
/var/lib/pam/password
```

or

`locate pass | more`



## Hunting ssh keys


`find / -name id_rsa 2> /dev/null`

```
TCM@debian:~$ find / -name id_rsa 2> /dev/null
/backups/supersecretkeys/id_rsa
```



