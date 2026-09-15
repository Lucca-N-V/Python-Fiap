d = 0
m = 0
f = 0
while True:
    i = int(input('Digite sua idade'))
    print('-' * 30)
    while i <= 0:
        i = int(input('Erro. Insira uma idade valída'))
        print('-' * 30)
    s = input('Digite seu sexo [M/F]').strip().upper()
    print('-' * 30)
    while s not in ['M', 'F']:
        s = input('Erro. Insira M ou F').strip().upper()
        print('-' * 30)
    if i > 18:
        d += 1
    if s == 'F' and i < 20:
        f += 1
    if s == 'M':
        m += 1
    p = input('Deseja parar? [S/N]').strip().upper()
    print('-' * 30)
    while p not in ['S', 'N']:
        p = input('Erro. Insira S ou N').strip().upper()
        print('-' * 30)
    if p == 'S':
        break
print('--------------FIM DA PESQUISA--------------')
print(f' {d} pessoas são maior de idade \n {m} pessoas são homens \n {f} pessoas são mulheres abaixo de 20 anos')
