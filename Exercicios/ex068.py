t = 0
q = 0
m = 0
b = 0
nb = 'Nada'
while True:
    p = float(input('Digite o preço do produto'))
    print('-' * 30)
    while p <= 0:
        p = float(input('Erro. Digite um valor válido'))
        print('-' * 30)
    n = input('Digite o nome do produto')
    print('-' * 30)
    t += p
    if p > 1000:
        m += 1
    if q == 0:
        b = p
        nb = n
    if p < b:
        b = p
        nb = n
    q += 1
    c = input('Deseja parar? [S/N]').strip().upper()
    print('-' * 30)
    while c not in ['S', 'N']:
        c = input('Erro. Escreva S ou N')
        print('-' * 30)
    if c == 'S':
        break
print('----------RESULTADOS---------')
print(f' O total gasto será de {t:.2f} \n {m} produtos custam mais de R$1000.00 \n O produto mais barato é {nb}')



