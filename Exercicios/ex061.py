x = int(input('Digite um número inteiro'))
n = int(input('Digite quantos termos você quer ver'))
z = 1
if n > 0:
    while z != n+1:
        if z == 1 or z == 2:
            a = x
            b = x
            z += 1
            print(a)
        elif (z + 1) % 2 == 0 and z != 1 and z != 2:
            a = a + b
            z += 1
            print(a)
        elif z % 2 == 0 and z != 1 and z != 2:
            b = b + a
            z += 1
            print(b)
else:
    print('Erro. Por favor coloque uma quantidade de termos positivo')
