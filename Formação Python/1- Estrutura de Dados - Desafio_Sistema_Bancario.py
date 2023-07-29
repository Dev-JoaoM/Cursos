saque_maximo = 500
QNT_SAQUES = 3

tabela_cliente = {}
tabela_conta_cliente = {}
extrato_contas = {}

cabecalho = '''
========================    
    EXTRATO BANCÁRIO
========================
'''


def menu():
    print("""\n\n
=====================
        MENU
=====================
    
[d] Depositar
[s] Sacar
[e] Extrato
[n] Novo Cliente
[c] Nova Conta
[u] Lista Clientes
[l] Lista Contas
[q] Sair
""")


def sacar(*,conta_numero, valor_saque, limite_saque, saques_limite): #chamar a função exibir extrato ou usar o extrato global
    # Se atendar a variável 'numero_saques' para não interferir na contagem de outras contas
    saldo_aux = tabela_conta_cliente[conta_numero]['saldo'] # Variável auxiliar apenas para diminuir a escrita nas verificações
    numero_saques = tabela_conta_cliente[conta_numero]['total_saques']
    valor_saque = float(valor_saque) if valor_saque.isnumeric() else 0
    
    if numero_saques < saques_limite:
        if valor_saque > 0 and valor_saque <= saldo_aux and valor_saque <= limite_saque:

            tabela_conta_cliente[conta_numero]['saldo'] -= valor_saque    
            tabela_conta_cliente[conta_numero]['total_saques'] += 1
            numero_saques += 1
            
            print('Operação Concluída. Retire seu dinheiro na boca do caixa.')
            return f'''
    Saque:    R$ {valor_saque:8.2f} 
    Saldo:    R$ {tabela_conta_cliente[conta_numero]['saldo']:8.2f}
        '''            
        elif valor_saque <= 0:
            print('\nValor de saque inválido.')

        elif valor_saque > saldo_aux:
            print('\nSaldo insuficiente.')

        elif valor_saque > limite_saque:
            print(f'\nValor maior que o limite de saque. Você pode sacar até R$ {limite_saque}.')

    else:
        print('Limite de saques atingido!')
    return ''
                
                
def depositar (conta_numero, valor_deposito,/):
    valor_deposito = float(valor_deposito) if valor_deposito.isnumeric() else 0
        
    if valor_deposito > 0:
        tabela_conta_cliente[conta_numero]['saldo'] += valor_deposito    
        print('\nDepósito realizado.')

        return f'''
    Depósito: R$ {valor_deposito:8.2f} 
    Saldo:    R$ {tabela_conta_cliente[conta_numero]['saldo']:8.2f}
        '''
        # Coloca 8 espaços antes do numero e duas casas decimais  
    else:
        print('\nValor de depósito inválido.')
        return ''    

def exibir_extrato(conta_numero,/,*, inicio):
    if extrato_contas[conta_numero] == '':
        print(f'{inicio}\nExtrato vazio.')
    else:
        print(f'{inicio}{extrato_contas[conta_numero]}\n\n SALDO ATUAL: {tabela_conta_cliente[conta_numero]["saldo"]}', '\n',"="*24)

def valida_cpf(op, cpf):         

    if len(cpf) != 11 or cpf.isnumeric() == False: # Verifica o tamanho da string 'cpf' e se todos os digitos são numeros
        print(f'O CPF "{cpf}" é inválido.')
        return False
    
    if op == 'n': # Se a for abertura de uma conta nova, verifica se já não tem um cpf cadastrado
        if cpf in tabela_cliente: # Verifica se já tem um cpf cadastrado 
            print(f'Já existe um(a) cliente vinculado(a) ao CPF: "{cpf}".')
            return False
        else:
            return True # Retorna True se o cpf é válido e não tem uma conta com esse cpf
    elif op =='c':
        if tabela_cliente == {} or cpf not in tabela_cliente:
            print(f'\nNão há usuários cadastrados com esse cpf "{cpf}".')
            print('Para cadastra-lo(a) escolha a opção "Novo Cliente"')
            return False     
    else:
        return True # Validação retorna 'True' se o cpf está de acordo e não tem outra conta já registrada


def cadastrar_Cliente(chave_cpf, dados):  
    tabela_cliente[chave_cpf] = dados 
    cadastrar_Conta_Corrente(chave_cpf)
    # Vincula o cliente com uma conta nova no ato
    print('\nCliente e Conta cadastrados com sucesso!')
    

