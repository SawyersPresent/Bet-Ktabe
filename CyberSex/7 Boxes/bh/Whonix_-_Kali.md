[VirtualBox](https://www.virtualbox.org/wiki/Downloads)
[Whonix](https://www.whonix.org/wiki/VirtualBox)
[Kali Linux](https://www.kali.org/get-kali/#kali-platforms)

`TOR only accepts TCP connections if the VPN server has been configured`
	
```bash
watch -n 3 "curl -s ip.me"
```

---
#### VirtualBox - Whonix - Kali
#### Gateway
- Snapshot [.]
- Connect to TOR

Updating the system
```bash
upgrade-nonroot
```

```bash
sudo apt-get-update-plus dist-upgrade
```

Testing to make sure
```bash
systemcheck

anon-verify
```

- Snapshot [..]

---
#### Kali-Whonix
- Snapshot [.]
##### In VirtualBox
- **Settings**
- Change **NAT** to **Internal Network**
##### In Kali (if prebuilt)
- **Advanced Network Configuration**
- Click the **plus** icon
- Choose **Ethernet**
- Go to IPv4 Settings and enter the following details from this table below
	
|Address|Netmask|Gateway|DNS servers|
|---|---|---|---|
|10.152.152.2-254|255.255.192.0|10.152.152.10|10.152.152.10|

Testing to make sure
```bash
curl --silent https://check.torproject.org | grep -m 1 "Congratulations. This browser is configured to use Tor."
```
#### Proxychains
```bash
sudo nano /etc/proxychains4.conf
```

	dynamic chain
	socks5 	127.0.0.1 9050

---
#### After Do
```bash
sudo apt update && sudo apt upgrade -y && sudo apt dist-upgrade -y && apt --fix-broken install -y && apt --fix-missing install -y && sudo apt autoremove -y && sudo apt clean -y
```

Creating a new user
```bash
passwd

sudo passwd root

sudo adduser username

sudo usermod -aG sudo username

sudo chsh -s /bin/bash username
```

Changing SSH keys
```bash
cd /etc/ssh/

sudo mkdir default_kali_keys

sudo mv ssh_host_* default_kali_keys/

sudo dpkg-reconfigure openssh-server

sudo md5sum ssh_host_*

echo "-------------------------------------------"

cd default_kali_keys/ && sudo md5sum ssh_host_*

cd ..

sudo rm -rf default_kali_keys

exit
```

```bash
sudo apt install tor -y

sudo systemctl start tor

sudo systemctl enable tor

sudo systemctl status tor
```

```bash
sudo apt-get install guake -y

sudo cp /usr/share/applications/guake.desktop /etc/xdg/autostart/

sudo reboot now
```

- Snapshot [..]

---
