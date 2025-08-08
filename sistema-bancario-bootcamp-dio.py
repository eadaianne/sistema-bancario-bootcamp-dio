saldo = 0.00
extrato = []
usuarios = []
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

def criar_nova_conta(*, nome, data_nascimento, cpf, endereco):
    validar_cpf(cpf)
    usuario = {
        'nome': nome,
        'data_nascimento': data_nascimento,
        'cpf': cpf,
        'endereco': endereco
    }
    return usuario

def validar_cpf(cpf):
    if len(cpf) != 11 or not cpf.isdigit():
        raise ValueError("CPF inválido. Deve conter 11 dígitos numéricos.")
    elif cpf in [usuario['cpf'] for usuario in usuarios]:
        raise ValueError("CPF já cadastrado. Por favor, utilize outro CPF.")

def formata_endereco():
    logradouro = input("Informe o logradouro: ")
    numero = input("Informe o número: ")
    bairro = input("Informe o bairro: ")
    cidade = input("Informe a cidade: ")
    estado = input("Informe o estado (sigla): ")
    endereco_formatado = f"{logradouro}, {numero} - {bairro} - {cidade}/{estado}"
    return endereco_formatado    

def exibir_menu():
    print("\n===== MENU =====")
    print("1. Saque")
    print("2. Depósito")
    print("3. Extrato")
    print("4. Criar nova conta")
    print("5. Sair")

def main():
    global saldo, saques_realizados, extrato, usuarios
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
            nome = input("Informe seu nome: ")
            data_nascimento = input("Informe sua data de nascimento (DD/MM/AAAA): ")
            cpf = input("Informe seu CPF (somente números): ")
            endereco = formata_endereco()
            usuarios.append(criar_nova_conta(
                nome=nome,
                data_nascimento=data_nascimento,
                cpf=cpf,
                endereco=endereco
            ))
            print("Conta criada com sucesso!")

        elif opcao == '5':
            print("Saindo do sistema. Até logo!")
            break

        else:
            print("Opção inválida. Tente novamente.")

        continuar = input("\nDeseja realizar outra operação? (s/n): ").lower()
        if continuar != 's':
            print("Encerrando sessão. Obrigado por usar nosso sistema!")
            break

main()