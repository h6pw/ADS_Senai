#5 - Faça um programa que simule a urna eletrônica.
#A tela a ser apresentada deverá ser da seguinte forma:
#As opcoes sao:
#1. Candidato Jair Rodrigues
#2. Candidato Carlos Luz
#3. Candidato Neves Rocha
#4. Nulo
#5. Branco
#Entre com o seu voto:
#O programa deverá ler os votos dos eleitores e, quando for entrado o número 6, apresentar as seguintes
#informações:
#a) O número de votos de cada candidato;
#b) A porcentagem de votos nulos;
#c) A porcentagem de votos brancos;
#d) O candidato vencedor.

jair = 998
carlos = 500
neves = 222
nulo = 50
branco = 9

while True:

    print("\nAs opções são:")
    print("1. Candidato Jair Rodrigues")
    print("2. Candidato Carlos Luz")
    print("3. Candidato Neves Rocha")
    print("4. Nulo")
    print("5. Branco")
    print("6. Encerrar votação")

    voto = int(input("Entre com o seu voto: "))

    if voto == 1:
        jair += 1
    elif voto == 2:
        carlos += 1
    elif voto == 3:
        neves += 1
    elif voto == 4:
        nulo += 1
    elif voto == 5:
        branco += 1
    elif voto == 6:
        break
    else:
        print("Opção inválida!")

total = jair + carlos + neves + nulo + branco

print("\nResultado da votação:")
print(f"Jair Rodrigues: {jair} votos")
print(f"Carlos Luz: {carlos} votos")
print(f"Neves Rocha: {neves} votos")

if total > 0:
    print(f"Porcentagem de votos nulos: {(nulo/total)*100:.2f}%")
    print(f"Porcentagem de votos brancos: {(branco/total)*100:.2f}%")

if jair > carlos and jair > neves:
    vencedor = "Jair Rodrigues"
elif carlos > jair and carlos > neves:
    vencedor = "Carlos Luz"
elif neves > jair and neves > carlos:
    vencedor = "Neves Rocha"
else:
    vencedor = "Empate"

print(f"Vencedor: {vencedor}")