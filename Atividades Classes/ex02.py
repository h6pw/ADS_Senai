# Crie um sistema de estoque com duas classes: Produto e Estoque.
# A classe Produto deve ter os atributos privados nome, preco e quantidade. 
# A classe Estoque deve ter os metodos: cadastrar produto, adicionar quantidade, remover quantidade e listar produtos. 
# O sistema deve rodar em um menu de opcoes.

class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

class Estoque:
    def __init__(self):
        self.lista_de_produtos = [
            Produto('Celular', 600.0, 10),
            Produto('Mouse', 50.0, 5)
        ]

    def listar(self):
        print("\n--- ESTOQUE ATUAL ---")
        for p in self.lista_de_produtos:
            print(f"Produto: {p.nome} | Preco: R$ {p.preco} | Qtd: {p.quantidade}")

    def adicionar_quantidade(self):
        nome_busca = input("Nome do produto para ADICIONAR: ")
        
        for p in self.lista_de_produtos:
            if p.nome.lower() == nome_busca.lower():
                qtd = int(input(f"Quanto deseja adicionar ao {p.nome}? "))
                p.quantidade += qtd
                print("Estoque atualizado!")
                return
        
        print("Produto não encontrado.")

    def remover_quantidade(self):
        nome_busca = input("Nome do produto para REMOVER: ")
        
        for p in self.lista_de_produtos:
            if p.nome.lower() == nome_busca.lower():
                qtd = int(input(f"Quanto deseja remover do {p.nome}? "))
                if qtd <= p.quantidade:
                    p.quantidade -= qtd
                    print("Saída registrada!")
                else:
                    print("Erro: Você não tem essa quantidade em estoque.")
                return 
        
        print("Produto não encontrado.")

def main():
    estoque = Estoque()
    
    while True:
        print("\n1. Listar | 2. Adicionar | 3. Remover | 4. Sair")
        opcao = input("Escolha: ")
        
        if opcao == '1':
            estoque.listar()
        elif opcao == '2':
            estoque.adicionar_quantidade()
        elif opcao == '3':
            estoque.remover_quantidade()
        elif opcao == '4':
            break
        else:
            print("Opção inválida.")

main()