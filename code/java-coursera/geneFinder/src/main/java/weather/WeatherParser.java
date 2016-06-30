package weather;

import org.apache.commons.csv.CSVParser;
import org.apache.commons.csv.CSVRecord;

import edu.duke.FileResource;

public class WeatherParser {
	
	/***
	 * This method returns the CSVRecord with the coldest temperature in the file
	 * and thus all the information about that coldest temperature, such as the hour of the
	 * coldest temperature
	 * @param parser
	 * @return
	 */
	public CSVRecord coldestHourInFile(CSVParser parser){
		
		
		
		
		return null;
		
	
	}
	
	
	/***
	 * Write the method fileWithColdestTemperaturethat has no parameters. This
method should return a String that is the name of the file from selected files that has the
coldest temperature.
	 */
	public String fileWithColdestTemperature(){
		return null;
	}
	
	
	/***
	 * You should also write a void method named
testFileWithColdestTemperature()to test this method. Note that after
determining the filename, you could call the method coldestHourInFileto
determine the coldest temperature on that day.
	 */
	public void testFileWithColdestTemperature(){
		
	}
	
	
	
	
	/***
	 * test this method and print out information about that
	 * coldest temperature such as the time of its occurrence.
	 * 
	 * NOTE: Sometimes there was not a valid reading at a specific hour, so the temperature
	 * field says ­9999. You should ignore these bogus temperature values when calculating
	 * the lowest temperature
	 */
	public void testColdestHourInFile(){
		
		FileResource fr = new FileResource();
		CSVParser parser = fr.getCSVParser();
		
		CSVRecord csvrecord = coldestHourInFile(parser);
		
		
		
		
	}

}
