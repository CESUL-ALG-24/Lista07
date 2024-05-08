from random import randint

num = randint(0, 100)

for i in range(1, 11):
    palpite = int(input("Informe seu palpite: "))

    if palpite == num:
        print(f"Você acertou em {i} tentativas")
        break

    if i == 10:
        print(f"O número sorteado era {num}! Você não acertou!")
    elif num > palpite:
        print("O número sorteado é maior que o seu palpite!")
    elif num < palpite:
        print("O número sorteado é menor que o seu palpite!")
