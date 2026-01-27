


## To generate VPNs you need to create users. then you need to 



```

```

# Saifs pack

```
[Interface]
PrivateKey = 2GNpuU9wEu8j9JhT/a0JaV109lVsW8s0BuqycLxCxW8=
Address = 198.51.100.2/32

[Peer]
PublicKey = zHU5B+YzDejhu6JqjQ2RiZT+Q3nvGo8VwFgLcF4N2Eg=
Endpoint = 192.168.0.11:51820
AllowedIPs = 10.2.0.0/16, 198.51.100.1/32
PersistentKeepalive = 25
```

## User 1

```
non functional
```

## User 2

```
+--------+------------------+-------+------------------------------------------------+
| USERID | PROXMOX USERNAME | ADMIN |                    API KEY                     |
+--------+------------------+-------+------------------------------------------------+
| USER2  | user2            | true  | USER2.hlVpy1ezeHn565%qeK1mCWWplBGXKAsME9=wna7r |
+--------+------------------+-------+------------------------------------------------+

root@ludus:~# export LUDUS_API_KEY="USER2.hlVpy1ezeHn565%qeK1mCWWplBGXKAsME9=wna7r"
root@ludus:~# ludus users wireguard
[Interface]
PrivateKey = QK1exe7GUY43Qm1w9MZeQSaYbKer3bXoGkY6hhzE6nc=
Address = 198.51.100.5/32

[Peer]
PublicKey = zHU5B+YzDejhu6JqjQ2RiZT+Q3nvGo8VwFgLcF4N2Eg=
Endpoint = 192.168.0.11:51820
AllowedIPs = 10.5.0.0/16, 198.51.100.1/32, 10.2.0.0/16
PersistentKeepalive = 25
```

## User3 

```
root@ludus:~# export LUDUS_API_KEY='ROOT.phBQThBY@QFr2SbyRzv6HvMWnrAJ0mEQTRCYhjqF' && ludus user add --name "USER3" --us
erid USER3 --admin --url https://127.0.0.1:8081
[INFO]  Adding user to Ludus, this can take up to a minute. Please wait.
+--------+------------------+-------+------------------------------------------------+
| USERID | PROXMOX USERNAME | ADMIN |                    API KEY                     |
+--------+------------------+-------+------------------------------------------------+
| USER3  | user3            | true  | USER3.CC6iYtGLb=rm8bD4BgYU6J4dd3jsC7Edhj1BqoI@ |
+--------+------------------+-------+------------------------------------------------+
root@ludus:~# export ^C
root@ludus:~# export LUDUS_API_KEY="USER3.CC6iYtGLb=rm8bD4BgYU6J4dd3jsC7Edhj1BqoI@"


root@ludus:~# ludus users wireguard
[Interface]
PrivateKey = wE2/hAigKSfiXLWfDoQkRekXiwVBco8Uk0q8NIok8Ww=
Address = 198.51.100.6/32

[Peer]
PublicKey = zHU5B+YzDejhu6JqjQ2RiZT+Q3nvGo8VwFgLcF4N2Eg=
Endpoint = 192.168.0.11:51820
AllowedIPs = 10.6.0.0/16, 198.51.100.1/32, 10.2.0.0/16
PersistentKeepalive = 25
```

## User 4

