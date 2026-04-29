# Escreva uma função que receba um dicionário como entrada e retorna duas listas. 
# Uma com chave e outra com valor.

def dicionario_lista(dicionario):
    lista_chaves = []
    lista_valores = []


    for chave, valor in dicionario.items():
        lista_chaves.append(chave)
        lista_valores.append(valor)

    return lista_chaves, lista_valores


dicionario = {'n1': 1, 'n2': 2, 'n3': 3}
chaves, valores = dicionario_lista(dicionario)
print(chaves)
print(valores)