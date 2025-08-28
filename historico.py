class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        self.transacoes.append({
            'tipo': transacao.__class__.__name__,
            'valor': transacao.valor
            })

    def exibir(self):
        if not self.transacoes:
            print("Não foram realizadas movimentações.")
        else:
            for t in self.transacoes:
                print(f"{t['tipo']}: R$ {t['valor']:.2f}")