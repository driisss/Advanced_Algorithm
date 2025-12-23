import java.util.Scanner;
public class Random {
    public static void main(String[] args) {
        Scanner scr=new Scanner(System.in);
        int num=scr.nextInt();
        fab(num);
    }
    public static void fab(int num){
      int num0=0;
      int num1=1;
      if (num==0) {
        System.out.println(num0);
      }
      else if (num==1) {
        System.out.println(num0);
        System.out.println(num1);
      }    
      else{    
        System.out.println(num0);
        System.out.println(num1);
      for(int i=2;i<num;i++){
                int f=num0+num1;
                num0=num1;
                num1=f;
                System.out.println(f);
        }
    }
}
}
