public class TryCatch {
    public static void main(String[] arg){
        try{
            int x,y,sum;
            x = 9;
            y = 10;
            sum = x + y;
            System.out.println("Sum is:" + sum);
        }catch(Exception e){
            System.out.println("An error occured: " + e.getMessage());
        }finally{
            System.out.println("Try catch finished");
            throw new ArithmeticException("Invalid operation");
        }
    }
}