```
root@ludus:~# export LUDUS_API_KEY='ROOT.phBQThBY@QFr2SbyRzv6HvMWnrAJ0mEQTRCYhjqF' && ludus user add --name "USER4" --userid USER4 --admin --url https://127.0.0.1:8081
[INFO]  Adding user to Ludus, this can take up to a minute. Please wait.
+--------+------------------+-------+------------------------------------------------+
| USERID | PROXMOX USERNAME | ADMIN |                    API KEY                     |
+--------+------------------+-------+------------------------------------------------+
| USER4  | user4            | true  | USER4.KQ2iMNEX5%Pc2SsQJmGuhaxXm=KlCYmtHCnrH1aP |
+--------+------------------+-------+------------------------------------------------+
root@ludus:~# export LUDUS_API_KEY="USER4.KQ2iMNEX5%Pc2SsQJmGuhaxXm=KlCYmtHCnrH1aP"
root@ludus:~# ludus users wireguard
[Interface]
PrivateKey = qJJx296uRox2D8g5uTiH+U8S32BOjJoIcEewKJ5Pu1g=
Address = 198.51.100.7/32

[Peer]
PublicKey = zHU5B+YzDejhu6JqjQ2RiZT+Q3nvGo8VwFgLcF4N2Eg=
Endpoint = 192.168.0.11:51820
AllowedIPs = 10.7.0.0/16, 198.51.100.1/32, 10.2.0.0/16
PersistentKeepalive = 25
```

## User 5

```
root@ludus:~# export LUDUS_API_KEY='ROOT.phBQThBY@QFr2SbyRzv6HvMWnrAJ0mEQTRCYhjqF' && ludus user add --name "USER5" --userid USER5 --admin --url https://127.0.0.1:8081
[INFO]  Adding user to Ludus, this can take up to a minute. Please wait.
+--------+------------------+-------+------------------------------------------------+
| USERID | PROXMOX USERNAME | ADMIN |                    API KEY                     |
+--------+------------------+-------+------------------------------------------------+
| USER5  | user5            | true  | USER5.WeaS5dTRVY3AS+52_x_JOMMFZ4kELJTu8P4EzlGU |
+--------+------------------+-------+------------------------------------------------+
root@ludus:~# export LUDUS_API_KEY="JD.G0XPn4WXFfI3hDkhxQiT-YlR2ZXXuf77-ZNxKA9f" && ludus range access grant --target JD --source USER5
[INFO]  Range access to sawyer2's range granted to user5. Have user5 pull an updated wireguard config.
root@ludus:~# ludus user wireguard --user USER5
[Interface]
PrivateKey = CCAXlB0YwS1NwvqO0UrVMQ8OHp24BC+ipUv+UbG+xk0=
Address = 198.51.100.8/32

[Peer]
PublicKey = zHU5B+YzDejhu6JqjQ2RiZT+Q3nvGo8VwFgLcF4N2Eg=
Endpoint = 192.168.0.11:51820
AllowedIPs = 10.8.0.0/16, 198.51.100.1/32, 10.2.0.0/16
PersistentKeepalive = 25
```

## User 6

```
root@ludus:~# export LUDUS_API_KEY='ROOT.phBQThBY@QFr2SbyRzv6HvMWnrAJ0mEQTRCYhjqF' && ludus user add --name "USER6" --userid USER6 --admin --url https://127.0.0.1:8081
[INFO]  Adding user to Ludus, this can take up to a minute. Please wait.
+--------+------------------+-------+------------------------------------------------+
| USERID | PROXMOX USERNAME | ADMIN |                    API KEY                     |
+--------+------------------+-------+------------------------------------------------+
| USER6  | user6            | true  | USER6.5ZBDIZjG%AroCm9gYdvVXcUMV=bmlYL%7jIWvKfL |
+--------+------------------+-------+------------------------------------------------+
root@ludus:~# export LUDUS_API_KEY="JD.G0XPn4WXFfI3hDkhxQiT-YlR2ZXXuf77-ZNxKA9f" && ludus range access grant --target JD --source USER6
[INFO]  Range access to sawyer2's range granted to user6. Have user6 pull an updated wireguard config.
root@ludus:~# ludus user wireguard --user USER6
[Interface]
PrivateKey = 2LdsOyLSIwClDmFO2cX3McMZLfvqNaReA1BowdrIIWM=
Address = 198.51.100.9/32

[Peer]
PublicKey = zHU5B+YzDejhu6JqjQ2RiZT+Q3nvGo8VwFgLcF4N2Eg=
Endpoint = 192.168.0.11:51820
AllowedIPs = 10.9.0.0/16, 198.51.100.1/32, 10.2.0.0/16
PersistentKeepalive = 25
```


