

```powershell

// ============================================= Local powershell enumeration ============================================= //

Import-Module activedirectory
Get-ADTrust -Filter *

Import-Module PowerView.ps1
Get-DomainTrust
Get-DomainTrustMapping














```






https://lorenzomeacci.com/trust-issues-attacking-trust-in-active-directory
