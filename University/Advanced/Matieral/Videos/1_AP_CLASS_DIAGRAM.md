
- UML class diagram
	- Its purpose is to represent the classes inside of the system
	- the relationship between the classes
	- classes inside a system
		- The attributes
		- data types
		- methods
		- relationships
		- displays private and public
	- Explaining relationships
		- Dependencies
			- basically its using an input from another class
			- example
				- 2 classes. EMPDAO and Emp
				- If EMPDAO's method are being used  in Emp that is a dependency because its using its methods
				- it doesnt matter what the numbers are, there is no meaning in seeing numbers on the dependency line
		- Generalizations
			- Basically inheritance
			- is the most common
			- going from subclasses towards the father class
			- line with triangle
		- Realizations
			- For interface
			- if a method in the subclass is in the father class its polymorphism then
			- it is FORCED for you to use ALL of the methods in the father class in the subclasses
			- cutted line with triangle
		- Composition
			- Its a death relationship
			- these relationships are called "part of/ belongs to"
			- A child can **NOT EXIT** without its father class 
			- this x creates a new X
		- Aggregation
			- it is a "has a" relationship
			- Can handle multiplicity
			- in the address example, its read 'address belongs TO employee'
			- how is it translated technically
			- use an assignment statement
		- Association
			- its a big problem
			- very close to aggregation
			- you need to create a new class


- Association vs aggregation
	- Association
		- you need to create a new class and this class you have to tie between it two objects
		- this association isnt like aggreation
		- 
	- Aggregation
		- You need to create a new instance of just opening a constructor this address = this address
		- when a class uses soemthing from ANOTHER CLASS




## REVISE ASSOCIATION
