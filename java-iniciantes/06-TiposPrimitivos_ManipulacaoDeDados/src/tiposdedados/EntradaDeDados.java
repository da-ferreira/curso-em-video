
package tiposdedados;

import java.util.Scanner;

public class EntradaDeDados {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        
        System.out.print("Digite o nome do aluno: ");
        String nome = in.nextLine();
        
        System.out.print("Digite a nota do aluno: ");
        float nota = in.nextFloat();
        
        System.out.printf("A nota de %s é %.2f\n", nome, nota);
        
    }
}
