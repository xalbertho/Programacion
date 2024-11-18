/*Ahora analizaremos lo que es for each (para todo) 
 * for each= traversing technique to iterate trough the elements in array/collection
 *          less steps, more readable
 *          less flexible
*/

import java.util.ArrayList;

public class ejemplo19 {
    public static void main(String[] args) {
        ArrayList<String> animales=new ArrayList<String>();
        animales.add("Gato");
        animales.add("perro");
        animales.add("raton");
        animales.add("Loro");
        
        for(String i:animales)
        {
            System.out.println(i);
        }
    }
    
}
