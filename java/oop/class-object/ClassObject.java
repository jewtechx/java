public class ClassObject{
    final int x = 100;

    /**
     * Static methods can be accessed even without creating objects of the class
     * Public classes can be accessed only y creating objects of the class
     */

    //static
    static void reverse(String text){
        String reversed_word = "";
        for(int i = 0; i < text.length(); ++i){
            reversed_word = text.charAt(i) + reversed_word;
        }
        System.out.println("Reversed word: " + reversed_word);
    }

    //public
    public void capitalize(String text){
        System.out.println(text.toUpperCase());
    }

    public static void main(String[] args){
        //instace of class
        ClassObject operator = new ClassObject();
        System.out.println(operator.x);

        //methods
        reverse("I am at the church");
        operator.capitalize("jew is the best programmer");
    }
}