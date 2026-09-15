x = int(input('Digite sua idade'))
if 0 < x <= 9:
    print('O atleta está na categoria Mirim!')
elif 9 < x <= 14:
    print('O atleta está na categoria Infaltil!')
elif 14 < x <= 19:
    print('O atleta está na categoria Junior!')
elif 19 < x <= 20:
    print('O atleta está na categoria Sênior!')
elif x >20:
    print('O atleta está na categoria Master!')
else:
    print('Erro. Por favor insira uma idade válida')