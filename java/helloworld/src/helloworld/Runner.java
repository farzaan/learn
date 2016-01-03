package helloworld;

public class Runner {

	public static void main(String[] args) {
		testMeths();
	}
	
	private static void testMeths(){
		
		new Variabes().testScoping(12);
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
