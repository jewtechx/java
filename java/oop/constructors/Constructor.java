import java.util.Scanner;

public class Constructor { 
    String[] report;

    public Constructor(String[] materials){
        report = materials;
    }

    public static void main(String[] args){
        Scanner user_req = new Scanner(System.in);

        System.out.println("Enter materials you will need");
        String materials_from_user = user_req.nextLine();

        String[] materials = materials_from_user.split(",");
        Constructor items = new Constructor(materials);

        for(int i = 0; i < materials.length; ++i){

             System.out.println(items.report[i]);
        }
        user_req.close();
    }
}