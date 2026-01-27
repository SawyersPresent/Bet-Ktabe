


```python


// ------------------------------------- OPSEC ------------------------------------- //

Non-Intrusive:
- L: list more information
- F: Flash the LED

Balanced:
- P : Print the outputs
- N : Change the device name

Aggressive:
- A : Alter the outputs
- C : Change the CPU state
- 1 : Configure the Network

  
// =================================================== Enumeration =================================================== //

// Find any of the scripts related to S7
find /usre/share/nmap -name "s7*.nse"
find / -name "s7*.nse" 2>/dev/null
https://github.com/cckuailong/ICS-Protocal-Detect-Nmap-Script.git

// Enumeration
nmap -sV 192.168.3.134 -p 102 --script s7-info,s7-enumerate -Pn




// metasploit
auxiliary/scanner/scada/profinet_siemens



// ------------------------------------- ICS Scripts ------------------------------------- //

https://github.com/tijldeneut/ICSSecurityScripts.git


```






















