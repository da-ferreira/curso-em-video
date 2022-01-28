
package source;

import java.util.Scanner;

/**
 * @author david-ferreira
 */

public class IdadePessoa {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in); 
        
        System.out.print("Digite seu ano de nascimento: ");
        int ano_nascimento = in.nextInt();
        int idade = 2021 - ano_nascimento;  // idade da pessoa.
        
        System.out.printf("Sua idade é %d.\n", idade);
        
        if (idade >= 18) {
            System.out.println("Voce é MAIOR de idade.");
        }
        else {
            System.out.println("Voce é MENOR de idade.");
        }
    }
}
