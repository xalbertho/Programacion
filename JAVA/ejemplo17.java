/*En este ejercicio veremos algunas cosas sobre lista de arreglos
 * arraylist=   una matriz redimensionable. Se pueden agregar y eliminar elementos después de la fase de compilación.
 *              almacenar tipos de datos de referencia
 */

import java.util.ArrayList;

public class ejemplo17 {
    public static void main(String[] args) {

        ArrayList<String> comida=new ArrayList<String>(); // esta es la sintaxis para crear una lista 
        comida.add("Pizza"); // para agregar un dato a la lista dinamica, usamos el metodo (nombrecadena).add(dato);
        comida.add("Tacos");
        comida.add("Hamnurgesas");

        //Para imprimir los datos de la lista usamos .get(posicion)
        // para hacer esto mas rapido, usamos un ciclo for
        for(int i=0; i<comida.size();i++)
        {
            System.out.println(comida.get(i)); //observemos que para obtener el dato, es similar a las interfaces graficas de Matlab----> .get(dato)
        }

        System.out.println();
        //podemos actualizar el valor de un elemento por individual usando el comando .set(posicion,dato)
        // solo se actualiza el primer valor, mas no se actualiza la longitud del array
        comida.set(0,"Pollo");
        for(int i=0; i<comida.size();i++)
        {
            System.out.println(comida.get(i)); //observemos que para obtener el dato, es similar a las interfaces graficas de Matlab----> .get(dato)
        }

        //tambien podemos remover un valor del array
        // removera el dato, y reducira el numero de elementos del array
        System.out.println();
        comida.remove(1);

        for(int i=0; i<comida.size();i++)
        {
            System.out.println(comida.get(i)); //observemos que para obtener el dato, es similar a las interfaces graficas de Matlab----> .get(dato)
        }





        
    }
}
