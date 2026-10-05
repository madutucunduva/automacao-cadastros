# AUTOMAÇÃO DE LOGIN E LEITURA DE BASE DE DADOS
# PASSO 1: Abrir o navegador
# PASSO 2: Fazer login
# PASSO 3: Importar a base de produtos pra cadastrar
# PASSO 4: Cadastrar um produto
# PASSO 5: Repetir o passo 4 para todos os produtos da base

import pyautogui
import time
import pandas as pd
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.PAUSE = 1

# Abrir o navegador
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(2)
#pyautogui.click(x=420, y=402)
#pyautogui.click(x=420, y=402)
#time.sleep(3)


# Fazer login
pyautogui.click(x=520, y=63)
pyautogui.write(link)
pyautogui.press("enter")
pyautogui.click(x=765, y=490)
time.sleep(1.5)
pyautogui.write("madu@gmail.com")
pyautogui.press("tab")
pyautogui.write("123456")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(1.5)

# Abrir a base de dados
from pathlib import Path
tabela = pd.read_csv(Path(__file__).parent / "produtos.csv")
print(tabela)


# Cadastrar intens da tabela
for linha in tabela.index:
    # codigo
    pyautogui.click(x=761, y=350)
    time.sleep(1.5)
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    # marca
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")
    # tipo
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")
    # categoria
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")
    # preco
    preco = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco))
    pyautogui.press("tab")
    # custo
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")
    # obs
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(obs))
    pyautogui.press("tab")
    # ok
    pyautogui.press("enter")
    time.sleep(2)

    pyautogui.scroll(5000)