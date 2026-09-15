x = int(input('Digite um númeiro inteiro qualuqer'))
y = int(input('Você quer seu número em binário ( escreva 1 se sim), octal ( escreva 2 se sim) ou hexadecimal ( escreva 3 se sim)?'))
if y == 1:
    print(f'Seu número em binario é {bin(x)[2:]} !')
elif y == 2:
    print(f'Seu número em octal é {oct(x)[2:]} !')
elif y == 3:
    print(f'Seu número em hexadecimal é de {hex(x)[2:].upper()} !')
else:
    print('Erro. Por favor digite um numero inteiro e responda a segunda pergunta com 1, 2 ou 3')
