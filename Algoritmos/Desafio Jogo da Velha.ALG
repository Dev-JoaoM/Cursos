Algoritmo "pgm15_Jogo da Velha"
// Disciplina   : [Curso em Video - Algoritmo]
// Professor   :  Gustavo Guanabara
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 21/07/2023


// 1 - Quais são os dados de entrada necessários?
//   Opções de jogada em uma matriz 3x3


// 2 - O que devo fazer com estes dados?
//   Ler a jogada
//   Verificar se a coordenada está vazia
//   Inserir a jogada na coordenada informada
//

// 3 - Quais são as restrições deste problema?
//  Ganha quem marcar 3 posições seguidas, na vertical, horizontal ou diagonal
//  Não pode jogar em cima de outra jogada
//  Uma jogada por jogador
//


// 4 - Qual é o resultado esperado?
//   Mostrar o tabuleiro atualizado depois de cada jogada
//   Mostrar quem venceu ou caso de empate "deu velha"
//   Finalizar o jogo depois de todas as jogadas
//


// 5 - Qual é a sequência de passos a ser feitas
//    para chegar ao resultado esperado?

//    1- Mostrar o  tabuleiro com cada posição em numero inteiro
//    2- Perguntar ao 1° jogador onde ele irá jogar
//    3- Ler a entrada e verificar se a posição está vazia
//    4- Se sim marcar a jogada na posição informada
//       Senão informar que a posição já está ocupada
//       Passo 2
//    5- Atualizar o tabuleiro
//    6- Perguntar ao 2° jogador onde ele irá jogar
//    7- Passo 3 e 4

Var
// Seção de Declarações das variáveis
mTabuleiro: vetor [1..3, 1..3] de caractere
i, j, num1, jogada, cont: inteiro
continuar: caractere
finish, jIva: logico
//############################################################################
Procedimento TABULEIRO()
var i, j: inteiro
inicio
      LimpaTela
      Para i <- 1 ate 3 faca
           //Escreval ("|----|----|----|")
           Escreval ("|---|---|---|")
           Para j <- 1 ate 3 faca

              Escreva ("| ", mTabuleiro[i,j]:2)
              //Escreva ("|",i,"-",j:1)
           FimPara
           Escreva("|")
           Escreval()
      FimPara
    Escreval ("|---|---|---|")
    //Escreval ("|----|----|----|")
FimProcedimento

//############################################################################
Procedimento Posicao (jog, car:inteiro)
var cont:inteiro
inicio
cont <- 0
   Para i <- 1 ate 3 faca
        Para j <- 1 ate 3 faca
             cont <- cont + 1  // conta até a posicao da jogada
             Se cont = jog entao  // Quando se iguala é porque chegou na posição
                Se (mTabuleiro[i,j] = "X") ou (mTabuleiro[i,j] = "O") entao
                   EscrevaL("JOGADA INVÁLIDA!")
                   EscrevaL()
                   jIva <- verdadeiro
                Senao
                     mTabuleiro[i,j] <- carac(car)
                     jIva <- falso
                Fimse
             FimSe
        FimPara
   FimPara
FimProcedimento

//############################################################################
Funcao completo ():logico
var
i, j: inteiro
vazio: inteiro
inicio
 Para i <- 1 ate 3 faca
      Para j <- 1 ate 3 faca
         Se (mTabuleiro[i,j] <> "X") E (mTabuleiro[i,j] <> "O") entao
            vazio <- vazio + 1
         FimSe
      FimPara
 FimPara

Se vazio >= 1 entao
   retorne falso
Senao
   retorne verdadeiro
   EscrevaL()
   EscrevaL ("DEU VELHA!!!")
fimse

FimFuncao
//############################################################################

Procedimento Vencedor()
var i,j: inteiro
inicio
   Para i <- 1 ate 3 faca // Verifica se tem ganhador na horizontal
        Se (mTabuleiro[i,1] = mTabuleiro[i,2]) e (mTabuleiro[i,2] = mTabuleiro[i,3]) entao
           finish <- verdadeiro
           EscrevaL ("JOGO FINALIZADO!!! O Vencedor é '", mTabuleiro[i, 1], "'")
        FimSe
   FimPara

   Se finish = falso entao
      Para j <- 1 ate 3 faca // Verifica se tem ganhador na vertical
        Se (mTabuleiro[1,j] = mTabuleiro[2,j]) e (mTabuleiro[2,j] = mTabuleiro[3,j]) entao
           finish <- verdadeiro
           EscrevaL ("JOGO FINALIZADO!!! O Vencedor é '", mTabuleiro[1, j], "'")
        FimSe
      FimPara
   FimSe
   
   Se finish = falso entao
       // Verifica se tem ganhador na diagonal principal
     Se (mTabuleiro[1, 1] = mTabuleiro[2, 2]) e (mTabuleiro[2, 2] = mTabuleiro[3, 3]) entao
        finish <- verdadeiro
        EscrevaL()
        EscrevaL ("JOGO FINALIZADO!!! O Vencedor é '", mTabuleiro[1, 1], "'")
     Senao        // Verifica se tem ganhador na diagonal segundaria
        Se (mTabuleiro[3, 1] = mTabuleiro[2, 2]) e (mTabuleiro[2, 2] = mTabuleiro[1, 3]) entao
           finish <- verdadeiro
           EscrevaL()
           EscrevaL ("JOGO FINALIZADO!!! O Vencedor é '", mTabuleiro[2, 2], "'")
        FimSe
     FimSe
   FimSe
FimProcedimento

Procedimento TabuleiroVazio()
var
num1,i,j: inteiro

inicio
num1 <- 49
//Escreva(carac(49))  49 = 1
 Para i <- 1 ate 3 faca
      Para j <- 1 ate 3 faca
           mTabuleiro[i,j] <- carac(num1)
           num1 <- num1 + 1
      FimPara
 FimPara
finish <- falso
FimProcedimento
//############################################################################
Inicio
// Seção de Comandos, procedimento, funções, operadores, etc...
Repita
TabuleiroVazio()

   Enquanto finish <> verdadeiro faca
   TABULEIRO()
   Vencedor()
   // X = 88, O = 79

      Se finish = falso entao
         Repita // Loop para se a jogada for inválida
            EscrevaL("Vai jogar [X] em qual posição?")
            Leia(jogada)
            Posicao(jogada, 88)
         Ate jIva = falso
      FimSe

      TABULEIRO()
      finish <- completo()
      Vencedor()

      Se finish = falso entao
         Repita
            EscrevaL("Vai jogar [O] em qual posição?")
            Leia(jogada)
            Posicao(jogada, 79)
         Ate jIva = falso
      FimSe

   FimEnquanto

   Escreval()
   EscrevaL("Deseja continuar? ")
   Leia(continuar)
   continuar <- minusc(continuar)

Ate continuar = "n"

Fimalgoritmo