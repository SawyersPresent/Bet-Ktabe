
```
[17:22:40] Starting:
[17:22:49] 403 -  281B  - /.ht_wsr.txt
[17:22:49] 403 -  281B  - /.htaccess.bak1
[17:22:49] 403 -  281B  - /.htaccess.sample
[17:22:49] 403 -  281B  - /.htaccess.save
[17:22:49] 403 -  281B  - /.htaccess.orig
[17:22:49] 403 -  281B  - /.htaccess_sc
[17:22:49] 403 -  281B  - /.htaccess_extra
[17:22:49] 403 -  281B  - /.htaccessOLD
[17:22:49] 403 -  281B  - /.htaccessOLD2
[17:22:49] 403 -  281B  - /.htaccessBAK
[17:22:49] 403 -  281B  - /.htaccess_orig
[17:22:49] 403 -  281B  - /.htm
[17:22:49] 403 -  281B  - /.html
[17:22:49] 403 -  281B  - /.htpasswd_test
[17:22:49] 403 -  281B  - /.httr-oauth
[17:22:49] 403 -  281B  - /.htpasswds
[17:22:52] 403 -  281B  - /.php
[17:33:31] 200 -  108B  - /robots.txt
[17:33:34] 403 -  281B  - /server-status
[17:33:34] 403 -  281B  - /server-status/
[17:33:57] 200 -    2KB - /wordpress/wp-login.php
[17:33:57] 200 -   10KB - /wordpress/

```



`DANTE{Y0u_Cant_G3t_at_m3_br0!}`

```
[17:26:26] Starting: wordpress/
[17:26:40] 403 -  281B  - /wordpress/.htaccess.bak1
[17:26:40] 403 -  281B  - /wordpress/.ht_wsr.txt
[17:26:40] 403 -  281B  - /wordpress/.htaccess.sample
[17:26:40] 403 -  281B  - /wordpress/.htaccess.orig
[17:26:40] 403 -  281B  - /wordpress/.htaccess.save
[17:26:40] 403 -  281B  - /wordpress/.htaccess_orig
[17:26:40] 403 -  281B  - /wordpress/.htaccess_sc
[17:26:40] 403 -  281B  - /wordpress/.htaccess_extra
[17:26:40] 403 -  281B  - /wordpress/.htaccessOLD
[17:26:40] 403 -  281B  - /wordpress/.htaccessBAK
[17:26:40] 403 -  281B  - /wordpress/.htaccessOLD2
[17:26:40] 403 -  281B  - /wordpress/.htm
[17:26:40] 403 -  281B  - /wordpress/.html
[17:26:40] 403 -  281B  - /wordpress/.htpasswds
[17:26:40] 403 -  281B  - /wordpress/.httr-oauth
[17:26:40] 403 -  281B  - /wordpress/.htpasswd_test
[17:26:42] 403 -  281B  - /wordpress/.php
[17:26:46] 200 -   12KB - /wordpress/.wp-config.php.swp
[17:27:48] 404 -   36KB - /wordpress/index.php/login/
[17:27:52] 200 -    7KB - /wordpress/license.txt
[17:27:55] 301 -    0B  - /wordpress/index.php  ->  http://10.10.110.100:65000/wordpress/
[17:28:14] 200 -    3KB - /wordpress/readme.html
[17:28:16] 200 -   34B  - /wordpress/robots.txt
[17:28:43] 200 -  558B  - /wordpress/wp-admin/install.php
[17:28:43] 301 -  336B  - /wordpress/wp-admin  ->  http://10.10.110.100:65000/wordpress/wp-admin/
[17:28:43] 500 -    3KB - /wordpress/wp-admin/setup-config.php
[17:28:43] 302 -    0B  - /wordpress/wp-admin/  ->  http://10.10.110.100:65000/wordpress/wp-login.php?redirect_to=http%3A%2F%2F10.10.110.100%3A65000%2Fwordpress%2Fwp-admin%2F&reauth=1
[17:28:43] 400 -    1B  - /wordpress/wp-admin/admin-ajax.php
[17:28:43] 200 -    0B  - /wordpress/wp-config.php
[17:28:44] 200 -    0B  - /wordpress/wp-content/
[17:28:44] 301 -  338B  - /wordpress/wp-content  ->  http://10.10.110.100:65000/wordpress/wp-content/
[17:28:45] 200 -    3KB - /wordpress/wp-content/debug.log
[17:28:45] 500 -    0B  - /wordpress/wp-content/plugins/hello.php
[17:28:45] 200 -  462B  - /wordpress/wp-content/uploads/
[17:28:45] 200 -   84B  - /wordpress/wp-content/plugins/akismet/akismet.php
[17:28:46] 301 -  339B  - /wordpress/wp-includes  ->  http://10.10.110.100:65000/wordpress/wp-includes/
[17:28:46] 200 -    4KB - /wordpress/wp-includes/
[17:28:46] 200 -    0B  - /wordpress/wp-cron.php
[17:28:46] 200 -    2KB - /wordpress/wp-login.php
[17:28:46] 500 -    0B  - /wordpress/wp-includes/rss-functions.php
[17:28:46] 302 -    0B  - /wordpress/wp-signup.php  ->  http://10.10.110.100:65000/wordpress/wp-login.php?action=register
[17:28:47] 405 -   42B  - /wordpress/xmlrpc.php

Task Completed

```



`http://10.10.110.100:65000/wordpress/wordpress/.wp-config.php.swp`


## Wordpress


James:Toyota

Upload reverse shell to twentynineteen itll work

