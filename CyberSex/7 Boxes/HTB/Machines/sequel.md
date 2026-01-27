

```python
Not shown: 988 filtered tcp ports (no-response)
PORT     STATE SERVICE       VERSION
53/tcp   open  domain        Simple DNS Plus
88/tcp   open  kerberos-sec  Microsoft Windows Kerberos (server time: 2025-01-12 19:53:30Z)
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn                                                           
389/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: sequel.htb0., Site: Default-First-Site-Name)
| ssl-cert: Subject: commonName=DC01.sequel.htb                                                                      
| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1::<unsupported>, DNS:DC01.sequel.htb                      
| Not valid before: 2024-06-08T17:35:00                                                                              
|_Not valid after:  2025-06-08T17:35:00                                                                              
|_ssl-date: 2025-01-12T19:54:50+00:00; +1m40s from scanner time.                                                     
445/tcp  open  microsoft-ds?                                                                                         
464/tcp  open  kpasswd5?                                                                                             
593/tcp  open  ncacn_http    Microsoft Windows RPC over HTTP 1.0                                                     
636/tcp  open  ssl/ldap      Microsoft Windows Active Directory LDAP (Domain: sequel.htb0., Site: Default-First-Site-Name)
|_ssl-date: 2025-01-12T19:54:50+00:00; +1m40s from scanner time.
| ssl-cert: Subject: commonName=DC01.sequel.htb
| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1::<unsupported>, DNS:DC01.sequel.htb
| Not valid before: 2024-06-08T17:35:00
|_Not valid after:  2025-06-08T17:35:00
1433/tcp open  ms-sql-s      Microsoft SQL Server 2019 15.00.2000.00; RTM
|_ssl-date: 2025-01-12T19:54:50+00:00; +1m40s from scanner time.
| ssl-cert: Subject: commonName=SSL_Self_Signed_Fallback
| Not valid before: 2025-01-12T15:25:36
|_Not valid after:  2055-01-12T15:25:36
| ms-sql-ntlm-info: 
|   10.129.242.46:1433: 
|     Target_Name: SEQUEL
|     NetBIOS_Domain_Name: SEQUEL
|     NetBIOS_Computer_Name: DC01
|     DNS_Domain_Name: sequel.htb
|     DNS_Computer_Name: DC01.sequel.htb
|     DNS_Tree_Name: sequel.htb
|_    Product_Version: 10.0.17763
| ms-sql-info: 
|   10.129.242.46:1433: 
|     Version: 
|       name: Microsoft SQL Server 2019 RTM
|       number: 15.00.2000.00
|       Product: Microsoft SQL Server 2019
|       Service pack level: RTM
|       Post-SP patches applied: false
|_    TCP port: 1433
3268/tcp open  ldap          Microsoft Windows Active Directory LDAP (Domain: sequel.htb0., Site: Default-First-Site-Name)
|_ssl-date: 2025-01-12T19:54:50+00:00; +1m40s from scanner time.
| ssl-cert: Subject: commonName=DC01.sequel.htb
| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1::<unsupported>, DNS:DC01.sequel.htb
| Not valid before: 2024-06-08T17:35:00
|_Not valid after:  2025-06-08T17:35:00
3269/tcp open  ssl/ldap      Microsoft Windows Active Directory LDAP (Domain: sequel.htb0., Site: Default-First-Site-Name)
| ssl-cert: Subject: commonName=DC01.sequel.htb
| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1::<unsupported>, DNS:DC01.sequel.htb
| Not valid before: 2024-06-08T17:35:00
|_Not valid after:  2025-06-08T17:35:00
|_ssl-date: 2025-01-12T19:54:50+00:00; +1m40s from scanner time.
Service Info: Host: DC01; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-time: 
|   date: 2025-01-12T19:54:11
|_  start_date: N/A
|_clock-skew: mean: 1m39s, deviation: 0s, median: 1m39s
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled and required

```



```python
This XML file does not appear to have any style information associated with it. The document tree is shown below.  

<sst xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" count="25" uniqueCount="24">

<si>

<t xml:space="preserve">First Name</t>

</si>

<si>

<t xml:space="preserve">Last Name</t>

</si>

<si>

<t xml:space="preserve">Email</t>

</si>

<si>

<t xml:space="preserve">Username</t>

</si>

<si>

<t xml:space="preserve">Password</t>

</si>

<si>
------------------------------------------------------
<t xml:space="preserve">Angela</t>

</si>

<si>

<t xml:space="preserve">Martin</t>

</si>

<si>

<t xml:space="preserve">angela@sequel.htb</t>

</si>

<si>

<t xml:space="preserve">angela</t>

</si>

<si>

<t xml:space="preserve">0fwz7Q4mSpurIt99</t>

</si>

<si>
------------------------------------------------------
<t xml:space="preserve">Oscar</t>

</si>

<si>

<t xml:space="preserve">Martinez</t>

</si>

<si>

<t xml:space="preserve">oscar@sequel.htb</t>

</si>

<si>

<t xml:space="preserve">oscar</t>

</si>

<si>

<t xml:space="preserve">86LxLBMgEWaKUnBG</t>

</si>

<si>
------------------------------------------------------
<t xml:space="preserve">Kevin</t>

</si>

<si>

<t xml:space="preserve">Malone</t>

</si>

<si>

<t xml:space="preserve">kevin@sequel.htb</t>

</si>

<si>

<t xml:space="preserve">kevin</t>

</si>

<si>

<t xml:space="preserve">Md9Wlq1E5bZnVDVo</t>

</si>

<si>

<t xml:space="preserve">NULL</t>

</si>

<si>
------------------------------------------------------------------
<t xml:space="preserve">sa@sequel.htb</t>

</si>

<si>

<t xml:space="preserve">sa</t>

</si>

<si>

<t xml:space="preserve">MSSQLP@ssw0rd!</t>

</si>

</sst>
```


```
PS C:\sql2019\ExpressAdv_ENU> type sql-Configuration.INI
[OPTIONS]
ACTION="Install"
QUIET="True"
FEATURES=SQL
INSTANCENAME="SQLEXPRESS"
INSTANCEID="SQLEXPRESS"
RSSVCACCOUNT="NT Service\ReportServer$SQLEXPRESS"
AGTSVCACCOUNT="NT AUTHORITY\NETWORK SERVICE"
AGTSVCSTARTUPTYPE="Manual"
COMMFABRICPORT="0"
COMMFABRICNETWORKLEVEL=""0"
COMMFABRICENCRYPTION="0"
MATRIXCMBRICKCOMMPORT="0"
SQLSVCSTARTUPTYPE="Automatic"
FILESTREAMLEVEL="0"
ENABLERANU="False" 
SQLCOLLATION="SQL_Latin1_General_CP1_CI_AS"
SQLSVCACCOUNT="SEQUEL\sql_svc"
SQLSVCPASSWORD="WqSZAF6CysDQbGb3"

```