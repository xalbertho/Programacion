import java.util.Scanner;

/*USO DE LA SENTENCIA IF, NOTESE QUE ES SIMILAR A C/C++, SOLO CAMBIA LA SINTAXIS PARA IMPRIMIR EN CONSOLA */

public class ejemplo8 {
    public static void main(String[] args) {
        Scanner teclado= new Scanner(System.in);
        System.out.println("Ingrese su edad: ");
        int edad=teclado.nextInt();

        if(edad>= 18)
        {
            System.out.println("Usted es mayor de edad");

        }
        else{
            System.out.println("Usted es menor de edad");
        }
        teclado.close();
    }
    
}
