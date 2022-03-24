
package resolucaotela;

import java.awt.Dimension;
import java.awt.Toolkit;

public class ResolucaoDaTela {
    public static void main(String[] args) {
        Toolkit tk = Toolkit.getDefaultToolkit();
        Dimension resolucao = tk.getScreenSize();
        
        System.out.printf("Sua tela tem resolução %d x %d.\n", resolucao.width, resolucao.height);
    }
}
