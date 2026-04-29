# 1 - Ler um valor inteiro (aceitar somente valores entre 1 e 10) e escrever a tabuada de 1 a 10 do valor lido.

numero = int(input('Digite um numero de 1 a 10: '))
multi = 1
resultado = numero * multi

if numero <= 10:

    while multi <= 10:
        print(f'{numero} x {multi} = {resultado}')
        multi += 1
        
else:
    print('Apenas valores entre 1-10 sao aceitos!')