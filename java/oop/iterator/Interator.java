import java.util.ArrayList;
import java.util.Iterator;

class Interator {
    public static void main(String[] args){
        ArrayList<String> accessories = new ArrayList<String>();

        Iterator<String> it = accessories.iterator();

        accessories.add("Laptop Charger");
        accessories.add("Laptop Ram");
        accessories.add("Laptop Harddisk");

  
                it.next();
       
    }
}