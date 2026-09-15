
while True:
    x = int(input('Gostaria de ver a tabuada de qual valor?( Digite um número negativo para cancelar)'))
    if x >= 0:
     for i in range (1,11):
          print(f'{x} x {i} = {x*i}')
    else:
        break
print('Programa encerrado')