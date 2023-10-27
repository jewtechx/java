class WhileLoop {
    public static void main(String[] args){
        int i = 0;
        while(i < 5){
            if(i % 2 == 0){
                System.out.println("$ $ $ $");
            }else if(i % 2 ==1){
                System.out.println(" $ $ $");
            }    
            i++;        
        }

        do{
            System.out.println("I am greeting even though you met me");
        }while(i > 5);
    }
}