
### BloodHound

By far, the most popular tool for enumerating Active Directory is [BloodHound](https://github.com/SpecterOps/BloodHound). The tool allows us to visualize the relationships and permissions within the domain, making it easier to identify potential attack paths. BloodHound has 2 products: `Enterprise` and `Community Edition`. The Enterprise Edition is a paid product that provides additional features, while the Community Edition is free and open-source.

However many people still prefer using the [`Legacy` version of BloodHound](https://github.com/SpecterOps/BloodHound-Legacy), which was the original version of the tool. The Legacy version is still available, but is no longer being maintained nor updated. 

#### Installation (CE)

1. installing docker / docker desktop would be the first step 
2. Download the latest release of **[Bloodhound CLI](https://github.com/SpecterOps/bloodhound-cli/releases)** for your operating system and architecture (AMD or ARM) and unpack the file. BloodHound CLI is a utility that makes it easy to install BloodHound Community Edition in containers on your machine. To avoid the software getting blocked as malware in the browser, we recommend downloading it via command line using the following commands ([substitute your architecture as appropriate](https://github.com/SpecterOps/bloodhound-cli/releases/latest)):

```
wget https://github.com/SpecterOps/bloodhound-cli/releases/latest/download/bloodhound-cli-linux-amd64.tar.gz
```

3. Next step would be to unpack the file downloaded

```
tar -xvzf bloodhound-cli-linux-amd64.tar.gz
```

4. now using the CLI itll be used to install 

```
./bloodhound-cli install
```

5. after the installation is done, make sure to pay attention to the output as a randomly generated password would be displayed

```
 Container bloodhound-graph-db-1  Created
 Container bloodhound-bloodhound-1  Creating
 Container bloodhound-bloodhound-1  Created
 Container bloodhound-graph-db-1  Starting
 Container bloodhound-app-db-1  Starting
 Container bloodhound-app-db-1  Started
 Container bloodhound-graph-db-1  Started
 Container bloodhound-graph-db-1  Waiting
 Container bloodhound-app-db-1  Waiting
 Container bloodhound-app-db-1  Healthy
 Container bloodhound-graph-db-1  Healthy
 Container bloodhound-bloodhound-1  Starting
 Container bloodhound-bloodhound-1  Started
[+] BloodHound is ready to go!
[+] You can log in as `admin` with this password: aW90ZF8ImvhtR8jAcWcMUyCz3QJSvBhL
[+] You can get your admin password by running: bloodhound-cli config get default_password
[+] You can access the BloodHound UI at: http://127.0.0.1:8080/ui/login
```

**DISCLAIER:** If you never forget your password then there is a quick password reset solution prepared in the bloodhound-cli binary

```
./bloodhound-cli resetpwd
```


6. Once this is all said and done head to  `http://127.0.0.1:8080/ui/login` and login with the credentials provided once the setup process was completed


#### Data Collection (CE)

**Option 1: Remote Collection**

For the CE version of bloodhound & legacy their ingestors are NOT backwards compatible hence you need to install the correct ingestors for each. We will start off by installing bloodhound-ce-python which will allows to collect data remotely

Dependencies:

```
pipx install bloodhound-ce
```

after installing it using pipx should display the output and what the binary is named

```
  installed package bloodhound-ce 1.8.0, installed using Python 3.13.3
  These apps are now globally available
    - bloodhound-ce-python
done! ✨ 🌟 ✨
```


To then use Bloodhound-ce-python its the same syntax as the normal bloodhound-python

```
bloodhound-ce-python -d asia.earth.local. -u 'async_testuser-001' -p 'P@ssw0rd' -ns 10.5.10.20 -c all --zip --dns-timeout 60 --dns-tcp
```


**Installing Rusthound**

```
git clone https://github.com/g0h4n/RustHound-CE.git
```

```
cd Rusthound-CE
make install
```

```
rusthound-ce -d asia.earth.local -u 'async_testuser-001' -p 'P@ssw0rd' -n 10.2.10.20 -c All -z
```



**NXC Module**


For the NXC Module its abit more tricky, to split up the issue simply. 


```
nxc ldap asia.earth.local -u 'T1-J.BARTOLEMO' -p 'Jp@ssW0rd!@' --bloodhound -c all --dns-server 10.5.10.20 -d asia.earth.local.
```





**Option 2: Local Collection**


SharpHound

```
unzip sharphound-v2.6.7.zip
```


1. To download the ingestor move your mouse to the left side of the screen there should be a `Download Collectors` button which is used to download the ingestors
2. After downloading the zip file, extract it where you please



![[Bloodhound-20250623144102201.webp|1028]]




![[Bloodhound-20250623144321152.webp|752]]



![[Bloodhound-20250623145035890.webp|1101]]


Using the collector that was downloaded, Use whatever preferred file transfer method to upload the collector. An **Important** note is to NOT use winrm when doing this entire process due to being affected by the Kerberos double hop problem, so its best to use SSH instead


```
PS C:\Users\async_testuser-001> cd Downloads
PS C:\Users\async_testuser-001\Downloads> klist

Current LogonId is 0:0x180d2da

Cached Tickets: (1)

#0>     Client: async_testuser-001 @ ASIA.EARTH.LOCAL
        Server: krbtgt/ASIA.EARTH.LOCAL @ ASIA.EARTH.LOCAL
        KerbTicket Encryption Type: AES-256-CTS-HMAC-SHA1-96
        Ticket Flags 0x40e10000 -> forwardable renewable initial pre_authent name_canonicalize 
        Start Time: 6/24/2025 13:32:04 (local)
        End Time:   6/24/2025 23:32:04 (local)
        Renew Time: 7/1/2025 13:32:04 (local)
        Session Key Type: AES-256-CTS-HMAC-SHA1-96
        Cache Flags: 0x1 -> PRIMARY 
        Kdc Called: dc02.asia.earth.local
```


As we can see here there is a ticket present hence we have a connection available to the domain 


```
PS C:\Users\async_testuser-001\Downloads> .\SharpHound.exe -c all 
2025-06-24T13:33:09.0051841+08:00|INFORMATION|This version of SharpHound is compatible with the 5.0.0 Release of BloodHound
2025-06-24T13:33:09.1457890+08:00|INFORMATION|Resolved Collection Methods: Group, LocalAdmin, GPOLocalGroup, Session, LoggedOn, Trusts, ACL, Container, RDP, ObjectProps, DCOM, SPNTargets, PSRemote, UserRights, CARegistry, DCRegistry, CertServices, LdapServices, WebClientService, SmbInfo, NTLMRegistry
2025-06-24T13:33:09.1927010+08:00|INFORMATION|Initializing SharpHound at 1:33 PM on 6/24/2025
2025-06-24T13:33:09.2551774+08:00|INFORMATION|Resolved current domain to asia.earth.local
2025-06-24T13:33:09.4113482+08:00|INFORMATION|Flags: Group, LocalAdmin, GPOLocalGroup, Session, LoggedOn, Trusts, ACL, Container, RDP, ObjectProps, DCOM, SPNTargets, PSRemote, UserRights, CARegistry, DCRegistry, CertServices, LdapServices, WebClientService, SmbInfo, NTLMRegistry
2025-06-24T13:33:09.5364227+08:00|INFORMATION|Beginning LDAP search for asia.earth.local
[...CUT...]
2025-06-24T13:33:31.7551167+08:00|INFORMATION|Status: 1132 objects finished (+1132 51.45454)/s -- Using 65 MB RAM
2025-06-24T13:33:31.7551167+08:00|INFORMATION|Enumeration finished in 00:00:22.2371609
2025-06-24T13:33:31.8644890+08:00|INFORMATION|Saving cache with stats: 97 ID to type mappings.
 4 name to SID mappings.
 8 machine sid mappings.
 7 sid to domain mappings.
 0 global catalog mappings.
2025-06-24T13:33:31.8957940+08:00|INFORMATION|SharpHound Enumeration Completed at 1:33 PM on 6/24/2025! Happy Graphing!
PS C:\Users\async_testuser-001\Downloads> ls


    Directory: C:\Users\async_testuser-001\Downloads


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a----         6/24/2025   1:33 PM          65280 20250624133321_BloodHound.zip
-a----         6/24/2025  10:19 AM        1286656 SharpHound.exe
-a----         6/24/2025   1:27 PM        1582265 SharpHound.ps1
-a----         6/24/2025   1:33 PM           6970 YmE2Nzk0MjYtNzA0Ny00NDQ5LTg3MTQtNGM1N2I3ODA3OWZk.bin
```


 Once the zip file is saved, exfiltrate it to your host machine and then (if your bloodhound CE is empty) click on the file ingest button within the "No data available" pop up 


![[Bloodhound-20250623152728874.webp|949]]


To then to get to the upload section click on the upload file button


![[Bloodhound-20250623152822400.webp|859]]

Proceeded you will be met the menu to drop your files in.


![[Bloodhound-20250623153535577.webp|908]]

After doing so click on upload and proceed


![[Bloodhound-20250623153613935.webp|813]]


Confirm your zip selected for the upload

![[Bloodhound-20250623153644408.webp|734]]


Now bloodhound is in the process of ingesting the information provided, this processes usually doesnt take more than ~1 minute, regardless its less about the amount of users and more so about the amount of ACL's that are present in the domain that need to be rendered, it comes to a point where if the amount of edges present are in the thousands then using bloodhound is just not viable


![[Bloodhound-20250623153745019.webp|912]]


Now the ingesting process is completed!


![[Bloodhound-20250623155803268.webp|1057]]



Now we can head over to the explore page and look at the queries present to explore the domain.


![[Bloodhound-20250623155917462.webp|1059]]








---

#### Installation (Legacy)

Now we install neo4j

```
sudo apt install neo4j
```

Starting it 

```
sudo neo4j start
```


Now to Installing Bloodhound-GUI itself

one simple method would be using the simple 

```
sudo apt install bloodhound
```

This automatically downloads the legacy version, The second method would be heading to The [Bloodhound Legacy](https://github.com/SpecterOps/BloodHound-Legacy/releases) repository and then download the latest release file, After doing so unzip the folder and run it with the `--no-sandbox` flag,   

```
./Bloodhound --no-sandbox
```

then proceed to authenticate to bloodhound with your neo4j credentials


#### Data Collection (Legacy)

With collection there are multiple methods in doing so. 

The first method would be using Bloodhound-python 

```
kali@kali ~/work> bloodhound-python -d asia.earth.local. -u 'async_testuser-001' -p 'P@ssw0rd' -ns 10.5.10.20 -c all --zip
INFO: BloodHound.py for BloodHound LEGACY (BloodHound 4.2 and 4.3)
INFO: Found AD domain: asia.earth.local
WARNING: Could not find a global catalog server, assuming the primary DC has this role
If this gives errors, either specify a hostname with -gc or disable gc resolution with --disable-autogc
INFO: Getting TGT for user
WARNING: Failed to get Kerberos TGT. Falling back to NTLM authentication. Error: Kerberos SessionError: KRB_AP_ERR_SKEW(Clock skew too great)
INFO: Connecting to LDAP server: dc02.asia.earth.local
INFO: Found 1 domains
INFO: Found 2 domains in the forest
INFO: Found 9 computers
INFO: Connecting to LDAP server: dc02.asia.earth.local
INFO: Connecting to GC LDAP server: dc02.asia.earth.local
INFO: Found 800 users
INFO: Found 83 groups
INFO: Found 2 gpos
INFO: Found 1 ous
INFO: Found 19 containers
INFO: Found 1 trusts
INFO: Starting computer enumeration with 10 workers
INFO: Querying computer: staging01.asia.earth.local
INFO: Querying computer: pt01.asia.earth.local
INFO: Querying computer: sql01.asia.earth.local
INFO: Querying computer: fs01.asia.earth.local
INFO: Querying computer: dev-pc003.asia.earth.local
INFO: Querying computer: dev-pc002.asia.earth.local
INFO: Querying computer: dev-pc001.asia.earth.local
INFO: Querying computer: web01.asia.earth.local
INFO: Querying computer: dc02.asia.earth.local
INFO: Done in 01M 37S
INFO: Compressing output into 20250624011824_bloodhound.zip
```











The third which works is rusthound

```
kali@kali ~/work> rusthound --domain asia.earth.local -u 'async_testuser-001' -p 'P@ssw0rd' -n 10.2.10.20 -z
---------------------------------------------------
Initializing RustHound at 01:20:41 on 06/24/25
Powered by g0h4n from OpenCyber
---------------------------------------------------

[2025-06-24T05:20:41Z INFO  rusthound] Verbosity level: Info
[2025-06-24T05:20:41Z INFO  rusthound::ldap] Connected to ASIA.EARTH.LOCAL Active Directory!
[2025-06-24T05:20:41Z INFO  rusthound::ldap] Starting data collection...
[2025-06-24T05:20:44Z INFO  rusthound::ldap] All data collected for NamingContext DC=asia,DC=earth,DC=local
[2025-06-24T05:20:44Z INFO  rusthound::json::parser] Starting the LDAP objects parsing...
[2025-06-24T05:20:44Z INFO  rusthound::json::parser::bh_41] MachineAccountQuota: 10
[2025-06-24T05:20:45Z INFO  rusthound::json::parser] Parsing LDAP objects finished!
[2025-06-24T05:20:45Z INFO  rusthound::json::checker] Starting checker to replace some values...
[2025-06-24T05:20:45Z INFO  rusthound::json::checker] Checking and replacing some values finished!
[2025-06-24T05:20:45Z INFO  rusthound::json::maker] 801 users parsed!
[2025-06-24T05:20:45Z INFO  rusthound::json::maker] 91 groups parsed!
[2025-06-24T05:20:45Z INFO  rusthound::json::maker] 9 computers parsed!
[2025-06-24T05:20:45Z INFO  rusthound::json::maker] 1 ous parsed!
[2025-06-24T05:20:45Z INFO  rusthound::json::maker] 1 domains parsed!
[2025-06-24T05:20:45Z INFO  rusthound::json::maker] 2 gpos parsed!
[2025-06-24T05:20:45Z INFO  rusthound::json::maker] 21 containers parsed!
[2025-06-24T05:20:45Z INFO  rusthound::json::maker] .//20250624012045_asia-earth-local_rusthound.zip created!

RustHound Enumeration Completed at 01:20:45 on 06/24/25! Happy Graphing!

```




