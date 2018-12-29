/**
 * The purpose of this program is to illustrate the use of the
 * while loop as a counter.
 *
 * @author Charles Babbage
 * @version 06/05/17
 */
public class ef
{
    public static void main(String [] args)
    {
        String[] animals = { "lion", "tiger", "hippo"};
        
        
        for(String animal : animals)
        {
            if(animal.length() < 5)
                System.out.println("Short: " + animal );
            else
                System.out.println("Long: " + animal );
        }
    }//end of main method
}//e