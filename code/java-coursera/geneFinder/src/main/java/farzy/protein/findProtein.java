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
    
    
    
    public String finProtein(String dna){
    	String nedna = dna.toLowerCase();
    	int start = nedna.indexOf("atg");
    	String next = stopCodon(nedna.substring(start));
		return next;
    	
       
    }
    
    /*
     * This will check for where the Codon ends
     */
    
    public String stopCodon(String dna){
       
       String nedna = dna.toLowerCase();
       int start = nedna.indexOf("atg");
       if(start == -1){
          return ""; 
        }
        
        
       String next = nedna.substring(start);
       int[] list = new int[] {next.indexOf("tag"), next.indexOf("taa"), next.indexOf("tga")};
       String[] ends = new String[] {"tag", "taa", "tga"};
       int i = 0;

       String endstring = new String();
       
       for(int f : list){
           i++;
       
           if(f != -1 && f - start % 3 == 0){
               endstring = ends[i];
               break;
            }
            
        }
        
      return endstring;
    }
    
    public void testing(){
        String input = ("AATGCTAGTTTAAATCTGA");
        String nes = finProtein(input);
        
        String resuly = stopCodon(input);
        System.out.println(resuly);
        System.out.println(nes);
    }

    public void realTesting(){
       DirectoryResource dr = new DirectoryResource();
        
       for(File f : dr.selectedFiles()){
           FileResource fil = new FileResource(f);
           String s = fil.asString();
           System.out.println("this is a protein => " + finProtein(s));
        }
    }

}

