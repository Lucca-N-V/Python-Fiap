p1 = float(input('Digite o primeiro termo da sua PA'))
r = float(input('Digite a razão da sua PA'))
z = 1
while z != 11:
    paw = p1 + (z - 1)*r
    z += 1
    print(f'{paw:.2f}')