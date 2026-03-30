import random

def jogo_adivinhacao():
    numero_secreto = random.randint(1, 100)
    tentativas = 0

    palpite = 0

    while palpite != numero_secreto:
        palpite = int(input('Digite seu palpite (1 a 100): '))
        tentativas += 1

        if palpite < numero_secreto:
            print("Muito baixo!")
        elif palpite > numero_secreto:
            print("Muito alto!")
        else:
            print(f"Parabéns! Você acertou em {tentativas} tentativas.")

jogo_adivinhacao()