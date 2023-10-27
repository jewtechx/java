class Recursion {
    public static void main(String[] args){
        int result = sum(10);
        int integral = integration(10,20);
        System.out.println(result);
        System.out.println(integral);
    }

/**
 * Every recursive function must have a halting condition 
 * in this case it's when k < 0
 */
    public static int sum(int k){
        if(k > 0){
            return k + sum(k -1);
        }else{
            return 0;
        }
    }

    public static int integration(int open_limit,int close_limit){
        if(close_limit > open_limit){
            return close_limit + integration(open_limit,close_limit - 1);
        }else{
            return close_limit;
        }
    }
}