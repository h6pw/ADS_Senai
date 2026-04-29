"""from math import sqrt, pow

-> importei a funcao de raiz/potencia, sem saber que tinha uma direta pra hipotenusa

oposto = float(input('Digite o valor do Cateto Oposto: '))
adjacente = float(input('Digite o valor do Cateto Adjacente: '))
hip = sqrt(pow(oposto, 2) + pow(adjacente, 2))

print('Um triangulo com cateto oposto = {}, cateto adjacente = {}, vai ter como hipotenusa = {}'.format(oposto, adjacente, hip))"""


from math import hypot
oposto = float(input('Digite o valor do Cateto Oposto: '))
adjacente = float(input('Digite o valor do Cateto Adjacente: '))
hip = hypot(oposto, adjacente)
print(hip)