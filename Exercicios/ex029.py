x = float(input('Digite a distancia de sua viangem em km'))
y = x-200
if 0 < x <= 200:
    print(f'O preço da sua viagem é de R${x*0.5}!')
elif x > 200:
    print(f'O preço da sua viagem é de R${y*0.45+100}!')
else:
    print('Erro. Por favor digite um número positivo')