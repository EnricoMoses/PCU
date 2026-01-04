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

daftar = ['Sistem informasi akademik dan sistem informasi keuangan kampus.', 'Sistem informasi akademik berbasis web.', 'Aplikasi data mahasiswa berbasis python.']

for i, j in combinations(daftar, 2):
    print(i, j)