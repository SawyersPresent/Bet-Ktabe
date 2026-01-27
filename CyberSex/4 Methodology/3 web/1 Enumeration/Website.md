

``` Python
// Vhost
ffuf -H "Host: FUZZ.domain.com" -w "/usr/share/seclists/Discovery/DNS/subdomains-top1million-110000.txt" -u http://domain.com/ -fs 154

// Directory busting
ffuf -w "/usr/share/seclists/Discovery/Web-Content/raft-small-directories.txt" -u https://domain.com/

//Subdomain bruteforcing
dnsenum --enum inlanefreight.com -f /usr/share/seclists/Discovery/DNS/subdomains-top1million-20000.txt -r

// DNS Zone transfer
dig axfr @nsztm1.digi.ninja zonetransfer.me


```
