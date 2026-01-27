


```python


  
// =================================================== Enumeration =================================================== //

// Find any of the scripts related to S7
find /usre/share/nmap -name "s7*.nse"
find / -name "s7*.nse" 2>/dev/null
https://github.com/cckuailong/ICS-Protocal-Detect-Nmap-Script.git

// Enumeration
nmap -sV 192.168.3.134 -p 102 --script s7-info,s7-enumerate -Pn




// metasploit module
admin/sacada/multi_cip_command




// ------------------------------------- ICS Scripts ------------------------------------- //

https://github.com/tijldeneut/ICSSecurityScripts.git


```






