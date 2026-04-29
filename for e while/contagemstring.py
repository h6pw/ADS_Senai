print('=== CONTADOR DE VOGAIS ===')

vogais = {"a","e","i","o","u"}
palavra = str(input("Insira uma palavra: ").lower())

contador = sum(1 for letra in palavra if letra in vogais)
    
print(f"A palavra {palavra} tem {contador} vogais")