import random

palavras = ["Dinossauro", "Aurora boreal", "Criptografia", "Escafandro", "Eclipse", "Giroscópio", "Labirinto",
            "Molécula", "Nanotecnologia", "Ocarina", "Platô tibetano", "Quasar", "Ressonância magnética", "Sismógrafo",
            "Telescópio espacial"]

palavra_secreta = random.choice(palavras).upper()

letras_certas = []
letras_erradas = []
tentativas = 6

while tentativas > 0:
    palavra_atual = ""
    for letra in palavra_secreta:
        if letra in letras_certas:
            palavra_atual += letra
        else:
            palavra_atual += "_"
    print(palavra_atual)

    palpite = input("Digite uma letra: ").upper()

    if palpite in letras_certas or palpite in letras_erradas:
        print("Você já tentou essa letra. Tente outra.")

    elif palpite in palavra_secreta:
        print("Letra correta!")
        letras_certas.append(palpite)

        acertou = True
        for letra in palavra_secreta:
            if letra not in letras_certas:
                acertou = False
                break
        if acertou:
            print("Parabéns! Você acertou a palavra secreta: ", palavra_secreta)
            break

    else:
        print("Letra errada.")
        letras_erradas.append(palpite)
        tentativas -= 1

        if tentativas == 5:
            print("  O")
        elif tentativas == 4:
            print("  O")
            print(" /")
        elif tentativas == 3:
            print("  O")
            print(" /|")
        elif tentativas == 2:
            print("  O")
            print(" /|\\")
        elif tentativas == 1:
            print("  O")
            print(" /|\\")
            print(" /")
        else:
            print("  O")
            print(" /|\\")
            print(" / \\")
            print("Você perdeu! A palavra secreta era: ", palavra_secreta)
            break
