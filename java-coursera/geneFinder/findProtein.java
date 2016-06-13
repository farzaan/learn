

public class findProtein {
    public String finProtein(String dna){
       int start = dna.indexOf("atg");
       String next = dna.substring(start);
       return(next);
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

