'''
        SISTEMA BANCÁRIO
        
Fazer as seguintes operações para um usuário:        

Depósito: Todos os depositos devem ser armazenados em uma variável e exibidos na operação de extrato.
    Depósito maiores que zero
    
Saque: São permitidos apenas 3 saques diários, com limite de 500 reais cada. Caso não tenha saldo em conta deve ser emitida
    uma mensagem informando a falta de dinheiro.
    Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato
    
Extrato: Exibir todas as operações de depósito e saque e o seu tipo.
    No fim da listagem deve ser exibido o saldo atual da conta.
    Os valores devem ser exibidos utilizando o formado R$ 1500.45

'''

menu = """
    Selecione uma opção
    
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0

limite_saque = 500
numero_saques = 0
QNT_SAQUES = 3

extrato = '''
    Extrato Bancário
'''

while True:
    opcao = input(menu)
    opcao = opcao.lower() #Deixa a letra em minuscula para a comparação
    
    if opcao == 'd': 
        valor_deposito = float(input('Digite o valor do depósito: '))
        
        if valor_deposito > 0:
            saldo += valor_deposito
            
            extrato += f'''
            Depósito: R$ {valor_deposito:8.2f} 
            Saldo:    R$ {saldo:8.2f}
            '''
            # Coloca 8 espaços antes do numero e duas casas decimais
            print('\nDepósito realizado.')
        else:
            print('\nValor de depósito inválido.')
            
    elif opcao == 's':
        valor_saque = float(input('Digite o valor do saque: '))
        
        if numero_saques < QNT_SAQUES:
            if valor_saque > 0 and valor_saque <= saldo and valor_saque <= limite_saque:
                saldo -= valor_saque
                numero_saques += 1
                
                extrato += f'''
            Saque:    R$ {valor_saque:8.2f}
            Saldo:    R$ {saldo:8.2f}
                '''
                print('Operação Concluída. Retire seu dinheiro na boca do caixa.')
            elif valor_saque <= 0:
                print('\nValor de saque inválido.')
            elif valor_saque > saldo:
                print('\nSaldo insuficiente.')
            elif valor_saque > limite_saque:
                print(f'\nValor maior que o limite de saque. Você pode sacar até R$ {limite_saque}.')
                
        else:
            print('Limite de saques atingido!')
        
    elif opcao == 'e':
        print(extrato)
    
    elif opcao== 'q':
        break
        
    else:
        print('Opção inválida, por favor selecione novamente a operação desejada.')