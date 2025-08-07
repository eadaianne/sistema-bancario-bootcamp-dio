saldo = 0.00
extrato = []
LIMITE_SAQUE = 500.00
LIMITE_SAQUES_DIARIOS = 3
saques_realizados = 0

def saque(*, saldo, saques_realizados, valor):

    if valor > LIMITE_SAQUE:
        print(f"Valor do saque excede o limite de R$ {LIMITE_SAQUE:.2f}.")
        return
    if saques_realizados >= LIMITE_SAQUES_DIARIOS:
        print(f"Limite de saques diários de {LIMITE_SAQUES_DIARIOS} atingido.")
        return
    if valor > saldo:
        print("Saldo insuficiente para realizar o saque.")
        return
    
    saldo -= valor
    extrato.append(f"Saque: R$ {valor:.2f}")
    saques_realizados += 1
    print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
    return saldo, saques_realizados

def deposito(valor):
    global saldo

    if valor <= 0:
        print("Valor do depósito deve ser positivo.")
        return
    
    saldo += valor
    extrato.append(f"Depósito: R$ {valor:.2f}")
    print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")

def extrato_bancario():
    print("\n===== EXTRATO BANCÁRIO =====")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        for linha in extrato:
            print(linha)
    print(f"Saldo atual: R$ {saldo:.2f}")

def exibir_menu():
    print("\n===== MENU =====")
    print("1. Saque")
    print("2. Depósito")
    print("3. Extrato")
    print("4. Sair")

def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            valor = float(input("Informe o valor do saque: R$ "))
            saque(saldo = saldo, saques_realizados = saques_realizados, valor = valor)
        elif opcao == '2':
            valor = float(input("Informe o valor do depósito: R$ "))
            deposito(valor)
        elif opcao == '3':
            extrato_bancario()
        elif opcao == '4':
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

        continuar = input("\nDeseja realizar outra operação? (s/n): ").lower()
        if continuar != 's':
            print("Encerrando sessão. Obrigado por usar nosso sistema!")
            break

# Executar o programa
main()
