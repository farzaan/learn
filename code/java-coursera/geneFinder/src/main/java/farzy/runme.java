package farzy;

import farzy.protein.findProtein;
import farzy.weather.WeatherParser;

public class runme {

	public static void main(String[] args){
		WeatherParser wp = new WeatherParser();
		
		wp.testColdestHourInFile();
		
		wp.testFileWithColdestTemperature();
		
		
	  }
}
