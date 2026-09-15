mv = 0
mm = 0
me = 0
for r in range(4):
    print(r)
    i = int(input('Digite sua idade'))
    s = input('Digite seu sexo'). strip() .lower()
    n = input('Digite seu nome').strip() .lower()
    me += i
    if r == 0:
        mv = i
    elif r != 0 and i > mv:
         mv = i
    if s == 'feminino' and i < 20:
        mm += 1
print(f'A pessoa mais velha tem {mv} anos. A média das idades é de {me/4:.2f} anos. E existem {mm} mulheres abaixo de 20 anos! ')
