# Tarefa Laços de Repetição
# 0 - Peça para  o usuário entrar com dois valores (primeiro e último).
# Faça a contagem entre esses números.
# Caso o último for menor que  o primeiro faça a contagem decrescente.
# Caso o último número for maior que o primeiro faça a contagem crescente.

n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o ultimo numero: '))

if n2 > n1:

    while n2 > n1-1:
        print(n1)
        n1 += 1

elif n1 > n2:

    while n1+1 > n2:
        print(n1)
        n1 += -1
