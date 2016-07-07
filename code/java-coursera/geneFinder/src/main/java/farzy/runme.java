package farzy;

import farzy.protein.findProtein;
import farzy.weather.WeatherParser;
import farzy.countryExports.CountyExports;

public class runme {

	public static void main(String[] args){
		//WeatherParser wp = new WeatherParser();
		CountyExports xs = new CountyExports();
		
		//wp.testColdestHourInFile();
		
		//wp.testFileWithColdestTemperature();
		
		//wp.testaverageTemperatureWithHighHumidityInFile();
		xs.methTester();
		
		
	  }
}
