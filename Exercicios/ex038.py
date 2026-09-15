x = float(input('Digite sua primeira nota'))
y = float(input('Digite sua segunda nota'))
a = (x + y) / 2
#if 0 < a < 5.0 and x <= 10 and y <= 10:
#    print(f'Sua média foi de {a:.2f}, infelizmente você foi reprovado')
#elif 5.0 <= a <= 6.9 and x <= 10 and y <= 10:
#    print(f'Sua média foi de {a:.2f}, você está de recuperação.')
#elif 7.0 <= a <= 9.9 and x <= 10 and y <= 10:
#    print(f'Sua média foi de {a:.2f}, você foi aprovado !')
#elif a == 10 and x == 10 and y == 10:
#    print('Sua média foi de 10, parabéns!!!')
#else:
#    print('Erro. Por favor digite números positivos ou notas verdadeiras')
if x <= 10 and y <= 10:
    if 0 < a < 5.0:
        print(f'Sua média foi de {a:.2f} infelizmente você foi reprovado')
    elif 5.0 <= a <= 6.9:
        print(f'Sua média foi de {a:.2f}, você está de recuperação.')
    elif 7.0 <= a <= 9.9:
        print(f'Sua média foi de {a:.2f}, você foi aprovado !')
    elif a == 10:
        print('Sua média foi de 10, parabéns!!!')
else:
     print('Erro. Por favor digite números positivos ou notas verdadeiras')