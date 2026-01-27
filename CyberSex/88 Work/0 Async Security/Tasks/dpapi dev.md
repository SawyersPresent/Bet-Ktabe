

```
P
```




![[dpapi dev-20250709162644966.webp]]





```
$user = "asia.earth.local\T1-T.LANGFORD"; $password = "2YE3NKgcbvYe"; $taskName = "CredCacheTask-T1-T.LANGFORD"; schtasks /create /tn $taskName /tr "powershell.exe -ExecutionPolicy Bypass -NoProfile -WindowStyle Hidden -Command `"& {while (`$true) {Write-EventLog -LogName Application -Source PowerShell -EntryType Information -EventId 1001 -Message \`"Log update from scheduled task\`"; Start-Sleep -Seconds 300}}`"" /sc onstart /ru $user /rp $password /f; schtasks /run /tn $taskName
```