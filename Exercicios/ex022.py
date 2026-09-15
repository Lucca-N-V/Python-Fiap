nome = input('Digite seu nome completo').strip()
s = 'silva'
if s in nome.lower():
    print('Seu nome contém a palavra Silva!')
else:
    print('Seu nome não contém a palavra Silva!')