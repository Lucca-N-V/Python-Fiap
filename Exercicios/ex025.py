x = float(input('Digite o valor de sua compra'))
y = input('Você é VIP? Responda com s ou n').strip().lower()

if y == "s" and x > 0:
    print(f'O valor da sua compra é de R${x*0.85}')
elif y == "n" and x > 500:
    print(f'O valor da sua compra é de R${x*0.95}')
elif y == "n" and x <= 500:
    print(f'O valor da sua compra é de {x} ')
else:
    print(f'Dados invalidos, digite s ou n e valores positivos')
