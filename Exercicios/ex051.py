ma = 0
me = 0
fossil = 0
for i in range (7):
    x = int(input('Digite o ano que você nasceu'))
    if 2026 - x >=18 and x > 1926:
        ma += 1
    elif 2026 - x <18 and x > 1926:
        me += 1
    else:
        fossil += 1
if fossil == 0:
    print(f'Dentre as 7 pessoas, {ma} já antingiram a maioridade e {me} são ainda menor de idade!')
elif fossil > 0:
    print(f'Dentre as 7 pessoas, {ma} já antingiram a maioridade e {me} são ainda menor de idade. Ademais temos {fossil} pessoas que não deveriam estar vivas!')

