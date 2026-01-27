
```
ludus:
  - vm_name: "CEO-PC"
    hostname: "CEO-PC"
    template: win2022-server-x64-template
    vlan: 10
    ip_last_octet: 10
    ram_gb: 4
    cpus: 2
    windows:
      sysprep: true
      gpos:
        - disable_defender
    domain:
      fqdn: josa.local
      role: primary-dc
    testing:
      snapshot: true
      block_internet: false
  - vm_name: "INTERN-PC"
    hostname: "INTERN-PC"
    template: win11-22h2-x64-enterprise-template
    vlan: 10
    ip_last_octet: 20
    ram_gb: 4
    cpus: 2
    windows:
      sysprep: true
    domain:
      fqdn: josa.local
      role: member
    testing:
      snapshot: true
      block_internet: false

defaults:
  snapshot_with_RAM: true
  stale_hours: 0 # How many hours until a pre-existing snapshot should be deleted and retaken (if entering and exiting testing mode quickly)
  ad_domain_functional_level: Win2012R2 # The functional level of each Windows domain created by Ludus - options are: "Win2003", "Win2008", "Win2008R2", "Win2012", "Win2012R2", "WinThreshold", or "Win2025"
  ad_forest_functional_level: Win2012R2 # The functional level of each Windows forest created by Ludus - options are: "Win2003", "Win2008", "Win2008R2", "Win2012", "Win2012R2", "WinThreshold", or "Win2025"
  ad_domain_admin: JosaAdmin # The domain admin username for every Windows domain
  ad_domain_admin_password: JosaAdmin # The domain admin password for every Windows domain
  ad_domain_user: JosaUser # The domain user username for every Windows domain
  ad_domain_user_password: JosaUser # The domain user password for every Windows domain
  ad_domain_safe_mode_password: JosaAdmin # The domain safe mode password for every Windows domain
  timezone: Asia/Jerusalem # The timezone for all VMs, use the TZ identifier format from https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
  enable_dynamic_wallpaper: true # Enable dynamic wallpaper (red/green) for all Windows VMs in the range
```








