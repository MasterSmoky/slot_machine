import random

carteira = float(input("Quanto você possui na sua carteira ?: "))
aposta = float(input("Quanto você deseja apostar ?: "))

print("### Máquina caça-níqueis ###\n")
print(f"Você possui R${carteira}\n")

if carteira < aposta:
    print("Você não tem dinheiro para apostar")
else:
    itens = ('Sino', 'Cereja', 'Sete', 'Bar')

    x = random.sample(itens, 3)
    j = itens[2], itens[2], itens[2]
    t = itens[0], itens[0], itens[0]
    d = itens[3], itens[3], itens[3]

    possibilidades = (x, j, t, d)
    probabelilidades = (10, 0.5, 0.8, 1)

    resultado = random.choices(possibilidades, probabelilidades)[0]

    print(resultado)

    if resultado == x:
        print("Tente de novo!")
        print(f"R${carteira - aposta}")
    if resultado == j:
        print("JACKPOT!!!")
        print(f"R${carteira + aposta * 10000}")
    if resultado == t:
        print("Você ganhou 3X")
        print(f"R${carteira + aposta * 3}")
    if resultado == d:
        print("Você ganhou 2X")
        print(f"R${carteira + aposta * 2}")