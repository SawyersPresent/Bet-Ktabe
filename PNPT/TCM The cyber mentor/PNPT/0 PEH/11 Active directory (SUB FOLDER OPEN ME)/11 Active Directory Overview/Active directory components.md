
what is Active directory?

- Active directory developed by Microsoft to manage windows domain networks
- Stores information related to objects, such as computers, Users, Printers, etc.
	- A phone book for windows
- Authenticates using Kerberos tickets
	- Non-windows devices like Linux machines, firewalls, etc. can also authenticate to active directory via RADIUS or LDAP
- Active directory is used in most fortune 500 companies
	- 99% of them use it, think IBM, Microsoft, Cisco, literally any big corporation you can think of
- Can be exploited without ever attacking patchable exploits
	- You can leverage trusts, groups, and other stuff to abuse to get Domain admin




- Physical
	- AD DS Data store
		- contains the database files and a lot of different information for users, and other configs
		- the most **important** part is that it has the NTDS.dit file which is very important
			- Can pull password hashes from this
	- Domain Controllers
		- The big phonebook that has everything worth having basically
	- Global catalog server
		- The [_global catalog (GC)_](https://learn.microsoft.com/en-us/previous-versions/windows/desktop/legacy/ms681905(v=vs.85)) allows users and applications to find objects in an Active Directory domain tree, given one or more attributes of the target object. 
		- https://learn.microsoft.com/en-us/windows/win32/ad/global-catalog
	- Read-Only domain controller
		- This provides a domain controller for use at branch offices where a full domain controller cannot be placed. The intent is to allow users in the branch offices to logon and perform tasks like file/printer sharing even when there is no network connectivity to hub sites.
		- https://learn.microsoft.com/en-us/windows/win32/ad/rodc-and-active-directory-schema
- Logical
	- partitions
	- schema
		- rulebook or a blueprint, defining every type of object which can be stored in our AD
		- sets rules for object creation and configuration
	- domains
		- domains are used to group and manage objects in an organization
		- administrative boundary for applying policies to groups of objects
		- an authentication and authorization boundary that provides a way to limit the scope of access to resources
	- domain trees
		- A hierarchy of domains
		- They share a contiguous namespace with the parent domain
		- By default it creates a two-way transitive trust with OTHER domains
			- Having parent and children domains
				- Example
					- The parent is called `contoso.com`
					- the children will be `emea.contoso.com` and `na.contoso.com`
	- forests
		- A Collection of one or more domain trees.
		- They share a common schema
		- share a common config partition
		- share a common global catalog to enable searching
		- Enables trusts between all domains in the forest
		- Share the enterprise admins and schema admins groups
	- sites
	- Organizational units
		- They are just sorta like containers that contain things
		- they can contain users, groups, etc. 
		- policies can be applied 
		- A way to group certain things in the container
		- what are they really used for?:
			- Manage a collection of objects in a consistent manner
			- delegate permissions to administer groups of objects
			- apply policies
		- example:
			- I have computer A, B and C
			- to create a policy where computer A and B do not have Microsoft defender but I want to let C have its permissions be on, that is possible with containers and policies
	- Trusts
		- Trusts provide a mechanism for users to gain access to resources in another domain
		- Directional trust
			- the trust direction flows from trusting domain to the trusted domain
		- Transitive trust
			- the trust relationship is extended beyond a two-domain trust to include other trusted domains
		- All domains in a forest trust all other domains in the forest
		- trusts **CAN** be extended **OUTSIDE** of the forest
	- Objects
		- They live **INSIDE** of **OU**'s that's how they work
		- types of objects:
			- User
				- enables network resource access for a user
			- InetOrgPerson
				- Similar to user account
				- Used for compatibility with other directory services
			- Contacts
				- Used primarily to assigning email addresses to external users
				- Does not enable network access
			- Groups
				- Used to simplify the administration of access control
			- Printers
				- Used to simplify the process of locating and connecting to printers
			- Shared folders
				- Enables users to search for shared folders based on properties
	- https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/understanding-the-active-directory-logical-model




https://learn.microsoft.com/en-us/windows/win32/ad/active-directory-domain-services