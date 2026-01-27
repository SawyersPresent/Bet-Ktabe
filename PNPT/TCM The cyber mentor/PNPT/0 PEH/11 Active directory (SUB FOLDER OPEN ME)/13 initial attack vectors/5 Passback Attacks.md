
A bug/vulnerability in terms of IoT devices like printers. etc.

These devices might have default credentials, things like an LDAP connection, use this link and scroll down to a section where your looking for a LDAP / SMB connection

Usually for these devices where the setup page is persent, there should be a configuration for the LDAP connection and you change it to YOUR IP address and setup a listener, you can use netcat OR responder (have it listening obviously). then the password gets sent over through clear text

[A Pen Tester’s Guide to Printer Hacking](https://www.mindpointgroup.com/blog/how-to-hack-through-a-pass-back-attack/)










