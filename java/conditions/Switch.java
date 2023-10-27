class Switch {
    public static void main(String[] args){
        int answer = 12 / 4;
        switch(answer){
            case 1:
                System.out.println("You have one chance left");
                break;
            case 2:
                System.out.println("You have two chances left");
                break;
            case 3:
                System.out.println("You have three chances left");
                break;
            default:
                System.out.println("You have 0 chances left");
                break;

        }
    }
}