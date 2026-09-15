x = float(input('Digite o valor do produto: '))
y = input('Pagamento (à vista, 2x, 3x, etc): ').strip().lower()
z = input('Forma (dinheiro, cheque, cartão): ').strip().lower()

if x <= 0:
    print('Erro. Insira um valor válido.')
else:

    if y in ['a vista', 'à vista', '1x']:
        if z in ['dinheiro', 'cheque']:
            print(f'Desconto de 10%! Valor: R$ {x * 0.9:.2f}')
        elif z in ['cartão', 'cartao']:
            print(f'Desconto de 5%! Valor: R$ {x * 0.95:.2f}')
        else:
            print('À vista aceitamos apenas dinheiro, cheque ou cartão.')


    elif z in ['cartão', 'cartao']:
        if y == '2x':
            print(f'Preço normal em 2x: R$ {x:.2f}')
        else:
            # Aqui caem 3x, 4x, etc. (Qualquer coisa diferente de 2x e à vista)
            print(f'Parcelado em {y} com 20% de juros: R$ {x * 1.2:.2f}')

    else:
        print('Erro. Parcelamento disponível apenas no cartão.')