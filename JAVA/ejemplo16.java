/*Em este ejemplo veremos sobre algunas de las introducciones 
 * proporciona una forma de utilizar tipos de datos primitivos como tipos de datos de referencia.
 *  Los tipos de datos de referencia contienen métodos útiles que se pueden utilizar con colecciones (por ejemplo, Arraylist).
 * en conclusion son funciones o envulturas que van a almacenar el tipo de dato
 * // primitive(datos primitivos)     // wrapper(clases envolventes)
 * -----------                        //----------
 * boolean                               Boolean
 * char                                     character
 * int                                   Integer
 * double                                  Double
 * 
 * Autoboxing= proceso atumatico mediante el cial java convierte un tipo  primiticco en su correspondiete clase envolvente cuando sea necesario
 * Unboxig= proceso opuesto, donde java convierte un objeto de una clase envolvente al tipo primitivo
 * 
*/

public class ejemplo16 {

   
    public static void main(String[] args) {
        Boolean a=true;
       // Character b='@';
        //Integer c=123;
        //Double d=3.1416;
        //String e="Alberto";

        if(a==true)
        {
            System.out.println("This is true");
        }
    }
}
