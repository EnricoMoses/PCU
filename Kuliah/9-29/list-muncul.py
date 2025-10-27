mylist = ['apel', 'pisang', 'apel', 'mangga', 'pisang', 'apel']

buah = []
jumlah = []

for i in mylist:
    if i in buah:
        idx = buah.index(i)
        jumlah[idx] += 1
    else:
        buah.append(i)
        jumlah.append(1)

for i in range(len(buah)):
    print(f'{mylist[i]}: {jumlah[i]}')

