

```powershell
PS C:\Users\USER> ssh-add C:\Users\USER\.ssh\id_rsa
Identity added: C:\Users\USER\.ssh\id_rsa (root@bsidesamman)

PS C:\Users\USER> ssh root@68.183.65.249
Linux bsidesamman 6.8.12-10-pve #1 SMP PREEMPT_DYNAMIC PMX 6.8.12-10 (2025-04-18T07:39Z) x86_64

This is a Ludus host.

Ludus is a project to enable teams to quickly and
safely deploy test environments (ranges) to test tools and
techniques against representative virtual machines.

Ludus leverages Proxmox which is licensed under APGLv3.

Docs:   https://68.183.65.249:8080/ludus
Web UI: https://68.183.65.249:8006

Ludus Version: 1.9.6+118a007

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Thu May 15 17:25:54 2025 from 132.147.119.52

```




```
root@bsidesamman:~# ludus user add --name "Randal" --userid Randal --admin --url https://127.0.0.1:8081
[INFO]  Adding user to Ludus, this can take up to a minute. Please wait.
+--------+------------------+-------+-------------------------------------------------+
| USERID | PROXMOX USERNAME | ADMIN |                     API KEY                     |
+--------+------------------+-------+-------------------------------------------------+
| Randal | randal           | true  | Randal.a08ACH_86=V80JO=lr=TWebQG73sEM5HZnAALM5+ |
+--------+------------------+-------+-------------------------------------------------+
```



```
export LUDUS_API_KEY='Randal.a08ACH_86=V80JO=lr=TWebQG73sEM5HZnAALM5+'
```