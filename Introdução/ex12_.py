print('Calculadora de Valor com Desconto')

vp = float(input('Qual o valor do produto? R$ '))
vd = float(input('Qual o valor do desconto em %? '))
vf1 = (vp*vd) / 100
vf2 = vp - vf1

print('O valor com desconto do produto vai ser igual a R${}'.format(vf2))