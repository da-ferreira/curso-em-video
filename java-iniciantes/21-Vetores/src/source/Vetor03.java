
package source;

import java.util.Arrays;

/**
 * @author david-ferreira
 */

public class Vetor03 {
    public static void main(String[] args) {
        double valores[] = {3.5, 2.75, 9, -4.50, 3.14159};
        
        Arrays.sort(valores);  // Ordenando o vetor.
        
        for (double valor: valores) {
            System.out.println(valor);
        }
    }
}
