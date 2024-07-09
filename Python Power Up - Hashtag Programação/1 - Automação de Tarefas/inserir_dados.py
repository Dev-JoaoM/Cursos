"""    
    Comandos do pyautogui usados

pyautogui.write -> escrever um texto
pyautogui.press -> apertar 1 tecla
pyautogui.click -> clicar em algum lugar da tela
pyautogui.hotkey -> combinação de teclas

"""

# Passo a passo do projeto
# Passo 1: Entrar no sistema da empresa 
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login

import pyautogui, time, pandas as pd

pyautogui.PAUSE = 0.3 # Pausa a cada comando do pyautogui

# abrir o navegador (chrome)
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(2) # tempo de espera para o computador
pyautogui.click(x=552, y=509) # seleciona um perfil
pyautogui.hotkey("ctrl", "t") # abre uma nova guia


# acessar o sistema
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(2)


# Passo 2: Fazer login
# selecionar o campo de email
pyautogui.click(x=3066, y=746)

# escrever o seu email
pyautogui.write("teste@gmail.com")
pyautogui.press("tab") # passando pro próximo campo
pyautogui.write("sua senha")
pyautogui.click(x=2860, y=930) # clique no botao de login
time.sleep(2)

# Passo 3: Importar a base de produtos pra cadastrar

tabela = pd.read_csv("produtos.csv")
print(tabela)

# Passo 4: Cadastrar os produtos
for linha in tabela.index:
    # clicar no campo de código
    pyautogui.click(x=2692, y=582)
    
    for coluna in tabela.columns:
        # pegar da tabela o valor da linha e da coluna que a gente quer preencher
        valor = tabela.loc[linha, coluna] 

        if not pd.isna(valor): # preenche se alugum valor não estiver vazio
            pyautogui.write(str(valor)) # preencher o campo

        pyautogui.press("tab") # próximo campo
                
    # cadastra o produto (botao enviar)
    pyautogui.press("enter") 

    # dar scroll de tudo pra cima
    pyautogui.scroll(5000)