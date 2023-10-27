import java.time.LocalDate;
import java.time.LocalTime;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

class Dates { 
    public static void main(String[] args){
        LocalDate date =   LocalDate.now();
        LocalTime time =   LocalTime.now();
        LocalDateTime datetime =   LocalDateTime.now();
        // LocalTimeFormatter formatdatetime =   DateTimeFormatter.ofPattern("dd-MM-yyyy HH:mm:ss");

        System.out.println("Time is: " + time );
        System.out.println("Date is: " + date );
        System.out.println("Date and time is: " + datetime );
        // System.out.println("Formatted Date and time is: " + formatdatetime);
    }
}