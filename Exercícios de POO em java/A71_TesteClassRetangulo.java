import java.util.Scanner;

public class A71_TesteClassRetangulo{

   public static void main(String args [])
   {
      A71_ClassRetangulo forma1 = new A71_ClassRetangulo(25, 10);
      forma1.verDados();
      
      System.out.println();
      
      A71_ClassRetangulo forma2;
      forma2 = new A71_ClassRetangulo(50,50);
      forma2.verDados();
      
      System.out.println();
      
      A71_ClassRetangulo forma3;
      forma3 = new A71_ClassRetangulo();
      forma3.verDados();
      

      }
}
