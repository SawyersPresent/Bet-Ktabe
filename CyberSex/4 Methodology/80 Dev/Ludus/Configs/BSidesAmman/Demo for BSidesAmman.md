


```python

PLAY [Apply inbound WireGuard to the router (Enterprise)] **********************

TASK [Gathering Facts] *********************************************************
ok: [JD-router-debian11-x64]

TASK [Check for enterprise license] ********************************************
skipping: [JD-router-debian11-x64]

TASK [Clear any inbound WireGuard related configurations] **********************
skipping: [JD-router-debian11-x64]

TASK [Setup inbound WireGuard on the router] ***********************************
skipping: [JD-router-debian11-x64]

PLAY [Deploy DC VMs] ***********************************************************

TASK [Gathering Facts] *********************************************************
ok: [localhost]

TASK [Deploy VM] ***************************************************************
skipping: [localhost] => (item={'vm_name': 'DEMO-albalad-dev-JD', 'hostname': 'dev03', 'template': 'win2022-server-x64-template', 'vlan': 10, 'ip_last_octet': 12, 'ram_gb': 6, 'cpus': 4, 'windows': {'sysprep': True}, 'domain': {'fqdn': 'albalad.bsides.rv', 'role': 'member'}})
included: /opt/ludus/ansible/range-management/tasks/proxmox/deploy-vm.yml for localhost => (item={'vm_name': 'DEMO-albalad-DC-JD', 'hostname': 'dc01', 'template': 'win2022-server-x64-template', 'vlan': 10, 'ip_last_octet': 11, 'ram_gb': 8, 'cpus': 6, 'windows': {'sysprep': True}, 'domain': {'fqdn': 'albalad.bsides.rv', 'role': 'primary-dc'}})

TASK [Create a VM from a template] *********************************************
changed: [localhost]

TASK [Pause for 5 seconds to allow the vmid to populate] ***********************
Pausing for 5 seconds
ok: [localhost]

TASK [Set the vm_id] ***********************************************************
ok: [localhost]
```


```python
TASK [Start the VM] ************************************************************
FAILED - RETRYING: [localhost]: Start the VM (3 retries left).
FAILED - RETRYING: [localhost]: Start the VM (2 retries left).
FAILED - RETRYING: [localhost]: Start the VM (1 retries left).
fatal: [localhost]: FAILED! => {"attempts": 3, "changed": false, "msg": "Reached timeout while waiting for starting VM. Last line in task before timeout: [{'t': 'TASK ERROR: MAX 4 vcpus allowed per VM on this node', 'n': 1}]"}

PLAY RECAP *********************************************************************
JD-router-debian11-x64     : ok=61   changed=44   unreachable=0    failed=0    skipped=55   rescued=0    ignored=0
localhost                  : ok=46   changed=20   unreachable=0    failed=1    skipped=7    rescued=0    ignored=0
```




after changing it so that both have 4 cpu cores it became abit easier but now theres another error 

```python
TASK [Wait for WinRM] **********************************************************
ok: [DEMO-albalad-dev-JD -> localhost]
ok: [DEMO-albalad-DC-JD -> localhost]

TASK [Create sysprepd file] ****************************************************
fatal: [DEMO-albalad-dev-JD]: UNREACHABLE! => {"changed": false, "msg": "ssl: The device is not ready.  (extended fault data: {'transport_message': 'Bad HTTP response returned from server. Code 500', 'http_status_code': 500, 'wsmanfault_code': 2147942421, 'fault_code': 's:Receiver', 'fault_subcode': 'w:InternalError'})", "unreachable": true}
fatal: [DEMO-albalad-DC-JD]: UNREACHABLE! => {"changed": false, "msg": "ssl: The device is not ready.  (extended fault data: {'transport_message': 'Bad HTTP response returned from server. Code 500', 'http_status_code': 500, 'wsmanfault_code': 2147942421, 'fault_code': 's:Receiver', 'fault_subcode': 'w:InternalError'})", "unreachable": true}

PLAY RECAP *********************************************************************
DEMO-albalad-DC-JD         : ok=28   changed=11   unreachable=1    failed=0    skipped=47   rescued=0    ignored=0
DEMO-albalad-dev-JD        : ok=26   changed=11   unreachable=1    failed=0    skipped=47   rescued=0    ignored=0
JD-router-debian11-x64     : ok=69   changed=44   unreachable=0    failed=0    skipped=57   rescued=0    ignored=0
localhost                  : ok=70   changed=26   unreachable=0    failed=0    skipped=11   rescued=0    ignored=0

^C
root@ludus:/mnt/hgfs/sharedfolderfortheludus/RangeVillage-Demo-main/BSidesAmman-2025# ludus range status
+---------+---------------+------------------+---------------+-------------------+-----------------+
| USER ID | RANGE NETWORK | LAST DEPLOYMENT  | NUMBER OF VMS | DEPLOYMENT STATUS | TESTING ENABLED |
+---------+---------------+------------------+---------------+-------------------+-----------------+
|   JD    |  10.2.0.0/16  | 2025-04-29 17:42 |       3       |       ERROR       |      FALSE      |
+---------+---------------+------------------+---------------+-------------------+-----------------+
+------------+------------------------+-------+-------------+
| PROXMOX ID |        VM NAME         | POWER |     IP      |
+------------+------------------------+-------+-------------+
|    105     | JD-router-debian11-x64 |  On   | 10.2.10.254 |
|    106     | DEMO-albalad-DC-JD     |  On   | 10.2.10.11  |
|    107     | DEMO-albalad-dev-JD    |  On   | 10.2.10.12  |
+------------+------------------------+-------+-------------+
```


10.2.1



then after the range deploys successfully, go inside of the repo and inside of the ansible folder

```python
root@ludus:~/RangeVillage-Demo-main/BSidesAmman-2025/ansible: ansible-playbook main.yml -i inventory.ini

PLAY [populate AD data] *****************************************************************************************************************************************************************************************

TASK [create users] *********************************************************************************************************************************************************************************************
included: /root/RangeVillage-Demo-main/BSidesAmman-2025/ansible/tasks/users.yml for dc01.albalad.bsides.rv

TASK [Create fake users] ****************************************************************************************************************************************************************************************
changed: [dc01.albalad.bsides.rv]

TASK [Debug user creation output] *******************************************************************************************************************************************************************************
ok: [dc01.albalad.bsides.rv] => {
    "user_creation_output": {
        "changed": true,
        "debug": [],
        "error": [],
        "failed": false,
        "host_err": "",
```




---



