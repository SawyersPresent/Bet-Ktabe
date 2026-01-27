This abuse can be carried out when controlling an object that has a `GenericAll`, `GenericWrite`, `WriteProperty` or `Validated-SPN` over the target. A member of the [Account Operator](https://www.thehacker.recipes/ad/movement/domain-settings/builtin-groups) group usually has those permissions.

The attacker can add an SPN (`ServicePrincipalName`) to that account. Once the account has an SPN, it becomes vulnerable to [Kerberoasting](https://www.thehacker.recipes/ad/movement/kerberos/kerberoast). This technique is called Targeted Kerberoasting.


From UNIX-like systems, this can be done with [targetedKerberoast.py](https://github.com/ShutdownRepo/targetedKerberoast) (Python)


```
targetedKerberoast.py -v -d $DOMAIN_FQDN -u $USER -p $PASSWORD
```