# Escreva uma função que receba duas listas de mesmo comprimento, uma contendo chaves e outra contendo valores, 
# e retorna um dicionário criado a partir dessas listas.

def lista_dicionario():

    lista1 = ['n1', 'n2', 'n3', 'n4']
    lista2 = [1, 2, 3, 4]

    dicionario = {}

    for i in range(len(lista1)):
        chave = lista1[i]
        valor = lista2[i]
        dicionario[chave] = valor

    print(dicionario)

lista_dicionario()