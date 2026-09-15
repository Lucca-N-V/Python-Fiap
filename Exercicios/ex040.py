x = float(input('Digite o comprimento da 1ª reta: '))
y = float(input('Digite o comprimento da 2ª reta: '))
z = float(input('Digite o comprimento da 3ª reta: '))


if x <= 0 or y <= 0 or z <= 0:
    print('Erro. Por favor insira valores positivos maiores que zero.')


elif x < y + z and y < x + z and z < x + y:


    if x == y == z:
        print('As retas formam um triângulo Equilátero!')
    elif x == y or x == z or y == z:
        print('As retas formam um triângulo Isósceles!')
    else:
        print('As retas formam um triângulo Escaleno!')

else:
    print('As retas não podem formar um triângulo.')