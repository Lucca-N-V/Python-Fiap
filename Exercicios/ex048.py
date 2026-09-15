p1 = float(input('Digite o primeiro termo da sua PA'))
r = float(input('Digite a razão da sua PA'))
for i in range(1,11):
    pa = p1 + (i-1)*r
    print(f'{pa:.2f}')