n = int(input().strip())

freq = {}

# fungsi bantu: cek apakah string bisa dikonversi ke angka (int / float)
def is_number(s: str) -> bool:
    try:
        float(s)          # kalau bisa di-float berarti numeric (termasuk 2.5, -3, 9.9)
        return True
    except ValueError:
        return False

for _ in range(n):
    key = input().strip()          # key tetap dibaca, tapi tidak dipakai
    value = input().rstrip("\n")   # baca value apa adanya

    # skip semua yang angka (int maupun float)
    if is_number(value):
        continue

    # hitung hanya value yang bukan angka
    if value in freq:
        freq[value] += 1
    else:
        freq[value] = 1

print(freq)
