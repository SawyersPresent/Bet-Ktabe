

- S7-300
	- Modular architecture for flexible configurations
	- reliable for complex processes
	- widely used in manufacturing and process control
	- proven durability in industrial environments
- S7-1200
	- Designed for small-to-medium applications
	- Compact form factor, cost-efficient
	- TIA Portal integration
	- Simplifies programming and maintenance
- S7-1500
	- High-speed process and diagnostics
	- faster cycle times, improved dat handling
	- Ideal for automotive, robotics, and process industries
	- Future-proof automation technology


# Protocol stack

- HOST LAYER
	- S7Comm Industrial protocol
- Media Layer
	- ProfiBus
	- ProfiNET
		- S7 Header
		- Parameter
		- Data
	     - Encapsulated by COTP Hd
		- TPKT, Encapsulated by a ISO on TCP frame. adds an extra layer and helps with routing over the network
		- Finally the ISO on TCP packet is embedded with a TCP segment, its transmitted over Ethernet


![[Theory-20251225190422205.webp|893]]














