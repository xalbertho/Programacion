/*
 * method= a block of code that is executed whenever it is called upon
 * digamos que es similar a una funcion en c/c++
 */

import java.util.Scanner;

public class ejemplo20 {
    
    public static void main(String[] args) {
        hello();

        Scanner teclado=new Scanner(System.in);
        System.out.println("Ingrese un numero: ");
        int x=teclado.nextInt();

        System.out.println("Ingrese un numero: ");
        int y=teclado.nextInt();
        suma(x, y);
        teclado.close();
        
    }
    static void hello()
    {
        System.out.println("Welcome");
    }
    static void suma(int x, int y)
    {
        int resultado=x+y;
        System.out.println("La suma es: "+resultado);
    }
   
}
