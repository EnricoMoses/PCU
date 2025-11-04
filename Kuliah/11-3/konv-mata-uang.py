try:
    rupiah = float(input('Masukkan rupiah: '))
    konversi = int(input('1 = USD, 2 = EUR, 3 = JPY : '))

    if konversi == 1:
        print(f'{rupiah/15500} USD')
    elif konversi == 2:
        print(f'{rupiah/17000} EUR')
    elif konversi == 3:
        print(f'{rupiah/110} JPY')
    else:
        raise ValueError('konversi')

except ValueError:
    print('Input harus berupa angka, dan konversi hanya 1-3')