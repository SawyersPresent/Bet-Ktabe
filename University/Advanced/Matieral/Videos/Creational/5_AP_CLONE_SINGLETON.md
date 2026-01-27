


# Prototype deep clone

Supposed to be fast interms of execution

the difference that in the code it looks like this

clones the object and gives me a chance to edit it a little bit

# Singleton

- creation
	- Namat gheir motakarer
	- high cost / high risk
- Class
	- Create a static attribute for the class
- Singleton
	- its idea is i only want ONE object
	- This can be used when the object creation is too high where its connected to a database
	- the server will crash if there are multiple instances


```java
public class Singleton {
	public static singleton isntance = null;
	private singleton(){
	}
	public static Singleton getInstance(){
		if(instance == null){
		instance = new singleton();
		}
	return instance;
	}
}
```

```java
public class testsinglton{
	public static void main(string[] args)
	singleton x = singleton.getInstance();
	singleton y = singleton.getinstance();
	singleton z = singleton.getinstance();
	system.out.println("x = " + x);
	system.out.println("y = " + y);
	system.out.println("z = " + z);

	if (x == y && y == z ) 
	system.out.println("three objects point to the same memory location");
}
```