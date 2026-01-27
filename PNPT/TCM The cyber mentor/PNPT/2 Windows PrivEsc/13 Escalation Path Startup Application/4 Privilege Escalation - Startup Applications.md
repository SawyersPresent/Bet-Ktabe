




## Manual enumeration

https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/icacls

```
icacls.exe "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup"
```

From the output notice that the “BUILTIN\\Users” group has full access ‘(F)’ to the directory.

```

C:\Users\user>icacls.exe "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup"
C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup BUILTIN\Users:(F)TCM-PC\TCM:(I)(OI)(CI)(DE,DC)
                                                             NT AUTHORITY\SYSTEM:(I)(OI)(CI)(F)
                                                             BUILTIN\Administrators:(I)(OI)(CI)(F)
                                                             BUILTIN\Users:(I)(OI)(CI)(RX)
                                                             Everyone:(I)(OI)(CI)(RX)
Successfully processed 1 files; Failed processing 0 files
```

and then as soon as we drop the file there and as soon as someone else logs in it will execute