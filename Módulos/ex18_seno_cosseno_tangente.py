import math

ang = float(input('Digite um angulo qualquer: '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))

print('O angulo {:.2f} \npossui seno = {:.2f} \ncosseno = {:.2f} \ntangente = {:.2f}'.format(ang, sen, cos, tan))