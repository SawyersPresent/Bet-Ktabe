

```
kali@kali ~ [1]> bloodhound-python -d painters.htb -dc DC.painters.htb -ns 192.168.110.55 -u riley -p P@ssw0rd -c all --zip
INFO: Found AD domain: painters.htb
INFO: Getting TGT for user
INFO: Connecting to LDAP server: DC.painters.htb
INFO: Found 1 domains
INFO: Found 1 domains in the forest
INFO: Found 6 computers
INFO: Connecting to GC LDAP server: dc.painters.htb
INFO: Connecting to LDAP server: DC.painters.htb
INFO: Found 11 users
INFO: Found 52 groups
INFO: Found 2 gpos
INFO: Found 1 ous
INFO: Found 19 containers
INFO: Found 1 trusts
INFO: Starting computer enumeration with 10 workers
INFO: Querying computer: WORKSTATION-1.painters.htb
INFO: Querying computer: Maintenance.painters.htb
INFO: Querying computer: PNT-SVRPSB.painters.htb
INFO: Querying computer: PNT-SVRBPA.painters.htb
INFO: Querying computer: DC.painters.htb
INFO: Querying computer: PNT-SVRSVC.painters.htb
WARNING: DCE/RPC connection failed: The NETBIOS connection with the remote host timed out.
WARNING: DCE/RPC connection failed: The NETBIOS connection with the remote host timed out.
WARNING: DCE/RPC connection failed: The NETBIOS connection with the remote host timed out.
INFO: Done in 00M 38S
INFO: Compressing output into 20240708090335_bloodhound.zip
```






Kerbroastable users

![[DC machine 3-20240708160014763.webp]]




![[DC machine 3-20240708160119483.webp]]


