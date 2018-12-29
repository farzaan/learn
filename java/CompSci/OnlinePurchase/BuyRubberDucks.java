import java.util.Scanner;
import java.util.Random;
import static java.lang.System.*;
//imports^
/**
 * The purpose of the program was to make a receipt program using strings and inputs
 *
 * @author Farzaan Nasar
 * @version 9/24/18
 */
public class BuyRubberDucks
{
    
    public static void main(String[] args){
        
        Scanner keyboard = new Scanner(System.in);
        System.out.println("Good Afternoon");
        System.out.print("Enter your first and last name: ");
        String firstname = keyboard.next();
        String lastname = keyboard.nextLine();
        //Gets full name of user and stores it^
        
        System.out.print("Enter today's date (mm/dd/yyyy): ");
        String date = keyboard.next();
        //Gets todays date from user and stores it^
        
        System.out.print("Enter type of duck: ");
        String itemName = keyboard.next();
        //Gets name of duck from user and stores it^
        System.out.print("Enter amount of duck: ");
        int itemAmount = keyboard.nextInt();
        //Gets amount of duck from user and stores it^
        System.out.print("Enter price of duck: ");
        String itemprice = keyboard.next();
        //Gets price of duck from user and stores it^
        System.out.print("Enter debit card number(#####-###-####): ");
        String itemDebit = keyboard.next();
        //Gets debit card from user and stores it^
        System.out.print("Enter PIN(####): ");
        String itemPIN = keyboard.next();
        //Gets PIN from user and stores it^
        System.out.println("*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~");
        System.out.println("*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~");
        System.out.println("Your e-Receipt\n");
        
        String dateReformat = date.replace("/", "-");
        System.out.println(dateReformat);
        //Reformats date and prints it out
        
        Random rand = new Random();
        int orderNumber = rand.nextInt(50) + 1;
        System.out.println("Order number: ra" + orderNumber + "\n");
        //Creates random order number and prints^
        
        System.out.println(firstname.substring(0,1) + "." + lastname);
        //Formats name and prints it out^
        
        String sub = itemDebit.substring(0,9);
        String itemDebitReformat = itemDebit.replace(sub, "#####-###");
        System.out.println("Account: " + itemDebitReformat);
        //Formats debit card and prints it out
        
        System.out.println("Type of Duck Purchased: " + itemName);
        double amount = 1.0 * itemAmount;
        System.out.println("Amount of Duck Purchased: " + amount);
        //Prints the amount and type of duck
       
        itemprice = itemprice.substring(1, itemprice.length());
        double reformat = Double.parseDouble(itemprice);
        System.out.println("Price of Duck Purchased: " + reformat + "\n");
        //Reformats item price
        
        double debitedAmount = amount * reformat;
        System.out.println("$" + debitedAmount + " will be debited to your account\n");
        //multiplies amount times the price to find total amount
        System.out.println("Thank you. Enjoy your duck");
        System.out.println("*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~");
        System.out.println("*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~");
    }
}
