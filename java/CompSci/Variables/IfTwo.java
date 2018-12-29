//(c) A+ Computer Science
// www.apluscompsci.com

//if statement practice

import java.util.Scanner;

public class IfTwo
{
    public static void main(String args[])
    {
        //define and instantiate a Scanner named keyboard
        Scanner keyboard = new Scanner(System.in);
        //a prompt may be handy
        System.out.println("type in a large value");
        //read in a double and save it in a variable named value
        double num = keyboard.nextDouble();
        //print out ben if value is greater than 1000
        if(num > 1000){
            System.out.println("ben");
        }
        //print out sam if value is less than -2000
        if(num < -2000){
            System.out.println("sam");
        }
        else{
            System.out.println("");
        }
    }
}

