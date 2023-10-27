class Methods {
        static void fetch(){
            System.out.println("Humidity:30mps,Wind:70%,Rain:100% chance");
        }

        static void logIn(String id,String password){
            System.out.println("Congratulations!!🎉. A user with id "+id+" has been created");
        }

        static int calculate(int x,int y){
            return x + y;
        }

        static String calculate(String salary,String time){
            return salary + time;
        }
        static double calculate(double hours,double level){
            return hours * level;
        }
    public static void main(String[] args){

        fetch();
        logIn("11225319","jksdosdsd");
        int value = calculate(12,12);
        int interest = calculate("20000000","12");
        int sleep = calculate(12.2123,12.1212);
        System.out.println("The answer is "+value+ " " + interest + " " + sleep);

    }
}