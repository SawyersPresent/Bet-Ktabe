

# Detection

use the sysinternals tool provided called autoruns.exe

ofcourse once it runs we can see something very suspicious

![[Pasted image 20240721144902.png]]

Another tool thats possible to use would be **PowerUp**'s invoke-allchecks

```
[*] Checking for modifidable registry autoruns and configs...

Key            : HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Run\My Program
Path           : "C:\Program Files\Autorun Program\program.exe"
ModifiableFile : @{Permissions=System.Object[]; ModifiablePath=C:\Program Files\Autorun Program\program.exe; IdentityReference=Everyone}
```


so now we know the program that has autorun on it... we need to see our permissions on it if we can even edit it


`accesschk64.exe -wvu`

- w
	- Shows you the write access
- v
	- Means verbose
- u
	- Means suppress errors

```
Microsoft Windows [Version 6.1.7601]
Copyright (c) 2009 Microsoft Corporation.  All rights reserved.

C:\Users\user\Desktop\Tools\Accesschk>accesschk64.exe -wvu "C:\Program Files\Autorun Program"

Accesschk v6.10 - Reports effective permissions for securable objects
Copyright (C) 2006-2016 Mark Russinovich
Sysinternals - www.sysinternals.com

C:\Program Files\Autorun Program\program.exe
  Medium Mandatory Level (Default) [No-Write-Up]
  RW Everyone
        FILE_ALL_ACCESS
  RW NT AUTHORITY\SYSTEM
        FILE_ALL_ACCESS
  RW BUILTIN\Administrators
        FILE_ALL_ACCESS

C:\Users\user\Desktop\Tools\Accesschk>
```

so now that we know everyone can edit to simple just create a reverse shell and write over that file with that same name


# Full output from powerup


```

C:\Users\user\Desktop\Tools\windows-privesc-check>powershell.exe -ep bypass
Windows PowerShell
Copyright (C) 2009 Microsoft Corporation. All rights reserved.

PS C:\Users\user\Desktop\Tools\PowerUp> . .\PowerUp.ps1
PS C:\Users\user\Desktop\Tools\PowerUp> Invoke-AllChecks

[*] Running Invoke-AllChecks

[*] Checking if user is in a local group with administrative privileges...

[*] Checking for unquoted service paths...

ServiceName    : AWSLiteAgent
Path           : C:\Program Files\Amazon\XenTools\LiteAgent.exe
ModifiablePath : @{Permissions=AppendData/AddSubdirectory; ModifiablePath=C:\;IdentityReference=NT AUTHORITY\Authenticated Users}
StartName      : LocalSystem
AbuseFunction  : Write-ServiceBinary -Name 'AWSLiteAgent' -Path <HijackPath>
CanRestart     : False

ServiceName    : AWSLiteAgent
Path           : C:\Program Files\Amazon\XenTools\LiteAgent.exe
ModifiablePath : @{Permissions=System.Object[]; ModifiablePath=C:\; IdentityReference=NT AUTHORITY\Authenticated Users}
StartName      : LocalSystem
AbuseFunction  : Write-ServiceBinary -Name 'AWSLiteAgent' -Path <HijackPath>
CanRestart     : False

ServiceName    : unquotedsvc
Path           : C:\Program Files\Unquoted Path Service\Common Files\unquotedpathservice.exe
ModifiablePath : @{Permissions=AppendData/AddSubdirectory; ModifiablePath=C:\;IdentityReference=NT AUTHORITY\Authenticated Users}
StartName      : LocalSystem
AbuseFunction  : Write-ServiceBinary -Name 'unquotedsvc' -Path <HijackPath>
CanRestart     : True

ServiceName    : unquotedsvc
Path           : C:\Program Files\Unquoted Path Service\Common Files\unquotedpathservice.exe
ModifiablePath : @{Permissions=System.Object[]; ModifiablePath=C:\; IdentityReference=NT AUTHORITY\Authenticated Users}
StartName      : LocalSystem
AbuseFunction  : Write-ServiceBinary -Name 'unquotedsvc' -Path <HijackPath>
CanRestart     : True




[*] Checking service executable and argument permissions...
ServiceName                     : filepermsvc
Path                            : "C:\Program Files\File Permissions Service\filepermservice.exe"
ModifiableFile                  : C:\Program Files\File Permissions Service\filepermservice.exe
ModifiableFilePermissions       : {ReadAttributes, ReadControl, Execute/Traverse, DeleteChild...}
ModifiableFileIdentityReference : Everyone
StartName                       : LocalSystem
AbuseFunction                   : Install-ServiceBinary -Name 'filepermsvc'
CanRestart                      : True




[*] Checking service permissions...

ServiceName   : daclsvc
Path          : "C:\Program Files\DACL Service\daclservice.exe"
StartName     : LocalSystem
AbuseFunction : Invoke-ServiceAbuse -Name 'daclsvc'
CanRestart    : True



[*] Checking %PATH% for potentially hijackable DLL locations...

Permissions       : {ReadAttributes, ReadControl, Execute/Traverse, WriteAttributes...}
ModifiablePath    : C:\Temp
IdentityReference : NT AUTHORITY\Authenticated Users
%PATH%            : C:\Temp
AbuseFunction     : Write-HijackDll -DllPath 'C:\Temp\wlbsctrl.dll'
Permissions       : {GenericWrite, Delete, GenericExecute, GenericRead}
ModifiablePath    : C:\Temp
IdentityReference : NT AUTHORITY\Authenticated Users
%PATH%            : C:\Temp
AbuseFunction     : Write-HijackDll -DllPath 'C:\Temp\wlbsctrl.dll'



[*] Checking for AlwaysInstallElevated registry key...

AbuseFunction : Write-UserAddMSI



[*] Checking for Autologon credentials in registry...

[*] Checking for modifidable registry autoruns and configs...

Key            : HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Run\My Program
Path           : "C:\Program Files\Autorun Program\program.exe"
ModifiableFile : @{Permissions=System.Object[]; ModifiablePath=C:\Program Files\Autorun Program\program.exe; IdentityReference=Everyone}



[*] Checking for modifiable schtask files/configs...
[*] Checking for unattended install files...

UnattendPath : C:\Windows\Panther\Unattend.xml


[*] Checking for encrypted web.config strings...

[*] Checking for encrypted application pool and virtual directory passwords...

[*] Checking for plaintext passwords in McAfee SiteList.xml files....

[*] Checking for cached Group Policy Preferences .xml files....


PS C:\Users\user\Desktop\Tools\PowerUp>
```