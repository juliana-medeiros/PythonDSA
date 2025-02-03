import random
from os import system, name

#função para limpar a tela a cada execução
def limpa_tela():
    if name == 'nt':
        _ = system('cls')


#função
def game():
    limpa_tela()

    print("\n Bem vindo(a) ao jogo da forca!")
    print("Adivinhe a palavra abaixo:\n")

    #Lista de palavras
    palavras = ['banana', 'abacate', 'uva', 'morango', 'laranja']

    #Escolhe randomicamente uma palavra
    palavra = random.choice(palavras)

    #List comprehension
    letras_descobertas = ['_' for letra in palavra]

    chances = 6

    #Lista para letras erradas
    letras_erradas = []

    #Loop enquanto o número de chances for MAIOR do que 0
    while chances > 0:

        print(" ".join(letras_descobertas))
        print("\n Chances restantes: ", chances)
        print("Letras erradas: ", " ".join(letras_erradas))

        #Tentativa
        tentativa = input("\n Digite uma letra: ").lower()

        #Condicional
        if tentativa in palavra:
            index = 0

            for letra in palavra:
                if tentativa == letra:
                    letras_descobertas[index] = letra
                index += 1
        else:
            chances -= 1
            letras_erradas.append(tentativa)

        #Condicional
        if "_" not in letras_descobertas:
            print("\n Você venceu, a palavra era: ", palavra)
            break

    #Condicional
    if "_" in letras_descobertas:
        print("\n Você perdeu, a palavra era: ", palavra)

#Bloco main
if __name__ == "__main__":
    game()
    print("\n Fim!")
