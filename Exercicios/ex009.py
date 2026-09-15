x = float(input('Qual a largura da sua parede em metros?'))
y = float(input('Qual a altura da sua parede em metros?'))
a = x * y

if a % 1 == 0:
    baldes = int(a/2)
else:
    baldes=(a//2+1)
print(f'A área da sua parede é de {a} m², e serão necessarios {baldes} baldes de tinta !')
