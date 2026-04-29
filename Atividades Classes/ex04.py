# Crie um sistema de locadora com duas classes: Veiculo e Locadora.
# A classe Veiculo deve ter os atributos privados modelo, placa e alugado. 
# A classe Locadora deve ter os metodos: cadastrar veiculo, alugar veiculo pela placa, devolver veiculo e listar veiculos disponiveis. 
# O sistema deve rodar em um menu de opcoes.

class Veiculo:
    def __init__(self, modelo, placa):
        self.__modelo = modelo
        self.__placa = placa
        self.__alugado = False

    def obter_modelo(self):
        return self.__modelo

    def obter_placa(self):
        return self.__placa

    def esta_alugado(self):
        return self.__alugado

    def alugar(self):
        self.__alugado = True

    def devolver(self):
        self.__alugado = False

class Locadora:
    def __init__(self):
        self.veiculos = []

    def cadastrar_veiculo(self):
        modelo = input("Modelo: ")
        placa = input("Placa: ")
        novo = Veiculo(modelo, placa)
        self.veiculos.append(novo)
        print("Cadastrado com sucesso!")

    def alugar_veiculo(self):
        placa = input("Placa para alugar: ")
        for v in self.veiculos:
            if v.obter_placa() == placa:
                if not v.esta_alugado():
                    v.alugar()
                    print(f"Sucesso! {v.obter_modelo()} alugado.")
                else:
                    print("Erro: Este veículo já está alugado.")
                return
        print("Veículo não encontrado.")

    def devolver_veiculo(self):
        placa = input("Placa para devolver: ")
        for v in self.veiculos:
            if v.obter_placa() == placa:
                v.devolver()
                print(f"Sucesso! {v.obter_modelo()} devolvido.")
                return
        print("Veículo não encontrado.")

    def listar_veiculos(self):
        print("\n--- Relatório de Veículos ---")
        for v in self.veiculos:
            if v.esta_alugado() == False:
                print(f"Modelo: {v.obter_modelo()} | Placa: {v.obter_placa()}")

def main():
    locadora = Locadora()
    
    while True:
        print("\nMENU LOCADORA:")
        print("1. Cadastrar | 2. Alugar | 3. Devolver | 4. Listar Tudo | 5. Sair")
        opcao = input("Opção: ")
        
        if opcao == '1':
            locadora.cadastrar_veiculo()
        elif opcao == '2':
            locadora.alugar_veiculo()
        elif opcao == '3':
            locadora.devolver_veiculo()
        elif opcao == '4':
            locadora.listar_veiculos()
        elif opcao == '5':
            break
        else:
            print("Opção inválida.")

main()