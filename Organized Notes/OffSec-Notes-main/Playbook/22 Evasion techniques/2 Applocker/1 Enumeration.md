

```python
Get-AppLockerPolicy -Effective | select -ExpandProperty RuleCollections
```


Navigating to this GitHub page **[here](https://github.com/api0cradle/UltimateAppLockerByPassList/blob/master/Generic-AppLockerbypasses.md)**, we can see that **api0cradle** has generously created a list of folders within `C:\Windows\*` that are writeable for standard users by default:

```
C:\Windows\Tasks  
C:\Windows\Temp  
C:\windows\tracing  
C:\Windows\Registration\CRMLog  
C:\Windows\System32\FxsTmp  
C:\Windows\System32\com\dmp  
C:\Windows\System32\Microsoft\Crypto\RSA\MachineKeys  
C:\Windows\System32\spool\PRINTERS  
C:\Windows\System32\spool\SERVERS  
C:\Windows\System32\spool\drivers\color  
C:\Windows\System32\Tasks\Microsoft\Windows\SyncCenter  
C:\Windows\System32\Tasks_Migrated (after peforming a version upgrade of Windows 10)  
C:\Windows\SysWOW64\FxsTmp  
C:\Windows\SysWOW64\com\dmp  
C:\Windows\SysWOW64\Tasks\Microsoft\Windows\SyncCenter  
C:\Windows\SysWOW64\Tasks\Microsoft\Windows\PLA\System
```

Output this into a `icacls.txt`

```
for /F %A in (C:\temp\icacls.txt) do ( cmd.exe /c icacls "%~A" 2>nul | findstr /i "(F) (M) (W) (R,W) (RX,WD) :\" | findstr /i ":\\ everyone authenticated users todos %username%" && echo. ) 
```

and as it re-iterates look for the `(RX,WD)`



## Alternate Data Stream - Work In Progress





# References

https://ppn.snovvcrash.rocks/pentest/infrastructure/ad/av-edr-evasion/applocker-bypass

