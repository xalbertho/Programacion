/*
 * En este programa hacemos el uso de .equals, la cual nos ayuda a comparar cadenas, indicando si tienen la misma direccion de memoria
 */


import java.util.Scanner;

public class ejemplo10 {
    public static void main(String[] args) {
     
        Scanner repuestas=new Scanner(System.in);
        System.out.println("Ingresa 'Q' para terminar ");
        String respuesta=repuestas.nextLine();

        if(respuesta.equals("Q") || respuesta.equals("q"))
        {
            System.out.println("Juego terminado");
        }
        else 
        {
            System.out.println("El jueno no a sido terminado");
        }
        repuestas.close();
    }
}
