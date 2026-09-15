x = float(input('Digite seu peso em kg'))
y = float(input('Digite sua altura em m'))
mc = x / y**y
if 0 < mc < 18.5 and x > 0 and y > 0:
    print(f'Sua massa corporea é de {mc:.2f} kg/m². Ela está classificada como abaixo do peso ideal')
elif 18.5 <= mc < 25 and x > 0 and y > 0:
    print(f'Sua massa corporea é de {mc:.2f} kg/m². Ela está classificada como peso ideal!')
elif 25 <= mc < 30 and x > 0 and y > 0:
    print(f'Sua massa corporea é de {mc:.2f} kg/m². Ela está classificada como sobrepeso')
elif 30 <= mc < 40 and x > 0 and y > 0:
    print(f'Sua massa corporea é de {mc:.2f} kg/m². Ela está classificada como Obesidade')
elif mc >= 40 and x > 0 and y > 0:
    print(f'Sua massa corporea é de {mc:.2f} kg/m². Ela está classificada como Obesidade mórbida!')
else:
    print('Erro. Por favor insira dados válidos')
