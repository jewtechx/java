public class Reverse{
    public static void main(String[] args){
        String main_string = "I will prove you wrong";
        String proof = "";

        for(int i = 0; i < main_string.length(); ++i){
            proof = main_string.charAt(i) + proof;
        }

        System.out.println("Proof: "+proof);
    }
}