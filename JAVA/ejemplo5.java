/* Introduccion a las interfaces en java */

import javax.swing.JOptionPane;
/**
 * ejemplo5
 */
public class ejemplo5 {

    public static void main(String[] args) {
        //          class JOption Ingrea sialgo             valor
        String name=JOptionPane.showInputDialog("Enter your name");
        //uso de Jop  mostrar mensaje        null=compontetne padre, texto que se va a mostrar
        JOptionPane.showMessageDialog(null, "Hello "+ name);

                // convertimos el dato de tipo string a un valor tipo int, con Integer.parseInt--- el resto es igual. se guarda en age
        int age=Integer.parseInt(JOptionPane.showInputDialog("Ingrese su edad"));
        JOptionPane.showMessageDialog(null,"tu tienes"+age+" años");

        // aqui hacemos un proceso similar, solo que convertimos el valor de tipo string a un valor de tipo double
        double altura=Double.parseDouble(JOptionPane.showInputDialog("Ingresa tu estatura: "));
        JOptionPane.showMessageDialog(null, "Tu altura es: "+altura);
        
    }
}

