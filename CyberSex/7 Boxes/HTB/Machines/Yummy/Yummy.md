
```
kali@kali ~> nmap -sC -sV -Pn 10.129.151.145
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-10-06 16:43 EDT
Nmap scan report for 10.129.151.145
Host is up (0.074s latency).
Not shown: 998 closed tcp ports (conn-refused)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 9.6p1 Ubuntu 3ubuntu13.5 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   256 a2:ed:65:77:e9:c4:2f:13:49:19:b0:b8:09:eb:56:36 (ECDSA)
|_  256 bc:df:25:35:5c:97:24:f2:69:b4:ce:60:17:50:3c:f0 (ED25519)
80/tcp open  http    Caddy httpd
|_http-title: Did not follow redirect to http://yummy.htb/
|_http-server-header: Caddy
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 11.79 seconds
```


https://fusionauth.io/dev-tools/jwt-decoder

---

## Book a table

```
GET /reminder/21 HTTP/1.1

Host: yummy.htb

User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0

Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8

Accept-Language: en-US,en;q=0.5

Accept-Encoding: gzip, deflate, br

Connection: keep-alive

Referer: http://yummy.htb/dashboard

Cookie: X-AUTH-Token=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6InRlc3RAVEVTVC5DT00iLCJyb2xlIjoiY3VzdG9tZXJfZWZlNGViZjciLCJpYXQiOjE3MjgyNDkzNzIsImV4cCI6MTcyODI1Mjk3MiwiandrIjp7Imt0eSI6IlJTQSIsIm4iOiIxNTgzOTc3MTIxMzU4OTMyMzM5OTUzNzAwNzY4MzExNTk4Nzg2NDg1MjIwNDMxMzQzNzU3OTI2NDM5NTYyMDA2OTYzMzk4MDkzMDIyNDc2MDYyMDA3NzY1NTcwMDQ0MTUwMjIxMjAyOTg5MzY4MjU2Mzk0NjUyNzk1MzgzNzQwOTU1MDIyOTQ1MzUyMDQ3OTM0NDA4MDIyNjQ2ODE2MjQ5Njk3NTk5NTUxMjY1NDIyNjg4NTc3Mjg0Nzk5ODE1MTc2NzM4NDE4NjEzNDA3MTg3ODIxNzY0NzQ4NTM0MzcwODMxMjAxMDA3MzUwNTE3ODczMzIzNTk5NDk3NDAwMDgyODA2MzIxMzgwNzA5ODE3NTAzMTMyMDc5ODA4NTAxMTc1MDQyNjU1MDI5ODM4MDQwODA4NTEyMTEwMDMiLCJlIjo2NTUzN319.APwmJsECJjxnMiAONogJVIqKrr2ymauWxSK3fnroaoLkl08reADZjjTimaw7VSbKGxL6KLwYXSdb6vi_Rd44Gah8Mq7N_YT-U6lPGbgzzy_HuZgR7Jf87BkuqZO8Ls_jLLTQ9UbbeEJgvGZHTuQxRAAPhqFKtNYQR_lRa32WTJwV7G0

Upgrade-Insecure-Requests: 1




```


