

Kerberos is a difficult and complex to get into but rewarding once mastered, here is the simplification of the entire Kerberos authentication process

- KRB_AS_REQ
	- The user tells the DC they want to authenticate, sends over their current timestamp  encrypted with the users password
- KRB_AS_REP
	- The KDC will decrypt this time stamp using the users password, once it is decrypted the user will receive a TGT encrypted with the `krbtgt` password. The session key is also sent over encrypted with the users hash
- KRB_TGS_REQ
	- The User sends over the TGT and a copy of the encrypted session key to the KDC. This request also contains the name (SPN) and the current timestamp encrypted .
- KRB_TGS_REP
	- If the KDC is able to decrypt the session key, the TGT and its corresponding session too then it sends back the Service Ticket (ST) encrypted with the service's password hash and the user's password hash to send back a new key 
- KRB_AP_REQ
	- Done with the KDC now they can use their service ticket (ST) to access the service they want by sending over the encrypted service ticket and Using the new session key to encrypt their time stamp to the target service  
- KRB_AP_REP
	- The service decrypts the ticket and the encrypted time stamp with the session key (Service tickets come with the session key inside), After receiving the request the service then verifies if the user can access the server by sending back a challenge-response encrypted with the session key. then the user can access the service



# ASREP-Roasting

`asreproasting` is a technique that allows an attacker to request a TGT which subsequently can be cracked offline to retrieve the users password. This is because the `DoesNotRequirePreAuth` flag set




# ASREQ-Roasting

As covered previously in the `KRB_AP_REQ` process, When the user sends over the challenge its through an unencrypted communication channel also it is encrypted with their own password. This means if an attacker was able to compromise a machine of which a user is authenticating from, they would be able to intercept the `ASREQ-Roasting`, Then it can be taken offline and cracked .In some cases even if the credentials are invalid in the domain they may be valid for something else.









---

This session key? or the session key?

