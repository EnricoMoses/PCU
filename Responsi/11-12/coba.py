produk = {
    "Laptop": {"harga": 10_000_000, "stok": 10},
    "Mouse": {"harga": 150_000, "stok": 25},
    "Keyboard": {"harga": 300_000, "stok": 5},
}

for nama, info in produk.items():
    print(nama, info)
    print(info["harga"])
    print(info["stok"])

