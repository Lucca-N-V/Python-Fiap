x = input('Digite uma frase qualuqer').strip().lower()
a = x.count("a")
a1 = x.find("a")
a2 = x.rfind('a')
if a > 1:
    print(f'Sua frase contém {a} letras "a", sendo que a primeira aparece na casa {a1}, e aparece pela última vez na casa {a2} !')
elif a == 1:
    print(f'Sua frase contém {a} letra a, sendo que ela aparece na casa {a1} !')
else:
    print('Sua frase não tem nenhuma letra "a"')