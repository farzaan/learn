
/**
 * The purpose of this program is to illustrate the use of the
 * while loop as a counter.
 *
 * @author Charles Babbage
 * @version 06/05/17
 */
public class CountingWithWhileLoops
{
    public static void main(String [] args)
    {
        double[] d = {8.95, 1.25, 2.65, 8.43, 34.20, 2.24};
        
        double sum = 0.0;
        
        for(double decimal : d)
        {
            sum += decimal * 2;
            System.out.println(sum);
        }
    }//end of main method
}//end of class
