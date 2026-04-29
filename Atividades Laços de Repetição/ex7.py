#7 - Faça um programa que mostre o fatorial de um número fornecido pelo usuário.

numero = int(input('Digite o numero que voce deseja saber o fatorial: '))

contador = numero
fatorial = 1

print(numero, "! =", numero, "x", numero-1, "x", "... x 1")

while contador > 0:
    fatorial = fatorial * contador
    contador -= 1

print("Resultado:", fatorial)