## USER7

```
[Interface]
PrivateKey = yJRH6xFlM/U+6P/gnM6nSvaI5c4ZoJhvGl7uFqvabUk=
Address = 198.51.100.11/32

[Peer]
PublicKey = zHU5B+YzDejhu6JqjQ2RiZT+Q3nvGo8VwFgLcF4N2Eg=
Endpoint = 192.168.0.11:51820
AllowedIPs = 10.11.0.0/16, 198.51.100.1/32, 10.2.0.0/16
```


## USER 8

```
[Interface]
PrivateKey = 4O2pOleZ4qkm4qe/4yinSBMdGVpx4NVDVzWib87zT0o=
Address = 198.51.100.10/32

[Peer]
PublicKey = zHU5B+YzDejhu6JqjQ2RiZT+Q3nvGo8VwFgLcF4N2Eg=
Endpoint = 192.168.0.11:51820
AllowedIPs = 10.10.0.0/16, 198.51.100.1/32, 10.2.0.0/16
PersistentKeepalive = 25
```


## USER 9

```
[Interface]
PrivateKey = aI0GBdryVWFc16u3MmUqriR3omU3DMz59TOBODXNIl4=
Address = 198.51.100.12/32

[Peer]
PublicKey = zHU5B+YzDejhu6JqjQ2RiZT+Q3nvGo8VwFgLcF4N2Eg=
Endpoint = 192.168.0.11:51820
AllowedIPs = 10.12.0.0/16, 198.51.100.1/32, 10.2.0.0/16
PersistentKeepalive = 25
```


## USER10

```
[Interface]
PrivateKey = AP35Dz1LohlVKaTPx+6l7U1dB+Z8B98vMzpQJa++uVY=
Address = 198.51.100.13/32

[Peer]
PublicKey = zHU5B+YzDejhu6JqjQ2RiZT+Q3nvGo8VwFgLcF4N2Eg=
Endpoint = 192.168.0.11:51820
AllowedIPs = 10.13.0.0/16, 198.51.100.1/32, 10.2.0.0/16
PersistentKeepalive = 25
```

## USER 11

```
[Interface]
PrivateKey = iOmeQW0jROy1F5Fjzg0sftquA4v5PUX6On/imrsgbn8=
Address = 198.51.100.14/32

[Peer]
PublicKey = zHU5B+YzDejhu6JqjQ2RiZT+Q3nvGo8VwFgLcF4N2Eg=
Endpoint = 192.168.1.4:51820
AllowedIPs = 10.14.0.0/16, 198.51.100.1/32, 10.2.0.0/16
PersistentKeepalive = 25
```

## USER 12

```
[Interface]
PrivateKey = mGKnJkLg1rZ8k8tphcDuXlXPry/+aFvlLebkcuPoEkY=
Address = 198.51.100.15/32

[Peer]
PublicKey = zHU5B+YzDejhu6JqjQ2RiZT+Q3nvGo8VwFgLcF4N2Eg=
Endpoint = 192.168.0.11:51820
AllowedIPs = 10.15.0.0/16, 198.51.100.1/32, 10.2.0.0/16
PersistentKeepalive = 25
```

## USER 13

```
[Interface]
PrivateKey = UAfRVlR1JzcMkeG205DeI429GoLbLPxcvDQubGrksF8=
Address = 198.51.100.16/32

[Peer]
PublicKey = zHU5B+YzDejhu6JqjQ2RiZT+Q3nvGo8VwFgLcF4N2Eg=
Endpoint = 192.168.0.11:51820
AllowedIPs = 10.16.0.0/16, 198.51.100.1/32, 10.2.0.0/16
PersistentKeepalive = 25
```













