/*En este codigo veremos algunos de los metodos que nos proporciona string
 * String= una referencia a un tipo de dato, de uno o varios caracteres
 * referencia al tipo de dato que se tiene acceso
 * Al igual que en c, java distingue ente mayusculas o minusculas
 */

public class ejemplo15 {
    public static void main(String[] args) {
        
        String name="Alberto";

        boolean resultado=name.equals("Alberto"); // booleano, devuelve true or false, dependiendo la condicion,, y si esta se cumple
        boolean resultado2=name.equalsIgnoreCase("alberto");//  ingora las diferencias entre mayusculas o minusculas, (devuelve true)
        System.out.println(resultado);
        System.out.println(resultado2);

        int longitud=name.length();// devuelve el numero de caracteres 
        System.out.println(longitud);

        char semilongitus= name.charAt(2); // devuelve el caracter de la posicion indicada
        System.out.println(semilongitus);

        int posicion=name.indexOf("o"); // devuelve la posicion del caracter especificado en el array indicado
        System.out.println(posicion);

        boolean vacio=name.isEmpty(); // este metodo devuelve true or false, si la cadenea es vacio o no, respectivamente (en este caso es false)
        System.out.println(vacio);

        String mayusculas=name.toUpperCase(); // convierte el string a mayusculas
        System.out.println(mayusculas);

        String minusculas=name.toLowerCase(); //convierte el string a minusculas
        System.out.println(minusculas);

        // String sinespacion=name.trim(); // elimna los cacacteres blancos iniciales y finales
         String remplazo=name.replace('o', 'a'); // remplaza caracteres de un string, en este caso cambiamos la '0' por 'a'
         System.out.println(remplazo);

         

    }
}
