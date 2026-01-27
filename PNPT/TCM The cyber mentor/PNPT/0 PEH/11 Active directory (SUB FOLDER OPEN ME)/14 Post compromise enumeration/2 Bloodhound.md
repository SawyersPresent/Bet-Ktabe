
# what he did
```
sudo bloodhound-python -d MARVEL.local -u fcastle -p Password1 -ns 192.168.xxx.xxx -c all
```

## what actually worked
```
bloodhound-python -u user -p 'Password' -d domain.local -ns 127.0.0.1 -dc FQDN -c All --dns-tcp
```

```
dnschef --fakeip <DC-IP> --fakedomains domain.local -q -t
```



```
bloodhound-python -u fcastle -p 'Password1' -d MARVEL.local -ns 127.0.0.1 -dc HYDRA-DC.MARVEL.local -c All --dns-tcp
```

```
dnschef --fakeip 192.168.176.129 --fakedomains MARVEL.local -q -t
```


- Domain admins
- Check permissions of what you own
- Kerbroastable user
- encouraged to click through them and check them all