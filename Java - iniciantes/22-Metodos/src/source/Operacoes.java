
package source;

/**
 * @author david-ferreira
 */

public class Operacoes {
    public static String contador(int inicio, int fim) {
        String formato = "";
        
        for (int i=inicio; i <= fim; i++) {
            formato += i + " ";
        }
        
        return formato;
    }
}
