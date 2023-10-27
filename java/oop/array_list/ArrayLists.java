import java.util.ArrayList;

public class ArrayLists {
  public static void main(String[] args) {
    ArrayList<String> cars = new ArrayList<String>();
    cars.add("Volvo");
    cars.add("BMW");
    cars.add("Ford");
    cars.add("Mazda");
    System.out.println(cars);
    System.out.println(cars.get(0));
    System.out.println(cars.get(1));
    System.out.println(cars.remove(3));
    System.out.println(cars.set(2, "Okada"));
  }
}