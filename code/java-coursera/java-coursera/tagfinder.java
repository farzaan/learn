import edu.duke.*;
import java.io.*;

public class tagfinder 
{
    public String findProtein(String dna){
        int start = dna.indexOf("atg");
        int stop = dna.indexOf("tag", start+3);
        if(start == -1){
            return ("");
        }
        if ((stop-start) % 3 == 0){
            return dna.substring(start+3, stop);
        }
        else{
            return ("");
        }
    }
    public void testing(){
    String input = ("gatatgggctgctagtgtggtagtgatgctgctcgctgctgatccgtcgtaagtgtgtgtacgatgctagc");
    String correct = ("ggctgc");
    String resuly = findProtein(input);
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
            System.out.println("this" + findProtein(s));
        }
    }
}
