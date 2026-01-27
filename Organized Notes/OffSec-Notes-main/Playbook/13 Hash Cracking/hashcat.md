---
tags:
  - tool
  - hash_cracking
---
# hashcat

Crack hashes

Reference: [example_hashes](https://hashcat.net/wiki/doku.php?id=example_hashes), make sure to remove escape characters from the hash if necessary (`\`)

# DISCLAIMER!!!

**remember to remove anything extra before the hash**

## Capabilities

```bash
# Crack hash
hashcat -m 0 $HASH /usr/share/wordlists/rockyou.txt --force
hashcat -m 0 hashes/$HASH wordlists/rockyou.txt --force

# Crack hash with rule file
hashcat -m 0 $HASH /usr/share/wordlists/rockyou.txt -r /usr/share/hashcat/rules/best64.rule --force
hashcat -m 0 $HASH /usr/share/wordlists/rockyou.txt -r /usr/share/hashcat/rules/rockyou-30000.rule --force

# Check cracked hash, add --show to the end of the last command
hashcat -m 0 hash /usr/share/wordlists/rockyou.txt --force --show

# Benchmark
hashcat -b
```

**Notes:**

- Convert a variety of encryption types with `ENC2john` where `ENC` is some type of encryption such as `pfx`, `ssh`, `keepass` and more
- In the case a converted hash is still erroring after troubleshooting, resort to using 

### Custom Rule File

See [Reference](https://hashcat.net/wiki/doku.php?id=rule_based_attack)

Given the following note left on a target

```
Dave's password list:

Window
rickc137
dave
superdave
megadave
umbrella

Note to myself:
New password policy starting in January 2022. Passwords need 3 numbers, a capital letter and a special character
```

We can create a rule file that capitalizes the first letter, adds the numbers `137` and a special character at the end. We will test only for the first 3 special characters on the keyboard (`!`, `@`, `#`) since they are likely more common

```
kali@kali:~/passwordattacks$ cat ssh.rule
c $1 $3 $7 $!
c $1 $3 $7 $@
c $1 $3 $7 $#
```

We can then create a wordlist from the previously used passwords

```
kali@kali:~/passwordattacks$ cat ssh.passwords
Window
rickc137
dave
superdave
megadave
umbrella
```

Lastly we can crack them with hashcat

```bash
hashcat -m 22921 ssh.hash ssh.passwords -r ssh.rule --force
```

Rule file that appends nothing, a "1" or a "!"

```
:
$1
$!
```



## Cracking using hashcat

```
- [ OpenCL Device Types ] -

  # | Device Type
 ===+=============
  1 | CPU
  2 | GPU
  3 | FPGA, DSP, Co-Processor

- [ Workload Profiles ] -

  # | Performance | Runtime | Power Consumption | Desktop Impact
 ===+=============+=========+===================+=================
  1 | Low         |   2 ms  | Low               | Minimal
  2 | Default     |  12 ms  | Economic          | Noticeable
  3 | High        |  96 ms  | High              | Unresponsive
  4 | Nightmare   | 480 ms  | Insane            | Headless
```


my preferred payload

```
PS E:\hash\hashcat-6.2.6> .\hashcat.exe -m 1800 shadow.txt rockyou.txt -O -D 2
```


```
PS E:\hash\hashcat-6.2.6> .\hashcat.exe -m 1800 shadow.txt rockyou.txt -O -D 2
hashcat (v6.2.6) starting

hiprtcCompileProgram is missing from HIPRTC shared library.

OpenCL API (OpenCL 2.1 AMD-APP (3608.0)) - Platform #1 [Advanced Micro Devices, Inc.]
=====================================================================================
* Device #1: AMD Radeon RX 6600, 8064/8176 MB (6732 MB allocatable), 14MCU

Minimum password length supported by kernel: 0
Maximum password length supported by kernel: 15

Hashes: 1 digests; 1 unique digests, 1 unique salts
Bitmaps: 16 bits, 65536 entries, 0x0000ffff mask, 262144 bytes, 5/13 rotates
Rules: 1

Optimizers applied:
* Optimized-Kernel
* Zero-Byte
* Single-Hash
* Single-Salt
* Uses-64-Bit

Watchdog: Temperature abort trigger set to 90c

Host memory required for this attack: 281 MB

Dictionary cache built:
* Filename..: rockyou.txt
* Passwords.: 14344391
* Bytes.....: 139921497
* Keyspace..: 14344384
* Runtime...: 2 secs

$6$Tb/euwmK$OXA.dwMeOAcopwBl68boTG5zi65wIHsc84OWAIye5VITLLtVlaXvRDJXET..it8r.jbrlpfZeMdwD3B0fGxJI0:password123 <-------- crakced!

Session..........: hashcat
Status...........: Cracked
Hash.Mode........: 1800 (sha512crypt $6$, SHA512 (Unix))
Hash.Target......: $6$Tb/euwmK$OXA.dwMeOAcopwBl68boTG5zi65wIHsc84OWAIy...fGxJI0
Time.Started.....: Thu Feb 29 22:09:08 2024 (0 secs)
Time.Estimated...: Thu Feb 29 22:09:08 2024 (0 secs)
Kernel.Feature...: Optimized Kernel
Guess.Base.......: File (rockyou.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:   105.1 kH/s (7.12ms) @ Accel:128 Loops:256 Thr:128 Vec:1
Recovered........: 1/1 (100.00%) Digests (total), 1/1 (100.00%) Digests (new)
Progress.........: 16390/14344384 (0.11%)
Rejected.........: 6/16390 (0.04%)
Restore.Point....: 0/14344384 (0.00%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:4864-5000
Candidate.Engine.: Device Generator
Candidates.#1....: 123456 -> c00kie
Hardware.Mon.#1..: Temp: 41c Fan:  0% Util: 31% Core:1230MHz Mem:1740MHz Bus:8

Started: Thu Feb 29 22:08:44 2024
Stopped: Thu Feb 29 22:09:10 2024
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
IN 40 SECONDS!!! :DDD, i guess no more tea breaks now LOL
```



for SSH keysand nything o fthe sort literally just ssh2john and then crack it