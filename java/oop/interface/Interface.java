import java.util.Scanner;

interface BookCheckIn {
    void checkIn();
}
interface BookCheckOut {
    void checkOut();
}

class Student implements BookCheckIn,BookCheckOut {
    // @Override
    public void checkIn() {
        Scanner input = new Scanner(System.in);
        System.out.println("Enter the book you want to check in: ");
        String bookIn = input.nextLine();
        System.out.println(bookIn + " checked in successfully. Please make sure to return it.");
    }

    // @Override
    public void checkOut() {
        Scanner input = new Scanner(System.in);
        System.out.println("Enter the book you want to check out: ");
        String bookOut = input.nextLine();
        System.out.println(bookOut + " checked out successfully. Looking forward to crush with you again.");
    }
}

public class Interface {
    public static void main(String[] args) {
        Student student = new Student();
        Scanner input = new Scanner(System.in);

        System.out.println("To check in a book, press \"i\". Press \"o\" to check out a book");
        String ask = input.nextLine();

        if (ask.equals("i")) {
            student.checkIn();
        } else if (ask.equals("o")) {
            student.checkOut();
        } else {
            System.out.println("Wrong input");
        }

        // Close the input scanner to prevent resource leak
        input.close();
    }
}
