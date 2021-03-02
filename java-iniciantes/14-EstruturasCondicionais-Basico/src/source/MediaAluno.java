
package source;

import java.util.Scanner;

/**
 * @author david-ferreira
 */

public class MediaAluno {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in); 
     
        System.out.print("Digite a primeira nota do aluno: ");
        float n1 = in.nextFloat();
        System.out.print("Digite a segunda nota do aluno: ");
        float n2 = in.nextFloat();
        
        float media = (n1 + n2) / 2;
        System.out.printf("A  média é %.2f.\n", media);
        
        if (media > 9) {
            System.out.println("PARABENS!!");
        }
    }
}
