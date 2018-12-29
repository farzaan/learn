//� A+ Computer Science
//www.apluscompsci.com

//Name - Farzaan Nasar 
//Date - 8/30
//Class - comp Sci
//Lab  - stars asnd stipes

import static java.lang.System.*;

public class StarsAndStripes
{
   public StarsAndStripes()
   {
      out.println("StarsAndStripes");
      printTwoBlankLines();
   }

   public void printTwentyStars()
   {
       out.println("********************");
   }

   public void printTwentyDashes()
   {
       out.println("--------------------");
   }

   public void printTwoBlankLines()
   {
       out.println(" ");
       out.println(" ");
   }
   
   public void printASmallBox()
   { 
       printTwentyDashes();
       printTwentyStars();
       printTwentyDashes();
       printTwentyStars();
       printTwentyDashes();
       printTwentyStars();
       printTwentyDashes();
   }
 
   public void printABigBox()
   { 
       printTwentyDashes();
       printTwentyStars();
       printTwentyDashes();
       printTwentyStars();
       printTwentyDashes();
       printTwentyStars();
       printTwentyDashes();
       printTwentyDashes();
       printTwentyStars();
       printTwentyDashes();
       printTwentyStars();
       printTwentyDashes();
       printTwentyStars();
       printTwentyDashes();
   }   
}