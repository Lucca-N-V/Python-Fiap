x = int(input('Digite sua idade'))
a = 18 - x
b = x - 18
if 0 < x < 17:
    print(f'Falta {a} anos para você se alistar!')
elif x == 17:
    print('Falta 1 ano para você se alistar, preste atenção !')
elif x ==18:
    print('Está na hora de se alistar em')
elif x > 19:
    print(f'Já passou o prazo de alistamento por {b} anos!')
elif x == 19:
    print('Já passou o prazo de alistamento por 1 ano! ')
else:
    print('Erro. Por favor insira uma idade válida')
