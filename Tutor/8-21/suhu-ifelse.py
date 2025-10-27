celcius = float(input('Masukkan suhu dalam celcius : '))
format = input('Masukkan format(reamur, fahrenheit, kelvin) : ')
# print(f'{celcius} Celcius')
# print(format == 'reamur')

if format == 'reamur':
    print(f'{ 4/5 * celcius} Reamur')
elif format == 'fahrenheit':
    print(f'{ 9/5 * celcius + 32} Fahrenheit')
elif format == 'kelvin':
    print(f'{celcius + 273} Kelvin')
else:
    print('Anda salah memasukkan format')

