class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.__titular = titular
        self.__saldo = saldo
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print('Depósito de R$', valor, 'efetuado')
        else:
            print('Valor inválido para depósito')
    def sacar(self, valor):
        if valor > 0:
            if self.__saldo >= valor:
                self.__saldo -= valor
                print('Saque de R$', valor, 'efetuado')
            else:
                print('Saldo insuficiente para saque.')
        else:
            print('Valor de saque incorreto')
    def mostrar_saldo(self):
        status = 'Devendo ao banco.' if self.__saldo < 0 else 'Em dia'
        print('Saldo R$', self.__saldo, '-', status)
    def get_titular(self):
        return self.__titular
    
class Banco:
    def __init__(self):
        self.correntistas = []
    def abrir_conta(self):
        nome = input('Digite o nome do titular: ')
        conta = ContaBancaria(nome)
        self.correntistas.append(conta)
        print('Conta aberta com sucesso!')
    def encontrar_conta(self, nome):
        for conta in self.correntistas:
            if conta.get_titular() == nome:
                return conta
        return None
    def depositar_fundos(self):
        nome = input('Digite o nome do titular: ')
        conta = self.encontrar_conta(nome)
        if conta:
            try:
                valor = float(input('Digite o depósito: '))
                conta.depositar(valor)
            except ValueError:
                print('Entrada Inválida')
        else:
            print('Correntista não encontrado.')
    def sacar_fundos(self):
        nome = input('Digite o nome do titular: ')
        conta = self.encontrar_conta(nome)
        if conta:
            try:
                valor = float(input('Digite o valor de saque:'))
                conta.sacar(valor)
            except ValueError:
                print('Entrada inválida.')
        else:
            print('Correntista não encontrado.')
    def mostrar_saldo_correntista(self):
        nome = input('Digite o nome do titular: ')
        conta = self.encontrar_conta(nome)
        if conta:
            conta.mostrar_saldo()
        else:
            print('Correntista não encontrado.')
    def listar_contas(self):
        if not self.correntistas:
            print('Nenhuma conta cadastrada.')
            return
        print('Lista de correntistas:')
        for conta in self.correntistas:
            print(conta.get_titular(), 'Saldo de R$', conta.mostrar_saldo())

def main():
    banco = Banco()
    while True:
        print('\n --- Menu Bancário ---')
        print('1. Abrir conta \n 2. Depositar \n 3. Sacar \n 4. Mostrar saldo \n 5. Listar correntistas \n 6. Sair')
        opcao = input('Escolha uma opção: ')
        if opcao == '1':
            banco.abrir_conta()
        elif opcao == '2':
            banco.depositar_fundos()
        elif opcao == '3':
            banco.sacar_fundos()
        elif opcao == '4':
            banco.mostrar_saldo_correntista()
        elif opcao == '5':
            banco.listar_contas()
        elif opcao == '6':
            print('Encerrando Sistema Bancário \n Até a próxima :D')
            break
        else:
            print('Opção Inválida \n Tente novamente.')
main()