
package tiposdedados;

/**
 * @author da-ferreira
 */

public class ModosDeAtribuicao {
    public static void main(String[] args) {
        // Declarando uma váriavel
        int idade1 = 3;
        float salario1 = 1825.54f;
        char letra1 = 'G';
        boolean casado1 = false;
        
        
        // Declarando uma váriavel com typecast, ou seja,
        // o valor tem que ser considerado como seu tipo (int, float, etc.)
        int idade2 = (int) 3;
        float salario2 = (float) 1825.54;
        char letra2 = (char) 'G';
        boolean casado2 = (boolean) false;
        
        
        // Declarando uma váriavel com classe
        // logo ela é um objeto, não uma variável.
        Integer idade3 = new Integer(3);
        Float salario3 = new Float(1825.54);
        Character letra3 = new Character('G');  // char
        Boolean casado3 = new Boolean(false);
    }
}
