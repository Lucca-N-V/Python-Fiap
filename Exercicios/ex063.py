print('O codigo vai ler 10 números')
x = int(input('Digite qualuqer número inteiro'))
q = 0
s = 0
ma = 0
me = 0
c = 'S'
while c == 'S':
    while q != 9:
        if q == 0:
            ma = x
            me = x
            q += 1
            s += x
            x = int(input('Digite qualuqer número inteiro'))
        elif x > ma and q != 0:
            ma = x
            q += 1
            s += x
            x = int(input('Digite qualuqer número inteiro'))
        elif x < me and q != 0:
            me = x
            q += 1
            s += x
            x = int(input('Digite qualuqer número inteiro'))
        else:
            q += 1
            s += x
            x = int(input('Digite qualuqer número inteiro'))
    c = input('Deseja continuar? [S, N]').strip() . upper()
    while c not in ['S', 'N']:
        c = input('Erro. Por favor responda corretamente').strip() .upper()
    if c == 'N':
        print(f'A média dos números digitados foram {s/q}, o maior número foi {ma} e o menor {me} !')
    else:
        q = 0
