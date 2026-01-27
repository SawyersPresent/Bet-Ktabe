
starting client
```
./client
```

starting teamserver
```
kali@kali ~/C/C/Server [SIGINT]> sudo ./teamserver -h

[*] Will use existing X509 certificate and keystore (for SSL)

[*] Starting teamserver
[*] Team Server Version: 4.9.1 (Pwn3rs)
[*] Setting 'https.protocols' system property: SSLv3,SSLv2Hello,TLSv1,TLSv1.1,TLSv1.2,TLSv1.3
[*] ./teamserver <host> <password> [/path/to/c2.profile] [YYYY-MM-DD]

	<host> is the (default) IP address of this Cobalt Strike team server
	<password> is the shared password to connect to this server
	[/path/to/c2.profile] is your Malleable C2 profile
	[YYYY-MM-DD] is a kill date for Beacon payloads run from this server

kali@kali ~/C/C/Server> sudo ./teamserver 192.168.176.128 12345
```





---

## Profiles

https://blog.zsec.uk/cobalt-strike-profiles/
https://github.com/threatexpress/malleable-c2




---

## Arsenal, Subject to change

https://github.com/mgeeky/cobalt-arsenal

https://github.com/dafthack/DomainPasswordSpray (can LOCK OUT ACCOUNTS WITH THIS BECAREFUL.)

https://github.com/REDMED-X/OperatorsKit





stuff


https://book.hacktricks.xyz/c2/cobalt-strike
https://hackmd.io/@castor-hacker/rJYecjvs6#Initial-Compromise

https://unit42.paloaltonetworks.com/cobalt-strike-malleable-c2-profile/