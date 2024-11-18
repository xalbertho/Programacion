import java.util.Scanner;

public class ejemplo12 {
    public static void main(String[] args) {
        
        Scanner teclado= new Scanner(System.in);
        System.err.println("ingrese un numero: ");
        int n=teclado.nextInt();
        int contador=n-1;
        int a=1;

        for(int i=0; i<n;i++)
        {
            for(int k=0; k<contador;k++)
            {
                System.out.print(" ");
            }

            for(int j=0;j<a;j++)
            {
                System.out.print("*");
            }

            System.out.print(" ");

            for(int j=0;j<a;j++)
            {
                System.out.print("*");
            }


            System.out.println();
        a++;
        contador--;
        }
        teclado.close();
    }
}
