
/**
 * ejemplo9
 */

import java.util.Scanner;



public class ejemplo9 {

    public static void main(String[] args) {

        Scanner teclado=new Scanner(System.in);

        String dia=teclado.nextLine();

        switch (dia) {
            case "Lunes":
                System.out.println("Hoy es Lunes ");
                
                break;
            case "Martes":
                System.out.println("Hoy es Martes ");
                break;
            case "Miercoles":
                System.out.println("Hoy es miercoles ");
                break;
            case "Jueves":
                System.out.println("Hoy es jueves ");
                break;
            
            case "Viernes":
                System.out.println("Hoy es viernes");
                break;
            case "sabado":
                System.out.println("Hoy es sabado");
                break;
            case "domingo":
                System.out.println("Hoy es domingo");
                break;

        
            default:
                System.err.println("Dia invalido: ");
                break;
        }
        teclado.close();
    }
}