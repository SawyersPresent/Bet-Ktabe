
1. What userAccountControl flag indicates a user is vulnerable to As-Rep Roasting? (as shown in the example)
	1. `DoesNotRequirePreauth`
2. What nxc ldap flag is used to perform an AS-REPRoast attack? (i.e. --spn)
	1. `--asreproast`
3. What hashcat mode used in the example to crack the TGT? (i.e. 1000)
	1. `18200`
4. What john format is used for AS-REP hashes? (i.e. raw-md5)
	1. `krb5asrep`
5. What Linux command can be used to capture network traffic to a pcap file? (i.e. netstat -a)
	1.  `tcpdump`
6. What hashcat mode is used for AS-REQ hashes? (i.e. 19800)
	1. `19900`
7. In a KDC-REQ-BODY structure, what is the name-type value for NT_PRINCIPAL? (i.e. 2)
	1. 1
8. What field in both KDC-REQ-BODY and KDC-REP structures identifies the client's principal name? (i.e. sname)
	1. `cname`
9. What field in a KDC-REQ-BODY structure identifies the service principal name being requested? (i.e. cname)
	1. `sname`
10. What AS_REP field contains the encrypted session key for an AS-REP response, as per RFC 4120, Section 5.4.2? (i.e. ticket)
	1. 
11. What GetUserSPNs.py option allows requesting service tickets for SPNs without a valid TGT, given a DONT_REQ_PREAUTH account? (i.e. --dont-use-tgt)
	1. `-no-preauth`
12. What is the name of the Microsoft-proprietary structure that defines the encrypted portion of a service ticket? (use the format that Microsoft Documentation officially refer to it as, i.e. MS-PCNA)
	1. `MS-PAC`
13. What PAC structure contains the authenticating user's identity details? (i.e. PAC_CLIENT_INFO)
	1. `PAC_LOGON_INFO`
14. What Impacket tool is used to forge a Silver Ticket? (i.e. getnthash.py)
	1. `tickerter.py`
15. What ticketer.py flag specifies the target Service Principal Name? (i.e. -service)
	1. `-spn`
16. What ticketer.py flag specifies the domain's SID? (i.e. -sid)
	1. `-domain-sid`
17. What ticketer.py flag specifies the NTLM hash of the service account? (i.e. -hash)
	1. `-nthash`
18. What S4U subprotocol allows a service to obtain a service ticket for itself without requiring user authentication? (i.e. s4u2proxy, all lowercase)
	1. `s4u2self`
19. What Impacket tool is used to perform S4U2self requests? (i.e. getTGT.py)
	1. `getST.py`
20. When using SSH to authenticate to a Windows host with a service ticket, but no TGT. You must use the lower-case for the host SPN. True or False?
	1. True
21. What S4U subprotocol allows a service to request a service ticket for another service on behalf of a user? (i.e. s4u2self, all lowercase)
	1. `s4u2proxy`
22. What PowerView cmdlet is used to enumerate computers configured with Unconstrained Delegation? (i.e. Get-ADComputer)
	1. `Get-DomainComputer -Unconstrained -Select dNSHostName`
23. What Rubeus.exe command is used to monitor for new TGTs being presented to a machine configured with Unconstrained Delegation? (i.e. kerberoast)
	1. `.\Rubeus.exe monitor /interval:5 /nowrap`
24. What Rubeus.exe flag is used to monitor only for TGTs presented by a specific target user? (i.e. --user)
	1. `/targetuser:DC02$`
25. What RpcRemoteFindFirstPrinterChangeNotificationEx parameter can be used to coerce a remote machine into authenticating to a local machine? (i.e. hPrinter)
	1. `pszLocalMachine`
26. What PowerView cmdlet and flag are used to enumerate computers configured for Constrained Delegation? (i.e. Get-DomainUser -TrustedToDelegate)
	1. `Get-DomainComputer -TrustedToAuth -Select cn,msDS-AllowedToDelegateTo,userAccountControl`
27. What userAccountControl flag indicates a machine is allowed to perform Protocol Transition? (i.e. TRUSTED_FOR_DELEGATION)
	1. `TRUSTED_TO_AUTH_FOR_DELEGATION`
28. What nxc ldap flag is used to find delegation configurations? (i.e. --get-sid)
	1. `--find-delegation`
29. What getST.py flag allows tampering with the service principal name in a service ticket after it has been obtained? (i.e. -service-override)
	1. `-altservice`
30. What Active Directory attribute is set on a resource to allow other services to delegate to it via RBCD? (i.e. msDS-AllowedDelegation)
	1. `msDS-AllowedToActOnBehalfOfOtherIdentity`
31. What Impacket tool is used to perform RBCD attacks (specifically to modify delegation rights)? (i.e. addDelegation.py)
	1. `rbcd.py`
32. What is the name of the attack that uses domain replication to obtain a copy of the domain's credentials? (all lowercase, i.e. genericall)
	1. `DCSync`
33. What RPC call is used by Domain Controllers to replicate changes to each other? (i.e. NetrLogonGetDomainInfo)
	1. `IDL_DRSGetNCChanges`
34. What two rights are required to make the `IDL_DRSGetNCChanges` RPC call? (i.e. `DS-Replication-Write,DS-Replication-Add`; comma separated, no space.)
	1. `DS-Replication-Get-Changes`,` DS-Replication-Get-Changes-All`
35. What type of ticket skips the AS-REQ and AS-REP steps and is completely forged using the krbtgt hash? (i.e. Silver Ticket)
	1. Golden Ticket
36. What type of ticket allows for the usual AS-REQ and AS-REP steps to be performed, but then modifies the PAC to add arbitrary principals? (i.e. Golden Ticket)
	1. Diamond Ticket
37. What Kerberos extension allows one user to obtain a service ticket to another user's account without that user needing a long-term key on disk? (i.e. S4U2proxy)
	1. `U2U`
38. What type of ticket obtains a legitimate PAC for a target user via S4U2self + U2U and injects it into an attacker-controlled account's TGT? (i.e. Golden Ticket)
	1. Saphire Ticket