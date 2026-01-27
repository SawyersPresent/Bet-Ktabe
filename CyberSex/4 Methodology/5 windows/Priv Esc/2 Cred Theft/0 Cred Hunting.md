

[[0 Credential Hunting]]


```powershell
// Searching for files
findstr /SIM /C:"password" *.txt *.ini *.cfg *.config *.xml

// searching for password string using powershell
gc 'C:\Users\htb-student\AppData\Local\Google\Chrome\User Data\Default\Custom Dictionary.txt' | Select-String password

Get-ChildItem C:\ -Recurse -Include *.txt,*.ps1,*.bat,*.config,*.xml,*.ini -ErrorAction SilentlyContinue | Select-String -Pattern "password","pwd","pass"

// Looking for Unattended.xml


// Try look for Powershell History File

cat C:\Users\<username>\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt

(Get-PSReadLineOption).HistorySavePath

gc (Get-PSReadLineOption).HistorySavePath

foreach($user in ((ls C:\users).fullname)){cat "$user\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadline\ConsoleHost_history.txt" -ErrorAction SilentlyContinue}


// Decrypting Powershell Credentials 
$credential = Import-Clixml -Path 'C:\scripts\pass.xml'
$credential.GetNetworkCredential().username
$credential.GetNetworkCredential().password

For example 

// PowerShell Credentials

This file -----> Connect-VC.ps1 = {
Get-Credential | Export-Clixml -Path 'C:\scripts\pass.xml'
$encryptedPassword = Import-Clixml -Path 'C:\scripts\pass.xml'
$decryptedPassword = $encryptedPassword.GetNetworkCredential().Password
Connect-VIServer -Server 'VC-01' -User 'bob_adm' -Password $decryptedPassword
}

```



## Mistake

Wasnt persistent shouldve checked every single fucking file LOL mybad

