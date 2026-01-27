

```
[Apr 15, 2025 - 16:27:13 (+03)] exegol-htb /workspace # nxc smb 10.5.10.0/24 -u '' -p ''
SMB         10.5.10.16      445    FS               [*] Windows Server 2022 Build 20348 (name:FS) (domain:async.local) (signing:False) (SMBv1:False)
SMB         10.5.10.2       445    DC               [*] Windows Server 2022 Build 20348 (name:DC) (domain:async.local) (signing:True) (SMBv1:False)
SMB         10.5.10.173     445    DEV              [*] Windows 11 Build 22621 (name:DEV) (domain:async.local) (signing:False) (SMBv1:False)
SMB         10.5.10.16      445    FS               [-] async.local\: STATUS_ACCESS_DENIED
SMB         10.5.10.2       445    DC               [+] async.local\:
SMB         10.5.10.173     445    DEV              [-] async.local\: STATUS_ACCESS_DENIED
Running nxc against 256 targets ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
```



```python
[Apr 15, 2025 - 16:29:54 (+03)] exegol-htb /workspace  nxc smb 10.5.10.0/24 -u 'a' -p '' --smb-timeout 10
SMB         10.5.10.16      445    FS               [*] Windows Server 2022 Build 20348 (name:FS) (domain:async.local) (signing:False) (SMBv1:False)
SMB         10.5.10.2       445    DC               [*] Windows Server 2022 Build 20348 (name:DC) (domain:async.local) (signing:True) (SMBv1:False)
SMB         10.5.10.173     445    DEV              [*] Windows 11 Build 22621 (name:DEV) (domain:async.local) (signing:False) (SMBv1:False)
SMB         10.5.10.16      445    FS               [+] async.local\a: (Guest)
SMB         10.5.10.2       445    DC               [-] async.local\a: STATUS_LOGON_FAILURE
SMB         10.5.10.173     445    DEV              [-] async.local\a: STATUS_LOGON_FAILURE
```

