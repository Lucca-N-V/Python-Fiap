import random
numero = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
v = 0
while True:
    x = int(input('Digite um número de 1 a 10'))
    y = random.choice(numero)
    z = input('Par ou Impár? [P/I]').strip().upper()
    while z not in ['P', 'I']:
        z = input('Erro. Digite P ou I').strip().upper()
    r = (x + y)
    print('-' * 30)
    if r % 2 == 0 and z == 'P':
        print(f'Você escolheu {x} e o computador {y} resultando em {x+y}, Voce ganhou')
        print('-'*30)
        print('Vamos novamente até você perder')
        v += 1
    elif (r + 1) % 2 == 0 and z == 'I':
        print(f'Você escolheu {x} e o computador {y} resultando em {x+y}, Voce ganhou')
        print('-' * 30)
        print('Vamos novamente até você perder')
        v += 1
    elif r % 2 == 0 and z == 'I':
        print(f'Você escolheu {x} e o computador {y} resultando em {x+y}, Voce perdeu...')
        break
    elif (r + 1) % 2 == 0 and z == 'P':
        print(f'Você escolheu {x} e o computador {y} resultando em {x+y}, Voce perdeu...')
        break
    print('-' * 30)
print('-' * 30)
if v == 0:
    print('Você ganhou 0 vezes, que azar em')
elif v == 1:
    print('Você ganhou 1 vez')
else:
    print(f'Você ganhou {v} vezes!')