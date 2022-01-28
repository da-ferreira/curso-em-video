
package idiomasistema;

import java.util.Locale;

public class IdiomaDoSistema {
    public static void main(String[] args) {
        Locale idioma = Locale.getDefault();
        
        System.out.printf("Seu sistema está em %s.\n", idioma.getDisplayLanguage());
    }
}
