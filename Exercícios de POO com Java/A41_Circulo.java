//Declaração da classe Circulo.java

public class A41_Circulo
{
   //atributo privado
    private double raio;
   
   //método construtor
   public A41_Circulo(double r)
   {
      setRaio(r);
   }
    
    //método informar raio 
    public double getRaio(){
        return raio;
    }
    
    //métodos alterar raio
    
   public void setRaio(double r)
   {
      if(r < 0)
         System.out.println ("O raio nao pode ser negativo.");
      else
         raio = r;
   }

   //metodo do diametro
   public double Diametro(double r)
   {
         double diametro = (r*2);
         return diametro;
   }
   
   //metodo da area
   public double Area(double r)
   {
         double area = Math.PI * Math.pow(r,2);
         return area;
   }
   
   
   //metodo da circuferencia
   public double Circuferencia(double r)
   {
         double circuferencia = Math.PI * 2 * r;
         return circuferencia;
   }
    //método exibir dados
    public void exibeDados()
    {
        System.out.println("\n\nDados do circulo de raio " + getRaio());
        System.out.printf("Diametro     : %.2f %n", Diametro(getRaio()));
        System.out.printf("Circuferencia: %.2f %n", Circuferencia(getRaio()));        
        System.out.printf("Area         : %.2f %n", Area(getRaio()));
                            
    }
    

    
}//fim da classe