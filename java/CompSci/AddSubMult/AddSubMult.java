//(c) A+ Computer Science
//www.apluscompsci.com
//Name -

import static java.lang.System.*; 
import java.util.Scanner;

public class AddSubMult
{
    public static double check( double a, double b )
    {
        if(a>b){
            return (a-b);
            //if a is less than b then subtract b from a 
        }
        if(a<b){
            return (b-a);
            //if b is greater than a then subtract a from b
        }
        else{
            return (a*b);
            //if a is equal to b then multiply a and b
        }
    }
}