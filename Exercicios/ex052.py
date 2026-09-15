ma = 0
me = 0
for i in range(5):
    x = float(input('Digite seu peso'))
    if i == 0:
        ma = x
        me = x
    else:
        if x > ma:
            ma = x
        if x < me:
            me = x
print(f'O maior peso é de {ma} Kg, e o menor peso é de {me} Kg.')