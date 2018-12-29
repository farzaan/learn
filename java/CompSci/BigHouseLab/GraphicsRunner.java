//(c) A+ Computer Science
//www.apluscompsci.com

//Name - Farzaan Nasar  
//Date - 9/4
//Class - Comp Sci
//Lab  - Big Hpuse

import javax.swing.JFrame;

public class GraphicsRunner extends JFrame
{
    private static final int WIDTH = 800;
    private static final int HEIGHT = 600;

    public GraphicsRunner()
    {
        super("Graphics Runner");

        setSize(WIDTH,HEIGHT);

        getContentPane().add(new BigHouse());
        
        //added other classes to run them 
        

        setVisible(true);

        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }

    public static void main( String args[] )
    {
        GraphicsRunner run = new GraphicsRunner();
    }
}