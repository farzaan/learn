package farzy.makeGray;

import edu.duke.*;

public class MakeGray{

	public ImageResource makeGray(ImageResource imgIn){
		ImageResource retImg = new ImageResource(imgIn.getHeight(), imgIn.getWidth());
		for(Pixel pix: retImg.pixels()){
			
			Pixel inPixel = imgIn.getPixel(pix.getX(), pix.getY());
			
			int avg = inPixel.getRed() + inPixel.getGreen() + inPixel.getBlue();
			int clrSet = avg/3;
			pix.setRed(clrSet);
			pix.setBlue(clrSet);
			pix.setGreen(clrSet);
		}
		
		return retImg;
	}
	
	public void testGray(){
		ImageResource in = new ImageResource();
		ImageResource er = makeGray(in);
		er.draw();
	}
	
	
	
}
