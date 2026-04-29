# Exercício 4 — Validador de senha
# Crie uma função validar_senha(senha) que verifique se a senha tem pelo
# menos 8 caracteres e retorne True ou False. No programa principal,
# use while para continuar pedindo uma senha ao usuário até que ela seja válida.

def validar_senha(senha):
    if len(senha) >= 8:
        return True
    else:
        return False

while True:
    password = input('Digite sua Senha: ')

    if validar_senha(password):
        print('Senha Cadastrada com Sucesso!')
        break
    else:
        print('Erro: A senha precisa ter pelo menos 8 caracteres. Tente novamente.')
