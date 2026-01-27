


# Configuration Naming Context (NC)


The Configuration Naming Context (NC) serves as the repository for forest-wide configuration data in Active Directory, necessitating its replication across the entire AD forest. The Distinguished Name (DN) for this context is `CN=Configuration,DC=inlanefreight,DC=ad`, wherein `DC=inlanefreight,DC=ad` denotes the DN of the forest root domain.

According to O’Reilly’s Active Directory [book](https://www.oreilly.com/library/view/active-directory-5th/9781449361211/ch04.html):

The Configuration NC is the primary repository for configuration information for a forest and is replicated to every domain controller in the forest. Additionally, every writable domain controller in the forest holds a writable copy of the Configuration NC.

To access the Configuration Naming Context (NC), follow these steps:

1. Open the Active Directory Services Interfaces (ADSI) Edit tool `adsiedit.msc`.
2. Click on `Action` in the menu bar.
3. Select `Connect to...` from the dropdown menu. ![ADSI Edit window displaying a welcome message. The "Action" menu is open with options to "Connect to," "Refresh," and "Help."](https://cdn.services-k8s.prod.aws.htb.systems/content/modules/253/CN_3.png)
4. In the `Connection Settings` window, under `Select a well-known Naming Context`, choose `Configuration`. ![ADSI Edit window displaying the configuration for DC01.INLANEFREIGHT.AD. It lists containers like CN=DisplaySpecifiers, CN=Extended-Rights, CN=Services, and CN=Sites.|782](https://cdn.services-k8s.prod.aws.htb.systems/content/modules/253/CN_2.png)
5. Click `OK` to connect.
6. Once connected, you will have access to the `Configuration Naming Context`, where you can view and manage configuration settings for Active Directory. ![ADSI Edit window displaying a welcome message. The "Action" menu is open with options to "Connect to," "Refresh," and "Help."|618](https://cdn.services-k8s.prod.aws.htb.systems/content/modules/253/CN_3.png)

Consequently, any modifications made to an object within Configuration at the forest root level will be `replicated downwards` to all domains within the forest. However, it is important to note that the `reverse` is also true. If an object within Configuration undergoes a change in a child domain, that alteration will propagate `upwards` to the forest root. This behavior is due to every writable domain controller in the forest maintaining a writable copy of the forest Configuration naming context.

---

## Configuration Naming Context (NC) Replication Abuse

Configuration Naming Context (NC) replication abuse refers to an offensive tactic wherein attackers exploit the `replication` mechanism of the `Configuration Naming Context` in Active Directory to propagate unauthorized changes or configurations across the domain infrastructure. By leveraging this method, attackers can potentially introduce backdoors, escalate privileges, or manipulate critical settings, thereby compromising the security and integrity of the entire Active Directory environment.

To retrieve the `Access Control List (ACL)` rights associated with the Distinguished Name (DN) for the Configuration Naming Context (NC) in Active Directory, PowerShell offers the convenient [Get-Acl](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.security/get-acl?view=powershell-7.4) cmdlet. By executing this command, administrators can gain insights into the security permissions configured for this pivotal component.

#### Enumerate ACL's for WRITE access on Configuration Naming Context

  Configuration Naming Context (NC)

```powershell-session
PS C:\Users\Administrator> $dn = "CN=Configuration,DC=INLANEFREIGHT,DC=AD"
PS C:\Users\Administrator> $acl = Get-Acl -Path "AD:\$dn"
PS C:\Users\Administrator> $acl.Access | Where-Object {$_.ActiveDirectoryRights -match "GenericAll|Write" }

ActiveDirectoryRights : GenericAll
InheritanceType       : None
ObjectType            : 00000000-0000-0000-0000-000000000000
InheritedObjectType   : 00000000-0000-0000-0000-000000000000
ObjectFlags           : None
AccessControlType     : Allow
IdentityReference     : NT AUTHORITY\SYSTEM
IsInherited           : False
InheritanceFlags      : None
PropagationFlags      : None

ActiveDirectoryRights : CreateChild, Self, WriteProperty, ExtendedRight, Delete, GenericRead, WriteDacl, WriteOwner
InheritanceType       : Descendents
ObjectType            : 00000000-0000-0000-0000-000000000000
InheritedObjectType   : 00000000-0000-0000-0000-000000000000
ObjectFlags           : None
AccessControlType     : Allow
IdentityReference     : INLANEFREIGHT\Domain Admins
IsInherited           : False
InheritanceFlags      : ContainerInherit
PropagationFlags      : InheritOnly

ActiveDirectoryRights : GenericAll
InheritanceType       : All
ObjectType            : 00000000-0000-0000-0000-000000000000
InheritedObjectType   : 00000000-0000-0000-0000-000000000000
ObjectFlags           : None
AccessControlType     : Allow
IdentityReference     : INLANEFREIGHT\Enterprise Admins
IsInherited           : False
InheritanceFlags      : ContainerInherit
PropagationFlags      : None  
```

Looking at ACL for Configuration Naming Context (NC) we find the following entities with necessary rights to modify Configuration NC in DC.

|**User**|**Rights on Configuration Naming Context (NC)**|
|---|---|
|`NT AUTHORITY\SYSTEM`|Full Control|
|`INLANEFREIGHT\Domain Admins`|Read all, List all, Write all, All Extended rights|
|`INLANEFREIGHT\Enterprise Admins`|Full Control|

---

Given that `NT AUTHORITY\SYSTEM` holds `Full Control` or `GenericAll` rights on `Configuration Naming Context (NC)`, it's crucial to acknowledge that a `SYSTEM` account on a child domain controller (DC) wields the authority to make authoritative modifications to the `Configuration Naming Context (NC)` within the forest by querying its `local replica`. Consequently, any alterations initiated in this context will propagate back to the parent domain through the replication process. This scenario opens avenues for potential abuse, wherein the parent domain could be compromised from within the child domain.

An attacker can abuse this to carry out various attacks such as, `ADCS (Active Directory Certificate Services) attacks`, manipulate `Group Policy Objects (GPOs)` at the site level, Changing `DNS entries` or execute `GoldenGMSA (Group Managed Service Account) attacks`. These attacks can lead to unauthorized access, privilege escalation, or other compromising actions within the parent domain from child domain.

In the upcoming sections, we will delve into a detailed examination of these attacks. By dissecting each method meticulously, we aim to provide comprehensive insights into the mechanisms, implications, and mitigation strategies associated with exploiting Active Directory vulnerabilities.





