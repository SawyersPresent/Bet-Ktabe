- you integrate stuff
- two principles


```
public interface Notification {
    public abstract void notifyUser();
}
```

```
public class SMSNotification implements Notification {
    @Override
    public void notifyUser() {
        System.out.println("Sending SMS notification");
    }
}

```


```
public class EmailNotification implements Notification {
    @Override
    public void notifyUser() {
        System.out.println("Sending email notification");
    }
}

```


```
public class NotificationFactory {
    public Notification createNotification(String channel) {
        if (channel.equals("SMS"))
            return new SMSNotification();
        if (channel.equals("EMAIL"))
            return new EmailNotification();
        return null;
    }
}

```



```
public class NotificationService {
    public static void main(String[] args) {
        NotificationFactory notificationFactory = new NotificationFactory();

        Notification notification = notificationFactory.createNotification("SMS");
        notification.notifyUser();

        notification = notificationFactory.createNotification("EMAIL");
        notification.notifyUser();
    }
}

```