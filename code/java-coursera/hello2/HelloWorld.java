import edu.duke.*;

public class HelloWorld {
	/**
	 * Read file of ways to say hello and print each line of the file
	 */
	public void sayHello(){
		URLResource webpage = new URLResource("http://www.dukelearntoprogram.com/java/somefile.txt"); 
		for (String words : webpage.words()) {
			System.out.println(words);

		}
System.out.println("Htis");

	}
}
