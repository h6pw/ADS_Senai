# Crie um sistema de clinica com duas classes: Animal e Clinica.
# A classe Animal deve ter os atributos privados nome, especie e dono. 
# A classe Clinica deve ter os metodos: cadastrar animal, buscar animal pelo nome do dono e listar todos os animais. 
# O sistema deve rodar em um menu de opcoes.

class Animal:
    def __init__(self, nome, especie, dono):
        self.nome = nome
        self.especie = especie
        self.dono = dono

class Clinica:
    def __init__(self):
        self.pets = [
            Animal('Pyke', 'Cachorro', 'Matheus')
        ]

    def cadastrar_animal(self):
        nome_pet = input('Digite o nome do pet: ')
        raca_pet = input('Digite a raca ou especie do pet: ')
        nome_dono = input('Digite o nome do dono: ')
        novo_cadastro = Animal(nome_pet, raca_pet, nome_dono)
        self.pets.append(novo_cadastro)
        print(f'O pet {nome_pet} foi cadastrado com sucesso!')

    def buscar_animal(self):
        dono = input("Digite o nome do dono: ")
        encontrados = [a for a in self.pets if dono == a.dono]
        if encontrados:
            print("Animais encontrados:")
            for pet in encontrados:
                print("Nome:", pet.nome, "- Especie:", pet.especie)
        else:
            print("Nenhum animal encontrado para esse dono.")

    def lista_animal(self):
        print("\n--- PETS CADASTRADOS ---")
        for p in self.pets:
            print(f"Nome: {p.nome} | Especie: {p.especie} | Dono: {p.dono}")



def main():
    clinica = Clinica()
    
    while True:
        print("\n1. Cadastrar Pet | 2. Procurar Pet via Dono | 3. Listar Pets | 4. Sair")
        opcao = input("Escolha: ")
        
        if opcao == '1':
            clinica.cadastrar_animal()
        elif opcao == '2':
            clinica.buscar_animal()
        elif opcao == '3':
            clinica.lista_animal()
        elif opcao == '4':
            break
        else:
            print("Opção inválida.")

main()