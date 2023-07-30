class A42_ContaCorrente
{
               //Declara��o dos Atributos (vari�veis de inst�ncia)
   private int nConta = 0;
   private String titular;
   private double saldo = 0;


//************************************************************************   
                     //M�todo (fun��o) Contrutor
   public A42_ContaCorrente() {
   }
   public A42_ContaCorrente (int c, String t, double s){
      setNconta(c);
      setTitular(t);
      setSaldo(s);
      }
//************************************************************************
                     //M�todos Padr�es

   //M�todo que valida o numero da conta
   private void setNconta(int c){
   if (c > 0)
      nConta = c;
   else
      System.out.println("O numero da conta precisa ser um numero maior do que zero.");
      }     
   //M�todo que retorna o numero da conta
   public int getNconta(){
      return nConta;
      } 


   //M�todo que valida o valor do saldo   
   private void setSaldo(double s){
   if (s >= 0)
      saldo = s;
   else
      System.out.println("O valor do saldo nao pode ser negativo.");
      }     
   //M�todo que retorna o saldo da conta
   public double getSaldo(){
      return saldo;
      }  


  //M�todo que atualiza o nome do titular da conta de acordo com o parametro de
  //entrada 't'
   public void setTitular(String t){
      titular = t;
      }

   //M�todo que retorna o nome do titular da conta
   public String getTitular(){
      return titular;
      }
//************************************************************************
                     //M�todos de C�lculos

   public void saque(double sq){

      if ((saldo - sq) >= 0)
         saldo -= sq;
      else
         System.out.println("\nSaldo Insuficiente!");
      }
      
   public void deposito(double dp){
      if (dp > 0)
         saldo += dp;
      else
         System.out.println("\nValor de deposito invalido!");
   }
  
  
  
  //M�todo para exibir os dados
  public void verDados(){
   System.out.println("==================================");
   System.out.println("Dados da Conta.");
   System.out.printf("Conta  : %07d", getNconta());
   System.out.println("\nTitular: " + getTitular());        
   System.out.printf("Saldo  : R$ %.2f", getSaldo());
   System.out.println("\n==================================");
   
  }
  
  }
  
