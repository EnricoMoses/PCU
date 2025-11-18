n = int(input().strip())

# dictionary untuk menyimpan berapa kali setiap value string muncul
freq = {}

for _ in range(n):
    key = input().strip()      # dibaca tapi tidak dipakai
    value = input().strip()

    # kalau value hanya berisi digit (angka) → abaikan
    if value.isdigit():
        continue

    # kalau mau case-insensitive bisa aktifkan baris ini:
    # value = value.lower()

    # hitung kemunculan value
    if value in freq:
        freq[value] += 1
    else:
        freq[value] = 1

print(freq)
