import math
d = 0
u = 0
c = 0
s = 0
p = int(input('Digite o valor que quer retirar'))
while p <= 0:
    p = int(input('Erro. insira um valor válido'))
if p < 10:
    print(f'Total de {p} cedulas de R$1.00')
if p == 10:
    print('Total de 1 cedula de R$10.00')
if 10 < p < 49:
    d = math.floor(p / 10)
    u = p - d * 10
    print(f' Total de {u} cedulas de R$1.00 \n Total de {d} cedulas de R$10.00')
if p == 50:
    print('Total de 1 cedula de R$50.00')
if 50 < p < 100:
    c = math.floor(p / 50)
    d = math.floor((p - c * 50) / 10)
    u = p - c * 50 - d * 10
    print(f' Total de {u} cedulas de R$1.00 \n Total de {d} cedulas de R$10.00 \n Total de {c} cedulas de R$50.00')
if p == 100:
    print('Total de 1 cedula de R$100.00')
if p > 100:
    s = math.floor(p / 100)
    c = math.floor((p - s * 100)/50)
    d = math.floor((p - s * 100 - c * 50)/10 )
    u = p - s * 100 - c * 50 - d * 10
    print(f' Total de {u} cedulas de R$1.00 \n Total de {d} cedulas de R$10.00 \n Total de {c} cedulas de R$50.00 \n Total de {s} cedulas de R$100.00')
# Resolução eficiente que não necessita de formulas que eu utilizei:
valor = int(input('Que valor você quer sacar? R$ '))
total = valor
cedula = 100  # Começamos pela maior nota
total_cedulas = 0

while True:
    if total >= cedula:
        total -= cedula
        total_cedulas += 1
    else:
        # Só imprime se a quantidade de cédulas for maior que zero
        if total_cedulas > 0:
            print(f'Total de {total_cedulas} cédulas de R$ {cedula:.2f}')

        # Lógica para "baixar" o valor da nota
        if cedula == 100:
            cedula = 50
        elif cedula == 50:
            cedula = 20  # Adicionei a de 20 pra ficar completo!
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1

        total_cedulas = 0

        if total == 0:
            break