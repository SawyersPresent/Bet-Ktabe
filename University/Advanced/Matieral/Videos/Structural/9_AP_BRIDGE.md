

- Decouple an abstraction from its implementation so that the two can vary independently.
- Allows you to separate the abstraction from the implementation.
- There are 2 parts in Bridge design pattern:
	- Abstraction
	- Implementation
- anything thats similar group together

- bridge basically does redesign so you organize stuff by seperating it
- its a single responsibility

![[Pasted image 20240625065017.png]]


- **Implementor**: This interface will define the methods related to color.
- **Concrete Implementor**: These classes will provide concrete implementations of the color interface.
- **Abstraction**: This abstract class will define the methods related to shapes.
- **Refined Abstraction**: These classes will extend the abstract class and provide concrete implementations of shapes.


1. implementor color

```
public interface Color {
    void applyColor();
}

```

2. Concrete implementor

```
public class RedColor implements Color {
    @Override
    public void applyColor() {
        System.out.println("Applying red color");
    }
}

public class GreenColor implements Color {
    @Override
    public void applyColor() {
        System.out.println("Applying green color");
    }
}

```


3. abstraction

```
public abstract class Shape {
    protected Color color;

    protected Shape(Color color) {
        this.color = color;
    }

    abstract void draw();
}

```

4. refined abstraction

```
public class Circle extends Shape {
    public Circle(Color color) {
        super(color);
    }

    @Override
    void draw() {
        System.out.print("Drawing Circle in ");
        color.applyColor();
    }
}

public class Square extends Shape {
    public Square(Color color) {
        super(color);
    }

    @Override
    void draw() {
        System.out.print("Drawing Square in ");
        color.applyColor();
    }
}

```


5. client code main

```
public class Main {
    public static void main(String[] args) {
        Shape redCircle = new Circle(new RedColor());
        Shape greenSquare = new Square(new GreenColor());

        redCircle.draw();
        greenSquare.draw();
    }
}
```

