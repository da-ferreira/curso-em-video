
package source;

import java.util.Scanner;

/**
 * @author david-ferreira
 */

public class OperadorTernario {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        
        System.out.print("Digite um numero: ");
        int n1 = in.nextInt();
        System.out.print("Digite outro numero: ");
        int n2 = in.nextInt();
        
        /*
         * a variável maior receberá o maior entre os dois.
         * O operador ternário funciona da seguinte maneira:
         * <expressao> ? <valor caso a expressao seja verdadeira> : <valor caso nao seja>;
         */
        
        int maior = n1 > n2 ? n1 : n2;
        int subtracao = n1 > n2 ? n1 - n2 : n2 - n1;
        
        System.out.printf("O maior é %d\n", maior);
        System.out.printf("Subtracao %d\n", subtracao);
    }
}
