

```
[project]
name = "netexec"
dynamic = ["version"]
description = "The Network Execution tool"
readme = "README.md"
requires-python = ">=3.12,<4.0"   # <-- change this line
license = { text = "BSD-2-Clause" }
authors = [
  { name = "Marshall Hallenbeck", email = "marshall.hallenbeck@gmail.com" },
  { name = "Alexander Neff", email = "alex99.neff@gmx.de" },
  { name = "Thomas Seigneuret", email = "seigneuret.thomas@pm.me" }
]

```


```
kali@kali ~/w/a/NetExec (main)> poetry env use python3.13
Using virtualenv: /home/kali/.cache/pypoetry/virtualenvs/netexec-tDXwFuxn-py3.13
```


```
                                                 ~/.local/share/pipx/venvs/netexec/lib/python3.13/site-packages/nxc/modules/
(venv) kali@kali ~/w/a/N/n/modules (main)> nxc ldap -L
/home/kali/.local/share/pipx/venvs/netexec/lib/python3.13/site-packages/masky/lib/smb.py:6: UserWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html. The pkg_resources package is slated for removal as early as 2025-11-30. Refrain from using this package or pin to Setuptools<81.
  from pkg_resources import resource_filename
[-] Failed loading module at /home/kali/.local/share/pipx/venvs/netexec/lib/python3.13/site-packages/nxc/modules/certipy-find.py: No module named 'certipy'
LOW PRIVILEGE MODULES
[*] adcs                      Find PKI Enrollment Services in Active Directory and Certificate Templates Names
[*] badsuccessor              Check if vulnerable to bad successor attack (DMSA)
[*] daclread                  Read and backup the Discretionary Access Control List of objects. Be careful, this module cannot read the DACLS recursively, see more explanation in the options.
[*] dump-computers            Dumps all computers in the domain
[*] entra-id                  Find the Entra ID sync server
[*] enum_trusts               [REMOVED] Extract all Trust Relationships, Trusting Direction, and Trust Transitivity
[*] find-computer             Finds computers in the domain via the provided text
[*] get-desc-users            Get description of the users. May contained password
[*] get-info-users            Get the info field of all users. May contain password
[*] get-network               Query all DNS records with the corresponding IP from the domain.
[*] get-unixUserPassword      Get unixUserPassword attribute from all users in ldap
[*] get-userPassword          Get userPassword attribute from all users in ldap
[*] group-mem                 [REMOVED] Retrieves all the members within a Group
[*] groupmembership           Query the groups to which a user belongs.
[*] laps                      Retrieves all LAPS passwords which the account has read permissions for.
[*] ldap-checker              [REMOVED] Checks whether LDAP signing and channel binding are required and / or enforced
[*] maq                       Retrieves the MachineAccountQuota domain-level attribute
[*] obsolete                  Extract all obsolete operating systems from LDAP
[*] pre2k                     Identify pre-created computer accounts, save the results to a file, and obtain TGTs for each
[*] pso                       Module to get the Fine Grained Password Policy/PSOs
[*] sccm                      Find a SCCM infrastructure in the Active Directory
[*] subnets                   Retrieves the different Sites and Subnets of an Active Directory
[*] user-desc                 Get user descriptions stored in Active Directory
[*] whoami                    Get details of provided user
```




```
(venv) kali@kali ~/w/a/N/n/modules (main)> pipx inject netexec "certipy-ad==5.0.3"
  injected package certipy-ad into venv netexec
done! ✨ 🌟 ✨

```




```
(venv) kali@kali ~/w/a/N/n/modules (main)> nxc ldap -L
/home/kali/.local/share/pipx/venvs/netexec/lib/python3.13/site-packages/masky/lib/smb.py:6: UserWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html. The pkg_resources package is slated for removal as early as 2025-11-30. Refrain from using this package or pin to Setuptools<81.
  from pkg_resources import resource_filename
LOW PRIVILEGE MODULES
[*] adcs                      Find PKI Enrollment Services in Active Directory and Certificate Templates Names
[*] badsuccessor              Check if vulnerable to bad successor attack (DMSA)
[*] certipy-find              
[*] daclread                  Read and backup the Discretionary Access Control List of objects. Be careful, this module cannot read the DACLS recursively, see more explanation in the options.
[*] dump-computers            Dumps all computers in the domain
[*] entra-id                  Find the Entra ID sync server
[*] enum_trusts               [REMOVED] Extract all Trust Relationships, Trusting Direction, and Trust Transitivity
[*] find-computer             Finds computers in the domain via the provided text
[*] get-desc-users            Get description of the users. May contained password
[*] get-info-users            Get the info field of all users. May contain password
[*] get-network               Query all DNS records with the corresponding IP from the domain.
[*] get-unixUserPassword      Get unixUserPassword attribute from all users in ldap
[*] get-userPassword          Get userPassword attribute from all users in ldap
[*] group-mem                 [REMOVED] Retrieves all the members within a Group
[*] groupmembership           Query the groups to which a user belongs.
[*] laps                      Retrieves all LAPS passwords which the account has read permissions for.
[*] ldap-checker              [REMOVED] Checks whether LDAP signing and channel binding are required and / or enforced
[*] maq                       Retrieves the MachineAccountQuota domain-level attribute
[*] obsolete                  Extract all obsolete operating systems from LDAP
[*] pre2k                     Identify pre-created computer accounts, save the results to a file, and obtain TGTs for each
[*] pso                       Module to get the Fine Grained Password Policy/PSOs
[*] sccm                      Find a SCCM infrastructure in the Active Directory
[*] subnets                   Retrieves the different Sites and Subnets of an Active Directory
[*] user-desc                 Get user descriptions stored in Active Directory
[*] whoami                    Get details of provided user

HIGH PRIVILEGE MODULES (requires admin privs)
```


