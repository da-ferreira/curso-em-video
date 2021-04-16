
package source;

/**
 * @author david-ferreira
 */

public class Repeticao {
    public static void main(String[] args) {
        for (int i=1; i <= 10; i += 2) {
            System.out.println(i);
        }
        
        System.out.println();
        
        for (int i=10; i > 0; i -= 2) {
            System.out.println(i);
        }
        
        System.out.println();
        
        for (int i=0; i <= 100; i += 10) {
            System.out.println(i);
        }
    }
}
