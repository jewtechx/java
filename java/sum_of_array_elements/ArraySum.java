class ArraySum {
    public static void main(String[] args){
        int[] numbers = {1,2,3,4,5,6};
        int sum = 0;
        int i;
        for(i = 0; i < numbers.length; ++i){
            sum += numbers[i];
        }
        System.out.println("Sum is:" + sum);
    }
}