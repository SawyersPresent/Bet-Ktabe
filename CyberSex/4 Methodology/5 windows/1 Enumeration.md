

```python
// --------------------- Enumerating Surroundings --------------------- //
tree /a /f

// Information about my user
whoami
whoami /priv
whoami /groups
whoami /all

// Getting all users
net user

// Getting all local groups
net localgroup

// Details about a group
net localgroup administrators

// Information about accounts
net accounts


// --------------------- network enumeration --------------------- //
ipconfig /all

arp -a 

route print

netstat -ano


// ------------------------------------------ Enumerating Protections ------------------------------------------ //
// Check defender status

Get-MpComputerStatus

// List App Locker rules
Get-AppLockerPolicy -Effective | select -ExpandProperty RuleCollections

Get-AppLockerPolicy -Local | Test-AppLockerPolicy -path C:\Windows\System32\cmd.exe -User Everyone

// to see environment variables
set

// system version and the sort really
systeminfo

// To see patches
wmic qfe
Get-HotFix | ft -AutoSize

// To see installed products
wmic product get name
Get-WmiObject -Class Win32_Product |  select Name, Version


// ------------------------------------------ Enumerating Services ------------------------------------------ //
// To see the running tasks
tasklist
tasklist /svc

// Enumerating tasks using registry keys
Get-ChildItem HKLM:\SYSTEM\CurrentControlSet\Services | Where-Object { (Get-ItemProperty $_.PSPath -ErrorAction SilentlyContinue).ImagePath } | Select-Object -ExpandProperty PSChildName

reg query "HKLM\SYSTEM\CurrentControlSet\Services" /s /v ImagePath 2>nul | findstr /r /c:"\\Services\\" | for /f "tokens=5 delims=\" %%a in ('findstr /r /c:"\\Services\\"') do @echo %%a


// Enumerating services using wmic 
wmic product get name



// ------------------------------------------ Enumerating Misc ------------------------------------------ //

// basic way 
query user
// Second way is to use runascs

// Listing Pipes
gci \\.\pipe\

// Checking the permissions of thing
accesschk.exe -accepteula -w \pipe\SQLLocal\SQLEXPRESS01 -v
accesschk.exe /accepteula thing.exe -v

// Always install elevated
reg query HKEY_CURRENT_USER\Software\Policies\Microsoft\Windows\Installer
reg query HKLM\SOFTWARE\Policies\Microsoft\Windows\Installer

// Enable Disabled privileges
https://raw.githubusercontent.com/fashionproof/EnableAllTokenPrivs/master/EnableAllTokenPrivs.ps1

// Finding credentials
???

```



