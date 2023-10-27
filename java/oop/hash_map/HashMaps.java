import java.util.HashMap;

class HashMaps {
    public static void main(String[] args){

        HashMap<String,Integer> grades = new HashMap<String,Integer>();
        
        grades.put("English",1);
        grades.put("Math",1);
        grades.put("Science",1);
        grades.put("ICT",2);

        System.out.println(grades.get("English"));
        System.out.println(grades.get("ICT"));
    }
}