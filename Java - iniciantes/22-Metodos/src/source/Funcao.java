
package source;

/**
 * @author david-ferreira
 */

public class Funcao {
    public static void main(String[] args) {
        int valor = soma(10, 15);
        System.out.println("A soma vale " + valor);
    }
    
    static int soma(int a, int b) {
        return a + b;
    }
}