```
root@ludus:/mnt/hgfs/sharedfolderfortheludus/RangeVillage-Demo-main/BSidesAmman-2025# ls
ansible  demo.yml  solution
root@ludus:/mnt/hgfs/sharedfolderfortheludus/RangeVillage-Demo-main/BSidesAmman-2025# vim demo.yml
root@ludus:/mnt/hgfs/sharedfolderfortheludus/RangeVillage-Demo-main/BSidesAmman-2025# ludus range deploy
[INFO]  Range deploy started
root@ludus:/mnt/hgfs/sharedfolderfortheludus/RangeVillage-Demo-main/BSidesAmman-2025# ludus range logs -f
[WARNING]: provided hosts list is empty, only localhost is available. Note that
the implicit localhost does not match 'all'

PLAY [Pre run checks] **********************************************************

TASK [Acquire session ticket] **************************************************
ok: [localhost]

TASK [Extract ticket from response] ********************************************
ok: [localhost]

TASK [Check for valid dynamic inventory] ***************************************
ok: [localhost] => {
    "changed": false,
    "msg": "Dynamic inventory loaded!"
}

PLAY [Deploy the router VM] ****************************************************

TASK [Gathering Facts] *********************************************************
ok: [localhost]

TASK [Deploy router VM] ********************************************************
included: /opt/ludus/ansible/range-management/tasks/proxmox/deploy-vm.yml for localhost

TASK [Create a VM from a template] *********************************************
changed: [localhost]

TASK [Pause for 5 seconds to allow the vmid to populate] ***********************
Pausing for 5 seconds
ok: [localhost]

TASK [Set the vm_id] ***********************************************************
ok: [localhost]

TASK [Update the VM description by vmid] ***************************************
changed: [localhost]

TASK [Update the VM description by name (take 1)] ******************************
skipping: [localhost]

TASK [Update the VM's options] *************************************************
changed: [localhost]

TASK [Update the VM network interfaces] ****************************************
changed: [localhost]

TASK [Start the VM] ************************************************************
changed: [localhost]

TASK [Check VM running status] *************************************************
ok: [localhost]

TASK [Wait for VM to acquire an IP address] ************************************
FAILED - RETRYING: [localhost]: Wait for VM to acquire an IP address (30 retries left).
FAILED - RETRYING: [localhost]: Wait for VM to acquire an IP address (29 retries left).
ok: [localhost]

TASK [Save off the IP for use with checking on the WinRM/SSH connectivity] *****
ok: [localhost]

TASK [Refresh inventory if needed] *********************************************
included: /opt/ludus/ansible/range-management/tasks/proxmox/refresh_inventory.yml for localhost

TASK [Refresh inventory] *******************************************************

TASK [Show last_deployed_ip] ***************************************************
ok: [localhost] => {
    "last_deployed_ip": "192.0.2.97"
}

TASK [Wait for the host's control interface (WinRM via HTTPS) to come up] ******
skipping: [localhost]

TASK [Wait for the host's control interface (SSH) to come up] ******************
ok: [localhost]

PLAY [Configure the router] ****************************************************

TASK [Gathering Facts] *********************************************************
ok: [JD-router-debian11-x64]

TASK [Check if the .ludus-configured file exists] ******************************
ok: [JD-router-debian11-x64]

TASK [End play if configured] **************************************************
skipping: [JD-router-debian11-x64]

TASK [Configure IP and Hostname] ***********************************************
included: /opt/ludus/ansible/range-management/tasks/proxmox/configure-ip-and-hostname.yml for JD-router-debian11-x64

TASK [Check if the IP has been statically set correctly (Linux)] ***************
changed: [JD-router-debian11-x64]

TASK [Ending play for this host (Linux)] ***************************************
skipping: [JD-router-debian11-x64]

TASK [End play if configured (Linux)] ******************************************
skipping: [JD-router-debian11-x64]

TASK [Get network interface configuration (Windows)] ***************************
skipping: [JD-router-debian11-x64]

TASK [Output result] ***********************************************************
skipping: [JD-router-debian11-x64]

TASK [Get IP address of network interface (Windows)] ***************************
skipping: [JD-router-debian11-x64]

TASK [Show IP address] *********************************************************
skipping: [JD-router-debian11-x64]

TASK [Ending play for this host (Windows)] *************************************
skipping: [JD-router-debian11-x64]

TASK [End play if configured (Windows)] ****************************************
skipping: [JD-router-debian11-x64]

TASK [Primary Method - Set up static IP address (Windows)] *********************
skipping: [JD-router-debian11-x64]

TASK [Set old_hardware fact (Windows)] *****************************************
skipping: [JD-router-debian11-x64]

TASK [Is fallback needed?] *****************************************************
skipping: [JD-router-debian11-x64]

TASK [Fallback - Create file with ip changes with netsh.exe] *******************
skipping: [JD-router-debian11-x64]

TASK [Fallback - Set registry key for script execution on next reboot] *********
skipping: [JD-router-debian11-x64]

TASK [Fallback - Set registry key for script execution on next reboot] *********
skipping: [JD-router-debian11-x64]

TASK [Fallback - Reboot the machine to apply static IP (Fallback Method)] ******
skipping: [JD-router-debian11-x64]

TASK [Change ansible's ip address for the host (Windows)] **********************
skipping: [JD-router-debian11-x64]

TASK [Wait for the host's network interface to come back up (Windows)] *********
skipping: [JD-router-debian11-x64]

TASK [Clean up static IP script after reboot] **********************************
skipping: [JD-router-debian11-x64]

TASK [Set DNS (Windows)] *******************************************************
skipping: [JD-router-debian11-x64]

TASK [Set DNS search domain (Windows)] *****************************************
skipping: [JD-router-debian11-x64]

TASK [Lookup the timezone string for Windows] **********************************
skipping: [JD-router-debian11-x64]

TASK [Fail this host if we can't find the timezone] ****************************
skipping: [JD-router-debian11-x64]

TASK [Set the timezone (Windows)] **********************************************
skipping: [JD-router-debian11-x64]

TASK [Hostname change (Windows)] ***********************************************
skipping: [JD-router-debian11-x64]

TASK [Reboot] ******************************************************************
skipping: [JD-router-debian11-x64]

TASK [Wait for the host's control interface (WinRM via HTTPS) to come up] ******
skipping: [JD-router-debian11-x64]

TASK [Install dbus for systemd hostname changes] *******************************
changed: [JD-router-debian11-x64]

TASK [Install ifupdown to enable interfaces] ***********************************
skipping: [JD-router-debian11-x64]

TASK [Check if /etc/cloud exists and is a directory] ***************************
skipping: [JD-router-debian11-x64]

TASK [Ensure /etc/cloud/cloud-init.disabled exists to stop cloud-init from DHCPing the interface] ***
skipping: [JD-router-debian11-x64]

TASK [Check if /etc/netplan/00-installer-config.yaml exists] *******************
skipping: [JD-router-debian11-x64]

TASK [Delete /etc/netplan/00-installer-config.yaml] ****************************
skipping: [JD-router-debian11-x64]

TASK [Remove netplan cloud-init] ***********************************************
skipping: [JD-router-debian11-x64]

TASK [Check if /etc/cloud/cloud.cfg.d exists] **********************************
skipping: [JD-router-debian11-x64]

TASK [Disable cloud dhcp network] **********************************************
skipping: [JD-router-debian11-x64]

TASK [Set DNS search domain for systemd-resolved] ******************************
skipping: [JD-router-debian11-x64]

TASK [Set DNS server for systemd-resolved] *************************************
skipping: [JD-router-debian11-x64]

TASK [get MAC for vlan interface (Linux)] **************************************
changed: [JD-router-debian11-x64 -> localhost]

TASK [Set the vlan_mac variable] ***********************************************
ok: [JD-router-debian11-x64]

TASK [get interface for MAC of vlan interface (Linux)] *************************
changed: [JD-router-debian11-x64 -> localhost]

TASK [Set the interface_name variable] *****************************************
ok: [JD-router-debian11-x64]

TASK [Assert we found the interface name] **************************************
ok: [JD-router-debian11-x64] => {
    "changed": false,
    "msg": "Successfully found the interface name for VM 105"
}

TASK [Set static IP from the template (Linux-Debian)] **************************
changed: [JD-router-debian11-x64]

TASK [Set static IP from the template (Linux-RedHat/CentOS/Alma/Rocky)] ********
skipping: [JD-router-debian11-x64]

TASK [Check for "new" static IP files on (Linux-RedHat/CentOS/Alma/Rocky) > 8] ***
skipping: [JD-router-debian11-x64]

TASK [Remove "new" static IP file (Linux-RedHat/CentOS/Alma/Rocky) > 8] ********
skipping: [JD-router-debian11-x64]

TASK [Enable new interface (Linux)] ********************************************
changed: [JD-router-debian11-x64]

TASK [Setting hostname (Linux)] ************************************************
changed: [JD-router-debian11-x64]

TASK [Setting hostname (Linux-RedHat/CentOS/Alma/Rocky)] ***********************
skipping: [JD-router-debian11-x64]

TASK [Add IP address to /etc/hosts] ********************************************
changed: [JD-router-debian11-x64]

TASK [Add hostname to /etc/hosts] **********************************************
changed: [JD-router-debian11-x64]

TASK [Remove default entry for 127.0.0.1 from /etc/hosts] **********************
changed: [JD-router-debian11-x64]

TASK [Set the timezone (Linux)] ************************************************
changed: [JD-router-debian11-x64]

TASK [Reboot to set ip and hostname (Linux)] ***********************************
changed: [JD-router-debian11-x64]

TASK [Change ansible's ip address for the host] ********************************
ok: [JD-router-debian11-x64]

TASK [Wait for the host's control interface (SSH) to come up] ******************
ok: [JD-router-debian11-x64 -> localhost]

TASK [Set up static IP address (macOS)] ****************************************
skipping: [JD-router-debian11-x64]

TASK [Change ansible's ip address for the host] ********************************
skipping: [JD-router-debian11-x64]

TASK [Wait for the host's control interface (SSH) to come up] ******************
skipping: [JD-router-debian11-x64]

TASK [Set DNS (macOS)] *********************************************************
skipping: [JD-router-debian11-x64]

TASK [Setting hostname (macOS)] ************************************************
skipping: [JD-router-debian11-x64]

TASK [Set the timezone (macOS)] ************************************************
skipping: [JD-router-debian11-x64]

TASK [Refresh inventory] *******************************************************

TASK [Configure router] ********************************************************
included: /opt/ludus/ansible/range-management/tasks/router/configure-router.yml for JD-router-debian11-x64

TASK [Setup ip forwarding on the router] ***************************************
changed: [JD-router-debian11-x64]

TASK [Disable ipv6] ************************************************************
changed: [JD-router-debian11-x64]

TASK [Install dnsmasq, ca-certificates, and iptables-persistent] ***************
changed: [JD-router-debian11-x64]

TASK [Disable DNS in dnsmasq (only use it for DHCP)] ***************************
changed: [JD-router-debian11-x64]

TASK [Restart dnsmasq service to pick up changes] ******************************
changed: [JD-router-debian11-x64]

TASK [Install AdGuardHome] *****************************************************
changed: [JD-router-debian11-x64]

TASK [Configure AdGuardHome] ***************************************************
changed: [JD-router-debian11-x64]

TASK [Restart AdGuardHome to take config] **************************************
changed: [JD-router-debian11-x64]

TASK [Drop a file to signal that we have completed configuration] **************
changed: [JD-router-debian11-x64]

PLAY [Setup VLANs] *************************************************************

TASK [Gathering Facts] *********************************************************
ok: [localhost]

TASK [Collect VLANs] ***********************************************************
ok: [localhost] => (item={'vm_name': 'DEMO-albalad-DC-JD', 'hostname': 'dc01', 'template': 'win2022-server-x64-template', 'vlan': 10, 'ip_last_octet': 11, 'ram_gb': 8, 'cpus': 6, 'windows': {'sysprep': True}, 'domain': {'fqdn': 'albalad.bsides.rv', 'role': 'primary-dc'}})
ok: [localhost] => (item={'vm_name': 'DEMO-albalad-dev-JD', 'hostname': 'dev03', 'template': 'win2022-server-x64-template', 'vlan': 10, 'ip_last_octet': 12, 'ram_gb': 6, 'cpus': 4, 'windows': {'sysprep': True}, 'domain': {'fqdn': 'albalad.bsides.rv', 'role': 'member'}})

TASK [Add all VLAN interfaces to the router] ***********************************
included: /opt/ludus/ansible/range-management/tasks/router/add-vlan-to-router.yml for localhost => (item=10)

TASK [Get the VM id of the router via Proxmox API] *****************************
changed: [localhost]

TASK [Set the router_vm_id from API lookup] ************************************
ok: [localhost]

TASK [Get MAC for vlan interface] **********************************************
changed: [localhost]

TASK [Show vlan_mac_command] ***************************************************
ok: [localhost] => {
    "msg": ""
}

TASK [Set the vlan_mac variable] ***********************************************
skipping: [localhost]

TASK [Show VLAN MAC] ***********************************************************
skipping: [localhost]

TASK [Get interface for MAC of vlan interface] *********************************
skipping: [localhost]

TASK [Set the interface_name_command variable] *********************************
skipping: [localhost]

TASK [Get the number for the next network interface (starts at 0)] *************
changed: [localhost]

TASK [Set the rotuer_net_interface variable] ***********************************
ok: [localhost]

TASK [Add network interface to router] *****************************************
changed: [localhost]

TASK [Get MAC for vlan interface] **********************************************
changed: [localhost]

TASK [Set the vlan_mac variable] ***********************************************
ok: [localhost]

TASK [Get interface for MAC of vlan interface] *********************************
changed: [localhost]

TASK [Set the interface_name_command variable] *********************************
ok: [localhost]

TASK [Get the interface with a 192.0.2.x ip (WAN)] *****************************
changed: [localhost]

TASK [Set the router_external_interface variable] ******************************
ok: [localhost]

TASK [Set up the IP configuration for the new interface] ***********************
changed: [localhost -> JD-router-debian11-x64(192.0.2.102)]

TASK [Enable new interface] ****************************************************
changed: [localhost -> JD-router-debian11-x64(192.0.2.102)]

TASK [Configure dnsmasq (part 1) - setup base config] **************************
changed: [localhost -> JD-router-debian11-x64(192.0.2.102)]

TASK [Configure dnsmasq (part 2) - enable and restart service] *****************
changed: [localhost -> JD-router-debian11-x64(192.0.2.102)]

PLAY [Apply all user defined network rules to the router] **********************

TASK [Gathering Facts] *********************************************************
ok: [JD-router-debian11-x64]

TASK [Set any user defined firewall rules] *************************************
included: /opt/ludus/ansible/range-management/tasks/firewall/set-firewall-rules.yml for JD-router-debian11-x64

TASK [Set the policy for the FORWARD chain to DROP] ****************************
changed: [JD-router-debian11-x64]

TASK [Create the LUDUS_DEFAULTS chain] *****************************************
changed: [JD-router-debian11-x64]

TASK [Create the LUDUS_USER_RULES chain] ***************************************
changed: [JD-router-debian11-x64]

TASK [Create the LUDUS_TESTING chain] ******************************************
changed: [JD-router-debian11-x64]

TASK [Flush the LUDUS_USER_RULES table to remove any user defined rules to prevent old rules from lingering] ***
changed: [JD-router-debian11-x64]

TASK [Flush the LUDUS_DEFAULTS table to remove any user defined rules to prevent old rules from lingering] ***
changed: [JD-router-debian11-x64]

TASK [Flush the INPUT to prevent locking ourselves out during rule setup] ******
changed: [JD-router-debian11-x64]

TASK [Get the VM id of the router via Proxmox API] *****************************
changed: [JD-router-debian11-x64 -> localhost]

TASK [Set the router_vm_id from API lookup] ************************************
ok: [JD-router-debian11-x64]

TASK [Get the interface with a 192.0.2.x ip (WAN)] *****************************
changed: [JD-router-debian11-x64 -> localhost]

TASK [Set the router_external_interface variable] ******************************
ok: [JD-router-debian11-x64]

TASK [Deny all other traffic from the external interface] **********************
changed: [JD-router-debian11-x64]

TASK [Allow the user's WireGuard IP to hit this router from the outside] *******
changed: [JD-router-debian11-x64]

TASK [Set range_access_grants_array from access_grants_array] ******************
ok: [JD-router-debian11-x64]

TASK [Modify router firewall to allow WireGuard IP's for access grants to this range] ***
skipping: [JD-router-debian11-x64]

TASK [Set the default WireGuard subnet rule] ***********************************
changed: [JD-router-debian11-x64]

TASK [Set the default allow related/established out to the user's WireGuard IP] ***
changed: [JD-router-debian11-x64]

TASK [Set the default external rule] *******************************************
changed: [JD-router-debian11-x64]

TASK [Set the default inter-VLAN rule] *****************************************
changed: [JD-router-debian11-x64]

TASK [Jump all traffic from FORWARD to LUDUS_DEFAULTS] *************************
changed: [JD-router-debian11-x64]

TASK [Jump all traffic from FORWARD to LUDUS_TESTING] **************************
changed: [JD-router-debian11-x64]

TASK [Jump all traffic from FORWARD to LUDUS_USER_RULES] ***********************
changed: [JD-router-debian11-x64]

TASK [Deny all range traffic to SSH on this router] ****************************
changed: [JD-router-debian11-x64]

TASK [Jump all traffic from INPUT to LUDUS_DEFAULTS] ***************************
changed: [JD-router-debian11-x64]

TASK [Loop over each user defined rule] ****************************************
skipping: [JD-router-debian11-x64]

TASK [Deny all range traffic to user defined "always_blocked_networks"] ********
skipping: [JD-router-debian11-x64]

TASK [Allow the Ludus IP to hit this router from the outside for ansible] ******
changed: [JD-router-debian11-x64]

TASK [Reset the conntrack entries to prevent previously allowed traffic to continue] ***
ASYNC OK on JD-router-debian11-x64: jid=j652746220104.4170
changed: [JD-router-debian11-x64]

TASK [Save current state of the firewall to a file] ****************************
changed: [JD-router-debian11-x64]

PLAY [Apply all user defined roles to the router (Enterprise)] *****************

TASK [Gathering Facts] *********************************************************
ok: [JD-router-debian11-x64]

TASK [Check for enterprise license] ********************************************
skipping: [JD-router-debian11-x64]

TASK [Set any user defined firewall rules] *************************************
skipping: [JD-router-debian11-x64]

PLAY [Apply outbound WireGuard to the router (Enterprise)] *********************

TASK [Gathering Facts] *********************************************************
ok: [JD-router-debian11-x64]

TASK [Check for enterprise license] ********************************************
skipping: [JD-router-debian11-x64]

TASK [Clear any outbound WireGuard related configurations] *********************
skipping: [JD-router-debian11-x64]

TASK [Setup outbound WireGuard on the router] **********************************
skipping: [JD-router-debian11-x64]

PLAY [Apply inbound WireGuard to the router (Enterprise)] **********************

TASK [Gathering Facts] *********************************************************
ok: [JD-router-debian11-x64]

TASK [Check for enterprise license] ********************************************
skipping: [JD-router-debian11-x64]

TASK [Clear any inbound WireGuard related configurations] **********************
skipping: [JD-router-debian11-x64]

TASK [Setup inbound WireGuard on the router] ***********************************
skipping: [JD-router-debian11-x64]

PLAY [Deploy DC VMs] ***********************************************************

TASK [Gathering Facts] *********************************************************
ok: [localhost]

TASK [Deploy VM] ***************************************************************
skipping: [localhost] => (item={'vm_name': 'DEMO-albalad-dev-JD', 'hostname': 'dev03', 'template': 'win2022-server-x64-template', 'vlan': 10, 'ip_last_octet': 12, 'ram_gb': 6, 'cpus': 4, 'windows': {'sysprep': True}, 'domain': {'fqdn': 'albalad.bsides.rv', 'role': 'member'}})
included: /opt/ludus/ansible/range-management/tasks/proxmox/deploy-vm.yml for localhost => (item={'vm_name': 'DEMO-albalad-DC-JD', 'hostname': 'dc01', 'template': 'win2022-server-x64-template', 'vlan': 10, 'ip_last_octet': 11, 'ram_gb': 8, 'cpus': 6, 'windows': {'sysprep': True}, 'domain': {'fqdn': 'albalad.bsides.rv', 'role': 'primary-dc'}})

TASK [Create a VM from a template] *********************************************
changed: [localhost]

TASK [Pause for 5 seconds to allow the vmid to populate] ***********************
Pausing for 5 seconds
ok: [localhost]

TASK [Set the vm_id] ***********************************************************
ok: [localhost]

TASK [Update the VM description by vmid] ***************************************
changed: [localhost]

TASK [Update the VM description by name (take 1)] ******************************
skipping: [localhost]

TASK [Update the VM's options] *************************************************
changed: [localhost]

TASK [Update the VM network interfaces] ****************************************
changed: [localhost]

TASK [Start the VM] ************************************************************
^C
root@ludus:/mnt/hgfs/sharedfolderfortheludus/RangeVillage-Demo-main/BSidesAmman-2025# ludus range abort
[INFO]  Ansible process aborted
root@ludus:/mnt/hgfs/sharedfolderfortheludus/RangeVillage-Demo-main/BSidesAmman-2025# ludus range destroy
[WARN]
!!! This will destroy all VMs for the range of user ID: JD !!!

Do you want to continue? (y/N):
y
[INFO]  Range destroy in progress
root@ludus:/mnt/hgfs/sharedfolderfortheludus/RangeVillage-Demo-main/BSidesAmman-2025# ludus range config set -f demo.yml
[INFO]  Your range config has been successfully updated.
root@ludus:/mnt/hgfs/sharedfolderfortheludus/RangeVillage-Demo-main/BSidesAmman-2025# ludus range config get
ludus:
  - vm_name: "DEMO-albalad-DC-{{ range_id }}"
    hostname: "dc01"
    template: win2022-server-x64-template
    vlan: 10
    ip_last_octet: 11
    ram_gb: 8
    cpus: 4
    windows:
      sysprep: true
    domain:
      fqdn: albalad.bsides.rv
      role: primary-dc

  - vm_name: "DEMO-albalad-dev-{{ range_id }}"
    hostname: "dev03"
    template: win2022-server-x64-template
    vlan: 10
    ip_last_octet: 12
    ram_gb: 6
    cpus: 4
    windows:
      sysprep: true
    domain:
      fqdn: albalad.bsides.rv
      role: member

defaults:
  ad_domain_admin: Admin
  ad_domain_admin_password: 6m51A3E6bRM4Z9fv
  ad_domain_user: User
  ad_domain_user_password: 6m51A3E6bRM4Z9fv

  # ignore
  snapshot_with_RAM: true                  # When entering testing mode, capture the RAM state which allows reverting to a running VM
  stale_hours: 0                           # How many hours until a pre-existing snapshot should be deleted and retaken (if entering and exiting testing mode quickly)
  ad_domain_functional_level: Win2012R2    # The functional level of each Windows domain created by Ludus - options are: "Win2003", "Win2008", "Win2008R2", "Win2012", "Win2012R2", or "WinThreshold"
  ad_forest_functional_level: Win2012R2    # The functional level of each Windows forest created by Ludus - options are: "Win2003", "Win2008", "Win2008R2", "Win2012", "Win2012R2", or "WinThreshold"
  ad_domain_safe_mode_password: 6m51A3E6bRM4Z9fv   # The domain safe mode password for every Windows domain
  enable_dynamic_wallpaper: false
  timezone: Asia/Singapore               # The timezone for all VMs, use the TZ identifier format from https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
root@ludus:/mnt/hgfs/sharedfolderfortheludus/RangeVillage-Demo-main/BSidesAmman-2025# ludus range deploy
[INFO]  Range deploy started
root@ludus:/mnt/hgfs/sharedfolderfortheludus/RangeVillage-Demo-main/BSidesAmman-2025# ludus range logs -f
[WARNING]: provided hosts list is empty, only localhost is available. Note that
the implicit localhost does not match 'all'

PLAY [Pre run checks] **********************************************************

TASK [Acquire session ticket] **************************************************
ok: [localhost]

TASK [Extract ticket from response] ********************************************
ok: [localhost]

TASK [Check for valid dynamic inventory] ***************************************
ok: [localhost] => {
    "changed": false,
    "msg": "Dynamic inventory loaded!"
}

PLAY [Deploy the router VM] ****************************************************

TASK [Gathering Facts] *********************************************************
ok: [localhost]

TASK [Deploy router VM] ********************************************************
included: /opt/ludus/ansible/range-management/tasks/proxmox/deploy-vm.yml for localhost

TASK [Create a VM from a template] *********************************************
changed: [localhost]

TASK [Pause for 5 seconds to allow the vmid to populate] ***********************
Pausing for 5 seconds
ok: [localhost]

TASK [Set the vm_id] ***********************************************************
ok: [localhost]

TASK [Update the VM description by vmid] ***************************************
changed: [localhost]

TASK [Update the VM description by name (take 1)] ******************************
skipping: [localhost]

TASK [Update the VM's options] *************************************************
changed: [localhost]

TASK [Update the VM network interfaces] ****************************************
changed: [localhost]

TASK [Start the VM] ************************************************************
changed: [localhost]

TASK [Check VM running status] *************************************************
ok: [localhost]

TASK [Wait for VM to acquire an IP address] ************************************
FAILED - RETRYING: [localhost]: Wait for VM to acquire an IP address (30 retries left).
FAILED - RETRYING: [localhost]: Wait for VM to acquire an IP address (29 retries left).
ok: [localhost]

TASK [Save off the IP for use with checking on the WinRM/SSH connectivity] *****
ok: [localhost]

TASK [Refresh inventory if needed] *********************************************
included: /opt/ludus/ansible/range-management/tasks/proxmox/refresh_inventory.yml for localhost

TASK [Refresh inventory] *******************************************************

TASK [Show last_deployed_ip] ***************************************************
ok: [localhost] => {
    "last_deployed_ip": "192.0.2.72"
}

TASK [Wait for the host's control interface (WinRM via HTTPS) to come up] ******
skipping: [localhost]

TASK [Wait for the host's control interface (SSH) to come up] ******************
ok: [localhost]

PLAY [Configure the router] ****************************************************

TASK [Gathering Facts] *********************************************************
ok: [JD-router-debian11-x64]

TASK [Check if the .ludus-configured file exists] ******************************
ok: [JD-router-debian11-x64]

TASK [End play if configured] **************************************************
skipping: [JD-router-debian11-x64]

TASK [Configure IP and Hostname] ***********************************************
included: /opt/ludus/ansible/range-management/tasks/proxmox/configure-ip-and-hostname.yml for JD-router-debian11-x64

TASK [Check if the IP has been statically set correctly (Linux)] ***************
changed: [JD-router-debian11-x64]

TASK [Ending play for this host (Linux)] ***************************************
skipping: [JD-router-debian11-x64]

TASK [End play if configured (Linux)] ******************************************
skipping: [JD-router-debian11-x64]

TASK [Get network interface configuration (Windows)] ***************************
skipping: [JD-router-debian11-x64]

TASK [Output result] ***********************************************************
skipping: [JD-router-debian11-x64]

TASK [Get IP address of network interface (Windows)] ***************************
skipping: [JD-router-debian11-x64]

TASK [Show IP address] *********************************************************
skipping: [JD-router-debian11-x64]

TASK [Ending play for this host (Windows)] *************************************
skipping: [JD-router-debian11-x64]

TASK [End play if configured (Windows)] ****************************************
skipping: [JD-router-debian11-x64]

TASK [Primary Method - Set up static IP address (Windows)] *********************
skipping: [JD-router-debian11-x64]

TASK [Set old_hardware fact (Windows)] *****************************************
skipping: [JD-router-debian11-x64]

TASK [Is fallback needed?] *****************************************************
skipping: [JD-router-debian11-x64]

TASK [Fallback - Create file with ip changes with netsh.exe] *******************
skipping: [JD-router-debian11-x64]

TASK [Fallback - Set registry key for script execution on next reboot] *********
skipping: [JD-router-debian11-x64]

TASK [Fallback - Set registry key for script execution on next reboot] *********
skipping: [JD-router-debian11-x64]

TASK [Fallback - Reboot the machine to apply static IP (Fallback Method)] ******
skipping: [JD-router-debian11-x64]

TASK [Change ansible's ip address for the host (Windows)] **********************
skipping: [JD-router-debian11-x64]

TASK [Wait for the host's network interface to come back up (Windows)] *********
skipping: [JD-router-debian11-x64]

TASK [Clean up static IP script after reboot] **********************************
skipping: [JD-router-debian11-x64]

TASK [Set DNS (Windows)] *******************************************************
skipping: [JD-router-debian11-x64]

TASK [Set DNS search domain (Windows)] *****************************************
skipping: [JD-router-debian11-x64]

TASK [Lookup the timezone string for Windows] **********************************
skipping: [JD-router-debian11-x64]

TASK [Fail this host if we can't find the timezone] ****************************
skipping: [JD-router-debian11-x64]

TASK [Set the timezone (Windows)] **********************************************
skipping: [JD-router-debian11-x64]

TASK [Hostname change (Windows)] ***********************************************
skipping: [JD-router-debian11-x64]

TASK [Reboot] ******************************************************************
skipping: [JD-router-debian11-x64]

TASK [Wait for the host's control interface (WinRM via HTTPS) to come up] ******
skipping: [JD-router-debian11-x64]

TASK [Install dbus for systemd hostname changes] *******************************
changed: [JD-router-debian11-x64]

TASK [Install ifupdown to enable interfaces] ***********************************
skipping: [JD-router-debian11-x64]

TASK [Check if /etc/cloud exists and is a directory] ***************************
skipping: [JD-router-debian11-x64]

TASK [Ensure /etc/cloud/cloud-init.disabled exists to stop cloud-init from DHCPing the interface] ***
skipping: [JD-router-debian11-x64]

TASK [Check if /etc/netplan/00-installer-config.yaml exists] *******************
skipping: [JD-router-debian11-x64]

TASK [Delete /etc/netplan/00-installer-config.yaml] ****************************
skipping: [JD-router-debian11-x64]

TASK [Remove netplan cloud-init] ***********************************************
skipping: [JD-router-debian11-x64]

TASK [Check if /etc/cloud/cloud.cfg.d exists] **********************************
skipping: [JD-router-debian11-x64]

TASK [Disable cloud dhcp network] **********************************************
skipping: [JD-router-debian11-x64]

TASK [Set DNS search domain for systemd-resolved] ******************************
skipping: [JD-router-debian11-x64]

TASK [Set DNS server for systemd-resolved] *************************************
skipping: [JD-router-debian11-x64]

TASK [get MAC for vlan interface (Linux)] **************************************
changed: [JD-router-debian11-x64 -> localhost]

TASK [Set the vlan_mac variable] ***********************************************
ok: [JD-router-debian11-x64]

TASK [get interface for MAC of vlan interface (Linux)] *************************
changed: [JD-router-debian11-x64 -> localhost]

TASK [Set the interface_name variable] *****************************************
ok: [JD-router-debian11-x64]

TASK [Assert we found the interface name] **************************************
ok: [JD-router-debian11-x64] => {
    "changed": false,
    "msg": "Successfully found the interface name for VM 105"
}

TASK [Set static IP from the template (Linux-Debian)] **************************
changed: [JD-router-debian11-x64]

TASK [Set static IP from the template (Linux-RedHat/CentOS/Alma/Rocky)] ********
skipping: [JD-router-debian11-x64]

TASK [Check for "new" static IP files on (Linux-RedHat/CentOS/Alma/Rocky) > 8] ***
skipping: [JD-router-debian11-x64]

TASK [Remove "new" static IP file (Linux-RedHat/CentOS/Alma/Rocky) > 8] ********
skipping: [JD-router-debian11-x64]

TASK [Enable new interface (Linux)] ********************************************
changed: [JD-router-debian11-x64]

TASK [Setting hostname (Linux)] ************************************************
changed: [JD-router-debian11-x64]

TASK [Setting hostname (Linux-RedHat/CentOS/Alma/Rocky)] ***********************
skipping: [JD-router-debian11-x64]

TASK [Add IP address to /etc/hosts] ********************************************
changed: [JD-router-debian11-x64]

TASK [Add hostname to /etc/hosts] **********************************************
changed: [JD-router-debian11-x64]

TASK [Remove default entry for 127.0.0.1 from /etc/hosts] **********************
changed: [JD-router-debian11-x64]

TASK [Set the timezone (Linux)] ************************************************
changed: [JD-router-debian11-x64]

TASK [Reboot to set ip and hostname (Linux)] ***********************************
changed: [JD-router-debian11-x64]

TASK [Change ansible's ip address for the host] ********************************
ok: [JD-router-debian11-x64]

TASK [Wait for the host's control interface (SSH) to come up] ******************
ok: [JD-router-debian11-x64 -> localhost]

TASK [Set up static IP address (macOS)] ****************************************
skipping: [JD-router-debian11-x64]

TASK [Change ansible's ip address for the host] ********************************
skipping: [JD-router-debian11-x64]

TASK [Wait for the host's control interface (SSH) to come up] ******************
skipping: [JD-router-debian11-x64]

TASK [Set DNS (macOS)] *********************************************************
skipping: [JD-router-debian11-x64]

TASK [Setting hostname (macOS)] ************************************************
skipping: [JD-router-debian11-x64]

TASK [Set the timezone (macOS)] ************************************************
skipping: [JD-router-debian11-x64]

TASK [Refresh inventory] *******************************************************

TASK [Configure router] ********************************************************
included: /opt/ludus/ansible/range-management/tasks/router/configure-router.yml for JD-router-debian11-x64

TASK [Setup ip forwarding on the router] ***************************************
changed: [JD-router-debian11-x64]

TASK [Disable ipv6] ************************************************************
changed: [JD-router-debian11-x64]

TASK [Install dnsmasq, ca-certificates, and iptables-persistent] ***************
changed: [JD-router-debian11-x64]

TASK [Disable DNS in dnsmasq (only use it for DHCP)] ***************************
changed: [JD-router-debian11-x64]

TASK [Restart dnsmasq service to pick up changes] ******************************
changed: [JD-router-debian11-x64]

TASK [Install AdGuardHome] *****************************************************
changed: [JD-router-debian11-x64]

TASK [Configure AdGuardHome] ***************************************************
changed: [JD-router-debian11-x64]

TASK [Restart AdGuardHome to take config] **************************************
changed: [JD-router-debian11-x64]

TASK [Drop a file to signal that we have completed configuration] **************
changed: [JD-router-debian11-x64]

PLAY [Setup VLANs] *************************************************************

TASK [Gathering Facts] *********************************************************
ok: [localhost]

TASK [Collect VLANs] ***********************************************************
ok: [localhost] => (item={'vm_name': 'DEMO-albalad-DC-JD', 'hostname': 'dc01', 'template': 'win2022-server-x64-template', 'vlan': 10, 'ip_last_octet': 11, 'ram_gb': 8, 'cpus': 4, 'windows': {'sysprep': True}, 'domain': {'fqdn': 'albalad.bsides.rv', 'role': 'primary-dc'}})
ok: [localhost] => (item={'vm_name': 'DEMO-albalad-dev-JD', 'hostname': 'dev03', 'template': 'win2022-server-x64-template', 'vlan': 10, 'ip_last_octet': 12, 'ram_gb': 6, 'cpus': 4, 'windows': {'sysprep': True}, 'domain': {'fqdn': 'albalad.bsides.rv', 'role': 'member'}})

TASK [Add all VLAN interfaces to the router] ***********************************
included: /opt/ludus/ansible/range-management/tasks/router/add-vlan-to-router.yml for localhost => (item=10)

TASK [Get the VM id of the router via Proxmox API] *****************************
changed: [localhost]

TASK [Set the router_vm_id from API lookup] ************************************
ok: [localhost]

TASK [Get MAC for vlan interface] **********************************************
changed: [localhost]

TASK [Show vlan_mac_command] ***************************************************
ok: [localhost] => {
    "msg": ""
}

TASK [Set the vlan_mac variable] ***********************************************
skipping: [localhost]

TASK [Show VLAN MAC] ***********************************************************
skipping: [localhost]

TASK [Get interface for MAC of vlan interface] *********************************
skipping: [localhost]

TASK [Set the interface_name_command variable] *********************************
skipping: [localhost]

TASK [Get the number for the next network interface (starts at 0)] *************
changed: [localhost]

TASK [Set the rotuer_net_interface variable] ***********************************
ok: [localhost]

TASK [Add network interface to router] *****************************************
changed: [localhost]

TASK [Get MAC for vlan interface] **********************************************
changed: [localhost]

TASK [Set the vlan_mac variable] ***********************************************
ok: [localhost]

TASK [Get interface for MAC of vlan interface] *********************************
changed: [localhost]

TASK [Set the interface_name_command variable] *********************************
ok: [localhost]

TASK [Get the interface with a 192.0.2.x ip (WAN)] *****************************
changed: [localhost]

TASK [Set the router_external_interface variable] ******************************
ok: [localhost]

TASK [Set up the IP configuration for the new interface] ***********************
changed: [localhost -> JD-router-debian11-x64(192.0.2.102)]

TASK [Enable new interface] ****************************************************
changed: [localhost -> JD-router-debian11-x64(192.0.2.102)]

TASK [Configure dnsmasq (part 1) - setup base config] **************************
changed: [localhost -> JD-router-debian11-x64(192.0.2.102)]

TASK [Configure dnsmasq (part 2) - enable and restart service] *****************
changed: [localhost -> JD-router-debian11-x64(192.0.2.102)]

PLAY [Apply all user defined network rules to the router] **********************

TASK [Gathering Facts] *********************************************************
ok: [JD-router-debian11-x64]

TASK [Set any user defined firewall rules] *************************************
included: /opt/ludus/ansible/range-management/tasks/firewall/set-firewall-rules.yml for JD-router-debian11-x64

TASK [Set the policy for the FORWARD chain to DROP] ****************************
changed: [JD-router-debian11-x64]

TASK [Create the LUDUS_DEFAULTS chain] *****************************************
changed: [JD-router-debian11-x64]

TASK [Create the LUDUS_USER_RULES chain] ***************************************
changed: [JD-router-debian11-x64]

TASK [Create the LUDUS_TESTING chain] ******************************************
changed: [JD-router-debian11-x64]

TASK [Flush the LUDUS_USER_RULES table to remove any user defined rules to prevent old rules from lingering] ***
changed: [JD-router-debian11-x64]

TASK [Flush the LUDUS_DEFAULTS table to remove any user defined rules to prevent old rules from lingering] ***
changed: [JD-router-debian11-x64]

TASK [Flush the INPUT to prevent locking ourselves out during rule setup] ******
changed: [JD-router-debian11-x64]

TASK [Get the VM id of the router via Proxmox API] *****************************
changed: [JD-router-debian11-x64 -> localhost]

TASK [Set the router_vm_id from API lookup] ************************************
ok: [JD-router-debian11-x64]

TASK [Get the interface with a 192.0.2.x ip (WAN)] *****************************
changed: [JD-router-debian11-x64 -> localhost]

TASK [Set the router_external_interface variable] ******************************
ok: [JD-router-debian11-x64]

TASK [Deny all other traffic from the external interface] **********************
changed: [JD-router-debian11-x64]

TASK [Allow the user's WireGuard IP to hit this router from the outside] *******
changed: [JD-router-debian11-x64]

TASK [Set range_access_grants_array from access_grants_array] ******************
ok: [JD-router-debian11-x64]

TASK [Modify router firewall to allow WireGuard IP's for access grants to this range] ***
skipping: [JD-router-debian11-x64]

TASK [Set the default WireGuard subnet rule] ***********************************
changed: [JD-router-debian11-x64]

TASK [Set the default allow related/established out to the user's WireGuard IP] ***
changed: [JD-router-debian11-x64]

TASK [Set the default external rule] *******************************************
changed: [JD-router-debian11-x64]

TASK [Set the default inter-VLAN rule] *****************************************
changed: [JD-router-debian11-x64]

TASK [Jump all traffic from FORWARD to LUDUS_DEFAULTS] *************************
changed: [JD-router-debian11-x64]

TASK [Jump all traffic from FORWARD to LUDUS_TESTING] **************************
changed: [JD-router-debian11-x64]

TASK [Jump all traffic from FORWARD to LUDUS_USER_RULES] ***********************
changed: [JD-router-debian11-x64]

TASK [Deny all range traffic to SSH on this router] ****************************
changed: [JD-router-debian11-x64]

TASK [Jump all traffic from INPUT to LUDUS_DEFAULTS] ***************************
changed: [JD-router-debian11-x64]

TASK [Loop over each user defined rule] ****************************************
skipping: [JD-router-debian11-x64]

TASK [Deny all range traffic to user defined "always_blocked_networks"] ********
skipping: [JD-router-debian11-x64]

TASK [Allow the Ludus IP to hit this router from the outside for ansible] ******
changed: [JD-router-debian11-x64]

TASK [Reset the conntrack entries to prevent previously allowed traffic to continue] ***
ASYNC OK on JD-router-debian11-x64: jid=j991921658474.4204
changed: [JD-router-debian11-x64]

TASK [Save current state of the firewall to a file] ****************************
changed: [JD-router-debian11-x64]

PLAY [Apply all user defined roles to the router (Enterprise)] *****************

TASK [Gathering Facts] *********************************************************
ok: [JD-router-debian11-x64]

TASK [Check for enterprise license] ********************************************
skipping: [JD-router-debian11-x64]

TASK [Set any user defined firewall rules] *************************************
skipping: [JD-router-debian11-x64]

PLAY [Apply outbound WireGuard to the router (Enterprise)] *********************

TASK [Gathering Facts] *********************************************************
ok: [JD-router-debian11-x64]

TASK [Check for enterprise license] ********************************************
skipping: [JD-router-debian11-x64]

TASK [Clear any outbound WireGuard related configurations] *********************
skipping: [JD-router-debian11-x64]

TASK [Setup outbound WireGuard on the router] **********************************
skipping: [JD-router-debian11-x64]

PLAY [Apply inbound WireGuard to the router (Enterprise)] **********************

TASK [Gathering Facts] *********************************************************
ok: [JD-router-debian11-x64]

TASK [Check for enterprise license] ********************************************
skipping: [JD-router-debian11-x64]

TASK [Clear any inbound WireGuard related configurations] **********************
skipping: [JD-router-debian11-x64]

TASK [Setup inbound WireGuard on the router] ***********************************
skipping: [JD-router-debian11-x64]

PLAY [Deploy DC VMs] ***********************************************************

TASK [Gathering Facts] *********************************************************
ok: [localhost]

TASK [Deploy VM] ***************************************************************
skipping: [localhost] => (item={'vm_name': 'DEMO-albalad-dev-JD', 'hostname': 'dev03', 'template': 'win2022-server-x64-template', 'vlan': 10, 'ip_last_octet': 12, 'ram_gb': 6, 'cpus': 4, 'windows': {'sysprep': True}, 'domain': {'fqdn': 'albalad.bsides.rv', 'role': 'member'}})
included: /opt/ludus/ansible/range-management/tasks/proxmox/deploy-vm.yml for localhost => (item={'vm_name': 'DEMO-albalad-DC-JD', 'hostname': 'dc01', 'template': 'win2022-server-x64-template', 'vlan': 10, 'ip_last_octet': 11, 'ram_gb': 8, 'cpus': 4, 'windows': {'sysprep': True}, 'domain': {'fqdn': 'albalad.bsides.rv', 'role': 'primary-dc'}})

TASK [Create a VM from a template] *********************************************
changed: [localhost]

TASK [Pause for 5 seconds to allow the vmid to populate] ***********************
Pausing for 5 seconds
ok: [localhost]

TASK [Set the vm_id] ***********************************************************
ok: [localhost]

TASK [Update the VM description by vmid] ***************************************
changed: [localhost]

TASK [Update the VM description by name (take 1)] ******************************
skipping: [localhost]

TASK [Update the VM's options] *************************************************
changed: [localhost]

TASK [Update the VM network interfaces] ****************************************
changed: [localhost]

TASK [Start the VM] ************************************************************
changed: [localhost]

TASK [Check VM running status] *************************************************
ok: [localhost]

TASK [Wait for VM to acquire an IP address] ************************************
FAILED - RETRYING: [localhost]: Wait for VM to acquire an IP address (30 retries left).
FAILED - RETRYING: [localhost]: Wait for VM to acquire an IP address (29 retries left).
FAILED - RETRYING: [localhost]: Wait for VM to acquire an IP address (28 retries left).
FAILED - RETRYING: [localhost]: Wait for VM to acquire an IP address (27 retries left).
FAILED - RETRYING: [localhost]: Wait for VM to acquire an IP address (26 retries left).
FAILED - RETRYING: [localhost]: Wait for VM to acquire an IP address (25 retries left).
FAILED - RETRYING: [localhost]: Wait for VM to acquire an IP address (24 retries left).
FAILED - RETRYING: [localhost]: Wait for VM to acquire an IP address (23 retries left).
FAILED - RETRYING: [localhost]: Wait for VM to acquire an IP address (22 retries left).
FAILED - RETRYING: [localhost]: Wait for VM to acquire an IP address (21 retries left).
ok: [localhost]

TASK [Save off the IP for use with checking on the WinRM/SSH connectivity] *****
ok: [localhost]

TASK [Refresh inventory if needed] *********************************************
included: /opt/ludus/ansible/range-management/tasks/proxmox/refresh_inventory.yml for localhost

TASK [Refresh inventory] *******************************************************

TASK [Show last_deployed_ip] ***************************************************
ok: [localhost] => {
    "last_deployed_ip": "10.2.10.243"
}

TASK [Wait for the host's control interface (WinRM via HTTPS) to come up] ******
ok: [localhost]

TASK [Wait for the host's control interface (SSH) to come up] ******************
skipping: [localhost]

PLAY [Deploy non-DC VMs] *******************************************************

TASK [Gathering Facts] *********************************************************
ok: [localhost]

TASK [Deploy VM] ***************************************************************
skipping: [localhost] => (item={'vm_name': 'DEMO-albalad-DC-JD', 'hostname': 'dc01', 'template': 'win2022-server-x64-template', 'vlan': 10, 'ip_last_octet': 11, 'ram_gb': 8, 'cpus': 4, 'windows': {'sysprep': True}, 'domain': {'fqdn': 'albalad.bsides.rv', 'role': 'primary-dc'}})
included: /opt/ludus/ansible/range-management/tasks/proxmox/deploy-vm.yml for localhost => (item={'vm_name': 'DEMO-albalad-dev-JD', 'hostname': 'dev03', 'template': 'win2022-server-x64-template', 'vlan': 10, 'ip_last_octet': 12, 'ram_gb': 6, 'cpus': 4, 'windows': {'sysprep': True}, 'domain': {'fqdn': 'albalad.bsides.rv', 'role': 'member'}})

TASK [Create a VM from a template] *********************************************
changed: [localhost]

TASK [Pause for 5 seconds to allow the vmid to populate] ***********************
Pausing for 5 seconds
ok: [localhost]

TASK [Set the vm_id] ***********************************************************
ok: [localhost]

TASK [Update the VM description by vmid] ***************************************
changed: [localhost]

TASK [Update the VM description by name (take 1)] ******************************
skipping: [localhost]

TASK [Update the VM's options] *************************************************
changed: [localhost]

TASK [Update the VM network interfaces] ****************************************
changed: [localhost]

TASK [Start the VM] ************************************************************
changed: [localhost]

TASK [Check VM running status] *************************************************
ok: [localhost]

TASK [Wait for VM to acquire an IP address] ************************************
FAILED - RETRYING: [localhost]: Wait for VM to acquire an IP address (30 retries left).
FAILED - RETRYING: [localhost]: Wait for VM to acquire an IP address (29 retries left).
FAILED - RETRYING: [localhost]: Wait for VM to acquire an IP address (28 retries left).
FAILED - RETRYING: [localhost]: Wait for VM to acquire an IP address (27 retries left).
FAILED - RETRYING: [localhost]: Wait for VM to acquire an IP address (26 retries left).
FAILED - RETRYING: [localhost]: Wait for VM to acquire an IP address (25 retries left).
FAILED - RETRYING: [localhost]: Wait for VM to acquire an IP address (24 retries left).
FAILED - RETRYING: [localhost]: Wait for VM to acquire an IP address (23 retries left).
FAILED - RETRYING: [localhost]: Wait for VM to acquire an IP address (22 retries left).
FAILED - RETRYING: [localhost]: Wait for VM to acquire an IP address (21 retries left).
FAILED - RETRYING: [localhost]: Wait for VM to acquire an IP address (20 retries left).
FAILED - RETRYING: [localhost]: Wait for VM to acquire an IP address (19 retries left).
FAILED - RETRYING: [localhost]: Wait for VM to acquire an IP address (18 retries left).
FAILED - RETRYING: [localhost]: Wait for VM to acquire an IP address (17 retries left).
FAILED - RETRYING: [localhost]: Wait for VM to acquire an IP address (16 retries left).
FAILED - RETRYING: [localhost]: Wait for VM to acquire an IP address (15 retries left).
FAILED - RETRYING: [localhost]: Wait for VM to acquire an IP address (14 retries left).
ok: [localhost]

TASK [Save off the IP for use with checking on the WinRM/SSH connectivity] *****
ok: [localhost]

TASK [Refresh inventory if needed] *********************************************
included: /opt/ludus/ansible/range-management/tasks/proxmox/refresh_inventory.yml for localhost

TASK [Refresh inventory] *******************************************************

TASK [Show last_deployed_ip] ***************************************************
ok: [localhost] => {
    "last_deployed_ip": "10.2.10.202"
}

TASK [Wait for the host's control interface (WinRM via HTTPS) to come up] ******
ok: [localhost]

TASK [Wait for the host's control interface (SSH) to come up] ******************
skipping: [localhost]

PLAY [Collect VM names] ********************************************************

TASK [Collect VM names] ********************************************************
ok: [localhost] => (item={'vm_name': 'DEMO-albalad-DC-JD', 'hostname': 'dc01', 'template': 'win2022-server-x64-template', 'vlan': 10, 'ip_last_octet': 11, 'ram_gb': 8, 'cpus': 4, 'windows': {'sysprep': True}, 'domain': {'fqdn': 'albalad.bsides.rv', 'role': 'primary-dc'}})
ok: [localhost] => (item={'vm_name': 'DEMO-albalad-dev-JD', 'hostname': 'dev03', 'template': 'win2022-server-x64-template', 'vlan': 10, 'ip_last_octet': 12, 'ram_gb': 6, 'cpus': 4, 'windows': {'sysprep': True}, 'domain': {'fqdn': 'albalad.bsides.rv', 'role': 'member'}})

PLAY [Configure IP and Hostname for all VMs] ***********************************

TASK [Gathering Facts] *********************************************************
[WARNING]: Failed to collect winrm due to timeout
[WARNING]: Failed to collect distribution due to timeout
ok: [DEMO-albalad-DC-JD]
ok: [DEMO-albalad-dev-JD]

TASK [Configure IP and Hostname] ***********************************************
included: /opt/ludus/ansible/range-management/tasks/proxmox/configure-ip-and-hostname.yml for DEMO-albalad-DC-JD, DEMO-albalad-dev-JD

TASK [Check if the IP has been statically set correctly (Linux)] ***************
skipping: [DEMO-albalad-DC-JD]
skipping: [DEMO-albalad-dev-JD]

TASK [Ending play for this host (Linux)] ***************************************
skipping: [DEMO-albalad-DC-JD]
skipping: [DEMO-albalad-dev-JD]

TASK [End play if configured (Linux)] ******************************************
skipping: [DEMO-albalad-DC-JD]

TASK [End play if configured (Linux)] ******************************************
skipping: [DEMO-albalad-dev-JD]

TASK [Get network interface configuration (Windows)] ***************************
changed: [DEMO-albalad-dev-JD]
changed: [DEMO-albalad-DC-JD]

TASK [Output result] ***********************************************************
ok: [DEMO-albalad-DC-JD] => {
    "msg": "DHCP\r\n"
}
ok: [DEMO-albalad-dev-JD] => {
    "msg": "DHCP\r\n"
}

TASK [Get IP address of network interface (Windows)] ***************************
skipping: [DEMO-albalad-DC-JD]
skipping: [DEMO-albalad-dev-JD]

TASK [Show IP address] *********************************************************
skipping: [DEMO-albalad-DC-JD]
skipping: [DEMO-albalad-dev-JD]

TASK [Ending play for this host (Windows)] *************************************
skipping: [DEMO-albalad-DC-JD]
skipping: [DEMO-albalad-dev-JD]

TASK [End play if configured (Windows)] ****************************************
skipping: [DEMO-albalad-DC-JD]

TASK [End play if configured (Windows)] ****************************************
skipping: [DEMO-albalad-dev-JD]

TASK [Primary Method - Set up static IP address (Windows)] *********************
ok: [DEMO-albalad-dev-JD]
ok: [DEMO-albalad-DC-JD]

TASK [Set old_hardware fact (Windows)] *****************************************
ok: [DEMO-albalad-DC-JD]
ok: [DEMO-albalad-dev-JD]

TASK [Is fallback needed?] *****************************************************
ok: [DEMO-albalad-DC-JD] => {
    "msg": {
        "ansible_async_watchdog_pid": 3980,
        "ansible_job_id": "j577422154316.4912",
        "changed": false,
        "failed": false,
        "finished": 0,
        "results_file": "C:\\Users\\localuser\\.ansible_async\\j577422154316.4912",
        "started": 1
    }
}
ok: [DEMO-albalad-dev-JD] => {
    "msg": {
        "ansible_async_watchdog_pid": 3592,
        "ansible_job_id": "j110145606129.2616",
        "changed": false,
        "failed": false,
        "finished": 0,
        "results_file": "C:\\Users\\localuser\\.ansible_async\\j110145606129.2616",
        "started": 1
    }
}

TASK [Fallback - Create file with ip changes with netsh.exe] *******************
skipping: [DEMO-albalad-DC-JD]
skipping: [DEMO-albalad-dev-JD]

TASK [Fallback - Set registry key for script execution on next reboot] *********
skipping: [DEMO-albalad-DC-JD]
skipping: [DEMO-albalad-dev-JD]

TASK [Fallback - Set registry key for script execution on next reboot] *********
skipping: [DEMO-albalad-DC-JD]
skipping: [DEMO-albalad-dev-JD]

TASK [Fallback - Reboot the machine to apply static IP (Fallback Method)] ******
skipping: [DEMO-albalad-DC-JD]
skipping: [DEMO-albalad-dev-JD]

TASK [Change ansible's ip address for the host (Windows)] **********************
ok: [DEMO-albalad-DC-JD]
ok: [DEMO-albalad-dev-JD]

TASK [Wait for the host's network interface to come back up (Windows)] *********
ok: [DEMO-albalad-DC-JD -> localhost]
ok: [DEMO-albalad-dev-JD -> localhost]

TASK [Clean up static IP script after reboot] **********************************
skipping: [DEMO-albalad-DC-JD]
skipping: [DEMO-albalad-dev-JD]

TASK [Set DNS (Windows)] *******************************************************
changed: [DEMO-albalad-DC-JD]
changed: [DEMO-albalad-dev-JD]

TASK [Set DNS search domain (Windows)] *****************************************
changed: [DEMO-albalad-dev-JD]
changed: [DEMO-albalad-DC-JD]

TASK [Lookup the timezone string for Windows] **********************************
ok: [DEMO-albalad-DC-JD]
ok: [DEMO-albalad-dev-JD]

TASK [Fail this host if we can't find the timezone] ****************************
skipping: [DEMO-albalad-DC-JD]
skipping: [DEMO-albalad-dev-JD]

TASK [Set the timezone (Windows)] **********************************************
changed: [DEMO-albalad-DC-JD]
changed: [DEMO-albalad-dev-JD]

TASK [Hostname change (Windows)] ***********************************************
changed: [DEMO-albalad-DC-JD]
changed: [DEMO-albalad-dev-JD]

TASK [Reboot] ******************************************************************
changed: [DEMO-albalad-dev-JD]
changed: [DEMO-albalad-DC-JD]

TASK [Wait for the host's control interface (WinRM via HTTPS) to come up] ******
ok: [DEMO-albalad-DC-JD -> localhost]
ok: [DEMO-albalad-dev-JD -> localhost]

TASK [Install dbus for systemd hostname changes] *******************************
skipping: [DEMO-albalad-dev-JD]
skipping: [DEMO-albalad-DC-JD]

TASK [Install ifupdown to enable interfaces] ***********************************
skipping: [DEMO-albalad-DC-JD]
skipping: [DEMO-albalad-dev-JD]

TASK [Check if /etc/cloud exists and is a directory] ***************************
skipping: [DEMO-albalad-DC-JD]
skipping: [DEMO-albalad-dev-JD]

TASK [Ensure /etc/cloud/cloud-init.disabled exists to stop cloud-init from DHCPing the interface] ***
skipping: [DEMO-albalad-DC-JD]
skipping: [DEMO-albalad-dev-JD]

TASK [Check if /etc/netplan/00-installer-config.yaml exists] *******************
skipping: [DEMO-albalad-DC-JD]
skipping: [DEMO-albalad-dev-JD]

TASK [Delete /etc/netplan/00-installer-config.yaml] ****************************
skipping: [DEMO-albalad-DC-JD]
skipping: [DEMO-albalad-dev-JD]

TASK [Remove netplan cloud-init] ***********************************************
skipping: [DEMO-albalad-DC-JD]
skipping: [DEMO-albalad-dev-JD]

TASK [Check if /etc/cloud/cloud.cfg.d exists] **********************************
skipping: [DEMO-albalad-dev-JD]
skipping: [DEMO-albalad-DC-JD]

TASK [Disable cloud dhcp network] **********************************************
skipping: [DEMO-albalad-DC-JD]
skipping: [DEMO-albalad-dev-JD]

TASK [Set DNS search domain for systemd-resolved] ******************************
skipping: [DEMO-albalad-DC-JD]
skipping: [DEMO-albalad-dev-JD]

TASK [Set DNS server for systemd-resolved] *************************************
skipping: [DEMO-albalad-DC-JD]
skipping: [DEMO-albalad-dev-JD]

TASK [get MAC for vlan interface (Linux)] **************************************
skipping: [DEMO-albalad-dev-JD]
skipping: [DEMO-albalad-DC-JD]

TASK [Set the vlan_mac variable] ***********************************************
skipping: [DEMO-albalad-DC-JD]
skipping: [DEMO-albalad-dev-JD]

TASK [get interface for MAC of vlan interface (Linux)] *************************
skipping: [DEMO-albalad-DC-JD]
skipping: [DEMO-albalad-dev-JD]

TASK [Set the interface_name variable] *****************************************
skipping: [DEMO-albalad-DC-JD]
skipping: [DEMO-albalad-dev-JD]

TASK [Assert we found the interface name] **************************************
skipping: [DEMO-albalad-DC-JD]
skipping: [DEMO-albalad-dev-JD]

TASK [Set static IP from the template (Linux-Debian)] **************************
skipping: [DEMO-albalad-DC-JD]
skipping: [DEMO-albalad-dev-JD]

TASK [Set static IP from the template (Linux-RedHat/CentOS/Alma/Rocky)] ********
skipping: [DEMO-albalad-DC-JD]
skipping: [DEMO-albalad-dev-JD]

TASK [Check for "new" static IP files on (Linux-RedHat/CentOS/Alma/Rocky) > 8] ***
skipping: [DEMO-albalad-DC-JD]
skipping: [DEMO-albalad-dev-JD]

TASK [Remove "new" static IP file (Linux-RedHat/CentOS/Alma/Rocky) > 8] ********
skipping: [DEMO-albalad-DC-JD]
skipping: [DEMO-albalad-dev-JD]

TASK [Enable new interface (Linux)] ********************************************
skipping: [DEMO-albalad-DC-JD]
skipping: [DEMO-albalad-dev-JD]

TASK [Setting hostname (Linux)] ************************************************
skipping: [DEMO-albalad-DC-JD]
skipping: [DEMO-albalad-dev-JD]

TASK [Setting hostname (Linux-RedHat/CentOS/Alma/Rocky)] ***********************
skipping: [DEMO-albalad-DC-JD]
skipping: [DEMO-albalad-dev-JD]

TASK [Add IP address to /etc/hosts] ********************************************
skipping: [DEMO-albalad-DC-JD]
skipping: [DEMO-albalad-dev-JD]

TASK [Add hostname to /etc/hosts] **********************************************
skipping: [DEMO-albalad-DC-JD]
skipping: [DEMO-albalad-dev-JD]

TASK [Remove default entry for 127.0.0.1 from /etc/hosts] **********************
skipping: [DEMO-albalad-DC-JD]
skipping: [DEMO-albalad-dev-JD]

TASK [Set the timezone (Linux)] ************************************************
skipping: [DEMO-albalad-DC-JD]
skipping: [DEMO-albalad-dev-JD]

TASK [Reboot to set ip and hostname (Linux)] ***********************************
skipping: [DEMO-albalad-DC-JD]
skipping: [DEMO-albalad-dev-JD]

TASK [Change ansible's ip address for the host] ********************************
skipping: [DEMO-albalad-DC-JD]
skipping: [DEMO-albalad-dev-JD]

TASK [Wait for the host's control interface (SSH) to come up] ******************
skipping: [DEMO-albalad-DC-JD]
skipping: [DEMO-albalad-dev-JD]

TASK [Set up static IP address (macOS)] ****************************************
skipping: [DEMO-albalad-dev-JD]
skipping: [DEMO-albalad-DC-JD]

TASK [Change ansible's ip address for the host] ********************************
skipping: [DEMO-albalad-dev-JD]
skipping: [DEMO-albalad-DC-JD]

TASK [Wait for the host's control interface (SSH) to come up] ******************
skipping: [DEMO-albalad-DC-JD]
skipping: [DEMO-albalad-dev-JD]

TASK [Set DNS (macOS)] *********************************************************
skipping: [DEMO-albalad-DC-JD]
skipping: [DEMO-albalad-dev-JD]

TASK [Setting hostname (macOS)] ************************************************
skipping: [DEMO-albalad-DC-JD]
skipping: [DEMO-albalad-dev-JD]

TASK [Set the timezone (macOS)] ************************************************
skipping: [DEMO-albalad-DC-JD]
skipping: [DEMO-albalad-dev-JD]

TASK [Refresh inventory] *******************************************************

PLAY [Add all hosts to DNS on the router] **************************************

TASK [Gathering Facts] *********************************************************
ok: [JD-router-debian11-x64]

TASK [Add host to router DNS] **************************************************
included: /opt/ludus/ansible/range-management/tasks/router/add-host-to-router-dns.yml for JD-router-debian11-x64

TASK [Get current DNS rules] ***************************************************
ok: [JD-router-debian11-x64]

TASK [Delete all rewrite rules to start fresh] *********************************
skipping: [JD-router-debian11-x64]

TASK [Add IP address of all hosts for this range_id to DNS without range_id prefix] ***
ok: [JD-router-debian11-x64] => (item={'vm_name': 'DEMO-albalad-DC-JD', 'hostname': 'dc01', 'template': 'win2022-server-x64-template', 'vlan': 10, 'ip_last_octet': 11, 'ram_gb': 8, 'cpus': 4, 'windows': {'sysprep': True}, 'domain': {'fqdn': 'albalad.bsides.rv', 'role': 'primary-dc'}})
ok: [JD-router-debian11-x64] => (item={'vm_name': 'DEMO-albalad-dev-JD', 'hostname': 'dev03', 'template': 'win2022-server-x64-template', 'vlan': 10, 'ip_last_octet': 12, 'ram_gb': 6, 'cpus': 4, 'windows': {'sysprep': True}, 'domain': {'fqdn': 'albalad.bsides.rv', 'role': 'member'}})

TASK [Add IP address of all hosts for this range_id to DNS with range_id prefix] ***
ok: [JD-router-debian11-x64] => (item={'vm_name': 'DEMO-albalad-DC-JD', 'hostname': 'dc01', 'template': 'win2022-server-x64-template', 'vlan': 10, 'ip_last_octet': 11, 'ram_gb': 8, 'cpus': 4, 'windows': {'sysprep': True}, 'domain': {'fqdn': 'albalad.bsides.rv', 'role': 'primary-dc'}})
ok: [JD-router-debian11-x64] => (item={'vm_name': 'DEMO-albalad-dev-JD', 'hostname': 'dev03', 'template': 'win2022-server-x64-template', 'vlan': 10, 'ip_last_octet': 12, 'ram_gb': 6, 'cpus': 4, 'windows': {'sysprep': True}, 'domain': {'fqdn': 'albalad.bsides.rv', 'role': 'member'}})

TASK [Add IP address of all hosts for this range_id to DNS without range_id prefix and with home.arpa] ***
ok: [JD-router-debian11-x64] => (item={'vm_name': 'DEMO-albalad-DC-JD', 'hostname': 'dc01', 'template': 'win2022-server-x64-template', 'vlan': 10, 'ip_last_octet': 11, 'ram_gb': 8, 'cpus': 4, 'windows': {'sysprep': True}, 'domain': {'fqdn': 'albalad.bsides.rv', 'role': 'primary-dc'}})
ok: [JD-router-debian11-x64] => (item={'vm_name': 'DEMO-albalad-dev-JD', 'hostname': 'dev03', 'template': 'win2022-server-x64-template', 'vlan': 10, 'ip_last_octet': 12, 'ram_gb': 6, 'cpus': 4, 'windows': {'sysprep': True}, 'domain': {'fqdn': 'albalad.bsides.rv', 'role': 'member'}})

TASK [Add IP address of all hosts for this range_id to DNS with range_id prefix and with home.arpa] ***
ok: [JD-router-debian11-x64] => (item={'vm_name': 'DEMO-albalad-DC-JD', 'hostname': 'dc01', 'template': 'win2022-server-x64-template', 'vlan': 10, 'ip_last_octet': 11, 'ram_gb': 8, 'cpus': 4, 'windows': {'sysprep': True}, 'domain': {'fqdn': 'albalad.bsides.rv', 'role': 'primary-dc'}})
ok: [JD-router-debian11-x64] => (item={'vm_name': 'DEMO-albalad-dev-JD', 'hostname': 'dev03', 'template': 'win2022-server-x64-template', 'vlan': 10, 'ip_last_octet': 12, 'ram_gb': 6, 'cpus': 4, 'windows': {'sysprep': True}, 'domain': {'fqdn': 'albalad.bsides.rv', 'role': 'member'}})

PLAY [Collect VMs with rewrite rules] ******************************************

TASK [Collect VMs with rewrite rules] ******************************************
skipping: [localhost] => (item={'vm_name': 'DEMO-albalad-DC-JD', 'hostname': 'dc01', 'template': 'win2022-server-x64-template', 'vlan': 10, 'ip_last_octet': 11, 'ram_gb': 8, 'cpus': 4, 'windows': {'sysprep': True}, 'domain': {'fqdn': 'albalad.bsides.rv', 'role': 'primary-dc'}})
skipping: [localhost] => (item={'vm_name': 'DEMO-albalad-dev-JD', 'hostname': 'dev03', 'template': 'win2022-server-x64-template', 'vlan': 10, 'ip_last_octet': 12, 'ram_gb': 6, 'cpus': 4, 'windows': {'sysprep': True}, 'domain': {'fqdn': 'albalad.bsides.rv', 'role': 'member'}})
skipping: [localhost]

PLAY [Add custom DNS rewrite rules] ********************************************

TASK [Gathering Facts] *********************************************************
ok: [JD-router-debian11-x64]

TASK [Add user-defined rewrites to the router] *********************************
skipping: [JD-router-debian11-x64]

PLAY [Collect Windows VMs to sysprep] ******************************************

TASK [Collect Windows VMs to sysprep] ******************************************
ok: [localhost] => (item={'vm_name': 'DEMO-albalad-DC-JD', 'hostname': 'dc01', 'template': 'win2022-server-x64-template', 'vlan': 10, 'ip_last_octet': 11, 'ram_gb': 8, 'cpus': 4, 'windows': {'sysprep': True}, 'domain': {'fqdn': 'albalad.bsides.rv', 'role': 'primary-dc'}})
ok: [localhost] => (item={'vm_name': 'DEMO-albalad-dev-JD', 'hostname': 'dev03', 'template': 'win2022-server-x64-template', 'vlan': 10, 'ip_last_octet': 12, 'ram_gb': 6, 'cpus': 4, 'windows': {'sysprep': True}, 'domain': {'fqdn': 'albalad.bsides.rv', 'role': 'member'}})

PLAY [Sysprep Windows VMs] *****************************************************

TASK [Gathering Facts] *********************************************************
ok: [DEMO-albalad-dev-JD]
ok: [DEMO-albalad-DC-JD]

TASK [Sysprep a VM] ************************************************************
included: /opt/ludus/ansible/range-management/tasks/windows/sysprep.yml for DEMO-albalad-DC-JD, DEMO-albalad-dev-JD

TASK [Check if sysprepd file exists] *******************************************
ok: [DEMO-albalad-dev-JD]
ok: [DEMO-albalad-DC-JD]

TASK [Skip tasks if sysprepd file exists] **************************************
skipping: [DEMO-albalad-DC-JD]

TASK [Skip tasks if sysprepd file exists] **************************************
skipping: [DEMO-albalad-dev-JD]

TASK [Create C:\Windows\Setup\Scripts directory] *******************************
changed: [DEMO-albalad-DC-JD]
changed: [DEMO-albalad-dev-JD]

TASK [Copy SetupComplete.cmd to C:\Windows\Setup\Scripts] **********************
changed: [DEMO-albalad-dev-JD]
changed: [DEMO-albalad-DC-JD]

TASK [Create C:\ludus\sysprep directory] ***************************************
changed: [DEMO-albalad-dev-JD]
changed: [DEMO-albalad-DC-JD]

TASK [Copy oob-disable.xml to C:\ludus\sysprep] ********************************
changed: [DEMO-albalad-dev-JD]
changed: [DEMO-albalad-DC-JD]

TASK [Run Sysprep] *************************************************************
changed: [DEMO-albalad-DC-JD]
changed: [DEMO-albalad-dev-JD]

TASK [Wait for 60 seconds for sysprep to finish] *******************************
Pausing for 60 seconds
ok: [DEMO-albalad-DC-JD]

TASK [Wait for WinRM] **********************************************************
ok: [DEMO-albalad-DC-JD -> localhost]
ok: [DEMO-albalad-dev-JD -> localhost]

TASK [Wait for 60 seconds for the second reboot] *******************************
Pausing for 60 seconds
ok: [DEMO-albalad-DC-JD]

TASK [Wait for WinRM] **********************************************************
ok: [DEMO-albalad-dev-JD -> localhost]
ok: [DEMO-albalad-DC-JD -> localhost]

TASK [Create sysprepd file] ****************************************************
fatal: [DEMO-albalad-dev-JD]: UNREACHABLE! => {"changed": false, "msg": "ssl: The device is not ready.  (extended fault data: {'transport_message': 'Bad HTTP response returned from server. Code 500', 'http_status_code': 500, 'wsmanfault_code': 2147942421, 'fault_code': 's:Receiver', 'fault_subcode': 'w:InternalError'})", "unreachable": true}
fatal: [DEMO-albalad-DC-JD]: UNREACHABLE! => {"changed": false, "msg": "ssl: The device is not ready.  (extended fault data: {'transport_message': 'Bad HTTP response returned from server. Code 500', 'http_status_code': 500, 'wsmanfault_code': 2147942421, 'fault_code': 's:Receiver', 'fault_subcode': 'w:InternalError'})", "unreachable": true}

PLAY RECAP *********************************************************************
DEMO-albalad-DC-JD         : ok=28   changed=11   unreachable=1    failed=0    skipped=47   rescued=0    ignored=0
DEMO-albalad-dev-JD        : ok=26   changed=11   unreachable=1    failed=0    skipped=47   rescued=0    ignored=0
JD-router-debian11-x64     : ok=69   changed=44   unreachable=0    failed=0    skipped=57   rescued=0    ignored=0
localhost                  : ok=70   changed=26   unreachable=0    failed=0    skipped=11   rescued=0    ignored=0

^C
root@ludus:/mnt/hgfs/sharedfolderfortheludus/RangeVillage-Demo-main/BSidesAmman-2025# ludus range status
+---------+---------------+------------------+---------------+-------------------+-----------------+
| USER ID | RANGE NETWORK | LAST DEPLOYMENT  | NUMBER OF VMS | DEPLOYMENT STATUS | TESTING ENABLED |
+---------+---------------+------------------+---------------+-------------------+-----------------+
|   JD    |  10.2.0.0/16  | 2025-04-29 17:42 |       3       |       ERROR       |      FALSE      |
+---------+---------------+------------------+---------------+-------------------+-----------------+
+------------+------------------------+-------+-------------+
| PROXMOX ID |        VM NAME         | POWER |     IP      |
+------------+------------------------+-------+-------------+
|    105     | JD-router-debian11-x64 |  On   | 10.2.10.254 |
|    106     | DEMO-albalad-DC-JD     |  On   | 10.2.10.11  |
|    107     | DEMO-albalad-dev-JD    |  On   | 10.2.10.12  |
+------------+------------------------+-------+-------------+
root@ludus:/mnt/hgfs/sharedfolderfortheludus/RangeVillage-Demo-main/BSidesAmman-2025# ludus range status
+---------+---------------+------------------+---------------+-------------------+-----------------+
| USER ID | RANGE NETWORK | LAST DEPLOYMENT  | NUMBER OF VMS | DEPLOYMENT STATUS | TESTING ENABLED |
+---------+---------------+------------------+---------------+-------------------+-----------------+
|   JD    |  10.2.0.0/16  | 2025-04-29 17:42 |       3       |       ERROR       |      FALSE      |
+---------+---------------+------------------+---------------+-------------------+-----------------+
+------------+------------------------+-------+-------------+
| PROXMOX ID |        VM NAME         | POWER |     IP      |
+------------+------------------------+-------+-------------+
|    105     | JD-router-debian11-x64 |  On   | 10.2.10.254 |
|    106     | DEMO-albalad-DC-JD     |  On   | 10.2.10.11  |
|    107     | DEMO-albalad-dev-JD    |  On   | 10.2.10.12  |
+------------+------------------------+-------+-------------+
root@ludus:/mnt/hgfs/sharedfolderfortheludus/RangeVillage-Demo-main/BSidesAmman-2025# ludus range logs -f
[WARNING]: provided hosts list is empty, only localhost is available. Note that
the implicit localhost does not match 'all'

PLAY [Pre run checks] **********************************************************

TASK [Acquire session ticket] **************************************************
ok: [localhost]

TASK [Extract ticket from response] ********************************************
ok: [localhost]

TASK [Check for valid dynamic inventory] ***************************************
ok: [localhost] => {
    "changed": false,
    "msg": "Dynamic inventory loaded!"
}

PLAY [Deploy the router VM] ****************************************************

TASK [Gathering Facts] *********************************************************
ok: [localhost]

TASK [Deploy router VM] ********************************************************
included: /opt/ludus/ansible/range-management/tasks/proxmox/deploy-vm.yml for localhost

TASK [Create a VM from a template] *********************************************
changed: [localhost]

TASK [Pause for 5 seconds to allow the vmid to populate] ***********************
Pausing for 5 seconds
ok: [localhost]

TASK [Set the vm_id] ***********************************************************
ok: [localhost]

TASK [Update the VM description by vmid] ***************************************
changed: [localhost]

TASK [Update the VM description by name (take 1)] ******************************
skipping: [localhost]

TASK [Update the VM's options] *************************************************
changed: [localhost]

TASK [Update the VM network interfaces] ****************************************
changed: [localhost]

TASK [Start the VM] ************************************************************
changed: [localhost]

TASK [Check VM running status] *************************************************
ok: [localhost]

TASK [Wait for VM to acquire an IP address] ************************************
FAILED - RETRYING: [localhost]: Wait for VM to acquire an IP address (30 retries left).
FAILED - RETRYING: [localhost]: Wait for VM to acquire an IP address (29 retries left).
ok: [localhost]

TASK [Save off the IP for use with checking on the WinRM/SSH connectivity] *****
ok: [localhost]

TASK [Refresh inventory if needed] *********************************************
included: /opt/ludus/ansible/range-management/tasks/proxmox/refresh_inventory.yml for localhost

TASK [Refresh inventory] *******************************************************

TASK [Show last_deployed_ip] ***************************************************
ok: [localhost] => {
    "last_deployed_ip": "192.0.2.72"
}

TASK [Wait for the host's control interface (WinRM via HTTPS) to come up] ******
skipping: [localhost]

TASK [Wait for the host's control interface (SSH) to come up] ******************
ok: [localhost]

PLAY [Configure the router] ****************************************************

TASK [Gathering Facts] *********************************************************
ok: [JD-router-debian11-x64]

TASK [Check if the .ludus-configured file exists] ******************************
ok: [JD-router-debian11-x64]

TASK [End play if configured] **************************************************
skipping: [JD-router-debian11-x64]

TASK [Configure IP and Hostname] ***********************************************
included: /opt/ludus/ansible/range-management/tasks/proxmox/configure-ip-and-hostname.yml for JD-router-debian11-x64

TASK [Check if the IP has been statically set correctly (Linux)] ***************
changed: [JD-router-debian11-x64]

TASK [Ending play for this host (Linux)] ***************************************
skipping: [JD-router-debian11-x64]

TASK [End play if configured (Linux)] ******************************************
skipping: [JD-router-debian11-x64]

TASK [Get network interface configuration (Windows)] ***************************
skipping: [JD-router-debian11-x64]

TASK [Output result] ***********************************************************
skipping: [JD-router-debian11-x64]

TASK [Get IP address of network interface (Windows)] ***************************
skipping: [JD-router-debian11-x64]

TASK [Show IP address] *********************************************************
skipping: [JD-router-debian11-x64]

TASK [Ending play for this host (Windows)] *************************************
skipping: [JD-router-debian11-x64]

TASK [End play if configured (Windows)] ****************************************
skipping: [JD-router-debian11-x64]

TASK [Primary Method - Set up static IP address (Windows)] *********************
skipping: [JD-router-debian11-x64]

TASK [Set old_hardware fact (Windows)] *****************************************
skipping: [JD-router-debian11-x64]

TASK [Is fallback needed?] *****************************************************
skipping: [JD-router-debian11-x64]

TASK [Fallback - Create file with ip changes with netsh.exe] *******************
skipping: [JD-router-debian11-x64]

TASK [Fallback - Set registry key for script execution on next reboot] *********
skipping: [JD-router-debian11-x64]

TASK [Fallback - Set registry key for script execution on next reboot] *********
skipping: [JD-router-debian11-x64]

TASK [Fallback - Reboot the machine to apply static IP (Fallback Method)] ******
skipping: [JD-router-debian11-x64]

TASK [Change ansible's ip address for the host (Windows)] **********************
skipping: [JD-router-debian11-x64]

TASK [Wait for the host's network interface to come back up (Windows)] *********
skipping: [JD-router-debian11-x64]

TASK [Clean up static IP script after reboot] **********************************
skipping: [JD-router-debian11-x64]

TASK [Set DNS (Windows)] *******************************************************
skipping: [JD-router-debian11-x64]

TASK [Set DNS search domain (Windows)] *****************************************
skipping: [JD-router-debian11-x64]

TASK [Lookup the timezone string for Windows] **********************************
skipping: [JD-router-debian11-x64]

TASK [Fail this host if we can't find the timezone] ****************************
skipping: [JD-router-debian11-x64]

TASK [Set the timezone (Windows)] **********************************************
skipping: [JD-router-debian11-x64]

TASK [Hostname change (Windows)] ***********************************************
skipping: [JD-router-debian11-x64]

TASK [Reboot] ******************************************************************
skipping: [JD-router-debian11-x64]

TASK [Wait for the host's control interface (WinRM via HTTPS) to come up] ******
skipping: [JD-router-debian11-x64]

TASK [Install dbus for systemd hostname changes] *******************************
changed: [JD-router-debian11-x64]

TASK [Install ifupdown to enable interfaces] ***********************************
skipping: [JD-router-debian11-x64]

TASK [Check if /etc/cloud exists and is a directory] ***************************
skipping: [JD-router-debian11-x64]

TASK [Ensure /etc/cloud/cloud-init.disabled exists to stop cloud-init from DHCPing the interface] ***
skipping: [JD-router-debian11-x64]

TASK [Check if /etc/netplan/00-installer-config.yaml exists] *******************
skipping: [JD-router-debian11-x64]

TASK [Delete /etc/netplan/00-installer-config.yaml] ****************************
skipping: [JD-router-debian11-x64]

TASK [Remove netplan cloud-init] ***********************************************
skipping: [JD-router-debian11-x64]

TASK [Check if /etc/cloud/cloud.cfg.d exists] **********************************
skipping: [JD-router-debian11-x64]

TASK [Disable cloud dhcp network] **********************************************
skipping: [JD-router-debian11-x64]

TASK [Set DNS search domain for systemd-resolved] ******************************
skipping: [JD-router-debian11-x64]

TASK [Set DNS server for systemd-resolved] *************************************
skipping: [JD-router-debian11-x64]

TASK [get MAC for vlan interface (Linux)] **************************************
changed: [JD-router-debian11-x64 -> localhost]

TASK [Set the vlan_mac variable] ***********************************************
ok: [JD-router-debian11-x64]

TASK [get interface for MAC of vlan interface (Linux)] *************************
changed: [JD-router-debian11-x64 -> localhost]

TASK [Set the interface_name variable] *****************************************
ok: [JD-router-debian11-x64]

TASK [Assert we found the interface name] **************************************
ok: [JD-router-debian11-x64] => {
    "changed": false,
    "msg": "Successfully found the interface name for VM 105"
}

TASK [Set static IP from the template (Linux-Debian)] **************************
changed: [JD-router-debian11-x64]

TASK [Set static IP from the template (Linux-RedHat/CentOS/Alma/Rocky)] ********
skipping: [JD-router-debian11-x64]

TASK [Check for "new" static IP files on (Linux-RedHat/CentOS/Alma/Rocky) > 8] ***
skipping: [JD-router-debian11-x64]

TASK [Remove "new" static IP file (Linux-RedHat/CentOS/Alma/Rocky) > 8] ********
skipping: [JD-router-debian11-x64]

TASK [Enable new interface (Linux)] ********************************************
changed: [JD-router-debian11-x64]

TASK [Setting hostname (Linux)] ************************************************
changed: [JD-router-debian11-x64]

TASK [Setting hostname (Linux-RedHat/CentOS/Alma/Rocky)] ***********************
skipping: [JD-router-debian11-x64]

TASK [Add IP address to /etc/hosts] ********************************************
changed: [JD-router-debian11-x64]

TASK [Add hostname to /etc/hosts] **********************************************
changed: [JD-router-debian11-x64]

TASK [Remove default entry for 127.0.0.1 from /etc/hosts] **********************
changed: [JD-router-debian11-x64]

TASK [Set the timezone (Linux)] ************************************************
changed: [JD-router-debian11-x64]

TASK [Reboot to set ip and hostname (Linux)] ***********************************
changed: [JD-router-debian11-x64]

TASK [Change ansible's ip address for the host] ********************************
ok: [JD-router-debian11-x64]

TASK [Wait for the host's control interface (SSH) to come up] ******************
ok: [JD-router-debian11-x64 -> localhost]

TASK [Set up static IP address (macOS)] ****************************************
skipping: [JD-router-debian11-x64]

TASK [Change ansible's ip address for the host] ********************************
skipping: [JD-router-debian11-x64]

TASK [Wait for the host's control interface (SSH) to come up] ******************
skipping: [JD-router-debian11-x64]

TASK [Set DNS (macOS)] *********************************************************
skipping: [JD-router-debian11-x64]

TASK [Setting hostname (macOS)] ************************************************
skipping: [JD-router-debian11-x64]

TASK [Set the timezone (macOS)] ************************************************
skipping: [JD-router-debian11-x64]

TASK [Refresh inventory] *******************************************************

TASK [Configure router] ********************************************************
included: /opt/ludus/ansible/range-management/tasks/router/configure-router.yml for JD-router-debian11-x64

TASK [Setup ip forwarding on the router] ***************************************
changed: [JD-router-debian11-x64]

TASK [Disable ipv6] ************************************************************
changed: [JD-router-debian11-x64]

TASK [Install dnsmasq, ca-certificates, and iptables-persistent] ***************
changed: [JD-router-debian11-x64]

TASK [Disable DNS in dnsmasq (only use it for DHCP)] ***************************
changed: [JD-router-debian11-x64]

TASK [Restart dnsmasq service to pick up changes] ******************************
changed: [JD-router-debian11-x64]

TASK [Install AdGuardHome] *****************************************************
changed: [JD-router-debian11-x64]

TASK [Configure AdGuardHome] ***************************************************
changed: [JD-router-debian11-x64]

TASK [Restart AdGuardHome to take config] **************************************
changed: [JD-router-debian11-x64]

TASK [Drop a file to signal that we have completed configuration] **************
changed: [JD-router-debian11-x64]

PLAY [Setup VLANs] *************************************************************

TASK [Gathering Facts] *********************************************************
ok: [localhost]

TASK [Collect VLANs] ***********************************************************
ok: [localhost] => (item={'vm_name': 'DEMO-albalad-DC-JD', 'hostname': 'dc01', 'template': 'win2022-server-x64-template', 'vlan': 10, 'ip_last_octet': 11, 'ram_gb': 8, 'cpus': 4, 'windows': {'sysprep': True}, 'domain': {'fqdn': 'albalad.bsides.rv', 'role': 'primary-dc'}})
ok: [localhost] => (item={'vm_name': 'DEMO-albalad-dev-JD', 'hostname': 'dev03', 'template': 'win2022-server-x64-template', 'vlan': 10, 'ip_last_octet': 12, 'ram_gb': 6, 'cpus': 4, 'windows': {'sysprep': True}, 'domain': {'fqdn': 'albalad.bsides.rv', 'role': 'member'}})

TASK [Add all VLAN interfaces to the router] ***********************************
included: /opt/ludus/ansible/range-management/tasks/router/add-vlan-to-router.yml for localhost => (item=10)

TASK [Get the VM id of the router via Proxmox API] *****************************
changed: [localhost]

TASK [Set the router_vm_id from API lookup] ************************************
ok: [localhost]

TASK [Get MAC for vlan interface] **********************************************
changed: [localhost]

TASK [Show vlan_mac_command] ***************************************************
ok: [localhost] => {
    "msg": ""
}

TASK [Set the vlan_mac variable] ***********************************************
skipping: [localhost]

TASK [Show VLAN MAC] ***********************************************************
skipping: [localhost]

TASK [Get interface for MAC of vlan interface] *********************************
skipping: [localhost]

TASK [Set the interface_name_command variable] *********************************
skipping: [localhost]

TASK [Get the number for the next network interface (starts at 0)] *************
changed: [localhost]

TASK [Set the rotuer_net_interface variable] ***********************************
ok: [localhost]

TASK [Add network interface to router] *****************************************
changed: [localhost]

TASK [Get MAC for vlan interface] **********************************************
changed: [localhost]

TASK [Set the vlan_mac variable] ***********************************************
ok: [localhost]

TASK [Get interface for MAC of vlan interface] *********************************
changed: [localhost]

TASK [Set the interface_name_command variable] *********************************
ok: [localhost]

TASK [Get the interface with a 192.0.2.x ip (WAN)] *****************************
changed: [localhost]

TASK [Set the router_external_interface variable] ******************************
ok: [localhost]

TASK [Set up the IP configuration for the new interface] ***********************
changed: [localhost -> JD-router-debian11-x64(192.0.2.102)]

TASK [Enable new interface] ****************************************************
changed: [localhost -> JD-router-debian11-x64(192.0.2.102)]

TASK [Configure dnsmasq (part 1) - setup base config] **************************
changed: [localhost -> JD-router-debian11-x64(192.0.2.102)]

TASK [Configure dnsmasq (part 2) - enable and restart service] *****************
changed: [localhost -> JD-router-debian11-x64(192.0.2.102)]

PLAY [Apply all user defined network rules to the router] **********************

TASK [Gathering Facts] *********************************************************
ok: [JD-router-debian11-x64]

TASK [Set any user defined firewall rules] *************************************
included: /opt/ludus/ansible/range-management/tasks/firewall/set-firewall-rules.yml for JD-router-debian11-x64

TASK [Set the policy for the FORWARD chain to DROP] ****************************
changed: [JD-router-debian11-x64]

TASK [Create the LUDUS_DEFAULTS chain] *****************************************
changed: [JD-router-debian11-x64]

TASK [Create the LUDUS_USER_RULES chain] ***************************************
changed: [JD-router-debian11-x64]

TASK [Create the LUDUS_TESTING chain] ******************************************
changed: [JD-router-debian11-x64]

TASK [Flush the LUDUS_USER_RULES table to remove any user defined rules to prevent old rules from lingering] ***
changed: [JD-router-debian11-x64]

TASK [Flush the LUDUS_DEFAULTS table to remove any user defined rules to prevent old rules from lingering] ***
changed: [JD-router-debian11-x64]

TASK [Flush the INPUT to prevent locking ourselves out during rule setup] ******
changed: [JD-router-debian11-x64]

TASK [Get the VM id of the router via Proxmox API] *****************************
changed: [JD-router-debian11-x64 -> localhost]

TASK [Set the router_vm_id from API lookup] ************************************
ok: [JD-router-debian11-x64]

TASK [Get the interface with a 192.0.2.x ip (WAN)] *****************************
changed: [JD-router-debian11-x64 -> localhost]

TASK [Set the router_external_interface variable] ******************************
ok: [JD-router-debian11-x64]

TASK [Deny all other traffic from the external interface] **********************
changed: [JD-router-debian11-x64]

TASK [Allow the user's WireGuard IP to hit this router from the outside] *******
changed: [JD-router-debian11-x64]

TASK [Set range_access_grants_array from access_grants_array] ******************
ok: [JD-router-debian11-x64]

TASK [Modify router firewall to allow WireGuard IP's for access grants to this range] ***
skipping: [JD-router-debian11-x64]

TASK [Set the default WireGuard subnet rule] ***********************************
changed: [JD-router-debian11-x64]

TASK [Set the default allow related/established out to the user's WireGuard IP] ***
changed: [JD-router-debian11-x64]

TASK [Set the default external rule] *******************************************
changed: [JD-router-debian11-x64]

TASK [Set the default inter-VLAN rule] *****************************************
changed: [JD-router-debian11-x64]

TASK [Jump all traffic from FORWARD to LUDUS_DEFAULTS] *************************
changed: [JD-router-debian11-x64]

TASK [Jump all traffic from FORWARD to LUDUS_TESTING] **************************
changed: [JD-router-debian11-x64]

TASK [Jump all traffic from FORWARD to LUDUS_USER_RULES] ***********************
changed: [JD-router-debian11-x64]

TASK [Deny all range traffic to SSH on this router] ****************************
changed: [JD-router-debian11-x64]

TASK [Jump all traffic from INPUT to LUDUS_DEFAULTS] ***************************
changed: [JD-router-debian11-x64]

TASK [Loop over each user defined rule] ****************************************
skipping: [JD-router-debian11-x64]

TASK [Deny all range traffic to user defined "always_blocked_networks"] ********
skipping: [JD-router-debian11-x64]

TASK [Allow the Ludus IP to hit this router from the outside for ansible] ******
changed: [JD-router-debian11-x64]

TASK [Reset the conntrack entries to prevent previously allowed traffic to continue] ***
ASYNC OK on JD-router-debian11-x64: jid=j991921658474.4204
changed: [JD-router-debian11-x64]

TASK [Save current state of the firewall to a file] ****************************
changed: [JD-router-debian11-x64]

PLAY [Apply all user defined roles to the router (Enterprise)] *****************

TASK [Gathering Facts] *********************************************************
ok: [JD-router-debian11-x64]

TASK [Check for enterprise license] ********************************************
skipping: [JD-router-debian11-x64]

TASK [Set any user defined firewall rules] *************************************
skipping: [JD-router-debian11-x64]

PLAY [Apply outbound WireGuard to the router (Enterprise)] *********************

TASK [Gathering Facts] *********************************************************
ok: [JD-router-debian11-x64]

TASK [Check for enterprise license] ********************************************
skipping: [JD-router-debian11-x64]

TASK [Clear any outbound WireGuard related configurations] *********************
skipping: [JD-router-debian11-x64]

TASK [Setup outbound WireGuard on the router] **********************************
skipping: [JD-router-debian11-x64]

PLAY [Apply inbound WireGuard to the router (Enterprise)] **********************

TASK [Gathering Facts] *********************************************************
ok: [JD-router-debian11-x64]

TASK [Check for enterprise license] ********************************************
skipping: [JD-router-debian11-x64]

TASK [Clear any inbound WireGuard related configurations] **********************
skipping: [JD-router-debian11-x64]

TASK [Setup inbound WireGuard on the router] ***********************************
skipping: [JD-router-debian11-x64]

PLAY [Deploy DC VMs] ***********************************************************

TASK [Gathering Facts] *********************************************************
ok: [localhost]

TASK [Deploy VM] ***************************************************************
skipping: [localhost] => (item={'vm_name': 'DEMO-albalad-dev-JD', 'hostname': 'dev03', 'template': 'win2022-server-x64-template', 'vlan': 10, 'ip_last_octet': 12, 'ram_gb': 6, 'cpus': 4, 'windows': {'sysprep': True}, 'domain': {'fqdn': 'albalad.bsides.rv', 'role': 'member'}})
included: /opt/ludus/ansible/range-management/tasks/proxmox/deploy-vm.yml for localhost => (item={'vm_name': 'DEMO-albalad-DC-JD', 'hostname': 'dc01', 'template': 'win2022-server-x64-template', 'vlan': 10, 'ip_last_octet': 11, 'ram_gb': 8, 'cpus': 4, 'windows': {'sysprep': True}, 'domain': {'fqdn': 'albalad.bsides.rv', 'role': 'primary-dc'}})

TASK [Create a VM from a template] *********************************************
changed: [localhost]

TASK [Pause for 5 seconds to allow the vmid to populate] ***********************
Pausing for 5 seconds
ok: [localhost]

TASK [Set the vm_id] ***********************************************************
ok: [localhost]

TASK [Update the VM description by vmid] ***************************************
changed: [localhost]

TASK [Update the VM description by name (take 1)] ******************************
skipping: [localhost]

TASK [Update the VM's options] *************************************************
changed: [localhost]

TASK [Update the VM network interfaces] ****************************************
changed: [localhost]

TASK [Start the VM] ************************************************************
changed: [localhost]

TASK [Check VM running status] *************************************************
ok: [localhost]

TASK [Wait for VM to acquire an IP address] ************************************
FAILED - RETRYING: [localhost]: Wait for VM to acquire an IP address (30 retries left).
FAILED - RETRYING: [localhost]: Wait for VM to acquire an IP address (29 retries left).
FAILED - RETRYING: [localhost]: Wait for VM to acquire an IP address (28 retries left).
FAILED - RETRYING: [localhost]: Wait for VM to acquire an IP address (27 retries left).
FAILED - RETRYING: [localhost]: Wait for VM to acquire an IP address (26 retries left).
FAILED - RETRYING: [localhost]: Wait for VM to acquire an IP address (25 retries left).
FAILED - RETRYING: [localhost]: Wait for VM to acquire an IP address (24 retries left).
FAILED - RETRYING: [localhost]: Wait for VM to acquire an IP address (23 retries left).
FAILED - RETRYING: [localhost]: Wait for VM to acquire an IP address (22 retries left).
FAILED - RETRYING: [localhost]: Wait for VM to acquire an IP address (21 retries left).
ok: [localhost]

TASK [Save off the IP for use with checking on the WinRM/SSH connectivity] *****
ok: [localhost]

TASK [Refresh inventory if needed] *********************************************
included: /opt/ludus/ansible/range-management/tasks/proxmox/refresh_inventory.yml for localhost

TASK [Refresh inventory] *******************************************************

TASK [Show last_deployed_ip] ***************************************************
ok: [localhost] => {
    "last_deployed_ip": "10.2.10.243"
}

TASK [Wait for the host's control interface (WinRM via HTTPS) to come up] ******
ok: [localhost]

TASK [Wait for the host's control interface (SSH) to come up] ******************
skipping: [localhost]

PLAY [Deploy non-DC VMs] *******************************************************

TASK [Gathering Facts] *********************************************************
ok: [localhost]

TASK [Deploy VM] ***************************************************************
skipping: [localhost] => (item={'vm_name': 'DEMO-albalad-DC-JD', 'hostname': 'dc01', 'template': 'win2022-server-x64-template', 'vlan': 10, 'ip_last_octet': 11, 'ram_gb': 8, 'cpus': 4, 'windows': {'sysprep': True}, 'domain': {'fqdn': 'albalad.bsides.rv', 'role': 'primary-dc'}})
included: /opt/ludus/ansible/range-management/tasks/proxmox/deploy-vm.yml for localhost => (item={'vm_name': 'DEMO-albalad-dev-JD', 'hostname': 'dev03', 'template': 'win2022-server-x64-template', 'vlan': 10, 'ip_last_octet': 12, 'ram_gb': 6, 'cpus': 4, 'windows': {'sysprep': True}, 'domain': {'fqdn': 'albalad.bsides.rv', 'role': 'member'}})

TASK [Create a VM from a template] *********************************************
changed: [localhost]

TASK [Pause for 5 seconds to allow the vmid to populate] ***********************
Pausing for 5 seconds
ok: [localhost]

TASK [Set the vm_id] ***********************************************************
ok: [localhost]

TASK [Update the VM description by vmid] ***************************************
changed: [localhost]

TASK [Update the VM description by name (take 1)] ******************************
skipping: [localhost]

TASK [Update the VM's options] *************************************************
changed: [localhost]

TASK [Update the VM network interfaces] ****************************************
changed: [localhost]

TASK [Start the VM] ************************************************************
changed: [localhost]

TASK [Check VM running status] *************************************************
ok: [localhost]

TASK [Wait for VM to acquire an IP address] ************************************
FAILED - RETRYING: [localhost]: Wait for VM to acquire an IP address (30 retries left).
FAILED - RETRYING: [localhost]: Wait for VM to acquire an IP address (29 retries left).
FAILED - RETRYING: [localhost]: Wait for VM to acquire an IP address (28 retries left).
FAILED - RETRYING: [localhost]: Wait for VM to acquire an IP address (27 retries left).
FAILED - RETRYING: [localhost]: Wait for VM to acquire an IP address (26 retries left).
FAILED - RETRYING: [localhost]: Wait for VM to acquire an IP address (25 retries left).
FAILED - RETRYING: [localhost]: Wait for VM to acquire an IP address (24 retries left).
FAILED - RETRYING: [localhost]: Wait for VM to acquire an IP address (23 retries left).
FAILED - RETRYING: [localhost]: Wait for VM to acquire an IP address (22 retries left).
FAILED - RETRYING: [localhost]: Wait for VM to acquire an IP address (21 retries left).
FAILED - RETRYING: [localhost]: Wait for VM to acquire an IP address (20 retries left).
FAILED - RETRYING: [localhost]: Wait for VM to acquire an IP address (19 retries left).
FAILED - RETRYING: [localhost]: Wait for VM to acquire an IP address (18 retries left).
FAILED - RETRYING: [localhost]: Wait for VM to acquire an IP address (17 retries left).
FAILED - RETRYING: [localhost]: Wait for VM to acquire an IP address (16 retries left).
FAILED - RETRYING: [localhost]: Wait for VM to acquire an IP address (15 retries left).
FAILED - RETRYING: [localhost]: Wait for VM to acquire an IP address (14 retries left).
ok: [localhost]

TASK [Save off the IP for use with checking on the WinRM/SSH connectivity] *****
ok: [localhost]

TASK [Refresh inventory if needed] *********************************************
included: /opt/ludus/ansible/range-management/tasks/proxmox/refresh_inventory.yml for localhost

TASK [Refresh inventory] *******************************************************

TASK [Show last_deployed_ip] ***************************************************
ok: [localhost] => {
    "last_deployed_ip": "10.2.10.202"
}

TASK [Wait for the host's control interface (WinRM via HTTPS) to come up] ******
ok: [localhost]

TASK [Wait for the host's control interface (SSH) to come up] ******************
skipping: [localhost]

PLAY [Collect VM names] ********************************************************

TASK [Collect VM names] ********************************************************
ok: [localhost] => (item={'vm_name': 'DEMO-albalad-DC-JD', 'hostname': 'dc01', 'template': 'win2022-server-x64-template', 'vlan': 10, 'ip_last_octet': 11, 'ram_gb': 8, 'cpus': 4, 'windows': {'sysprep': True}, 'domain': {'fqdn': 'albalad.bsides.rv', 'role': 'primary-dc'}})
ok: [localhost] => (item={'vm_name': 'DEMO-albalad-dev-JD', 'hostname': 'dev03', 'template': 'win2022-server-x64-template', 'vlan': 10, 'ip_last_octet': 12, 'ram_gb': 6, 'cpus': 4, 'windows': {'sysprep': True}, 'domain': {'fqdn': 'albalad.bsides.rv', 'role': 'member'}})

PLAY [Configure IP and Hostname for all VMs] ***********************************

TASK [Gathering Facts] *********************************************************
[WARNING]: Failed to collect winrm due to timeout
[WARNING]: Failed to collect distribution due to timeout
ok: [DEMO-albalad-DC-JD]
ok: [DEMO-albalad-dev-JD]

TASK [Configure IP and Hostname] ***********************************************
included: /opt/ludus/ansible/range-management/tasks/proxmox/configure-ip-and-hostname.yml for DEMO-albalad-DC-JD, DEMO-albalad-dev-JD

TASK [Check if the IP has been statically set correctly (Linux)] ***************
skipping: [DEMO-albalad-DC-JD]
skipping: [DEMO-albalad-dev-JD]

TASK [Ending play for this host (Linux)] ***************************************
skipping: [DEMO-albalad-DC-JD]
skipping: [DEMO-albalad-dev-JD]

TASK [End play if configured (Linux)] ******************************************
skipping: [DEMO-albalad-DC-JD]

TASK [End play if configured (Linux)] ******************************************
skipping: [DEMO-albalad-dev-JD]

TASK [Get network interface configuration (Windows)] ***************************
changed: [DEMO-albalad-dev-JD]
changed: [DEMO-albalad-DC-JD]

TASK [Output result] ***********************************************************
ok: [DEMO-albalad-DC-JD] => {
    "msg": "DHCP\r\n"
}
ok: [DEMO-albalad-dev-JD] => {
    "msg": "DHCP\r\n"
}

TASK [Get IP address of network interface (Windows)] ***************************
skipping: [DEMO-albalad-DC-JD]
skipping: [DEMO-albalad-dev-JD]

TASK [Show IP address] *********************************************************
skipping: [DEMO-albalad-DC-JD]
skipping: [DEMO-albalad-dev-JD]

TASK [Ending play for this host (Windows)] *************************************
skipping: [DEMO-albalad-DC-JD]
skipping: [DEMO-albalad-dev-JD]

TASK [End play if configured (Windows)] ****************************************
skipping: [DEMO-albalad-DC-JD]

TASK [End play if configured (Windows)] ****************************************
skipping: [DEMO-albalad-dev-JD]

TASK [Primary Method - Set up static IP address (Windows)] *********************
ok: [DEMO-albalad-dev-JD]
ok: [DEMO-albalad-DC-JD]

TASK [Set old_hardware fact (Windows)] *****************************************
ok: [DEMO-albalad-DC-JD]
ok: [DEMO-albalad-dev-JD]

TASK [Is fallback needed?] *****************************************************
ok: [DEMO-albalad-DC-JD] => {
    "msg": {
        "ansible_async_watchdog_pid": 3980,
        "ansible_job_id": "j577422154316.4912",
        "changed": false,
        "failed": false,
        "finished": 0,
        "results_file": "C:\\Users\\localuser\\.ansible_async\\j577422154316.4912",
        "started": 1
    }
}
ok: [DEMO-albalad-dev-JD] => {
    "msg": {
        "ansible_async_watchdog_pid": 3592,
        "ansible_job_id": "j110145606129.2616",
        "changed": false,
        "failed": false,
        "finished": 0,
        "results_file": "C:\\Users\\localuser\\.ansible_async\\j110145606129.2616",
        "started": 1
    }
}

TASK [Fallback - Create file with ip changes with netsh.exe] *******************
skipping: [DEMO-albalad-DC-JD]
skipping: [DEMO-albalad-dev-JD]

TASK [Fallback - Set registry key for script execution on next reboot] *********
skipping: [DEMO-albalad-DC-JD]
skipping: [DEMO-albalad-dev-JD]

TASK [Fallback - Set registry key for script execution on next reboot] *********
skipping: [DEMO-albalad-DC-JD]
skipping: [DEMO-albalad-dev-JD]

TASK [Fallback - Reboot the machine to apply static IP (Fallback Method)] ******
skipping: [DEMO-albalad-DC-JD]
skipping: [DEMO-albalad-dev-JD]

TASK [Change ansible's ip address for the host (Windows)] **********************
ok: [DEMO-albalad-DC-JD]
ok: [DEMO-albalad-dev-JD]

TASK [Wait for the host's network interface to come back up (Windows)] *********
ok: [DEMO-albalad-DC-JD -> localhost]
ok: [DEMO-albalad-dev-JD -> localhost]

TASK [Clean up static IP script after reboot] **********************************
skipping: [DEMO-albalad-DC-JD]
skipping: [DEMO-albalad-dev-JD]

TASK [Set DNS (Windows)] *******************************************************
changed: [DEMO-albalad-DC-JD]
changed: [DEMO-albalad-dev-JD]

TASK [Set DNS search domain (Windows)] *****************************************
changed: [DEMO-albalad-dev-JD]
changed: [DEMO-albalad-DC-JD]

TASK [Lookup the timezone string for Windows] **********************************
ok: [DEMO-albalad-DC-JD]
ok: [DEMO-albalad-dev-JD]

TASK [Fail this host if we can't find the timezone] ****************************
skipping: [DEMO-albalad-DC-JD]
skipping: [DEMO-albalad-dev-JD]

TASK [Set the timezone (Windows)] **********************************************
changed: [DEMO-albalad-DC-JD]
changed: [DEMO-albalad-dev-JD]

TASK [Hostname change (Windows)] ***********************************************
changed: [DEMO-albalad-DC-JD]
changed: [DEMO-albalad-dev-JD]

TASK [Reboot] ******************************************************************
changed: [DEMO-albalad-dev-JD]
changed: [DEMO-albalad-DC-JD]

TASK [Wait for the host's control interface (WinRM via HTTPS) to come up] ******
ok: [DEMO-albalad-DC-JD -> localhost]
ok: [DEMO-albalad-dev-JD -> localhost]

TASK [Install dbus for systemd hostname changes] *******************************
skipping: [DEMO-albalad-dev-JD]
skipping: [DEMO-albalad-DC-JD]

TASK [Install ifupdown to enable interfaces] ***********************************
skipping: [DEMO-albalad-DC-JD]
skipping: [DEMO-albalad-dev-JD]

TASK [Check if /etc/cloud exists and is a directory] ***************************
skipping: [DEMO-albalad-DC-JD]
skipping: [DEMO-albalad-dev-JD]

TASK [Ensure /etc/cloud/cloud-init.disabled exists to stop cloud-init from DHCPing the interface] ***
skipping: [DEMO-albalad-DC-JD]
skipping: [DEMO-albalad-dev-JD]

TASK [Check if /etc/netplan/00-installer-config.yaml exists] *******************
skipping: [DEMO-albalad-DC-JD]
skipping: [DEMO-albalad-dev-JD]

TASK [Delete /etc/netplan/00-installer-config.yaml] ****************************
skipping: [DEMO-albalad-DC-JD]
skipping: [DEMO-albalad-dev-JD]

TASK [Remove netplan cloud-init] ***********************************************
skipping: [DEMO-albalad-DC-JD]
skipping: [DEMO-albalad-dev-JD]

TASK [Check if /etc/cloud/cloud.cfg.d exists] **********************************
skipping: [DEMO-albalad-dev-JD]
skipping: [DEMO-albalad-DC-JD]

TASK [Disable cloud dhcp network] **********************************************
skipping: [DEMO-albalad-DC-JD]
skipping: [DEMO-albalad-dev-JD]

TASK [Set DNS search domain for systemd-resolved] ******************************
skipping: [DEMO-albalad-DC-JD]
skipping: [DEMO-albalad-dev-JD]

TASK [Set DNS server for systemd-resolved] *************************************
skipping: [DEMO-albalad-DC-JD]
skipping: [DEMO-albalad-dev-JD]

TASK [get MAC for vlan interface (Linux)] **************************************
skipping: [DEMO-albalad-dev-JD]
skipping: [DEMO-albalad-DC-JD]

TASK [Set the vlan_mac variable] ***********************************************
skipping: [DEMO-albalad-DC-JD]
skipping: [DEMO-albalad-dev-JD]

TASK [get interface for MAC of vlan interface (Linux)] *************************
skipping: [DEMO-albalad-DC-JD]
skipping: [DEMO-albalad-dev-JD]

TASK [Set the interface_name variable] *****************************************
skipping: [DEMO-albalad-DC-JD]
skipping: [DEMO-albalad-dev-JD]

TASK [Assert we found the interface name] **************************************
skipping: [DEMO-albalad-DC-JD]
skipping: [DEMO-albalad-dev-JD]

TASK [Set static IP from the template (Linux-Debian)] **************************
skipping: [DEMO-albalad-DC-JD]
skipping: [DEMO-albalad-dev-JD]

TASK [Set static IP from the template (Linux-RedHat/CentOS/Alma/Rocky)] ********
skipping: [DEMO-albalad-DC-JD]
skipping: [DEMO-albalad-dev-JD]

TASK [Check for "new" static IP files on (Linux-RedHat/CentOS/Alma/Rocky) > 8] ***
skipping: [DEMO-albalad-DC-JD]
skipping: [DEMO-albalad-dev-JD]

TASK [Remove "new" static IP file (Linux-RedHat/CentOS/Alma/Rocky) > 8] ********
skipping: [DEMO-albalad-DC-JD]
skipping: [DEMO-albalad-dev-JD]

TASK [Enable new interface (Linux)] ********************************************
skipping: [DEMO-albalad-DC-JD]
skipping: [DEMO-albalad-dev-JD]

TASK [Setting hostname (Linux)] ************************************************
skipping: [DEMO-albalad-DC-JD]
skipping: [DEMO-albalad-dev-JD]

TASK [Setting hostname (Linux-RedHat/CentOS/Alma/Rocky)] ***********************
skipping: [DEMO-albalad-DC-JD]
skipping: [DEMO-albalad-dev-JD]

TASK [Add IP address to /etc/hosts] ********************************************
skipping: [DEMO-albalad-DC-JD]
skipping: [DEMO-albalad-dev-JD]

TASK [Add hostname to /etc/hosts] **********************************************
skipping: [DEMO-albalad-DC-JD]
skipping: [DEMO-albalad-dev-JD]

TASK [Remove default entry for 127.0.0.1 from /etc/hosts] **********************
skipping: [DEMO-albalad-DC-JD]
skipping: [DEMO-albalad-dev-JD]

TASK [Set the timezone (Linux)] ************************************************
skipping: [DEMO-albalad-DC-JD]
skipping: [DEMO-albalad-dev-JD]

TASK [Reboot to set ip and hostname (Linux)] ***********************************
skipping: [DEMO-albalad-DC-JD]
skipping: [DEMO-albalad-dev-JD]

TASK [Change ansible's ip address for the host] ********************************
skipping: [DEMO-albalad-DC-JD]
skipping: [DEMO-albalad-dev-JD]

TASK [Wait for the host's control interface (SSH) to come up] ******************
skipping: [DEMO-albalad-DC-JD]
skipping: [DEMO-albalad-dev-JD]

TASK [Set up static IP address (macOS)] ****************************************
skipping: [DEMO-albalad-dev-JD]
skipping: [DEMO-albalad-DC-JD]

TASK [Change ansible's ip address for the host] ********************************
skipping: [DEMO-albalad-dev-JD]
skipping: [DEMO-albalad-DC-JD]

TASK [Wait for the host's control interface (SSH) to come up] ******************
skipping: [DEMO-albalad-DC-JD]
skipping: [DEMO-albalad-dev-JD]

TASK [Set DNS (macOS)] *********************************************************
skipping: [DEMO-albalad-DC-JD]
skipping: [DEMO-albalad-dev-JD]

TASK [Setting hostname (macOS)] ************************************************
skipping: [DEMO-albalad-DC-JD]
skipping: [DEMO-albalad-dev-JD]

TASK [Set the timezone (macOS)] ************************************************
skipping: [DEMO-albalad-DC-JD]
skipping: [DEMO-albalad-dev-JD]

TASK [Refresh inventory] *******************************************************

PLAY [Add all hosts to DNS on the router] **************************************

TASK [Gathering Facts] *********************************************************
ok: [JD-router-debian11-x64]

TASK [Add host to router DNS] **************************************************
included: /opt/ludus/ansible/range-management/tasks/router/add-host-to-router-dns.yml for JD-router-debian11-x64

TASK [Get current DNS rules] ***************************************************
ok: [JD-router-debian11-x64]

TASK [Delete all rewrite rules to start fresh] *********************************
skipping: [JD-router-debian11-x64]

TASK [Add IP address of all hosts for this range_id to DNS without range_id prefix] ***
ok: [JD-router-debian11-x64] => (item={'vm_name': 'DEMO-albalad-DC-JD', 'hostname': 'dc01', 'template': 'win2022-server-x64-template', 'vlan': 10, 'ip_last_octet': 11, 'ram_gb': 8, 'cpus': 4, 'windows': {'sysprep': True}, 'domain': {'fqdn': 'albalad.bsides.rv', 'role': 'primary-dc'}})
ok: [JD-router-debian11-x64] => (item={'vm_name': 'DEMO-albalad-dev-JD', 'hostname': 'dev03', 'template': 'win2022-server-x64-template', 'vlan': 10, 'ip_last_octet': 12, 'ram_gb': 6, 'cpus': 4, 'windows': {'sysprep': True}, 'domain': {'fqdn': 'albalad.bsides.rv', 'role': 'member'}})

TASK [Add IP address of all hosts for this range_id to DNS with range_id prefix] ***
ok: [JD-router-debian11-x64] => (item={'vm_name': 'DEMO-albalad-DC-JD', 'hostname': 'dc01', 'template': 'win2022-server-x64-template', 'vlan': 10, 'ip_last_octet': 11, 'ram_gb': 8, 'cpus': 4, 'windows': {'sysprep': True}, 'domain': {'fqdn': 'albalad.bsides.rv', 'role': 'primary-dc'}})
ok: [JD-router-debian11-x64] => (item={'vm_name': 'DEMO-albalad-dev-JD', 'hostname': 'dev03', 'template': 'win2022-server-x64-template', 'vlan': 10, 'ip_last_octet': 12, 'ram_gb': 6, 'cpus': 4, 'windows': {'sysprep': True}, 'domain': {'fqdn': 'albalad.bsides.rv', 'role': 'member'}})

TASK [Add IP address of all hosts for this range_id to DNS without range_id prefix and with home.arpa] ***
ok: [JD-router-debian11-x64] => (item={'vm_name': 'DEMO-albalad-DC-JD', 'hostname': 'dc01', 'template': 'win2022-server-x64-template', 'vlan': 10, 'ip_last_octet': 11, 'ram_gb': 8, 'cpus': 4, 'windows': {'sysprep': True}, 'domain': {'fqdn': 'albalad.bsides.rv', 'role': 'primary-dc'}})
ok: [JD-router-debian11-x64] => (item={'vm_name': 'DEMO-albalad-dev-JD', 'hostname': 'dev03', 'template': 'win2022-server-x64-template', 'vlan': 10, 'ip_last_octet': 12, 'ram_gb': 6, 'cpus': 4, 'windows': {'sysprep': True}, 'domain': {'fqdn': 'albalad.bsides.rv', 'role': 'member'}})

TASK [Add IP address of all hosts for this range_id to DNS with range_id prefix and with home.arpa] ***
ok: [JD-router-debian11-x64] => (item={'vm_name': 'DEMO-albalad-DC-JD', 'hostname': 'dc01', 'template': 'win2022-server-x64-template', 'vlan': 10, 'ip_last_octet': 11, 'ram_gb': 8, 'cpus': 4, 'windows': {'sysprep': True}, 'domain': {'fqdn': 'albalad.bsides.rv', 'role': 'primary-dc'}})
ok: [JD-router-debian11-x64] => (item={'vm_name': 'DEMO-albalad-dev-JD', 'hostname': 'dev03', 'template': 'win2022-server-x64-template', 'vlan': 10, 'ip_last_octet': 12, 'ram_gb': 6, 'cpus': 4, 'windows': {'sysprep': True}, 'domain': {'fqdn': 'albalad.bsides.rv', 'role': 'member'}})

PLAY [Collect VMs with rewrite rules] ******************************************

TASK [Collect VMs with rewrite rules] ******************************************
skipping: [localhost] => (item={'vm_name': 'DEMO-albalad-DC-JD', 'hostname': 'dc01', 'template': 'win2022-server-x64-template', 'vlan': 10, 'ip_last_octet': 11, 'ram_gb': 8, 'cpus': 4, 'windows': {'sysprep': True}, 'domain': {'fqdn': 'albalad.bsides.rv', 'role': 'primary-dc'}})
skipping: [localhost] => (item={'vm_name': 'DEMO-albalad-dev-JD', 'hostname': 'dev03', 'template': 'win2022-server-x64-template', 'vlan': 10, 'ip_last_octet': 12, 'ram_gb': 6, 'cpus': 4, 'windows': {'sysprep': True}, 'domain': {'fqdn': 'albalad.bsides.rv', 'role': 'member'}})
skipping: [localhost]

PLAY [Add custom DNS rewrite rules] ********************************************

TASK [Gathering Facts] *********************************************************
ok: [JD-router-debian11-x64]

TASK [Add user-defined rewrites to the router] *********************************
skipping: [JD-router-debian11-x64]

PLAY [Collect Windows VMs to sysprep] ******************************************

TASK [Collect Windows VMs to sysprep] ******************************************
ok: [localhost] => (item={'vm_name': 'DEMO-albalad-DC-JD', 'hostname': 'dc01', 'template': 'win2022-server-x64-template', 'vlan': 10, 'ip_last_octet': 11, 'ram_gb': 8, 'cpus': 4, 'windows': {'sysprep': True}, 'domain': {'fqdn': 'albalad.bsides.rv', 'role': 'primary-dc'}})
ok: [localhost] => (item={'vm_name': 'DEMO-albalad-dev-JD', 'hostname': 'dev03', 'template': 'win2022-server-x64-template', 'vlan': 10, 'ip_last_octet': 12, 'ram_gb': 6, 'cpus': 4, 'windows': {'sysprep': True}, 'domain': {'fqdn': 'albalad.bsides.rv', 'role': 'member'}})

PLAY [Sysprep Windows VMs] *****************************************************

TASK [Gathering Facts] *********************************************************
ok: [DEMO-albalad-dev-JD]
ok: [DEMO-albalad-DC-JD]

TASK [Sysprep a VM] ************************************************************
included: /opt/ludus/ansible/range-management/tasks/windows/sysprep.yml for DEMO-albalad-DC-JD, DEMO-albalad-dev-JD

TASK [Check if sysprepd file exists] *******************************************
ok: [DEMO-albalad-dev-JD]
ok: [DEMO-albalad-DC-JD]

TASK [Skip tasks if sysprepd file exists] **************************************
skipping: [DEMO-albalad-DC-JD]

TASK [Skip tasks if sysprepd file exists] **************************************
skipping: [DEMO-albalad-dev-JD]

TASK [Create C:\Windows\Setup\Scripts directory] *******************************
changed: [DEMO-albalad-DC-JD]
changed: [DEMO-albalad-dev-JD]

TASK [Copy SetupComplete.cmd to C:\Windows\Setup\Scripts] **********************
changed: [DEMO-albalad-dev-JD]
changed: [DEMO-albalad-DC-JD]

TASK [Create C:\ludus\sysprep directory] ***************************************
changed: [DEMO-albalad-dev-JD]
changed: [DEMO-albalad-DC-JD]

TASK [Copy oob-disable.xml to C:\ludus\sysprep] ********************************
changed: [DEMO-albalad-dev-JD]
changed: [DEMO-albalad-DC-JD]

TASK [Run Sysprep] *************************************************************
changed: [DEMO-albalad-DC-JD]
changed: [DEMO-albalad-dev-JD]

TASK [Wait for 60 seconds for sysprep to finish] *******************************
Pausing for 60 seconds
ok: [DEMO-albalad-DC-JD]

TASK [Wait for WinRM] **********************************************************
ok: [DEMO-albalad-DC-JD -> localhost]
ok: [DEMO-albalad-dev-JD -> localhost]

TASK [Wait for 60 seconds for the second reboot] *******************************
Pausing for 60 seconds
ok: [DEMO-albalad-DC-JD]

TASK [Wait for WinRM] **********************************************************
ok: [DEMO-albalad-dev-JD -> localhost]
ok: [DEMO-albalad-DC-JD -> localhost]

TASK [Create sysprepd file] ****************************************************
fatal: [DEMO-albalad-dev-JD]: UNREACHABLE! => {"changed": false, "msg": "ssl: The device is not ready.  (extended fault data: {'transport_message': 'Bad HTTP response returned from server. Code 500', 'http_status_code': 500, 'wsmanfault_code': 2147942421, 'fault_code': 's:Receiver', 'fault_subcode': 'w:InternalError'})", "unreachable": true}
fatal: [DEMO-albalad-DC-JD]: UNREACHABLE! => {"changed": false, "msg": "ssl: The device is not ready.  (extended fault data: {'transport_message': 'Bad HTTP response returned from server. Code 500', 'http_status_code': 500, 'wsmanfault_code': 2147942421, 'fault_code': 's:Receiver', 'fault_subcode': 'w:InternalError'})", "unreachable": true}

PLAY RECAP *********************************************************************
DEMO-albalad-DC-JD         : ok=28   changed=11   unreachable=1    failed=0    skipped=47   rescued=0    ignored=0
DEMO-albalad-dev-JD        : ok=26   changed=11   unreachable=1    failed=0    skipped=47   rescued=0    ignored=0
JD-router-debian11-x64     : ok=69   changed=44   unreachable=0    failed=0    skipped=57   rescued=0    ignored=0
localhost                  : ok=70   changed=26   unreachable=0    failed=0    skipped=11   rescued=0    ignored=0


```