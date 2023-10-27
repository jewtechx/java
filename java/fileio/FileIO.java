import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class FileIO {
    public static void main(String[] args){

        //creating the file
        try{
             File csv_data = new File("students.csv");
        if(csv_data.createNewFile()){
            System.out.println("File created: "+ csv_data.getName());
        }else{
            System.out.println("File already exists");
        }
        }catch(IOException e){
            System.out.println("An error occured");
            e.printStackTrace();
        }

        //writing to the file
        try{
            FileWriter write_csv_data = new FileWriter("C:\\Users\\Jew Larbi Danquah\\Documents\\Works\\java\\fileio\\students.csv");
            write_csv_data.write("jew,kofi,larbi,danquah");
            write_csv_data.close();
            System.out.println("Successfully wrote to the file");
        }catch(IOException e){
            System.out.println("An error occured");
            e.printStackTrace();
        }

        // reading the file
       try {
      File myObj = new File("students.csv");
      Scanner myReader = new Scanner(myObj);
      while (myReader.hasNextLine()) {
        String data = myReader.nextLine();
        System.out.println(data);
      }
      myReader.close();
    } catch (FileNotFoundException e) {
      System.out.println("An error occurred.");
      e.printStackTrace();
    }


    //delete file 

    
         File myObj = new File("students.csv"); 
    if (myObj.delete()) { 
      System.out.println("Deleted the file: " + myObj.getName());
    } else {
      System.out.println("Failed to delete the file.");
    } 
    
    }
}