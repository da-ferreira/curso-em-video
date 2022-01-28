
package source;

import java.util.Scanner;

/**
 * @author david-ferreira
 */

public class Numeros {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        
        int numero;
        int soma = 0;
        String resposta;
        
        do {
            System.out.print("Digite um número: ");
            numero = in.nextInt();
            
            soma += numero;
            
            System.out.print("Quer continuar? [S/N]: ");
            resposta = in.next();
            
        } while (resposta.equals("S"));
        
        System.out.println("A soma de todos os valores digitados é " + soma);
    }
}
