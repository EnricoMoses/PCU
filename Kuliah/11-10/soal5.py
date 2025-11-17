def input_tup(numbers):
    tup = tuple(map(int, numbers))
    return tup


input_nama = input('Masukkan angka dipisahkan dengan koma: ')
input_nama = input_nama.split(',')
# print(input_nama)
print(input_tup(input_nama))


