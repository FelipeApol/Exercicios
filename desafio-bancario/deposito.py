"""Operação de depósito
Deve ser possível depositar valores positivos para a minha conta bancária. 
A v1 do projeto trabalha apenas com 1 usuário, dessa forma não precisamos 
nos preocupar em identificar qual é o número da agência e conta bancária. 
Todos os depósitos devem ser armazenados em uma variável e exibidos na operação 
de extrato.
"""

def depositar(saldo, valor):
    """Deposita um valor na conta bancária.

    Args:
        saldo (float): Saldo atual da conta.
        valor (float): Valor a ser depositado.

    Returns:
        float: Novo saldo da conta após o depósito.
    """
    if valor > 0:
        saldo += valor
        print(f"Depósito de R${valor:.2f} realizado com sucesso!")
    else:
        print("Valor inválido. O depósito deve ser maior que zero.")
    
    return saldo

# Teste da função de depósito
saldo_atual = 0.0  # Saldo inicial da conta
deposito_valor = float(input("Digite o valor a ser depositado: "))
saldo_atual = depositar(saldo_atual, deposito_valor)  # Realiza o depósito do valor informado pelo usuário
print(f"Saldo atual: R${saldo_atual:.2f}")
