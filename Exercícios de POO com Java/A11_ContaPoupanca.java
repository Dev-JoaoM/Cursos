public class A11_ContaPoupanca extends A10_Conta{
   private double taxaJuros;
   
   //Construtor da classe filha pegando os atributos da classe mae
   public A11_ContaPoupanca (int c, String t, double s, double tx) {
      super(c, t, s); //atributos da classe mae sendo instanciados na classe filha
      setTaxaJuros(tx);
   }
   
   private void setTaxaJuros(double tx){
      if (tx < 0.0)
         System.out.println("A taxa informada e invalida. Ela deve ser maior do que 0.\n");
      else
         taxaJuros = (tx/100);
   }
   
   public double getTaxaJuros(){
      return taxaJuros;
   }
 
   double juros;
   //metodo de calculo
   public void atualizaSaldo(double tx){
         setTaxaJuros(tx);//joga a taxa de entrada para o set da taxa, la tem a validação e alteração para valor decimal
         juros = getTaxaJuros() * super.getSaldo();//pega o saldo classe mae e multiplica pela taxa de juros em decimal         
         super.setSaldo(super.getSaldo() + juros);//saldo da classe mae + os juros estão sendo passados como parametro para o metodo setSaldo da classe mae para atualizar o saldo da conta
   }
 
 
   public void imprime2(){
      System.out.println("\nDados da Conta Poupanca");
      System.out.println("Acrescimo de Juros de: " + juros);
      super.imprime();//imprime o metoda da classe mae, com: nConta, Titular e Saldo

    }
      

}