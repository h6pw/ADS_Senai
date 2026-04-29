class Pessoa:
    def __init__(self, nome=None, idade=None):
        if nome is None:
            nome = input('Digite seu nome: ')
        if idade is None:
            idade = int(input('Digite sua idade: '))
        self.nome = nome
        self.idade = idade
    def apresentar(self):
        print(f'Oi {self.nome}')
        print(f'você tem: {self.idade} anos')

pessoa1 = Pessoa()
pessoa1.apresentar()