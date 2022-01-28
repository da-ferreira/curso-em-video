
package source;

/**
 * @author david-ferreira
 */

public class ComparacaoString {
    public static void main(String[] args) {
        String nome1 = "David";
        String nome2 = "David";
        String nome3 = new String("David");
        
        // Isso resultara em falso, porque as estruturas são diferentes,
        // embora o conteudo seja igual.
        System.out.println(nome1 == nome3);
        
        // É recomendado usar o método String.equals(string2) para checar
        // se o conteudo de duas Strings são iguais.
        // Isso tmb se aplica a todas as classes involucros.
        System.out.println(nome1.equals(nome3));
    }
}
