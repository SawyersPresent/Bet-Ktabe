
```
PS D:\Exegol> exegol start
[*] Exegol is currently in version v4.3.10
[*] Exegol Discord serv.: https://discord.gg/cXThyp7D6P
[*] Exegol documentation: https://exegol.rtfd.io/
[*] Starting exegol
[!] No containers have been created yet

🛸 Available images
┌───────────┬─────────┬──────────────────────┐
│ Image tag │ Size    │ Status               │
├───────────┼─────────┼──────────────────────┤
│ full      │ 19.9GB  │ Up to date (v.3.1.6) │
│ nightly   │ ~51.8GB │ Not installed        │
│ web       │ ~24.7GB │ Not installed        │
│ ad        │ ~40.0GB │ Not installed        │
│ light     │ ~17.4GB │ Not installed        │
│ osint     │ ~12.2GB │ Not installed        │
└───────────┴─────────┴──────────────────────┘

[*] You can use a name that does not already exist to build a new image from local sources
[?] Select an image by its name (full): full
[!] Host network mode for Docker desktop (Windows & macOS) is not available.
[*] To share network ports between the host and exegol, use the --port parameter.
[?] Enter the name of your new exegol container (default): default

⭐ Container summary
┌──────────────────┬───────────────────────────────────────┐
│             Name │ default                               │
│            Image │ full - v.3.1.6 (Up to date)           │
├──────────────────┼───────────────────────────────────────┤
│      Credentials │ root : yqaiE8PyX3SyTxDYWfbmtdDBHpBL5V │
│   Remote Desktop │ Off 🪓                                │
│      Console GUI │ On ✔ (X11)                            │
│          Network │ bridge                                │
│         Timezone │ On ✔                                  │
│ Exegol resources │ On ✔ (/opt/resources)                 │
│     My resources │ On ✔ (/opt/my-resources)              │
│    Shell logging │ Off 🪓                                │
│       Privileged │ Off ✔                                 │
│        Workspace │ Dedicated (/workspace)                │
└──────────────────┴───────────────────────────────────────┘

[?] Is the container configuration correct? [Y/n]: Y
[*] Command line of the configuration: exegol start default full
[*] To use exegol without interaction, read CLI options with exegol start -h
[*] Creating new exegol container
[+] Exegol container successfully created !
```





----

issues

when running bloodhound and neo4j make sure that the neo4j is as follows

```
neo4j start
```

https://github.com/ThePorgs/Exegol-images/issues/370


