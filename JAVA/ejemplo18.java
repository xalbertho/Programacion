/* Veremos ahora sobre los arreglos bidimencionales dinamicos



 *        <<<<<-----  COMENTO ESTE CODIGO PARA QUE NO ME MARQUE LAS ADVERTENCIAS QUE SE DESCRIBEN EN EL CUERPO DE ESTE CODIGO------>
 */

 
 /* 
import java.util.ArrayList;
import java.util.*;

public class ejemplo18 {

    public static void main(String[] args) {

        ArrayList<ArrayList<String>> grocerylist=new ArrayList(); // este array mas adelante se encargara de concatenar todas las listas
        
        //aqui vamos a omitir <String> en arraylist, con el fin de que nos imprima con los corchetes cada array,
        // es posible que nos marque una advertencia al momento de ejecutar el programa
        ArrayList<String> bakeryList= new ArrayList(); // creamos un arreglo con algunos strings
        bakeryList.add("Pasta");
        bakeryList.add("Pan de ajo");
        bakeryList.add("Donas");

        ArrayList<String>  producelist= new ArrayList();// hacemos lo mismo para esta segunda lista
        producelist.add("Jitomates");
        producelist.add("ASDAS");

        ArrayList<String> listabebidas= new ArrayList(); //nuevamente con una tercera lista;
        listabebidas.add("Cocacola");
        listabebidas.add("Agua");


        grocerylist.add(bakeryList); // aquui concatenamos cada lista de tipo string en una lista mayor
        grocerylist.add(producelist);
        grocerylist.add(listabebidas);

        System.out.println(grocerylist); // imprimimos en pantalla las 3 cadenas, notese que se evito <tipo> en new arraylist, esto con el fin de que nos imprima de esta forma -->[elemento1,2,...] 
        System.out.println(grocerylist.get(0).get(0));// esta sintaxis nos ayuda a imprimir de forma mas especifica el elemento 0, del arreglo 0
    

    }
    
}
*/