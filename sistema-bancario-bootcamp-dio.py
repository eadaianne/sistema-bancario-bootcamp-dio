saldo = 0.00
extrato = []
LIMITE_SAQUE = 500.00
LIMITE_SAQUES_DIARIOS = 3
saques_realizados = 0

def saque(*, saldo, saques_realizados, valor):
    if valor > LIMITE_SAQUE:
        print(f"Valor do saque excede o limite de R$ {LIMITE_SAQUE:.2f}.")
        return saldo, saques_realizados, None
    if saques_realizados >= LIMITE_SAQUES_DIARIOS:
        print(f"Limite de saques diários de {LIMITE_SAQUES_DIARIOS} atingido.")
        return saldo, saques_realizados, None
    if valor > saldo:
        print("Saldo insuficiente para realizar o saque.")
        return saldo, saques_realizados, None

    saldo -= valor
    saques_realizados += 1
    print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
    return saldo, saques_realizados, f"Saque: R$ {valor:.2f}"

def deposito(saldo, valor, /):
    if valor <= 0:
        print("Valor do depósito deve ser positivo.")
        return saldo, None
    saldo += valor
    print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
    return saldo, f"Depósito: R$ {valor:.2f}"

def extrato_bancario(saldo, *, extrato):
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
    global saldo, saques_realizados, extrato
    print("Bem-vindo ao Sistema Bancário!")
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            valor = float(input("Informe o valor do saque: R$ "))
            saldo, saques_realizados, descricao = saque(
                saldo=saldo,
                saques_realizados=saques_realizados,
                valor=valor
            )
            if descricao:
                extrato.append(descricao)

        elif opcao == '2':
            valor = float(input("Informe o valor do depósito: R$ "))
            saldo, descricao = deposito(saldo, valor)
            if descricao:
                extrato.append(descricao)

        elif opcao == '3':
            extrato_bancario(saldo, extrato=extrato)

        elif opcao == '4':
            print("Saindo do sistema. Até logo!")
            break

        else:
            print("Opção inválida. Tente novamente.")

        continuar = input("\nDeseja realizar outra operação? (s/n): ").lower()
        if continuar != 's':
            print("Encerrando sessão. Obrigado por usar nosso sistema!")
            break

main()