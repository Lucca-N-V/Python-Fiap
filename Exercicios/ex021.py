x = input('Diga o nome de uma cidade').strip() .upper()
d = x.split()
y = 'SANTO'
if d[0] == y:
    print('Sua cidade começa com a palavra "Santo"')
else:
    print('Sua cidade não começa com a palavra "Santo"')
