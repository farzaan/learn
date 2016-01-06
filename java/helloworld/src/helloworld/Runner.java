package helloworld;

import classtest.FirstClass;

public class Runner {

	public static void main(String[] args) {
		testMeths();
		//somemeth();
	}
	
	private static void testMeths(){
		FirstClass myclass = new FirstClass();
		myclass.isBo = false;
		myclass.Examplestring = ("This is a set of data");
		System.out.print(myclass.Examplestring);
		new Variabes().testScoping(12);
		new Types().firstnum();
		new Types().stringstest();
		new Types().arrays();
	}
	
	private static void somemeth(){
		System.out.println("hello world, WTH");
		
		
		String text = "iwe";
		
		switch(text){
		case "iwe":
			System.out.println("yo kai watch");
			break;
		default:
			System.out.println("This");
		}
	}
}
