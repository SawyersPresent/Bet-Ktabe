
- finding out if it s
	- find out the closest discord server to the ME region
- finding out why
- final words and confirmation


## Jordan Confirmation

![[Steps to this research-20251009122931546.webp]]



![[Steps to this research-20251009123042592.webp]]



![[Steps to this research-20251009123626130.webp]]



## regions that discord supports

- brazil
- honk kong
- india
- japan
- rotterdam
- singapore 
- south africa
- sydney
- US
	- US Central
	- US East
	- US South
	- US West





## what infrastructure is discord using?

![[Steps to this research-20251009125211228.webp]]

okay how can we get confirmation of any of this?

in this paragraph we can see this being done

![[Steps to this research-20251009125627724.webp]]

https://discord.com/blog/how-discord-supercharges-network-disks-for-extreme-low-latency
https://www.reddit.com/user/ReallyAmused/

- private relay apple bypasses 
- orange and zain do DPI, deep packet inspcetion
- sunday 2pm saifs apprenticeship, now in 15 minutes??
- https://www.semanticscholar.org/paper/Discord-Server-Forensics%3A-Analysis-and-Extraction-Iqbal-Motylinski/2d72f6719074b325484660dc4dd14f57bf8bf6ec




 - IP blocking
 - DNS blocking
 - SNI blocking
 - DPI blocking
	 - used in the CLUBHOUSE application
	 - used in the facebook application
	 - they could map sandvines mapping

Look at fingerprints to see the difference


- ISP are identified by ASN
- each ISP has a different ASN


https://josa.ngo/blog/78



Traffic question

- Ask them what their network is, google what is my IP? from the IP I can figure out what the ASN is.
-  screenshot whatever comes up here [https://ipinfo.io/what-is-my-ip](https://ipinfo.io/what-is-my-ip)
- OONI
	- Open source Observatory (of) Network Interferance
	- we can connect with them 
- Notifications
	- Handled by google and apple, they are probably the domains sending not anything else
	- DPI could be blocking on the messaging portions
	- push notiifications are handled by the PUSH OS
	- [https://developer.apple.com/documentation/usernotifications/sending-notification-requests-to-apns](https://developer.apple.com/documentation/usernotifications/sending-notification-requests-to-apns)
	- [https://developers.google.com/workspace/admin/reports/v1/guides/push?hl=en](https://developers.google.com/workspace/admin/reports/v1/guides/push?hl=en)
- maria and elizibeta work at OONI
	- can tag me to relevant people



# Meeting with ISSA

- blocking with DPI confirmed by zain
	- they were using sandvine
- keep testing to see if this might be the case, find previous research that assists in this




# Citizen lab report

## **Attribution of middlebox to Sandvine**

### **Fingerprint elements**

Based on our PCAPs, we identified several elements of the injection in Turkey which, in conjunction, form what we believe to be a highly distinctive fingerprint:

1. **In all injected packets, the IPID is always 13330** (0x3412, which is 0x1234 endian-swapped) for all injected packets. This value is unusual, as the IPID is typically incremented or pseudorandomly generated, and is not a fixed value.
2. **In all packets, the IP flags are all zero**. This characteristic is unusual as modern TCP stacks typically default-enable Path MTU Discovery for TCP sockets, which results in the “don’t fragment” IP flag being set to 1.
3. **The injected packet received by the client is either an empty RST/ACK packet, or a FIN/ACK packet, with an HTTP 307 redirect whose headers exactly match the form of redirect in Figure 1.**
4. **If a FIN/ACK is injected, then the injector sends an unsolicited final ACK packet to the client ~100ms later**. This behavior is unusual, as a well-behaving TCP stack would wait to see the FIN/ACK from the client before sending the final ACK.


https://www.qurium.org/alerts/internet-blocking-in-jordan/
https://citizenlab.ca/2018/03/bad-traffic-sandvines-packetlogic-devices-deploy-government-spyware-turkey-syria/


