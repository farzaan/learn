package helloworld;

import classtest.FirstClass;

public class Variabes {
	private  static int age = 50;
	public void testScoping(int aAge){
		FirstClass clasimport = new FirstClass();
		clasimport.isBo = true;
		clasimport.print();
		clasimport.print("This is an overloaf");
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
