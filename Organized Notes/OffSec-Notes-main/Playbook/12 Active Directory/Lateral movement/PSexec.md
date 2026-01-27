
### PsExec

Requires:

- User logging in to be a member of the `administrators` local group
- `ADMIN$` share must be available (default)
- File and printer sharing must be turned on (default)

```bash
./PsExec64.exe -i \\files04 -u corp\jen -p Nexus123! cmd
```
