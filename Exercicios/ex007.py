x = int(input('Digite um número'))
print(f'A tabuada do seu número é {x*0}, {x*1}, {x*2}, {x*3}, {x*4}, {x*5}, {x*6}, {x*7}, {x*8}, {x*9}, {x*10}"')

print(f'Tabuada do {x}')


for i in range(10, 0, -1):
    print(f'{x} x {i} = {x * i}')