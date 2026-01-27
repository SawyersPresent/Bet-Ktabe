#### RedGuard
  
```
git clone https://github.com/wikiZ/RedGuard.git
cd RedGuard
go build -ldflags "-s -w" -trimpath
sudo chmod +x ./RedGuard&&./RedGuard
```

#### Creation SSL cert for redguard, that need to be made on redguard path, create dir cert-rsa
  
```
openssl req -x509 -newkey rsa:2048 -keyout cert-rsa/cert.key -out cert-rsa/cert.crt -sha256 -nodes -subj "/C=US/O=Google Trust Services LLC/CN=https:,,go.dev"
```

#### Find the _.RedGuard_CobaltStrike.ini
  
```
sudo find / -name ".RedGuard_CobaltStrike.ini"
```

Edit the .ini
```
sudo nano .RedGuard_CobaltStrike.ini
```
  
```
[cert]
# User Optional name
DNSName      = *.go.dev
# Cert User CommonName
CommonName   = *.go.dev
# Cert User Locality
Locality     = HangZhou
# Cert User Organization
Organization = Alibaba (China) Technology Co., Ltd.
# Cert User Country
Country      = CN
# Whether to use the certificate you have applied for true/false
HasCert      = true
 
[proxy]
# key   : Header Host value of the reverse proxy
# value : The actual address forwarded by the reverse proxy
HostTarget    = {"go.dev":"http://127.0.0.1:8080", "go.dev":"https://127.0.0.1:4433"}
# HTTPS Reverse proxy port
Port_HTTPS    = :443
# HTTP Reverse proxy port
Port_HTTP     = :7080
# RedGuard interception action: redirect / reset / proxy (Hijack HTTP Response)
drop_action   = redirect
# URL to redirect to
Redirect      = https://go.dev
# IP address owning restrictions example:AllowLocation = 山东,上海,杭州 or shanghai,beijing
AllowLocation = *
# Whitelist list example: AllowIP = 172.16.1.1,192.168.1.1
AllowIP       = *
# Limit the  time of requests example: AllowTime = 8:00 - 16:00
AllowTime     = *
# C2 Malleable File Path
MalleableFile = *
# Edge Host Communication Domain
EdgeHost      = *
# Edge Host Proxy Target example: EdgeTarget = 360.com
EdgeTarget    = *
# Customize the header to be deleted example: Keep-Alive,Transfer-Encoding
DelHeader     = *
 
[SampleFinger]
# HTTP Request Header Field
FieldName   = *
# Sample Finger example:xxxxxx,xxxxxx
FieldFinger = *
```
#### Run RedGuard
  
```
./RedGuard
```

#### Browser do
- try to visit https:ur_ip:redguard_port
- if you redirected to [go.dev](https://go.dev), all ok
- check certificate, if it exist all good.

#### Setup a listener in Cobalt
  
- Choose HTTPS Listener
- - HTTP Hosts: Server IP
- - Host rotation - round-robin
- - Max retry - none
- - HTTPS Host Stager: default
- - HTTPS Port (C2) - 443
- - HTTPS Port (Bind) - 4433
- - HTTPS Host Header - [go.dev](https://go.dev)

---


