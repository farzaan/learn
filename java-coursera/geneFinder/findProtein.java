import edu.duke.*;
import java.io.*;

public class findProtein {
    public String finProtein(String dna){
       int start = dna.indexOf("atg");
       String next = dna.substring(start);
       int[] list = new int[] {next.indexOf("tag"), next.indexOf("taa"), next.indexOf("tga")};
       int i = 0;
       for(int f : list){
           i++;
           if(f != -1){
              break ;
            }
           
        }
       String endstring;
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
    String input = ("gatatgggctgctagtgtggtagtgatgctgctcgctgctgatccgtcgtaagtgtgtgtacgatgctagc");
    String correct = ("ggctgc");
    String resuly = finProtein(input);
    if (correct.equals(resuly)) {
        System.out.println("right for "+ input);
    }
    else {
        System.out.println("wrong for testcase "+ resuly);
    }
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

