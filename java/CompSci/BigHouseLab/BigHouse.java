//(c) A+ Computer Science
//www.apluscompsci.com

//Name - Farzaan Nasar  
//Date - 9/4
//Class - Comp Sci
//Lab  - Big Hpuse

import java.awt.Graphics;
import java.awt.Color;
import java.awt.Canvas;

public class BigHouse extends Canvas
{
   public BigHouse()  //constructor - sets up the class
   {
      setSize(800,600);
      setBackground(Color.WHITE);
      setVisible(true);
   }

   public void paint( Graphics window )
   {
      bigHouse(window);
      
   }

   public void bigHouse( Graphics window )
   {
      window.setColor(Color.BLUE);

      window.drawString( "BIG HOUSE ", 200, 70 );

      window.setColor(Color.BLUE);

      window.fillRect( 200, 200, 400, 400 );
      //^creates house rect^
      window.setColor(Color.YELLOW);
      
      window.fillOval(375,250,50,50);
      //^creates window^
      window.setColor(Color.RED);
      
      window.fillRect(365,400,75,200);
      //^creates door^
      window.setColor(Color.GRAY);
      window.fillArc(200,100,400,200,0,180);
      //^creates roof^
   }
}