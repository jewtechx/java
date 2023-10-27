class Strings{
    public static void main(String[] args){
        String text = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        System.out.println("The length of the text is "+text.length());

        String greeting = "Hello Java world";
        System.out.println(greeting.toLowerCase());
        System.out.println(greeting.toUpperCase());

        String locate = "Tell me where I can locate my peace";
        System.out.println(locate.indexOf("locate"));
    }
}