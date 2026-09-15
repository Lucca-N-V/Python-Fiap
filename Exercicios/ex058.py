x = int(input('Digite um número inteiro'))
i = x
if x != 1:
    while i - 1 != 0:
        if i - 1 == x - 1:
            a = i
            i -= 1
            b = a
        else:
            a = i
            i -= 1
            b *= a
else:
    b = 1
print(f'O fatorial de seu número equivale a {b} !')
