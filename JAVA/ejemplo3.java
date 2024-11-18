import java.util.Scanner;

 /**
  * ejemplo3
  */
 public class ejemplo3 {
 
    public static void main(String[] args) {
        
        Scanner scanner= new Scanner((System.in));

        System.out.println("Cual es tu nombre?: ");
        String name=scanner.nextLine();
        System.out.println("Cuantos años tienes? :");
        int x= scanner.nextInt();
        // debemos tomar en cuenta que .nextInt solo alamacenara el valor de la edad (18\n)
        // y dejara el salto de linea \n. asi cuando llamamos el siguiente .nextLine sonsume ese
        //caracter y lo guarda como una linea vacia. Para solucionar este problema basta con llamar
        // nexline() para que absorva ese caracter vacio
        scanner.nextLine(); // consumir el caracter \n
        System.out.println("Cual es tu comida favorita?: ");
        String food=scanner.nextLine();


        System.out.println("Hello "+name);
        System.out.println("Tu tienes "+x+" años de edad");
        System.out.println("Tu comida favorita es: "+food);

        scanner.close();

    }
 }