km = float(input('Quantos km foram percorridos? '))
dias = int(input('Por quantos dias que o carro foi alugado? '))
valor = (km*0.15) + (dias*60)
print('O valor a ser pago sera {:.2f}R$'.format(valor))