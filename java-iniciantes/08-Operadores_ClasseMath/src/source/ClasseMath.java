
package source;

public class ClasseMath {
    public static void main(String[] args) {
        double PI = Math.PI;  // valor de pi
        int exponenciacao = (int) Math.pow(4, 2);
        double raiz_quadrada = Math.sqrt(25);
        double raiz_cubica = Math.cbrt(27);
        
        // Arredondamentos
        
        System.out.println(Math.abs(-10));  // valor absoluto, ou seja, fica so 10.
        System.out.println(Math.floor(3.9));  // arredonda para baixo (chão), resulta em 3.
        System.out.println(Math.ceil(4.2));  // arredonda para cima (teto), resulta em 5.
        
        // Se o valor depois da virgula for >= a 5, o arredondamento é feito para cima,
        // caso contrário, é feito para baixo.
        System.out.println(Math.round(5.6));  // arredonda aritmeticamente, resulta em 6
        System.out.println(Math.round(5.4));  // resulta em 5.
        System.out.println(Math.round(5.5));  // resulta em 6.
        
        // GERADOR DE NUMEROS ALEATÓRIOS
        // Math.random() <- gera um numero aleatorio (double) entre 0.0 e 1.0.
        System.out.println(Math.random());
        
        /*
        * Há um macete matematico para pegar numeros aleatorios em intervalos. Segue a formula abaixo:
        *
        * inicio_do_invervalo + Math.random() * (fim_do_intervalo - inicio_do_invervalo)
        *
        * Se eu quero um numero entre 5 até 10, faço:
        * 5 + Math.random() * (10 - 5)
        *
        * Se eu quero um numero entre 0 até 9, faço:
        * 0 + Math.random() * (9 - 0)
        */
        
        int random_5_10 = (int) (5 + Math.random() * (10 - 5));
        int random_0_9 = (int) (0 + Math.random() * (9 - 0));
        
        System.out.println("Numero aleatio entre 5 até 10: " + random_5_10);
        System.out.println("Numero aleatio entre 0 até 9: " + random_0_9);
    }
}
