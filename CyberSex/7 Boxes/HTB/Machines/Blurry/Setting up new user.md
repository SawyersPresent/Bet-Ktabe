
GETTING STARTED
Get started in a jiffy:
1. Install



```
pip install clearml
```

Run the ClearML setup script
pip install clearml
2. Configure
	1. Local
		1. Run the ClearML setup scrip
		2. `clearml-init`
	2. Notebook
		1. `%env CLEARML_WEB_HOST=http://app.blurry.htb`
		2. `%env CLEARML_API_HOST=http://api.blurry.htb`
		3. `%env CLEARML_FILES_HOST=http://files.blurry.htb`
		4. `%env CLEARML_API_ACCESS_KEY=<You’re API access key>`   <--------------------
		5. `%env CLEARML_API_SECRET_KEY=<You’re API secret key>`   <--------------------
	3. Complete the clearml configuration information as prompted.
4. Integrate
	1. Add ClearML to your code. For example:
```
from clearml import Task
task = Task.init(project_name="my project", task_name="my task")
```

im using the local btw dont forget saif

```
api {
  web_server: http://app.blurry.htb
  api_server: http://api.blurry.htb
  files_server: http://files.blurry.htb
  credentials {
    "access_key" = "ZYWU1KP5ZCRAU7JRSS9J"
    "secret_key" = "yARuMIowdxHKjJRZjyI7NA6qdnFdJN9KntzEDAfE7pH1ZxWerx"
  }
}

```


(they launch automatically usually)

Execute any draft task manually using:
```
clearml-agent execute --id 
```



Projects visible

| TYPE            | TITLE                 | PROJECT    | STARTED           | UPDATED           | STATUS    |
| --------------- | --------------------- | ---------- | ----------------- | ----------------- | --------- |
| Data Processing | Review JSON Artifacts | Black Swan | Jun 10 2024 8:18  | Jun 10 2024 8:18  | Completed |
| Training        | pickle_an             | AN_HTB     | Jun 10 2024 5:53  | Jun 10 2024 5:57  | Published |
| Data Processing | Review JSON Artifacts | Black Swan | Jun 3 2024 9:28   | Jun 3 2024 9:28   | Completed |
| Data Processing | Review JSON Artifacts | Black Swan | Jun 3 2024 9:22   | Jun 3 2024 9:22   | Completed |
| Data Processing | Review JSON Artifacts | Black Swan | May 30 2024 10:32 | May 30 2024 10:32 | Completed |


Picke-an looks interesting

