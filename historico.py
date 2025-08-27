class Historico:
    def __init__(self):
        self.historico = []

    def adicionar_transacao(self, transacao):
        self.historico.append [
            'tipo': transacao.__class__.__name__,
            'valor': transacao.valor
        ]