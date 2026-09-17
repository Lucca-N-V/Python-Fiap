ma = 0
me = 0
idoso = 0
for i in range (7):
    x = int(input('Digite o ano que você nasceu'))
    if 2026 - x >=18 and x > 1926:
        ma += 1
    elif 2026 - x <18 and x > 1926:
        me += 1
    else:
        idoso += 1
if idoso == 0:
    print(f'Dentre as 7 pessoas, {ma} já antingiram a maioridade e {me} são ainda menor de idade!')
elif idoso > 0:
    print(f'Dentre as 7 pessoas, {ma} já antingiram a maioridade e {me} são ainda menor de idade. Ademais temos {idoso} pessoas')

