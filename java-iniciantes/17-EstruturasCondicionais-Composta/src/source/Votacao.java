
package source;

import java.util.Scanner;

/**
 * @author david-ferreira
 */

public class Votacao {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        
        System.out.print("Digite seu ano de nascimento: ");
        int ano_nascimento = in.nextInt();
        int idade = 2021 - ano_nascimento;
        
        /* SEM ELSE IF */
        
        if (idade < 16) {
            System.out.println("Não vota!");
        }
        else {
            if ((idade >= 16 && idade < 18) || (idade > 70)) {
                System.out.println("Voto opcional!");
            }
            else {
                System.out.println("Voto obrigatório!");
            }
        }
        
        /* COM ELSE IF */

        if (idade < 16) {
            System.out.println("Não vota!");
        }
        else if ((idade >= 16 && idade < 18) || (idade > 70)) {
            System.out.println("Voto opcional!");
        }
        else {
            System.out.println("Voto obrigatório!");
        }
    }
}
