

```
ludus:
  - vm_name: "{{ range_id }}-ad-dc-win2022-server-x64"
    hostname: "{{ range_id }}-DC01"
    template: win2022-server-x64-template
    vlan: 10
    ip_last_octet: 11
    ram_gb: 8
    cpus: 4
    windows:
      sysprep: true
    domain:
      fqdn: allports.local
      role: primary-dc

  - vm_name: "{{ range_id }}-ad-dc-win2022-server2"
    hostname: "{{ range_id }}-DC02"
    template: win2022-server-x64-template
    vlan: 10
    ip_last_octet: 12
    ram_gb: 8
    cpus: 4
    windows:
      sysprep: true
    domain:
      fqdn: allports.local
      role: member
  - vm_name: "{{ range_id }}-ad-dc-win2022-server3"
    hostname: "{{ range_id }}-DC03"
    template: win2022-server-x64-template
    vlan: 10
    ip_last_octet: 13
    ram_gb: 8
    cpus: 4
    windows:
      sysprep: true
    domain:
      fqdn: allports.local
      role: member


defaults:
  snapshot_with_RAM: true
  stale_hours: 0 # How many hours until a pre-existing snapshot should be deleted and retaken (if entering and exiting testing mode quickly)
  ad_domain_functional_level: Win2012R2 # The functional level of each Windows domain created by Ludus - options are: "Win2003", "Win2008", "Win2008R2", "Win2012", "Win2012R2", "WinThreshold", or "Win2025"
  ad_forest_functional_level: Win2012R2 # The functional level of each Windows forest created by Ludus - options are: "Win2003", "Win2008", "Win2008R2", "Win2012", "Win2012R2", "WinThreshold", or "Win2025"
  ad_domain_admin: sawyerAdmin # The domain admin username for every Windows domain
  ad_domain_admin_password: password # The domain admin password for every Windows domain
  ad_domain_user: sawyerUser # The domain user username for every Windows domain
  ad_domain_user_password: password # The domain user password for every Windows domain
  ad_domain_safe_mode_password: password # The domain safe mode password for every Windows domain
  timezone: Asia/Jerusalem # The timezone for all VMs, use the TZ identifier format from https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
  enable_dynamic_wallpaper: true # Enable dynamic wallpaper (red/green) for all Windows VMs in the range
```