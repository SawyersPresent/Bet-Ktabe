
```
kali@kali 2026-01-23 17:57:54 ~/tools> ./fscan -h 10.10.110.0/24 -nobr

   ___                              _    
  / _ \     ___  ___ _ __ __ _  ___| | __ 
 / /_\/____/ __|/ __| '__/ _` |/ __| |/ /
/ /_\\_____\__ \ (__| | | (_| | (__|   <    
\____/     |___/\___|_|  \__,_|\___|_|\_\   
                     fscan version: 1.8.4
start infoscan
trying RunIcmp2
The current user permissions unable to send icmp packets
start ping
(icmp) Target 10.10.110.2     is alive
(icmp) Target 10.10.110.123   is alive
(icmp) Target 10.10.110.124   is alive
[*] Icmp alive hosts len is: 3
10.10.110.123:80 open
10.10.110.124:80 open
10.10.110.123:22 open
10.10.110.123:8000 open
10.10.110.123:8089 open
[*] alive ports len is: 5
start vulscan
[*] WebTitle http://10.10.110.123      code:200 len:22567  title:ACME Bank
[*] WebTitle http://10.10.110.123:8000 code:303 len:339    title:303 See Other 跳转url: http://10.10.110.123:8000/zh-CN/
[*] WebTitle https://10.10.110.123:8089 code:401 len:453    title:None
[*] WebTitle http://10.10.110.123:8000/zh-CN/account/login?return_to=%2Fzh-CN%2F code:200 len:13486  title:""
[*] WebTitle http://10.10.110.124      code:200 len:3079   title:Offshore Dev
已完成 5/5
[*] 扫描结束,耗时: 33.36101986s

```








