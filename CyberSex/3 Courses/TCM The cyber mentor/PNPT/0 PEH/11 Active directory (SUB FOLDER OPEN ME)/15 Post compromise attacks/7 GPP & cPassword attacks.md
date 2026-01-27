

- Overview
	- Group Policy preferences (GPP allowed admins to create policies using embedded credentials
	- the credentials were encrypted and placed in a "cPassword"
	- The key was accidentally released (whoopsie daisy)
	- Patched in MS14-025 but it doesnt prevent previous uses
	- STILL RELEVANT ON PENTESTS *(ALLEGDLY)*


theres a decrypt program for kali
```
gpp-decerypt <cPassword>
```

in metasploit
```
auxiliary/smb_enum_gpp
```


other scripts
[gpp-decrypt](https://github.com/t0thkr1s/gpp-decrypt)
```
python3 gpp-decrypt.py -c <cPASSWORD>
python3 gpp-decrypt.py -f <Gpp_file>
```
