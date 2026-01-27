
```
┌──(root㉿kali)-[/home/kali]
└─# curl -fsSL https://raw.githubusercontent.com/phishingclub/phishingclub/main/install.sh | bash
Getting Phishing Club
Installing from /tmp/phishingclub.lpYlKM

                                            
                                            
   🐟 Phishing Club Interactive Installer   
                                            
                                            

Mode:  Basic Mode   (F1: Basic | F2: Advanced)

HTTP port [80]: 80
HTTPS port [443]: 443
Admin port [0]: 0 (random port)
Admin host []: localhost
Use Auto TLS [true]: true/false
ACME email []:  

    Install    
Configuration saved to /opt/phishingclub/config.json
Step: check sqlite dependency
SQLite version: 3.46.1 2024-08-13 09:16:08 c9c2ab54ba1f5f46360f1b4f35d849cd3f080e6fc2b6c60e91b16c63f69aalt1 (64-bit)
Step: create user and group
Step: create directories
Step: install binary
Step: install systemd service
Step: set permissions
Step: enable service
Step: start service
Step: print info

<<< IMPORTANT >>>
Username: admin
Password: y7wE8U2kUNdxhvU9aNuh7kHPv6xCLR5y
Phishing HTTPS server available:
https://[::]:443
Phishing HTTP server available:
https://[::]:80
Admin server available:
https://[::]:44081

Installer completed successfully! 🐟

# Tips
'journalctl -u phishingclub.service -f' to see logs
'systemctl status phishingclub' to check status of the service


```