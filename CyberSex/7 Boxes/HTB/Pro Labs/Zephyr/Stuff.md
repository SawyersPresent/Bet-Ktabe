what
- Firewall
	- Sometimes these ports are blocked so you need to see what the whitelisted ports
		- 53
		- 80
		- 443
		- 445




```
 Protocol   Local Address          Foreign Address        State         PID/Program Name
========== ====================== ====================== ============= =======================
 tcp        192.168.110.51:445     192.168.210.13:52474   ESTABLISHED   0/
 tcp        192.168.110.51:22      10.10.14.4:44750       ESTABLISHED   0/
 tcp        192.168.110.51:22      10.10.14.4:47526       ESTABLISHED   0/
 tcp        192.168.110.51:22      10.10.14.5:57742       ESTABLISHED   0/
 tcp        192.168.110.51:39742   10.10.14.5:443         ESTABLISHED   4567/agent
 tcp        192.168.110.51:60856   192.168.210.13:443     ESTABLISHED   3605/python3
 tcp        192.168.110.51:22      192.168.110.51:34608   ESTABLISHED   0/
 tcp        192.168.110.51:41016   10.10.17.202:80        ESTABLISHED   36020/agent
 tcp        192.168.110.51:49542   192.168.210.10:53      ESTABLISHED   30584/agentdy
 tcp        192.168.110.51:22      10.10.17.182:52764     ESTABLISHED   0/
 tcp        192.168.110.51:22      10.10.17.191:48966     ESTABLISHED   0/
 tcp        192.168.110.51:22      10.10.14.10:39746      ESTABLISHED   0/
 tcp        192.168.110.51:38200   10.10.17.182:9001      ESTABLISHED   0/
 tcp        192.168.110.51:55750   10.10.14.4:53          ESTABLISHED   30584/agentdy
 tcp        192.168.110.51:22      10.10.17.202:52038     ESTABLISHED   0/
 tcp        192.168.110.51:34608   192.168.110.51:22      ESTABLISHED   3605/python3
 tcp        192.168.110.51:54074   192.168.210.10:135     ESTABLISHED   30584/agentdy
 tcp        192.168.110.51:22      10.10.17.202:39642     ESTABLISHED   0/
 tcp        192.168.110.51:36472   192.168.210.13:443     ESTABLISHED   3605/python3
 tcp        192.168.110.51:49950   10.10.17.202:443       ESTABLISHED   35987/WEARY_PERFORMAN

```


SMB sweep to see surroundings with NXC

```
kali@kali ~> nxc smb 192.168.110.0/24 -u 'riley' -p 'P@ssw0rd'
SMB         192.168.110.55  445    DC               [*] Windows Server 2022 Build 20348 x64 (name:DC) (domain:painters.htb) (signing:True) (SMBv1:False)
SMB         192.168.110.53  445    PNT-SVRBPA       [*] Windows Server 2022 Build 20348 x64 (name:PNT-SVRBPA) (domain:painters.htb) (signing:False) (SMBv1:False)
SMB         192.168.110.52  445    PNT-SVRSVC       [*] Windows Server 2022 Build 20348 x64 (name:PNT-SVRSVC) (domain:painters.htb) (signing:False) (SMBv1:False)
SMB         192.168.110.55  445    DC               [+] painters.htb\riley:P@ssw0rd
SMB         192.168.110.53  445    PNT-SVRBPA       [+] painters.htb\riley:P@ssw0rd
SMB         192.168.110.52  445    PNT-SVRSVC       [+] painters.htb\riley:P@ssw0rd
Running nxc against 256 targets ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
```


```
sudo ip tuntap add user kali mode tun ligolo
sudo ip link set ligolo up
sudo ip route add 192.168.110.0/24 dev ligolo
sudo ip route add 192.168.210.0/24 dev ligolo
sudo ip route add 240.0.0.1 dev ligolo
```

```
WARN[0000] Using default selfcert domain 'ligolo', beware of CTI, SOC and IoC!
WARN[0000] Using self-signed certificates
ERRO[0000] Certificate cache error: open ligolo-selfcerts/ligolo_cert: permission denied, returning a new certificate
ligolo-ng » session
? Specify a session : 2 - #2 - riley@mail - 10.10.110.35:5057
[Agent : riley@mail] » start --tun ligolo
[Agent : riley@mail] » INFO[0896] Starting tunnel to riley@mail

```




https://software-sinner.medium.com/how-to-tunnel-and-pivot-networks-using-ligolo-ng-cf828e59e740