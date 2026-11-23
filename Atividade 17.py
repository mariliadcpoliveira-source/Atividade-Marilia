Crie uma classe ContaBancaria com titular, saldo inicial e métodos
para depositar, sacar (impedindo saldo negativo) e extrato.

-Resposta

class ContaBancaria:
    def __init__(self, titular, saldo=0.0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            return True
        print("Saldo insuficiente ou valor inválido.")
        return False

    def extrato(self):
        print(f"Titular: {self.titular} | Saldo: R$ {self.saldo:.2f}")

conta = ContaBancaria("Ana", 100)
conta.depositar(50)
conta.sacar(30)
conta.extrato()

