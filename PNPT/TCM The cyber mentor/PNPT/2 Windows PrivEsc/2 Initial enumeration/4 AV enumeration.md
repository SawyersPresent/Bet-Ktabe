

Discovering firewalls and AV

```
sc query windefend
```


tells us all the services running

```
sc queryex type= service
```


to find out the firewall's status

```
netsh firewall show state 
netsh advfirewall firewall dump
```

