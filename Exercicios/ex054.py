m = 0
f = 0
x = 'M'
while x in ['M', 'F']:
    x = input('Digite seu sexo [M, F]').strip().upper()
    if x == 'M':
        m += 1
    elif x == 'F':
        f += 1
print(f'Erro de digitação. Ate agora foram {m} homens e {f} mulheres')