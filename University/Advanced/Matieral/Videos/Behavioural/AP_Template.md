![[Pasted image 20240625071513.png]]


- Templates allows you to defines a skeleton of an algorithm in a base class and let subclasses override the steps without changing the overall algorithm’s structure.
- It is important that subclasses do not override the template method itself 25 → Final.
### Components of the Template Method Pattern in the Example

1. **Order Class**: Represents an order with items.
2. **OrderPrinter Abstract Class**: Defines the template method and abstract methods for subclasses to implement.
3. **Concrete Printer Classes (TextPrinter, HtmlPrinter)**: Implement the abstract methods defined in `OrderPrinter`.
4. **Client Class**: Uses the template method to print the order.

Let's walk through each part of the code provided in the images:

1. **Order Class**: 
```
public class Order {
    private String id;
    private LocalDate date;
    private Map<String, Double> items = new HashMap<>();

    public Order(String id) {
        this.id = id;
        date = LocalDate.now();
    }

    public String getId() {
        return id;
    }

    public LocalDate getDate() {
        return date;
    }

    public Map<String, Double> getItems() {
        return items;
    }

    public void addItem(String name, double price) {
        items.put(name, price);
    }
}

```
2. **OrderPrinter Abstract Class**: 
```
public abstract class OrderPrinter {
    public final void printOrder(Order order, String filename) throws IOException {
        try (PrintWriter writer = new PrintWriter(filename)) {
            writer.println(start());
            writer.println(formatOrderNumber(order));
            writer.println(formatItems(order));
            writer.println(end());
        }
    }

    protected abstract String start();
    protected abstract String formatOrderNumber(Order order);
    protected abstract String formatItems(Order order);
    protected abstract String end();
}

```
3. **Concrete Printer Classes (TextPrinter, HtmlPrinter)**: 
```
public class TextPrinter extends OrderPrinter {
    @Override
    protected String start() {
        return "Order Details";
    }

    @Override
    protected String formatOrderNumber(Order order) {
        return "Order #" + order.getId();
    }

    @Override
    protected String formatItems(Order order) {
        StringBuilder builder = new StringBuilder("Items\n");
        for (Map.Entry<String, Double> entry : order.getItems().entrySet()) {
            builder.append(entry.getKey()).append(" $").append(entry.getValue()).append("\n");
        }
        builder.append("------------------------");
        return builder.toString();
    }

    @Override
    protected String end() {
        return "";
    }
}

```

html printer
```
public class HtmlPrinter extends OrderPrinter {
    @Override
    protected String start() {
        return "<html><head><title>Order Details</title></head><body>";
    }

    @Override
    protected String formatOrderNumber(Order order) {
        return "<h1>Order #" + order.getId() + "</h1>";
    }

    @Override
    protected String formatItems(Order order) {
        StringBuilder builder = new StringBuilder("<p><ul>");
        for (Map.Entry<String, Double> entry : order.getItems().entrySet()) {
            builder.append("<li>").append(entry.getKey()).append(" $").append(entry.getValue()).append("</li>");
        }
        builder.append("</ul></p>");
        return builder.toString();
    }

    @Override
    protected String end() {
        return "</body></html>";
    }
}

```
4. **Client Class**: 
```
public class Client {
    public static void main(String[] args) throws IOException {
        Order order = new Order("1001");

        order.addItem("Sony Xperia 5 III", 900);
        order.addItem("Iphone 13", 1000);
        order.addItem("S22 Ultra", 1200);

        OrderPrinter printer = new HtmlPrinter(); //new TextPrinter();
        printer.printOrder(order, "d:\\a.html"); //d:\\a.txt
    }
}

```