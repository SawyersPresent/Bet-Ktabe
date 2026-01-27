




- Password re-use is always a thing
- Just because IPv6 is disabled it doesnt mean that SMB relay or other types are disabled
	- which COULD get me a shell




- Limitations
	- IPv6 disabled
	- IDPS
	- PAM
		- Can capture
		- Usually cant crack tho
- Think outside the box
	- whats the attack strat?
	- SMB relay attack using interfact
		- `Instead of trying to crack the hash, we can actually relay the hash to another machine and pretend we are the captured user, which would provide us shell access given certain conditions`
			- `SMB signing must be disabled on the target.  By default, SMB signing is enabled on Windows Servers and disabled on Windows Workstations`
			- `The relayed user credential must be an admin on the machine it is being relayed to.  This is not entirely true, however we get significantly more benefits out of a machine admin`
	- This SMB attack is successful
- Post-Exploitation
	- Dump the hashes
		- secretsdump
		- mimikatz
	- Use NXC to spray again