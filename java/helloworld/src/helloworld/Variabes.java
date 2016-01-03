package helloworld;

public class Variabes {
	private  static int age = 50;
	public void testScoping(int aAge){
		
		//age = 4;
				
		System.out.println(age);
		{
			int age = aAge;
			System.out.println(age);
		}
	
		System.out.println(age);
	}
	
	
public int testPrimitives(int aAge){
		
		//age = 4;
				
		System.out.println(age);
		{
			int age = aAge;
			System.out.println(age);
		}
	
		System.out.println(age);
		
		return age;
	}

}
