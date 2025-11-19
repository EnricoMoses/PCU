from converter import c_to_f, f_to_c

def input_float(prompt):
    while True:
        try:
            nilai = float(input(prompt))
            return nilai
        except ValueError:
            print('Input tidak valid. Harap masukkan lagi')

def format_angka(x):
    if isinstance(x, float) and x.is_integer():
        return str(int(x))
    return str(x)

print('''1. Celsius → Fahrenheit
2. Fahrenheit → Celsius''')

pilihan = input('Pilih konversi(1/2): ')
suhu = input_float('Masukkan suhu: ')

if pilihan == '1':
    c = suhu
    f = c_to_f(c)
    print(f'{format_angka(c)} C = {format_angka(f)} F')
elif pilihan == '2':
    f = suhu
    c = c_to_f(f)
    print(f'{format_angka(f)} F = {format_angka(c)} C')
else:
    print('Pilihan tidak valid')