
package tiposdedados;

public class CompatibilidadeDeTipos {
    public static void main(String[] args) {
        
        // Convertendo uma idade (int) a cima para uma string.
        int idade = 30;
        String valor = Integer.toString(idade);
        
        // Convertendo uma string para inteiro.
        String valor2 = "30";
        int idade2 = Integer.parseInt(valor2);
        
        // Convertendo uma string para float.
        String valor3 = "30.57";
        float idade3 = Float.parseFloat(valor3);
        
        
    }
}
