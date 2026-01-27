

```
# Can ping and scan

nmap -sC -sV 10.5.10.70
nmap -sC -sV -Pn -p- 10.5.10.70



```


veyr odd behaviour

1. you can ping right after you run the nmap, if you wait even 5 more seconds before pinging the host then you get a massive unreachable error
2. this applies also to winrm weirdly, so if you run nmap and then winrm right after you get a shell. but if you wait a little winrm responds saying the host is unreachable


![[Limit testing-20250623123142480.webp]]



![[Limit testing-20250623123741975.webp]]

![[Limit testing-20250623123842339.webp]]



![[Limit testing-20250623123856037.webp]]