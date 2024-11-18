import java.util.Scanner;

/**
 * abarcamos algunas de las funciones que contiene java, como lo son:
 * Math.max(double, double)--> regresa el valor maximo
 * Math.abs(y)---> devuelve su valor absoluto;
 * math.sqrt(y) ---> devuelve la raiz cuadrada
 * math.round ---> redondea el valor
 * math. ceil ---> redonde siempre hacia arriba 3,14=4;
 * 
 */
public class ejemplo6 {

    public static void main(String[] args) {
        double x;
        double y;

       double z;
       Scanner scanner=new Scanner(System.in);
       System.out.println("Ingresa el lado de x: ");
       x=scanner.nextDouble();
       
       System.out.println("Ingresa el valor de y: ");
       y=scanner.nextDouble();

        
      z= Math.sqrt((x*x)+(y*y));

      System.out.println("La hipotenusa es: "+z);

      scanner.close();

    
    }
}