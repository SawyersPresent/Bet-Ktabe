
https://claude.ai/share/6b220d7d-d5b4-4974-b457-a3d0071713d0


```
root@ludus:~/openvpn-install# curl ifconfig.me
79.134.155.177root@ludus:~/openvpn-install# curl icanhazip.com
79.134.155.177
root@ludus:~/openvpn-install# ./openvpn-install.sh
Welcome to the OpenVPN installer!
The git repository is available at: https://github.com/angristan/openvpn-install

I need to ask you a few questions before starting the setup.
You can leave the default options and just press enter if you are okay with them.

I need to know the IPv4 address of the network interface you want OpenVPN listening to.
Unless your server is behind NAT, it should be your public IPv4 address.
IP address: 79.134.155.177

Checking for IPv6 connectivity...

Your host does not appear to have IPv6 connectivity.

Do you want to enable IPv6 support (NAT)? [y/n]: n

What port do you want OpenVPN to listen to?
   1) Default: 1194
   2) Custom
   3) Random [49152-65535]
Port choice [1-3]: 1

What protocol do you want OpenVPN to use?
UDP is faster. Unless it is not available, you shouldn't use TCP.
   1) UDP
   2) TCP
Protocol [1-2]: 1

What DNS resolvers do you want to use with the VPN?
   1) Current system resolvers (from /etc/resolv.conf)
   2) Self-hosted DNS Resolver (Unbound)
   3) Cloudflare (Anycast: worldwide)
   4) Quad9 (Anycast: worldwide)
   5) Quad9 uncensored (Anycast: worldwide)
   6) FDN (France)
   7) DNS.WATCH (Germany)
   8) OpenDNS (Anycast: worldwide)
   9) Google (Anycast: worldwide)
   10) Yandex Basic (Russia)
   11) AdGuard DNS (Anycast: worldwide)
   12) NextDNS (Anycast: worldwide)
   13) Custom
DNS [1-12]: 3

Do you want to use compression? It is not recommended since the VORACLE attack makes use of it.
Enable compression? [y/n]: n

Do you want to customize encryption settings?
Unless you know what you're doing, you should stick with the default parameters provided by the script.
Note that whatever you choose, all the choices presented in the script are safe (unlike OpenVPN's defaults).
See https://github.com/angristan/openvpn-install#security-and-encryption to learn more.

Customize encryption settings? [y/n]: n

Okay, that was all I needed. We are ready to setup your OpenVPN server now.
You will be able to generate a client at the end of the installation.
Press any key to continue...
Hit:1 http://deb.debian.org/debian bookworm InRelease
Get:2 http://security.debian.org/debian-security bookworm-security InRelease [48.0 kB]
Get:3 http://deb.debian.org/debian bookworm-updates InRelease [55.4 kB]
Get:4 http://security.debian.org/debian-security bookworm-security/main Sources [183 kB]
Get:5 http://security.debian.org/debian-security bookworm-security/main amd64 Packages [285 kB]
Get:6 http://security.debian.org/debian-security bookworm-security/main Translation-en [173 kB]
Hit:7 http://download.proxmox.com/debian/pve bookworm InRelease
Fetched 745 kB in 2s (400 kB/s)
Reading package lists... Done
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following additional packages will be installed:
  dirmngr gnupg-l10n gnupg-utils gpg gpg-agent gpg-wks-client gpg-wks-server gpgconf gpgsm gpgv
Suggested packages:
  pinentry-gnome3 tor parcimonie xloadimage scdaemon
The following packages will be upgraded:
  ca-certificates dirmngr gnupg gnupg-l10n gnupg-utils gpg gpg-agent gpg-wks-client gpg-wks-server gpgconf gpgsm gpgv
12 upgraded, 0 newly installed, 0 to remove and 187 not upgraded.
Need to get 8,412 kB of archives.
After this operation, 3,072 B of additional disk space will be used.
Get:1 http://deb.debian.org/debian bookworm/main amd64 gpgv amd64 2.2.40-1.1+deb12u1 [649 kB]
Get:2 http://deb.debian.org/debian bookworm/main amd64 ca-certificates all 20230311+deb12u1 [155 kB]
Get:3 http://deb.debian.org/debian bookworm/main amd64 gpgsm amd64 2.2.40-1.1+deb12u1 [671 kB]
Get:4 http://deb.debian.org/debian bookworm/main amd64 gpg-wks-client amd64 2.2.40-1.1+deb12u1 [540 kB]
Get:5 http://deb.debian.org/debian bookworm/main amd64 gpg-wks-server amd64 2.2.40-1.1+deb12u1 [531 kB]
Get:6 http://deb.debian.org/debian bookworm/main amd64 gpg amd64 2.2.40-1.1+deb12u1 [949 kB]
Get:7 http://deb.debian.org/debian bookworm/main amd64 gnupg-utils amd64 2.2.40-1.1+deb12u1 [927 kB]
Get:8 http://deb.debian.org/debian bookworm/main amd64 gnupg-l10n all 2.2.40-1.1+deb12u1 [1,093 kB]
Get:9 http://deb.debian.org/debian bookworm/main amd64 dirmngr amd64 2.2.40-1.1+deb12u1 [792 kB]
Get:10 http://deb.debian.org/debian bookworm/main amd64 gnupg all 2.2.40-1.1+deb12u1 [846 kB]
Get:11 http://deb.debian.org/debian bookworm/main amd64 gpg-agent amd64 2.2.40-1.1+deb12u1 [694 kB]
Get:12 http://deb.debian.org/debian bookworm/main amd64 gpgconf amd64 2.2.40-1.1+deb12u1 [564 kB]
Fetched 8,412 kB in 1s (6,857 kB/s)
apt-listchanges: Reading changelogs...
Preconfiguring packages ...
(Reading database ... 59373 files and directories currently installed.)
Preparing to unpack .../gpgv_2.2.40-1.1+deb12u1_amd64.deb ...
Unpacking gpgv (2.2.40-1.1+deb12u1) over (2.2.40-1.1) ...
Setting up gpgv (2.2.40-1.1+deb12u1) ...
(Reading database ... 59373 files and directories currently installed.)
Preparing to unpack .../00-ca-certificates_20230311+deb12u1_all.deb ...
Unpacking ca-certificates (20230311+deb12u1) over (20230311) ...
Preparing to unpack .../01-gpgsm_2.2.40-1.1+deb12u1_amd64.deb ...
Unpacking gpgsm (2.2.40-1.1+deb12u1) over (2.2.40-1.1) ...
Preparing to unpack .../02-gpg-wks-client_2.2.40-1.1+deb12u1_amd64.deb ...
Unpacking gpg-wks-client (2.2.40-1.1+deb12u1) over (2.2.40-1.1) ...
Preparing to unpack .../03-gpg-wks-server_2.2.40-1.1+deb12u1_amd64.deb ...
Unpacking gpg-wks-server (2.2.40-1.1+deb12u1) over (2.2.40-1.1) ...
Preparing to unpack .../04-gpg_2.2.40-1.1+deb12u1_amd64.deb ...
Unpacking gpg (2.2.40-1.1+deb12u1) over (2.2.40-1.1) ...
Preparing to unpack .../05-gnupg-utils_2.2.40-1.1+deb12u1_amd64.deb ...
Unpacking gnupg-utils (2.2.40-1.1+deb12u1) over (2.2.40-1.1) ...
Preparing to unpack .../06-gnupg-l10n_2.2.40-1.1+deb12u1_all.deb ...
Unpacking gnupg-l10n (2.2.40-1.1+deb12u1) over (2.2.40-1.1) ...
Preparing to unpack .../07-dirmngr_2.2.40-1.1+deb12u1_amd64.deb ...
Unpacking dirmngr (2.2.40-1.1+deb12u1) over (2.2.40-1.1) ...
Preparing to unpack .../08-gnupg_2.2.40-1.1+deb12u1_all.deb ...
Unpacking gnupg (2.2.40-1.1+deb12u1) over (2.2.40-1.1) ...
Preparing to unpack .../09-gpg-agent_2.2.40-1.1+deb12u1_amd64.deb ...
Unpacking gpg-agent (2.2.40-1.1+deb12u1) over (2.2.40-1.1) ...
Preparing to unpack .../10-gpgconf_2.2.40-1.1+deb12u1_amd64.deb ...
Unpacking gpgconf (2.2.40-1.1+deb12u1) over (2.2.40-1.1) ...
Setting up ca-certificates (20230311+deb12u1) ...
Updating certificates in /etc/ssl/certs...
rehash: warning: skipping ca-certificates.crt,it does not contain exactly one certificate or CRL
2 added, 0 removed; done.
Setting up gnupg-l10n (2.2.40-1.1+deb12u1) ...
Setting up gpgconf (2.2.40-1.1+deb12u1) ...
Setting up gpg (2.2.40-1.1+deb12u1) ...
Setting up gnupg-utils (2.2.40-1.1+deb12u1) ...
Setting up gpg-agent (2.2.40-1.1+deb12u1) ...
Setting up gpgsm (2.2.40-1.1+deb12u1) ...
Setting up dirmngr (2.2.40-1.1+deb12u1) ...
Setting up gpg-wks-server (2.2.40-1.1+deb12u1) ...
Setting up gpg-wks-client (2.2.40-1.1+deb12u1) ...
Setting up gnupg (2.2.40-1.1+deb12u1) ...
Processing triggers for man-db (2.11.2-2) ...
Processing triggers for ca-certificates (20230311+deb12u1) ...
Updating certificates in /etc/ssl/certs...
0 added, 0 removed; done.
Running hooks in /etc/ca-certificates/update.d...
done.
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
iptables is already the newest version (1.8.9-2).
iptables set to manually installed.
wget is already the newest version (1.21.3-1+deb12u1).
ca-certificates is already the newest version (20230311+deb12u1).
The following additional packages will be installed:
  easy-rsa libccid libcurl3-gnutls libcurl4 libnl-genl-3-200 libpcsclite1 libpkcs11-helper1 libssl3 opensc
  opensc-pkcs11 pcscd
Suggested packages:
  pcmciautils resolvconf openvpn-dco-dkms openvpn-systemd-resolved
The following NEW packages will be installed:
  easy-rsa libccid libnl-genl-3-200 libpcsclite1 libpkcs11-helper1 opensc opensc-pkcs11 openvpn pcscd
The following packages will be upgraded:
  curl libcurl3-gnutls libcurl4 libssl3 openssl
5 upgraded, 9 newly installed, 0 to remove and 182 not upgraded.
Need to get 7,131 kB of archives.
After this operation, 7,783 kB of additional disk space will be used.
Get:1 http://security.debian.org/debian-security bookworm-security/main amd64 libssl3 amd64 3.0.17-1~deb12u3 [2,028 kB]
Get:2 http://deb.debian.org/debian bookworm/main amd64 libccid amd64 1.5.2-1 [367 kB]
Get:3 http://deb.debian.org/debian bookworm/main amd64 libpcsclite1 amd64 1.9.9-2 [49.7 kB]
Get:4 http://deb.debian.org/debian bookworm/main amd64 pcscd amd64 1.9.9-2 [89.7 kB]
Get:5 http://deb.debian.org/debian bookworm/main amd64 curl amd64 7.88.1-10+deb12u14 [316 kB]
Get:6 http://deb.debian.org/debian bookworm/main amd64 libcurl4 amd64 7.88.1-10+deb12u14 [392 kB]
Get:7 http://deb.debian.org/debian bookworm/main amd64 easy-rsa all 3.1.0-1 [54.8 kB]
Get:8 http://deb.debian.org/debian bookworm/main amd64 libcurl3-gnutls amd64 7.88.1-10+deb12u14 [386 kB]
Get:9 http://security.debian.org/debian-security bookworm-security/main amd64 openssl amd64 3.0.17-1~deb12u3 [1,434 kB]
Get:10 http://deb.debian.org/debian bookworm/main amd64 libnl-genl-3-200 amd64 3.7.0-0.2+b1 [21.6 kB]
Get:11 http://deb.debian.org/debian bookworm/main amd64 libpkcs11-helper1 amd64 1.29.0-1 [51.2 kB]
Get:12 http://deb.debian.org/debian bookworm/main amd64 opensc-pkcs11 amd64 0.23.0-0.3+deb12u2 [917 kB]
Get:13 http://deb.debian.org/debian bookworm/main amd64 opensc amd64 0.23.0-0.3+deb12u2 [372 kB]
Get:14 http://deb.debian.org/debian bookworm/main amd64 openvpn amd64 2.6.3-1+deb12u3 [652 kB]
Fetched 7,131 kB in 1s (5,866 kB/s)
apt-listchanges: Reading changelogs...
Preconfiguring packages ...
Selecting previously unselected package libccid.
(Reading database ... 59375 files and directories currently installed.)
Preparing to unpack .../00-libccid_1.5.2-1_amd64.deb ...
Unpacking libccid (1.5.2-1) ...
Selecting previously unselected package libpcsclite1:amd64.
Preparing to unpack .../01-libpcsclite1_1.9.9-2_amd64.deb ...
Unpacking libpcsclite1:amd64 (1.9.9-2) ...
Selecting previously unselected package pcscd.
Preparing to unpack .../02-pcscd_1.9.9-2_amd64.deb ...
Unpacking pcscd (1.9.9-2) ...
Preparing to unpack .../03-libssl3_3.0.17-1~deb12u3_amd64.deb ...
Unpacking libssl3:amd64 (3.0.17-1~deb12u3) over (3.0.15-1~deb12u1) ...
Preparing to unpack .../04-curl_7.88.1-10+deb12u14_amd64.deb ...
Unpacking curl (7.88.1-10+deb12u14) over (7.88.1-10+deb12u12) ...
Preparing to unpack .../05-libcurl4_7.88.1-10+deb12u14_amd64.deb ...
Unpacking libcurl4:amd64 (7.88.1-10+deb12u14) over (7.88.1-10+deb12u12) ...
Preparing to unpack .../06-openssl_3.0.17-1~deb12u3_amd64.deb ...
Unpacking openssl (3.0.17-1~deb12u3) over (3.0.15-1~deb12u1) ...
Selecting previously unselected package easy-rsa.
Preparing to unpack .../07-easy-rsa_3.1.0-1_all.deb ...
Unpacking easy-rsa (3.1.0-1) ...
Preparing to unpack .../08-libcurl3-gnutls_7.88.1-10+deb12u14_amd64.deb ...
Unpacking libcurl3-gnutls:amd64 (7.88.1-10+deb12u14) over (7.88.1-10+deb12u12) ...
Selecting previously unselected package libnl-genl-3-200:amd64.
Preparing to unpack .../09-libnl-genl-3-200_3.7.0-0.2+b1_amd64.deb ...
Unpacking libnl-genl-3-200:amd64 (3.7.0-0.2+b1) ...
Selecting previously unselected package libpkcs11-helper1:amd64.
Preparing to unpack .../10-libpkcs11-helper1_1.29.0-1_amd64.deb ...
Unpacking libpkcs11-helper1:amd64 (1.29.0-1) ...
Selecting previously unselected package opensc-pkcs11:amd64.
Preparing to unpack .../11-opensc-pkcs11_0.23.0-0.3+deb12u2_amd64.deb ...
Unpacking opensc-pkcs11:amd64 (0.23.0-0.3+deb12u2) ...
Selecting previously unselected package opensc.
Preparing to unpack .../12-opensc_0.23.0-0.3+deb12u2_amd64.deb ...
Unpacking opensc (0.23.0-0.3+deb12u2) ...
Selecting previously unselected package openvpn.
Preparing to unpack .../13-openvpn_2.6.3-1+deb12u3_amd64.deb ...
Unpacking openvpn (2.6.3-1+deb12u3) ...
Setting up libccid (1.5.2-1) ...
Setting up libssl3:amd64 (3.0.17-1~deb12u3) ...
Setting up libcurl3-gnutls:amd64 (7.88.1-10+deb12u14) ...
Setting up libpkcs11-helper1:amd64 (1.29.0-1) ...
Setting up opensc-pkcs11:amd64 (0.23.0-0.3+deb12u2) ...
Setting up libpcsclite1:amd64 (1.9.9-2) ...
Setting up libnl-genl-3-200:amd64 (3.7.0-0.2+b1) ...
Setting up libcurl4:amd64 (7.88.1-10+deb12u14) ...
Setting up curl (7.88.1-10+deb12u14) ...
Setting up openssl (3.0.17-1~deb12u3) ...
Setting up easy-rsa (3.1.0-1) ...
Setting up openvpn (2.6.3-1+deb12u3) ...
Created symlink /etc/systemd/system/multi-user.target.wants/openvpn.service → /lib/systemd/system/openvpn.service.
Setting up opensc (0.23.0-0.3+deb12u2) ...
Setting up pcscd (1.9.9-2) ...
Created symlink /etc/systemd/system/sockets.target.wants/pcscd.socket → /lib/systemd/system/pcscd.socket.
pcscd.service is a disabled or a static unit, not starting it.
Processing triggers for mailcap (3.70+nmu1) ...
Processing triggers for libc-bin (2.36-9+deb12u10) ...
Processing triggers for man-db (2.11.2-2) ...
--2025-11-12 08:36:58--  https://github.com/OpenVPN/easy-rsa/releases/download/v3.1.2/EasyRSA-3.1.2.tgz
Resolving github.com (github.com)... 140.82.121.4
Connecting to github.com (github.com)|140.82.121.4|:443... connected.
HTTP request sent, awaiting response... 302 Found
Location: https://release-assets.githubusercontent.com/github-production-release-asset/4519663/c2688102-7cd5-4fcc-b272-083d48dc4b4d?sp=r&sv=2018-11-09&sr=b&spr=https&se=2025-11-12T14%3A27%3A53Z&rscd=attachment%3B+filename%3DEasyRSA-3.1.2.tgz&rsct=application%2Foctet-stream&skoid=96c2d410-5711-43a1-aedd-ab1947aa7ab0&sktid=398a6654-997b-47e9-b12b-9515b896b4de&skt=2025-11-12T13%3A27%3A28Z&ske=2025-11-12T14%3A27%3A53Z&sks=b&skv=2018-11-09&sig=93Bv%2Fh88GqyCUhbahDKee9DGMvKQfBS%2B9G78b%2FAAFmw%3D&jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmVsZWFzZS1hc3NldHMuZ2l0aHVidXNlcmNvbnRlbnQuY29tIiwia2V5Ijoia2V5MSIsImV4cCI6MTc2Mjk1NDkxOSwibmJmIjoxNzYyOTU0NjE5LCJwYXRoIjoicmVsZWFzZWFzc2V0cHJvZHVjdGlvbi5ibG9iLmNvcmUud2luZG93cy5uZXQifQ.EaSCsKoLntngL-O64fe74wCYjNZVMsY_eRfPI85CrNo&response-content-disposition=attachment%3B%20filename%3DEasyRSA-3.1.2.tgz&response-content-type=application%2Foctet-stream [following]
--2025-11-12 08:36:59--  https://release-assets.githubusercontent.com/github-production-release-asset/4519663/c2688102-7cd5-4fcc-b272-083d48dc4b4d?sp=r&sv=2018-11-09&sr=b&spr=https&se=2025-11-12T14%3A27%3A53Z&rscd=attachment%3B+filename%3DEasyRSA-3.1.2.tgz&rsct=application%2Foctet-stream&skoid=96c2d410-5711-43a1-aedd-ab1947aa7ab0&sktid=398a6654-997b-47e9-b12b-9515b896b4de&skt=2025-11-12T13%3A27%3A28Z&ske=2025-11-12T14%3A27%3A53Z&sks=b&skv=2018-11-09&sig=93Bv%2Fh88GqyCUhbahDKee9DGMvKQfBS%2B9G78b%2FAAFmw%3D&jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmVsZWFzZS1hc3NldHMuZ2l0aHVidXNlcmNvbnRlbnQuY29tIiwia2V5Ijoia2V5MSIsImV4cCI6MTc2Mjk1NDkxOSwibmJmIjoxNzYyOTU0NjE5LCJwYXRoIjoicmVsZWFzZWFzc2V0cHJvZHVjdGlvbi5ibG9iLmNvcmUud2luZG93cy5uZXQifQ.EaSCsKoLntngL-O64fe74wCYjNZVMsY_eRfPI85CrNo&response-content-disposition=attachment%3B%20filename%3DEasyRSA-3.1.2.tgz&response-content-type=application%2Foctet-stream
Resolving release-assets.githubusercontent.com (release-assets.githubusercontent.com)... 185.199.108.133, 185.199.110.133, 185.199.111.133, ...
Connecting to release-assets.githubusercontent.com (release-assets.githubusercontent.com)|185.199.108.133|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 68984 (67K) [application/octet-stream]
Saving to: ‘/root/easy-rsa.tgz’

/root/easy-rsa.tgz            100%[=================================================>]  67.37K  --.-KB/s    in 0.08s

2025-11-12 08:36:59 (878 KB/s) - ‘/root/easy-rsa.tgz’ saved [68984/68984]


Notice
------
'init-pki' complete; you may now create a CA or requests.

Your newly created PKI dir is:
* /etc/openvpn/easy-rsa/pki

* Using Easy-RSA configuration: /etc/openvpn/easy-rsa/vars

* The preferred location for 'vars' is within the PKI folder.
  To silence this message move your 'vars' file to your PKI
  or declare your 'vars' file with option: --vars=<FILE>

* Using x509-types directory: /etc/openvpn/easy-rsa/x509-types


* Using SSL: openssl OpenSSL 3.0.17 1 Jul 2025 (Library: OpenSSL 3.0.17 1 Jul 2025)

* Using Easy-RSA configuration: /etc/openvpn/easy-rsa/vars

* The preferred location for 'vars' is within the PKI folder.
  To silence this message move your 'vars' file to your PKI
  or declare your 'vars' file with option: --vars=<FILE>
Using configuration from /etc/openvpn/easy-rsa/pki/81d6c73b/temp.d87dbb1a
-----

Notice
------
CA creation complete and you may now import and sign cert requests.
Your new CA certificate file for publishing is at:
/etc/openvpn/easy-rsa/pki/ca.crt

* Using SSL: openssl OpenSSL 3.0.17 1 Jul 2025 (Library: OpenSSL 3.0.17 1 Jul 2025)

* Using Easy-RSA configuration: /etc/openvpn/easy-rsa/vars

* The preferred location for 'vars' is within the PKI folder.
  To silence this message move your 'vars' file to your PKI
  or declare your 'vars' file with option: --vars=<FILE>
-----

Notice
------
Keypair and certificate request completed. Your files are:
req: /etc/openvpn/easy-rsa/pki/reqs/server_0D1uuPpBhRt6VMuv.req
key: /etc/openvpn/easy-rsa/pki/private/server_0D1uuPpBhRt6VMuv.key
Using configuration from /etc/openvpn/easy-rsa/pki/ae535e16/temp.c0dd1d7c
Check that the request matches the signature
Signature ok
The Subject's Distinguished Name is as follows
commonName            :ASN.1 12:'server_0D1uuPpBhRt6VMuv'
Certificate is to be certified until Nov 10 13:36:59 2035 GMT (3650 days)

Write out database with 1 new entries
Database updated

Notice
------
Certificate created at:
* /etc/openvpn/easy-rsa/pki/issued/server_0D1uuPpBhRt6VMuv.crt

Notice
------
Inline file created:
* /etc/openvpn/easy-rsa/pki/inline/server_0D1uuPpBhRt6VMuv.inline

* Using SSL: openssl OpenSSL 3.0.17 1 Jul 2025 (Library: OpenSSL 3.0.17 1 Jul 2025)

* Using Easy-RSA configuration: /etc/openvpn/easy-rsa/vars

* The preferred location for 'vars' is within the PKI folder.
  To silence this message move your 'vars' file to your PKI
  or declare your 'vars' file with option: --vars=<FILE>
Using configuration from /etc/openvpn/easy-rsa/pki/0c6ab088/temp.73d88acf

Notice
------
An updated CRL has been created.
CRL file: /etc/openvpn/easy-rsa/pki/crl.pem

2025-11-12 08:36:59 DEPRECATED OPTION: The option --secret is deprecated.
2025-11-12 08:36:59 WARNING: Using --genkey --secret filename is DEPRECATED.  Use --genkey secret filename instead.
* Applying /usr/lib/sysctl.d/10-pve-ct-inotify-limits.conf ...
* Applying /usr/lib/sysctl.d/10-pve.conf ...
* Applying /usr/lib/sysctl.d/50-pid-max.conf ...
* Applying /etc/sysctl.d/99-openvpn.conf ...
* Applying /usr/lib/sysctl.d/99-protect-links.conf ...
* Applying /etc/sysctl.d/99-sysctl.conf ...
* Applying /usr/lib/sysctl.d/pve-firewall.conf ...
* Applying /etc/sysctl.conf ...
fs.inotify.max_queued_events = 8388608
fs.inotify.max_user_instances = 65536
fs.inotify.max_user_watches = 4194304
vm.max_map_count = 262144
net.ipv4.neigh.default.gc_thresh3 = 8192
net.ipv6.neigh.default.gc_thresh3 = 8192
kernel.keys.maxkeys = 2000
net.bridge.bridge-nf-call-ip6tables = 0
net.bridge.bridge-nf-call-iptables = 0
net.bridge.bridge-nf-call-arptables = 0
net.bridge.bridge-nf-filter-vlan-tagged = 0
net.ipv4.igmp_link_local_mcast_reports = 0
fs.aio-max-nr = 1048576
kernel.pid_max = 4194304
net.ipv4.ip_forward = 1
fs.protected_fifos = 1
fs.protected_hardlinks = 1
fs.protected_regular = 2
fs.protected_symlinks = 1
vm.swappiness = 0
net.ipv6.conf.all.disable_ipv6 = 1
net.ipv6.conf.default.disable_ipv6 = 1
net.ipv6.conf.lo.disable_ipv6 = 1
net.ipv4.ip_forward = 1
net.ipv4.conf.all.rp_filter = 2
vm.swappiness = 0
net.ipv6.conf.all.disable_ipv6 = 1
net.ipv6.conf.default.disable_ipv6 = 1
net.ipv6.conf.lo.disable_ipv6 = 1
net.ipv4.ip_forward = 1
Created symlink /etc/systemd/system/multi-user.target.wants/openvpn@server.service → /etc/systemd/system/openvpn@.service.
Created symlink /etc/systemd/system/multi-user.target.wants/iptables-openvpn.service → /etc/systemd/system/iptables-openvpn.service.

Tell me a name for the client.
The name must consist of alphanumeric character. It may also include an underscore or a dash.
Client name: tester1

Do you want to protect the configuration file with a password?
(e.g. encrypt the private key with a password)
   1) Add a passwordless client
   2) Use a password for the client
Select an option [1-2]: 1

* Using SSL: openssl OpenSSL 3.0.17 1 Jul 2025 (Library: OpenSSL 3.0.17 1 Jul 2025)

* Using Easy-RSA configuration: /etc/openvpn/easy-rsa/vars

* The preferred location for 'vars' is within the PKI folder.
  To silence this message move your 'vars' file to your PKI
  or declare your 'vars' file with option: --vars=<FILE>
-----

Notice
------
Keypair and certificate request completed. Your files are:
req: /etc/openvpn/easy-rsa/pki/reqs/tester1.req
key: /etc/openvpn/easy-rsa/pki/private/tester1.key
Using configuration from /etc/openvpn/easy-rsa/pki/6c034c92/temp.d68882ca
Check that the request matches the signature
Signature ok
The Subject's Distinguished Name is as follows
commonName            :ASN.1 12:'tester1'
Certificate is to be certified until Nov 10 13:37:21 2035 GMT (3650 days)

Write out database with 1 new entries
Database updated

Notice
------
Certificate created at:
* /etc/openvpn/easy-rsa/pki/issued/tester1.crt

Notice
------
Inline file created:
* /etc/openvpn/easy-rsa/pki/inline/tester1.inline
Client tester1 added.

The configuration file has been written to /root/tester1.ovpn.
Download the .ovpn file and import it in your OpenVPN client.
```




