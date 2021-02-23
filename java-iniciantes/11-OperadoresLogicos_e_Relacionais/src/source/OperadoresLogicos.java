
package source;

/**
 * @author david-ferreira
 */

public class OperadoresLogicos {
    public static void main(String[] args) {
       
        /*
        * Operadores Lógicos
        * 
        * && (AND), (true && false) == false 
        * || (OR), (true || false) == true
        *
        * ^ (XOR), (true ^ true) == false
        *   - Nesse xor, ou uma condição é verdadeira OU EXCLUSICAMENTE
        *   - a outra condição é verdadeira. Ou seja, nunca dois true ou dois false.
        *   - ver exemplo abaixo.
        *        
        * ! (NOT), (! false) == true
        */
        
        System.out.println(! true);  // <- false
        
        System.out.println("\n---XOR---\n");
        System.out.println(true ^ true);  // <- false
        System.out.println(true ^ false);  // <- true
        System.out.println(false ^ true);  // <- true
        System.out.println(false ^ false);  // <- false
    }
}
