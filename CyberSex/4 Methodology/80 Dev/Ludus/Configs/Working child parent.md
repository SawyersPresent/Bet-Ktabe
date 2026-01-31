
```python
  defaults:
    snapshot_with_RAM: true
    stale_hours: 0
    ad_domain_functional_level: "Win2012R2"
    ad_forest_functional_level: "Win2012R2"
    ad_domain_admin: "sawyerAdmin"
    ad_domain_admin_password: "password"
    ad_domain_user: "sawyerUser"
    ad_domain_user_password: "password"
    ad_domain_safe_mode_password: "password"
    timezone: "Asia/Jerusalem"
    enable_dynamic_wallpaper: true

  ludus:
    # Parent domain DC (test.local)
    - vm_name: "{{ range_id }}-ad-dc-win2022-server-x64"
      hostname: "DC"
      template: win2022-server-x64-template
      vlan: 20
      ip_last_octet: 11          # 10.2.20.11
      ram_gb: 10
      cpus: 4
      windows:
        sysprep: true
      domain:
        fqdn: test.local
        role: primary-dc
      roles:
        - badsectorlabs.ludus_adcs

    # Child domain controller (creates dev.test.local)
    - vm_name: "{{ range_id }}-Internal-VLAN30-devdc01"
      hostname: "devdc01"
      template: win2022-server-x64-template
      vlan: 30
      ip_last_octet: 10          # 10.2.30.10
      ram_gb: 4
      cpus: 1
      windows:
        sysprep: true
      roles:
        - ludus_child_domain
      role_vars:
        dns_domain_name: "dev.test.local"                 # child FQDN
        domain_admin_user: "administrator@test.local"    # parent admin (must exist)
        domain_admin_password: "password"
        safe_mode_password: "password"
        create_dns_delegation: true
        parent_dc_ip: "10.2.20.11"                       # parent DC IP
        current_host_ip: "10.2.30.10"                    # this child DC IP
        reboot: true
        install_dns: true
        child_domain_admin_user: "labadmin"
        child_domain_admin_password: "password"

    # Member joined to the child domain
    - vm_name: "{{ range_id }}-Internal-VLAN30-fs01"
      hostname: "fs01"
      template: win2022-server-x64-template
      vlan: 30
      ip_last_octet: 20          # 10.2.30.20
      ram_gb: 2
      cpus: 1
      windows:
        sysprep: true
      roles:
        - ludus_child_domain_join
      role_vars:
        dc_ip: "10.2.30.10"                          # child DC IP
        dns_domain_name: "dev.test.local"
        domain_admin_user: "administrator@dev.test.local"
        domain_admin_password: "password"
        # domain_ou_path: "OU=Servers,DC=dev,DC=test,DC=local"  # optional
```


here isa more realistic exmaple





```
  defaults:
    snapshot_with_RAM: true
    stale_hours: 0
    ad_domain_functional_level: "Win2012R2"
    ad_forest_functional_level: "Win2012R2"
    ad_domain_admin: "sawyerAdmin"
    ad_domain_admin_password: "password"
    ad_domain_user: "sawyerUser"
    ad_domain_user_password: "password"
    ad_domain_safe_mode_password: "password"
    timezone: "Asia/Jerusalem"
    enable_dynamic_wallpaper: true

  ludus:
    # Parent domain DC (probatio.localis)
    - vm_name: "{{ range_id }}-dc-parent"
      hostname: "dc-parent"
      template: win2022-server-x64-template
      vlan: 20
      ip_last_octet: 11          # 10.2.20.11
      ram_gb: 10
      cpus: 4
      windows:
        sysprep: true
      domain:
        fqdn: probatio.localis
        role: primary-dc
      roles:
        - badsectorlabs.ludus_adcs

    # Child domain controller (lab.probatio.localis)
    - vm_name: "{{ range_id }}-dc-child"
      hostname: "dc-child"
      template: win2022-server-x64-template
      vlan: 30
      ip_last_octet: 10          # 10.2.30.10
      ram_gb: 4
      cpus: 1
      windows:
        sysprep: true
      roles:
        - ludus_child_domain
      role_vars:
        dns_domain_name: "lab.probatio.localis"                 # child FQDN
        domain_admin_user: "administrator@probatio.localis"    # parent admin
        domain_admin_password: "password"
        safe_mode_password: "password"
        create_dns_delegation: true
        parent_dc_ip: "10.2.20.11"                             # parent DC IP
        current_host_ip: "10.2.30.10"                          # this child DC IP
        reboot: true
        install_dns: true
        child_domain_admin_user: "labadmin"
        child_domain_admin_password: "password"

    # Member joined to the child domain
    - vm_name: "{{ range_id }}-fs-child"
      hostname: "fs-child"
      template: win2022-server-x64-template
      vlan: 30
      ip_last_octet: 20          # 10.2.30.20
      ram_gb: 2
      cpus: 1
      windows:
        sysprep: true
      roles:
        - ludus_child_domain_join
      role_vars:
        dc_ip: "10.2.30.10"                                # child DC IP
        dns_domain_name: "lab.probatio.localis"
        domain_admin_user: "administrator@lab.probatio.localis"
        domain_admin_password: "password"
        # domain_ou_path: "OU=Servers,DC=lab,DC=probatio,DC=localis"  # optional
```


