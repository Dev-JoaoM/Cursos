/*Elaborar um programa que declare uma matriz bidimensional que represente
 uma estante com 4 prateleiras e 3 compartimentos cada prateleira.
  Fa�a um programa que leia a quantidade de pe�as em cada compartimento de prateleira.
 Exiba os valores das pe�as por prateleira*/
 
 
 public class A62_EstanteBidimensional{
 
   public static void main (String args[]){
   int estante[][] = {{4,7,9},{7,2,6},{45,10,15},{12,32,7}};
   int prateleira = 0;
   
  for(int i=0; i<4; i++){
   for(int j=0; j<3; j++){
      System.out.print(estante[i][j] + "\t");
      prateleira += estante[i][j];
      }
   System.out.print("\nO valor das pecas da "+ (i+1) + " prateleira e " + prateleira + ".\n\n");    
   prateleira = 0;
      } 
   
   }
 }