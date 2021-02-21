
package source;

import java.util.Scanner;

public class OperadoresAritmeticos {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        
        int n1 = 3;
        int n2 = 5;
        
        float media = (n1 + n2) / 2;
        
        System.out.println("A media é " + media);
        
        
        int numero = 5;
        
        /*
        * O pré-incremento faz a adição/subtracao na variavel,
        * e depois, com a variavel, faz as operações restantes.
        *
        * Já o pos-incremento faz todas as operações, e depois faz a
        * adicao/subtracao na varivael.
        *
        * No exemplo abaixo, com o pré-incremento, o "valor" fica com 11.
        * Com o pós-incremenento, o "valor" fica com 10.
        */
        int valor = 5 + ++numero;
        System.out.println(valor);  // <- 11
    }
}
