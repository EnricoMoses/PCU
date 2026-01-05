# from itertools import combinations
#
# for i in combinations([['a', 'b'], ['c', 'd'], ['e', 'f']], 2):
#     print(i)
from itertools import combinations

# n = input().strip()
# print(n)

# n = []
# n.append('halo')
# print(n)

# str = 'Sistem informasi akademik dan sistem informasi keuangan kampus.'
# str = 'Sistem informasi akademik berbasis web.'
# s = str.lower().replace('.', '').replace(',', '').split()
#
# print(s)
#
# unik = []
# for i in s:
#     print(i)
#     if i not in unik:
#         unik.append(i)
#
# print(unik)
# print(len(unik))

# print(0/0)
#
# w1 = ['sistem', 'informasi', 'akademik', 'dan', 'keuangan', 'kampus']
# w2 = ['sistem', 'informasi', 'akademik', 'berbasis', 'web']
#
# sama = 0
# for kata in w1:
#     if kata in w2:
#         sama += 1
#
# # print(sama)
# print(max(len(w1), len(w2)))

# daftar = ['Sistem informasi akademik dan sistem informasi keuangan kampus.', 'Sistem informasi akademik berbasis web.', 'Aplikasi data mahasiswa berbasis python.']
#
# for i, j in combinations(daftar, 2):
#     print(i, j)

# i = 0
#
# while True:
#     print(i)
#     i += 1
#     if i == 10:
#         break

# nama = '1,2'
#
# parts = nama.split(',')
# print(parts)

# TipeBarang = ('Makanan', 'Minuman', 'Alat_Tulis', 'Alat_Makan')
#
# for i, t in enumerate(TipeBarang):
#     print(i, t)

# print(TipeBarang[5])
#
# Iventory = {
#     'mie instan' : {
#         'jumlah_stok': 40,
#         'harga_rata': 1200.5,
#         'tipe_barang': 'Makanan'
#     },
#     'kopi tubruk': {
#         'jumlah_stok': 40,
#         'harga_rata': 1200.5,
#         'tipe_barang': 'Makanan'
#     },
# }
#
# print(Iventory['mie instan']['jumlah_stok'])
#
# for nama, data in Iventory.items():
#     print(nama, data['jumlah_stok'])
#
# print(Iventory['kopi tubruk'])

listt = [[85, 'Blora'], [90, 'Purwodadi'], [100, 'Malang']]
print(listt[0][1])
print(listt[1][1])

data_mahasiswa = {
    'jojo': {
        'nilai': 85,
        'asal': 'Blora'
    },
    'michael': {
        'nilai': 90,
        'asal': 'Purwodadi'
    },
    'kevin':{
        'nilai': 100,
        'asal': 'Malang'
    },
}

print(data_mahasiswa['kevin']['asal'])

data_mahasiswa['Alex'] = {
    'nilai': 70,
    'asal': 'Semarang'
}

# # print(data_mahasiswa)
#
# for nama, data in data_mahasiswa.items():
#     if data['nilai'] > 85:
#         print(nama, data)
#
# if 'Enrico' in data_mahasiswa:
#     print(data_mahasiswa['Enrico'])

# data = data_mahasiswa['Alex']
# data['nilai'] = 100
# data['asal'] = 'Jakarta'

data_mahasiswa['Alex']['nilai'] = 100
data_mahasiswa['Alex']['asal'] = 'Jakarta'
print(data_mahasiswa)