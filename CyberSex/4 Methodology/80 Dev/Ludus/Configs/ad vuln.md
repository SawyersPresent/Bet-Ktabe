ludus ansible role add -d .
```yaml
  - vm_name: "{{ range_id }}-ad-dc-win2022-server-x64-1"
    hostname: "{{ range_id }}-DC01"
    template: win2022-server-x64-template
    vlan: 10
    ip_last_octet: 11
    ram_gb: 4
    cpus: 4
    windows:
      sysprep: true
    domain:
      fqdn: maldev.local
      role: primary-dc
    roles:
      - ludus-ad-vulns
    role_vars:
      ludus_ad_vulns_openshares: true
      ludus_ad_vulns_kerberoasting: true
      kerberoasting_users:
      - identity: fives
        service_principal_name: HTTP/ArcTraining

      ludus_ad_vulns_unconstrained_delegation_user: true
      unconstrained_delegation_user: 
      - identity: cody 

      ludus_ad_vulns_set_acl: true
      acl_definitions:
        grant_generic_all_from_cptrex_to_bounty_group:
          for: "cptrex"
          to: "CN=Bounty Hunters,OU=Bounty Hunters,DC=maldev,DC=local"
          right: "GenericAll"
          inheritance: "None"   
      ludus_ad_vulns_unconstrained_delegation_machine: true
      unconstrained_delegation_machine:
      - machine_name: maldev-srv1-2022
```