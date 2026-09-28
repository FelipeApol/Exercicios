"""Operação de saque
O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500,00 por saque.
Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que
não será possível sacar o dinheiro por falta de saldo. Todos os saques devem ser armazenados
em uma variável e exibidos na operação de extrato.

- [ ] realizar 3 saques diários com limite máximo de R$ 500,00 por saque.
- [ ] caso o usuário não tenha saldo em conta, exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo.
- [ ] verificar se o usuário atingiu o limite diário de saques e exibir uma mensagem informando que não será possível realizar mais saques no dia.
- [ ] verificar se o valor do saque é positivo e menor ou igual a R$ 500,00.
- [ ] todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.

"""


def sacar(saldo, valor, saques_realizados):
    """Realiza um saque na conta bancária.

    Args:
        saldo (float): Saldo atual da conta.
        valor (float): Valor a ser sacado.
        saques_realizados (int): Número de saques realizados no dia.

    Returns:
        tuple: Novo saldo da conta após o saque e o número atualizado de saques realizados.
    """
    if saques_realizados >= 3:
        print(
            "Limite diário de saques atingido. Você não pode realizar mais saques hoje."
        )
        return saldo, saques_realizados

    if valor > 500:
        print("Valor inválido. O saque deve ser menor ou igual a R$ 500,00.")
        return saldo, saques_realizados

    if valor > saldo:
        print("Saldo insuficiente para realizar o saque.")
        return saldo, saques_realizados

    saldo -= valor
    saques_realizados += 1
    print(f"Saque de R${valor:.2f} realizado com sucesso!")

    return saldo, saques_realizados


# Teste da função de saque
saldo_atual = 1000.0  # Saldo inicial da conta
saques_realizados = 0  # Contador de saques realizados no dia

while True:
    saque_valor = float(input("Digite o valor a ser sacado (ou 0 para sair): "))
    if saque_valor == 0:
        break
    saldo_atual, saques_realizados = sacar(saldo_atual, saque_valor, saques_realizados)
    print(f"Saldo atual: R${saldo_atual:.2f}")
    print(f"Saques realizados hoje: {saques_realizados}/3")
