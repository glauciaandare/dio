class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

class SistemaBancario:
    def __init__(self):
        self.contas = []

    def criar_conta(self, titular, saldo):
        nova_conta = ContaBancaria(titular, saldo)
        self.contas.append(nova_conta)

    def listar_contas(self):
        saida = ", ".join([f"{conta.titular}: R$ {conta.saldo}" for conta in self.contas])
        print(saida)

# Criando instância do sistema bancário
sistema = SistemaBancario()

# Entrada de dados
while True:
    entrada = input().strip()
    if entrada.upper() == "FIM":
        break
    titular, saldo = entrada.split(", ")
    sistema.criar_conta(titular, int(saldo))

# Listando todas as contas cadastradas
sistema.listar_contas()
