
```
[domain_controllers]
CEO-PC ansible_host=10.2.10.10

[workstations]
INTERN-PC ansible_host=10.2.10.20

[windows:children]
domain_controllers
workstations

[windows:vars]
ansible_user=josa\JosaAdmin
ansible_password=JosaAdmin
ansible_connection=winrm
ansible_winrm_transport=ntlm
ansible_winrm_server_cert_validation=ignore
ansible_port=5986

[all:vars]
domain_name=josa.local
domain_admin=JosaAdmin
domain_user=JosaUser
```