
compromising a machine with access to `/etc/shadow` & `/etc/passwd` files.

to escalate if you were able to modify `/etc/passwd`, you should remove the password holder and then be able to login sucessfully. the things we can do are including but not limited to

- deleting the hash/editing the hash to a password we know
- modifying the groups of the user or change the id to 0 
- etc

https://blog.geoda-security.com/2019/02/privilege-escalation-exploiting-write.html



## Read access


Copy out the `/etc/passwd`  and then copy all the contents of the `/etc/shadow` file, there should be a tool called unshadow what it does is that it organizes it to be crackable the syntax is simple to it too. `unshadow <passwdfile> <shadowfile>` and then delete any other user who doesn't have a hash



## Cracking

using hashcat works, usually for linux shadow file

| 1800 | sha512crypt $6$, SHA512 (Unix) 2 | $6$52450745$k5ka2p8bFuSmoVT1tzOyyuaREkkKBcCNqoDKzYiJL9RaE8yMnPgh2XzzF0NDrUhgrcLwg78xs1w5pJiypEdFX/ |
| ---- | -------------------------------- | -------------------------------------------------------------------------------------------------- |


https://hashcat.net/wiki/doku.php?id=example_hashes



----

from tryhackme 

