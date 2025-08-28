from pessoa_fisica import PessoaFisica
from conta_corrente import ContaCorrente
from deposito import Deposito
from saque import Saque

def exibir_menu():
    print(
        "\n===== MENU =====\n"
        "1. Saque\n"
        "2. Depósito\n"
        "3. Extrato\n"
        "4. Cadastrar usuário\n"
        "5. Exibir informações do usuário\n"
        "6. Criar nova conta\n"
        "7. Exibir contas cadastradas\n"
        "8. Sair"
    )

def buscar_usuario(cpf, usuarios):
    return next((u for u in usuarios if u.cpf == cpf), None)

def validar_cpf(cpf, usuarios):
    if len(cpf) != 11 or not cpf.isdigit():
        print("CPF inválido. Deve conter 11 dígitos numéricos.")
        return False
    elif cpf in [usuario.cpf for usuario in usuarios]:
        print("CPF já cadastrado. Por favor, utilize outro CPF.")
        return False
    return True


def exibir_informacoes_usuario(usuarios):
    cpf = input("Informe o CPF do usuário: ").strip()
    usuario = buscar_usuario(cpf, usuarios)

    if not usuario:
        print("Usuário não encontrado.")
        return

    print(f"\n=== INFORMAÇÕES DO USUÁRIO ===")
    print(f"Nome: {usuario.nome}")
    print(f"CPF: {usuario.cpf}")
    print(f"Data de Nascimento: {usuario.data_nascimento}")
    print(f"Endereço: {usuario.endereco}")

    if usuario.contas:
        print("\nContas do usuário:")
        for conta in usuario.contas:
            print(f"Agência: {conta.agencia} | Conta: {conta.numero} | Saldo: R$ {conta.saldo:.2f}")
    else:
        print("\nEste usuário não possui contas cadastradas.")

def selecionar_conta(usuario):
    if not usuario.contas:
        print("Usuário não possui contas.")
        return None
    print("Contas disponíveis:")
    for c in usuario.contas:
        print(f"{c.numero} - Saldo: R$ {c.saldo:.2f}")
    numero_conta = input("Informe o número da conta que deseja usar: ").strip()
    conta = next((c for c in usuario.contas if c.numero == numero_conta), None)
    if not conta:
        print("Conta não encontrada.")
        return None
    return conta

def main():
    usuarios = []
    contas = []

    print("Bem-vindo ao Sistema Bancário!")
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":  # Saque
            cpf = input("Informe o CPF do usuário: ").strip()
            usuario = buscar_usuario(cpf, usuarios)
            if usuario:
                conta = selecionar_conta(usuario)
                if conta:
                    valor = float(input("Informe o valor do saque: "))
                    usuario.realizar_transacao(conta, Saque(valor))
            else:
                print("Usuário não encontrado.")

        elif opcao == "2":  # Depósito
            cpf = input("Informe o CPF do usuário: ").strip()
            usuario = buscar_usuario(cpf, usuarios)
            if usuario:
                conta = selecionar_conta(usuario)
                if conta:
                    valor = float(input("Informe o valor do depósito: "))
                    usuario.realizar_transacao(conta, Deposito(valor))
            else:
                print("Usuário não encontrado.")

        elif opcao == "3":  # Extrato
            cpf = input("Informe o CPF do usuário: ").strip()
            usuario = buscar_usuario(cpf, usuarios)
            if usuario:
                conta = selecionar_conta(usuario)
                if conta:
                    print(f"\n=== Extrato da Conta {conta.numero} ===")
                    conta.historico.exibir()
                    print(f"Saldo atual: R$ {conta.saldo:.2f}")
            else:
                print("Usuário não encontrado.")

        elif opcao == "4":  # Cadastrar usuário
            nome = input("Nome: ").strip()
            cpf = input("CPF: ").strip()
            
            if not validar_cpf(cpf, usuarios):
                continue
            
            data_nascimento = input("Data de Nascimento (dd/mm/aaaa): ").strip()
            endereco = input("Endereço: ").strip()
            usuario = PessoaFisica(nome, cpf, data_nascimento, endereco)
            usuarios.append(usuario)
            print("Usuário cadastrado com sucesso!")

        elif opcao == "5":  # Exibir informações do usuário
            exibir_informacoes_usuario(usuarios)

        elif opcao == "6":  # Criar nova conta
            cpf = input("Informe o CPF do usuário: ").strip()
            usuario = buscar_usuario(cpf, usuarios)
            if usuario:
                numero_conta = str(len(contas) + 1)
                conta = ContaCorrente(numero_conta, usuario)
                usuario.adicionar_conta(conta)
                contas.append(conta)
                print(f"Conta criada com sucesso! Número: {numero_conta}")
            else:
                print("Usuário não encontrado.")

        elif opcao == "7":  # Exibir todas as contas
            if not contas:
                print("Nenhuma conta cadastrada.")
            for c in contas:
                print(f"Agência: {c.agencia} | Conta: {c.numero} | Titular: {c.cliente.nome} | Saldo: R$ {c.saldo:.2f}")

        elif opcao == "8":  # Sair
            print("Saindo do sistema. Até logo!")
            break

        else:
            print("Opção inválida. Tente novamente.")


        continuar = input("\nDeseja realizar outra operação? (s/n): ").strip().lower()
        if continuar != "s":
            print("Encerrando sessão. Obrigado por usar nosso sistema!")
            break

if __name__ == "__main__":
    main()
