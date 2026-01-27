

# Slide 1


![[Pasted image 20240506211201.png]]



## What is business intelligence

- an infrastructure that contains an assortment of processes and tools all with the goal of providing businesses with complete and actionable data to aid in their decision making processes
	- some things included in BI are
		- Data visualization
		- data infrastructure and tools
		- business analytics
		- preparation
		- benchmarking
		- statistical analysis
- The modern analytics flow is as follows
	- access & view
	- Interact
	- nalyze& discover
	- share
	- promote & govern
	- back to access and view

![[Pasted image 20240506211443.png]]




## How to develop  abusiness intelligence strategy

how to create it from the ground up
1. know your business strategy and goals
2. identify key stakeholders
3. choose a sponsored from your key stakeholders
4. choose your BI platform and tools
5. Create a BI team
6. Define your scope
7. Prepare your data infrastructure
8. Define your goals and roadmap


### What is a stakeholder?

"a stakeholder is party that has an interest in the company and can either affect or be affected by the business. the primary stakeholders in a typical corpo are its investors, employees, customers and suppliers"

however with the increasing attention on corporate social responsibility the concept has been extended to include communities. governments and trade associations 


## Data

### data everywhere
expert explaination mashallah... dont ask me i dont even fucking know either what this means

"the world we live in is a big data generating machine"

Scenario 1: you were hired at a startup company and the company just launched its website, your first task is to monitor the website traffic ◦ Monitoring → A process 

Scenario 2: “Imagine spending 24 hours looking out the window, and for every minute, counting and recording the number of cars which pass your house.” ◦ Monitoring and counting → A process


### What is data?

Data can exist as:
- as numbers
- text on paper
- as bits and bytes stored in electronic memory
- as facts stored in a persons mind
- Data is the plural of datum, a single piece of information.


Key terms for data
- numeric
	- data that are expressed on a numeric scale
		- Continuous
			- Data that can take on any value in an interval
		- Discrete
			- Data that can take on only integer values, such as counts.
- Categorical
	- Data that can take on only a specific set of values representing a set of possible categories
		- Binary
			- a special case of categorical data with just two categories of values, things like true/fasle
		- Ordinal
			- categorical data that has an explicit ordering

#### How does this benefit us?

- helps determine the type of visual display
- Helps determine how to manipulate data
- Helps determine how to store data
- Helps determine type of data analysis or statistical model



## Structured data

- Types ig?
	- conforms to a data model
	- well defined structure
	- can be easily accessed
	- can be used by a person or a computer program
- characteristics
	- stored in well defined schemas such as databases
	- clear types
	- data conforms to a data mode clear types
	- data resides in fixed fields
	- easy to access and query 
	- rows & columns 
	- managed by SQL
- Sources
	- SQL databases
	- Spreadsheets such as excel
	- OLTP systems 
	- RFID tags
	- server logs
	- medical devices
- Advantages
	- well defined structure
	- easy storage and access
	- data can be indexed (helps in searching)
	- mining is easy 
	- update/delete/insert is very easy too
	- BI operations is easy as well aka data warehousing
	- scalable
	- secure (column level)
	- structured data is foundation to big data




## Semi-Structured

- characteristics
	- Has no data model but some structure  
	- cant be stored in rows and columns  
	- contains tags ( elements) metadata  
	- little metadata  
	- attribute types may differ even in the same group  
	- lack of structure makes it hard to be used in a computer program
- sources
	- XML
	- email
	- binary.exe
	- zipped files
	- data from multiples sources
	- webpages
	- json
- Advantages
	- Not constrained by a fixed schema
	- flexible
	- portable
	- can be viewed as structured data
	- don't need to know sql 
	- deals with heterogeneity of sources
- Disadvantages of semi structured data
	- Lacks uniform difficult to store
	- Hard to identify relationships
	- Queries less efficient
- Solution
	- use special DMS to store this type of data
	- XML tags can be used
	- Object exchange model represents data by graph
	- RDBMS utilize mapping technique


## Unstructured data

Description
- Has no data model but have some structure
- cant be stored in rows and columns
- does not have semantic rules
- lacks format or sequence
- lack of structure, cant be used in a computer program

- sources of unstructured data
	- images
	- videos 
	- memo
	- report
	- survey
	- .dox .ppt
- Advantages
	- Support for lack of format data
	- No fixed schema
	- flexible
	- portable
	- scalable
	- works with heterogeneity of sources
	- analyzed by intelligence and analytics applications
- Disadvantages
	- Difficulty to store due to lack of schema & structure
	- Problem with indexing due to no structure and attributes
	- Search is not accurate
	- Problem with data security
- Problem with it
	- storage
	- challenge to store images, videos and audio etc.
	- hard to update, delete, search etc
	- storage cost
	- indexing is difficult
- solution
	- Convert to manageable formats
	- use content addressable system
	- store via XML and maybe RDBMS blobs

## Data input and capture

### Data input

- "Any information that is provided to a computer or a software program is known as an input"
- since the information provided is also considered to be data the process of providing information to the computer is also known as data input

### Data capture

- Data capture is the process of collection structured and unstructured information electronically and converting it into data readable by a computer
- Data capture is very similar to data entry but used mostly on data sources that contain basic response types

#### Data capture methods

- manual data capture
- automated data capture
- OCR optical character recognition
- ICR intelligent character recognition
- Barcode QR code recognition
- Voice captures
- smart cards