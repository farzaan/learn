/**
 * Created by farzaannasar on 5/27/16.
 */
import printing.Printer;

public class testClass {
    public static void main(String[] args)
    {
        Printer p = new Printer();
        for(Integer i=1; i <= 100; i++){
            if((i % 2) != 0) {
                i = i * 2;
                p.print(i.toString());
            }
        }



    }
}
