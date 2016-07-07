package farzy.countryExports;

import org.apache.commons.csv.CSVParser;
import org.apache.commons.csv.CSVRecord;

import edu.duke.FileResource;
/*
 * The CSV file exportdata.csv has information on the export products of countries; you can download a .zip folder with this and other export data files here.
In particular it has three column headers labeled Country, Exports, and Value (dollars). The Country column represents a country from the world, the Exports 
column is a list of export items for a country, and the Value (dollars) column is the dollar amount in millions of their exports in the format of a dollar sign,
 followed by an integer number with a comma separator every three digits from the right. An example of such a number might be “$400,000,000”.


 */
public class CountyExports {
	/*/
	 * Write a method named countryInfo that has two parameters, parser is a CSVParser and country is a String. 
	 * This method returns a string of information about the country or returns “NOT FOUND” if there is no information about the country. 
	 * The format of the string returned is the country, followed by “: “, followed by a list of the countries’ exports, followed by “: “, followed by the 
	 * countries export value.
	 *  For example, using the file exports_small.csv and the country Germany, the program returns the string:
	 */
	
	
	
	public String countryInfo(CSVParser parser , String Country){
		String cntryInfo = null;
		for(CSVRecord cntryRecord: parser){
			String cntryName = cntryRecord.get("Country");
			if(Country.equals(cntryName)){
				cntryInfo = String.format("%s: %s: %s",Country , cntryRecord.get("Exports"), cntryRecord.get("Value (dollars)"));
			}
		}
		
		return cntryInfo;
	}
	
	
	public void methTester(){
		FileResource fr = new FileResource();
		CSVParser parser = fr.getCSVParser();
		System.out.println(countryInfo(parser , "Germany"));
	}
}
