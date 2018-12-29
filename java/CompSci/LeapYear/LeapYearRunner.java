//(c) A+ Computer Science
//www.apluscompsci.com

//Name -
//Date -
//Lab  -

import static java.lang.System.*; 
import java.util.Scanner;

public class LeapYearRunner
{
    public static void main( String args[] )
    {
        Scanner keyboard = new Scanner(System.in);
        
        int num  = keyboard.nextInt();
        LeapYear year = new LeapYear();
        if (year.isLeapYear(num) == true){
            System.out.println("true");
        } else{
            System.out.println("false");
        }
        
                    
    }
}