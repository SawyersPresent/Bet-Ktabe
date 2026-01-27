
Wordlists

```python
# Vhosts/subdomains
/usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt  # 4989
/usr/share/seclists/Discovery/DNS/subdomains-top1million-20000.txt # 19966

# Extensions
/usr/share/seclists/Discovery/Web-Content/web-extensions.txt # 41

# Directory Fuzzing
/usr/share/seclists/Discovery/Web-Content/raft-small-directories.txt  # 20116
/usr/share/seclists/Discovery/Web-Content/raft-medium-directories.txt # 30000

# File Fuzzing
/usr/share/seclists/Discovery/Web-Content/raft-small-files.txt  # 11424
/usr/share/seclists/Discovery/Web-Content/raft-medium-files.txt # 17129

# Parameter names
/usr/share/seclists/Discovery/Web-Content/burp-parameter-names.txt # 6453

# Special characters
/usr/share/seclists/Fuzzing/special-chars.txt # 32

# All characters and symbols
/usr/share/seclists/Fuzzing/alphanum-case-extra.txt # 95

# Usernames
/home/kali/repos/statistically-likely-usernames/jsmith2.txt     # 4997
/usr/share/seclists/Usernames/Names/names.txt                   # 10177
/home/kali/repos/statistically-likely-usernames/jsmith.txt      # 48705
/usr/share/seclists/Usernames/xato-net-10-million-usernames.txt # 8295455

# SSH Key formats
id_rsa
id_ecdsa
id_ecdsa_sk
id_ed25519
id_ed25519_sk
```


**Note:** `directory-list-2.3` contains comments and requires `-ic` to ignore comments in `ffuf`

### Exploit Specific

```
# LFI
/usr/share/seclists/Fuzzing/LFI/LFI-Jhaddix.txt # 929
```

technology specific

```
# IIS
/usr/share/seclists/Discovery/Web-Content/IIS.fuzz.txt
```



- is this homebrew?
	- less of a hassle


CVEDETAILS

https://www.cvedetails.com/vulnerability-list/vendor_id-3885/product_id-6856/Xwiki-Xwiki.html

look for high CVE's and depending on what you want, user to root, or nothing to user etc.