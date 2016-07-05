package farzy.weather;

import java.io.File;

import org.apache.commons.csv.CSVParser;
import org.apache.commons.csv.CSVRecord;

import edu.duke.DirectoryResource;
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
		
		CSVRecord ColdestSoFar = null;
		for(CSVRecord currentRow : parser){
			 if(ColdestSoFar == null){
				 ColdestSoFar = currentRow;
			 }
			 else
			 {
				 double currentTemp = Double.parseDouble(currentRow.get("TemperatureF"));
				 double Coldest = Double.parseDouble(currentRow.get("TemperatureF"));
				 if(currentTemp < Coldest){
					 ColdestSoFar = currentRow; 
				 }
			 }
		}
		
		
		return ColdestSoFar;
		
	
	}
	
	
	/***
	 * Write the method fileWithColdestTemperaturethat has no parameters. This
method should return a String that is the name of the file from selected files that has the
coldest temperature.
	 */
	public String fileWithColdestTemperature(){
		DirectoryResource dr = new DirectoryResource();
        CSVRecord coldestRecord = null;
        File coldestFile = null;
        
	    for(File f : dr.selectedFiles()){
	           FileResource fil = new FileResource(f);
	           CSVParser rt = fil.getCSVParser();
	           CSVRecord x = coldestHourInFile(rt);
	          
	           if(coldestRecord == null){
	        	   coldestRecord = x;
	           }
	           double Coldest = Double.parseDouble(coldestRecord.get("TemperatureF"));
	           double current = Double.parseDouble(x.get("TemperatureF"));
	           

        	   coldestRecord = x;
        	   coldestFile = f;

	           
	           if(Coldest > current){
	        	   coldestRecord = x;
	        	   coldestFile = f;
	           }		
	    }
	    
	    System.out.println(String.format("Coldest day was in file %s", coldestFile.getName()));
		System.out.println(String.format("Coldest temperature on that day was %s", coldestRecord.get("TemperatureF")));
		
		System.out.println("All the Temperatures on the coldest day were:");
		
		FileResource fil = new FileResource(coldestFile);
        CSVParser rt = fil.getCSVParser();
		for(CSVRecord currentRow : rt){

			System.out.println(String.format("%s %s: %s", currentRow.get("DateUTC"), currentRow.get("TimeEST"), currentRow.get("TemperatureF")));
		}
		
		
		
		return coldestFile.getName();
	}
	
	
	/***
	 * You should also write a void method named
testFileWithColdestTemperature()to test this method. Note that after
determining the filename, you could call the method coldestHourInFileto
determine the coldest temperature on that day.
	 */
	public void testFileWithColdestTemperature(){
		fileWithColdestTemperature();
	}
	
	
	public void printme(String toprint){
		System.out.println(toprint);
		
		
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
		System.out.println(csvrecord.get("TimeEST"));
		
		
		
		
	}

}
