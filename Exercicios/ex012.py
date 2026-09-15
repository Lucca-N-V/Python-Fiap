x = float(input('Digite seu 1 número'))
y = float(input('Digite seu 2 número'))
z = float(input('Digite seu 3 número'))
if x >= y and x >= z:
    print(f'O maior número é {x}!')
elif y >= x and y >= z:
    print(f'O maior número é {y}!')
elif z >= x and z >= y:
    print(f'O maior número é {z}!')
elif y == x and y == z and z == x:
    print(f'O maior número é {x}')