x = (input('Digite um número de 0 a 9999')).strip()
if len(x) == 4:
    print(f'Unidade = {x[3]} !')
    print(f'Dezena = {x[2]} !')
    print(f'Centena = {x[1]} !')
    print(f'Milhar = {x[0]} !')
elif len(x) == 1:
    print(f'Unidade = {x[0]} !')
elif len(x) == 2:
    print(f'Unidade = {x[1]} !')
    print(f'Unidade = {x[0]} !')
elif len(x) == 3:
    print(f'Unidade = {x[2]} !')
    print(f'Dezena = {x[1]} !')
    print(f'Centena = {x[0]} !')
else:
    print('Por favor recomeçe, seguindo as regras desta vez')