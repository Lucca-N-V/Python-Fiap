x = float(input('Digite um valor'))
y = float(input('Digite um valor'))
z = int(input('Escolha uma opção \n 1 - Somar \n 2 - Multiplicar \n 3 - Maior/Menor \n 4 - Novos números \n 5 - Cancelar o programa'))
if z not in [1, 2, 3, 4, 5]:
    print('Erro, por favor escolha uma opção válida')
elif z in [1, 2, 3, 5]:
    if z == 1:
        print(f'{x:.2f} + {y:.2f} = {x + y:.2f}')
    elif z == 2:
        print(f'{x:.2f} x {y:.2f} = {x * y:.2f}')
    elif z == 3:
        if x > y:
            print(f'{x} é maior que {y}')
        elif y > x:
            print(f'{y} é maior que {x}')
        else:
            print('Os números tem o mesmo valor')
    elif z == 5:
        print('Programa finalizado com sucesso')
else:
    while z == 4:
        x = float(input('Digite um valor'))
        y = float(input('Digite um valor'))
        z = int(input(
            'Escolha uma opção \n 1 - Somar \n 2 - Multiplicar \n 3 - Maior/Menor \n 4 - Novos números \n 5 - Cancelar o programa'))
        if z not in [1, 2, 3, 4, 5]:
            print('Erro, por favor escolha uma opção válida')
        elif z in [1, 2, 3, 5]:
            if z == 1:
                print(f'{x:.2f} + {y:.2f} = {x + y:.2f}')
            elif z == 2:
                print(f'{x:.2f} x {y:.2f} = {x * y:.2f}')
            elif z == 3:
                if x > y:
                    print(f'{x} é maior que {y}')
                elif y > x:
                    print(f'{y} é maior que {x}')
                else:
                    print('Os números tem o mesmo valor')
            elif z == 5:
                print('Programa finalizado com sucesso')

