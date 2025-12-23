public class ThreadTesting extends Thread{
    public void run(){
        for(int i=0;i<10;i++){
            System.out.println("cat"+i+".jpg");
        }
    }
    public static void main(String[] args) {
        System.out.println("app start");

        ThreadTesting t=new ThreadTesting();
        t.start();
        for(int i=0;i<10;i++){
            System.out.println(i);
        }
        System.out.println("app end");
    }
}
