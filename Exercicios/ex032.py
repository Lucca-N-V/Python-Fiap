x = float(input('Escreva seu sálario'))
if x > 1250.00:
    print(f'O seu novo sálario será de R$ {x+(x/10):.2f} !')
elif 0 < x <= 1250.00:
    print(f'O seu novo sálario é de R$ {x+(x*15/100):.2f} !')
else:
    print('Erro. Por favor começe a ganhar um salário')