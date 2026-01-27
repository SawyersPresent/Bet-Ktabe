
```
PS C:\Users\USER\pipx\venvs\exegol> exegol start HTB -d /dev/net/tun --cap 'NET_ADMIN' --cap 'SYS_ADMIN'  -V 'D:\ExStuff\ExWorkspace:/opt/shared'
[*] Exegol Community is currently in version v5.1.7
[*] More about Exegol at: https://exegol.com
[*] Skipping interactive mode (arguments supplied)
[*] Creating new container HTB

🛸 Available images
┌─────────┬──────────┬───────────────────────┐
│ Image   │ Size     │ Status                │
├─────────┼──────────┼───────────────────────┤
│ free    │ 16.9 GB  │ Up to date (v.3.1.8)  │
│ full    │ 43.73 GB │ Pro / Enterprise only │
│ web     │ 19.06 GB │ Pro / Enterprise only │
│ light   │ 14.84 GB │ Pro / Enterprise only │
│ osint   │ 11.43 GB │ Pro / Enterprise only │
│ ad      │ 28.74 GB │ Pro / Enterprise only │
│ nightly │ 43.85 GB │ Pro / Enterprise only │
└─────────┴──────────┴───────────────────────┘

[?] Select an image by its name (free):
[!] Host network mode for Docker Desktop is not available, you need to upgrade Docker Desktop to enable it!
[*] To share network ports (without host network) between the host and exegol, use the --port parameter.

⭐ Container summary
┌──────────────────┬───────────────────────────────────────┐
│             Name │ htb                                   │
│            Image │ free - v.3.1.8 (Up to date)           │
├──────────────────┼───────────────────────────────────────┤
│      Credentials │ root : kNBmYPd2KSi8cArZ7CTb7ckg8V9UcG │
│   Remote Desktop │ Off 🪓                                │
│      Console GUI │ On ✔ (X11)                            │
│          Network │ Docker                                │
│         Timezone │ On ✔                                  │
│ Exegol resources │ On ✔ (/opt/resources)                 │
│     My resources │ On ✔ (/opt/my-resources)              │
│    Shell logging │ Off 🪓                                │
│       Privileged │ Off ✔                                 │
│     Capabilities │ NET_ADMIN, SYS_ADMIN                  │
│        Workspace │ Dedicated (/workspace)                │
│          Devices │ /dev/net/tun                          │
│          Volumes │ D:/ExStuff/ExWorkspace ➡ /opt/shared  │
└──────────────────┴───────────────────────────────────────┘

[*] Creating new exegol container
[+] Exegol container successfully created!
```