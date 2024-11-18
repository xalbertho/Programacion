/*
 * En este  ejemplo veremos arrays en 2 dimensiones, lo que comunmente conocemos como matrices;
 * 
 */

import java.util.Scanner;

public class ejemplo14 {

    public static void main(String[] args) {
        
        Scanner teclado= new Scanner(System.in);
        String[][] nombres= new String[2][2];


        for(int i=0; i<nombres.length;i++)
        {
            
                for(int j=0; j<nombres[i].length;j++)
                {
                System.out.println("Ingrese el modelo del elemto "+i+j);
                nombres[i][j]=teclado.nextLine();
                }
            
        }
        
        System.out.println();
        
        for(int i=0; i<nombres.length;i++)
        {
            
                for(int j=0; j<nombres[i].length;j++)
                {
                System.out.print(nombres[i][j]);
                System.err.print(" ");
             
                }
                System.out.println();
            
        }
        teclado.close();
    }
    
}
