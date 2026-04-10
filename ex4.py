class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.__titular = titular
        self.__saldo = saldo
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
    def mostrarSaldo(self):
        print(f'Saldo de: {self.__saldo}')
    def mostrarTitular(self):
        print(f'Correntista: {self.__titular}')

conta = ContaBancaria('Ana')
conta.depositar(5000)
conta.sacar(1000)
conta.mostrarSaldo()
conta.mostrarTitular()