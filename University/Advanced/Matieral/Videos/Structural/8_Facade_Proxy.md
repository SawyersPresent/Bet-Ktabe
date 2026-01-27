

# Facade

![[Pasted image 20240625064336.png]]

take everything, store it in 1 method and then just go with it

- to reduce complexity for the UI/UX or the client
- distancing them away from the internals of the code



# Proxy


![[Pasted image 20240625064322.png]]

### Components of the Example

1. **Internet Interface**
2. **RealInternet Class (Real Subject)**
3. **ProxyInternet Class (Proxy)**
4. **TestProxy Class (Client)**


1. interface
```
public interface Internet {
    public void connectTo(String serverHost) throws Exception;
}
```

2. real subject
```
public class RealInternet implements Internet {
    @Override
    public void connectTo(String serverHost) throws Exception {
        System.out.println("Connecting to " + serverHost);
    }
}

```

3. proxy
```
public class ProxyInternet implements Internet {
    private Internet internet = new RealInternet();
    private static List<String> unauthorizedSites;

    static {
        unauthorizedSites = new ArrayList<String>();
        unauthorizedSites.add("aaa.com");
        unauthorizedSites.add("bbb.com");
        unauthorizedSites.add("ccc.com");
    }

    @Override
    public void connectTo(String serverHost) throws Exception {
        if (unauthorizedSites.contains(serverHost.toLowerCase())) {
            throw new Exception("Access Denied");
        }
        internet.connectTo(serverHost);
    }
}

```

4. client 
```
public class TestProxy {
    public static void main(String[] args) {
        Internet internet = new ProxyInternet();
        try {
            internet.connectTo("https://htu.edu.jo/");
            internet.connectTo("aaa.com");
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }
}
```