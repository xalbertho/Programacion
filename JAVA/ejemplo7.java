/* EN este programa veremos la forma de generar valores aleatorios
 * debemos imporyar Random, usar la classe random para definir random y 
 * poder usar esto, de tal forma que x=random();, si ponemos un valor en los
 * parentesis, saldra un valor de cero hasta un numero menor al que ingresamos
 */
import java.util.Random;

public class ejemplo7 {
    public static void main(String[] args) {
        Random random=new Random();

        int x=random.nextInt(6);
        double y=random.nextDouble();
        boolean z=random.nextBoolean();

        System.out.println(z);
        System.out.println(y);
        System.out.println(x);
    }
}
