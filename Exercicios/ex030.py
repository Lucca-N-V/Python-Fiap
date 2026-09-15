x = float(input('Digite um ano'))
if x % 4 ==0 and x % 1 == 0 and x>= 0:
    print('O ano é bissexto!')
elif x % 4 !=0 and x % 1 == 0 and x >= 0:
    print('O ano não é bissexto!')
elif x % 1 != 0 or x < 0:
    print('Erro. Por favor insira um ano válido')
