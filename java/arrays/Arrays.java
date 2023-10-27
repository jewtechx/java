class Arrays {
    public static void main(String[] args){
        String[] names = {"Jew","Kelvin","Elclif","Faaj"};
        for(String name : names){
            System.out.println(name);
        }

          int[][] myNumbers = { {1, 2, 3, 4}, {5, 6, 7} };
          for(int i = 0; i < myNumbers.length; ++i){
              for(int j = 0; j < myNumbers[i].length; ++j){
                System.out.println(myNumbers[i][j]);
              }
          }
    }
}