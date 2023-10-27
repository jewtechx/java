package oop.threads;

class move extends Thread {
    public void run(){
        for(int i = 0; i < 100; ++i){
            System.out.println("We are moving!!");
            try{

                Thread.sleep(10);
            }catch(InterruptedException e){e.printStackTrace();}
        }
    }

   
}


class stop extends Thread {
    public void run(){
        for(int i = 0; i < 100; ++i){
            System.out.println("No stopping...");
             try{

                Thread.sleep(10);
            }catch(InterruptedException e){e.printStackTrace();}
        }
    }

    public void start() {
    }
}

public class Threading{
    public static void main(String[] arg){
       move move = new move();
       stop stop = new stop();

       move.start();
       stop.start();
    }
}
