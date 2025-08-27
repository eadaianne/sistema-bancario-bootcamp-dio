from conta import Conta

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite = 500.0, limite_saques = 3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor):
        saques_realizados = len[transacao for transacao in self.historico.transacoes
                                if transacao['tipo'] == 'Saque']
        excedeu_saldo = valor > self.saldo
        excedeu_limite = valor > self.limite
        excedeu_saques = saques_realizados >= self.limite_saques

        if excedeu_saldo:
            print("Saldo insuficiente.")
        elif excedeu_limite:
            print("Valor do saque excede o limite.")
        elif excedeu_saques:
            print("Número máximo de saques diários excedido.")
        elif valor < 0:
            print("Valor inválido para saque.")
        else:
            return super().sacar(valor)
        return False