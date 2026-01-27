

`SharpView` uses strings instead of PowerShell objects. Therefore we cannot specify properties using `Select` or `Select-Object`, to parse the output or select specific AD objects as easily


Quick Misc functions before the cheatsheet

```python
Export-PowerViewCSV             -   thread-safe CSV append
Resolve-IPAddress               -   resolves a hostname to an IP
ConvertTo-SID                   -   converts a given user/group name to a security identifier (SID)
Convert-ADName                  -   converts object names between a variety of formats
ConvertFrom-UACValue            -   converts a UAC int value to human readable form
Add-RemoteConnection            -   pseudo "mounts" a connection to a remote path using the specified credential object
Remove-RemoteConnection         -   destroys a connection created by New-RemoteConnection
Invoke-UserImpersonation        -   creates a new "runas /netonly" type logon and impersonates the token
Invoke-RevertToSelf             -   reverts any token impersonation
Get-DomainSPNTicket             -   request the kerberos ticket for a specified service principal name (SPN)
Invoke-Kerberoast               -   requests service tickets for kerberoast-able accounts and returns extracted ticket hashes
Get-PathAcl                     -   get the ACLs for a local/remote file path with optional group recursion
```



powerview.py

```
Get-ObjectAcl "DontHackMeUser" -Select SecurityIdentifier,AccessMask,ActiveDirectoryRights,ObjectAceType -Where 'SecurityIdentifier not Principal Self' -ResolveGUIDs
```


```python

// ============================================================== Cheatsheet ================================================================= //
// Finding pre-2000 computer accounts, it looks for workstation trust and password_noreq
Get-DomainComputer -LDAPFilter "(&(userAccountControl:1.2.840.113556.1.4.803:=32)(userAccountControl:1.2.840.113556.1.4.803:=4096))"
Get-DomainComputer -LDAPFilter "(userAccountControl: 1.2.840.113556.1.4.803:=4128)"

// 



```






