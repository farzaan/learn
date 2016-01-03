package helloworld;

import static org.junit.Assert.*;

import org.junit.Before;
import org.junit.Test;

public class VariabesTest {

	private Variabes sut;
	
	@Before
	public void setUp() throws Exception {
		
		sut = new Variabes();
	}

	@Test
	public void testTestScoping() {
		
		sut.testScoping(12);
		//fail("Not yet implemented");
	}
	
	@Test
	public void testPrimitive() {
		
		
		assertEquals("Should return the outer scope value", 50, sut.testPrimitives(12));
		//fail("Not yet implemented");
	}

}
