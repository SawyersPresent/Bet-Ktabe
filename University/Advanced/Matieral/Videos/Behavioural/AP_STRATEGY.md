![[Pasted image 20240625071209.png]]
### Components of the Strategy Pattern in the Example

1. **Strategy Interface**: Defines the method that all concrete strategies must implement.
2. **Concrete Strategy Classes**: Implementations of the Strategy interface.
3. **Context Class**: Uses a Strategy object.

Let's walk through each part of the code provided in the images:


1. **Strategy Interface**:
```
public interface Strategy {
    int doOperation(int num1, int num2);
}

```
2. **Concrete Strategy Classes**:
```
public class OperationAdd implements Strategy {
    @Override
    public int doOperation(int num1, int num2) {
        return num1 + num2;
    }
}

```

```
public class OperationMultiply implements Strategy {
    @Override
    public int doOperation(int num1, int num2) {
        return num1 * num2;
    }
}

```
4. **Context Class**: 
```
public class Context {
    private Strategy strategy;

    public Context(Strategy strategy) {
        this.strategy = strategy;
    }

    public int executeStrategy(int num1, int num2) {
        return strategy.doOperation(num1, num2);
    }
}

```