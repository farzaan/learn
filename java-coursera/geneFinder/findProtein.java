import edu.duke.*;
import java.io.*;

public class findProtein {
    public String finProtein(String dna){
       String nedna = dna.toLowerCase();
       int start = nedna.indexOf("atg");
       int end = nedna.indexOf(stopCodon(nedna));
       return (nedna.substring(start, end +3));
    }
    public String stopCodon(String dna){
       String nedna = dna.toLowerCase();
       int endsa = dna.length() - 1;
       int start = nedna.indexOf("atg");
       String next = nedna.substring(start, endsa);
       int[] list = new int[] {next.indexOf("tag"), next.indexOf("taa"), next.indexOf("tga")};
       int i = 0;
       for(int f : list){
           i++;
           if(f != -1){
              break ;
            }
           
        }
       String endstring = new String();
       switch(i){
           case 1:endstring = "tag";
                  break;
           case 2:endstring = "taa";
                  break;
           case 3:endstring = "tga";
                  break;    
        }
      
       return endstring;
    }
    public void testing(){
    String input = ("AATGCTAGTTTAAATCTGA");
    String nes = finProtein(input);
    //String resuly = stopCodon(input);
   // System.out.println(resuly);
    System.out.println(nes);
}
    public void realTesting(){
        DirectoryResource dr = new DirectoryResource();
       for(File f : dr.selectedFiles()){
           FileResource fil = new FileResource(f);
           String s = fil.asString();
           System.out.println("this" + finProtein(s));
        }
    }

}

