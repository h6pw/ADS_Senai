print ('QUANTOS LITROS DE TINTA SERAO NECESSARIOS PARA X AREA')

l= float(input('Digite a largura em metros: '))
a = float(input('Digite a altura em metros: '))
area = float((l*a))
tinta = area / 2
print('O valor da area da parede corresponde a {}m² \ne vao ser necessarios {:.2f}L de tinta'.format(area, tinta))