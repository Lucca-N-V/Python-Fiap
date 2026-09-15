import random
o = ['pedra', 'papel', 'tesoura']
x = input('Digite pedra ou papel ou tesoura!').strip() .lower()
y = random.choice(o)
a = 'pedra'
b = 'papel'
c = 'tesoura'
if x in ['pedra', 'papel', 'tesoura']:
    if x == a and y == c:
        print(f'O computador escolheu {y}. Parabens você ganhou!')
    elif x == a and y == b:
        print(f'O computador escolheu {y}. Infelizmente você perdeu')
    elif x == b and y == a:
        print(f'O computador escolheu {y}. Parabens você ganhou!')
    elif x == b and y == c:
        print(f'O computador escolheu {y}. Infelizmente você perdeu')
    elif x == c and y == b:
        print(f'O computador escolheu {y}. Parabens você ganhou!')
    elif x == c and y == a:
        print(f'O computador escolheu {y}. Infelizmente você perdeu')
    else:
        print(f'Você e o computador escolheram {x}. Empate.')
else:
    print('Erro. Por favor escreva corretamente as palavras')