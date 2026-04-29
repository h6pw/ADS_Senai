# Exercício 3 — Tabuada personalizada
# Crie uma função tabuada(numero) que use while para gerar e exibir 
# a tabuada de um número de 1 a 10. Depois, use um for para chamar a função com cada número de uma lista como [2, 5, 7].

def tabuada(numero):
    x = 1
    while x <= 10:
        print(f"{numero} x {x} = {numero * x}")
        x += 1

numeros = [2, 5, 7]

for n in numeros:
    print(f"\nTabuada do {n}:")
    tabuada(n)