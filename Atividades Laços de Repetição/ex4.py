# 4 - Faça um programa que peça ao usuário para digitar o número de vezes que ele quer jogar uma moeda.
# O programa deve simular o lançamento de uma moeda e imprimir o resultado de cada lançamento (cara ou coroa).
# No final, o programa deve imprimir o número total de caras e o número total de coroas.
# Use a biblioteca abaixo para números aleatórios:
# import random
# resultado = random.randint(0, 1)

import random

tentativas = int(input('Digite o numero de vezes que deseja jogar uma moeda: '))
cara = 0
coroa = 0
jogadas = 0

for jogadas in range(tentativas):
    resultado = random.randint(0,1)

    if resultado == 0:
        cara += 1
        print(f'Jogada {jogadas+1}: Cara')
    else:
        coroa += 1
        print(f'Jogada {jogadas+1}: Coroa')

print(f'\nTotal de caras: {cara}')
print(f'Total de coroas: {coroa}')