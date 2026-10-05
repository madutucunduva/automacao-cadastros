# 🤖 Automação de Cadastro de Produtos

Robô em Python que faz login em um sistema web e cadastra automaticamente todos os produtos de uma planilha, sem nenhuma digitação manual.

Projeto desenvolvido durante o **Intensivão de Python** da [Hashtag Treinamentos](https://www.hashtagtreinamentos.com/).

## 💡 O problema

Cadastrar centenas de produtos um a um em um sistema é uma tarefa lenta, repetitiva e sujeita a erros de digitação. Este robô assume esse trabalho: ele lê a base de produtos e preenche o formulário do sistema sozinho, linha por linha.

## ⚙️ Como funciona

1. Abre o navegador e acessa o sistema
2. Faz login com usuário e senha
3. Importa a base de produtos (`produtos.csv`) com o Pandas
4. Preenche o formulário de cadastro com os dados de cada produto
5. Repete o processo até cadastrar todos os itens da base

## 📁 Arquivos do projeto

- `automacao_cadastro.py`: script principal da automação
- `auxiliar.py`: script de apoio para descobrir as coordenadas da tela
- `produtos.csv`: base de produtos a serem cadastrados
- `requirements.txt`: bibliotecas necessárias

## 🛠️ Tecnologias

- **Python**
- **PyAutoGUI**: controle do mouse e do teclado
- **Pandas**: leitura e manipulação da base de dados

## ▶️ Como executar

1. Instale as dependências:

```
pip install -r requirements.txt
```

2. Execute o script:

```
python automacao_cadastro.py
```

## 🎯 Ajustando as posições da tela

O PyAutoGUI clica em posições fixas da tela, e as coordenadas do código foram ajustadas para a minha resolução. Para adaptar à sua tela, use o script `auxiliar.py`:

1. Execute o script:

```
python auxiliar.py
```

2. Nos 5 segundos seguintes, posicione o mouse sobre o ponto onde o robô deve clicar.
3. O terminal vai mostrar as coordenadas `x` e `y` dessa posição.
4. Substitua os valores correspondentes no `automacao_cadastro.py`.

O sistema utilizado é um ambiente de testes disponibilizado pela Hashtag Treinamentos para fins didáticos, e os dados de login no código são fictícios.

## 👩‍💻 Autora

**Maria Eduarda Tucunduva**

[LinkedIn](https://www.linkedin.com/in/maria-eduarda-tucunduva) · [GitHub](https://github.com/madutucunduva)