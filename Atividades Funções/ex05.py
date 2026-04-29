# Exercício 5 — Relatório de turma
# Crie duas funções: calcular_media(notas) e situacao_aluno(media).
# Monte uma lista de dicionários com nome e notas de 4 alunos. Use for para percorrer a lista,
# chamar as duas funções e exibir um relatório com nome, média e situação de cada aluno.

def calcular_media(notas):
    return sum(notas) / len(notas)

def situacao_aluno(media):
    if media >= 7:
        return 'Aprovado'
    else:
        return 'Reprovado'

alunos = [
    {'nome': 'Matheus', 'notas': [8, 9, 10, 7]},
    {'nome': 'Guilherme', 'notas': [7, 6, 6, 8]},
    {'nome': 'Ryan', 'notas': [10, 8, 7, 6]},
    {'nome': 'Alex', 'notas': [6, 8, 9, 10]}
]

for aluno in alunos:
    nome = aluno['nome']
    notas = aluno['notas']

    media = calcular_media(notas)

    situacao = situacao_aluno(media)

    print(f"NOME: {nome} | MÉDIA: {media} | SITUAÇÃO: {situacao}")