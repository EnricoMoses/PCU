from tabulate import tabulate

data_barang = [
    ['Pensil', 3000],
    ['Buku', 5000]
]

header = ['Barang', 'Harga']
print(tabulate(data_barang, headers=header, tablefmt='grid'))