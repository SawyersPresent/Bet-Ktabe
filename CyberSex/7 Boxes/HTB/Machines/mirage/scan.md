

```
kali@kali ~> nmap -sC -sV 10.129.242.58                                                                                                                                                            15:23:32 [25/25]
Starting Nmap 7.95 ( https://nmap.org ) at 2025-07-19 19:21 UTC
Nmap scan report for 10.129.242.58       
Host is up (0.065s latency).             
Not shown: 986 closed tcp ports (reset)  
PORT     STATE SERVICE       VERSION     
53/tcp   open  domain        Simple DNS Plus      
88/tcp   open  kerberos-sec  Microsoft Windows Kerberos (server time: 2025-07-20 02:22:00Z)
111/tcp  open  rpcbind       2-4 (RPC #100000)                                                                                                                                                                     
| rpcinfo:           
|   program version    port/proto  service                                                               
|   100000  2,3,4        111/tcp   rpcbind
|   100000  2,3,4        111/tcp6  rpcbind
|   100000  2,3,4        111/udp   rpcbind        
|   100000  2,3,4        111/udp6  rpcbind
|   100003  2,3         2049/udp   nfs
|   100003  2,3         2049/udp6  nfs                                                                   
|   100003  2,3,4       2049/tcp   nfs                                                                                                                                                                             
|   100003  2,3,4       2049/tcp6  nfs            
|   100005  1,2,3       2049/tcp   mountd
|   100005  1,2,3       2049/tcp6  mountd                                                                
|   100005  1,2,3       2049/udp   mountd
|   100005  1,2,3       2049/udp6  mountd
|   100021  1,2,3,4     2049/tcp   nlockmgr   
|   100021  1,2,3,4     2049/tcp6  nlockmgr                                                                                                                                                                        
|   100021  1,2,3,4     2049/udp   nlockmgr
|   100021  1,2,3,4     2049/udp6  nlockmgr                                                              
|   100024  1           2049/tcp   status
|   100024  1           2049/tcp6  status
|   100024  1           2049/udp   status         
|_  100024  1           2049/udp6  status                                                                                                                                                                          
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: mirage.htb0., Site: Default-First-Site-Name)
| ssl-cert: Subject:                   
| Subject Alternative Name: DNS:dc01.mirage.htb, DNS:mirage.htb, DNS:MIRAGE
| Not valid before: 2025-07-04T19:58:41                                                                  
|_Not valid after:  2105-07-04T19:58:41    
|_ssl-date: TLS randomness does not represent time
445/tcp  open  microsoft-ds?                                                                             
464/tcp  open  kpasswd5?|_ssl-date: TLS randomness does not represent time
3269/tcp open  ssl/ldap      Microsoft Windows Active Directory LDAP (Domain: mirage.htb0., Site: Default-First-Site-Name)
|_ssl-date: TLS randomness does not represent time
| ssl-cert: Subject: 
| Subject Alternative Name: DNS:dc01.mirage.htb, DNS:mirage.htb, DNS:MIRAGE
| Not valid before: 2025-07-04T19:58:41
|_Not valid after:  2105-07-04T19:58:41
5985/tcp open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
Service Info: Host: DC01; OS: Windows; CPE: cpe:/o:microsoft:windows
593/tcp  open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp  open  ssl/ldap      Microsoft Windows Active Directory LDAP (Domain: mirage.htb0., Site: Default-First-Site-Name)
|_ssl-date: TLS randomness does not represent time
| ssl-cert: Subject:         
| Subject Alternative Name: DNS:dc01.mirage.htb, DNS:mirage.htb, DNS:MIRAGE
| Not valid before: 2025-07-04T19:58:41
|_Not valid after:  2105-07-04T19:58:41
2049/tcp open  nlockmgr      1-4 (RPC #100021)
3268/tcp open  ldap          Microsoft Windows Active Directory LDAP (Domain: mirage.htb0., Site: Default-First-Site-Name)
| ssl-cert: Subject:                                                                                     
| Subject Alternative Name: DNS:dc01.mirage.htb, DNS:mirage.htb, DNS:MIRAGE
| Not valid before: 2025-07-04T19:58:41

```



```
kali@kali ~/h/mirage> showmount -e 10.129.242.58
Export list for 10.129.242.58:
/MirageReports (everyone)
```



```

```



the pdfs say that they blindly trust `nats-svc.mirage.htb`


```

```



```
kali@kali ~> dig ns mirage.htb @10.129.242.58

; <<>> DiG 9.20.9-1-Debian <<>> ns mirage.htb @10.129.242.58
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 52474
;; flags: qr aa rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 4

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 4000
;; QUESTION SECTION:
;mirage.htb.                    IN      NS

;; ANSWER SECTION:
mirage.htb.             3600    IN      NS      dc01.mirage.htb.

;; ADDITIONAL SECTION:
dc01.mirage.htb.        3600    IN      A       10.129.242.58
dc01.mirage.htb.        3600    IN      AAAA    dead:beef::1eb
dc01.mirage.htb.        3600    IN      AAAA    dead:beef::5a7f:dd79:e025:d946

;; Query time: 67 msec
;; SERVER: 10.129.242.58#53(10.129.242.58) (UDP)
;; WHEN: Sat Jul 19 20:36:00 UTC 2025
;; MSG SIZE  rcvd: 130


```




```
kali@kali ~> dig any mirage.htb @10.129.242.58

; <<>> DiG 9.20.9-1-Debian <<>> any mirage.htb @10.129.242.58
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 32007
;; flags: qr aa rd ra; QUERY: 1, ANSWER: 5, AUTHORITY: 0, ADDITIONAL: 4

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 4000
;; QUESTION SECTION:
;mirage.htb.                    IN      ANY

;; ANSWER SECTION:
mirage.htb.             600     IN      A       10.129.242.58
mirage.htb.             3600    IN      NS      dc01.mirage.htb.
mirage.htb.             3600    IN      SOA     dc01.mirage.htb. hostmaster.mirage.htb. 156 900 600 86400 3600
mirage.htb.             600     IN      AAAA    dead:beef::5a7f:dd79:e025:d946
mirage.htb.             600     IN      AAAA    dead:beef::1eb

;; ADDITIONAL SECTION:
dc01.mirage.htb.        3600    IN      A       10.129.242.58
dc01.mirage.htb.        3600    IN      AAAA    dead:beef::5a7f:dd79:e025:d946
dc01.mirage.htb.        3600    IN      AAAA    dead:beef::1eb

;; Query time: 60 msec
;; SERVER: 10.129.242.58#53(10.129.242.58) (TCP)
;; WHEN: Sat Jul 19 20:36:15 UTC 2025
;; MSG SIZE  rcvd: 249

```

