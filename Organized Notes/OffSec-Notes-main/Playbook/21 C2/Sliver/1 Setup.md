


```
kali@kali ~> sudo systemctl status sliver.service
● sliver.service - Sliver
     Loaded: loaded (/etc/systemd/system/sliver.service; disabled; preset: disabled)
     Active: active (running) since Thu 2024-07-04 08:56:18 EDT; 2min 46s ago
   Main PID: 17740 (sliver-server)
      Tasks: 8 (limit: 2262)
     Memory: 14.8M (peak: 15.3M)
        CPU: 82ms
     CGroup: /system.slice/sliver.service
             └─17740 /root/sliver-server daemon

Jul 04 08:56:18 kali systemd[1]: Started sliver.service - Sliver.

```