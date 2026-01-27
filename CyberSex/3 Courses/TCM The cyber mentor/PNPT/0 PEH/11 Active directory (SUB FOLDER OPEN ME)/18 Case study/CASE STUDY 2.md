

- Limitations
	- IPv6 cant do so no mitm6
	- LLMNR
- Thinking outside the box
	- Start looking at what's available
		- Sweep for internal web pages
			- Default credentials
				- If logged in check for passwords and sauce.
			- Apache
			- Printers
	- After getting credentials
	- Try using nxc with administrator (with no username)
- Post exploit
	- After you exploit a user pull passwords
		- Secretsdump
		- NXC SAM dump
		- Inspect it see if any other accounts have similar passwords
		- Password re-use once, means password re-use always, use NXC
- Notes
	- Windows 7
	- Windows 8 
	- Windows server 8 
	- Windows server 2012
		- Run WDigest.exe



