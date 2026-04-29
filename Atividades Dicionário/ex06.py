# Escreva uma função que receba um dicionário como entrada 
# e retorna uma nova lista com as chaves ordenadas em ordem alfabética.

def dicionario_lista_ordem(dicionario):
    return sorted(dicionario.keys())


dicionario = {'A': 1, 'X': 2, 'M': 3, 'Y': 4, 'Z': 7, 'B': 2}
chaves = dicionario_lista_ordem(dicionario)
print(chaves)