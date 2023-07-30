import java.util.Scanner;
public class A42_TesteContaCorrente{
   public static void main(String args [])
   {
      A42_ContaCorrente cc1 = new A42_ContaCorrente(12345, "Joao da Silva", 0);
      cc1.verDados();
      
      A42_ContaCorrente cc2;
      cc2 = new A42_ContaCorrente(54321, "Maria dos Santos", 500);
      cc2.verDados();
      
      Scanner entrada = new Scanner(System.in);
      
      System.out.printf("\nValor para deposito em c1: ");
      double vlr = entrada.nextDouble();
      cc1.deposito(vlr);
      cc1.verDados();
      
      System.out.printf("\nValor de saque em c2: ");
      cc2.saque(entrada.nextDouble());
      cc2.verDados();
      }
}
