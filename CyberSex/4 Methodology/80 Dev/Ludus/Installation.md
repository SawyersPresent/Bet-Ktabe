

# debian host creds

```python
user:root
root:root
```


```python
root@ludus:~ ludus-install-status
Ludus install completed successfully
Root API key: ROOT.phBQThBY@QFr2SbyRzv6HvMWnrAJ0mEQTRCYhjqF
```


### API KEYS:

create these API keys, each key is ment to be for a specific user, you wont actually use said keys to log in but rather you'll use them to split up different labs so you wont have to delete fucking everything all the fucking time.

```python

root@ludus:~ LUDUS_API_KEY='ROOT.phBQThBY@QFr2SbyRzv6HvMWnrAJ0mEQTRCYhjqF'  ludus user add --name "sawyer2" --userid JD
 --admin --url https://127.0.0.1:8081
[INFO]  Adding user to Ludus, this can take up to a minute. Please wait.
+--------+------------------+-------+---------------------------------------------+
| USERID | PROXMOX USERNAME | ADMIN |                   API KEY                   |
+--------+------------------+-------+---------------------------------------------+
| JD     | sawyer2          | true  | JD.G0XPn4WXFfI3hDkhxQiT-YlR2ZXXuf77-ZNxKA9f |
+--------+------------------+-------+---------------------------------------------+

root@ludus:~ export LUDUS_API_KEY='JD.G0XPn4WXFfI3hDkhxQiT-YlR2ZXXuf77-ZNxKA9f'
root@ludus:~ ludus user creds get
+------------------+----------------------+
| PROXMOX USERNAME |   PROXMOX PASSWORD   |
+------------------+----------------------+
| sawyer2          | Elp4JyfjRNMtIvSWNMip |
+------------------+----------------------+

```



```
[INFO]  Adding user to Ludus, this can take up to a minute. Please wait.
+--------+------------------+-------+-------------------------------------------------+
| USERID | PROXMOX USERNAME | ADMIN |                     API KEY                     |
+--------+------------------+-------+-------------------------------------------------+
| SAWYER | sawyer3          | true  | SAWYER.q%nvEr=do%uxYMbcd2tU+X6rQ_i3XBL=LU3R426n |
+--------+------------------+-------+-------------------------------------------------+
root@ludus:~/JOSA/JOSA-WinPriv-2025# export LUDUS_API_KEY='SAWYER.q%nvEr=do%uxYMbcd2tU+X6rQ_i3XBL=LU3R426n'
```


```python
root@ludus:/home/user# ludus-install-status
Ludus install completed successfully
Root API key: ROOT.=OaPNMBnyjpZO2-bMMC@By=8%IOR623ugX4a6Jvd
root@ludus:/home/user# cd
root@ludus:~ LUDUS_API_KEY='ROOT.=OaPNMBnyjpZO2-bMMC@By=8%IOR623ugX4a6Jvd' \
 ludus user add --name "Cert Users" --userid CD --admin --url https://127.0.0.1:8081
[INFO]  Adding user to Ludus, this can take up to a minute. Please wait.
+--------+------------------+-------+---------------------------------------------+
| USERID | PROXMOX USERNAME | ADMIN |                   API KEY                   |
+--------+------------------+-------+---------------------------------------------+
| CD     | cert-users       | true  | CD.nH4s5=0XJf0FvrcgIV1N+di0gaqfZvb0pqxio4NU |
+--------+------------------+-------+---------------------------------------------+
```


## Getting access inside using Wireguard

Wiregaurd can be used to access the inside of the lab. Creating configs is pretty easy

```python
root@ludus:/home/user> ludus user wireguard --user JD --url https://127.0.0.1:8081
[Interface]
PrivateKey = gB9JUFY4Uy1j3KDQ9kUlB4nFkkjyA8AoJSa6xQt7Q0U=
Address = 198.51.100.2/32

[Peer]
PublicKey = tJzY8ufNbKfpK3vrIE8I662u9KWTp6xxYM2MlK6duAk=
Endpoint = 192.168.3.139:51820
AllowedIPs = 10.2.0.0/16, 198.51.100.1/32
PersistentKeepalive = 25
```


## Environments

#### ADCS + Elastic

- issues
	- sometimes there happens to be a timeout issues, adding up the async_timeout should do the trick, i upped mine to `5900`
	- also i had kept checking on the vms and clicking on the console to make sure that theyre are actually rebooting and are able to log in


config file;

```python
ludus:

  - vm_name: "{{ range_id }}-elastic"
    hostname: "{{ range_id }}-elastic"
    template: debian-12-x64-server-template
    vlan: 20
    ip_last_octet: 1
    ram_gb: 8
    cpus: 4
    linux: true
    testing:
      snapshot: false
      block_internet: false
    roles:
      - badsectorlabs.ludus_elastic_container
    role_vars:
      ludus_elastic_password: "thisisapassword"

  - vm_name: "{{ range_id }}-win11-22h2-enterprise-x64-1"
    hostname: "{{ range_id }}-WIN11-22H2-1"
    template: win11-22h2-x64-enterprise-template
    vlan: 20
    ip_last_octet: 21
    ram_gb: 8
    cpus: 4
    windows:
      install_additional_tools: false
    roles:
      - badsectorlabs.ludus_elastic_agent

  - vm_name: "{{ range_id }}-ad-dc-win2022-server-x64-1"
    hostname: "{{ range_id }}-DC01-2022"
    template: win2022-server-x64-template
    vlan: 20
    ip_last_octet: 20
    ram_gb: 6
    cpus: 4
    windows:
      sysprep: true
    domain:
      fqdn: ludus.domain
      role: primary-dc
    roles:
      - badsectorlabs.ludus_adcs
      - badsectorlabs.ludus_elastic_agent
```