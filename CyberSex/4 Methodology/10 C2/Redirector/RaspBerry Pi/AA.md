


```python
noor@SawyersPi:~/Redirector $ nano PiRedirector.sh
noor@SawyersPi:~/Redirector $ sudo bash PiRedirector.sh 192.168.0.196
[*] Setting up IP-based redirector to 192.168.0.196
Hit:1 http://archive.raspberrypi.com/debian bookworm InRelease
Hit:2 http://deb.debian.org/debian bookworm InRelease
Hit:3 http://deb.debian.org/debian-security bookworm-security InRelease
Hit:4 http://deb.debian.org/debian bookworm-updates InRelease
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
199 packages can be upgraded. Run 'apt list --upgradable' to see them.
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
apache2 is already the newest version (2.4.62-1~deb12u2).
0 upgraded, 0 newly installed, 0 to remove and 199 not upgraded.
Module proxy already enabled
Considering dependency proxy for proxy_http:
Module proxy already enabled
Module proxy_http already enabled
Module headers already enabled
Module rewrite already enabled
<html><body><h1>Redirector Online</h1></body></html>
[*] Restarting Apache...
[+] HTTP redirector is live. Access the Raspberry Pi IP on port 80 to reach the C2 backend at 192.168.0.196.
```


