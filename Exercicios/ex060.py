p1 = float(input('Digite o primeiro termo da sua PA'))
r = float(input('Digite a razão da sua PA'))
z = 1
while z != 11:
    paw = p1 + (z - 1)*r
    z += 1
    print(f'{paw:.2f}')
q = input('Você deseja continuar?[S, N]').strip() .upper()
while q not in ['S', 'N']:
    q = input('Erro. Escreva "S" ou "N"').strip() .upper()
if q == 'N':
    print('Fim do programa')
else:
    while q == 'S':
        n = int(input('Digite quantos termos a mais você quer'))
        w = 1
        y = w + (z - 1)
        while w != n+1:
            paw = p1 + (y - 1)*r
            w += 1
            y += 1
            z += 1
            print(f'{paw:.2f}')
        q = input('Você deseja continuar?[S, N]').strip().upper()
        while q not in ['S', 'N']:
            q = input('Erro. Escreva "S" ou "N"').strip().upper()
    print('Fim do programa')

