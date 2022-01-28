
package source;

/**
 * @author daferreira
 */

public class Vetor {
    public static void main(String[] args) {
        /* Primeira forma de criar um vetor */
        
        int vetor1[] = new int[4];
        vetor1[0] = 3;
        vetor1[1] = 5;
        vetor1[2] = 7;
        vetor1[3] = 6;
        
        /* Segunda forma de criar um vetor */
        
        int vetor2[] = {3, 5, 7, 6};
        
        for (int i=0; i < vetor1.length; i++) {
            System.out.println(vetor1[i]);
        }
    }
}
