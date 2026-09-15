q = 1
import random
x = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
y = random.choice(x)
z = int(input('Escreva um número de 1 a 10'))
while z != y:
    z = int(input('Tente novamente'))
    if z != y:
        q += 1
print(f'Você ganhou em {q} chutes !!!')
