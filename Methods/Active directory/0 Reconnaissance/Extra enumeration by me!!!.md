
# With no creds quick checklist

- LDAP
	- Null session
	- anonymous connections
	- use NetExec to exploit this stuff for enumerate users, groups, etc.
		- Use Net
- SMB
	- null session
	- Anonymous connections
	- use NetExec with its other options
		- `nxc smb <IP> --shares`
		- `nxc smb <IP> --users`
		- `nxc smb <IP> --groups`
	- 
- MSRPC
	- 
- Tools
	- ADenum
		- extremely useful does automatic everything but might get banned on certain exams, i think itll be allowed on the PNPT
			- https://github.com/SecuProject/ADenum?tab=readme-ov-file
	- Username-anarchy


- Finding usernames
- Finding groups
- Finding shares
- 







# With credentials!!

- Use bloodhound python
	- `bloodhound-python -d example.local -dc example.local -ns <nameserver-ip> -u 'username@example.local' -p 'password'`
- Use rusthound
	- `rusthound -d example.local -u 'usrname@example.local' -p 'password' -i 10.0.0.1 --zip`
- bloodyAD can also be used to enact actions and changes
	- https://github.com/CravateRouge/bloodyAD/wiki/Enumeration





```
# List all users
net user /domain
net user <username> /domain
Get-ADUser -Filter *
Get-ADUser -Identity <username> -Server dc.example.com -Properties *
Get-ADUser -Filter 'Name -like "*michael"' -Server dc.example.com | Format-Table Name,SamAccountName -A

# List all groups
net group /domain
net group "<group>" /domain
PS> Get-ADGroup -Identity <group> -Server dc.example.com -Properties *
PS> Get-ADGroupMember -Identity <group> -Server dc.example.com

# List the password policy
net accounts /domain

# List AD objects
$ChangeDate = New-Object DateTime(2022, 02, 28, 12, 00, 00)
Get-ADObject -Filter 'whenChanged -gt $ChangeDate' -includeDeletedObjects -Server dc.example.com

# Retrieve information about the given domain.
Get-ADDomain -Server dc.example.com

# Change the password of AD user
Set-ADAccountPassword -Identity <username> -Server dc.example.com  -OldPassword (ConvertTo-SecureString -AsPlaintext "oldpass" -force) -NewPassword (ConvertTo-SecureString -AsPlaintext "newpass" -force)

# SYSVOL - A shared folder storing the Group Policy Objects (GPOs).
dir \\dc.example.com\SYSVOL\
```





https://exploit-notes.hdks.org/exploit/windows/active-directory/#naming-convention