# Crie um sistema escolar com duas classes: Aluno e Escola.
#A classe Aluno deve ter os atributos privados nome, matricula e lista de notas. 
# A classe Escola deve ter os metodos: matricular aluno, lancar nota, calcular media do aluno e listar alunos. 
# O sistema deve rodar em um menu de opcoes.

class Aluno:
    def __init__(self, nome, matricula):
        self.__nome = nome
        self.__matricula = matricula
        self.__lista_notas = []

    def obter_nome(self):
        return self.__nome
    
    def obter_matricula(self):
        return self.__matricula
    
    def obter_lista_notas(self):
        return self.__lista_notas

    def adicionar_nota(self, nota):
        self.__lista_notas.append(nota)

class Escola:
    def __init__(self):
        self.alunos = [
            Aluno('Matheus', '1'),
        ]

    def listar_alunos(self):
        print("\n--- Relatório de Alunos ---")
        if not self.alunos:
            print("Não existem alunos cadastrados.")
        else:
            for a in self.alunos:
                print(f"Nome: {a.obter_nome()} | Matrícula: {a.obter_matricula()} | Notas: {a.obter_lista_notas()}")

    def matricular_aluno(self):
        nome = input("Digite o nome do aluno: ")
        matricula = input("Digite o número da matrícula: ")
        novo_aluno = Aluno(nome, matricula)
        self.alunos.append(novo_aluno)
        print(f"Aluno {nome} matriculado com sucesso!")

    def lancar_nota(self):
        matricula_busca = input("Digite a matrícula do aluno para lançar nota: ")
        for a in self.alunos:
            if a.obter_matricula() == matricula_busca:
                nota = float(input(f"Digite a nota para {a.obter_nome()}: "))
                a.adicionar_nota(nota)
                print("Nota lançada!")
                return
        print("Aluno não encontrado.")

    def calcular_media_aluno(self):
        matricula_busca = input("Digite a matrícula para calcular a média: ")
        for a in self.alunos:
            if a.obter_matricula() == matricula_busca:
                notas = a.obter_lista_notas()
                if notas:
                    media = sum(notas) / len(notas)
                    print(f"A média do aluno {a.obter_nome()} é: {media:.2f}")
                else:
                    print("O aluno ainda não possui notas lançadas.")
                return
        print("Aluno não encontrado.")

def main():
    escola = Escola()
    
    while True:
        print("\n--- SISTEMA ESCOLAR ---")
        print("1. Matricular Aluno")
        print("2. Lançar Nota")
        print("3. Calcular Média")
        print("4. Listar Alunos")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            escola.matricular_aluno()
        elif opcao == '2':
            escola.lancar_nota()
        elif opcao == '3':
            escola.calcular_media_aluno()
        elif opcao == '4':
            escola.listar_alunos()
        elif opcao == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

main()
