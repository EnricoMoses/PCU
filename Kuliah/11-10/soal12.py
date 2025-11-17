# Data stok awal
stok = {
    "apel": {"harga": 5000, "stok": 10},
    "jeruk": {"harga": 7000, "stok": 5},
    "mangga": {"harga": 8000, "stok": 8}
}

# Data transaksi (nama_barang, jumlah)
transaksi = [
    ("apel", 3),
    ("mangga", 2),
    ("jeruk", 1),
    ("apel", 2)
]

total_belanja = 0  # untuk menampung total harga

# Proses setiap transaksi
for nama_barang, jumlah in transaksi:
    harga = stok[nama_barang]["harga"]           # ambil harga per item
    total_belanja += harga * jumlah              # tambahkan ke total belanja
    stok[nama_barang]["stok"] -= jumlah          # kurangi stoknya

# Tampilkan total belanja
print(f"Total belanja: Rp {total_belanja}")

# Tampilkan sisa stok
print("Sisa stok:")
for nama_barang, info in stok.items():
    print(f"{nama_barang}: {info['stok']}")
