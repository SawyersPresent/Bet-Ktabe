
TDLR;

searching for passwords in unconventional places

```powershell

// ---------------- Searching file contents for strings ---------------- //

// Searching file contents for strings 1
cd c:\Users\htb-student\Documents & findstr /SI /M "password" *.xml *.ini *.txt

// Searching file contents for strings 2
findstr /si password *.xml *.ini *.txt *.config

// Searching file contents for strings 3
C:\htb> findstr /spin "password" *.*

// ---------------- Searching for File contents with powershell ---------------- //

// Searching file contents with powershell 
select-string -Path C:\Users\htb-student\Documents\*.txt -Pattern password



// ----------------  Searching for File Extensions ---------------- //

// searching for fie extensions 1
dir /S /B *pass*.txt == *pass*.xml == *pass*.ini == *cred* == *vnc* == *.config*

// searching for fie extensions 2
where /R C:\ *.config

// searching for file extensions using Powershell
Get-ChildItem C:\ -Recurse -Include *.rdp, *.config, *.vnc, *.cred -ErrorAction Ignore



// ----------------  Searching for Sticky Note Passwords ---------------- //

// usual location of the DB
C:\Users\<user>\AppData\Local\Packages\Microsoft.MicrosoftStickyNotes_8wekyb3d8bbwe\LocalState\plum.sqlite

// now we read it using powershell
Set-ExecutionPolicy Bypass -Scope Process

// Donwload and Import PSSQLIte
Import-Module .\PSSQLite.psd1

$db = 'C:\Users\htb-student\AppData\Local\Packages\Microsoft.MicrosoftStickyNotes_8wekyb3d8bbwe\LocalState\plum.sqlite'

Invoke-SqliteQuery -Database $db -Query "SELECT Text FROM Note" | ft -wrap

```

