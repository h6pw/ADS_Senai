# Escreva uma função que receba itens (números) em um dicionário como entrada e retorne a chave com o maior valor.

def maior_valor():

    numeros = {
    'n1': 300,
    'n2': 200,
    'n3': 500
    }

    maior = max(numeros.keys)
    print(maior)

maior_valor()