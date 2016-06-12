

public class tagfinder 
{
    public String findProtein(String dna){
        int start = dna.indexOf("atg");
        int stop = dna.indexOf("tag", start+3);
        if ((stop-start) % 3 == 0){
            return dna.substring(start, stop+3);
        }
        else{
            return ("");
        }
    }
}
