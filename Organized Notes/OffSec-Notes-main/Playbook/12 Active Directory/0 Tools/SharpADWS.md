
https://github.com/wh0amitz/SharpADWS



What is it? How do I use it?. idk still experimenting





```
*Evil-WinRM* PS C:\Users\Administrator\Documents> .\SharpADWS.exe

SharpADWS 1.0.0-beta - Copyright (c) 2024 WHOAMI (whoamianony.top)

  -h                      Display this help screen

Connection options:
  -d                      Specify domain for enumeration
  -u                      Username to use for ADWS Connection
  -p                      Password to use for ADWS Connection

Supported methods:
  Cache                   Dump all objectSids to cache file for Acl methods
  Acl                     Enumerate and analyze DACLs for specified objects, specifically Users, Computers, Groups, Domains, DomainControllers and GPOs
  DCSync                  Enumerate all DCSync-capable accounts and can set DCSync backdoors
  DontReqPreAuth          Enumerates all accounts that do not require kerberos preauthentication, and can enable this option for accounts
  Kerberoastable          Enumerates all Kerberoastable accounts, and can write SPNs for accounts
  AddComputer             Add a machine account within the scope of ms-DS-MachineAccountQuota for RBCD attack
  RBCD                    Read, write and remove msDS-AllowedToActOnBehalfOfOtherIdentity attributes for Resource-Based Constrained Delegation attack
  Certify                 Enumerate all ADCS data like Certify.exe, and can write template attributes
  Whisker                 List, add and remove msDS-KeyCredentialLink attribute like Whisker.exe for ShadowCredentials attack
  FindDelegation          Enumerate all delegation relationships for the target domain

Acl options:
  -dn                     RFC 2253 DN to base search from
  -scope                  Set your Scope, support Base (Default), Onelevel, Subtree
  -trustee                The sAMAccountName of a security principal to check for its effective permissions
  -right                  Filter DACL for a specific AD rights
  -rid                    Specify a rid value and filter out DACL that security principal's rid is greater than it
  -user                   Enumerate DACL for all user objects
  -computer               Enumerate DACL for all computer objects
  -group                  Enumerate DACL for all group objects
  -domain                 Enumerate DACL for all domain objects
  -domaincontroller       Enumerate DACL for all domain controller objects
  -gpo                    Enumerate DACL for all gpo objects

DCSync options:
  -action [{list, write}] Action to operate on DCSync method
          list            List all accounts with DCSync permissions
          write           Escalate accounts with DCSync permissions
  -target                 Specify the sAMAccountName of the account

DontReqPreAuth options:
  -action [{list, write}] Action to operate on DontReqPreAuth method
          list            List all accounts that do not require kerberos preauthentication
          write           Enable do not require kerberos preauthentication for an account
  -target                 Specify the sAMAccountName of the account

Kerberoastable options:
  -action [{list, write}] Action to operate on Kerberoastable method
          list            List all kerberoastable accounts
          write           Write SPNs for an account to kerberoast
  -target                 Specify the sAMAccountName of the account

AddComputer options:
  -computer-name          Name of computer to add, without '$' suffix
  -computer-pass          Password to set for the computer

RBCD options:
  -action [{read,write,remove}]
                          Action to operate on RBCD method
          read            Read the msDS-AllowedToActOnBehalfOfOtherIdentity attribute of the account
          write           Write the msDS-AllowedToActOnBehalfOfOtherIdentity attribute of the account
          remove          Remove the msDS-AllowedToActOnBehalfOfOtherIdentity attribute value of the account added by the write action

Certify options:
  -action [{find, modify}]
                          Action to operate on Certify method
          find            Find all CA and certificate templates
          modify          Modify certificate templates
  -enrolleeSuppliesSubject
                          Enumerate certificate templates with CT_FLAG_ENROLLEE_SUPPLIES_SUBJECT flag for find action,
                          and can enable CT_FLAG_ENROLLEE_SUPPLIES_SUBJECT flag for modify action
  -clientAuth             Enumerate certificate templates with client authentication pKIExtendedKeyUsage for find action,
                          and can enable Client Authentication for modify action

Whisker options:
  -action [{list, add, remove}]
                          Action to operate on ShadowCredentials method
          list            List all the values of the msDS-KeyCredentialLink attribute for an account
          add             Add a new value to the msDS-KeyCredentialLink attribute for an account
          remove          Remove a value from the msDS-KeyCredentialLink attribute for an account
  -device-id              Specify the DeviceID to remove
  -target                 Specify the sAMAccountName of the account

FindDelegation options:
  No options, just run!

```




# 

```
*Evil-WinRM* PS C:\Users\Administrator\Documents> .\SharpADWS.exe Cache
```



# 