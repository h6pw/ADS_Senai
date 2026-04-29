class Calculadora:
    def adicionar(self, a, b):
        return a+b
    def subtrair(self, a, b):
        return a-b
    def multiplicar(self, a,b):
        return a*b
    def dividir(self, a, b):
        if b == 0:
            return('não é possível dividir por 0 (zero)')
        else:
            return a/b


    
calc = Calculadora()
print(calc.adicionar(10,5))
print(calc.subtrair(10,5))
print(calc.multiplicar(10,5))
print(calc.dividir(10,5))