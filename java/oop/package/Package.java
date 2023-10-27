package java_prime;

import java.util.Scanner;

public class Package {
    public static boolean isPrime(int number) {
        if (number <= 1) {
            return false; // 1 and any number less than 1 are not prime
        }

        if (number <= 3) {
            return true; // 2 and 3 are prime
        }

        if (number % 2 == 0 || number % 3 == 0) {
            return false; // Numbers divisible by 2 or 3 are not prime
        }

        int i = 5;
        while (i * i <= number) {
            if (number % i == 0 || number % (i + 2) == 0) {
                return false; // Numbers divisible by factors other than 2 and 3 are not prime
            }
            i += 6;
        }

        return true; // If no factors were found, the number is prime
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int number = scanner.nextInt();
        scanner.close();

        if (isPrime(number)) {
            System.out.println(number + " is a prime number.");
        } else {
            System.out.println(number + " is not a prime number.");
        }
    }
}
