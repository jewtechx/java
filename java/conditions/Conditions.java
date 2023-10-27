class Conditions {
    public static void main(String[] args){
        String driver = 2 % 2 == 0 ? "Bluetooth" : "Wireless";
        System.out.println("We need to download the "+driver+" driver");
    }
}