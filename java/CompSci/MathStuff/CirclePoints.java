import java.util.Scanner;  
/**
 * A program that calculates the (x,y) coordinates of points on a circle of a given radius.
 *
 * @author Farzaan Nasar
 * @version 12/3/18
 */
public class CirclePoints
{
    
    public static void main(String[ ] args){
        // instance variables
        double xone = 0.0;
        double yone = 0.0;
        double yonesquared = 0.0;
        double ytwo = 0.0;
        double radius = 1.0; 
        
        //Scanner keyboard = new Scanner(System.in);
        //radius = keyboard.nextDouble();
        xone = radius;
        System.out.println("Points on a Circle with a Radius of 1.0");
        System.out.printf("%8s%8s%8s%8s\n ", "x1", "y1", "x1", "y2");
        System.out.println("***************************************");
        //Formatting and frills^
        for(xone = radius; xone >= (-radius); xone -= 0.1){
            yonesquared = Math.pow(radius,2) - Math.pow(xone, 2);
            //Performs pythagorean theorem ^
            yone = Math.sqrt(yonesquared);
            //Takes square root^
            ytwo = -yone;
            System.out.printf("%8.2f%8.2f%8.2f%8.2f\n", xone, yone, xone, ytwo);
        }
        
    }
}
