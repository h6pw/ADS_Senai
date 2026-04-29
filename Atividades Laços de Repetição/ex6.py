#6 - Faça um algoritmo em python capaz de realizar o cálculo de rentabilidade de uma poupança,
#esse algoritmo deve receber como entrada o valor inicial que o usuário está disposto a guardar.
#Como saída, o programa deve imprimir na tela mês a mês o montante por 12 meses
#aplicado a uma taxa de 0,5 % ao mês de rentabilidade.
#A fórmula do montante (M) de uma aplicação financeira é dada por:
#M = P * (1 + i)^n
#onde:
#P é o capital inicial (ou principal)
#i é a taxa de juros aplicada (em forma decimal) - divida o valor dado por 100
#n é o número de períodos de tempo em que o dinheiro ficará investido.

P = float(input('Digite o valor a ser investido em R$: '))
i = 0.005
n = 1

while n <= 12:
    M = P * (1 + i) ** n
    print(f'Mês {n}: R$ {M:.2f}')
    n += 1