print('=== TABUADA ===')
n = int(input('Digite um numero: '))
x = 0

for x in range(1,11):
    print(f'{n} * {x} = {n*x}')

while x < 10:
    x += 1
    print(f'{n} * {x} = {n*x}')