
package source;

import java.util.Arrays;

/**
 * @author david-ferreira
 */

public class Vetor04 {
    public static void main(String[] args) {
        int vetor[] = {3, 7, 6, 1, 9, 4, 2};
        Arrays.sort(vetor);
        int posicao = Arrays.binarySearch(vetor, 1);
        
        System.out.println(posicao); 
    }
}
