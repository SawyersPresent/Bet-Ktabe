Unconstrained delegation lets a service (or computer) impersonate anyone who authenticates to it because the user’s TGT rides along in the service ticket. If that account is compromised, an attacker just
  waits or forces a privileged Kerberos login. The attacker’s service then grabs the TGT inside the ST and can access other services as that user, or abuse S4U2self to elevate locally. Domain controllers
  default to this setting, so any non‑“sensitive” user who hits an unconstrained host leaks their TGT. Common abuse paths: wait for an admin to log on, or trigger the MS-RPRN “Printer Bug” to coerce
  authentication and steal a DC’s machine TGT, then DCSync or move laterally


![Active Directory Users and Computers window showing properties for DC02. The "Delegation" tab is selected with the option "Trust this computer for delegation to any service (Kerberos only)" enabled.|734](https://cdn.services-k8s.prod.aws.htb.systems/content/modules/253/Unconstrained_delegation_1.png)


### Performing the Attack

![Diagram illustrating an attack using the "printer bug" between DC02 (Child DC) and DC01 (Parent DC). Steps include authentication requests, TGT extraction, and DCsync, exploiting unconstrained delegation and two-way transitive trust.|745](https://cdn.services-k8s.prod.aws.htb.systems/content/modules/253/UD_IF.png)

Let's execute `Rubeus` to monitor stored tickets. If a `Ticket Granting Ticket (TGT)` is discovered within a `Ticket Granting Service (TGS)` ticket, Rubeus will promptly display it to us, enabling us to identify any potential security risks or access attempts within the environment.






