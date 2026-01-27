



use msfconsole to can and enumerate SMB


most useful ones so far are

- `auxiliary/scanner/smb/smb_version`
- `auxiliary/scanner/smb/smb_enumusers`
- `auxiliary/scanner/snmp/snmp_enumshares`
- `auxiliary/scanner/smb/smb_login`
- `auxiliary/scanner/snmp/snmp_enumshares`

```
msf6 > search aux scanner smb

Matching Modules
================

   #   Name                                                            Disclosure Date  Rank    Check  Description
   -   ----                                                            ---------------  ----    -----  -----------
   0   auxiliary/scanner/http/citrix_dir_traversal                     2019-12-17       normal  No     Citrix ADC (NetScaler) Directory Traversal Scanner
   1   auxiliary/scanner/smb/impacket/dcomexec                         2018-03-19       normal  No     DCOM Exec
   2   auxiliary/scanner/smb/impacket/secretsdump                                       normal  No     DCOM Exec
   3   auxiliary/scanner/dcerpc/dfscoerce                                               normal  No     DFSCoerce
   4   auxiliary/scanner/smb/smb_ms17_010                                               normal  No     MS17-010 SMB RCE Detection
   5   auxiliary/scanner/smb/psexec_loggedin_users                                      normal  No     Microsoft Windows Authenticated Logged In Users Enumeration
   6   auxiliary/scanner/dcerpc/petitpotam                                              normal  No     PetitPotam
   7   auxiliary/scanner/sap/sap_smb_relay                                              normal  No     SAP SMB Relay Abuse
   8   auxiliary/scanner/sap/sap_soap_rfc_eps_get_directory_listing                     normal  No     SAP SOAP RFC EPS_GET_DIRECTORY_LISTING Directories Information Disclosure
   9   auxiliary/scanner/sap/sap_soap_rfc_pfl_check_os_file_existence                   normal  No     SAP SOAP RFC PFL_CHECK_OS_FILE_EXISTENCE File Existence Check
   10  auxiliary/scanner/sap/sap_soap_rfc_rzl_read_dir                                  normal  No     SAP SOAP RFC RZL_READ_DIR_LOCAL Directory Contents Listing
   11  auxiliary/scanner/smb/smb_enumusers_domain                                       normal  No     SMB Domain User Enumeration
   12  auxiliary/scanner/smb/smb_enum_gpp                                               normal  No     SMB Group Policy Preference Saved Passwords Enumeration
   13  auxiliary/scanner/smb/smb_login                                                  normal  No     SMB Login Check Scanner
   14  auxiliary/scanner/smb/smb_lookupsid                                              normal  No     SMB SID User Enumeration (LookupSid)
   15  auxiliary/admin/smb/check_dir_file                                               normal  No     SMB Scanner Check File/Directory Utility
   16  auxiliary/scanner/smb/pipe_auditor                                               normal  No     SMB Session Pipe Auditor
   17  auxiliary/scanner/smb/pipe_dcerpc_auditor                                        normal  No     SMB Session Pipe DCERPC Auditor
   18  auxiliary/scanner/smb/smb_enumshares                                             normal  No     SMB Share Enumeration
   19  auxiliary/scanner/smb/smb_enumusers                                              normal  No     SMB User Enumeration (SAM EnumUsers)
   20  auxiliary/scanner/smb/smb_version                                                normal  No     SMB Version Detection
   21  auxiliary/scanner/snmp/snmp_enumshares                                           normal  No     SNMP Windows SMB Share Enumeration
   22  auxiliary/scanner/smb/smb_uninit_cred                                            normal  Yes    Samba _netr_ServerPasswordSet Uninitialized Credential State
   23  auxiliary/scanner/smb/impacket/wmiexec                          2018-03-19       normal  No     WMI Exec


Interact with a module by name or index. For example info 23, use 23 or use auxiliary/scanner/smb/impacket/wmiexec

```



set `RHOSTS` and `LHOST` and `run`

```
msf6 auxiliary(scanner/smb/smb_version) > run

[*] 192.168.244.133:139   - SMB Detected (versions:) (preferred dialect:) (signatures:optional)
[*] 192.168.244.133:139   -   Host could not be identified: Unix (Samba 2.2.1a)
[*] 192.168.244.133:      - Scanned 1 of 1 hosts (100% complete)
[*] Auxiliary module execution completed
```


Using SMBClient


```
kali@kali ~> smbclient -L  \\\\192.168.244.133\\
Server does not support EXTENDED_SECURITY  but 'client use spnego = yes' and 'client ntlmv2 auth = yes' is set
Anonymous login successful
Password for [WORKGROUP\kali]:

	Sharename       Type      Comment
	---------       ----      -------
	IPC$            IPC       IPC Service (Samba Server) <----------- Directory
	ADMIN$          IPC       IPC Service (Samba Server) <--------- Directory
Reconnecting with SMB1 for workgroup listing.
Server does not support EXTENDED_SECURITY  but 'client use spnego = yes' and 'client ntlmv2 auth = yes' is set
Anonymous login successful

	Server               Comment
	---------            -------
	KIOPTRIX             Samba Server  <----- Server name and comment

	Workgroup            Master
	---------            -------
	MYGROUP              KIOPTRIX   <--------- More Description

```

or just manually enter the SMB and dick around yourself

```
kali@kali ~> smbclient \\\\192.168.244.133\\IPC\$
Password for [WORKGROUP\kali]:
Server does not support EXTENDED_SECURITY  but 'client use spnego = yes' and 'client ntlmv2 auth = yes' is set
Anonymous login successful
Try "help" to get a list of possible commands.
smb: \> ls
NT_STATUS_NETWORK_ACCESS_DENIED listing \*
smb: \> 

```


in my case the `$` escapes but i assume that most others wont have my same issues hence you might not need to escape it like me with an extra `\`

