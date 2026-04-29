# 3 - Faça um programa que peça ao usuário para digitar uma sequência de números inteiros.
# O programa deve imprimir a soma dos números digitados, mas parar a soma se o usuário digitar um número negativo.

soma = 0

for numero in range(5):
    numero = int(input("Digite um número inteiro: "))

    if numero < 0:
        print(f'numero {numero} negativo encontrado! interrompendo soma')
        break

    soma += numero

print(f"A soma dos números positivos digitados é {soma}")