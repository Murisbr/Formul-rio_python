# Formulário com Python e CSV

Esse é um projeto simples que desenvolvi usando Python com Tkinter, que é a biblioteca padrão para interfaces gráficas. A ideia foi criar um formulário que salva os dados em um arquivo CSV.

## Funcionalidade

O programa permite que o usuário preencha os seguintes campos:

- Nome
- E-mail
- Idade
- Sexo

Depois de preencher, ao clicar em "Enviar", os dados são salvos em um arquivo `.csv` dentro de uma pasta específica no computador. Se o arquivo não existir, ele é criado com o cabeçalho. Se já existir, os dados são apenas adicionados.

## O que foi usado

- Python 3
- Tkinter para a interface gráfica
- CSV (biblioteca nativa do Python)
- os (para criação/verificação de pasta)

## Como usar

1. Execute o script Python.
2. Preencha todos os campos do formulário.
3. Clique em "Enviar".
4. Os dados serão salvos automaticamente no arquivo CSV.

> Obs: O caminho da pasta onde o CSV é salvo está fixo no código, mas pode ser alterado conforme sua necessidade.

## Exemplo de dados salvos

