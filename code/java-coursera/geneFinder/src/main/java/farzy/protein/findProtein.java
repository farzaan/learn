package farzy.protein;

import edu.duke.*;

import java.util.ArrayList; 
import java.util.List;
import java.io.*;

public class findProtein {
	public void startRet(String dna){
		int start = 0;
		
		while (true){
			int loc = dna.indexOf("atg", start);
			if(loc == -1){
				break;
			}
			System.out.println(loc);
		}
		
	}
    
    
    
    public void finProtein(String dna){
    	String nedna = dna.toLowerCase();
    	String f = null;
    	int start = nedna.indexOf("atg");
    	
    	int ende = stopIndex(nedna, start);
    	while(start != -1){
    		
    		System.out.println(start);
    		System.out.println(ende);
    		
    		System.out.println(nedna.substring(start, ende+3));
    		nedna = nedna.substring(ende);
    		
    		start = nedna.indexOf("atg");
    		ende = stopIndex(nedna, start);
    	}
    	
       
    }
    
    /*
     * This will check for where the Codon ends
     */
    
    public int stopIndex(String dna, int index){
       int stop1 = dna.indexOf("tga", index);
       if(stop1 == -1 || (stop1 -index) % 3 != 0){
    	   stop1 = dna.length();
       }
       int stop2 = dna.indexOf("tag", index);
       if(stop2 == -1 || (stop2 -index) % 3 != 0){
    	   stop2 = dna.length();
       }
       int stop3 = dna.indexOf("taa", index);
       if(stop3 == -1 || (stop3 -index) % 3 != 0){
    	   stop3 = dna.length();
       }
       return Math.min(stop1, Math.min(stop2, stop3));
       
    	
       
       
    }
    /*
    public void testing(){
        String input = ("AATGCTAGTTTAAATCTGA");
        String nes = finProtein(input);
        
       
        System.out.println(nes);
    }
*/
    public void realTesting(){
       DirectoryResource dr = new DirectoryResource();
        
       for(File f : dr.selectedFiles()){
           FileResource fil = new FileResource(f);
           String s = fil.asString();
           finProtein(s);
        }
    }

}

