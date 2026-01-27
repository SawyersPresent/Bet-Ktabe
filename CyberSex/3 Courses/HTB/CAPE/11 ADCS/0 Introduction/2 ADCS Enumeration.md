


































---
# Content

When auditing an organization's infrastructure, determining the presence and configuration of Active Directory Certificate Services (AD CS) becomes crucial. While some organizations opt for AD CS deployment, others may forego it entirely. This variability necessitates investigating whether the ADCS service exists within the Domain being audited.

In certain environments like lab setups or specific Capture The Flag (CTF) challenges, the ADCS server might be installed on the Domain Controller. However, in most cases, organizations prefer installing this service on an independent server. Yet, exceptions do exist, making it essential to ascertain the presence of ADCS and its hosting server.

## Enumeration From Windows

One indicative factor of an ADCS installation is the presence of the built-in `Cert Publishers` group. This group typically authorizes `Certificate Authorities` to publish certificates to the directory, often indicating the presence of an ADCS server. That means that the ADCS server will be a member of this group. We can use `net group`, `net localgroup`, or any other group enumeration tool to verify this:

#### Querying Cert Publishers group membership

  ADCS Enumeration

```powershell-session
PS C:\Tools> net localgroup "Cert Publishers"
Alias name     Cert Publishers
Comment        Members of this group are permitted to publish certificates to the directory

Members

-------------------------------------------------------------------------------
LAB-DC$
The command completed successfully.
```

Alternatively, exploring the `Public Key Services container` structure unveils not only the existence of ADCS but also details its configuration. All ADCS-related containers reside within the configuration naming context under the `Public Key Services container`:

```
CN=Public Key Services, CN=Services, CN=Configuration, DC={forest root domain}
```

