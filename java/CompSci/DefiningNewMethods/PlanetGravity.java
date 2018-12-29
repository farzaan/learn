
/**
 * Find the gravity force on different planets 
 *
 * @author Syed Nasar
 * 
 */
public class PlanetGravity
{
    // instance variables - replace the example below with your own
    public static void main(String[] args){
        String[] planets = {"Mercury", "Earth", "Venus", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"};
        double[] diameter = {4880, 12756, 12103.6, 6794, 142984, 120536, 51118, 49532};
        double[] mass = {3.30e23, 5.97e24, 4.869e24, 6.421e23, 1.900e27, 5.68e26, 8.68e25, 1.0247e26};
        double[] gravityList = new double[planets.length];
        for(int i = 0; i < planets.length; i++ ){
            gravityList[i] = gravityMeth(diameter[i] * 1000, mass[i]);
            //Plugs the data into the method^^  
        }
        printer(planets, diameter, mass, gravityList);
    }
    public static double gravityMeth(double diameter, double mass){
        double gravity = ((6.67*Math.pow(10,-11)) * mass)/Math.pow(diameter/2, 2);
        return gravity;
    }
    public static void printer(String[] planets, double[] diameter, double[] mass, double[] gravityList){
        System.out.printf("%8s%8s%8s%8s\n", "Planet","Diameter(km)","Mass(km)","g(m/s^s))");
        for(int i = 0; i < planets.length; i++){
            System.out.printf("%8.2f%8.2f%8.2f%8.2f\n", planets[i], diameter[i], mass[i], gravityList[i]);
            System.out.println(gravityList[i]);
        }
    }
}
