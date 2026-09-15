s = 0
x = int(input('Digite qualuqer número inteiro'))
for i in range (1, x+1):
    if x % i == 0:
        s += 1
if s == 2:
    print('Seu número é primo!')
else:
    print('Seu número não é primo')