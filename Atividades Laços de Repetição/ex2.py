# 2 - Faça um programa que peça ao usuário para adivinhar um número entre 1 e 100.
# Enquanto o número digitado não for igual a um número secreto definido pelo programa,
# o programa deve pedir ao usuário que tente novamente. Quando o usuário acertar o número,
# o programa deve imprimir "Parabéns, você acertou!".
# Use a biblioteca abaixo para números aleatórios:
# import random
# numero_secreto = random.randint(1, 100)

import random

numero_secreto = random.randint(1,100)

print('Tente adivinhar um numero de 1 a 100 em 3 tentativas!')

for tentativa in range(3):
    palpite = int(input('Digite seu palpite: '))

    if palpite == numero_secreto:
        print('Parabéns, você acertou!')
    else:
        restantes = 2 - tentativa
        if restantes > 0:
            print(f'Errado! ({restantes} tentativas restantes)')
        else:
            print(f'Acabaram as tentativas! O numero secreto era {numero_secreto}')