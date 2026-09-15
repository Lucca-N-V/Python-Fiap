import random
x = 1, 2, 3, 4, 5
y = random.choice(x)
z = int(input('Escreva um número de 0 a 5'))
#if y == z:
#    print('Parabens, o computador escolheu o mesmo número!')
#elif y != z:
 #   print(f'Infelizmente o computador escolheu o numero {y}, você perdeu...')
#else:
 #   print('Erro. Por favor siga as regras.')

while z != y:
    z = int(input('Você perdeu, tente novamente'))
if y == z:
    print('Parabens, ganahste!')