```
GET /export/Yummy_reservation_20241006_211652.ics HTTP/1.1

Host: yummy.htb

User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0

Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8

Accept-Language: en-US,en;q=0.5

Accept-Encoding: gzip, deflate, br

Referer: http://yummy.htb/dashboard

Connection: keep-alive

Cookie: X-AUTH-Token=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6InRlc3RAVEVTVC5DT00iLCJyb2xlIjoiY3VzdG9tZXJfZWZlNGViZjciLCJpYXQiOjE3MjgyNDkzNzIsImV4cCI6MTcyODI1Mjk3MiwiandrIjp7Imt0eSI6IlJTQSIsIm4iOiIxNTgzOTc3MTIxMzU4OTMyMzM5OTUzNzAwNzY4MzExNTk4Nzg2NDg1MjIwNDMxMzQzNzU3OTI2NDM5NTYyMDA2OTYzMzk4MDkzMDIyNDc2MDYyMDA3NzY1NTcwMDQ0MTUwMjIxMjAyOTg5MzY4MjU2Mzk0NjUyNzk1MzgzNzQwOTU1MDIyOTQ1MzUyMDQ3OTM0NDA4MDIyNjQ2ODE2MjQ5Njk3NTk5NTUxMjY1NDIyNjg4NTc3Mjg0Nzk5ODE1MTc2NzM4NDE4NjEzNDA3MTg3ODIxNzY0NzQ4NTM0MzcwODMxMjAxMDA3MzUwNTE3ODczMzIzNTk5NDk3NDAwMDgyODA2MzIxMzgwNzA5ODE3NTAzMTMyMDc5ODA4NTAxMTc1MDQyNjU1MDI5ODM4MDQwODA4NTEyMTEwMDMiLCJlIjo2NTUzN319.APwmJsECJjxnMiAONogJVIqKrr2ymauWxSK3fnroaoLkl08reADZjjTimaw7VSbKGxL6KLwYXSdb6vi_Rd44Gah8Mq7N_YT-U6lPGbgzzy_HuZgR7Jf87BkuqZO8Ls_jLLTQ9UbbeEJgvGZHTuQxRAAPhqFKtNYQR_lRa32WTJwV7G0; session=eyJfZmxhc2hlcyI6W3siIHQiOlsic3VjY2VzcyIsIlJlc2VydmF0aW9uIGRvd25sb2FkZWQgc3VjY2Vzc2Z1bGx5Il19XX0.ZwL-RA.ePuPVkz8TxodaraxgJNKQYP-Co4

Upgrade-Insecure-Requests: 1




```



```
Cookie: X-AUTH-Token=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6InRlc3RAVEVTVC5DT00iLCJyb2xlIjoiY3VzdG9tZXJfYTNlOTNmY2QiLCJpYXQiOjE3MjgyNDc1OTAsImV4cCI6MTcyODI1MTE5MCwiandrIjp7Imt0eSI6IlJTQSIsIm4iOiIxNTgzOTc3MTIxMzU4OTMyMzM5OTUzNzAwNzY4MzExNTk4Nzg2NDg1MjIwNDMxMzQzNzU3OTI2NDM5NTYyMDA2OTYzMzk4MDkzMDIyNDc2MDYyMDA3NzY1NTcwMDQ0MTUwMjIxMjAyOTg5MzY4MjU2Mzk0NjUyNzk1MzgzNzQwOTU1MDIyOTQ1MzUyMDQ3OTM0NDA4MDIyNjQ2ODE2MjQ5Njk3NTk5NTUxMjY1NDIyNjg4NTc3Mjg0Nzk5ODE1MTc2NzM4NDE4NjEzNDA3MTg3ODIxNzY0NzQ4NTM0MzcwODMxMjAxMDA3MzUwNTE3ODczMzIzNTk5NDk3NDAwMDgyODA2MzIxMzgwNzA5ODE3NTAzMTMyMDc5ODA4NTAxMTc1MDQyNjU1MDI5ODM4MDQwODA4NTEyMTEwMDMiLCJlIjo2NTUzN319.AYtsFlDVrz7aMUZUOnKI3he4V5vAVNCZbzn1gCaYS-T9c27v-UVOrfhTZ2fMeW4P9kh7WU_Xs2rf3czScia4kHGUw5U0iTMLWn06SJXVxDYNpmQgZSgbWOEVL4TtBKR7r166vB2X1aUgb_4W6SfnE4rPHy6i40SGON8zqT3xpbb3roE
```

```
{
  "alg": "RS256",
  "typ": "JWT"
}
```

```
{
  "email": "test@TEST.COM",
  "role": "customer_a3e93fcd",
  "iat": 1728247590,
  "exp": 1728251190,
  "jwk": {
    "kty": "RSA",
    "n": "158397712135893233995370076831159878648522043134375792643956200696339809302247606200776557004415022120298936825639465279538374095502294535204793440802264681624969759955126542268857728479981517673841861340718782176474853437083120100735051787332359949740008280632138070981750313207980850117504265502983804080851211003",
    "e": 65537
  }
}
```



```
session=eyJfZmxhc2hlcyI6W3siIHQiOlsic3VjY2VzcyIsIlJlc2VydmF0aW9uIGRvd25sb2FkZWQgc3VjY2Vzc2Z1bGx5Il19XX0.ZwL5qQ.Wp8GbbfhAzXpGUWXSNuAjGQrRBc
```


![[Yummy-20241007002246148.webp]]