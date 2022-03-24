
package source;

/**
 * @author david-ferreira
 */

public class Contador01 {
    public static void main(String[] args) {
        int contador = 0;
        
        while (contador < 10) {
            contador++;
            
            /* O comando continue, ao ser executado dentro de um loop,
             * ignora tudo que está em baixo (os comandos) e volta a executar
             * a condição do laço. No caso abaixo, se o contador for 5 ou 7,
             * a linha de execução do programa voltará a condição do laço, 
             * não executando o println.
             */
            if (contador == 5 || contador == 7)
                continue;
            
            System.out.println("Cambalhota " + contador);
        }
    }
}
