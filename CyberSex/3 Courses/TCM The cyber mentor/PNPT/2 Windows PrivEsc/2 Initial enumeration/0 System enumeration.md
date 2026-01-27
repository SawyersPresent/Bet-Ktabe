- Hostname
- Architecture
- Hotfixes
- Patching
- Drives
- etc.
- What is the system providing on a high level


```
systeminfo
hostname
systeminfo | findstr /B /C:"OS Name" /C:"OS Version" /C:"System Type"

```

extract patching

window management information Command Line
```
wmic qfe
wmic qfe get Caption, Description, HotFixID, InstalledOn
```

to find drives 

```
wmic logicaldisk 
wmic logicaldisk get caption, description, providername 
```

