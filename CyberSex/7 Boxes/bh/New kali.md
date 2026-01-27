

```
sudo apt update && sudo apt upgrade -y && sudo apt dist-upgrade -y && apt --fix-broken install -y && apt --fix-missing install -y && sudo apt autoremove -y && sudo apt clean -y
```


```
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


```
sudo apt install tor -y sudo systemctl start tor sudo systemctl enable tor sudo systemctl status tor use this to install tor
```