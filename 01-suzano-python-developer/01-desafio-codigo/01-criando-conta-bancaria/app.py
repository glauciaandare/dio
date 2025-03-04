class ContaBancaria:
    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0
        self.operacoes = []

    def depositar(self, valor):
        self.saldo += valor
        self.operacoes.append(f"+{valor}")

    def sacar(self, valor):
        if self.saldo + valor >= 0:
            self.saldo += valor
            self.operacoes.append(str(valor))
        else:
            self.operacoes.append("Saque não permitido")

    def extrato(self):
        operacoes_formatadas = ", ".join(self.operacoes)
        print(f"Operações: {operacoes_formatadas}; Saldo: {self.saldo}")


# Leitura da entrada
nome_titular = input().strip()
conta = ContaBancaria(nome_titular)

entrada_transacoes = input().strip()
transacoes = [int(valor) for valor in entrada_transacoes.split(",")]

# Processamento das transações
for valor in transacoes:
    if valor > 0:
        conta.depositar(valor)
    else:
        conta.sacar(valor)

# Impressão do extrato final
conta.extrato()