def cadastrar_Conta_Corrente(num_cpf):
    AGENCIA = '0001' # numero da agencia é imutavel
    nome = tabela_cliente[cpf]["nome"] # Pega o nome do cliente que corresponde ao cpf
    numero_conta = 1  if tabela_conta_cliente == {} else (len(tabela_conta_cliente)+1)
    numero_conta = str(numero_conta)
    valor_conta = 0
    qnt_saque = 0
    extrato_contas[numero_conta] = '' # Inicio o extrato de cada conta, assim posso acessar esse valor vazio para inclementar as movimentação da conta
    # se a tabela de conta é vazia o numero_conta recebe 1 para ser a primeira conta
    # se não numero_conta recebe o tamanho da tabela de conta +1, assim o numero_conta terá o valor da proxima conta
    tabela_conta_cliente.update({numero_conta:dict(agencia=AGENCIA, CPF = num_cpf, usuario=nome, saldo = valor_conta, total_saques = qnt_saque)})

def listar_contas():
    if tabela_conta_cliente:
        print('''
===================================
    Lista de Contas Cadastradas
              ''')
        print("\n".join([f"Número da conta {chave}: {valor}" for chave, valor in tabela_conta_cliente.items()]))
    else:
        print('\n Não há contas cadastradas')

def listar_clientes():
    if tabela_cliente:
        print('''
=====================================
    Lista de Clientes Cadastradas
              ''')
        print("\n".join([f"Número do CPF {chave}: {valor}" for chave, valor in tabela_cliente.items()]))
    else:
        print('\n Não há clientes cadastradas')
        

def valida_conta(conta_numero):
    if conta_numero not in tabela_conta_cliente:
        print('\nEssa conta não exite!')
        return False
    else: 
        return True
    
####################################################################################################################################################
#                           INÍCIO DA EXECUÇÃO

while True:
    menu()
    opcao = input('Escolha uma opção: ')
    opcao = opcao.lower() #Deixa a letra em minuscula para as comparações

    if opcao == 'd': # Faz um depósito
        num_conta = input('Digite o número da conta: ')
        result = valida_conta(num_conta)
        #Verifica se a conta existe
        if result == False:
            True
        else:       
            valor = input('Digite o valor do depósito: ')
            extrato_contas[num_conta] += depositar(num_conta, valor)
            
    elif opcao == 's': # Faz um saque
        num_conta = input('Digite o número da conta: ')
        result = valida_conta(num_conta)
        #Verifica se a conta existe
        if result == False:
            True
        else:       
            valor = input('Digite o valor do saque: ')
            extrato_contas[num_conta] += sacar(
                conta_numero=num_conta, 
                valor_saque=valor, 
                limite_saque=saque_maximo, 
                saques_limite=QNT_SAQUES)
    
    elif opcao == 'e': # exibe o extrato
        num_conta = input('Digite o número da conta: ')
        result = valida_conta(num_conta)
        #Verifica se a conta existe
        if result == False:
            True
        else:
            exibir_extrato(num_conta, inicio=cabecalho)
        
    elif opcao == 'n': # Cadastro de novo cliente
        
        # ENTRADA E VALIDAÇÃO DE CPF
        cpf = input('Digite o CPF (apenas números): ')
        resultado = valida_cpf (opcao, cpf) 
        if resultado == False:
            True
        else:    
            # ENTRADA DAS INFORMAÇÕES
            nome = input('Digite o nome completo: ')
            nasc = input('Digite a data de nascimento (dd/mm/aaaa): ')
            rua = input('Digite a rua: ')
            num = input('Digite o número da casa: ')
            bairro = input('Digite o bairro: ')
            cidade = input('Digite a cidade: ')
            uf = input('Digite a sigla do Estado (UF): ')
            # ATRIBUIÇÃO DOS DADOS AO DICIONÁRIO
            endereco = {"lagradouro": rua, 'nro': num, 'bairro': bairro, "cidade":cidade, 'Estado': uf}
            informacoes = dict(nome = nome, nascimento = nasc, endereco = endereco)
            
            # CADASTRO DE CLIENTE E ABERTURA DA 1° CONTA
            cadastrar_Cliente(cpf, informacoes)           
        
    elif opcao =='c': #Conta nova para um usuário que já existe

        # ENTRADA E VALIDAÇÃO DE CPF
        cpf = input('Digite o CPF (apenas números): ')
        resultado = valida_cpf (opcao, cpf) 
        if resultado == False:
            True
        else:       
            print(f'\nDados do Cliente: {tabela_cliente[cpf]}')
            cadastrar_Conta_Corrente(cpf)
            print(f'A nova conta para o cliente "{tabela_cliente[cpf]["nome"]}" cadastrada com sucesso!')
        
    elif opcao == 'u': #lista clientes
        listar_clientes()
    elif opcao == 'l': #lista contas
        listar_contas()
    elif opcao == 'q':
        break    
    else:
        print('\nOpção inválida, por favor selecione novamente a operação desejada.')