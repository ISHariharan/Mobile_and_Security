import java.util.*;
import java.lang.*;

class des{
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);

        System.out.println("Enter your name : ");
        String name = scanner.nextLine();
        System.out.println("Entered name : " + name);

        for(int i=0; i<name.length(); i++){
            String bits = Integer.toBinaryString((int)name.charAt(i));
            System.out.println("Bit of character " + name.charAt(i) + " : " + bits);
        }
    }
}