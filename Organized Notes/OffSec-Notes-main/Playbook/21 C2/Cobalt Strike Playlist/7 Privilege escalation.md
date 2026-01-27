Table of contents
- escalation
	- exploits and elevators
	- misconfigurations
		- SharpUp
		- kerberoasting
	- Credentials
- Bypass UAC & get SYSTEM
- Credential & Harvesting
- mimikatz in beacon



### elevate & misc

- List privilege escalation options
	- Elevate
	- spawn an elevated session
		- elevate (module) (listener)
		  (session) -> access -> elevate 
- List command elevators
	- RunAsAdmin
	- Run a command in elevated context
		- runasadmin (module) (command)
- Elevate vs RunAsAdmin
	- Elevate
		- is to spawn an elevated session
	- runasadmin
		- you get to choose how to use this primitive in a way that makes sense for your situation
		- bring your own weaponization!
			- Drop an EXE to disk and run it
			- running commands on weakened target
			- use (session) -> Access -> One-liner to generate a PowerShell oneliner to spawn a session
- Spawn As
	- Use credentials to spawn a session as another user
	- (beacon) -> access -> spawn as
	- pay attention to the cwd, if your in a direcetory or the beacon cannot read or the new session cant read then the sessions going tofail
	- the command parser is position based, 



### PrivEsc using third parties like metasploit





- The escalation problem set
	- I have no right/privileges to anything better?
	- "I am an administrator, but dont have administrator rights."
	- "WTF?!?, I am in an elevated context but I cant do what I want to do."
- When you have for example an administrator user but dont have administrator rights, you think you have full rights but you cant do what you really want to do?
- UAC (User Account Control)
	- Introduced in windows Vista
	- three levels of process integrity
		- high (administrator rights)
		- medium (standard user rights)
		- low (restricted rights)
	- Local administrator
		- Run as standard user (medium integrity)
		- Must elevate to assume full rights (full integrity)
		- UAC bypass scenario!
	- For situation awareness use `whoami /all`
		- look at what groups your in 
		- Look at what integrity level your process is running at
	- How to bypass UAC?
		- use `elevate uac-token-duplication (listener)`
			- Fixed in windows 10 RS5 (october 2018)
			- NOTE: this attacks privileged context cannot interact with processes in other desktop sessions
		- or `runasadmin uac-cmstplua (command)`
			- note: COM elevation in some process contexts will always prompt and BLOCK your beacon agent
		- or... options in the elevate kit


to abuse this in CS it goes as follows

```
oneliner (create a oneliner)

runasadmin uac-cmstplua powershell -nop -exec bypass -EncodedCommand <BASE64_PAYLOAD_HERE>

#connect once more using local host
connect 127.0.0.1:9292
```


- access token
	- created after logon
	- associated with each process and thread
	- contains:
		- user and group information
		- a list of privileges on local computer
		- restrictions (user/group rights taken away)
		- reference to credentials (supports single sign-on)
	- Persists in memory until reboot
	- token privileges
		- which privileges does your token have?
			- `run whoami /priv`
			- enable the disabled privs with `getprivs` in beacon
				- **note**: probably very sus
			- powerful privileges
				- SeCreateTokenPrivilege
				- SeDebugPrivilege
				- SeTcbPrivilege
- `get SYSTEM`
	- One way to privesc is to try and get the `SYSTEM` Token
	- often it has full set of privileges available
	- use `getsystem` to search for and impersonate `SYTEM` token
	- use `elecvate svc-exe (listener)` to spawn a session via a service executable
	- Note:
		- Very much optional and not usually required
		- get SYSTEM helps u to get out of restracted situations in beacons
	- Credentials and hashes
		- Logonpasswords
			- RUNS MIMIKATZ, TRIES TO PULL OUT OF LSASS
			- Recovers credentials
			- alternatives are 
				- safetykatz.exe
					- now safetykatz is different because it doesnt read the memory of lsass
					- instead it uses a windows API to dump the memory of lsass into a file and process it with mimikatz in memory
				- Internal Monologue (current user)
					- helps get the current users plaintext pass, it basically issues a challenge to the current system for authentication system to get a responses with the salt of your choosing, you might be able to get back an encrypted blob which is favorable to cracking offline 
		- Hashump
			- Dumps hashes of local accounts in the system
			- for safer options
				- Use dcsync for domain accounts.
				- `mimikatz !lsadump::sam` for local
		- Note:
			- Both of these inject into LSASS which is **VERY** risky
		- view -> credentials


- mimikatz in beacon
	- Use `mimikatz (command) (arguments)`
		- runs a mimikatz command
		- runs in temporary process
	- `mimikatz !(command) (arguments)`
		- elevate to system and run mimikatz command
		- elevates then executes
	- `mimikatz @(command) (arguments)`
		- use current token to run mimikatz command
		- temporary process also communicates current token to said process



- escalation options
	- Exploits and elevators
	- misconfigurations
	- credentials
- Bypass UAC and get SYSTEM
- credential and hash harvesting
- mimikatz in beacon



https://youtu.be/oOIdvPtuy5U?list=PLcjpg2ik7YT6H5l9Jx-1ooRYpfvznAInJ