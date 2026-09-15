x = float(input('Digite seu 1 número'))
y = float(input('Digite seu 2 número'))
z = float(input('Digite seu 3 número'))
if x >= y and x >= z and y >= z:
    print(f'O maior número é {x} e o menor é {z} !')
elif x >= y and x >= z and z >= y:
    print(f'O maior número é {x} e o menor é {y} !')
elif y >= x and y >= z and x >= z:
    print(f'O maior número é {y} e o menor é {z} !')
elif y >= x and y >= z and z >= x:
    print(f'O maior número é {y} e o menor é {x} !')
elif z >= x and z >= y and y >= x:
    print(f'O maior número é {z} e o menor é {x} !')
elif z >= x and z >= y and x >= y:
    print(f'O maior número é {z} e o menor é {y} !')
elif y == x and y == z and z == x:
    print(f'O maior e o menor número é {x}')