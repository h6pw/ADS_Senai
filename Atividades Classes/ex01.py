#Crie um sistema de biblioteca com duas classes: Livro e Biblioteca.
# A classe Livro deve ter os atributos privados titulo, autor e disponivel. 
# A classe Biblioteca deve ter uma lista de livros e os metodos: cadastrar livro, emprestar livro, devolver livro e listar livros. 
# O sistema deve rodar em um menu de opcoes.


class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True

class Biblioteca:
    def __init__(self):
        self.lista_de_livros = [
            Livro('Harry Potter', 'J.K. Rowling'),
            Livro('Game of Thrones', 'George R.R. Martin'),
            Livro('Senhor dos Aneis', 'J.R.R. Tolkien')
        ]

    def cadastrar_livro(self):
        titulo = input('Digite o nome do livro: ')
        autor = input('Digite o nome do autor: ')
        novo_livro = Livro(titulo, autor)
        self.lista_de_livros.append(novo_livro)
        print(f'Livro "{titulo}" cadastrado!')

    def emprestar_livro(self):
        nome = input('Nome do livro para emprestar: ')
        for livro in self.lista_de_livros:
            if livro.titulo == nome:
                if livro.disponivel:
                    livro.disponivel = False
                    print(f'Sucesso! Você pegou o livro "{nome}".')
                    return
                else:
                    print('Este livro já está emprestado.')
                    return
        print('Livro não encontrado.')

    def devolver_livro(self):
        nome = input('Nome do livro para devolver: ')
        for livro in self.lista_de_livros:
            if livro.titulo == nome:
                livro.disponivel = True
                print(f'Obrigado! "{nome}" foi devolvido.')
                return
        print('Este livro não pertence à nossa biblioteca.')

    def listar_livros(self):
        print('\n--- Acervo da Biblioteca ---')
        for livro in self.lista_de_livros:
            status = "Disponível" if livro.disponivel else "Emprestado"
            print(f'[{status}] {livro.titulo} - {livro.autor}')

def main():
    biblioteca = Biblioteca() 
    
    while True:
        print('\nMenu de opções:')
        print('1. Cadastrar | 2. Emprestar | 3. Devolver | 4. Listar | 5. Sair')
        opcao = input('Digite a opção: ')

        if opcao == '1': biblioteca.cadastrar_livro()
        elif opcao == '2': biblioteca.emprestar_livro()
        elif opcao == '3': biblioteca.devolver_livro()
        elif opcao == '4': biblioteca.listar_livros()
        elif opcao == '5': break
        else: print('Opção inválida.')


main()