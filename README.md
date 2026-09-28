# Exercícios de Python

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Em%20desenvolvimento-orange)
![Exercícios](https://img.shields.io/badge/Exerc%C3%ADcios-Strings-5B8DEF)

Este repositório reúne uma série de exercícios práticos de programação em Python, com foco em lógica, manipulação de strings e criação de pequenos sistemas de negócio. O objetivo é desenvolver a prática de resolução de problemas, reforçar conceitos básicos da linguagem e criar uma base sólida para estudos futuros.

## Objetivo do projeto

- Praticar lógica de programação com Python;
- Explorar operações com strings e textos;
- Resolver problemas simples e objetivos de forma estruturada;
- Desenvolver pequenos sistemas com regras de negócio;
- Aprimorar a capacidade de escrever scripts úteis e funcionais;
- Consolidar conceitos fundamentais da linguagem.

## Estrutura do repositório

```text
Exercicios/
├── README.md
├── Biliblioteca/
│   ├── biblioteca.py
│   └── README.md
├── desafio-bancario/
│   ├── deposito.py
│   ├── saque.py
│   └── README.md
└── Strings/
    ├── ContagemDeCaractes.py
    ├── ContagemDePalavras.py
    ├── InverterFrase.py
    └── palindromo.py
```

## Lista de exercícios

| Arquivo | Descrição | Conceito praticado |
|---------|-----------|--------------------|
| `Strings/ContagemDeCaractes.py` | Conta quantos caracteres existem em uma frase ou texto. | Manipulação de strings |
| `Strings/ContagemDePalavras.py` | Conta o número de palavras em uma frase. | Divisão e análise de texto |
| `Strings/InverterFrase.py` | Inverte a ordem das letras de uma frase. | Laços e concatenação |
| `Strings/palindromo.py` | Verifica se uma palavra ou frase é um palíndromo. | Comparação de strings |
| `Biliblioteca/README.md` | Descreve o exercício de cadastro e listagem de livros. | Funções com parâmetros e varargs |
| `Biliblioteca/biblioteca.py` | Implementa o sistema de biblioteca com cadastro e listagem de livros. | Estruturas de funções e entrada de dados |
| `desafio-bancario/README.md` | Descreve o sistema bancário com depósito, saque e extrato. | Lógica de programação e controle de fluxo |
| `desafio-bancario/deposito.py` | Implementa a operação de depósito em conta. | Funções e validações |
| `desafio-bancario/saque.py` | Implementa a operação de saque com limites diários. | Regras de negócio e condicionais |

## Exercício de biblioteca

Além dos exercícios de strings, o repositório conta com um desafio de biblioteca para praticar funções com parâmetros opcionais e lista de argumentos variáveis.

### Requisitos do exercício

- Criar uma função chamada `cadastrar_livro` que receba `titulo`, `autor` e `disponivel` (com valor padrão `True`);
- A função deve retornar uma string formatada com os dados do livro;
- Criar uma função chamada `listar_livros` que receba um número variável de títulos de livros e imprima cada um em uma linha.

## Desafio bancário

O repositório também inclui o desafio de sistema bancário, que tem como objetivo desenvolver uma versão inicial de um programa para gerenciar operações bancárias em Python.

### Requisitos do desafio

- Criar um sistema bancário com as operações de sacar, depositar e visualizar extrato;
- Permitir depósitos de valores positivos;
- Validar saques diários com limite máximo de R$ 500,00 por operação;
- Impedir saques quando não houver saldo suficiente;
- Registrar todas as movimentações e exibir o saldo atual no extrato;
- Exibir mensagens adequadas quando não houver movimentações.

### Operação de depósito

Deve ser possível depositar valores positivos para a conta bancária. A primeira versão do projeto trabalha com apenas 1 usuário, então não é necessário identificar agência ou número da conta.

### Operação de saque

O sistema deve permitir realizar 3 saques diários, com limite máximo de R$ 500,00 por saque. Caso o usuário não tenha saldo em conta, o sistema deve informar que não será possível sacar o dinheiro por falta de saldo.

### Operação de extrato

A operação de extrato deve listar todos os depósitos e saques realizados. No final deve ser exibido o saldo atual da conta. Se não houver movimentações, a mensagem exibida deve ser: "Não foram realizadas movimentações".

Os valores devem seguir o formato monetário em reais, como por exemplo:

```text
1500.45 = R$ 1500.45
```

## Requisitos

Para executar os scripts, você precisa ter o Python 3 instalado no seu computador.

### Verificar a instalação

```bash
python --version
```

Se o comando retornar a versão do Python, a instalação foi concluída com sucesso.

## Como executar os exercícios

Navegue até a pasta do projeto e execute qualquer script com o comando abaixo:

```bash
python "Strings/ContagemDeCaractes.py"
```

Exemplo com outro exercício:

```bash
python "Strings/InverterFrase.py"
```

Você também pode executar diretamente pelo terminal dentro da pasta do projeto:

```bash
cd Exercicios
python "Strings/palindromo.py"
```

## Exemplos de uso

### 1. Contagem de caracteres
Entrada:

```python
texto = "Python"
```

Saída esperada:

```text
Número de caracteres: 6
```

### 2. Inverter frase
Entrada:

```python
frase = "Python é divertido"
```

Saída esperada:

```text
odivnited é nohtyP
```

## Tecnologias utilizadas

- Python 3
- Lógica de programação
- Estruturas básicas de strings

## Contribuição

Este repositório é um espaço de prática pessoal e de estudo. Você pode explorar os scripts, testar novas soluções e até melhorar os códigos existentes.

## Autor

Projeto desenvolvido para prática de Python e exercícios de programação.
