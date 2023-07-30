//TesteCiculo.java
//utiliza classe circulo
import java.util.Scanner;


public class A41_TesteCirculo
{
   public static void main (String args [])
   {
   Scanner scanner = new Scanner(System.in);
   System.out.printf("Informe o raio do circulo: ");
   double raioIN = scanner.nextDouble();
   
      A41_Circulo c = new A41_Circulo(raioIN);
      c.exibeDados();
      

}
}

