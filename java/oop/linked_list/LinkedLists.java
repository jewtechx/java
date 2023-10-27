import java.util.LinkedList;

class LinkedLists {
    public static void main(String[] args){
        LinkedList<String> emails = new LinkedList<String>();

        emails.add("Sheeps");
        emails.add("Goats");
        emails.add("Bees");
        emails.add("Pigs");
        emails.add("Computer");

        System.out.println(emails.get(3));

        emails.removeFirst();
        emails.removeLast();
        emails.addFirst("Antelop");
        System.out.println(emails);
    }
}