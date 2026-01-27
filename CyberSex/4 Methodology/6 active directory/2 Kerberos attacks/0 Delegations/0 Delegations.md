
# Delegations

delegation is a Kerberos capability that enables a service to authenticate to another service as the original user. The Kerberos protocol allows a user to authenticate to a service to use it, and Kerberos delegation enables that service to authenticate to another service as the original user.

In this example, a user authenticates to WEBSRV to access the website. Once authenticated on the website, the user needs to access information stored in a database, but should not be given access to all the information within it. The service account managing the website must communicate with the database using the user's rights so that the database only gives access to resources that the user has the right to access. This is where delegation comes into play. The service account, here WEBSRV$, will pretend to be the user when accessing the database. This is called delegation.


## Unconstrained delegation



## Constrained delegation






## S4U2Self

When a user authenticates to a service without using Kerberos authentication (like NTLM per say) and there is no TGS ticket?, the answer is S4U2Self

The extension allows a service to obtain a forwardable TGS ticket to itself **on behalf of an arbitrary user**, Thus this allows the service to act on behalf of that user. then once the service has this TGS it can finally move forward into making a TGS request to use the desired resource **S4U2Proxy** embedding the brand new forwardable TGS ticket it just asked for.

this extension allows delegation even if the authentication protocol is not always the same between the user and the different services. this is called **protocol transition.** if the **Kerberos only** option is chosen then the service account cannot do protocol transition, hence we **cannot use** S4U2Self. 

If protocol transition is **enabled** then S4U2Self is **possible**.




## S4U2Proxy

this extension corresponds to the TGS requests made by a service account to impersonate a user.  for it to work properly. the service needs to apply a service ticket as "additional-ticket" (used as evidence that the service using s4u2proxy has the authority to do it on behalf of a user)

For an S4U2Proxy request to work and have the KDC issue ST:

- the ST used as an "additional-ticket" must have the forwardable flag set 
- alternatively 
	- in the TGS-REQ. specifically inside of the pre-authentication data the "PA-PAC-OPTIONS" structure must contain a padata value with the resource-based constrained delegation bit set. 
		- _nota bene 1: this only applies if the resource-based constrained delegation (RBCD) is actually possible and authorized in the proper AD objects attributes_
		- _nota bene 2: Rubeus and Impacket's getST always set that bit when doing S4U2proxy._
- S4U2Proxy always **ALWAYS** results in a forwardable ST, even when the ticket used as an evidence wasn't forwardable 



| Attribute                                  | Delegation | Purpose |
| :----------------------------------------- | :--------- | :------ |
| `TRUSTED_FOR_DELEGATION`                   | KUD        |         |
| `TRUSTED_TO_AUTHENTICATE_FOR_DELEGATION`   | KCD        |         |
| `msDS-AllowedToActOnBehalfOfOtherIdentity` | RBCD       |         |
|                                            |            |         |




## KUD




## KCD




## RBCD






# References

https://learn.microsoft.com/en-us/windows-server/security/windows-authentication/windows-authentication-concepts#delegated-authentication
https://learn.microsoft.com/en-us/powershell/scripting/security/remoting/ps-remoting-second-hop?view=powershell-7.5#resource-based-kerberos-constrained-delegation
https://blog.harmj0y.net/activedirectory/s4u2pwnage/
https://shenaniganslabs.io/2019/01/28/Wagging-the-Dog.html
https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-ada2/cea4ac11-a4b2-4f2d-84cc-aebb4a4ad405