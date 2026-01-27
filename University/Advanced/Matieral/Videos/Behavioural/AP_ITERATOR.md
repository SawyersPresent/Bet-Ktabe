![[Pasted image 20240625072008.png]]

▪An enum is a special "class" that represents a group of constants → Unchangeable variables.
▪To create an enum, use the enum keyword (instead of class or interface). 
▪Separate the constants with a comma.
▪Enum constants are public, static and final. 
▪An enum cannot be used to create objects, and it cannot extend other classes (but it can implement interfaces). 
▪Use enums when you have values that you know aren't going to change, like days, colors, etc.


### Components of the Iterator Pattern in the Example

1. **Iterator Interface**: Defines the methods for accessing and traversing elements.
2. **Concrete Iterator Class**: Implements the Iterator interface.
3. **Enum**: Represents a collection of constants.
4. **Client Class**: Uses the iterator to traverse the elements.

