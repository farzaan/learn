package helloworld;

public class Runner {

	public static void main(String[] args) {
		testMeths();
		somemeth();
	}
	
	private static void testMeths(){
		
		new Variabes().testScoping(12);
		new Types().firstnum();
		new Types().stringstest();
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
