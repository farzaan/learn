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
	/*
	 * 5. Write a void method named bigExporters that has two parameters, parser is a CSVParser, and amount is a String in the format of a dollar sign, 
	 * followed by an integer number with a comma separator every three digits from the right. An example of such a string might be “$400,000,000”. 
	 * This method prints the names of countries and their Value amount for all countries whose Value (dollars) string is longer than the amount string.
	 *  You do not need to parse either string value as an integer, just compare the lengths of the strings. For example, if bigExporters is called with the file
	 *   exports_small.csv and amount with the string $999,999,999, then this method would print eight countries and their export values shown here
	 */
	 public void bigExporters(CSVParser parser,String amount){
		 int y = amount.length();
		 for(CSVRecord record: parser){
			 int x = record.get("Value (dollars)").length();
			 if (x >= y){
				 System.out.println(String.format("%s %s", record.get("Country"), record.get("Value (dollars)")));
			 }
		 }
		 
	 }
	
	
	
	/*
	 * Write a method named numberOfExporters, which has two parameters, parser is a CSVParser, and exportItem is a String. 
	 * This method returns the number of countries that export exportItem. 
	 * For example, using the file exports_small.csv, this method called with the item “gold” would return 3.
	 */
	public int numberOfExporters(CSVParser parser, String exportItem){
		int cntCntr = 0;
		for(CSVRecord record: parser){
			if(record.get("Exports").contains(exportItem)){
				cntCntr++;
			}
		} 
		
	return cntCntr;
	}
	
	
	/*
	 * Write a void method named listExportersTwoProducts that has three parameters, parser is a CSVParser, exportItem1 is a String and exportItem2 is a String. 
	 * This method prints the names of all the countries that have both exportItem1 and exportItem2 as export items. 
	 * For example, using the file exports_small.csv, this method called with the items “gold” and “diamonds” would print the countries
	 */
	public void listExportersOfTwoProducts(CSVParser parser, String export1, String export2){
		
		for(CSVRecord record: parser){
			String preSplit = record.get("Exports");
			if(preSplit.contains(export1) && preSplit.contains(export2)){
				System.out.println(record.get("Country"));
				
			}
		}
	}
	
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
		listExportersOfTwoProducts(parser, "gold", "diamonds");
		parser = fr.getCSVParser();
		System.out.println(countryInfo(parser , "Germany"));
		parser = fr.getCSVParser();
		System.out.println(numberOfExporters(parser, "gold"));
		parser = fr.getCSVParser();
		bigExporters(parser, "$999,999,999");

		
	}
}
