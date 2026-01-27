

Kerberos Authentication
To authenticate with certain kerberos environments, the FQDN needs to be specified and the /etc/krb5.conf file needs to be modified to the following.

```
[libdefaults]
    default_realm = VINTAGE.HTB

# The following krb5.conf variables are only for MIT Kerberos.
    kdc_timesync = 1
    ccache_type = 4
    forwardable = true
    proxiable = true
    rdns = false

# The following libdefaults parameters are only for Heimdal Kerberos.
    fcc-mit-ticketflags = true

[realms]
    VINTAGE.HTB = {
        kdc = dc01.vintage.htb
        admin_server = dc01.vintage.htb
    }

[domain_realm]
    .vintage.htb = VINTAGE.HTB
    vintage.htb = VINTAGE.HTB

```
All vintage.htb or dc01.vintage.htb values need to be modified accordingly.

# Connect via kerberos after modifying /etc/krb5.conf
evil-winrm -i dc01.vintage.htb -r vintage.htb