Additionally, the [SpecterOps](https://specterops.io/) team, who published the White Paper [Certified Pre-Owned - Abusing Active Directory Certificate Services](https://specterops.io/wp-content/uploads/sites/3/2022/06/Certified_Pre-Owned.pdf) outlined eight attack types on ADCS labeled as `ESC1` to `ESC8`. Additionally, they developed [Certify](https://github.com/GhostPack/Certify), a C# tool designed to enumerate and exploit misconfigurations within Active Directory Certificate Services (AD CS).

In order to create the `Certify` executable, we need to compile the code from the [Certify Github](https://github.com/GhostPack/Certify) or we can use the binary compiled in the [Flangvik SharpCollection repository](https://github.com/Flangvik/SharpCollection/blob/master/NetFramework_4.7_x64/Certify.exe).

To do the enumeration using Certify.exe we only need to run `Certify.exe find` from an authenticated session with a domain user:

#### Enumerate ESC9 from Windows

  ADCS Enumeration

```powershell-session
PS C:\Tools> .\Certify.exe find

   _____          _   _  __
  / ____|        | | (_)/ _|
 | |     ___ _ __| |_ _| |_ _   _
 | |    / _ \ '__| __| |  _| | | |
 | |___|  __/ |  | |_| | | | |_| |
  \_____\___|_|   \__|_|_|  \__, |
                             __/ |
                            |___./
  v1.1.0

[*] Action: Find certificate templates
[*] Using the search base 'CN=Configuration,DC=lab,DC=local'

...SNIP...
    CA Name                               : LAB-DC.lab.local\lab-LAB-DC-CA
    Template Name                         : ESC9
    Schema Version                        : 2
    Validity Period                       : 99 years
    Renewal Period                        : 6 weeks
    msPKI-Certificate-Name-Flag          : SUBJECT_ALT_REQUIRE_UPN, SUBJECT_ALT_REQUIRE_EMAIL, SUBJECT_REQUIRE_EMAIL, SUBJECT_REQUIRE_DIRECTORY_PATH
    mspki-enrollment-flag                 : INCLUDE_SYMMETRIC_ALGORITHMS, PUBLISH_TO_DS, AUTO_ENROLLMENT, NO_SECURITY_EXTENSION
    Authorized Signatures Required        : 0
    pkiextendedkeyusage                   : Client Authentication, Encrypting File System, Secure Email
    mspki-certificate-application-policy  : Client Authentication, Encrypting File System, Secure Email
    Permissions
      Enrollment Permissions
        Enrollment Rights           : LAB\Domain Admins             S-1-5-21-2570265163-3918697770-3667495639-512
                                      LAB\Domain Users              S-1-5-21-2570265163-3918697770-3667495639-513
                                      LAB\Enterprise Admins         S-1-5-21-2570265163-3918697770-3667495639-519
      Object Control Permissions
        Owner                       : LAB\Administrator             S-1-5-21-2570265163-3918697770-3667495639-500
        WriteOwner Principals       : LAB\Administrator             S-1-5-21-2570265163-3918697770-3667495639-500
                                      LAB\Domain Admins             S-1-5-21-2570265163-3918697770-3667495639-512
                                      LAB\Enterprise Admins         S-1-5-21-2570265163-3918697770-3667495639-519
        WriteDacl Principals        : LAB\Administrator             S-1-5-21-2570265163-3918697770-3667495639-500
                                      LAB\Domain Admins             S-1-5-21-2570265163-3918697770-3667495639-512
                                      LAB\Enterprise Admins         S-1-5-21-2570265163-3918697770-3667495639-519
        WriteProperty Principals    : LAB\Administrator             S-1-5-21-2570265163-3918697770-3667495639-500
                                      LAB\Domain Admins             S-1-5-21-2570265163-3918697770-3667495639-512
                                      LAB\Enterprise Admins         S-1-5-21-2570265163-3918697770-3667495639-519
...SNIP...
```

**Note:** `Certify.exe` typically fetches credentials from the current context session, which can be convenient or problematic based on scenarios requiring specific user privileges.

## Enumeration from Linux

From Linux, we can use [NetExec](https://github.com/Pennyw0rth/NetExec) to identify if there are ADCS servers in the Domain using the ADCS module:

#### NetExec ADCS enumeration

  ADCS Enumeration

```shell-session
Hillside_1@htb[/htb]$ netexec ldap 10.129.205.199 -u "blwasp" -p "Password123!" -M adcs
SMB         10.129.205.199  445    LAB-DC           [*] Windows 10.0 Build 17763 x64 (name:LAB-DC) (Domain:lab.local) (signing:False) (SMBv1:False)
LDAP        10.129.205.199  389    LAB-DC           [+] lab.local\blwasp:Password123! 
ADCS        10.129.205.199  389    LAB-DC           [*] Starting LDAP search with search filter '(objectClass=pKIEnrollmentService)'
ADCS                                                Found PKI Enrollment Server: LAB-DC.lab.local
ADCS                                                Found CN: lab-LAB-DC-CA
ADCS                                                Found PKI Enrollment WebService: https://lab-dc.lab.local/lab-LAB-DC-CA_CES_Kerberos/service.svc/CE
```

In addition, the Linux counterpart of `Certify.exe` is [Certipy](https://github.com/ly4k/Certipy), a Python tool created by [Oliver Lyak](https://twitter.com/ly4k_) that can then be used to operate multiple attacks and enumeration operations. To date, this is the best enumeration (and exploitation) tooling, featuring [BloodHound](https://github.com/BloodHoundAD/BloodHound) support, extensive control over its behavior, and support of many (if not all) attack scenarios.

To install Certipy we can use `pip`:

#### Install Certipy with pip

  ADCS Enumeration

```shell-session
Hillside_1@htb[/htb]$ pip3 install certipy-ad
Requirement already satisfied: certipy-ad in /usr/local/lib/python3.9/dist-packages/certipy_ad-4.8.2-py3.9.egg (4.8.2)
Requirement already satisfied: asn1crypto in /usr/lib/python3/dist-packages (from certipy-ad) (1.4.0)
...SNIP...
```

To use `certipy`, we need to provide the credentials of a domain user. We will also include the domain IP, although we can skip this step if we have DNS resolution with the domain. Finally, we will use the `-stdout` option to specify that we want to display the result of the enumeration:

#### Using Certipy to enumerate ADCS Service

  ADCS Enumeration

```shell-session
Hillside_1@htb[/htb]$ certipy find -u 'BlWasp@lab.local' -p 'Password123!' -dc-ip 10.129.205.199 -stdout
[*] Finding certificate templates
[*] Found 40 certificate templates
[*] Finding certificate authorities
[*] Found 1 certificate authority
[*] Found 18 enabled certificate templates
[*] Trying to get CA configuration for 'lab-LAB-DC-CA' via CSRA
[*] Got CA configuration for 'lab-LAB-DC-CA'
[*] Enumeration output:
Certificate Authorities
  0
    CA Name                             : lab-LAB-DC-CA
    DNS Name                            : LAB-DC.lab.local
    Certificate Subject                 : CN=lab-LAB-DC-CA, DC=lab, DC=local
    Certificate Serial Number           : 16BD1CE8853DB8B5488A16757CA7C101
    Certificate Validity Start          : 2022-03-26 00:07:46+00:00
    Certificate Validity End            : 2027-03-26 00:17:46+00:00
    Web Enrollment                      : Enabled
    User Specified SAN                  : Enabled
    Request Disposition                 : Issue
    Enforce Encryption for Requests     : Disabled
    Permissions
      Owner                             : LAB.LOCAL\Administrators
      Access Rights
        Enroll                          : LAB.LOCAL\Authenticated Users
                                          LAB.LOCAL\Black Wasp
                                          LAB.LOCAL\user_manageCA
        ManageCa                        : LAB.LOCAL\Black Wasp
                                          LAB.LOCAL\user_manageCA
                                          LAB.LOCAL\Domain Admins
                                          LAB.LOCAL\Enterprise Admins
                                          LAB.LOCAL\Administrators
        ManageCertificates              : LAB.LOCAL\Domain Admins
                                          LAB.LOCAL\Enterprise Admins
                                          LAB.LOCAL\Administrators
    [!] Vulnerabilities
      ESC6                              : Enrollees can specify SAN and Request Disposition is set to Issue. Does not work after May 2022
      ESC7                              : 'LAB.LOCAL\\Black Wasp' has dangerous permissions
      ESC8                              : Web Enrollment is enabled and Request Disposition is set to Issue
      ESC11                             : Encryption is not enforced for ICPR requests and Request Disposition is set to Issue
Certificate Templates
...SNIP...
  39
    Template Name                       : ESC1
    Display Name                        : ESC1
    Certificate Authorities             : lab-LAB-DC-CA
    Enabled                             : True
    Client Authentication               : True
    Enrollment Agent                    : False
    Any Purpose                         : False
    Enrollee Supplies Subject           : True
    Certificate Name Flag               : EnrolleeSuppliesSubject
    Enrollment Flag                     : PublishToDs
                                          IncludeSymmetricAlgorithms
    Private Key Flag                    : 16777216
                                          65536
                                          ExportableKey
    Extended Key Usage                  : Client Authentication
                                          Secure Email
                                          Encrypting File System
    Requires Manager Approval           : False
    Requires Key Archival               : False
    Authorized Signatures Required      : 0
    Validity Period                     : 99 years
    Renewal Period                      : 6 weeks
    Minimum RSA Key Length              : 2048
    Permissions
      Enrollment Permissions
        Enrollment Rights               : LAB.LOCAL\Domain Admins
                                          LAB.LOCAL\Domain Users
                                          LAB.LOCAL\Enterprise Admins
      Object Control Permissions
        Owner                           : LAB.LOCAL\Administrator
        Write Owner Principals          : LAB.LOCAL\Domain Admins
                                          LAB.LOCAL\Enterprise Admins
                                          LAB.LOCAL\Administrator
        Write Dacl Principals           : LAB.LOCAL\Domain Admins
                                          LAB.LOCAL\Enterprise Admins
                                          LAB.LOCAL\Administrator
        Write Property Principals       : LAB.LOCAL\Domain Admins
                                          LAB.LOCAL\Enterprise Admins
                                          LAB.LOCAL\Administrator
    [!] Vulnerabilities
      ESC1                              : 'LAB.LOCAL\\Domain Users' can enroll, enrollee supplies subject and template allows client authentication
```

In subsequent sections, we'll delve deeper into the functionality and diverse attack scenarios using these tools.