
package tiposdedados;

public class TiposDeDados {
    public static void main(String[] args) {
        /*
         * Familia: Lógico  
         * Tipo Primitivo: boolean
         * Classe Invólucro: Boolean
         * Tamanho: 1 bit
         */
        
        boolean verdadeiro = true;
        
        /*
         * Familia: Literais  
         * Tipo Primitivo: char
         * Classe Invólucro: Character, String
         * Tamanho: 1 byte, 1 byte cada
         */
        
        char opcao = 'A';
        String nome = "JAVA";
        
        /*
         * Familia: Inteiros  
         * Tipo Primitivo: byte, short, int, long
         * Classe Invólucro: Byte, Short, Integer, Long
         * Tamanho: 1 byte (até 127), 2 byte (até 32.767), 4 byte (até 2.147.483), 8 byte (até 2^63)
         */
        
        byte idade = 90;
        short renda = 10000;
        int populacao = 2000000;
        long chinaMaisIndia = 3500000;
        
         /*
         * Familia: Reais  
         * Tipo Primitivo: float, double
         * Classe Invólucro: Float, Double
         * Tamanho: 4 byte (até 7 digitos depois da virgula), 8 byte (até 15 digitos depois da virgula)
         */
         
         float salario = 1580.5687f;
         double pi = 3.141592653589793;
        
        
    }
}
