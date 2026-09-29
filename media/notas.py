"""Crie um app que mostre no console a média de 3 notas.
Usando o Exemplo de listar de notas crie uma app com janelas em Python para receber 3 notas e mostrar a média

Algoritmo:
1. [x] Receber 3 notas do usuário
2. [x] Calcular a média das notas
3. [x] Mostrar a média no console
4. [ ] Criar funções
5. [ ] Criar janelas

"""

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
media = (nota1 + nota2 + nota3) / 3
print(f"A média das notas é: {media}")