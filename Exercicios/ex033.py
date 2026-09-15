x1 = float(input('Digite a cordenada x de um dos vertices'))
y1 = float(input('Digite a cordenada y do vertice anterior'))
x2 = float(input('Digite a cordenada x de um dos vertices restantes'))
y2 = float(input('Digite a cordenada y do vertice anterior'))
x3 = float(input('Digite a cordenada x do ultímo vertice'))
y3 = float(input('Digite a cordenada y do vertice anterior'))
d = (x1 * y2) + (x2 * y3) + (x3 * y1)
e = (y1 * x2) + (y2 * x3) + (y3 * x1)
r = d - e
print(r)
if r == 0:
    print('As linhas não formam um triângulo !')
else:
    print(f'As linhas formam um triângulo, cuja a área mede {abs(r/2):.2f} !')
