produk = {
    "Laptop": {"harga": 10_000_000, "stok": 5},
    "Mouse": {"harga": 150_000, "stok": 25},
    "Keyboard": {"harga": 300_000, "stok": 10},
}

def inventory_values(produk_dict):
    per_produk = {}
    total = 0
    for nama, info in produk_dict.items():
        nilai_item = info["harga"] * info["stok"]
        per_produk[nama] = nilai_item
        total += nilai_item
    return per_produk, total

def format_rupiah(n):
    return f"Rp {n:,.0f}"

inv_dict, inv_total = inventory_values(produk)
for nama in ["Laptop", "Mouse", "Keyboard"]:
    print(f"{nama}: {format_rupiah(inv_dict[nama])}")
print(f"Total inventori: {format_rupiah(inv_total)}")