import random

carteira = 100

print("### Máquina caça-níqueis ###\n")
print(f"Você possui R${carteira}\n")

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
    print(carteira - 50)
if resultado == j:
    print("JACKPOT!!!")
    print(carteira * 10000)
if resultado == t:
    print("Você ganhou 3X")
    print(carteira * 3)
if resultado == d:
    print("Você ganhou 2X")
    print(carteira * 2)