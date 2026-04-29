# Exercício 2 — Contador de positivos e negativos
# Crie uma função analisar_numeros(lista) que percorra uma lista com for 
# e retorne quantos números são positivos, negativos e zeros. Teste com uma lista de pelo menos 6 números.


def analisar_numeros(lista):
    p = 0
    n = 0
    z = 0

    for numero in lista:
        if numero > 0:
            p += 1
        elif numero < 0:
            n += 1 
        else:
            z += 1

    return p, n, z

numeros = [1, 4, 7, -8, -9, 0]

p, n, z = analisar_numeros(numeros)

print(numeros)
print(f'Total de números positivos = {p}')
print(f'Total de números negativos = {n}')
print(f'Total de zeros = {z}')