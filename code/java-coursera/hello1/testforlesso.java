import edu.duke.*;
import java.io.*;
/**
 * Write a description of testforlesson here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class testforlesso{
    
public ImageResource makeGray(ImageResource inImage){
    ImageResource outImage = new ImageResource(inImage.getWidth(), inImage.getHeight());
    for(Pixel pixel: outImage.pixels()){
        Pixel inPixel = inImage.getPixel(pixel.getX(), pixel.getY());
        int RGBval = (inPixel.getRed() + inPixel.getBlue() + inPixel.getGreen())/3;
        pixel.setRed(RGBval);
        pixel.setBlue(RGBval);
        pixel.setGreen(RGBval);
        

    }
    return outImage;
}

//public void testgray(){
  //  ImageResource pic = new ImageResource();
    //ImageResource gray = makeGray(pic);
    //ray.draw();
//}
public void selectandconvert(){
    DirectoryResource dric = new DirectoryResource();
    for(File f : dric.selectedFiles()) {
        ImageResource inImage = new ImageResource(f);
        ImageResource grayim = makeGray(inImage);
        grayim.draw();
    }
   
}
}

