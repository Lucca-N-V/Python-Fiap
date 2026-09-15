print('Para finalizar o código basta digitar 999')
x = int(input('Digite qualuqer número inteiro'))
q = 0
s = 0
while x != 999:
    if x != 999:
        q += 1
        s += x
        x = int(input('Digite qualuqer número inteiro'))
print(f'Você digitou {q} números, e a soma deles é de {s} !')