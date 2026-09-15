x = input('Digite uma frase').strip() . upper()
y = x.split()
z = ''.join(y)
i = ''
for l in range(len(z)-1, -1 , -1):
    i += z[l]
if i == z:
    print('Palindromo')
else:
    print('Não é palindromo')