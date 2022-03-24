
package source;

import java.util.Scanner;

/**
 * @author david-ferreira
 */

public class Pernas {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        
        System.out.print("Informe o número de pernas do ser: ");
        int pernas = in.nextInt();
        String tipo;
        
        /* COM SWITCH CASE */
        
        switch (pernas) {
            case 1:
                tipo = "Saci"; 
                break;
            case 2:
                tipo = "Bípede"; 
                break;
            case 3:
                tipo = "Tripé";
                break;
            case 4:
                tipo = "Quadruple";
                break;
            case 6:
                tipo = "Aranha";
                break;
            default:
                tipo = "ET";
        }
        
        System.out.println("Isto é um " + tipo + ".");
        
        /* COM ELSE IF */
    
        System.out.print("Informe o número de pernas do ser: ");
        pernas = in.nextInt();
        
        if (pernas == 1) {
            tipo = "Saci";
        }
        else if (pernas == 2) {
            tipo = "Bípede";
        }
        else if (pernas == 3) {
            tipo = "Tripé";
        }
        else if (pernas == 4) {
            tipo = "Quadruple";
        }
        else if (pernas == 6) {
            tipo = "Aranha";
        }
        else {
            tipo = "ET";
        }
        
        System.out.println("Isto é um " + tipo + ".");
    } 
}
