---
tags:
  - tool
  - hash_cracking
---
# john

Crack hashes (slower than hashcat)

## Capabilities

```bash
# Crack a hash
john --wordlist=/usr/share/wordlists/rockyou.txt hash

# Crack a hash with a rule list
john --wordlist=/usr/share/wordlists/rockyou.txt --rules=exampleRules hash
```

To use a hashcat rule file, prepend a compatibility line and append it to `/etc/john/john.conf`

**Contents of example.rules**

```
[List.Rules:exampleRules]
c $1 $3 $7 $!
c $1 $3 $7 $@
c $1 $3 $7 $#
```

```bash
sudo sh -c 'cat /home/kali/oscp/course/password_attacks/rule >> /etc/john/john.conf'
```






if i ever wanna crack something and dont know howto convert it use john 


```
kali@kali ~/t/s/nfs> ls /usr/share/john
1password2john.py*      dumb16.conf                    ldif2john.pl*              pse2john.py*
7z2john.pl*             dumb32.conf                    leet.pl*                   ps_token2john.py*
adxcsouf2john.py*       dynamic.conf                   lib/                       pwsafe2john.py*
aem2john.py*            dynamic_disabled.conf          libreoffice2john.py*       __pycache__/
aix2john.pl*            dynamic_flat_sse_formats.conf  lion2john-alt.pl*          radius2john.pl*
aix2john.py*            ecryptfs2john.py*              lion2john.pl*              radius2john.py*
alnum.chr               ejabberd2john.py*              lm_ascii.chr               regex_alphabets.conf
alnumspace.chr          electrum2john.py*              lotus2john.py*             repeats16.conf
alpha.chr               encfs2john.py*                 lower.chr                  repeats32.conf
andotp2john.py*         enpass2john.py*                lowernum.chr               restic2john.py*
androidbackup2john.py*  enpass5tojohn.py*              lowerspace.chr             rexgen2rules.pl*
androidfde2john.py*     ethereum2john.py*              luks2john.py*              rockyou.txt
ansible2john.py*        filezilla2john.py*             mac2john-alt.py*           rules/
apex2john.py*           fuzz.dic                       mac2john.py*               rulestack.pl*
applenotes2john.py*     fuzz_option.pl*                mcafee_epo2john.py*        sap2john.pl*
aruba2john.py*          geli2john.py*                  monero2john.py*            sense2john.py*
ascii.chr               genincstats.rb*                money2john.py*             sha-dump.pl*
atmail2john.pl*         hccapx2john.py*                mosquitto2john.py*         sha-test.pl*
axcrypt2john.py*        hextoraw.pl*                   mozilla2john.py*           signal2john.py*
bestcrypt2john.py*      htdigest2john.py*              multibit2john.py*          sipdump2john.py*
bestcryptve2john.py     hybrid.conf                    neo2john.py*               ssh2john.py*
bitcoin2john.py*        ibmiscanner2john.py*           netntlm.pl*                sspr2john.py*
bitshares2john.py*      ikescan2john.py*               netscreen.py*              staroffice2john.py*
bitwarden2john.py*      ios7tojohn.pl*                 office2john.py*            stats
bks2john.py*            itunes_backup2john.pl*         openbsd_softraid2john.py*  strip2john.py*
blockchain2john.py*     iwork2john.py*                 openssl2john.py*           telegram2john.py*
ccache2john.py*         john.conf                      padlock2john.py*           test_tezos2john.py
cisco2john.pl*          kdcdump2john.py*               pass_gen.pl*               tezos2john.py*
codepage.pl*            keychain2john.py*              password.lst               truecrypt2john.py*
cracf2john.py*          keyring2john.py*               pcap2john.py*              unisubst.conf
cronjob*                keystore2john.py*              pdf2john.pl*               unrule.pl*
dashlane2john.py*       kirbi2john.py*                 pem2john.py*               upper.chr
deepsound2john.py*      known_hosts2john.py*           pfx2john.py*               uppernum.chr
dictionary.rfc2865      korelogic.conf                 pgpdisk2john.py*           utf8.chr
digits.chr              krb2john.py*                   pgpsda2john.py*            vdi2john.pl*
diskcryptor2john.py*    kwallet2john.py*               pgpwde2john.py*            vmx2john.py*
dmg2john.py*            lanman.chr                     pkcs12kdf.py               zed2john.py*
dns/                    lastpass2john.py*              potcheck.pl*               ztex/
DPAPImk2john.py*        latin1.chr                     prosody2john.py*

```