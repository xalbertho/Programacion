
/*
 * Para este ejercicio vamos a hacer uso de una herramienta, la cual es .isBlank, la cual es un valor booleano y devuelve 
 * verdadero si la cadena a comparar esta vacia, de lo contrario devuelve false
 */

import java.util.Scanner;

public class ejemplo11 {
    public static void main(String[] args) {
        
        Scanner teclado=new Scanner(System.in);

        String nombre="";

        while(nombre.isBlank())
        
        {
            System.out.println("Ingrese su nombre: ");
            nombre=teclado.nextLine();
        }
        System.out.println("Bienvenido "+nombre);
        teclado.close();
    }
}
