x = float(input('Digite a velocidade do carro em km/h'))
y = x-80
if x > 80:
    print(f'Você recebeu uma multa de R${y*7}, diriga com mais cuidado...')
else:
    print('Você não recebeu uma multa!')