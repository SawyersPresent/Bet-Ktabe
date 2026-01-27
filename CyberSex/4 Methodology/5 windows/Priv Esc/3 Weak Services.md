


Even if a host is patched and well managed then it doesnt really matter if they install services that are vulnerable and exposed.


```powershell
// We enumerate the installed services using WMI
wmic product get name

// We try to find the running services by looking through the local ports
netstat -ano 
netstat -ano | findstr 6064

// We can then enumerate the process ID
get-process -Id 3324


// Now lets get the running service
get-service 
get-service | ? {$_.DisplayName -like 'Druva*'}
get-service | ? {$_.DisplayName -like '*Sync*'}


// No we enumerate more, CVE, exploits, configs, anything of the sort
```
