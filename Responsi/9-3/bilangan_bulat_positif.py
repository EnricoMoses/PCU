bilangan = int(input('Bilangan: '))

if bilangan % 2 == 0:
    if bilangan % 4 == 0 :
        print('Genap dan Kelipatan 4')
    else :
        print('Genap')
else :
    print('Ganjil')
