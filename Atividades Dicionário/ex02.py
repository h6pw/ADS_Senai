# Escreva uma função que receba Nome e Idade. Retorne valores que contêm a chave "idade" e cujo valor é maior que 18.

def maior_18():

    idades = {
        'idade1': 22,
        'idade2': 25,
        'idade3': 10,
        'idade4': 7
    }

    for idade in idades.values():
        if idade >= 18:
            print(f'A idade de {idade} anos é maior que 18 anos.')

maior_18()