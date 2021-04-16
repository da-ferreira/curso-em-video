
package source;

/**
 * @author david-ferreira
 */

public class Repeticao {
    public static void main(String[] args) {
        int contador = 1;
        
        /* A diferença do do-while para o while é que o primeiro,
         * executa primeira o bloco de comandos depois a condição.
         */
        
        do {
            System.out.println("Cambalhota " + contador);
            contador++;
            
        } while (contador <= 4);
    }
}
