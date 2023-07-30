/*
Elaborar um programa que declare um vetor de 20 elementos reais.
O programa deve requisitar ao usuário um valor real a ser pesquisado no conjunto. 
Caso seja encontrado, deve-se exibir a mensagem de que o mesmo foi encontrado e em qual posição.
 Em caso de não existência, exiba mensagem apropriada.

*/

import java.util.Scanner;

public class A61_BuscaVetor{

   public static void main (String args[]){
      Scanner leia = new Scanner (System.in);
      double consulta;
      int i = 0,  aux = 0, posicao = 0;
      double Vetor20[] = {15.5,10,21.9,30.98,42,65,75.6,97,14.7,86,21,59,32,45,165,4.9,98,147,546.45,21.59};
      
      System.out.print("Digite o valor que deseja pesquisar: ");
      consulta = leia.nextDouble();
      

         
         while (i < Vetor20.length){
            if (Vetor20[i] == consulta){
               aux = 1;
               posicao = i+1;
            }
            i += 1;
        }
    
      if (aux == 1)
         System.out.println("\nO valor " + consulta + " foi encontrado na posicao " + posicao);
      else
         System.out.printf("\nO valor " + consulta + " nao foi encontrado na pesquisa");
      
 }
}  