# Escreva uma função que receba um dicionário como entrada e retorna uma nova lista contendo apenas as chaves

def dicionario_lista(dicionario):
    lista_chaves = []

    for chave in dicionario.keys():
        lista_chaves.append(chave)

    return lista_chaves


dicionario = {'n1': 1, 'n2': 2, 'n3': 3}
chaves = dicionario_lista(dicionario)
print(chaves)
