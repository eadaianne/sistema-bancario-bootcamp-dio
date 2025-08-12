LIMITE_SAQUE = 500.00
LIMITE_SAQUES_DIARIOS = 3


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
    if valor <= 0:
        print("Valor inválido para saque.")
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


def extrato_bancario(saldo, extrato):
    print("\n===== EXTRATO BANCÁRIO =====")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        for linha in extrato:
            print(linha)
    print(f"Saldo atual: R$ {saldo:.2f}")


def criar_novo_usuario(*, nome, data_nascimento, cpf, endereco):
    usuario = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco,
    }
    return usuario


def validar_cpf(cpf, usuarios):
    if len(cpf) != 11 or not cpf.isdigit():
        raise ValueError("CPF inválido. Deve conter 11 dígitos numéricos.")
    elif cpf in [usuario["cpf"] for usuario in usuarios]:
        raise ValueError("CPF já cadastrado. Por favor, utilize outro CPF.")


def formata_endereco():
    logradouro = input("Informe o logradouro: ")
    numero = input("Informe o número: ")
    bairro = input("Informe o bairro: ")
    cidade = input("Informe a cidade: ")
    estado = input("Informe o estado (sigla): ")
    endereco_formatado = f"{logradouro}, {numero} - {bairro} - {cidade}/{estado}"
    return endereco_formatado


def exibir_informacoes_usuario(cpf, usuarios):
    if not any(usuario["cpf"] == cpf for usuario in usuarios):
        print("Usuário não encontrado.")
        return
    else:
        usuario = next(usuario for usuario in usuarios if usuario["cpf"] == cpf)
        print(f"===== INFORMAÇÕES DO USUÁRIO: =====")
        print(f"Nome: {usuario['nome']}")
        print(f"Data de Nascimento: {usuario['data_nascimento']}")
        print(f"CPF: {usuario['cpf']}")
        print(f"Endereço: {usuario['endereco']}")


def exibir_menu():
    print(
        "\n===== MENU =====\n"
        "1. Saque\n"
        "2. Depósito\n"
        "3. Extrato\n"
        "4. Criar nova conta\n"
        "5. Exibir informações do usuário\n"
        "6. Sair"
    )


def executar_saque(saldo, saques_realizados, extrato):
    try:
        valor = float(input("Informe o valor do saque: R$ "))
    except ValueError:
        print("Valor inválido.")
        return saldo, saques_realizados, extrato

    saldo, saques_realizados, descricao = saque(
        saldo=saldo, saques_realizados=saques_realizados, valor=valor
    )

    if descricao:
        extrato.append(descricao)

    return saldo, saques_realizados, extrato


def executar_deposito(saldo, extrato):
    try:
        valor = float(input("Informe o valor do depósito: R$ "))
    except ValueError:
        print("Valor inválido.")
        return saldo, extrato

    saldo, descricao = deposito(saldo, valor)
    if descricao:
        extrato.append(descricao)

    return saldo, extrato


def executar_criar_novo_usuario(usuarios):
    cpf = input("Informe seu CPF (somente números): ")
    try:
        validar_cpf(cpf, usuarios)
    except ValueError as e:
        print(e)
        return usuarios

    nome = input("Informe seu nome: ")
    data_nascimento = input("Informe sua data de nascimento (DD/MM/AAAA): ")
    endereco = formata_endereco()

    usuarios.append(
        criar_novo_usuario(
            nome=nome,
            data_nascimento=data_nascimento,
            cpf=cpf,
            endereco=endereco,
        )
    )
    print("Usuário criado com sucesso!")
    return usuarios


def executar_exibir_informacoes_usuario(usuarios):
    cpf = input("Informe o CPF do usuário: ")
    exibir_informacoes_usuario(cpf, usuarios)


def executar_extrato_bancario(saldo, extrato):
    extrato_bancario(saldo, extrato=extrato)


def main():
    saques_realizados = 0
    saldo = 0.00
    extrato = []
    usuarios = []

    print("Bem-vindo ao Sistema Bancário!")
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            saldo, saques_realizados, extrato = executar_saque(
                saldo=saldo, saques_realizados=saques_realizados, extrato=extrato
            )

        elif opcao == "2":
            saldo, extrato = executar_deposito(saldo, extrato)

        elif opcao == "3":
            executar_extrato_bancario(saldo, extrato=extrato)

        elif opcao == "4":
            usuarios = executar_criar_novo_usuario(usuarios)

        elif opcao == "5":
            executar_exibir_informacoes_usuario(usuarios)

        elif opcao == "6":
            print("Saindo do sistema. Até logo!")
            break

        else:
            print("Opção inválida. Tente novamente.")

        continuar = input("\nDeseja realizar outra operação? (s/n): ").lower()
        if continuar != "s":
            print("Encerrando sessão. Obrigado por usar nosso sistema!")
            break


main()
