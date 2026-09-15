x = float(input('Digite o valor da casa'))
y = float(input('Digite o seu salário'))
z = float(input('Digite em quantos anos você pretende pagar a casa'))
a = (x / z) / 12
if a > y*0.3 and x > 0 and y > 0 and z > 0:
    print('Você não pode realizar a compra, já que o valor da prestação mensal não pode exceder 30% de seu sálario')
elif a <= y*0.3 and x > 0 and y > 0 and z > 0:
    print(f'O valor de cada prestação mensal será de {a:.2f} !')
else:
    print('Erro. Por favor digite números positivos')
