

https://software-sinner.medium.com/how-to-tunnel-and-pivot-networks-using-ligolo-ng-cf828e59e740

```
riley@mail:~$ ping 192.168.110.53
PING 192.168.110.53 (192.168.110.53) 56(84) bytes of data.
64 bytes from 192.168.110.53: icmp_seq=1 ttl=128 time=0.609 ms
```

```
kali@kali ~> nxc smb 192.168.110.53
SMB         192.168.110.53  445    PNT-SVRBPA       [*] Windows Server 2022 Build 20348 x64 (name:PNT-SVRBPA) (domain:painters.htb) (signing:False) (SMBv1:False)
```

```
kali@kali ~> nxc smb 192.168.110.53 -u 'riley' -p 'P@ssw0rd'
SMB         192.168.110.53  445    PNT-SVRBPA       [*] Windows Server 2022 Build 20348 x64 (name:PNT-SVRBPA) (domain:painters.htb) (signing:False) (SMBv1:False)
SMB         192.168.110.53  445    PNT-SVRBPA       [+] painters.htb\riley:P@ssw0rd
```

```
kali@kali ~> nxc smb 192.168.110.53 -u 'riley' -p 'P@ssw0rd' --shares
SMB         192.168.110.53  445    PNT-SVRBPA       [*] Windows Server 2022 Build 20348 x64 (name:PNT-SVRBPA) (domain:painters.htb) (signing:False) (SMBv1:False)
SMB         192.168.110.53  445    PNT-SVRBPA       [+] painters.htb\riley:P@ssw0rd
SMB         192.168.110.53  445    PNT-SVRBPA       [*] Enumerated shares
SMB         192.168.110.53  445    PNT-SVRBPA       Share           Permissions     Remark
SMB         192.168.110.53  445    PNT-SVRBPA       -----           -----------     ------
SMB         192.168.110.53  445    PNT-SVRBPA       ADMIN$                          Remote Admin
SMB         192.168.110.53  445    PNT-SVRBPA       C$                              Default share
SMB         192.168.110.53  445    PNT-SVRBPA       IPC$            READ            Remote IPC
```

