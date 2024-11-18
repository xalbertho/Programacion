/*
 * En este ejercicio vamos a implentear el uso de arrays
 * pareciese q se pueden crear arrays dinamicos de la misma forma que en c++
 */

import java.util.Scanner;

public class ejemplo13 {
    
    public static void main(String[] args) {
        
        String[] nombres=new String[3]; //notese  que al comparar con c/c++, hay una diferencia al momento de delclarar un array
        int[] numero=new int[3]; 

        Scanner teclado=new Scanner(System.in);
        nombres[0]="Alberto";
        nombres[1]="barrios";
        nombres[2]="Jose";

        for(int i=0;i<3;i++)
        {
            System.out.println("Ingresa el numero del nombre: "+nombres[i]);
            numero[i]=teclado.nextInt();
            
        }

        for(int i=0; i<3;i++){

        System.out.println("EL USUARIO "+nombres[i]+" Tiene el numero "+numero[i]);
        }
        teclado.close();
    }
}
