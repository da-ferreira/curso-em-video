
package source;

import java.util.Arrays;

/**
 * @author david-ferreira
 */

public class Vetor05 {
    public static void main(String[] args) {
        /* Preenchendo um vetor com um único valor */
        int vetor[] = new int[100];
        Arrays.fill(vetor, 1);  // Todas as posições do vetor estão igual a 1.
        
        for (int valor : vetor) {
            System.out.println(valor);
        }
    }
}
